"""
Tasks API Router
================

FastAPI router for task contract CRUD, versioning, state transitions,
claims, decomposition, audit trail, and artefact submission.

Path param ``task_id`` maps to the internal ``contract_id``.
"""

from __future__ import annotations

from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from api.deps import get_db_session
from api.schemas import (
    AuditTrailResponse,
    ClaimRequest,
    DecomposeRequest,
    StateTransitionRequest,
    TaskCreateRequest,
    TaskListResponse,
    TaskResponse,
    TaskUpdateRequest,
    TaskVersionResponse,
)
from tasks.domain import TaskContract
from tasks.enums import ContractKind, ContractStatus
from tasks.repository import (
    ActorNotFoundError,
    ContractNotFoundError,
    ContractRepository,
    CrossReferenceError,
)
from tasks.state_machine import InvalidTransitionError

router = APIRouter(prefix="/tasks", tags=["tasks"])


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _get_repo(session: Session = Depends(get_db_session)) -> ContractRepository:
    return ContractRepository(session)


def _contract_to_response(contract: TaskContract, contract_kind: str) -> TaskResponse:
    """Convert a domain model to an API response."""
    return TaskResponse(
        contract_id=contract.contract_id,
        version=contract.version,
        contract_kind=contract_kind,
        status=contract.status,
        contract_type=contract.contract_type,
        created_at=contract.created_at,
        document=contract.model_dump(exclude={"audit_trail"}),
    )


# ---------------------------------------------------------------------------
# Create
# ---------------------------------------------------------------------------


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    request: TaskCreateRequest,
    repo: ContractRepository = Depends(_get_repo),
) -> TaskResponse:
    """Create a new task contract."""
    if request.contract_kind != ContractKind.task:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Only contract_kind='task' is supported (got '{request.contract_kind}')",
        )

    # Validate the document against the TaskContract domain model
    try:
        contract = TaskContract.model_validate(request.contract_document)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid contract document: {e}",
        ) from e

    # Ensure contract_id is set
    if not contract.contract_id:
        contract.contract_id = str(uuid4())

    try:
        created = repo.create_contract(contract, actor_id=request.actor_id)
    except ActorNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    except CrossReferenceError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e

    return _contract_to_response(created, request.contract_kind.value)


# ---------------------------------------------------------------------------
# List
# ---------------------------------------------------------------------------


@router.get("", response_model=TaskListResponse)
def list_tasks(
    contract_kind: Optional[ContractKind] = Query(None),
    status_filter: Optional[ContractStatus] = Query(None, alias="status"),
    actor_id: Optional[str] = Query(None),
    parent_id: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    repo: ContractRepository = Depends(_get_repo),
) -> TaskListResponse:
    """List tasks with optional filters."""
    contracts = repo.list_contracts(
        contract_kind=contract_kind,
        status=status_filter,
        actor_id=actor_id,
        parent_id=parent_id,
        limit=limit,
        offset=offset,
    )
    items = [_contract_to_response(c, ContractKind.task.value) for c in contracts]
    return TaskListResponse(total=len(items), limit=limit, offset=offset, items=items)


# ---------------------------------------------------------------------------
# Get
# ---------------------------------------------------------------------------


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: str,
    version: Optional[str] = Query(None),
    repo: ContractRepository = Depends(_get_repo),
) -> TaskResponse:
    """Get a task contract. Returns the latest version unless ``version`` is specified."""
    try:
        contract = repo.get_contract(task_id, version=version)
    except ContractNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    return _contract_to_response(contract, ContractKind.task.value)


# ---------------------------------------------------------------------------
# Versions
# ---------------------------------------------------------------------------


@router.get("/{task_id}/versions", response_model=list[TaskVersionResponse])
def get_task_versions(
    task_id: str,
    repo: ContractRepository = Depends(_get_repo),
) -> list[TaskVersionResponse]:
    """Get all versions of a task contract."""
    versions = repo.get_contract_versions(task_id)
    return [TaskVersionResponse(**v) for v in versions]


@router.get("/{task_id}/versions/{version}", response_model=TaskResponse)
def get_task_version(
    task_id: str,
    version: str,
    repo: ContractRepository = Depends(_get_repo),
) -> TaskResponse:
    """Get a specific version of a task contract."""
    try:
        contract = repo.get_contract(task_id, version=version)
    except ContractNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    return _contract_to_response(contract, ContractKind.task.value)


# ---------------------------------------------------------------------------
# Update (creates new version)
# ---------------------------------------------------------------------------


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: str,
    request: TaskUpdateRequest,
    repo: ContractRepository = Depends(_get_repo),
) -> TaskResponse:
    """Update a task contract. Creates a new version."""
    try:
        updated = repo.update_contract(
            contract_id=task_id,
            actor_id=request.actor_id,
            changes=request.changes,
            version_bump=request.version_bump,
        )
    except ContractNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except ActorNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    except CrossReferenceError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    return _contract_to_response(updated, ContractKind.task.value)


# ---------------------------------------------------------------------------
# State transition
# ---------------------------------------------------------------------------


@router.post("/{task_id}/transition", response_model=TaskResponse)
def transition_task(
    task_id: str,
    request: StateTransitionRequest,
    repo: ContractRepository = Depends(_get_repo),
) -> TaskResponse:
    """Transition a task contract to a new state."""
    try:
        updated = repo.transition_state(
            contract_id=task_id,
            actor_id=request.actor_id,
            to_state=request.to_state,
            reason=request.reason,
        )
    except ContractNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except InvalidTransitionError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    except ActorNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    return _contract_to_response(updated, ContractKind.task.value)


# ---------------------------------------------------------------------------
# Claim
# ---------------------------------------------------------------------------


@router.post("/{task_id}/claim", response_model=TaskResponse)
def claim_task(
    task_id: str,
    request: ClaimRequest,
    repo: ContractRepository = Depends(_get_repo),
) -> TaskResponse:
    """Claim a task contract as performer."""
    try:
        updated = repo.claim_contract(
            contract_id=task_id,
            actor_id=request.actor_id,
        )
    except ContractNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    except ActorNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    return _contract_to_response(updated, ContractKind.task.value)


# ---------------------------------------------------------------------------
# Decompose
# ---------------------------------------------------------------------------


@router.post("/{task_id}/decompose", response_model=list[TaskResponse])
def decompose_task(
    task_id: str,
    request: DecomposeRequest,
    repo: ContractRepository = Depends(_get_repo),
) -> list[TaskResponse]:
    """Decompose a task contract into child contracts."""
    # Validate child specs
    try:
        child_specs = [TaskContract.model_validate(spec) for spec in request.child_specs]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid child spec: {e}",
        ) from e

    try:
        children = repo.decompose_contract(
            parent_id=task_id,
            actor_id=request.actor_id,
            child_specs=child_specs,
        )
    except ContractNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except ActorNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    except CrossReferenceError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    return [_contract_to_response(c, ContractKind.task.value) for c in children]


# ---------------------------------------------------------------------------
# Audit trail
# ---------------------------------------------------------------------------


@router.get("/{task_id}/audit", response_model=AuditTrailResponse)
def get_task_audit(
    task_id: str,
    repo: ContractRepository = Depends(_get_repo),
) -> AuditTrailResponse:
    """Get the audit trail for a task contract."""
    events = repo.get_audit_trail(task_id)
    from api.schemas import AuditEventResponse

    return AuditTrailResponse(
        contract_id=task_id,
        events=[
            AuditEventResponse(
                event_id=e.event_id,
                contract_id=e.contract_id,
                contract_kind=ContractKind.task.value,
                event_type=e.event_type,
                actor_id=e.actor_id,
                timestamp=e.timestamp,
                reason=e.reason,
                before_snapshot=e.before_snapshot,
                after_snapshot=e.after_snapshot,
                immutable_hash=e.immutable_hash,
                previous_hash=e.previous_hash,
            )
            for e in events
        ],
    )
