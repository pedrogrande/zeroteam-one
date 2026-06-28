# Task contract data model

***

## Design Philosophy

The contract is structured as a **root aggregate** (`TaskContract`) with 15+ subordinate entities. Many fields are polymorphic (e.g., `Actor` covers humans, agents, organisations, and protocols), so the model uses a **discriminated union / type field pattern** throughout. All identity fields are UUIDs; all timestamps are ISO 8601.

***

## Entity Relationship Overview

The core relationships:

- `TaskContract` **1 → 1** `OriginIntent`, `TaskSpec`, `Schedule`, `Priority`, `ExecutionState`
- `TaskContract` **1 → many** `ActorRole`, `AcceptanceCriterion`, `Artefact`, `Input`, `Dependency`, `Risk`, `AuditEvent`, `NotificationRule`, `ReputationEffect`, `Ruleset`
- `ActorRole` references a shared `Actor` entity (normalised — one actor can hold many roles across many contracts)
- `AcceptanceCriterion` **1 → 1** `VerificationRecord`
- `Artefact` **1 → 1** `VerificationRecord`
- `TaskContract` **self-referencing** via parent/child lineage and prior version references

***

## Core Schemas

### `TaskContract` (Root)

The top-level document/record that anchors all other entities.

```json
{
  "contract_id": "uuid",
  "version": "semver string",
  "created_at": "ISO 8601",
  "governing_protocol_version": "string",
  "jurisdiction": {
    "type": "enum: legal | organisational | decentralised",
    "reference": "string"
  },
  "contract_type": "enum: one-off | recurring | ad-hoc",
  "status": "enum: draft | open | claimed | in-progress | paused | under-review | disputed | completed | cancelled | expired",
  "origin": "OriginIntent (embedded)",
  "specification": "TaskSpec (embedded)",
  "value_declaration": "ValueDeclaration (embedded)",
  "schedule": "Schedule (embedded)",
  "priority": "Priority (embedded)",
  "execution_state": "ExecutionState (embedded)",
  "actor_roles": ["ActorRole"],
  "capability_requirements": "CapabilityRequirements (embedded)",
  "inputs": ["Input"],
  "dependencies": ["Dependency"],
  "risks": ["Risk"],
  "quality": "QualitySpec (embedded)",
  "governance": "Governance (embedded)",
  "compensation": "CompensationSpec (embedded)",
  "verification": "VerificationSpec (embedded)",
  "notifications": ["NotificationRule"],
  "learning": "LearningRecord (embedded)",
  "audit_trail": ["AuditEvent"],
  "lineage": "ContractLineage (embedded)",
  "signatures": ["Commitment"]
}
```

***

### `Actor` (Shared / Normalised)

Referenced by role records — not embedded directly.

```json
{
  "actor_id": "uuid",
  "actor_type": "enum: human | agent | organisation | protocol",
  "display_name": "string",
  "trust_score": "float | null",
  "reputation_score": "float | null",
  "public_key": "string | null"
}
```

### `ActorRole`

Maps an actor to a contract with a role designation.

```json
{
  "role_id": "uuid",
  "contract_id": "uuid (FK)",
  "actor_id": "uuid (FK)",
  "role_type": "enum: requester | performer | owner | reviewer | verifier | stakeholder | witness",
  "authority_level": "string | null",
  "claim_mechanism": "enum: assigned | self-selected | auctioned | delegated | null",
  "claim_timestamp": "ISO 8601 | null",
  "delegability_permitted": "boolean",
  "review_type": "enum: quality | compliance | safety | domain-expertise | null",
  "review_structure": "enum: sequential | parallel | null",
  "input_rights": "enum: none | advisory | approval | null",
  "notification_entitlements": ["string"]
}
```

***

### `TaskSpec`

Covers sections II.1–II.5 of the outline.

```json
{
  "title": "string",
  "description": "string",
  "task_type": "string",
  "functional_domain": "string",
  "value_stream_category": "string",
  "tags": ["string"],
  "scope": {
    "inclusions": ["string"],
    "exclusions": ["string"],
    "assumptions": ["string"],
    "constraints": ["string"]
  },
  "acceptance_criteria": ["AcceptanceCriterion"],
  "min_quality_threshold": "string",
  "target_quality_standard": "string",
  "expected_outputs": {
    "artefacts": ["Artefact"],
    "state_changes": ["string"],
    "decisions_to_record": ["string"],
    "communications_to_send": ["string"],
    "handoff": {
      "recipient_actor_id": "uuid",
      "format": "string",
      "timing": "string"
    }
  },
  "effort": {
    "complexity_rating": "enum: trivial | low | medium | high | extreme",
    "cognitive_load_type": "enum: generative | analytical | procedural | communicative",
    "estimated_effort_minutes": "integer",
    "estimated_lead_time_minutes": "integer",
    "max_permitted_duration_minutes": "integer",
    "flow_potential_rating": "enum: low | medium | high",
    "focus_mode_required": "boolean"
  }
}
```

***

### `AcceptanceCriterion`

Each criterion is independently verifiable.

```json
{
  "criterion_id": "uuid",
  "contract_id": "uuid (FK)",
  "sequence": "integer",
  "description": "string",
  "verification_method": "string",
  "verifier_actor_id": "uuid (FK)",
  "verification_record": "VerificationRecord | null"
}
```

### `Artefact`

Represents any deliverable produced by the task.

```json
{
  "artefact_id": "uuid",
  "contract_id": "uuid (FK)",
  "artefact_type": "string",
  "format": "string",
  "destination": "string",
  "submission_timestamp": "ISO 8601 | null",
  "storage_reference": "string | null",
  "immutable_hash": "string | null",
  "verification_record": "VerificationRecord | null"
}
```

### `VerificationRecord`

Shared by both `AcceptanceCriterion` and `Artefact`.

```json
{
  "verification_id": "uuid",
  "verifier_actor_id": "uuid (FK)",
  "verified_at": "ISO 8601",
  "method": "string",
  "result": "enum: pass | fail | pending",
  "independence_required": "boolean",
  "quorum_required": "integer | null",
  "proof_type": "string",
  "proof_storage_reference": "string",
  "proof_immutable": "boolean"
}
```

***

### `ValueDeclaration`

Covers section III — multi-party value accounting.

```json
{
  "to_requester": {
    "value_type": "enum: financial | operational | strategic | relational | informational",
    "estimated_value_quantum": "string",
    "realisation_timeframe": "string",
    "decay_profile": "enum: none | linear | exponential | cliff-edge"
  },
  "to_performer": {
    "compensation_preview": "string",
    "skill_development_opportunity": "boolean",
    "knowledge_gain": "string",
    "portfolio_contribution": "boolean"
  },
  "to_organisation": {
    "strategic_alignment_score": "float",
    "contribution_to_mission": "string",
    "leverage_score": "float",
    "waste_classification": "enum: value-creating | enabling | protecting | discovering"
  },
  "to_broader_stakeholders": {
    "third_party_beneficiaries": ["string"],
    "community_value": "string",
    "negative_externalities": ["string"]
  },
  "value_verification": {
    "assessment_method": "string",
    "realisation_timeline": "string",
    "accountable_assessor_actor_id": "uuid"
  }
}
```

***

### `Input`

Represents a required input or dependency resource.

```json
{
  "input_id": "uuid",
  "contract_id": "uuid (FK)",
  "description": "string",
  "input_type": "enum: data | decision | artefact | access | briefing",
  "provided_by_actor_id": "uuid (FK)",
  "required_before_start": "boolean",
  "availability_status": "enum: available | pending | blocked"
}
```

### `Dependency`

Task-to-task dependency record.

```json
{
  "dependency_id": "uuid",
  "contract_id": "uuid (FK)",
  "depends_on_contract_id": "uuid (FK) | null",
  "blocks_contract_id": "uuid (FK) | null",
  "dependency_type": "enum: hard | soft | informational",
  "resolution_status": "enum: resolved | unresolved | waived"
}
```

***

### `Schedule`

Covers sections VII and VIII.

```json
{
  "earliest_start": "ISO 8601 | null",
  "due_date": "ISO 8601",
  "deadline_type": "enum: hard | soft",
  "expiry_condition": "string",
  "time_sensitivity": "string",
  "time_sensitivity_ruleset_version": "string",
  "recurrence": {
    "recurrence_type": "enum: once | scheduled | ad-hoc",
    "cron_expression": "string | null",
    "instance_number": "integer | null",
    "parent_recurrence_contract_id": "uuid | null"
  },
  "trigger_condition": "string | null",
  "pre_conditions_checklist": ["string"]
}
```

### `Priority`

```json
{
  "priority_classification": "enum: must-have | should-have | could-have | wont-have",
  "priority_score": "float",
  "ruleset_version": "string",
  "last_reviewed_at": "ISO 8601",
  "allocation": {
    "allocation_type": "enum: assigned | claimable | auctioned | delegated | automated",
    "claim_window_open": "ISO 8601 | null",
    "claim_window_close": "ISO 8601 | null",
    "max_concurrent_claims": "integer",
    "allocation_authority_actor_id": "uuid | null"
  }
}
```

***

### `Risk`

One record per identified risk.

```json
{
  "risk_id": "uuid",
  "contract_id": "uuid (FK)",
  "risk_type": "enum: non-completion | execution-quality | safety | dependency | data-security | compliance | reputational",
  "description": "string",
  "likelihood": "enum: low | medium | high",
  "consequence_severity": "enum: low | medium | high | critical",
  "risk_tier": "integer (1–4)",
  "mitigation_strategy": "string",
  "owner_actor_id": "uuid (FK)"
}
```

***

### `CompensationSpec`

Covers sections XII.1–XII.3.

```json
{
  "base_compensation": {
    "compensation_type": "enum: monetary | token | credit | reputational | in-kind",
    "amount_or_formula": "string",
    "payment_trigger": "enum: on-completion | on-verification | on-value-realisation",
    "payment_mechanism": "string"
  },
  "incentives": [
    {
      "incentive_type": "enum: bonus | penalty",
      "condition": "string",
      "value": "string",
      "ruleset_version": "string"
    }
  ],
  "reputation_effects": {
    "on_success": "string",
    "on_failure": "string",
    "reputation_system_reference": "string"
  }
}
```

***

### `ExecutionState`

Covers section XIII — lifecycle state machine.

```json
{
  "current_state": "enum: draft | open | claimed | in-progress | paused | under-review | disputed | completed | cancelled | expired",
  "valid_transitions": [
    {
      "from": "string",
      "to": "string",
      "trigger": "string",
      "authority_actor_id": "uuid"
    }
  ],
  "pause_conditions": ["string"],
  "cancellation_conditions": ["string"],
  "cancellation_consequences": "string",
  "cancellation_authority_actor_id": "uuid | null",
  "dispute": {
    "trigger_conditions": ["string"],
    "resolution_mechanism": "enum: human-arbitration | protocol-rule | dao-vote",
    "resolution_timeline": "string",
    "escalation_path": "string"
  }
}
```

***

### `AuditEvent`

Immutable append-only log entries.

```json
{
  "event_id": "uuid",
  "contract_id": "uuid (FK)",
  "event_type": "enum: state-transition | edit | assignment | claim | verification | cancellation | dispute",
  "actor_id": "uuid (FK)",
  "timestamp": "ISO 8601",
  "reason": "string | null",
  "before_snapshot": "object | null",
  "after_snapshot": "object | null",
  "immutable_hash": "string"
}
```

***

### `ContractLineage`

Self-referencing for decomposition and versioning.

```json
{
  "parent_contract_id": "uuid | null",
  "child_contract_ids": ["uuid"],
  "prior_version_ids": ["uuid"]
}
```

***

### `LearningRecord`

Covers section XVI — post-completion capture.

```json
{
  "expected_outcome": "string",
  "actual_outcome": "string | null",
  "outcome_variance": "string | null",
  "task_validated": "boolean | null",
  "retrospective": {
    "trigger_conditions": ["string"],
    "format_reference": "string",
    "notes": "string | null",
    "conducted_by_actor_id": "uuid | null",
    "conducted_at": "ISO 8601 | null"
  },
  "knowledge_outputs": [
    {
      "output_type": "enum: template | decision-record | process-documentation | insight",
      "knowledge_base_reference": "string",
      "reusability": "enum: single-use | team | organisation | public",
      "guidelines_version": "string"
    }
  ],
  "capability_development": {
    "skill_development_flag": "boolean",
    "supervising_actor_id": "uuid | null",
    "competency_evidence_generated": "boolean"
  }
}
```

***

### `Commitment` (Signatures)

One record per signing party.

```json
{
  "commitment_id": "uuid",
  "contract_id": "uuid (FK)",
  "actor_id": "uuid (FK)",
  "commitment_type": "enum: requester | performer | reviewer | verifier | witness",
  "cryptographic_signature": "string",
  "signed_at": "ISO 8601",
  "declaration": "string",
  "witness_type": "enum: organisational | decentralised | notarial | null"
}
```

***

### `Ruleset`

Referenced throughout the contract for governance versioning.

```json
{
  "ruleset_id": "uuid",
  "ruleset_name": "string",
  "version": "semver string",
  "domain": "string"
}
```

***

## Relationship Map

| Relationship | Cardinality | FK Direction |
|---|---|---|
| `TaskContract` → `Actor` (via `ActorRole`)   | M:N | `ActorRole.contract_id`, `ActorRole.actor_id` |
| `TaskContract` → `AcceptanceCriterion`   | 1:N | `AcceptanceCriterion.contract_id` |
| `TaskContract` → `Artefact`   | 1:N | `Artefact.contract_id` |
| `AcceptanceCriterion` → `VerificationRecord`   | 1:1 | `VerificationRecord.criterion_id` |
| `Artefact` → `VerificationRecord`   | 1:1 | `VerificationRecord.artefact_id` |
| `TaskContract` → `Input`   | 1:N | `Input.contract_id` |
| `TaskContract` → `Dependency`   | 1:N | `Dependency.contract_id` |
| `Dependency` → `TaskContract` (self-ref)   | M:N | `Dependency.depends_on_contract_id` |
| `TaskContract` → `Risk`   | 1:N | `Risk.contract_id` |
| `TaskContract` → `AuditEvent`   | 1:N | `AuditEvent.contract_id` |
| `TaskContract` → `TaskContract` (parent/child)   | 1:N | `ContractLineage.parent_contract_id` |
| `TaskContract` → `Ruleset`   | M:N | join table `ContractRuleset` |
| `TaskContract` → `Commitment`   | 1:N | `Commitment.contract_id` |

***

## Key Design Decisions

- **Actor is normalised** — a single `Actor` table serves all role types (human, agent, org, protocol), discriminated by `actor_type`, avoiding duplication across requester/performer/reviewer fields.
- **VerificationRecord is shared** — both `AcceptanceCriterion` and `Artefact` link to a `VerificationRecord`, keeping verification logic DRY.
- **State machine externalised** — `ExecutionState.valid_transitions` encodes the allowed state graph, making it inspectable and auditable rather than hard-coded.
- **AuditEvent is append-only** — before/after snapshots plus a hash chain supports the immutability requirement in section XVII.
- **ValueDeclaration is embedded** — multi-perspective value (requester, performer, org, society) is a document-style embedded object rather than separate tables, since it's always queried as a whole.
- **Ruleset versioning** — every sub-section that references a ruleset version maps to the shared `Ruleset` entity via a join table, enabling governance traceability across contract versions.
