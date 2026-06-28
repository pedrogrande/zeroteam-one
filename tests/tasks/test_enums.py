"""
Tests for tasks/enums.py
========================

Verify enum values match the v0.1 spec and serialize to strings.
"""

from tasks.enums import (
    ActorType,
    ContractKind,
    ContractStatus,
    ContractType,
    PriorityClassification,
    RoleType,
    VerificationResult,
)


def test_contract_kind_values():
    assert ContractKind.task == "task"
    assert ContractKind.workflow == "workflow"
    assert ContractKind.goal == "goal"


def test_contract_status_values():
    assert ContractStatus.draft == "draft"
    assert ContractStatus.in_progress == "in-progress"
    assert ContractStatus.under_review == "under-review"
    assert ContractStatus.completed == "completed"
    assert ContractStatus.cancelled == "cancelled"


def test_actor_type_values():
    assert ActorType.human == "human"
    assert ActorType.agent == "agent"
    assert ActorType.organisation == "organisation"
    assert ActorType.protocol == "protocol"


def test_role_type_values():
    assert RoleType.requester == "requester"
    assert RoleType.performer == "performer"
    assert RoleType.reviewer == "reviewer"
    assert RoleType.verifier == "verifier"
    assert RoleType.witness == "witness"


def test_priority_classification_values():
    assert PriorityClassification.must_have == "must-have"
    assert PriorityClassification.wont_have == "wont-have"


def test_contract_type_values():
    assert ContractType.one_off == "one-off"
    assert ContractType.recurring == "recurring"
    assert ContractType.ad_hoc == "ad-hoc"


def test_verification_result_values():
    assert VerificationResult.pass_ == "pass"
    assert VerificationResult.fail == "fail"
    assert VerificationResult.pending == "pending"


def test_all_enums_are_str():
    """All enums should be StrEnum so they serialize to strings in JSONB."""
    for kind in ContractKind:
        assert isinstance(kind.value, str)
    for status in ContractStatus:
        assert isinstance(status.value, str)
