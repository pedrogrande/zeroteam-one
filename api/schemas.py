"""
API Schemas
===========

Pydantic request/response models for the API layer.

These are separate from ``tasks/domain.py`` (the canonical data model)
so the API can evolve independently — field names, response shapes, and
pagination wrappers live here, not in the domain model.
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from tasks.enums import ContractKind, ContractStatus


# ---------------------------------------------------------------------------
# Pagination
# ---------------------------------------------------------------------------


class PaginationParams(BaseModel):
    limit: int = Field(default=50, ge=1, le=500)
    offset: int = Field(default=0, ge=0)


class PaginatedResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[Any]


# ---------------------------------------------------------------------------
# Actor
# ---------------------------------------------------------------------------


class ActorCreateRequest(BaseModel):
    actor_id: Optional[str] = None
    actor_type: str
    display_name: str
    trust_score: Optional[float] = None
    reputation_score: Optional[float] = None
    public_key: Optional[str] = None


class ActorResponse(BaseModel):
    actor_id: str
    actor_type: str
    display_name: str
    trust_score: Optional[float] = None
    reputation_score: Optional[float] = None
    public_key: Optional[str] = None


# ---------------------------------------------------------------------------
# Task / Contract
# ---------------------------------------------------------------------------


class TaskCreateRequest(BaseModel):
    """Create a new task contract.

    The ``contract_document`` is the full task contract domain model as a
    dict — it will be validated against the ``TaskContract`` Pydantic model.
    ``actor_id`` is the creator (must exist in the actors table).
    """

    actor_id: str
    contract_kind: ContractKind = ContractKind.task
    contract_document: dict[str, Any]


class TaskUpdateRequest(BaseModel):
    """Update a task contract (creates a new version).

    ``changes`` is a dict of field → value applied to the current contract.
    """

    actor_id: str
    changes: dict[str, Any]
    version_bump: str = Field(default="patch", pattern="^(patch|minor|major)$")


class StateTransitionRequest(BaseModel):
    """Transition a contract to a new state."""

    actor_id: str
    to_state: ContractStatus
    reason: Optional[str] = None


class ClaimRequest(BaseModel):
    """Claim a contract as performer."""

    actor_id: str


class DecomposeRequest(BaseModel):
    """Decompose a contract into child contracts."""

    actor_id: str
    child_specs: list[dict[str, Any]]


class TaskResponse(BaseModel):
    """Full task contract response."""

    contract_id: str
    version: str
    contract_kind: str
    status: str
    contract_type: str
    created_at: str
    document: dict[str, Any]


class TaskListResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[TaskResponse]


class TaskVersionResponse(BaseModel):
    contract_id: str
    version: str
    contract_kind: str
    created_at: Optional[str] = None


class AuditEventResponse(BaseModel):
    event_id: str
    contract_id: str
    contract_kind: str
    event_type: str
    actor_id: str
    timestamp: str
    reason: Optional[str] = None
    before_snapshot: Optional[dict[str, Any]] = None
    after_snapshot: Optional[dict[str, Any]] = None
    immutable_hash: str
    previous_hash: Optional[str] = None


class AuditTrailResponse(BaseModel):
    contract_id: str
    events: list[AuditEventResponse]


# ---------------------------------------------------------------------------
# Artefact
# ---------------------------------------------------------------------------


class ArtefactSubmitRequest(BaseModel):
    """Submit an artefact to a contract."""

    actor_id: str
    artefact: dict[str, Any]


class VerificationRequest(BaseModel):
    """Verify an artefact."""

    verifier_actor_id: str
    method: str
    result: str = Field(pattern="^(pass|fail|pending)$")
    independence_required: bool = False
    quorum_required: Optional[int] = None
    proof_type: Optional[str] = None
    proof_storage_reference: Optional[str] = None
    proof_immutable: bool = False
