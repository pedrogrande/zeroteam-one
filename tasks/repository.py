"""
Task Contract Repository
========================

Data access layer for the polymorphic contract store.

All methods are ``contract_kind``-aware. The repository:

- Validates all cross-references before write (actor IDs exist in
  ``actors``, dependency contract IDs exist in ``contracts``) — this
  compensates for JSONB's inability to enforce FKs inside the document.
- Creates a new version row on every edit (immutable versioning).
- Appends an ``AuditEvent`` with before/after snapshots on every change.
- Computes a SHA-256 hash chain on audit events for tamper-evidence.
- Deserializes the JSONB ``document`` to the right ``ContractBase``
  subclass via ``CONTRACT_KIND_REGISTRY``.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Optional
from uuid import uuid4

from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session

from tasks.domain import (
    CONTRACT_KIND_REGISTRY,
    Actor,
    ActorRole,
    AuditEvent,
    ContractBase,
    ContractLineage,
    TaskContract,
    deserialize_contract,
)
from tasks.enums import ContractKind, ContractStatus, EventType, RoleType
from tasks.models import (
    ActorModel,
    AuditEventModel,
    ContractModel,
    ContractVersionModel,
)
from tasks.state_machine import assert_transition

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    """Current UTC timestamp as ISO 8601 string."""
    return datetime.now(timezone.utc).isoformat()


def _sha256(data: str) -> str:
    """SHA-256 hex digest of a string."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def _document_json(contract: ContractBase) -> str:
    """Canonical JSON for hashing — sorted keys, no extra whitespace."""
    return contract.model_dump_json(exclude_none=False, exclude={"audit_trail"})


def _bump_version(version: str, bump: str = "patch") -> str:
    """Bump a semver string. ``bump`` is one of ``patch``, ``minor``, ``major``."""
    major, minor, patch = (int(x) for x in version.split("."))
    if bump == "major":
        return f"{major + 1}.0.0"
    if bump == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def _contract_to_document(contract: ContractBase) -> dict[str, Any]:
    """Serialize a contract to a JSONB-compatible dict (excludes audit_trail)."""
    return json.loads(contract.model_dump_json(exclude={"audit_trail"}))


def _parse_dt(value: Optional[str]) -> Optional[datetime]:
    """Parse an ISO 8601 string to a datetime, or return None."""
    if value is None:
        return None
    return datetime.fromisoformat(value)


def _extract_scalar_fields(contract: ContractBase) -> dict[str, Any]:
    """Extract scalar columns from a contract domain model for the ORM row."""
    return {
        "status": contract.status,
        "contract_type": contract.contract_type,
        "created_at": _parse_dt(contract.created_at),
        "due_date": (_parse_dt(contract.schedule.due_date) if contract.schedule else None),
        "requester_actor_id": _find_requester_id(contract),
        "performer_actor_id": _find_performer_id(contract),
        "parent_contract_id": contract.lineage.parent_contract_id,
    }


def _find_requester_id(contract: ContractBase) -> Optional[str]:
    """Find the requester actor_id from actor_roles."""
    for role in contract.actor_roles:
        if role.role_type == RoleType.requester:
            return role.actor_id
    return None


def _find_performer_id(contract: ContractBase) -> Optional[str]:
    """Find the performer actor_id from actor_roles."""
    for role in contract.actor_roles:
        if role.role_type == RoleType.performer:
            return role.actor_id
    return None


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class ContractNotFoundError(LookupError):
    """Raised when a contract is not found."""


class ActorNotFoundError(LookupError):
    """Raised when an actor is not found."""


class CrossReferenceError(ValueError):
    """Raised when a cross-reference inside the JSONB document is invalid."""


# ---------------------------------------------------------------------------
# ActorRepository
# ---------------------------------------------------------------------------


class ActorRepository:
    """CRUD for the normalised ``actors`` table."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def create_actor(self, actor: Actor) -> ActorModel:
        model = ActorModel(
            actor_id=actor.actor_id,
            actor_type=actor.actor_type,
            display_name=actor.display_name,
            trust_score=actor.trust_score,
            reputation_score=actor.reputation_score,
            public_key=actor.public_key,
        )
        self.session.add(model)
        self.session.flush()
        return model

    def get_actor(self, actor_id: str) -> Optional[ActorModel]:
        return self.session.get(ActorModel, actor_id)

    def list_actors(self, limit: int = 100, offset: int = 0) -> list[ActorModel]:
        stmt = select(ActorModel).limit(limit).offset(offset)
        return list(self.session.scalars(stmt))

    def update_trust_score(self, actor_id: str, trust_score: float) -> Optional[ActorModel]:
        model = self.get_actor(actor_id)
        if model is None:
            return None
        model.trust_score = trust_score
        self.session.flush()
        return model

    def assert_exists(self, actor_id: str) -> None:
        """Raise ``ActorNotFoundError`` if the actor doesn't exist."""
        if self.get_actor(actor_id) is None:
            raise ActorNotFoundError(f"Actor not found: {actor_id}")


# ---------------------------------------------------------------------------
# AuditRepository
# ---------------------------------------------------------------------------


class AuditRepository:
    """Append-only audit log with SHA-256 hash chain."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def append_event(
        self,
        contract_id: str,
        contract_kind: ContractKind,
        event_type: EventType,
        actor_id: str,
        reason: Optional[str] = None,
        before_snapshot: Optional[dict[str, Any]] = None,
        after_snapshot: Optional[dict[str, Any]] = None,
    ) -> AuditEventModel:
        """Append an audit event and compute the hash chain.

        The hash is ``SHA256(previous_hash + event_json)`` where
        ``event_json`` is the canonical JSON of the event (excluding the
        hash fields). The first event has ``previous_hash = None``.
        """
        # Get the previous event's hash for the chain
        prev_stmt = (
            select(AuditEventModel)
            .where(AuditEventModel.contract_id == contract_id)
            .order_by(desc(AuditEventModel.timestamp))
            .limit(1)
        )
        prev_event = self.session.scalars(prev_stmt).first()
        previous_hash = prev_event.immutable_hash if prev_event else None

        event_id = str(uuid4())
        timestamp = _now_iso()

        # Compute hash over the event payload (excluding hash fields)
        payload = {
            "event_id": event_id,
            "contract_id": contract_id,
            "contract_kind": contract_kind.value,
            "event_type": event_type.value,
            "actor_id": actor_id,
            "timestamp": timestamp,
            "reason": reason,
            "before_snapshot": before_snapshot,
            "after_snapshot": after_snapshot,
            "previous_hash": previous_hash,
        }
        payload_json = json.dumps(payload, sort_keys=True, default=str)
        immutable_hash = _sha256((previous_hash or "") + payload_json)

        model = AuditEventModel(
            event_id=event_id,
            contract_id=contract_id,
            contract_kind=contract_kind.value,
            event_type=event_type.value,
            actor_id=actor_id,
            timestamp=_parse_dt(timestamp),
            reason=reason,
            before_snapshot=before_snapshot,
            after_snapshot=after_snapshot,
            immutable_hash=immutable_hash,
            previous_hash=previous_hash,
        )
        self.session.add(model)
        self.session.flush()
        return model

    def get_audit_trail(self, contract_id: str) -> list[AuditEventModel]:
        """Return all audit events for a contract, oldest first."""
        stmt = (
            select(AuditEventModel)
            .where(AuditEventModel.contract_id == contract_id)
            .order_by(AuditEventModel.timestamp)
        )
        return list(self.session.scalars(stmt))


# ---------------------------------------------------------------------------
# ContractRepository
# ---------------------------------------------------------------------------


class ContractRepository:
    """CRUD + versioning + state transitions for contracts."""

    def __init__(self, session: Session) -> None:
        self.session = session
        self.actors = ActorRepository(session)
        self.audit = AuditRepository(session)

    # -----------------------------------------------------------------------
    # Cross-reference validation
    # -----------------------------------------------------------------------

    def _validate_cross_references(self, contract: ContractBase) -> None:
        """Validate that all actor_id and contract_id references in the
        document exist in the DB. Compensates for JSONB's lack of FK enforcement.
        """
        # Validate actor_roles
        for role in contract.actor_roles:
            self.actors.assert_exists(role.actor_id)

        # Validate acceptance criteria verifiers
        spec = getattr(contract, "specification", None)
        if spec is not None:
            for criterion in spec.acceptance_criteria:
                self.actors.assert_exists(criterion.verifier_actor_id)

        # Validate dependency contract references
        for dep in getattr(contract, "dependencies", []):
            if dep.depends_on_contract_id is not None:
                if not self._contract_exists(dep.depends_on_contract_id):
                    raise CrossReferenceError(
                        f"Dependency references non-existent contract: {dep.depends_on_contract_id}"
                    )
            if dep.blocks_contract_id is not None:
                if not self._contract_exists(dep.blocks_contract_id):
                    raise CrossReferenceError(f"Dependency blocks non-existent contract: {dep.blocks_contract_id}")

        # Validate lineage references
        if contract.lineage.parent_contract_id is not None:
            if not self._contract_exists(contract.lineage.parent_contract_id):
                raise CrossReferenceError(f"Parent contract not found: {contract.lineage.parent_contract_id}")

    def _contract_exists(self, contract_id: str) -> bool:
        """Check if any version of a contract exists (by logical identity)."""
        stmt = select(ContractModel.row_id).where(ContractModel.contract_id == contract_id).limit(1)
        return self.session.scalars(stmt).first() is not None

    # -----------------------------------------------------------------------
    # Create
    # -----------------------------------------------------------------------

    def create_contract(
        self,
        contract: ContractBase,
        actor_id: str,
    ) -> ContractBase:
        """Create a new contract (version 1.0.0, status=draft).

        Validates cross-references, inserts the contract row, appends an
        audit event, and returns the created contract.
        """
        # Ensure the creating actor exists
        self.actors.assert_exists(actor_id)

        # Validate all cross-references in the document
        self._validate_cross_references(contract)

        # Ensure contract_id is set
        if not contract.contract_id:
            contract.contract_id = str(uuid4())
        if not contract.created_at:
            contract.created_at = _now_iso()

        # Insert the contract row
        scalars = _extract_scalar_fields(contract)
        doc = _contract_to_document(contract)
        doc_json = json.dumps(doc, sort_keys=True, default=str)
        document_hash = _sha256(doc_json)

        model = ContractModel(
            contract_id=contract.contract_id,
            version=contract.version,
            contract_kind=(contract._contract_kind_value() if hasattr(contract, "_contract_kind_value") else "task"),
            status=scalars["status"],
            contract_type=scalars["contract_type"],
            created_at=scalars["created_at"],
            due_date=scalars["due_date"],
            requester_actor_id=scalars["requester_actor_id"],
            performer_actor_id=scalars["performer_actor_id"],
            parent_contract_id=scalars["parent_contract_id"],
            document=doc,
            document_hash=document_hash,
        )
        self.session.add(model)
        self.session.flush()

        # Insert version index
        version_model = ContractVersionModel(
            contract_id=contract.contract_id,
            version=contract.version,
            contract_kind=model.contract_kind,
            row_id=model.row_id,
        )
        self.session.add(version_model)

        # Append audit event
        self.audit.append_event(
            contract_id=contract.contract_id,
            contract_kind=ContractKind(model.contract_kind),
            event_type=EventType.edit,
            actor_id=actor_id,
            reason="Contract created",
            after_snapshot=doc,
        )

        self.session.flush()
        return contract

    # -----------------------------------------------------------------------
    # Read
    # -----------------------------------------------------------------------

    def get_contract(
        self,
        contract_id: str,
        version: Optional[str] = None,
    ) -> ContractBase:
        """Get a contract by ID. Returns the latest version if ``version`` is None."""
        if version is not None:
            stmt = select(ContractModel).where(
                ContractModel.contract_id == contract_id,
                ContractModel.version == version,
            )
        else:
            # Latest version = highest row_id for this contract_id
            stmt = (
                select(ContractModel)
                .where(ContractModel.contract_id == contract_id)
                .order_by(desc(ContractModel.row_id))
                .limit(1)
            )
        model = self.session.scalars(stmt).first()
        if model is None:
            raise ContractNotFoundError(
                f"Contract not found: {contract_id}" + (f" version={version}" if version else "")
            )
        return self._model_to_contract(model)

    def get_contract_versions(self, contract_id: str) -> list[dict[str, Any]]:
        """Return a summary list of all versions for a contract."""
        stmt = (
            select(ContractVersionModel)
            .where(ContractVersionModel.contract_id == contract_id)
            .order_by(ContractVersionModel.created_at)
        )
        versions = self.session.scalars(stmt).all()
        return [
            {
                "contract_id": str(v.contract_id),
                "version": v.version,
                "contract_kind": v.contract_kind,
                "created_at": v.created_at.isoformat() if v.created_at else None,
            }
            for v in versions
        ]

    def list_contracts(
        self,
        contract_kind: Optional[ContractKind] = None,
        status: Optional[ContractStatus] = None,
        actor_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ContractBase]:
        """List contracts with optional filters. Uses scalar columns for speed."""
        # Subquery: latest row_id per contract_id
        latest_subq = (
            select(
                ContractModel.contract_id,
                func.max(ContractModel.row_id).label("max_row_id"),
            )
            .group_by(ContractModel.contract_id)
            .subquery()
        )

        stmt = select(ContractModel).join(
            latest_subq,
            (ContractModel.row_id == latest_subq.c.max_row_id),
        )

        if contract_kind is not None:
            stmt = stmt.where(ContractModel.contract_kind == contract_kind.value)
        if status is not None:
            stmt = stmt.where(ContractModel.status == status.value)
        if actor_id is not None:
            stmt = stmt.where(
                (ContractModel.requester_actor_id == actor_id) | (ContractModel.performer_actor_id == actor_id)
            )
        if parent_id is not None:
            stmt = stmt.where(ContractModel.parent_contract_id == parent_id)

        stmt = stmt.order_by(desc(ContractModel.created_at)).limit(limit).offset(offset)
        models = self.session.scalars(stmt).all()
        return [self._model_to_contract(m) for m in models]

    # -----------------------------------------------------------------------
    # Update (creates new version)
    # -----------------------------------------------------------------------

    def update_contract(
        self,
        contract_id: str,
        actor_id: str,
        changes: dict[str, Any],
        version_bump: str = "patch",
    ) -> ContractBase:
        """Update a contract by creating a new version.

        ``changes`` is a dict of field → value applied to the current
        contract. The current version is preserved; a new row is inserted
        with the bumped version.
        """
        self.actors.assert_exists(actor_id)
        current = self.get_contract(contract_id)
        before_snapshot = _contract_to_document(current)

        # Apply changes
        updated_dict = current.model_dump(exclude={"audit_trail"})
        updated_dict.update(changes)
        new_version = _bump_version(current.version, version_bump)

        # Reconstruct the contract with the new version
        contract_cls = type(current)
        updated_dict["version"] = new_version
        updated_contract = contract_cls.model_validate(updated_dict)

        # Validate cross-references in the updated document
        self._validate_cross_references(updated_contract)

        after_snapshot = _contract_to_document(updated_contract)
        doc_json = json.dumps(after_snapshot, sort_keys=True, default=str)
        document_hash = _sha256(doc_json)
        scalars = _extract_scalar_fields(updated_contract)

        # Insert new version row
        model = ContractModel(
            contract_id=contract_id,
            version=new_version,
            contract_kind=self._get_contract_kind_value(current),
            status=scalars["status"],
            contract_type=scalars["contract_type"],
            created_at=scalars["created_at"],
            due_date=scalars["due_date"],
            requester_actor_id=scalars["requester_actor_id"],
            performer_actor_id=scalars["performer_actor_id"],
            parent_contract_id=scalars["parent_contract_id"],
            document=after_snapshot,
            document_hash=document_hash,
        )
        self.session.add(model)
        self.session.flush()

        # Insert version index
        version_model = ContractVersionModel(
            contract_id=contract_id,
            version=new_version,
            contract_kind=model.contract_kind,
            row_id=model.row_id,
        )
        self.session.add(version_model)

        # Append audit event
        self.audit.append_event(
            contract_id=contract_id,
            contract_kind=ContractKind(model.contract_kind),
            event_type=EventType.edit,
            actor_id=actor_id,
            reason=f"Updated to version {new_version}",
            before_snapshot=before_snapshot,
            after_snapshot=after_snapshot,
        )

        self.session.flush()
        return updated_contract

    # -----------------------------------------------------------------------
    # State transition
    # -----------------------------------------------------------------------

    def transition_state(
        self,
        contract_id: str,
        actor_id: str,
        to_state: ContractStatus,
        reason: Optional[str] = None,
    ) -> ContractBase:
        """Transition a contract to a new state. Validates via the state machine."""
        self.actors.assert_exists(actor_id)
        current = self.get_contract(contract_id)
        from_state = ContractStatus(current.status)

        # Validate the transition
        assert_transition(from_state, to_state)

        # Create new version with updated status
        changes = {
            "status": to_state.value,
            "execution_state": {"current_state": to_state.value},
        }
        return self.update_contract(
            contract_id=contract_id,
            actor_id=actor_id,
            changes=changes,
            version_bump="patch",
        )

    # -----------------------------------------------------------------------
    # Claim
    # -----------------------------------------------------------------------

    def claim_contract(
        self,
        contract_id: str,
        actor_id: str,
    ) -> ContractBase:
        """Claim a contract as performer. Sets performer actor role and status=claimed."""
        self.actors.assert_exists(actor_id)
        current = self.get_contract(contract_id)

        if ContractStatus(current.status) != ContractStatus.open:
            raise ValueError(f"Contract must be 'open' to claim, is '{current.status}'")

        # Add or update the performer role
        roles = [r for r in current.actor_roles if r.role_type != RoleType.performer]
        roles.append(
            ActorRole(
                role_id=str(uuid4()),
                contract_id=contract_id,
                actor_id=actor_id,
                role_type=RoleType.performer,
                claim_mechanism="self-selected",
                claim_timestamp=_now_iso(),
            )
        )

        changes = {
            "actor_roles": [r.model_dump() for r in roles],
            "status": ContractStatus.claimed.value,
            "execution_state": {"current_state": ContractStatus.claimed.value},
        }
        return self.update_contract(
            contract_id=contract_id,
            actor_id=actor_id,
            changes=changes,
        )

    # -----------------------------------------------------------------------
    # Decompose
    # -----------------------------------------------------------------------

    def decompose_contract(
        self,
        parent_id: str,
        actor_id: str,
        child_specs: list[TaskContract],
    ) -> list[ContractBase]:
        """Create child contracts linked to a parent via lineage."""
        self.actors.assert_exists(actor_id)
        parent = self.get_contract(parent_id)

        child_ids: list[str] = []
        children: list[ContractBase] = []
        for child_spec in child_specs:
            child_spec.lineage = ContractLineage(parent_contract_id=parent_id)
            if not child_spec.contract_id:
                child_spec.contract_id = str(uuid4())
            child = self.create_contract(child_spec, actor_id)
            child_ids.append(child.contract_id)
            children.append(child)

        # Update parent's lineage to include child IDs
        parent.lineage.child_contract_ids.extend(child_ids)
        self.update_contract(
            contract_id=parent_id,
            actor_id=actor_id,
            changes={"lineage": parent.lineage.model_dump()},
        )

        return children

    # -----------------------------------------------------------------------
    # Audit trail
    # -----------------------------------------------------------------------

    def get_audit_trail(self, contract_id: str) -> list[AuditEvent]:
        """Return the audit trail for a contract as domain models."""
        models = self.audit.get_audit_trail(contract_id)
        return [
            AuditEvent(
                event_id=str(m.event_id),
                contract_id=str(m.contract_id),
                event_type=m.event_type,
                actor_id=str(m.actor_id),
                timestamp=m.timestamp.isoformat() if m.timestamp else "",
                reason=m.reason,
                before_snapshot=m.before_snapshot,
                after_snapshot=m.after_snapshot,
                immutable_hash=m.immutable_hash,
                previous_hash=m.previous_hash,
            )
            for m in models
        ]

    # -----------------------------------------------------------------------
    # Internal helpers
    # -----------------------------------------------------------------------

    def _model_to_contract(self, model: ContractModel) -> ContractBase:
        """Deserialize an ORM model to the right ContractBase subclass."""
        kind = ContractKind(model.contract_kind)
        return deserialize_contract(kind, model.document)

    def _get_contract_kind_value(self, contract: ContractBase) -> str:
        """Get the contract_kind string for a contract domain model."""
        for kind, cls in CONTRACT_KIND_REGISTRY.items():
            if isinstance(contract, cls):
                return kind.value
        return ContractKind.task.value
