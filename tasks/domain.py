"""
Task Contract Domain Models
===========================

Pydantic v2 models mirroring the task contract data model v0.1 spec.

Two-layer inheritance for polymorphism:

- ``ContractBase`` — shared fields across all contract kinds (contract_id,
  version, status, origin, schedule, priority, execution_state, actor_roles,
  audit_trail, lineage, signatures, notifications).
- ``TaskContract(ContractBase)`` — adds task-specific embedded entities
  (specification, value_declaration, capability_requirements, inputs,
  dependencies, risks, quality, governance, compensation, verification,
  learning).

Future contract types (``WorkflowContract``, etc.) inherit from
``ContractBase`` and register in ``CONTRACT_KIND_REGISTRY`` — no table
migration needed.

Conventions:
- UUIDs are ``str`` (not ``uuid.UUID``) for JSONB round-trip simplicity.
- Timestamps are ISO 8601 strings.
- ``use_enum_values=True`` so enums serialize to strings in JSONB.
- ``populate_by_name=True`` so alias names are accepted on input.
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from tasks.enums import (
    ActorType,
    AllocationType,
    AvailabilityStatus,
    ClaimMechanism,
    CognitiveLoadType,
    CommitmentType,
    ComplexityRating,
    ConsequenceSeverity,
    ContractKind,
    ContractStatus,
    ContractType,
    DeadlineType,
    DecayProfile,
    DependencyType,
    DisputeResolutionMechanism,
    EventType,
    FlowPotentialRating,
    IncentiveType,
    InputRights,
    InputType,
    JurisdictionType,
    KnowledgeOutputType,
    Likelihood,
    PaymentTrigger,
    PriorityClassification,
    RecurrenceType,
    ResolutionStatus,
    ReviewStructure,
    ReviewType,
    Reusability,
    RiskType,
    RoleType,
    VerificationResult,
    ValueType,
    WasteClassification,
    WitnessType,
    CompensationType,
    DeadlineType as _DeadlineType,  # noqa: F401 — re-export guard
)

# ---------------------------------------------------------------------------
# Base config shared by all domain models
# ---------------------------------------------------------------------------

_DOMAIN_CONFIG = ConfigDict(
    use_enum_values=True,
    populate_by_name=True,
    extra="forbid",
)


# ---------------------------------------------------------------------------
# Actor (shared / normalised)
# ---------------------------------------------------------------------------


class Actor(BaseModel):
    """Referenced by role records — not embedded directly in contracts."""

    model_config = _DOMAIN_CONFIG

    actor_id: str
    actor_type: ActorType
    display_name: str
    trust_score: Optional[float] = None
    reputation_score: Optional[float] = None
    public_key: Optional[str] = None


# ---------------------------------------------------------------------------
# ActorRole
# ---------------------------------------------------------------------------


class ActorRole(BaseModel):
    """Maps an actor to a contract with a role designation."""

    model_config = _DOMAIN_CONFIG

    role_id: str
    contract_id: str
    actor_id: str
    role_type: RoleType
    authority_level: Optional[str] = None
    claim_mechanism: Optional[ClaimMechanism] = None
    claim_timestamp: Optional[str] = None
    delegability_permitted: bool = False
    review_type: Optional[ReviewType] = None
    review_structure: Optional[ReviewStructure] = None
    input_rights: Optional[InputRights] = None
    notification_entitlements: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# VerificationRecord (shared by AcceptanceCriterion and Artefact)
# ---------------------------------------------------------------------------


class VerificationRecord(BaseModel):
    model_config = _DOMAIN_CONFIG

    verification_id: str
    verifier_actor_id: str
    verified_at: str
    method: str
    result: VerificationResult = VerificationResult.pending
    independence_required: bool = False
    quorum_required: Optional[int] = None
    proof_type: Optional[str] = None
    proof_storage_reference: Optional[str] = None
    proof_immutable: bool = False


# ---------------------------------------------------------------------------
# AcceptanceCriterion
# ---------------------------------------------------------------------------


class AcceptanceCriterion(BaseModel):
    model_config = _DOMAIN_CONFIG

    criterion_id: str
    contract_id: str
    sequence: int
    description: str
    verification_method: str
    verifier_actor_id: str
    verification_record: Optional[VerificationRecord] = None


# ---------------------------------------------------------------------------
# Artefact
# ---------------------------------------------------------------------------


class Artefact(BaseModel):
    model_config = _DOMAIN_CONFIG

    artefact_id: str
    contract_id: str
    artefact_type: str
    format: str
    destination: str
    submission_timestamp: Optional[str] = None
    storage_reference: Optional[str] = None
    immutable_hash: Optional[str] = None
    verification_record: Optional[VerificationRecord] = None


# ---------------------------------------------------------------------------
# TaskSpec and nested entities
# ---------------------------------------------------------------------------


class Scope(BaseModel):
    model_config = _DOMAIN_CONFIG

    inclusions: list[str] = Field(default_factory=list)
    exclusions: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)


class Handoff(BaseModel):
    model_config = _DOMAIN_CONFIG

    recipient_actor_id: str
    format: str
    timing: str


class ExpectedOutputs(BaseModel):
    model_config = _DOMAIN_CONFIG

    artefacts: list[Artefact] = Field(default_factory=list)
    state_changes: list[str] = Field(default_factory=list)
    decisions_to_record: list[str] = Field(default_factory=list)
    communications_to_send: list[str] = Field(default_factory=list)
    handoff: Optional[Handoff] = None


class Effort(BaseModel):
    model_config = _DOMAIN_CONFIG

    complexity_rating: ComplexityRating = ComplexityRating.medium
    cognitive_load_type: CognitiveLoadType = CognitiveLoadType.analytical
    estimated_effort_minutes: int = 0
    estimated_lead_time_minutes: int = 0
    max_permitted_duration_minutes: int = 240
    flow_potential_rating: FlowPotentialRating = FlowPotentialRating.medium
    focus_mode_required: bool = False


class TaskSpec(BaseModel):
    model_config = _DOMAIN_CONFIG

    title: str
    description: str
    task_type: str
    functional_domain: str
    value_stream_category: str
    tags: list[str] = Field(default_factory=list)
    scope: Scope = Field(default_factory=Scope)
    acceptance_criteria: list[AcceptanceCriterion] = Field(default_factory=list)
    min_quality_threshold: Optional[str] = None
    target_quality_standard: Optional[str] = None
    expected_outputs: ExpectedOutputs = Field(default_factory=ExpectedOutputs)
    effort: Effort = Field(default_factory=Effort)


# ---------------------------------------------------------------------------
# ValueDeclaration and nested entities
# ---------------------------------------------------------------------------


class ValueToRequester(BaseModel):
    model_config = _DOMAIN_CONFIG

    value_type: ValueType = ValueType.operational
    estimated_value_quantum: str
    realisation_timeframe: str
    decay_profile: DecayProfile = DecayProfile.none


class ValueToPerformer(BaseModel):
    model_config = _DOMAIN_CONFIG

    compensation_preview: str
    skill_development_opportunity: bool = False
    knowledge_gain: Optional[str] = None
    portfolio_contribution: bool = False


class ValueToOrganisation(BaseModel):
    model_config = _DOMAIN_CONFIG

    strategic_alignment_score: float = 0.0
    contribution_to_mission: str
    leverage_score: float = 0.0
    waste_classification: WasteClassification = WasteClassification.value_creating


class ValueToBroaderStakeholders(BaseModel):
    model_config = _DOMAIN_CONFIG

    third_party_beneficiaries: list[str] = Field(default_factory=list)
    community_value: Optional[str] = None
    negative_externalities: list[str] = Field(default_factory=list)


class ValueVerification(BaseModel):
    model_config = _DOMAIN_CONFIG

    assessment_method: str
    realisation_timeline: str
    accountable_assessor_actor_id: str


class ValueDeclaration(BaseModel):
    model_config = _DOMAIN_CONFIG

    to_requester: ValueToRequester
    to_performer: ValueToPerformer
    to_organisation: ValueToOrganisation
    to_broader_stakeholders: ValueToBroaderStakeholders = Field(default_factory=ValueToBroaderStakeholders)
    value_verification: Optional[ValueVerification] = None


# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------


class Input(BaseModel):
    model_config = _DOMAIN_CONFIG

    input_id: str
    contract_id: str
    description: str
    input_type: InputType
    provided_by_actor_id: str
    required_before_start: bool = False
    availability_status: AvailabilityStatus = AvailabilityStatus.pending


# ---------------------------------------------------------------------------
# Dependency
# ---------------------------------------------------------------------------


class Dependency(BaseModel):
    model_config = _DOMAIN_CONFIG

    dependency_id: str
    contract_id: str
    depends_on_contract_id: Optional[str] = None
    blocks_contract_id: Optional[str] = None
    dependency_type: DependencyType = DependencyType.informational
    resolution_status: ResolutionStatus = ResolutionStatus.unresolved


# ---------------------------------------------------------------------------
# Schedule
# ---------------------------------------------------------------------------


class Recurrence(BaseModel):
    model_config = _DOMAIN_CONFIG

    recurrence_type: RecurrenceType = RecurrenceType.once
    cron_expression: Optional[str] = None
    instance_number: Optional[int] = None
    parent_recurrence_contract_id: Optional[str] = None


class Schedule(BaseModel):
    model_config = _DOMAIN_CONFIG

    earliest_start: Optional[str] = None
    due_date: str
    deadline_type: DeadlineType = DeadlineType.soft
    expiry_condition: Optional[str] = None
    time_sensitivity: Optional[str] = None
    time_sensitivity_ruleset_version: Optional[str] = None
    recurrence: Recurrence = Field(default_factory=Recurrence)
    trigger_condition: Optional[str] = None
    pre_conditions_checklist: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Priority
# ---------------------------------------------------------------------------


class Allocation(BaseModel):
    model_config = _DOMAIN_CONFIG

    allocation_type: AllocationType = AllocationType.assigned
    claim_window_open: Optional[str] = None
    claim_window_close: Optional[str] = None
    max_concurrent_claims: int = 1
    allocation_authority_actor_id: Optional[str] = None


class Priority(BaseModel):
    model_config = _DOMAIN_CONFIG

    priority_classification: PriorityClassification = PriorityClassification.should_have
    priority_score: float = 0.0
    ruleset_version: Optional[str] = None
    last_reviewed_at: str
    allocation: Allocation = Field(default_factory=Allocation)


# ---------------------------------------------------------------------------
# Risk
# ---------------------------------------------------------------------------


class Risk(BaseModel):
    model_config = _DOMAIN_CONFIG

    risk_id: str
    contract_id: str
    risk_type: RiskType
    description: str
    likelihood: Likelihood = Likelihood.medium
    consequence_severity: ConsequenceSeverity = ConsequenceSeverity.medium
    risk_tier: int = Field(default=2, ge=1, le=4)
    mitigation_strategy: str
    owner_actor_id: str


# ---------------------------------------------------------------------------
# CompensationSpec
# ---------------------------------------------------------------------------


class BaseCompensation(BaseModel):
    model_config = _DOMAIN_CONFIG

    compensation_type: CompensationType = CompensationType.reputational
    amount_or_formula: str
    payment_trigger: PaymentTrigger = PaymentTrigger.on_completion
    payment_mechanism: str


class Incentive(BaseModel):
    model_config = _DOMAIN_CONFIG

    incentive_type: IncentiveType
    condition: str
    value: str
    ruleset_version: Optional[str] = None


class ReputationEffects(BaseModel):
    model_config = _DOMAIN_CONFIG

    on_success: str
    on_failure: str
    reputation_system_reference: Optional[str] = None


class CompensationSpec(BaseModel):
    model_config = _DOMAIN_CONFIG

    base_compensation: Optional[BaseCompensation] = None
    incentives: list[Incentive] = Field(default_factory=list)
    reputation_effects: Optional[ReputationEffects] = None


# ---------------------------------------------------------------------------
# ExecutionState
# ---------------------------------------------------------------------------


class ValidTransition(BaseModel):
    model_config = _DOMAIN_CONFIG

    from_state: str
    to_state: str
    trigger: str
    authority_actor_id: str


class Dispute(BaseModel):
    model_config = _DOMAIN_CONFIG

    trigger_conditions: list[str] = Field(default_factory=list)
    resolution_mechanism: DisputeResolutionMechanism = DisputeResolutionMechanism.human_arbitration
    resolution_timeline: Optional[str] = None
    escalation_path: Optional[str] = None


class ExecutionState(BaseModel):
    model_config = _DOMAIN_CONFIG

    current_state: ContractStatus = ContractStatus.draft
    valid_transitions: list[ValidTransition] = Field(default_factory=list)
    pause_conditions: list[str] = Field(default_factory=list)
    cancellation_conditions: list[str] = Field(default_factory=list)
    cancellation_consequences: Optional[str] = None
    cancellation_authority_actor_id: Optional[str] = None
    dispute: Dispute = Field(default_factory=Dispute)


# ---------------------------------------------------------------------------
# AuditEvent
# ---------------------------------------------------------------------------


class AuditEvent(BaseModel):
    """Immutable append-only log entry. Stored in the ``audit_events`` table,
    not inside the JSONB document. Included in ``ContractBase.audit_trail``
    as a read projection."""

    model_config = _DOMAIN_CONFIG

    event_id: str
    contract_id: str
    event_type: EventType
    actor_id: str
    timestamp: str
    reason: Optional[str] = None
    before_snapshot: Optional[dict[str, Any]] = None
    after_snapshot: Optional[dict[str, Any]] = None
    immutable_hash: str
    previous_hash: Optional[str] = None


# ---------------------------------------------------------------------------
# ContractLineage
# ---------------------------------------------------------------------------


class ContractLineage(BaseModel):
    model_config = _DOMAIN_CONFIG

    parent_contract_id: Optional[str] = None
    child_contract_ids: list[str] = Field(default_factory=list)
    prior_version_ids: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# LearningRecord
# ---------------------------------------------------------------------------


class Retrospective(BaseModel):
    model_config = _DOMAIN_CONFIG

    trigger_conditions: list[str] = Field(default_factory=list)
    format_reference: Optional[str] = None
    notes: Optional[str] = None
    conducted_by_actor_id: Optional[str] = None
    conducted_at: Optional[str] = None


class KnowledgeOutput(BaseModel):
    model_config = _DOMAIN_CONFIG

    output_type: KnowledgeOutputType
    knowledge_base_reference: str
    reusability: Reusability = Reusability.team
    guidelines_version: Optional[str] = None


class CapabilityDevelopment(BaseModel):
    model_config = _DOMAIN_CONFIG

    skill_development_flag: bool = False
    supervising_actor_id: Optional[str] = None
    competency_evidence_generated: bool = False


class LearningRecord(BaseModel):
    model_config = _DOMAIN_CONFIG

    expected_outcome: str
    actual_outcome: Optional[str] = None
    outcome_variance: Optional[str] = None
    task_validated: Optional[bool] = None
    retrospective: Retrospective = Field(default_factory=Retrospective)
    knowledge_outputs: list[KnowledgeOutput] = Field(default_factory=list)
    capability_development: CapabilityDevelopment = Field(default_factory=CapabilityDevelopment)


# ---------------------------------------------------------------------------
# Commitment (Signatures)
# ---------------------------------------------------------------------------


class Commitment(BaseModel):
    model_config = _DOMAIN_CONFIG

    commitment_id: str
    contract_id: str
    actor_id: str
    commitment_type: CommitmentType
    cryptographic_signature: str
    signed_at: str
    declaration: str
    witness_type: Optional[WitnessType] = None


# ---------------------------------------------------------------------------
# Ruleset
# ---------------------------------------------------------------------------


class Ruleset(BaseModel):
    model_config = _DOMAIN_CONFIG

    ruleset_id: str
    ruleset_name: str
    version: str
    domain: str


# ---------------------------------------------------------------------------
# NotificationRule
# ---------------------------------------------------------------------------


class NotificationRule(BaseModel):
    model_config = _DOMAIN_CONFIG

    trigger_event: str
    recipient_actor_ids: list[str] = Field(default_factory=list)
    channel: str
    ruleset_version: Optional[str] = None


# ---------------------------------------------------------------------------
# QualitySpec
# ---------------------------------------------------------------------------


class QualitySpec(BaseModel):
    model_config = _DOMAIN_CONFIG

    target_quality_level: str
    quality_criteria: list[str] = Field(default_factory=list)
    quality_ruleset_version: Optional[str] = None
    assessed_by_actor_id: Optional[str] = None
    assessment_method: Optional[str] = None
    achieved_quality: Optional[str] = None
    quality_variance: Optional[str] = None


# ---------------------------------------------------------------------------
# Governance
# ---------------------------------------------------------------------------


class Governance(BaseModel):
    model_config = _DOMAIN_CONFIG

    confidentiality_classification: Optional[str] = None
    handling_obligations: list[str] = Field(default_factory=list)
    permitted_actor_ids: list[str] = Field(default_factory=list)
    data_retention_requirements: Optional[str] = None
    confidentiality_ruleset_version: Optional[str] = None
    compliance_obligations: list[str] = Field(default_factory=list)
    compliance_verification_method: Optional[str] = None
    compliance_verifier_actor_id: Optional[str] = None
    governing_rulesets: list[Ruleset] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# CapabilityRequirements
# ---------------------------------------------------------------------------


class CapabilityRequirements(BaseModel):
    model_config = _DOMAIN_CONFIG

    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    skill_assessment_method: Optional[str] = None
    skill_ruleset_version: Optional[str] = None
    required_knowledge_domains: list[str] = Field(default_factory=list)
    organisation_specific_context: list[str] = Field(default_factory=list)
    required_tools: list[str] = Field(default_factory=list)
    access_requirements: list[str] = Field(default_factory=list)
    licensing_requirements: list[str] = Field(default_factory=list)
    min_experience_classification: Optional[str] = None
    experience_ruleset_version: Optional[str] = None
    eligibility_criteria: list[str] = Field(default_factory=list)
    disqualifying_conditions: list[str] = Field(default_factory=list)
    trust_score_minimum: Optional[float] = None
    reputation_threshold: Optional[float] = None


# ---------------------------------------------------------------------------
# VerificationSpec
# ---------------------------------------------------------------------------


class VerificationSpec(BaseModel):
    model_config = _DOMAIN_CONFIG

    verification_sequence: list[str] = Field(default_factory=list)
    independent_verification_required: bool = False
    decentralised_quorum: Optional[int] = None
    verification_deadline: Optional[str] = None
    proof_types: list[str] = Field(default_factory=list)
    proof_storage_references: list[str] = Field(default_factory=list)
    proof_immutability_required: bool = False


# ---------------------------------------------------------------------------
# OriginIntent
# ---------------------------------------------------------------------------


class OriginIntent(BaseModel):
    """Covers section I — origin and intent."""

    model_config = _DOMAIN_CONFIG

    originating_desire: str
    problem_or_gap: str
    current_state: str
    desired_state: str
    parent_desire_reference: Optional[str] = None
    value_stream_position: Optional[str] = None
    outcome_contribution: Optional[str] = None
    entropy_resolved: Optional[str] = None
    created_by_actor_id: str
    creation_source: str
    creation_timestamp: str
    originating_context_reference: Optional[str] = None


# ---------------------------------------------------------------------------
# Jurisdiction
# ---------------------------------------------------------------------------


class Jurisdiction(BaseModel):
    model_config = _DOMAIN_CONFIG

    type: JurisdictionType
    reference: str


# ---------------------------------------------------------------------------
# ContractBase — shared fields across all contract kinds
# ---------------------------------------------------------------------------


class ContractBase(BaseModel):
    """Shared fields across all contract kinds.

    Subclasses (``TaskContract``, future ``WorkflowContract``, etc.) add
    kind-specific embedded entities.
    """

    model_config = _DOMAIN_CONFIG

    contract_id: str
    version: str = "1.0.0"
    created_at: str
    governing_protocol_version: Optional[str] = None
    jurisdiction: Optional[Jurisdiction] = None
    contract_type: ContractType = ContractType.one_off
    status: ContractStatus = ContractStatus.draft
    origin: Optional[OriginIntent] = None
    schedule: Optional[Schedule] = None
    priority: Optional[Priority] = None
    execution_state: ExecutionState = Field(default_factory=ExecutionState)
    actor_roles: list[ActorRole] = Field(default_factory=list)
    audit_trail: list[AuditEvent] = Field(default_factory=list)
    lineage: ContractLineage = Field(default_factory=ContractLineage)
    signatures: list[Commitment] = Field(default_factory=list)
    notifications: list[NotificationRule] = Field(default_factory=list)

    @field_validator("actor_roles")
    @classmethod
    def _no_duplicate_actor_roles(cls, v: list[ActorRole]) -> list[ActorRole]:
        """JSONB can't enforce uniqueness at the DB level — check here."""
        seen: set[tuple[str, str]] = set()
        for role in v:
            key = (role.actor_id, role.role_type)
            if key in seen:
                raise ValueError(f"Duplicate actor_role: actor_id={role.actor_id}, role_type={role.role_type}")
            seen.add(key)
        return v


# ---------------------------------------------------------------------------
# TaskContract — task-specific contract
# ---------------------------------------------------------------------------


class TaskContract(ContractBase):
    """Task contract — the v0.1 spec's root aggregate with task-specific
    embedded entities."""

    specification: Optional[TaskSpec] = None
    value_declaration: Optional[ValueDeclaration] = None
    capability_requirements: Optional[CapabilityRequirements] = None
    inputs: list[Input] = Field(default_factory=list)
    dependencies: list[Dependency] = Field(default_factory=list)
    risks: list[Risk] = Field(default_factory=list)
    quality: Optional[QualitySpec] = None
    governance: Optional[Governance] = None
    compensation: Optional[CompensationSpec] = None
    verification: Optional[VerificationSpec] = None
    learning: Optional[LearningRecord] = None


# ---------------------------------------------------------------------------
# Contract kind registry — maps ContractKind → domain model class
# ---------------------------------------------------------------------------

CONTRACT_KIND_REGISTRY: dict[ContractKind, type[ContractBase]] = {
    ContractKind.task: TaskContract,
}
"""Maps a ``ContractKind`` to its Pydantic domain model class.

The repository uses this to deserialize the JSONB ``document`` column to
the right class. Adding a new contract type = new model + new enum value +
register here. No table migration.
"""


def deserialize_contract(contract_kind: ContractKind, document: dict[str, Any]) -> ContractBase:
    """Deserialize a JSONB document to the right ``ContractBase`` subclass.

    Raises ``ValueError`` if the contract kind is not registered.
    """
    cls = CONTRACT_KIND_REGISTRY.get(contract_kind)
    if cls is None:
        raise ValueError(f"Unknown contract_kind: {contract_kind!r}")
    return cls.model_validate(document)
