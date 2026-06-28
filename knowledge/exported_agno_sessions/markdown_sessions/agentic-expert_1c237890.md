# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `1c237890...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-20T07:29:41 |
| **Runs** | 12 completed / 12 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-20T07:29:41* · `glm-5.1:cloud` · `48290412...`

### Prompt

I have implemented a data schema for CAWDP with SurrealDB in Agno.

```python
"""
CAWDP v2.2 — Consolidated SurrealDB Schema
============================================

Single-database schema with table prefixes (design_, runtime_, monitoring_)
to avoid cross-database record<> reference limitations in SurrealDB.

Applied on startup via apply_schema() — idempotent, gated by env var.
"""

from os import getenv
from textwrap import dedent
from time import sleep

from surrealdb import Surreal

from db.url import (
    SURREALDB_DATABASE,
    SURREALDB_NAMESPACE,
    SURREALDB_URL,
    surrealdb_credentials,
)

# ---------------------------------------------------------------------------
# Consolidated SurrealQL
# ---------------------------------------------------------------------------

SCHEMA_SURQL = dedent("""\
    -- ====================================================================
    -- DESIGN tables — artefacts, workflows, tasks, specifications
    -- ====================================================================

    -- workflows — Top-level container for a CAWDP design run
    DEFINE TABLE design_workflows SCHEMAFULL
      PERMISSIONS
        FOR select WHERE $auth.workflow_id = NONE OR $auth.workflow_id = id
        FOR create, update, delete WHERE $auth.role = 'admin';

    DEFINE FIELD name ON design_workflows TYPE string;
    DEFINE FIELD description ON design_workflows TYPE string;
    DEFINE FIELD version ON design_workflows TYPE string ASSERT $value != NONE;
    DEFINE FIELD mode ON design_workflows TYPE string
      ASSERT $value INSIDE ['DESIGN', 'EVOLVE'];
    DEFINE FIELD current_phase ON design_workflows TYPE string
      ASSERT $value INSIDE ['P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'];
    DEFINE FIELD locked ON design_workflows TYPE bool DEFAULT false;
    DEFINE FIELD parent_workflow ON design_workflows TYPE record<design_workflows> DEFAULT NONE;
    DEFINE FIELD created_at ON design_workflows TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_workflows TYPE datetime DEFAULT time::now();

    -- agent_specifications — One row per agent (renamed from "agents" to avoid Agno collision)
    DEFINE TABLE design_agent_specifications SCHEMAFULL;

    DEFINE FIELD workflow ON design_agent_specifications TYPE record<design_workflows>;
    DEFINE FIELD name ON design_agent_specifications TYPE string;
    DEFINE FIELD agent_class ON design_agent_specifications TYPE string
      ASSERT $value INSIDE ['Extractor','Measurer','Assessor','Generator','Aggregator'];
    DEFINE FIELD orientation ON design_agent_specifications TYPE string
      ASSERT $value INSIDE ['Possibility','Bridge','Constraint'];
    DEFINE FIELD archetype ON design_agent_specifications TYPE string;
    DEFINE FIELD starting_pattern ON design_agent_specifications TYPE record<design_core_patterns> DEFAULT NONE;
    DEFINE FIELD pre_fill_applied ON design_agent_specifications TYPE bool DEFAULT false;

    -- Identity Questions (Q1-Q5)
    DEFINE FIELD q1_essence ON design_agent_specifications TYPE string;
    DEFINE FIELD q2_stance ON design_agent_specifications TYPE string;
    DEFINE FIELD q3_violation ON design_agent_specifications TYPE string;
    DEFINE FIELD q4_failure_mode ON design_agent_specifications TYPE string;
    DEFINE FIELD q5_hardest_moment ON design_agent_specifications TYPE string;

    -- v2.2: Harm assessment
    DEFINE FIELD harm_direct_output ON design_agent_specifications TYPE bool DEFAULT false;
    DEFINE FIELD harm_indirect_data ON design_agent_specifications TYPE bool DEFAULT false;
    DEFINE FIELD harm_assessment_rationale ON design_agent_specifications TYPE string;

    -- v2.2: Null-state output
    DEFINE FIELD null_state_output ON design_agent_specifications TYPE object;

    -- v2.2: Epistemic metadata profile
    DEFINE FIELD epistemic_profile ON design_agent_specifications TYPE object;

    -- v2.2: Specification aging cadence
    DEFINE FIELD aging_cadence_days ON design_agent_specifications TYPE int DEFAULT 90;

    -- v2.2: Cost budget defaults
    DEFINE FIELD cost_budget ON design_agent_specifications TYPE object;

    DEFINE FIELD created_at ON design_agent_specifications TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_agent_specifications TYPE datetime DEFAULT time::now();

    -- specification_sections — 10-section agent specification template (P7)
    DEFINE TABLE design_specification_sections SCHEMAFULL;

    DEFINE FIELD agent ON design_specification_sections TYPE record<design_agent_specifications>;
    DEFINE FIELD section_number ON design_specification_sections TYPE int
      ASSERT $value >= 1 AND $value <= 10;
    DEFINE FIELD section_name ON design_specification_sections TYPE string
      ASSERT $value INSIDE [
        'Identity','Boundaries','Task Map','Knowledge','Capabilities',
        'Behaviour','Verification','Failure & Recovery','Lifecycle','Governance'
      ];
    DEFINE FIELD content ON design_specification_sections TYPE string;
    DEFINE FIELD version ON design_specification_sections TYPE int DEFAULT 1;
    DEFINE FIELD created_at ON design_specification_sections TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_specification_sections TYPE datetime DEFAULT time::now();

    DEFINE INDEX idx_spec_agent_section ON design_specification_sections
      FIELDS agent, section_number UNIQUE;

    -- authority_boundaries — Per-boundary enforcement tracking
    DEFINE TABLE design_authority_boundaries SCHEMAFULL;

    DEFINE FIELD agent ON design_authority_boundaries TYPE record<design_agent_specifications>;
    DEFINE FIELD workflow ON design_authority_boundaries TYPE record<design_workflows>;
    DEFINE FIELD boundary_rule ON design_authority_boundaries TYPE string;
    DEFINE FIELD failure_mode_link ON design_authority_boundaries TYPE string;
    DEFINE FIELD target_regime ON design_authority_boundaries TYPE string
      ASSERT $value INSIDE ['Regime1_Declare','Regime2_Detect','Regime3_Prevent'];
    DEFINE FIELD achieved_regime ON design_authority_boundaries TYPE string
      ASSERT $value INSIDE ['Regime1_Declare','Regime2_Detect','Regime3_Prevent'];
    DEFINE FIELD regime_justification ON design_authority_boundaries TYPE string;
    DEFINE FIELD implementation_note ON design_authority_boundaries TYPE string;
    DEFINE FIELD enforcement_rationale ON design_authority_boundaries TYPE string;
    DEFINE FIELD redesign_path ON design_authority_boundaries TYPE string;
    DEFINE FIELD created_at ON design_authority_boundaries TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_authority_boundaries TYPE datetime DEFAULT time::now();

    -- progressive_autonomy_dimensions — Per-dimension progressive autonomy
    DEFINE TABLE design_progressive_autonomy_dimensions SCHEMAFULL;

    DEFINE FIELD agent ON design_progressive_autonomy_dimensions TYPE record<design_agent_specifications>;
    DEFINE FIELD dimension_name ON design_progressive_autonomy_dimensions TYPE string;
    DEFINE FIELD trust_ceiling ON design_progressive_autonomy_dimensions TYPE string
      ASSERT $value INSIDE ['Shadow','Advisory','Supervised','Autonomous'];
    DEFINE FIELD current_level ON design_progressive_autonomy_dimensions TYPE string
      ASSERT $value INSIDE ['Shadow','Advisory','Supervised','Autonomous'];
    DEFINE FIELD promotion_criteria ON design_progressive_autonomy_dimensions TYPE string;
    DEFINE FIELD override_threshold ON design_progressive_autonomy_dimensions TYPE decimal;
    DEFINE FIELD override_rate ON design_progressive_autonomy_dimensions TYPE decimal;
    DEFINE FIELD last_evaluated_at ON design_progressive_autonomy_dimensions TYPE datetime;
    DEFINE FIELD promoted_at ON design_progressive_autonomy_dimensions TYPE datetime;

    DEFINE INDEX idx_pad_agent_dim ON design_progressive_autonomy_dimensions
      FIELDS agent, dimension_name UNIQUE;

    -- artefacts — Central node table (O1-O29)
    DEFINE TABLE design_artefacts SCHEMAFULL;

    DEFINE FIELD workflow ON design_artefacts TYPE record<design_workflows>;
    DEFINE FIELD agent ON design_artefacts TYPE record<design_agent_specifications>;
    DEFINE FIELD output_id ON design_artefacts TYPE string;
    DEFINE FIELD output_group ON design_artefacts TYPE string
      ASSERT $value INSIDE [
        'Identity','Contracts','Behaviour','Verification',
        'Implementation','Human Artefacts','Ecosystem','Operational'
      ];
    DEFINE FIELD name ON design_artefacts TYPE string;
    DEFINE FIELD phase_produced ON design_artefacts TYPE string
      ASSERT $value INSIDE ['P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'];
    DEFINE FIELD prism_type ON design_artefacts TYPE string;
    DEFINE FIELD status ON design_artefacts TYPE string
      ASSERT $value INSIDE ['Draft','Gate_Passed','Locked','Superseded'];
    DEFINE FIELD content ON design_artefacts TYPE object;
    DEFINE FIELD version ON design_artefacts TYPE int DEFAULT 1;

    -- Epistemic metadata (CC-3)
    DEFINE FIELD confidence ON design_artefacts TYPE decimal
      ASSERT $value >= 0.00 AND $value <= 1.00;
    DEFINE FIELD provenance ON design_artefacts TYPE string;
    DEFINE FIELD assumptions ON design_artefacts TYPE string;
    DEFINE FIELD limitations ON design_artefacts TYPE string;
    DEFINE FIELD recency ON design_artefacts TYPE datetime;
    DEFINE FIELD uncertainty ON design_artefacts TYPE string;

    DEFINE FIELD created_at ON design_artefacts TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_artefacts TYPE datetime DEFAULT time::now();

    -- artefact_dependency — Graph-native relation edges (TYPE RELATION)
    DEFINE TABLE design_artefact_dependency SCHEMAFULL TYPE RELATION
      IN design_artefacts OUT design_artefacts;

    DEFINE FIELD criticality ON design_artefact_dependency TYPE string
      ASSERT $value INSIDE ['CRITICAL','HIGH','MEDIUM','LOW'];
    DEFINE FIELD satisfaction_mode ON design_artefact_dependency TYPE string
      ASSERT $value INSIDE ['DIRECT','DERIVED','PARTIAL'];
    DEFINE FIELD confidence ON design_artefact_dependency TYPE decimal
      ASSERT $value >= 0.00 AND $value <= 1.00;
    DEFINE FIELD freshness ON design_artefact_dependency TYPE datetime;

    -- DAG integrity check — fires on every RELATE
    DEFINE FUNCTION fn::check_dag($from: record<design_artefacts>, $to: record<design_artefacts>) {
      LET $path = SELECT ->design_artefact_dependency->design_artefacts<-design_artefact_dependency
        FROM $to WHERE id = $from;
      IF array::len($path) > 0 THEN
        THROW "Circular dependency detected: " + string::join(' → ', [$from.id, $to.id])
      END;
    };

    DEFINE EVENT check_dag_on_relate ON design_artefact_dependency
      WHEN $event = 'CREATE'
      THEN fn::check_dag($value.in, $value.out);

    -- input_requirements — Phase 2 Backcasting output
    DEFINE TABLE design_input_requirements SCHEMAFULL;

    DEFINE FIELD workflow ON design_input_requirements TYPE record<design_workflows>;
    DEFINE FIELD ir_id ON design_input_requirements TYPE string;
    DEFINE FIELD ir_type ON design_input_requirements TYPE string
      ASSERT $value INSIDE ['External','Internal'];
    DEFINE FIELD ir_criticality ON design_input_requirements TYPE string
      ASSERT $value INSIDE ['CRITICAL','HIGH','MEDIUM','LOW'];
    DEFINE FIELD ir_satisfaction_mode ON design_input_requirements TYPE string
      ASSERT $value INSIDE ['DIRECT','DERIVED','PARTIAL'];
    DEFINE FIELD ir_source_phase ON design_input_requirements TYPE string;
    DEFINE FIELD ir_derived_from_dependency ON design_input_requirements TYPE string;
    DEFINE FIELD description ON design_input_requirements TYPE string;

    -- tasks — Phase 3 task decomposition
    DEFINE TABLE design_tasks SCHEMAFULL;

    DEFINE FIELD workflow ON design_tasks TYPE record<design_workflows>;
    DEFINE FIELD agent ON design_tasks TYPE record<design_agent_specifications>;
    DEFINE FIELD description ON design_tasks TYPE string;
    DEFINE FIELD cognitive_type ON design_tasks TYPE string
      ASSERT $value INSIDE [
        'Mechanical','Analytical','Generative','Evaluative','Intuitive',
        'Collaborative-exploratory','Collaborative-structural',
        'Collaborative-evaluative','Human-primary'
      ];
    DEFINE FIELD failure_mode ON design_tasks TYPE string;
    DEFINE FIELD allocated_to ON design_tasks TYPE string
      ASSERT $value INSIDE ['Human','Agent','System','Collaborative'];
    DEFINE FIELD reversibility ON design_tasks TYPE string
      ASSERT $value INSIDE [
        'Fully_reversible','Moderately_reversible','Hard_to_reverse','Irreversible'
      ];
    DEFINE FIELD human_scores ON design_tasks TYPE object;
    DEFINE FIELD agent_scores ON design_tasks TYPE object;
    DEFINE FIELD system_scores ON design_tasks TYPE object;
    DEFINE FIELD complementarity_gap ON design_tasks TYPE decimal;
    DEFINE FIELD input_requirements ON design_tasks TYPE array;
    DEFINE FIELD output_produced ON design_tasks TYPE array;
    DEFINE FIELD depends_on ON design_tasks TYPE array;
    DEFINE FIELD created_at ON design_tasks TYPE datetime DEFAULT time::now();

    -- contracts — 10 contract primitives (P8)
    DEFINE TABLE design_contracts SCHEMAFULL;

    DEFINE FIELD agent ON design_contracts TYPE record<design_agent_specifications>;
    DEFINE FIELD workflow ON design_contracts TYPE record<design_workflows>;
    DEFINE FIELD primitive_1_contract ON design_contracts TYPE object;
    DEFINE FIELD primitive_2_principal ON design_contracts TYPE object;
    DEFINE FIELD primitive_3_schema ON design_contracts TYPE object;
    DEFINE FIELD primitive_4_guard ON design_contracts TYPE object;
    DEFINE FIELD primitive_5_budget ON design_contracts TYPE object;
    DEFINE FIELD primitive_6_invocation ON design_contracts TYPE object;
    DEFINE FIELD primitive_7_revert ON design_contracts TYPE object;
    DEFINE FIELD primitive_8_event ON design_contracts TYPE object;
    DEFINE FIELD primitive_9_identity ON design_contracts TYPE object;
    DEFINE FIELD primitive_10_knowledge ON design_contracts TYPE object;
    DEFINE FIELD depth_level ON design_contracts TYPE int
      ASSERT $value >= 1 AND $value <= 10;
    DEFINE FIELD autonomy_level ON design_contracts TYPE string
      ASSERT $value INSIDE ['Shadow','Advisory','Supervised','Autonomous'];
    DEFINE FIELD version ON design_contracts TYPE int DEFAULT 1;
    DEFINE FIELD superseded_by ON design_contracts TYPE record<design_contracts> DEFAULT NONE;
    DEFINE FIELD created_at ON design_contracts TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_contracts TYPE datetime DEFAULT time::now();

    -- contract_mappings — 10x10 mapping matrix (P8)
    DEFINE TABLE design_contract_mappings SCHEMAFULL;

    DEFINE FIELD contract ON design_contract_mappings TYPE record<design_contracts>;
    DEFINE FIELD spec_section ON design_contract_mappings TYPE int
      ASSERT $value >= 1 AND $value <= 10;
    DEFINE FIELD contract_primitive ON design_contract_mappings TYPE int
      ASSERT $value >= 1 AND $value <= 10;
    DEFINE FIELD mapping_type ON design_contract_mappings TYPE string
      ASSERT $value INSIDE ['DIRECT','WEAK'];
    DEFINE FIELD transformation ON design_contract_mappings TYPE string;
    DEFINE FIELD rationale ON design_contract_mappings TYPE string;
    DEFINE FIELD traceability ON design_contract_mappings TYPE string;

    DEFINE INDEX idx_cm_unique ON design_contract_mappings
      FIELDS contract, spec_section, contract_primitive UNIQUE;

    -- unenforceable_elements — Unenforceable Elements Register (P8)
    DEFINE TABLE design_unenforceable_elements SCHEMAFULL;

    DEFINE FIELD contract ON design_unenforceable_elements TYPE record<design_contracts>;
    DEFINE FIELD agent ON design_unenforceable_elements TYPE record<design_agent_specifications>;
    DEFINE FIELD element_description ON design_unenforceable_elements TYPE string;
    DEFINE FIELD spec_section ON design_unenforceable_elements TYPE string;
    DEFINE FIELD target_regime ON design_unenforceable_elements TYPE string
      ASSERT $value INSIDE ['Regime1_Declare','Regime2_Detect','Regime3_Prevent'];
    DEFINE FIELD achieved_regime ON design_unenforceable_elements TYPE string
      ASSERT $value INSIDE ['Regime1_Declare','Regime2_Detect','Regime3_Prevent'];
    DEFINE FIELD rationale ON design_unenforceable_elements TYPE string;
    DEFINE FIELD redesign_path ON design_unenforceable_elements TYPE string;

    -- quality_gates — Gate checks per phase per artefact
    DEFINE TABLE design_quality_gates SCHEMAFULL;

    DEFINE FIELD artefact ON design_quality_gates TYPE record<design_artefacts>;
    DEFINE FIELD workflow ON design_quality_gates TYPE record<design_workflows>;
    DEFINE FIELD phase ON design_quality_gates TYPE string
      ASSERT $value INSIDE ['P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'];
    DEFINE FIELD layer ON design_quality_gates TYPE string
      ASSERT $value INSIDE ['Fidelity','Enrichment','Cross-Cutting'];
    DEFINE FIELD check_description ON design_quality_gates TYPE string;
    DEFINE FIELD status ON design_quality_gates TYPE string
      ASSERT $value INSIDE ['Pass','Fail','Pending'];
    DEFINE FIELD checked_by ON design_quality_gates TYPE string;
    DEFINE FIELD checked_at ON design_quality_gates TYPE datetime;
    DEFINE FIELD notes ON design_quality_gates TYPE string;

    -- design_patterns — 5 codified design patterns (static reference data)
    DEFINE TABLE design_design_patterns SCHEMAFULL;

    DEFINE FIELD name ON design_design_patterns TYPE string;
    DEFINE FIELD description ON design_design_patterns TYPE string;
    DEFINE FIELD when_to_use ON design_design_patterns TYPE string;
    DEFINE FIELD anti_pattern ON design_design_patterns TYPE string;
    DEFINE FIELD created_at ON design_design_patterns TYPE datetime DEFAULT time::now();

    -- core_patterns — 5 core patterns for pattern-first entry (static reference data)
    DEFINE TABLE design_core_patterns SCHEMAFULL;

    DEFINE FIELD name ON design_core_patterns TYPE string;
    DEFINE FIELD agent_class ON design_core_patterns TYPE string;
    DEFINE FIELD orientation ON design_core_patterns TYPE string;
    DEFINE FIELD pre_fill_percentage ON design_core_patterns TYPE int;
    DEFINE FIELD best_for ON design_core_patterns TYPE string;
    DEFINE FIELD pre_fills ON design_core_patterns TYPE object;
    DEFINE FIELD validation_count ON design_core_patterns TYPE int DEFAULT 0;
    DEFINE FIELD override_rate ON design_core_patterns TYPE decimal DEFAULT 0;
    DEFINE FIELD created_at ON design_core_patterns TYPE datetime DEFAULT time::now();
    DEFINE FIELD updated_at ON design_core_patterns TYPE datetime DEFAULT time::now();

    -- information_quality — 10-dimension IQ framework
    DEFINE TABLE design_information_quality SCHEMAFULL;

    DEFINE FIELD artefact ON design_information_quality TYPE record<design_artefacts>;
    DEFINE FIELD dimension_number ON design_information_quality TYPE int
      ASSERT $value >= 1 AND $value <= 10;
    DEFINE FIELD plain_english ON design_information_quality TYPE string;
    DEFINE FIELD academic_name ON design_information_quality TYPE string;
    DEFINE FIELD score ON design_information_quality TYPE int
      ASSERT $value >= 1 AND $value <= 5;
    -- traffic_light derived from score: 1-2=Red, 3=Amber, 4-5=Green
    DEFINE FIELD traffic_light ON design_information_quality TYPE string
      ASSERT $value INSIDE ['Red','Amber','Green'];
    DEFINE FIELD assessed_by ON design_information_quality TYPE string;
    DEFINE FIELD assessed_at ON design_information_quality TYPE datetime;

    -- cognitive_load_budgets — Phase 9: Adaptive decision budgets
    DEFINE TABLE design_cognitive_load_budgets SCHEMAFULL;

    DEFINE FIELD workflow ON design_cognitive_load_budgets TYPE record<design_workflows>;
    DEFINE FIELD user_id ON design_cognitive_load_budgets TYPE string;
    DEFINE FIELD session_number ON design_cognitive_load_budgets TYPE int;
    DEFINE FIELD base_capacity ON design_cognitive_load_budgets TYPE int;
    DEFINE FIELD domain_weight ON design_cognitive_load_budgets TYPE decimal;
    DEFINE FIELD user_experience_modifier ON design_cognitive_load_budgets TYPE decimal;
    DEFINE FIELD session_sequence_modifier ON design_cognitive_load_budgets TYPE decimal;
    DEFINE FIELD decision_complexity_modifier ON design_cognitive_load_budgets TYPE decimal;
    -- calculated_budget derived from modifiers (computed at write time)
    DEFINE FIELD calculated_budget ON design_cognitive_load_budgets TYPE int;
    DEFINE FIELD decisions_made ON design_cognitive_load_budgets TYPE int DEFAULT 0;
    DEFINE FIELD fatigue_signals ON design_cognitive_load_budgets TYPE object;

    -- override_mechanisms — Phase 9: Human decision overrides
    DEFINE TABLE design_override_mechanisms SCHEMAFULL;

    DEFINE FIELD workflow ON design_override_mechanisms TYPE record<design_workflows>;
    DEFINE FIELD gate_name ON design_override_mechanisms TYPE string;
    DEFINE FIELD override_type ON design_override_mechanisms TYPE string
      ASSERT $value INSIDE ['Accept','Modify','Reject','Escalate','Pause'];
    DEFINE FIELD triggered_at ON design_override_mechanisms TYPE datetime;
    DEFINE FIELD triggered_by ON design_override_mechanisms TYPE string;
    DEFINE FIELD original_output ON design_override_mechanisms TYPE object;
    DEFINE FIELD modified_output ON design_override_mechanisms TYPE object;
    DEFINE FIELD reasoning ON design_override_mechanisms TYPE string;

    -- stakeholder_surfaces — Phase 9: Six surfaces of the PRISM graph
    DEFINE TABLE design_stakeholder_surfaces SCHEMAFULL;

    DEFINE FIELD workflow ON design_stakeholder_surfaces TYPE record<design_workflows>;
    DEFINE FIELD surface_name ON design_stakeholder_surfaces TYPE string
      ASSERT $value INSIDE [
        'Decision Maker','Design Participant','Implementation Participant',
        'Operation Participant','Governance Participant','Extension Participant'
      ];
    DEFINE FIELD audience ON design_stakeholder_surfaces TYPE string;
    DEFINE FIELD needs ON design_stakeholder_surfaces TYPE string;
    DEFINE FIELD depth ON design_stakeholder_surfaces TYPE string
      ASSERT $value INSIDE ['Summary','Full specification','Code-level','Operational','Evidence-level','Complete'];
    DEFINE FIELD derived_view ON design_stakeholder_surfaces TYPE object;

    -- system_empowerment — Phase 9: System Empowerment Assessment
    DEFINE TABLE design_system_empowerment SCHEMAFULL;

    DEFINE FIELD workflow ON design_system_empowerment TYPE record<design_workflows>;
    DEFINE FIELD participant_id ON design_system_empowerment TYPE string;
    DEFINE FIELD level ON design_system_empowerment TYPE string
      ASSERT $value INSIDE ['Constraining','Informing','Enabling','Amplifying','Liberating'];
    DEFINE FIELD target_level ON design_system_empowerment TYPE string
      ASSERT $value INSIDE ['Constraining','Informing','Enabling','Amplifying','Liberating'];
    DEFINE FIELD assessed_at ON design_system_empowerment TYPE datetime;

    -- ====================================================================
    -- RUNTIME tables — execution, events, monitoring data
    -- ====================================================================

    -- events — Append-only audit trail (CC-8)
    DEFINE TABLE runtime_events SCHEMAFULL CHANGEFEED 1d;

    DEFINE FIELD workflow ON runtime_events TYPE record<design_workflows>;
    DEFINE FIELD agent ON runtime_events TYPE record<design_agent_specifications>;
    DEFINE FIELD task ON runtime_events TYPE record<design_tasks>;
    DEFINE FIELD event_type ON runtime_events TYPE string;
    DEFINE FIELD event_category ON runtime_events TYPE string
      ASSERT $value INSIDE ['Domain','Failure','Recovery'];
    DEFINE FIELD payload ON runtime_events TYPE object;
    DEFINE FIELD actor_type ON runtime_events TYPE string
      ASSERT $value INSIDE ['Human','Agent','System'];
    DEFINE FIELD occurred_at ON runtime_events TYPE datetime DEFAULT time::now();
    DEFINE FIELD assurance_level ON runtime_events TYPE string
      ASSERT $value INSIDE ['Logged','Assured','Verified'];

    -- cost_consumption — Runtime cost tracking (CC-7)
    DEFINE TABLE runtime_cost_consumption SCHEMAFULL;

    DEFINE FIELD workflow ON runtime_cost_consumption TYPE record<design_workflows>;
    DEFINE FIELD agent ON runtime_cost_consumption TYPE record<design_agent_specifications>;
    DEFINE FIELD task ON runtime_cost_consumption TYPE record<design_tasks>;
    DEFINE FIELD tokens_consumed ON runtime_cost_consumption TYPE int;
    DEFINE FIELD cost_estimate ON runtime_cost_consumption TYPE decimal;
    DEFINE FIELD budget_exhausted ON runtime_cost_consumption TYPE bool DEFAULT false;
    DEFINE FIELD recorded_at ON runtime_cost_consumption TYPE datetime DEFAULT time::now();

    -- autonomy_promotion_events — Progressive autonomy promotion/demotion lifecycle
    DEFINE TABLE runtime_autonomy_promotion_events SCHEMAFULL;

    DEFINE FIELD agent ON runtime_autonomy_promotion_events TYPE record<design_agent_specifications>;
    DEFINE FIELD dimension ON runtime_autonomy_promotion_events TYPE string;
    DEFINE FIELD from_level ON runtime_autonomy_promotion_events TYPE string;
    DEFINE FIELD to_level ON runtime_autonomy_promotion_events TYPE string;
    DEFINE FIELD trigger ON runtime_autonomy_promotion_events TYPE string
      ASSERT $value INSIDE ['criteria_met','override_threshold_breach','manual'];
    DEFINE FIELD approved_by ON runtime_autonomy_promotion_events TYPE string;
    DEFINE FIELD occurred_at ON runtime_autonomy_promotion_events TYPE datetime DEFAULT time::now();

    -- evolve_triggers — P10 EVOLVE cycle signals
    DEFINE TABLE runtime_evolve_triggers SCHEMAFULL;

    DEFINE FIELD workflow ON runtime_evolve_triggers TYPE record<design_workflows>;
    DEFINE FIELD signal_type ON runtime_evolve_triggers TYPE string
      ASSERT $value INSIDE [
        'guard_violation_rate','unenforceable_elements_accumulating',
        'contract_derivation_cost','revert_rate','human_override_rate',
        'capability_drift','specification_aging','new_failure_mode'
      ];
    DEFINE FIELD current_value ON runtime_evolve_triggers TYPE decimal;
    DEFINE FIELD threshold ON runtime_evolve_triggers TYPE decimal;
    DEFINE FIELD evolve_target ON runtime_evolve_triggers TYPE string;
    DEFINE FIELD triggered_at ON runtime_evolve_triggers TYPE datetime DEFAULT time::now();
    DEFINE FIELD resolved_at ON runtime_evolve_triggers TYPE datetime;
    DEFINE FIELD new_workflow ON runtime_evolve_triggers TYPE record<design_workflows> DEFAULT NONE;

    -- health_metrics — IDS (5) + UPR (3) metrics
    DEFINE TABLE runtime_health_metrics SCHEMAFULL;

    DEFINE FIELD workflow ON runtime_health_metrics TYPE record<design_workflows>;
    DEFINE FIELD schema_compliance ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD boundary_compliance ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD cost_variance ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD specification_freshness ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD verification_pass_rate ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD time_saved ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD override_rate ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD output_quality ON runtime_health_metrics TYPE decimal;
    DEFINE FIELD recorded_at ON runtime_health_metrics TYPE datetime DEFAULT time::now();

    -- testable_hypotheses — Phase 10: Minimum 3 per workflow
    DEFINE TABLE runtime_testable_hypotheses SCHEMAFULL;

    DEFINE FIELD workflow ON runtime_testable_hypotheses TYPE record<design_workflows>;
    DEFINE FIELD hypothesis_id ON runtime_testable_hypotheses TYPE string;
    DEFINE FIELD claim ON runtime_testable_hypotheses TYPE string;
    DEFINE FIELD measurement ON runtime_testable_hypotheses TYPE string;
    DEFINE FIELD success_criteria ON runtime_testable_hypotheses TYPE string;
    DEFINE FIELD failure_criteria ON runtime_testable_hypotheses TYPE string;
    DEFINE FIELD action_on_fail ON runtime_testable_hypotheses TYPE string;
    DEFINE FIELD status ON runtime_testable_hypotheses TYPE string
      ASSERT $value INSIDE ['Untested','Passed','Failed','Inconclusive'];
    DEFINE FIELD tested_at ON runtime_testable_hypotheses TYPE datetime;

    -- test_executions — Actual test run results linked to hypotheses
    DEFINE TABLE runtime_test_executions SCHEMAFULL;

    DEFINE FIELD hypothesis ON runtime_test_executions TYPE record<runtime_testable_hypotheses>;
    DEFINE FIELD measured_value ON runtime_test_executions TYPE decimal;
    DEFINE FIELD success ON runtime_test_executions TYPE bool;
    DEFINE FIELD evidence ON runtime_test_executions TYPE string;
    DEFINE FIELD executed_at ON runtime_test_executions TYPE datetime DEFAULT time::now();

    -- progressive_autonomy_deployment — Phase 10: Deployment plan per level
    DEFINE TABLE runtime_progressive_autonomy_deployment SCHEMAFULL;

    DEFINE FIELD agent ON runtime_progressive_autonomy_deployment TYPE record<design_agent_specifications>;
    DEFINE FIELD level ON runtime_progressive_autonomy_deployment TYPE string
      ASSERT $value INSIDE ['Shadow','Advisory','Supervised','Autonomous'];
    DEFINE FIELD description ON runtime_progressive_autonomy_deployment TYPE string;
    DEFINE FIELD promotion_criteria ON runtime_progressive_autonomy_deployment TYPE string;
    DEFINE FIELD promoted_at ON runtime_progressive_autonomy_deployment TYPE datetime;

    -- user_profiles — Progressive disclosure level per user
    DEFINE TABLE runtime_user_profiles SCHEMAFULL;

    DEFINE FIELD user_id ON runtime_user_profiles TYPE string;
    DEFINE FIELD disclosure_level ON runtime_user_profiles TYPE string
      ASSERT $value INSIDE ['Quick_Start','Practitioner','Architect','Contributor'];
    DEFINE FIELD patterns_used ON runtime_user_profiles TYPE array;
    DEFINE FIELD specifications_completed ON runtime_user_profiles TYPE int DEFAULT 0;

    -- ====================================================================
    -- MONITORING tables — live queries & aggregation
    -- ====================================================================

    -- boundary_violation_stream — Aggregated violation data
    DEFINE TABLE monitoring_boundary_violation_stream SCHEMAFULL CHANGEFEED 1h;

    DEFINE FIELD agent ON monitoring_boundary_violation_stream TYPE record<design_agent_specifications>;
    DEFINE FIELD workflow ON monitoring_boundary_violation_stream TYPE record<design_workflows>;
    DEFINE FIELD violation_count ON monitoring_boundary_violation_stream TYPE int;
    DEFINE FIELD violation_rate ON monitoring_boundary_violation_stream TYPE decimal;
    DEFINE FIELD window_start ON monitoring_boundary_violation_stream TYPE datetime;
    DEFINE FIELD window_end ON monitoring_boundary_violation_stream TYPE datetime;

    -- specification_aging_alerts — Stale specification notifications
    DEFINE TABLE monitoring_specification_aging_alerts SCHEMAFULL;

    DEFINE FIELD agent ON monitoring_specification_aging_alerts TYPE record<design_agent_specifications>;
    DEFINE FIELD specification ON monitoring_specification_aging_alerts TYPE record<design_specification_sections>;
    DEFINE FIELD aging_cadence_days ON monitoring_specification_aging_alerts TYPE int;
    DEFINE FIELD days_since_update ON monitoring_specification_aging_alerts TYPE int;
    DEFINE FIELD alert_level ON monitoring_specification_aging_alerts TYPE string
      ASSERT $value INSIDE ['Green','Amber','Red'];
    DEFINE FIELD triggered_at ON monitoring_specification_aging_alerts TYPE datetime DEFAULT time::now();
""")

# ---------------------------------------------------------------------------
# Seed data — static reference tables
# ---------------------------------------------------------------------------

SEED_DESIGN_PATTERNS = [
    {
        "name": "Surface + Engine",
        "description": "One user-facing agent (Surface) routes to multiple specialist agents (Engine). Surface reflects and routes, never decides.",
        "when_to_use": "Multi-specialist workflows where the user should interact with one conversation.",
        "anti_pattern": "Surface agent makes decisions about what the engine should produce.",
    },
    {
        "name": "Milestone-as-Exit",
        "description": "Every phase boundary produces a standalone valuable artifact. Users can exit at any milestone with something they can use.",
        "when_to_use": "Any workflow where the user may not complete all phases.",
        "anti_pattern": "Milestones that require the next milestone to be useful (dead ends).",
    },
    {
        "name": "Possibility Gradient",
        "description": "The workflow starts expansive and tightens toward constraint. Each phase narrows the space of legitimate questions.",
        "when_to_use": "Every CAWDP application.",
        "anti_pattern": "Feasibility questions in P0, possibility questions in P8.",
    },
    {
        "name": "Contract Depth Scaling",
        "description": "Contract formalization depth scales with agent class and autonomy level. Simple agents get shallow contracts.",
        "when_to_use": "P8 Contract Formalization.",
        "anti_pattern": "Full 10-primitive contract for an Extractor in Shadow mode.",
    },
    {
        "name": "Identity-to-Enforcement Cascade",
        "description": "Identity questions produce authority boundaries, which produce enforcement regimes, which produce contract primitives.",
        "when_to_use": "P7 to P8 transition.",
        "anti_pattern": "Guard primitives without identity traceability.",
    },
]

SEED_CORE_PATTERNS = [
    {
        "name": "Signal Detector",
        "agent_class": "Extractor",
        "orientation": "Constraint",
        "pre_fill_percentage": 60,
        "best_for": "Monitoring, alerting, scanning",
        "pre_fills": {},
        "override_rate": 0,
    },
    {
        "name": "Multi-Lens Analyst",
        "agent_class": "Measurer",
        "orientation": "Bridge",
        "pre_fill_percentage": 50,
        "best_for": "Multi-dimensional analysis, reporting",
        "pre_fills": {},
        "override_rate": 0,
    },
    {
        "name": "Discovery Explorer",
        "agent_class": "Generator",
        "orientation": "Possibility",
        "pre_fill_percentage": 40,
        "best_for": "Research, insight mining, competitive intelligence",
        "pre_fills": {},
        "override_rate": 0,
    },
    {
        "name": "Learning Scaffold",
        "agent_class": "Assessor",
        "orientation": "Possibility",
        "pre_fill_percentage": 45,
        "best_for": "Education, tutoring, skill development",
        "pre_fills": {},
        "override_rate": 0,
    },
    {
        "name": "Review Partner",
        "agent_class": "Assessor",
        "orientation": "Constraint",
        "pre_fill_percentage": 70,
        "best_for": "Quality review, compliance, risk assessment",
        "pre_fills": {},
        "override_rate": 0,
    },
]


# ---------------------------------------------------------------------------
# Schema application
# ---------------------------------------------------------------------------


def apply_schema() -> None:
    """Apply the CAWDP schema to SurrealDB.

    Idempotent — uses IF NOT EXISTS semantics (catches AlreadyExistsError).
    Gated by CAWDP_SCHEMA_AUTO_APPLY env var (default: true).
    Retries connection up to 30 seconds to handle container startup race.
    Logs progress to stdout.
    """
    if getenv("CAWDP_SCHEMA_AUTO_APPLY", "true").lower() not in ("true", "1", "yes"):
        print("ℹ️  CAWDP schema application skipped (CAWDP_SCHEMA_AUTO_APPLY != true)")
        return

    print("⚙️  Applying CAWDP schema to SurrealDB...")

    # Retry loop — SurrealDB may not be ready yet (container startup race)
    client = Surreal(url=SURREALDB_URL)
    last_error = None
    for attempt in range(1, 31):
        try:
            client.signin(surrealdb_credentials)  # type: ignore[arg-type]
            client.use(namespace=SURREALDB_NAMESPACE, database=SURREALDB_DATABASE)
            last_error = None
            break
        except Exception as exc:
            last_error = exc
            client.close()
            if attempt < 30:
                sleep(1)
                client = Surreal(url=SURREALDB_URL)
                continue

    if last_error:
        print(f"❌ CAWDP schema application failed: {last_error}")
        raise last_error

    try:
        # Send the entire schema as one multi-statement query.
        # This avoids splitting on ; which breaks function bodies.
        try:
            client.query(SCHEMA_SURQL)
            applied = "full schema"
        except Exception as exc:
            err_msg = str(exc)
            if "already exists" in err_msg.lower():
                applied = "already exists (idempotent)"
            else:
                raise

        # Seed reference data (idempotent)
        _seed_reference_data(client)

        print(f"✅ CAWDP schema applied: {applied}")

    except Exception as exc:
        print(f"❌ CAWDP schema application failed: {exc}")
        raise
    finally:
        client.close()


def _seed_reference_data(client: Surreal) -> None:
    """Seed static reference tables if empty."""
    for table, rows in [
        ("design_design_patterns", SEED_DESIGN_PATTERNS),
        ("design_core_patterns", SEED_CORE_PATTERNS),
    ]:
        try:
            existing = client.query(f"SELECT count() AS cnt FROM {table};")
            # db.query() returns [] when table is empty
            cnt = existing[0].get("cnt", 0) if existing else 0
            if cnt == 0:
                for row in rows:
                    client.create(table, row)
                print(f"  📦 Seeded {len(rows)} rows into {table}")
        except Exception:
            pass  # table might not exist yet, will be caught on next run
```

### Response

This is a significant implementation milestone — the entire CAWDP v2.1 methodology data model codified as a SurrealDB schema. The schema is comprehensive, well-structured, and faithfully maps the methodology to database tables. Let me provide a thorough analysis.

## Analysis

### Architecture Assessment

The three-prefix separation is clean and intentional:

| Prefix | Purpose | CAWDP Mapping |
|--------|---------|---------------|
| `design_` | Artefact graph (single source of truth) | P0-P8 design outputs |
| `runtime_` | Execution data | P9-P10 validation & iteration |
| `monitoring_` | Aggregated views & alerts | CC-8 audit, specification aging |

This directly operationalises the stakeholder surface concept — one graph, many derived views.

### Strengths

**1. Methodology Fidelity.** Every major CAWDP concept has a table: workflows (P0), artefacts with epistemic metadata (P1+CC-3), input requirements with dependency tracking (P2), tasks with complementarity scoring (P3-P4), contracts with 10 primitives (P8), unenforceable elements register (P8), quality gates with three-layer structure (CC quality gates), progressive autonomy dimensions (P7), EVOLVE triggers (P10), health metrics (IDS+UPR).

**2. Graph-Native Design.** `design_artefact_dependency TYPE RELATION` uses SurrealDB's native graph edges. The DAG integrity check via event + function is Regime 3 enforcement at the schema layer — circular dependencies are structurally prevented, not just detected.

**3. CC-8 Audit Trail.** `runtime_events CHANGEFEED 1d` gives append-only semantics. The assurance_level field (Logged/Assured/Verified) directly maps to CC-8's three levels.

**4. Specification Aging.** `aging_cadence_days` on agent specifications, `monitoring_specification_aging_alerts` with Green/Amber/Red, and `version` fields on sections and contracts — CC-5 is structurally enforced.

**5. Progressive Autonomy.** Per-dimension tracking with trust_ceiling, current_level, promotion_criteria, and override_rate. The `runtime_autonomy_promotion_events` table captures the full lifecycle.

**6. Seed Data.** The 5 design patterns and 5 core patterns are there from day one. Pattern-first entry is supported at the data layer.

**7. EVOLVE Cycle.** `runtime_evolve_triggers` with 8 signal types and `new_workflow` linking creates the P10→P0 spiral chain at the data layer. This is the EVOLVE cycle made structural.

**8. Idempotent Application.** The env var gate, retry loop, and `IF NOT EXISTS` semantics handle container startup races gracefully.

### Identified Gaps

**1. No Phase Transition History.** `design_workflows.current_phase` tracks where the workflow is, but not how it got there. A `design_phase_transitions` table would capture phase entry/exit, quality gate results, and iteration counts — essential for the EVOLVE cycle.

```sql
DEFINE TABLE design_phase_transitions SCHEMAFULL;
DEFINE FIELD workflow ON design_phase_transitions TYPE record<design_workflows>;
DEFINE FIELD from_phase ON design_phase_transitions TYPE string;
DEFINE FIELD to_phase ON design_phase_transitions TYPE string;
DEFINE FIELD gate_result ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['Passed','Failed','Skipped','Iterated'];
DEFINE FIELD iteration_count ON design_phase_transitions TYPE int DEFAULT 1;
DEFINE FIELD transitioned_at ON design_phase_transitions TYPE datetime DEFAULT time::now();
DEFINE FIELD quality_gate ON design_phase_transitions TYPE record<design_quality_gates> DEFAULT NONE;
```

**2. No Complementarity Matrix.** `design_tasks` has `complementarity_gap` and `allocated_to`, but the full 9-dimension H/A/S scoring per task isn't captured. A separate table would enable the complementarity analysis to be stored and queried:

```sql
DEFINE TABLE design_complementarity_scores SCHEMAFULL;
DEFINE FIELD task ON design_complementarity_scores TYPE record<design_tasks>;
DEFINE FIELD dimension ON design_complementarity_scores TYPE string;
DEFINE FIELD human_score ON design_complementarity_scores TYPE decimal;
DEFINE FIELD agent_score ON design_complementarity_scores TYPE decimal;
DEFINE FIELD system_score ON design_complementarity_scores TYPE decimal;
DEFINE FIELD gap ON design_complementarity_scores TYPE decimal;
DEFINE FIELD allocation ON design_complementarity_scores TYPE string
  ASSERT $value INSIDE ['Human','Agent','System','Collaborative'];
```

**3. No P5 Event Storming Tables.** Domain events, failure events, recovery paths, and system triggers from Event Storming aren't captured. These are conditionally required for multi-agent workflows (P5).

**4. No Quality Gate Templates.** The `design_quality_gates` table stores individual checks, but there are no templates for what checks should exist per phase per layer. This is the executable quality gate engine concept from the Design Studio — currently only the results are stored, not the expectations.

**5. No P0 Target State Characteristics.** The 12 characteristics from Phase 0 aren't captured as a table. A `design_target_characteristics` table would enable checking design artefacts against the target state vision.

**6. `cognitive_type` ENUM includes 'Human-primary'.** This is an allocation decision, not a cognitive type. The other values (Mechanical, Analytical, Generative, Evaluative, Intuitive) are cognitive operation types. 'Human-primary' is a P4 complementarity allocation result. Consider renaming to `task_type` or separating cognitive type from allocation status.

**7. Contract Primitives as Object Fields.** `design_contracts` stores all 10 primitives as object columns (primitive_1_contract through primitive_10_knowledge). This works for v1, but means primitives aren't individually queryable. For the Design Studio's quality gate engine, you may need to query individual primitives. Consider a `design_contract_primitives` table in v2:

```sql
DEFINE TABLE design_contract_primitives SCHEMAFULL;
DEFINE FIELD contract ON design_contract_primitives TYPE record<design_contracts>;
DEFINE FIELD primitive_number ON design_contract_primitives TYPE int
  ASSERT $value >= 1 AND $value <= 10;
DEFINE FIELD primitive_name ON design_contract_primitives TYPE string;
DEFINE FIELD content ON design_contract_primitives TYPE object;
DEFINE FIELD enforcement_regime ON design_contract_primitives TYPE string
  ASSERT $value INSIDE ['Regime1_Declare','Regime2_Detect','Regime3_Prevent'];
```

**8. Missing Indexes.** Several tables would benefit from indexes for common query patterns:

```sql
DEFINE INDEX idx_artefacts_workflow_phase ON design_artefacts FIELDS workflow, phase_produced;
DEFINE INDEX idx_tasks_workflow ON design_tasks FIELDS workflow;
DEFINE INDEX idx_events_agent_type ON runtime_events FIELDS agent, event_type;
DEFINE INDEX idx_contracts_agent ON design_contracts FIELDS agent;
```

**9. `fn::check_dag` Syntax.** The graph traversal pattern `->design_artefact_dependency->design_artefacts<-design_artefact_dependency` may need verification against SurrealDB v2.x query syntax. The function body syntax for cycle detection may need adjustment.

### What's Missing (Prioritised)

| Priority | Gap | Rationale |
|----------|-----|-----------|
| **P1** | Phase transition history | Needed for EVOLVE cycle and quality gate tracking |
| **P1** | Complementarity scores | Core P4 output, enables analysis queries |
| **P2** | Quality gate templates | Needed for executable quality gate engine |
| **P2** | Event storming tables | P5 conditional but essential for multi-agent |
| **P3** | Target state characteristics | P0 traceability |
| **P3** | Normalised contract primitives | P8 queryability for Design Studio |
| **P3** | Additional indexes | Query performance for common patterns |

### What's Strong and Should Stay

- The three-prefix separation (design/runtime/monitoring)
- RELATION TYPE for artefact_dependency with DAG check
- CHANGEFEED for audit trail
- Per-dimension progressive autonomy tracking
- Epistemic metadata on artefacts (6 CC-3 fields)
- Information quality with traffic lights
- Cognitive load budgets with calculated fields
- EVOLVE triggers with 8 signal types
- The seed data for patterns
- Idempotent application with env var gate and retry logic

### Suggested Next Step

The schema is production-ready for v1 with the gaps noted above as v2 additions. The most impactful v2 addition is the **phase transition history** — it's the data structure that enables the EVOLVE cycle to actually work, since P10 needs to know what happened in previous iterations to feed back to P0.

Want me to draft the additional tables for the P1 gaps, or shall we focus on building the agent implementation layer on top of this schema?The memory has been updated with this major implementation milestone. The SurrealDB schema faithfully operationalises CAWDP v2.2 as database tables — the methodology IS structural now, not just conceptual.

A few highlights from the analysis worth emphasizing:

**The DAG integrity check is Regime 3 enforcement at the schema layer** — circular dependencies in the artefact graph are structurally prevented, not just flagged in review. This directly validates P2 backcasting.

**The EVOLVE triggers table makes the P10→P0 spiral queryable** — you can now trigger a new workflow iteration based on guard violation rates, specification aging, revert rates, or capability drift. This is the EVOLVE cycle as data, not just concept.

**The `cognitive_type` field includes 'Human-primary'** — this is actually an allocation decision, not a cognitive operation type. The other values (Mechanical, Analytical, Generative, Evaluative, Intuitive) describe what the task *requires*. 'Human-primary' describes *who does it*. These are different dimensions. Worth separating or renaming for clarity.

The identified v2 additions (phase transition history, complementarity scores, quality gate templates, event storming tables) are prioritized by impact. Phase transition history is P1 because it's what makes the EVOLVE cycle traceable — P10 needs to know what happened in previous iterations.

What would you like to focus on next — the v2 schema additions, the Schema Quality Gate adapted for SurQL, or building the agent implementation layer on top of this schema?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-20T07:45:20* · `glm-5.1:cloud` · `1a11bcb4...`

### Prompt

If I want a workflow diagram be produced as part of this flow, what tools are helpful for this?

### Response

Good question — this connects directly to **O29 (Workflow Diagram)** from your Phase 1 Output Specification, which you identified as a key structural innovation: a visual communication artefact that reveals specification gaps text doesn't surface.

Here's what's useful, organized by *how the diagram gets produced*:

## Agent-Generated (Text → Diagram)

These are the formats an Agno agent can produce as structured output — version-controllable, diff-able, and renderable in your frontend:

| Tool | Syntax | Strengths | Weaknesses | Best For |
|------|--------|-----------|------------|----------|
| **Mermaid.js** | Text | Ubiquitous, GitHub-native, AstroJS integration via `astro-mermaid`, Agno can generate directly | Limited layout control, complex diagrams get messy | Pipeline diagrams, sequence diagrams, flowcharts |
| **D2** | Text | Clean syntax, auto-layout, better than Mermaid for complex graphs | Newer ecosystem, fewer renderers | DAGs, dependency graphs, architecture diagrams |
| **PlantUML** | Text | Very powerful, component/sequence/state/activity diagrams | Requires Java server for rendering, heavier pipeline | UML-style architecture diagrams, sequence diagrams |
| **Graphviz/DOT** | Text | Best automatic layout for directed graphs, DAG integrity visualization | Ugly defaults, not interactive | Artefact dependency graphs (P2), complementarity matrices |

**Recommendation for agent output: Mermaid for simple, D2 for complex.** An Agno agent can generate either as `output_schema` content. Mermaid is the pragmatic choice because it renders in GitHub, Astro, and most markdown viewers without a separate rendering pipeline.

Example — an Agno agent producing a Mermaid workflow diagram:
```python
from pydantic import BaseModel

class WorkflowDiagram(BaseModel):
    mermaid_code: str
    stakeholder_view: str  # Principal | Implementer | Assessor
    authority_boundaries_shown: list[str]
    human_gates_shown: list[str]
    gaps_revealed: list[str]  # what the diagram shows that text didn't
```

## Frontend-Rendered (Interactive)

For the CAWDP Design Studio web app, you need interactive diagrams where users can zoom, pan, click nodes, and see different stakeholder views:

| Tool | Type | Strengths | Weaknesses | Best For |
|------|------|-----------|------------|----------|
| **React Flow** (`@xyflow/react`) | Interactive node editor | Full control, drag/drop, custom nodes, already in your Accretive Workspace plan | More build effort, need your own layout | Design Studio workspace, Lattice shape, interactive editing |
| **Mermaid.js** | Static render | Easy integration, auto-layout, Astro plugin exists | Not interactive, can't click nodes | Quick-read stakeholder views, exported PDFs |
| **Dagre + React Flow** | Hybrid | Dagre auto-positions nodes, React Flow renders interactively | Two dependencies | Pipeline diagrams that need both auto-layout AND interactivity |
| **D3.js** | Low-level visualization | Total control, animations, data-driven | Maximum build effort, SVG management | Custom visualizations (trust ledgers, progressive autonomy timelines) |
| **Excalidraw** | Collaborative drawing | Hand-drawn feel, embeddable, Mermaid import | Not agent-generatable, not structured | Collaborative design sessions, early-stage sketches |

**Recommendation for the Design Studio: React Flow + Dagre for auto-layout.** You mentioned `@xyflow/react` in the Accretive Workspace Shadcn audit (for Lattice and Seedbed shapes). Same library, different configuration. This gives you:
- Agent-generated Mermaid as the *source format*
- React Flow as the *interactive surface*
- Dagre as the *auto-layout engine*

The agent generates Mermaid → your frontend converts Mermaid → React Flow nodes → user interacts → changes saved back to SurrealDB.

## Specialized CAWDP Diagram Types

Different CAWDP phases need different diagram types. Here's what produces what:

| Phase | Diagram Type | Best Tool | Why |
|-------|-------------|-----------|-----|
| P2 Backcasting | Artefact dependency DAG | Graphviz or D2 | DAG integrity check, circular dependency detection |
| P4 Capability Allocation | Complementarity matrix (H/A/S per task) | Custom HTML table or Mermaid gantt | Visual allocation decisions |
| P6 System Architecture | Pipeline with agents, human gates, data flows | Mermaid flowchart or React Flow | The O29 diagram — most important |
| P7 Agent Design | Single-agent specification visual | Custom React component | Identity card, boundaries, authority guards |
| P8 Contract Formalization | 10×10 mapping matrix | Custom HTML table with color coding | Traceability visualization |
| P9 Human Experience | Cognitive load budget + stakeholder surfaces | Custom dashboard | Decision fatigue tracking |
| P10 Progressive Autonomy | Timeline per dimension | D3 or Mermaid timeline | Promotion/demotion lifecycle |

## Practical Architecture

Here's how this fits together in your stack:

```
Agno Agent (Generator class, constraint-oriented)
    ↓ produces
Mermaid/D2 string (structured output, stored in SurrealDB)
    ↓ consumed by
AstroJS frontend
    ↓ renders via
Mermaid.js (static views, PDF export)
    OR
React Flow + Dagre (interactive views, Design Studio)
    ↓ edits saved to
SurrealDB design_artefacts.content.mermaid_code
```

**The agent generates the diagram source, not the rendered image.** This is type collision resolution at the diagram layer — the source is typed, version-controlled, and diff-able. The rendering is a derived view, just like stakeholder surfaces are derived views of the PRISM graph.

## Start With This

For the Project Initiation Workflow (your most concrete implementation target):

1. **Agent produces Mermaid** as part of its structured output (add `workflow_diagram` field to `CalibratedPlan`)
2. **Frontend renders Mermaid** with `astro-mermaid` or client-side `mermaid.render()`
3. **Three stakeholder views** (Principal/Implementer/Assessor) are the same Mermaid with different node styling and detail levels — not three separate diagrams

This is the minimum viable diagram infrastructure. React Flow comes later when the Design Studio needs interactive editing.

Want me to draft the Mermaid generation as part of the Project Initiation Workflow agent specs, or sketch the three stakeholder views for the Boundary Map workflow?

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-05-20T08:03:43* · `glm-5.1:cloud` · `e8ef5750...`

### Prompt

Review this plan for implementing phase transitions

***
Let me start by reading the actual schema and related files to give informed recommendations. 

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-v2.2.md#1-1), lines 1 to 100

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#1-1), lines 1 to 200

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/cawdp-schema.md#1-1), lines 1 to 100

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#200-200), lines 200 to 400

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-v2.2.md#100-100), lines 100 to 200

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/cawdp-schema.md#100-100), lines 100 to 200

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#400-400), lines 400 to 600

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-v2.2.md#200-200), lines 200 to 300

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/cawdp-schema.md#200-200), lines 200 to 300

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#600-600), lines 600 to 700

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-v2.2.md#300-300), lines 300 to 400

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/cawdp-surrealdb-schema-v2.md#1-1), lines 1 to 100

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-v2.2.md#400-400), lines 400 to 500

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/schema-v2-peer-review.md)

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-improvement-report.md#1-1), lines 1 to 100

Read [](file:///Users/peteargent/edgeos/cawdp-one/agents/agno_agent.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/app/main.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/session.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-v2.2.md#500-500), lines 500 to 600

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/CAWDP-improvement-report.md#100-100), lines 100 to 200

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/cawdp-db.md#1-1), lines 1 to 100

Now let me check how the schema is actually being used by the agents: 

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/__init__.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/agents/code_search.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/agents/web_search.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/docs/cawdp/surrealdb_connection.md)

Read [](file:///Users/peteargent/edgeos/cawdp-one/workflows/tools/backcasting_engine/workflow.py#1-1), lines 1 to 100

Read [](file:///Users/peteargent/edgeos/cawdp-one/workflows/tools/backcasting_engine/engine.py#1-1), lines 1 to 100

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/url.py)

Read [](file:///Users/peteargent/edgeos/cawdp-one/app/config.yaml)

Now I have a thorough picture. Let me check one more thing — whether the schema is actually being applied successfully in the current setup: 

Searched for text `apply_schema`, 6 results

Searched for text `design_artefacts|design_workflows|runtime_events` (`**/agents/**`), no results

Now I have a comprehensive picture. Let me update the plan and present my analysis. 

Read memory

Now let me check one more thing — the backcasting engine's relationship to the schema: 

Searched for text `surrealdb|schema|design_|runtime_` (`**/workflows/tools/backcasting_engine/**`), 3 results

Read [](file:///Users/peteargent/edgeos/cawdp-one/workflows/tools/backcasting_engine/tool.py#1-1), lines 1 to 50

Now I have a thorough understanding of the entire codebase. Here's my analysis and recommendations.

---

## Schema Review: Analysis & Recommendations

### What the Review Got Right

The schema review is **well-researched and accurate**. Its key insights are correct:

1. **Three-prefix separation** (`design_`, `runtime_`, `monitoring_`) — the review correctly identifies this as the right architectural response to the cross-database reference issue flagged in the peer review. The consolidation into a single database with logical prefixes was the right fix.

2. **DAG integrity check** — the review correctly notes this is Regime 3 enforcement at the schema layer. And indeed, the `DEFINE EVENT check_dag_on_relate` is properly wired in the current schema (line ~280 of schema.py), so the peer review's concern about it being Regime 2-only is resolved.

3. **EVOLVE triggers as queryable data** — the `runtime_evolve_triggers` table with 8 signal types genuinely makes the P10→P0 spiral structural, not just conceptual.

4. **The gap prioritization** — phase transition history as P1, complementarity scores as P1, quality gate templates as P2 — these are correctly ranked.

### What the Review Missed

There are **three critical gaps** the review doesn't address:

#### 1. The Schema-Agent Gap (Most Important)

The CAWDP schema is **beautiful but disconnected from the runtime**. The three agents (`web_search`, `code_search`, `agno_agent`) use SurrealDB only for Agno's session/memory persistence via `get_surrealdb()`. **None of them query or write to the CAWDP tables.** The backcasting engine saves artefacts to JSON files on disk, not to `design_artefacts` or `design_input_requirements`.

This means:
- The schema is applied on startup but nothing populates it
- The EVOLVE cycle can't trigger because `runtime_evolve_triggers` is never written to
- Quality gates are never recorded in `design_quality_gates`
- The artefact dependency graph exists as a schema but has no nodes

**The schema is infrastructure without traffic.**

#### 2. No Agent That Uses the Schema

There's no agent that acts as a **CAWDP workflow orchestrator** — an agent that:
- Creates `design_workflows` records
- Writes artefacts to `design_artefacts` as phases complete
- Records quality gate results in `design_quality_gates`
- Populates `runtime_evolve_triggers` from monitoring data

The `agno_agent` in agno_agent.py is the closest candidate (it has Agno docs knowledge), but it's a general-purpose assistant, not a CAWDP workflow engine.

#### 3. No Schema-to-Code Pipeline

The schema defines `design_agent_specifications` with 10 specification sections, but there's no mechanism to **generate agent code from a specification**. The methodology says "design-to-code traceable" (S3), but the pipeline stops at the database.

### Prioritized Recommendations

| Priority | Action | Why |
|----------|--------|-----|
| **P0** | Build a CAWDP orchestrator agent that populates the schema | Without this, the schema is decorative |
| **P1** | Wire the backcasting engine to write to `design_input_requirements` and `design_artefact_dependency` | It already does the work — just needs persistence |
| **P1** | Add phase transition history table | The review correctly identifies this as the EVOLVE cycle enabler |
| **P2** | Add complementarity scores table | Core P4 output, enables analysis queries |
| **P2** | Fix `cognitive_type` enum — separate allocation from cognitive operation type | The review correctly flags 'Human-primary' as a category error |
| **P2** | Add quality gate templates | Needed for executable quality gate engine |
| **P3** | Normalize contract primitives into a separate table | Queryability for Design Studio |
| **P3** | Add missing indexes | Query performance |
| **P3** | Add event storming tables | Conditional — only needed for multi-agent workflows |

### Recommended Next Step

**Build the CAWDP orchestrator agent first.** Before adding more tables or fixing the `cognitive_type` enum, create an agent that actually uses the schema you have. This will:

1. Validate the schema against real usage (you'll find issues no review can catch)
2. Give you data to query, which drives the need for indexes and normalized tables
3. Make the EVOLVE cycle real — `runtime_evolve_triggers` needs data to trigger anything
4. Create the feedback loop that justifies the v2 additions

The backcasting engine is the natural starting point — it already has the algorithm, models, and gap detection. Wiring it to write to `design_input_requirements` and `design_artefact_dependency` would be the first concrete step toward a populated schema. 

Analyzing your answers...

Good choice — phase transition history is the foundation for the EVOLVE cycle. Let me research the exact insertion point and patterns before drafting the plan. 

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#1-1), lines 1 to 50

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#50-50), lines 50 to 250

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#80-80), lines 80 to 95

Now let me check the exact line numbers for the insertion point: 

Searched for text `agent_specifications — One row per agent` (`**/db/schema.py`), 1 result

Searched for text `agent_specifications` (`**/db/schema.py`), 20 results

Read [](file:///Users/peteargent/edgeos/cawdp-one/db/schema.py#35-35), lines 35 to 52

Now I have everything I need. Let me save the plan. 

Created memory file [](file:///Users/peteargent/Library/Application%20Support/Code/User/workspaceStorage/3795162488fe118b2e893d8b55629d40/GitHub.copilot-chat/memory-tool/memories/NzdkMmFiM2QtNGY1YS00YzZhLTljZGQtMTZhY2IwZTJmNmM2/plan.md)

Here's the plan:

---

## Plan: Add Phase Transition History Table

**TL;DR** — Add a `design_phase_transitions` table to schema.py that captures phase entry/exit, quality gate results, and iteration counts. This is the data structure that enables the EVOLVE cycle (P10→P0) to be traceable, and it's the highest-priority gap identified in the schema review.

**Steps**

1. **Add `design_phase_transitions` table definition** to `SCHEMA_SURQL` in schema.py
   - Insert after the `design_workflows` block (after line 48: `updated_at`) and before the `agent_specifications` comment (line 50)
   - Fields: `workflow`, `from_phase`, `to_phase`, `gate_result` (Passed/Failed/Skipped/Iterated), `iteration_count`, `transitioned_at`, `quality_gate` (optional record link to `design_quality_gates`)
   - Add index: `idx_phase_transitions_workflow` on `workflow` for common query pattern

2. **Update `schema-review.md`** to mark this gap as resolved

3. **Verify** — restart the app and confirm the schema applies without errors

**Relevant files**
- schema.py — insert the new table definition at line ~49 (between `design_workflows` and `design_agent_specifications`)
- schema-review.md — update the "Phase Transition History" gap status

**Verification**
1. `docker compose restart agentos-api` — check logs for `✅ CAWDP schema applied`
2. Connect to SurrealDB and run `INFO FOR TABLE design_phase_transitions;` to confirm the table exists with all fields
3. Insert a test row: `CREATE design_phase_transitions SET workflow = <workflow_id>, from_phase = 'P0', to_phase = 'P1', gate_result = 'Passed', iteration_count = 1;`
4. Query it back: `SELECT * FROM design_phase_transitions;`

**Decisions**
- Table goes in the `design_` prefix (not `runtime_`) because it tracks design-time phase progression, not runtime execution
- `quality_gate` is `option<record<design_quality_gates>>` — links to the specific gate result when a transition is gated, `NONE` for un-gated transitions
- `iteration_count` starts at 1 and increments on re-entry to the same phase (e.g., P10→P0 iteration 2)
- No `created_at`/`updated_at` needed — `transitioned_at` serves as the timestamp

***

### Response

The plan is sound in concept — phase transition history is the highest-priority schema gap because it makes the EVOLVE cycle traceable. But there are five issues that need fixing before you write the SurQL.

## Issue 1: Initial Transition Has No "From" Phase

When a workflow is created at P0, there's no preceding phase. The `from_phase` assertion `$value INSIDE ['P0','P1',...,'P10']` would reject the initial transition. Two options:

**Option A:** Allow `NONE` as the default, meaning "workflow start":
```sql
DEFINE FIELD from_phase ON design_phase_transitions TYPE string
  DEFAULT NONE;  -- NONE means "workflow start, no previous phase"
```

But then you lose the assertion validation on valid phase names.

**Option B (recommended):** Add `'START'` to the assertion:
```sql
DEFINE FIELD from_phase ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['START','P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'];
```

This makes every transition explicit — even the initial one. A P0 creation looks like `from_phase='START', to_phase='P0'`, which is clear and queryable.

## Issue 2: Missing Trigger and Actor

A phase transition needs to know *why* it happened and *who* triggered it. Without these, the EVOLVE cycle can't distinguish between:
- A human clicking "advance to next phase"
- A quality gate automatically passing
- An EVOLVE trigger cycling P10→P0

```sql
DEFINE FIELD trigger ON design_phase_transitions TYPE string
  ASSERT $value INSIDE [
    'human_decision',     -- principal or operator advanced manually
    'quality_gate_pass',  -- all required gates passed, auto-advance
    'evolve_signal',      -- P10→P0 cycle triggered by runtime signal
    'iteration_return'    -- returning to a previous phase for rework
  ];

DEFINE FIELD actor_type ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['Human','Agent','System'];

DEFINE FIELD actor_id ON design_phase_transitions TYPE string;  -- which human/agent/system
```

This links directly to the `actor_type` field already in `runtime_events` (consistent schema).

## Issue 3: Quality Gate Link Is One-to-Many, Not One-to-One

The plan links to a single `design_quality_gates` record. But CAWDP quality gates are three-layer (Fidelity/Enrichment/Cross-Cutting). A phase transition might pass multiple gate checks. The link should be to a gate *set*, not a single gate.

**Option A:** Keep the single record link but make it link to a "gate set" concept (a group of related checks for one phase transition).

**Option B (simpler, recommended):** Drop the direct record link and use a string reference instead:

```sql
DEFINE FIELD gate_result ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['Passed','Failed','Skipped','Iterated'];

DEFINE FIELD gate_summary ON design_phase_transitions TYPE object;
  -- {fidelity: 'Passed', enrichment: 'Passed', cross_cutting: 'Passed'}
  -- lightweight summary, full detail stays in design_quality_gates
```

This avoids premature normalization. The `design_quality_gates` table already has `workflow` and `phase` fields — you query it separately when you need the detail. The transition record stores the summary for quick reads.

## Issue 4: EVOLVE Trigger Link

When P10 cycles back to P0, the transition should link to the specific EVOLVE trigger that caused it. This is the P10→P0 spiral made structural:

```sql
DEFINE FIELD evolve_trigger ON design_phase_transitions TYPE record<runtime_evolve_triggers> DEFAULT NONE;
```

Only populated when `trigger='evolve_signal'`. For all other transitions, it's `NONE`. This gives you a direct traceable chain: EVOLVE trigger → phase transition → new workflow iteration.

## Issue 5: Iteration Count Should Be Computed, Not Stored

The plan says `iteration_count TYPE int DEFAULT 1`. But this creates a consistency risk — what if someone writes `2` when the actual count of previous P0 entries is `3`?

**Better approach:** Compute it at query time or use a SurrealDB function:

```sql
-- Don't store iteration_count as a field at all
-- Instead, compute it when needed:
DEFINE FUNCTION fn::phase_iteration($wf: record<design_workflows>, $phase: string) {
  SELECT count() AS iteration FROM design_phase_transitions
    WHERE workflow = $wf AND to_phase = $phase
    GROUP BY ALL;
};
```

Or if you want it stored for convenience, validate it:

```sql
DEFINE FIELD iteration_count ON design_phase_transitions TYPE int
  ASSERT $value = (SELECT count() FROM design_phase_transitions
    WHERE workflow = $parent.workflow AND to_phase = $parent.to_phase) + 1;
```

But SurrealDB assertion subqueries may not support `$parent` references. The safer bet is to compute it at query time and not store it at all. The data to compute it from is already in the table — every previous `to_phase` entry for the same workflow is a countable iteration.

## Revised Table Definition

Putting it all together:

```sql
-- phase_transitions — Tracks workflow progression through CAWDP phases
DEFINE TABLE design_phase_transitions SCHEMAFULL;

DEFINE FIELD workflow ON design_phase_transitions TYPE record<design_workflows>;
DEFINE FIELD from_phase ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['START','P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'];
DEFINE FIELD to_phase ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'];
DEFINE FIELD gate_result ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['Passed','Failed','Skipped','Iterated'];
DEFINE FIELD gate_summary ON design_phase_transitions TYPE object;
  -- {fidelity: 'Passed', enrichment: 'Passed', cross_cutting: 'Passed'}
DEFINE FIELD trigger ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['human_decision','quality_gate_pass','evolve_signal','iteration_return'];
DEFINE FIELD actor_type ON design_phase_transitions TYPE string
  ASSERT $value INSIDE ['Human','Agent','System'];
DEFINE FIELD actor_id ON design_phase_transitions TYPE string;
DEFINE FIELD evolve_trigger ON design_phase_transitions TYPE record<runtime_evolve_triggers> DEFAULT NONE;
DEFINE FIELD transitioned_at ON design_phase_transitions TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_pt_workflow ON design_phase_transitions FIELDS workflow;
DEFINE INDEX idx_pt_workflow_phase ON design_phase_transitions FIELDS workflow, to_phase;
DEFINE INDEX idx_pt_evolve ON design_phase_transitions FIELDS evolve_trigger;
```

## The Bigger Issue: Schema Without Traffic

This is the same concern from the earlier analysis — **the schema is beautiful but nothing populates it.** Adding `design_phase_transitions` is correct and necessary, but it doesn't solve the fundamental problem: no agent writes to any `design_` table.

The backcasting engine saves to JSON files. The agents use SurrealDB only for Agno session/memory persistence. The EVOLVE triggers table is empty.

Before adding more tables, I'd prioritize building the **CAWDP orchestrator agent** that:
1. Creates `design_workflows` records
2. Writes `design_phase_transitions` on every phase change
3. Populates `design_artefacts` as phases complete
4. Records `design_quality_gates` results

This would validate the schema against real usage and surface issues no review can catch. The phase transition table is structurally right — but it needs an agent that writes transitions to it.

**Recommendation:** Add the table (with the fixes above), but make the next step building the orchestrator that populates it, not adding more tables.The table definition needs those five fixes before you write it. But the bigger priority is building the agent that writes transitions to it. The schema is ready — it needs traffic.

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-05-20T12:11:34* · `glm-5.1:cloud` · `2351b7aa...`

### Prompt

what are you thoughts on this plan?

***
# Plan: CAWDP Orchestrator Agent

**TL;DR** — Build an agent (and supporting infrastructure) that populates the CAWDP schema tables. Currently 31 tables exist but nothing writes to them. This bridges the agent runtime to the schema, making the EVOLVE cycle and quality gate tracking real.

### Architecture

```
AgentOS Runtime
  └── cawdp_orchestrator (Agent)
        ├── create_workflow() tool     → design_workflows
        ├── record_transition() tool   → design_phase_transitions
        ├── record_artefact() tool     → design_artefacts + dependencies
        ├── record_gate_result() tool  → design_quality_gates
        ├── record_requirement() tool  → design_input_requirements
        └── run_backcasting() tool     → (existing, wired to SurrealDB)
```

### Phases

| Phase | What | Files | Depends On |
|-------|------|-------|------------|
| **1** | **Database writer module** — async functions that write to each CAWDP table. Encapsulates SurQL so agents don't need raw queries. | `db/writer.py` (new) | — |
| **2** | **Agno tools** — wrap writer functions as `@tool` following the closure pattern from `backcasting_engine/tool.py` | `agents/tools/cawdp_tools.py` (new) | Phase 1 |
| **3** | **Orchestrator agent** — follows the exact pattern from web_search.py with tools + instructions | `agents/cawdp_orchestrator.py` (new) | Phase 2 |
| **4** | **Wire backcasting engine** — after `trace_dependencies()`, write results to `design_input_requirements` and `design_artefact_dependency` instead of JSON files | workflow.py (modify) | Phase 1 |
| **5** | **Register** in main.py + add quick prompts to config.yaml | main.py, config.yaml (modify) | Phase 3 |

Phase 3 and Phase 4 are independent — can run in parallel after Phase 1.

### Key Design Decisions

- **Writer module first** (`db/writer.py`) — keeps SurQL in one place, tools and workflows just call Python functions
- **Closure pattern for tools** — same as `backcasting_engine/tool.py`, keeps dependency injection explicit
- **Backcasting engine stays as-is** — it just gets a persistence target. The workflow and its steps don't change
- **No frontend, no Slack, no automated EVOLVE** — deliberately excluded. This is the persistence layer only

### Verification

1. `docker compose restart cawdp-api` — confirm schema + agent load
2. Ask orchestrator: "Create a new DESIGN workflow for a code review agent" → verify `design_workflows` row
3. Ask: "Advance to P1 with gate_result=Passed" → verify `design_phase_transitions` + `current_phase` updated
4. Run backcasting workflow → verify `design_input_requirements` and `design_artefact_dependency` populated
***

### Response

The plan is 80% right — the layering, the phase dependencies, the scope exclusions, and the verification steps are all solid. But there are three issues that will bite you if you build it as written.

## Issue 1: The Tools Are CRUD, Not CAWDP

`create_workflow()`, `record_transition()`, `record_artefact()` are database inserts with an LLM tax. A user saying "Advance to P1 with gate_result=Passed" is exposing schema mechanics to a human. That's the opposite of "the methodology is invisible to the user."

**The tools should map to user actions, not table writes.**

```python
# CRUD-level (current plan)
@tool
def record_transition(workflow_id: str, from_phase: str, to_phase: str, 
                       gate_result: str): ...

# CAWDP-level (what you actually need)
@tool
def start_workflow(name: str, description: str, mode: str = "DESIGN") -> str:
    """Start a new CAWDP design run. Returns workflow ID."""
    ...

@tool  
def advance_phase(workflow_id: str, gate_summary: dict) -> str:
    """Advance the workflow to the next CAWDP phase.
    Validates current phase, records transition, updates workflow state.
    Returns new phase name."""
    ...

@tool
def save_artefact(workflow_id: str, output_id: str, name: str, 
                  content: dict, confidence: float, provenance: str) -> str:
    """Save a design artefact with epistemic metadata.
    Links to workflow's current phase automatically."""
    ...

@tool
def link_dependency(from_artefact: str, to_artefact: str, 
                    criticality: str) -> str:
    """Create a typed dependency between two artefacts.
    Enforces DAG integrity."""
    ...
```

The key difference: `advance_phase()` internally figures out `from_phase` from the workflow's `current_phase`, validates the transition is legitimate, records the transition, updates the workflow, and returns the new phase. The user (or calling agent) never needs to know phase IDs or gate structures.

## Issue 2: The Writer Must Be CAWDP-Aware, Not SQL-Passthrough

The plan says "Encapsulates SurQL so agents don't need raw queries." That's the right goal, but it needs to go further. The writer should enforce CAWDP's business rules:

```python
# db/writer.py

VALID_TRANSITIONS = {
    "START": ["P0"],
    "P0": ["P1"], "P1": ["P2"], "P2": ["P3"], "P3": ["P4"],
    "P4": ["P5"], "P5": ["P6"], "P6": ["P7"], "P7": ["P8"],
    "P8": ["P9"], "P9": ["P10"], "P10": ["P0"],  # EVOLVE cycle
}

async def advance_workflow(client: Surreal, workflow_id: str, 
                          gate_summary: dict, trigger: str,
                          actor_type: str, actor_id: str) -> str:
    """Advance workflow to next phase. Returns new phase name.
    
    Enforces:
    - Transition is valid (from current_phase to next)
    - current_phase on workflow updated atomically
    - Phase transition recorded with gate summary
    - EVOLVE trigger linked when applicable
    """
    # 1. Read current phase
    wf = await client.query(
        "SELECT current_phase FROM design_workflows WHERE id = $id",
        {"id": workflow_id}
    )
    current = wf[0]["current_phase"]
    
    # 2. Validate transition
    valid_next = VALID_TRANSITIONS.get(current, [])
    if not valid_next:
        raise ValueError(f"No valid transition from {current}")
    next_phase = valid_next[0]  # Linear for now
    
    # 3. Record transition
    await client.query(
        """CREATE design_phase_transitions SET
           workflow = $wf, from_phase = $from, to_phase = $to,
           gate_result = 'Passed', gate_summary = $gs,
           trigger = $trigger, actor_type = $actor_type,
           actor_id = $actor_id, transitioned_at = time::now()""",
        {"wf": workflow_id, "from": current, "to": next_phase,
         "gs": gate_summary, "trigger": trigger,
         "actor_type": actor_type, "actor_id": actor_id}
    )
    
    # 4. Update workflow current_phase (atomic with transition)
    await client.query(
        """UPDATE design_workflows SET current_phase = $phase,
           updated_at = time::now() WHERE id = $id""",
        {"phase": next_phase, "id": workflow_id}
    )
    
    return next_phase
```

This means the agent's tool just calls `advance_workflow()` and gets back `"P1"`. The LLM never needs to know about transition validation, atomic state updates, or valid phase sequences.

## Issue 3: Backcasting → Graph Is Not a Simple Persistence Swap

Phase 4 says "wire backcasting engine to write to SurrealDB instead of JSON." But the backcasting engine produces flat dependency pairs, and `design_artefact_dependency` is a **RELATION type**. This requires SurrealDB's `RELATE` syntax:

```sql
-- Not an INSERT — a RELATION
RELATE design_artefacts:abc123->design_artefact_dependency->design_artefacts:def456 SET
  criticality = 'CRITICAL',
  satisfaction_mode = 'DIRECT',
  confidence = 0.95,
  freshness = time::now();
```

The writer module needs a `link_artefact_dependency()` function that:
1. Ensures both artefact records exist in `design_artefacts`
2. Creates the RELATION with metadata
3. Relies on the existing `check_dag_on_relate` event for cycle detection

The current backcasting engine would need its output models mapped to this function. It's not a drop-in replacement for JSON — it's a transformation from flat pairs to graph edges.

## Revised Architecture

```
db/writer.py (Phase 1)
  ├── start_workflow()         → design_workflows + initial transition
  ├── advance_workflow()      → design_phase_transitions + current_phase update
  ├── save_artefact()         → design_artefacts with CC-3 metadata
  ├── link_dependency()       → design_artefact_dependency RELATION
  ├── save_gate_result()      → design_quality_gates
  ├── save_requirement()      → design_input_requirements
  └── get_workflow_state()    → read current phase, artefacts, gates

agents/tools/cawdp_tools.py (Phase 2)
  ├── start_workflow_tool     → wraps writer.start_workflow()
  ├── advance_phase_tool      → wraps writer.advance_workflow()
  ├── save_artefact_tool      → wraps writer.save_artefact()
  ├── link_dependency_tool    → wraps writer.link_dependency()
  └── run_backcasting_tool    → wraps writer (Phase 4)

agents/cawdp_orchestrator.py (Phase 3)
  └── Uses tools above, instructions enforce CAWDP phase logic

workflows/tools/backcasting_engine/ (Phase 4)
  └── After trace_dependencies(), call writer.link_dependency()
     and writer.save_requirement() instead of JSON dump
```

## What the Plan Gets Right (Keep These)

- **Writer module first** — correct layering, SurQL in one place
- **Closure pattern** — consistent with existing codebase
- **Phase 3 and 4 parallel after Phase 1** — correct dependency analysis
- **Scope exclusion** — no frontend, no Slack, no automated EVOLVE
- **Verification steps** — concrete and testable (with the improvement that users shouldn't speak schema language)

## One More Thing: The Orchestrator Is the Engine, Not the Surface

From your design patterns: **Surface + Engine**. The CAWDP orchestrator is the *engine* — it writes to the database and enforces business rules. The *surface* is the user-facing agent (the Agent Designer Agent, or the Milestone 1 Mirror agent) that guides the user through the conversation.

The current plan positions the orchestrator as a user-facing agent. But a user shouldn't say "advance to P1" — they should say "I've finished describing what this agent is for." The surface agent translates user intent into orchestrator calls.

For v1, it's fine to have the orchestrator be directly callable (for testing). But the architecture should anticipate that a surface agent will sit in front of it. This means the tools need to be CAWDP-aware enough that a surface agent can call them without understanding schema internals.

Want me to draft `db/writer.py` with the CAWDP-aware functions, or start with the tool definitions in `agents/tools/cawdp_tools.py`?The three issues are architectural, not cosmetic. Building CRUD-level tools means you'll rebuild them in two weeks when you realize users shouldn't know about phase IDs. Building a SQL-passthrough writer means the LLM is doing business rule enforcement it shouldn't be trusted with. Skipping the RELATE transformation means the backcasting wiring won't work.

The plan's layering, phasing, scope exclusions, and verification steps are all correct. Just elevate the tools and writer to CAWDP-awareness and it'll work first time.

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-05-20T21:31:39* · `glm-5.1:cloud` · `74c89e18...`

### Prompt

What's your advice for implementing the Complementarity scores tool?

### Response

Let me think through this from first principles — what the tool actually needs to do, how it connects to the schema, and where it fits in the writer/tool/agent layering.

## What the Complementarity Score Tool Does

It's a Phase 4 (ALLOCATE) tool. An agent scores each task across multiple capability dimensions for Human, Agent, and System. The gap between scores determines the allocation recommendation. The agent prepares the scores; the human makes the allocation decision.

This is an **Assessor-class** operation — it never finalizes allocation.

## The Scoring Dimensions

The dimensions should be flexible per use case, but you need sensible defaults. From your CAWDP applications across six agents, these dimensions recur:

```python
DEFAULT_DIMENSIONS = {
    "ethical_judgment":     "Can this actor make ethical decisions about this task?",
    "domain_expertise":    "Does this actor have the domain knowledge this task requires?",
    "pattern_recognition": "Can this actor spot patterns across data?",
    "consistency":         "Can this actor produce identical results every time?",
    "scale":              "Can this actor handle volume without quality loss?",
    "speed":              "How fast can this actor complete this task?",
    "creativity":         "Can this actor generate novel, appropriate outputs?",
    "empathy":            "Can this actor understand and respond to human needs?",
}
```

Different use cases add domain-specific dimensions. The competitive intelligence workflow added "adversarial awareness." The educational tutor added "scaffolding intuition." The tool should accept custom dimensions.

## The Gap Calculation

The gap is the difference between the **highest-scoring actor** and the **second-highest** for a given task. A large gap means one actor is clearly superior. A small gap means actors are comparable (collaborative candidate).

```
For a single task:
  Human scores:  [9, 8, 7, 3, 2, 2, 5, 9]  (ethical, domain, pattern, consistency, scale, speed, creativity, empathy)
  Agent scores:  [2, 5, 8, 9, 9, 9, 6, 1]
  System scores: [1, 1, 3, 9, 9, 9, 1, 1]

  Average Human: 5.6
  Average Agent: 6.1
  Average System: 4.3
  
  Gap (Human vs Agent): |5.6 - 6.1| = 0.5  → Collaborative
  Gap (Human vs System): |5.6 - 4.3| = 1.3
  Gap (Agent vs System): |6.1 - 4.3| = 1.8
```

But average-based gaps lose dimension-level detail. A task where Human scores 9 on ethical judgment and 2 on consistency should be flagged differently from one where Human scores 5 on everything.

**Better approach: dimension-level gaps, then aggregate.**

```python
@dataclass
class DimensionScore:
    dimension: str
    human: int      # 1-10
    agent: int      # 1-10
    system: int     # 1-10

    @property
    def highest_actor(self) -> str:
        scores = {"Human": self.human, "Agent": self.agent, "System": self.system}
        return max(scores, key=scores.get)

    @property
    def gap(self) -> int:
        """Gap between highest and second-highest."""
        scores = sorted([self.human, self.agent, self.system], reverse=True)
        return scores[0] - scores[1]

    @property
    def allocation_hint(self) -> str:
        """Single-dimension allocation hint based on gap."""
        if self.human >= 8 and self.gap >= 6:
            return "Human-only"    # e.g., ethical judgment H:9, A:2, gap=7
        if self.agent >= 8 and self.gap >= 6:
            return "Agent-primary"  # e.g., consistency A:9, H:2, gap=7
        if self.system >= 8 and self.gap >= 6:
            return "System-primary"
        if self.gap <= 2:
            return "Collaborative"  # comparable capabilities
        return self.highest_actor + "-leaning"
```

## The Allocation Decision

The task-level allocation comes from the dimension-level pattern, not a single aggregate score:

```python
@dataclass
class TaskAllocation:
    task_id: str
    dimensions: list[DimensionScore]
    recommended_allocation: str
    confidence: float
    rationale: str
    human_gate_required: bool   # any dimension where gap >= 6 and Human leads?
    
    @property
    def has_human_only_dimension(self) -> bool:
        return any(d.human >= 8 and d.gap >= 6 for d in self.dimensions)
    
    @property 
    def has_agent_only_dimension(self) -> bool:
        return any(d.agent >= 8 and d.gap >= 6 for d in self.dimensions)
```

The key rule from your methodology: **if any dimension has Human gap ≥ 6, the task requires human involvement (human-only or collaborative).** A single high-stakes dimension vetoes full agent autonomy, regardless of how many other dimensions favour the agent.

## How It Connects to the Schema

You have two storage targets:

**1. `design_tasks` (existing table)** — already has `human_scores`, `agent_scores`, `system_scores` (as objects), `complementarity_gap`, `allocated_to`, and `cognitive_type`.

**2. `design_complementarity_scores` (missing table — P1 gap)** — you need this for dimension-level scoring. The current `design_tasks` stores aggregate objects but can't be queried per-dimension.

Add the table:

```sql
DEFINE TABLE design_complementarity_scores SCHEMAFULL;

DEFINE FIELD task ON design_complementarity_scores TYPE record<design_tasks>;
DEFINE FIELD workflow ON design_complementarity_scores TYPE record<design_workflows>;
DEFINE FIELD dimension_name ON design_complementarity_scores TYPE string;
DEFINE FIELD human_score ON design_complementarity_scores TYPE int
  ASSERT $value >= 1 AND $value <= 10;
DEFINE FIELD agent_score ON design_complementarity_scores TYPE int
  ASSERT $value >= 1 AND $value <= 10;
DEFINE FIELD system_score ON design_complementarity_scores TYPE int
  ASSERT $value >= 1 AND $value <= 10;
DEFINE FIELD gap ON design_complementarity_scores TYPE int;
DEFINE FIELD allocation_hint ON design_complementarity_scores TYPE string;
DEFINE FIELD scored_by ON design_complementarity_scores TYPE string;
DEFINE FIELD scored_at ON design_complementarity_scores TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_cs_task ON design_complementarity_scores FIELDS task;
DEFINE INDEX idx_cs_task_dim ON design_complementarity_scores FIELDS task, dimension_name UNIQUE;
```

The UNIQUE index on `(task, dimension_name)` prevents duplicate dimension scores for the same task.

## The Writer Function

Following the CAWDP-aware writer pattern:

```python
# db/writer.py

GAP_THRESHOLD = 6  # From CAWDP methodology: 6+ = human-only dimension

async def score_task_complementarity(
    client: Surreal,
    task_id: str,
    workflow_id: str,
    dimensions: list[dict],  # [{name, human, agent, system}, ...]
    scored_by: str,
) -> dict:
    """Score a task's complementarity across dimensions.
    
    Enforces:
    - All scores 1-10
    - No duplicate dimensions per task
    - Gap calculated correctly
    - Allocation hints derived from gap + threshold
    - Human-only dimensions flagged
    - Aggregate allocation proposed
    
    Returns: {recommended_allocation, confidence, rationale, 
              human_gate_required, dimension_count}
    """
    # 1. Validate scores
    for d in dimensions:
        for actor in ["human", "agent", "system"]:
            if not (1 <= d[actor] <= 10):
                raise ValueError(f"{d['name']}: {actor} score {d[actor]} out of range 1-10")
    
    # 2. Calculate gaps and hints per dimension
    scored_dims = []
    human_only_dims = []
    for d in dimensions:
        scores = sorted([d["human"], d["agent"], d["system"]], reverse=True)
        gap = scores[0] - scores[1]
        
        if d["human"] >= 8 and gap >= GAP_THRESHOLD:
            hint = "Human-only"
            human_only_dims.append(d["name"])
        elif d["agent"] >= 8 and gap >= GAP_THRESHOLD:
            hint = "Agent-primary"
        elif d["system"] >= 8 and gap >= GAP_THRESHOLD:
            hint = "System-primary"
        elif gap <= 2:
            hint = "Collaborative"
        else:
            leader = max(
                [("Human", d["human"]), ("Agent", d["agent"]), ("System", d["system"])],
                key=lambda x: x[1]
            )[0]
            hint = f"{leader}-leaning"
        
        scored_dims.append({
            "dimension_name": d["name"],
            "human_score": d["human"],
            "agent_score": d["agent"],
            "system_score": d["system"],
            "gap": gap,
            "allocation_hint": hint,
        })
    
    # 3. Determine task-level allocation
    if human_only_dims:
        recommended = "Human" if len(human_only_dims) >= 2 else "Collaborative"
        rationale = f"Human-required dimensions: {', '.join(human_only_dims)}"
        confidence = 0.85 + 0.05 * len(human_only_dims)  # more human dims = higher confidence
    else:
        # Weight by dimension count
        hints = [d["allocation_hint"] for d in scored_dims]
        agent_count = sum(1 for h in hints if "Agent" in h)
        system_count = sum(1 for h in hints if "System" in h)
        collab_count = sum(1 for h in h == "Collaborative" for h in hints)
        
        if agent_count > system_count + collab_count:
            recommended = "Agent"
        elif system_count > agent_count + collab_count:
            recommended = "System"
        else:
            recommended = "Collaborative"
        rationale = f"Dimension pattern: {agent_count}A/{system_count}S/{collab_count}C"
        confidence = 0.6  # Less confident when no human-only dims
    
    # 4. Write dimension scores to design_complementarity_scores
    for sd in scored_dims:
        await client.query(
            """CREATE design_complementarity_scores SET
               task = $task, workflow = $wf,
               dimension_name = $dim, human_score = $h,
               agent_score = $a, system_score = $s,
               gap = $gap, allocation_hint = $hint,
               scored_by = $by, scored_at = time::now()""",
            {"task": task_id, "wf": workflow_id, **sd, "by": scored_by}
        )
    
    # 5. Update design_tasks with aggregate allocation
    await client.query(
        """UPDATE design_tasks SET
           human_scores = $h_scores, agent_scores = $a_scores,
           system_scores = $s_scores, complementarity_gap = $max_gap,
           allocated_to = $alloc, updated_at = time::now()
           WHERE id = $id""",
        {
            "id": task_id,
            "h_scores": {d["dimension_name"]: d["human"] for d in dimensions},
            "a_scores": {d["dimension_name"]: d["agent"] for d in dimensions},
            "s_scores": {d["dimension_name"]: d["system"] for d in dimensions},
            "max_gap": max(d["gap"] for d in scored_dims),
            "alloc": recommended,
        }
    )
    
    return {
        "recommended_allocation": recommended,
        "confidence": round(confidence, 2),
        "rationale": rationale,
        "human_gate_required": len(human_only_dims) > 0,
        "dimension_count": len(scored_dims),
        "human_only_dimensions": human_only_dims,
    }
```

## The Agno Tool

Following the closure pattern and user-action naming:

```python
# agents/tools/cawdp_tools.py

from agno.tools import tool as agno_tool
from db.writer import score_task_complementarity, DEFAULT_DIMENSIONS

def make_complementarity_tool(client_getter):
    """Create complementarity scoring tool with injected SurrealDB client."""
    
    @agno_tool(
        name="score_task_allocation",
        description=(
            "Score a task's complementarity across Human/Agent/System capabilities. "
            "Returns recommended allocation with rationale. "
            "Agent PREPARES the scores — human MAKES the allocation decision."
        ),
    )
    def score_task_allocation(
        task_id: str,
        workflow_id: str,
        dimensions: list[dict] | None = None,
        custom_dimensions: list[str] | None = None,
    ) -> str:
        """Score a task for complementarity allocation.
        
        Args:
            task_id: The task record ID
            workflow_id: The workflow this task belongs to
            dimensions: Optional list of {name, human, agent, system} scores (1-10 each).
                       If not provided, uses default dimensions and the agent must estimate scores.
            custom_dimensions: Optional dimension names to add to defaults.
        
        Returns:
            JSON string with recommended_allocation, confidence, rationale,
            human_gate_required, and dimension scores.
        """
        # Build dimension list
        if dimensions is None:
            # Agent needs to score — return dimension names for LLM to estimate
            dims_to_score = list(DEFAULT_DIMENSIONS.keys())
            if custom_dimensions:
                dims_to_score.extend(custom_dimensions)
            return json.dumps({
                "action": "estimate_scores",
                "dimensions": dims_to_score,
                "scale": "1-10 per actor per dimension",
                "hint": "For each dimension, estimate Human/Agent/System capability (1-10) and call again with dimensions populated."
            })
        
        client = client_getter()
        result = asyncio.run(score_task_complementarity(
            client=client,
            task_id=task_id,
            workflow_id=workflow_id,
            dimensions=dimensions,
            scored_by="cawdp_orchestrator",
        ))
        
        return json.dumps(result, indent=2)
    
    return score_task_allocation
```

Notice the two-call pattern: if the caller doesn't provide scores, the tool returns the dimension names and asks the LLM to estimate them. The LLM then calls back with populated scores. This keeps the tool honest — it doesn't invent scores, the LLM does.

## The Orchestrator Instructions

The orchestrator's system prompt should include the CAWDP allocation rules so it scores correctly:

```
When scoring task complementarity:
1. Score each dimension 1-10 for Human, Agent, and System
2. Ethical judgment and values alignment are almost always Human-superior (8-10)
3. Consistency, scale, and speed are almost always Agent/System-superior (8-10)
4. Domain expertise varies — if the task requires deep domain knowledge that only the principal has, Human scores high
5. Pattern recognition varies — agents are strong on data patterns, humans on contextual patterns
6. If Human gap ≥ 6 on ANY dimension, the task requires human involvement
7. You PREPARE scores and recommended allocation — you NEVER finalize allocation
8. Always flag which dimensions drove the recommendation
9. If uncertain about a score, score lower and flag uncertainty in rationale
```

## What Not To Do

1. **Don't let the tool auto-allocate.** The tool proposes; human decides. The `allocated_to` field on `design_tasks` should only be set after human review of the complementarity scores.

2. **Don't hardcode dimensions per cognitive type.** Mechanical tasks favour Agent/System, but not on every dimension. Let the scores determine the pattern, not assumptions.

3. **Don't aggregate too early.** Dimension-level scores are more valuable than task-level averages. The `design_complementarity_scores` table exists precisely so you can query per-dimension later.

4. **Don't skip the gap threshold.** The 6-point threshold isn't arbitrary — it came from your assignment marking workflow analysis where gap ≥ 6 reliably identified human-only subtasks. Changing it requires empirical evidence.

## Build Order

1. Add `design_complementarity_scores` table to `schema.py`
2. Add `score_task_complementarity()` to `db/writer.py`
3. Add `score_task_allocation` tool to `agents/tools/cawdp_tools.py`
4. Add allocation rules to orchestrator instructions
5. Test: create a task, score it, verify dimension records in SurrealDB, verify task updated with aggregate

Want me to draft the schema addition and writer function as ready-to-merge code?

---

## Run 6 — Agentic Expert ✓ COMPLETED

*2026-05-20T21:53:40* · `glm-5.1:cloud` · `0b188183...`

### Prompt

Let's take a step back and look at what we're trying to do here before jumping to code.

We want to be able to assign the best actor to the task at hand. An agent should never do what a human is better at, and a human should never have to do what an agent is better at.

If an agent just goes of 'cognitive operation' strengths scores, though, we often hist this problem I saw this week where the scores say the human should do the task, but it didn't take into consideration that humans struggle to imagine what could go wrong if they don't have a lot of experience to have seen what could go wrong, or find it difficult to know exactly what they want until they are offered what they don't want. See this table where it was marked as "human only" but should be collaborative.

| ID | Task | Type | H | A | S | Gap | Allocation | Authority | If Wrong Actor |
|---|---|---|---|---|---|---|---|---|---|
| T1.1 | Discover principal's purpose | Intuitive | 10 | 2 | 0 | 8 | **Human-only** | Human | Agent suggests purpose → specification capture |
| T1.2 | Identify what this workflow IS | Intuitive | 10 | 2 | 0 | 8 | **Human-only** | Human | Agent defines identity → template-filling, not genuine |
| T1.4 | Discover what would violate identity | Intuitive | 10 | 3 | 0 | 7 | **Human-only** | Human | Agent generates never-rules → generic boundaries, not identity-specific |
| T2.1 | Define "excellent outcomes" | Intuitive | 10 | 2 | 0 | 8 | **Human-only** | Human | Agent defines excellence → generic metrics, not domain-specific |
| T4.1 | Identify authority boundaries | Evaluative | 9 | 3 | 1 | 6 | **Human-only** | Human | Agent identifies boundaries → generic boundaries, not domain-specific |


Perhaps the strengths scores can give good results as a first pass. Perhaps the agent performing the complementarity assignments can then ask questions about each task to understand if there are other conditions related to the task that might change the assignment.

What other methods could be applied to help us find more nuance and strengthen this element of the framework?

### Response

You've identified the exact failure mode. The gap score says "human is better at this" and stops there. But "better at" isn't the same as "should do alone."

## Why the Gap Score Fails on These Tasks

Look at your five tasks. The gap score says "Human-only" because the human scores 9-10 on intuitive/evaluative dimensions. That's true — the human IS better at these. But the gap score doesn't capture *why* collaborative is still right:

| Task | What the score sees | What the score misses |
|------|-------------------|---------------------|
| T1.1 Discover purpose | Human is better at knowing their own purpose | Human can't cold-start without prompting. They need something to react to |
| T1.2 Identify what this IS | Human has the intuitive grasp | Human faces a blank page. Agent can offer patterns that unlock genuine thinking |
| T1.4 Discover violations | Human knows their own boundaries | Human may not have encountered enough edge cases to know what violates identity. Agent has seen thousands of failure patterns |
| T2.1 Define excellence | Human knows what "good" looks like | Human struggles to articulate excellence upfront. Agent can propose options that surface the human's real preferences |
| T4.1 Identify boundaries | Human has evaluative judgment | Same as T1.4 — the human hasn't seen enough failure modes to draw boundaries accurately without help |

The pattern is the same every time: **the human has the judgment, but the human needs preparation to exercise it.** The gap score measures capability. It doesn't measure cold-start difficulty, experience dependency, or preparation value.

## The Two-Factor Model

The complementarity gap is the **capability** dimension. You need a second dimension: **preparation need**.

```
                    PREPARATION NEED
                    LOW          HIGH
              ┌─────────────┬─────────────┐
         HIGH │  Human-only │ Collaborative│  ← All five tasks are HERE
CAPABILITY  │  (gap ≥ 6,  │  (human has  │
  GAP       │  human can  │  judgment but │
              │  do alone)  │  needs prep) │
              ├─────────────┼─────────────┤
         LOW │  System /   │  Collaborative│
              │  Agent      │  (agent      │
              │  (gap ≥ 6,  │  prepares,   │
              │  can auto)  │  human still  │
              │             │  decides)     │
              └─────────────┴─────────────┘
```

This reframes your five tasks: they're all HIGH capability gap + HIGH preparation need. The gap score puts them in "Human-only" but the preparation factor moves them to "Collaborative."

## Five Adjustment Factors

Here are five factors that modify the gap-based allocation. Each one can shift a task from "Human-only" to "Collaborative":

### 1. Cold Start Difficulty

Can the human begin this task without prompting, scaffolding, or examples?

| Score | Meaning |
|-------|---------|
| Low | Human can start immediately from their own knowledge |
| Medium | Human benefits from structure but can start without it |
| High | Human faces a blank page. Needs prompts, patterns, or options to react to |

All five of your tasks score **High** on cold start. "Discover principal's purpose" — where do you even begin? The agent offers patterns; the human recognizes which one fits.

**Allocation shift:** High cold start → always collaborative, regardless of gap score.

### 2. Experience Dependency

Does the human have enough domain experience to do this task well without the agent's broader pattern recognition?

| Score | Meaning |
|-------|---------|
| Low | Human has extensive domain experience and has seen many edge cases |
| Medium | Human has some experience but may not have encountered all failure modes |
| High | Human is in unfamiliar territory. Agent's broad training data is a genuine asset |

T1.4 and T4.1 score **High** on experience dependency. The human may not know what could violate identity or where boundaries should be because they haven't seen enough examples. The agent has seen thousands of boundary violations and can surface failure modes the human wouldn't think of.

**Allocation shift:** High experience dependency → collaborative, with agent preparing options and the human selecting/validating.

### 3. Discovery vs Decision

Is this task about discovering what you want (open-ended), or deciding between known options (constrained)?

| Score | Meaning |
|-------|---------|
| Decision | Options are known. Human selects from clear choices. |
| Mixed | Some options are known, some need discovery. |
| Discovery | Human doesn't know what they want until they see what they don't want. |

T1.1, T1.2, T2.1 are **Discovery** tasks. You can't choose your purpose from a menu — you discover it by reacting to options that feel right or wrong.

**Allocation shift:** Discovery tasks → collaborative, with agent preparing options and human refining/rejecting.

### 4. Preparation Value

Would agent preparation significantly improve the human's output quality, even if the human could do it alone?

| Score | Meaning |
|-------|---------|
| Low | Agent preparation adds minimal value. Human does it better alone. |
| Medium | Agent preparation saves time but doesn't change output quality. |
| High | Agent preparation changes the quality of the output. Without it, the human produces worse results. |

T1.4 "Discover what would violate identity" scores **High**. The agent can propose boundaries based on patterns from thousands of designs. The human validates which ones apply. Without the agent's preparation, the human might miss boundaries they haven't encountered.

**Allocation shift:** High preparation value → collaborative, because the output quality changes.

### 5. Reversibility

If the wrong allocation is made and the task goes wrong, how hard is it to correct?

| Score | Meaning |
|-------|---------|
| High | Easy to undo. Wrong allocation has low cost. |
| Medium | Possible to undo but with effort. |
| Low | Irreversible or very costly. Identity-level decisions can't be easily redone. |

T1.1-T1.4 score **Low** on reversibility. A wrong purpose or identity specification cascades through every subsequent design decision. This means the human MUST have final authority — but it also means the human needs the best possible preparation to get it right.

**Allocation shift:** Low reversibility → human has final authority, but collaborative preparation is MORE important (not less) because the cost of error is high.

## The Adjusted Allocation Process

This gives you a two-pass process:

**Pass 1: Gap Score (Capability)**
Score each dimension 1-10 for H/A/S. Calculate gaps. Propose initial allocation.

**Pass 2: Adjustment Factors (Preparation Need)**
For each task, assess the five factors. Any factor rated "High" that shifts toward collaboration overrides the gap-based allocation.

```
For each task:
  1. Calculate gap-based allocation (existing method)
  2. Assess cold start, experience dependency, discovery vs decision,
     preparation value, reversibility
  3. If ANY adjustment factor is High AND shifts toward collaboration:
     → Override to "Collaborative" with human final authority
  4. If reversibility is Low:
     → Human MUST have final authority (regardless of other factors)
  5. Document WHY the allocation shifted, not just that it did
```

Applied to your five tasks:

| Task | Gap Allocation | Cold Start | Experience | Discovery | Prep Value | Reversibility | Adjusted Allocation | Rationale |
|------|---------------|------------|------------|-----------|------------|---------------|-------------------|-----------|
| T1.1 | Human-only | High | — | Discovery | High | Low | **Collaborative** | Human has judgment but faces blank page. Agent proposes, human selects |
| T1.2 | Human-only | High | — | Discovery | High | Low | **Collaborative** | Same pattern — identity discovery needs prompting |
| T1.4 | Human-only | High | High | — | High | Low | **Collaborative** | Human may not have seen enough edge cases. Agent surfaces failure patterns |
| T2.1 | Human-only | High | — | Discovery | High | Low | **Collaborative** | Excellence is discovered through reaction, not specified from blank page |
| T4.1 | Human-only | — | High | Mixed | High | Low | **Collaborative** | Boundaries benefit from broad pattern recognition. Human validates |

Notice the rationale is different for each. The adjustment isn't "all of these are collaborative" — it's "each is collaborative for a different reason." That rationale matters because it determines *how* the collaboration works:

- Cold start difficulty → agent provides options, human selects
- Experience dependency → agent surfaces patterns, human validates
- Discovery → agent proposes, human refines
- Preparation value → agent prepares, human decides
- Low reversibility → human has final authority, but agent preparation is critical

## What This Means for the Tool

The complementarity scoring tool needs three calls, not one:

```
Call 1: Score cognitive dimensions (existing gap method)
Call 2: Assess adjustment factors for any task rated "Human-only" or close to the threshold
Call 3: Present adjusted allocation with rationale
```

The adjustment factors can be simple assessments — the agent doesn't need to score them 1-10. A simpler approach:

```
For each "Human-only" task, answer five questions:
1. Can the human start this without prompting? (Yes/Partially/No)
2. Does the human have deep experience with this type of decision? (Yes/Some/No)
3. Is this about discovering what you want, or choosing between known options? (Decision/Mixed/Discovery)
4. Would agent preparation change the quality of the output? (No/Somewhat/Yes)
5. If this goes wrong, how hard is it to correct? (Easy/Medium/Hard)

If 2+ answers are in the "needs help" column → Collaborative, with human final authority
If reversibility is Hard → Human final authority (always), regardless of other factors
```

This is the agent *preparing judgment* for the human *making judgment* on allocation — the same principle applied to the allocation process itself.

The gap score gives you a defensible starting point. The adjustment factors give you the nuance that prevents the exact error you identified: marking discovery tasks as "Human-only" when they're collaborative because the human needs preparation to exercise their superior judgment.

Want me to fold this into the complementarity tool design, or should we first test the adjustment framework against more of your existing task allocations to validate it?

---

## Run 7 — Agentic Expert ✓ COMPLETED

*2026-05-20T22:21:16* · `glm-5.1:cloud` · `e939446d...`

### Prompt

I like all this. however, this helped me see that there is potentially another approach or potentially important prior step we could optimise here - the task decomposition and cognitive operation assignment steps.

Even just the wording of T1.1, "Discover principal's purpose", is not necessarily a great way to title or think about the task here. And then we compound problems by assigning an actor before we have really understood what is needed as outcomes from this subtask. 

It's like in this example we had one agent decomposing tasks, assigning cognitive operations and processing complementarity all in one operation which has led to issues. So even if we improve the process with your suggestions, there could be a compounding of problems that the new decision matrix builds upon.

A few potential improvement areas:
1. Would more agents doing these steps rather than being done in one produce better results?
2. Could tools or rules or perhaps agent skills produce better task decomposition results? What does a great decomposed subtask look like for better assignment results?
3. Are there opportunities to improve cognitive modality assignment?

### Response

You've found the root cause. The complementarity scoring problem is a *downstream symptom* of an upstream decomposition problem. If the tasks are badly defined and badly typed, no scoring method will produce good allocations.

Let me work through each of your three questions.

## 1. Should These Steps Use Separate Agents?

Yes, and for a specific reason: class collision. The three steps are genuinely different cognitive operations with different failure modes:

| Step | Cognitive Operation | Agent Class | Failure Mode |
|------|-------------------|-------------|-------------|
| Task decomposition | Generative | Generator | Over-decomposition, under-decomposition, conflation |
| Cognitive type assignment | Analytical | Measurer | Misclassification, over-simplification |
| Complementarity analysis | Evaluative | Assessor | Overt classification, missing preparation need |

When one agent does all three, it creates the same problem you identified: it decomposes, types, and allocates in one pass, and each step's errors compound into the next. The decomposition shapes what the typing sees, which shapes what the allocation scores. A bad decomposition cascades.

But more agents isn't automatically better. The right structure is:

```
Generator (Decomposer) → produces subtasks
        ↓
Measurer (Typer) → assigns cognitive operations
        ↓
Assessor (Complementarity Analyst) → scores and allocates
        ↓
Human Gate → validates allocation
```

Each agent has a single authority boundary: the Decomposer never judges quality, the Typer never allocates actors, the Assessor never changes the decomposition. And critically, each step can be reviewed and corrected before the next step compounds its errors.

## 2. What Does a Great Decomposed Subtask Look Like?

This is the most important question. Let me show you the problem with the current tasks and then what well-decomposed tasks look like.

### The Problem: Conflated Tasks

"Discover principal's purpose" is actually three cognitive operations jammed into one task:

| Hidden inside T1.1 | Cognitive Operation | Who's Better |
|-------------------|--------------------|--------------|
| Elicit the principal's purpose from conversation | Intuitive + Elicitive | Human knows, agent needs to ask |
| Structure the elicited purpose into a specification | Analytical | Agent is better at structuring |
| Validate the specification captures the real intent | Evaluative | Human must confirm |

The current decomposition calls this "Intuitive" and assigns it to Human-only. But only the first and third sub-operations are genuinely intuitive. The second is analytical and could be done by an agent.

### What a Well-Decomposed Task Looks Like

A well-decomposed task should have five properties:

**1. Single primary cognitive operation**

One verb, one thinking type. If you need "and" to describe what the task does, it's conflated.

| Bad (conflated) | Good (decomposed) |
|-----------------|-------------------|
| "Discover principal's purpose" | "Elicit the principal's purpose through guided conversation" |
| "Identify what this workflow IS" | "Structure the principal's description into a purpose specification" |
| "Define excellent outcomes" | "Propose outcome criteria based on domain patterns" |

**2. Clear output artefact**

What concrete thing does this task produce?

| Bad (vague output) | Good (specific artefact) |
|--------------------|------------------------|
| "Discover purpose" | "Purpose statement — one sentence capturing why this agent exists" |
| "Identify what this IS" | "Identity specification — 4 identity questions answered" |
| "Define excellent outcomes" | "Outcome criteria — measurable success conditions with thresholds" |

**3. Explicit preparation need**

Does the human need prompting, or can they start cold?

| Cold Start Level | Meaning | Implication |
|-----------------|---------|------------|
| Self-starting | Human can produce the artefact from their own knowledge | May be human-only if gap ≥ 6 |
| Scaffolded | Human needs structure or prompts to begin | Always collaborative — agent provides scaffold, human fills in |
| Discovery | Human discovers what they want by reacting to options | Always collaborative — agent proposes, human refines |

**4. Explicit authority boundary**

Who makes the final call on this task's output?

| Authority | Meaning |
|-----------|---------|
| Human-only | Human produces the output, agent may prepare but doesn't contribute to content |
| Human-final | Agent prepares, human decides. Collaborative. |
| Agent-primary | Agent produces, human reviews. Collaborative. |
| System-enforced | Automated with human override. |

**5. Failure mode**

What does "wrong" look like for this specific task?

| Task | Failure Mode | If Wrong Actor |
|------|-------------|----------------|
| Elicit purpose | Generic purpose that doesn't capture real intent | Agent suggests → template-filling |
| Structure purpose | Purpose stays as vague description, never becomes specification | Human struggles → blank page |
| Validate purpose | Purpose looks right but misses the real intent | Agent validates → rubber-stamping |

### Re-Decomposed: The Five Tasks

Let me re-decompose the five "Human-only" tasks using these properties:

**T1.1 "Discover principal's purpose" → Two tasks:**

| ID | Task | Primary Operation | Output Artefact | Cold Start | Authority | Failure If Wrong |
|----|------|------------------|----------------|-----------|-----------|-----------------|
| T1.1a | Elicit principal's purpose through guided conversation | Elicitive (Intuitive) | Raw purpose notes | Discovery — human discovers by reacting | Human-final | Agent suggests purpose → template-filling |
| T1.1b | Structure raw purpose notes into a purpose specification | Analytical | Purpose specification document | Self-starting (has input) | Agent-primary with human review | Human structures → blank page, low quality |

T1.1a is collaborative (discovery). T1.1b is collaborative (agent-primary with human review). Neither is "human-only" once you see the decomposition.

**T1.2 "Identify what this workflow IS" → Two tasks:**

| ID | Task | Primary Operation | Output Artefact | Cold Start | Authority | Failure If Wrong |
|----|------|------------------|----------------|-----------|-----------|-----------------|
| T1.2a | Present identity pattern options and collect reactions | Elicitive | Identity pattern selection + reactions | Discovery — human reacts to options | Human-final | Agent defines identity → generic, not genuine |
| T1.2b | Draft identity specification from selected pattern + reactions | Analytical | Identity specification (4 questions) | Scaffolded — has pattern + reactions | Agent-primary with human review | Human drafts → blank page, incomplete |

**T1.4 "Discover what would violate identity" → Two tasks:**

| ID | Task | Primary Operation | Output Artefact | Cold Start | Authority | Failure If Wrong |
|----|------|------------------|----------------|-----------|-----------|-----------------|
| T1.4a | Propose identity boundary violations based on pattern library | Generative | Proposed never-rules list | Self-starting — agent has pattern library | Agent-primary | Human proposes from blank → misses boundaries they haven't encountered |
| T1.4b | Validate and refine proposed never-rules against real identity | Evaluative | Finalized never-rules with rationale | Self-starting — has proposals to evaluate | Human-final | Agent validates → generic, not domain-specific |

**T2.1 "Define excellent outcomes" → Two tasks:**

| ID | Task | Primary Operation | Output Artefact | Cold Start | Authority | Failure If Wrong |
|----|------|------------------|----------------|-----------|-----------|-----------------|
| T2.1a | Propose outcome criteria based on domain patterns | Generative | Proposed criteria list with thresholds | Self-starting — agent has patterns | Agent-primary | Human defines from blank → generic or incomplete |
| T2.1b | Validate and prioritise proposed criteria | Evaluative | Prioritised criteria with human rationale | Self-starting — has proposals to evaluate | Human-final | Agent prioritises → wrong weight on wrong criteria |

**T4.1 "Identify authority boundaries" → Two tasks:**

| ID | Task | Primary Operation | Output Artefact | Cold Start | Authority | Failure If Wrong |
|----|------|------------------|----------------|-----------|-----------|-----------------|
| T4.1a | Propose boundary candidates based on agent class failure modes | Generative | Proposed boundaries with failure mode rationale | Self-starting — agent has failure mode patterns | Agent-primary | Human proposes from blank → misses boundaries they haven't seen fail |
| T4.1b | Validate and adjust proposed boundaries for specific domain | Evaluative | Finalized boundaries with domain adjustments | Self-starting — has proposals to evaluate | Human-final | Agent finalizes → generic boundaries, not domain-specific |

### The Pattern

Every "Human-only" intuitive task decomposes into two subtasks:

1. **Generate/Propose** — the agent offers options, patterns, or structures based on its broad training (Agent-primary)
2. **Validate/Select/Refine** — the human exercises judgment on prepared material (Human-final)

This is the "agent prepares judgment, human makes judgment" principle applied at the decomposition level. The original decomposition missed it because "Intuitive" was treated as a single operation rather than a multi-step process.

## 3. Improving Cognitive Modality Assignment

The current cognitive types are too coarse. They capture what kind of thinking is needed, but not how the task is *initiated* or what *support* the thinking needs. Two tasks can both be "Intuitive" but require completely different collaboration patterns:

- "Decide whether to approve this specification" — Intuitive, but the human can do it cold
- "Articulate your purpose" — Intuitive, but the human needs prompting to begin

I'd add a second dimension to cognitive type: **initiation mode**.

| Initiation Mode | Meaning | Implication |
|----------------|---------|------------|
| Self-starting | Human can begin from their own knowledge | May be human-only if gap ≥ 6 |
| Scaffolded | Human needs structure or prompts | Always collaborative — agent provides scaffold |
| Discovery | Human discovers by reacting to options | Always collaborative — agent proposes, human refines |

And a third: **experience dependency**.

| Experience Level | Meaning | Implication |
|-----------------|---------|------------|
| Expert-dependent | Only someone with deep domain experience can do this well | Human-primary, but agent can prepare |
| Pattern-augmented | Broad pattern recognition genuinely helps | Collaborative — agent brings patterns, human validates |
| Procedural | Follows known procedures | Agent-primary, human reviews |

So a well-typed task looks like:

```
T1.1a: Elicit principal's purpose
  Cognitive operation: Elicitive (Intuitive)
  Initiation mode: Discovery
  Experience dependency: Expert-dependent
  Output artefact: Raw purpose notes
  Authority: Human-final
  Failure if wrong actor: Agent suggests → template-filling
```

This gives the complementarity analyst much better input. Instead of scoring "Intuitive: Human=10, Agent=2" and concluding "Human-only," it scores:

- **Elicitive operation**: Human has the answer (10), Agent can ask good questions (6) → Human-primary
- **Discovery initiation**: Human can't start cold (2), Agent can propose options (8) → Agent-prepares
- **Expert-dependent**: Human has domain knowledge (10), Agent has broad patterns (5) → Human-decides
- **Combined**: Human has the answer but needs prompting. Agent proposes options, human selects. **Collaborative, human-final.**

The decomposition now produces an allocation that matches reality.

## The Improved Process

```
Step 1: DECOMPOSE (Generator — "never be vague")
  - Split every task into single-operation subtasks
  - Each task has one primary cognitive operation
  - Each task produces a clear output artefact
  - Each task has an explicit failure mode
  - If a task needs "and" to describe it, split it further

Step 2: TYPE (Measurer — "never interpret")
  - Assign primary cognitive operation
  - Assign initiation mode (self-starting / scaffolded / discovery)
  - Assign experience dependency (expert-dependent / pattern-augmented / procedural)
  - Never assign allocation — that's the next step's job

Step 3: ALLOCATE (Assessor — "never finalize")
  - Score complementarity (capability gap)
  - Score adjustment factors (cold start, experience dependency, discovery vs decision, preparation value, reversibility)
  - Propose allocation with rationale
  - Flag any "Human-only" allocation for human review (may be collaborative)
  - Human makes final allocation decision
```

Three agents, three authority boundaries, three failure modes applied at the right level. The Decomposer produces clear tasks. The Typer measures them accurately. The Assessor proposes allocation without finalizing. The human decides.

This also means the complementarity scoring tool from the previous conversation should receive **already-well-decomposed** tasks with **already-assigned initiation mode and experience dependency**. The adjustment factors then have much better input to work with, and fewer tasks will be misclassified as "Human-only" in the first place.

Want me to incorporate this decomposition standard into the CAWDP methodology document and the complementarity scoring tool design?

---

## Run 8 — Agentic Expert ✓ COMPLETED

*2026-05-20T22:32:53* · `glm-5.1:cloud` · `721f6805...`

### Prompt

Yes, start with how this should be described in a new version of CAWDP. Then list the tools, skills or other resources that can help CAWDP agents perform these tasks excellently.

### Response

## CAWDP v2.2 — Decomposition and Allocation Revisions

### Phase 3: Task Decomposition (Revised)

#### 3.1 The Decomposition Quality Standard

Every subtask must satisfy five properties. If any property is missing, the subtask is conflated, vague, or incomplete — and will produce a bad allocation downstream.

**Property 1: Single Primary Cognitive Operation**

One verb, one thinking type. If you need "and" to describe what the task does, split it.

| ❌ Conflated | ✅ Decomposed |
|-------------|-------------|
| "Discover principal's purpose" | "Elicit the principal's purpose through guided conversation" |
| "Identify what this workflow IS" | "Structure the principal's description into a purpose specification" |
| "Define excellent outcomes" | "Propose outcome criteria based on domain patterns" |
| "Identify authority boundaries" | "Propose boundary candidates based on agent class failure modes" |

The "and" test: "Elicit the principal's purpose **and** structure it into a specification" → two tasks. "Propose boundary candidates **and** validate them for this domain" → two tasks.

**Property 2: Clear Output Artefact**

What concrete thing does this task produce? A document, a decision, a list, a score, a specification. If the output is vague ("understanding," "clarity," "alignment"), the task is not well-decomposed.

| ❌ Vague Output | ✅ Specific Artefact |
|----------------|---------------------|
| "Discover purpose" | "Purpose statement — one sentence capturing why this agent exists" |
| "Identify what this IS" | "Identity specification — four identity questions answered" |
| "Define excellent outcomes" | "Outcome criteria — measurable success conditions with thresholds" |
| "Identify boundaries" | "Boundary map — named boundaries with failure modes and authority assignments" |

**Property 3: Explicit Initiation Mode**

How does the human (or agent) begin this task?

| Mode | Meaning | Allocation Implication |
|------|---------|----------------------|
| Self-starting | Can begin from own knowledge without prompting | May be solo if capability gap ≥ 6 |
| Scaffolded | Needs structure, template, or prompt to begin | Always collaborative — agent provides scaffold, human fills in |
| Discovery | Discovers what they want by reacting to options | Always collaborative — agent proposes, human refines |

This is the dimension the original decomposition missed. "Intuitive" tasks are often "Discovery" initiation — the human has superior judgment but cannot begin without prompting. This is why "Human-only" allocation was wrong for five tasks.

**Property 4: Explicit Authority Boundary**

Who has final authority over this task's output?

| Authority | Meaning | When Used |
|-----------|---------|-----------|
| Human-only | Human produces, agent does not contribute to content | Rare — only when agent preparation would corrupt the output |
| Human-final | Agent prepares, human decides | Common — discovery, scaffolded, and high-reversibility tasks |
| Agent-primary | Agent produces, human reviews | Common — analytical, procedural tasks with moderate reversibility |
| System-enforced | Automated with human override | Low-reversibility, high-consistency tasks |

**Property 5: Explicit Failure Mode**

What does "wrong" look like for this task if the wrong actor is assigned? This is the inverse of the authority boundary — the failure mode IS the reason for the boundary.

| Task | Failure Mode | If Wrong Actor |
|------|-------------|---------------|
| Elicit purpose | Generic purpose that misses real intent | Agent suggests purpose → template-filling, not genuine |
| Structure purpose | Purpose stays vague, never becomes specification | Human structures from blank → incomplete, low quality |
| Propose never-rules | Missing boundaries the human hasn't encountered | Human proposes from blank → misses patterns from experience |
| Validate never-rules | Generic boundaries that don't fit the domain | Agent validates → rubber-stamping, not genuine validation |

#### 3.2 The Conflation Test

Before a subtask passes Phase 3 quality gate, it must pass the conflation test:

```
For each subtask:
1. Can you describe it with a single verb? (No "and")
2. Does it produce ONE specific output artefact?
3. Is its initiation mode clear? (Self-starting / Scaffolded / Discovery)
4. Is its authority boundary clear? (Who has final say?)
5. Can you name its specific failure mode?
6. Does it have ONE primary cognitive operation?

If any answer is "no," the subtask is conflated and must be split further.
```

#### 3.3 The Intuitive Task Decomposition Pattern

Tasks typed as "Intuitive" or "Evaluative" frequently decompose into two subtasks following the "agent prepares judgment, human makes judgment" principle:

1. **Propose** — the agent offers options, patterns, or structures (Agent-primary, Generative or Analytical)
2. **Validate** — the human exercises judgment on prepared material (Human-final, Evaluative)

This is not a coincidence — it's the core CAWDP principle applied at decomposition level. When a task is typed as "Intuitive" or "Evaluative" with initiation mode "Discovery" or "Scaffolded," the Decomposer should expect it to split into Propose + Validate.

The decomposition should not automatically split every Intuitive task. The split depends on initiation mode:

| Intuitive Task Initiation | Decomposition |
|--------------------------|--------------|
| Self-starting | May remain one task (human can do it alone) |
| Scaffolded | Split: Propose structure + Validate content |
| Discovery | Split: Propose options + Validate selection |

#### 3.4 Three-Agent Separation for Decompose-Type-Allocate

Task decomposition, cognitive typing, and capability allocation are genuinely different cognitive operations with different failure modes. They should be performed by different agents with different authority boundaries:

| Step | Agent Class | Authority Boundary | Failure Mode |
|------|------------|-------------------|-------------|
| Decompose | Generator | Never be vague | Over-decomposition, under-decomposition, conflation |
| Type | Measurer | Never interpret | Misclassification, over-simplification |
| Allocate | Assessor | Never finalize | Overt classification, missing preparation need |

When one agent performs all three steps, each step's errors compound into the next. The decomposition shapes what the typing sees, which shapes what the allocation scores. A conflated task produces a misclassified type, which produces a bad allocation.

Separating the steps creates review points between each stage. The Measurer can flag conflated tasks. The Assessor can flag misclassified types. The human can flag allocations that don't match reality.

---

### Phase 4: Capability Allocation (Revised)

#### 4.1 Two-Pass Allocation Process

**Pass 1: Capability Gap (Existing)**

Score each dimension 1-10 for Human, Agent, and System. Calculate gaps. Propose initial allocation based on the highest-scoring actor and gap magnitude.

This is the existing complementarity analysis. It correctly identifies *capability* — who is better at this dimension.

**Pass 2: Adjustment Factors (New)**

For each task, assess five factors that modify the gap-based allocation. Any factor that shifts toward collaboration overrides the gap-based allocation.

| Factor | Low | Medium | High | Allocation Shift |
|--------|-----|--------|------|-----------------|
| Cold Start Difficulty | Human can begin immediately | Human benefits from structure | Human faces blank page | High → Collaborative |
| Experience Dependency | Human has deep domain experience | Human has some experience | Human hasn't encountered enough edge cases | High → Collaborative (agent brings patterns) |
| Discovery vs Decision | Options are known | Some known, some need discovery | Human discovers by reacting | Discovery → Collaborative |
| Preparation Value | Agent prep adds minimal value | Agent prep saves time | Agent prep changes output quality | High → Collaborative |
| Reversibility | Easy to undo | Possible with effort | Irreversible or very costly | Low → Human final authority (always) |

**Adjustment Rules:**

1. If two or more factors rate "High" in the shift-toward-collaboration column → Override to Collaborative
2. If Reversibility is Low → Human has final authority, regardless of other factors
3. If Cold Start is High (Discovery or Scaffolded) → Always Collaborative, even when gap ≥ 6
4. Document *why* the allocation shifted, not just that it did — the rationale determines *how* the collaboration works

**Application to the Five Problematic Tasks:**

| Task | Gap Allocation | Cold Start | Experience | Discovery | Prep Value | Reversibility | Adjusted | Rationale |
|------|---------------|------------|------------|-----------|------------|---------------|----------|-----------|
| T1.1 Elicit purpose | Human-only | Discovery | — | Discovery | High | Low | Collaborative | Human has judgment but faces blank page |
| T1.2 Identify identity | Human-only | Discovery | — | Discovery | High | Low | Collaborative | Same pattern — needs prompting |
| T1.4 Discover violations | Human-only | — | High | — | High | Low | Collaborative | Agent surfaces patterns human hasn't encountered |
| T2.1 Define excellence | Human-only | Discovery | — | Discovery | High | Low | Collaborative | Excellence is discovered by reaction |
| T4.1 Identify boundaries | Human-only | — | High | Mixed | High | Low | Collaborative | Boundaries benefit from broad pattern recognition |

#### 4.2 Human-Primary ≠ Human-Only

This principle was already in CAWDP v2.1 but needs strengthening:

> For all human-primary tasks: the agent PREPARES options → human REFINES, ACCEPTS, or REJECTS → agent CAPTURES decision with reasoning.

The adjustment factors determine *how* the agent prepares:

| Adjustment Factor Dominant | How Agent Prepares |
|--------------------------|-------------------|
| Cold Start (Discovery) | Agent proposes options for human to react to |
| Cold Start (Scaffolded) | Agent provides structure/template for human to fill |
| Experience Dependency | Agent surfaces patterns and failure modes for human to validate |
| Preparation Value | Agent prepares analysis or draft for human to review |
| Reversibility (Low) | Agent prepares comprehensive options, human has final authority |

#### 4.3 The Allocation Rationale

Every allocation decision must include a rationale that explains *why* this actor was assigned, not just *which* actor was assigned. This rationale:

- Determines *how* the collaboration works (what "collaborative" means in practice)
- Enables review — if the rationale is wrong, the allocation is wrong
- Provides decision archaeology — future readers can understand why an allocation was made
- Feeds the specification — rationale becomes authority boundary documentation

Format:

```
Task: [name]
Allocation: [H/A/S/Collaborative]
Rationale: [why this actor, referencing specific adjustment factors]
Authority: [who has final say]
Preparation: [how the agent prepares, if collaborative]
Failure Mode: [what goes wrong if wrong actor is assigned]
```

---

### Updated Cognitive Operation Taxonomy

The cognitive operation types are expanded from the original set to include two new dimensions:

**Primary Cognitive Operation:**

| Type | Description | Agent Class Signature |
|------|-------------|----------------------|
| Mechanical | Repetitive, rule-based, no judgment | System-primary |
| Analytical | Processing, measuring, comparing | Agent-primary (Measurer) |
| Generative | Creating, proposing, synthesizing | Agent-primary (Generator) |
| Elicitive | Drawing out, prompting, reflecting | Collaborative (human has answer, agent elicits) |
| Evaluative | Judging, validating, prioritizing | Human-final (agent prepares, human decides) |
| Intuitive | Knowing from experience, gut feel | Human-primary (with adjustment for initiation mode) |

**Initiation Mode (New):**

| Mode | Meaning | Allocation Impact |
|------|---------|------------------|
| Self-starting | Can begin from own knowledge without prompting | Solo allocation possible if gap ≥ 6 |
| Scaffolded | Needs structure, template, or prompt to begin | Always collaborative — agent provides scaffold |
| Discovery | Discovers what they want by reacting to options | Always collaborative — agent proposes, human refines |

**Experience Dependency (New):**

| Level | Meaning | Allocation Impact |
|-------|---------|------------------|
| Expert-dependent | Only deep domain experience produces quality output | Human-primary, but agent can prepare |
| Pattern-augmented | Broad pattern recognition genuinely improves output | Collaborative — agent brings patterns, human validates |
| Procedural | Follows known procedures and rules | Agent-primary, human reviews |

---

### Quality Gate Update

Phase 3 quality gate gains an additional check:

**Layer 1 — Fidelity:**
- [ ] Every subtask passes the conflation test (6 properties)
- [ ] Every subtask has a single primary cognitive operation
- [ ] Every subtask has a clear output artefact
- [ ] Every subtask has an explicit initiation mode
- [ ] Every subtask has an explicit failure mode
- [ ] Intuitive tasks with Discovery/Scaffolded initiation are split into Propose + Validate

**Layer 2 — Enrichment:**
- [ ] Adjustment factors are assessed for every task initially rated "Human-only"
- [ ] Allocation rationale is documented for every task
- [ ] Human-primary tasks specify how the agent prepares

**Layer 3 — Cross-cutting:**
- [ ] CC-1 Verification Independence: Decompose, Type, and Allocate are performed by different agents
- [ ] CC-2 Human Enrichment: Every "Human-only" allocation is reviewed for collaborative potential
- [ ] CC-9 Possibility Orientation: Decomposition doesn't prematurely constrain possibilities

---

### Cross-Cutting Concern Update

**CC-2 Human Enrichment Assessment — strengthened:**

The assessment must now explicitly check for "Human-primary ≠ Human-only" at the decomposition level:

- For every task rated "Human-only" by gap score, assess the five adjustment factors
- If two or more factors shift toward collaboration, override to "Collaborative, human-final"
- If initiation mode is Discovery or Scaffolded, always override to "Collaborative"
- Document the preparation method: how does the agent prepare for the human's judgment?
- Verify that the preparation method matches the adjustment factor (Discovery → propose options; Scaffolded → provide structure; Experience → surface patterns)

---

## Tools, Skills, and Resources for Excellent Decomposition and Allocation

### For Decomposition (Generator)

**Task Splitting Rules**

A checklist the Decomposer agent runs on every subtask:

```
1. SINGLE VERB TEST: Can you describe this task with one verb?
   - If "and" appears → split
   - If multiple cognitive operations are needed → split

2. OUTPUT ARTEFACT TEST: Can you name the specific thing this task produces?
   - If the output is "understanding" or "clarity" → not decomposed
   - If the output is a specific document/decision/list → pass

3. INITIATION MODE TEST: How does the actor begin this task?
   - If the human faces a blank page → Discovery or Scaffolded
   - If the actor can begin from requirements → Self-starting

4. CONFLATION TEST: Does this task contain multiple cognitive operations?
   - "Elicit AND structure" → split into Elicit + Structure
   - "Propose AND validate" → split into Propose + Validate
   - "Analyse AND decide" → split into Analyse + Decide

5. FAILURE MODE TEST: Can you name what goes wrong if the wrong actor is assigned?
   - If you can't name a specific failure → the task isn't specific enough
```

**Decomposition Pattern Library**

Common decomposition patterns the Decomposer should know:

| Pattern | When to Use | Example |
|---------|------------|---------|
| Propose + Validate | Task requires human judgment but human faces blank page | T1.1: Propose purpose options → Validate real purpose |
| Elicit + Structure | Human has knowledge but can't articulate it cold | T1.2: Elicit identity reactions → Structure into specification |
| Generate + Filter | Many options needed, then select best | T4.1: Generate boundary candidates → Filter for domain relevance |
| Analyse + Decide | Data needs processing before decision | Financial analysis → Investment decision |
| Draft + Review | Output needs creation then quality check | Draft specification → Review against requirements |
| Measure + Interpret | Data needs collection then meaning-making | Collect metrics → Interpret trends |
| Extract + Assess | Raw material needs extraction then evaluation | Extract key claims → Assess their validity |

**The Intuitive Task Split Rule**

> If a task is typed as Intuitive or Evaluative AND has initiation mode Discovery or Scaffolded, the Decomposer should expect it to decompose into Propose + Validate. The Propose subtask is typically Agent-primary (Generative or Analytical). The Validate subtask is always Human-final (Evaluative).

This is the decomposition-level application of "agent prepares judgment, human makes judgment."

### For Typing (Measurer)

**Cognitive Operation Classification Guide**

Each cognitive operation with characteristic signals and typical agent class:

| Operation | Signals | Typical Agent Class | Initiation Mode Range |
|-----------|---------|-------------------|----------------------|
| Mechanical | Repetitive, rule-based, no judgment needed | System | Self-starting |
| Analytical | Comparing, measuring, calculating, structuring | Measurer | Self-starting |
| Generative | Creating, proposing, drafting, synthesizing | Generator | Self-starting |
| Elicitive | Drawing out, prompting, reflecting, surfacing | Assessor (possibility-oriented) | Discovery or Scaffolded |
| Evaluative | Judging, validating, prioritizing, deciding | Assessor (constraint-oriented) | Self-starting or Scaffolded |
| Intuitive | Knowing from experience, gut feel, domain expertise | Human-primary | Discovery, Scaffolded, or Self-starting |

**Initiation Mode Decision Tree**

```
Can the actor begin this task from their own knowledge without any input or prompting?
├── YES → Self-starting
│   └── May be solo allocation if gap ≥ 6
├── PARTIALLY — needs structure or template
│   └── Scaffolded
│       └── Always collaborative — agent provides scaffold
└── NO — needs options to react to
    └── Discovery
        └── Always collaborative — agent proposes, human refines
```

**Experience Dependency Decision Tree**

```
Does this task require deep domain-specific experience that only the principal has?
├── YES — only the principal has seen enough edge cases
│   └── Expert-dependent
│       └── Human-primary, but agent can prepare (surface patterns, propose options)
├── PARTIALLY — domain experience helps but broad patterns are also valuable
│   └── Pattern-augmented
│       └── Collaborative — agent brings patterns, human validates
└── NO — follows known procedures or patterns
    └── Procedural
        └── Agent-primary, human reviews
```

**Classification Self-Check**

After typing, the Measurer runs:

```
1. Does each task have exactly ONE primary cognitive operation?
2. Does each task have an initiation mode?
3. Does each task have an experience dependency level?
4. Are Intuitive/Evaluative tasks with Discovery/Scaffolded initiation
   flagged for potential Propose + Validate decomposition?
5. Have I assigned any allocations? (If yes — that's the Assessor's job)
```

### For Allocation (Assessor)

**Adjustment Factor Assessment Template**

For each task initially rated "Human-only":

```
Task: [name]
Initial allocation (gap-based): [allocation]

Adjustment Factors:
  Cold Start Difficulty: [Self-starting / Scaffolded / Discovery]
  Experience Dependency: [Expert-dependent / Pattern-augmented / Procedural]
  Discovery vs Decision: [Decision / Mixed / Discovery]
  Preparation Value: [Low / Medium / High]
  Reversibility: [High / Medium / Low]

Adjustment Count: [number of factors that shift toward collaboration]

Adjusted Allocation: [allocation]
Rationale: [why this allocation, referencing specific factors]
Preparation Method: [how agent prepares for human judgment]
Authority: [who has final say]
Failure Mode: [what goes wrong if wrong actor]
```

**Override Rules**

```
RULE 1: If 2+ adjustment factors shift toward collaboration → Override to Collaborative
RULE 2: If initiation mode is Discovery or Scaffolded → Always Collaborative
RULE 3: If reversibility is Low → Human has final authority (always)
RULE 4: If experience dependency is Expert-dependent → Human-primary, but agent prepares
RULE 5: If preparation value is High → Agent preparation is required, not optional
RULE 6: Document WHY, not just WHAT — rationale determines how collaboration works
```

**Allocation Rationale Template**

```
Task: [name]
Allocated to: [Human-only / Collaborative (human-final) / Collaborative (agent-primary) / Agent-primary / System-enforced]
Rationale: [specific reason, referencing gap score and/or adjustment factors]
Preparation: [how agent prepares for human judgment, if collaborative]
Authority: [who has final say on this task's output]
Failure Mode: [what goes wrong if wrong actor is assigned]
```

### Cross-Step Resources

**Decomposition-Type-Allocation Review Checklist**

A human or quality gate review between each step:

```
After Decomposition (before Typing):
□ Every subtask passes the conflation test (6 properties)
□ No subtask needs "and" to describe it
□ Every subtask has a clear output artefact
□ Intuitive tasks with Discovery/Scaffolded initiation are flagged for splitting

After Typing (before Allocation):
□ Every subtask has one primary cognitive operation
□ Every subtask has an initiation mode
□ Every subtask has an experience dependency level
□ No allocations have been assigned (that's the next step)
□ Intuitive/Evaluative tasks with Discovery/Scaffolded initiation are flagged

After Allocation (before proceeding):
□ Every "Human-only" allocation has been assessed for adjustment factors
□ Every allocation has a rationale
□ Every collaborative allocation specifies the preparation method
□ CC-1: Decomposer, Typer, and Assessor are different agents
□ CC-2: Every "Human-only" allocation has been reviewed for collaborative potential
```

**The Decomposition-Allocation Integrity Check**

This is the key insight from our conversation, codified as a rule:

> **If a task is rated "Human-only" by capability gap but has Discovery or Scaffolded initiation mode, it is almost certainly collaborative — the human has superior judgment but needs agent preparation to exercise it. The gap score measures capability, not preparation need. Both must be assessed before allocation.**

This single check would have caught all five of the problematic tasks in the original decomposition.The methodology revision is captured. The key insight that started this whole thread — "the scores say Human-only but the task is genuinely Collaborative" — is now structurally prevented by two mechanisms:

1. **Upstream**: Better decomposition that splits conflated tasks before they reach allocation
2. **Downstream**: Adjustment factors that catch the preparation need that capability gaps miss

Both mechanisms are now codified in the methodology with quality gates, checklists, and agent separation to prevent the errors from compounding.

What's your next priority — the complementarity scoring tool implementation with the two-pass process, or continuing to refine another part of the methodology?

---

## Run 9 — Agentic Expert ✓ COMPLETED

*2026-05-20T22:47:29* · `glm-5.1:cloud` · `63b054bf...`

### Prompt

So I am building the Agno workflow to help build agentic workflows. 
We've built the schema and a backcasting tracing tool. 
This decomposition-allocation process follows that. You've suggested great tools.

How should this new understanding be implemented in the Agno workflow application I'm building?

### Response

Good question. Let me think through this from the architecture you already have, not from scratch.

## Where You Are

You have:
- SurrealDB schema with `design_tasks` and related tables
- A backcasting tracing tool (Phase 2)
- The three-layer architecture: `db/writer.py` → `agents/tools/cawdp_tools.py` → `agents/cawdp_orchestrator.py`
- The Surface + Engine pattern (user-facing agent, back-office specialists)

Decomposition-allocation is Phases 3-4 in your pipeline. The question is: what agents, what tools, what schema changes, and how does it all flow?

## The Architecture

### Three Agents, One Workflow, One Human Gate

```
Decomposer (Generator)  →  Typer (Measurer)  →  Allocator (Assessor)  →  Human Gate
"never be vague"            "never interpret"      "never finalize"         (human decides)
```

Each agent has one job. The Decomposer never types. The Typer never allocates. The Allocator never finalizes. The human never decomposes, types, or scores — they review allocations and decide.

This is an Agno Workflow with three sequential steps and one HumanReview gate at the end. The human gate comes after allocation, not between each step, because the intermediate outputs (decomposed tasks, typed tasks) are reviewable within the allocation review.

### Schema Changes

You need new fields on `design_tasks` and one new table for the adjustment factors.

**Add to `design_tasks`:**

```sql
-- Phase 3: Decomposition fields
DEFINE FIELD output_artefact ON design_tasks TYPE string;
DEFINE FIELD initiation_mode ON design_tasks TYPE string
  ASSERT $value IN ['self-starting', 'scaffolded', 'discovery'];
DEFINE FIELD experience_dependency ON design_tasks TYPE string
  ASSERT $value IN ['expert-dependent', 'pattern-augmented', 'procedural'];
DEFINE FIELD authority_boundary ON design_tasks TYPE string
  ASSERT $value IN ['human-only', 'human-final', 'agent-primary', 'system-enforced'];
DEFINE FIELD decomposition_pattern ON design_tasks TYPE string
  ASSERT $value IN [
  'propose-validate', 'elicit-structure', 'generate-filter',
  'analyse-decide', 'draft-review', 'measure-interpret', 'extract-assess',
  'single-task'
];
DEFINE FIELD conflation_check ON design_tasks TYPE object;

-- Phase 4: Allocation fields (beyond existing complementarity)
DEFINE FIELD allocation_rationale ON design_tasks TYPE string;
DEFINE FIELD preparation_method ON design_tasks TYPE string;
DEFINE FIELD adjusted_allocation ON design_tasks TYPE string;
DEFINE FIELD adjustment_summary ON design_tasks TYPE object;
```

**New table for adjustment factor detail:**

```sql
DEFINE TABLE design_adjustment_factors SCHEMAFULL;

DEFINE FIELD task ON design_adjustment_factors TYPE record<design_tasks>;
DEFINE FIELD workflow ON design_adjustment_factors TYPE record<design_workflows>;
DEFINE FIELD cold_start_difficulty ON design_adjustment_factors TYPE string
  ASSERT $value IN ['self-starting', 'scaffolded', 'discovery'];
DEFINE FIELD experience_dependency ON design_adjustment_factors TYPE string
  ASSERT $value IN ['expert-dependent', 'pattern-augmented', 'procedural'];
DEFINE FIELD discovery_vs_decision ON design_adjustment_factors TYPE string
  ASSERT $value IN ['decision', 'mixed', 'discovery'];
DEFINE FIELD preparation_value ON design_adjustment_factors TYPE string
  ASSERT $value IN ['low', 'medium', 'high'];
DEFINE FIELD reversibility ON design_adjustment_factors TYPE string
  ASSERT $value IN ['high', 'medium', 'low'];
DEFINE FIELD override_count ON design_adjustment_factors TYPE int;
DEFINE FIELD assessed_by ON design_adjustment_factors TYPE string;
DEFINE FIELD assessed_at ON design_adjustment_factors TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_af_task ON design_adjustment_factors FIELDS task;
DEFINE INDEX idx_af_workflow ON design_adjustment_factors FIELDS workflow;
```

The adjustment factors live in their own table because they're assessed per-task, they're separate from the capability scores, and they need their own querying. The `override_count` is the number of factors that shift toward collaboration — if ≥ 2, the allocation overrides to Collaborative.

### Writer Functions

Each agent step has a corresponding writer function that enforces business rules.

**Phase 3 — Decomposition:**

```python
# db/writer.py

DECOMPOSITION_PATTERNS = [
    'propose-validate', 'elicit-structure', 'generate-filter',
    'analyse-decide', 'draft-review', 'measure-interpret',
    'extract-assess', 'single-task'
]

INITIATION_MODES = ['self-starting', 'scaffolded', 'discovery']
EXPERIENCE_DEPS = ['expert-dependent', 'pattern-augmented', 'procedural']
AUTHORITY_BOUNDARIES = ['human-only', 'human-final', 'agent-primary', 'system-enforced']

async def decompose_task(
    client: Surreal,
    parent_task_id: str,
    workflow_id: str,
    subtasks: list[dict],
    decomposition_pattern: str,
    decomposed_by: str,
) -> list[str]:
    """Decompose a parent task into subtasks.
    
    Enforces:
    - Every subtask must have 5 properties (conflation check)
    - Decomposition pattern must be valid
    - Parent task status updated to 'decomposed'
    - Subtasks inherit workflow context
    
    Returns: list of created task IDs
    """
    # 1. Validate decomposition pattern
    if decomposition_pattern not in DECOMPOSITION_PATTERNS:
        raise ValueError(f"Invalid decomposition pattern: {decomposition_pattern}")
    
    # 2. Validate each subtask has required properties
    created_ids = []
    for st in subtasks:
        conflation = validate_subtask_properties(st)
        if not conflation['passed']:
            raise ValueError(
                f"Subtask '{st.get('name', 'unnamed')}' fails conflation check: "
                f"{conflation['failures']}"
            )
        
        # 3. Create subtask record
        result = await client.query(
            """CREATE design_tasks SET
               workflow = $wf,
               parent_task = $parent,
               name = $name,
               description = $desc,
               cognitive_type = $cog_type,
               output_artefact = $output,
               initiation_mode = $init_mode,
               experience_dependency = $exp_dep,
               authority_boundary = $auth_bound,
               failure_mode = $fail_mode,
               decomposition_pattern = $pattern,
               conflation_check = $conflation,
               phase = 'decomposed',
               decomposed_by = $by,
               created_at = time::now()
            """,
            {
                "wf": workflow_id,
                "parent": parent_task_id,
                "name": st['name'],
                "desc": st['description'],
                "cog_type": st['cognitive_type'],
                "output": st['output_artefact'],
                "init_mode": st['initiation_mode'],
                "exp_dep": st['experience_dependency'],
                "auth_bound": st['authority_boundary'],
                "fail_mode": st['failure_mode'],
                "pattern": decomposition_pattern,
                "conflation": conflation,
                "by": decomposed_by,
            }
        )
        created_ids.append(result[0]['id'])
    
    # 4. Update parent task status
    await client.query(
        """UPDATE design_tasks SET
           phase = 'decomposed',
           decomposition_pattern = $pattern,
           updated_at = time::now()
           WHERE id = $id""",
        {"id": parent_task_id, "pattern": decomposition_pattern}
    )
    
    return created_ids


def validate_subtask_properties(st: dict) -> dict:
    """Check all 5 properties + conflation test.
    
    Returns: {passed: bool, failures: list[str]}
    """
    failures = []
    
    # 1. Single primary cognitive operation (no "and")
    name = st.get('name', '')
    desc = st.get('description', '')
    if ' and ' in name.lower() or ' and ' in desc.lower():
        failures.append("Task contains 'and' — likely conflated. Split further.")
    
    # 2. Clear output artefact
    output = st.get('output_artefact', '')
    if not output or output in ['understanding', 'clarity', 'alignment', 'awareness']:
        failures.append(f"Output '{output}' is vague. Specify a concrete artefact.")
    
    # 3. Valid initiation mode
    if st.get('initiation_mode') not in INITIATION_MODES:
        failures.append(f"Invalid initiation mode: {st.get('initiation_mode')}")
    
    # 4. Valid authority boundary
    if st.get('authority_boundary') not in AUTHORITY_BOUNDARIES:
        failures.append(f"Invalid authority boundary: {st.get('authority_boundary')}")
    
    # 5. Failure mode specified
    if not st.get('failure_mode'):
        failures.append("No failure mode specified — what goes wrong if wrong actor?")
    
    # 6. Valid cognitive type
    if st.get('cognitive_type') not in [
        'mechanical', 'analytical', 'generative', 'elicitive', 'evaluative', 'intuitive'
    ]:
        failures.append(f"Invalid cognitive type: {st.get('cognitive_type')}")
    
    return {
        'passed': len(failures) == 0,
        'failures': failures,
        'task_name': name
    }
```

**Phase 4 — Allocation (two-pass):**

```python
# db/writer.py (continued)

GAP_THRESHOLD = 6  # From CAWDP: 6+ = human-only dimension

OVERRIDE_RULES = {
    'cold_start_discovery': 'Discovery initiation → always collaborative',
    'cold_start_scaffolded': 'Scaffolded initiation → always collaborative',
    'two_plus_factors': '2+ adjustment factors → override to Collaborative',
    'low_reversibility': 'Low reversibility → human final authority always',
    'expert_dependent': 'Expert-dependent → human-primary with agent preparation',
    'high_prep_value': 'High preparation value → agent preparation required',
}

async def assess_adjustment_factors(
    client: Surreal,
    task_id: str,
    workflow_id: str,
    cold_start: str,           # self-starting / scaffolded / discovery
    experience_dep: str,       # expert-dependent / pattern-augmented / procedural
    discovery_vs_decision: str, # decision / mixed / discovery
    prep_value: str,            # low / medium / high
    reversibility: str,         # high / medium / low
    assessed_by: str,
) -> dict:
    """Assess adjustment factors for a task's allocation.
    
    Enforces:
    - Valid factor values
    - Override rule application
    - Override count calculation
    - Rationale generation
    """
    # 1. Validate factor values
    if cold_start not in INITIATION_MODES:
        raise ValueError(f"Invalid cold start: {cold_start}")
    if experience_dep not in EXPERIENCE_DEPS:
        raise ValueError(f"Invalid experience dependency: {experience_dep}")
    if discovery_vs_decision not in ['decision', 'mixed', 'discovery']:
        raise ValueError(f"Invalid discovery vs decision: {discovery_vs_decision}")
    if prep_value not in ['low', 'medium', 'high']:
        raise ValueError(f"Invalid preparation value: {prep_value}")
    if reversibility not in ['high', 'medium', 'low']:
        raise ValueError(f"Invalid reversibility: {reversibility}")
    
    # 2. Count overrides
    overrides = []
    
    # Rule: Discovery/Scaffolded → always collaborative
    if cold_start in ['discovery', 'scaffolded']:
        overrides.append(('cold_start', cold_start, 'always collaborative'))
    
    # Rule: Expert-dependent → human-primary with agent preparation
    if experience_dep == 'expert-dependent':
        overrides.append(('experience_dependency', experience_dep, 'human-primary with preparation'))
    
    # Rule: Discovery vs Decision
    if discovery_vs_decision == 'discovery':
        overrides.append(('discovery_vs_decision', discovery_vs_decision, 'collaborative'))
    
    # Rule: High preparation value → agent preparation required
    if prep_value == 'high':
        overrides.append(('preparation_value', prep_value, 'agent preparation required'))
    
    # Rule: Low reversibility → human final authority
    if reversibility == 'low':
        overrides.append(('reversibility', reversibility, 'human final authority'))
    
    # Rule: 2+ factors → override to collaborative
    override_count = len(overrides)
    collaborative_override = override_count >= 2
    
    # 3. Determine preparation method
    preparation_method = determine_preparation_method(
        cold_start, experience_dep, discovery_vs_decision, prep_value, reversibility
    )
    
    # 4. Write to design_adjustment_factors
    await client.query(
        """CREATE design_adjustment_factors SET
           task = $task, workflow = $wf,
           cold_start_difficulty = $cs,
           experience_dependency = $ed,
           discovery_vs_decision = $dvd,
           preparation_value = $pv,
           reversibility = $rev,
           override_count = $oc,
           assessed_by = $by,
           assessed_at = time::now()
        """,
        {
            "task": task_id, "wf": workflow_id,
            "cs": cold_start, "ed": experience_dep,
            "dvd": discovery_vs_decision, "pv": prep_value,
            "rev": reversibility, "oc": override_count, "by": assessed_by,
        }
    )
    
    # 5. Update design_tasks with adjustment summary
    await client.query(
        """UPDATE design_tasks SET
           initiation_mode = $cs,
           experience_dependency = $ed,
           adjustment_summary = {
               override_count: $oc,
               collaborative_override: $co,
               overrides: $overrides,
               preparation_method: $pm
           },
           updated_at = time::now()
           WHERE id = $id""",
        {
            "id": task_id, "cs": cold_start, "ed": experience_dep,
            "oc": override_count, "co": collaborative_override,
            "overrides": overrides, "pm": preparation_method,
        }
    )
    
    return {
        "task_id": task_id,
        "override_count": override_count,
        "collaborative_override": collaborative_override,
        "overrides": overrides,
        "preparation_method": preparation_method,
    }


def determine_preparation_method(
    cold_start, experience_dep, discovery_vs_decision, prep_value, reversibility
) -> str:
    """Determine how the agent should prepare for human judgment."""
    if cold_start == 'discovery':
        return "Agent proposes options for human to react to"
    if cold_start == 'scaffolded':
        return "Agent provides structure/template for human to fill in"
    if experience_dep == 'expert-dependent':
        return "Agent surfaces patterns and failure modes for human validation"
    if prep_value == 'high':
        return "Agent prepares analysis or draft for human review"
    if reversibility == 'low':
        return "Agent prepares comprehensive options; human has final authority"
    return "Agent provides supporting information for human decision"


async def allocate_task(
    client: Surreal,
    task_id: str,
    workflow_id: str,
    gap_allocation: str,      # from Pass 1: human-only / agent-primary / etc
    adjusted_allocation: str,  # from Pass 2: may differ from gap allocation
    rationale: str,
    preparation_method: str,
    authority: str,            # who has final say
    allocated_by: str,
) -> dict:
    """Finalize task allocation with rationale.
    
    Enforces:
    - If gap_allocation differs from adjusted_allocation, rationale must explain why
    - If collaborative, preparation_method must be specified
    - Authority must match allocation type
    """
    # 1. Validate allocation change requires rationale
    if gap_allocation != adjusted_allocation and not rationale:
        raise ValueError(
            f"Allocation changed from {gap_allocation} to {adjusted_allocation} "
            f"but no rationale provided. Every override needs a WHY."
        )
    
    # 2. Collaborative allocations need a preparation method
    if 'collaborative' in adjusted_allocation.lower() and not preparation_method:
        raise ValueError(
            f"Collaborative allocation for task {task_id} requires a preparation method."
        )
    
    # 3. Update task allocation
    await client.query(
        """UPDATE design_tasks SET
           allocated_to = $alloc,
           adjusted_allocation = $adj_alloc,
           allocation_rationale = $rationale,
           preparation_method = $prep,
           authority_boundary = $auth,
           phase = 'allocated',
           allocated_by = $by,
           updated_at = time::now()
           WHERE id = $id""",
        {
            "id": task_id,
            "alloc": adjusted_allocation,
            "adj_alloc": adjusted_allocation,
            "rationale": rationale,
            "prep": preparation_method,
            "auth": authority,
            "by": allocated_by,
        }
    )
    
    return {
        "task_id": task_id,
        "gap_allocation": gap_allocation,
        "adjusted_allocation": adjusted_allocation,
        "allocation_changed": gap_allocation != adjusted_allocation,
        "rationale": rationale,
        "preparation_method": preparation_method,
        "authority": authority,
    }
```

### Agno Tools

Following the closure pattern and user-action naming from the orchestrator review:

```python
# agents/tools/cawdp_tools.py

from agno.tools import tool as agno_tool
from db.writer import (
    decompose_task,
    assess_adjustment_factors,
    allocate_task,
    score_task_complementarity,
)

def make_decomposition_tools(client_getter):
    """Create decomposition, typing, and allocation tools."""
    
    @agno_tool(
        name="decompose_task",
        description=(
            "Split a parent task into well-decomposed subtasks. "
            "Each subtask must have: single cognitive operation, "
            "clear output artefact, explicit initiation mode, "
            "explicit authority boundary, and explicit failure mode. "
            "If a task needs 'and' to describe it, split it further."
        ),
    )
    def decompose_task_tool(
        parent_task_id: str,
        workflow_id: str,
        subtasks: list[dict],
        decomposition_pattern: str,
    ) -> str:
        """Decompose a parent task into subtasks.
        
        Each subtask dict must have:
            name: str - single-verb task name
            description: str - what this task does
            cognitive_type: str - mechanical/analytical/generative/elicitive/evaluative/intuitive
            output_artefact: str - specific thing this task produces
            initiation_mode: str - self-starting/scaffolded/discovery
            experience_dependency: str - expert-dependent/pattern-augmented/procedural
            authority_boundary: str - human-only/human-final/agent-primary/system-enforced
            failure_mode: str - what goes wrong if wrong actor
        
        Args:
            parent_task_id: The parent task to decompose
            workflow_id: The workflow this belongs to
            subtasks: List of subtask dictionaries
            decomposition_pattern: Which decomposition pattern to use
        """
        client = client_getter()
        result = asyncio.run(decompose_task(
            client=client,
            parent_task_id=parent_task_id,
            workflow_id=workflow_id,
            subtasks=subtasks,
            decomposition_pattern=decomposition_pattern,
            decomposed_by="cawdp_decomposer",
        ))
        return json.dumps(result, indent=2)
    
    @agno_tool(
        name="assess_adjustment_factors",
        description=(
            "Assess the five adjustment factors that modify gap-based allocation. "
            "These factors catch preparation need that capability gaps miss. "
            "Apply override rules: Discovery/Scaffolded → always collaborative, "
            "2+ factors → override to collaborative, "
            "Low reversibility → human final authority."
        ),
    )
    def assess_adjustment_factors_tool(
        task_id: str,
        workflow_id: str,
        cold_start_difficulty: str,
        experience_dependency: str,
        discovery_vs_decision: str,
        preparation_value: str,
        reversibility: str,
    ) -> str:
        """Assess adjustment factors for a task's allocation.
        
        Args:
            task_id: The task to assess
            workflow_id: The workflow this belongs to
            cold_start_difficulty: self-starting/scaffolded/discovery
            experience_dependency: expert-dependent/pattern-augmented/procedural
            discovery_vs_decision: decision/mixed/discovery
            preparation_value: low/medium/high
            reversibility: high/medium/low
        """
        client = client_getter()
        result = asyncio.run(assess_adjustment_factors(
            client=client,
            task_id=task_id,
            workflow_id=workflow_id,
            cold_start=cold_start_difficulty,
            experience_dep=experience_dependency,
            discovery_vs_decision=discovery_vs_decision,
            prep_value=preparation_value,
            reversibility=reversibility,
            assessed_by="cawdp_allocator",
        ))
        return json.dumps(result, indent=2)
    
    @agno_tool(
        name="allocate_task",
        description=(
            "Finalize task allocation with gap-based allocation, "
            "adjusted allocation, rationale, and preparation method. "
            "If gap allocation differs from adjusted allocation, "
            "rationale must explain WHY the allocation changed. "
            "Collaborative allocations require a preparation method."
        ),
    )
    def allocate_task_tool(
        task_id: str,
        workflow_id: str,
        gap_allocation: str,
        adjusted_allocation: str,
        rationale: str,
        preparation_method: str,
        authority: str,
    ) -> str:
        """Finalize task allocation.
        
        Args:
            task_id: The task to allocate
            workflow_id: The workflow this belongs to
            gap_allocation: Allocation from Pass 1 (capability gap)
            adjusted_allocation: Allocation from Pass 2 (adjustment factors)
            rationale: WHY this allocation, referencing specific factors
            preparation_method: How agent prepares for human judgment (if collaborative)
            authority: Who has final say (human-only/human-final/agent-primary/system-enforced)
        """
        client = client_getter()
        result = asyncio.run(allocate_task(
            client=client,
            task_id=task_id,
            workflow_id=workflow_id,
            gap_allocation=gap_allocation,
            adjusted_allocation=adjusted_allocation,
            rationale=rationale,
            preparation_method=preparation_method,
            authority=authority,
            allocated_by="cawdp_allocator",
        ))
        return json.dumps(result, indent=2)
    
    return [decompose_task_tool, assess_adjustment_factors_tool, allocate_task_tool]
```

### Agent Definitions

Three agents, three authority boundaries, three failure modes:

```python
# agents/decomposer.py

decomposer = Agent(
    name="CAWDP Decomposer",
    model=Ollama(id="glm-5.1:cloud"),
    tools=[decompose_task_tool, ...],
    instructions=[
        "You are a Generator-class agent. Your authority boundary: never be vague.",
        "Your job: decompose parent tasks into well-formed subtasks.",
        "Every subtask must pass the conflation test:",
        "  1. Single primary cognitive operation (no 'and')",
        "  2. Clear output artefact (specific, not vague)",
        "  3. Explicit initiation mode (self-starting/scaffolded/discovery)",
        "  4. Explicit authority boundary (who has final say)",
        "  5. Explicit failure mode (what goes wrong if wrong actor)",
        "",
        "DECOMPOSITION PATTERNS:",
        "  propose-validate: agent proposes, human validates (for discovery/scaffolded tasks)",
        "  elicit-structure: agent elicits, then structures raw input",
        "  generate-filter: agent generates options, human filters",
        "  analyse-decide: agent analyses, human decides",
        "  draft-review: agent drafts, human reviews",
        "  measure-interpret: agent measures, human interprets",
        "  extract-assess: agent extracts, human assesses",
        "",
        "INTUITIVE TASK RULE:",
        "If a task is Intuitive or Evaluative with Discovery/Scaffolded initiation,",
        "it almost always decomposes into Propose + Validate.",
        "The Propose subtask is Agent-primary (Generative or Analytical).",
        "The Validate subtask is Human-final (Evaluative).",
        "",
        "FAILURE MODE: over-decomposition, under-decomposition, or conflation.",
        "If a task needs 'and' to describe it, split it further.",
        "If a subtask is too small to have a clear output artefact, merge it.",
    ],
)
```

```python
# agents/typer.py

typer = Agent(
    name="CAWDP Typer",
    model=Ollama(id="glm-5.1:cloud"),
    tools=[classify_cognitive_type_tool, ...],
    instructions=[
        "You are a Measurer-class agent. Your authority boundary: never interpret.",
        "Your job: classify each task's cognitive operation, initiation mode, "
        "and experience dependency. You do NOT allocate actors.",
        "",
        "COGNITIVE OPERATIONS:",
        "  mechanical: repetitive, rule-based, no judgment → System-primary",
        "  analytical: processing, measuring, comparing → Agent-primary (Measurer)",
        "  generative: creating, proposing, synthesizing → Agent-primary (Generator)",
        "  elicitive: drawing out, prompting, reflecting → Collaborative",
        "  evaluative: judging, validating, prioritizing → Human-final",
        "  intuitive: knowing from experience, gut feel → Human-primary (with adjustment)",
        "",
        "INITIATION MODES:",
        "  self-starting: can begin from own knowledge → may be solo if gap ≥ 6",
        "  scaffolded: needs structure or prompts → always collaborative",
        "  discovery: discovers by reacting to options → always collaborative",
        "",
        "EXPERIENCE DEPENDENCY:",
        "  expert-dependent: only deep domain experience produces quality → human-primary with prep",
        "  pattern-augmented: broad patterns genuinely help → collaborative",
        "  procedural: follows known procedures → agent-primary",
        "",
        "FAILURE MODE: misclassification, over-simplification.",
        "Never assign allocation — that is the Assessor's job.",
        "Flag Intuitive/Evaluative tasks with Discovery/Scaffolded initiation for splitting.",
    ],
)
```

```python
# agents/allocator.py

allocator = Agent(
    name="CAWDP Allocator",
    model=Ollama(id="glm-5.1:cloud"),
    tools=[
        score_task_allocation,     # Pass 1: capability gap
        assess_adjustment_factors,  # Pass 2: adjustment factors
        allocate_task,              # Final allocation
    ],
    instructions=[
        "You are an Assessor-class agent. Your authority boundary: never finalize.",
        "Your job: score capability gaps, assess adjustment factors, "
        "and PROPOSE allocation. The human MAKES the final allocation.",
        "",
        "TWO-PASS PROCESS:",
        "",
        "PASS 1 — Capability Gap:",
        "Score each dimension 1-10 for Human/Agent/System.",
        "Calculate gaps between highest and second-highest.",
        "Gap ≥ 6 on any Human dimension → potential Human-only.",
        "Gap ≥ 6 on any Agent dimension → potential Agent-primary.",
        "",
        "PASS 2 — Adjustment Factors:",
        "For every task initially rated 'Human-only', assess:",
        "  1. Cold Start Difficulty (self-starting/scaffolded/discovery)",
        "  2. Experience Dependency (expert-dependent/pattern-augmented/procedural)",
        "  3. Discovery vs Decision (decision/mixed/discovery)",
        "  4. Preparation Value (low/medium/high)",
        "  5. Reversibility (high/medium/low)",
        "",
        "OVERRIDE RULES:",
        "  - 2+ factors shift toward collaboration → override to Collaborative",
        "  - Discovery/Scaffolded initiation → always collaborative",
        "  - Low reversibility → human final authority always",
        "  - Expert-dependent → human-primary with agent preparation",
        "  - High preparation value → agent preparation required",
        "  - Document WHY, not just WHAT",
        "",
        "ALLOCATION RATIONALE FORMAT:",
        "  Task: [name]",
        "  Gap allocation: [from Pass 1]",
        "  Adjusted allocation: [from Pass 2]",
        "  Rationale: [why, referencing specific factors]",
        "  Preparation: [how agent prepares, if collaborative]",
        "  Authority: [who has final say]",
        "",
        "FAILURE MODE: overt classification, missing preparation need.",
        "The gap score measures CAPABILITY. Adjustment factors measure PREPARATION NEED.",
        "Both must be assessed before allocation.",
        "You PREPARE allocation. The human DECIDES.",
    ],
)
```

### Workflow Structure

```python
# workflows/decomposition_allocation.py

from agno.workflows import Workflow
from agno.workflows.types import OnReject

decomp_alloc_workflow = Workflow(
    name="decomposition_allocation",
    steps=[
        # Step 1: Decompose
        Step(
            name="decompose",
            agent=decomposer,
            tools=[decompose_task_tool],
            output_schema=DecomposedTasks,  # Pydantic model
        ),
        # Step 2: Type
        Step(
            name="type",
            agent=typer,
            tools=[classify_cognitive_type_tool],
            output_schema=TypedTasks,
        ),
        # Step 3: Allocate (two-pass)
        Step(
            name="allocate",
            agent=allocator,
            tools=[
                score_task_allocation,       # Pass 1
                assess_adjustment_factors,   # Pass 2
                allocate_task,               # Propose allocation
            ],
            output_schema=AllocatedTasks,
        ),
        # Step 4: Human review
        Step(
            name="human_review",
            agent=human_review_agent,
            requires_output_review=True,
            on_reject=OnReject.retry,  # Re-try allocation with feedback
        ),
    ],
)
```

### The Key Insight for Implementation

The adjustment factors are the breakthrough. Without them, the allocator would look at T1.1 "Discover principal's purpose" (Intuitive, gap=8) and conclude "Human-only." With them, the allocator looks at the same task, sees Discovery initiation + High preparation value, and overrides to "Collaborative, human-final."

The two-pass process is the implementation of the core CAWDP principle at the allocation level:

- Pass 1 answers: "Who is *better* at this?" (Capability)
- Pass 2 answers: "Can the better actor do it *alone*?" (Preparation need)

When the answer to Pass 2 is "no, they need preparation," the allocation shifts from solo to collaborative. That's the mechanism that catches the five problematic tasks you identified.

Want me to draft the Pydantic schemas for the inter-agent data passing next?

---

## Run 10 — Agentic Expert ✓ COMPLETED

*2026-05-20T23:19:24* · `glm-5.1:cloud` · `2e77dc4f...`

### Prompt

review and provide feedback on this implementation plan:

***
# Plan: Decomposition-Allocation (Phases 3-4)

**TL;DR** — Implement the CAWDP v2.2 Decomposer → Typer → Allocator pipeline as three standalone agents called by the orchestrator. Schema additions to `design_tasks` + new `design_adjustment_factors` table. Writer functions with business rule enforcement. Separate tool factory following the backcasting engine closure pattern. Workflow-only registration (not in main.py).

---

### Phase A — Schema & Writer *(foundation, blocks everything else)*

| Step | What | File |
|------|------|------|
| 1 | Add fields to `design_tasks`: `output_artefact`, `initiation_mode`, `experience_dependency`, `authority_boundary`, `decomposition_pattern`, `conflation_check`, `allocation_rationale`, `preparation_method`, `adjusted_allocation`, `adjustment_summary`, `phase`. Add `Elicitive` to `cognitive_type` enum. | schema.py |
| 2 | Create `design_adjustment_factors` table with 5 factor fields + override tracking | schema.py |
| 3 | Add writer functions: `validate_subtask_properties`, `decompose_task`, `assess_adjustment_factors`, `determine_preparation_method`, `allocate_task` | writer.py |
| 4 | Export new writer functions | __init__.py |

### Phase B — Tool Factory *(depends on Phase A)*

| Step | What | File |
|------|------|------|
| 5 | `create_decomposition_tools()` → `[decompose_task_tool]` and `create_allocation_tools()` → `[assess_adjustment_factors_tool, allocate_task_tool]` — closure pattern from backcasting engine | `agents/tools/decomp_alloc_tools.py` **NEW** |

### Phase C — Agent Definitions *(depends on Phase B)*

| Step | What | File |
|------|------|------|
| 6 | **Decomposer** — Generator-class, "never be vague", conflation test, decomposition pattern library, intuitive task split rule | `agents/decomposer.py` **NEW** |
| 7 | **Typer** — Measurer-class, "never interpret", cognitive operation guide, initiation mode decision tree, experience dependency tree | `agents/typer.py` **NEW** |
| 8 | **Allocator** — Assessor-class, "never finalize", two-pass process, override rules, allocation rationale template | `agents/allocator.py` **NEW** |

### Phase D — Orchestrator Integration *(depends on Phase C)*

| Step | What | File |
|------|------|------|
| 9 | Extend orchestrator instructions with P3/P4 phase descriptions and quality gate checks | cawdp_orchestrator.py |
| 10 | Add sub-agent delegation tools (`run_decomposition`, `run_typing`, `run_allocation`) — follows `code_search.py` context-provider pattern | cawdp_orchestrator.py |
| 11 | Add quick prompts for new agents | config.yaml |

### Phase E — Eval Cases *(depends on Phase D)*

| Step | What | File |
|------|------|------|
| 12 | Add eval cases: conflation test, typing classification, two-pass allocation | cases.py |

---

### Key patterns to follow

- **Tool factory**: tool.py — closure pattern with `client_getter`, `@tool`, `asyncio.run()` wrapper
- **Sub-agent delegation**: code_search.py — tool that internally calls a sub-agent
- **Agent shape**: cawdp_orchestrator.py — `Agent(id=..., model=..., db=get_surrealdb(), tools=..., instructions=...)`
- **Writer pattern**: writer.py — `_get_client()`, try/finally with `client.close()`, SurrealQL parameter binding

### Verification

1. validate.sh — ruff check + mypy passes
2. `docker compose up -d --build` — container builds and starts
3. Manual test: start workflow → run decomposition → run typing → run allocation → verify records in SurrealDB
4. `python -m evals` — new eval cases pass

### Decisions

- **Pipeline**: Separate agents called by orchestrator (not Agno Workflow)
- **Model**: `Ollama(id="glm-5.1:cloud")` — matches your preferences
- **Tool factory**: Separate `create_decomposition_tools()` / `create_allocation_tools()` — follows backcasting engine pattern
- **Registration**: Workflow-only — NOT in main.py, only invoked through orchestrator
- **Out of scope**: No Agno Workflow definition, no frontend, no HITL endpoints
***

### Response

Good plan. The dependency ordering is right, the pattern references are correct, and the decision to keep it orchestrator-managed rather than Agno Workflow is sensible given you want the orchestrator controlling phase transitions.

Three critical gaps, four important improvements, two minor observations.

## Critical Gaps

### 1. The Typer has no tools or writer

Phase B creates tools for Decomposition and Allocation but not Typing. The Typer needs to update existing tasks with classification data — cognitive_type, initiation_mode, experience_dependency. This means:

**Missing from Phase A (writer):** A `classify_task` writer function that updates an existing task's classification fields and validates the values.

**Missing from Phase B (tools):** A `create_typing_tools()` factory that produces `classify_task_tool`.

**Missing from Phase C:** The Typer agent needs its tool factory injected.

The Typer isn't just reading — it's writing classification decisions to the database. Without a writer and tool, it can't do its job.

```python
# writer.py — missing function

async def classify_task(
    client: Surreal,
    task_id: str,
    cognitive_type: str,       # mechanical/analytical/generative/elicitive/evaluative/intuitive
    initiation_mode: str,      # self-starting/scaffolded/discovery
    experience_dependency: str, # expert-dependent/pattern-augmented/procedural
    classified_by: str,
) -> dict:
    """Classify a task's cognitive type, initiation mode, and experience dependency.
    
    Enforces:
    - Valid cognitive type values
    - Valid initiation mode values
    - Valid experience dependency values
    - Task must exist and be in 'decomposed' phase
    - Never assigns allocation (that's the Allocator's job)
    """
```

```python
# decomp_alloc_tools.py — missing factory

def create_typing_tools(client_getter):
    """Create typing tools following the closure pattern."""
    
    @agno_tool(name="classify_task", description="...")
    def classify_task_tool(task_id, cognitive_type, initiation_mode, experience_dependency):
        client = client_getter()
        result = asyncio.run(classify_task(
            client=client,
            task_id=task_id,
            cognitive_type=cognitive_type,
            initiation_mode=initiation_mode,
            experience_dependency=experience_dependency,
            classified_by="cawdp_typer",
        ))
        return json.dumps(result, indent=2)
    
    return [classify_task_tool]
```

This also means Phase B should have three tool factories, not two:

| Factory | Tools |
|---------|-------|
| `create_decomposition_tools()` | `[decompose_task_tool]` |
| `create_typing_tools()` | `[classify_task_tool]` |
| `create_allocation_tools()` | `[assess_adjustment_factors_tool, allocate_task_tool]` |

### 2. Missing `gap_allocation` field

The design has Pass 1 (capability gap) producing an initial allocation and Pass 2 (adjustment factors) producing an adjusted allocation. The adjusted allocation is stored, but the initial gap-based allocation isn't. You need both for:

- **Transparency**: Show the human what changed and why
- **Decision archaeology**: Understand why allocations shifted over time
- **Quality**: Verify that override rules are being applied correctly

Add to `design_tasks`:

```sql
DEFINE FIELD gap_allocation ON design_tasks TYPE string
  ASSERT $value IN ['human-only', 'human-final', 'agent-primary', 'system-enforced', 'collaborative'];
```

And the `allocate_task` writer should enforce: if `gap_allocation != adjusted_allocation`, rationale MUST be populated. This is already in my earlier writer code but the plan's schema doesn't include `gap_allocation`.

### 3. Missing complementarity scoring storage

The Allocator does Pass 1 (capability gap scoring) before Pass 2 (adjustment factors). Where do the H/A/S dimension scores and gap calculations go? You need either:

**Option A** — Fields on `design_tasks`:

```sql
DEFINE FIELD capability_scores ON design_tasks TYPE object;  -- {human: 7, agent: 3, system: 1}
DEFINE FIELD capability_gap ON design_tasks TYPE number;       -- calculated gap
```

**Option B** — Separate `design_capability_scores` table (better for querying and history):

```sql
DEFINE TABLE design_capability_scores SCHEMAFULL;

DEFINE FIELD task ON design_capability_scores TYPE record<design_tasks>;
DEFINE FIELD workflow ON design_capability_scores TYPE record<design_workflows>;
DEFINE FIELD dimension ON design_capability_scores TYPE string;  -- e.g., "intuitive", "analytical"
DEFINE FIELD human_score ON design_capability_scores TYPE number;
DEFINE FIELD agent_score ON design_capability_scores TYPE number;
DEFINE FIELD system_score ON design_capability_scores TYPE number;
DEFINE FIELD gap ON design_capability_scores TYPE number;
DEFINE FIELD scored_by ON design_capability_scores TYPE string;
DEFINE FIELD scored_at ON design_capability_scores TYPE datetime DEFAULT time::now();
```

Option B is better because tasks can have multiple dimensions scored, and you want to query across tasks and workflows. The gap allocation should be derivable from the scores but also stored on the task for quick reference.

## Important Improvements

### 4. Eval cases should include the five problematic tasks

The five tasks that started this conversation are the perfect eval cases — they're the exact failure mode the two-pass process is designed to catch:

```python
# cases.py — eval cases for decomposition-allocation

PROBLEMATIC_TASKS_EVAL = [
    {
        "name": "Discover principal's purpose",
        "original_type": "Intuitive",
        "original_allocation": "Human-only",
        "expected_decomposition": "propose-validate",  # should split
        "expected_initiation": "discovery",
        "expected_adjusted_allocation": "Collaborative (human-final)",
        "expected_rationale": "Human has judgment but faces blank page",
    },
    {
        "name": "Identify what this workflow IS",
        "original_type": "Intuitive",
        "original_allocation": "Human-only",
        "expected_decomposition": "elicit-structure",  # should split
        "expected_initiation": "discovery",
        "expected_adjusted_allocation": "Collaborative (human-final)",
        "expected_rationale": "Identity discovery needs prompting",
    },
    {
        "name": "Discover what would violate identity",
        "original_type": "Intuitive",
        "original_allocation": "Human-only",
        "expected_decomposition": "generate-filter",  # should split
        "expected_initiation": "scaffolded",  # needs patterns to react to
        "expected_adjusted_allocation": "Collaborative (human-final)",
        "expected_rationale": "Agent surfaces failure patterns human hasn't encountered",
    },
    {
        "name": "Define excellent outcomes",
        "original_type": "Intuitive",
        "original_allocation": "Human-only",
        "expected_decomposition": "propose-validate",
        "expected_initiation": "discovery",
        "expected_adjusted_allocation": "Collaborative (human-final)",
        "expected_rationale": "Excellence is discovered through reaction",
    },
    {
        "name": "Identify authority boundaries",
        "original_type": "Evaluative",
        "original_allocation": "Human-only",
        "expected_decomposition": "generate-filter",
        "expected_initiation": "scaffolded",
        "expected_adjusted_allocation": "Collaborative (human-final)",
        "expected_rationale": "Boundaries benefit from broad pattern recognition",
    },
]
```

These should be the primary eval test: if the two-pass process doesn't catch all five and override them to Collaborative, the implementation is wrong.

### 5. Specify object structures for `conflation_check` and `adjustment_summary`

The plan lists these as `TYPE object` but doesn't define their structure. Without explicit structures, the database accepts anything and the writer can't enforce schemas. Define them:

```python
# conflation_check structure
{
    "passed": bool,
    "failures": list[str],         # list of failed property names
    "task_name": str,
    "single_verb": bool,           # property 1
    "clear_output": bool,          # property 2
    "valid_initiation": bool,      # property 3
    "valid_authority": bool,       # property 4
    "valid_failure_mode": bool,    # property 5
    "no_conflation": bool,         # property 6 (no "and")
}

# adjustment_summary structure
{
    "override_count": int,
    "collaborative_override": bool,
    "overrides": [
        {"factor": str, "value": str, "implication": str}
    ],
    "preparation_method": str,
    "gap_allocation": str,          # from Pass 1
    "adjusted_allocation": str,     # from Pass 2
    "rationale": str,               # why it changed
}
```

### 6. Document the data flow explicitly

The plan defines each agent but doesn't show how data moves between them. This matters because the orchestrator manages the sequence:

```
Orchestrator calls Decomposer
    → Decomposer creates subtasks via decompose_task_tool
    → Each subtask has: name, description, cognitive_type (preliminary),
      output_artefact, initiation_mode, experience_dependency,
      authority_boundary, failure_mode, conflation_check
    → Writer enforces conflation test and creates records

Orchestrator calls Typer
    → Typer reads decomposed tasks
    → Typer classifies: cognitive_type, initiation_mode, experience_dependency
    → Typer updates tasks via classify_task_tool
    → Writer validates values and updates records
    → Typer flags Intuitive/Evaluative + Discovery/Scaffolded for splitting

Orchestrator calls Allocator (two-pass)
    → Allocator reads classified tasks
    → Pass 1: score_task_allocation_tool — H/A/S scores, gap calculation
    → Pass 2: assess_adjustment_factors_tool — 5 factors, override rules
    → allocate_task_tool — gap_allocation, adjusted_allocation, rationale
    → Writer enforces override rules and rationale requirements

Orchestrator presents to human for review
    → Human reviews allocations
    → Human can accept, reject (with feedback), or edit
```

### 7. Human gate mechanism

The plan says "No Agno Workflow definition" in Decisions. That's fine — the orchestrator manages the sequence. But you need to be explicit about how the human gate works. The orchestrator should:

1. After Allocator completes, present the allocation table to the human
2. Human can accept all, reject specific allocations (with feedback), or edit specific allocations
3. If rejected, orchestrator re-runs allocation with feedback incorporated
4. Only after human approval does the workflow advance to the next phase

This should be noted in Phase D orchestrator integration — the orchestrator needs a `review_allocation` tool or similar mechanism.

## Minor Observations

### 8. The Decomposer might need read tools

The Decomposer needs to read the parent task and workflow context to decompose properly. The plan only mentions `decompose_task_tool` (a write tool). Consider adding `get_task` and `get_workflow` tools, or having the orchestrator pass context as part of the delegation call.

The same applies to the Typer and Allocator — they need to read tasks to classify or score them. Either the orchestrator passes context, or each agent needs read access.

### 9. `score_task_allocation` (Pass 1)

The Allocator agent definition from my earlier response included a `score_task_allocation` tool for Pass 1 (capability gap scoring). The plan's Phase B doesn't include this tool — it only lists `assess_adjustment_factors_tool` and `allocate_task_tool`. The Allocator needs all three: score (Pass 1) → assess factors (Pass 2) → allocate (final).

## Revised Step List

| # | What | File | Notes |
|---|------|------|-------|
| 1 | Add fields to `design_tasks`: `output_artefact`, `initiation_mode`, `experience_dependency`, `authority_boundary`, `decomposition_pattern`, `conflation_check`, `gap_allocation`, `allocation_rationale`, `preparation_method`, `adjusted_allocation`, `adjustment_summary`. Add `Elicitive` to `cognitive_type` enum. | schema.py | Added `gap_allocation` |
| 2 | Create `design_adjustment_factors` table | schema.py | |
| 3 | Create `design_capability_scores` table | schema.py | New — for H/A/S scores |
| 4 | Add writer functions: `validate_subtask_properties`, `decompose_task`, `classify_task`, `score_task_capability`, `assess_adjustment_factors`, `determine_preparation_method`, `allocate_task` | writer.py | Added `classify_task` and `score_task_capability` |
| 5 | Export new writer functions | __init__.py | |
| 6 | `create_decomposition_tools()` → `[decompose_task_tool]` | decomp_alloc_tools.py | |
| 7 | `create_typing_tools()` → `[classify_task_tool]` | decomp_alloc_tools.py | New |
| 8 | `create_allocation_tools()` → `[score_task_capability_tool, assess_adjustment_factors_tool, allocate_task_tool]` | decomp_alloc_tools.py | Added `score_task_capability_tool` |
| 9 | Decomposer agent | decomposer.py | |
| 10 | Typer agent | typer.py | |
| 11 | Allocator agent | allocator.py | |
| 12 | Extend orchestrator instructions + delegation tools | cawdp_orchestrator.py | |
| 13 | Add quick prompts for new agents | config.yaml | |
| 14 | Add eval cases including the five problematic tasks | cases.py | |
| 15 | Define `conflation_check` and `adjustment_summary` object structures in schema | schema.py | |

The plan is solid. The three gaps (Typer tools, gap_allocation field, capability scores storage) are the things that would bite you during implementation. The rest is polish that makes the system more robust and queryable.

---

## Run 11 — Agentic Expert ✓ COMPLETED

*2026-05-21T04:45:25* · `glm-5.1:cloud` · `e2deccf3...`

### Prompt

Perhaps there is now an opportunities to look at the event storming step and consider the value of a tool or workflow here

### Response

You're right — Event Storming is the natural next step after decomposition-allocation, and it has specific properties that make it particularly suited to agent assistance. Let me explain why, then what the implementation could look like.

## Why Event Storming Benefits Most from Tool Assistance

The four steps we've built tools for so far — backcasting, decomposition, typing, allocation — are all **constructive**. They build something up: dependency chains, subtasks, classifications, allocations. Each step adds structure to the design.

Event Storming is different. It's **adversarial**. Its job is to break the design — to find what's missing, what can go wrong, and what happens when it does. This is fundamentally a different cognitive operation, and it's one humans are bad at naturally. We optimistically focus on happy paths.

Three specific things Event Storming does that benefit from systematic tool assistance:

**1. Systematic coverage.** Every task transition is an opportunity for events, and every event is an opportunity for failure. A human doing this manually will focus on obvious failure points and miss the long tail. A tool can walk every transition systematically.

**2. Failure mode identification from known patterns.** The CAWDP 5-class taxonomy already has characteristic failure modes per agent class. A tool can match each task's allocated agent class to its known failure pattern and generate failure event candidates that a human might not think of.

**3. Data flow validation.** This directly connects back to Phase 2 backcasting. Every output that Phase 2 traced as a dependency should have a corresponding event in Phase 5. A tool can cross-reference the two and flag gaps.

## What Event Storming Produces

From the CAWDP meta-application and the Assignment Marking pipeline, Event Storming produces four things:

| Output | What It Is | Schema Table |
|--------|-----------|--------------|
| Domain events | Normal flow events — things that happen during successful execution | `design_domain_events` |
| Failure events | Things that go wrong — mapped to task + agent class failure modes | `design_failure_events` |
| Recovery paths | What to do when failures occur — who acts, what they do, how it resolves | `design_recovery_paths` |
| System triggers | Automated system responses — events that trigger system actions without human intervention | `design_system_triggers` |

These are linked to `design_tasks` (which event occurs at which task) and to each other (which failure event triggers which recovery path).

## The Schema

```sql
-- Domain events: things that happen during normal execution
DEFINE TABLE design_domain_events SCHEMAFULL;

DEFINE FIELD workflow ON design_domain_events TYPE record<design_workflows>;
DEFINE FIELD task ON design_domain_events TYPE record<design_tasks>;
DEFINE FIELD event_name ON design_domain_events TYPE string;
DEFINE FIELD event_type ON design_domain_events TYPE string
  ASSERT $value IN [
    'task_started', 'task_completed', 'task_failed',
    'phase_entered', 'phase_exited',
    'handoff_initiated', 'handoff_completed',
    'quality_gate_passed', 'quality_gate_failed',
    'progress_milestone', 'state_changed',
    'external_trigger', 'data_received'
  ];
DEFINE FIELD description ON design_domain_events TYPE string;
DEFINE FIELD trigger_condition ON design_domain_events TYPE string;   -- what causes this event
DEFINE FIELD payload ON design_domain_events TYPE string;             -- what data this event carries
DEFINE FIELD downstream_effects ON design_domain_events TYPE string;  -- what this event triggers
DEFINE FIELD identified_by ON design_domain_events TYPE string;
DEFINE FIELD identified_at ON design_domain_events TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_devent_workflow ON design_domain_events FIELDS workflow;
DEFINE INDEX idx_devent_task ON design_domain_events FIELDS task;
DEFINE INDEX idx_devent_type ON design_domain_events FIELDS event_type;

-- Failure events: things that go wrong
DEFINE TABLE design_failure_events SCHEMAFULL;

DEFINE FIELD workflow ON design_failure_events TYPE record<design_workflows>;
DEFINE FIELD task ON design_failure_events TYPE record<design_tasks>;
DEFINE FIELD agent_class ON design_failure_events TYPE string
  ASSERT $value IN ['extractor', 'measurer', 'assessor', 'generator', 'aggregator', 'human', 'system'];
DEFINE FIELD failure_name ON design_failure_events TYPE string;
DEFINE FIELD failure_type ON design_failure_events TYPE string
  ASSERT $value IN [
    'omission',           -- agent misses something it should catch
    'false_alarm',        -- agent flags something incorrectly
    'commission',         -- agent produces harmful output
    'timeout',            -- agent doesn't respond in time
    'data_quality',       -- input data is poor
    'boundary_violation', -- agent exceeds authority boundary
    'handoff_failure',    -- output doesn't reach next step
    'cascading_failure',  -- one failure triggers another
    'stale_data',         -- data is outdated (specification aging)
    'context_loss',       -- agent loses context between steps
    'human_override',     -- human rejects agent output
    'validation_failure'  -- verification catches a problem
  ];
DEFINE FIELD severity ON design_failure_events TYPE string
  ASSERT $value IN ['low', 'medium', 'high', 'critical'];
DEFINE FIELD characteristic_failure ON design_failure_events TYPE string;
  -- Maps to CAWDP 5-class taxonomy:
  -- Extractor: "never judges" → judgment creep
  -- Measurer: "never interprets" → noise-as-signal
  -- Assessor: "overconfidence" → false certainty
  -- Generator: "never be vague" → fabrication
  -- Aggregator: "never adds" → omission
DEFINE FIELD description ON design_failure_events TYPE string;
DEFINE FIELD detection_mechanism ON design_failure_events TYPE string;  -- how would you know this happened?
DEFINE FIELD likelihood ON design_failure_events TYPE string
  ASSERT $value IN ['unlikely', 'possible', 'likely', 'very_likely'];
DEFINE FIELD identified_by ON design_failure_events TYPE string;
DEFINE FIELD identified_at ON design_failure_events TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_fevent_workflow ON design_failure_events FIELDS workflow;
DEFINE INDEX idx_fevent_task ON design_failure_events FIELDS task;
DEFINE INDEX idx_fevent_agent_class ON design_failure_events FIELDS agent_class;
DEFINE INDEX idx_fevent_severity ON design_failure_events FIELDS severity;

-- Recovery paths: what to do when failures occur
DEFINE TABLE design_recovery_paths SCHEMAFULL;

DEFINE FIELD workflow ON design_recovery_paths TYPE record<design_workflows>;
DEFINE FIELD failure_event ON design_recovery_paths TYPE record<design_failure_events>;
DEFINE FIELD recovery_strategy ON design_recovery_paths TYPE string
  ASSERT $value IN [
    'retry',              -- try the same task again
    'escalate',           -- escalate to human
    'fallback',           -- use fallback tier
    'skip',               -- skip this task and continue
    'restart_phase',      -- restart the entire phase
    'halt',               -- stop the pipeline
    'reprocess',          -- reprocess with different parameters
    'alternative_path'   -- use a different agent or approach
  ];
DEFINE FIELD recovery_description ON design_recovery_paths TYPE string;
DEFINE FIELD recovery_actor ON design_recovery_paths TYPE string
  ASSERT $value IN ['human', 'agent', 'system', 'human_agent_collaborative'];
DEFINE FIELD recovery_trigger ON design_recovery_paths TYPE string;  -- what triggers this recovery
DEFINE FIELD time_budget ON design_recovery_paths TYPE string;       -- how long recovery should take
DEFINE FIELD success_criteria ON design_recovery_paths TYPE string;  -- how do we know recovery worked
DEFINE FIELD designed_by ON design_recovery_paths TYPE string;
DEFINE FIELD designed_at ON design_recovery_paths TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_rpath_workflow ON design_recovery_paths FIELDS workflow;
DEFINE INDEX idx_rpath_failure ON design_recovery_paths FIELDS failure_event;
DEFINE INDEX idx_rpath_strategy ON design_recovery_paths FIELDS recovery_strategy;

-- System triggers: automated responses
DEFINE TABLE design_system_triggers SCHEMAFULL;

DEFINE FIELD workflow ON design_system_triggers TYPE record<design_workflows>;
DEFINE FIELD trigger_event ON design_system_triggers TYPE string;     -- what event triggers this
DEFINE FIELD trigger_source ON design_system_triggers TYPE string;    -- domain_event or failure_event
DEFINE FIELD trigger_type ON design_system_triggers TYPE string
  ASSERT $value IN [
    'automatic_progression',  -- task completed → advance to next
    'quality_gate_check',     -- task completed → run quality gate
    'timeout_alert',          -- time exceeded → alert
    'escalation_trigger',     -- failure → escalate to human
    'fallback_activation',    -- failure → activate fallback
    'specification_aging',    -- staleness detected → flag for review
    'cost_threshold',         -- budget exceeded → halt
    'progressive_autonomy',  -- criteria met → promote autonomy level
    'data_freshness'          -- data outdated → trigger re-extraction
  ];
DEFINE FIELD action ON design_system_triggers TYPE string;            -- what the system does
DEFINE FIELD action_parameters ON design_system_triggers TYPE object;  -- parameters for the action
DEFINE FIELD enforced_by ON design_system_triggers TYPE string
  ASSERT $value IN ['declare', 'detect', 'prevent'];  -- CC-4 enforcement regime
DEFINE FIELD designed_by ON design_system_triggers TYPE string;
DEFINE FIELD designed_at ON design_system_triggers TYPE datetime DEFAULT time::now();

DEFINE INDEX idx_strigger_workflow ON design_system_triggers FIELDS workflow;
DEFINE INDEX idx_strigger_type ON design_system_triggers FIELDS trigger_type;
DEFINE INDEX idx_strigger_enforcement ON design_system_triggers FIELDS enforced_by;
```

## The Agent

Event Storming uses a fundamentally different cognitive operation than decomposition-allocation. It's **adversarial** — looking for what can go wrong. This is a **Measurer + Assessor** combination:

```python
# agents/event_stormer.py

event_stormer = Agent(
    name="CAWDP Event Stormer",
    model=Ollama(id="glm-5.1:cloud"),
    tools=[
        identify_domain_events_tool,
        identify_failure_events_tool,
        design_recovery_path_tool,
        design_system_trigger_tool,
        validate_data_flow_tool,
        cross_reference_backcasting_tool,
    ],
    instructions=[
        "You are a Measurer+Assessor class agent with bridge orientation.",
        "Your authority boundary: measure what can fail, assess recovery options, "
        "never design the workflow itself.",
        "",
        "YOUR JOB: For every task in the workflow, systematically identify:",
        "  1. Domain events (normal flow events at each task transition)",
        "  2. Failure events (things that can go wrong, mapped to agent class failure modes)",
        "  3. Recovery paths (what to do when failures occur)",
        "  4. System triggers (automated responses)",
        "",
        "CHARACTERISTIC FAILURE MODES BY CLASS:",
        "  Extractor: judgment creep (starts interpreting, not just extracting)",
        "  Measurer: noise-as-signal (treats noise as meaningful signal)",
        "  Assessor: overconfidence (expresses certainty beyond evidence)",
        "  Generator: fabrication (generates plausible but false content)",
        "  Aggregator: omission (drops content during assembly)",
        "  Human: override (rejects correct output), rubber-stamp (approves without review)",
        "  System: timeout, data quality, context loss",
        "",
        "FAILURE IDENTIFICATION APPROACH:",
        "  For each task, ask:",
        "  - What if the agent misses something? (omission)",
        "  - What if the agent flags something incorrectly? (false alarm)",
        "  - What if the agent produces harmful output? (commission)",
        "  - What if the agent doesn't respond? (timeout)",
        "  - What if input data is poor? (data quality)",
        "  - What if the agent exceeds its authority boundary? (boundary violation)",
        "  - What if the output doesn't reach the next step? (handoff failure)",
        "  - What if one failure triggers another? (cascading failure)",
        "  - What if data is outdated? (specification aging)",
        "  - What if the agent loses context? (context loss)",
        "  - What if the human overrides correct output? (human override)",
        "  - What if verification catches a problem? (validation failure)",
        "",
        "RECOVERY STRATEGY SELECTION:",
        "  retry: when failure is transient or random",
        "  escalate: when human judgment is needed",
        "  fallback: when alternative agent or approach exists",
        "  skip: when task is non-critical and can be bypassed",
        "  restart_phase: when failure corrupts the entire phase",
        "  halt: when failure could cause cascading harm",
        "  reprocess: when different parameters might succeed",
        "  alternative_path: when different agent class or approach works",
        "",
        "SYSTEM TRIGGER DESIGN:",
        "  For each event, ask: should this trigger an automatic system response?",
        "  If yes, what enforcement regime? (declare/detect/prevent)",
        "  Progressive autonomy: criteria met → promote autonomy level",
        "  Specification aging: staleness detected → flag for review",
        "  Cost thresholds: budget exceeded → halt",
        "  Quality gates: task completed → run quality gate",
        "",
        "DATA FLOW VALIDATION:",
        "  Cross-reference Phase 2 backcasting outputs with Phase 5 events.",
        "  Every output dependency from Phase 2 should have a corresponding",
        "  domain event in Phase 5. Gaps = missing events.",
        "  Every input requirement from Phase 2 should have a corresponding",
        "  event that produces it. Gaps = missing data sources.",
        "",
        "FAILURE MODE: identifying only obvious failures, missing the long tail.",
        "Systematic coverage is more important than creative failure identification.",
    ],
)
```

## The Tools

```python
# agents/tools/event_storming_tools.py

def create_event_storming_tools(client_getter):
    """Create event storming tools following the closure pattern."""

    @agno_tool(
        name="identify_domain_events",
        description=(
            "Identify domain events for a task — normal flow events that "
            "occur during successful execution. Walk every task transition "
            "systematically and identify what events occur at each."
        ),
    )
    def identify_domain_events_tool(
        workflow_id: str,
        task_id: str,
        events: list[dict],
    ) -> str:
        """Identify domain events for a task.

        Each event dict must have:
            event_name: str - descriptive name
            event_type: str - category from defined types
            description: str - what happens
            trigger_condition: str - what causes this event
            payload: str - what data this event carries
            downstream_effects: str - what this event triggers

        Args:
            workflow_id: The workflow this belongs to
            task_id: The task this event occurs at
            events: List of domain event dictionaries
        """
        client = client_getter()
        result = asyncio.run(identify_domain_events(
            client=client,
            workflow_id=workflow_id,
            task_id=task_id,
            events=events,
            identified_by="cawdp_event_stormer",
        ))
        return json.dumps(result, indent=2)

    @agno_tool(
        name="identify_failure_events",
        description=(
            "Identify failure events for a task — things that can go wrong, "
            "mapped to the allocated agent's characteristic failure modes. "
            "Use the 5-class taxonomy failure patterns as starting points."
        ),
    )
    def identify_failure_events_tool(
        workflow_id: str,
        task_id: str,
        agent_class: str,
        failures: list[dict],
    ) -> str:
        """Identify failure events for a task.

        Each failure dict must have:
            failure_name: str - descriptive name
            failure_type: str - category from defined types
            severity: str - low/medium/high/critical
            description: str - what goes wrong
            detection_mechanism: str - how would you know this happened
            likelihood: str - unlikely/possible/likely/very_likely

        Args:
            workflow_id: The workflow this belongs to
            task_id: The task where this failure could occur
            agent_class: The class of agent allocated to this task
        """
        client = client_getter()
        result = asyncio.run(identify_failure_events(
            client=client,
            workflow_id=workflow_id,
            task_id=task_id,
            agent_class=agent_class,
            failures=failures,
            identified_by="cawdp_event_stormer",
        ))
        return json.dumps(result, indent=2)

    @agno_tool(
        name="design_recovery_path",
        description=(
            "Design a recovery path for a failure event — what to do "
            "when this failure occurs, who acts, and what success looks like."
        ),
    )
    def design_recovery_path_tool(
        workflow_id: str,
        failure_event_id: str,
        recovery_strategy: str,
        recovery_description: str,
        recovery_actor: str,
        recovery_trigger: str,
        time_budget: str,
        success_criteria: str,
    ) -> str:
        """Design a recovery path for a failure event.

        Args:
            workflow_id: The workflow this belongs to
            failure_event_id: The failure event this recovery addresses
            recovery_strategy: retry/escalate/fallback/skip/restart_phase/halt/reprocess/alternative_path
            recovery_description: What to do
            recovery_actor: human/agent/system/human_agent_collaborative
            recovery_trigger: What triggers this recovery
            time_budget: How long recovery should take
            success_criteria: How do we know recovery worked
        """
        client = client_getter()
        result = asyncio.run(design_recovery_path(
            client=client,
            workflow_id=workflow_id,
            failure_event_id=failure_event_id,
            recovery_strategy=recovery_strategy,
            recovery_description=recovery_description,
            recovery_actor=recovery_actor,
            recovery_trigger=recovery_trigger,
            time_budget=time_budget,
            success_criteria=success_criteria,
            designed_by="cawdp_event_stormer",
        ))
        return json.dumps(result, indent=2)

    @agno_tool(
        name="design_system_trigger",
        description=(
            "Design a system trigger — an automated response to an event. "
            "Specify what event triggers it, what action the system takes, "
            "and what enforcement regime applies (declare/detect/prevent)."
        ),
    )
    def design_system_trigger_tool(
        workflow_id: str,
        trigger_event: str,
        trigger_source: str,
        trigger_type: str,
        action: str,
        action_parameters: dict,
        enforced_by: str,
    ) -> str:
        """Design a system trigger for automated responses.

        Args:
            workflow_id: The workflow this belongs to
            trigger_event: What event triggers this
            trigger_source: domain_event or failure_event
            trigger_type: automatic_progression/quality_gate_check/etc
            action: What the system does
            action_parameters: Parameters for the action
            enforced_by: declare/detect/prevent
        """
        client = client_getter()
        result = asyncio.run(design_system_trigger(
            client=client,
            workflow_id=workflow_id,
            trigger_event=trigger_event,
            trigger_source=trigger_source,
            trigger_type=trigger_type,
            action=action,
            action_parameters=action_parameters,
            enforced_by=enforced_by,
            designed_by="cawdp_event_stormer",
        ))
        return json.dumps(result, indent=2)

    @agno_tool(
        name="validate_data_flow",
        description=(
            "Cross-reference Phase 2 backcasting outputs with Phase 5 events. "
            "Every output dependency from Phase 2 should have a corresponding "
            "domain event. Every input requirement should have a producing event. "
            "Gaps indicate missing events."
        ),
    )
    def validate_data_flow_tool(
        workflow_id: str,
    ) -> str:
        """Validate data flow between Phase 2 backcasting and Phase 5 events.

        Checks:
        1. Every output dependency from Phase 2 has a domain event that produces it
        2. Every input requirement from Phase 2 has a domain event that satisfies it
        3. Every handoff between tasks has a domain event
        4. Every failure event has a recovery path

        Returns a gap report with missing events and unaddressed failures.
        """
        client = client_getter()
        result = asyncio.run(validate_data_flow(
            client=client,
            workflow_id=workflow_id,
        ))
        return json.dumps(result, indent=2)

    @agno_tool(
        name="cross_reference_backcasting",
        description=(
            "Cross-reference Phase 2 input requirements with Phase 5 events. "
            "Identify which events produce the inputs that Phase 2 identified "
            "as dependencies, and which events consume the outputs that "
            "Phase 2 identified as deliverables."
        ),
    )
    def cross_reference_backcasting_tool(
        workflow_id: str,
    ) -> str:
        """Cross-reference backcasting dependencies with event storming events.

        Produces a traceability matrix showing:
        - Which Phase 2 outputs are produced by which Phase 5 events
        - Which Phase 2 input requirements are satisfied by which Phase 5 events
        - Which Phase 2 dependencies have no corresponding Phase 5 event (gap)
        - Which Phase 5 events have no corresponding Phase 2 dependency (orphan)
        """
        client = client_getter()
        result = asyncio.run(cross_reference_backcasting(
            client=client,
            workflow_id=workflow_id,
        ))
        return json.dumps(result, indent=2)

    return [
        identify_domain_events_tool,
        identify_failure_events_tool,
        design_recovery_path_tool,
        design_system_trigger_tool,
        validate_data_flow_tool,
        cross_reference_backcasting_tool,
    ]
```

## Writer Functions

The key writer functions, following the enforcement pattern:

```python
# db/writer.py — Event Storming additions

AGENT_CLASS_FAILURE_MODES = {
    'extractor': 'judgment creep — starts interpreting, not just extracting',
    'measurer': 'noise-as-signal — treats noise as meaningful signal',
    'assessor': 'overconfidence — expresses certainty beyond evidence',
    'generator': 'fabrication — generates plausible but false content',
    'aggregator': 'omission — drops content during assembly',
    'human': 'override (rejects correct output) or rubber-stamp (approves without review)',
    'system': 'timeout, data quality, context loss',
}

async def identify_domain_events(
    client: Surreal,
    workflow_id: str,
    task_id: str,
    events: list[dict],
    identified_by: str,
) -> list[str]:
    """Create domain events for a task.
    
    Enforces:
    - Valid event types
    - Every task transition has events
    - Events are linked to tasks
    """
    valid_types = [
        'task_started', 'task_completed', 'task_failed',
        'phase_entered', 'phase_exited',
        'handoff_initiated', 'handoff_completed',
        'quality_gate_passed', 'quality_gate_failed',
        'progress_milestone', 'state_changed',
        'external_trigger', 'data_received',
    ]
    
    created_ids = []
    for event in events:
        if event.get('event_type') not in valid_types:
            raise ValueError(f"Invalid event type: {event.get('event_type')}")
        
        result = await client.query(
            """CREATE design_domain_events SET
               workflow = $wf,
               task = $task,
               event_name = $name,
               event_type = $type,
               description = $desc,
               trigger_condition = $trigger,
               payload = $payload,
               downstream_effects = $effects,
               identified_by = $by,
               identified_at = time::now()
            """,
            {
                "wf": workflow_id,
                "task": task_id,
                "name": event['event_name'],
                "type": event['event_type'],
                "desc": event['description'],
                "trigger": event.get('trigger_condition', ''),
                "payload": event.get('payload', ''),
                "effects": event.get('downstream_effects', ''),
                "by": identified_by,
            }
        )
        created_ids.append(result[0]['id'])
    
    return created_ids


async def identify_failure_events(
    client: Surreal,
    workflow_id: str,
    task_id: str,
    agent_class: str,
    failures: list[dict],
    identified_by: str,
) -> list[str]:
    """Create failure events for a task.
    
    Enforces:
    - Valid failure types
    - Valid severity levels
    - Agent class matches task allocation
    - Characteristic failure mode is populated from taxonomy
    - Every failure has a detection mechanism
    """
    valid_failure_types = [
        'omission', 'false_alarm', 'commission', 'timeout',
        'data_quality', 'boundary_violation', 'handoff_failure',
        'cascading_failure', 'stale_data', 'context_loss',
        'human_override', 'validation_failure',
    ]
    
    valid_severities = ['low', 'medium', 'high', 'critical']
    valid_likelihoods = ['unlikely', 'possible', 'likely', 'very_likely']
    valid_classes = ['extractor', 'measurer', 'assessor', 'generator', 'aggregator', 'human', 'system']
    
    # Validate agent class
    if agent_class not in valid_classes:
        raise ValueError(f"Invalid agent class: {agent_class}")
    
    # Get characteristic failure mode from taxonomy
    characteristic_failure = AGENT_CLASS_FAILURE_MODES.get(
        agent_class, 'unknown'
    )
    
    created_ids = []
    for failure in failures:
        # Validate failure type
        if failure.get('failure_type') not in valid_failure_types:
            raise ValueError(f"Invalid failure type: {failure.get('failure_type')}")
        
        # Validate severity
        if failure.get('severity') not in valid_severities:
            raise ValueError(f"Invalid severity: {failure.get('severity')}")
        
        # Validate likelihood
        if failure.get('likelihood') not in valid_likelihoods:
            raise ValueError(f"Invalid likelihood: {failure.get('likelihood')}")
        
        # Require detection mechanism
        if not failure.get('detection_mechanism'):
            raise ValueError(
                f"Failure '{failure.get('failure_name')}' has no detection mechanism. "
                f"Every failure must have a way to detect it."
            )
        
        result = await client.query(
            """CREATE design_failure_events SET
               workflow = $wf,
               task = $task,
               agent_class = $class,
               failure_name = $name,
               failure_type = $type,
               severity = $severity,
               characteristic_failure = $char_fail,
               description = $desc,
               detection_mechanism = $detection,
               likelihood = $likelihood,
               identified_by = $by,
               identified_at = time::now()
            """,
            {
                "wf": workflow_id,
                "task": task_id,
                "class": agent_class,
                "name": failure['failure_name'],
                "type": failure['failure_type'],
                "severity": failure['severity'],
                "char_fail": characteristic_failure,
                "desc": failure['description'],
                "detection": failure['detection_mechanism'],
                "likelihood": failure.get('likelihood', 'possible'),
                "by": identified_by,
            }
        )
        created_ids.append(result[0]['id'])
    
    return created_ids


async def validate_data_flow(
    client: Surreal,
    workflow_id: str,
) -> dict:
    """Cross-reference Phase 2 backcasting with Phase 5 events.
    
    Checks:
    1. Every output dependency has a producing event
    2. Every input requirement has a satisfying event
    3. Every task transition has a handoff event
    4. Every failure event has a recovery path
    
    Returns a gap report.
    """
    gaps = {
        "missing_producing_events": [],  # Phase 2 outputs with no Phase 5 event
        "missing_satisfying_events": [],  # Phase 2 inputs with no Phase 5 event
        "missing_handoff_events": [],     # Task transitions with no handoff event
        "unrecovered_failures": [],       # Failure events with no recovery path
        "orphan_events": [],             # Phase 5 events with no Phase 2 dependency
    }
    
    # 1. Check Phase 2 output dependencies
    outputs = await client.query(
        "SELECT * FROM design_artefacts WHERE workflow = $wf",
        {"wf": workflow_id}
    )
    output_deps = await client.query(
        "SELECT * FROM design_output_dependencies WHERE workflow = $wf",
        {"wf": workflow_id}
    )
    
    for dep in output_deps:
        producing_events = await client.query(
            "SELECT count() FROM design_domain_events WHERE workflow = $wf AND downstream_effects INCLUDES $dep_id",
            {"wf": workflow_id, "dep_id": dep['id']}
        )
        if producing_events[0]['count'] == 0:
            gaps["missing_producing_events"].append({
                "output": dep.get('output_name', dep['id']),
                "required_by": dep.get('required_by', ''),
            })
    
    # 2. Check Phase 2 input requirements
    input_reqs = await client.query(
        "SELECT * FROM design_input_requirements WHERE workflow = $wf",
        {"wf": workflow_id}
    )
    
    for req in input_reqs:
        satisfying_events = await client.query(
            "SELECT count() FROM design_domain_events WHERE workflow = $wf AND payload INCLUDES $req_id",
            {"wf": workflow_id, "req_id": req['id']}
        )
        if satisfying_events[0]['count'] == 0:
            gaps["missing_satisfying_events"].append({
                "requirement": req.get('ir_description', req['id']),
                "criticality": req.get('ir_criticality', ''),
            })
    
    # 3. Check for unrecovered failures
    failures = await client.query(
        "SELECT * FROM design_failure_events WHERE workflow = $wf",
        {"wf": workflow_id}
    )
    
    for failure in failures:
        recovery = await client.query(
            "SELECT count() FROM design_recovery_paths WHERE failure_event = $fid",
            {"fid": failure['id']}
        )
        if recovery[0]['count'] == 0:
            gaps["unrecovered_failures"].append({
                "failure": failure.get('failure_name', failure['id']),
                "severity": failure.get('severity', ''),
                "agent_class": failure.get('agent_class', ''),
            })
    
    # Summary
    total_gaps = sum(len(v) for v in gaps.values())
    gaps["summary"] = {
        "total_gaps": total_gaps,
        "producing_event_gaps": len(gaps["missing_producing_events"]),
        "satisfying_event_gaps": len(gaps["missing_satisfying_events"]),
        "handoff_gaps": len(gaps["missing_handoff_events"]),
        "unrecovered_failures": len(gaps["unrecovered_failures"]),
        "orphan_events": len(gaps["orphan_events"]),
    }
    
    return gaps
```

## The Data Flow Validation Connection

The most valuable tool is `validate_data_flow`. It cross-references Phase 2 backcasting outputs with Phase 5 events and produces a gap report. This is the systematic coverage that humans are bad at — checking every dependency chain to make sure nothing is missing.

The validation produces five types of gaps:

| Gap Type | What It Means | Severity |
|----------|-------------|----------|
| Missing producing event | Phase 2 says this output is needed, but no Phase 5 event produces it | High — the pipeline has a hole |
| Missing satisfying event | Phase 2 says this input is required, but no Phase 5 event satisfies it | High — a task will fail at startup |
| Missing handoff event | A task transition has no event marking the handoff | Medium — tracking gap |
| Unrecovered failure | A failure event has no recovery path | Critical — the pipeline has no fallback |
| Orphan event | Phase 5 event has no Phase 2 dependency | Low — possibly unnecessary |

## How It Fits in the Pipeline

Event Storming (Phase 5) sits between Allocation (Phase 4) and System Architecture (Phase 6). The orchestrator calls it after the human gate on allocation:

```
Backcasting (Phase 2) → Decomposition (Phase 3) → Typing → Allocation (Phase 4)
    → Human Gate on Allocation
    → Event Storming (Phase 5)
    → Data Flow Validation
    → Human Gate on Event Storming
    → System Architecture (Phase 6)
```

The data flow validation tool creates a direct line from Phase 2 (backcasting dependency chains) through Phase 5 (events that produce/consume those dependencies) to Phase 6 (system architecture that implements the events). This is the "backcasting has its direction" insight made structural — every output traced in Phase 2 must have an event in Phase 5 that produces it.

## What Makes This Valuable

The Event Storming step is where CAWDP's stress-testing becomes structural. Without it:

- Failure modes are identified casually, not systematically
- Recovery paths are assumed, not designed
- System triggers are implicit, not specified
- Data flow gaps are discovered in production, not in design

With it:

- Every task gets failure analysis mapped to its agent class
- Every failure gets a recovery strategy with an actor and success criteria
- Every automated response gets an enforcement regime (declare/detect/prevent)
- Every Phase 2 dependency gets checked against Phase 5 events

The characteristic failure modes per agent class (Extractor: judgment creep, Measurer: noise-as-signal, etc.) give the Event Stormer systematic starting points that a human working alone might miss. The data flow validation gives it a systematic completeness check that a human can't do manually for complex workflows.

Want me to write up the full implementation plan for this as a Phase F addition to your existing plan?

---

## Run 12 — Agentic Expert ✓ COMPLETED

*2026-05-21T06:39:29* · `glm-5.1:cloud` · `3d2b821e...`

### Prompt

Here's an implementation plan for this. What are your notes?

***
# Feasibility Review: Event Storming Tool

### Verdict: **Highly Feasible** — the proposal maps cleanly onto existing patterns

The proposal is well-researched and follows the established architecture. Here's my detailed assessment:

---

### ✅ What Works Well

**1. Phase slot already exists.** The orchestrator's phase sequence already includes P5 (Event Storming) and `VALID_TRANSITIONS` in writer.py maps `P4 → P5`. The pipeline is ready — just needs the agent and tools.

**2. Agent pattern is a direct copy of existing sub-agents.** The proposed `event_stormer.py` follows the exact same shape as decomposer.py, typer.py, and allocator.py:
- Agent definition with instructions, model, `db=get_surrealdb()`, tools from a factory
- Tool factory closure pattern (`create_event_storming_tools(client_getter)`)
- Writer functions in writer.py
- Orchestrator delegates via `run_event_storming` tool

**3. The Measurer+Assessor framing is correct.** Event Storming is adversarial — finding what can go wrong — which maps naturally to Measurer (measure what can fail) + Assessor (assess recovery options). The "bridge orientation" is right too, since it connects Phase 2 backcasting to Phase 6 architecture.

**4. Data flow validation is the killer feature.** Cross-referencing Phase 2 backcasting outputs with Phase 5 events is exactly the kind of systematic check that humans miss. The existing `design_input_requirements` and `design_artefact_dependency` tables make this queryable.

---

### ⚠️ Issues & Recommendations

#### 1. Schema tables already partially exist — reuse `runtime_events`

The proposal creates four new `design_*` tables. But the schema already has `runtime_events` with `event_category` (Domain, Failure, Recovery). This creates ambiguity:

| Proposal Table | Existing Table | Recommendation |
|---|---|---|
| `design_domain_events` | `runtime_events` (event_category='Domain') | **Keep `design_domain_events`** — design-time vs runtime is a meaningful distinction. The design tables capture *planned* events; `runtime_events` captures *actual* occurrences. |
| `design_failure_events` | `runtime_events` (event_category='Failure') | Same reasoning — keep separate. |
| `design_recovery_paths` | None | New table needed. |
| `design_system_triggers` | None | New table needed. |

**Recommendation**: Add a `design_phase` field to the new tables (like `design_tasks` has `phase`) so they can track whether events are draft, reviewed, or locked. The proposal's `identified_at` is good but doesn't capture workflow state.

#### 2. The `validate_data_flow` tool needs to query `design_input_requirements` — but those use `ir_id` strings, not SurrealDB record IDs

Looking at writer.py, `save_requirement` stores `ir_id` as a string field, not a record reference. The proposal's validation queries assume record IDs. The cross-reference needs to match on `ir_id` or `description` strings, not SurrealDB record IDs.

**Recommendation**: Add a `design_output_dependencies` table (or reuse `design_artefact_dependency` with a task context) so the data flow validation has concrete edges to traverse. The proposal's `validate_data_flow` function queries `design_output_dependencies` and `design_input_requirements` — but `design_output_dependencies` doesn't exist in the schema yet.

#### 3. The `cross_reference_backcasting` tool overlaps with `validate_data_flow`

Both tools do essentially the same thing — cross-reference Phase 2 outputs with Phase 5 events. The proposal defines both as separate tools, but the difference is subtle:
- `validate_data_flow`: checks every output dependency has a producing event
- `cross_reference_backcasting`: produces a traceability matrix

**Recommendation**: Merge into a single `validate_event_coverage` tool that returns both a gap report AND a traceability matrix. Two tools will confuse the agent.

#### 4. The `characteristic_failure` field on `design_failure_events` should be auto-populated, not agent-provided

The proposal has the agent pass `characteristic_failure` as a string. But this is a deterministic mapping from `agent_class` — it should be computed by the writer function, just like the proposal's `AGENT_CLASS_FAILURE_MODES` dict. The agent shouldn't be trusted to supply this correctly.

**Recommendation**: The writer function should auto-populate `characteristic_failure` from the `agent_class` field, exactly as the proposal's `identify_failure_events` already does. Remove it from the tool's input parameters.

#### 5. The `design_system_triggers` table's `action_parameters` field is `TYPE object` — but SurrealDB v2 doesn't support generic `object` well for queries

The proposal defines `action_parameters ON design_system_triggers TYPE object`. In SurrealDB v2, `object` fields are opaque — you can't query into them with dot notation unless you define a `FLEXIBLE SCHEMA` or use `SCHEMALESS`.

**Recommendation**: Either make `design_system_triggers` `SCHEMALESS` (since trigger parameters are inherently variable), or define specific parameter fields. I'd recommend `SCHEMALESS` — it's the pragmatic choice for heterogeneous action parameters.

#### 6. The orchestrator needs a `run_event_storming` delegation tool

The proposal doesn't explicitly add this to the orchestrator. Following the pattern from `run_decomposition`, `run_typing`, and `run_allocation`, the orchestrator needs:
- A `run_event_storming` tool that delegates to the event stormer agent
- A `review_event_storming` tool that presents results to the human
- Registration of the event stormer agent (imported, not registered in main.py — it's a sub-agent)

#### 7. The proposal's `validate_data_flow` function uses `INCLUDES` operator — verify SurrealDB v2 support

The proposal uses `downstream_effects INCLUDES $dep_id` and `payload INCLUDES $req_id`. The `INCLUDES` operator checks if an array contains a value. This works if `downstream_effects` and `payload` are arrays, but they're defined as `TYPE string` in the schema.

**Recommendation**: Change `downstream_effects` and `payload` to `TYPE array` in the schema, or use `CONTAINS` for string matching. Array is more appropriate since these are lists of references.

---

### Implementation Plan

Here's how I'd implement this, following the existing patterns exactly:

**Phase 1 — Schema (1 file)**
1. Add four new tables to schema.py: `design_domain_events`, `design_failure_events`, `design_recovery_paths`, `design_system_triggers` — following the proposal's schema but with the fixes above (auto-populated `characteristic_failure`, `SCHEMALESS` for triggers, array types for payload/effects)

**Phase 2 — Writer functions (1 file)**
2. Add to writer.py:
   - `AGENT_CLASS_FAILURE_MODES` dict
   - `identify_domain_events()` — validates event types, writes to `design_domain_events`
   - `identify_failure_events()` — validates failure types/severity/likelihood, auto-populates characteristic failure, writes to `design_failure_events`
   - `design_recovery_path()` — validates strategy/actor, writes to `design_recovery_paths`
   - `design_system_trigger()` — validates trigger type/enforcement, writes to `design_system_triggers`
   - `validate_event_coverage()` — queries `design_input_requirements` + new event tables, returns gap report + traceability matrix

**Phase 3 — Tool factory (1 file)**
3. Create `agents/tools/event_storming_tools.py` with `create_event_storming_tools(client_getter)` — following the exact closure pattern from decomp_alloc_tools.py. Tools:
   - `identify_domain_events`
   - `identify_failure_events`
   - `design_recovery_path`
   - `design_system_trigger`
   - `validate_event_coverage` (merged from the two validation tools)

**Phase 4 — Agent (1 file)**
4. Create `agents/event_stormer.py` — following the exact pattern from decomposer.py/allocator.py. Measurer+Assessor class, bridge orientation.

**Phase 5 — Orchestrator (1 file)**
5. Add to cawdp_orchestrator.py:
   - Import `event_stormer`
   - Add `run_event_storming` tool (delegates to event stormer)
   - Add `review_event_storming` tool (presents results for human gate)
   - Update instructions to mention P5 flow

**Phase 6 — Config (1 file)**
6. Add quick prompts for event storming to config.yaml

**Verification**
7. Run `docker compose up --build` and test the full P0→P5 pipeline
8. Run validate.sh for lint/type checks

---

### Files to Modify

| File | Change |
|---|---|
| schema.py | Add 4 new `design_*` tables (~80 lines) |
| writer.py | Add 5 writer functions + constants (~200 lines) |
| `agents/tools/event_storming_tools.py` | **New** — tool factory (~120 lines) |
| `agents/event_stormer.py` | **New** — agent definition (~80 lines) |
| cawdp_orchestrator.py | Add 2 delegation tools + import + instruction update (~40 lines) |
| config.yaml | Add quick prompts (~5 lines) |

---

### Scope Boundaries

**In scope**: The four event storming tables, writer functions, tool factory, agent, orchestrator integration, data flow validation against Phase 2 backcasting.

**Deliberately excluded**: 
- Runtime event capture (the existing `runtime_events` table handles this separately)
- Phase 6 System Architecture integration (that's a separate phase)
- UI for reviewing event storming results (the orchestrator's `review_event_storming` tool handles this via agent output)

---

### Key Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Schema for triggers | `SCHEMALESS` | Action parameters are inherently heterogeneous |
| `characteristic_failure` | Auto-populated by writer | Deterministic from agent_class; agent shouldn't supply it |
| `payload`/`downstream_effects` | `TYPE array` not `string` | Need `INCLUDES` operator for validation queries |
| Validation vs cross-reference | Single `validate_event_coverage` tool | Two tools would confuse the agent; one tool returns both gap report and matrix |
| Agent class | Measurer+Assessor, bridge orientation | Adversarial analysis maps to measure+assess; bridge connects P2→P5→P6 |
***

### Response

Clean plan. The feasibility assessment is accurate — this does map onto existing patterns. My notes focus on six gaps and two refinements.

## Gaps

### 1. Recovery path ordering is missing

A failure event can have multiple recovery paths: try retry first, then escalate if retry fails, then halt if escalation fails. The schema has no ordering field.

```sql
DEFINE FIELD execution_order ON design_recovery_paths TYPE number;
  -- 1 = try first, 2 = try second, etc.
```

Without this, recovery paths are an unordered set, not a sequence. The agent can write "retry, then escalate, then halt" but the database can't enforce the order. The Event Stormer needs to assign priority, and the writer should validate that orders are sequential within a failure event.

### 2. Cascading failure linkage is missing

The failure types include `cascading_failure`, but there's no structural way to link one failure to another. If Failure A triggers Failure B, the agent can note it in the description field, but queries can't traverse cascade chains.

```sql
DEFINE FIELD cascaded_from ON design_failure_events TYPE option<record<design_failure_events>>;
  -- NULL for root failures, record reference for cascaded failures
```

This enables cascade chain queries: "show me all failures that cascade from this root failure" — critical for understanding blast radius. The writer should validate that `cascaded_from` references an existing failure event and prevent circular references.

### 3. Event-to-artefact linkage is missing

The data flow validation checks that every Phase 2 output has a producing event and every Phase 2 input has a satisfying event. But domain events are only linked to tasks, not to the specific artefacts they produce or requirements they satisfy. The validation can check *task-level coverage* (every task has events) but not *artefact-level coverage* (every artefact is produced by an event).

Add two array fields to domain events:

```sql
DEFINE FIELD satisfies_requirements ON design_domain_events TYPE array;
  -- array of ir_id strings from design_input_requirements
DEFINE FIELD produces_artefacts ON design_domain_events TYPE array;
  -- array of artefact IDs from design_artefacts
```

This uses string IDs (not record references) to match the existing `ir_id` pattern in `design_input_requirements`. The validation query then checks:

```python
# For each input requirement, is there a domain event that satisfies it?
for req in input_requirements:
    satisfying = await client.query(
        "SELECT count() FROM design_domain_events "
        "WHERE workflow = $wf AND satisfies_requirements INCLUDES $ir_id",
        {"wf": workflow_id, "ir_id": req['ir_id']}
    )
    if satisfying[0]['count'] == 0:
        gaps['missing_satisfying_events'].append(req)

# For each output artefact, is there a domain event that produces it?
for artefact in output_artefacts:
    producing = await client.query(
        "SELECT count() FROM design_domain_events "
        "WHERE workflow = $wf AND produces_artefacts INCLUDES $artefact_id",
        {"wf": workflow_id, "artefact_id": artefact['id']}
    )
    if producing[0]['count'] == 0:
        gaps['missing_producing_events'].append(artefact)
```

### 4. Eval cases are missing from the plan

The decomposition-allocation plan includes eval cases for the five problematic tasks. Event storming needs eval cases too, and they should test the specific value this phase adds:

```python
EVENT_STORMING_EVAL = [
    # 1. Coverage: every task has domain events
    {
        "name": "every task has domain events",
        "check": "SELECT count() FROM design_tasks WHERE workflow = $wf "
                 "AND id NOT IN (SELECT task FROM design_domain_events)",
        "expected": 0,  # no tasks without events
    },
    # 2. Completeness: every task has failure events
    {
        "name": "every task has failure events",
        "check": "SELECT count() FROM design_tasks WHERE workflow = $wf "
                 "AND id NOT IN (SELECT task FROM design_failure_events)",
        "expected": 0,
    },
    # 3. Characteristic failure mapping: failures map to correct agent class
    {
        "name": "Extractor failures have judgment creep characteristic",
        "test_failure": {
            "agent_class": "extractor",
            "failure_type": "boundary_violation",
            "expected_characteristic": "judgment creep — starts interpreting, not just extracting",
        },
    },
    # 4. Recovery coverage: every high/critical failure has a recovery path
    {
        "name": "every high/critical failure has a recovery path",
        "check": "SELECT count() FROM design_failure_events "
                 "WHERE workflow = $wf AND severity IN ['high', 'critical'] "
                 "AND id NOT IN (SELECT failure_event FROM design_recovery_paths)",
        "expected": 0,
    },
    # 5. System triggers for critical failures: every critical failure has a system trigger
    {
        "name": "every critical failure has a system trigger",
        "check": "SELECT count() FROM design_failure_events "
                 "WHERE workflow = $wf AND severity = 'critical' "
                 "AND id NOT IN (SELECT failure_event FROM design_system_triggers)",
        "expected": 0,
    },
    # 6. Data flow: every Phase 2 input requirement is satisfied by an event
    {
        "name": "every input requirement has a satisfying event",
        "check": "select ir_id from design_input_requirements "
                 "where workflow = $wf and ir_id not in "
                 "(select satisfies_requirements[*] from design_domain_events "
                 "where workflow = $wf)",
        "expected": [],  # no unsatisfied requirements
    },
]
```

### 5. `design_phase` field on all four tables

Your recommendation to add a workflow state field is right. Add to all four event tables:

```sql
DEFINE FIELD design_phase ON design_domain_events TYPE string
  ASSERT $value IN ['draft', 'reviewed', 'locked'];
DEFINE FIELD design_phase ON design_failure_events TYPE string
  ASSERT $value IN ['draft', 'reviewed', 'locked'];
DEFINE FIELD design_phase ON design_recovery_paths TYPE string
  ASSERT $value IN ['draft', 'reviewed', 'locked'];
DEFINE FIELD design_phase ON design_system_triggers TYPE string
  ASSERT $value IN ['draft', 'reviewed', 'locked'];
```

This matches the pattern on `design_tasks` and enables the human gate to mark events as reviewed or locked.

### 6. The agent should process per-workflow, not per-task

The tool signatures take `task_id` as a parameter for domain events and failure events. This is correct for granularity — events are per-task. But the orchestrator delegates once, not per-task. The Event Stormer should iterate over all tasks internally.

The agent instructions should say: "For every task in the workflow, identify domain events and failure events. Process all tasks before moving to recovery paths and system triggers."

The `identify_domain_events` and `identify_failure_events` tools accept a single `task_id`, so the agent calls them multiple times. This is fine — the agent iterates, the orchestrator delegates once.

## Refinements

### 7. Clarify what `validate_event_coverage` checks structurally vs semantically

The merged tool should be explicit about two levels:

| Check | Type | What It Does |
|-------|------|-------------|
| Every task has ≥1 domain event | Structural | Query: task count vs event count per task |
| Every task has ≥1 failure event | Structural | Query: task count vs failure count per task |
| Every high/critical failure has recovery | Structural | Query: severity filter + recovery join |
| Every critical failure has system trigger | Structural | Query: severity filter + trigger join |
| Every Phase 2 output has producing event | Structural + Semantic | Query: artefact IDs in `produces_artefacts` arrays |
| Every Phase 2 input has satisfying event | Structural + Semantic | Query: ir_id strings in `satisfies_requirements` arrays |
| Cascade chain integrity | Structural | Query: `cascaded_from` references exist and aren't circular |

The structural checks are automatic. The semantic checks (produces_artefacts, satisfies_requirements) require the agent to have correctly linked events to Phase 2 artefacts — the tool can flag gaps but the agent must fix them.

### 8. The `characteristic_failure` auto-population should also set `design_phase`

The writer function already auto-populates `characteristic_failure` from `agent_class`. It should also set `design_phase = 'draft'` on all new records. This gives the human gate a clear workflow: draft (agent creates) → reviewed (human reviews) → locked (human approves).

## Summary

| Item | Type | Action |
|------|------|--------|
| Recovery path ordering | Schema gap | Add `execution_order` field |
| Cascading failure linkage | Schema gap | Add `cascaded_from` field |
| Event-to-artefact linkage | Schema gap | Add `satisfies_requirements` and `produces_artefacts` arrays |
| Eval cases | Plan gap | Add 6 eval cases |
| `design_phase` field | Your rec, confirmed | Add to all 4 tables |
| Per-workflow processing | Clarification | Agent iterates internally, orchestrator delegates once |
| Structural vs semantic validation | Clarification | Two levels in `validate_event_coverage` |
| Auto-set `design_phase` | Refinement | Writer sets `design_phase = 'draft'` on all new records |

The plan is ready to implement with these additions. The three schema gaps (ordering, cascading, artefact linkage) are the most important — they determine whether the data model can actually represent what Event Storming produces.

---
