"""
Task Contract State Machine
============================

Validates state transitions for the ``ExecutionState`` lifecycle.

The state graph encodes the allowed transitions from the v0.1 spec's
``ExecutionState.valid_transitions``. The repository calls
``validate_transition`` before applying a state change.
"""

from tasks.enums import ContractStatus

# ---------------------------------------------------------------------------
# Valid transitions — maps each status to the set of allowed target states
# ---------------------------------------------------------------------------

VALID_TRANSITIONS: dict[ContractStatus, frozenset[ContractStatus]] = {
    ContractStatus.draft: frozenset(
        {
            ContractStatus.open,
            ContractStatus.cancelled,
        }
    ),
    ContractStatus.open: frozenset(
        {
            ContractStatus.claimed,
            ContractStatus.cancelled,
            ContractStatus.expired,
        }
    ),
    ContractStatus.claimed: frozenset(
        {
            ContractStatus.in_progress,
            ContractStatus.open,  # un-claim
            ContractStatus.cancelled,
        }
    ),
    ContractStatus.in_progress: frozenset(
        {
            ContractStatus.paused,
            ContractStatus.under_review,
            ContractStatus.completed,
            ContractStatus.disputed,
            ContractStatus.cancelled,
        }
    ),
    ContractStatus.paused: frozenset(
        {
            ContractStatus.in_progress,
            ContractStatus.cancelled,
        }
    ),
    ContractStatus.under_review: frozenset(
        {
            ContractStatus.completed,
            ContractStatus.in_progress,  # rework needed
            ContractStatus.disputed,
        }
    ),
    ContractStatus.disputed: frozenset(
        {
            ContractStatus.in_progress,
            ContractStatus.cancelled,
            ContractStatus.completed,
        }
    ),
    ContractStatus.completed: frozenset(),  # terminal
    ContractStatus.cancelled: frozenset(),  # terminal
    ContractStatus.expired: frozenset(),  # terminal
}


class InvalidTransitionError(ValueError):
    """Raised when a state transition is not allowed."""

    def __init__(self, from_state: ContractStatus, to_state: ContractStatus) -> None:
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(f"Invalid state transition: {from_state.value} → {to_state.value}")


def validate_transition(from_state: ContractStatus, to_state: ContractStatus) -> bool:
    """Return ``True`` if the transition is allowed, ``False`` otherwise."""
    allowed = VALID_TRANSITIONS.get(from_state, frozenset())
    return to_state in allowed


def get_valid_transitions(from_state: ContractStatus) -> list[ContractStatus]:
    """Return the list of states reachable from ``from_state``."""
    return sorted(VALID_TRANSITIONS.get(from_state, frozenset()), key=lambda s: s.value)


def assert_transition(from_state: ContractStatus, to_state: ContractStatus) -> None:
    """Raise ``InvalidTransitionError`` if the transition is not allowed."""
    if not validate_transition(from_state, to_state):
        raise InvalidTransitionError(from_state, to_state)
