<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Write the new workflow contract specification to include your recommendations

I now have everything I need: the full CAWDP v2.3 phase and field structure from `paste.txt`, the existing 13-section workflow contract field history, the new human-centred approach developed in the conversation history, and the implementation status from yesterday. Here is the complete new specification.

***

# Workflow Contract Specification v2.0

## CAWDP Contract — Full Field Specification

**Document ID:** WCS-SPEC-002
**Version:** 2.0
**Date:** 3 June 2026
**Status:** `Canonical — Supersedes WCS-SPEC-001`
**Source Authority:** CAWDP v2.3, Implementation Status Report (2 June 2026), Human-Centred Approach Integration

***

## Design Principles

This specification reflects three sources of authority:[^1]

1. **CAWDP v2.3 phase sequence** — the contract's sections map directly to the Discovery diamond (P0–P2) and are structured so that each section can only be meaningfully completed after the previous section's thinking is done
2. **Human-centred workflow definition** — a workflow exists in response to a human need and creates value for stakeholders; the contract must capture that origin before asking about process
3. **Existing schema reality** — the SurrealDB schema already defines the `workflow_contract` table with 13 sections and all Stage 1 + Stage 2 fields; this specification defines the *canonical content* of those fields, not new schema

***

## Stage 1 Sections

Stage 1 answers: *What is this workflow, why does it exist, who does it affect, and what must be true for it to succeed?*

Stage 1 corresponds to CAWDP P0 (Purpose \& Vision) and the first half of P1 (Output Specification — recipient/value anchoring). It must be completed before Stage 2 is unlocked.

***

### Section 1 — Identity

*What this workflow IS and WHERE it sits.*


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `identity.name` | Workflow Name | `string` | Short verb-noun format. e.g. "Process Invoice", "Onboard New Client" | All | Shallow |
| `identity.version` | Version | `string` | Semantic version. Use `1.0` if newly defined | All | Shallow |
| `identity.workflow_class` | Workflow Class | `enum` | Extractor / Measurer / Assessor / Generator / Aggregator — from CAWDP v2.3 Class × Orientation taxonomy | 3–5 | Shallow |
| `identity.orientation` | Orientation | `enum` | Possibility-Oriented / Bridge-Oriented / Constraint-Oriented | 3–5 | Shallow |
| `identity.design_shape` | Design Shape | `enum` | Discovery / Document Only / Mapping / Automation / Facilitated / Iterative / Full — from design shape triage | All | Shallow |
| `identity.rigour_level` | Rigour Level | `int` | 1–5, set by triage | All | Shallow |
| `identity.is_new` | Is This a New Workflow? | `boolean` | True = new, False = redesign of existing | All | Shallow |
| `identity.existing_documentation` | Existing Documentation | `string?` | URL or reference if workflow is currently documented somewhere | Optional | Shallow |
| `identity.parent_workflow` | Parent Workflow | `record<workflow>?` | If this workflow is a component of a larger workflow, reference it here | Optional | Shallow |


***

### Section 2 — Human Origin

*Why this workflow exists — traced to a human need, not an operational function.*

This section is new in v2.0. It corresponds to the CAWDP v2.3 P0 identity questions re-anchored in human-centred design. No other section can be meaningfully completed before this one.[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `human_origin.human_goal` | Human Goal | `string` | The underlying human need or desire this workflow serves. Trace back beyond the operational function. e.g. "A business owner needs to know their obligations are met without hiring a specialist" not "Process tax filings" | All | Deep |
| `human_origin.problem_solved` | Problem Solved | `string` | What gap between current reality and desired reality does a successful outcome close? Describe specifically | All | Deep |
| `human_origin.current_state_description` | Current State | `string` | What is the state of the world before this workflow runs? If redesign: what is the state of the existing workflow? | All | Medium |
| `human_origin.desired_state_description` | Desired State | `string` | What state must exist when this workflow completes successfully? How would each stakeholder group recognise that the transformation occurred? | All | Deep |
| `human_origin.trigger` | Trigger | `string` | What event, signal, condition, or schedule starts this workflow? | All | Shallow |
| `human_origin.trigger_type` | Trigger Type | `enum` | Event / Time-based schedule / Manual initiation / Completion of another workflow / External signal / Combination | All | Shallow |
| `human_origin.multiple_start_points` | Multiple Valid Starting Points | `boolean` | True if there are different valid starting conditions that determine different paths | Optional | Shallow |
| `human_origin.start_point_detail` | Starting Point Detail | `string?` | If multiple start points: describe each and the condition that determines which applies | Optional | Medium |


***

### Section 3 — Stakeholder Map

*Who exists in relation to this workflow — directly and indirectly.*

This section is new in v2.0. It must be completed before Purpose \& Value, because value statements without a named recipient are meaningless. This section structures the stakeholder map that CAWDP v2.3 requires at P0 but does not yet make explicit.[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `stakeholders.direct_actors` | Direct Actors | `array<object>` | The people and roles who perform steps in this workflow. Each entry: `{ role, description, count_estimate }` | All | Medium |
| `stakeholders.direct_beneficiaries` | Direct Beneficiaries | `array<object>` | Who directly receives the output of a successful run. Each entry: `{ group, what_they_receive, how_they_recognise_success }` | All | Medium |
| `stakeholders.indirect_stakeholders` | Indirect Stakeholders | `array<object>` | Who is affected by the workflow's outcomes without directly participating. Each entry: `{ group, nature_of_impact, positive_or_negative }` | 3–5 | Medium |
| `stakeholders.governing_parties` | Governing Parties | `array<object>` | Who sets the constraints, rules, or compliance requirements that apply to this workflow. Each entry: `{ party, constraint_type, authority_source }` | 3–5 | Medium |
| `stakeholders.power_asymmetries` | Power Asymmetries | `string?` | Are there actors in this workflow with unequal power or authority? Describe where power dynamics may affect how steps are performed or decisions are made | 4–5 | Deep |
| `stakeholders.trust_risk` | Trust Risk | `string?` | Could this workflow erode trust between any stakeholder groups if performed poorly, inconsistently, or opaquely? Describe the mechanism | 3–5 | Medium |
| `stakeholders.stakeholder_tensions` | Stakeholder Tensions | `array<object>?` | Where do the needs or desired outcomes of different stakeholder groups diverge? Each entry: `{ groups_in_tension, nature_of_conflict, resolution_approach }` | 4–5 | Deep |


***

### Section 4 — Purpose \& Value

*What this workflow produces for whom, and what it is worth.*

Previously "purpose_value". Now explicitly anchored to the stakeholder map from Section 3 — value statements must name a recipient group.[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `purpose_value.purpose_statement` | Purpose Statement | `string` | One to two sentences. Why does this workflow exist? Must trace to a declared human need from Section 2 | All | Deep |
| `purpose_value.value_for_direct_beneficiaries` | Value for Direct Beneficiaries | `string` | What does a successful outcome deliver for each direct beneficiary group named in Section 3? | All | Deep |
| `purpose_value.value_for_organisation` | Value for Organisation | `string` | What does the organisation gain from running this workflow successfully? | All | Medium |
| `purpose_value.cost_of_not_running` | Cost of Not Running | `string` | What is the consequence of this workflow not existing or not being run? For each stakeholder group | 2–5 | Medium |
| `purpose_value.value_distribution` | Value Distribution | `enum` | Even / Uneven — is value distributed approximately evenly across stakeholder groups, or does one group receive disproportionate benefit at another's cost? | 3–5 | Shallow |
| `purpose_value.value_distribution_notes` | Value Distribution Notes | `string?` | If uneven: describe which groups benefit more and which bear more cost without proportionate benefit | 3–5 | Medium |
| `purpose_value.workflow_worth` | Workflow Worth | `enum` | Justified / Marginal / Unjustified — does the value this workflow produces justify its cost in time, resource, and human effort? | 3–5 | Deep |
| `purpose_value.workflow_worth_rationale` | Worth Rationale | `string?` | Required if Marginal or Unjustified: explain the rationale for running this workflow despite the assessment | 3–5 | Deep |


***

### Section 5 — Stakeholder Harm \& Impact

*What could go wrong — for whom.*

This section is new in v2.0. It captures the harm dimension that was previously absent from the workflow contract. It combines the "What Could Go Wrong?" methods with stakeholder specificity. Aligned with CAWDP v2.3's requirement that every failure mode be tied to a specific stakeholder consequence.[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `stakeholder_impact.harm_if_workflow_fails` | Harm if Workflow Fails | `array<object>` | For each stakeholder group: who could be harmed if this workflow fails or produces poor outputs? Each entry: `{ stakeholder_group, harm_description, severity }` where severity is `Low / Medium / High / Critical` | 2–5 | Medium |
| `stakeholder_impact.harm_if_poorly_performed` | Harm if Poorly Performed | `array<object>` | Who could be harmed by inconsistent, opaque, or biased execution — even if the workflow technically completes? Each entry: `{ stakeholder_group, harm_mechanism }` | 3–5 | Medium |
| `stakeholder_impact.indirect_harms` | Indirect Harms | `array<object>?` | Harms that fall on parties not directly involved in the workflow. Each entry: `{ affected_party, harm_description, likelihood }` | 4–5 | Deep |
| `stakeholder_impact.blast_radius` | Blast Radius | `enum` | Isolated / Team / Organisation / External stakeholders — the scope of harm if this workflow fails or is performed incorrectly | 2–5 | Shallow |
| `stakeholder_impact.unintended_outputs` | Unintended Outputs | `string?` | Does this workflow produce side effects — positive or negative — beyond its stated purpose? | 3–5 | Medium |
| `stakeholder_impact.emotional_labour` | Emotional Labour | `boolean` | Does any step require emotional labour from actors — managing distress, delivering difficult news, handling conflict? | 3–5 | Shallow |
| `stakeholder_impact.emotional_labour_detail` | Emotional Labour Detail | `string?` | If yes: describe which steps, what kind of emotional labour, and whether support structures exist | 3–5 | Medium |


***

### Section 6 — Completion Criteria

*What done looks like — for each stakeholder group.*

Previously "completion_criteria" and "completion_triggers" (two separate sections, now merged).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `completion.definition_of_done` | Definition of Done | `string` | The conditions that must ALL be true for this workflow to be considered complete | All | Deep |
| `completion.stakeholder_recognition` | Stakeholder Recognition | `array<object>` | How would each stakeholder group recognise that the transformation occurred? Each entry: `{ stakeholder_group, recognition_criteria }` | 3–5 | Medium |
| `completion.artefacts_produced` | Artefacts Produced | `array<string>` | List of documents, records, decisions, communications, or outputs the completed workflow produces | All | Medium |
| `completion.completion_triggers` | Completion Triggers | `array<string>` | Actions or downstream workflows triggered by successful completion | Optional | Shallow |
| `completion.partial_completion_value` | Partial Completion Value | `enum` | Better than before / Neutral / Worse than before — does partial completion leave the system in a better, neutral, or worse state than before it began? | 2–5 | Medium |
| `completion.partial_completion_notes` | Partial Completion Notes | `string?` | Required if Worse than before: describe what state partial completion leaves and what remediation is required | 2–5 | Medium |


***

### Section 7 — Failure Modes \& Abortion Triggers

*What can go wrong — at workflow and step level.*

Previously "failure_modes" and "abortion_triggers" (two separate sections, now merged with stakeholder harm linkage).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `failure.known_failure_modes` | Known Failure Modes | `array<object>` | Each entry: `{ failure_mode, likely_step, stakeholder_groups_affected, blast_radius, reversible }` | 2–5 | Deep |
| `failure.exception_paths` | Exception Paths | `array<object>?` | Defined exception-handling paths for known failure modes. Each entry: `{ failure_mode, exception_path, trigger }` | 3–5 | Deep |
| `failure.retry_policy` | Retry Policy | `string?` | Can failed steps be retried before the workflow is considered failed? How many retries and under what conditions? | 3–5 | Shallow |
| `failure.failure_consequence` | Failure Consequence | `string` | What happens if the workflow fails partway through — rollback, notification, handoff, or nothing? | 2–5 | Medium |
| `failure.abortion_triggers` | Abortion Triggers | `array<string>` | Events or conditions that legitimately end this workflow before completion (not failure — authorised stop) | 2–5 | Medium |
| `failure.irreversible_steps` | Irreversible Steps | `array<object>?` | Steps that cannot be undone. Each entry: `{ step_name, why_irreversible, safeguards }` | 3–5 | Medium |
| `failure.safety_risks` | Safety Risks | `array<object>?` | Steps that pose physical, psychological, legal, or reputational risk to actors or affected parties. Each entry: `{ step, risk_type, risk_description, mitigation }` | 3–5 | Deep |


***

### Section 8 — Risk Profile

*Systemic risk — at the workflow level, not just the step level.*

Previously "risk_profile" (retained and expanded).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `risk_profile.overall_risk_level` | Overall Risk Level | `enum` | Low / Medium / High / Critical | 2–5 | Shallow |
| `risk_profile.risk_rationale` | Risk Rationale | `string` | Why this risk level was assigned | 2–5 | Medium |
| `risk_profile.key_risks` | Key Risks | `array<object>` | Each entry: `{ risk, likelihood, impact, stakeholders_affected, mitigation }` | 3–5 | Deep |
| `risk_profile.actor_capability_risk` | Actor Capability Risk | `string?` | Does running this workflow build or degrade the capability of the actors performing it? Describe over time | 3–5 | Medium |
| `risk_profile.context_stability` | Context Stability | `enum` | Stable / Likely to change / Unstable — stability of the environment in which this workflow operates | 2–5 | Shallow |
| `risk_profile.context_change_notes` | Context Change Notes | `string?` | If Likely to change or Unstable: what is changing and how should the workflow adapt? | 3–5 | Medium |


***

### Section 9 — Non-Completion Costs

*What it costs to leave this workflow unfinished or unrun.*

Previously "non_completion_costs" (retained). Linked to Section 5 (stakeholder harm) and Section 6 (partial completion value).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `non_completion.cost_per_stakeholder` | Cost Per Stakeholder Group | `array<object>` | For each stakeholder group: the consequence of non-completion. Each entry: `{ stakeholder_group, consequence, severity }` | 2–5 | Medium |
| `non_completion.cost_to_organisation` | Cost to Organisation | `string` | What does the organisation lose if this workflow is never completed or permanently abandoned? | 2–5 | Medium |
| `non_completion.urgency` | Urgency | `enum` | Immediate / Near-term / Medium-term / No deadline — is there a time constraint on completion? | All | Shallow |
| `non_completion.deadline` | Deadline | `date?` | Hard deadline if applicable | Optional | Shallow |
| `non_completion.deadline_consequence` | Deadline Consequence | `string?` | What happens if the deadline is missed? | Optional | Medium |


***

### Section 10 — Visibility \& Governance

*Who can see what, and who is accountable.*

Previously "visibility_governance" (retained and expanded with stakeholder transparency dimension).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `visibility.accountable_role` | Accountable Role | `string` | The role responsible for the workflow as a whole if something goes wrong — may differ from the performers | All | Shallow |
| `visibility.audit_trail_required` | Audit Trail Required | `boolean` | Is a record of actions, actors, and timestamps required? | 2–5 | Shallow |
| `visibility.audit_trail_detail` | Audit Trail Detail | `string?` | If yes: what must be recorded — what actions, which actors, what decisions? | 2–5 | Medium |
| `visibility.progress_visibility` | Progress Visibility | `string` | Who can see the current state or progress of this workflow in real time? | 3–5 | Medium |
| `visibility.role_restricted_information` | Role-Restricted Information | `boolean` | Are there steps or information within this workflow restricted by role? | 3–5 | Shallow |
| `visibility.restriction_detail` | Restriction Detail | `string?` | If yes: what is hidden and from whom? | 3–5 | Medium |
| `visibility.notifications` | Notifications | `array<object>?` | What signals or communications does this workflow produce as it progresses? Each entry: `{ trigger, recipient_group, message_type }` | 3–5 | Medium |
| `visibility.compliance_constraints` | Compliance Constraints | `array<string>?` | Organisational, legal, or regulatory constraints that apply to this workflow | 3–5 | Medium |


***

### Section 11 — Relationships \& Dependencies

*How this workflow connects to others.*

Previously "relationships" (expanded). Corresponds to the CAWDP v2.3 P6 requirement to check the manifest and declare dependency contracts.[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `relationships.is_component_of` | Is Component Of | `record<workflow>?` | If this is a sub-workflow of a larger process, reference it | Optional | Shallow |
| `relationships.depends_on` | Depends On | `array<object>?` | Workflows that must reach a certain state before this one can proceed. Each entry: `{ workflow, required_state, criticality }` | 3–5 | Medium |
| `relationships.triggers_on_completion` | Triggers on Completion | `array<object>?` | Workflows triggered by completion of this one. Each entry: `{ workflow, trigger_condition }` | Optional | Shallow |
| `relationships.shared_resources` | Shared Resources | `array<object>?` | Resources, actors, or tools shared with other workflows that may cause contention. Each entry: `{ resource, competing_workflows, contention_risk }` | 3–5 | Medium |
| `relationships.can_run_concurrently` | Can Run Concurrently | `boolean` | Can multiple instances of this workflow run simultaneously? | 2–5 | Shallow |
| `relationships.concurrent_conflict_detail` | Concurrent Conflict Detail | `string?` | If yes: what conflicts or resource contention may arise from simultaneous instances? | 2–5 | Medium |
| `relationships.consumes_from_manifest` | Consumes from Manifest | `array<record<output_specification>>?` | Outputs from other workflow contracts that this workflow consumes as inputs — registered against those contracts | 3–5 | Medium |
| `relationships.produces_for_manifest` | Produces for Manifest | `array<record<output_specification>>?` | Outputs of this workflow that are registered in the shared manifest and may be consumed by others | 3–5 | Medium |


***

### Section 12 — Assumptions \& Open Questions

*What we believe to be true, and what we don't yet know.*

Previously "assumptions" (retained and expanded). Corresponds to CAWDP v2.3 epistemic metadata requirements (CC-3).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `assumptions.spec_assumptions` | Specification Assumptions | `array<object>` | What the specifier assumed to be true in completing this contract. Each entry: `{ assumption, confidence, what_changes_if_wrong }` | 3–5 | Deep |
| `assumptions.outdated_logic_risk` | Outdated Logic Risk | `boolean` | Does this workflow encode assumptions that were once valid but may no longer be true? | 3–5 | Shallow |
| `assumptions.outdated_logic_detail` | Outdated Logic Detail | `string?` | If yes: which assumptions and what triggered the flag | 3–5 | Medium |
| `assumptions.open_questions` | Open Questions | `array<string>?` | Questions that remain unresolved that could materially affect this workflow's design | 3–5 | Medium |
| `assumptions.confidence_level` | Specification Confidence | `enum` | High / Medium / Low — overall specifier confidence in the accuracy of this contract | 3–5 | Shallow |


***

### Section 13 — Knowledge \& Learning

*What completing this workflow generates and what doing it well requires.*

Previously "knowledge_learning" (retained and expanded with actor capability dimension).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `knowledge.knowledge_generated` | Knowledge Generated | `string` | What does completing this workflow teach — about time, quality, exceptions, or actor experience? | 3–5 | Medium |
| `knowledge.reusable_assets` | Reusable Knowledge Assets | `array<string>?` | Templates, decisions, discoveries, or how-to guides produced by this workflow that are reusable | 3–5 | Shallow |
| `knowledge.actor_capability_effect` | Actor Capability Effect | `enum` | Builds / Neutral / Degrades — does performing this workflow build or degrade the capability of the actor? | 3–5 | Medium |
| `knowledge.actor_capability_notes` | Actor Capability Notes | `string?` | Explain the mechanism — what is built or degraded and over what timeframe | 3–5 | Medium |
| `knowledge.retrospective_questions` | Retrospective Questions | `array<string>?` | Key questions to ask after completion to improve future runs | Optional | Shallow |


***

### Section 14 — Time \& Recurrence

*When and how often this workflow runs.*

Previously "time_recurrence" (retained and expanded).[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `time.expected_duration` | Expected Duration | `string` | Estimated elapsed time from trigger to completion | All | Shallow |
| `time.recurrence` | Recurrence | `enum` | Once / Scheduled / Ad hoc | All | Shallow |
| `time.recurrence_pattern` | Recurrence Pattern | `string?` | If scheduled: the recurrence pattern (e.g. daily, weekly, end of month) | Optional | Shallow |
| `time.can_pause_resume` | Can Pause and Resume | `boolean` | Can this workflow be paused and resumed without restarting? | 2–5 | Shallow |
| `time.pause_conditions` | Pause Conditions | `string?` | If yes: what causes a pause and what allows resumption? | 2–5 | Medium |
| `time.external_wait_steps` | External Wait Steps | `array<string>?` | Steps that involve waiting for external events, decisions, or parties | 3–5 | Medium |


***

## Stage 2 Sections

Stage 2 answers: *How is this workflow structured, who does what, and what does each step require?* It corresponds to CAWDP P1 (Output Specification — schema/dependency detail), P2 (Backcasting — input tracing), and P3 (Task Decomposition — structural). Stage 2 is unlocked only after Stage 1 gate approval and, for Practitioner and Architect tiers, after the Backcasting Output is accepted.

***

### Section 15 — CAWDP Phase Artefacts

*The formal CAWDP design artefacts, linked by reference.*


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `backcasting.backcasting_artefact` | Backcasting Output | `record<backcasting_output>?` | Reference to the accepted Backcasting Output artefact for this contract | 3–5 | Shallow |
| `backcasting.input_specification_refs` | Input Specification References | `array<record<input_specification>>?` | References to approved Input Specification records for this contract | 3–5 | Shallow |
| `backcasting.p0_identity_answers` | P0 Identity Answers | `object?` | The five CAWDP v2.3 identity questions answered: `{ Q1_what_it_does, Q2_orientation, Q3_violation, Q4_failed_run, Q5_hardest_moment }` | 4–5 | Deep |
| `backcasting.target_state_characteristics` | Target State Characteristics | `array<object>?` | The four dimensions from P0 (Workflow, Specification, Human, Ecosystem) with 5+ characteristics each. Each entry: `{ dimension, characteristic, testable_criterion }` | 5 | Deep |


***

### Section 16 — Task \& Step Structure

*The decomposed work — what happens inside this workflow.*

Corresponds to CAWDP P3. This section is the primary Stage 2 content for most contracts.


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `structure.steps` | Steps | `array<object>` | Ordered list of steps. Each entry: `{ step_id, name, description, cognitive_type, initiation_mode, actor_type, mandatory, inputs_required, outputs_produced, failure_mode, stakeholders_affected, blast_radius_if_fails, reversible }` | 3–5 | Deep |
| `structure.parallel_steps` | Parallel Steps | `array<object>?` | Steps that run simultaneously. Each entry: `{ step_ids, dependency_between_them }` | 3–5 | Medium |
| `structure.loops` | Loops | `array<object>?` | Steps that repeat. Each entry: `{ step_id, exit_condition }` | 3–5 | Medium |
| `structure.optional_steps` | Optional Steps | `array<object>?` | Steps that may be skipped. Each entry: `{ step_id, skip_condition }` | 3–5 | Medium |
| `structure.paths` | Multiple Paths | `array<object>?` | Distinct paths through the workflow. Each entry: `{ path_id, description, determining_condition, steps }` | 3–5 | Deep |
| `structure.sub_workflows` | Sub-Workflows | `array<object>?` | Workflows invoked as components. Each entry: `{ step_id, sub_workflow_ref, invocation_condition }` | 3–5 | Shallow |


***

### Section 17 — Actor Experience

*What it is like to perform this workflow — for each actor.*

This section is new in v2.0. Corresponds to the P7 "Actor Experience" extension recommended in the new approach analysis.[^1]


| Field ID | Field Name | Type | Description | Mandatory (Rigour) | Production Method |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `actor_experience.experience_by_role` | Experience by Role | `array<object>` | For each actor role: what is the likely experience of performing this role? Each entry: `{ role, experience_description, effort_level, typical_challenges }` | 3–5 | Deep |
| `actor_experience.sustainabilty` | Sustainability Assessment | `enum` | Sustainable / Marginal / Unsustainable — is this workflow sustainable at expected volume and frequency for the actors performing it? | 3–5 | Medium |
| `actor_experience.friction_reduction` | Friction Reduction Opportunities | `array<string>?` | What could reduce friction for actors without compromising quality? | 4–5 | Medium |
| `actor_experience.capability_build_plan` | Capability Build Plan | `string?` | If actor capability degrades (from Section 13): what is the mitigation plan? | 4–5 | Deep |


***

### Section 18 — Approval Records

*Who reviewed and approved this contract.*

This section is managed by the system and cannot be edited directly. It is populated by the API on status transitions.


| Field ID | Field Name | Type | Description | System Managed |
| :-- | :-- | :-- | :-- | :-- |
| `approvals.stage_1_approver` | Stage 1 Approver | `string` | Identity of the actor who approved Stage 1 | Yes |
| `approvals.stage_1_approved_at` | Stage 1 Approved At | `datetime` | Timestamp of Stage 1 approval | Yes |
| `approvals.stage_1_conditions` | Stage 1 Conditions | `string?` | Any conditions attached to Stage 1 approval | Yes |
| `approvals.stage_2_approver` | Stage 2 Approver | `string` | Identity of the actor who approved Stage 2 | Yes |
| `approvals.stage_2_approved_at` | Stage 2 Approved At | `datetime` | Timestamp of Stage 2 approval | Yes |
| `approvals.stage_2_conditions` | Stage 2 Conditions | `string?` | Any conditions attached to Stage 2 approval | Yes |


***

## Contract-Level Metadata

System-managed fields present on every `workflow_contract` record.


| Field | Type | Description |
| :-- | :-- | :-- |
| `status` | `enum` | Draft / Stage 1 Review / Stage 1 Approved / Stage 2 Review / Approved / Superseded |
| `rigour_level` | `int` | 1–5, set at creation from triage |
| `created_at` | `datetime` | Timestamp |
| `updated_at` | `datetime` | Last modified |
| `workflow` | `record<workflow>` | Parent workflow record |


***

## Mandatory Field Matrix by Rigour Level

| Section | Fields Mandatory At Rigour 1–2 | Additional Fields Mandatory At Rigour 3 | Additional Fields Mandatory At Rigour 4–5 |
| :-- | :-- | :-- | :-- |
| 1 — Identity | `name`, `version`, `design_shape`, `rigour_level`, `is_new` | + `workflow_class`, `orientation` | No additions |
| 2 — Human Origin | `human_goal`, `problem_solved`, `current_state_description`, `desired_state_description`, `trigger`, `trigger_type` | No additions | + `multiple_start_points` detail if true |
| 3 — Stakeholder Map | `direct_actors`, `direct_beneficiaries` | + `indirect_stakeholders`, `governing_parties`, `trust_risk` | + `power_asymmetries`, `stakeholder_tensions` |
| 4 — Purpose \& Value | `purpose_statement`, `value_for_direct_beneficiaries`, `value_for_organisation` | + `cost_of_not_running`, `value_distribution`, `workflow_worth` | + `value_distribution_notes`, `workflow_worth_rationale` |
| 5 — Stakeholder Harm | `harm_if_workflow_fails`, `blast_radius` | + `harm_if_poorly_performed`, `emotional_labour` | + `indirect_harms`, `unintended_outputs`, `emotional_labour_detail` |
| 6 — Completion | `definition_of_done`, `artefacts_produced` | + `stakeholder_recognition`, `partial_completion_value` | + `partial_completion_notes` if Worse |
| 7 — Failure Modes | None mandatory at 1 | + `known_failure_modes`, `failure_consequence`, `abortion_triggers` | + `exception_paths`, `irreversible_steps`, `safety_risks` |
| 8 — Risk Profile | None mandatory at 1 | + `overall_risk_level`, `risk_rationale`, `context_stability` | + `key_risks`, `actor_capability_risk`, `context_change_notes` |
| 9 — Non-Completion | None mandatory at 1–2 (Quick Start) | + `cost_per_stakeholder`, `cost_to_organisation`, `urgency` | + `deadline_consequence` if deadline set |
| 10 — Visibility | None mandatory at 1 | + `accountable_role`, `audit_trail_required`, `progress_visibility` | + `compliance_constraints`, `role_restricted_information` detail |
| 11 — Relationships | None mandatory | + `depends_on`, `can_run_concurrently`, `consumes_from_manifest` | + `shared_resources`, `produces_for_manifest`, `concurrent_conflict_detail` |
| 12 — Assumptions | None mandatory at 1–2 | + `spec_assumptions`, `open_questions`, `confidence_level` | + `outdated_logic_risk` detail |
| 13 — Knowledge | None mandatory at 1–2 | + `knowledge_generated`, `actor_capability_effect` | + `reusable_assets`, `actor_capability_notes` |
| 14 — Time | `expected_duration`, `recurrence` | + `can_pause_resume`, `recurrence_pattern` | + `external_wait_steps`, `pause_conditions` |
| 15 — CAWDP Artefacts | None | + `backcasting_artefact`, `input_specification_refs` | + `p0_identity_answers` at 4, + `target_state_characteristics` at 5 |
| 16 — Task Structure | None at 1–2 | + `steps` | + `paths`, `sub_workflows` |
| 17 — Actor Experience | None | + `experience_by_role`, `sustainability` | + `friction_reduction`, `capability_build_plan` if degrading |


***

## Section Ordering and Stage Gates

### Stage 1 Gate Prerequisites (sections 1–14)

All Stage 1 mandatory fields across sections 1–14 must be populated for the rigour level before Stage 1 submission is permitted. The output specifications for this contract must also be created and approved.

### Stage 2 Gate Prerequisites (sections 15–17)

For rigour 3–5: `backcasting_artefact` must reference an `Accepted` backcasting output, and at least one `input_specification` must be `Approved`. Sections 15–17 mandatory fields must be populated.

### Why This Order

Sections 1–3 (Identity, Human Origin, Stakeholder Map) must precede sections 4–5 (Purpose \& Value, Stakeholder Harm) because value statements without named recipients are abstract, and harm assessments without a stakeholder map are incomplete. Sections 6–9 (Completion, Failure, Risk, Non-Completion) build on the transformation and harm foundation established in 2–5. Sections 10–14 are governance, relationships, and meta — they can be completed in any order once 1–9 are done. Sections 15–17 are Stage 2 because they require the backcasting process to be complete before they can be filled with genuine content rather than speculation.[^1]
<span style="display:none">[^2]</span>

<div align="center">⁂</div>

[^1]: paste.txt

[^2]: 1737772d-081d-495e-92b3-a19e0dbe2321.md

