"""
Task Contract Enums
===================

Discriminated-union enums for every polymorphic field in the task contract
data model. All are ``StrEnum`` so they serialize to plain strings in JSONB
and are accepted as ``str`` by Pydantic's ``use_enum_values=True``.
"""

from enum import StrEnum


class ContractKind(StrEnum):
    """Polymorphic discriminator for the ``contracts`` table.

    Extensible — adding a new contract type (workflow, goal, etc.) only
    requires adding a value here and registering the domain model in
    ``CONTRACT_KIND_REGISTRY``. No table migration.
    """

    task = "task"
    workflow = "workflow"
    goal = "goal"


class ActorType(StrEnum):
    human = "human"
    agent = "agent"
    organisation = "organisation"
    protocol = "protocol"


class ContractType(StrEnum):
    one_off = "one-off"
    recurring = "recurring"
    ad_hoc = "ad-hoc"


class ContractStatus(StrEnum):
    draft = "draft"
    open = "open"
    claimed = "claimed"
    in_progress = "in-progress"
    paused = "paused"
    under_review = "under-review"
    disputed = "disputed"
    completed = "completed"
    cancelled = "cancelled"
    expired = "expired"


class RoleType(StrEnum):
    requester = "requester"
    performer = "performer"
    owner = "owner"
    reviewer = "reviewer"
    verifier = "verifier"
    stakeholder = "stakeholder"
    witness = "witness"


class ClaimMechanism(StrEnum):
    assigned = "assigned"
    self_selected = "self-selected"
    auctioned = "auctioned"
    delegated = "delegated"


class ReviewType(StrEnum):
    quality = "quality"
    compliance = "compliance"
    safety = "safety"
    domain_expertise = "domain-expertise"


class ReviewStructure(StrEnum):
    sequential = "sequential"
    parallel = "parallel"


class InputRights(StrEnum):
    none = "none"
    advisory = "advisory"
    approval = "approval"


class InputType(StrEnum):
    data = "data"
    decision = "decision"
    artefact = "artefact"
    access = "access"
    briefing = "briefing"


class DependencyType(StrEnum):
    hard = "hard"
    soft = "soft"
    informational = "informational"


class ResolutionStatus(StrEnum):
    resolved = "resolved"
    unresolved = "unresolved"
    waived = "waived"


class DeadlineType(StrEnum):
    hard = "hard"
    soft = "soft"


class RecurrenceType(StrEnum):
    once = "once"
    scheduled = "scheduled"
    ad_hoc = "ad-hoc"


class PriorityClassification(StrEnum):
    must_have = "must-have"
    should_have = "should-have"
    could_have = "could-have"
    wont_have = "wont-have"


class AllocationType(StrEnum):
    assigned = "assigned"
    claimable = "claimable"
    auctioned = "auctioned"
    delegated = "delegated"
    automated = "automated"


class RiskType(StrEnum):
    non_completion = "non-completion"
    execution_quality = "execution-quality"
    safety = "safety"
    dependency = "dependency"
    data_security = "data-security"
    compliance = "compliance"
    reputational = "reputational"


class Likelihood(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"


class ConsequenceSeverity(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class CompensationType(StrEnum):
    monetary = "monetary"
    token = "token"
    credit = "credit"
    reputational = "reputational"
    in_kind = "in-kind"


class PaymentTrigger(StrEnum):
    on_completion = "on-completion"
    on_verification = "on-verification"
    on_value_realisation = "on-value-realisation"


class IncentiveType(StrEnum):
    bonus = "bonus"
    penalty = "penalty"


class ValueType(StrEnum):
    financial = "financial"
    operational = "operational"
    strategic = "strategic"
    relational = "relational"
    informational = "informational"


class DecayProfile(StrEnum):
    none = "none"
    linear = "linear"
    exponential = "exponential"
    cliff_edge = "cliff-edge"


class WasteClassification(StrEnum):
    value_creating = "value-creating"
    enabling = "enabling"
    protecting = "protecting"
    discovering = "discovering"


class EventType(StrEnum):
    state_transition = "state-transition"
    edit = "edit"
    assignment = "assignment"
    claim = "claim"
    verification = "verification"
    cancellation = "cancellation"
    dispute = "dispute"


class CommitmentType(StrEnum):
    requester = "requester"
    performer = "performer"
    reviewer = "reviewer"
    verifier = "verifier"
    witness = "witness"


class WitnessType(StrEnum):
    organisational = "organisational"
    decentralised = "decentralised"
    notarial = "notarial"


class VerificationResult(StrEnum):
    pass_ = "pass"
    fail = "fail"
    pending = "pending"


class JurisdictionType(StrEnum):
    legal = "legal"
    organisational = "organisational"
    decentralised = "decentralised"


class ComplexityRating(StrEnum):
    trivial = "trivial"
    low = "low"
    medium = "medium"
    high = "high"
    extreme = "extreme"


class CognitiveLoadType(StrEnum):
    generative = "generative"
    analytical = "analytical"
    procedural = "procedural"
    communicative = "communicative"


class FlowPotentialRating(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"


class KnowledgeOutputType(StrEnum):
    template = "template"
    decision_record = "decision-record"
    process_documentation = "process-documentation"
    insight = "insight"


class Reusability(StrEnum):
    single_use = "single-use"
    team = "team"
    organisation = "organisation"
    public = "public"


class DisputeResolutionMechanism(StrEnum):
    human_arbitration = "human-arbitration"
    protocol_rule = "protocol-rule"
    dao_vote = "dao-vote"


class AvailabilityStatus(StrEnum):
    available = "available"
    pending = "pending"
    blocked = "blocked"
