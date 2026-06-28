"""
Tests for tasks/state_machine.py
================================

Verify state transition validation.
"""

import pytest

from tasks.enums import ContractStatus
from tasks.state_machine import (
    InvalidTransitionError,
    assert_transition,
    get_valid_transitions,
    validate_transition,
)


def test_valid_transition_draft_to_open():
    assert validate_transition(ContractStatus.draft, ContractStatus.open) is True


def test_valid_transition_open_to_claimed():
    assert validate_transition(ContractStatus.open, ContractStatus.claimed) is True


def test_valid_transition_in_progress_to_completed():
    assert validate_transition(ContractStatus.in_progress, ContractStatus.completed) is True


def test_invalid_transition_draft_to_completed():
    """Cannot jump from draft to completed."""
    assert validate_transition(ContractStatus.draft, ContractStatus.completed) is False


def test_invalid_transition_completed_to_anything():
    """Completed is terminal."""
    assert validate_transition(ContractStatus.completed, ContractStatus.in_progress) is False
    assert validate_transition(ContractStatus.completed, ContractStatus.open) is False


def test_invalid_transition_cancelled_to_anything():
    """Cancelled is terminal."""
    assert validate_transition(ContractStatus.cancelled, ContractStatus.open) is False


def test_assert_transition_raises():
    with pytest.raises(InvalidTransitionError):
        assert_transition(ContractStatus.draft, ContractStatus.completed)


def test_assert_transition_passes():
    """Should not raise for a valid transition."""
    assert_transition(ContractStatus.draft, ContractStatus.open)


def test_get_valid_transitions_draft():
    transitions = get_valid_transitions(ContractStatus.draft)
    assert ContractStatus.open in transitions
    assert ContractStatus.cancelled in transitions
    assert ContractStatus.completed not in transitions


def test_get_valid_transitions_completed_empty():
    """Terminal states should have no valid transitions."""
    assert get_valid_transitions(ContractStatus.completed) == []
    assert get_valid_transitions(ContractStatus.cancelled) == []


def test_get_valid_transitions_in_progress():
    """in_progress should have multiple valid targets."""
    transitions = get_valid_transitions(ContractStatus.in_progress)
    assert ContractStatus.paused in transitions
    assert ContractStatus.under_review in transitions
    assert ContractStatus.completed in transitions
    assert ContractStatus.disputed in transitions


def test_full_lifecycle():
    """A typical lifecycle: draft → open → claimed → in_progress → completed."""
    assert_transition(ContractStatus.draft, ContractStatus.open)
    assert_transition(ContractStatus.open, ContractStatus.claimed)
    assert_transition(ContractStatus.claimed, ContractStatus.in_progress)
    assert_transition(ContractStatus.in_progress, ContractStatus.completed)
