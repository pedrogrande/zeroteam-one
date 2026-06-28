"""
Tests for tasks/domain.py
=========================

Verify Pydantic model validation, serialization, ContractBase/TaskContract
inheritance, CONTRACT_KIND_REGISTRY, and the duplicate actor_role validator.
"""

from uuid import uuid4

import pytest
from pydantic import ValidationError

from tasks.domain import (
    CONTRACT_KIND_REGISTRY,
    ContractBase,
    TaskContract,
    deserialize_contract,
)
from tasks.domain import Actor, ActorRole, TaskSpec
from tasks.enums import (
    ActorType,
    ContractKind,
    ContractStatus,
    ContractType,
    RoleType,
)


def _make_actor() -> Actor:
    return Actor(
        actor_id=str(uuid4()),
        actor_type=ActorType.human,
        display_name="Test Actor",
    )


def _make_minimal_task_contract() -> TaskContract:
    return TaskContract(
        contract_id=str(uuid4()),
        created_at="2026-06-27T00:00:00+00:00",
        contract_type=ContractType.one_off,
        status=ContractStatus.draft,
    )


def test_task_contract_minimal():
    """A TaskContract with only required fields should validate."""
    contract = _make_minimal_task_contract()
    assert contract.contract_id
    assert contract.version == "1.0.0"
    assert contract.status == "draft"


def test_task_contract_inherits_contract_base():
    """TaskContract should inherit from ContractBase."""
    assert issubclass(TaskContract, ContractBase)


def test_contract_kind_registry_has_task():
    """The registry should map ContractKind.task → TaskContract."""
    assert CONTRACT_KIND_REGISTRY[ContractKind.task] is TaskContract


def test_deserialize_contract_task():
    """deserialize_contract should produce a TaskContract for kind=task."""
    contract = _make_minimal_task_contract()
    doc = contract.model_dump()
    result = deserialize_contract(ContractKind.task, doc)
    assert isinstance(result, TaskContract)
    assert result.contract_id == contract.contract_id


def test_deserialize_contract_unknown_kind():
    """deserialize_contract should raise for an unregistered kind."""
    with pytest.raises(ValueError, match="Unknown contract_kind"):
        deserialize_contract(ContractKind.workflow, {})


def test_task_contract_serialization_roundtrip():
    """model_dump → model_validate should round-trip."""
    contract = _make_minimal_task_contract()
    contract.specification = TaskSpec(
        title="Test Task",
        description="A test task",
        task_type="deliver",
        functional_domain="engineering",
        value_stream_category="build",
    )
    doc = contract.model_dump()
    restored = TaskContract.model_validate(doc)
    assert restored.specification is not None
    assert restored.specification.title == "Test Task"


def test_duplicate_actor_roles_rejected():
    """The @field_validator should reject duplicate actor_id + role_type."""
    actor_id = str(uuid4())
    contract = _make_minimal_task_contract()
    contract.actor_roles = [
        ActorRole(
            role_id=str(uuid4()),
            contract_id=contract.contract_id,
            actor_id=actor_id,
            role_type=RoleType.requester,
        ),
        ActorRole(
            role_id=str(uuid4()),
            contract_id=contract.contract_id,
            actor_id=actor_id,
            role_type=RoleType.requester,
        ),
    ]
    with pytest.raises(ValidationError, match="Duplicate actor_role"):
        TaskContract.model_validate(contract.model_dump())


def test_different_roles_same_actor_allowed():
    """Same actor with different role types should be allowed."""
    actor_id = str(uuid4())
    contract = _make_minimal_task_contract()
    contract.actor_roles = [
        ActorRole(
            role_id=str(uuid4()),
            contract_id=contract.contract_id,
            actor_id=actor_id,
            role_type=RoleType.requester,
        ),
        ActorRole(
            role_id=str(uuid4()),
            contract_id=contract.contract_id,
            actor_id=actor_id,
            role_type=RoleType.owner,
        ),
    ]
    # Should not raise
    restored = TaskContract.model_validate(contract.model_dump())
    assert len(restored.actor_roles) == 2


def test_task_spec_defaults():
    """TaskSpec nested models should have sensible defaults."""
    spec = TaskSpec(
        title="T",
        description="D",
        task_type="deliver",
        functional_domain="eng",
        value_stream_category="build",
    )
    assert spec.scope.inclusions == []
    assert spec.effort.max_permitted_duration_minutes == 240
    assert spec.expected_outputs.artefacts == []


def test_actor_model_validation():
    """Actor should validate with required fields."""
    actor = _make_actor()
    assert actor.actor_type == "human"
    assert actor.display_name == "Test Actor"


def test_contract_base_extra_forbid():
    """ContractBase should reject extra fields (extra='forbid')."""
    with pytest.raises(ValidationError):
        TaskContract(
            contract_id=str(uuid4()),
            created_at="2026-06-27T00:00:00+00:00",
            non_existent_field="oops",  # type: ignore[call-arg]
        )
