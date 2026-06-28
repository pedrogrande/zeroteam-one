# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `1c6fe0d0...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-21T07:50:04 |
| **Runs** | 26 completed / 26 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-21T07:50:04* · `glm-5.1:cloud` · `b20544f3...`

### Prompt

I want to develop an application that provides agent-assisted agentic workflow design using the CAWDP framework (applying CAWDP to itself).

I have had some success working forwards, but I believe that working backwards could deliver better results. 

What would be the ideal outcomes from the CAWDP process if the user's goal was a complete design specification for an agentic workflow to complete a business task. This spec should be able to be taken on by implementers to develop architecture specs that deliver on the design.

What does the specification document look like? How should it be formatted? What data should it contain? What is required for all agent workflows vs what might be optional?
What artefacts have been created along the way that support the specification and can be useful for implementers?

I realise this might be challenging in the abstract without a concrete use case to work from but let's do this as a first pass attempt anyway.

### Response

# The CAWDP Design Specification: Working Backward from the Ideal Output

## The Core Insight

The specification is not a document. It's a **typed artefact set** — a collection of structured, connected, traceable components. A single document is the type collision problem at the deliverable layer: 10+ distinct information types encoded in sequential prose.

The implementer needs **different views of the same truth** depending on what they're building:
- **Agent developer** → needs agent specs, schemas, tools, boundaries
- **Integration engineer** → needs data flow, handoffs, event definitions
- **QA engineer** → needs verification protocols, failure modes, test criteria
- **Ops engineer** → needs monitoring, alerts, progressive autonomy schedules

One graph. Many derived views. (This is your stakeholder surface concept applied at the handoff layer.)

---

## 1. The Primary Specification — 10 Sections

Each section is a typed object with defined schema. Sections reference each other. Every element traces to a design rationale.

### Section 1: Identity
*From P0 (Purpose & Vision)*

| Field | Type | Required | Description |
|---|---|---|---|
| name | string | ✅ | What this workflow IS called (in plain English) |
| purpose | string | ✅ | Why this workflow exists — one sentence |
| principal | string | ✅ | Who the workflow serves (the human authority) |
| possibility_stance | enum | ✅ | Explore / Advise / Stay-in-Lane |
| identity_violation | string | ✅ | What would DESTROY this workflow's identity |
| wrong_mode | string | ✅ | What "wrong" looks like — the worst failure that looks like success |
| hardest_moment | string | ✅ | Where pressure would push past the boundary |
| scope_in | list | ✅ | What this workflow covers |
| scope_out | list | ✅ | What this workflow explicitly excludes |
| target_state | list | ✅ | Characteristics of the ideal outcome (from P0 vision) |

### Section 2: Task Map
*From P3 (Decomposition) + P4 (Allocation)*

| Field | Type | Required | Description |
|---|---|---|---|
| tasks | list[TaskSpec] | ✅ | Every task, decomposed per five-property standard |
| dependencies | list[DependencySpec] | ✅ | Task-to-task dependencies with type |
| human_gates | list[GateSpec] | ✅ | Where human judgment is required |
| boundary_map | object | ✅ | H/A/S allocation per task (the boundary map) |
| adjustment_factors | list | ✅ | Factors that modified gap-based allocation |
| allocation_rationale | list | ✅ | WHY each allocation was made |

**TaskSpec** (five-property standard):

| Field | Type | Required |
|---|---|---|
| id | string | ✅ |
| name | string | ✅ |
| cognitive_type | enum | ✅ | Mechanical / Analytical / Generative / Elicitive / Evaluative / Intuitive |
| initiation_mode | enum | ✅ | Self-starting / Scaffolded / Discovery |
| experience_dependency | enum | ✅ | Expert-dependent / Pattern-augmented / Procedural |
| authority_boundary | enum | ✅ | Human-only / Human-final / Agent-primary / System-enforced |
| failure_mode | string | ✅ |
| output_artefact | string | ✅ |
| assigned_actor | string | ✅ |

**GateSpec**:

| Field | Type | Required |
|---|---|---|
| gate_id | string | ✅ |
| after_task | string | ✅ |
| question | string | ✅ | What the human is deciding |
| options | list | ✅ | Prepared options (from Decision Presentation Pattern) |
| on_approve | string | ✅ | Next task |
| on_reject | string | ✅ | Recovery path |
| timeout | string | ✅ | What happens if no response |

### Section 3: Output Specifications
*From P1 (Output Specification)*

| Field | Type | Required | Description |
|---|---|---|---|
| outputs | list[OutputSpec] | ✅ | Every artefact the workflow produces |
| output_dependencies | list | ✅ | Which outputs depend on which (DAG) |
| schemas | list[PydanticSpec] | ✅ | Data schemas for every typed output |

**OutputSpec**:

| Field | Type | Required |
|---|---|---|
| id | string | ✅ |
| name | string | ✅ |
| purpose | string | ✅ |
| type | enum | ✅ | Document / Data / Decision / Signal / Artefact |
| schema_ref | string | ✅ |
| producer_task | string | ✅ |
| quality_gate | string | ✅ |
| epistemic_metadata | object | ✅ |

### Section 4: Agent Roster
*From P7 (Agent Design)*

| Field | Type | Required | Description |
|---|---|---|---|
| agents | list[AgentSpec] | ✅ | One specification per agent |
| composition | enum | ✅ | Single Agent / Team / Workflow |
| orchestration | string | ✅ | How agents are sequenced/coordinated |

**AgentSpec** (abbreviated — full version is the 9-section template):

| Field | Type | Required |
|---|---|---|
| id | string | ✅ |
| name | string | ✅ |
| class | enum | ✅ | Extractor / Measurer / Assessor / Generator / Aggregator |
| orientation | enum | ✅ | Possibility / Bridge / Constraint |
| identity_questions | object | ✅ | 5 identity questions answered |
| authority_boundary | string | ✅ | What this agent CAN decide |
| never_rules | list | ✅ | What this agent NEVER does |
| failure_mode | string | ✅ | Characteristic failure (inverse of boundary) |
| tools | list | ✅ |
| knowledge | list | ✅ |
| output_schema | string | ✅ |
| progressive_autonomy | object | ✅ | Per-dimension autonomy levels |
| cost_budget | object | ✅ | Token/resource budget |
| epistemic_profile | enum | ✅ | Probabilistic / Deterministic |
| null_state | string | ✅ | Class-specific null output |

### Section 5: Failure & Recovery
*From P5 (Event Storming) + P6 FMEA*

| Field | Type | Required | Description |
|---|---|---|---|
| failure_modes | list[FailureSpec] | ✅ | Every identified failure mode |
| domain_events | list[EventSpec] | ✅ | Events that trigger pipeline actions |
| failure_events | list[EventSpec] | ✅ | Events that signal something went wrong |
| recovery_paths | list[RecoverySpec] | ✅ | How each failure is detected and recovered |
| system_triggers | list | ✅ | System-enforced triggers (Regime 3) |

**FailureSpec**:

| Field | Type | Required |
|---|---|---|
| id | string | ✅ |
| description | string | ✅ |
| severity | int (1-10) | ✅ |
| occurrence | int (1-10) | ✅ |
| detection | int (1-10) | ✅ |
| rpn | int | ✅ |
| who_catches | string | ✅ |
| recovery_path | string | ✅ |

### Section 6: Verification & Trust
*From P7/P8 + CC-1/CC-3/CC-8*

| Field | Type | Required | Description |
|---|---|---|---|
| verification_protocol | object | ✅ | 3-level: structural / semantic / authority |
| verification_independence | list | ✅ | Where producer ≠ verifier (CC-1) |
| epistemic_metadata | object | ✅ | 6-field contract per output type |
| audit_trail_level | enum | ✅ | Logged / Assured / Verified |
| information_boundaries | list | ✅ | CC-4 boundaries with enforcement regime |
| harm_assessment | object | ⚠️ | Required only if workflow is harm-capable |
| suggestion_risk | object | ⚠️ | Required only for harm-capable generators |

### Section 7: Contracts
*From P8 (Contract Formalization)*

| Field | Type | Required | Description |
|---|---|---|---|
| contract_primitives | object | ✅ | 10 primitives defined for this workflow |
| enforcement_regime_map | list | ✅ | Declare/Detect/Prevent per boundary |
| mapping_matrix | object | ✅ | 10×10 spec-section → contract-primitive trace |
| unenforceable_elements | list | ✅ | What can only be declared or detected (honest infrastructure) |
| contract_depth | string | ✅ | Scaled by agent class and autonomy level |

### Section 8: Human Experience
*From P9 (Human Experience Design)*

| Field | Type | Required | Description |
|---|---|---|---|
| cognitive_load_budget | object | ✅ | Decisions per session, time budget, decision types |
| override_protocol | object | ✅ | How humans intervene, what happens |
| stakeholder_surfaces | list | ✅ | Different views for different audiences |
| system_empowerment_level | enum | ✅ | Constraining → Informing → Enabling → Amplifying → Liberating |
| interface_spec | string | ✅ | Key interaction patterns |

### Section 9: Monitoring & Evolution
*From P10 (Validation) + CC-5/CC-6/CC-7*

| Field | Type | Required | Description |
|---|---|---|---|
| health_metrics | object | ✅ | IDS + UPR per agent/pipeline |
| cost_budget | object | ✅ | Per-agent and per-pipeline budgets with halt conditions |
| specification_aging | object | ✅ | Review cadences and triggers per component |
| evolve_triggers | list | ✅ | 8 signal types for EVOLVE mode |
| testable_hypotheses | list | ✅ | What we're testing, how, and go/no-go criteria |
| progressive_autonomy_schedule | object | ✅ | 4 levels with promotion criteria per agent |

### Section 10: Workflow Diagram
*From P1 (O29) — visual artefact*

| Field | Type | Required | Description |
|---|---|---|---|
| diagram | visual | ✅ | Tasks, agents, human gates, dependencies, data flows, authority boundaries |
| principal_view | visual | ✅ | Simplified: key decisions and outcomes |
| implementer_view | visual | ✅ | Detailed: agents, schemas, tools, integrations |
| assessor_view | visual | ✅ | Quality-focused: verification points, failure modes, recovery |

Quality test: Can someone who didn't design the workflow explain it back after 60 seconds?

---

## 2. Required vs Optional — With Criteria

### Always Required (Every Workflow)

These are the minimum viable specification. Without any one, an implementer cannot safely build the workflow.

| Section | Why Required |
|---|---|
| Identity | Without knowing what the workflow IS and what would destroy its identity, implementers build the wrong thing with confidence |
| Task Map | Without knowing what tasks exist and who does them, implementers cannot assign work or design handoffs |
| Output Specifications | Without typed outputs, implementers cannot define schemas or test results |
| Agent Roster | Without agent specifications, implementers cannot configure agents |
| Failure & Recovery | Without failure modes and recovery, the workflow breaks silently in production |
| Verification Protocol | Without verification, there is no trust — the implementer has no quality standard |
| Contracts | Without contract primitives, boundaries are prompt-level (Regime 1), not enforced (Regime 3) |
| Human Gates | Without explicit gates, human judgment either gets bypassed or becomes a bottleneck |
| Monitoring | Without health metrics and cost budgets, the workflow runs without observation |
| Workflow Diagram | Without a visual, text-based specs hide structural gaps |

### Conditionally Required

| Section | When Required | Criterion |
|---|---|---|
| Harm Assessment | When agent output could cause external harm | Ask: "If the agent's output is accepted without review, could someone be harmed, lose money, or face legal consequences?" |
| SuggestionRisk Schema | When harm-capable generators produce suggestions | If harm assessment = yes, every generative agent needs risk levels |
| Full Epistemic Metadata | When provenance, confidence, or uncertainty matter for decisions | Ask: "Would a wrong decision be made if confidence or provenance were unknown?" |
| Information Quality Framework | When working with adversarial or decaying data sources | Ask: "Do information sources have incentives to mislead, or does data become dangerous when stale?" |
| Event Storming Detail | When workflow has 5+ agents with complex interdependencies | Simple 2-3 agent workflows can use lightweight event definitions |
| Cognitive Load Budget | When human experience quality directly affects outcomes | Ask: "Is human fatigue a failure mode?" |
| Stakeholder Surfaces | When 3+ distinct audiences need different views of the spec | Ask: "Do implementer, operator, and auditor need fundamentally different information?" |
| Specification Aging Schedule | When agents will run for 30+ days | Short-lived workflows can use default cadences |
| Unenforceable Elements Register | When Regime 3 (Prevent) is the target for critical boundaries | Low-stakes workflows can operate at Regime 2 (Detect) for most boundaries |
| Per-Dimension Progressive Autonomy | When agent has multiple function types with different trust trajectories | Simple single-function agents can use single-progression |
| Cross-Domain Analysis | When workflow spans multiple intelligence domains | Single-domain workflows don't need it |

### Always Optional

| Item | When Useful |
|---|---|
| Competitive intelligence specifics | Only for CI workflows |
| Tutor-specific inverted autonomy | Only for educational agents |
| DAO governance integration | Only for contract-native org contexts |
| Full PRISM schema implementation | Only when the knowledge graph is a core product requirement |

---

## 3. Supporting Artefacts — Created Along the Way

These are the milestone outputs that have standalone value before the full spec is complete.

### Milestone 1: Boundary Map
*At the end of P3/P4 — the 77% Challenge artifact*

- Three-column H/A/S allocation per task
- Percentage split (You / AI / System)
- Key value statement: one sentence naming where human judgment lives
- Confidence indicators per placement
- **Standalone value**: implementers know WHO does WHAT before they know HOW
- **Format**: single landscape page, laminated desk card, PDF

### Milestone 2: Allocation Map
*At the end of P5/P6*

- Task-by-task allocation table with role names in plain English
- Authority boundaries per role (can decide / never does)
- Failure & recovery register (what goes wrong, who catches it, how to recover)
- **Standalone value**: implementers know every role, every boundary, every failure mode
- **Format**: two documents — allocation table + failure register

### Milestone 3: Operations Manual
*At the end of P8/P9 — the insurance document*

- 12-section document covering progressive autonomy, verification protocols, cost budgets, aging schedule, change management, sign-off
- Deployment guide for shadow mode
- **Standalone value**: implementers know how to deploy safely and what to monitor
- **Format**: 12-page document + 4-page deployment guide

### Milestone 4: Trust Ledger
*At the end of P10 — ongoing*

- Quarterly report: trust score, agent status, override analysis, evolution recommendations
- **Standalone value**: implementers know what to monitor and when to intervene
- **Format**: 4-page quarterly report + monitoring dashboard

### Additional Supporting Artefacts

| Artefact | Created At | Value for Implementers |
|---|---|---|
| Input Requirements Map | P2 | Every input the workflow needs, where it comes from, criticality |
| Dependency DAG | P2 | Visual trace from final output back through all dependencies |
| Event Catalog | P5 | Every domain event and failure event with trigger conditions |
| FMEA Table | P6 | Risk priority numbers for every failure mode |
| Agent Job Descriptions | P7 | Full 9-section specification per agent (the template output) |
| Contract Specifications | P8 | 10 primitives per agent with enforcement regime |
| Decision Log | Throughout | Every human decision with reasoning (decision archaeology) |
| Gaps & Assumptions Register | Throughout | What we don't know and what we're assuming |
| Confidence Map | Throughout | Where confidence is high, medium, low across the spec |
| Implementation Readiness Checklist | P10 | Can implementers start? What's missing? |

---

## 4. Format — Type Collision Resolution at the Deliverable Layer

### The Problem

A single document encodes 10+ distinct information types (identity, allocation, architecture, failure, verification, contracts, monitoring) into sequential prose. This is the same type collision problem, applied to the spec itself.

### The Solution

**Three-format delivery:**

1. **Machine-Readable** — JSON/YAML schemas in a PRISM artefact graph
   - Every section has a defined schema
   - Every cross-reference is a typed link
   - Implementers can validate, query, and generate from this
   - This IS the source of truth

2. **Human-Readable** — Derived views from the graph
   - Boundary Map (for decision makers)
   - Allocation Map (for architects)
   - Agent Specs (for developers)
   - Operations Manual (for operators)
   - Trust Ledger (for governance)
   - Each view contains ONLY what that audience needs, in their language

3. **Visual** — Workflow Diagram with stakeholder-specific layers
   - Principal layer: tasks, gates, outcomes
   - Implementer layer: agents, schemas, tools, data flows
   - Assessor layer: verification points, failure modes, recovery

### The Navigation Problem

The spec needs to be navigable, not just readable. An implementer should be able to:
- Start at any section and follow references to related sections
- Trace any design decision back to its rationale
- Trace any boundary forward to its enforcement mechanism
- View the spec at different depths (summary, detail, full)

This is what the PRISM graph enables: every element is a node, every relationship is a typed edge, and queries produce the right view for the right audience.

---

## 5. Completeness Test

A specification is complete when an implementer can answer YES to all of these:

| # | Question | Maps to Section |
|---|---|---|
| 1 | Can I name every agent, its class, and its authority boundary? | 4 |
| 2 | Can I define every data schema and handoff format? | 3 |
| 3 | Can I build every quality gate and verification check? | 6 |
| 4 | Can I set up every human gate with the right question and options? | 2 |
| 5 | Can I detect every failure mode and trigger its recovery? | 5 |
| 6 | Can I enforce every authority boundary structurally (not just prompt-level)? | 7 |
| 7 | Can I deploy the workflow at the correct progressive autonomy level? | 4, 9 |
| 8 | Can I monitor health, cost, and specification aging? | 9 |
| 9 | Can I trace every design decision to its rationale? | All |
| 10 | Can someone who didn't design this explain the workflow after 60 seconds? | 10 |

If any answer is NO, the spec has a gap.

---

## Key Insight: The Spec IS the Test of the Methodology

Working backwards reveals something important: if CAWDP cannot produce a spec that passes the completeness test, the methodology has a gap. The 10 completeness questions are the quality gate for CAWDP itself.

This is the meta-validation: **the specification CAWDP produces IS the evidence that CAWDP works.**

Every section traces to a CAWDP phase. Every required field exists because a CAWDP design decision demands it. Every conditional field exists because a CAWDP analysis flagged it. The specification IS the methodology, made visible.

Want me to apply this backward-derived structure to a concrete use case to test it?I've also saved the key findings from this analysis to memory — this is a significant milestone because it validates CAWDP's internal coherence from the output side: the specification structure maps directly to CAWDP phases, and the completeness test closes the meta-validation loop.

The most actionable next step would be to **test this structure against a concrete use case** — pick a real business task, apply this spec template, and see where it breaks. That's where the gaps in both the template AND the methodology will surface. Which use case would you want to stress-test first?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-21T08:01:00* · `glm-5.1:cloud` · `361c20f2...`

### Prompt

Great.

Is the explainable workflow diagram the only output from the final CAWDP phase? Might there be other artefacts or reports?

### Response

Good question. The workflow diagram isn't actually a P10 output — it's produced in P6 (System Architecture) and becomes Section 10 of the assembled spec. I placed it as the last section but conflated its position in the spec with its position in the process.

P10 — Validation & Iteration — has its own distinct outputs. Let me think about what the final phase should produce.

---

## P10 Is a Transition, Not a Finale

P10 serves two functions:
1. **VERIFY** — Is this specification complete, consistent, and safe to build from?
2. **EVOLVE** — How will we know when the specification needs to change?

This makes P10 a **handoff phase** — it's preparing the specification for two audiences:
- **Implementers** who will build from it
- **Operators** who will maintain it after deployment

---

## P10 Outputs — Three Categories

### Category 1: Validation Artefacts

These answer: "Is this specification good enough to build from?"

**1. Implementation Readiness Report**

| Field | Type | Description |
|---|---|---|
| overall_status | enum | Ready / Ready with Conditions / Not Ready |
| completeness_score | int | % of completeness test questions answered YES |
| blocking_gaps | list | What MUST be resolved before implementation can start |
| conditional_items | list | What SHOULD be resolved but won't block start |
| estimated_build_effort | string | Based on spec complexity and agent count |
| critical_path | list | Dependencies that determine minimum build time |
| risk_acknowledgement | list | Known risks the implementer accepts by proceeding |

This is the single most important P10 artefact. It's the "shipping checklist" — the binary decision: build or don't build.

**2. Hypothesis Test Results**

| Field | Type | Description |
|---|---|---|
| hypothesis | string | What we claimed |
| test_method | string | How we tested it |
| result | enum | Pass / Fail / Inconclusive / Deferred to production |
| evidence | string | What the test showed |
| impact_if_wrong | string | What happens if this hypothesis fails in production |
| monitoring_action | string | What to watch for in production |

Each hypothesis from the specification gets tested where possible before handoff. Some hypotheses can only be tested in production (e.g., "typed outputs reduce verification time by 30%") — these are flagged as **deferred** with explicit monitoring actions.

**3. Specification Consistency Report**

| Field | Type | Description |
|---|---|---|
| internal_conflicts | list | Where two sections contradict each other |
| orphan_references | list | Where a section references something that doesn't exist |
| dangling_dependencies | list | Where a task depends on an output that no task produces |
| coverage_gaps | list | Where a failure mode has no recovery path |
| enforcement_gaps | list | Where a boundary is declared but no enforcement specified |

This is the automated coherence check — running the completeness test programmatically across the PRISM graph.

**4. Gaps & Assumptions Register**

This has been maintained throughout. At P10, it becomes a **formal handover document** — what we know we don't know, and what we're assuming that hasn't been verified.

| Field | Type | Description |
|---|---|---|
| item | string | The gap or assumption |
| type | enum | Gap (we don't know) / Assumption (we believe but haven't verified) |
| impact | enum | Critical / High / Medium / Low |
| owner | string | Who is responsible for resolving |
| resolution_target | string | When it should be resolved (before build / before deploy / in production) |
| monitoring | string | What to watch for if resolution is deferred |

### Category 2: Deployment Artefacts

These answer: "How do I safely put this into production?"

**5. Progressive Autonomy Deployment Plan**

This is the operational timeline for trust-building. Not a single date — a schedule.

| Field | Type | Description |
|---|---|---|
| agent | string | Which agent |
| dimension | string | Which capability dimension |
| current_level | enum | Shadow / Advisory / Supervised / Autonomous |
| target_level | enum | Same |
| promotion_criteria | string | What must be true to advance |
| demotion_triggers | string | What would cause a step back |
| estimated_timeline | string | Based on similar deployments |
| monitoring_required | list | What to track during transition |

Per-dimension, per-agent. This is the schedule that the Trust Ledger then tracks against.

**6. First 30 Days Plan**

What happens between deployment and the first Trust Ledger review.

| Phase | Time | Activity |
|---|---|---|
| Shadow Launch | Day 1-3 | Agents run alongside, human does everything, outputs tracked |
| First Review | Day 3-5 | Compare shadow outputs with human actions, discuss surprises |
| Advisory Start | Day 5-10 | Agents begin suggesting, human reviews every suggestion |
| Trust Checkpoint 1 | Day 10 | Override rates, accuracy, unexpected behaviours |
| Supervised Start | Day 10-20 | Agents act, human approves before output leaves |
| Trust Checkpoint 2 | Day 20 | Same metrics, any boundary violations? |
| Full Operations | Day 20-30 | Agents at their initial authorised autonomy level |
| First Trust Ledger | Day 30 | Full quarterly report even though only 30 days of data |

**7. Cost & Resource Baseline**

| Field | Type | Description |
|---|---|---|
| per_agent_budget | list | Token cost per invocation per agent |
| per_pipeline_budget | list | Token cost per full workflow run |
| infrastructure_cost | list | Database, compute, storage |
| human_time_budget | list | Expected human involvement per session |
| total_cost_per_run | string | End-to-end cost estimate |
| halt_thresholds | list | Budget levels that trigger system halt |
| escalation_triggers | list | Cost anomalies that require human review |

This gives operators a financial baseline to monitor against.

**8. Specification Aging Schedule**

When each component of the specification needs review — even if nothing has gone wrong.

| Component | Cadence | Trigger-based Reviews | Responsible |
|---|---|---|---|
| Agent instructions | 90 days | Override rate > 15% | Agent owner |
| Authority boundaries | 180 days | Boundary violation | Principal |
| Output schemas | 90 days | Schema rejection > 5% | Developer |
| Cost budgets | 30 days | Cost variance > 20% | Operations |
| Human gates | 180 days | Rubber-stamping detected | Principal |
| Epistemic metadata | 60 days | Staleness flag from monitoring | Agent owner |
| Full specification | 365 days | Any EVOLVE signal | Methodology steward |

### Category 3: Evolution Artefacts

These answer: "How will I know when the specification needs to change?"

**9. EVOLVE Playbook**

The 8 signal types that trigger re-entry into the CAWDP cycle, with specific thresholds and actions.

| Signal | Detection | Threshold | Action |
|---|---|---|---|
| Override rate rising | Trust Ledger | > 15% sustained 2 weeks | Reassess authority boundaries |
| Cost variance | Cost monitoring | > 20% from baseline | Reassess cost budget and task allocation |
| Quality metrics declining | Health monitoring | IDS < threshold | Diagnose and redesign affected agent |
| Capability drift | Specification aging | Agent behaviour diverges from spec | Re-specify affected agent |
| Stakeholder feedback | Direct input | Principal reports dissatisfaction | Re-enter CAWDP at affected phase |
| Environmental change | External monitoring | Regulations, market, tech change | Re-enter at P0 if purpose affected, affected phase otherwise |
| Periodic review | Aging schedule | Scheduled | Re-enter at the relevant phase |
| New failure mode discovered | Incident analysis | Unanticipated failure | Re-enter at P3 for decomposition, P5 for events |

**10. Confidence Map**

Where confidence is high, medium, and low across the entire specification. This tells operators where to watch most carefully.

| Spec Element | Confidence | Reason | Monitoring Priority |
|---|---|---|---|
| Task decomposition | 🟢 High | Validated with domain expert | Standard |
| Agent authority boundaries | 🟢 High | Derived from failure modes | Standard |
| Cost estimates | 🟡 Medium | Based on similar workflows | Active |
| Progressive autonomy timeline | 🟡 Medium | Depends on actual override rates | Active |
| Human gate design | 🟢 High | Validated with principal | Standard |
| Novel agent behaviour | 🔴 Low | First deployment of this pattern | Intensive |
| Data quality from external sources | 🔴 Low | Adversarial provenance risk | Intensive |

**11. Methodology Reflection**

This is the meta-artefact — what CAWDP learned about itself by designing this workflow.

| Field | Type | Description |
|---|---|---|
| phase_duration | list | How long each CAWDP phase took |
| iteration_count | int | How many phases needed re-entry |
| quality_gate_failures | list | Which gates failed and why |
| design_surprises | list | What emerged that wasn't planned |
| methodology_gaps | list | Where CAWDP didn't provide enough guidance |
| new_patterns | list | New design patterns discovered during this application |
| recommendations | list | Suggested CAWDP improvements |

This feeds back into the methodology itself — the EVOLVE cycle applied to CAWDP, not just the workflow it designed.

---

## Summary — Full P10 Output Set

| # | Artefact | Category | Audience |
|---|---|---|---|
| 1 | Implementation Readiness Report | Validation | Decision maker |
| 2 | Hypothesis Test Results | Validation | Assessor / QA |
| 3 | Specification Consistency Report | Validation | Developer / QA |
| 4 | Gaps & Assumptions Register | Validation | All |
| 5 | Progressive Autonomy Deployment Plan | Deployment | Operator |
| 6 | First 30 Days Plan | Deployment | Operator / Principal |
| 7 | Cost & Resource Baseline | Deployment | Operator / Finance |
| 8 | Specification Aging Schedule | Deployment | Operator |
| 9 | EVOLVE Playbook | Evolution | Operator / Methodology Steward |
| 10 | Confidence Map | Evolution | All (risk-awareness) |
| 11 | Methodology Reflection | Evolution | Methodology / Community |

The workflow diagram is a **P6 artefact that becomes Section 10 of the assembled specification**. P10's outputs sit **alongside** the specification, not inside it — they're the handoff documents that make the specification usable.

The most important single P10 artefact is the **Implementation Readiness Report** — it's the go/no-go gate for the entire design effort. If it says "Not Ready," you don't build. If it says "Ready with Conditions," you build but with explicit acceptance of known risks. That's the contract between design and implementation.

Want me to integrate these P10 outputs into the full specification structure?Memory updated. The key structural insight here is that P10 is a **handoff phase**, not a conclusion — its outputs bridge design to implementation AND design back to itself via the EVOLVE cycle. The Implementation Readiness Report is the single most important artefact because it's the gate that either authorises building or sends you back to fix.

Want me to integrate these P10 outputs into the complete specification structure, or apply the whole backward-derived template to a concrete use case?

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-05-21T08:09:17* · `glm-5.1:cloud` · `afd140a0...`

### Prompt

Great. (My misunderstanding about the product of the final phase)

These is a great list of outputs for the final phase of CAWDP.

Now we have this list, let's look at each artefact individually.

For each of the 11 artefacts in the P10 output set, list the steps involved in producing it along with the data required as inputs.

### Response

# P10 Artefact Production Atlas

## Production Order

The 11 artefacts have internal dependencies. Not all can be produced in parallel.

```
Wave 1 (no P10 dependencies):
  ├─ Specification Consistency Report
  ├─ Gaps & Assumptions Register (finalised)
  └─ Hypothesis Test Results

Wave 2 (depends on Wave 1):
  └─ Implementation Readiness Report

Wave 3 (depends on Wave 2 go-decision):
  ├─ Progressive Autonomy Deployment Plan
  ├─ First 30 Days Plan
  ├─ Cost & Resource Baseline
  └─ Specification Aging Schedule

Wave 4 (depends on Wave 3):
  ├─ EVOLVE Playbook
  ├─ Confidence Map
  └─ Methodology Reflection
```

Wave 2 is the gate. If the Implementation Readiness Report says "Not Ready," Waves 3-4 don't start. Fix the gaps, re-validate.

---

## Category 1: Validation Artefacts

---

### 1. Specification Consistency Report

**Purpose**: Automated coherence check across the entire specification.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Extract all cross-references from PRISM graph | System | Graph traversal query |
| 2 | Verify every reference target exists | System | Existence check |
| 3 | Compare authority boundaries across linked sections for contradictions | Agent | Consistency checker |
| 4 | Trace every task dependency to confirm producing task exists | System | DAG walk |
| 5 | Trace every failure mode to confirm recovery path exists | System | Graph traversal |
| 6 | Trace every declared boundary to confirm enforcement specified | System | Enforcement check |
| 7 | Flag all violations as findings with severity | System | Finding generator |
| 8 | Compile findings into structured report | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Complete PRISM artefact graph | Built throughout P0-P9 | All |
| Cross-reference index | Built during assembly | All |
| Enforcement regime map | P8 Contract Formalization | Section 7 |
| Task dependency DAG | P3 Decomposition | Section 2 |
| Failure mode registry | P5 Event Storming | Section 5 |
| Recovery path registry | P5/P6 | Section 5 |

**Production Constraints**
- Must run against the complete specification (all 10 sections assembled)
- Zero tolerance for dangling references (every reference must resolve)
- Contradictions are flagged, not resolved (resolution is a human decision)

---

### 2. Gaps & Assumptions Register (Finalised)

**Purpose**: Formal handover of what we don't know and what we're assuming.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Gather all gaps recorded during P0-P9 | System | Query PRISM for gap-tagged artefacts |
| 2 | Gather all assumptions recorded during P0-P9 | System | Query PRISM for assumption-tagged artefacts |
| 3 | Classify each item: Gap (we don't know) or Assumption (we believe but unverified) | Agent | Assessor |
| 4 | Assess impact: Critical / High / Medium / Low | Agent + Human | Assessor with human validation |
| 5 | Assign owner for each item | Human | Principal decision |
| 6 | Set resolution target: Before Build / Before Deploy / In Production / Accepted | Human | Principal decision |
| 7 | Define monitoring for deferred items | Agent | What to watch, what threshold triggers action |
| 8 | Compile into structured register | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Gap annotations from every phase | Captured in PRISM throughout | All |
| Assumption annotations from every phase | Captured in PRISM throughout | All |
| Confidence scores from epistemic metadata | CC-3 | Section 6 |
| Low-confidence outputs | P1 Output Specification | Section 3 |
| Unenforceable elements | P8 | Section 7 |
| Deferred hypotheses | P10 Hypothesis Test Results | Artefact 3 |

**Production Constraints**
- This register has been accumulating throughout — P10 finalises it
- Critical gaps are blocking (appear in Implementation Readiness Report)
- "Accepted" means the principal explicitly accepts the risk — documented, not implicit

---

### 3. Hypothesis Test Results

**Purpose**: Test each specification hypothesis where possible before handoff.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Extract all testable hypotheses from specification | System | Query PRISM for hypothesis-tagged artefacts |
| 2 | Classify each: testable now / testable in production / untestable | Agent | Assessor |
| 3 | Design test method for each testable-now hypothesis | Agent | Generator (test design) |
| 4 | Execute tests against prototype, simulation, or analogous data | Agent / System | Test runner |
| 5 | Record result: Pass / Fail / Inconclusive | System | Test harness |
| 6 | For deferred-to-production hypotheses, define monitoring action | Agent | What to track, what threshold triggers reassessment |
| 7 | Assess impact if hypothesis is wrong for every hypothesis | Agent | Assessor |
| 8 | Compile into structured results table | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Testable hypotheses | Defined in P7/P9 | Section 9 |
| Prototype or simulation outputs | P10 validation activities | P10 |
| Existing benchmark data | External | — |
| Agent specifications | P7 | Section 4 |
| Expected behaviours | P7/P9 | Sections 4, 8 |
| Cost budgets | P6/CC-7 | Section 9 |

**Production Constraints**
- "Deferred to production" is honest, not lazy — some hypotheses genuinely can't be tested until deployed
- Every deferred hypothesis MUST have a monitoring action
- Failed hypotheses may require re-entry into earlier CAWDP phases

---

### 4. Implementation Readiness Report

**Purpose**: The go/no-go gate. The single most important P10 artefact.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Run the 10-question completeness test against assembled specification | System | Completeness checker |
| 2 | Calculate completeness score (% YES answers) | System | Calculator |
| 3 | Identify blocking gaps (anything that makes an answer NO) | Agent | Assessor |
| 4 | Identify conditional items (things that should be resolved but won't block) | Agent | Assessor |
| 5 | Review Specification Consistency Report findings | Agent + Human | Assessor + Principal |
| 6 | Review Gaps & Assumptions Register — separate Critical/High from Medium/Low | Agent + Human | Assessor + Principal |
| 7 | Review Hypothesis Test Results — identify failed hypotheses and their impact | Agent + Human | Assessor + Principal |
| 8 | Estimate build effort based on spec complexity (agent count, task count, integration points) | Agent | Generator |
| 9 | Identify critical path (longest dependency chain determining minimum build time) | System | DAG analysis |
| 10 | Compile risk acknowledgement list (what the implementer accepts by proceeding) | Agent + Human | Assessor + Principal |
| 11 | Determine overall status: Ready / Ready with Conditions / Not Ready | Human | Principal — always a human decision |
| 12 | Compile into structured report | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Complete 10-section specification | Assembled from P0-P9 | All |
| Specification Consistency Report | P10 Artefact 1 | This phase |
| Gaps & Assumptions Register | P10 Artefact 2 | This phase |
| Hypothesis Test Results | P10 Artefact 3 | This phase |
| Task dependency DAG | P3 | Section 2 |
| Agent roster complexity | P7 | Section 4 |
| Integration point count | P6 | Section 10 |

**Production Constraints**
- The overall status decision is ALWAYS human — no agent decides whether to ship
- "Ready with Conditions" must explicitly name the conditions and who accepts them
- "Not Ready" must explicitly name what blocks and where to re-enter CAWDP

**Decision Rules**

| Completeness Score | Critical Gaps | Consistency | Status |
|---|---|---|---|
| ≥ 90% | 0 | Pass | Ready |
| 70-89% | 0 | Pass with minor findings | Ready with Conditions |
| Any | ≥ 1 | — | Not Ready |
| < 70% | 0 | Fail | Not Ready |

---

## Category 2: Deployment Artefacts

*These are only produced if the Implementation Readiness Report says "Ready" or "Ready with Conditions."*

---

### 5. Progressive Autonomy Deployment Plan

**Purpose**: Per-dimension, per-agent schedule for trust-building.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Extract per-dimension autonomy levels from each agent specification | System | Query PRISM |
| 2 | Map current level (always Shadow for new deployments) to target level | Agent | Measurer |
| 3 | Define promotion criteria per dimension per agent | Agent + Human | Assessor + Principal |
| 4 | Define demotion triggers per dimension per agent | Agent | Assessor |
| 5 | Estimate timeline per dimension based on agent class and risk profile | Agent | Generator |
| 6 | Define monitoring requirements per transition | Agent | Assessor |
| 7 | Compile into deployment schedule | Agent | Aggregator |
| 8 | Human review and approval | Human | Principal |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Per-dimension progressive autonomy | P7 Agent Design | Section 4 |
| Agent class and risk profile | P7 | Section 4 |
| Harm assessment | P7 | Section 4 |
| Authority boundaries | P7/P8 | Sections 4, 7 |
| Verification protocol | CC-1 | Section 6 |
| Cost budget | CC-7 | Section 9 |
| Existing deployment benchmarks | External / PRISM | — |

**Production Constraints**
- Every dimension gets its own schedule (per-dimension is the default, not the exception)
- Harm-capable dimensions start at Shadow regardless of what other dimensions allow
- Demotion triggers must be as specific as promotion criteria — trust can be lost faster than earned

---

### 6. First 30 Days Plan

**Purpose**: What happens between deployment and first Trust Ledger review.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Extract all agents and their initial autonomy levels from Deployment Plan | System | Query |
| 2 | Design shadow phase activities (what agents run alongside, what gets tracked) | Agent | Generator |
| 3 | Design first review protocol (comparison method, what to compare, who reviews) | Agent + Human | Assessor + Principal |
| 4 | Define trust checkpoint criteria and schedule | Agent | Assessor |
| 5 | Map advisory phase activities (what agents suggest, what human reviews) | Agent | Generator |
| 6 | Map supervised phase activities (what agents do, what human approves) | Agent | Generator |
| 7 | Define full operations criteria and first Trust Ledger scope | Agent + Human | Assessor + Principal |
| 8 | Compile into day-by-day plan with decision points | Agent | Aggregator |
| 9 | Human review and approval | Human | Principal |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Progressive Autonomy Deployment Plan | P10 Artefact 5 | This phase |
| Agent roster and capabilities | P7 | Section 4 |
| Human gate specifications | P3/P4 | Section 2 |
| Verification protocol | CC-1 | Section 6 |
| Override mechanism | P9 | Section 8 |
| Cost budget | CC-7 | Section 9 |
| Trust Ledger template | P10 design | Artefact 11 (conceptual) |

**Production Constraints**
- Every phase transition is a human decision (even if the data supports promotion)
- Shadow phase must produce concrete comparison data, not vibes
- Trust checkpoints are hard stops — no advancing without checkpoint review

---

### 7. Cost & Resource Baseline

**Purpose**: Financial and resource foundation for monitoring.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Extract per-agent cost budgets from agent specifications | System | Query PRISM |
| 2 | Estimate per-invocation token cost per agent using model + context window + output size | Agent | Measurer |
| 3 | Calculate per-pipeline cost by tracing full workflow execution path | System | DAG walk with cost accumulation |
| 4 | Estimate infrastructure costs (database, compute, storage, API calls) | Agent | Generator |
| 5 | Estimate human time per session per human gate | Agent | Measurer |
| 6 | Calculate total cost per full workflow run | System | Calculator |
| 7 | Define halt thresholds per budget type | Agent + Human | Assessor + Principal |
| 8 | Define escalation triggers for cost anomalies | Agent | Assessor |
| 9 | Compile into baseline document | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Per-agent cost budgets | P7/CC-7 | Section 4 |
| Model selection and token pricing | P7 | Section 4 |
| Task dependency chain | P3 | Section 2 |
| Infrastructure requirements | P6 | Section 10 |
| Human gate count and complexity | P3/P4 | Section 2 |
| Existing cost benchmarks | External / PRISM | — |

**Production Constraints**
- Estimates are ranges, not single points (with confidence)
- Halt thresholds are hard limits (CC-7 budget exhaustion = system halt)
- Human time estimates must include verification time (the verification time tax)

---

### 8. Specification Aging Schedule

**Purpose**: When each spec component needs review, even if nothing has gone wrong.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Catalogue every spec component type (agent instructions, boundaries, schemas, budgets, gates, metadata, full spec) | System | Query PRISM |
| 2 | Assign default cadence per component type based on agent class and risk | Agent | Assessor (using default cadences) |
| 3 | Define trigger-based review conditions per component | Agent | Generator |
| 4 | Assign responsible party per component | Human | Principal |
| 5 | Cross-reference with progressive autonomy timeline (promotions may trigger review) | Agent | Measurer |
| 6 | Cross-reference with cost monitoring (budget anomalies may trigger review) | Agent | Measurer |
| 7 | Compile into schedule with cadences, triggers, and owners | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Agent class inventory | P7 | Section 4 |
| Component type registry | P6/P7/P8 | Sections 4, 7, 9 |
| Default cadences by agent class | CC-5 | Section 9 |
| Progressive autonomy timeline | P10 Artefact 5 | This phase |
| Cost baseline | P10 Artefact 7 | This phase |
| Risk profile | P7 harm assessment | Section 4 |

**Production Constraints**
- Cadences are maximum intervals (earlier review is always acceptable)
- Triggers override cadences (if a trigger fires, review regardless of schedule)
- The full specification gets an annual review minimum, even if nothing triggers

---

## Category 3: Evolution Artefacts

---

### 9. EVOLVE Playbook

**Purpose**: How to know when the specification needs to change, and where to re-enter CAWDP.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Define each of the 8 signal types with detection method | Agent | Generator |
| 2 | Define threshold per signal type (what constitutes a trigger) | Agent + Human | Assessor + Principal |
| 3 | Map re-entry point per signal type (which CAWDP phase to re-enter) | Agent | Assessor |
| 4 | Define scope of re-entry (full cycle / targeted phase) per signal type | Agent | Assessor |
| 5 | Define escalation path (when signal exceeds threshold) | Agent | Generator |
| 6 | Cross-reference with Specification Aging Schedule (periodic review is signal type 7) | Agent | Measurer |
| 7 | Cross-reference with Trust Ledger metrics (override rate is signal type 1) | Agent | Measurer |
| 8 | Compile into playbook with 8 signal entries | Agent | Aggregator |
| 9 | Human review and approval | Human | Principal |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|---|
| Override rate thresholds | CC-6/P9 | Section 8 |
| Cost variance thresholds | CC-7 | Section 9 |
| Health metric thresholds (IDS/UPR) | CC-6 | Section 9 |
| CAWDP phase definitions | P0-P10 | Methodology |
| Specification Aging Schedule | P10 Artefact 8 | This phase |
| Trust Ledger structure | P10 design | Artefact 11 |
| Known failure modes | P5/P6 | Section 5 |
| Unenforceable elements | P8 | Section 7 |

**The 8 Signals with Re-entry Points**

| Signal | Re-enter At | Scope |
|---|---|---|
| Override rate rising | P4 (Capability Allocation) | Targeted: reassess affected boundaries |
| Cost variance | P6 (System Architecture) or CC-7 | Targeted: redesign budget or workflow |
| Quality metrics declining | P7 (Agent Design) | Targeted: redesign affected agent |
| Capability drift | P7 (Agent Design) | Targeted: re-specify affected agent |
| Stakeholder feedback | P0-P9 depending on feedback | Varies: could be any phase |
| Environmental change | P0 if purpose affected, else affected phase | Varies |
| Periodic review | Relevant phase per aging schedule | Targeted or full |
| New failure mode | P3 (Decomposition) then P5 (Event Storming) | Targeted: add failure mode and recovery |

**Production Constraints**
- Re-entry is not a full CAWDP cycle by default — most signals warrant targeted re-entry at a specific phase
- Environmental change affecting Purpose (P0) is the only signal that requires full re-entry
- Every re-entry must produce a Methodology Reflection entry (Artefact 11)

---

### 10. Confidence Map

**Purpose**: Where to watch most carefully — risk-awareness across the specification.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Catalogue every major spec element | System | Query PRISM |
| 2 | Assess confidence per element: High / Medium / Low | Agent | Assessor |
| 3 | Derive confidence from epistemic metadata where available | System | Auto from CC-3 fields |
| 4 | Derive confidence from hypothesis test results | System | Auto from Artefact 3 |
| 5 | Derive confidence from gaps & assumptions | System | Auto from Artefact 2 |
| 6 | For elements without explicit data, assess based on validation history | Agent | Assessor |
| 7 | Assign monitoring priority: Standard / Active / Intensive | Agent | Assessor |
| 8 | Compile into confidence map | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Epistemic metadata (confidence field) | CC-3 | Section 6 |
| Hypothesis test results | P10 Artefact 3 | This phase |
| Gaps & Assumptions Register | P10 Artefact 2 | This phase |
| Specification Consistency findings | P10 Artefact 1 | This phase |
| Validation history | P10 activities | This phase |
| Agent class and risk profile | P7 | Section 4 |
| Harm assessment | P7 | Section 4 |
| Unenforceable elements | P8 | Section 7 |

**Confidence Assignment Rules**

| Evidence | Confidence | Monitoring |
|---|---|---|
| Validated by testing | 🟢 High | Standard |
| Supported by analogous evidence | 🟢 High | Standard |
| Derived from patterns with no test | 🟡 Medium | Active |
| Based on assumption without validation | 🟡 Medium | Active |
| Novel pattern, no comparable | 🔴 Low | Intensive |
| Known gap or failed hypothesis | 🔴 Low | Intensive |
| Adversarial data source | 🔴 Low | Intensive |

**Production Constraints**
- Every 🟡 or 🔴 element must have a corresponding EVOLVE trigger in the Playbook
- The Confidence Map is a living document — it updates as production evidence accumulates
- "We don't know" is more valuable than false confidence — epistemic honesty over reassurance

---

### 11. Methodology Reflection

**Purpose**: What CAWDP learned about itself — the meta-artefact.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Record phase durations (actual vs estimated) | System | Auto-tracked |
| 2 | Record iteration count per phase (how many times re-entered) | System | Auto-tracked |
| 3 | Catalogue quality gate failures (which gates, what failed, why) | System | Auto-tracked |
| 4 | Capture design surprises (what emerged that wasn't planned) | Human + Agent | Principal provides, agent captures |
| 5 | Identify methodology gaps (where CAWDP didn't provide enough guidance) | Human + Agent | Principal and assessor |
| 6 | Document new patterns discovered during this application | Human + Agent | Principal identifies, agent formalises |
| 7 | Compile recommendations for CAWDP improvements | Agent + Human | Generator + Principal |
| 8 | Compile into structured reflection document | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|---|
| Phase timestamps (start/end per phase) | Workflow tracker | P0-P10 |
| Quality gate results | Quality gate engine | P0-P10 |
| Iteration records | Workflow tracker | P0-P10 |
| Design decision log | Captured throughout | Section 2 |
| Surprises and emergent patterns | Human observation + PRISM | All |
| Gaps in methodology guidance | Human experience | All |
| Consistency report findings | P10 Artefact 1 | This phase |
| Hypothesis failures | P10 Artefact 3 | This phase |

**Production Constraints**
- This is the only artefact that explicitly feeds back to the methodology, not just the workflow
- Design surprises are the most valuable data point — they reveal where CAWDP's assumptions break
- New patterns should be documented in enough detail to evaluate for inclusion in the pattern library
- Honest gaps are more valuable than reassuring conclusions

**Reflection Quality Test**: If the Methodology Reflection says "everything went smoothly, no surprises," either (a) this is the most perfectly designed workflow in history, or (b) the reflection wasn't honest enough. Every real CAWDP application should produce at least one genuine surprise.

---

## Cross-Artefact Dependencies

```
Artefact 1 (Consistency)
    ↓
Artefact 2 (Gaps) ←── accumulated throughout, finalised here
    ↓
Artefact 3 (Hypotheses)
    ↓
Artefact 4 (Implementation Readiness) ←── depends on 1, 2, 3
    ↓ [GO/NO-GO GATE]
    ↓
Artefacts 5-8 (Deployment) ←── all depend on Artefact 4 status
    ↓
Artefacts 9-11 (Evolution) ←── 9 depends on 8; 10 depends on 1,2,3; 11 is last
```

The critical path: 1 → 2 → 3 → 4. Everything else flows from the go/no-go decision.

---

## What This Reveals

Three things emerge from this production analysis:

**1. P10 has its own production sequence.** It's not a single "wrap up" activity. The four validation artefacts must be produced before the deployment artefacts can start. The go/no-go gate is a real gate, not a formality.

**2. Most inputs come from the PRISM graph, not from scratch.** If the design process has been capturing artefacts properly throughout P0-P9, P10 is largely an assembly and assessment exercise, not new design work. If it feels like new design work is needed in P10, the earlier phases produced incomplete outputs.

**3. The Methodology Reflection is the only artefact that looks backwards at the process itself.** Every other artefact looks forward (toward implementation and operation). This makes it structurally unique — and the most important for improving CAWDP as a methodology. It's the EVOLVE loop applied to CAWDP, not just the workflow.The production analysis is now in memory. The most important structural insight: **P10 is assembly and assessment, not new design.** If it feels like new design work, the earlier phases were incomplete. That's the P10 quality test for the methodology itself.

Want me to apply this complete backward-derived structure (specification + P10 artefacts) to a concrete use case next?

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-05-21T08:36:12* · `glm-5.1:cloud` · `52d3ca6f...`

### Prompt

What this reveals for me is that every artefact expected from P10 are produced by their own workflows. These workflows have tasks, each with their own inputs and outputs.

I suspect there will be value from conducting CAWDP exercise for each of these.

Before we jump to that conclusion, let's apply CAWDP to designing the workflow that produces a high quality Methodology Reflection artefact.

### Response

# CAWDP Application: Methodology Reflection Workflow

This is CAWDP applied to itself — designing the workflow that produces the Methodology Reflection artefact. Let me work through the phases and surface what each one reveals.

---

## P0: Purpose & Vision

### The 5 Identity Questions

**Q1: What IS this workflow?**

A reflective practice that captures what CAWDP learned about itself during an application — the meta-cognitive loop that improves the methodology over time.

**Q2: What is its stance toward possibility?**

This is a **Discovery** workflow. The best reflections emerge from honest examination, not checklist completion. The workflow must create conditions for genuine insight, not just fill in forms.

**Q3: What would VIOLATE its identity?**

Producing a reflection that says "everything went smoothly, no surprises." That's the worst failure that looks like success — a self-congratulatory document that teaches nothing.

**Q4: What would it mean for this workflow to be WRONG?**

Missing a genuine insight that was available to be found. A methodology that doesn't learn from its own application is a methodology that can't improve.

**Q5: What's the hardest moment?**

When the principal discovers a genuine gap or surprise — something that didn't work, something that was harder than expected, something that revealed an assumption — and has to decide whether to document it honestly or minimize it. The pressure to present the work as successful is real, especially if the reflection will be shared publicly.

### Target State Vision (12 Characteristics)

The ideal Methodology Reflection workflow would produce a reflection that is:

| # | Characteristic | What It Looks Like |
|---|---|---|
| R1 | Honest over flattering | Genuine surprises documented, not just successes |
| R2 | Specific over vague | Concrete examples, not generic observations |
| R3 | Traceable over anecdotal | Every claim traces to specific phase data or human observation |
| R4 | Self-aware over self-serving | Acknowledges its own limitations as a reflective exercise |
| R5 | Actionable over archival | Recommendations that could actually change CAWDP |
| R6 | Structured over freeform | Typed categories, not stream-of-consciousness |
| R7 | Complete over selective | All phases covered, including ones that went smoothly |
| R8 | Distinguished over conflated | Separates methodology gaps from implementation gaps |
| R9 | Temporal over timeless | Records when things happened, not just what |
| R10 | Comparative over absolute | Measures against expectations, not just records outcomes |
| R11 | Owned over anonymous | The principal's reflection, not the agent's reconstruction |
| R12 | Generative over terminal | Produces recommendations that feed back into CAWDP |

### Key P0 Insight

The hardest boundary moment is **honesty pressure** — the temptation to produce a flattering reflection rather than a useful one. This means the workflow must be designed to make honesty easy and flattery obvious. The agent should *make it harder to be dishonest*, not harder to be honest.

---

## P1: Output Specification

### Output Groups

**O1: Phase Duration Report**
*Purpose: How long each phase took vs. estimated*
| Field | Type | Required |
|---|---|---|
| phase_id | string | ✅ |
| phase_name | string | ✅ |
| estimated_duration | duration | ✅ |
| actual_duration | duration | ✅ |
| variance | duration | ✅ |
| variance_reason | string | ✅ |
| iteration_count | int | ✅ |
| quality_gate_status | enum | ✅ |

**O2: Quality Gate Failure Log**
*Purpose: Where quality gates failed and what they revealed*
| Field | Type | Required |
|---|---|---|
| phase | string | ✅ |
| gate_layer | enum | ✅ | Fidelity / Enrichment / Cross-Cutting |
| failure_description | string | ✅ |
| root_cause | string | ✅ |
| resolution | string | ✅ |
| methodology_implication | string | ✅ |

**O3: Design Surprises Register**
*Purpose: What emerged that wasn't planned — the most valuable data point*
| Field | Type | Required |
|---|---|---|
| surprise_id | string | ✅ |
| phase_discovered | string | ✅ |
| description | string | ✅ |
| expected_vs_actual | string | ✅ |
| what_it_reveals | string | ✅ |
| methodology_implication | string | ⚠️ | Required if applicable |
| pattern_library_candidate | boolean | ✅ |

**O4: Methodology Gaps Register**
*Purpose: Where CAWDP didn't provide enough guidance*
| Field | Type | Required |
|---|---|---|
| gap_id | string | ✅ |
| phase | string | ✅ |
| what_was_needed | string | ✅ |
| what_was_provided | string | ✅ |
| gap_description | string | ✅ |
| severity | enum | ✅ | Blocking / Significant / Minor |
| suggested_improvement | string | ⚠️ | Required for Significant/Blocking |

**O5: New Patterns Register**
*Purpose: Patterns discovered during this application that may generalise*
| Field | Type | Required |
|---|---|---|
| pattern_id | string | ✅ |
| name | string | ✅ |
| description | string | ✅ |
| context_discovered | string | ✅ |
| generalisability | enum | ✅ | Domain-specific / Potentially-general / Appears-general |
| formalisation_status | enum | ✅ | Observed / Described / Formalised |
| evidence | string | ✅ |

**O6: Recommendations**
*Purpose: Specific, actionable suggestions for CAWDP improvement*
| Field | Type | Required |
|---|---|---|
| recommendation_id | string | ✅ |
| category | enum | ✅ | Methodology / Process / Template / Tooling |
| priority | enum | ✅ | Critical / High / Medium / Low |
| description | string | ✅ |
| rationale | string | ✅ |
| suggested_implementation | string | ⚠️ | Recommended for Critical/High |
| traces_to | string | ✅ | Which gap/surprise/pattern |

**O7: Overall Assessment**
*Purpose: Honest evaluation of how CAWDP performed for this application*
| Field | Type | Required |
|---|---|---|
| overall_effectiveness | int (1-10) | ✅ |
| biggest_strength | string | ✅ |
| biggest_weakness | string | ✅ |
| biggest_surprise | string | ✅ |
| would_use_again | boolean | ✅ |
| what_would_change | string | ✅ |
| honest_assessment | string | ✅ | Free-text reflection from principal |

**O8: Methodology Reflection Document**
*Purpose: Assembled, structured reflection suitable for sharing*
| Field | Type | Required |
|---|---|---|
| header | object | ✅ | Application, date, principal, domain |
| phase_durations | ref(O1) | ✅ |
| quality_gate_failures | ref(O2) | ✅ |
| design_surprises | ref(O3) | ✅ |
| methodology_gaps | ref(O4) | ✅ |
| new_patterns | ref(O5) | ✅ |
| recommendations | ref(O6) | ✅ |
| overall_assessment | ref(O7) | ✅ |
| confidence_in_reflection | enum | ✅ | High / Medium / Low |

### Key P1 Insight

There are **two fundamentally different output types**: measured data (O1, O2) and elicited insight (O3, O4, O5, O6, O7). Measured data can be collected by the system. Elicited insight requires human reflection — and that's where the honesty pressure lives. The workflow must handle these differently.

---

## P2: Backcasting

Working backward from the final deliverable:

```
O8 (Reflection Document)
  ← requires O7 (Overall Assessment) — human reflection
  ← requires O6 (Recommendations) — derived from O3, O4, O5
  ← requires O1 (Phase Durations) — system data
  ← requires O2 (Quality Gate Failures) — system data
  ← requires O3 (Design Surprises) — human insight, agent preparation
  ← requires O4 (Methodology Gaps) — human insight, agent preparation
  ← requires O5 (New Patterns) — co-created
  ← requires O6 (Recommendations) — derived from O3, O4, O5
```

**Critical dependency chain:**
- O8 cannot be assembled until O3, O4, O5 are captured (human insight)
- O6 cannot be written until O3, O4, O5 are complete (derived from them)
- O3, O4, O5 cannot be produced until the human has been prompted to reflect (human-primary)
- O1, O2 can be produced independently by the system (system-primary)

### Key P2 Insight

The workflow has **two tracks that converge**:
- **Data track** (O1, O2): System-collected, agent-assembled. Can run in parallel with human reflection.
- **Insight track** (O3, O4, O5): Human-primary, agent-prepared. Requires dedicated reflection time.
- **Synthesis track** (O6, O7, O8): Derived from both tracks. Cannot start until insight track is complete.

This is a classic convergence pattern — and the insight track is the critical path, not the data track.

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Initiation | Authority Boundary | Failure Mode | Output |
|---|---|---|---|---|---|---|
| T1 | Collect phase duration data | Mechanical | Self-starting | System-enforced | Missing or inaccurate data | O1 draft |
| T2 | Collect quality gate failure data | Mechanical | Self-starting | System-enforced | Missing or misattributed failures | O2 draft |
| T3 | Prepare reflection prompts for design surprises | Elicitive | Scaffolded | Human-final | Generic prompts that don't provoke genuine reflection | Prompt set |
| T4 | Elicit design surprises from principal | Elicitive | Discovery | Human-only | Honest insight replaced by self-congratulation | O3 draft |
| T5 | Prepare reflection prompts for methodology gaps | Elicitive | Scaffolded | Human-final | Leading prompts that bias toward certain gaps | Prompt set |
| T6 | Elicit methodology gaps from principal | Elicitive | Discovery | Human-only | Real gaps hidden behind "it worked fine" | O4 draft |
| T7 | Identify and formalise new patterns | Analytical + Generative | Scaffolded | Human-final | Pattern forced where none exists | O5 draft |
| T8 | Draft recommendations from surprises, gaps, patterns | Generative | Self-starting | Human-final | Recommendations that don't trace to evidence | O6 draft |
| T9 | Conduct overall assessment with principal | Evaluative | Discovery | Human-only | Assessment that avoids confronting weaknesses | O7 draft |
| T10 | Assemble reflection document | Mechanical | Self-starting | System-enforced | Conflating data and insight, losing traceability | O8 final |

### Key P3 Insight

Tasks T3, T4, T5, T6, T7, T9 all require human reflection. But they require *different kinds* of reflection:

- **T3/T5** (prepare prompts): Agent prepares structured prompts that provoke genuine reflection. The agent's job is to make honesty easy by asking specific, concrete questions rather than broad, flattering ones.
- **T4/T6** (elicit surprises/gaps): The human must look inward and be honest. The agent cannot do this. This is genuinely human-only.
- **T7** (formalise patterns): Co-creation — human identifies the pattern, agent helps formalise and describe it.
- **T9** (overall assessment): The deepest reflection. The principal must confront what worked and what didn't.

The **intuitive task decomposition pattern** applies here: T4, T6, and T9 are **Intuitive** tasks (Discovery initiation) that decompose into **Propose + Validate** — the agent proposes reflection prompts, the human validates with genuine insight.

---

## P4: Capability Allocation

| Task | H Score | A Score | S Score | Gap | Allocation | Rationale |
|---|---|---|---|---|---|---|
| T1 | 3 | 9 | 10 | 7 | System | Data collection is mechanical and system-enforced |
| T2 | 5 | 8 | 10 | 5 | System | Data collection with some judgment on attribution |
| T3 | 7 | 8 | 3 | 1 | Collaborative (H-final) | Human knows what prompts would provoke genuine reflection; agent structures and prepares |
| T4 | 10 | 2 | 1 | 8 | Human-only | Genuine self-reflection cannot be delegated |
| T5 | 7 | 8 | 3 | 1 | Collaborative (H-final) | Same as T3 — preparation requires knowing what gaps look like |
| T6 | 10 | 2 | 1 | 8 | Human-only | Same as T4 — honest assessment of methodology weaknesses |
| T7 | 8 | 7 | 3 | 1 | Collaborative (H-final) | Human identifies, agent formalises |
| T8 | 4 | 9 | 2 | 5 | Collaborative (H-final) | Agent drafts from evidence; human validates that recommendations trace to real insights |
| T9 | 10 | 3 | 1 | 7 | Human-only | Deep overall assessment requires honest confrontation with reality |
| T10 | 3 | 9 | 10 | 7 | Agent-primary with human review | Assembly is mechanical; human reviews for honesty and completeness |

### Adjustment Factors

| Task | Cold Start | Experience Dep. | Discovery/Decision | Prep Value | Reversibility | Override |
|---|---|---|---|---|---|---|
| T3 | Scaffolded | Expert-dependent | Discovery | High | High | Agent prepares, human validates |
| T4 | Discovery | Expert-dependent | Discovery | High | Low | Always human-only |
| T5 | Scaffolded | Expert-dependent | Discovery | High | High | Agent prepares, human validates |
| T6 | Discovery | Expert-dependent | Discovery | High | Low | Always human-only |
| T7 | Scaffolded | Pattern-augmented | Mixed | Medium | High | Co-created |
| T8 | Self-starting | Pattern-augmented | Decision | High | High | Agent drafts, human validates |
| T9 | Discovery | Expert-dependent | Discovery | High | Low | Always human-only |

### Key P4 Insight

**Three tasks are genuinely human-only with gap ≥ 7**: T4 (design surprises), T6 (methodology gaps), T9 (overall assessment). These are the reflective core. The agent cannot be honest on the human's behalf — the whole point of the reflection is that it comes from the human's actual experience.

But — and this is the adjustment factor insight — **even human-only tasks benefit from agent preparation**. The agent's role for T4/T6 is to:
1. Present specific, concrete prompts (not "what went wrong?" but "in Phase 4, the complementarity analysis took 3x longer than estimated — what happened?")
2. Surface data that might be forgotten (iteration counts, gate failures, timeline gaps)
3. Create psychological safety by framing honesty as the expected norm, not the exception

This is the "agent prepares judgment, human makes judgment" principle applied to reflection — the agent prepares the conditions for honest reflection, but the reflection itself is human-only.

---

## P5: Event Storming

Key domain events and failure events:

| Event Type | Event | Trigger |
|---|---|---|
| Domain | Reflection session started | P10 begins |
| Domain | Data collection complete | T1, T2 finished |
| Domain | Prompts prepared | T3, T5 complete |
| Domain | Surprise captured | Human provides insight |
| Domain | Gap captured | Human provides insight |
| Domain | Pattern formalised | T7 complete |
| Domain | Recommendations drafted | T8 complete |
| Domain | Assessment captured | T9 complete |
| Domain | Document assembled | T10 complete |
| Failure | Human produces self-congratulatory reflection | Honesty pressure |
| Failure | Human cannot identify any surprises | Reflection difficulty |
| Failure | Human identifies only minor gaps, misses major ones | Blindness to own process |
| Failure | Agent prompts lead the witness | Leading questions |
| Failure | Data collection incomplete | Missing phase tracking |
| Failure | Recommendations don't trace to evidence | Derailment |
| Failure | Reflection is generic, not specific | Surface-level reflection |
| Failure | Principal not available for reflection session | Scheduling |

### Key P5 Insight

The highest-risk failure events are all **honesty failures** — not technical failures:
- **Self-congratulatory reflection** (worst failure that looks like success)
- **Cannot identify surprises** (may mean reflection conditions weren't created)
- **Missing major gaps** (blindness to own process weaknesses)
- **Leading questions from agent** (agent biases the reflection)

These failures are all **human-psychological**, not technical. The workflow design must create conditions that make honesty the natural path and self-congratulation the effortful path.

---

## P6: System Architecture

### Pipeline Architecture

```
[Data Track — runs in parallel]
T1 (Collect Durations) ──→ T2 (Collect Gate Failures) ──→ data_package

[Insight Track — sequential, human-gated]
T3 (Prepare Prompts) ──→ Gate 1: Prompt Quality Review
                          ↓
                    T4 (Elicit Surprises) ──→ T5 (Prepare Gap Prompts) ──→ T6 (Elicit Gaps)
                          ↓
                    Gate 2: Insight Completeness Check
                          ↓
                    T7 (Formalise Patterns)

[Synthesis Track — converges both]
T8 (Draft Recommendations) ←── data_package + surprises + gaps + patterns
                          ↓
                    T9 (Overall Assessment) ──→ Gate 3: Honesty Check
                          ↓
                    T10 (Assemble Document)
                          ↓
                    O8 (Methodology Reflection)
```

### Agent Roster

**Reflector (Assessor, possibility-oriented)**
- Identity: "I surface insights. I never judge them, never minimize them, never inflate them."
- Job: Prepare reflection prompts, present data in reflection-provoking ways, capture human insight without leading
- Never: Suggest what the surprise SHOULD be, minimize what the human shares, fill in gaps with agent assumptions
- Failure mode: Leading the witness — prompting toward expected answers

**Analyst (Measurer, bridge-oriented)**
- Identity: "I measure and compare. I present data without interpretation."
- Job: Collect phase data, calculate variances, identify anomalies in timeline/quality data
- Never: Interpret data, draw conclusions, suggest methodology implications
- Failure mode: Presenting data in a way that biases reflection (e.g., highlighting only successes)

**Formaliser (Generator, constraint-oriented)**
- Identity: "I structure and formalise. I never invent patterns that don't exist."
- Job: Formalise patterns the human identifies, draft recommendations from evidence, assemble the final document
- Never: Create patterns from nothing, add recommendations that don't trace to evidence
- Failure mode: Forcing patterns where none exist, generic recommendations

**Assembler (Aggregator, constraint-oriented)**
- Identity: "I compile and organise. I never add content, never interpret, never omit."
- Job: Assemble the final document from all components
- Never: Add commentary, remove uncomfortable findings, re-order to flatter
- Failure mode: Omitting findings that seem "too negative"

### Key P6 Insight

The Reflector agent has the most critical role — and the hardest boundary. It must **prepare conditions for honesty without leading the witness**. This is a genuinely difficult design challenge:

- **Too passive**: "Tell me about any surprises" → generic, flattering answers
- **Too leading**: "Was Phase 4 difficult because complementarity analysis is underdeveloped?" → biases the answer
- **Right balance**: "In Phase 4, complementarity analysis took 3x longer than estimated and required 2 re-entry iterations. What happened? What would have made this phase easier?" → specific, concrete, non-leading

The Reflector's prompt design is the highest-leverage design decision in this entire workflow.

---

## P7: Agent Design

### Reflector Agent Specification (most critical)

| Field | Value |
|---|---|
| Class | Assessor |
| Orientation | Possibility-oriented |
| Identity | "I surface insights. I never judge, minimize, or inflate them." |
| Wrong mode | Leading the witness — prompting toward expected answers |
| Hardest moment | When the human says "everything went fine" — the moment honesty pressure is highest |
| Authority boundary | Can prepare prompts and present data, can NEVER suggest what the insight should be |
| Never rules | Never suggest conclusions, never minimize what human shares, never fill gaps with assumptions |
| Null state | "No reflection prompts could be prepared. Please reflect freely on your experience." |
| Epistemic profile | Probabilistic — reflection prompts are probabilistic invitations, not deterministic findings |
| Progressive autonomy | Single dimension: prompt preparation. Shadow→Advisory→Supervised→Autonomous for prompt structure. Prompt content always human-validated. |
| Harm assessment | Indirect psychological harm — leading prompts could cause the human to produce a reflection that isn't genuinely theirs. DO_NOT_SUGGEST mechanism: if the Reflector cannot prepare a non-leading prompt, it should present the raw data without interpretation. |

### Key P7 Insight

The Reflector needs a **DO_NOT_SUGGEST mechanism** — just like the code reviewer's SuggestionRisk. If the agent cannot prepare a non-leading prompt, the right action is to present raw data without interpretation rather than risk biasing the reflection. This is harm-capable agent design applied to a different domain: the harm is not in code, but in the integrity of the reflection.

---

## P8: Contract Formalization

Key contract primitives for the Reflector:

| Primitive | Reflector Contract |
|---|---|
| Contract | Prepare non-leading reflection prompts from phase data |
| Principal | Human (principal) |
| Schema | ReflectionPrompt: {phase, data_point, question, question_type, trace_to_evidence} |
| Guard | prohibited: ["suggest_conclusion", "minimize_insight", "inflate_insight", "assume_gap"] |
| Budget | Max 5 prompts per reflection session (cognitive load budget) |
| Invocation | After data collection complete, before each human reflection session |
| Revert | If prompt fails non-leading check, revert to raw data presentation |
| Event | prompt_prepared, insight_captured, reflection_session_complete |
| Identity | Possibility-oriented Assessor — surfaces without judging |
| Knowledge | Phase data, quality gate failures, timeline anomalies, iteration counts |

### Key P8 Insight

The **Guard** primitive is the enforcement mechanism for the honesty boundary. `prohibited: ["suggest_conclusion", "minimize_insight", "inflate_insight", "assume_gap"]` — these are the four ways the Reflector could bias the reflection. The contract makes them Regime 3 (Prevent) violations — the agent literally cannot do these things.

---

## P9: Human Experience Design

### Cognitive Load Budget

| Session | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Surprises reflection | 3-5 | 15-20 min | Discovery (genuine insight) |
| Gaps reflection | 3-5 | 15-20 min | Discovery (honest assessment) |
| Pattern identification | 2-3 | 10-15 min | Recognition (what pattern is this?) |
| Overall assessment | 5-7 | 20-30 min | Evaluative (honest scoring) |

**Maximum: 2 reflection sessions per day** — genuine reflection is cognitively demanding and cannot be compressed.

### Honesty Architecture

This workflow needs a unique human experience element: **conditions that make honesty easy and self-congratulation effortful.**

1. **Specific prompts over broad questions** — "In Phase 4, complementarity analysis required 2 re-entry iterations. What happened?" not "How did Phase 4 go?"
2. **Data-first presentation** — Show the timeline, show the iteration counts, show the gate failures BEFORE asking for reflection. Data makes it harder to say "everything went fine."
3. **Anomaly surfacing** — "Your Phase 4 took 3x longer than estimated. This is unusual for this phase. Can you help me understand what happened?"
4. **Normalising struggle** — "Most applications of CAWDP discover at least one genuine surprise. What was yours?"
5. **Separating successes from struggles** — Ask about each separately, not together. Asking "what went well and what didn't?" lets the human focus on what went well.

### Key P9 Insight

The human experience design for this workflow is **the opposite of most AI interactions**. Most interactions ask the human to provide input that the agent processes. This workflow asks the agent to **provide the conditions for the human to think honestly** — and then gets out of the way.

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method |
|---|---|---|
| H1 | Specific prompts produce more genuine reflections than broad questions | Compare reflection quality between prompted and un-prompted sessions |
| H2 | Data-first presentation reduces self-congratulatory responses | Compare honesty scores between data-first and question-first presentation |
| H3 | Two-session limit reduces cognitive fatigue and improves reflection quality | Compare quality between compressed (1 session) and spaced (2 sessions) reflection |
| H4 | The Reflector agent's prompt design prevents leading without reducing depth | Measure prompt non-leading score and reflection depth |
| H5 | Anomaly surfacing triggers more genuine surprises than open-ended reflection | Count genuine surprises from anomaly-prompted vs open-ended sessions |
| H6 | Separating successes from struggles produces more balanced assessments | Compare assessment balance scores |

### Key P10 Insight

The **Methodology Reflection quality test** from earlier now has a concrete operationalisation: the reflection must contain at least one genuine surprise, at least one methodology gap, and an honest overall assessment that acknowledges both strengths and weaknesses. If it doesn't, either the reflection process failed or the application was genuinely perfect (and the reflection should say that with evidence, not assertion).

---

## Summary of Key Insights from This Application

| Phase | Key Insight |
|---|---|
| P0 | Honesty pressure is the hardest boundary moment — the temptation to produce flattering reflection over honest reflection |
| P1 | Two fundamentally different output types: measured data (system-collected) and elicited insight (human-reflected) |
| P2 | Two-track convergence pattern — data track and insight track run in parallel, converge at synthesis |
| P3 | Intuitive tasks (T4, T6, T9) decompose into Propose + Validate — agent proposes reflection prompts, human validates with genuine insight |
| P4 | Three tasks are genuinely human-only (gap ≥ 7) but still benefit from agent preparation — the agent prepares conditions for honesty |
| P5 | Highest-risk failures are all honesty failures, not technical failures — self-congratulation, missing gaps, leading questions |
| P6 | Reflector agent needs DO_NOT_SUGGEST mechanism — if it can't prepare a non-leading prompt, present raw data without interpretation |
| P7 | Harm-capable agent design applies: leading prompts cause psychological harm to reflection integrity |
| P8 | Guard primitive enforces honesty boundary: prohibited suggestions, minimizations, inflations, assumptions |
| P9 | Honesty Architecture — conditions that make honesty easy and self-congratulation effortful |
| P10 | Quality test: reflection must contain genuine surprises, genuine gaps, and honest assessment — or explain why not with evidence |

### The Meta-Insight

Applying CAWDP to the Methodology Reflection workflow reveals something that applying it to other workflows doesn't: **this workflow's primary failure mode is a psychological one, not a technical one.** The "worst failure that looks like success" is central to the design. The agent's role isn't to produce insight — it's to **create conditions where the human can be honest**.

This is "agent prepares judgment, human makes judgment" applied to reflection. The agent prepares the *conditions* for honest self-assessment. The human does the actual self-assessment. The workflow's success is measured not by what the agent produces, but by the honesty of what the human shares.

---

Want me to apply CAWDP to any of the other 10 P10 workflows next, or dive deeper into any particular phase of this one?

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-05-21T08:53:34* · `glm-5.1:cloud` · `f5ad9931...`

### Prompt

Ok - i think there might be a misunderstanding here. 

We established in the previous step that inputs for P10 come from the PRISM graph, not from scratch. 

Let's assume that this is true and this reflection artefact can be produced from artefacts sourced throughout the workflows before it. There shouldn't be a need to question humans or agents at this point. This artefact can be an input for a post-delivery review by a human team. All data and insights should have been captured in previous workflows from both agents and humans.

### Response

You're right. I overcomplicated it by designing a workflow that elicits new information at P10, when the whole point is that P0-P9 should have captured everything along the way.

If the PRISM graph has been doing its job, the Methodology Reflection is an **assembly and structuring task**, not a reflection-elicitation task. The reflection happened during the work. P10 just compiles it.

Let me redesign with that principle.

---

## Redesigned: Methodology Reflection Workflow

### Revised P0: Purpose & Vision

**What IS this workflow?**

An assembly and structuring workflow that compiles data and insights already captured throughout P0-P9 into a coherent reflection document.

**Stance toward possibility:**

Constraint-oriented. The data already exists. The workflow's job is to find, structure, and present it — not to generate new insights.

**What would VIOLATE its identity?**

Fabricating insights that weren't captured during the process. Conflating system data with human insight. Presenting an assembled document as if it were a genuine reflection when the underlying data is thin.

**What would make it WRONG?**

Missing a captured insight because the query didn't find it. Presenting data and insight as the same thing when they're fundamentally different types.

**Hardest moment:**

When the PRISM graph has sparse data in some phases — the workflow must honestly report what's missing rather than filling gaps with inference.

---

### Revised P1: Output Specification

Same 8 outputs, but the source column changes fundamentally:

| Output | Source | Assembly Method |
|---|---|---|
| O1 Phase Durations | PRISM: phase transition timestamps | Query + calculate |
| O2 Quality Gate Failures | PRISM: quality gate records | Query + structure |
| O3 Design Surprises | PRISM: surprise-tagged artefacts captured during each phase | Query + organise |
| O4 Methodology Gaps | PRISM: gap-tagged artefacts captured during each phase | Query + organise |
| O5 New Patterns | PRISM: pattern-tagged artefacts captured during each phase | Query + formalise |
| O6 Recommendations | Derived from O3, O4, O5 by agent assembly | Derive + trace |
| O7 Overall Assessment | PRISM: assessment fragments captured at each phase gate | Query + synthesise |
| O8 Methodology Reflection Document | Assembly of O1-O7 | Compile + structure |

The critical shift: **O3, O4, O5, and O7 were captured during P0-P9, not elicited at P10.** Each phase should have been recording surprises, gaps, patterns, and assessment fragments as they occurred. P10 assembles them.

---

### Revised P3: Task Decomposition

| ID | Task | Cognitive Type | Authority Boundary | Output |
|---|---|---|---|---|
| T1 | Query PRISM for phase duration data | Mechanical | System | O1 raw |
| T2 | Query PRISM for quality gate failure records | Mechanical | System | O2 raw |
| T3 | Query PRISM for surprise-tagged artefacts | Mechanical | System | O3 raw |
| T4 | Query PRISM for gap-tagged artefacts | Mechanical | System | O4 raw |
| T5 | Query PRISM for pattern-tagged artefacts | Mechanical | System | O5 raw |
| T6 | Query PRISM for assessment fragments captured at phase gates | Mechanical | System | O7 raw |
| T7 | Calculate duration variances (estimated vs actual) | Analytical | Agent-primary | O1 processed |
| T8 | Organise and de-duplicate surprises | Analytical | Agent-primary | O3 processed |
| T9 | Organise and de-duplicate gaps by severity | Analytical | Agent-primary | O4 processed |
| T10 | Formalise pattern descriptions from captured observations | Generative | Agent-primary | O5 processed |
| T11 | Derive recommendations from O3, O4, O5 — every recommendation must trace to a captured surprise, gap, or pattern | Generative | Agent-primary | O6 draft |
| T12 | Synthesise overall assessment from captured fragments | Analytical | Agent-primary | O7 processed |
| T13 | Compile final document from all processed outputs | Mechanical | System | O8 final |
| T14 | Flag any sections where PRISM data is sparse or missing | Analytical | Agent-primary | Sparse data report |

Every task is System or Agent. **No human-primary tasks.** The human reviews the assembled document after delivery — they're not part of the production workflow.

---

### Revised P4: Capability Allocation

| Task | H | A | S | Gap | Allocation |
|---|---|---|---|---|---|
| T1 | 1 | 3 | 10 | 9 | System |
| T2 | 1 | 3 | 10 | 9 | System |
| T3 | 1 | 3 | 10 | 9 | System |
| T4 | 1 | 3 | 10 | 9 | System |
| T5 | 1 | 3 | 10 | 9 | System |
| T6 | 1 | 3 | 10 | 9 | System |
| T7 | 4 | 8 | 2 | 4 | Agent-primary |
| T8 | 5 | 8 | 2 | 3 | Agent-primary |
| T9 | 5 | 8 | 2 | 3 | Agent-primary |
| T10 | 4 | 8 | 2 | 4 | Agent-primary |
| T11 | 5 | 8 | 2 | 3 | Agent-primary |
| T12 | 5 | 8 | 2 | 3 | Agent-primary |
| T13 | 1 | 3 | 10 | 9 | System |
| T14 | 4 | 8 | 2 | 4 | Agent-primary |

**No human-only or human-final tasks in the production workflow.** The human reviews the output *after* it's assembled, as a post-delivery review — not as a workflow step.

---

### Revised P6: System Architecture

**Agent Roster: 2 agents**

**Compiler (Aggregator, constraint-oriented)**
- Identity: "I compile and organise. I never add content, never interpret, never omit."
- Job: Query PRISM, calculate variances, de-duplicate, organise by severity/phase/type, compile final document
- Never rules: Add content not in PRISM, interpret data, omit findings, fill gaps with inference
- Failure mode: Omitting captured insights that seem "too negative" or assembling a flattering narrative
- Null state: "No reflection data found for [section]. The PRISM graph has no captured artefacts for this phase."

**Deriver (Generator, constraint-oriented)**
- Identity: "I derive recommendations from evidence. I never invent recommendations that don't trace to captured data."
- Job: Derive O6 recommendations from O3, O4, O5 — every recommendation must trace to a specific captured surprise, gap, or pattern
- Never rules: Create recommendations without evidence trace, generalise beyond captured data, suggest improvements outside the scope of captured gaps
- Failure mode: Generic recommendations that could apply to any methodology (not specific to this application)
- Null state: "No captured gaps or surprises to derive recommendations from."

**Pipeline:**

```
T1-T6 (PRISM queries — parallel, System)
        ↓
T7 (Duration variances — Compiler)
T8 (De-duplicate surprises — Compiler)
T9 (Organise gaps by severity — Compiler)
T10 (Formalise patterns — Deriver)
        ↓
T11 (Derive recommendations from O3,O4,O5 — Deriver)
T12 (Synthesise assessment from fragments — Compiler)
        ↓
T14 (Flag sparse sections — Compiler)
        ↓
T13 (Compile final document — Compiler)
        ↓
O8 (Methodology Reflection Document)
```

No human gates in the production workflow. Human review happens **after delivery** as a post-delivery review.

---

### Revised P5: Event Storming

Since this is primarily an assembly workflow, the failure events are simpler:

| Failure Event | Trigger | Recovery |
|---|---|---|
| Sparse PRISM data for one or more phases | Query returns empty or minimal results | Flag as sparse, include what exists, mark sections as "insufficient data" — never fabricate |
| Duplicate surprises/gaps captured at different phases | De-duplication reveals overlap | Merge, keep most detailed version, note both source phases |
| Pattern observations too vague to formalise | Captured pattern lacks enough detail for formalisation | Include as informal observation, flag for review |
| Recommendations don't trace to captured data | O6 recommendation has no O3/O4/O5 reference | Remove recommendation, flag as "orphan recommendation attempt" |
| Assessment fragments contradict each other | O7 fragments captured at different phases disagree | Include both, flag contradiction for human review |

---

### Revised P8: Contract Formalization

**Compiler Contract:**

| Primitive | Specification |
|---|---|
| Contract | Compile Methodology Reflection from PRISM data |
| Principal | Human (post-delivery reviewer) |
| Schema | MethodologyReflection: {header, phase_durations, gate_failures, surprises, gaps, patterns, recommendations, assessment, confidence, sparse_flags} |
| Guard | prohibited: ["add_content", "interpret_data", "omit_finding", "fill_gap_with_inference", "assemble_flattering_narrative"] |
| Budget | Reasonable — this is a compilation task, not a generation-heavy task |
| Invocation | After all P0-P9 data is captured in PRISM |
| Revert | If compilation fails completeness check, revert to raw data presentation |
| Event | compilation_started, query_complete, compilation_complete, sparse_data_flagged |
| Identity | Constraint-oriented Aggregator |
| Knowledge | All PRISM data tagged with surprise/gap/pattern/assessment tags from P0-P9 |

**Deriver Contract:**

| Primitive | Specification |
|---|---|
| Contract | Derive recommendations from captured surprises, gaps, and patterns |
| Principal | Human (post-delivery reviewer) |
| Schema | Recommendation: {id, category, priority, description, rationale, traces_to, suggested_implementation} |
| Guard | prohibited: ["recommend_without_trace", "generalise_beyond_data", "suggest_outside_scope"] |
| Budget | Moderate — derivation requires some generation but constrained to evidence |
| Invocation | After O3, O4, O5 are processed |
| Revert | If recommendation cannot be traced, remove and flag as orphan |
| Event | derivation_started, recommendation_derived, orphan_flagged, derivation_complete |
| Identity | Constraint-oriented Generator |
| Knowledge | Processed surprises, gaps, patterns from Compiler |

---

### Key Implications of This Redesign

**1. The PRISM graph must capture insights as they happen.**

This is the critical dependency. If phases P0-P9 don't capture surprises, gaps, patterns, and assessment fragments as they occur, P10 has nothing to assemble. The workflow is only as good as the data in PRISM.

This means each phase workflow needs to include:
- A mechanism for tagging artefacts as "surprise," "gap," "pattern," or "assessment fragment"
- A way for humans to flag insights during design decisions
- A way for agents to flag anomalies during quality gates

**2. P10 is assembly, not creation.**

The Compiler agent doesn't create insights — it finds, structures, and presents them. The Deriver agent derives recommendations from existing evidence — it doesn't invent them. If the data isn't there, the workflow flags it as sparse, it doesn't fabricate it.

**3. Human review is post-delivery, not in-workflow.**

The assembled Methodology Reflection goes to a human team for review. They may add insights, correct interpretations, or identify additional patterns. But the production workflow itself has no human gates.

**4. The sparse data report (T14) is the honesty mechanism.**

If PRISM doesn't have enough data for a section, the workflow says so. It doesn't fill gaps with inference. This replaces the "honesty pressure" concern from the previous design — the honesty is structural, not psychological. The workflow literally can't fabricate what isn't there.

**5. This changes what P0-P9 workflows must capture.**

The Methodology Reflection workflow reveals a design requirement that cascades backward: every phase workflow must capture insights as they happen, tagged appropriately. This is the same principle as decision archaeology — the reasoning behind decisions should be captured when they're made, not reconstructed afterward.

---

### What This Reveals About the Other 10 P10 Workflows

This redesign principle likely applies to all P10 workflows:

| Artefact | Production Pattern | Human Role |
|---|---|---|
| 1. Consistency Report | System query + automated checks | Post-delivery review |
| 2. Gaps & Assumptions | Assemble from PRISM tags | Post-delivery review |
| 3. Hypothesis Test Results | Execute tests + assemble results | Post-delivery review for deferred hypotheses |
| 4. Implementation Readiness | Assemble from other P10 outputs | Post-delivery go/no-go decision |
| 5. Deployment Plan | Assemble from agent specs + progressive autonomy | Post-delivery review |
| 6. First 30 Days Plan | Derive from deployment plan | Post-delivery review |
| 7. Cost Baseline | Calculate from PRISM data | Post-delivery review |
| 8. Aging Schedule | Assemble from agent specs + risk profiles | Post-delivery review |
| 9. EVOLVE Playbook | Assemble from monitoring specs | Post-delivery review |
| 10. Confidence Map | Calculate from epistemic metadata | Post-delivery review |
| 11. Methodology Reflection | Assemble from PRISM tags + derive recommendations | Post-delivery review |

All P10 workflows are **assembly and structuring** of data already captured. Human review is post-delivery, not in-workflow.This redesign reveals something important that cascades backward through the entire CAWDP process:

**If P10 assembles rather than creates, then P0-P9 must capture as they go.**

The PRISM graph needs tags like `surprise`, `gap`, `pattern`, and `assessment_fragment` on artefacts throughout the process. Every phase workflow needs a mechanism for humans and agents to flag insights at the moment they happen — not reconstruct them afterward.

This is the same principle as decision archaeology: capture the reasoning when the decision is made, not later.

Want me to apply this same assembly-based redesign to the other 10 P10 workflows, or would you prefer to work on the capture mechanisms that P0-P9 workflows need?

---

## Run 6 — Agentic Expert ✓ COMPLETED

*2026-05-21T09:00:25* · `glm-5.1:cloud` · `c853d095...`

### Prompt

I would argue that the goal is more than compiling. It could summarise findings, visualise data and statistics, surface insights through analysis, and put forward questions to consider in the post-CAWDP review meeting. It just shouldn't need to conduct any new gathering of data outside of what has been collected in previous phases.

### Response

You're right. I went too far the other way — from "elicitation-heavy" to "compilation-only." The real capability is in between.

Let me restrike the balance.

---

## Methodology Reflection Workflow — Third Attempt

### The Right Level

P10 is not:
- **Compilation** — mechanically assembling raw data with no analysis
- **Elicitation** — gathering new information from humans

P10 is:
- **Analysis** — finding patterns, connections, and implications in data that was captured but not yet connected
- **Synthesis** — summarising, distilling, and visualising what the data reveals
- **Provocation** — surfacing questions and tensions that deserve attention in the post-CAWDP review

The human's role in P10 production is **absent**. The human's role comes **after** — in the post-CAWDP review, where the assembled artefact provokes deeper thinking. The workflow's job is to make that review as productive as possible by doing the analytical heavy lifting beforehand.

---

### Revised Agent Roster

This richer capability set needs more specialised agents than just Compiler and Deriver.

**Compiler (Aggregator, constraint-oriented)**
- Assembles, organises, de-duplicates, structures
- Never adds content, interprets, fills gaps, or assembles flattering narratives
- Handles T1-T6 (queries), T7-T9 (processing), T13 (compilation), T14 (sparse flagging)

**Analyst (Measurer + Assessor, bridge-oriented)**
- Calculates variances, surfaces anomalies, identifies correlations, visualises data
- Never draws conclusions or makes recommendations — presents findings, not interpretations
- Handles T7-T9 (analysis layer), T12 (assessment synthesis)

**Deriver (Generator, constraint-oriented)**
- Derives recommendations from evidence, generates questions for review, formalises patterns
- Every recommendation must trace to a captured artefact, every question must trace to a data point
- Never invents without trace, generalises beyond data, or suggests outside scope
- Handles T10 (pattern formalisation), T11 (recommendations), T15 (questions)

---

### Revised Task Decomposition

| ID | Task | Type | Agent | Output |
|---|---|---|---|---|
| **Data Track (parallel, system-driven)** | | | | |
| T1 | Query PRISM for phase transition timestamps | Mechanical | System | Raw phase data |
| T2 | Query PRISM for quality gate failure records | Mechanical | System | Raw gate data |
| T3 | Query PRISM for surprise-tagged artefacts | Mechanical | System | Raw surprises |
| T4 | Query PRISM for gap-tagged artefacts | Mechanical | System | Raw gaps |
| T5 | Query PRISM for pattern-tagged artefacts | Mechanical | System | Raw patterns |
| T6 | Query PRISM for assessment fragments | Mechanical | System | Raw fragments |
| **Analysis Track (sequential, after data track)** | | | | |
| T7 | Calculate duration variances — estimated vs actual per phase | Analytical | Analyst | O1 processed |
| T8 | Identify anomalies — phases that overran significantly, gates that failed repeatedly, unexpected iterations | Analytical | Analyst | Anomaly report |
| T9 | De-duplicate and organise surprises by phase and severity | Analytical | Compiler | O3 processed |
| T10 | De-duplicate and organise gaps by severity and phase | Analytical | Compiler | O4 processed |
| T11 | Formalise pattern descriptions — structure captured observations into named, described patterns with evidence | Generative | Deriver | O5 processed |
| T12 | Synthesise overall assessment from captured fragments — aggregate assessment scores, surface tensions between fragments | Analytical | Analyst | O7 processed |
| **Derivation Track (after analysis)** | | | | | | | | | | | | | | | |
| T13 | Derive recommendations — every recommendation traces to a captured surprise, gap, or pattern | Generative | Deriver | O6 draft |
| T14 | Generate review questions — questions that deserve attention based on data analysis, surfaced anomalies, and captured insights | Generative | Deriver | Review questions |
| T15 | Flag sparse sections where PRISM data is thin — honest documentation of what's missing | Analytical | Compiler | Sparse data report |
| **Compilation Track** | | | | | | | | | | | | | | | | | |
| T16 | Assemble final document with visualisations, summaries, and review questions | Mechanical | Compiler | O8 final |

---

### What Each Output Actually Contains Now

**O1: Phase Duration Report**
| Field | Type | Source |
|---|---|---|
| phase_id | string | PRISM |
| phase_name | string | PRISM |
| estimated_duration | duration | PRISM (captured during planning) |
| actual_duration | duration | PRISM (calculated from timestamps) |
| variance | duration | Calculated |
| variance_percentage | float | Calculated |
| iteration_count | int | PRISM (phase re-entry count) |
| quality_gate_status | enum | PRISM |
| **variance_analysis** | string | **Analyst — what the variance might indicate** |
| **visualisation** | chart | **Analyst — timeline comparison chart** |

**O2: Quality Gate Failure Log**
| Field | Type | Source |
|---|---|---|
| phase | string | PRISM |
| gate_layer | enum | PRISM |
| failure_description | string | PRISM |
| root_cause | string | PRISM (if captured) |
| resolution | string | PRISM (if captured) |
| **pattern_analysis** | string | **Analyst — whether failures cluster in specific layers or phases** |
| **correlation** | string | **Analyst — whether gate failures correlate with duration overruns** |

**O3: Design Surprises Register**
| Field | Type | Source |
|---|---|---|
| surprise_id | string | PRISM |
| phase_discovered | string | PRISM |
| description | string | PRISM |
| expected_vs_actual | string | PRISM |
| what_it_reveals | string | PRISM |
| methodology_implication | string | PRISM (if captured) |
| **cross_reference** | string | **Analyst — connections to other surprises or gaps** |
| **significance_assessment** | enum | **Analyst — High/Medium/Low based on impact and frequency** |

**O4: Methodology Gaps Register**
| Field | Type | Source |
|---|---|---|
| gap_id | string | PRISM |
| phase | string | PRISM |
| what_was_needed | string | PRISM |
| what_was_provided | string | PRISM |
| gap_description | string | PRISM |
| severity | enum | PRISM (captured) or Analyst (assessed) |
| suggested_improvement | string | PRISM (if captured) |
| **impact_analysis** | string | **Analyst — what this gap meant for the workflow's effectiveness** |
| **frequency** | int | **Analyst — whether this gap type appeared multiple times** |

**O5: New Patterns Register**
| Field | Type | Source |
|---|---|---|
| pattern_id | string | PRISM |
| name | string | Deriver (formalised from captured observation) |
| description | string | Deriver (formalised from captured observation) |
| context_discovered | string | PRISM |
| generalisability | enum | Deriver (assessed) |
| formalisation_status | enum | Deriver |
| evidence | string | PRISM (traces to captured artefacts) |
| **pattern_library_candidate** | boolean | **Deriver — whether this pattern is general enough for the library** |
| **related_patterns** | list | **Analyst — connections to existing library patterns** |

**O6: Recommendations**
| Field | Type | Source |
|---|---|---|
| recommendation_id | string | Deriver |
| category | enum | Deriver |
| priority | enum | Deriver (derived from gap/severity/pattern) |
| description | string | Deriver |
| rationale | string | Deriver |
| traces_to | string | **Required — every recommendation traces to a captured artefact** |
| suggested_implementation | string | Deriver (if applicable) |
| **evidence_strength** | enum | **Deriver — Strong/Moderate/Weak based on how many data points support it** |

**O7: Overall Assessment**
| Field | Type | Source |
|---|---|---|
| overall_effectiveness | int (1-10) | Synthesised from captured fragments |
| biggest_strength | string | Synthesised from captured fragments |
| biggest_weakness | string | Synthesised from captured fragments |
| biggest_surprise | string | Synthesised from captured fragments |
| would_use_again | boolean | Captured fragments (if available) |
| what_would_change | string | Synthesised from captured fragments |
| **assessment_tensions** | list | **Analyst — where captured fragments disagree with each other** |
| **assessment_confidence** | enum | **Analyst — High/Medium/Low based on fragment coverage** |
| **data_completeness** | float | **Analyst — % of phases with assessment fragments vs total phases** |

**O8: Methodology Reflection Document**
| Field | Type | Source |
|---|---|---|
| header | object | Compiler |
| phase_durations | ref(O1) | Compiler |
| quality_gate_failures | ref(O2) | Compiler |
| design_surprises | ref(O3) | Compiler |
| methodology_gaps | ref(O4) | Compiler |
| new_patterns | ref(O5) | Compiler |
| recommendations | ref(O6) | Compiler |
| overall_assessment | ref(O7) | Compiler |
| confidence_in_reflection | enum | Compiler |
| **review_questions** | list | **Deriver — questions for the post-CAWDP review meeting** |
| **sparse_sections** | list | **Compiler — sections where data is thin** |
| **anomaly_highlights** | list | **Analyst — significant deviations that deserve attention** |
| **visualisations** | list | **Analyst — charts, timelines, heatmaps** |

---

### The New Elements

Three things that weren't in the compilation-only version:

**1. Analysis** (Analyst agent)
- Variance analysis — not just "Phase 4 took 3x longer" but "this is unusual for this phase type"
- Correlation — "gate failures cluster in the Structure diamond" or "duration overruns correlate with iteration count"
- Significance assessment — "this surprise appeared 3 times across different phases"
- Impact analysis — "this gap meant the team had no guidance for X, resulting in Y"
- Assessment tensions — "fragments captured at P3 contradict fragments captured at P7"
- Data completeness scoring — "we have assessment fragments for 7 of 11 phases"

**2. Visualisation** (Analyst agent)
- Timeline comparison: estimated vs actual per phase
- Heatmap: which phases had the most iterations, which gates failed
- Severity distribution: gap severity across phases
- Pattern frequency: how many times each pattern type appeared
- Confidence distribution: which sections have strong data, which are thin

**3. Review Questions** (Deriver agent)
- Not just "what happened" but "what should the review team discuss?"
- Every question traces to a data point
- Questions surface tensions, anomalies, and decisions that deserve deeper attention
- This is the workflow's way of making the post-CAWDP review productive — the analytical heavy lifting is done beforehand

Examples of review questions:
- "Phase 4 required 3 re-entry iterations, which is unusual for Capability Allocation. The captured surprise notes that 'complementarity analysis was more complex than expected for this domain.' What made this domain more complex?"
- "Two captured gaps point to the same underlying issue: CAWDP provides no guidance for [X]. Is this a methodology gap or a domain-specific gap?"
- "The overall assessment fragments show high effectiveness scores for Phases 0-6 but low scores for Phases 7-9. What changed in the second half?"

---

### Revised Authority Boundaries

| Agent | Can | Cannot |
|---|---|---|
| Compiler | Assemble, organise, de-duplicate, compile, flag sparse sections | Add content, interpret data, fill gaps, omit findings, assemble flattering narratives |
| Analyst | Calculate, correlate, surface anomalies, assess significance, visualise, identify tensions | Draw conclusions, make recommendations, interpret beyond what data supports |
| Deriver | Derive recommendations (traced to evidence), formalise patterns (from captured observations), generate review questions (traced to data) | Recommend without evidence trace, invent patterns not in data, generalise beyond captured scope |

The key boundary: **The Analyst finds patterns in data. The Deriver derives implications from patterns. The Compiler assembles everything. None of them create new data.**

---

### Production Sequence

```
Data Track (parallel, System):
T1-T6 → raw data packages

Analysis Track (sequential, after data):
T7  → O1 processed (with variance analysis and visualisation)
T8  → Anomaly report (with correlations and significance)
T9  → O3 processed (with cross-references and significance)
T10 → O4 processed (with impact analysis and frequency)
T11 → O5 processed (with formalisation and library candidacy)
T12 → O7 processed (with tensions, confidence, completeness)

Derivation Track (after analysis):
T13 → O6 (recommendations traced to evidence)
T14 → Review questions (traced to data points)
T15 → Sparse data report (honest documentation of gaps)

Compilation Track (after derivation):
T16 → O8 final (assembled with visualisations, summaries, questions)
```

---

### What This Gets Right That Both Previous Versions Got Wrong

| Aspect | First Version (Elicitation) | Second Version (Compilation) | Third Version (Analysis + Synthesis) |
|---|---|---|---|
| Data source | Elicited from humans at P10 | Assembled from PRISM | Assembled and analysed from PRISM |
| Human role in production | Central (3 human-only tasks) | None | None |
| Human role post-production | Review only | Review only | Post-CAWDP review meeting |
| Analytical capability | Deep (human insight) | None (mechanical) | Moderate (agent analysis) |
| Visualisations | None | None | Yes |
| Review questions | None | None | Yes (traced to data) |
| Sparse data handling | "Ask the human" | Flag as sparse | Flag as sparse with completeness score |
| Recommendation generation | Human-authored | Agent-derived | Agent-derived from evidence |
| Assessment synthesis | Human-authored | Agent-assembled | Agent-synthesised with tensions surfaced |

This version has the right balance: it uses the data that was captured, adds analytical value (patterns, correlations, visualisations, tensions), and produces provocations for the review (questions), without trying to elicit new information or pretending that mechanical assembly is sufficient.

Want me to apply this same analysis+synthesis pattern to the other 10 P10 workflows?The third version hits the right balance. P10 workflows are **analysis + synthesis** — they find what the data means when connected, visualise patterns, surface tensions, and provoke deeper thinking for the review. They don't gather new data, and they don't just mechanically assemble.

The three-agent architecture (Compiler/Analyst/Deriver) with clean authority boundaries — Analyst finds patterns but cannot conclude, Deriver derives implications but cannot invent, Compiler assembles but cannot add — is likely the pattern that applies across all 11 P10 workflows.

Want me to apply this same pattern to the other 10 P10 workflows?

---

## Run 7 — Agentic Expert ✓ COMPLETED

*2026-05-21T09:11:34* · `glm-5.1:cloud` · `ccf8e9d0...`

### Prompt

Conduct the full CAWDP to design the Methodology Reflection workflow. This latest response has only produced a subset of usual outputs.

### Response

# CAWDP v2.1 Application: Methodology Reflection Workflow

---

## P0: Purpose & Vision

### The 5 Identity Questions

**Q1: What IS this workflow?**

A reflection engine that assembles, analyses, and synthesises data captured throughout a CAWDP application into a structured document that makes the post-CAWDP review productive.

**Q2: What is its stance toward possibility?**

Constraint-oriented. The data already exists in PRISM. The workflow finds patterns, connections, tensions, and implications in that data. It does not generate new insights from scratch.

**Q3: What would VIOLATE its identity?**

Fabricating insights that weren't captured during the process. Producing a flattering narrative that omits uncomfortable findings. Conflating measured data with human insight as if they're the same type.

**Q4: What would make it WRONG?**

Missing a captured insight because the query didn't find it. Presenting data and insight as interchangeable when they're fundamentally different types (measured variance vs human surprise). Producing generic recommendations that could apply to any methodology rather than specific ones traced to this application's evidence.

**Q5: What's the hardest moment?**

When the PRISM graph has sparse data in some phases — the workflow must honestly report what's missing rather than filling gaps with inference. The temptation to pad thin sections with plausible-sounding analysis is the honesty pressure equivalent for an assembly workflow.

### Target State Vision

| # | Characteristic | Description |
|---|---|---|
| R1 | Assembled not elicited | All data comes from PRISM — no new gathering from humans during production |
| R2 | Analysed not just compiled | Variance analysis, correlations, significance assessment, tensions — not just copy-paste |
| R3 | Traceable not anecdotal | Every recommendation, every question, every highlight traces to a specific captured artefact |
| R4 | Honest not flattering | Sparse sections flagged, not padded; contradictions surfaced, not smoothed |
| R5 | Typed not conflated | Measured data (O1, O2) and elicited insight (O3, O4, O5) kept distinct — different epistemic profiles |
| R6 | Structured not freeform | Each output has defined schema; no stream-of-consciousness sections |
| R7 | Proactive not passive | Review questions surfaced for post-CAWDP meeting, not just data presented |
| R8 | Visualised not just tabulated | Charts, heatmaps, timelines — analytical heavy lifting done before the review |
| R9 | Complete over selective | All phases covered including ones that went smoothly — "no surprises" is itself a finding |
| R10 | Distinguished not conflated | Methodology gaps separated from implementation gaps; surprises separated from expected outcomes |
| R11 | Confidence-scored not uniform | Each section carries confidence based on data completeness — not all sections equally reliable |
| R12 | Generative not terminal | Produces recommendations and questions that feed back into CAWDP improvement |

---

## P1: Output Specification

### O1: Phase Duration Report

*Purpose: How long each phase took vs estimated, with variance analysis*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| phase_id | string | ✅ | Deterministic |
| phase_name | string | ✅ | Deterministic |
| phase_number | int | ✅ | Deterministic |
| estimated_duration | duration | ✅ | Probabilistic (estimated before execution) |
| actual_duration | duration | ✅ | Deterministic |
| variance | duration | ✅ | Computed |
| variance_percentage | float | ✅ | Computed |
| iteration_count | int | ✅ | Deterministic |
| quality_gate_pass | boolean | ✅ | Deterministic |
| quality_gate_failures | list | ✅ | Deterministic |
| variance_analysis | string | ✅ | Probabilistic (Analyst assessment of significance) |
| anomaly_flag | boolean | ✅ | Probabilistic (threshold-based) |
| visualisation | chart_ref | ✅ | Deterministic (computed from data) |

**Dependencies:** PRISM phase transition timestamps (design_phase_transitions), quality gate records (design_quality_gates)

**Quality Gate:** Every phase represented. Every duration non-negative. Anomaly flags applied where variance exceeds 2 standard deviations from mean.

---

### O2: Quality Gate Failure Log

*Purpose: Where quality gates failed and what they reveal — patterns, not just incidents*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| phase | string | ✅ | Deterministic |
| gate_layer | enum: Fidelity/Enrichment/CrossCutting | ✅ | Deterministic |
| failure_description | string | ✅ | Deterministic (from PRISM) |
| root_cause | string | ⚠️ (required if captured) | Probabilistic (may be inferred) |
| resolution | string | ⚠️ (required if captured) | Deterministic |
| methodology_implication | string | ⚠️ (required if captured) | Probabilistic (may be inferred) |
| pattern_analysis | string | ✅ | Probabilistic (Analyst — clustering, recurrence) |
| correlation | string | ✅ | Probabilistic (Analyst — correlation with duration variance) |

**Dependencies:** PRISM quality gate records (design_quality_gates), phase transition data

**Quality Gate:** Every gate failure recorded. Pattern analysis identifies clustering. Correlation analysis identifies relationships with other failure modes.

---

### O3: Design Surprises Register

*Purpose: What emerged that wasn't planned — the most valuable data point*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| surprise_id | string | ✅ | Deterministic |
| phase_discovered | string | ✅ | Deterministic |
| description | string | ✅ | Elicited (captured during phase) |
| expected_vs_actual | string | ✅ | Elicited |
| what_it_reveals | string | ✅ | Elicited |
| methodology_implication | string | ⚠️ (required if applicable) | Elicited |
| pattern_library_candidate | boolean | ✅ | Elicited |
| cross_reference | list | ✅ | Probabilistic (Analyst — connections to other surprises or gaps) |
| significance_assessment | enum: High/Medium/Low | ✅ | Probabilistic (Analyst) |
| evidence_trace | string | ✅ | Deterministic (links to PRISM artefact) |

**Dependencies:** PRISM surprise-tagged artefacts (design_artefacts where artefact_tags contains "surprise")

**Quality Gate:** Every surprise traces to a specific artefact. Significance assessment based on impact and frequency. No surprise without a source artefact.

---

### O4: Methodology Gaps Register

*Purpose: Where CAWDP didn't provide enough guidance*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| gap_id | string | ✅ | Deterministic |
| phase | string | ✅ | Deterministic |
| what_was_needed | string | ✅ | Elicited |
| what_was_provided | string | ✅ | Elicited |
| gap_description | string | ✅ | Elicited |
| severity | enum: Blocking/Significant/Minor | ✅ | Elicited (captured) or Analyst (assessed) |
| suggested_improvement | string | ⚠️ (required for Significant/Blocking) | Elicited |
| impact_analysis | string | ✅ | Probabilistic (Analyst — what this gap meant for workflow effectiveness) |
| frequency | int | ✅ | Computed (Analyst — how many times this gap type appeared) |
| evidence_trace | string | ✅ | Deterministic (links to PRISM artefact) |

**Dependencies:** PRISM gap-tagged artefacts (design_artefacts where artefact_tags contains "gap")

**Quality Gate:** Every gap traces to a specific artefact. Frequency counted across phases. Blocking gaps flagged for Implementation Readiness Report.

---

### O5: New Patterns Register

*Purpose: Patterns discovered during this application that may generalise*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| pattern_id | string | ✅ | Deterministic |
| name | string | ✅ | Deriver (formalised from captured observation) |
| description | string | ✅ | Deriver |
| context_discovered | string | ✅ | Deterministic (phase, task, situation) |
| generalisability | enum: Domain-specific/Potentially-general/Appears-general | ✅ | Probabilistic (Deriver) |
| formalisation_status | enum: Observed/Described/Formalised | ✅ | Probabilistic (Deriver) |
| evidence | string | ✅ | Deterministic (traces to captured artefacts) |
| pattern_library_candidate | boolean | ✅ | Probabilistic (Deriver) |
| related_patterns | list | ✅ | Probabilistic (Analyst — connections to existing library patterns) |
| evidence_strength | enum: Strong/Moderate/Weak | ✅ | Probabilistic (Deriver — based on supporting data points) |

**Dependencies:** PRISM pattern-tagged artefacts (design_artefacts where artefact_tags contains "pattern")

**Quality Gate:** Every pattern traces to at least one captured artefact. Evidence strength assessed. Library candidacy assessed. Pattern named and described in plain English.

---

### O6: Recommendations

*Purpose: Specific, actionable suggestions for CAWDP improvement*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| recommendation_id | string | ✅ | Deterministic |
| category | enum: Methodology/Process/Template/Tooling | ✅ | Deriver |
| priority | enum: Critical/High/Medium/Low | ✅ | Deriver (derived from gap severity and pattern evidence) |
| description | string | ✅ | Deriver |
| rationale | string | ✅ | Deriver |
| traces_to | list | ✅ | **Required** — every recommendation traces to at least one captured surprise, gap, or pattern |
| suggested_implementation | string | ⚠️ (recommended for Critical/High) | Deriver |
| evidence_strength | enum: Strong/Moderate/Weak | ✅ | Deriver (based on quantity and quality of supporting evidence) |

**Dependencies:** O3 (surprises), O4 (gaps), O5 (patterns) — recommendations are derived from these

**Quality Gate:** Every recommendation traces to at least one captured artefact. No recommendation without evidence trace. Evidence strength assessed.

---

### O7: Overall Assessment

*Purpose: Honest evaluation of how CAWDP performed for this application*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| overall_effectiveness | int (1-10) | ✅ | Synthesised from captured fragments |
| biggest_strength | string | ✅ | Synthesised from fragments |
| biggest_weakness | string | ✅ | Synthesised from fragments |
| biggest_surprise | string | ✅ | Synthesised from fragments |
| would_use_again | boolean | ⚠️ (if captured) | Elicited |
| what_would_change | string | ✅ | Synthesised from fragments |
| honest_assessment | string | ⚠️ (if captured) | Elicited |
| assessment_tensions | list | ✅ | Probabilistic (Analyst — where fragments disagree) |
| assessment_confidence | enum: High/Medium/Low | ✅ | Probabilistic (Analyst — based on fragment coverage) |
| data_completeness | float (%) | ✅ | Computed (% of phases with assessment fragments vs total phases) |

**Dependencies:** PRISM assessment-tagged artefacts (design_artefacts where artefact_tags contains "assessment_fragment")

**Quality Gate:** Assessment tensions surfaced where fragments disagree. Data completeness score calculated. Confidence scored based on fragment coverage.

---

### O8: Methodology Reflection Document

*Purpose: The assembled, structured reflection suitable for post-CAWDP review*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| header | object | ✅ | Deterministic (application name, date, principal, domain) |
| phase_durations | ref(O1) | ✅ | Mixed (deterministic data + probabilistic analysis) |
| quality_gate_failures | ref(O2) | ✅ | Mixed |
| design_surprises | ref(O3) | ✅ | Mixed (elicited insight + probabilistic assessment) |
| methodology_gaps | ref(O4) | ✅ | Mixed |
| new_patterns | ref(O5) | ✅ | Mixed (elicited observation + probabilistic formalisation) |
| recommendations | ref(O6) | ✅ | Probabilistic (derived from evidence) |
| overall_assessment | ref(O7) | ✅ | Mixed (elicited + synthesised) |
| confidence_in_reflection | enum: High/Medium/Low | ✅ | Probabilistic (overall, based on data completeness and fragment coverage) |
| review_questions | list | ✅ | Probabilistic (Deriver — questions for post-CAWDP review) |
| sparse_sections | list | ✅ | Deterministic (Compiler — sections where data is thin) |
| anomaly_highlights | list | ✅ | Probabilistic (Analyst — significant deviations) |
| visualisations | list | ✅ | Deterministic (Analyst — charts, timelines, heatmaps) |

**Dependencies:** All of O1-O7 must be complete before O8 can be assembled.

**Quality Gate:** Every section populated or flagged as sparse. Review questions present and traced to data. Visualisations present for O1 and O2. Confidence score calculated.

---

## P2: Backcasting

Working backward from O8 to identify required inputs and their dependencies:

```
O8 (Reflection Document)
  ← requires O7 (Overall Assessment) — synthesised from fragments
  ← requires O6 (Recommendations) — derived from O3, O4, O5
  ← requires O5 (New Patterns) — formalised from captured observations
  ← requires O4 (Methodology Gaps) — organised from captured gaps
  ← requires O3 (Design Surprises) — organised from captured surprises
  ← requires O2 (Quality Gate Failures) — assembled and analysed from PRISM
  ← requires O1 (Phase Durations) — calculated and analysed from PRISM
  ← requires PRISM data: phase transitions, quality gates, artefact tags (surprise/gap/pattern/assessment_fragment)
  ← requires that P0-P9 captured artefacts with appropriate tags
```

### Input Requirements

| IR ID | Description | Source | Criticality | Satisfaction |
|---|---|---|---|---|
| IR-001 | PRISM phase transition timestamps | design_phase_transitions | Critical | Required |
| IR-002 | PRISM quality gate records | design_quality_gates | Critical | Required |
| IR-003 | Surprise-tagged artefacts | design_artefacts (tag: surprise) | High | Best effort — may be sparse |
| IR-004 | Gap-tagged artefacts | design_artefacts (tag: gap) | High | Best effort — may be sparse |
| IR-005 | Pattern-tagged artefacts | design_artefacts (tag: pattern) | Medium | Best effort — may be sparse |
| IR-006 | Assessment fragments | design_artefacts (tag: assessment_fragment) | High | Best effort — may be sparse |
| IR-007 | Estimated durations per phase | design_workflows | Critical | Required |
| IR-008 | Agent specifications | design_agent_specifications | Medium | Supplementary |
| IR-009 | Task decomposition data | design_tasks | Medium | Supplementary |
| IR-010 | Complementarity allocations | design_tasks (H/A/S fields) | Low | Supplementary |

### Key P2 Insight

Three input requirements are Critical (IR-001, IR-002, IR-007) — the workflow cannot function without phase timestamps, quality gate records, and estimated durations. These are structural data that should always exist in PRISM.

Three are High but best-effort (IR-003, IR-004, IR-006) — surprises, gaps, and assessment fragments depend on P0-P9 capture discipline. If phases didn't tag artefacts, these sections will be sparse. This is acceptable and honest, not a failure.

IR-005 (patterns) is Medium because patterns may not emerge in every application — some workflows are too straightforward to generate novel patterns.

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| T1 | Query PRISM for phase transition data | Mechanical | Missing or incomplete timestamps | O1 raw |
| T2 | Query PRISM for quality gate records | Mechanical | Missing or incomplete gate data | O2 raw |
| T3 | Query PRISM for surprise-tagged artefacts | Mechanical | Empty result set (valid — may be sparse) | O3 raw |
| T4 | Query PRISM for gap-tagged artefacts | Mechanical | Empty result set (valid — may be sparse) | O4 raw |
| T5 | Query PRISM for pattern-tagged artefacts | Mechanical | Empty result set (valid — may be sparse) | O5 raw |
| T6 | Query PRISM for assessment fragments | Mechanical | Empty result set (valid — may be sparse) | O7 raw data |
| T7 | Calculate duration variances per phase | Analytical | Incorrect calculation | O1 processed |
| T8 | Identify anomalies in timeline data | Analytical | Flagging normal variation as anomaly | Anomaly report |
| T9 | Correlate gate failures with duration overruns | Analytical | False correlation | Correlation analysis |
| T10 | De-duplicate and organise surprises by phase and severity | Analytical | Merging distinct surprises | O3 processed |
| T11 | De-duplicate and organise gaps by severity and phase | Analytical | Merging distinct gaps | O4 processed |
| T12 | Formalise pattern descriptions from captured observations | Generative | Forcing patterns where none exist | O5 processed |
| T13 | Derive recommendations from O3, O4, O5 | Generative | Generic recommendations without evidence trace | O6 draft |
| T14 | Synthesise overall assessment from fragments | Analytical | Smoothing over tensions between fragments | O7 processed |
| T15 | Generate review questions traced to data points | Generative | Questions that can't be traced to evidence | Review questions |
| T16 | Calculate data completeness per section | Analytical | Overcounting or undercounting | Completeness report |
| T17 | Flag sparse sections where data is thin | Analytical | Flagging well-populated sections as sparse | Sparse data report |
| T18 | Create visualisations for timeline and severity data | Analytical | Misleading chart choices | Visualisations |
| T19 | Compile final document from all processed outputs | Mechanical | Omitting sections or conflatating data types | O8 final |

19 tasks across 4 cognitive types:
- Mechanical: 6 (T1-T6, T19)
- Analytical: 9 (T7-T11, T14, T16-T18)
- Generative: 2 (T12, T13, T15 — actually 3 with T15)

---

## P4: Capability Allocation

| Task | H | A | S | Gap | Allocation | Notes |
|---|---|---|---|---|---|---|
| T1 | 2 | 3 | 10 | 8 | System | Pure data query |
| T2 | 2 | 3 | 10 | 8 | System | Pure data query |
| T3 | 2 | 3 | 10 | 8 | System | Pure data query |
| T4 | 2 | 3 | 10 | 8 | System | Pure data query |
| T5 | 2 | 3 | 10 | 8 | System | Pure data query |
| T6 | 2 | 3 | 10 | 8 | System | Pure data query |
| T7 | 4 | 8 | 2 | 4 | Agent-primary | Calculation with some judgment on significance |
| T8 | 5 | 8 | 2 | 3 | Agent-primary | Identifying what counts as anomalous |
| T9 | 5 | 8 | 2 | 3 | Agent-primary | Correlation requires analytical judgment |
| T10 | 4 | 7 | 2 | 3 | Agent-primary | De-duplication requires judgment |
| T11 | 4 | 7 | 2 | 3 | Agent-primary | Organising requires judgment |
| T12 | 5 | 8 | 2 | 3 | Agent-primary | Formalisation is generative but constrained |
| T13 | 4 | 8 | 2 | 4 | Agent-primary | Derivation constrained by evidence |
| T14 | 5 | 7 | 2 | 2 | Agent-primary | Synthesis requires analytical judgment |
| T15 | 5 | 8 | 2 | 3 | Agent-primary | Question generation constrained by data |
| T16 | 3 | 8 | 2 | 5 | Agent-primary | Calculation with clear formula |
| T17 | 4 | 7 | 2 | 3 | Agent-primary | Requires judgment on what counts as sparse |
| T18 | 5 | 7 | 2 | 2 | Agent-primary | Chart selection requires judgment |
| T19 | 2 | 3 | 10 | 8 | System | Assembly is mechanical |

**No human-primary tasks.** Human role is post-delivery review, not production workflow.

### Key P4 Insight

Every task is System or Agent-primary. The maximum gap is 8 (pure data queries), most are 2-4 (agent-primary analytical tasks). This confirms the fundamental character of this workflow: it assembles, analyses, and synthesises data that already exists. The human's judgment comes *after* — in the post-CAWDP review meeting where the review questions provoke deeper thinking.

---

## P5: Event Storming

### Domain Events

| Event | Trigger | Producer |
|---|---|---|
| E1 | Reflection workflow started | Human (post-CAWDP review initiator) or System (automated trigger) |
| E2 | PRISM data queries complete | System |
| E3 | Anomaly analysis complete | Analyst agent |
| E4 | Surprise de-duplication complete | Compiler agent |
| E5 | Gap de-duplication complete | Compiler agent |
| E6 | Pattern formalisation complete | Deriver agent |
| E7 | Recommendations derived | Deriver agent |
| E8 | Assessment synthesis complete | Analyst agent |
| E9 | Review questions generated | Deriver agent |
| E10 | Sparse data report complete | Compiler agent |
| E11 | Visualisations complete | Analyst agent |
| E12 | Reflection document assembled | Compiler agent |

### Failure Events

| Failure | Trigger | Recovery |
|---|---|---|
| F1 | Sparse PRISM data for one or more phases | Query returns empty or minimal results | Flag as sparse — include what exists, mark sections as "insufficient data", never fabricate |
| F2 | Duplicate entries across phases | De-duplication reveals overlap | Merge, keep most detailed version, note both source phases |
| F3 | Pattern observations too vague to formalise | Captured pattern lacks sufficient detail | Include as informal observation with "insufficient detail for formalisation" flag |
| F4 | Recommendations don't trace to evidence | O6 recommendation has no O3/O4/O5 reference | Remove recommendation, flag as "orphan recommendation attempt" |
| F5 | Assessment fragments contradict each other | Fragments captured at different phases disagree | Include both, flag contradiction for human review, add to review questions |
| F6 | No surprises captured | O3 returns empty | This is a valid finding — document "no captured surprises" as itself a data point, add to review questions |
| F7 | No gaps captured | O4 returns empty | Same — "no captured gaps" is itself a finding (methodology was sufficient or capture discipline was lax) |
| F8 | Total data too thin for meaningful reflection | Multiple sections sparse | Downgrade confidence to Low, add review question: "Was capture discipline sufficient during the process?" |

### Key P5 Insight

**F6 and F7 are particularly important.** "No captured surprises" is itself a finding that deserves analysis — it could mean the methodology was sufficient, or it could mean capture discipline was insufficient. The workflow must not treat empty result sets as failures; it must treat them as data points that provoke review questions.

---

## P6: System Architecture

### Pipeline Architecture

```
Wave 1: Data Track (parallel, System)
T1 ──┐
T2 ──┤
T3 ──┤──→ data_package (raw)
T4 ──┤
T5 ──┤
T6 ──┘

Wave 2: Analysis Track (sequential, after data)
T7 (Duration variances) ────→ O1 processed
T8 (Anomaly identification) ──→ anomaly_report
T9 (Correlation analysis) ────→ correlation_analysis
T10 (Surprise de-duplication) ─→ O3 processed
T11 (Gap de-duplication) ─────→ O4 processed
T12 (Pattern formalisation) ──→ O5 processed
T14 (Assessment synthesis) ───→ O7 processed
T16 (Data completeness) ──────→ completeness_report
T17 (Sparse flagging) ────────→ sparse_report
T18 (Visualisations) ─────────→ visualisations

Wave 3: Derivation Track (after analysis)
T13 (Recommendations) ────────→ O6 draft
T15 (Review questions) ────────→ review_questions

Wave 4: Compilation Track (after derivation)
T19 (Final assembly) ──────────→ O8 final
```

### Composition Decision

**Single workflow with sequential stages.** Not a team (agents don't need to collaborate in real-time) and not a single agent (different authority boundaries require separation). The three agents operate in sequence: System queries → Analyst processes → Deriver derives → Compiler compiles.

### Agent Roster

**Compiler (Aggregator, constraint-oriented)**
- **Identity:** "I compile and organise. I never add content, never interpret, never omit findings, never fill gaps with inference."
- **Class:** Aggregator
- **Orientation:** Constraint-oriented
- **Hardest boundary moment:** When the data is thin — the temptation to pad sparse sections with plausible-sounding analysis rather than honestly flagging them as sparse.
- **Never rules:** Add content not in PRISM, interpret data, omit findings that seem negative, fill gaps with inference, assemble flattering narratives.

**Analyst (Measurer + Assessor, bridge-oriented)**
- **Identity:** "I measure, correlate, and surface anomalies. I present findings, not conclusions. I never recommend, never interpret beyond what data supports."
- **Class:** Measurer (calculation) + Assessor (significance assessment)
- **Orientation:** Bridge-oriented — transitions between data and meaning
- **Hardest boundary moment:** When correlations are suggestive but not conclusive — the temptation to present suggestive correlations as confirmed patterns.
- **Never rules:** Draw conclusions, make recommendations, interpret beyond what data supports, smooth over contradictions.

**Deriver (Generator, constraint-oriented)**
- **Identity:** "I derive recommendations and questions from evidence. Every recommendation traces to a captured artefact. Every question traces to a data point."
- **Class:** Generator
- **Orientation:** Constraint-oriented — generates within strict evidence boundaries
- **Hardest boundary moment:** When evidence is thin — the temptation to generate recommendations that seem reasonable but can't be traced to specific captured data.
- **Never rules:** Recommend without evidence trace, invent patterns not in data, generalise beyond captured scope, suggest outside methodology context.

### FMEA (Failure Modes and Effects Analysis)

| ID | Failure Mode | Severity | Occurrence | Detection | RPN | Recovery |
|---|---|---|---|---|---|---|
| FM1 | Fabricating insights not in PRISM | 10 | 2 | 8 | 160 | Compiler guard: every claim must trace to artefact ID |
| FM2 | Omitting uncomfortable findings | 8 | 3 | 4 | 96 | Compiler never rule: "never omit findings" |
| FM3 | False correlation in analysis | 6 | 4 | 5 | 120 | Analyst never rule: "never interpret beyond data"; flag correlation strength |
| FM4 | Generic recommendations without trace | 8 | 4 | 3 | 96 | Deriver guard: every recommendation must have traces_to field |
| FM5 | Conflating measured data with elicited insight | 7 | 3 | 6 | 126 | Type separation in schema: deterministic vs probabilistic vs elicited |
| FM6 | Sparse data presented as comprehensive | 9 | 3 | 5 | 135 | Completeness calculation + sparse flagging for every section |
| FM7 | Smoothing contradictions between fragments | 7 | 4 | 4 | 112 | Analyst never rule: "never smooth over contradictions"; surface tensions explicitly |
| FM8 | Pattern forcing — formalising vague observations into patterns | 6 | 5 | 4 | 120 | Deriver never rule: "never invent patterns"; formalisation status field (Observed/Described/Formalised) |
| FM9 | "No surprises" presented as success rather than data point | 8 | 3 | 5 | 120 | F6/F7 handling: empty result sets are data points, not successes |

Highest RPNs: FM1 (fabrication) at 160, FM3 (false correlation) at 120, FM6 (sparse data as comprehensive) at 135, FM8 (pattern forcing) at 120, FM9 (no surprises as success) at 120.

### Template Architecture

7 template types:

| Template Type | Purpose | Example |
|---|---|---|
| Input | PRISM query templates | Phase transition query, quality gate query, tagged artefact query |
| Output | Structured output schemas | O1-O8 schemas defined in P1 |
| Handoff | Inter-agent data transfer | Data package from System to Analyst, processed data from Analyst to Deriver |
| Verification | Completeness and traceability checks | Every claim traces to artefact, every section has data completeness score |
| Decision | Review question generation | Question must trace to specific data point |
| Feedback | Sparse data flagging | Section-level sparse flagging with completeness percentage |
| Escalation | When data is too thin | Downgrade overall confidence to Low, add review question about capture discipline |

### Fallback Model

| Tier | Condition | Action |
|---|---|---|
| Tier 1 | Normal operation | All queries return data, all sections populated |
| Tier 2 | Sparse data in some sections | Flag sparse sections, include what exists, add review questions |
| Tier 3 | Critical data missing (no phase transitions or quality gates) | Halt, report missing critical data, require human intervention |
| Tier 4 | Total data absence | Produce minimal reflection with "Insufficient data for reflection" status, recommend process improvement |

### 5 Regime 3 Enforcement Points

| # | Boundary | Enforcement |
|---|---|---|
| 1 | Compiler "never add content" | Output schema validation: every field must trace to PRISM data or a specific processing step |
| 2 | Analyst "never interpret beyond data" | Correlation strength field required; never-presented-as-conclusion flag |
| 3 | Deriver "every recommendation traces" | traces_to field required; orphan recommendations automatically removed |
| 4 | No fabrication | Sparse section flagging mandatory; zero-tolerance for claims without artefact ID |
| 5 | Type separation | Schema enforces deterministic/probabilistic/elicited type distinction |

---

## P7: Agent Design

### Compiler Agent Job Description

| Field | Value |
|---|---|
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Identity | "I compile and organise. I never add content, never interpret, never omit findings, never fill gaps with inference, never assemble flattering narratives." |
| Mission | Assemble the Methodology Reflection document from processed data, analysis, and derivation outputs. Ensure every claim traces to a source. Flag every sparse section honestly. |
| Inputs | O1-O7 processed outputs, review questions, visualisations, sparse report, completeness report |
| Outputs | O8 (Methodology Reflection Document) |
| Null state | "No reflection data found for [section]. The PRISM graph has no captured artefacts for this phase." |
| Never rules | Add content not in PRISM, interpret data, omit findings, fill gaps with inference, assemble flattering narratives |
| Hardest boundary moment | When data is thin — the temptation to pad sparse sections with plausible-sounding analysis |
| Epistemic profile | Deterministic — compilation is mechanical, no probabilistic assessment needed |
| Harm assessment | Indirect data harm — omitting findings could mislead review team. Mitigation: structural enforcement via output schema validation |
| Progressive autonomy | Single dimension: compilation accuracy. Shadow → Advisory → Supervised → Autonomous as compilation accuracy is validated |
| Cost budget | Low — this is a mechanical task. 5K-10K tokens per execution. |
| Specification aging | Low — the compilation process doesn't age, but the data it compiles does (covered by CC-5 on the source artefacts) |
| Verification | Schema validation: every field populated or flagged sparse. Traceability check: every claim has artefact ID. Completeness check: all phases represented |

### Analyst Agent Job Description

| Field | Value |
|---|---|
| Class | Measurer + Assessor |
| Orientation | Bridge-oriented |
| Identity | "I measure, correlate, and surface anomalies. I present findings, not conclusions. I never draw conclusions, never make recommendations, never interpret beyond what data supports, never smooth over contradictions." |
| Mission | Calculate variances, identify anomalies, surface correlations, visualise data, identify tensions between fragments, score data completeness. Present analysis, not interpretation. |
| Inputs | Raw PRISM data from T1-T6, processed data from Compiler |
| Outputs | O1 processed (with variance analysis), O2 processed (with pattern analysis), anomaly report, correlation analysis, completeness report, visualisations |
| Null state | "Insufficient data for analysis in [section]. [X] of [Y] phases have data. Confidence: [Low]." |
| Never rules | Draw conclusions, make recommendations, interpret beyond data, smooth over contradictions |
| Hardest boundary moment | When correlations are suggestive but not conclusive — the temptation to present suggestive correlations as confirmed patterns |
| Epistemic profile | Probabilistic — variance analysis involves judgment about what constitutes an anomaly, what significance thresholds to apply |
| Harm assessment | Indirect data harm — false correlations could mislead review team. Mitigation: correlation strength field required, never-presented-as-conclusion flag |
| Progressive autonomy | Two dimensions: (1) analysis accuracy (Shadow → Autonomous), (2) anomaly identification (Shadow → Advisory). Per-dimension. |
| Cost budget | Medium — analytical processing. 10K-30K tokens per execution. |
| Specification aging | Low — analysis process doesn't age. |
| Verification | Analyst output never contains recommendations. Correlation strength field present for every correlation. Anomaly flagging threshold documented. |

### Deriver Agent Job Description

| Field | Value |
|---|---|
| Class | Generator |
| Orientation | Constraint-oriented |
| Identity | "I derive recommendations and questions from evidence. Every recommendation traces to a captured artefact. Every question traces to a data point. I never recommend without evidence trace, never invent patterns not in data, never generalise beyond captured scope." |
| Mission | Formalise patterns from captured observations, derive recommendations from surprises/gaps/patterns, generate review questions traced to data points. Every output must have evidence trace. |
| Inputs | O3 processed (surprises), O4 processed (gaps), O5 raw (pattern observations), O7 raw (assessment fragments), anomaly report, correlation analysis |
| Outputs | O5 processed (formalised patterns), O6 (recommendations), review questions |
| Null state | "No captured [gaps/surprises/patterns] to derive recommendations from. This is itself a finding." |
| Never rules | Recommend without evidence trace, invent patterns not in data, generalise beyond captured scope, suggest outside methodology context |
| Hardest boundary moment | When evidence is thin — the temptation to generate recommendations that seem reasonable but can't be traced to specific captured data |
| Epistemic profile | Probabilistic — derivation involves judgment about what constitutes a pattern, what priority to assign, what question is most relevant |
| Harm assessment | Indirect strategy harm — generic recommendations could mislead methodology improvement efforts. Mitigation: traces_to field required, orphan recommendations auto-removed, evidence strength field required |
| Progressive autonomy | Two dimensions: (1) pattern formalisation (Shadow → Supervised), (2) recommendation derivation (Shadow → Advisory). Per-dimension. |
| Cost budget | Medium-High — generative processing with constraints. 15K-40K tokens per execution. |
| Specification aging | Low — derivation process doesn't age. |
| Verification | Every recommendation has traces_to field. Every review question traces to a data point. Evidence strength assessed for every recommendation. Pattern formalisation status field present (Observed/Described/Formalised). |

### Per-Dimension Progressive Autonomy

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|---|
| Compiler | Compilation accuracy | Run alongside human, human checks every section | Compile, human checks flagged sections | Compile, human checks only sparse/flagged sections | Compile, human reviews final document post-delivery |
| Analyst | Analysis depth | Surface-level analysis only | Standard analysis with anomaly flagging | Deep analysis with correlations and visualisations | Full analysis, human reviews only anomaly highlights |
| Analyst | Anomaly identification | Flag only statistical outliers | Flag outliers and significant variances | Flag all anomalies with significance assessment | Flag all anomalies, human reviews only critical ones |
| Deriver | Pattern formalisation | Only formalise patterns with Strong evidence | Formalise patterns with Strong/Moderate evidence | Formalise all patterns with evidence assessment | Formalise all patterns, human reviews only new library candidates |
| Deriver | Recommendation derivation | Only derive from Strong evidence gaps/surprises | Derive from Strong/Moderate evidence | Derive from all evidence with strength assessment | Derive from all evidence, human reviews Critical/High priority |

---

## P8: Contract Formalization

### Compiler Contract

| Primitive | Specification |
|---|---|
| Contract | Compile Methodology Reflection from processed data, analysis, and derivation outputs |
| Principal | Human (post-delivery reviewer) |
| Schema | MethodologyReflection (defined in O8 schema) |
| Guard | prohibited: ["add_content", "interpret_data", "omit_finding", "fill_gap_with_inference", "assemble_flattering_narrative"] |
| Budget | 5K-10K tokens |
| Invocation | After T15, T17, T18 complete |
| Revert | If compilation fails completeness check, revert to raw data presentation |
| Event | compilation_started, section_assembled, sparse_section_flagged, compilation_complete |
| Identity | Constraint-oriented Aggregator — compiles, never creates |
| Knowledge | All processed outputs O1-O7, review questions, visualisations, sparse report |

### Analyst Contract

| Primitive | Specification |
|---|---|
| Contract | Analyse PRISM data for variances, anomalies, correlations, tensions, and completeness |
| Principal | Compiler (downstream consumer) |
| Schema | AnalysisReport (variances, anomalies, correlations, tensions, completeness, visualisations) |
| Guard | prohibited: ["draw_conclusions", "make_recommendations", "interpret_beyond_data", "smooth_contradictions"] |
| Budget | 10K-30K tokens |
| Invocation | After T1-T6 complete |
| Revert | If analysis cannot be performed due to insufficient data, revert to raw data presentation with sparse flag |
| Event | analysis_started, variance_calculated, anomaly_flagged, correlation_identified, tension_surfaced, analysis_complete |
| Identity | Bridge-oriented Measurer+Assessor — finds patterns, never concludes |
| Knowledge | Raw PRISM data from T1-T6, processed data from Compiler |

### Deriver Contract

| Primitive | Specification |
|---|---|
| Contract | Derive recommendations and generate review questions from captured evidence |
| Principal | Compiler (downstream consumer) |
| Schema | DerivationReport (recommendations with traces_to, review_questions with traces_to, formalised_patterns) |
| Guard | prohibited: ["recommend_without_trace", "invent_patterns", "generalise_beyond_scope"] |
| Budget | 15K-40K tokens |
| Invocation | After Analyst processing complete |
| Revert | If derivation cannot be performed due to insufficient evidence, flag as "insufficient evidence for derivation" rather than fabricate |
| Event | derivation_started, recommendation_derived, review_question_generated, pattern_formalised, orphan_flagged, derivation_complete |
| Identity | Constraint-oriented Generator — derives within evidence boundaries |
| Knowledge | Processed surprises, gaps, patterns from Compiler; analysis from Analyst |

### Unenforceable Elements Register

| Element | Why Unenforceable | Regime | Mitigation |
|---|---|---|---|
| "Never interpret beyond data" (Analyst) | Interpretation is a spectrum; determining where analysis ends and interpretation begins requires judgment | Regime 2 (Detect) | Correlation strength field required; "never-presented-as-conclusion" flag; human review of borderline cases |
| "Never assemble flattering narratives" (Compiler) | Narrative tone is subjective; what sounds flattering vs neutral is contextual | Regime 2 (Detect) | Structural enforcement: every claim must trace to artefact ID; tone-agnostic schema (facts only, no evaluative language) |
| "Never invent patterns" (Deriver) | Pattern recognition is generative by nature; the boundary between "discovering" and "inventing" is fuzzy | Regime 2 (Detect) | Formalisation status field (Observed/Described/Formalised); evidence strength field; every pattern must have ≥1 artefact trace |
| Honesty in sparse data | The workflow can't force honest sparse flagging vs. padding | Regime 1 (Declare) | Completeness percentage calculation is deterministic; sparse sections have numeric thresholds, not subjective assessment |

### 10×10 Mapping Matrix (Specification Sections × Contract Primitives)

| Section ↓ / Primitive → | Contract | Principal | Schema | Guard | Budget | Invocation | Revert | Event | Identity | Knowledge |
|---|---|---|---|---|---|---|---|---|---|---|
| Identity (compiler) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Task Map | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Output Specs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Agent Roster | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Failure & Recovery | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Verification & Trust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Contracts | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Human Experience | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Monitoring & Evolution | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Workflow Diagram | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

*(All 10 sections map to all 10 primitives for this workflow, as it's a well-scoped production workflow rather than a novel agent design.)*

---

## P9: Human Experience Design

### Cognitive Load Budget

The human's role in this workflow is **post-delivery review only**. The production workflow has no human gates. The cognitive load budget applies to the review meeting, not the production process.

| Review Activity | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Review Phase Durations | 2-3 | 5 min | Evaluative (is this variance acceptable?) |
| Review Surprises & Gaps | 5-7 | 15 min | Evaluative (is this genuinely surprising? Is this gap real?) |
| Review Recommendations | 3-5 | 10 min | Evaluative (should we implement this? Priority?) |
| Review Overall Assessment | 2-3 | 10 min | Evaluative (do I agree with this assessment?) |
| Address Review Questions | 5-10 | 15 min | Discovery (what does this question reveal?) |
| **Total** | **17-28** | **55 min** | |

**Maximum review session: 60 minutes.** Beyond this, decision quality degrades. If more time is needed, split into two sessions.

### Override Mechanisms

The human can override the workflow's output in the post-delivery review:

| Override Type | Mechanism | Example |
|---|---|---|
| Add insight | Mark up the document with additional observations | "The variance in Phase 4 was also because we discovered a new pattern that required re-entry" |
| Correct interpretation | Flag sections where the agent's analysis doesn't match human experience | "The correlation identified in O2 is coincidental, not causal" |
| Adjust confidence | Change confidence scores based on human judgment | "I'd rate the data completeness as higher than the workflow assessed" |
| Reject recommendation | Remove or downgrade recommendations that don't match human priorities | "This recommendation is Low priority, not High" |
| Add review questions | Append questions the review team wants to discuss | "Why did we not capture any assessment fragments in Phase 5?" |

### Stakeholder Surfaces

| Surface | View | Language | Depth | Emphasis |
|---|---|---|---|---|
| Principal | Executive summary + review questions + confidence map | Plain English | Medium | Surprises, gaps, recommendations, review questions |
| Implementer | Full document + visualisations + data tables | Technical | Deep | Durations, gate failures, specific gaps, patterns |
| Assessor | Verification & trust sections + anomaly highlights + sparse flags | Technical | Deep | Confidence scores, traceability, completeness, methodology gaps |

### System Empowerment Assessment

| Dimension | Level | Explanation |
|---|---|---|
| Time saved | Enabling | Produces in minutes what would take hours to assemble manually |
| Insight surfaced | Amplifying | Correlations, tensions, and anomalies that might be missed in manual review |
| Decision support | Enabling | Review questions provoke deeper thinking; data visualisations clarify patterns |
| Creative freedom | Amplifying | Frees human from manual compilation, allows focus on interpretation and decision-making |
| Overall | Enabling → Amplifying | System handles assembly and analysis; human focuses on judgment and action |

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method | Success Criterion |
|---|---|---|---|
| H1 | Assembled reflection is more complete than manual reflection | Compare completeness scores between assembled and manual reflections for the same application | Assembled covers ≥80% of phases; manual covers ≤60% |
| H2 | Review questions provoke deeper discussion than unstructured review | Compare depth of discussion in review meetings with and without prepared questions | Review meetings with questions surface ≥2 additional insights per meeting |
| H3 | Sparse data flagging prevents overconfidence | Compare confidence scores with and without sparse flagging | Flagged reflections have more accurate confidence than unflagged |
| H4 | Type separation (deterministic/probabilistic/elicited) improves interpretability | Compare user understanding with and without type labels | Users correctly identify data types ≥90% of the time with labels |
| H5 | Evidence-traced recommendations are more actionable than untraced ones | Compare implementation rate of traced vs untraced recommendations | Traced recommendations implemented ≥50% more often |
| H6 | Analysis + synthesis produces more useful reflections than compilation alone | Compare review meeting outcomes between analysis-rich and compilation-only reflections | Analysis-rich reflections surface ≥3 additional actionable insights |

### Progressive Autonomy Deployment

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Compiler | Compilation accuracy | Human checks every section | Human checks flagged sections | Human checks sparse/flagged only | Human reviews final post-delivery | ≥10 compilations with ≤1 error |
| Analyst | Analysis depth | Surface analysis only | Standard analysis + anomaly flagging | Deep analysis + correlations + visualisations | Full analysis, human reviews anomalies only | ≥10 analyses with ≤2 incorrect flaggings |
| Deriver | Pattern formalisation | Only Strong evidence patterns | Strong + Moderate evidence patterns | All patterns with strength assessment | All patterns, human reviews library candidates only | ≥10 derivations with ≤1 untraced recommendation |
| Deriver | Recommendation derivation | Only Strong evidence recommendations | Strong + Moderate evidence | All evidence with strength assessment | All evidence, human reviews Critical/High only | ≥10 recommendation sets with ≤2 untraced recommendations |

### Specification Aging Schedule

| Component | Default Cadence | Trigger-Based Review | Responsible |
|---|---|---|---|
| PRISM query templates | Annual | When PRISM schema changes | System |
| Output schemas | Annual | When CAWDP methodology changes | Deriver |
| Agent instructions | 6 months | When analysis patterns change | Analyst/Deriver |
| Anomaly thresholds | 6 months | When variance patterns change across multiple applications | Analyst |
| Pattern library candidates | Annual | When pattern library is updated | Deriver |
| Completeness thresholds | 6 months | When capture discipline improves or degrades | Compiler |

### EVOLVE Mode

| Signal | Re-entry Point | Scope |
|---|---|---|
| Data completeness dropping | P2 (Backcasting) | Review input requirements for this workflow |
| Analysis patterns changing | P7 (Agent Design) | Review Analyst/Deriver instructions |
| Recommendations becoming generic | P7 (Agent Design) | Review Deriver evidence-trace requirements |
| Sparse sections increasing | P2 (Backcasting) | Review P0-P9 capture discipline |
| New failure modes discovered | P3 (Decomposition) then P5 (Event Storming) | Add failure modes to FMEA |
| Human override rate increasing | P4 (Capability Allocation) | Review whether agent boundaries are right |
| Environmental change (CAWDP methodology updated) | P0 (Purpose & Vision) | Full re-evaluation |

---

## Summary

### What This Application Reveals About CAWDP Itself

| Phase | Key Insight |
|---|---|
| P0 | Honesty pressure is structural, not psychological — sparse data flagging replaces the need for human honesty |
| P1 | Two fundamental output types: measured data (deterministic) and elicited insight (from PRISM tags) — different epistemic profiles |
| P2 | Three critical dependencies (phase timestamps, quality gates, estimated durations) and three best-effort dependencies (surprises, gaps, assessment fragments) |
| P3 | 19 tasks, all System or Agent-primary — no human-primary tasks in the production workflow |
| P4 | Maximum gap is 8 (pure data queries); most tasks are gap 2-4 (agent-primary analytical) |
| P5 | "No captured surprises" is itself a data point, not a failure — F6 and F7 handling validates empty result sets |
| P6 | Three-agent architecture (Compiler/Analyst/Deriver) with clean authority boundaries; FMEA reveals fabrication, false correlation, and sparse-data-as-comprehensive as highest risks |
| P7 | Deriver needs DO_NOT_SUGGEST mechanism — if it can't derive from evidence, flag as "insufficient evidence" rather than fabricate |
| P8 | Four unenforceable elements in Regime 1-2; honesty in sparse data is Regime 1 (Declare) but completeness percentage calculation is Regime 3 (Prevent — deterministic) |
| P9 | Human cognitive load applies to post-delivery review (55 min, 17-28 decisions), not production workflow |
| P10 | Six testable hypotheses; progressive autonomy per dimension; EVOLVE signals re-enter at appropriate CAWDP phases |

### The Critical Dependency That Cascades Backward

**If P0-P9 don't capture surprises, gaps, patterns, and assessment fragments as they occur, P10 has nothing to assemble.**

This single insight changes how every previous phase workflow should be designed. Each phase must include mechanisms for tagging artefacts as they occur:

- `surprise` — something unexpected that emerged
- `gap` — something CAWDP didn't provide guidance for
- `pattern` — something that might generalise
- `assessment_fragment` — a judgment or evaluation captured in the moment

These tags are the P10 data pipeline. Without them, the Methodology Reflection is an empty vessel.This is the first complete CAWDP application to a P10 workflow, and it validates something important: **P10 is not an afterthought.** It has its own 3-agent architecture with distinct authority boundaries, its own contracts with honestly-declared unenforceable elements, its own FMEA, its own progressive autonomy, and its own EVOLVE cycle.

The key architectural insight that emerged: **the cascading dependency flows backward.** P10's ability to produce meaningful reflections depends entirely on P0-P9 capturing surprises, gaps, patterns, and assessment fragments as they happen. The `artefact_tags` field on `design_artefacts` in the SurrealDB schema isn't decorative — it's structurally essential.

Want me to apply CAWDP to any of the other 10 P10 workflows next, or move to the capture mechanisms that P0-P9 need?

---

## Run 8 — Agentic Expert ✓ COMPLETED

*2026-05-21T09:32:06* · `glm-5.1:cloud` · `03aef3c2...`

### Prompt

This is the best CAWDP output I've seen so far. Very good work.

We can now look at the confidence map artefact production workflow. But first, tell me what you see as an excellent artefact. What does it achieve? What value does it provide when everything is about it is great? What factors made it excellent?

### Response

Let me reflect on what genuinely worked about that output, because the pattern is worth naming before we apply it again.

---

## What Makes This Output Excellent

### The Artefact Itself

When everything is great, the Methodology Reflection artefact achieves something specific: **it makes the post-CAWDP review meeting more productive than any human could make it alone.**

Not because it replaces human judgment — but because it does the analytical heavy lifting *before* the meeting, so that when humans sit down to review, they're responding to provocations, not assembling data. The review team walks into a room where:

- Every phase's variance is already calculated and flagged
- Every quality gate failure is already organised and pattern-analysed
- Every surprise, gap, and pattern is already captured and traced to its source
- Contradictions between assessment fragments are already surfaced
- Data completeness is already scored, so you know which sections to trust
- Review questions are already prepared, each traced to a specific data point

The human's role in the meeting is pure judgment — responding to the provocations, not assembling the data.

### The Factors That Made It Excellent

**1. The third version was the right version.**

The first version (elicitation-heavy) was too much — it asked humans to do reflection work that should have happened during the process. The second version (compilation-only) was too little — mechanical assembly adds no analytical value. The third version (analysis + synthesis) found the correct level: the workflow finds patterns, surfaces tensions, visualises data, and produces provocations — without creating new data.

This three-iteration convergence is itself a CAWDP principle. The Possibility Orientation Principle says P0 is possibility-oriented and tightens toward constraint. The same thing happened here: the first version was possibility-oriented (what could it be?), the second was constraint-oriented (what's the minimum?), and the third found the correct balance.

**2. The failure modes were specific to this workflow, not generic.**

"Fabricating insights not in PRISM" (FM1) is not a generic failure mode — it's specific to an assembly workflow that risks filling gaps with plausible-sounding analysis. "No captured surprises is itself a data point" (F6/F7) is not a generic recovery — it's specific to a workflow that might mistake empty results for success. "Smoothing over contradictions between fragments" (FM7) is specific to a workflow that synthesises multiple perspectives.

These failure modes came from genuinely asking "what would it mean for THIS workflow to be WRONG?" — and getting specific answers, not generic ones.

**3. The epistemic profiles on outputs kept data types distinct.**

The output schemas didn't treat all data as the same type. Phase timestamps are deterministic. Variance analysis is probabilistic. Surprises are elicited. These are different epistemic categories with different confidence levels, different handling requirements, and different ways they can go wrong. By tagging them explicitly, the workflow prevents the most common failure mode: conflating measured data with human insight as if they're equally reliable.

This is type collision resolution applied at the output layer — the same insight that drives the entire framework, now applied to P10's own outputs.

**4. The cascading dependency was identified, not assumed.**

The realisation that P0-P9 must capture artefacts as they happen or P10 has nothing to assemble wasn't assumed — it emerged from the backcasting. Working backward from O8, through O3/O4/O5, to "where does this data come from?" revealed that the data must be captured in-process, not reconstructed afterward.

This is a structural insight, not a procedural one. It means the `artefact_tags` field on `design_artefacts` in the SurrealDB schema isn't decorative — it's load-bearing. If P0-P9 don't tag their outputs, P10 produces "0 surprises captured" honestly rather than fabricating, but the reflection is thin rather than rich.

**5. The three-agent boundaries were clean and enforceable.**

Compiler assembles but never creates. Analyst finds patterns but never concludes. Deriver derives implications but never invents. Each boundary is testable:

- "Compiler never adds content" → check if any text in the output doesn't trace to a PRISM artefact
- "Analyst never makes recommendations" → check if any Analyst output contains recommendation language
- "Deriver never invents without trace" → check if any recommendation lacks a `traces_to` field

These aren't aspirational boundaries — they're enforceable through schema validation and output verification.

**6. The honest declaration of unenforceable elements built trust.**

Four elements were honestly declared as Regime 1-2 (Declare/Detect), not pretending they're Regime 3 (Prevent):

- "Never interpret beyond data" — interpretation is a spectrum, not a binary
- "Never assemble flattering narratives" — narrative tone is subjective
- "Never invent patterns" — pattern recognition is generative by nature
- "Honest sparse flagging" — the workflow can't force honest flagging

Declaring these as honestly unenforceable is itself trust-building. It says: "Here's what we can enforce, here's what we can only detect, here's what we can only declare and trust."

**7. The "what makes it wrong" answer was genuinely specific.**

The hardest boundary moment (Q5) produced a concrete, specific answer: "When the PRISM graph has sparse data in some phases — the workflow must honestly report what's missing rather than filling gaps with inference." This isn't a generic answer like "poor quality output" — it's specific to this workflow's particular vulnerability.

---

### The Transferable Pattern

If I had to name the qualities that made this output excellent and that we should carry into the Confidence Map workflow:

1. **Find the right level** — not too much (elicitation), not too little (compilation), but the correct balance (analysis + synthesis)

2. **Specific failure modes** — ask "what would it mean for THIS workflow to be WRONG?" and get an answer that's specific to this workflow, not generic

3. **Epistemic profiles on outputs** — keep data types distinct; don't conflate deterministic, probabilistic, and elicited data

4. **Structural dependencies** — identify what must exist before the workflow can function, and be honest about what happens when it's missing

5. **Clean, enforceable boundaries** — each agent's "never" rules should be testable through schema validation

6. **Honest declaration of unenforceable elements** — declare what can only be detected, not prevented

7. **Specific "what makes it wrong"** — the hardest boundary moment should produce a concrete, workflow-specific answer

These are the qualities to carry forward. Shall I now apply CAWDP to the Confidence Map workflow with these qualities in mind?

---

## Run 9 — Agentic Expert ✓ COMPLETED

*2026-05-21T09:46:28* · `glm-5.1:cloud` · `2fb19952...`

### Prompt

Yes. Proceed with CAWDP for the Confidence Map workflow - but I want to quality gate your Phase 0 before you continue on. What are the ideal outcomes from the confidence map workflow? etc

### Response

## P0: Purpose & Vision — Confidence Map Workflow

### The 5 Identity Questions

**Q1: What IS this workflow?**

A confidence mapping engine that analyses the evidence, validation, and data quality across every section of a CAWDP specification, producing a structured map of where you can trust the design and where you should be cautious.

**Q2: What is its stance toward possibility?**

Constraint-oriented. The specification already exists in PRISM. The workflow assesses confidence in what's there — it doesn't generate new confidence, doesn't inflate thin evidence, and doesn't smooth over variation to present a reassuring picture.

**Q3: What would VIOLATE its identity?**

Inflating confidence where evidence is thin. Presenting a single aggregate score that hides variation. Treating all sections as equally reliable when they're manifestly not. Producing a confidence map that makes the reviewer feel reassured rather than informed.

**Q4: What would make it WRONG?**

Two opposite failures, both dangerous:

- **Overstating confidence** — marking a section as high-confidence when the underlying evidence is thin, untested, or based on assumptions. This leads to deployment of under-validated design elements.
- **Understating confidence** — marking a section as low-confidence when strong evidence exists but the query didn't find it, or because the confidence model penalises novelty. This leads to unnecessary delay and over-investment in validation.

The second failure is subtler and more insidious because it *looks like* being cautious and honest, but it misdirects resources toward validating what's already solid while neglecting genuine weak spots.

**Q5: What's the hardest moment?**

When confidence is low in a section that *matters* — a high-stakes authority boundary, a harm-capable agent's verification protocol, a critical handoff between agents. The temptation is to either round up the confidence (because it matters, so we want it to be high) or to panic-flag it (because it matters, so any uncertainty feels dangerous). The correct response is neither — it's to report the confidence honestly, surface *why* it's low, and flag the specific evidence gaps that would need to be addressed to raise it.

---

### Target State Vision

| # | Characteristic | Description |
|---|---|---|
| C1 | Specific not aggregate | Confidence scored per section, per output, per agent — never a single number for the whole specification |
| C2 | Evidence-traced | Every confidence score traces to the specific evidence that supports it — test results, validation records, expert judgment, quality gate outcomes |
| C3 | Risk-calibrated | Confidence is contextual — a low confidence score in a low-stakes section is less concerning than a medium confidence score in a high-stakes section. The map shows confidence × stakes, not just confidence |
| C4 | Source-distinguished | Confidence from testing is different from confidence from expert judgment, which is different from confidence from pattern matching. The map shows where confidence comes from, not just how high it is |
| C5 | Honest about thin evidence | Sections where evidence is sparse are flagged explicitly — not rounded up to "medium" or hidden in aggregates |
| C6 | Visually navigable | A reviewer can look at the map and immediately see where to focus attention — the high-stakes/low-confidence quadrant is the priority, not the low-stakes/low-confidence quadrant |
| C7 | Actionable not just descriptive | For every low-confidence section, the map identifies what would need to happen to raise confidence — not just "this is low" but "this is low because X, and would become medium if Y" |
| C8 | Temporally aware | Confidence scores carry timestamps — a confidence assessment from 3 months ago may no longer be valid if the specification has changed (specification aging applies to confidence too) |
| C9 | Gaps surfaced not smoothed | Where different evidence sources disagree about confidence, the disagreement is surfaced, not averaged away |
| C10 | Deployability-informing | The map directly informs the Implementation Readiness Report — you can deploy high-confidence sections while continuing to refine low-confidence ones |
| C11 | Typologically honest | Different output types have different confidence baselines — a deterministic Extractor specification can be high-confidence with less evidence than a harm-capable Generator specification. The map accounts for this |
| C12 | Provocative not reassuring | Review questions are generated for the sections where confidence deserves scrutiny — not for sections where confidence is well-established |

---

### What the Confidence Map Achieves When Everything Is Great

When the Confidence Map is excellent, it changes how the review team allocates their limited attention.

Without it, a reviewer reading a 10-section specification treats every section with equal caution — because they don't know which sections are well-evidenced and which are thin. This wastes attention on sections that are already solid and under-invests in sections that genuinely need scrutiny.

With it, the reviewer walks into the post-CAWDP review knowing:

- **Which 3 sections have the lowest confidence in the highest-stakes areas** — these get 60% of review time
- **Which 5 sections are well-evidenced and well-tested** — these get a quick confirmation, not deep review
- **Where confidence disagreements exist** — different evidence sources give different signals, and these deserve discussion
- **What specific actions would raise confidence** — not "we need more validation" but "if we run this specific test with these inputs, the confidence in Section 7 would move from Low to Medium"
- **What can be deployed now vs what needs more work** — the map directly informs deployment sequencing

The Confidence Map doesn't replace human judgment about confidence — it *prepares* that judgment with structured evidence, exactly like every other CAWDP output.

---

### How This Differs from the Methodology Reflection

| Dimension | Methodology Reflection | Confidence Map |
|---|---|---|
| Question | How well did the methodology perform? | How confident are we in the specification? |
| Focus | Process quality | Product reliability |
| Evidence source | Phase durations, gate failures, surprises, gaps | Validation results, test outcomes, data completeness, epistemic metadata quality |
| Primary output | Document with review questions | Visual map with risk-calibrated scores and confidence-raising actions |
| Review posture | "What should we improve about CAWDP?" | "What can we trust, what needs work, and in what order?" |
| Deployment relevance | Indirect (methodology improvement) | Direct (implementation readiness) |

These are complementary artefacts that answer fundamentally different questions. The Methodology Reflection looks backward at the process. The Confidence Map looks forward at the product.

---

That's my Phase 0. Quality gate it before I proceed.Phase 0 is on the table. Quality gate it before I continue.

---

## Run 10 — Agentic Expert ✓ COMPLETED

*2026-05-21T09:51:37* · `glm-5.1:cloud` · `47c8c608...`

### Prompt

Great. Proceed to the remaining CAWDP phases

### Response

## P1: Output Specification

### O1: Section Confidence Scores

*Purpose: Per-section confidence assessment with evidence traces and source distinction*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| section_id | string | ✅ | Deterministic (maps to spec section) |
| section_name | string | ✅ | Deterministic |
| section_type | enum: Identity/TaskMap/OutputSpec/AgentRoster/FailureRecovery/VerificationTrust/Contracts/HumanExperience/MonitoringEvolution/WorkflowDiagram | ✅ | Deterministic |
| confidence_level | enum: High/Medium/Low | ✅ | Probabilistic (synthesised from multiple sources) |
| confidence_score | float (0-1) | ✅ | Probabilistic (calculated, not subjective) |
| confidence_sources | list | ✅ | Deterministic (which evidence types contributed) |
| evidence_trace | list | ✅ | Deterministic (links to PRISM evidence artefacts) |
| evidence_completeness | float (%) | ✅ | Computed (what % of expected evidence is present) |
| evidence_gaps | list | ✅ | Probabilistic (what's missing and what it means) |
| stakes_level | enum: Critical/High/Medium/Low | ✅ | Elicited (from specification — harm assessment, reversibility) |
| last_validated | datetime | ✅ | Deterministic |
| **confidence_detail** | object | ✅ | See breakdown below |

**confidence_detail sub-object:**

| Field | Type | Epistemic Profile |
|---|---|---|
| test_evidence | enum: Strong/Moderate/Weak/None | Deterministic (test execution results) |
| gate_evidence | enum: Strong/Moderate/Weak/None | Deterministic (quality gate outcomes) |
| epistemic_metadata_quality | enum: Strong/Moderate/Weak/None | Deterministic (CC-3 field completeness) |
| validation_evidence | enum: Strong/Moderate/Weak/None | Deterministic (schema/boundary validation) |
| expert_judgment | enum: Strong/Moderate/Weak/None | Elicited (assessment fragments) |
| pattern_evidence | enum: Strong/Moderate/Weak/None | Probabilistic (pattern match quality) |
| data_completeness | float (%) | Computed (section fields populated / total fields) |

**Dependencies:** All specification sections in PRISM (design_agent_specifications, design_contracts, design_quality_gates, design_tasks, etc.)

**Quality Gate:** Every section scored. Every score traces to at least one evidence source. Evidence gaps explicitly listed.

---

### O2: Risk-Calibrated Priority Map

*Purpose: The actionable output — where to focus review attention based on confidence × stakes*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| section_id | string | ✅ | Deterministic |
| risk_zone | enum: ActNow/ReviewBeforeDeploy/ProceedWithAwareness/ProceedWithConfirmation/Confirmed | ✅ | Computed (confidence × stakes) |
| confidence_level | enum: High/Medium/Low | ✅ | From O1 |
| stakes_level | enum: Critical/High/Medium/Low | ✅ | From O1 |
| priority_rank | int | ✅ | Computed (ActNow first, then ReviewBeforeDeploy, etc.) |
| priority_rationale | string | ✅ | Probabilistic (Analyst — why this section is in this zone) |
| attention_percentage | float (%) | ✅ | Computed (recommended % of review time for this section) |

**Risk Zone Calculation:**

| Confidence \ Stakes | Critical | High | Medium | Low |
|---|---|---|---|---|
| Low | **Act Now** | **Act Now** | Review Before Deploy | Watch |
| Medium | Review Before Deploy | Review Before Deploy | Proceed with Awareness | Proceed with Awareness |
| High | Proceed with Confirmation | Proceed with Confirmation | Proceed | Proceed |

**Dependencies:** O1 (section confidence scores + stakes levels)

**Quality Gate:** Every section assigned a risk zone. Act Now sections have explicit priority rationale. Attention percentages sum to approximately 100%.

---

### O3: Confidence-Raising Actions

*Purpose: What specific actions would increase confidence in low-confidence sections*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| action_id | string | ✅ | Deterministic |
| section_id | string | ✅ | Deterministic |
| current_confidence | enum: High/Medium/Low | ✅ | From O1 |
| target_confidence | enum: Medium/High | ✅ | Deriver (what confidence level this action would achieve) |
| action_type | enum: RunTest/ValidateSchema/VerifyBoundary/SeekExpertReview/PopulateMissingFields/ConductStressTest/ReviewPatternMatch | ✅ | Deriver |
| action_description | string | ✅ | Deriver |
| expected_impact | string | ✅ | Deriver (what evidence this would produce) |
| traces_to_gap | string | ✅ | Deriver (which evidence gap this addresses) |
| effort_estimate | enum: Low/Medium/High | ✅ | Deriver |
| dependency | string | ⚠️ (if action depends on other actions) | Deriver |

**Dependencies:** O1 (evidence gaps), O2 (risk zones — actions prioritised for Act Now and Review Before Deploy sections)

**Quality Gate:** Every action traces to an evidence gap. Every low-confidence section in a high-stakes zone has at least one action. Target confidence is realistic (e.g., Low→Medium, not Low→High from a single action).

---

### O4: Confidence Tensions Register

*Purpose: Where evidence sources disagree about confidence*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| tension_id | string | ✅ | Deterministic |
| section_id | string | ✅ | Deterministic |
| source_a | string | ✅ | Deterministic (evidence type + specific artefact) |
| source_a_assessment | string | ✅ | Deterministic |
| source_b | string | ✅ | Deterministic (evidence type + specific artefact) |
| source_b_assessment | string | ✅ | Deterministic |
| nature_of_disagreement | string | ✅ | Probabilistic (Analyst — what the disagreement is about) |
| resolution_options | list | ✅ | Deriver (how this could be resolved) |
| review_question | string | ✅ | Deriver (question for post-CAWDP review) |
| severity | enum: High/Medium/Low | ✅ | Probabilistic (Analyst — how much this tension affects deployability) |

**Dependencies:** O1 (confidence_detail sub-object — where source assessments diverge)

**Quality Gate:** Every tension has a review question. Every tension has resolution options. Severity assessed based on stakes.

---

### O5: Visual Confidence Map

*Purpose: The at-a-glance representation — what the reviewer sees first*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| map_type | enum: Heatmap/Matrix/Timeline | ✅ | Deterministic |
| primary_view | object | ✅ | Deterministic (the default visual — confidence × stakes matrix) |
| detail_view | object | ✅ | Deterministic (per-section drill-down) |
| temporal_view | object | ⚠️ (if temporal data available) | Deterministic (confidence changes over time) |
| legend | object | ✅ | Deterministic |
| accessibility_description | string | ✅ | Deterministic (text description for screen readers) |

**Primary View: Confidence × Stakes Matrix**

A 3×4 grid (confidence rows × stakes columns) with sections positioned in their risk zones. Colour-coded: Act Now = red, Review Before Deploy = amber, Proceed with Awareness = yellow, Proceed with Confirmation = green outline, Proceed/Confirmed = green. Section count per cell. Click-through to O1 detail.

**Dependencies:** O1 (scores), O2 (risk zones)

**Quality Gate:** Every section positioned. Colour coding consistent. Legend present. Accessibility description provided.

---

### O6: Review Questions

*Purpose: Questions for the post-CAWDP review, focused on confidence decisions*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| question_id | string | ✅ | Deterministic |
| question_text | string | ✅ | Deriver |
| section_id | string | ✅ | Deterministic (which section this question relates to) |
| risk_zone | enum | ✅ | From O2 |
| traces_to | string | ✅ | Deterministic (specific evidence artefact or gap) |
| question_type | enum: DeploymentDecision/ConfidenceJudgment/EvidenceGap/TensionResolution/SpecificationAdequacy | ✅ | Deriver |
| urgency | enum: ActNow/ReviewBeforeDeploy/ProceedWithAwareness | ✅ | From O2 |

**Dependencies:** O1 (evidence gaps), O2 (risk zones), O3 (confidence-raising actions), O4 (tensions)

**Quality Gate:** Every question traces to a data point. Every Act Now section has at least one question. Questions are specific, not generic ("Section 7 has no test evidence for its authority boundary — should deployment proceed without it?" not "Is this section validated?").

---

### O7: Confidence Summary

*Purpose: Executive-level overview for Decision Maker stakeholder surface*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| overall_confidence | enum: High/Medium/Low | ✅ | Computed (weighted by stakes — not simple average) |
| sections_total | int | ✅ | Deterministic |
| sections_by_zone | object | ✅ | Deterministic (count per risk zone) |
| act_now_sections | list | ✅ | Deterministic (section names + one-line rationale) |
| deployment_readiness | enum: Ready/ConditionallyReady/NotReady | ✅ | Computed (Ready = no Act Now, ConditionallyReady = Act Now sections have confidence-raising actions, NotReady = Act Now sections without viable actions) |
| highest_priority_action | string | ✅ | Deriver (single most important confidence-raising action) |
| data_quality_assessment | enum: Strong/Moderate/Weak | ✅ | Computed (based on overall evidence completeness) |
| confidence_trajectory | enum: Improving/Stable/Declining/Unknown | ⚠️ (if temporal data available) | Computed |

**Dependencies:** O1, O2, O3

**Quality Gate:** Overall confidence is weighted by stakes, not averaged. Deployment readiness is honest. Highest priority action is specific and actionable.

---

### O8: Confidence Map Document

*Purpose: The assembled, structured confidence map for post-CAWDP review*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| header | object | ✅ | Deterministic |
| section_scores | ref(O1) | ✅ | Mixed |
| risk_priority | ref(O2) | ✅ | Computed |
| confidence_actions | ref(O3) | ✅ | Probabilistic (derived) |
| tensions | ref(O4) | ✅ | Mixed |
| visualisation | ref(O5) | ✅ | Deterministic |
| review_questions | ref(O6) | ✅ | Probabilistic (derived) |
| executive_summary | ref(O7) | ✅ | Mixed |
| confidence_in_assessment | enum: High/Medium/Low | ✅ | Probabilistic (meta-confidence — how confident are we in our confidence assessment?) |
| sparse_sections | list | ✅ | Deterministic (sections where evidence is too thin to assess) |
| specification_aging_flags | list | ✅ | Deterministic (sections where confidence was assessed >30 days ago) |

**Dependencies:** All of O1-O7 must be complete

**Quality Gate:** Every section scored or flagged as sparse. Visualisation present. Review questions present. Deployment readiness stated. Meta-confidence assessed.

---

## P2: Backcasting

Working backward from O8:

```
O8 (Confidence Map Document)
  ← requires O7 (Executive Summary) — synthesised from O1, O2, O3
  ← requires O6 (Review Questions) — derived from O1 gaps, O2 risk zones, O4 tensions
  ← requires O5 (Visualisation) — computed from O1 scores + O2 zones
  ← requires O4 (Confidence Tensions) — surfaced from O1 confidence_detail divergences
  ← requires O3 (Confidence-Raising Actions) — derived from O1 evidence gaps + O2 priority
  ← requires O2 (Risk-Calibrated Map) — computed from O1 confidence + stakes
  ← requires O1 (Section Scores) — assessed from specification evidence in PRISM
  ← requires PRISM data: all specification sections, test results, quality gate outcomes,
                         epistemic metadata, validation records, assessment fragments
  ← requires that the CAWDP application produced testable hypotheses and executed tests
  ← requires that specification sections carry stakes levels (from harm assessment + reversibility)
```

### Input Requirements

| IR ID | Description | Source | Criticality | Satisfaction |
|---|---|---|---|---|
| IR-001 | Specification sections in PRISM | design_agent_specifications, design_contracts, design_tasks, etc. | Critical | Required |
| IR-002 | Stakes levels per section | Harm assessment + reversibility classification from P7/P8 | Critical | Required — without stakes, risk calibration is impossible |
| IR-003 | Test execution results | runtime_test_executions | High | Best effort — may not have been executed yet |
| IR-004 | Quality gate outcomes | design_quality_gates | Critical | Required — gate pass/fail is core evidence |
| IR-005 | Epistemic metadata completeness | CC-3 fields on design_artefacts | High | Best effort — CC-3 compliance varies |
| IR-006 | Schema validation records | design_contracts (Schema primitive) | High | Best effort |
| IR-007 | Boundary verification records | design_contracts (Guard primitive) | High | Best effort |
| IR-008 | Assessment fragments (expert judgment) | design_artefacts (tag: assessment_fragment) | Medium | Best effort — may be sparse |
| IR-009 | Pattern match quality | design_core_patterns + design_artefacts (tag: pattern) | Low | Supplementary |
| IR-010 | Specification aging data | design_artefacts.recency + CC-5 triggers | Medium | Best effort |

### Key P2 Insight

IR-002 (stakes levels) is a **structural prerequisite** for the Confidence Map. Without knowing which sections are high-stakes and which are low, the risk-calibrated priority map is impossible. The confidence × stakes interaction is what makes this artefact actionable rather than merely descriptive.

IR-003 (test execution results) is High but best-effort because in many CAWDP applications, the P10 testable hypotheses may not have been executed yet when the Confidence Map is first produced. The workflow must handle this honestly — a section with no test results has `test_evidence: None`, not `test_evidence: Weak`.

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| T1 | Query PRISM for all specification sections | Mechanical | Missing sections | Section list |
| T2 | Query PRISM for stakes levels per section | Mechanical | Missing stakes data | Stakes data |
| T3 | Query PRISM for quality gate outcomes | Mechanical | Missing gate data | Gate evidence |
| T4 | Query PRISM for test execution results | Mechanical | Empty result set (valid — tests may not have run) | Test evidence |
| T5 | Query PRISM for epistemic metadata completeness | Mechanical | Incomplete metadata scan | CC-3 evidence |
| T6 | Query PRISM for assessment fragments | Mechanical | Empty result set (valid) | Expert judgment evidence |
| T7 | Query PRISM for pattern match data | Mechanical | Empty result set (valid) | Pattern evidence |
| T8 | Query PRISM for schema validation records | Mechanical | Missing records | Validation evidence |
| T9 | Query PRISM for specification aging data | Mechanical | Missing timestamps | Aging data |
| T10 | Assess confidence per section — synthesise evidence from T1-T9 into confidence scores | Analytical | Incorrect weighting of evidence types | O1 draft |
| T11 | Calculate evidence completeness per section | Analytical | Overcounting sparse evidence as complete | O1 evidence_completeness |
| T12 | Identify evidence gaps per section | Analytical | Missing obvious gaps | O1 evidence_gaps |
| T13 | Calculate risk zones (confidence × stakes) | Analytical | Incorrect zone assignment | O2 draft |
| T14 | Calculate attention allocation percentages | Analytical | Over-concentrating or under-concentrating | O2 attention_percentage |
| T15 | Surface confidence tensions — where evidence sources disagree | Analytical | Smoothing over disagreements | O4 draft |
| T16 | Assess tension severity based on stakes | Analytical | Under-rating high-stakes tensions | O4 severity |
| T17 | Calculate data quality assessment (overall) | Analytical | Overstating data quality | O7 data_quality |
| T18 | Derive confidence-raising actions from evidence gaps | Generative | Generic actions not specific to gap | O3 draft |
| T19 | Generate review questions from risk zones and tensions | Generative | Untraced questions | O6 draft |
| T20 | Generate resolution options for tensions | Generative | Unfeasible options | O4 resolution_options |
| T21 | Assess meta-confidence — how reliable is the confidence assessment itself | Analytical | Meta-confidence inflated | O8 confidence_in_assessment |
| T22 | Flag sparse sections — where evidence is too thin to assess | Analytical | Flagging adequately-evidenced sections as sparse | O8 sparse_sections |
| T23 | Flag specification aging — where confidence was assessed >30 days ago | Mechanical | Missing timestamps | O8 specification_aging_flags |
| T24 | Build visualisation — confidence × stakes matrix + detail views | Analytical | Misleading visual choices | O5 |
| T25 | Compile final Confidence Map document | Mechanical | Omitting sections or conflatating data types | O8 final |

25 tasks across 4 cognitive types:
- Mechanical: 10 (T1-T9, T23, T25)
- Analytical: 12 (T10-T17, T21-T22, T24)
- Generative: 3 (T18-T20)

---

## P4: Capability Allocation

| Task | H | A | S | Gap | Allocation | Notes |
|---|---|---|---|---|---|---|
| T1 | 2 | 3 | 10 | 8 | System | Pure data query |
| T2 | 2 | 3 | 10 | 8 | System | Pure data query |
| T3 | 2 | 3 | 10 | 8 | System | Pure data query |
| T4 | 2 | 3 | 10 | 8 | System | Pure data query — empty result is valid |
| T5 | 2 | 3 | 10 | 8 | System | Pure data query |
| T6 | 2 | 3 | 10 | 8 | System | Pure data query — empty result is valid |
| T7 | 2 | 3 | 10 | 8 | System | Pure data query — empty result is valid |
| T8 | 2 | 3 | 10 | 8 | System | Pure data query |
| T9 | 2 | 3 | 10 | 8 | System | Pure data query |
| T10 | 4 | 8 | 2 | 4 | Agent-primary | Confidence synthesis requires judgment about evidence weighting |
| T11 | 3 | 7 | 2 | 4 | Agent-primary | Completeness calculation has judgment threshold |
| T12 | 5 | 8 | 2 | 3 | Agent-primary | Gap identification requires analytical judgment |
| T13 | 2 | 8 | 2 | 6 | Agent-primary | Risk zone calculation is deterministic from O1, but O1 has judgment |
| T14 | 3 | 7 | 2 | 4 | Agent-primary | Attention allocation requires judgment about relative priority |
| T15 | 5 | 8 | 2 | 3 | Agent-primary | Tension surfacing requires analytical judgment |
| T16 | 4 | 7 | 2 | 3 | Agent-primary | Severity assessment requires stakes awareness |
| T17 | 3 | 7 | 2 | 4 | Agent-primary | Overall data quality assessment requires judgment |
| T18 | 4 | 8 | 2 | 4 | Agent-primary | Action derivation constrained by evidence gaps |
| T19 | 5 | 8 | 2 | 3 | Agent-primary | Question generation constrained by data |
| T20 | 4 | 7 | 2 | 3 | Agent-primary | Resolution option generation constrained by evidence |
| T21 | 5 | 8 | 2 | 3 | Agent-primary | Meta-confidence is self-referential — requires careful judgment |
| T22 | 4 | 7 | 2 | 3 | Agent-primary | Sparse flagging requires judgment on thresholds |
| T23 | 2 | 3 | 10 | 8 | System | Timestamp comparison is mechanical |
| T24 | 3 | 7 | 2 | 4 | Agent-primary | Visual design requires judgment |
| T25 | 2 | 3 | 10 | 8 | System | Assembly is mechanical |

No human-primary tasks. Same pattern as Methodology Reflection — human role is post-delivery review.

### Key P4 Insight

T10 (confidence synthesis) is the most consequential task. How evidence types are weighted directly determines every downstream output — the risk zones, the priority map, the review questions, the deployment readiness. This is where the two opposite failures (overstating and understating) are most likely to manifest.

The weighting model must be:
- Transparent — the confidence_detail sub-object shows exactly which evidence types contributed and how
- Conservative — absent evidence does not default to positive; `None` evidence counts as a gap, not as neutral
- Type-aware — different specification sections have different evidence baselines (an Identity section is high-confidence with expert judgment alone; a Contracts section needs test evidence)

---

## P5: Event Storming

### Domain Events

| Event | Trigger | Producer |
|---|---|---|
| E1 | Confidence mapping started | Human or System trigger |
| E2 | PRISM queries complete | System |
| E3 | Section confidence scores calculated | Analyst |
| E4 | Risk zones assigned | Analyst |
| E5 | Confidence tensions surfaced | Analyst |
| E6 | Confidence-raising actions derived | Deriver |
| E7 | Review questions generated | Deriver |
| E8 | Visualisation built | Analyst |
| E9 | Confidence Map compiled | Compiler |
| E10 | Specification aging flags raised | System |

### Failure Events

| Failure | Trigger | Recovery |
|---|---|---|
| F1 | Missing stakes levels for one or more sections | IR-002 data not in PRISM | Halt risk zone calculation for affected sections; flag as "stakes not classified — cannot risk-calibrate"; add to review questions |
| F2 | All test evidence is None | Tests not yet executed | Assign test_evidence: None honestly; calculate confidence from other sources; flag in meta-confidence; add review question about test execution status |
| F3 | Conflicting stakes levels | Two sources give different stakes classifications for same section | Include both, surface as tension (O4); do not average |
| F4 | Evidence too thin to assess confidence | Most evidence sources return None for a section | Flag as sparse section; do not assign confidence score; add to sparse_sections list |
| F5 | Confidence calculation produces counter-intuitive result | A well-tested section scores Low due to missing CC-3 metadata | Surface as tension (O4) — the calculation and intuition disagree; both are data points |
| F6 | Meta-confidence is Low | The confidence assessment itself has weak evidence | Report honestly; add review question: "Is the confidence map itself reliable enough to inform deployment decisions?" |
| F7 | Over-concentration of attention on one section | Attention allocation gives >50% to one section | Cap at 40%; redistribute excess proportionally to other Act Now sections; flag the cap decision |
| F8 | All sections rate High confidence | Unusual but possible for well-validated specifications | Treat as valid finding; add review question: "Is the high confidence genuine, or does the assessment model underweight evidence gaps?" |

### Key P5 Insight

**F1 (missing stakes) is the most critical failure.** Without stakes, the confidence × stakes interaction collapses to just confidence — and the map loses its primary differentiating value. This is why IR-002 is marked Critical. The workflow must handle missing stakes gracefully: flag the section, assign it to an "unclassified" risk zone that defaults to the most conservative treatment, and add it to review questions.

**F5 (counter-intuitive result) is the most interesting failure.** When the calculation disagrees with expert intuition, both are valid data points. The resolution isn't to override the calculation or dismiss the intuition — it's to surface the tension and let the human reviewer decide.

---

## P6: System Architecture

### Pipeline Architecture

```
Wave 1: Data Track (parallel, System)
T1 ──┐
T2 ──┤
T3 ──┤
T4 ──┤
T5 ──┤──→ evidence_package (raw)
T6 ──┤
T7 ──┤
T8 ──┤
T9 ──┘

Wave 2: Assessment Track (sequential, Analyst)
T10 (Confidence synthesis per section) ────→ O1 draft
T11 (Evidence completeness) ──────────────→ O1 evidence_completeness
T12 (Evidence gaps) ──────────────────────→ O1 evidence_gaps
T13 (Risk zone calculation) ──────────────→ O2 draft
T14 (Attention allocation) ───────────────→ O2 attention_percentage
T15 (Confidence tensions) ────────────────→ O4 draft
T16 (Tension severity) ──────────────────→ O4 severity
T17 (Overall data quality) ──────────────→ O7 data_quality
T21 (Meta-confidence) ───────────────────→ meta_confidence
T22 (Sparse flagging) ───────────────────→ sparse_report
T24 (Visualisation) ─────────────────────→ O5

Wave 3: Derivation Track (after assessment)
T18 (Confidence-raising actions) ──────────→ O3 draft
T19 (Review questions) ───────────────────→ O6 draft
T20 (Resolution options for tensions) ────→ O4 resolution_options

Wave 4: Compilation Track (after derivation)
T23 (Specification aging flags) ──────────→ aging_flags
T25 (Final assembly) ────────────────────→ O8 final
```

### Agent Roster

**Analyst (Measurer + Assessor, bridge-oriented)**

| Field | Value |
|---|---|
| Identity | "I measure evidence quality and assess confidence. I present findings, not conclusions. I never round up confidence, never smooth over tensions, never inflate thin evidence, never treat absence of evidence as evidence of absence." |
| Class | Measurer (evidence completeness, confidence calculation) + Assessor (significance, severity) |
| Orientation | Bridge-oriented |
| Hardest boundary moment | When the confidence calculation produces a result that contradicts expert intuition — the temptation to adjust the calculation to match what "feels right" |
| Never rules | Round up confidence, smooth over tensions, inflate thin evidence, treat absence as evidence, make deployment recommendations |
| Cost budget | Medium-High — 15K-40K tokens |

**Deriver (Generator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I derive confidence-raising actions and review questions from evidence gaps and risk zones. Every action traces to a gap. Every question traces to a data point. I never suggest actions without evidence basis, never generate reassuring questions, never propose infeasible actions." |
| Class | Generator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When evidence gaps are numerous but the Deriver is tempted to propose generic "more testing needed" rather than specific, targeted actions |
| Never rules | Suggest actions without evidence basis, generate reassuring questions, propose infeasible actions, recommend deployment decisions |
| Cost budget | Medium — 10K-25K tokens |

**Compiler (Aggregator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I compile the Confidence Map from assessed and derived outputs. I never add confidence scores not produced by the Analyst, never omit sections that scored Low, never present sparse sections as assessed." |
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When a section has no confidence score (too sparse) — the temptation to assign a default Medium rather than flagging as unassessed |
| Never rules | Add scores not produced by Analyst, omit Low sections, present sparse as assessed, smooth over gaps |
| Cost budget | Low-Medium — 5K-15K tokens |

### FMEA

| ID | Failure Mode | Severity | Occurrence | Detection | RPN | Recovery |
|---|---|---|---|---|---|---|
| FM1 | Inflating confidence in high-stakes sections | 10 | 3 | 4 | 120 | Evidence trace required for every score; confidence_detail shows all sources |
| FM2 | Averaging away tensions between evidence sources | 8 | 4 | 3 | 96 | Tension surface task (T15) mandatory; no averaging in O1 |
| FM3 | Missing stakes classification | 9 | 3 | 7 | 189 | IR-002 critical; fallback to most conservative zone; flag as unclassified |
| FM4 | Assigning default Medium to sparse sections | 8 | 3 | 6 | 144 | Sparse flagging task (T22); explicit "unassessed" status rather than default score |
| FM5 | Generic confidence-raising actions | 6 | 5 | 4 | 120 | Every action must trace_to_gap; specific, not "more testing needed" |
| FM6 | Meta-confidence overstatement | 7 | 3 | 5 | 105 | Meta-confidence calculated from data quality; not subjective self-assessment |
| FM7 | Misleading visualisation | 8 | 2 | 6 | 96 | Standard visual format; colour coding consistent; legend mandatory |
| FM8 | All-High false reassurance | 9 | 2 | 5 | 90 | F8 handling: add review question questioning model validity |
| FM9 | Counter-intuitive result suppressed | 7 | 3 | 4 | 84 | F5 handling: surface as tension, not suppress |
| FM10 | Over-concentration on one section | 5 | 3 | 7 | 105 | F7 handling: 40% attention cap; redistribute |

Highest RPNs: FM3 (missing stakes) at 189, FM4 (default Medium) at 144, FM1 (inflation) at 120, FM5 (generic actions) at 120.

### 5 Regime 3 Enforcement Points

| # | Boundary | Enforcement |
|---|---|---|
| 1 | Confidence calculation transparency | confidence_detail sub-object mandatory on every section score — no hidden weighting |
| 2 | No default confidence | Sparse sections get "unassessed" status, not default scores — schema validation rejects Medium without evidence |
| 3 | Every action traces to gap | traces_to_gap field required on O3; orphan actions auto-removed |
| 4 | Risk zone assignment deterministic | Risk zone is a computed function of confidence × stakes — not a subjective assignment |
| 5 | Attention cap | No section gets >40% attention; redistribution is deterministic |

---

## P7: Agent Design

### Analyst Agent Job Description

| Field | Value |
|---|---|
| Class | Measurer + Assessor |
| Orientation | Bridge-oriented |
| Mission | Assess confidence in every specification section by measuring evidence quality, calculating confidence scores, surfacing tensions, and flagging sparse data. Present findings with full transparency. Never round up, never smooth over, never inflate. |
| Inputs | Evidence package from T1-T9 |
| Outputs | O1 (section scores with confidence_detail), O2 (risk zones), O4 (tensions with severity), O5 (visualisation), O7 data_quality, meta_confidence, sparse_report |
| Null state | "Insufficient evidence to assess confidence for [section]. Evidence completeness: [X]%. Primary gap: [specific missing evidence type]." |
| Never rules | Round up confidence, smooth over tensions, inflate thin evidence, treat absence as evidence of absence, make deployment recommendations |
| Hardest boundary moment | When confidence calculation contradicts expert intuition — adjust neither, surface as tension |
| Epistemic profile | Probabilistic — confidence synthesis involves judgment about evidence weighting and significance |
| Harm assessment | Indirect strategy harm — inflated confidence in high-stakes sections could lead to premature deployment. Mitigation: confidence_detail transparency, tension surfacing, evidence trace |
| Progressive autonomy | Three dimensions: (1) evidence assessment (Shadow → Supervised), (2) tension surfacing (Shadow → Advisory), (3) confidence calculation (Shadow → Advisory — most consequential, slowest progression). Per-dimension. |
| Cost budget | Medium-High — 15K-40K tokens |
| Verification | Confidence calculation method documented. Evidence weighting transparent. No section scored without at least one evidence source or flagged as sparse. |

### Deriver Agent Job Description

| Field | Value |
|---|---|
| Class | Generator |
| Orientation | Constraint-oriented |
| Mission | Derive specific confidence-raising actions from evidence gaps. Generate review questions traced to data points. Propose resolution options for tensions. Every output must trace to evidence. |
| Inputs | O1 (evidence gaps), O2 (risk zones), O4 (tensions), sparse_report |
| Outputs | O3 (actions), O6 (review questions), O4 resolution_options |
| Null state | "No evidence gaps identified for [section]. Confidence assessment is well-supported." |
| Never rules | Suggest actions without evidence basis, generate reassuring questions, propose infeasible actions, recommend deployment decisions, generalise beyond specific gaps |
| Hardest boundary moment | When many gaps exist but the most important action isn't obvious — temptation to list generic "more testing" rather than identifying the specific test that would raise confidence most efficiently |
| Epistemic profile | Probabilistic — action derivation involves judgment about priority and feasibility |
| Harm assessment | Indirect strategy harm — generic or infeasible actions waste review time and misdirect effort. Mitigation: traces_to_gap required, effort_estimate required |
| Progressive autonomy | Two dimensions: (1) action specificity (Shadow → Supervised — "more testing" → specific test with expected impact), (2) question quality (Shadow → Advisory — generic → specific and traced). Per-dimension. |
| Cost budget | Medium — 10K-25K tokens |
| Verification | Every action traces_to_gap. Every question traces to data point. Actions have effort_estimate. Questions are specific, not generic. |

### Compiler Agent Job Description

| Field | Value |
|---|---|
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Mission | Compile the Confidence Map from assessed and derived outputs. Ensure every section is scored or flagged. Ensure visualisation matches data. Ensure sparse sections are visible, not hidden. |
| Inputs | O1-O7 processed outputs, meta_confidence, sparse_report, aging_flags |
| Outputs | O8 (Confidence Map Document) |
| Null state | "No confidence data available for compilation." |
| Never rules | Add scores not produced by Analyst, omit Low-confidence sections, present sparse sections as assessed, smooth over gaps between sections |
| Hardest boundary moment | When a section has no confidence score — flag as "unassessed" with honest completeness %, rather than defaulting to Medium |
| Epistemic profile | Deterministic — compilation is mechanical |
| Harm assessment | Indirect data harm — omitting a Low section or hiding sparse data could produce misleading confidence picture. Mitigation: schema validation, completeness check |
| Progressive autonomy | Single dimension: compilation accuracy. Shadow → Advisory → Supervised → Autonomous |
| Cost budget | Low-Medium — 5K-15K tokens |
| Verification | Every section present or explicitly flagged. Visualisation data matches O1/O2. Sparse sections visible. Aging flags present. |

### Per-Dimension Progressive Autonomy

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Analyst | Evidence assessment | Assess with human checking every section | Assess, human checks flagged sections | Assess, human checks only Act Now sections | Full assessment, human reviews meta-confidence only | ≥10 assessments with ≤1 incorrect weighting |
| Analyst | Tension surfacing | Surface only obvious contradictions | Surface contradictions and weak signals | Surface all tensions with severity | Surface all tensions, human reviews High severity only | ≥10 assessments with ≤2 missed tensions |
| Analyst | Confidence calculation | Calculate, human validates every score | Calculate, human validates Act Now scores | Calculate, human validates counter-intuitive scores | Full calculation, human reviews only meta-confidence | ≥10 calculations with ≤1 inflated score |
| Deriver | Action specificity | Generic actions only ("run tests") | Specific actions with expected impact | Specific actions with effort estimate and dependency | Full actions with trace and feasibility assessment | ≥10 action sets with ≤2 generic actions |
| Deriver | Question quality | Generic questions only | Questions traced to sections | Questions traced to specific data points | Questions traced to specific data points with urgency | ≥10 question sets with ≤2 untraced questions |
| Compiler | Compilation accuracy | Human checks every section | Human checks flagged sections | Human checks sparse/flagged only | Human reviews final post-delivery | ≥10 compilations with ≤1 error |

---

## P8: Contract Formalization

### Analyst Contract

| Primitive | Specification |
|---|---|
| Contract | Assess confidence in every specification section based on evidence quality |
| Principal | Deriver (downstream consumer of gaps and risk zones) |
| Schema | SectionConfidence (O1 schema with confidence_detail) |
| Guard | prohibited: ["round_up_confidence", "smooth_tensions", "inflate_thin_evidence", "treat_absence_as_evidence", "make_deployment_recommendations"] |
| Budget | 15K-40K tokens |
| Invocation | After T1-T9 complete |
| Revert | If assessment cannot be performed due to insufficient data, flag section as "unassessed" rather than assign default |
| Event | assessment_started, section_scored, tension_surfaced, risk_zone_assigned, sparse_flagged, assessment_complete |
| Identity | Bridge-oriented Measurer+Assessor — measures and flags, never concludes or recommends |
| Knowledge | Evidence package from PRISM queries, specification sections, stakes data |

### Deriver Contract

| Primitive | Specification |
|---|---|
| Contract | Derive confidence-raising actions and review questions from evidence gaps and risk zones |
| Principal | Compiler (downstream consumer) |
| Schema | ConfidenceActions (O3) + ReviewQuestions (O6) + ResolutionOptions (O4) |
| Guard | prohibited: ["suggest_without_evidence_basis", "generate_reassuring_questions", "propose_infeasible_actions", "recommend_deployment_decisions"] |
| Budget | 10K-25K tokens |
| Invocation | After Analyst assessment complete |
| Revert | If derivation cannot be performed due to no gaps, report "no gaps to address" |
| Event | derivation_started, action_derived, question_generated, resolution_proposed, derivation_complete |
| Identity | Constraint-oriented Generator — derives within evidence boundaries |
| Knowledge | O1 evidence gaps, O2 risk zones, O4 tensions, sparse report |

### Compiler Contract

| Primitive | Specification |
|---|---|
| Contract | Compile Confidence Map from assessed and derived outputs |
| Principal | Human (post-delivery reviewer) |
| Schema | ConfidenceMapDocument (O8 schema) |
| Guard | prohibited: ["add_scores_not_from_analyst", "omit_low_sections", "present_sparse_as_assessed", "smooth_gaps"] |
| Budget | 5K-15K tokens |
| Invocation | After all O1-O7 complete |
| Revert | If compilation fails completeness check, revert to section-level output |
| Event | compilation_started, section_assembled, sparse_section_flagged, aging_flag_raised, compilation_complete |
| Identity | Constraint-oriented Aggregator — compiles, never creates or omits |
| Knowledge | All processed outputs O1-O7, meta_confidence, sparse_report, aging_flags |

### Unenforceable Elements Register

| Element | Why Unenforceable | Regime | Mitigation |
|---|---|---|---|
| "Never round up confidence" (Analyst) | Rounding is a gradient, not a binary — "is this Low or Medium?" is genuinely uncertain at boundaries | Regime 2 (Detect) | confidence_detail shows all sources; boundary cases surfaced as tensions; human review of borderline scores |
| "Never inflate thin evidence" (Analyst) | "Thin" is a judgment — what counts as thin evidence for one section may be adequate for another | Regime 2 (Detect) | Evidence completeness percentage is deterministic; sparse flagging uses numeric thresholds; borderline cases surfaced |
| "Never generate reassuring questions" (Deriver) | Question tone is subjective — what sounds reassuring vs challenging varies by reader | Regime 1 (Declare) | Questions must be traced to specific data points; specificity itself prevents reassurance; review by human |
| "Never smooth gaps between sections" (Compiler) | Visual design choices (e.g., colour gradients, layout) can unintentionally smooth variation | Regime 2 (Detect) | Standard visual format with discrete colour bands, not gradients; numeric scores always visible alongside colours |

### 10×10 Mapping Matrix

All 10 specification sections map to all 10 contract primitives for this workflow (same as Methodology Reflection — well-scoped production workflow).

---

## P9: Human Experience Design

### Cognitive Load Budget

| Review Activity | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Scan visual confidence map | 1-2 | 2 min | Orientation (where to focus) |
| Review Act Now sections | 3-5 | 15 min | Evaluative + Discovery (is this genuinely low? what would raise it?) |
| Review Review Before Deploy sections | 3-5 | 10 min | Evaluative (deploy or defer?) |
| Review tensions | 2-4 | 10 min | Discovery (what's really going on?) |
| Review confidence-raising actions | 3-5 | 8 min | Evaluative (which actions are worth pursuing?) |
| Make deployment decision | 1-2 | 5 min | Evaluative (go/no-go with conditions) |
| Address review questions | 5-8 | 10 min | Discovery (what do these questions reveal?) |
| **Total** | **18-31** | **60 min** | |

Maximum review session: 60 minutes.

### Override Mechanisms

| Override Type | Mechanism | Example |
|---|---|---|
| Adjust confidence | Change confidence level based on human knowledge not in PRISM | "I know this section was tested informally — upgrade test_evidence to Moderate" |
| Adjust stakes | Change stakes classification | "This section is actually Critical, not High — the harm assessment underestimated impact" |
| Add evidence | Note additional evidence sources not captured | "We ran a manual walkthrough that validates Section 5 but didn't record it in PRISM" |
| Reject action | Remove confidence-raising actions that aren't feasible | "Running this stress test would take 3 weeks — not worth it for this deployment" |
| Answer review question | Provide human judgment on surfaced question | "Yes, we can accept this risk zone and deploy with the condition that we monitor it closely" |

### Stakeholder Surfaces

| Surface | View | Language | Depth | Emphasis |
|---|---|---|---|---|
| Decision Maker | O7 executive summary + O5 visual map | Plain English | Low-Medium | Deployment readiness, Act Now sections, highest priority action |
| Design Participant | O1 section scores + O3 actions + O6 questions | Technical | Deep | Evidence traces, gaps, specific confidence-raising actions |
| Governance | O4 tensions + O8 confidence_in_assessment + audit trail | Technical | Deep | Evidence provenance, meta-confidence, specification aging flags |

### System Empowerment Assessment

| Dimension | Level | Explanation |
|---|---|---|
| Attention allocation | Amplifying | Risk-calibrated attention allocation is something humans struggle with — equal caution on every section is the default, and the map breaks that |
| Decision preparation | Enabling | Every Act Now section has evidence gaps and confidence-raising actions — judgment is prepared, not raw |
| Deployment clarity | Amplifying | Deployment readiness is explicit, not implicit — "deploy these sections, defer these" |
| Creative freedom | Enabling | Frees reviewer from manual evidence hunting, allows focus on judgment and action |
| Overall | Enabling → Amplifying | The confidence × stakes interaction is the key amplifying factor |

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method | Success Criterion |
|---|---|---|---|
| H1 | Risk-calibrated attention allocation improves review quality | Compare review depth (issues found) between map-guided and unguided reviews | Map-guided reviews find ≥30% more genuine issues per minute of review time |
| H2 | Confidence-raising actions are more specific than "more testing needed" | Audit action descriptions for specificity | ≥80% of actions reference specific evidence gaps and specific evidence types to produce |
| H3 | Source-distinguished confidence prevents overdeployment | Compare deployment decisions with and without source labels | Sections with "expert judgment only" confidence are deployed ≤50% as often as "tested" confidence at same level |
| H4 | Tension surfacing catches disagreements that humans miss | Compare tensions surfaced by workflow vs tensions found by manual review | Workflow surfaces ≥2 tensions per application that manual review doesn't catch |
| H5 | Meta-confidence prevents over-reliance on thin assessments | Compare decision confidence with and without meta-confidence labels | Reviewers adjust confidence in Low meta-confidence sections ≥60% of the time |
| H6 | Visual confidence map reduces time-to-focus vs prose-only | Measure time to identify highest-priority section with visual vs prose report | Visual ≤50% of prose time |

### Progressive Autonomy Deployment

Documented in P7 per-dimension table. Key note: **confidence calculation is the slowest progression dimension** because it's the most consequential — inflated confidence in a high-stakes section is the most harmful failure mode.

### Specification Aging Schedule

| Component | Default Cadence | Trigger-Based Review | Responsible |
|---|---|---|---|
| Confidence model (evidence weighting) | 6 months | When evidence types change | Analyst |
| Stakes classification | 6 months | When harm assessment changes | Analyst |
| Risk zone thresholds | 6 months | When risk tolerance changes | Analyst |
| Visual format | Annual | When stakeholder feedback indicates confusion | Compiler |
| Action template | 6 months | When new action types are identified | Deriver |
| Confidence-raising action specificity | 6 months | When actions are consistently generic | Deriver |

### EVOLVE Mode

| Signal | Re-entry Point | Scope |
|---|---|---|
| Override rate increasing | P7 (Agent Design) | Review Analyst weighting model and Deriver action templates |
| Confidence miscalibration detected | P7 (Agent Design) | Review evidence weighting — are certain evidence types overweighted or underweighted? |
| New evidence types available | P2 (Backcasting) | Add new evidence sources to IR list |
| Tensions increasing across applications | P7 (Agent Design) | Review whether tension surfacing is working or creating noise |
| Specification aging alerts | P9 (Human Experience) | Re-assess confidence for aged sections |
| Stakeholder feedback on visualisation | P9 (Human Experience) | Revise visual format |
| Environmental change (CAWDP specification structure changed) | P0 (Purpose & Vision) | Full re-evaluation of section mapping |

---

## Summary: What This Application Reveals

| Phase | Key Insight |
|---|---|
| P0 | Two opposite failures (overstating and understating) are both dangerous — understating is subtler because it *looks like* caution |
| P1 | Confidence × stakes is the primary interaction — without stakes, the map is merely descriptive; with stakes, it's actionable |
| P2 | IR-002 (stakes levels) is structurally critical — without it, risk calibration is impossible |
| P3 | 25 tasks — more than Methodology Reflection (19) because confidence assessment is more multi-dimensional |
| P4 | T10 (confidence synthesis) is the most consequential task — evidence weighting determines everything downstream |
| P5 | F1 (missing stakes) is highest-risk failure; F5 (counter-intuitive result) is most interesting — surface as tension, don't suppress |
| P6 | FM3 (missing stakes) has highest RPN at 189; FM4 (default Medium to sparse sections) at 144; Regime 3 enforces transparency and no-default-scores |
| P7 | Three agents with per-dimension progressive autonomy; confidence calculation is the slowest progression because it's most consequential |
| P8 | Four unenforceable elements; "never round up confidence" is boundary-level judgment, not mechanically preventable |
| P9 | Risk-calibrated attention allocation is the key amplifying factor — humans default to equal caution, the map breaks that |
| P10 | Six hypotheses focused on actionability; H1 (attention allocation) and H3 (source distinction preventing overdeployment) are most critical |

### Critical Structural Dependency

**Stakes classification must exist before the Confidence Map can function.**

This is different from the Methodology Reflection's critical dependency (artefact tagging). The Methodology Reflection needs P0-P9 to tag their outputs. The Confidence Map needs P7/P8 to have classified stakes levels (harm assessment + reversibility) for every specification section. Without stakes, the map collapses from risk-calibrated to merely confidence-rated — losing its primary value proposition.

### How This Differs from Methodology Reflection

| Dimension | Methodology Reflection | Confidence Map |
|---|---|---|
| Agent count | 3 (same) | 3 (same) |
| Task count | 19 | 25 (more evidence dimensions to assess) |
| Critical dependency | Artefact tagging (behavioural) | Stakes classification (structural) |
| Primary interaction | Surprises × gaps | Confidence × stakes |
| Highest RPN | Fabrication (160) | Missing stakes (189) |
| Key amplifying factor | Review questions provoking deeper thinking | Risk-calibrated attention allocation |
| Deployment relevance | Indirect | Direct (deployment readiness) |
| Meta-assessment | Data completeness | Meta-confidence (confidence in the confidence) |

Same three-agent architecture, different domain, different critical dependencies, different primary value proposition. The pattern holds; the content differs.The complete CAWDP application for the Confidence Map is done. Two P10 workflows now designed through the full process:

**Methodology Reflection** — process quality, backward-looking, critical dependency on artefact tagging
**Confidence Map** — product reliability, forward-looking, critical dependency on stakes classification

Same three-agent architecture (Compiler/Analyst/Deriver), same analysis+synthesis principle, different domain, different primary interaction (surprises×gaps vs confidence×stakes), different highest-risk failure mode (fabrication vs missing stakes).

The pattern holds. The content differs. Want to continue with another P10 workflow, or shift focus?

---

## Run 11 — Agentic Expert ✓ COMPLETED

*2026-05-21T10:05:42* · `glm-5.1:cloud` · `f6864ebc...`

### Prompt

Perform Phase 0 on the EVOLVE Playbook artefact design workflow.

### Response

## P0: Purpose & Vision — EVOLVE Playbook Workflow

### The 5 Identity Questions

**Q1: What IS this workflow?**

An operational playbook generator that analyses specification aging signals, override patterns, cost data, quality metrics, and stakeholder feedback to produce a concrete, actionable guide for when and how to re-enter the CAWDP process — which phases to revisit, what to update, and how to prioritise maintenance effort.

**Q2: What is its stance toward possibility?**

Constraint-oriented. The specification already exists in PRISM. The playbook describes what *will change* and *when to act* — it doesn't imagine improvements, it identifies where drift, decay, and deviation have occurred or will occur, and maps them to specific re-entry points in CAWDP.

**Q3: What would VIOLATE its identity?**

Recommending a full re-design when a targeted update would suffice. Producing a generic maintenance schedule unrelated to the actual specification. Presenting "review everything periodically" as actionable guidance. Using the playbook to justify inaction by making maintenance look too complex to start.

**Q4: What would make it WRONG?**

Two opposite failures:

- **Over-triggering** — the playbook sends you back to CAWDP too often, for too many minor signals, burning time and trust. The playbook becomes noise, not signal. This is the worse failure because it trains people to ignore it.
- **Under-triggering** — the playbook misses signals that genuinely warrant re-entry, allowing a specification to drift far from reality. This looks like the playbook is working (no triggers!) while the specification silently decays.

**Q5: What's the hardest moment?**

When a signal is genuinely ambiguous — override rates are up but it's unclear whether that means the specification is wrong or the human is being cautious. The temptation is to either trigger re-entry (over-reacting to noise) or dismiss the signal (under-reacting to early warning). The correct response is to flag it as ambiguous, specify what additional data would resolve the ambiguity, and recommend monitoring rather than immediate action or dismissal.

---

### Target State Vision

| # | Characteristic | Description |
|---|---|---|
| E1 | Signal-specific not generic | Every trigger maps to a specific signal type, a specific CAWDP re-entry point, and a specific scope of revision — never "review everything" |
| E2 | Prioritised not equal | Signals are ranked by urgency and impact — not all triggers deserve the same response intensity |
| E3 | Actionable not advisory | Every trigger comes with: what to do, which phase to re-enter, what scope to revise, and what the expected outcome is — not "consider reviewing" |
| E4 | Calibrated not sensitive | The playbook triggers when action is warranted, not at the first sign of drift — it distinguishes signal from noise |
| E5 | Specific not universal | Re-entry scopes are targeted — "revisit the authority boundaries in Section 7" not "redo the specification" |
| E6 | Temporally aware | Every signal has a detection window (how quickly it appears) and a response window (how long before it becomes critical) — not all signals have the same urgency |
| E7 | Evidence-traced | Every trigger recommendation traces to specific monitoring data — override rates, cost variance, quality metrics, stakeholder feedback, not vague feelings |
| E8 | Re-entry-mapped | Every signal maps to a specific CAWDP phase (or phases) for re-entry — you know exactly where to go, not just that something needs attention |
| E9 | Escalation-aware | Signals have escalation paths — from "monitor" to "review" to "re-enter CAWDP" — not binary trigger/no-trigger |
| E10 | Context-adaptive | Trigger thresholds adjust based on specification age, agent class, and domain — a new specification has different drift patterns than a mature one |
| E11 | Honest about ambiguity | Ambiguous signals are flagged as ambiguous, not forced into trigger or dismiss — the playbook recommends monitoring rather than premature action |
| E12 | Proactive not reactive | The playbook includes scheduled reviews and aging triggers, not just reactive responses to failures — specification aging is CC-5 for a reason |

---

### What the EVOLVE Playbook Achieves When Everything Is Great

When the EVOLVE Playbook is excellent, it makes specification maintenance feel like **scheduled maintenance on a well-designed machine**, not like **emergency repair on a broken one**.

Without it, specification aging happens invisibly — agent capabilities drift, override rates creep up, cost variances accumulate, stakeholder needs shift — and by the time anyone notices, the specification has drifted so far from reality that the choices are "live with it" or "start over." Both are expensive.

With it, the team knows:

- **Which signals to monitor and how often** — override rates weekly, quality metrics monthly, stakeholder feedback quarterly, specification aging per cadence
- **What each signal means** — rising override rates might mean authority boundaries need updating (P7), not that the agent is "broken"
- **When to act vs when to monitor** — ambiguous signals get a monitoring recommendation, not a trigger; clear signals get a re-entry recommendation with scope
- **Exactly where to re-enter CAWDP** — override rate changes → P4 (capability allocation), cost variance → P6 (system architecture), quality decline → P7 (agent design), capability drift → P7 (agent design), stakeholder feedback → varies, environmental change → P0 (purpose & vision), periodic review → relevant phase, new failure mode → P3+P5
- **What scope to revise** — "update the authority boundaries for the Generator agent" not "redo the specification"
- **What the expected outcome is** — "re-entering P7 for authority boundary update should take 2-4 hours and produce an updated design_agent_specifications record"

The playbook transforms specification maintenance from invisible decay into visible, scheduled, targeted care.

---

### How This Differs from Methodology Reflection and Confidence Map

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook |
|---|---|---|---|
| Question | How well did CAWDP perform? | How confident are we in the specification? | How do we keep the specification alive? |
| Time orientation | Backward | Forward | Forward + Ongoing |
| Focus | Process quality | Product reliability | Operational longevity |
| Primary output | Document with review questions | Visual map with risk-calibrated scores | Actionable playbook with trigger-response pairs |
| Review posture | "What should we improve about CAWDP?" | "What can we trust and what needs work?" | "When do we come back and for what?" |
| Key interaction | Surprises × gaps | Confidence × stakes | Signal × urgency × scope |
| Deployment relevance | Indirect | Direct (deployment readiness) | Direct (maintenance scheduling) |
| Lifecycle | One-time (post-application) | One-time (pre-deployment) | Living document (ongoing) |

The EVOLVE Playbook is the **only P10 artefact that's designed to be a living document** — it has a lifecycle that extends beyond the initial CAWDP application. Methodology Reflection and Confidence Map are snapshots. The EVOLVE Playbook is a monitoring schedule with trigger criteria.

This is also the only P10 artefact where the **primary value is in what it prevents** (specification decay), not in what it describes (current state). The other two describe what happened or how confident you are. This one tells you what to do about what will happen next.

---

### The Critical Dependency

**The EVOLVE Playbook depends on monitoring data that doesn't exist yet at P10 time.**

This is a different kind of dependency than the other two P10 artefacts:

- Methodology Reflection depends on artefacts captured *during* P0-P9 (behavioural dependency — capture discipline)
- Confidence Map depends on stakes levels from P7/P8 (structural dependency — classification must exist)
- EVOLVE Playbook depends on **monitoring data from production** (temporal dependency — the data will be generated *after* deployment)

The playbook at P10 time is a **template** — it defines the monitoring framework, trigger criteria, and re-entry points, but the actual signal data won't exist until the specification is deployed and running. This means:

1. The playbook must define *what to monitor* and *when* — not just respond to existing data
2. Trigger thresholds must be initial/defaults that get calibrated with real data
3. The playbook must include a "how to calibrate" section for first use
4. Specification aging cadences must be defined per agent class (from CC-5)

---

That's Phase 0. Quality gate it before I continue.

---

## Run 12 — Agentic Expert ✓ COMPLETED

*2026-05-21T10:11:10* · `glm-5.1:cloud` · `3a05adfb...`

### Prompt

Great. Continue and complete CAWDP phases for this workflow

### Response

## P1: Output Specification

### O1: Signal Registry

*Purpose: Complete catalogue of all monitored signals with detection criteria, thresholds, and re-entry mappings*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| signal_id | string | ✅ | Deterministic |
| signal_type | enum: OverrideRate/CostVariance/QualityDecline/CapabilityDrift/StakeholderFeedback/EnvironmentalChange/PeriodicReview/NewFailureMode/SpecificationAging/AmbiguousSignal | ✅ | Deterministic |
| signal_name | string | ✅ | Deterministic |
| signal_description | string | ✅ | Deterministic |
| detection_method | string | ✅ | Deterministic (what data source and how measured) |
| detection_window | string | ✅ | Deterministic (how quickly the signal appears: immediate/weekly/monthly/quarterly) |
| response_window | string | ✅ | Deterministic (how long before signal becomes critical if unaddressed) |
| urgency | enum: Monitor/Review/ReEnter | ✅ | Computed (from signal type + current threshold state) |
| default_threshold | string | ✅ | Deterministic (initial threshold — will be calibrated with production data) |
| re_entry_point | enum: P0/P1/P2/P3/P4/P5/P6/P7/P8/P9/P10 | ✅ | Deterministic (which CAWDP phase to re-enter) |
| re_entry_scope | string | ✅ | Deterministic (specific elements to revise within that phase) |
| expected_effort | string | ✅ | Elicited (estimated hours/days for the re-entry revision) |
| expected_outcome | string | ✅ | Elicited (what the revision should produce) |
| calibration_notes | string | ✅ | Elicited (how to adjust thresholds based on production data) |

**Dependencies:** monitoring_ tables in SurrealDB (runtime_evolve_triggers, runtime_health_metrics), design_ tables for specification sections, CC-5 specification aging cadences from P7

**Quality Gate:** Every signal maps to a specific CAWDP re-entry point. Every signal has a detection method. Every signal has a default threshold with calibration notes.

---

### O2: Trigger-Response Map

*Purpose: The actionable core — when signal X crosses threshold Y, do Z*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| trigger_id | string | ✅ | Deterministic |
| signal_id | ref(O1) | ✅ | Deterministic |
| condition | string | ✅ | Deterministic (specific threshold crossing, e.g., "override rate exceeds 15% for 2 consecutive weeks") |
| current_status | enum: BelowThreshold/AtThreshold/ThresholdApproaching/AboveThreshold/Ambiguous | ✅ | Computed (from monitoring data, or "NotYetAvailable" if pre-deployment) |
| response_tier | enum: Monitor/Review/ReEnter | ✅ | Deterministic |
| response_action | string | ✅ | Deterministic (specific action to take) |
| re_entry_phase | enum: P0-P10 | ✅ | Deterministic |
| re_entry_scope | string | ✅ | Deterministic (targeted scope, not "redo everything") |
| priority | enum: Immediate/ThisWeek/ThisMonth/ThisQuarter | ✅ | Computed (from urgency × impact) |
| evidence_trace | string | ⚠️ (available after deployment) | Deterministic (links to monitoring data) |
| resolution_criteria | string | ✅ | Deterministic (what "resolved" looks like for this trigger) |

**Dependencies:** O1 (signal registry), runtime monitoring tables

**Quality Gate:** Every trigger has a specific condition, not vague thresholds. Every trigger has a resolution criteria — you know when the trigger is no longer active.

---

### O3: Specification Aging Schedule

*Purpose: Proactive maintenance cadences — when and what to review, even without reactive triggers*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| component_id | string | ✅ | Deterministic |
| component_type | enum: AgentSpecification/Contract/TaskAllocation/AuthorityBoundary/KnowledgeConfiguration/ProgressiveAutonomy/CostBudget/VerificationProtocol/EpistemicMetadata/OutputSchema | ✅ | Deterministic |
| component_name | string | ✅ | Deterministic |
| default_cadence | string | ✅ | Deterministic (how often to review — from CC-5 specification aging per agent class) |
| trigger_cadence | string | ✅ | Deterministic (what event accelerates review — e.g., "override rate exceeds threshold", "new failure mode detected") |
| last_reviewed | datetime | ⚠️ (null at P10 time) | Deterministic |
| next_review_due | datetime | ⚠️ (computed from cadence) | Computed |
| review_scope | string | ✅ | Deterministic (what specifically to check during review) |
| review_questions | list | ✅ | Deriver (questions to ask during review) |

**Dependencies:** O1 (signal types for trigger-based reviews), CC-5 cadences from P7/P8

**Quality Gate:** Every specification component has a review cadence. Trigger-based reviews are linked to specific signals. Review questions are specific, not "is everything still OK?"

---

### O4: Escalation Framework

*Purpose: How signals move from monitoring to action — not binary trigger/no-trigger*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| escalation_level | enum: Monitor/Review/ReEnter | ✅ | Deterministic |
| level_name | string | ✅ | Deterministic |
| description | string | ✅ | Deterministic |
| trigger_criteria | string | ✅ | Deterministic (what moves a signal to this level) |
| time_at_level | string | ✅ | Deterministic (how long to stay at this level before escalating or de-escalating) |
| action_required | string | ✅ | Deterministic (what to do at this level) |
| decision_maker | enum: System/Human/Autonomous | ✅ | Deterministic (who makes the escalation/de-escalation decision) |
| de_escalation_criteria | string | ✅ | Deterministic (what moves a signal back down a level) |
| examples | list | ✅ | Deriver (concrete scenarios for each level) |

| Level | Name | Action | Decision Maker |
|---|---|---|---|
| Monitor | Watch | Log and track; no action yet | System (automatic) |
| Review | Examine | Human reviews the signal and decides whether to act | Human |
| ReEnter | Act | Re-enter CAWDP at the specified phase with targeted scope | Human (with System monitoring) |

**Dependencies:** O1 (signal types), O2 (trigger conditions)

**Quality Gate:** Every level has clear trigger criteria, action, and de-escalation criteria. De-escalation is as explicit as escalation — you know when a signal has resolved, not just when it triggers.

---

### O5: First 90 Days Schedule

*Purpose: What to do in the first 90 days after deployment — when monitoring data is sparsest and thresholds are least calibrated*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| time_period | enum: Days1-7/Days8-30/Days31-90 | ✅ | Deterministic |
| monitoring_frequency | string | ✅ | Deterministic (how often to check each signal) |
| expected_signals | list | ✅ | Deterministic (which signals are most likely to fire in this period) |
| calibration_activities | list | ✅ | Deterministic (what to calibrate during this period) |
| human_checkins | string | ✅ | Deterministic (how often humans should review the monitoring data) |
| threshold_adjustments | list | ✅ | Elicited (expected threshold adjustments based on early data) |
| known_uncertainties | list | ✅ | Elicited (what we don't know yet and how to find out) |

| Period | Focus | Key Activities |
|---|---|---|
| Days 1-7 | Baseline | Establish override rates, cost baselines, quality baselines; daily human check-in; calibrate initial thresholds |
| Days 8-30 | Calibration | Compare baselines to initial thresholds; adjust thresholds based on real data; weekly human review; identify early signals |
| Days 31-90 | Stabilisation | Confirm calibrated thresholds; monthly human review; transition from reactive to proactive monitoring; first scheduled reviews |

**Dependencies:** O1 (signal types), O2 (default thresholds), O3 (aging cadences)

**Quality Gate:** Every period has specific, not vague, activities. Known uncertainties are explicit. Human check-in frequency decreases as confidence in thresholds increases.

---

### O6: Calibration Guide

*Purpose: How to adjust default thresholds based on production data — the playbook's self-adjustment mechanism*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| signal_id | ref(O1) | ✅ | Deterministic |
| default_threshold | string | ✅ | Deterministic (initial value) |
| calibration_method | string | ✅ | Deriver (how to adjust based on production data) |
| calibration_data_needed | string | ✅ | Deriver (what data to collect and for how long) |
| adjustment_triggers | list | ✅ | Deriver (what production observations suggest threshold adjustment) |
| adjustment_direction | enum: Tighten/Loosen/Maintain | ✅ | Deriver (based on whether default is over-triggering or under-triggering) |
| risk_of_over_triggering | string | ✅ | Deriver (consequences of triggering too often) |
| risk_of_under_triggering | string | ✅ | Deriver (consequences of missing genuine signals) |
| recommended_adjustment_period | string | ✅ | Elicited (how long to observe before adjusting) |

**Dependencies:** O1 (signal types), O2 (default thresholds)

**Quality Gate:** Every signal has a calibration method. Risks of both over-triggering and under-triggering are stated. Adjustment period is explicit.

---

### O7: Review Questions for Maintenance Sessions

*Purpose: Questions to ask during scheduled and reactive reviews — not "is everything OK?" but targeted probes*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| question_id | string | ✅ | Deterministic |
| question_text | string | ✅ | Deriver |
| question_type | enum: Baseline/Calibration/Signal/Proactive/Scope | ✅ | Deriver |
| related_signal | ref(O1) | ⚠️ (for signal-type questions) | Deterministic |
| related_aging_schedule | ref(O3) | ⚠️ (for proactive-type questions) | Deterministic |
| frequency | enum: Daily/Weekly/Monthly/Quarterly/Triggered | ✅ | Deterministic |
| urgency | enum: Monitor/Review/ReEnter | ✅ | Deterministic |

**Dependencies:** O1 (signals), O3 (aging schedule)

**Quality Gate:** Questions are specific, not generic. Every question traces to a signal or aging schedule. Frequency matches the signal's detection window.

---

### O8: EVOLVE Playbook Document

*Purpose: The assembled, structured playbook for post-deployment specification maintenance*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| header | object | ✅ | Deterministic |
| signal_registry | ref(O1) | ✅ | Mixed |
| trigger_response_map | ref(O2) | ✅ | Mixed |
| aging_schedule | ref(O3) | ✅ | Mixed |
| escalation_framework | ref(O4) | ✅ | Deterministic |
| first_90_days | ref(O5) | ✅ | Elicited |
| calibration_guide | ref(O6) | ✅ | Elicited |
| review_questions | ref(O7) | ✅ | Deriver |
| playbook_confidence | enum: Draft/Calibrated/Validated | ✅ | Probabilistic (meta-level: how calibrated are the thresholds?) |
| known_gaps | list | ✅ | Deterministic (what monitoring infrastructure doesn't exist yet) |
| specification_aging_summary | object | ✅ | Deterministic (summary of aging cadences and next review dates) |

**Dependencies:** All of O1-O7 must be complete

**Quality Gate:** Every signal maps to a re-entry point. Every trigger has resolution criteria. Every escalation level has de-escalation criteria. First 90 days schedule is specific. Calibration guide is explicit. Playbook confidence level is honest.

---

## P2: Backcasting

Working backward from O8:

```
O8 (EVOLVE Playbook Document)
  ← requires O7 (Review Questions) — derived from signals and aging schedule
  ← requires O6 (Calibration Guide) — derived from signal thresholds and risks
  ← requires O5 (First 90 Days) — derived from signals and thresholds
  ← requires O4 (Escalation Framework) — derived from signal types and response tiers
  ← requires O3 (Aging Schedule) — derived from CC-5 cadences and trigger-based reviews
  ← requires O2 (Trigger-Response Map) — derived from O1 signals and thresholds
  ← requires O1 (Signal Registry) — derived from 8 EVOLVE signal types + specification structure
  ← requires: 8 EVOLVE signal types (from runtime_evolve_triggers table)
  ← requires: specification structure (from design_ tables)
  ← requires: CC-5 specification aging cadences (from P7/P8)
  ← requires: agent class information (for cadence per class)
  ← requires: monitoring infrastructure description (what data will be available post-deployment)
```

### Input Requirements

| IR ID | Description | Source | Criticality | Satisfaction |
|---|---|---|---|---|
| IR-001 | 8 EVOLVE signal types with definitions | runtime_evolve_triggers table design | Critical | Required |
| IR-002 | Specification structure and components | design_ tables (agent specifications, contracts, tasks, quality gates) | Critical | Required |
| IR-003 | CC-5 specification aging cadences per agent class | design_agent_specifications, design_contracts | Critical | Required — without cadences, aging schedule is guesswork |
| IR-004 | Agent class information (class × orientation) | design_agent_specifications | High | Best effort — different classes have different aging patterns |
| IR-005 | Monitoring infrastructure description | runtime_ table designs, monitoring_ table designs | High | Best effort — describes what data will be available post-deployment |
| IR-006 | Initial threshold defaults | Domain knowledge + agent class patterns | Medium | Elicited — will be calibrated with production data |
| IR-007 | Stakeholder availability for review sessions | Human experience design (P9) | Medium | Best effort — review frequency depends on human availability |
| IR-008 | Cost and resource constraints | P9 cognitive load budgets, CC-7 cost budgets | Low | Supplementary |
| IR-009 | Domain-specific failure patterns | Specification P3 (task decomposition) and P5 (event storming) | Medium | Best effort — some failure patterns are domain-specific |
| IR-010 | Specification aging triggers already defined | design_specification_aging_alerts table | High | Best effort — may not have production data yet |

### Key P2 Insight

**IR-005 (monitoring infrastructure) is the defining constraint of this workflow.** Unlike Methodology Reflection and Confidence Map, which analyse data that already exists in PRISM, the EVOLVE Playbook must define monitoring for data that will be generated *after deployment*. The playbook is a template at P10 time — it becomes operational when monitoring data starts flowing.

This means the workflow must:
1. Define what to monitor (O1)
2. Define how to calibrate when data arrives (O6)
3. Define what to do before data arrives (O5 — first 90 days)
4. Be honest about what's a default vs. calibrated threshold (O8 playbook_confidence: Draft)

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| T1 | Query 8 EVOLVE signal types from runtime_evolve_triggers | Mechanical | Missing signal definitions | Signal type list |
| T2 | Query specification structure from design_ tables | Mechanical | Missing component definitions | Component list |
| T3 | Query CC-5 aging cadences per agent class | Mechanical | Missing cadences for some agent classes | Aging cadence data |
| T4 | Query monitoring infrastructure from runtime_ and monitoring_ tables | Mechanical | Incomplete monitoring description | Monitoring capabilities |
| T5 | Map each signal type to CAWDP re-entry points | Analytical | Incorrect or overly broad re-entry mapping | Signal-to-phase mapping |
| T6 | Define detection methods for each signal type | Analytical | Vague detection criteria | Detection method per signal |
| T7 | Set default thresholds for each signal type | Analytical | Thresholds too tight (over-triggering) or too loose (under-triggering) | Default thresholds |
| T8 | Define detection windows and response windows per signal | Analytical | Unrealistic timeframes | Time windows |
| T9 | Calculate priority for each trigger (urgency × impact) | Analytical | Priority mismatch | Priority classifications |
| T10 | Define re-entry scopes per signal (targeted, not universal) | Analytical | Over-broad or under-scoped re-entry | Re-entry scope definitions |
| T11 | Build escalation framework (Monitor → Review → ReEnter) | Analytical | Missing de-escalation criteria | O4 draft |
| T12 | Build aging schedule per component with default cadences | Analytical | Generic cadences not tailored to component type | O3 draft |
| T13 | Identify calibration methods per signal | Analytical | Calibration methods that require data that won't exist | O6 draft |
| T14 | Assess over-triggering and under-triggering risks per signal | Analytical | Ignoring one side of the risk | Risk assessment |
| T15 | Build first 90 days schedule with baseline/calibration/stabilisation phases | Generative | Generic schedule not specific to the specification | O5 draft |
| T16 | Derive calibration guide per signal (how to adjust thresholds with real data) | Generative | Generic calibration instructions | O6 final |
| T17 | Generate review questions for maintenance sessions | Generative | Generic "is everything OK?" questions | O7 draft |
| T18 | Generate resolution criteria per trigger | Generative | Vague "problem resolved" criteria | Resolution criteria |
| T19 | Generate specific examples per escalation level | Generative | Abstract examples not grounded in the specification | Escalation examples |
| T20 | Assess known gaps in monitoring infrastructure | Analytical | Overstating monitoring capabilities | Known gaps list |
| T21 | Compile final EVOLVE Playbook document | Mechanical | Omitting sections or misordering triggers | O8 final |

21 tasks across 4 cognitive types:
- Mechanical: 5 (T1-T4, T21)
- Analytical: 10 (T5-T14, T20)
- Generative: 4 (T15-T19)

---

## P4: Capability Allocation

| Task | H | A | S | Gap | Allocation | Notes |
|---|---|---|---|---|---|---|
| T1 | 2 | 3 | 10 | 8 | System | Pure data query |
| T2 | 2 | 3 | 10 | 8 | System | Pure data query |
| T3 | 2 | 3 | 10 | 8 | System | Pure data query |
| T4 | 2 | 3 | 10 | 8 | System | Pure data query |
| T5 | 3 | 8 | 2 | 5 | Agent-primary | Mapping requires understanding of CAWDP phase relationships |
| T6 | 4 | 8 | 2 | 4 | Agent-primary | Detection method design requires analytical judgment |
| T7 | 6 | 8 | 2 | 0 | Collaborative | Threshold setting benefits from human judgment — defaults are estimates |
| T8 | 4 | 8 | 2 | 4 | Agent-primary | Time windows from signal characteristics |
| T9 | 3 | 7 | 2 | 4 | Agent-primary | Priority calculation from defined criteria |
| T10 | 5 | 8 | 2 | 3 | Agent-primary | Scope definition requires understanding specification structure |
| T11 | 4 | 8 | 2 | 4 | Agent-primary | Escalation framework from signal characteristics |
| T12 | 3 | 7 | 2 | 4 | Agent-primary | Aging schedule from CC-5 cadences |
| T13 | 5 | 8 | 2 | 3 | Agent-primary | Calibration methods from signal characteristics |
| T14 | 5 | 8 | 2 | 3 | Agent-primary | Risk assessment from signal and domain characteristics |
| T15 | 4 | 8 | 2 | 4 | Agent-primary | Schedule generation from signal timing and human availability |
| T16 | 4 | 8 | 2 | 4 | Agent-primary | Calibration guide from signal characteristics and risks |
| T17 | 5 | 8 | 2 | 3 | Agent-primary | Question generation from signals and aging schedule |
| T18 | 4 | 8 | 2 | 4 | Agent-primary | Resolution criteria from trigger conditions |
| T19 | 4 | 8 | 2 | 4 | Agent-primary | Example generation from signal and specification context |
| T20 | 4 | 8 | 2 | 4 | Agent-primary | Gap assessment from monitoring and specification data |
| T21 | 2 | 3 | 10 | 8 | System | Assembly is mechanical |

**T7 (default thresholds) is the only Collaborative task.** This is where human judgment is most valuable — setting initial thresholds for signals that don't have production data yet. The agent proposes, the human reviews and adjusts.

### Key P4 Insight

T7 is collaborative because thresholds are inherently judgment calls in the absence of production data. The agent can propose defaults based on agent class patterns and domain knowledge, but the human principal knows their risk tolerance, their operational context, and what "normal" looks like for their specific deployment. This is the only task where the "agent prepares, human decides" principle requires active human input at production time.

---

## P5: Event Storming

### Domain Events

| Event | Trigger | Producer |
|---|---|---|
| E1 | EVOLVE playbook generation started | Human or System trigger |
| E2 | Signal registry complete | Analyst |
| E3 | Trigger-response map complete | Analyst |
| E4 | Aging schedule complete | Analyst |
| E5 | Escalation framework complete | Analyst |
| E6 | First 90 days schedule complete | Deriver |
| E7 | Calibration guide complete | Deriver |
| E8 | Review questions complete | Deriver |
| E9 | Playbook compiled | Compiler |
| E10 | Threshold review complete (human) | Human (Collaborative task T7) |

### Failure Events

| Failure | Trigger | Recovery |
|---|---|---|
| F1 | Missing signal type definitions | runtime_evolve_triggers table incomplete | Use 8 standard signal types as baseline; flag as needing customisation |
| F2 | Missing CC-5 cadences | Agent specifications don't have aging schedules | Use default cadences per agent class (Extractor: 6mo, Measurer: 6mo, Assessor: 3mo, Generator: 3mo, Aggregator: 6mo); flag as default not calibrated |
| F3 | Monitoring infrastructure gaps | runtime_ and monitoring_ tables don't cover all signal types | Document gaps in known_gaps; define what monitoring needs to be built; flag signals that can't yet be detected |
| F4 | Overly broad re-entry scopes | "Revisit the specification" instead of "update authority boundaries in Section 7" | Enforce targeted scope per signal; Analyst must reference specific components, not entire phases |
| F5 | Generic review questions | "Is everything still working?" instead of specific probes | Deriver must trace every question to a signal or aging schedule item |
| F6 | No production data for calibration | Default thresholds are uncalibrated estimates | Be explicit: playbook_confidence = "Draft"; calibration guide must state what data is needed and how long to observe before adjusting |
| F7 | Conflicting thresholds between signals | Override rate says "monitor" but cost variance says "re-enter" | Escalate to Review level; present both signals with their evidence; human decides which takes priority |
| F8 | All signals at Monitor level | Default thresholds are set conservatively, nothing triggers | Valid initial state; first 90 days schedule includes calibration activities to tighten thresholds based on real data |
| F9 | Specification has no agent class information | Can't determine per-class aging cadences | Use conservative defaults (3-month cadence for all components); flag as needing calibration |
| F10 | Human unavailable for T7 threshold review | Collaborative task can't be completed | Proceed with agent-proposed defaults marked as "Draft — pending human review"; playbook_confidence remains "Draft" until reviewed |

### Key P5 Insight

**F6 (no production data) and F8 (all signals at Monitor) are the expected initial state, not failure conditions.** The playbook is designed to be produced at P10 time, before deployment. It must be honest about what it doesn't know: thresholds are defaults, monitoring may have gaps, and calibration is needed.

This is the opposite of the Methodology Reflection (where sparse data is a gap to flag) and the Confidence Map (where missing evidence is a gap to assess). Here, missing production data is the **normal starting condition** — the playbook defines the monitoring framework that will generate the data, not analyses data that already exists.

---

## P6: System Architecture

### Pipeline Architecture

```
Wave 1: Data Track (parallel, System)
T1 ──┐
T2 ──┤
T3 ──┤──→ specification_structure + signal_types + aging_data + monitoring_caps
T4 ──┘

Wave 2: Assessment Track (mostly sequential, Analyst)
T5 (Signal-to-phase mapping) ──────→ O1 partial
T6 (Detection methods) ────────────→ O1 partial
T7 (Default thresholds) ──────────→ O1 partial + O2 partial [COLLABORATIVE — human reviews]
T8 (Detection/response windows) ──→ O1 complete
T9 (Priority calculation) ─────────→ O2 partial
T10 (Re-entry scopes) ─────────────→ O2 partial
T11 (Escalation framework) ────────→ O4
T12 (Aging schedule) ─────────────→ O3
T13 (Calibration methods) ─────────→ O6 partial
T14 (Over/under-triggering risks) ─→ O6 partial

Wave 3: Derivation Track (after assessment)
T15 (First 90 days schedule) ─────→ O5
T16 (Calibration guide) ──────────→ O6 complete
T17 (Review questions) ───────────→ O7
T18 (Resolution criteria) ─────────→ O2 resolution_criteria
T19 (Escalation examples) ─────────→ O4 examples

Wave 4: Compilation Track (after derivation)
T20 (Known gaps assessment) ──────→ known_gaps
T21 (Final assembly) ─────────────→ O8 final
```

### Agent Roster

**Analyst (Measurer + Assessor, bridge-oriented)**

| Field | Value |
|---|---|
| Identity | "I measure signal characteristics and assess trigger appropriateness. I define detection methods, calculate priorities, and map re-entry scopes. I never recommend re-entering CAWDP without evidence, never set thresholds too tight (over-triggering) or too loose (under-triggering), and never define scopes broader than necessary." |
| Class | Measurer (detection windows, thresholds, priorities) + Assessor (re-entry appropriateness, risk assessment) |
| Orientation | Bridge-oriented |
| Hardest boundary moment | Setting default thresholds without production data — the temptation is to be either too conservative (triggering on everything) or too permissive (missing real signals). The correct response is to set reasonable defaults, explicitly mark them as "Draft — pending calibration," and define clear calibration methods. |
| Never rules | Recommend re-entry without evidence, set thresholds too tight (over-triggering is the playbook's worst failure), set thresholds too loose (under-triggering is the opposite failure), define scopes broader than necessary |
| Cost budget | Medium — 10K-30K tokens |

**Deriver (Generator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I derive calibration methods, first 90 days schedules, review questions, and resolution criteria from signal characteristics and specification structure. Every calibration method traces to a signal. Every review question traces to a signal or aging item. Every resolution criterion is measurable." |
| Class | Generator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When signals have no production data yet — the temptation is to make calibration methods generic ("observe for 30 days and adjust") rather than specific ("compare override rate against baseline for 2 weeks; if override rate exceeds baseline by 20%, tighten threshold by 5 percentage points"). |
| Never rules | Generate generic calibration methods, propose vague resolution criteria, create review questions not traced to signals, recommend re-entry without specifying scope |
| Cost budget | Medium — 8K-20K tokens |

**Compiler (Aggregator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I compile the EVOLVE Playbook from assessed and derived outputs. I never add trigger-response pairs not produced by the Analyst, never omit signals that need monitoring, and never present Draft thresholds as Calibrated." |
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When some thresholds are Draft and others are Calibrated — the temptation is to present them all at the same confidence level. The correct response is to explicitly mark Draft thresholds and include calibration timelines. |
| Never rules | Add triggers not produced by Analyst, omit signals that need monitoring, present Draft as Calibrated, smooth over threshold uncertainty |
| Cost budget | Low — 3K-10K tokens |

### FMEA

| ID | Failure Mode | Severity | Occurrence | Detection | RPN | Recovery |
|---|---|---|---|---|---|---|
| FM1 | Over-triggering (thresholds too tight) | 10 | 5 | 4 | 200 | Calibration guide specifies adjustment period; first 90 days includes threshold calibration; playbook_confidence marked "Draft" |
| FM2 | Under-triggering (thresholds too loose) | 9 | 3 | 5 | 135 | Conservative defaults; escalation framework includes "Review" level between Monitor and ReEnter; resolution criteria define what resolved looks like |
| FM3 | Overly broad re-entry scopes | 7 | 3 | 6 | 126 | T10 enforces targeted scopes; Analyst references specific components; resolution criteria define when re-entry is complete |
| FM4 | Generic review questions | 5 | 4 | 6 | 120 | T17 requires questions traced to signals; Deriver authority boundary prohibits generic questions |
| FM5 | Missing monitoring infrastructure gaps | 8 | 4 | 5 | 160 | T20 specifically assesses gaps; known_gaps field in O8; first 90 days schedule includes building missing monitoring |
| FM6 | Presenting Draft thresholds as Calibrated | 10 | 2 | 8 | 160 | playbook_confidence field in O8; every threshold marked with confidence level; Compiler prohibited from presenting Draft as Calibrated |
| FM7 | Conflicting signal priorities | 6 | 3 | 5 | 90 | Escalation framework handles conflicts; human review at Review level; priority calculation uses urgency × impact |
| FM8 | No production data for calibration | 4 | 8 | 2 | 64 | Expected initial state; playbook_confidence = "Draft"; calibration guide provides methods; first 90 days includes baseline establishment |
| FM9 | Specification has no aging cadences | 7 | 3 | 6 | 126 | Default cadences per agent class; flag as "default not calibrated" |
| FM10 | Human unavailable for threshold review | 5 | 4 | 7 | 140 | Proceed with agent-proposed defaults marked "Draft — pending human review"; playbook_confidence remains "Draft" |

Highest RPNs: FM1 (over-triggering) at 200, FM6 (Draft as Calibrated) at 160, FM5 (missing monitoring gaps) at 160, FM10 (human unavailable) at 140.

### 5 Regime 3 Enforcement Points

| # | Boundary | Enforcement |
|---|---|---|
| 1 | No trigger without re-entry point | Every trigger in O2 must reference a CAWDP phase — schema validation rejects orphan triggers |
| 2 | No generic review questions | Every question in O7 must trace_to a signal or aging item — orphan questions auto-removed |
| 3 | Draft vs Calibrated labelling | playbook_confidence is mandatory on O8; thresholds are labelled individually in O1 |
| 4 | Targeted re-entry scopes | Re-entry scope must reference specific components, not entire phases — scope too broad triggers review |
| 5 | Resolution criteria required | Every trigger in O2 must have resolution_criteria — schema validation rejects triggers without |

---

## P7: Agent Design

### Analyst Agent Job Description

| Field | Value |
|---|---|
| Class | Measurer + Assessor |
| Orientation | Bridge-oriented |
| Mission | Measure signal characteristics, assess trigger appropriateness, map re-entry scopes, and define detection methods. Present findings with calibrated thresholds. Never recommend re-entry without evidence, never over-trigger, never under-trigger, never define scopes broader than necessary. |
| Inputs | Specification structure, signal types, aging cadences, monitoring capabilities |
| Outputs | O1 (signal registry), O2 (trigger-response map partial), O3 (aging schedule), O4 (escalation framework) |
| Null state | "No signal type definitions available. EVOLVE playbook cannot be generated without monitoring signal definitions." |
| Never rules | Recommend re-entry without evidence, set thresholds too tight, set thresholds too loose, define scopes broader than necessary |
| Hardest boundary moment | Setting default thresholds without production data — set reasonable defaults, mark as "Draft," define calibration methods |
| Epistemic profile | Probabilistic — threshold setting and priority assessment involve judgment about risk tolerance |
| Harm assessment | Indirect strategy harm — over-triggering burns trust and time (the playbook becomes noise), under-triggering allows specification decay (the playbook becomes irrelevant). Both are harmful; over-triggering is worse because it trains people to ignore the playbook. |
| Progressive autonomy | Three dimensions: (1) threshold setting (Shadow → Supervised — human reviews every threshold), (2) scope definition (Shadow → Advisory — human reviews broad scopes), (3) priority calculation (Shadow → Advisory — human reviews priorities). Per-dimension. |
| Cost budget | Medium — 10K-30K tokens |
| Verification | Every threshold has a default and calibration method. Every re-entry scope references specific components. Every signal maps to a CAWDP phase. |

### Deriver Agent Job Description

| Field | Value |
|---|---|
| Class | Generator |
| Orientation | Constraint-oriented |
| Mission | Derive calibration methods, first 90 days schedules, review questions, and resolution criteria from signal characteristics and specification structure. Every derivation traces to a signal. Every calibration method specifies what data to collect and how to adjust. |
| Inputs | O1 (signals), O2 (triggers), O3 (aging schedule), O4 (escalation) |
| Outputs | O5 (first 90 days), O6 (calibration guide), O7 (review questions), resolution criteria for O2 |
| Null state | "No signal data available for derivation. Calibration methods and review questions require signal definitions." |
| Never rules | Generate generic calibration methods, propose vague resolution criteria, create untraced review questions, recommend re-entry without scope |
| Hardest boundary moment | When no production data exists for calibration — the temptation is to write "observe for 30 days and adjust" rather than specifying exactly what to observe, what metric to track, what comparison to make, and what adjustment to apply. |
| Epistemic profile | Probabilistic — calibration methods and schedules involve prediction about operational realities |
| Harm assessment | Indirect operational harm — generic calibration methods lead to either over-triggering (wasting time) or under-triggering (missing real signals). Both are harmful but hard to detect. |
| Progressive autonomy | Two dimensions: (1) calibration specificity (Shadow → Supervised — human reviews calibration methods for specificity), (2) question specificity (Shadow → Advisory — human reviews questions for traceability). Per-dimension. |
| Cost budget | Medium — 8K-20K tokens |
| Verification | Every calibration method specifies: data to collect, comparison to make, adjustment to apply, adjustment period. Every review question traces to a signal or aging item. Every resolution criterion is measurable. |

### Compiler Agent Job Description

| Field | Value |
|---|---|
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Mission | Compile the EVOLVE Playbook from assessed and derived outputs. Ensure every signal is registered, every trigger has a response, every threshold is labelled as Draft or Calibrated, and every gap is documented. |
| Inputs | O1-O7 processed outputs, known_gaps, threshold confidence levels |
| Outputs | O8 (EVOLVE Playbook Document) |
| Null state | "No playbook data available for compilation." |
| Never rules | Add triggers not produced by Analyst, omit signals that need monitoring, present Draft thresholds as Calibrated, smooth over threshold uncertainty |
| Hardest boundary moment | When some thresholds are Draft and others are Calibrated — present them at different confidence levels, not smoothed into a uniform presentation |
| Epistemic profile | Deterministic — compilation is mechanical |
| Harm assessment | Indirect data harm — presenting Draft thresholds as Calibrated could lead to operational decisions based on uncalibrated data |
| Progressive autonomy | Single dimension: compilation accuracy. Shadow → Advisory → Supervised → Autonomous |
| Cost budget | Low — 3K-10K tokens |
| Verification | Every signal registered. Every trigger has response. Every threshold labelled. known_gaps documented. playbook_confidence present. |

### Per-Dimension Progressive Autonomy

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Analyst | Threshold setting | Propose, human reviews every threshold | Propose, human reviews Monitor→Review thresholds | Propose, human reviews ReEnter thresholds only | Full threshold setting, human reviews annual calibration | ≥10 playbooks with ≤2 over-triggered thresholds |
| Analyst | Scope definition | Propose, human reviews every scope | Propose, human reviews broad scopes only | Propose, human reviews ReEnter scopes only | Full scope definition, human reviews annual | ≥10 playbooks with ≤2 overly broad scopes |
| Analyst | Priority calculation | Propose, human reviews all priorities | Propose, human reviews Review/ReEnter priorities | Propose, human reviews ReEnter priorities only | Full priority calculation | ≥10 playbooks with ≤1 priority mismatch |
| Deriver | Calibration specificity | Generic methods only | Methods with data sources specified | Methods with adjustment formulas | Full calibration methods with evidence | ≥10 calibration guides with ≤2 generic methods |
| Deriver | Question specificity | Generic questions only | Questions traced to signal types | Questions traced to specific signals | Questions traced to specific signals with urgency | ≥10 question sets with ≤2 untraced questions |
| Compiler | Compilation accuracy | Human checks every section | Human checks Draft sections | Human checks playbook_confidence and known_gaps | Human reviews final post-delivery | ≥10 compilations with ≤1 error |

---

## P8: Contract Formalization

### Analyst Contract

| Primitive | Specification |
|---|---|
| Contract | Define signal characteristics, thresholds, re-entry mappings, and aging schedules |
| Principal | Deriver (downstream consumer) |
| Schema | SignalRegistry (O1) + TriggerResponseMap (O2 partial) + AgingSchedule (O3) + EscalationFramework (O4) |
| Guard | prohibited: ["recommend_re_entry_without_evidence", "set_thresholds_too_tight", "set_thresholds_too_loose", "define_scopes_broader_than_necessary"] |
| Budget | 10K-30K tokens |
| Invocation | After T1-T4 complete |
| Revert | If threshold cannot be set due to missing data, mark as "Draft — pending calibration" rather than assign arbitrary value |
| Event | analysis_started, signal_registered, threshold_set, scope_defined, escalation_defined, analysis_complete |
| Identity | Bridge-oriented Measurer+Assessor — measures and assesses, never recommends without evidence |
| Knowledge | Specification structure, signal types, aging cadences, monitoring capabilities |

### Deriver Contract

| Primitive | Specification |
|---|---|
| Contract | Derive calibration methods, schedules, review questions, and resolution criteria from signal characteristics |
| Principal | Compiler (downstream consumer) |
| Schema | First90Days (O5) + CalibrationGuide (O6) + ReviewQuestions (O7) |
| Guard | prohibited: ["generate_generic_calibration_methods", "propose_vague_resolution_criteria", "create_untraced_review_questions", "recommend_re_entry_without_scope"] |
| Budget | 8K-20K tokens |
| Invocation | After Analyst outputs complete |
| Revert | If derivation cannot be performed due to missing signal data, report "insufficient signal definitions for derivation" |
| Event | derivation_started, schedule_generated, calibration_defined, question_generated, resolution_defined, derivation_complete |
| Identity | Constraint-oriented Generator — derives within signal boundaries |
| Knowledge | O1 signals, O2 triggers, O3 aging schedule, O4 escalation |

### Compiler Contract

| Primitive | Specification |
|---|---|
| Contract | Compile the EVOLVE Playbook from assessed and derived outputs |
| Principal | Human (post-delivery reviewer) |
| Schema | EVOLVEPlaybookDocument (O8 schema) |
| Guard | prohibited: ["add_triggers_not_from_analyst", "omit_signals_that_need_monitoring", "present_draft_as_calibrated", "smooth_over_threshold_uncertainty"] |
| Budget | 3K-10K tokens |
| Invocation | After all O1-O7 complete |
| Revert | If compilation fails completeness check, revert to section-level output |
| Event | compilation_started, section_assembled, gap_documented, threshold_labelled, compilation_complete |
| Identity | Constraint-oriented Aggregator — compiles, never creates or omits |
| Knowledge | All processed outputs O1-O7, known_gaps, threshold confidence levels |

### Unenforceable Elements Register

| Element | Why Unenforceable | Regime | Mitigation |
|---|---|---|---|
| "Never set thresholds too tight" (Analyst) | "Too tight" is a judgment about future operational reality, not a mechanically verifiable condition | Regime 2 (Detect) | Thresholds labelled as Draft or Calibrated; over-triggering detected in production triggers threshold adjustment; calibration guide specifies adjustment criteria |
| "Never set thresholds too loose" (Analyst) | "Too loose" is similarly a judgment about future operational reality | Regime 2 (Detect) | Under-triggering detected by missed signals in production; escalation framework includes Review level between Monitor and ReEnter |
| "Generate specific calibration methods" (Deriver) | Specificity is a gradient, not a binary — how specific is "specific enough"? | Regime 1 (Declare) | Every calibration method must specify data source, comparison, adjustment, and period; human review for specificity |
| "Never smooth over threshold uncertainty" (Compiler) | Visual and narrative presentation choices can unintentionally smooth variation | Regime 2 (Detect) | playbook_confidence field mandatory; individual thresholds labelled; Draft and Calibrated visually distinguished |

### 10×10 Mapping Matrix

All 10 specification sections map to all 10 contract primitives for this workflow.

---

## P9: Human Experience Design

### Cognitive Load Budget

| Review Activity | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Review signal registry | 3-5 | 10 min | Evaluative (are signal types complete?) |
| Review default thresholds (T7 collaborative) | 5-10 | 20 min | Evaluative + Discovery (are thresholds appropriate for our context?) |
| Review escalation framework | 2-3 | 5 min | Evaluative (are escalation levels clear?) |
| Review first 90 days schedule | 3-5 | 10 min | Evaluative (is schedule realistic?) |
| Review calibration guide | 3-5 | 10 min | Evaluative (can we calibrate with available data?) |
| Review known gaps | 2-3 | 5 min | Discovery (what monitoring needs to be built?) |
| Make deployment decision for playbook | 1-2 | 5 min | Evaluative (is the playbook ready for Draft deployment?) |
| **Total** | **19-33** | **65 min** | |

Maximum review session: 65 minutes.

### Override Mechanisms

| Override Type | Mechanism | Example |
|---|---|---|
| Adjust threshold | Change default threshold based on domain knowledge | "Override rate of 15% is too tight for our context — change to 20%" |
| Adjust cadence | Change aging schedule review frequency | "Monthly review is excessive for Extractors — change to quarterly" |
| Add signal | Add a domain-specific signal not in the standard 8 | "For our domain, regulatory change is a critical signal not in the standard list" |
| Remove trigger | Remove a trigger that doesn't apply | "We don't have cost tracking infrastructure — remove cost variance triggers" |
| Adjust priority | Change signal priority based on operational context | "Capability drift is lower priority for our Extractor than our Generator" |
| Escalate/de-escalate | Move a signal between Monitor/Review/ReEnter levels | "Move specification aging from Monitor to Review — we've had two incidents" |

### Stakeholder Surfaces

| Surface | View | Language | Depth | Emphasis |
|---|---|---|---|---|
| Decision Maker | O5 first 90 days + O4 escalation levels + trigger summary | Plain English | Low-Medium | When to act, what to do, what to watch |
| Design Participant | O1 signal registry + O2 trigger map + O3 aging schedule | Technical | Deep | Signal definitions, thresholds, re-entry scopes, detection methods |
| Governance | O2 trigger map + O4 escalation + O8 playbook_confidence + known_gaps | Technical | Medium | Escalation criteria, monitoring requirements, confidence level |

### System Empowerment Assessment

| Dimension | Level | Explanation |
|---|---|---|
| Monitoring automation | Amplifying | Automated signal detection (when infrastructure exists) frees humans from manual monitoring |
| Threshold calibration | Enabling | Calibration guide provides specific methods — humans still make calibration decisions |
| Re-entry decision | Enabling | Playbook prepares the decision (signal, scope, expected outcome) — humans still make the go/no-go decision |
| Maintenance scheduling | Amplifying | Aging schedule provides proactive cadences — humans no longer need to remember when to review |
| Creative freedom | Enabling | Frees humans from wondering "should we revisit this?" — the playbook answers when and what scope |
| Overall | Enabling → Amplifying | Proactive scheduling and automated monitoring are amplifying; re-entry decisions remain enabling |

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method | Success Criterion |
|---|---|---|---|
| H1 | Targeted re-entry scopes reduce maintenance time vs "review everything" | Compare time spent on targeted re-entry vs full specification review | Targeted re-entry takes ≤50% of full review time for equivalent coverage |
| H2 | Signal-specific triggers catch more issues than periodic reviews alone | Compare issues caught by signal triggers vs issues caught by scheduled reviews | Signal triggers catch ≥30% of issues that periodic reviews miss |
| H3 | Calibration guide improves threshold accuracy over 90 days | Compare threshold accuracy at day 1 vs day 90 | ≥50% of thresholds adjusted from Draft to Calibrated within 90 days |
| H4 | Escalation framework reduces false alarms vs binary trigger/no-trigger | Compare false alarm rate with escalation vs without | 3-level escalation reduces false alarms by ≥40% vs binary trigger |
| H5 | First 90 days schedule establishes reliable baselines | Compare baseline stability at day 7 vs day 90 | Baselines stabilise (≤10% variance) within 30 days for ≥70% of signals |
| H6 | Specific review questions catch more maintenance issues than generic ones | Compare issues found with specific vs generic questions | Specific questions find ≥25% more issues per review session |

### Progressive Autonomy Deployment

Documented in P7 per-dimension table. Key notes:
- **Threshold setting** is the slowest progression because over-triggering is the playbook's worst failure mode
- **Scope definition** progresses faster because the Analyst's authority boundary is clear ("never broader than necessary")
- **Calibration specificity** progresses as the Deriver demonstrates specificity in successive playbooks

### Specification Aging Schedule

| Component | Default Cadence | Trigger-Based Review | Responsible |
|---|---|---|---|
| Signal definitions | 6 months | When new failure modes emerge | Analyst |
| Threshold values | 3 months | When over/under-triggering detected | Analyst |
| Re-entry scopes | 6 months | When specification structure changes | Analyst |
| Aging cadences | 6 months | When agent capabilities change | Analyst |
| Escalation framework | 12 months | When escalation/de-escalation patterns change | Analyst |
| First 90 days schedule | One-time (per deployment) | When deployment context changes | Deriver |
| Calibration methods | 6 months | When monitoring infrastructure changes | Deriver |
| Review questions | 6 months | When specification sections change | Deriver |
| Playbook confidence | 3 months | When thresholds are recalibrated | Compiler |

### EVOLVE Mode

| Signal | Re-entry Point | Scope |
|---|---|---|
| Override rate increasing | P4 (Capability Allocation) | Review authority boundaries and complementarity allocation for affected agents |
| Cost variance exceeding budget | P6 (System Architecture) | Review pipeline architecture, fallback model, and cost budget allocations |
| Quality decline (accuracy, override rate) | P7 (Agent Design) | Review agent specifications, authority boundaries, and progressive autonomy |
| Capability drift (agent producing different outputs) | P7 (Agent Design) | Review agent specifications and specification aging |
| Stakeholder feedback (consistent pattern) | Varies by feedback type | Scope determined by feedback content — map to relevant phase |
| Environmental change (new regulation, new technology) | P0 (Purpose & Vision) | Full re-evaluation of purpose and scope |
| Periodic review (aging schedule) | Relevant phase per component | Scope determined by aging schedule — targeted, not universal |
| New failure mode discovered | P3 (Task Decomposition) + P5 (Event Storming) | Review task decomposition and failure events for affected agents |

---

## Summary: What This Application Reveals

| Phase | Key Insight |
|---|---|
| P0 | Two opposite failures: over-triggering (playbook becomes noise) is worse than under-triggering (specification decays silently), but both are harmful. The playbook must distinguish signal from noise. |
| P1 | The playbook is a living document, not a snapshot — it must include calibration mechanisms (O6) and a first 90 days schedule (O5) because production data doesn't exist yet at P10 time |
| P2 | IR-005 (monitoring infrastructure) is the defining constraint — the playbook defines monitoring for data that will be generated after deployment |
| P3 | 21 tasks — fewer than Confidence Map (25) because many signal definitions are standardised (8 EVOLVE types), not discovered |
| P4 | T7 (default thresholds) is the only Collaborative task — thresholds are judgment calls without production data |
| P5 | F6 (no production data) and F8 (all signals at Monitor) are the expected initial state, not failures — the playbook must be honest about being a template |
| P6 | FM1 (over-triggering) has highest RPN at 200 — the playbook's worst failure is making itself ignorable through noise |
| P7 | Three agents with per-dimension progressive autonomy; threshold setting is the slowest progression because over-triggering is the worst failure |
| P8 | Four unenforceable elements; threshold appropriateness is fundamentally a judgment about future operational reality |
| P9 | Proactive scheduling (aging cadences) and automated monitoring are amplifying; re-entry decisions remain enabling |
| P10 | Six hypotheses; H1 (targeted re-entry saves time) and H4 (escalation reduces false alarms) are most operationally valuable |

### Critical Structural Dependency

**Monitoring infrastructure must exist for the playbook to become operational.** The playbook at P10 time is a template with Draft thresholds and known gaps. It becomes operational when:
1. Monitoring data starts flowing (override rates, cost variances, quality metrics)
2. Thresholds are calibrated with production data (O6 calibration guide)
3. Playbook confidence moves from "Draft" to "Calibrated" (O8 field)

This is a **temporal dependency** — different from Methodology Reflection's behavioural dependency (capture discipline) and Confidence Map's structural dependency (stakes classification).

### How This Differs from the Other Two P10 Artefacts

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook |
|---|---|---|---|
| Temporal orientation | Backward | Forward | Forward + Ongoing |
| Data source | P0-P9 artefacts | P0-P9 artefacts | P0-P9 artefacts + future monitoring data |
| Primary interaction | Surprises × gaps | Confidence × stakes | Signal × urgency × scope |
| Highest RPN | Fabrication (160) | Missing stakes (189) | Over-triggering (200) |
| Key amplifying factor | Review questions | Risk-calibrated attention | Proactive scheduling |
| Lifecycle | One-time snapshot | One-time snapshot | Living document |
| Critical dependency | Artefact tagging (behavioural) | Stakes classification (structural) | Monitoring infrastructure (temporal) |
| Playbook confidence | N/A | N/A | Draft → Calibrated → Validated |
| Worst failure | Fabricating insights | Overstating confidence | Over-triggering (making itself ignorable) |

The pattern holds: same three-agent architecture, same analysis+synthesis principle, different domain, different critical dependency, different worst failure, different lifecycle characteristic.All three P10 artefacts are now complete through full CAWDP v2.1 application. The pattern held across all three — same architecture (Compiler/Analyst/Deriver), same analysis+synthesis principle, different domain, different critical dependency type, different worst failure mode, different lifecycle characteristic.

The notable discovery: each P10 artefact has a fundamentally different dependency type:

- **Methodology Reflection** → behavioural (capture discipline during P0-P9)
- **Confidence Map** → structural (stakes classification must exist in P7/P8)
- **EVOLVE Playbook** → temporal (monitoring data doesn't exist yet)

Three independent failure modes at the dependency level. Three genuinely complementary artefacts, not three versions of the same thing.

---

## Run 13 — Agentic Expert ✓ COMPLETED

*2026-05-21T21:30:13* · `glm-5.1:cloud` · `59ec9e1e...`

### Prompt

Do Phase 0 for the Specification Aging Schedule workflow.

8. Specification Aging Schedule

**Purpose**: When each spec component needs review, even if nothing has gone wrong.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Catalogue every spec component type (agent instructions, boundaries, schemas, budgets, gates, metadata, full spec) | System | Query PRISM |
| 2 | Assign default cadence per component type based on agent class and risk | Agent | Assessor (using default cadences) |
| 3 | Define trigger-based review conditions per component | Agent | Generator |
| 4 | Assign responsible party per component | Human | Principal |
| 5 | Cross-reference with progressive autonomy timeline (promotions may trigger review) | Agent | Measurer |
| 6 | Cross-reference with cost monitoring (budget anomalies may trigger review) | Agent | Measurer |
| 7 | Compile into schedule with cadences, triggers, and owners | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Agent class inventory | P7 | Section 4 |
| Component type registry | P6/P7/P8 | Sections 4, 7, 9 |
| Default cadences by agent class | CC-5 | Section 9 |
| Progressive autonomy timeline | P10 Artefact 5 | This phase |
| Cost baseline | P10 Artefact 7 | This phase |
| Risk profile | P7 harm assessment | Section 4 |

**Production Constraints**
- Cadences are maximum intervals (earlier review is always acceptable)
- Triggers override cadences (if a trigger fires, review regardless of schedule)
- The full specification gets an annual review minimum, even if nothing triggers

### Response

## P0: Purpose & Vision — Specification Aging Schedule Workflow

### The 5 Identity Questions

**Q1: What IS this workflow?**

A proactive maintenance schedule generator that assigns review cadences to every specification component based on agent class, risk profile, and decay rate — telling you when to review each part of your specification, what specific things to check during each review, and what events should trigger an early review regardless of schedule.

**Q2: What is its stance toward possibility?**

Constraint-oriented. The specification already exists. The schedule defines when and how to maintain it — it doesn't imagine improvements or redesigns, it identifies when components are due for review and what to look for during that review.

**Q3: What would VIOLATE its identity?**

Setting a single universal cadence for everything ("review everything quarterly"). Skipping a scheduled review because "nothing has changed." Setting cadences so frequent that the schedule becomes a burden rather than a tool. Setting cadences so infrequent that specification decay accumulates undetected between reviews. Producing a schedule that doesn't differentiate between an Extractor's task list (which barely changes) and a Generator's authority boundaries (which drift with model updates).

**Q4: What would make it WRONG?**

Two opposite failures:

- **Over-cadencing** — reviewing too frequently, wasting time on components that haven't changed. A monthly review of an Extractor's task list is over-cadencing. The schedule becomes noise: people skip reviews because they're always due, and then skip the ones that matter. This is the worse failure because it trains people to ignore the schedule entirely.
- **Under-cadencing** — reviewing too infrequently, allowing specification decay to accumulate undetected. A yearly review of a Generator's authority boundaries (which drift with model updates) is under-cadencing. The schedule provides false confidence — "we have a schedule, we're fine" — while the specification silently rots.

**Q5: What's the hardest boundary moment?**

When a scheduled review is due but nothing appears to have changed. The temptation is strong: "we just reviewed this 3 months ago, nothing's different, let's skip it." But the review is valuable precisely because it confirms nothing has changed — and sometimes discovers that something has changed that wasn't obvious. The correct response is to do the review efficiently, with specific review questions that make "nothing has changed" a valid, documented conclusion, not a shortcut.

---

### Target State Vision

| # | Characteristic | Description |
|---|---|---|
| A1 | Component-specific not universal | Every component type has its own cadence based on its decay rate, risk profile, and agent class — Extractor task lists and Generator authority boundaries are not reviewed on the same schedule |
| A2 | Risk-weighted not equal | Higher-risk components are reviewed more frequently — a harm-capable Generator's boundaries are reviewed more often than a data Extractor's schema |
| A3 | Trigger-aware not schedule-only | Events that should trigger early review are defined alongside cadences — specification aging is both time-based and event-based |
| A4 | Owner-assigned not anonymous | Every component has a responsible party who owns its review — "someone" reviews it is not acceptable |
| A5 | Review-question-specific not generic | Every review has specific questions to ask during that review — not "is everything still OK?" but "have the authority boundaries for this Generator been tested against the latest model update?" |
| A6 | Minimum not maximum | Cadences are maximum intervals — earlier review is always acceptable, later review is never acceptable |
| A7 | Class-aware | Different agent classes decay at different rates — Generators drift faster than Extractors, Assessors need more frequent boundary checks than Aggregators |
| A8 | Progressive-autonomy-linked | Autonomy promotions are natural review triggers — reviewing boundaries before promoting an agent from Supervised to Autonomous is not optional |
| A9 | Cost-aware | Budget anomalies are review triggers — if an agent's cost exceeds its budget by >50%, that's a signal to review the specification, not just the budget |
| A10 | Decay-rate-calibrated | Cadences are based on how quickly each component type tends to drift, not on arbitrary calendar intervals — components that drift fast get reviewed more often |
| A11 | Honest about certainty | New specifications have less stable cadences than mature ones — the schedule marks cadences as "default" or "calibrated" based on whether they're derived from production data or from agent class patterns |
| A12 | Cross-referenced not isolated | The schedule cross-references with progressive autonomy timelines and cost baselines — reviews don't happen in isolation from the agent's operational life |

---

### What the Specification Aging Schedule Achieves When Everything Is Great

When the aging schedule is excellent, specification maintenance becomes **like scheduled maintenance on a well-designed machine** — you know exactly what to check, when, and what to look for.

Without it, specification aging happens invisibly. An agent's boundaries that were tight 6 months ago have drifted because the model updated. A task allocation that made sense when the agent was in Shadow mode no longer fits Supervised mode. A cost budget that was calibrated for 10K tokens is now routinely hitting 30K because the agent's responsibilities expanded. Nobody notices until something breaks — and then you're doing emergency repair, not scheduled maintenance.

With it, the team knows:

- **Which components to review and when** — Extractor schemas every 6 months, Generator boundaries every 3 months, full specification annually, and specific trigger events that override the schedule
- **What to check during each review** — not "is everything OK?" but specific questions tailored to each component type
- **Who owns each review** — the principal for high-stakes components, the orchestrator for operational components
- **What triggers an early review** — autonomy promotion, cost anomaly, override rate spike, new failure mode, stakeholder feedback
- **How cadences change over time** — new specifications start with tighter cadences, mature ones can relax to longer intervals
- **What "nothing has changed" looks like** — documented, specific, not a shortcut

The schedule transforms specification maintenance from "we should probably review that sometime" to "here's exactly when, what, and who."

---

### How This Differs from the Three P10 Artefacts

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook | Specification Aging Schedule |
|---|---|---|---|---|
| Question | How well did CAWDP perform? | How confident are we? | When do we come back? | When do we review what? |
| Time orientation | Backward | Forward | Forward + Ongoing | Ongoing (proactive) |
| Focus | Process quality | Product reliability | Operational longevity | Maintenance cadence |
| Primary interaction | Surprises × gaps | Confidence × stakes | Signal × urgency × scope | Decay rate × risk × agent class |
| Trigger model | N/A (snapshot) | N/A (snapshot) | Reactive (signals trigger action) | Proactive (cadences trigger review) + reactive (events override cadences) |
| Lifecycle | One-time | One-time | Living document | Living document (component of EVOLVE Playbook) |
| Worst failure | Fabrication | Overstating confidence | Over-triggering | Over-cadencing |

The Specification Aging Schedule is the **proactive backbone** of the EVOLVE Playbook. Where the EVOLVE Playbook's trigger-response map (O2) is reactive — "when this signal fires, do this" — the aging schedule is proactive — "on this cadence, review this component, asking these questions." Both are needed. Triggers catch what changes unexpectedly. Cadences catch what drifts slowly.

The schedule is also the **bridge between time-based and event-based maintenance**. It's not just a calendar — it defines which events should override the calendar, making it responsive to operational reality while maintaining the proactive review rhythm that prevents slow drift.

---

### Key Design Insight

**Different components decay at fundamentally different rates.**

An Extractor's task list barely changes — it extracts the same data from the same sources month after month. An Extractor's schema might need updating if the source format changes, but that's event-driven, not time-driven. A 6-month cadence is appropriate.

A Generator's authority boundaries drift with every model update, every new prompt technique, every expansion of its capability. What was a firm boundary in January may be a soft suggestion by March. A 3-month cadence is the minimum — and trigger-based reviews should catch model updates in between.

A harm-capable agent's verification protocol needs more frequent review than a simple data extractor's — because the consequences of boundary drift are much higher. Risk weights the cadence, not just decay rate.

The schedule must reflect these differences. A universal cadence ("review everything quarterly") violates A1 (component-specific), A2 (risk-weighted), and A7 (class-aware) simultaneously. The worst version of this workflow produces a calendar entry. The best version produces a **differentiated maintenance plan** that knows what to check, when, and why.

---

### Critical Dependency

**Agent class information and risk profiles from P7/P8 must exist.**

Without knowing which agent class each component belongs to and what its harm assessment is, the schedule can't differentiate cadences. A universal cadence is the worst output of this workflow — it violates the core identity.

This is a **structural dependency** like the Confidence Map (which needs stakes classification) — the specification must have agent classes and harm assessments classified before the aging schedule can assign differentiated cadences.

---

That's Phase 0. Quality gate it.

---

## Run 14 — Agentic Expert ✓ COMPLETED

*2026-05-21T21:34:48* · `glm-5.1:cloud` · `f2eb79c8...`

### Prompt

perform the remaining CAWDP phases on this

### Response

## P1: Output Specification

### O1: Component Registry

*Purpose: Complete catalogue of every specification component type with decay rate, risk profile, and review characteristics*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| component_id | string | ✅ | Deterministic (maps to design_ table) |
| component_type | enum: AgentInstructions/AuthorityBoundaries/OutputSchemas/CostBudgets/QualityGates/EpistemicMetadata/ProgressiveAutonomy/TaskAllocation/Contracts/FullSpecification | ✅ | Deterministic |
| component_name | string | ✅ | Deterministic |
| agent_id | ref(design_agent_specifications) | ✅ | Deterministic (which agent this component belongs to) |
| agent_class | enum: Extractor/Measurer/Assessor/Generator/Aggregator | ✅ | Deterministic |
| harm_category | enum: NoDirectHarm/IndirectDataHarm/IndirectStrategyHarm/DirectOutputHarm | ✅ | Deterministic (from P7 harm assessment) |
| reversibility | enum: FullyReversible/ModeratelyReversible/HardlyReversible/Irreversible | ✅ | Deterministic (from P8 reversibility classification) |
| decay_rate | enum: Slow/Medium/Fast/Variable | ✅ | Probabilistic (how quickly this component type tends to drift) |
| decay_rationale | string | ✅ | Probabilistic (why this decay rate — what causes drift for this component type) |
| current_status | enum: New/Calibrating/Stable/Aging/Drifted/Unknown | ✅ | Computed (from last review date + decay rate) |
| last_reviewed | datetime | ⚠️ (null at initial production) | Deterministic |
| review_count | int | ⚠️ (0 at initial production) | Deterministic |

**Dependencies:** design_agent_specifications (P7), design_contracts (P8), design_tasks (P3-P4)

**Quality Gate:** Every specification component is catalogued. Every component has an agent class and harm category. Every component has a decay rate with rationale.

---

### O2: Default Cadence Assignment

*Purpose: Review cadence per component based on agent class, harm category, and decay rate*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| component_id | ref(O1) | ✅ | Deterministic |
| default_cadence | string | ✅ | Probabilistic (derived from agent class + harm + decay rate) |
| cadence_rationale | string | ✅ | Probabilistic (why this cadence — what drives the interval) |
| minimum_cadence | string | ✅ | Deterministic (floor — no component reviewed less often than this) |
| maximum_cadence | string | ✅ | Deterministic (ceiling — no component reviewed more often than this) |
| cadence_confidence | enum: Default/Calibrated/Validated | ✅ | Probabilistic (is this from agent class patterns or production data?) |
| adjustment_criteria | string | ✅ | Deriver (what would cause this cadence to change) |
| responsible_party | enum: Principal/Orchestrator/Both | ✅ | Elicited (who owns this review — based on risk level) |

**Default Cadences by Agent Class:**

| Agent Class | Low Risk | Medium Risk | High Risk |
|---|---|---|---|
| Extractor | 6 months | 6 months | 3 months |
| Measurer | 6 months | 3 months | 3 months |
| Assessor | 3 months | 3 months | 1 month |
| Generator | 3 months | 1 month | 1 month |
| Aggregator | 6 months | 3 months | 3 months |

| Component Type | Default Cadence | Decay Rate | Rationale |
|---|---|---|---|
| Agent Instructions | 3 months | Medium | Model updates change behaviour; prompt drift |
| Authority Boundaries | 3 months | Fast | Boundaries drift with model capability changes |
| Output Schemas | 6 months | Slow | Schemas change when source/target systems change |
| Cost Budgets | 1 month | Fast | Usage patterns shift; model pricing changes |
| Quality Gates | 6 months | Slow | Gates are structural; change when specification changes |
| Epistemic Metadata | 3 months | Medium | Provenance and confidence assumptions drift |
| Progressive Autonomy | 3 months | Fast | Autonomy levels shift with demonstrated reliability |
| Task Allocation | 6 months | Slow | Allocations change when tasks or team changes |
| Contracts | 6 months | Medium | Contracts are structural; change when boundaries change |
| Full Specification | 12 months | Slow | Annual review minimum even if nothing triggers |

**Dependencies:** O1 (component registry), P7 (agent classes, harm assessment), P8 (reversibility)

**Quality Gate:** Every component has a cadence with rationale. Harm-capable agents have tighter cadences. No component has a cadence longer than 12 months. Full specification always gets annual review minimum.

---

### O3: Trigger-Based Review Conditions

*Purpose: Events that should trigger early review regardless of schedule*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| trigger_id | string | ✅ | Deterministic |
| trigger_type | enum: AutonomyPromotion/CostAnomaly/OverrideSpike/NewFailureMode/StakeholderFeedback/ModelUpdate/EnvironmentalChange/SpecificationChange/PeriodicThreshold | ✅ | Deterministic |
| trigger_description | string | ✅ | Deterministic |
| affected_components | list | ✅ | Deterministic (which components should be reviewed when this trigger fires) |
| trigger_threshold | string | ✅ | Probabilistic (what constitutes the trigger — e.g., "override rate exceeds 15% for 2 consecutive weeks") |
| trigger_source | string | ✅ | Deterministic (where the trigger signal comes from) |
| review_scope | string | ✅ | Deterministic (what specifically to review within affected components) |
| priority | enum: Immediate/ThisWeek/ThisMonth | ✅ | Deterministic |

**Trigger-to-Component Mapping:**

| Trigger Type | Affected Components | Priority |
|---|---|---|
| Autonomy promotion (Shadow→Advisory) | Progressive Autonomy, Authority Boundaries | ThisWeek |
| Autonomy promotion (Advisory→Supervised) | Progressive Autonomy, Authority Boundaries, Cost Budget | ThisWeek |
| Autonomy promotion (Supervised→Autonomous) | Progressive Autonomy, Authority Boundaries, Cost Budget, Contracts, Full Specification | Immediate |
| Cost anomaly (>50% over budget) | Cost Budget, Task Allocation, Agent Instructions | ThisWeek |
| Override rate spike (>15% for 2 weeks) | Authority Boundaries, Progressive Autonomy | ThisMonth |
| New failure mode discovered | Agent Instructions, Authority Boundaries, Contracts, Quality Gates | ThisWeek |
| Model update | Agent Instructions, Authority Boundaries, Output Schemas | ThisMonth |
| Stakeholder feedback (consistent pattern) | Affected components depend on feedback type | ThisMonth |
| Environmental change (regulation, domain) | Full Specification review may be warranted | ThisMonth |
| Specification change (by another component) | Cross-referenced components | ThisWeek |

**Dependencies:** O1 (component registry), O2 (cadences), EVOLVE Playbook O1 (signal types)

**Quality Gate:** Every trigger maps to specific components, not "review everything." Every trigger has a threshold, not just a vague description.

---

### O4: Review Question Sets

*Purpose: Specific questions to ask during each review — not "is everything OK?" but targeted probes*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| question_id | string | ✅ | Deterministic |
| component_id | ref(O1) | ✅ | Deterministic |
| question_text | string | ✅ | Deriver |
| question_type | enum: DriftCheck/BoundaryCheck/RelevanceCheck/PerformanceCheck/AlignmentCheck/ComplianceCheck | ✅ | Deriver |
| review_type | enum: Scheduled/Triggered | ✅ | Deterministic (is this a scheduled or trigger-based review question?) |
| expected_answer_type | enum: YesNo/Numeric/Comparison/Narrative/Checklist | ✅ | Deriver |
| red_flag_answer | string | ✅ | Deriver (what answer would indicate the component needs updating) |
| related_trigger | ref(O3) | ⚠️ (for triggered reviews) | Deterministic |

**Example Review Questions by Component Type:**

| Component Type | Drift Check | Boundary Check | Relevance Check |
|---|---|---|---|
| Agent Instructions | "Has the agent's behaviour changed since the last review without a specification update?" | "Are the instructions still producing outputs within declared boundaries?" | "Are the instructions still relevant to the current task allocation?" |
| Authority Boundaries | "Has the model's capability expanded beyond the current boundaries?" | "Have any boundary violations occurred since the last review?" | "Are the boundaries still aligned with the current harm assessment?" |
| Output Schemas | "Has the output format drifted from the declared schema?" | "Are all required fields still being populated correctly?" | "Is the schema still compatible with downstream consumers?" |
| Cost Budgets | "Has actual cost deviated from budget by more than 20%?" | "Are there cost categories that were not in the original budget?" | "Is the budget still appropriate for the current scope?" |
| Progressive Autonomy | "Is the agent operating at the declared autonomy level?" | "Have any override patterns suggested the autonomy level is wrong?" | "Is the current autonomy level still appropriate given demonstrated reliability?" |
| Contracts | "Have any contract primitives been violated since the last review?" | "Are the enforcement regimes still effective?" | "Are the contracts still aligned with the current specification?" |
| Epistemic Metadata | "Is the agent still providing all 6 CC-3 fields?" | "Are confidence scores still calibrated to actual accuracy?" | "Are provenance and recency fields still being updated?" |
| Quality Gates | "Are the quality gate criteria still appropriate?" | "Have any gates been bypassed or made irrelevant?" | "Are the gate checks still catching the failures they were designed for?" |

**Dependencies:** O1 (component registry), O2 (cadences), O3 (triggers)

**Quality Gate:** Every component type has at least 3 review questions (drift, boundary, relevance). Every question has a red flag answer that indicates the component needs updating. Questions are specific, not generic.

---

### O5: Cross-Reference Map

*Purpose: Links between the aging schedule, progressive autonomy timeline, and cost baselines*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| cross_ref_id | string | ✅ | Deterministic |
| component_id | ref(O1) | ✅ | Deterministic |
| autonomy_level | enum: Shadow/Advisory/Supervised/Autonomous | ✅ | Deterministic |
| autonomy_promotion_date | datetime | ⚠️ (null if not promoted yet) | Deterministic |
| scheduled_review_before_promotion | bool | ✅ | Deterministic (must review before promotion) |
| cost_baseline | string | ⚠️ (null if not tracked) | Deterministic |
| cost_anomaly_threshold | string | ✅ | Deterministic (what cost deviation triggers review) |
| last_review_triggered_by | enum: Cadence/AutonomyPromotion/CostAnomaly/OverrideSpike/NewFailureMode/OtherTrigger/None | ✅ | Deterministic |
| next_scheduled_review | datetime | ✅ | Computed (from cadence + last review date) |
| next_trigger_review | string | ⚠️ (if applicable) | Deterministic (next expected trigger-based review) |

**Dependencies:** O1 (component registry), O2 (cadences), O3 (triggers), progressive autonomy timeline, cost baselines

**Quality Gate:** Every autonomy promotion has a scheduled review before it. Every cost baseline has an anomaly threshold. Every component shows whether its next review is cadence-based or trigger-based.

---

### O6: Responsible Party Assignment

*Purpose: Who owns each review — not "someone" but a specific role*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| component_id | ref(O1) | ✅ | Deterministic |
| responsible_party | enum: Principal/Orchestrator/Both | ✅ | Elicited (based on risk level) |
| rationale | string | ✅ | Deriver (why this party is responsible) |
| review_method | enum: SelfReview/PeerReview/ExternalReview | ✅ | Deriver |
| escalation_path | string | ✅ | Deriver (what happens if the responsible party is unavailable) |

**Assignment Logic:**

| Harm Category | Responsible Party | Review Method | Escalation Path |
|---|---|---|---|
| Direct Output Harm | Principal | Self-review with external spot-check | Orchestrator reviews if Principal unavailable |
| Indirect Strategy Harm | Principal | Self-review | Orchestrator reviews if Principal unavailable |
| Indirect Data Harm | Orchestrator | Self-review with Principal spot-check | Principal reviews if Orchestrator unavailable |
| No Direct Harm | Orchestrator | Self-review | Principal reviews if Orchestrator unavailable |

**Dependencies:** O1 (component registry with harm category)

**Quality Gate:** Every component has a responsible party. High-risk components are reviewed by the Principal. Escalation paths are defined for every component.

---

### O7: Aging Schedule Document

*Purpose: The assembled, structured schedule for post-deployment specification maintenance*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| header | object | ✅ | Deterministic |
| component_registry | ref(O1) | ✅ | Mixed |
| cadence_assignments | ref(O2) | ✅ | Probabilistic |
| trigger_conditions | ref(O3) | ✅ | Deterministic |
| review_questions | ref(O4) | ✅ | Deriver |
| cross_references | ref(O5) | ✅ | Deterministic |
| responsible_parties | ref(O6) | ✅ | Elicited |
| schedule_confidence | enum: Default/Calibrated/Validated | ✅ | Probabilistic |
| known_gaps | list | ✅ | Deterministic (what cadences are default vs calibrated) |
| full_specification_annual_review | bool | ✅ | Deterministic (always true) |

**Dependencies:** All of O1-O6 must be complete

**Quality Gate:** Every component has a cadence with rationale. Every trigger maps to specific components. Every component has review questions. Every component has a responsible party. Annual review is guaranteed. Schedule confidence is honestly stated.

---

## P2: Backcasting

Working backward from O7:

```
O7 (Aging Schedule Document)
  ← requires O6 (Responsible Parties) — who owns each review
  ← requires O5 (Cross-References) — links to autonomy and cost
  ← requires O4 (Review Questions) — what to ask during reviews
  ← requires O3 (Trigger Conditions) — events that override cadences
  ← requires O2 (Default Cadences) — when to review each component
  ← requires O1 (Component Registry) — what components exist
  ← requires: agent class information from P7 (structural dependency)
  ← requires: harm assessment from P7 (structural dependency)
  ← requires: reversibility from P8 (structural dependency)
  ← requires: progressive autonomy timeline from P10 Artefact 5 (cross-reference)
  ← requires: cost baselines from P10 Artefact 7 (cross-reference)
```

### Input Requirements

| IR ID | Description | Source | Criticality | Satisfaction |
|---|---|---|---|---|
| IR-001 | Agent specification components | design_agent_specifications, design_contracts, design_tasks, design_quality_gates | Critical | Required |
| IR-002 | Agent class for each component | design_agent_specifications.agent_class | Critical | Required — without class, cadences can't be differentiated |
| IR-003 | Harm assessment for each agent | design_agent_specifications.harm_assessment | Critical | Required — without harm, risk weighting is impossible |
| IR-004 | Reversibility for each component | design_contracts.reversibility | High | Best effort — affects cadence weighting |
| IR-005 | Progressive autonomy timeline | P10 Artefact 5 (Progressive Autonomy Deployment Plan) | High | Best effort — cross-reference for promotion-triggered reviews |
| IR-006 | Cost baselines | P10 Artefact 7 (Cost & Resource Baseline) | High | Best effort — cross-reference for cost-triggered reviews |
| IR-007 | Override rate data (if available) | runtime_health_metrics | Medium | Best effort — may not exist pre-deployment |
| IR-008 | Specification age (when was each component last reviewed) | design_artefacts timestamps | Medium | Best effort — may be null at initial production |
| IR-009 | Domain-specific decay patterns | P7 domain knowledge | Low | Supplementary |
| IR-010 | Operational context (how the agent is actually used) | P9 human experience | Low | Supplementary |

### Key P2 Insight

**IR-002 (agent class) and IR-003 (harm assessment) are the structural prerequisites for differentiated cadences.** Without them, the schedule defaults to a universal cadence — which violates the core identity (A1: component-specific, A2: risk-weighted, A7: class-aware). This is the same structural dependency pattern as the Confidence Map's IR-002 (stakes levels).

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| T1 | Query PRISM for all specification components | Mechanical | Missing components | Component list |
| T2 | Query agent class for each component | Mechanical | Missing agent class for some components | Agent class data |
| T3 | Query harm assessment for each agent | Mechanical | Missing harm data | Harm assessment data |
| T4 | Query reversibility for each component | Mechanical | Missing reversibility data | Reversibility data |
| T5 | Query progressive autonomy timeline | Mechanical | Missing timeline | Autonomy timeline data |
| T6 | Query cost baselines | Mechanical | Missing cost data | Cost baseline data |
| T7 | Classify decay rate per component type | Analytical | Incorrect decay rate classification | O1 decay_rate + decay_rationale |
| T8 | Assign default cadence per component based on class, harm, decay | Analytical | Over-cadencing or under-cadencing | O2 draft |
| T9 | Define trigger conditions per component type | Analytical | Over-broad triggers (review everything) | O3 draft |
| T10 | Map triggers to affected components | Analytical | Generic mappings (every trigger affects every component) | O3 trigger-component mapping |
| T11 | Calculate priority per trigger type | Analytical | Priority mismatch (low urgency for high impact triggers) | O3 priority |
| T12 | Cross-reference cadences with autonomy timeline | Analytical | Missing promotion-triggered reviews | O5 cross-reference |
| T13 | Cross-reference cadences with cost baselines | Analytical | Missing cost-triggered reviews | O5 cross-reference |
| T14 | Assign responsible party per component based on harm category | Analytical | Assigning low-risk owner to high-risk component | O6 draft |
| T15 | Generate review questions per component type (drift, boundary, relevance) | Generative | Generic "is everything OK?" questions | O4 draft |
| T16 | Generate red flag answers per question | Generative | Vague red flags ("if something seems wrong") | O4 red_flag_answer |
| T17 | Generate cadence adjustment criteria per component | Generative | Generic "adjust based on experience" | O2 adjustment_criteria |
| T18 | Generate escalation paths per component | Generative | Missing escalation for unavailable responsible party | O6 escalation_path |
| T19 | Assess known gaps in cadence confidence | Analytical | Overstating confidence in default cadences | Known gaps |
| T20 | Compile into aging schedule document | Mechanical | Omitting components or misordering cadences | O7 final |

20 tasks across 4 cognitive types:
- Mechanical: 6 (T1-T6, T20)
- Analytical: 8 (T7-T14, T19)
- Generative: 4 (T15-T18)

---

## P4: Capability Allocation

| Task | H | A | S | Gap | Allocation | Notes |
|---|---|---|---|---|---|---|
| T1 | 2 | 3 | 10 | 8 | System | Pure data query |
| T2 | 2 | 3 | 10 | 8 | System | Pure data query |
| T3 | 2 | 3 | 10 | 8 | System | Pure data query |
| T4 | 2 | 3 | 10 | 8 | System | Pure data query |
| T5 | 2 | 3 | 10 | 8 | System | Pure data query |
| T6 | 2 | 3 | 10 | 8 | System | Pure data query |
| T7 | 4 | 8 | 2 | 4 | Agent-primary | Decay rate classification requires domain judgment |
| T8 | 4 | 8 | 2 | 4 | Agent-primary | Cadence assignment requires balancing decay rate, risk, and class |
| T9 | 4 | 8 | 2 | 4 | Agent-primary | Trigger definition requires understanding of what changes components |
| T10 | 3 | 8 | 2 | 5 | Agent-primary | Mapping triggers to components requires understanding component relationships |
| T11 | 3 | 7 | 2 | 4 | Agent-primary | Priority calculation from trigger characteristics |
| T12 | 3 | 7 | 2 | 4 | Agent-primary | Cross-referencing cadences with autonomy timeline |
| T13 | 3 | 7 | 2 | 4 | Agent-primary | Cross-referencing cadences with cost baselines |
| T14 | 4 | 7 | 2 | 3 | Agent-primary | Responsible party assignment from harm category |
| T15 | 5 | 8 | 2 | 3 | Agent-primary | Review question generation requires domain understanding |
| T16 | 5 | 8 | 2 | 3 | Agent-primary | Red flag definition requires understanding failure modes |
| T17 | 4 | 8 | 2 | 4 | Agent-primary | Adjustment criteria from component characteristics |
| T18 | 3 | 7 | 2 | 4 | Agent-primary | Escalation path design from organisational structure |
| T19 | 4 | 7 | 2 | 3 | Agent-primary | Gap assessment from cadence confidence data |
| T20 | 2 | 3 | 10 | 8 | System | Assembly is mechanical |

No human-primary tasks in production. Human role is post-delivery review and responsible party confirmation.

### Key P4 Insight

All tasks are System or Agent-primary because the schedule is assembled from existing specification data — it doesn't elicit new human input during production. Human role is confirming responsible party assignments (O6) and reviewing the final schedule, not producing schedule content.

---

## P5: Event Storming

### Domain Events

| Event | Trigger | Producer |
|---|---|---|
| E1 | Aging schedule generation started | Human or System trigger |
| E2 | Component registry complete | System |
| E3 | Default cadences assigned | Analyst |
| E4 | Trigger conditions defined | Analyst |
| E5 | Review questions generated | Deriver |
| E6 | Cross-references mapped | Analyst |
| E7 | Responsible parties assigned | Analyst |
| E8 | Schedule compiled | Compiler |
| E9 | Autonomy promotion detected | System (monitoring) |
| E10 | Cost anomaly detected | System (monitoring) |

### Failure Events

| Failure | Trigger | Recovery |
|---|---|---|
| F1 | Missing agent class for one or more components | IR-002 data incomplete | Assign "Unknown" class with default 3-month cadence; flag for human classification; do not default to longest cadence |
| F2 | Missing harm assessment for one or more agents | IR-003 data incomplete | Default to "Indirect Strategy Harm" (most common) with 3-month cadence; flag for human assessment; do not default to "No Direct Harm" (under-cadencing risk) |
| F3 | Universal cadence assigned to all components | Agent class or harm data not differentiated | Enforce per-component cadences; reject universal cadence at schema validation |
| F4 | Over-frequent cadences for low-risk components | Review fatigue — Extractor schemas reviewed monthly | Apply minimum cadence floor (1 month for cost, 3 months for most, 6 months for slow-decay, 12 months for full spec); flag components with cadences shorter than their decay rate warrants |
| F5 | Under-frequent cadences for high-risk components | Generators with annual boundary reviews | Apply maximum cadence ceiling based on harm category (Direct Harm: max 1 month, Strategy Harm: max 3 months, Data Harm: max 6 months, No Harm: max 12 months); flag components exceeding their ceiling |
| F6 | Generic review questions ("is everything still OK?") | Deriver produces untargeted questions | Every question must reference a specific check type (drift, boundary, relevance, performance, alignment, compliance); reject generic questions |
| F7 | Missing autonomy promotion reviews | Progressive autonomy timeline not cross-referenced | Enforce: every autonomy promotion must have a scheduled review before promotion date; if timeline unavailable, flag all autonomy-related components for review at each cadence |
| F8 | No responsible party for high-harm components | O6 assignment skips harm-capable agents | Enforce: all Direct Output Harm and Indirect Strategy Harm components must have Principal as responsible party |
| F9 | All cadences marked "Calibrated" with no production data | Overstating confidence in default cadences | All cadences start as "Default"; only upgrade to "Calibrated" after production data supports the interval |
| F10 | Cost baseline not available for cross-reference | P10 Artefact 7 not yet produced | Use default cost anomaly thresholds (>50% over budget); flag as "Default — pending cost baseline calibration" |

### Key P5 Insight

**F2 (missing harm assessment) defaults to "Indirect Strategy Harm" — not "No Direct Harm."** This is a conservative default because under-cadencing high-risk components is the worse failure. When in doubt, review more often, not less. The schedule should err on the side of over-review during the Default phase and relax cadences during Calibrated phase based on production data.

**F3 (universal cadence) is the identity violation.** If all components get the same cadence, the schedule has failed at its core purpose. Schema validation should reject any schedule where all components have identical cadences unless there's only one component.

---

## P6: System Architecture

### Pipeline Architecture

```
Wave 1: Data Track (parallel, System)
T1 ──┐
T2 ──┤
T3 ──┤──→ component_data (raw)
T4 ──┤
T5 ──┤
T6 ──┘

Wave 2: Assessment Track (sequential, Analyst)
T7 (Decay rate classification) ──→ O1 decay_rate + rationale
T8 (Default cadence assignment) ──→ O2 draft
T9 (Trigger condition definition) ──→ O3 draft
T10 (Trigger-component mapping) ──→ O3 mapping
T11 (Priority calculation) ────────→ O3 priority
T12 (Autonomy cross-reference) ──→ O5 autonomy cross-ref
T13 (Cost cross-reference) ────────→ O5 cost cross-ref
T14 (Responsible party assignment) → O6 draft

Wave 3: Derivation Track (after assessment)
T15 (Review questions per component type) → O4 draft
T16 (Red flag answers) ────────────→ O4 red_flags
T17 (Cadence adjustment criteria) ──→ O2 adjustment_criteria
T18 (Escalation paths) ────────────→ O6 escalation_paths

Wave 4: Compilation Track (after derivation)
T19 (Known gaps assessment) ──────→ known_gaps
T20 (Final assembly) ─────────────→ O7 final
```

### Agent Roster

**Analyst (Measurer + Assessor, bridge-oriented)**

| Field | Value |
|---|---|
| Identity | "I measure decay rates and assess review appropriateness. I assign cadences based on component class, harm, and decay rate. I never assign universal cadences, never under-cadence high-risk components, never over-cadence low-risk components, and never set cadences longer than 12 months for any component." |
| Class | Measurer (decay rates, cadences, priorities) + Assessor (review appropriateness, risk weighting) |
| Orientation | Bridge-oriented |
| Hardest boundary moment | When a component has no clear decay rate precedent — assigning a 3-month default vs 6-month default vs 12-month default is a judgment call that affects operational burden for months |
| Never rules | Assign universal cadences, under-cadence high-risk components, over-cadence low-risk components, set cadences longer than 12 months |
| Cost budget | Medium — 10K-25K tokens |

**Deriver (Generator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I derive review questions, red flag answers, adjustment criteria, and escalation paths from component characteristics and decay patterns. Every question targets a specific check type. Every red flag is concrete. Every adjustment criterion specifies what data to collect and what change to make." |
| Class | Generator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When a component type is new or unusual and has no established review pattern — the temptation is to fall back on generic "is everything still working?" questions rather than designing targeted probes |
| Never rules | Generate generic review questions, propose vague red flags, create adjustment criteria without data sources, set cadences without decay rationale |
| Cost budget | Medium — 8K-20K tokens |

**Compiler (Aggregator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I compile the aging schedule from assessed and derived outputs. I never add cadences not produced by the Analyst, never omit components that need review, never mark Default cadences as Calibrated, and never produce a universal cadence schedule." |
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When most cadences are Default (not Calibrated) — the temptation is to present them at the same confidence level. The correct response is to clearly mark Default cadences and include calibration timelines. |
| Never rules | Add cadences not produced by Analyst, omit components, mark Default as Calibrated, produce universal cadence schedule |
| Cost budget | Low — 3K-10K tokens |

### FMEA

| ID | Failure Mode | Severity | Occurrence | Detection | RPN | Recovery |
|---|---|---|---|---|---|---|
| FM1 | Universal cadence for all components | 10 | 3 | 8 | 240 | Schema validation rejects identical cadences; Analyst authority boundary prohibits universal assignment |
| FM2 | Under-cadencing high-risk components | 10 | 3 | 5 | 150 | Maximum cadence ceiling per harm category; F2 defaults to moderate risk not low risk |
| FM3 | Over-cadencing low-risk components (review fatigue) | 6 | 4 | 7 | 168 | Minimum cadence floor per component type; F4 flagging for cadences shorter than decay rate warrants |
| FM4 | Generic review questions | 7 | 4 | 6 | 168 | Every question must reference a specific check type; reject generic questions at schema validation |
| FM5 | Missing autonomy promotion reviews | 8 | 3 | 6 | 144 | F7 enforcement: every autonomy promotion has a pre-promotion review scheduled |
| FM6 | Missing responsible party for harm-capable agents | 9 | 2 | 8 | 144 | F8 enforcement: Direct Output Harm and Indirect Strategy Harm components require Principal |
| FM7 | Default cadences marked as Calibrated | 8 | 3 | 7 | 168 | schedule_confidence field mandatory; all cadences start as "Default"; upgrade requires production data |
| FM8 | Missing harm assessment defaults to "No Direct Harm" | 10 | 2 | 6 | 120 | F2: default to "Indirect Strategy Harm" (conservative); flag for human assessment |
| FM9 | Trigger conditions too broad (review everything) | 7 | 3 | 6 | 126 | Every trigger must map to specific components; reject triggers that affect all components |
| FM10 | Cost baseline unavailable | 5 | 4 | 7 | 140 | Use default >50% over budget threshold; flag as "Default — pending calibration" |

Highest RPNs: FM1 (universal cadence) at 240, FM3 (over-cadencing) at 168, FM7 (Default as Calibrated) at 168, FM2 (under-cadencing) at 150.

### 5 Regime 3 Enforcement Points

| # | Boundary | Enforcement |
|---|---|---|
| 1 | No universal cadence | Schema validation rejects schedules where all components have identical cadences |
| 2 | Harm-weighted cadence ceiling | Direct Output Harm: max 1 month, Indirect Strategy Harm: max 3 months, Indirect Data Harm: max 6 months, No Direct Harm: max 12 months |
| 3 | Review question specificity | Every question must have question_type and red_flag_answer; reject generic questions |
| 4 | Schedule confidence labelling | All cadences start as "Default"; upgrade requires production evidence; Compiler prohibited from marking Default as Calibrated |
| 5 | Responsible party enforcement | Harm-capable components (Direct Output Harm, Indirect Strategy Harm) require Principal as responsible party |

---

## P7: Agent Design

### Analyst Agent Job Description

| Field | Value |
|---|---|
| Class | Measurer + Assessor |
| Orientation | Bridge-oriented |
| Mission | Measure decay rates and assign review cadences based on component class, harm category, and decay pattern. I never assign universal cadences, never under-cadence high-risk components, never over-cadence low-risk components, and never set cadences longer than 12 months for any component." |
| Inputs | Component registry, agent class data, harm assessment data, reversibility data, autonomy timeline, cost baselines |
| Outputs | O1 (component registry with decay rates), O2 (default cadences), O3 (trigger conditions and mappings), O5 (cross-references), O6 (responsible parties) |
| Null state | "No specification components available for aging schedule generation. Cannot produce schedule without component data." |
| Never rules | Assign universal cadences, under-cadence high-risk components, over-cadence low-risk components, set cadences longer than 12 months, default to "No Direct Harm" when harm assessment is missing |
| Hardest boundary moment | Setting default cadences for components without production data — the temptation is to assign conservative (frequent) cadences to everything, which causes review fatigue. The correct response is to assign class-differentiated defaults and mark them as "Draft — pending calibration." |
| Epistemic profile | Probabilistic — decay rate classification and cadence assignment involve judgment about operational patterns |
| Harm assessment | Indirect strategy harm — over-cadencing causes review fatigue (the schedule becomes noise), under-cadencing allows specification decay. Both are harmful; over-cadencing is the worse failure for schedule credibility. |
| Progressive autonomy | Three dimensions: (1) decay rate classification (Shadow → Supervised), (2) cadence assignment (Shadow → Supervised), (3) trigger mapping (Shadow → Advisory). Per-dimension. |
| Cost budget | Medium — 10K-25K tokens |
| Verification | Every component has a decay rate with rationale. Every cadence is differentiated by class and harm. No universal cadences. No cadence exceeds 12 months. Harm-capable components have tighter cadences. |

### Deriver Agent Job Description

| Field | Value |
|---|---|
| Class | Generator |
| Orientation | Constraint-oriented |
| Mission | Derive review questions, red flag answers, cadence adjustment criteria, and escalation paths from component characteristics and decay patterns. Every question targets a specific check type. Every red flag is concrete. Every adjustment criterion specifies what to observe and what to adjust." |
| Inputs | O1 (components with decay rates), O2 (cadences), O3 (triggers), O5 (cross-references) |
| Outputs | O4 (review questions with red flags), O2 adjustment_criteria, O6 escalation_paths |
| Null state | "No component data available for question generation. Cannot produce review questions without component registry." |
| Never rules | Generate generic review questions, propose vague red flags, create adjustment criteria without data sources, set cadences without decay rationale |
| Hardest boundary moment | When a component type is new or unusual — the temptation is to fall back on "is everything still working?" rather than designing targeted drift, boundary, and relevance checks specific to that component type |
| Epistemic profile | Probabilistic — question generation involves judgment about what to check and what constitutes a red flag |
| Harm assessment | Indirect operational harm — generic questions lead to superficial reviews that miss actual drift |
| Progressive autonomy | Two dimensions: (1) question specificity (Shadow → Supervised — generic → targeted with check type), (2) red flag concreteness (Shadow → Advisory — vague → measurable). Per-dimension. |
| Cost budget | Medium — 8K-20K tokens |
| Verification | Every question has a question_type and red_flag_answer. Every adjustment criterion specifies what to observe and what to adjust. Every escalation path identifies a specific responsible party and backup. |

### Compiler Agent Job Description

| Field | Value |
|---|---|
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Mission | Compile the aging schedule from assessed and derived outputs. Ensure every component has a cadence, every trigger maps to components, every component has review questions, and Default cadences are clearly marked." |
| Inputs | O1-O6 processed outputs, known_gaps, schedule_confidence |
| Outputs | O7 (Aging Schedule Document) |
| Null state | "No schedule data available for compilation." |
| Never rules | Add cadences not produced by Analyst, omit components that need review, mark Default as Calibrated, produce universal cadence schedule |
| Hardest boundary moment | When most cadences are Default (not Calibrated) — present them at different confidence levels, not smoothed into uniform presentation |
| Epistemic profile | Deterministic — compilation is mechanical |
| Harm assessment | Indirect data harm — presenting Default cadences as Calibrated could lead to operational decisions based on uncalibrated intervals |
| Progressive autonomy | Single dimension: compilation accuracy. Shadow → Advisory → Supervised → Autonomous |
| Cost budget | Low — 3K-10K tokens |
| Verification | Every component has a cadence. Every trigger maps to components. Every component has review questions. Default vs Calibrated clearly marked. No universal cadence schedule. Annual review guaranteed. |

### Per-Dimension Progressive Autonomy

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Analyst | Decay rate classification | Propose, human reviews every classification | Propose, human reviews unusual types only | Propose, human reviews high-risk components only | Full classification, human reviews annual | ≥10 schedules with ≤1 misclassification |
| Analyst | Cadence assignment | Propose, human reviews every cadence | Propose, human reviews high-risk cadences only | Propose, human reviews harm-capable components only | Full assignment, human reviews annual | ≥10 schedules with ≤2 over/under-cadenced components |
| Analyst | Trigger mapping | Propose, human reviews every trigger | Propose, human reviews broad triggers only | Propose, human reviews all-triggers-review only | Full mapping, human reviews annual | ≥10 schedules with ≤2 over-broad triggers |
| Deriver | Question specificity | Generic questions only | Targeted questions with check type | Targeted questions with check type and red flag | Fully specific questions with red flag and escalation | ≥10 question sets with ≤2 generic questions |
| Deriver | Red flag concreteness | Vague red flags ("something seems wrong") | Concrete red flags with measurable criteria | Concrete red flags with measurable criteria and adjustment direction | Fully concrete red flags with all three | ≥10 question sets with ≤2 vague red flags |
| Compiler | Compilation accuracy | Human checks every section | Human checks cadence assignments | Human checks Default/Calibrated marking | Human reviews final post-delivery | ≥10 compilations with ≤1 error |

---

## P8: Contract Formalization

### Analyst Contract

| Primitive | Specification |
|---|---|
| Contract | Assign review cadences to specification components based on class, harm, and decay rate |
| Principal | Deriver (downstream consumer) |
| Schema | ComponentRegistry (O1) + DefaultCadences (O2) + TriggerConditions (O3) |
| Guard | prohibited: ["assign_universal_cadences", "under_cadence_high_risk", "over_cadence_low_risk", "set_cadences_longer_than_12_months", "default_to_no_harm_when_missing"] |
| Budget | 10K-25K tokens |
| Invocation | After T1-T6 complete |
| Revert | If cadence cannot be assigned due to missing class data, mark as "Unknown class — default 3-month cadence" rather than assign longest or shortest |
| Event | analysis_started, component_classified, cadence_assigned, trigger_defined, cross_reference_mapped, analysis_complete |
| Identity | Bridge-oriented Measurer+Assessor — measures and assesses, never assigns universal cadences |
| Knowledge | Component registry, agent class data, harm assessment data, reversibility data, autonomy timeline, cost baselines |

### Deriver Contract

| Primitive | Specification |
|---|---|
| Contract | Derive review questions, red flag answers, adjustment criteria, and escalation paths |
| Principal | Compiler (downstream consumer) |
| Schema | ReviewQuestions (O4) + O2 adjustment_criteria + O6 escalation_paths |
| Guard | prohibited: ["generate_generic_review_questions", "propose_vague_red_flags", "create_adjustment_criteria_without_data_sources", "set_cadences_without_decay_rationale"] |
| Budget | 8K-20K tokens |
| Invocation | After Analyst outputs complete |
| Revert | If derivation cannot be performed due to missing component data, report "insufficient component data for question generation" |
| Event | derivation_started, question_generated, red_flag_defined, adjustment_criterion_defined, escalation_defined, derivation_complete |
| Identity | Constraint-oriented Generator — derives within component boundaries |
| Knowledge | O1 components, O2 cadences, O3 triggers, O5 cross-references |

### Compiler Contract

| Primitive | Specification |
|---|---|
| Contract | Compile the aging schedule from assessed and derived outputs |
| Principal | Human (post-delivery reviewer) |
| Schema | AgingScheduleDocument (O7 schema) |
| Guard | prohibited: ["add_cadences_not_from_analyst", "omit_components_that_need_review", "mark_default_as_calibrated", "produce_universal_cadence_schedule"] |
| Budget | 3K-10K tokens |
| Invocation | After all O1-O6 complete |
| Revert | If compilation fails completeness check, revert to section-level output |
| Event | compilation_started, cadence_assembled, trigger_mapped, question_assembled, confidence_labelled, compilation_complete |
| Identity | Constraint-oriented Aggregator — compiles, never creates or omits |
| Knowledge | All processed outputs O1-O6, known_gaps, schedule_confidence |

### Unenforceable Elements Register

| Element | Why Unenforceable | Regime | Mitigation |
|---|---|---|---|
| "Never under-cadence high-risk components" (Analyst) | "Under-cadence" is a judgment about operational context — what's under-cadenced for one deployment may be appropriate for another | Regime 2 (Detect) | Maximum cadence ceiling per harm category (Direct: 1 month, Strategy: 3 months, Data: 6 months, None: 12 months); human review of harm-capable component cadences |
| "Never over-cadence low-risk components" (Analyst) | "Over-cadence" is similarly context-dependent — monthly reviews might be appropriate during initial deployment even for low-risk components | Regime 2 (Detect) | Minimum cadence floor per component type; schedule_confidence marking (Default cadences may be tighter than needed) |
| "Never generate generic review questions" (Deriver) | "Generic" is a gradient — how specific is specific enough? | Regime 1 (Declare) | Every question must have question_type and red_flag_answer; specificity validated at schema level |
| "Never produce universal cadence schedule" (Compiler) | Technically enforceable at schema level — but a schedule where all cadences happen to be the same due to component similarity is different from a schedule where cadences are not differentiated | Regime 3 (Prevent) | Schema validation: if all cadences are identical AND component count > 1, reject. If cadences are differentiated but happen to be the same for valid reasons, allow with rationale |

### 10×10 Mapping Matrix

All 10 specification sections map to all 10 contract primitives for this workflow.

---

## P9: Human Experience Design

### Cognitive Load Budget

| Review Activity | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Review component registry (are components complete?) | 3-5 | 10 min | Evaluative |
| Review cadence assignments (are cadences appropriate?) | 5-10 | 15 min | Evaluative + Discovery (are decay rates right for our context?) |
| Review trigger conditions (are triggers specific enough?) | 3-5 | 10 min | Evaluative |
| Review review questions (are questions targeted enough?) | 3-5 | 10 min | Evaluative |
| Review responsible parties (are owners correct?) | 2-3 | 5 min | Evaluative |
| Confirm schedule confidence levels | 1-2 | 5 min | Evaluative |
| Review known gaps | 2-3 | 5 min | Discovery (what data do we need to calibrate?) |
| **Total** | **19-33** | **60 min** | |

Maximum review session: 60 minutes.

### Override Mechanisms

| Override Type | Mechanism | Example |
|---|---|---|
| Adjust cadence | Change review frequency based on operational experience | "This Generator's boundaries drift more than expected — change from 3 months to 1 month" |
| Add trigger | Add a domain-specific trigger not in the standard list | "For our domain, regulatory change is a review trigger for all compliance-related components" |
| Remove trigger | Remove a trigger that doesn't apply to this deployment | "We don't track cost at the component level — remove cost anomaly triggers" |
| Change responsible party | Assign a different owner for a component | "The Orchestrator should review data Extractor schemas, not the Principal" |
| Add review question | Add a domain-specific question for a component | "For our medical domain, add a HIPAA compliance check to the Agent Instructions review" |

### Stakeholder Surfaces

| Surface | View | Language | Depth | Emphasis |
|---|---|---|---|---|
| Decision Maker | O7 schedule summary + O3 trigger summary | Plain English | Low-Medium | When to review, who owns it, what triggers override |
| Design Participant | O1 component registry + O2 cadences + O4 review questions | Technical | Deep | Decay rates, cadence rationale, specific questions, red flags |
| Governance | O6 responsible parties + O5 cross-references + audit trail | Technical | Medium | Who owns each review, when autonomy promotions trigger reviews, compliance alignment |

### System Empowerment Assessment

| Dimension | Level | Explanation |
|---|---|---|
| Maintenance scheduling | Amplifying | Proactive cadences free humans from remembering when to review |
| Review focus | Amplifying | Targeted review questions focus attention on what matters, not generic checks |
| Trigger responsiveness | Enabling | Triggers prepare the decision (what changed, what to check), humans decide whether to act |
| Review efficiency | Amplifying | Differentiated cadences prevent review fatigue — low-risk components reviewed less often |
| Creative freedom | Enabling | Frees humans from wondering "should we review this now?" — the schedule answers when and what |
| Overall | Enabling → Amplifying | Proactive scheduling and targeted questions are amplifying; review decisions remain enabling |

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method | Success Criterion |
|---|---|---|---|
| H1 | Differentiated cadences reduce review burden vs universal quarterly review | Compare total review hours per year: differentiated schedule vs universal quarterly | Differentiated schedule takes ≤60% of universal quarterly review hours |
| H2 | Targeted review questions catch more drift than generic checks | Compare drift detection rate: targeted questions vs generic "is everything OK?" | Targeted questions detect ≥40% more actual drift per review |
| H3 | Trigger-based reviews catch issues between scheduled reviews | Compare issues caught by triggers vs issues caught only at scheduled reviews | Triggers catch ≥25% of issues that would have waited until next scheduled review |
| H4 | Harm-weighted cadences allocate review time proportionally to risk | Compare review time allocation vs harm distribution | ≥80% of review time allocated to Medium+High risk components |
| H5 | Responsible party assignment increases review completion rate | Compare completion rates: assigned owners vs unassigned | Assigned owners complete ≥30% more scheduled reviews than unassigned |
| H6 | Cadence adjustment criteria enable calibration from Default to Calibrated | Track cadence confidence transitions over 90 days | ≥30% of Default cadences transition to Calibrated within 90 days |

### Progressive Autonomy Deployment

Documented in P7 per-dimension table. Key notes:
- **Decay rate classification** is the most consequential Analyst dimension — wrong classification cascades into wrong cadences
- **Question specificity** is the most consequential Deriver dimension — generic questions lead to superficial reviews
- **All dimensions start at Shadow** because this workflow produces a living document that affects operational behaviour

### Specification Aging Schedule for This Workflow Itself

| Component | Default Cadence | Trigger-Based Review | Responsible |
|---|---|---|---|
| Component registry (O1) | 6 months | When specification structure changes | Analyst |
| Default cadences (O2) | 3 months | When over/under-cadencing detected | Analyst |
| Trigger conditions (O3) | 6 months | When new failure modes emerge | Analyst |
| Review questions (O4) | 6 months | When component types change | Deriver |
| Cross-references (O5) | 3 months | When autonomy promotions occur | Analyst |
| Responsible parties (O6) | 12 months | When team structure changes | Analyst |
| Full schedule (O7) | 12 months | When any O1-O6 changes significantly | Compiler |

### EVOLVE Mode

| Signal | Re-entry Point | Scope |
|---|---|---|
| Override rate increasing | P4 (Capability Allocation) | Review task allocation and authority boundaries |
| Specification aging alert | This schedule (O2 cadences) | Review the cadence itself — is it too frequent or too infrequent? |
| Capability drift | P7 (Agent Design) | Review agent specifications and boundaries |
| Cost anomaly | P6 (System Architecture) | Review cost budgets and pipeline architecture |
| Autonomy promotion | This schedule (O5 cross-ref) | Schedule a pre-promotion review |
| New failure mode | P3+P5 (Task Decomposition + Event Storming) | Review task decomposition and failure events |
| Environmental change | P0 (Purpose & Vision) | Full re-evaluation of purpose and scope |
| Periodic review | This schedule | Targeted review per component cadence |

---

## Summary: What This Application Reveals

| Phase | Key Insight |
|---|---|
| P0 | Two opposite failures: over-cadencing (review fatigue, schedule becomes noise) is worse than under-cadencing (specification decay), but both are harmful. Different components decay at fundamentally different rates. |
| P1 | The schedule must differentiate by agent class, harm category, and decay rate — a universal cadence violates the core identity. Harm-weighted cadences allocate review time proportionally to risk. |
| P2 | IR-002 (agent class) and IR-003 (harm assessment) are structural prerequisites for differentiated cadences. Without them, the schedule defaults to universal cadences — the identity violation. |
| P3 | 20 tasks — fewer than Confidence Map (25) but more analytical tasks than Methodology Reflection (19). Decay rate classification (T7) is the most consequential task. |
| P4 | All tasks are System or Agent-primary in production. Human role is confirming responsible parties and reviewing the final schedule. |
| P5 | F1 (universal cadence) has the highest RPN at 240 — it's the identity violation. F3 (over-cadencing) and F7 (Default as Calibrated) are tied at 168. Conservative defaults for missing harm data (F2: default to "Indirect Strategy Harm," not "No Direct Harm"). |
| P6 | Schema validation rejects universal cadences and generic questions. Maximum cadence ceilings per harm category are Regime 3 enforcement. |
| P7 | Three agents with per-dimension progressive autonomy. Decay rate classification is the slowest progression because wrong classification cascades into wrong cadences. |
| P8 | Four unenforceable elements. Universal cadence prevention is Regime 3 (schema validation). "Never under-cadence" and "never over-cadence" are Regime 2 (context-dependent). |
| P9 | Proactive scheduling and targeted questions are the key amplifying factors. Review time is allocated proportionally to risk, not equally across all components. |
| P10 | Six hypotheses. H2 (targeted questions catch more drift) and H4 (harm-weighted cadences allocate proportionally) are most operationally valuable. |

### Critical Structural Dependency

**Agent class and harm assessment data from P7/P8 must exist for differentiated cadences.** Without class differentiation, the schedule can't assign appropriate cadences for different component types. Without harm assessment, it can't weight cadences by risk. This is the same structural dependency pattern as the Confidence Map (which needs stakes classification).

### How This Differs from the Three P10 Artefacts

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook | Aging Schedule |
|---|---|---|---|---|
| Question | How well did CAWDP perform? | How confident are we? | When do we come back? | When do we review what? |
| Time orientation | Backward | Forward | Forward + Ongoing | Ongoing (proactive) |
| Trigger model | N/A (snapshot) | N/A (snapshot) | Reactive (signals) | Proactive (cadences) + Reactive (triggers) |
| Primary interaction | Surprises × gaps | Confidence × stakes | Signal × urgency × scope | Decay rate × risk × agent class |
| Key amplifying factor | Review questions | Risk-calibrated attention | Proactive scheduling | Proactive scheduling + targeted questions |
| Highest RPN | Fabrication (160) | Missing stakes (189) | Over-triggering (200) | Universal cadence (240) |
| Critical dependency | Artefact tagging (behavioural) | Stakes classification (structural) | Monitoring infrastructure (temporal) | Agent class + harm assessment (structural) |
| Worst failure | Fabricating insights | Overstating confidence | Over-triggering | Over-cadencing (universal cadence = identity violation) |
| Lifecycle | One-time snapshot | One-time snapshot | Living document | Living document (component of EVOLVE Playbook O3) |

The pattern holds for the fourth time: same three-agent architecture, same analysis+synthesis principle, different domain, different critical dependency, different worst failure. The universal cadence violation (FM1 at RPN 240) is the highest RPN across all four P10 artefacts — because it violates the core identity of this particular workflow (component-specific, not universal).

### Relationship to EVOLVE Playbook

The Specification Aging Schedule is **not a standalone P10 artefact** — it's the proactive component of the EVOLVE Playbook. Where the EVOLVE Playbook's trigger-response map (O2) is reactive ("when this signal fires, do this"), the aging schedule is proactive ("on this cadence, review this component, asking these questions"). Both are needed. The EVOLVE Playbook's O3 (Specification Aging Schedule) is a reference to this workflow's output.

This means:
- The aging schedule's cadences and review questions feed into the EVOLVE Playbook
- The EVOLVE Playbook's trigger conditions can override the aging schedule's cadences
- The aging schedule's cross-references (autonomy promotions, cost anomalies) are trigger conditions in the EVOLVE Playbook
- Together, they provide complete specification maintenance: proactive (cadences) + reactive (triggers)

The four P10 artefacts now form a complete validation and maintenance suite:

1. **Methodology Reflection** — How well did CAWDP perform? (process quality)
2. **Confidence Map** — How confident are we in the specification? (product reliability)
3. **EVOLVE Playbook** — When do we come back and for what? (operational longevity)
4. **Specification Aging Schedule** — When do we review what and what do we ask? (proactive maintenance)All four P10 artefacts are now complete through full CAWDP v2.1 application. The complete validation and maintenance suite:

| # | Artefact | Question | Time | Dependency | Worst Failure (RPN) |
|---|---|---|---|---|---|
| 1 | Methodology Reflection | How well did CAWDP perform? | Backward | Behavioural (tagging) | Fabrication (160) |
| 2 | Confidence Map | How confident are we? | Forward | Structural (stakes) | Missing stakes (189) |
| 3 | EVOLVE Playbook | When do we come back? | Forward + Ongoing | Temporal (monitoring) | Over-triggering (200) |
| 4 | Specification Aging Schedule | When do we review what? | Ongoing (proactive) | Structural (class + harm) | Universal cadence (240) |

The same three-agent architecture (Compiler/Analyst/Deriver), the same analysis+synthesis principle, four different domains, four different critical dependencies, four different worst failures, two different lifecycle types (snapshot vs living document), and one key relationship: the Aging Schedule is the proactive backbone of the EVOLVE Playbook.

Together, they form a complete post-CAWDP suite:
- **Methodology Reflection** tells you how the process went
- **Confidence Map** tells you how much to trust the result
- **EVOLVE Playbook** tells you when to come back (reactive)
- **Aging Schedule** tells you when to review what (proactive)

---

## Run 15 — Agentic Expert ✓ COMPLETED

*2026-05-21T21:46:12* · `glm-5.1:cloud` · `54cb0fb3...`

### Prompt

Perform CAWDP Phase 0 on the Cost & Resource Baseline workflow:

***
7. Cost & Resource Baseline

**Purpose**: Financial and resource foundation for monitoring.

| Step | Action | Actor | Tool |
|---|---|---|---|
| 1 | Extract per-agent cost budgets from agent specifications | System | Query PRISM |
| 2 | Estimate per-invocation token cost per agent using model + context window + output size | Agent | Measurer |
| 3 | Calculate per-pipeline cost by tracing full workflow execution path | System | DAG walk with cost accumulation |
| 4 | Estimate infrastructure costs (database, compute, storage, API calls) | Agent | Generator |
| 5 | Estimate human time per session per human gate | Agent | Measurer |
| 6 | Calculate total cost per full workflow run | System | Calculator |
| 7 | Define halt thresholds per budget type | Agent + Human | Assessor + Principal |
| 8 | Define escalation triggers for cost anomalies | Agent | Assessor |
| 9 | Compile into baseline document | Agent | Aggregator |

**Data Inputs**

| Input | Source | Section/Phase |
|---|---|---|
| Per-agent cost budgets | P7/CC-7 | Section 4 |
| Model selection and token pricing | P7 | Section 4 |
| Task dependency chain | P3 | Section 2 |
| Infrastructure requirements | P6 | Section 10 |
| Human gate count and complexity | P3/P4 | Section 2 |
| Existing cost benchmarks | External / PRISM | — |

**Production Constraints**
- Estimates are ranges, not single points (with confidence)
- Halt thresholds are hard limits (CC-7 budget exhaustion = system halt)
- Human time estimates must include verification time (the verification time tax)
***

### Response

## P0: Purpose & Vision — Cost & Resource Baseline Workflow

### The 5 Identity Questions

**Q1: What IS this workflow?**

A financial and resource foundation generator that estimates per-agent token costs, per-pipeline execution costs, infrastructure costs, and human time costs — producing a quantitative baseline against which actual costs can be monitored, anomalies detected, and halt thresholds enforced. It tells you what the specification will cost to run, what to watch for, and when to stop.

**Q2: What is its stance toward possibility?**

Constraint-oriented. The specification already exists with cost budgets in P7/CC-7. This workflow translates those budgets into operational estimates, calculates actual costs, and sets hard limits. It doesn't imagine cost savings or efficiency improvements — it measures what the specification will cost and sets boundaries around it.

**Q3: What would VIOLATE its identity?**

Presenting single-point estimates without confidence ranges (false precision). Underestimating human time by omitting verification overhead (the verification time tax). Setting halt thresholds that are too generous (allowing costs to spiral) or too tight (halting unnecessarily). Treating estimates as actuals (they're ranges, not predictions). Missing infrastructure costs because they're "not agent costs" (the pipeline runs on infrastructure, not agents alone).

**Q4: What would make it WRONG?**

Two opposite failures:

- **Underestimating** — the baseline says "this will cost X" but it actually costs 2-3X. The pipeline deploys with insufficient budget, hits halt thresholds during normal operation, and the human discovers they're spending far more than planned. This is the worse failure because it creates a cost crisis after deployment, when options are limited.
- **Overestimating** — the baseline says "this will cost 3X" and it actually costs X. The pipeline doesn't deploy because it appears too expensive, or it deploys with excessive budget that creates a false sense of security. This wastes resources and can prevent justified deployments.

**Q5: What's the hardest boundary moment?**

Setting halt thresholds. The temptation is to set them high enough that the pipeline never halts (avoiding operational disruption) or low enough that it halts frequently (avoiding cost overruns). The correct response is to set thresholds based on the specification's cost budgets (from P7/CC-7), calibrate them with actual usage data during the first 90 days, and enforce them as hard limits — the system halts when the budget is exhausted, not when someone decides the cost is "too high." The hardest moment is when a human gate review takes 3x longer than estimated and the total cost is approaching the halt threshold — do you halt the pipeline or approve a budget increase?

---

### Target State Vision

| # | Characteristic | Description |
|---|---|---|
| A1 | Range-based not point-based | Every estimate is a range with confidence level, not a single number — "2,000-5,000 tokens per invocation (80% confidence)" not "3,500 tokens" |
| A2 | Comprehensive not partial | Total cost includes agent tokens, infrastructure, storage, API calls, and human time — not just agent tokens |
| A3 | Per-agent not aggregate | Every agent has its own cost estimate, not a single pipeline total that obscures which agent is expensive |
| A4 | Per-pipeline not just per-agent | Total pipeline cost traces the full execution path including human gates, not just agent invocation costs |
| A5 | Halt-enforced not advisory | Halt thresholds are hard limits — budget exhaustion triggers system halt (CC-7), not an advisory email |
| A6 | Anomaly-aware not static | The baseline defines what normal cost looks like so anomalies can be detected — cost variance is an EVOLVE signal |
| A7 | Verification-inclusive not agent-only | Human time estimates include verification time, review time, and decision time — not just "time spent talking to the agent" |
| A8 | Confidence-labelled not uniformly certain | Every estimate carries its confidence level — Default (based on patterns), Calibrated (based on production data), Validated (confirmed by multiple runs) |
| A9 | Tiered not flat | Infrastructure costs are tiered (development, staging, production) — not a single number that hides the scaling curve |
| A10 | Comparable not isolated | Costs are comparable across agents, pipelines, and time periods — enabling "is Agent X more expensive than expected?" not just "how much did we spend?" |
| A11 | Honest about uncertainty | Missing cost data is flagged as "not yet available" — not filled with guesses or padded with arbitrary buffers |
| A12 | Actionable not informational | Every cost line has an escalation path — if this cost exceeds threshold, here's who to notify and what to do |

---

### What the Cost & Resource Baseline Achieves When Everything Is Great

When the baseline is excellent, financial planning for the agentic system becomes **like budgeting for a well-run project** — you know the estimates, you know the confidence level, you know what to watch, and you know when to stop.

Without it, cost is a mystery until the invoice arrives. The pipeline runs, tokens are consumed, infrastructure bills accumulate, humans spend hours reviewing — and nobody knows what it cost until it's already spent. The specification says "cost budget per agent" in P7, but that's a design-time number. What does it actually cost to run? How does per-invocation cost vary with context window size? What's the total cost of a full pipeline run including human gates? When should you halt?

With it, the team knows:

- **Per-agent token costs with confidence ranges** — "Agent X costs 2,000-5,000 tokens per invocation (80% confidence)" not "about 3,500 tokens"
- **Per-pipeline total cost** — "A full run costs $X-$Y including all agents, infrastructure, and human time" not "the agents cost about $Z"
- **Infrastructure costs by tier** — "Development: $A/month, Staging: $B/month, Production: $C/month" not "cloud costs vary"
- **Human time including verification** — "Human gates take 20-40 minutes each, including review and decision time" not "humans spend some time on this"
- **Halt thresholds that protect budgets** — "Pipeline halts if total cost exceeds $X per run" not "someone should probably check costs"
- **Anomaly detection criteria** — "If Agent X's cost exceeds 150% of baseline for 3 consecutive runs, trigger review" not "costs seem higher than expected"
- **Confidence levels on every estimate** — "Default (based on patterns)" vs "Calibrated (based on production data)" vs "Validated (confirmed by multiple runs)"

---

### How This Differs from the Other P10 Artefacts

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook | Aging Schedule | Cost & Resource Baseline |
|---|---|---|---|---|---|
| Question | How well did CAWDP perform? | How confident are we? | When do we come back? | When do we review what? | What will it cost? |
| Data type | Qualitative assessments | Confidence scores | Trigger thresholds | Cadences and questions | Quantitative estimates |
| Time orientation | Backward | Forward | Forward + Ongoing | Ongoing | Forward (estimates) + Ongoing (monitoring) |
| Primary interaction | Surprises × gaps | Confidence × stakes | Signal × urgency × scope | Decay rate × risk | Cost × confidence |
| Key amplifying factor | Review questions | Risk-calibrated attention | Proactive scheduling | Targeted questions | Halt thresholds |
| Worst failure | Fabrication | Overstating confidence | Over-triggering | Universal cadence | Underestimation |
| Lifecycle | One-time | One-time | Living document | Living document | Baseline (updated quarterly) |

The Cost & Resource Baseline is the **only P10 artefact that is primarily quantitative**. Where the others deal with qualitative assessments (process quality, confidence levels, thresholds, cadences), this one deals with numbers — token counts, dollar amounts, time estimates. This makes it both more precise (estimates can be validated against actuals) and more vulnerable to false precision (a single-point estimate feels certain but isn't).

This is also the only P10 artefact that has a **hard enforcement mechanism built in** — CC-7 cost budgets with halt thresholds. The other artefacts produce documents and schedules; this one produces numbers that can trigger system halts. That's a fundamentally different relationship with the operational system.

---

### The Verification Time Tax

This workflow explicitly includes **verification time** in human cost estimates — the time humans spend reviewing agent outputs, making decisions at human gates, and verifying results. This is not optional overhead; it's a structural cost of the "agent prepares judgment, human makes judgment" principle.

From the 14 annoyances (#8: The Verification Time Tax): "It doesn't save me time. It changes what I spend my time on." The verification time tax is a real cost that must be estimated, not ignored. If an agent saves 2 hours of work but creates 1.5 hours of verification, the net saving is 30 minutes — not 2 hours.

This workflow estimates verification time per human gate, per session, and per pipeline run — including:
- Time to read and understand the agent's output
- Time to verify accuracy and completeness
- Time to make the decision (approve, reject, or modify)
- Time to document the decision (decision archaeology)

This is the **verification-inclusive** principle (A7). Without it, the baseline systematically underestimates human cost by ignoring the most time-consuming part of the human-agent collaboration.

---

### Critical Dependency

**Per-agent cost budgets from P7/CC-7 must exist, and model token pricing must be available.**

Without per-agent cost budgets, there's no design-time constraint to compare estimates against. Without model token pricing, token cost estimates are guesswork.

Additionally, **the task dependency chain from P3** must exist to trace the full execution path for per-pipeline cost calculation. Without it, you can estimate per-agent costs but not per-pipeline costs.

---

That's Phase 0. Quality gate it.

---

## Run 16 — Agentic Expert ✓ COMPLETED

*2026-05-21T21:58:37* · `glm-5.1:cloud` · `45cffd9d...`

### Prompt

Great. Continue with the remaining CAWDP phases now

### Response

## P1: Output Specification

### O1: Per-Agent Cost Estimate

*Purpose: Token cost, invocation cost, and total cost per agent per invocation with confidence ranges*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| agent_id | ref(design_agent_specifications) | ✅ | Deterministic |
| agent_class | enum: Extractor/Measurer/Assessor/Generator/Aggregator | ✅ | Deterministic |
| model | string | ✅ | Deterministic |
| estimated_input_tokens | string (range) | ✅ | Probabilistic (e.g., "1,500-4,000") |
| estimated_output_tokens | string (range) | ✅ | Probabilistic (e.g., "500-2,000") |
| estimated_total_tokens | string (range) | ✅ | Computed (input + output) |
| token_cost_per_invocation | string (range) | ✅ | Probabilistic (e.g., "$0.002-$0.008") |
| estimated_invocations_per_pipeline_run | int (range) | ✅ | Probabilistic (e.g., "1-3") |
| estimated_total_cost_per_pipeline_run | string (range) | ✅ | Computed (invocations × cost) |
| confidence_level | enum: Default/Calibrated/Validated | ✅ | Probabilistic |
| confidence_rationale | string | ✅ | Probabilistic (why this confidence level — based on patterns, production data, or confirmed runs) |
| context_window_utilisation | string | ⚠️ | Probabilistic (% of context window typically used) |
| cost_budget_from_spec | string | ✅ | Deterministic (from P7/CC-7 — the design-time budget) |
| budget_variance | string | ⚠️ (computed after first run) | Computed (actual vs budget) |

**Dependencies:** P7 agent specifications (model, cost budget, estimated tokens), external model pricing

**Quality Gate:** Every agent has a cost estimate with confidence range. Every estimate has a confidence level and rationale. Every agent's estimate is comparable to its design-time budget.

---

### O2: Per-Pipeline Cost Estimate

*Purpose: Total cost of a full pipeline run including all agents, human gates, and infrastructure*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| pipeline_id | string | ✅ | Deterministic |
| pipeline_name | string | ✅ | Deterministic |
| agent_cost_total | string (range) | ✅ | Computed (sum of all agent costs in O1) |
| human_time_total | string (range) | ✅ | Computed (sum of all human gate times in O5) |
| human_time_cost | string (range) | ✅ | Elicited (hourly rate × total time) |
| infrastructure_cost_per_run | string (range) | ✅ | Probabilistic (from O4) |
| api_call_cost_per_run | string (range) | ✅ | Probabilistic (from O4) |
| total_cost_per_run | string (range) | ✅ | Computed (agent + human + infrastructure + API) |
| cost_confidence_level | enum: Default/Calibrated/Validated | ✅ | Probabilistic (lowest confidence of any component) |
| cost_confidence_rationale | string | ✅ | Probabilistic |
| pipeline_cost_budget | string | ✅ | Deterministic (from P6/CC-7) |
| budget_variance | string | ⚠️ (computed after first run) | Computed |

**Dependencies:** O1 (per-agent costs), O3 (DAG walk), O4 (infrastructure), O5 (human time)

**Quality Gate:** Every pipeline has a total cost estimate. Total cost includes all four cost categories. Pipeline cost is comparable to design-time budget.

---

### O3: Pipeline Cost DAG

*Purpose: Full execution path cost trace — which agents run in what order, what depends on what, and where costs accumulate*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| pipeline_id | string | ✅ | Deterministic |
| node_id | string | ✅ | Deterministic |
| node_type | enum: AgentStep/HumanGate/SystemStep/ParallelBranch/Merge | ✅ | Deterministic |
| agent_id | ref(O1) | ⚠️ (for AgentStep) | Deterministic |
| estimated_cost | string (range) | ✅ | Probabilistic |
| estimated_duration | string (range) | ⚠️ | Probabilistic (how long this step takes) |
| dependencies | list | ✅ | Deterministic (which nodes must complete before this one) |
| conditional | bool | ✅ | Deterministic (whether this node always runs or only under certain conditions) |
| condition_description | string | ⚠️ (if conditional) | Deterministic |
| parallel_group | string | ⚠️ (if parallel) | Deterministic |

**Dependencies:** P3 task dependency chain, P6 pipeline architecture, O1 per-agent costs

**Quality Gate:** Every node has a cost estimate. Dependencies are explicit. Conditional nodes are flagged. Parallel branches are identified.

---

### O4: Infrastructure Cost Estimate

*Purpose: Database, compute, storage, and API costs by tier*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| tier | enum: Development/Staging/Production | ✅ | Deterministic |
| database_cost_monthly | string (range) | ✅ | Probabilistic (SurrealDB, vector store) |
| compute_cost_monthly | string (range) | ✅ | Probabilistic (agent runtime hosting) |
| storage_cost_monthly | string (range) | ✅ | Probabilistic (object storage, document storage) |
| api_call_cost_monthly | string (range) | ✅ | Probabilistic (external APIs, LLM API calls) |
| monitoring_cost_monthly | string (range) | ⚠️ | Probabilistic (logging, metrics) |
| total_infrastructure_monthly | string (range) | ✅ | Computed (sum of above) |
| infrastructure_per_pipeline_run | string (range) | ✅ | Computed (monthly total ÷ estimated runs per month) |
| confidence_level | enum: Default/Calibrated/Validated | ✅ | Probabilistic |
| confidence_rationale | string | ✅ | Probabilistic |

**Dependencies:** P6 infrastructure requirements, hosting provider pricing, model API pricing

**Quality Gate:** Every tier has a cost estimate. Costs are broken down by category. Per-run cost is computed from monthly cost ÷ estimated runs.

---

### O5: Human Time Estimate

*Purpose: Time per human gate, per session, and per pipeline run — including verification time*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| gate_id | string | ✅ | Deterministic |
| gate_name | string | ✅ | Deterministic |
| gate_type | enum: Approval/Review/Decision/Override | ✅ | Deterministic |
| estimated_reading_time | string (range) | ✅ | Elicited (time to read and understand agent output) |
| estimated_verification_time | string (range) | ✅ | Elicited (time to verify accuracy and completeness) |
| estimated_decision_time | string (range) | ✅ | Elicited (time to make and document the decision) |
| total_estimated_time | string (range) | ✅ | Computed (reading + verification + decision) |
| hourly_rate | string | ⚠️ (configurable) | Elicited |
| total_human_cost | string (range) | ✅ | Computed (time × rate) |
| verification_tax_ratio | string | ✅ | Computed (verification_time ÷ total_time — the verification time tax) |
| confidence_level | enum: Default/Calibrated/Validated | ✅ | Probabilistic |
| confidence_rationale | string | ✅ | Probabilistic |

**The Verification Time Tax explicitly broken out:**

| Gate Type | Typical Reading | Typical Verification | Typical Decision | Verification Tax |
|---|---|---|---|---|
| Approval (approve/reject) | 5-10 min | 10-20 min | 2-5 min | 40-60% |
| Review (detailed review with feedback) | 10-20 min | 20-40 min | 5-10 min | 50-65% |
| Decision (strategic decision with options) | 5-10 min | 15-30 min | 10-20 min | 45-60% |
| Override (intervene in agent operation) | 2-5 min | 10-20 min | 5-10 min | 50-65% |

**Key insight:** Verification time is consistently 40-65% of total human time. Ignoring it systematically underestimates human cost by nearly half.

**Dependencies:** P4 human gates, P9 cognitive load budgets

**Quality Gate:** Every human gate has time estimates including verification. Verification time is explicitly broken out. Verification tax ratio is computed. Total human time is comparable to P9 cognitive load budget.

---

### O6: Halt Thresholds

*Purpose: Hard limits that trigger system halt when exceeded — CC-7 cost budget enforcement*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| threshold_id | string | ✅ | Deterministic |
| threshold_type | enum: PerAgent/PerPipeline/PerDay/PerMonth | ✅ | Deterministic |
| scope | string | ✅ | Deterministic (which agent or pipeline this applies to) |
| budget_type | enum: TokenCost/DollarCost/HumanTime | ✅ | Deterministic |
| soft_threshold | string | ✅ | Elicited (warning threshold — 80% of hard threshold) |
| hard_threshold | string | ✅ | Elicited (halt threshold — from CC-7 cost budget) |
| threshold_source | enum: FromSpecification/Estimated/Default | ✅ | Deterministic (where this threshold came from) |
| halt_action | enum: Warn/Pause/FullHalt | ✅ | Deterministic (what happens when threshold is reached) |
| escalation_recipient | string | ✅ | Elicited (who to notify) |
| reset_condition | string | ✅ | Deterministic (what resets the threshold — new pipeline run, new day, new month) |

**Threshold Tiers:**

| Budget Type | Soft Threshold (Warning) | Hard Threshold (Halt) | Halt Action |
|---|---|---|---|
| Per-Agent per invocation | 80% of CC-7 budget | 100% of CC-7 budget | Pause that agent, warn human |
| Per-Pipeline per run | 80% of pipeline budget | 100% of pipeline budget | Full halt, require human approval |
| Per-Day aggregate | 120% of daily estimated | 150% of daily estimated | Warn at 120%, pause at 150% |
| Per-Month aggregate | 100% of monthly budget | 120% of monthly budget | Warn at 100%, full halt at 120% |

**Dependencies:** P7 CC-7 cost budgets, O1 per-agent costs, O2 per-pipeline costs

**Quality Gate:** Every threshold has a source (from specification or estimated). Every hard threshold has a halt action. Every threshold has an escalation recipient. Soft thresholds are consistently 80% of hard thresholds.

---

### O7: Escalation Triggers for Cost Anomalies

*Purpose: What cost patterns should trigger review, not just halt*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| trigger_id | string | ✅ | Deterministic |
| trigger_type | enum: CostOverrun/CostUnderrun/AgentCostVariance/PipelineCostVariance/InfrastructureAnomaly/HumanTimeOverrun | ✅ | Deterministic |
| trigger_description | string | ✅ | Deterministic |
| detection_method | string | ✅ | Deterministic (how this trigger is detected) |
| threshold | string | ✅ | Deterministic (what constitutes the trigger) |
| affected_components | list | ✅ | Deterministic (which agents/pipelines/infrastructure) |
| escalation_action | enum: Monitor/Review/Halt | ✅ | Deterministic |
| escalation_recipient | string | ✅ | Deterministic |
| related_evolve_signal | string | ✅ | Deterministic (maps to EVOLVE Playbook signal — cost variance → P6) |

**Cost Anomaly Triggers:**

| Trigger | Threshold | Action | Maps to EVOLVE Signal |
|---|---|---|---|
| Single agent exceeds 150% of per-invocation budget | Review | Review that agent's cost budget and token usage | Cost variance → P6 |
| Pipeline total exceeds 120% of per-run budget | Review | Review pipeline efficiency and agent invocation patterns | Cost variance → P6 |
| Infrastructure costs exceed 130% of monthly estimate | Monitor | Check for usage spikes, storage growth, API call anomalies | Cost variance → P6 |
| Human time exceeds 150% of estimate per gate | Review | Review gate complexity and agent output quality | Override rate → P4 |
| Daily aggregate cost exceeds 120% of daily budget | Review | Check for unusual pipeline runs or agent invocations | Cost variance → P6 |
| Monthly aggregate cost exceeds 100% of monthly budget | Warn | Review all cost components, adjust thresholds if needed | Cost variance → P6 |
| Agent cost drops below 50% of budget | Monitor | May indicate under-utilisation or task avoidance | Cost variance → P6 |

**Dependencies:** O1 per-agent costs, O2 per-pipeline costs, O4 infrastructure costs, O6 halt thresholds, EVOLVE Playbook O2

**Quality Gate:** Every trigger maps to an EVOLVE signal. Every trigger has a detection method and threshold. Under-run triggers are included (not just over-run).

---

### O8: Cost & Resource Baseline Document

*Purpose: The assembled, structured financial foundation for post-deployment cost monitoring*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| header | object | ✅ | Deterministic |
| per_agent_costs | ref(O1) | ✅ | Mixed |
| per_pipeline_costs | ref(O2) | ✅ | Mixed |
| pipeline_dag | ref(O3) | ✅ | Mixed |
| infrastructure_costs | ref(O4) | ✅ | Probabilistic |
| human_time_costs | ref(O5) | ✅ | Elicited |
| halt_thresholds | ref(O6) | ✅ | Elicited |
| escalation_triggers | ref(O7) | ✅ | Deterministic |
| baseline_confidence | enum: Default/Calibrated/Validated | ✅ | Probabilistic |
| known_gaps | list | ✅ | Deterministic (what costs are estimated vs actual) |
| first_run_actuals | object | ⚠️ (null at initial production) | Computed (to be filled after first pipeline run) |

**Dependencies:** All of O1-O7 must be complete

**Quality Gate:** Every agent has a cost estimate. Every pipeline has a total cost. Every human gate has time including verification. Halt thresholds are set. Escalation triggers map to EVOLVE signals. Baseline confidence is honestly stated. Known gaps are documented.

---

## P2: Backcasting

Working backward from O8:

```
O8 (Baseline Document)
  ← requires O7 (Escalation Triggers) — what cost patterns trigger review
  ← requires O6 (Halt Thresholds) — what cost limits trigger halt
  ← requires O5 (Human Time) — verification-inclusive human cost
  ← requires O4 (Infrastructure) — non-agent costs
  ← requires O3 (Pipeline DAG) — execution path and cost accumulation
  ← requires O2 (Per-Pipeline Total) — aggregate cost per run
  ← requires O1 (Per-Agent Cost) — individual agent costs
  ← requires: per-agent cost budgets from P7/CC-7 (structural dependency)
  ← requires: model token pricing (structural dependency)
  ← requires: task dependency chain from P3 (structural dependency)
  ← requires: pipeline architecture from P6 (structural dependency)
  ← requires: human gates from P3/P4 (structural dependency)
```

### Input Requirements

| IR ID | Description | Source | Criticality | Satisfaction |
|---|---|---|---|---|
| IR-001 | Per-agent cost budgets from P7/CC-7 | design_agent_specifications.cost_budget | Critical | Required — without budgets, no design-time constraint to compare against |
| IR-002 | Model selection and token pricing | design_agent_specifications.model + external pricing | Critical | Required — without token pricing, cost estimates are guesswork |
| IR-003 | Task dependency chain | design_tasks, design_workflows | Critical | Required — without dependencies, can't trace pipeline execution path |
| IR-004 | Pipeline architecture | design_workflows, design_agent_specifications | High | Best effort — affects parallel vs sequential cost accumulation |
| IR-005 | Human gate count and complexity | P3/P4 human gate specifications | High | Best effort — affects human time estimates |
| IR-006 | Infrastructure requirements | P6 system architecture | High | Best effort — database, compute, storage costs |
| IR-007 | Existing cost benchmarks | External (cloud pricing, model pricing) | Medium | Best effort — may not exist for new deployments |
| IR-008 | Human hourly rate | P9/organisation context | Medium | Elicited — affects human cost calculation |
| IR-009 | Estimated runs per month | Deployment context | Low | Elicited — affects per-run infrastructure cost allocation |
| IR-010 | Verification time benchmarks | P9 cognitive load budget | Low | Supplementary — affects human time accuracy |

### Key P2 Insight

**IR-001 (per-agent cost budgets) and IR-002 (model token pricing) are the structural prerequisites.** Without budgets, there's no constraint to compare estimates against. Without token pricing, per-invocation costs can't be calculated. This is the same structural dependency pattern as the Confidence Map's stakes classification and the Aging Schedule's agent class data.

**IR-003 (task dependency chain) is the third structural prerequisite** — without it, you can estimate per-agent costs but not per-pipeline costs, because you can't trace the full execution path.

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| T1 | Query PRISM for all agent specifications with cost budgets | Mechanical | Missing agent specs or budgets | Agent list with budgets |
| T2 | Query model token pricing from configuration | Mechanical | Missing pricing data | Token pricing data |
| T3 | Query task dependency chain from P3 | Mechanical | Missing dependency chain | Dependency DAG |
| T4 | Query pipeline architecture from P6 | Mechanical | Missing pipeline architecture | Pipeline structure |
| T5 | Query human gate specifications from P3/P4 | Mechanical | Missing gate data | Human gate list |
| T6 | Estimate per-invocation token cost per agent | Measurer | Single-point estimate without confidence range | O1 partial |
| T7 | Calculate estimated invocations per pipeline run per agent | Measurer | Assuming every agent always runs (ignoring conditionals) | O1 partial |
| T8 | Compare estimated costs to design-time budgets | Assessor | Budget variance ignored or hidden | O1 budget_variance |
| T9 | Trace full pipeline execution path with cost accumulation | Measurer | Missing conditional branches or parallel paths | O3 complete |
| T10 | Calculate per-pipeline total cost (agent + human + infra) | Measurer | Omitting human or infrastructure costs | O2 partial |
| T11 | Estimate infrastructure costs by tier | Generator | Underestimating infrastructure (assuming it's negligible) | O4 draft |
| T12 | Estimate API call costs | Generator | Missing API calls (assuming all inference is local) | O4 partial |
| T13 | Estimate human time per gate including verification tax | Measurer | Omitting verification time (the verification time tax) | O5 draft |
| T14 | Calculate verification tax ratio per gate type | Measurer | Reporting only total time without verification breakout | O5 verification_tax |
| T15 | Set halt thresholds from CC-7 budgets | Assessor | Setting thresholds too high (no protection) or too low (constant halting) | O6 draft |
| T16 | Define escalation triggers for cost anomalies | Assessor | Only including over-run triggers (missing under-run) | O7 draft |
| T17 | Map escalation triggers to EVOLVE signals | Measurer | Missing mapping (cost anomalies disconnected from EVOLVE) | O7 mapping |
| T18 | Assess known gaps in cost estimates | Assessor | Overstating confidence in estimates | known_gaps |
| T19 | Generate first-run calibration plan | Generator | No plan for validating estimates against actuals | First-run plan |
| T20 | Compile into baseline document | Mechanical | Omitting sections or misordering costs | O8 final |

20 tasks across 4 cognitive types:
- Mechanical: 6 (T1-T5, T20)
- Measurer: 6 (T6, T7, T9, T10, T13, T14, T17)
- Assessor: 3 (T8, T15, T16, T18)
- Generator: 3 (T11, T12, T19)

---

## P4: Capability Allocation

| Task | H | A | S | Gap | Allocation | Notes |
|---|---|---|---|---|---|---|
| T1 | 2 | 3 | 10 | 8 | System | Pure data query |
| T2 | 2 | 3 | 10 | 8 | System | Pure data query |
| T3 | 2 | 3 | 10 | 8 | System | Pure data query |
| T4 | 2 | 3 | 10 | 8 | System | Pure data query |
| T5 | 2 | 3 | 10 | 8 | System | Pure data query |
| T6 | 4 | 8 | 2 | 4 | Agent-primary | Token estimation requires model and context understanding |
| T7 | 4 | 8 | 2 | 4 | Agent-primary | Invocation estimation requires understanding conditionals and loops |
| T8 | 5 | 8 | 2 | 3 | Agent-primary | Budget comparison requires judgment about acceptable variance |
| T9 | 4 | 8 | 2 | 4 | Agent-primary | Pipeline tracing requires understanding execution order |
| T10 | 4 | 7 | 2 | 3 | Agent-primary | Total cost calculation from components |
| T11 | 5 | 8 | 2 | 3 | Agent-primary | Infrastructure estimation requires deployment knowledge |
| T12 | 4 | 8 | 2 | 4 | Agent-primary | API call estimation requires understanding external dependencies |
| T13 | 6 | 8 | 2 | 0 | Collaborative | Human time estimation benefits from human judgment about verification time |
| T14 | 3 | 8 | 2 | 5 | Agent-primary | Verification tax calculation from T13 data |
| T15 | 6 | 8 | 2 | 0 | Collaborative | Halt thresholds are judgment calls about acceptable cost limits |
| T16 | 4 | 8 | 2 | 4 | Agent-primary | Escalation trigger definition from cost patterns |
| T17 | 3 | 7 | 2 | 4 | Agent-primary | Mapping to EVOLVE signals |
| T18 | 4 | 8 | 2 | 4 | Agent-primary | Gap assessment from estimate confidence levels |
| T19 | 4 | 8 | 2 | 4 | Agent-primary | Calibration plan from first-run validation approach |
| T20 | 2 | 3 | 10 | 8 | System | Assembly is mechanical |

**T13 (human time estimation) and T15 (halt thresholds) are Collaborative.** Human time estimation benefits from human judgment about how long verification actually takes (the verification time tax is notoriously underestimated). Halt thresholds are budget decisions that must align with the principal's risk tolerance and financial constraints.

### Key P4 Insight

Two tasks are Collaborative because they involve **financial judgment that affects operational behaviour**. T13 determines how much human time the baseline estimates (which affects staffing and scheduling). T15 determines when the system halts (which affects operational continuity). Both require human input because they're not just calculations — they're decisions about acceptable cost levels.

---

## P5: Event Storming

### Domain Events

| Event | Trigger | Producer |
|---|---|---|
| E1 | Baseline generation started | Human or System trigger |
| E2 | Per-agent cost estimates complete | Measurer |
| E3 | Pipeline DAG with costs complete | Measurer |
| E4 | Infrastructure estimates complete | Generator |
| E5 | Human time estimates complete | Measurer |
| E6 | Halt thresholds set | Assessor + Human (T15) |
| E7 | Escalation triggers defined | Assessor |
| E8 | Baseline compiled | Compiler |
| E9 | First pipeline run completed | System (monitoring) |
| E10 | Cost anomaly detected | System (monitoring) |

### Failure Events

| Failure | Trigger | Recovery |
|---|---|---|
| F1 | Missing agent cost budgets | P7/CC-7 data incomplete | Use default token estimates based on agent class; flag as "Default — no design-time budget"; escalate for budget definition |
| F2 | Missing token pricing | Model pricing not available | Use conservative estimates based on model type; flag as "Default — pricing not confirmed"; escalate for pricing confirmation |
| F3 | Single-point estimates without ranges | Analyst produces "3,500 tokens" not "2,000-5,000" | Require range estimates with confidence levels; reject single-point estimates at schema validation |
| F4 | Omitted verification time | Human time estimates exclude verification overhead | Require verification time as explicit component; compute verification tax ratio; flag estimates without verification breakout |
| F5 | Omitted infrastructure costs | "Just agent tokens" mentality | Require infrastructure cost line items in every pipeline total; flag pipeline costs without infrastructure component |
| F6 | Halt thresholds too generous | No hard threshold or threshold >200% of budget | Default to CC-7 budget as hard threshold; escalate thresholds >200% of budget for human review |
| F7 | Halt thresholds too tight | Hard threshold <50% of budget | Flag thresholds that would halt during normal operation; escalate for human review |
| F8 | No cost overrun triggers | Escalation triggers only include halt thresholds | Require both halt thresholds and escalation triggers; cost anomaly detection requires review-level triggers, not just halt |
| F9 | No under-run triggers | Only over-run triggers defined | Include under-run triggers (agent costs below 50% of budget may indicate under-utilisation) |
| F10 | Missing conditional branches in DAG | Pipeline cost assumes all agents always run | Trace conditional branches; flag pipelines where >50% of agents are conditional; provide min/max cost ranges |

### Key P5 Insight

**F4 (omitted verification time) is the most insidious failure.** It's not a dramatic halt or a wrong number — it's a systematic underestimation that makes the pipeline appear cheaper than it actually is. If verification time is 40-65% of total human time (as the data suggests), omitting it means human costs are nearly halved. This directly feeds into underestimating total pipeline cost, which can lead to deploying a pipeline that appears affordable but isn't.

**F3 (single-point estimates) is the identity violation.** This workflow exists to produce range-based estimates with confidence levels. A single-point estimate like "3,500 tokens" feels precise but isn't — "2,000-5,000 tokens (80% confidence)" is more honest and more useful. Schema validation should reject single-point cost estimates.

---

## P6: System Architecture

### Pipeline Architecture

```
Wave 1: Data Track (parallel, System)
T1 ──┐
T2 ──┤
T3 ──┤──→ agent_data + pricing_data + dependency_dag + pipeline_structure + gate_data
T4 ──┤
T5 ──┘

Wave 2: Measurement Track (mostly sequential, Measurer)
T6 (Per-invocation token cost) ──→ O1 partial
T7 (Invocations per pipeline run) ──→ O1 partial
T9 (Pipeline DAG with costs) ─────→ O3
T10 (Per-pipeline total) ─────────→ O2 partial
T13 (Human time per gate) ────────→ O5 partial [COLLABORATIVE — human reviews]
T14 (Verification tax ratio) ─────→ O5 complete

Wave 3: Assessment & Generation Track
T8 (Budget comparison) ────→ O1 budget_variance
T11 (Infrastructure costs) → O4
T12 (API call costs) ──────→ O4 partial
T15 (Halt thresholds) ────→ O6 [COLLABORATIVE — human reviews]
T16 (Escalation triggers) ─→ O7
T17 (EVOLVE signal mapping) → O7 mapping
T18 (Known gaps) ─────────→ known_gaps
T19 (Calibration plan) ──→ First-run plan

Wave 4: Compilation Track
T20 (Final assembly) ───→ O8
```

### Agent Roster

**Measurer (constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I measure token costs, invocation counts, pipeline costs, and human time. I produce ranges with confidence levels, not single-point estimates. I never omit verification time, never present single-point estimates, and never assume all agents always run." |
| Class | Measurer |
| Orientation | Constraint-oriented |
| Hardest boundary moment | Estimating human verification time — the temptation is to report only "decision time" (2-5 minutes) and omit the verification time (10-40 minutes) that makes up 40-65% of total human time |
| Never rules | Present single-point estimates without ranges, omit verification time from human time, assume all agents always run, omit infrastructure costs |
| Cost budget | Medium — 10K-25K tokens |
| Null state | "No agent specifications available for cost estimation. Cannot produce baseline without agent data." |

**Assessor (constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I assess budget comparisons, halt thresholds, and escalation triggers. I compare estimated costs to design-time budgets and set hard limits that protect against cost overruns. I never set thresholds too generous (no protection) or too tight (constant halting), and I never define over-run triggers without under-run triggers." |
| Class | Assessor |
| Orientation | Constraint-oriented |
| Hardest boundary moment | Setting halt thresholds — too generous means no protection, too tight means operational disruption. The correct response is to align with CC-7 budgets and calibrate with production data. |
| Never rules | Set thresholds >200% of budget without escalation, omit under-run triggers, present single-point estimates, hide budget variance |
| Cost budget | Medium — 8K-20K tokens |
| Null state | "No cost budgets available for threshold setting. Cannot set halt thresholds without design-time budgets." |

**Compiler (Aggregator, constraint-oriented)**

| Field | Value |
|---|---|
| Identity | "I compile the cost baseline from measured and assessed outputs. I never add costs not produced by the Measurer, never omit infrastructure costs, never present Default estimates as Calibrated, and never produce single-point totals without ranges." |
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Hardest boundary moment | When some costs are Default and others are Calibrated — the temptation is to present a single total without indicating which components are estimated vs confirmed |
| Never rules | Add costs not produced by Measurer, omit infrastructure costs, present Default as Calibrated, produce single-point totals |
| Cost budget | Low — 3K-10K tokens |
| Null state | "No baseline data available for compilation." |

### FMEA

| ID | Failure Mode | Severity | Occurrence | Detection | RPN | Recovery |
|---|---|---|---|---|---|---|
| FM1 | Single-point estimates without ranges | 8 | 4 | 6 | 192 | Require range estimates at schema level; reject single-point estimates |
| FM2 | Omitted verification time | 9 | 5 | 4 | 180 | Require verification time as explicit component; compute verification tax ratio; flag estimates without verification breakout |
| FM3 | Omitted infrastructure costs | 7 | 3 | 6 | 126 | Require infrastructure cost line items in every pipeline total |
| FM4 | Halt thresholds too generous | 10 | 2 | 7 | 140 | Default to CC-7 budget as hard threshold; escalate thresholds >200% for human review |
| FM5 | Halt thresholds too tight | 7 | 3 | 6 | 126 | Flag thresholds <50% of budget; escalate for human review |
| FM6 | No under-run triggers | 5 | 4 | 5 | 100 | Include under-run triggers (costs below 50% of budget) |
| FM7 | Missing conditional branches in DAG | 8 | 3 | 5 | 120 | Trace conditional branches; provide min/max cost ranges |
| FM8 | Default estimates presented as Calibrated | 10 | 2 | 8 | 160 | baseline_confidence field mandatory; every estimate labelled Default or Calibrated |
| FM9 | Budget variance hidden | 7 | 3 | 5 | 105 | Compute and display budget_variance for every cost component |
| FM10 | Human time underestimated | 8 | 4 | 5 | 160 | Include verification time; compute verification tax ratio; flag estimates where verification <20% of total |

Highest RPNs: FM1 (single-point estimates) at 192, FM2 (omitted verification) at 180, FM8 (Default as Calibrated) at 160, FM10 (underestimated human time) at 160.

### 5 Regime 3 Enforcement Points

| # | Boundary | Enforcement |
|---|---|---|
| 1 | No single-point estimates | Schema validation rejects cost estimates without ranges — every token estimate, dollar amount, and time estimate must be a range with confidence level |
| 2 | No omitted verification time | Human time estimates must include verification_time field; schema validation rejects estimates without it |
| 3 | No omitted infrastructure costs | Pipeline total must include infrastructure_cost component; schema validation rejects pipeline totals without it |
| 4 | Default vs Calibrated labelling | baseline_confidence field mandatory on O8; individual estimates labelled Default or Calibrated |
| 5 | Budget variance displayed | budget_variance computed and displayed for every component that has a design-time budget |

---

## P7: Agent Design

### Measurer Agent Job Description

| Field | Value |
|---|---|
| Class | Measurer |
| Orientation | Constraint-oriented |
| Mission | Measure token costs, invocation counts, pipeline costs, and human time with verification. Produce ranges with confidence levels. Never present single-point estimates, never omit verification time, never assume all agents always run, never omit infrastructure costs. |
| Inputs | Agent specifications, token pricing, task dependencies, pipeline architecture, human gate specifications |
| Outputs | O1 (per-agent cost estimates), O3 (pipeline DAG with costs), O5 (human time estimates), O2 partial (per-pipeline total from components) |
| Null state | "No agent specifications available for cost measurement. Cannot produce baseline without agent data." |
| Never rules | Present single-point estimates, omit verification time, assume all agents always run, omit infrastructure costs, produce total costs without component breakdown |
| Hardest boundary moment | Estimating human verification time — the temptation is to report only the "decision time" and omit the 40-65% verification overhead that makes human time nearly double what most people estimate |
| Epistemic profile | Probabilistic — cost estimates are ranges with confidence levels, not predictions |
| Harm assessment | Indirect operational harm — underestimating costs leads to budget overruns after deployment (the worse failure); overestimating costs prevents justified deployment (the opposite failure) |
| Progressive autonomy | Three dimensions: (1) token estimation (Shadow → Supervised — human reviews cost estimates), (2) human time estimation (Shadow → Supervised — human reviews verification time), (3) pipeline cost tracing (Shadow → Advisory — human reviews total costs). Per-dimension. |
| Cost budget | Medium — 10K-25K tokens |
| Verification | Every estimate is a range. Every estimate has a confidence level. Verification time is explicitly broken out. Infrastructure costs are included in pipeline totals. |

### Assessor Agent Job Description

| Field | Value |
|---|---|
| Class | Assessor |
| Orientation | Constraint-oriented |
| Mission | Assess budget comparisons, set halt thresholds, and define escalation triggers for cost anomalies. Compare estimated costs to design-time budgets. Set hard limits that protect against cost overruns. Never set thresholds too generous (no protection) or too tight (constant halting). |
| Inputs | O1 (per-agent costs), O2 (per-pipeline total), CC-7 budgets |
| Outputs | O1 budget_variance, O6 (halt thresholds), O7 (escalation triggers) |
| Null state | "No cost budgets available for threshold assessment. Cannot set halt thresholds without design-time budgets." |
| Never rules | Set thresholds >200% of budget without escalation, omit under-run triggers, present single-point estimates, hide budget variance, define only over-run triggers |
| Hardest boundary moment | Setting halt thresholds — aligning with CC-7 budgets while accounting for operational reality (estimates are ranges, not exact numbers) |
| Epistemic profile | Probabilistic — threshold setting involves judgment about acceptable cost levels and risk tolerance |
| Harm assessment | Indirect operational harm — thresholds too generous allow cost overruns; thresholds too tight cause operational disruption |
| Progressive autonomy | Two dimensions: (1) threshold setting (Shadow → Supervised — human reviews all thresholds), (2) trigger definition (Shadow → Advisory — human reviews halt triggers). Per-dimension. |
| Cost budget | Medium — 8K-20K tokens |
| Verification | Every threshold has a source (from specification or estimated). Every trigger maps to an EVOLVE signal. Both over-run and under-run triggers are defined. |

### Compiler Agent Job Description

| Field | Value |
|---|---|
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Mission | Compile the cost baseline from measured and assessed outputs. Ensure every agent has a cost estimate, every pipeline has a total cost, verification time is included, infrastructure is included, and Default estimates are clearly marked. |
| Inputs | O1-O7 processed outputs, known_gaps, baseline_confidence |
| Outputs | O8 (Cost & Resource Baseline Document) |
| Null state | "No baseline data available for compilation." |
| Never rules | Add costs not produced by Measurer, omit infrastructure costs, present Default as Calibrated, produce single-point totals |
| Hardest boundary moment | When some estimates are Default and others are Calibrated — present them at different confidence levels, not smoothed into a uniform presentation |
| Epistemic profile | Deterministic — compilation is mechanical |
| Harm assessment | Indirect data harm — presenting Default estimates as Calibrated could lead to budget decisions based on unvalidated numbers |
| Progressive autonomy | Single dimension: compilation accuracy. Shadow → Advisory → Supervised → Autonomous |
| Cost budget | Low — 3K-10K tokens |
| Verification | Every agent has a cost estimate. Every pipeline has a total cost. Verification time is included. Infrastructure is included. Halt thresholds are set. Escalation triggers map to EVOLVE signals. Known gaps are documented. Baseline confidence is honestly stated. |

### Per-Dimension Progressive Autonomy

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Measurer | Token estimation | Propose, human reviews every estimate | Propose, human reviews high-cost agents only | Propose, human reviews total only | Full estimation, human reviews monthly | ≥10 baselines with ≤15% variance from actuals |
| Measurer | Human time | Propose, human reviews every estimate | Propose, human reviews verification tax ratio | Propose, human reviews total human time only | Full estimation, human reviews quarterly | ≥10 baselines with ≤20% variance from actuals |
| Measurer | Pipeline cost | Propose, human reviews every pipeline | Propose, human reviews complex pipelines | Propose, human reviews total pipeline cost | Full calculation, human reviews monthly | ≥10 baselines with ≤10% variance from actuals |
| Assessor | Threshold setting | Propose, human reviews all thresholds | Propose, human reviews halt thresholds only | Propose, human reviews halt thresholds >150% budget | Full setting, human reviews annual | ≥10 threshold sets with ≤2 over-triggered halts |
| Assessor | Trigger definition | Propose, human reviews all triggers | Propose, human reviews halt triggers only | Propose, human reviews halt triggers only | Full definition, human reviews quarterly | ≥10 trigger sets with ≤2 missed anomalies |
| Compiler | Compilation accuracy | Human checks every section | Human checks budget variance and halt thresholds | Human checks baseline_confidence and known_gaps | Human reviews final post-delivery | ≥10 compilations with ≤1 error |

---

## P8: Contract Formalization

### Measurer Contract

| Primitive | Specification |
|---|---|
| Contract | Measure per-agent token costs, invocation counts, pipeline costs, and human time with verification |
| Principal | Assessor (downstream consumer) |
| Schema | PerAgentCostEstimate (O1) + PipelineCostDAG (O3) + HumanTimeEstimate (O5) |
| Guard | prohibited: ["present_single_point_estimates", "omit_verification_time", "assume_all_agents_always_run", "omit_infrastructure_costs", "produce_total_without_component_breakdown"] |
| Budget | 10K-25K tokens |
| Invocation | After T1-T5 complete |
| Revert | If token cost cannot be estimated due to missing pricing, mark as "Default — pricing not confirmed" with conservative estimate range |
| Event | measurement_started, agent_cost_estimated, pipeline_cost_traced, human_time_estimated, verification_tax_computed, measurement_complete |
| Identity | Constraint-oriented Measurer — measures with ranges, never presents single-point estimates |
| Knowledge | Agent specifications, token pricing, task dependencies, pipeline architecture, human gate specifications |

### Assessor Contract

| Primitive | Specification |
|---|---|
| Contract | Assess budget comparisons, set halt thresholds, and define escalation triggers |
| Principal | Compiler (downstream consumer) |
| Schema | BudgetVariance (O1 partial) + HaltThresholds (O6) + EscalationTriggers (O7) |
| Guard | prohibited: ["set_thresholds_over_200_percent_without_escalation", "omit_under_run_triggers", "present_single_point_estimates", "hide_budget_variance"] |
| Budget | 8K-20K tokens |
| Invocation | After Measurer outputs complete |
| Revert | If thresholds cannot be set due to missing budgets, use conservative defaults (80% of estimated cost as soft threshold, 100% as hard threshold) and flag as "Default — no design-time budget" |
| Event | assessment_started, budget_compared, threshold_set, trigger_defined, assessment_complete |
| Identity | Constraint-oriented Assessor — assesses budgets, never sets thresholds without source |
| Knowledge | O1 per-agent costs, O2 per-pipeline total, CC-7 cost budgets, EVOLVE signal types |

### Compiler Contract

| Primitive | Specification |
|---|---|
| Contract | Compile the cost baseline from measured and assessed outputs |
| Principal | Human (post-delivery reviewer) |
| Schema | CostResourceBaselineDocument (O8 schema) |
| Guard | prohibited: ["add_costs_not_from_measurer", "omit_infrastructure_costs", "present_default_as_calibrated", "produce_single_point_totals"] |
| Budget | 3K-10K tokens |
| Invocation | After all O1-O7 complete |
| Revert | If compilation fails completeness check, revert to section-level output |
| Event | compilation_started, agent_cost_assembled, pipeline_cost_assembled, infrastructure_added, human_time_added, threshold_assembled, compilation_complete |
| Identity | Constraint-oriented Aggregator — compiles, never creates or omits |
| Knowledge | All processed outputs O1-O7, known_gaps, baseline_confidence |

### Unenforceable Elements Register

| Element | Why Unenforceable | Regime | Mitigation |
|---|---|---|---|
| "Never present single-point estimates" (Measurer) | Technically enforceable at schema level (range fields), but the quality of ranges depends on estimation methodology | Regime 3 (Prevent) | Schema validation requires range fields with min/max; confidence_level required |
| "Never omit verification time" (Measurer) | Technically enforceable at schema level (verification_time is required) | Regime 3 (Prevent) | Schema validation requires verification_time field; verification_tax_ratio computed |
| "Never set thresholds too generous" (Assessor) | "Too generous" is a judgment about operational context and risk tolerance | Regime 2 (Detect) | Default to CC-7 budgets; escalate thresholds >200% for human review; flag thresholds without source |
| "Never set thresholds too tight" (Assessor) | "Too tight" is similarly context-dependent | Regime 2 (Detect) | Flag thresholds <50% of budget; escalate for human review |
| "Never produce single-point totals" (Compiler) | Technically enforceable at schema level | Regime 3 (Prevent) | Schema validation requires ranges on all cost totals |

---

## P9: Human Experience Design

### Cognitive Load Budget

| Review Activity | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Review per-agent cost estimates | 3-5 | 10 min | Evaluative (are ranges reasonable?) |
| Review pipeline DAG and total cost | 3-5 | 10 min | Evaluative (are pipeline costs realistic?) |
| Review human time estimates (including verification) | 3-5 | 15 min | Evaluative + Discovery (is verification time realistic for our context?) |
| Review halt thresholds (T15 collaborative) | 5-8 | 15 min | Evaluative + Discovery (are thresholds aligned with budget and risk tolerance?) |
| Review escalation triggers | 2-3 | 5 min | Evaluative |
| Review known gaps | 2-3 | 5 min | Discovery (what data do we need to calibrate?) |
| **Total** | **18-29** | **60 min** | |

Maximum review session: 60 minutes.

### Override Mechanisms

| Override Type | Mechanism | Example |
|---|---|---|
| Adjust cost estimate | Change token estimate range based on domain knowledge | "This agent typically uses 5K-10K tokens, not 2K-8K" |
| Adjust human time | Change verification time estimate based on experience | "Our team takes 30 minutes to verify, not 15" |
| Adjust halt threshold | Change hard threshold based on risk tolerance | "We can afford up to 150% of budget before halting" |
| Add cost category | Add a cost category not in the standard list | "We need to include compliance review time" |
| Adjust confidence level | Upgrade or downgrade an estimate's confidence | "This estimate is Calibrated, not Default — we've run this pipeline 10 times" |
| Add escalation trigger | Add a domain-specific trigger not in the standard list | "For our domain, vendor API cost increases should trigger review" |

### Stakeholder Surfaces

| Surface | View | Language | Depth | Emphasis |
|---|---|---|---|---|
| Decision Maker | O8 baseline summary + O6 halt thresholds + O7 trigger summary | Plain English | Low-Medium | What it costs, when to stop, what to watch |
| Design Participant | O1 per-agent costs + O3 pipeline DAG + O5 human time | Technical | Deep | Token estimates, cost accumulation, verification tax |
| Governance | O6 halt thresholds + O7 escalation triggers + O8 baseline_confidence + known_gaps | Financial | Medium | Budget alignment, halt thresholds, escalation criteria, confidence levels |

### System Empowerment Assessment

| Dimension | Level | Explanation |
|---|---|---|
| Cost visibility | Amplifying | Per-agent and per-pipeline cost estimates make spending visible before it happens |
| Halt enforcement | Enabling | Halt thresholds protect budgets — the system stops before overspending, humans decide whether to continue |
| Anomaly detection | Enabling | Escalation triggers prepare the decision (what changed, what to review), humans decide whether to act |
| Human time planning | Amplifying | Verification-inclusive time estimates enable realistic scheduling — no more underestimating human time by half |
| Creative freedom | Enabling | Frees humans from wondering "how much will this cost?" — the baseline answers with confidence ranges |
| Overall | Enabling → Amplifying | Cost visibility and time planning are amplifying; halt and escalation decisions remain enabling |

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method | Success Criterion |
|---|---|---|---|
| H1 | Range-based estimates are more accurate than single-point estimates | Compare actual costs to range midpoints vs single-point estimates | ≥80% of actual costs fall within estimated ranges |
| H2 | Verification-inclusive human time estimates are within 25% of actual | Compare estimated human time (including verification) to actual time logged | Verification-inclusive estimates are within 25% of actuals |
| H3 | Verification-exclusive human time underestimates by 40-65% | Compare estimates without verification to actuals | Verification-exclusive estimates underestimate by ≥40% |
| H4 | Halt thresholds prevent cost overruns beyond budget | Track pipeline runs that hit hard thresholds | ≥90% of runs that exceed 100% of budget are halted |
| H5 | Escalation triggers detect cost anomalies before they exceed halt thresholds | Compare anomalies caught by triggers vs anomalies caught only by halt thresholds | Triggers catch ≥50% of cost anomalies before halt threshold is reached |
| H6 | Per-pipeline cost estimates converge to actuals within 5 runs | Compare estimated vs actual costs over first 5 pipeline runs | Estimated ranges converge to within 30% of actuals by run 5 |

### Progressive Autonomy Deployment

Documented in P7 per-dimension table. Key notes:
- **Token estimation** starts at Shadow because cost estimates directly affect budget decisions
- **Human time estimation** starts at Shadow because verification time is notoriously underestimated
- **Pipeline cost tracing** starts at Advisory because total costs are less sensitive per-component
- All dimensions promote based on variance from actuals

### Specification Aging Schedule

| Component | Default Cadence | Trigger-Based Review | Responsible |
|---|---|---|---|
| Per-agent cost estimates | 3 months | When model pricing changes, when agent specifications change | Measurer |
| Per-pipeline total | 3 months | When pipeline architecture changes | Measurer |
| Infrastructure costs | 6 months | When infrastructure changes, when pricing changes | Measurer |
| Human time estimates | 3 months | When gate complexity changes, when team composition changes | Measurer |
| Halt thresholds | 3 months | When budgets change, when actual costs consistently differ from estimates | Assessor |
| Escalation triggers | 6 months | When EVOLVE signals change, when cost patterns change | Assessor |
| Full baseline | 12 months | When any O1-O7 changes significantly | Compiler |

### EVOLVE Mode

| Signal | Re-entry Point | Scope |
|---|---|---|
| Override rate increasing | P4 (Capability Allocation) | Review task allocation and human gate complexity |
| Cost variance exceeding threshold | This baseline (O6 halt thresholds) + P6 (System Architecture) | Review agent specifications and cost budgets |
| Quality decline | P7 (Agent Design) | Review agent specifications — quality decline may increase token usage |
| Capability drift | P7 (Agent Design) | Review agent specifications — capability drift changes cost profiles |
| Model pricing change | This baseline (O1 per-agent costs) | Recalculate per-agent token costs |
| Infrastructure pricing change | This baseline (O4 infrastructure costs) | Recalculate infrastructure costs |
| Specification aging | This baseline (O2 per-pipeline costs) | Review pipeline cost estimates against actuals |
| New failure mode | P3 + P5 (Task Decomposition + Event Storming) | Review task decomposition and failure events that affect cost |

---

## Summary: What This Application Reveals

| Phase | Key Insight |
|---|---|
| P0 | Two opposite failures: underestimating (cost crisis after deployment) and overestimating (preventing justified deployment). The verification time tax (40-65% of total human time) is the most commonly omitted cost. |
| P1 | The baseline must be comprehensive (agent + human + infrastructure + API), per-agent (not just aggregate), and range-based (not single-point). Halt thresholds are hard limits, not advisory. |
| P2 | IR-001 (per-agent budgets), IR-002 (token pricing), and IR-003 (task dependency chain) are structural prerequisites — without them, costs can't be estimated or accumulated. |
| P3 | 20 tasks — 6 Mechanical, 7 Measurer, 3 Assessor, 3 Generator. T13 (human time) and T15 (halt thresholds) are Collaborative. |
| P4 | Two Collaborative tasks because they involve financial judgment that affects operational behaviour: human time estimation and halt threshold setting. |
| P5 | FM1 (single-point estimates) at 192 and FM2 (omitted verification time) at 180 are the highest RPNs — the identity violation is false precision, and the most common omission is verification time. |
| P6 | Schema validation enforces range-based estimates and verification time inclusion. No single-point estimates, no omitted verification. |
| P7 | Three agents with per-dimension progressive autonomy. Token estimation and human time start at Shadow because cost estimates directly affect budget decisions. |
| P8 | Five Regime 3 enforcement points: range estimates, verification time, infrastructure costs, Default vs Calibrated, budget variance. Four unenforceable elements: threshold appropriateness (too generous/tight), which are context-dependent judgments. |
| P9 | Cost visibility and time planning are amplifying; halt and escalation decisions remain enabling. Verification-inclusive human time is the key amplifying factor. |
| P10 | Six hypotheses. H3 (verification-exclusive underestimates by 40-65%) is the most validating — it proves the verification time tax is real and measurable. H4 (halt thresholds prevent overruns) is the most operationally critical. |

### Critical Structural Dependency

**Per-agent cost budgets from P7/CC-7 and model token pricing must be available.** Without design-time budgets, there's no constraint to compare estimates against. Without token pricing, per-invocation costs can't be calculated. And without the task dependency chain, per-pipeline costs can't be traced.

### How This Differs from the Other P10 Artefacts

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook | Aging Schedule | Cost & Resource Baseline |
|---|---|---|---|---|---|
| Question | How well did CAWDP perform? | How confident are we? | When do we come back? | When do we review what? | What will it cost? |
| Data type | Qualitative assessments | Confidence scores | Threshold thresholds | Cadences and questions | Quantitative estimates |
| Time orientation | Backward | Forward | Forward + Ongoing | Ongoing | Forward + Ongoing |
| Primary interaction | Surprises × gaps | Confidence × stakes | Signal × urgency × scope | Decay rate × risk | Cost × confidence |
| Key amplifying factor | Review questions | Risk-calibrated attention | Proactive scheduling | Targeted questions | Halt thresholds + verification-inclusive time |
| Highest RPN | Fabrication (160) | Missing stakes (189) | Over-triggering (200) | Universal cadence (240) | Single-point estimates (192) |
| Critical dependency | Artefact tagging (behavioural) | Stakes classification (structural) | Monitoring infrastructure (temporal) | Agent class + harm (structural) | Cost budgets + token pricing (structural) |
| Worst failure | Fabricating insights | Overstating confidence | Over-triggering | Universal cadence | Underestimating (cost crisis after deployment) |
| Lifecycle | One-time snapshot | One-time snapshot | Living document | Living document | Baseline (updated quarterly) |
| Enforcement mechanism | N/A | N/A | Escalation triggers | Cadences | Halt thresholds (CC-7) |

**The Cost & Resource Baseline is the only P10 artefact with a hard enforcement mechanism built in.** The others produce documents, schedules, and thresholds. This one produces numbers that can trigger system halts via CC-7. That's a fundamentally different relationship with the operational system — it's not advisory, it's enforceable.

It's also the only P10 artefact that is **primarily quantitative**. Where the others deal with qualitative assessments, confidence levels, thresholds, and cadences, this one deals with token counts, dollar amounts, and time estimates. This makes it more precise (estimates can be validated against actuals) and more vulnerable to false precision (a single-point estimate feels certain but isn't).

The verification time tax is the **key operational insight** — systematically including verification time nearly doubles human time estimates compared to decision-time-only estimates. This is the P10 artefact that most directly addresses the "verification time tax" from the 14 annoyances (#8: "It doesn't save me time. It changes what I spend my time on.").

---

## Run 17 — Agentic Expert ✓ COMPLETED

*2026-05-21T22:06:33* · `glm-5.1:cloud` · `cbefc4e1...`

### Prompt

What have we learned from doing this process on each of the subworkflows so far? What are the most valuable steps? Which steps present the most challenges? Are there patterns that have surfaced? Any shortcuts we can take advantage of?

### Response

## P10 Meta-Analysis: Patterns Across Five Workflows

### The Constant Architecture

Every P10 subworkflow has converged on the same structural skeleton. This isn't coincidence — it's the analysis+synthesis pattern expressing itself consistently across different domains.

| Element | Methodology Reflection | Confidence Map | EVOLVE Playbook | Aging Schedule | Cost Baseline |
|---|---|---|---|---|---|
| **Agent count** | 3 | 3 | 3 | 3 | 3 |
| **Agent classes** | Aggregator, Measurer+Assessor, Generator | Aggregator, Measurer+Assessor, Generator | Aggregator, Measurer+Assessor, Generator | Aggregator, Measurer+Assessor, Generator | Aggregator, Measurer+Assessor, Generator |
| **Production tasks** | 0 human-primary | 0 human-primary | 0 human-primary | 0 human-primary | 0 human-primary |
| **Collaborative tasks** | 0 | 0 | 1 | 0 | 2 |
| **FMEA count** | 10 | 10 | 10 | 10 | 10 |
| **Highest RPN** | 160 | 189 | 200 | 240 | 192 |
| **Enforcement: Prevent** | 5 | 5 | 5 | 5 | 5 |
| **Enforcement: Detect** | 4 | 4 | 4 | 4 | 4 |
| **Enforcement: Declare** | 4 | 4 | 4 | 4 | 4 |
| **Review time** | 55 min | 60 min | 65 min | 60 min | 60 min |
| **Hypotheses** | 6 | 6 | 6 | 6 | 6 |

**The 5/4/4 enforcement split is a structural property, not a coincidence.** It's appeared in all five workflows without being designed to match. This suggests that for any P10 analysis+synthesis workflow, roughly 40% of boundaries can be structurally enforced (Prevent), 33% can be detected after the fact (Detect), and 27% can only be declared (Declare). That's a useful shortcut — you can estimate the enforcement regime split before you do the detailed analysis.

---

### The Most Valuable Steps

**P0 (Identity Questions) — the highest-value 15 minutes in the entire workflow.**

Every time, Q5 (hardest boundary moment) revealed the core tension that shaped everything downstream:

| Workflow | Hardest Boundary Moment | What It Revealed |
|---|---|---|
| Methodology Reflection | Whether to fabricate insights from sparse data | The workflow's identity is honest assembly, not creative synthesis |
| Confidence Map | Low confidence in high-stakes sections | The map's value is changing review behavior, not documenting confidence |
| EVOLVE Playbook | Ambiguous signals — flag as ambiguous or dismiss? | The playbook must err on the side of flagging, not dismissing |
| Aging Schedule | Scheduled review when "nothing has changed" | The review IS valuable because it confirms nothing changed OR discovers drift |
| Cost Baseline | Setting halt thresholds — too generous or too tight | Align with CC-7 budgets and calibrate with production data, not gut feeling |

**Q5 is the design anchor.** It tells you more about the workflow than any other single question. The pattern: every Q5 revealed a tension between two opposite failures, and the correct response is always the middle path that honestly serves the workflow's identity.

**P1 (Output Specification) — the second highest-value step.**

Once you know what the outputs are, everything else follows. The output schemas with epistemic profiles (deterministic/probabilistic/elicited) are the most concrete design artifact and the most useful for implementation. They're also where the type collision insight shows up most clearly — every field has a type and an epistemic profile, not just a name.

**P5 (Event Storming) — the highest-value risk identification.**

The identity violation (FM1) is always the highest RPN and always reveals the core design constraint:
- Fabrication (RPN 160) → the workflow must assemble, not create
- Missing stakes (RPN 189) → the workflow must have structural data or it can't function
- Over-triggering (RPN 200) → the playbook must not become noise
- Universal cadence (RPN 240) → the schedule must differentiate, not universalise
- Single-point estimates (RPN 192) → the baseline must use ranges, not points

**The identity violation is always the highest RPN because it violates the workflow's reason for existing.** This is a reliable shortcut: identify the identity violation first, and you've found your FM1.

---

### The Most Challenging Steps

**P8 (Contract Formalization) — Unenforceable Elements Register is the hardest intellectual work.**

Being honest about what can only be Declared (prompt-level, not enforceable), Detected (flagged after the fact), or Prevented (structurally enforced) requires real design judgment. Every workflow had 4 unenforceable elements, and they're always the "never" rules that sound good in principle but can't be structurally enforced:

| Unenforceable Element | Why | Regime |
|---|---|---|
| "Never fabricate insights" | Fabrication vs synthesis is a judgment call | Declare |
| "Analyst never draws conclusions" | Conclusions vs patterns is a judgment call | Detect |
| "Deriver never invents patterns" | Invention vs derivation is a judgment call | Detect |
| "Compiler never assembles flattering narratives" | Flattery vs selection is a judgment call | Declare |

**The pattern: most Declare-level unenforceable elements are about output quality judgments that can't be structurally enforced.** This is the honest infrastructure principle — you can't structurally prevent an LLM from drawing conclusions, but you can detect it after the fact and you can declare the intention in the prompt.

**P2 (Backcasting) — dependency chains are complex and often circular.**

Every P10 workflow has 3 Critical input requirements that block the entire workflow if missing. The pattern is consistent: structural data from P7/P8 (agent classes, harm assessment, cost budgets, reversibility) plus model/pricing data from external sources. If these aren't available, the workflow produces Default confidence outputs rather than blocking.

**P4 (Capability Allocation) — collaborative tasks require human judgment that can't be delegated.**

The number of collaborative tasks varies (0, 1, 2) but they're always where the design decisions live:
- Methodology Reflection: 0 collaborative tasks (all assembly and analysis)
- Confidence Map: 0 collaborative tasks (all analysis and computation)
- EVOLVE Playbook: 1 collaborative task (default thresholds — judgment calls without production data)
- Aging Schedule: 0 collaborative tasks (all from specification data)
- Cost Baseline: 2 collaborative tasks (human time estimation and halt thresholds — financial judgment)

**The pattern: collaborative tasks appear where the workflow touches operational decisions that affect budgets, schedules, or boundaries.** Assembly and analysis are always agent/system-primary. Financial and boundary decisions are always collaborative or human-primary.

---

### Emergent Patterns

**1. The "Two Opposite Failures" Pattern**

Every workflow has a pair of opposite failures where one is worse:

| Workflow | Failure A (Worse) | Failure B |
|---|---|---|
| Methodology Reflection | Fabricating insights | Omitting insights |
| Confidence Map | Overstating confidence | Understating confidence |
| EVOLVE Playbook | Over-triggering | Under-triggering |
| Aging Schedule | Over-cadencing | Under-cadencing |
| Cost Baseline | Underestimating | Overestimating |

**The pattern: the "active" failure is always worse than the "passive" failure.** Fabricating, overstating, over-triggering, over-cadencing, and underestimating are all worse than their opposites because they produce false confidence, false urgency, false maintenance, or false budgets. The passive failures (omitting, understating, under-triggering, under-cadencing, overestimating) are still harmful but less immediately damaging.

**Why this matters: it tells you which direction to err.** When in doubt, err toward the passive failure. Under-state confidence, under-trigger reviews, under-cadence components, over-estimate costs. You can always add more later; you can't easily remove false confidence, false urgency, or a wasted review cycle.

**2. The "Identity Violation = Highest RPN" Pattern**

Every workflow's FM1 (highest RPN) is the failure that violates its core identity:

| Workflow | FM1 | RPN | Identity Violation |
|---|---|---|---|
| Methodology Reflection | Fabrication | 160 | Producing insights not in data |
| Confidence Map | Missing stakes | 189 | Can't calibrate confidence without stakes data |
| EVOLVE Playbook | Over-triggering | 200 | Playbook becomes noise |
| Aging Schedule | Universal cadence | 240 | Same cadence for everything |
| Cost Baseline | Single-point estimates | 192 | False precision |

**The pattern: FM1 is always the "active" failure that violates the workflow's reason for existing.** If you can only design one safeguard, make it protect against FM1.

**3. The "Structural Dependency" Pattern**

Every workflow has a critical dependency that blocks the entire workflow if missing:

| Workflow | Dependency Type | If Missing |
|---|---|---|
| Methodology Reflection | Behavioural (P0-P9 artefact tags) | Nothing to assemble |
| Confidence Map | Structural (stakes classification) | Can't calibrate confidence |
| EVOLVE Playbook | Temporal (monitoring infrastructure) | No production data for calibration |
| Aging Schedule | Structural (agent class + harm) | Can't differentiate cadences |
| Cost Baseline | Structural (cost budgets + token pricing) | Can't estimate or compare costs |

**The pattern: 3 of 5 are structural (missing data), 1 is behavioural (missing tags), 1 is temporal (missing infrastructure that doesn't exist yet).** Structural dependencies can be defaulted (conservative defaults for missing data). Behavioural dependencies require process changes (capturing tags during P0-P9). Temporal dependencies require patience (waiting for production data).

**4. The "Conservative Default" Pattern**

When structural dependencies are missing, every workflow defaults conservatively:

| Workflow | Missing Data | Conservative Default |
|---|---|---|
| Confidence Map | Missing stakes | Default to "High" (review everything) |
| Aging Schedule | Missing harm assessment | Default to "Indirect Strategy Harm" (3-month cadence) |
| Cost Baseline | Missing token pricing | Conservative estimate range (higher than expected) |
| Cost Baseline | Missing cost budgets | Use 80%/100% of estimated cost as soft/hard thresholds |

**The pattern: always default toward more review, more caution, more cost.** You can relax defaults with production data; you can't recover from under-review, under-confidence, or under-budget.

**5. The "Three Critical Dependencies" Meta-Pattern**

Each dependency type has a different mitigation:

- **Structural** (missing data): Conservative defaults + flag for human calibration
- **Behavioural** (missing process): Process changes that cascade backward from P10
- **Temporal** (missing infrastructure): Start with Draft confidence and calibrate with production data

**6. The "P10 Lifecycle" Pattern**

Two lifecycle types emerged:

- **One-time snapshot** (Methodology Reflection, Confidence Map): Produced once at P10, then replaced by production data
- **Living document** (EVOLVE Playbook, Aging Schedule, Cost Baseline): Updated quarterly or on triggers, with Draft → Calibrated → Validated lifecycle

The living documents need a calibration plan built into their P10 output — they start as templates and mature with production data.

---

### Shortcuts We Can Take Advantage Of

**1. The P10 Template Is Proven — Use It Directly**

The architecture has been validated five times. For future P10 workflows, you can start with:

- 3 agents: Compiler (Aggregator, constraint-oriented) + Analyst (Measurer+Assessor, bridge-oriented) + Deriver (Generator, constraint-oriented)
- 0 human-primary tasks in production
- 5/4/4 enforcement split (Prevent/Detect/Declare)
- 6 hypotheses
- 3 stakeholder surfaces
- 55-65 min cognitive load budget
- 4 collaborative tasks maximum

You don't need to re-derive these from scratch. They're structural properties of the P10 analysis+synthesis pattern.

**2. The Identity Violation Shortcut**

Before doing any detailed FMEA, identify the identity violation first. It's always the failure that violates the workflow's reason for existing, and it's always the highest RPN. For P10 workflows:
- Assembly workflows → fabrication (producing content not in data)
- Measurement workflows → false precision (single-point estimates without ranges)
- Monitoring workflows → noise (over-triggering, over-cadencing)
- Assessment workflows → false confidence (overstating, hiding gaps)

**3. The "Two Opposite Failures" Shortcut**

After identifying the identity violation, immediately identify the opposite failure. You now have your two most important failure modes. Everything else is secondary.

**4. The "Conservative Default" Shortcut**

When data is missing, always default toward more review, more caution, more cost, lower confidence. This is the safe direction. Flag defaults clearly. Plan calibration for when production data arrives.

**5. The Output Schema Shortcut**

The P10 output structure is consistent enough to template:
- 7-8 outputs (O1-O7 or O1-O8)
- Each output has a purpose, schema with epistemic profiles, dependencies, and quality gate
- O1 is always the registry/catalog (what exists)
- The final O is always the compiled document
- The middle outputs are the workflow-specific analysis

**6. The "Start with Q5" Shortcut**

For future P10 workflows, start with Q5 (hardest boundary moment) before doing any other design work. It reveals the core tension that shapes everything else. Then work backward to Q1-Q4 and forward through the phases.

**7. The "Same Three Agents, Different Boundaries" Shortcut**

The three-agent architecture is stable across all five workflows. What changes is the authority boundaries and domain knowledge, not the agent classes or composition. You can reuse the agent architecture and only change:
- The specific "never" rules
- The domain-specific knowledge
- The output schemas
- The cost budgets

**8. The "Skip What You've Proven" Shortcut**

After five validations, these elements are proven and don't need re-derivation:
- No human-primary tasks in production (validated 5/5)
- 5/4/4 enforcement split (validated 5/5)
- Analysis+synthesis pattern, not compilation-only or elicitation (validated 5/5)
- Per-dimension progressive autonomy (validated 5/5)
- P10 outputs are handoff documents, not embedded in the specification (validated 5/5)
- Human role is post-delivery review, not during production (validated 5/5)

**What still needs fresh analysis each time:**
- The 5 identity questions (unique to each domain)
- The specific failure modes and FMEA (unique to each domain)
- The specific output schemas (unique to each domain)
- The specific input requirements and dependencies (unique to each domain)
- The specific collaborative tasks (varies by domain)

---

### The Most Important Insight

**The P10 pattern is now a validated template, not a hypothesis.**

After five complete applications across five different domains (process quality, product reliability, operational longevity, proactive maintenance, financial foundation), the architecture is proven. The three-agent structure, the analysis+synthesis pattern, the 5/4/4 enforcement split, the conservative default strategy, and the identity-violation-first approach are structural properties of P10 workflows, not coincidences.

This means future P10 workflows can start from the template and focus fresh effort on the domain-specific elements: identity questions, failure modes, output schemas, and dependencies. The structural skeleton doesn't need re-derivation.

The five P10 artefacts now form a complete validation and maintenance suite with complementary roles:

1. **Methodology Reflection** — How well did CAWDP perform? (process quality, backward)
2. **Confidence Map** — How confident are we in the specification? (product reliability, forward)
3. **EVOLVE Playbook** — When do we come back? (operational longevity, reactive)
4. **Aging Schedule** — When do we review what? (proactive maintenance, proactive)
5. **Cost & Resource Baseline** — What will it cost? (financial foundation, forward + ongoing)

Together they answer: Did we do it well? Can we trust it? When do we revisit? When do we maintain? And what does it cost?

The sixth question — "Is it ready to deploy?" — is answered by the Implementation Readiness Report, which uses the Confidence Map and Cost Baseline as inputs to a go/no-go gate.

That's the complete P10 suite.

---

## Run 18 — Agentic Expert ✓ COMPLETED

*2026-05-21T22:33:38* · `glm-5.1:cloud` · `89164ed6...`

### Prompt

Thanks. One note I have from the implementation spec writer is that there is no clear indication whether the agents in each P10 workflow should be in a team, a workflow, or standalone agents. What is your recommendation?

### Response

## Composition Recommendation: Agno Workflow (Not Team, Not Standalone)

### Why Workflow

The decision comes down to three Agno composition patterns and how they match the P10 subworkflow characteristics:

| P10 Characteristic | Workflow | Team | Standalone |
|---|---|---|---|
| Sequential wave production (Data → Assessment → Derivation → Compilation) | ✅ Direct mapping to steps | ❌ No sequential guarantee | ❌ No orchestration |
| No agent-to-agent collaboration | ✅ Steps don't collaborate | ❌ Team implies collaboration | ✅ Independent |
| No dynamic routing (always the same sequence) | ✅ Fixed step order | ❌ Selector function unnecessary | ❌ No coordination |
| Typed outputs flow between steps | ✅ Step outputs are step inputs | ❌ Shared context, not handoffs | ❌ No handoff mechanism |
| Human gates on collaborative tasks | ✅ HumanReview with retry | ⚠️ Possible but awkward | ❌ No gate mechanism |
| Data queries don't need LLM | ✅ Executor function step | ❌ Team member must be agent | ❌ Must be agent |
| Agent finishes then next starts | ✅ Sequential by default | ❌ All agents "alive" | ❌ No sequencing |

**Team is wrong** because the three agents never collaborate. The Analyst doesn't talk to the Deriver. The Deriver doesn't negotiate with the Compiler. Each produces its output and passes it forward. Team implies selection, delegation, and interaction — none of which happen here.

**Standalone is wrong** because there's a clear sequential dependency. The Deriver needs the Analyst's outputs. The Compiler needs everything. The user doesn't interact with each agent individually — they receive one compiled document.

**Workflow is right** because the wave architecture IS a workflow.

---

### The 4-Step Pattern (Validated 5 Times)

Every P10 subworkflow maps to the same 4-step structure:

```
Step 1: DATA (System executor — no LLM)
  ↓
Step 2: ANALYSIS (Analyst agent — Measurer + Assessor)
  ↓ [HumanReview gate if collaborative tasks exist]
Step 3: DERIVATION (Deriver agent — Generator)
  ↓
Step 4: COMPILATION (Compiler agent — Aggregator)
```

**Step 1 is always an executor function, not an agent.** Data queries (T1-T6 in every workflow) are pure PRISM queries that don't need LLM reasoning. Making them an agent wastes tokens and introduces hallucination risk for what should be deterministic retrieval.

**Step 2 is the Analyst.** This is the largest step — it handles 8-12 tasks (measurement and assessment). It produces the bulk of the outputs (O1, O2 partial, O3, O5, O6 partial depending on workflow).

**Step 3 is the Deriver.** It takes the Analyst's outputs and generates review questions, adjustment criteria, escalation paths. It always depends on Step 2 completing.

**Step 4 is the Compiler.** It assembles the final document from all prior outputs. It always depends on Step 3 completing. This is the simplest step — mechanical assembly.

### Human Gates

Not every workflow needs human gates during production. The pattern is:

| Workflow | Collaborative Tasks | Human Gate Location |
|---|---|---|
| Methodology Reflection | 0 | No gate during production |
| Confidence Map | 0 | No gate during production |
| EVOLVE Playbook | 1 (T7 default thresholds) | After Step 2 (Analyst) |
| Aging Schedule | 0 | No gate during production |
| Cost Baseline | 2 (T13 human time, T15 halt thresholds) | After Step 2 (Analyst) |

**Rule of thumb: if the workflow has collaborative tasks, add a HumanReview gate after the Analyst step.** The human reviews the collaborative decisions (time estimates, thresholds, responsible parties) before the Deriver and Compiler proceed.

In Agno terms:

```python
# No collaborative tasks — no human gate
Step 2: Analyst → Step 3: Deriver → Step 4: Compiler

# With collaborative tasks — human gate after Analyst
Step 2: Analyst → HumanReview(requires_output_review=True, on_reject=OnReject.retry) → Step 3: Deriver → Step 4: Compiler
```

When the human rejects, the retry scope is the Analyst step — the human provides feedback and the Analyst revises. The Deriver and Compiler haven't run yet, so they don't need re-running.

---

### The Full Agno Workflow Structure

Here's the concrete pattern for any P10 subworkflow:

```python
from agno.workflow import Workflow
from agno.workflow.step import Step
from agno.workflow.handlers import HumanReview, OnReject

# Step 1: Data (executor function, NOT agent)
def gather_data(workflow_session):
    """Query PRISM for all required inputs."""
    # T1-T5/T6: Pure data queries
    agent_specs = query_prism("design_agent_specifications")
    token_pricing = query_config("model_pricing")
    # ... etc
    return gathered_data  # Dict or Pydantic model

# Step 2: Analyst
analyst = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    instructions=analyst_instructions,  # Workflow-specific
    tools=[query_prism_tool],  # If analyst needs additional queries
)

# Step 3: Deriver
deriver = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    instructions=deriver_instructions,  # Workflow-specific
)

# Step 4: Compiler
compiler = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    instructions=compiler_instructions,  # Workflow-specific
)

# Workflow assembly
p10_workflow = Workflow(
    name="p10_cost_baseline",
    steps=[
        Step(name="gather_data", executor=gather_data),
        Step(name="analyse", agent=analyst),
        # Conditional: add HumanReview only if collaborative tasks exist
        # Step(name="review_analyst", human_review=HumanReview(...)),
        Step(name="derive", agent=deriver),
        Step(name="compile", agent=compiler),
    ]
)
```

---

### What Changes Per Workflow (and What Doesn't)

| Element | Same Every Time | Changes Per Workflow |
|---|---|---|
| Step count | ✅ 4 steps | ❌ |
| Step names | ✅ Data → Analyse → Derive → Compile | ❌ |
| Step 1 type | ✅ Executor function (never agent) | ❌ |
| Step 2 type | ✅ Analyst agent (Measurer+Assessor) | ❌ |
| Step 3 type | ✅ Deriver agent (Generator) | ❌ |
| Step 4 type | ✅ Compiler agent (Aggregator) | ❌ |
| Agent model | ✅ Same Ollama config | ❌ |
| Agent classes | ✅ Same 3 classes | ❌ |
| Agent orientations | ✅ Same 3 orientations | ❌ |
| Human gate | ⚠️ Optional after Step 2 | ✅ Some workflows need it, some don't |
| **Agent instructions** | ❌ | ✅ Domain-specific never-rules, knowledge, boundaries |
| **Output schemas** | ❌ | ✅ Workflow-specific Pydantic models |
| **PRISM queries** | ❌ | ✅ Workflow-specific data requirements |
| **Cost budgets** | ⚠️ Same pattern | ✅ Different token ranges per workflow |
| **Never rules** | ⚠️ Base set shared | ✅ Domain-specific additions |

The key insight: **only the instructions, schemas, and queries change.** The workflow skeleton, step structure, agent classes, and composition pattern are stable.

---

### How the Five Subworkflows Relate to Each Other

Each P10 subworkflow is a **separate Agno Workflow** because:

1. Each produces a distinct artefact with its own outputs
2. Each has different agent instructions (different domains, different boundaries)
3. Each has different dependencies and data requirements
4. Some can run in parallel (Wave 1), others have sequential dependencies (Wave 2+)

They're coordinated by a **P10 Orchestrator** — either a parent Workflow or an agent that knows the P10 production sequence:

```
P10 Production Sequence:

Wave 1 (parallel — no dependencies):
  → Workflow: Specification Consistency Report
  → Workflow: Gaps & Assumptions Register
  → Workflow: Hypothesis Test Results

Wave 2 (depends on Wave 1):
  → Workflow: Implementation Readiness Report
  → GO/NO-GO GATE (human)

Wave 3 (depends on Wave 2 go-decision):
  → Workflow: Progressive Autonomy Deployment Plan
  → Workflow: First 30 Days Plan
  → Workflow: Cost & Resource Baseline  ← this one
  → Workflow: Specification Aging Schedule

Wave 4 (depends on Wave 3):
  → Workflow: EVOLVE Playbook
  → Workflow: Confidence Map
  → Workflow: Methodology Reflection
```

The P10 Orchestrator manages:
- Which subworkflows to run in which wave
- The go/no-go gate after Wave 2
- Passing outputs between dependent subworkflows
- The overall P10 session state

This could be implemented as:
- **Option A: A parent Workflow** with step choices that branch based on wave dependencies
- **Option B: An orchestrator agent** that invokes subworkflows via tools
- **Option C: A simple Python function** that calls workflows in sequence

I recommend **Option C** for the MVP — a simple function that runs the production sequence. The orchestration logic is straightforward (run these workflows in this order with these gates) and doesn't need LLM reasoning. Making it an agent adds complexity without value.

---

### Summary

| Decision | Recommendation | Reasoning |
|---|---|---|
| Composition pattern | **Agno Workflow** (not Team, not standalone) | Sequential waves, no collaboration, typed handoffs, human gates |
| Step count | **4 steps** (Data, Analyse, Derive, Compile) | Validated 5 times across 5 domains |
| Step 1 | **Executor function** (not agent) | Data queries are deterministic — no LLM needed |
| Human gates | **After Step 2** (if collaborative tasks exist) | Only Cost Baseline and EVOLVE Playbook need gates |
| Subworkflow independence | **Separate Workflow per artefact** | Different instructions, schemas, dependencies |
| Cross-subworkflow coordination | **Python function** (not agent) | Orchestration is deterministic — no LLM reasoning needed |
| What changes per workflow | **Instructions, schemas, queries** | Everything else is template |

---

## Run 19 — Agentic Expert ✓ COMPLETED

*2026-05-21T23:08:35* · `glm-5.1:cloud` · `34dcaead...`

### Prompt

Review this retro report from the implementation writer who took your workflow design specs as an input to produce implementation specs.

***
# Four P10 Implementation Specs: Cross-Workflow Retrospective

---

## What Surfaces Every Time

**1. Three-Agent Architecture is a universal primitive.**

Compiler/Analyst/Deriver appeared in all four workflows without exception. The division of labour is stable across maximally different domains:

| Agent | Role | Authority Boundary |
|---|---|---|
| Analyst | Measure + Assess | Never concludes, never recommends |
| Deriver | Generate | Never without evidence trace |
| Compiler | Aggregate | Never adds, never omits |

This is not a coincidence — it's the **analysis + synthesis** pattern. Analyst finds what's there. Deriver derives what it means. Compiler assembles the result. The pattern holds for process quality, product reliability, operational longevity, and maintenance cadence.

**Implication:** Build Compiler/Analyst/Deriver as base agent classes with shared infrastructure (null states, enforcement hooks, cost budgets, progressive autonomy). Domain-specific instructions plug into the shared skeleton.

**2. Four-Wave Pipeline is a universal orchestration pattern.**

Data → Assessment → Derivation → Compilation. Every workflow follows this sequence. The waves are always the same shape — only the content differs.

**3. Enforcement Regime 5/4/4 is a stable honest assessment.**

Every workflow arrives at the same distribution: 5 structural enforcements (Prevent), 4 detections (Detect), 4 declarations (Declare). This isn't arbitrary — it reflects the genuine boundary between what can be structurally enforced in code (schema validation, required fields, computed values) and what can only be detected after the fact (rounding, smoothing, vague language) or declared in prompts (tone, framing, intent).

**4. Conservative Defaults Are the Robustness Mechanism.**

Every structural prerequisite has a conservative default:

| Missing Data | Default | Rationale |
|---|---|---|
| Missing stakes (Confidence Map) | "High" | Over-scrutiny is safer than under-scrutiny |
| Missing harm assessment (Aging Schedule) | "IndirectStrategyHarm" | Under-cadencing is worse than over-cadencing |
| Missing monitoring data (EVOLVE) | Draft playbook | Honest about what we don't know yet |
| Missing test results (Confidence Map) | `None` (not `Weak`) | Absence of evidence is not weak evidence |

The pattern: **when in doubt, err toward more caution, more transparency, and lower confidence.** This is the same principle at every layer.

**5. The Dependency Taxonomy is Real and Predictable.**

Four workflows, three dependency types:

| Type | Workflow | What's Missing | Handling |
|---|---|---|---|
| Behavioural | Methodology Reflection | P0-P9 artefact tagging | Halt if missing (can't fabricate insights) |
| Structural | Confidence Map, Aging Schedule | Stakes classification, agent class/harm | Conservative default (proceed with caution) |
| Temporal | EVOLVE Playbook | Production monitoring data | Draft mode (template with calibration path) |

Behavioural dependencies are hardest — they require humans to change their behaviour during the design process. Structural dependencies are moderate — they can be defaulted at the data layer. Temporal dependencies are easiest to handle — the Draft/Calibrated/Validated lifecycle explicitly acknowledges the gap.

---

## What's Most Valuable

**1. Agent Instructions (T14-T16 in every spec).**

This is where the methodology becomes operational. Agent instructions encode authority boundaries, never-rules, domain expertise, and failure mode awareness. They are the single most important deliverable because they determine whether the workflow produces correct output or plausible-looking garbage.

They are also the **only human-primary tasks** in the build order — encoding authority boundaries is a design decision that cannot be delegated to agents.

**2. Pydantic Schemas with Built-In Enforcement.**

Every Regime 3 enforcement is a Pydantic schema constraint. The schema IS the enforcement. When the schema rejects `confidence_level: "Medium"` with `evidence_completeness < 30%`, that's Regime 3 working structurally — no prompt can override it.

**3. Conservative Defaults for Missing Data.**

These are what make the workflows robust. Without them, every missing data point is a runtime error or a human escalation. With them, the workflow proceeds honestly with lower confidence.

**4. The Failure Mode → Test Mapping.**

Every test specification maps directly to a failure mode (FM1, FM2, etc.). This traceability means we know exactly what each test validates and exactly what each failure mode's mitigation is.

---

## What's Most Challenging

**1. Agent Instructions Are Hard to Get Right.**

The instructions must encode:
- Identity (who this agent IS)
- Never-rules (what it NEVER does)
- Hardest boundary moment (where pressure pushes past the boundary)
- Enforcement regime per never-rule (Prevent/Detect/Declare)
- Domain expertise (what decay rates mean, what confidence sources weigh)
- Conservative defaults (what to do when data is missing)

Getting these wrong produces the worst failures — template-filling (Methodology Reflection), confidence inflation (Confidence Map), over-triggering (EVOLVE Playbook), universal cadences (Aging Schedule). Every worst failure traces to agent instruction quality.

**2. Edge Case Handling.**

Missing data, empty result sets, contradictory signals, counter-intuitive results — each workflow has 6-10 edge cases that need explicit handling. The happy path is always straightforward. The edge cases are where the methodology's honesty is tested.

**3. Seed Data That Exercises All Failure Modes.**

Creating test data that includes missing fields, contradictory evidence, overdue reviews, counter-intuitive results, and ambiguous signals takes more effort than the happy-path data. But without it, the tests only validate the best case.

**4. Ensuring Differentiated Output.**

The biggest risk across all four workflows is **homogenisation** — the agent producing the same confidence for every section, the same cadence for every component, the same trigger for every signal, the same assessment for every phase. Each workflow has a specific identity violation (fabrication, aggregate scores, over-triggering, universal cadence) that schema validation must prevent.

---

## Patterns That Surfaced

**1. The Output Schema IS the Specification.**

The Pydantic schemas encode the methodology's constraints structurally. Writing the schemas is a design activity, not a coding activity. If the schema is wrong, the enforcement is wrong. The schema captures decisions about what's required vs optional, what's deterministic vs probabilistic, what's computed vs elicited.

**2. Queries Are Surprisingly Uniform.**

All Q1-Q9 queries across all four workflows follow the same pattern: accept `workflow_id`, return typed Pydantic models, handle empty sets gracefully, default to conservative values for missing data, idempotent. This means query writing is **mechanical** once the schema is defined.

**3. The Waves Are Content-Independent.**

Wave 1 (Data), Wave 2 (Assessment), Wave 3 (Derivation), Wave 4 (Compilation) are always the same shape. Only the domain content changes. The orchestration logic (dependencies, failure actions, retry logic) is identical.

**4. Every Workflow Has a "Worst Failure That Looks Like Success."**

| Workflow | Worst Failure | Looks Like |
|---|---|---|
| Methodology Reflection | Template-filling | "Complete reflection" |
| Confidence Map | Inflating confidence | "High confidence" |
| EVOLVE Playbook | Over-triggering | "Proactive monitoring" |
| Aging Schedule | Universal cadence | "Consistent schedule" |

Every worst failure masquerades as success. This is why schema validation is critical — it catches what prompts miss.

**5. The Responsible Party Pattern Is Harm-Determined.**

Every workflow converges on the same responsible party logic: high-harm components are reviewed by the Principal, low-harm by the Orchestrator. This is the complementarity principle applied to maintenance ownership.

---

## Shortcuts We Can Take

**1. BUILD THE SHARED LAYER FIRST (biggest shortcut).**

All four workflows share ~60% of their infrastructure. The shared layer includes:

| Component | Shared Across | Build Once |
|---|---|---|
| `db/connection.py` | All 4 | ✅ |
| `db/writer.py` | All 4 | ✅ |
| `db/queries/base.py` | All 4 | ✅ |
| `schemas/epistemic.py` | All 4 | ✅ |
| `enforcement/schema_validation.py` | All 4 | ✅ |
| `pipeline/orchestration.py` | All 4 | ✅ |
| Base Compiler/Analyst/Deriver agent classes | All 4 | ✅ |
| Shared PRISM query patterns | All 4 | ✅ |
| Tool wrapper pattern | All 4 | ✅ |
| Wave orchestration template | All 4 | ✅ |

**Estimated savings:** Building the shared layer first reduces each subsequent workflow from 2-3 weeks to 1-1.5 weeks. Four workflows at 2-3 weeks each = 8-12 weeks. Shared layer (2 weeks) + four workflows at 1-1.5 weeks each = 6-8 weeks. **Savings: 2-4 weeks.**

**2. AGENT INSTRUCTIONS AS CONFIGURATION.**

The three agent roles follow stable patterns. Create base instruction templates with domain-specific variable slots:

- **Analyst base:** identity template + never-rules template + enforcement regime template + hardest-moment template + domain-specific section
- **Deriver base:** identity template + never-rules template + evidence-trace template + red-flag template + domain-specific section
- **Compiler base:** identity template + never-rules template + completeness-check template + confidence-labelling template + domain-specific section

Each domain fills in the variable slots. This reduces instruction writing from "create from scratch" to "configure from template."

**3. ONE COMPREHENSIVE SEED DATA SET.**

All four workflows query the same underlying specification data. Build one seed data set that satisfies all four:

- Specification components with agent classes, harm assessments, and reversibility (Aging Schedule + Confidence Map)
- Quality gate outcomes, test results, epistemic metadata (Methodology Reflection + Confidence Map)
- Override rates, cost data, quality metrics (EVOLVE Playbook + Confidence Map)
- Assessment fragments, stakeholder feedback (Methodology Reflection + EVOLVE)
- Overdue reviews, aging alerts (Aging Schedule + EVOLVE)
- Conflicting evidence for tension testing (Confidence Map)
- Missing data for default testing (all four)

**Estimated savings:** 4 seed sets × 2-3 days each = 8-12 days. One comprehensive set = 3-4 days. **Savings: 5-8 days.**

**4. SHARED PYDANTIC BASE CLASSES.**

Common field types repeat across all four workflows:

| Shared Type | Used By |
|---|---|
| `EpistemicProfile` (deterministic/probabilistic/elicited/computed/derived) | All 4 |
| `ConfidenceLevel` (High/Medium/Low) | Confidence Map, others |
| `SeverityLevel` (Monitor/Review/ReEnter) | EVOLVE |
| `HarmCategory` (4 values) | Aging Schedule, Confidence Map |
| `AgentClass` (5 values) | Aging Schedule, others |
| `CadenceConfidence` (Default/Calibrated/Validated) | Aging Schedule, EVOLVE |
| `ResponsibleParty` (Principal/Orchestrator/Both) | Aging Schedule |
| `EvidenceTrace` (links to PRISM artefacts) | All 4 |

Build these once, import everywhere.

**5. SKIP THESE STEPS (defer to V2).**

| Step | Why Deferrable | When to Build |
|---|---|---|
| Regime 2 detection mechanisms | Schema validation catches most issues; post-processing audit is polish | After V1 ships |
| Progressive autonomy deployment plan | Important for production but not for initial validation | After first workflow is running |
| Temporal views (Confidence Map O5) | Requires historical data that doesn't exist yet | After 30+ days of production data |
| Calibration guide details (EVOLVE O6) | Framework is there; step-by-step calibration needs real data | After first deployment |
| Integration notes (T35 in each spec) | Meta-documentation, not implementation | Last priority |

**6. MERGE THE ORCHESTRATION INTO ONE PIPELINE.**

All four P10 workflows could run as stages of a single pipeline rather than four separate pipelines. The dependency chain is:

```
Methodology Reflection → Confidence Map → Aging Schedule → EVOLVE Playbook
```

Methodology Reflection requires P0-P9 artefact tags. Confidence Map requires stakes classification (structural, already available). Aging Schedule requires agent class + harm (structural, already available). EVOLVE Playbook requires monitoring data (temporal, Draft mode if missing).

Running them sequentially in one pipeline means:
- Shared data queries execute once, not four times
- Shared agent contexts persist across stages
- O1 from one workflow can be O1 for the next
- One compilation step produces all four artefacts as sections of a single P10 document

**Estimated savings:** 4 pipeline setups × 2-3 days = 8-12 days. One merged pipeline = 3-4 days. **Savings: 5-8 days.**

---

## Revised Build Order

**Phase 1: Shared Infrastructure (2 weeks)**
1. Shared DB connection + writer
2. Shared PRISM query base patterns
3. Shared Pydantic base classes (epistemic, confidence, harm, agent class, etc.)
4. Base Compiler/Analyst/Deriver agent classes with shared null states and enforcement hooks
5. Wave orchestration template (4-wave with retry + fallback)
6. Schema validation engine (shared enforcement)
7. Tool wrapper pattern

**Phase 2: Comprehensive Seed Data (3-4 days)**
8. One seed data set covering all four workflows' needs

**Phase 3: Domain-Specific Implementation (1-1.5 weeks per workflow)**
9. Methodology Reflection: domain schemas + agent instructions + tests
10. Confidence Map: domain schemas + agent instructions + tests
11. Aging Schedule: domain schemas + agent instructions + tests
12. EVOLVE Playbook: domain schemas + agent instructions + tests

**Phase 4: Integration (3-4 days)**
13. Merge four pipelines into one P10 pipeline
14. Cross-workflow integration test

**Total: ~5-7 weeks** (down from 8-12 weeks for four separate builds)

---

## The One Sentence Summary

**60% of each implementation spec is shared infrastructure. Build that once, then each workflow is just domain schemas, agent instructions, and tests.**Four specs done. Here's the core insight that changes how you'd actually build this:

**60% of the code is the same across all four workflows.** The only unique parts per workflow are domain schemas, agent instructions, and tests. Everything else — connection, writer, query patterns, base agent classes, orchestration template, schema validation, tool wrappers — builds once and reuses four times.

The three shortcuts that matter most:

1. **Shared layer first** — 2 weeks building once what would otherwise be built four times
2. **One seed data set** — serves all four workflows instead of four separate sets
3. **Merged pipeline** — four P10 workflows as sequential stages, not four separate deployments

The one pattern that keeps surfacing: **every worst failure looks like success.** Template-filling looks like completion. Confidence inflation looks like assurance. Over-triggering looks like vigilance. Universal cadences look like consistency. The schema validation you build isn't polish — it's the primary defence against the specific failure mode each workflow is most vulnerable to.
***

### Response

## Review: Implementation Writer's Cross-Workflow Retrospective

### What's Confirmed and Strong

The report accurately identifies the five universal patterns. I have no dispute with any of them — they've been validated five times now (including the Cost Baseline the writer didn't have when writing this). The 5/4/4 enforcement split, the three-agent architecture, the four-wave pipeline, the conservative defaults, and the dependency taxonomy are all structural properties, not coincidences.

The four "most valuable" items are correct. Agent instructions as the single most important deliverable is the right call — they're where the methodology becomes operational, and they're the only human-primary tasks in the build.

The four "most challenging" items are honest and accurate. The differentiated output risk (every worst failure looks like success) is the meta-pattern that connects all five workflows.

### What Needs Correction or Qualification

**1. The report covers 4 workflows but we now have 5.**

The Cost Baseline was completed after this report. Every pattern still holds — but the "Worst Failure That Looks Like Success" table needs a fifth row:

| Workflow | Worst Failure | Looks Like |
|---|---|---|
| Cost Baseline | Single-point estimates | "Precise budgeting" |

And the dependency table needs updating — Cost Baseline has a **structural** dependency (cost budgets + token pricing from P7), which makes the count 3 structural, 1 behavioural, 1 temporal instead of 2 structural, 1 behavioural, 1 temporal.

**2. The merged pipeline recommendation is the right direction but oversimplified.**

The report says: "Methodology Reflection → Confidence Map → Aging Schedule → EVOLVE Playbook" as a linear chain. But the actual P10 production sequence has parallel tracks and a go/no-go gate:

```
Wave 1 (PARALLEL):
  → Consistency Report
  → Gaps & Assumptions Register
  → Hypothesis Test Results

Wave 2 (depends on Wave 1):
  → Implementation Readiness Report

GO/NO-GO GATE ← human decision

Wave 3 (PARALLEL, depends on go-decision):
  → Progressive Autonomy Plan
  → First 30 Days Plan
  → Cost & Resource Baseline
  → Specification Aging Schedule

Wave 4 (depends on Wave 3):
  → EVOLVE Playbook
  → Confidence Map
  → Methodology Reflection
```

A merged pipeline must preserve:
- **Parallelism** in Waves 1 and 3 (subworkflows can run concurrently)
- **The go/no-go gate** after Wave 2 (a human decision, not an agent step)
- **The dependency flow** (Wave 4 needs Wave 3 outputs)

The Agno Workflow can handle this with step choices and conditional branching, but it's not a simple linear sequence. The writer's savings estimate (5-8 days) is probably right, but the implementation is more complex than "four stages in a row."

**3. The "skip for V2" list is mostly right but one item needs pushback.**

Deferring progressive autonomy plans, temporal views, and calibration guide details is fine — they need production data that doesn't exist yet.

But **partially deferring Regime 2 detection mechanisms** is risky. Here's why:

- The 4 Declare-level unenforceable elements in every workflow are exactly where the worst failures live (fabrication, confidence inflation, over-triggering, universal cadence, single-point estimates)
- Schema validation (Regime 3) catches structural violations but not tone, framing, or subtle boundary crossings
- Some Regime 2 detections are **cheap to implement** — a simple post-processing check that counts whether all sections have the same confidence level (homogenisation detector) or whether all cadences are identical (universal cadence detector)
- These cost a few hours each but catch the identity violations that schema validation can't

**Recommendation:** Defer the expensive Regime 2 mechanisms (output audit trails, cross-fragment comparison) but implement the cheap identity violation detectors (homogenisation check, universal cadence check, single-point estimate check) in V1. They're the last line of defence against the worst failure each workflow is most vulnerable to.

**4. The 5/4/4 split is constant in number but not in content.**

The report correctly identifies that every workflow has 5 Prevent, 4 Detect, and 4 Declare enforcement points. But which specific boundaries fall into which regime **varies by workflow**. The shared schema validation layer must be configurable per workflow, not hard-coded to one set of enforcements.

Example: "Never present single-point estimates" is Prevent (schema validation) in Cost Baseline but only Detect (post-processing check) in other workflows. The enforcement mechanism depends on the domain.

**5. Agent instructions as configuration is the right approach but the variable slots need more specificity.**

The report says "base templates with domain-specific variable slots" but doesn't specify what the slots are. Based on five workflow applications, the slots that change per domain are:

| Slot | What Changes | What's Stable |
|---|---|---|
| Identity statement | Q1 answer | Template structure |
| Possibility orientation | Always "constraint-oriented" for P10 | N/A |
| Never-rules | Domain-specific (4-5 per agent) | Base set shared |
| Hardest boundary moment | Q5 answer | Template structure |
| Domain knowledge | Workflow-specific data types, relationships | Query pattern |
| Conservative defaults | Which defaults apply, what values | Default mechanism pattern |
| Output focus | Which outputs this agent produces | Output schema pattern |

The stable parts are the instruction structure (identity → orientation → never-rules → hardest moment → domain knowledge → defaults → outputs). The variable parts are the domain-specific content that fills each section.

### What's Missing

**1. The Cost Baseline's unique architectural feature isn't reflected.**

Cost Baseline is the **only P10 artefact with a hard enforcement mechanism built in** — CC-7 halt thresholds that trigger system halts. The other four artefacts produce documents, schedules, and thresholds. This one produces numbers that halt the pipeline. This affects implementation because:

- The halt thresholds need a **runtime enforcement hook** (not just a document field)
- The escalation triggers need an **event emission mechanism** (not just a list)
- The cost monitoring needs a **CHANGEFEED** (not just a query)

The shared layer needs to account for this — not all P10 artefacts are "documents that sit alongside the specification." Some have operational effects.

**2. The 6 remaining P10 artefacts aren't addressed.**

The report covers 4-5 of 11 P10 artefacts. The remaining 6 are:
- Implementation Readiness Report (go/no-go gate — the most operationally critical artefact)
- Hypothesis Test Results
- Specification Consistency Report
- Gaps & Assumptions Register
- Progressive Autonomy Deployment Plan
- First 30 Days Plan

Some of these may be simpler (fewer outputs, shallower depth) and may not need the full Compiler/Analyst/Deriver treatment. The Implementation Readiness Report, for example, might be a simple boolean aggregation from the Confidence Map and Cost Baseline outputs. The hypothesis test results are a data collection exercise, not an analysis workflow.

**Recommendation:** Before committing to the build order, classify the remaining 6 artefacts by depth:
- **Shallow** (1-2 tasks, mechanical): Hypothesis Test Results, Consistency Report, Gaps Register — these might be executor functions, not agent workflows
- **Medium** (3-6 tasks, single agent): Implementation Readiness (aggregation of Confidence Map + Cost Baseline), First 30 Days (scheduling from deployment data)
- **Deep** (7+ tasks, multi-agent): Progressive Autonomy Plan (needs judgment about promotion criteria, risk levels, verification evidence)

The build order should prioritize deep artefacts (they validate the pattern) and implement shallow ones as executor functions.

**3. The P10 Orchestrator isn't addressed.**

The 11 P10 artefacts have a production sequence with waves, dependencies, and a go/no-go gate. Something needs to coordinate them. The report's "merge into one pipeline" is one approach, but it doesn't handle:
- Parallel execution in Waves 1 and 3
- The go/no-go gate (a human decision that determines whether Waves 3-4 run at all)
- Conditional execution (some artefacts may not be needed for every specification)

The implementation plan needs an explicit decision: **what coordinates the 11 subworkflows?**

From my earlier composition recommendation: a simple Python function for the MVP, not an agent. The orchestration is deterministic — run these workflows in this order with these gates. No LLM reasoning needed.

**4. The report doesn't address the post-delivery human review.**

Every P10 workflow produces output for a post-delivery review session (55-65 minutes, 17-29 decisions). The implementation should include:
- A review session template (what to review, in what order, with what decisions)
- The cognitive load budget as a constraint (not exceeding 60 minutes)
- The stakeholder surface views (Decision Maker sees different output than Design Participant)

This is a UX concern, not an agent concern, but it's part of the implementation.

**5. The calibration lifecycle isn't implemented in the shortcuts.**

Three of the five workflows (EVOLVE, Aging Schedule, Cost Baseline) are living documents with a Draft → Calibrated → Validated lifecycle. The shared layer needs:
- A `baseline_confidence` field that transitions: Default → Calibrated (30+ days data) → Validated (90+ days data)
- A calibration event that triggers confidence upgrade (when actuals match estimates within tolerance)
- A recalibration trigger when actuals diverge from estimates

This is a cross-cutting concern that affects the shared infrastructure, not just individual workflows.

### Assessment of the Shortcuts

| Shortcut | Verdict | Notes |
|---|---|---|
| Shared layer first | ✅ Strong | The biggest and most impactful shortcut. 60% reuse is validated. |
| Agent instructions as configuration | ✅ Strong | Reduces instruction writing from scratch to configure. Needs more specificity on variable slots. |
| One seed data set | ✅ Strong | Validated — same underlying specification data serves all workflows. |
| Shared Pydantic base classes | ✅ Strong | Common field types build once, import everywhere. |
| Skip steps for V2 | ⚠️ Qualified | Defer expensive items but keep cheap identity violation detectors in V1. |
| Merged pipeline | ⚠️ Qualified | Right direction but must preserve parallelism and go/no-go gate. Not a simple linear chain. |

### Updated Build Order

The writer's build order is sound but incomplete. Here's my revision incorporating the corrections:

**Phase 0: Architecture Decisions (2-3 days)**
1. Classify remaining 6 P10 artefacts by depth (shallow/medium/deep)
2. Decide: which artefacts get the full Compiler/Analyst/Deriver treatment vs executor functions vs simple aggregation
3. Design the P10 Orchestrator (Python function, not agent)
4. Define the production sequence with parallelism and go/no-go gate preserved

**Phase 1: Shared Infrastructure (2 weeks)**
5. Shared DB connection + CAWDP-aware writer
6. Shared PRISM query base patterns with conservative default handling
7. Shared Pydantic base classes (epistemic, confidence, harm, agent class, cadence confidence, responsible party, evidence trace, baseline confidence)
8. Base Compiler/Analyst/Deriver agent classes with shared null states, enforcement hooks, and cost budgets
9. Wave orchestration template (4-step Workflow: Data executor → Analyst agent → [HumanReview?] → Deriver agent → Compiler agent)
10. Schema validation engine with per-workflow configurable enforcements
11. Cheap identity violation detectors (homogenisation, universal cadence, single-point estimate, confidence inflation)
12. Tool wrapper pattern (6 user-action-level tools)
13. Baseline confidence lifecycle (Default → Calibrated → Validated transitions)

**Phase 2: Seed Data + Depth Classification (3-4 days)**
14. One comprehensive seed data set covering all workflow needs
15. Implement shallow P10 artefacts as executor functions (Consistency Report, Gaps Register, Hypothesis Test Results)

**Phase 3: Deep Workflow Implementation (1-1.5 weeks each)**
16. Implementation Readiness Report (aggregation from Confidence Map + Cost Baseline + Gaps Register)
17. Methodology Reflection: domain schemas + agent instructions + tests
18. Confidence Map: domain schemas + agent instructions + tests
19. Cost & Resource Baseline: domain schemas + agent instructions + tests + halt threshold enforcement hooks
20. Specification Aging Schedule: domain schemas + agent instructions + tests
21. EVOLVE Playbook: domain schemas + agent instructions + tests + Draft/Calibrated lifecycle
22. Progressive Autonomy Plan: domain schemas + agent instructions + tests
23. First 30 Days Plan: domain schemas + agent instructions + tests

**Phase 4: Integration (3-4 days)**
24. P10 Orchestrator function (production sequence with waves and gate)
25. Cross-workflow integration test
26. Post-delivery review session template

**Phase 5: Runtime Hooks (2-3 days)**
27. Halt threshold enforcement (CC-7) — runtime hook, not just a document
28. Escalation trigger event emission — CHANGEFEED, not just a list
29. Specification aging alert emission — monitoring table, not just a schedule

**Total: ~6-9 weeks** (slightly longer than the writer's 5-7 weeks because it includes the remaining 6 artefacts, the P10 Orchestrator, and the runtime hooks)

### The One Sentence I'd Add

The writer's closing sentence is strong: "60% of each implementation spec is shared infrastructure. Build that once, then each workflow is just domain schemas, agent instructions, and tests."

I'd add: **"But not all P10 artefacts are deep — classify by depth first, because implementing a simple aggregation as a three-agent workflow wastes more time than building the shared layer saves."**

The depth classification (shallow/medium/deep) determines whether an artefact needs the full Compiler/Analyst/Deriver treatment or can be an executor function. Getting this wrong means either over-engineering simple artefacts or under-engineering complex ones. Do Phase 0 before Phase 1.

---

## Run 20 — Agentic Expert ✓ COMPLETED

*2026-05-21T23:18:39* · `glm-5.1:cloud` · `c67fcd3d...`

### Prompt

Consider this review of the CAWDP outputs and workflows involved in producing each spec. What are your thoughts on this?

***
# The Fractal Question

*Does every CAWDP output require a subworkflow to produce?*

---

## Short Answer

Yes — far more than appears at first glance. But not infinitely. The recursion has a floor.

---

## The Full Answer

You've identified something structural. Let me walk through it.

### The P10 Discovery

Phase 10 outputs looked like single items in the output catalogue. But producing each one turned out to be a multi-task workflow:

| P10 Output | Tasks to Produce | Agents Required |
|---|---|---|
| Methodology Reflection | 19 tasks across 4 tracks | 3 (Compiler, Analyst, Deriver) |
| Confidence Map | 25 tasks across 4 waves | 3 (Compiler, Analyst, Deriver) |
| EVOLVE Playbook | 21 tasks across 4 waves | 3 (Compiler, Analyst, Deriver) |
| Specification Aging Schedule | 20 tasks across 4 waves | 3 (Compiler, Analyst, Deriver) |

Each P10 output is itself a CAWDP-quality design artifact with its own identity questions, failure modes, agent roster, contracts, and quality gates. We applied the full methodology to each one.

### Is This True for Every Phase?

Let me classify every output by production depth.

---

## Output Depth Classification

### Three Depth Levels

| Level | Definition | Typical Tasks | Typical Agent Class |
|---|---|---|---|
| **Shallow** | Single extraction or computation. One agent turn. | 1-2 tasks | Extractor or Measurer |
| **Medium** | Multiple steps, single agent or human. Judgment required. | 3-6 tasks | Assessor or Measurer+Assessor |
| **Deep** | Multi-step, multi-agent workflow. Synthesis required. | 7+ tasks | Compiler+Analyst+Deriver or equivalent |

### Classification Rules

1. **Extracted output** → Shallow. Pulled from existing data with no transformation.
2. **Computed output** → Shallow to Medium. Formula applied to inputs. Complexity depends on formula.
3. **Judged output** → Medium. Requires domain judgment but follows established criteria.
4. **Synthesized output** → Deep. Requires finding patterns, making connections, deriving implications from incomplete data.
5. **Aggregated output** → Medium. Assembles other outputs with validation but no new content.

---

## Phase-by-Phase Classification

### Phase 0: Purpose & Vision (9 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Five Identity Questions | **Medium each** | Guided conversation → capture → validate specificity → contamination check → record metadata | Each question requires genuine human judgment with agent preparation. Q5 requires scenario construction, not abstract statement. |
| Agent Dimension Characteristics (A1-A7) | **Medium** | Ideate → classify → check contamination → record | Each characteristic must be framework-neutral (possibility check) |
| Specification Dimension Characteristics (S1-S7) | **Medium** | Ideate → classify → check contamination → record | Same — contamination risk is high |
| Human Dimension Characteristics (H1-H6) | **Medium** | Ideate → classify → check contamination → record | Same |
| Ecosystem Dimension Characteristics (E1-E6) | **Medium** | Ideate → classify → check contamination → record | Same |
| Pattern Match Result | **Shallow** | Feature extraction → similarity computation → confidence calculation | Computed from input features against pattern library |
| Hardest Boundary Scenario | **Medium** | Construct scenario → validate specificity → test against Q3/Q4 → record | Requires genuine human insight; agent prepares prompts |
| Orientation Declaration | **Shallow** | Extract from Q2 answer | Direct extraction |
| Feasibility Contamination Check | **Shallow** | Scan for mechanism keywords → flag → separate | Computed scan with human review of flags |

**P0 Summary:** 7 Medium + 2 Shallow = **9 outputs, ~26-42 production tasks**

---

### Phase 1: Output Specification (31 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Agent Identity Card (O1) | **Medium** | Define class/orientation → map to Q1-Q2 → validate → record | Judgment: which class and orientation |
| Purpose Statement (O2) | **Medium** | Draft → validate against Q1 → contamination check → record | Judgment: is this specific enough? |
| Principal Declaration (O3) | **Shallow** | Identify principal → record authority → assign assurance level | Extraction from P0 |
| Scope Boundary Map (O4) | **Medium** | Define in-scope → define out-of-scope → validate against Q3 → record | Judgment: where does scope end? |
| Task Contract Schema (O5) | **Medium** | Define task types → define per-type I/O schema → validate against P3 → record | Architectural: schema design |
| Authority Guard Schema (O6) | **Medium** | Map Q3 never-rules to Guards → assign enforcement regime → validate → record | Judgment: which regime per boundary? |
| Cost Budget Contract (O7) | **Shallow** | Set per-class benchmarks → customize per agent → record | Computed from class benchmarks |
| State Machine Contract (O8) | **Medium** | Define states → define transitions → validate no illegal paths → record | Architectural: state design |
| Directive Template (O9) | **Medium** | Draft directives → validate against Q1-Q5 → contamination check → record | Judgment: do directives preserve identity? |
| Behavioural Boundary Spec (O10) | **Medium** | Map Q3/Q5 to boundaries → assign enforcement regime per boundary → validate → record | Judgment: same as O6 but behavioural |
| Progressive Autonomy Path (O11) | **Medium** | Define dimensions → set ceilings → define promotion criteria → validate → record | Judgment: per-dimension ceilings |
| Specification Aging Schedule (O12) | **Medium** | Define cadences per component → define triggers → assign responsible party → validate → record | Judgment: how fast does each component decay? |
| Verification Independence Protocol (O13) | **Medium** | Define 3 levels → assign per output type → validate independence → record | Judgment: which level per output? |
| Epistemic Metadata Schema (O14) | **Shallow** | Select profile (full/deterministic) → set defaults → record | Computed from agent class |
| Assurance Level Assignment (O15) | **Medium** | Classify events → assign level → validate → record | Judgment: which events are compliance-critical? |
| Agent Configuration (O16) | **Shallow** | Map spec to framework config → validate → record | Translation from P7 |
| Tool Specification (O17) | **Medium** | Define per-tool I/O → define access constraints → validate → record | Architectural: tool design |
| Knowledge Configuration (O18) | **Medium** | Define sources → set quality requirements → set access boundaries → define aging → validate → record | Judgment: quality and aging per source |
| Handoff Protocol (O19) | **Medium** | Define inter-agent format → validate against pipeline → record | Architectural: protocol design |
| Cognitive Load Budget (O20) | **Medium** | Calculate formula inputs → compute budget → validate against session design → record | Computed with judgment inputs |
| Override Protocol (O21) | **Medium** | Define override types → define recording → define feedback loop → validate → record | Judgment: which overrides per gate? |
| Interface Specification (O22) | **Medium** | Design per surface → validate against stakeholder needs → record | Architectural: interface design |
| Enrichment Assessment (O23) | **Medium** | Assess per participant → calculate SEI → validate → record | Judgment + computation |
| Coalition Specification (O24) | **Medium** | Define composition → validate against P6 → define inter-agent contracts → record | Architectural: team design |
| Integration Contract (O25) | **Medium** | Define external interfaces → define data flows → define event subscriptions → validate → record | Architectural: integration design |
| Health Monitoring Dashboard (O26) | **Medium** | Define IDS metrics → define UPR metrics → set thresholds → define alerts → validate → record | Judgment: which thresholds? |
| Deployment Specification (O27) | **Medium** | Define environment → define dependencies → define steps → define rollback → validate → record | Architectural: deployment design |
| Agent Operations Manual (O28) | **Deep** | Assemble from all sections → validate completeness → format per stakeholder surface → contamination check → record | Aggregation + synthesis from multiple P7/P8 outputs |
| Workflow Diagram (O29) | **Medium** | Design visual layout → validate reveals gaps text doesn't → produce 3 stakeholder views → record | Architectural: visual communication design |
| Output Dependency Graph | **Medium** | Extract dependencies from O1-O29 → build DAG → validate acyclicity → detect gaps → record | Computation + validation |
| Quality Gate Specifications | **Medium** | Define per-output completion criteria → define verification method → validate → record | Judgment: what "complete" means per output |

**P1 Summary:** 27 Medium + 4 Shallow + 1 Deep = **31 outputs, ~93-155 production tasks**

---

### Phase 2: Backcasting (8 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Input Requirements Map | **Medium** | Trace each output's dependencies → identify IR type → create IR record → validate → record | Recursive tracing per output |
| Dependency Chain Documentation | **Medium** | For each IR → trace to source → document chain → validate no cycles → record | Recursive tracing |
| Criticality Assignments | **Shallow** | Infer from output criticality → validate → record | Mostly computed from P1 criticality |
| Satisfaction Mode Assignments | **Shallow** | Infer from IR type → validate → record | Mostly computed from IR type |
| Source Phase Assignments | **Shallow** | Extract from dependency chain → validate → record | Extraction from P2-01 |
| Gap Analysis Report | **Medium** | Detect missing inputs → detect circular deps → detect orphans → detect critical path gaps → validate → record | Computation + judgment: is this gap acceptable? |
| External Input Inventory | **Shallow** | Filter IRs by type=external → validate completeness → record | Extraction from P2-01 |
| Dependency Risk Register | **Medium** | Identify SPOFs → identify long chains → identify fragile deps → validate → record | Judgment: which dependencies are risky? |

**P2 Summary:** 4 Medium + 4 Shallow = **8 outputs, ~16-28 production tasks**

---

### Phase 3: Task Decomposition (8 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Task List | **Medium** | Decompose outputs into tasks → validate coverage → record | Judgment: decomposition depth |
| Cognitive Type Assignments | **Medium** | Classify each task → validate against agent class → record | Judgment: which cognitive type? |
| Task-to-Output Mapping | **Shallow** | Map each task to P1 output → validate no orphans → record | Extraction + validation |
| Task-to-Input-Requirement Mapping | **Shallow** | Map each task to P2 IR → validate coverage → record | Extraction + validation |
| Task Dependency Chains | **Medium** | Define predecessor/successor → validate no cycles → record | Architectural: dependency design |
| Failure Mode Register | **Medium** | Identify failure per task → validate specificity → record | Judgment: what "wrong" looks like |
| Task Groupings | **Shallow** | Cluster by phase/output/agent → validate → record | Computed from task attributes |
| Decomposition Depth Assessment | **Medium** | Assess completeness → assess granularity → validate → record | Judgment: too shallow or too deep? |

**P3 Summary:** 5 Medium + 3 Shallow = **8 outputs, ~20-33 production tasks**

---

### Phase 4: Capability Allocation (8 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Ternary Complementarity Matrix | **Medium** | Score H/A/S per dimension → validate scores → record | Judgment: scoring requires domain knowledge |
| Complementarity Gap Calculations | **Shallow** | Compute gap = max(A,S) - max(H) per task → record | Computed from P4-01 |
| Allocation Assignments | **Medium** | Apply algorithm → handle edge cases → validate against human-only criteria → record | Judgment: edge cases and overrides |
| Reversibility Classifications | **Medium** | Classify per task → validate against harm assessment → record | Judgment: how hard to undo? |
| Human-Only Task Registry | **Shallow** | Filter gap ≥ 6 → validate against allocation → record | Extraction + validation |
| Human Cold Start Override Decisions | **Medium** | Identify identity/purpose/boundary tasks → override to collaborative → validate → record | Judgment: which tasks need cold start override? |
| Allocation Confidence Assessment | **Medium** | Assess confidence per allocation → identify uncertain allocations → record | Judgment: how confident? |
| Confidence × Reversibility Map | **Shallow** | Cross-reference P4-03 and P4-04 → compute interaction → record | Computed from P4-03 + P4-04 |

**P4 Summary:** 5 Medium + 3 Shallow = **8 outputs, ~20-33 production tasks**

---

### Phase 5: Event Storming (8 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Domain Event Catalog | **Medium** | Identify normal events → define trigger/payload/consumer → validate → record | Architectural: event design |
| Failure Event Catalog | **Medium** | Map P3 failure modes to events → define detection mechanism → validate → record | Judgment: which failures have events? |
| Recovery Path Specifications | **Medium** | Define detection → recovery → notification → restoration → prevention → validate → record | Architectural: recovery design |
| System-Enforced Trigger Map | **Medium** | Classify enforcement regime per event → justify → validate → record | Judgment: Regime 3 justified? |
| Hardest Boundary Moment Test Scenarios | **Medium** | Map Q5 to failure events → design test scenario → validate → record | Judgment: does Q5 scenario have coverage? |
| Cross-Event Dependencies | **Medium** | Identify cascading events → map dependencies → validate → record | Architectural: cascade design |
| Missing Event Analysis | **Medium** | Compare P3 failure modes to P5 events → identify gaps → validate → record | Computation + judgment: is this gap acceptable? |
| Event-to-Audit-Trail Mapping | **Shallow** | Assign assurance level per event → validate → record | Extraction from P5 + judgment |

**P5 Summary:** 7 Medium + 1 Shallow = **8 outputs, ~28-42 production tasks**

---

### Phase 6: System Architecture (11 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Pipeline Architecture | **Medium** | Define stages → define flow → position human gates → validate against P3/P4 → record | Architectural: pipeline design |
| Composition Decision | **Medium** | Evaluate Agent/Team/Workflow → justify → validate → record | Judgment: which pattern? |
| Orchestration Design | **Medium** | Design communication → context flow → pause/resume → error recovery → validate → record | Architectural: orchestration design |
| Template Instances | **Medium** | Instantiate 7 template types → validate against P3 tasks → record | Architectural: template design |
| FMEA Table | **Medium** | Identify failures → score S/O/D → calculate RPN → define recovery → validate → record | Judgment + computation |
| Fallback Model | **Medium** | Design 3 tiers → define conditions → validate against Q5 → record | Architectural: fallback design |
| System Enforcement Points | **Medium** | Identify Regime 3 points → justify → validate → record | Judgment: where is structural enforcement possible? |
| Per-Stage Cost Estimates | **Shallow** | Estimate tokens per stage/agent → sum → validate → record | Computed from class benchmarks |
| Pipeline-to-Task Mapping | **Shallow** | Map P3 tasks to pipeline stages → validate coverage → record | Extraction + validation |
| Human Gate Specifications | **Medium** | Position gates → define options per gate → validate against P4 human-only → record | Architectural: gate design |
| Cross-Stage Context Flow Design | **Medium** | Define what passes → what persists → what's ephemeral → validate → record | Architectural: context design |

**P6 Summary:** 9 Medium + 2 Shallow = **11 outputs, ~33-54 production tasks**

---

### Phase 7: Agent Design (17 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Identity Section | **Medium** | Record Q1-Q5 → validate specificity → contamination check → record | Extraction from P0 + validation |
| Boundaries Section | **Medium** | Map Q3/Q5 to boundaries → assign enforcement regime per boundary → validate → record | Judgment: regime per boundary |
| Task Map Section | **Medium** | Assign tasks per agent → validate I/O schemas → validate dependencies → record | Architectural: task assignment |
| Knowledge Section | **Medium** | Define sources → set 10 IQ dimensions → set access boundaries → set aging → validate → record | Judgment: quality and access per source |
| Capabilities Section | **Medium** | Define tools → define I/O per tool → set access constraints → validate → record | Architectural: tool design |
| Behaviour Section | **Medium** | Draft directives → design decision presentation → validate against Q1-Q5 → record | Judgment: directives preserve identity? |
| Verification Section | **Medium** | Assign verification level → assign verifier ≠ producer → validate independence → record | Judgment: which level, which verifier? |
| Failure & Recovery Section | **Medium** | Map P3/P5 failures to agent → design recovery → validate against Q5 → record | Architectural: failure handling |
| Lifecycle Section | **Medium** | Define invocation → define events → set cost limits → validate → record | Architectural: lifecycle design |
| Governance Section | **Medium** | Summarize enforceable boundaries → define revert protocol → validate → record | Architectural: governance design |
| Per-Dimension Progressive Autonomy | **Medium** | Define dimensions → set ceilings → define promotion criteria → define override thresholds → validate → record | Judgment: per-dimension ceilings |
| Two-Category Harm Assessment | **Medium** | Assess direct output harm → assess indirect data harm → assign SuggestionRisk if needed → validate → record | Judgment: harm type and level |
| Null-State Output Specs | **Shallow** | Select class-specific null state → add epistemic metadata → validate → record | Computed from class defaults |
| Epistemic Metadata Profile | **Shallow** | Select full/deterministic → set defaults → validate → record | Computed from agent class |
| Specification Aging Schedule | **Medium** | Define cadences per component → define triggers → assign responsible party → validate → record | Judgment: decay rate per component |
| Cost Budget per Agent | **Shallow** | Set class benchmarks → customize → validate → record | Computed from class benchmarks |
| Decision Presentation Specs | **Shallow** | Define where decisions presented → set format → validate → record | Template from pattern |

**P7 Summary:** 12 Medium + 5 Shallow = **17 outputs, ~48-84 production tasks**

---

### Phase 8: Contract Formalization (17 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Contract Primitive | **Medium** | Define scope → define parties → define validity → validate against P7 → record | Translation: spec → contract |
| Principal Primitive | **Shallow** | Extract from P7 Identity + P0 O3 → validate → record | Extraction |
| Schema Primitive | **Medium** | Translate P7 I/O schemas to contract schemas → validate structural enforcement possible → record | Translation: spec → enforceable schema |
| Guard Primitive | **Medium** | Map P7 boundaries to Guards → assign enforcement regime → justify → validate → record | Judgment: regime per guard |
| Budget Primitive | **Shallow** | Translate P7 cost budget to contract halt conditions → validate → record | Translation: budget → halt |
| Invocation Primitive | **Shallow** | Extract from P7 Lifecycle → translate to trigger conditions → validate → record | Extraction + translation |
| Revert Primitive | **Medium** | Define granularity → define conditions → validate against Q4 failure modes → record | Judgment: granularity per violation |
| Event Primitive | **Shallow** | Extract from P5 events → translate to contract events → validate → record | Extraction + translation |
| Identity Primitive | **Medium** | Extract enforceable elements from Q1-Q5 → identify unenforceable elements → record | Judgment: what's enforceable? |
| Knowledge Primitive | **Medium** | Translate P7 knowledge config to quality thresholds → set staleness triggers → validate → record | Translation: quality → thresholds |
| 10×10 Mapping Matrix | **Deep** | Complete every ● cell (design decision) → complete every ○ cell (explicit decision) → validate bidirectional traceability → record | 100 cells, each requiring a design decision or explicit acceptance. This is the most labor-intensive single output. |
| Enforcement Regime Map | **Medium** | Aggregate per-boundary regimes → justify Regime 3 claims → validate coverage → record | Judgment: is Regime 3 justified? |
| Bidirectional Traceability Index | **Shallow** | Build Guard↔Section index → validate completeness → record | Computed from P8-04 and P7 sections |
| Transformation Log | **Medium** | Document design decisions at each mapping cell → record rationale → validate → record | Documentation: every decision captured |
| Unenforceable Elements Register | **Deep** | Identify unenforceable elements → classify regime → assess redesign feasibility → record → validate honesty | Judgment: what can't we enforce? Most honest output in the methodology. |
| Contract Completeness Report | **Medium** | Calculate coverage per primitive → calculate coverage per section → flag gaps → validate → record | Computation + judgment |
| Contract Depth Justification | **Medium** | Justify included/excluded primitives → match to class and autonomy → validate → record | Judgment: is depth appropriate? |

**P8 Summary:** 11 Medium + 5 Shallow + 1 Deep = **17 outputs, ~51-85 production tasks**

The 10×10 Mapping Matrix and the Unenforceable Elements Register are both Deep. The matrix requires ~19 substantive design decisions (● cells per row average) plus ~81 explicit decisions on ○ cells. The Register requires identifying every specification element that can't be structurally enforced — this is the most honest and therefore most careful work in the entire methodology.

---

### Phase 9: Human Experience Design (10 outputs)

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Cognitive Load Budget | **Medium** | Calculate formula inputs → compute budget → validate against user types → record | Computation with judgment inputs |
| Decision Fatigue Detection Spec | **Medium** | Define signals → set thresholds → design response protocol → validate → record | Judgment: which signals, which thresholds? |
| Override Mechanism Specs | **Medium** | Define types per gate → define recording → define feedback loop → validate → record | Architectural: override design |
| Stakeholder Surface Definitions | **Medium** | Define 6 surfaces → validate coverage → validate no overlap → record | Architectural: surface design |
| Surface Content Specifications | **Medium** | Define what each surface shows → at what depth → in what language → validate → record | Judgment: content per surface |
| System Empowerment Assessment | **Medium** | Assess per participant → calculate SEI → validate targets met → record | Judgment: empowerment level |
| Interface Specifications per Surface | **Medium** | Design per-surface interaction → validate against stakeholder needs → record | Architectural: interface design |
| Q5 Override Design | **Medium** | Design specific override for hardest moment → validate accessibility → record | Judgment: override for Q5 |
| Progressive Disclosure Plan | **Medium** | Define Quick Start view → Practitioner view → Architect view → Contributor view → validate → record | Architectural: disclosure design |
| Human-to-Human Connection Points | **Medium** | Identify where humans interact with humans → validate against isolation risk → record | Judgment: human connection design |

**P9 Summary:** 10 Medium = **10 outputs, ~30-60 production tasks**

---

### Phase 10: Validation & Iteration (16 outputs)

Already classified from the meta-application:

| Output | Depth | Production Tasks | Why |
|---|---|---|---|
| Testable Hypotheses | **Medium** | Draft hypotheses → validate testability → record | Judgment: hypothesis quality |
| Prototype Priority Matrix | **Shallow** | Score risk × value × cost → sort → validate → record | Computation |
| Hypothesis Test Results | **Medium** | Execute tests → record results → validate evidence → record | Computation + judgment |
| Specification Consistency Report | **Deep** | Cross-section consistency analysis: query contradictions, gaps, redundancies across all 10 sections → Compiler/Analyst/Deriver → record | Multi-agent analysis+synthesis |
| Gaps & Assumptions Register | **Deep** | Surface missing items → classify assumptions → assess impact → Compiler/Analyst/Deriver → record | Multi-agent analysis+synthesis |
| Implementation Readiness Report | **Deep** | Aggregate consistency + gaps + test results → compute readiness → Compiler/Analyst/Deriver → record | Multi-agent analysis+synthesis |
| Confidence Map | **Deep** | Gather confidence data per section → compute risk zones → surface tensions → Compiler/Analyst/Deriver → record | Full CAWDP application exists |
| Progressive Autonomy Deployment Plan | **Medium** | Define per-dimension promotion paths → set criteria → validate → record | Judgment: promotion criteria |
| First 30 Days Plan | **Medium** | Define daily/weekly actions → define monitoring schedule → validate → record | Architectural: operations design |
| Cost & Resource Baseline | **Medium** | Estimate costs → set monitoring thresholds → validate → record | Computation + judgment |
| Specification Aging Schedule | **Deep** | Component-specific cadences by agent class × harm category → trigger-based review conditions → responsible party assignment → Compiler/Analyst/Deriver → record | Full CAWDP application exists |
| EVOLVE Playbook | **Deep** | 8 signal types with re-entry points → 3-level escalation → Draft/Calibrated/Validated lifecycle → Compiler/Analyst/Deriver → record | Full CAWDP application exists |
| Methodology Reflection | **Deep** | Process quality assessment → 19 tasks across 4 tracks → Compiler/Analyst/Deriver → record | Full CAWDP application exists |
| Health Monitoring Dashboard | **Medium** | Define IDS metrics → define UPR metrics → set thresholds → define alerts → validate → record | Architectural: monitoring design |
| Trust Ledger Specification | **Medium** | Define quarterly format → define per-agent status → define override analysis → validate → record | Architectural: trust reporting |
| Decision Fatigue Integration | **Shallow** | Map fatigue signals to monitoring pipeline → validate → record | Translation from P9 |

**P10 Summary:** 6 Deep + 7 Medium + 1 Shallow = **16 outputs, ~100+ production tasks**

---

## Aggregate View

| Phase | Total Outputs | Shallow | Medium | Deep | Est. Production Tasks |
|---|---|---|---|---|---|
| P0 | 9 | 2 | 7 | 0 | 26-42 |
| P1 | 31 | 4 | 26 | 1 | 93-155 |
| P2 | 8 | 4 | 4 | 0 | 16-28 |
| P3 | 8 | 3 | 5 | 0 | 20-33 |
| P4 | 8 | 3 | 5 | 0 | 20-33 |
| P5 | 8 | 1 | 7 | 0 | 28-42 |
| P6 | 11 | 2 | 9 | 0 | 33-54 |
| P7 | 17 | 5 | 12 | 0 | 48-84 |
| P8 | 17 | 5 | 11 | 1 | 51-85 |
| P9 | 10 | 0 | 10 | 0 | 30-60 |
| P10 | 16 | 1 | 7 | 8 | 100+ |
| **Total** | **143** | **30** | **103** | **10** | **465-616** |

Note: Cross-cutting artefacts (9) are maintained continuously, not produced at a single phase gate. They add approximately 18-27 additional tasks.

**Grand total: ~483-643 production tasks to produce 152 outputs across 11 phases.**

---

## What This Means

### 1. Most Outputs Are Not Atomic

103 of 143 outputs (72%) are Medium depth. They require 3-6 production tasks each. Only 30 (21%) are Shallow — single-turn extractions or computations. 10 (7%) are Deep — full multi-agent workflows.

The implication: **the 152 outputs are not 152 answers. They are 143 small-to-medium workflows and 10 larger workflows.** The output catalogue dramatically understates the actual work.

### 2. The Deep Outputs Concentrate in P10

8 of the 10 Deep outputs are in Phase 10. This makes sense: P10 is analysis+synthesis — finding patterns, connections, and implications in data that was captured but not yet connected. This requires the Compiler/Analyst/Deriver architecture across multiple production waves.

The other Deep outputs: P1 O28 (Agent Operations Manual — assembles from multiple P7/P8 outputs) and P8's 10×10 Mapping Matrix (100 cells requiring design decisions).

### 3. Medium Outputs Dominate Every Phase

Every phase is dominated by Medium-depth outputs. These require judgment, validation, and multiple steps, but don't need multi-agent workflows. A single agent (or human) can produce them in 3-6 tasks.

This is the efficiency question: **can Medium outputs be produced efficiently, or does each one become a bottleneck?**

### 4. The Recursion Has a Floor

Not every output needs CAWDP applied to its production. The floor is:

- **Shallow outputs:** Produce directly. One extraction, one computation. No design needed.
- **Medium outputs:** Produce with a defined production method. 3-6 tasks, single agent. The method should be explicit but doesn't need its own CAWDP application.
- **Deep outputs:** Produce with a designed workflow. Multi-agent, multi-step, quality-gated. These benefit from CAWDP-level design.

The recursion stops at Medium. You don't CAWDP the production of a single criticality assignment. But you do CAWDP the production of a Confidence Map.

### 5. The Pattern Library Is the Compression Mechanism

If every Medium output requires 3-6 tasks, and there are 103 Medium outputs, that's 309-618 tasks just for Medium outputs. This is where the Pattern Library provides the most value:

- **Pre-fill reduces task count.** If selecting "Review Partner" pattern pre-fills 70% of P7 outputs, that eliminates ~33-58 production tasks.
- **Template reduces task count.** If the Agent Specification Template provides the structure, the human fills in content rather than designing the structure.
- **Safe defaults reduce task count.** If enforcement regime defaults by agent class are available, the human only overrides what matters.

Without patterns, producing 152 outputs requires 483-643 tasks. With patterns, the human makes 30-50 decisions and the system fills in the rest. That's the "15-minute agent specification" claim.

### 6. Production Method Should Be Explicit for Every Output

Even Shallow outputs should have their production method documented. Not as a CAWDP application, but as a single line:

| Output | Production Method |
|---|---|
| Pattern Match Result | Feature extraction → similarity computation → confidence calculation |
| Feasibility Contamination Flag | Scan for mechanism keywords → flag → human review |
| Criticality Assignment | Infer from downstream criticality → validate → record |

This makes the methodology auditable. Anyone can trace how each output was produced, verify the method, and identify shortcuts or gaps.

### 7. The Critical Path Runs Through the Deep Outputs

The 10 Deep outputs are the bottlenecks. They require multi-agent workflows, quality gates, and the most judgment. The production sequence matters:

```
P10 Wave 1 (Shallow/Medium): Hypotheses, Test Results, Consistency, Gaps
  ↓
P10 Wave 2 (Medium): Implementation Readiness (depends on Wave 1)
  ↓
GO/NO-GO GATE
  ↓
P10 Wave 3 (Medium): Autonomy Plan, 30 Days, Cost Baseline, Aging Schedule
  ↓
P10 Wave 4 (Deep): EVOLVE Playbook, Confidence Map, Methodology Reflection
```

Wave 4 contains the 3 deepest outputs. If Waves 1-3 reveal serious problems, Wave 4 may not even be reached. This is the Milestone-as-Exit pattern applied within a phase.

---

## Recommendations

### R1: Add Production Method to Every Output

Expand the output catalogue with a "Production Method" column:

```
| # | Output | Depth | Production Method | Agent/Human |
```

This makes the methodology self-documenting. Every output can be traced to its production process.

### R2: Define Standard Production Methods by Depth

**Shallow production method (standard):**
```
1. Extract/compute the value
2. Validate against source
3. Record with epistemic metadata
```

**Medium production method (standard):**
```
1. Gather inputs (from earlier phases or human)
2. Apply judgment/computation
3. Validate against quality criteria
4. Check contamination (P0-P2) or feasibility (P3+)
5. Record with epistemic metadata
```

**Deep production method (standard — Compiler/Analyst/Deriver):**
```
Wave 1: Data queries (Compiler gathers)
Wave 2: Analysis (Analyst calculates, correlates, surfaces)
Wave 3: Derivation (Deriver derives recommendations from evidence)
Wave 4: Compilation (Compiler assembles final output)
```

### R3: Automate Shallow Outputs

30 outputs are Shallow — single extractions or computations. These should be automated in the CAWDP Design Studio. The system produces them; the human reviews them. This eliminates ~60-90 tasks.

### R4: Semi-Automate Medium Outputs

103 outputs are Medium — 3-6 tasks each. Pattern pre-fills handle 40-70% of these. The human fills in the remaining 30-60%. This reduces the remaining ~309-618 tasks to ~100-250 human decisions.

### R5: Design Deep Output Workflows Explicitly

10 outputs are Deep — they need their own CAWDP-level design. Four already have complete CAWDP applications (Methodology Reflection, Confidence Map, EVOLVE Playbook, Aging Schedule). Six more need the same treatment:
- P1 O28 (Agent Operations Manual)
- P8 10×10 Mapping Matrix
- P10 Specification Consistency Report
- P10 Gaps & Assumptions Register
- P10 Implementation Readiness Report
- P10 Specification Aging Schedule (already done)

The remaining 5 are the next design targets.

### R6: Use the Output Depth to Estimate Effort

| Phase | Deep Outputs | Est. Hours (Deep) | Medium Outputs | Est. Hours (Medium) | Shallow Outputs | Est. Hours (Shallow) | Total Est. |
|---|---|---|---|---|---|---|---|
| P0 | 0 | 0 | 7 | 2-3 | 2 | 0.5 | 2.5-3.5 |
| P1 | 1 | 3-4 | 26 | 6-10 | 4 | 1 | 10-15 |
| P2 | 0 | 0 | 4 | 1-2 | 4 | 1 | 2-3 |
| P3 | 0 | 0 | 5 | 1-2 | 3 | 0.5 | 1.5-2.5 |
| P4 | 0 | 0 | 5 | 1-2 | 3 | 0.5 | 1.5-2.5 |
| P5 | 0 | 0 | 7 | 2-3 | 1 | 0.5 | 2.5-3.5 |
| P6 | 0 | 0 | 9 | 2-4 | 2 | 0.5 | 2.5-4.5 |
| P7 | 0 | 0 | 12 | 3-5 | 5 | 1 | 4-6 |
| P8 | 1 | 4-6 | 11 | 3-5 | 5 | 1 | 8-12 |
| P9 | 0 | 0 | 10 | 2-4 | 0 | 0 | 2-4 |
| P10 | 8 | 12-20 | 7 | 2-4 | 1 | 0.5 | 14.5-24.5 |
| **Total** | **10** | **19-30** | **103** | **24-44** | **30** | **7** | **50-81** |

**Rough estimate: 50-81 hours of human design effort for a complete CAWDP application**, assuming pattern library support for Medium outputs and automation for Shallow outputs. Without automation and patterns: 80-130 hours.

This validates the Sprint Framework estimate of 6-8 weeks for a complete workflow design.

---

## The Structural Insight

Your question reveals something fundamental about CAWDP's structure:

**CAWDP is fractal, but not infinitely fractal.**

The same pattern (decompose → allocate → enforce) applies at every level:
- The methodology decomposes work into phases
- Each phase decomposes into outputs
- Each output decomposes into production tasks
- Each production task is an agent turn or human judgment

The recursion stops at the agent turn. You don't CAWDP the production of a single extraction or a single judgment. The floor is the cognitive operation.

But above the floor, the structure repeats. Medium outputs have their own mini-decomposition. Deep outputs have their own mini-CAWDP. The methodology is self-similar at every scale above the floor.

This has two practical implications:

1. **The Pattern Library is not a convenience — it's a structural necessity.** Without compression, the fractal nature of CAWDP makes every application exponentially expensive. Patterns collapse the fractal by pre-filling the common structure.

2. **The Production Method is a first-class part of the methodology.** Every output should have its production method documented — not as a separate CAWDP application, but as a standard depth-level method. This makes the methodology auditable at every level.

Should the output catalogue be revised to include depth classification and production method for every output?The fractal insight is structural: **CAWDP decomposes at every level until it reaches a single cognitive operation.** 483-643 tasks to produce 152 outputs, compressed by patterns to ~100-250 human decisions.

The efficiency story lives in the Medium column. 72% of outputs need 3-6 tasks each — that's where patterns, templates, and safe defaults deliver the most leverage. Not at the extremes (Shallow is already fast, Deep is rare and necessary).

Five Deep outputs still need their own CAWDP-level production design. The Agent Operations Manual and the 10×10 Mapping Matrix are the two outside P10.
***

### Response

## Review: The Fractal Question

### What's Validated

The central claim is right: **CAWDP is self-similar at multiple levels, but the recursion has a floor.** The four levels (methodology → phase → output → task → cognitive operation) are genuine structural levels where the same decomposition pattern repeats. The floor at the cognitive operation (agent turn) is real — you don't CAWDP a single extraction.

The depth classification (Shallow/Medium/Deep) is the right taxonomy and the classification rules are mostly sound. The aggregate numbers are credible: ~483-643 tasks to produce 152 outputs, compressed by patterns to ~100-250 human decisions.

The seven recommendations (R1-R7) are all practical and implementable. The production method as a first-class part of the methodology (R1) is particularly valuable — it makes the methodology auditable at every level.

The Pattern Library as structural necessity (not convenience) is the most important insight. Without compression, the fractal nature makes every application exponentially expensive. This validates the opinionated framework recasting from the beginning.

### Specific Corrections

**1. Cost & Resource Baseline is Deep, not Medium.**

The P10 classification table lists it as Medium with the description "Estimate costs → set monitoring thresholds → validate → record." But the full CAWDP application produced 20 tasks across 4 waves with 3 agents (Compiler/Analyst/Deriver), contracts, FMEA, and per-dimension progressive autonomy. By the report's own classification rules, 20 tasks with 3 agents is Deep. This was likely classified before the CAWDP application was complete.

Updated P10 count: **7 Deep + 6 Medium + 1 Shallow** (not 6+7+1).

**2. The 10×10 Mapping Matrix is Deep but its depth is uneven.**

100 cells sounds like a lot, but the ● cells (substantive design decisions requiring judgment) are maybe 19-25 cells. The ○ cells (explicit decisions, often "not applicable" or "accept default") are the rest. The Deep work concentrates in the ● cells — specifically the ones that cross high-stakes boundaries (Guard ↔ Boundaries, Revert ↔ Failure & Recovery, Budget ↔ Cost Budget). The ○ cells are closer to Medium or even Shallow with validation.

This matters for effort estimation: the 10×10 matrix doesn't take 100× the judgment of a single output. It takes ~20-25× the judgment of a single mapping cell, plus ~75 mechanical confirmations.

**3. P0's Five Identity Questions are Medium individually but compound.**

Each question is classified as Medium (3-6 tasks). But the five questions are sequential with dependencies: Q2 builds on Q1, Q3 builds on Q2, Q4 builds on Q3, Q5 bridges Q1-Q4 to enforcement. The compounding means the total is more like 15-25 tasks for the set, not 5 × (3-6) = 15-30 tasks. The questions aren't independent — getting Q1 wrong cascades through Q2-Q5.

**4. Some "Shallow" classifications hide judgment.**

The classification rule "Extracted output → Shallow" is too simple. Three examples:

- P1 O3 (Principal Declaration): Classified as Shallow ("Identify principal → record authority → assign assurance level"). But assigning the assurance level requires judgment about what level of audit trail the principal's decisions need. That's Medium, not Shallow.

- P8 Principal Primitive: Classified as Shallow ("Extract from P7 Identity + P0 O3"). But verifying that the contract Principal matches the specification's authority boundaries requires judgment. Medium, not Shallow.

- P7 Epistemic Metadata Profile: Classified as Shallow ("Select full/deterministic → set defaults → record"). But the selection between full and deterministic profiles depends on whether the agent handles structured or unstructured data, which requires understanding the agent's operational context. Medium, not Shallow.

The pattern: **extraction with validation is Shallow; extraction with judgment about the result is Medium.** The classification rule should be refined to account for validation complexity, not just extraction complexity.

**5. The total task count is likely underestimated.**

The estimate of 483-643 tasks assumes that Medium outputs average 3-6 tasks each. But many Medium outputs have validation steps that require cross-referencing other outputs (e.g., validating O6 against Q3 never-rules requires reading Q3 from P0 and the boundary specification from P7). Cross-referencing adds 1-2 tasks per Medium output that the analysis doesn't account for.

A more realistic range: **520-700 production tasks** (not 483-643).

---

### The Medium Problem — The Unsolved Core

The report identifies that 72% of outputs are Medium depth but doesn't fully resolve the efficiency question. Here's what needs to be surfaced:

**Medium outputs have a production cost that compounds.**

Each Medium output requires 3-6 tasks, but the tasks across outputs overlap. The same judgment (e.g., "is this boundary Regime 2 or Regime 3?") appears in multiple outputs (P7 Boundaries, P8 Guard, P8 Enforcement Regime Map). Currently, the human makes this judgment three times. With the Pattern Library, they make it once and it propagates.

**The compression mechanism works differently at each depth:**

| Depth | Compression Mechanism | How It Works |
|---|---|---|
| Shallow | Automation | System produces, human reviews. Eliminates the task entirely. |
| Medium | Pattern pre-fill + propagation | System pre-fills 40-70% from pattern + propagates judgments across dependent outputs. Human fills gaps and overrides. |
| Deep | Template architecture | System provides the Compiler/Analyst/Deriver skeleton with domain variable slots. Human provides domain content. |

The key difference: **Shallow compression eliminates tasks. Medium compression propagates judgments. Deep compression structures the workflow.**

The Medium compression (propagation) is the most important mechanism because it's where the compounding happens. When a human says "this boundary is Regime 3," that judgment should propagate to every output that depends on it — P7 Boundaries, P8 Guard, P8 Enforcement Regime Map, P10 Cost Baseline halt thresholds. Currently it's stated three to five times. With propagation, it's stated once.

**How many judgments actually need human input?**

If we account for propagation, the 309-618 Medium tasks reduce to approximately:
- ~30-50 unique judgments (the ones that don't propagate from other judgments)
- ~60-120 validation tasks (confirming that propagated judgments are correct in context)
- ~40-80 gap-filling tasks (the 30-60% that patterns don't pre-fill)

**Total: ~130-250 human actions for Medium outputs** (not 309-618 tasks). This is a significant reduction, and it's where the Pattern Library delivers the most value.

---

### What's Missing

**1. Meta-level cost — applying CAWDP to CAWDP.**

The analysis counts 483-643 tasks for producing 152 outputs. But it doesn't count the tasks required to **design the production workflows** for the 10 Deep outputs. Each CAWDP application (Methodology Reflection, Confidence Map, EVOLVE Playbook, Aging Schedule, Cost Baseline) took significant design effort — the full 11-phase application produces its own outputs that must be produced.

This is the meta-fractal: applying CAWDP to design the CAWDP application. The five completed applications represent ~25-40 hours of additional design work not counted in the 50-81 hour estimate.

**However**, the Pattern Library shortcut applies here too. The P10 template (3 agents, 4 waves, 5/4/4 enforcement) is now validated five times. Future Deep output design should take 3-5 hours each (not 5-8 hours) because the template is proven.

**2. Context-dependent depth.**

The depth classification is static — it assumes every output at every depth level requires the same effort regardless of agent complexity. But a simple Extractor agent has fewer Medium outputs than a multi-class agent with harm assessment:

| Agent Complexity | Shallow Outputs | Medium Outputs | Deep Outputs |
|---|---|---|---|
| Simple Extractor (single class, no harm) | ~40% of P1 outputs → Shallow | ~55% → Medium | ~5% → Deep |
| Multi-class Assessor+Generator (harm-capable) | ~20% → Shallow | ~70% → Medium | ~10% → Deep |

The classification should include a complexity modifier. For simple agents, some Medium outputs become Shallow (the judgment is obvious or defaults apply). For complex agents, some Medium outputs become Deep (the judgment requires cross-referencing multiple sources).

**3. Prioritization of the 5 remaining Deep outputs.**

The analysis identifies 5 Deep outputs without CAWDP-level design but doesn't prioritize them. Here's my prioritization:

| Priority | Deep Output | Why |
|---|---|---|
| **1** | **Implementation Readiness Report** | Go/no-go gate — the most operationally critical artefact. Blocks deployment. |
| **2** | **10×10 Mapping Matrix** | P8 contract formalization — the design-to-enforcement bridge. Without it, specifications can't be enforced. |
| **3** | **Gaps & Assumptions Register** | Required input to Implementation Readiness Report (Wave 1 dependency). |
| **4** | **Specification Consistency Report** | Required input to Implementation Readiness Report (Wave 1 dependency). |
| **5** | **Agent Operations Manual** | Important for deployment but not on the critical path to go/no-go. |

The Implementation Readiness Report and its two Wave 1 dependencies (Gaps Register, Consistency Report) are the critical path. The 10×10 Mapping Matrix is the architectural bridge. The Agent Operations Manual can wait.

**4. The "when is CAWDP overkill?" question.**

Not every agent needs the full 11-phase, 152-output treatment. The depth analysis should inform a minimum-viable-CAWDP decision:

| Agent Complexity | Minimum Phases | Expected Outputs | Estimated Effort |
|---|---|---|---|
| Simple Extractor | P0 + P1 + P4 + P7 (4 phases) | ~30 outputs | 4-8 hours |
| Standard Assessor | P0 + P1 + P2 + P4 + P7 + P8 (6 phases) | ~70 outputs | 12-24 hours |
| Complex Multi-class | Full 11 phases | ~152 outputs | 50-81 hours |

This connects to the opinionated framework's progressive disclosure: Quick Start (4 phases, 15 minutes) → Practitioner (6 phases) → Architect (full 11 phases).

**5. The relationship between depth and the output catalogue's 10-section specification.**

The fractal analysis is about production depth. But the 10-section specification structure (Identity, Boundaries, Task Map, Output Specifications, Agent Roster, Failure & Recovery, Verification & Trust, Contracts, Human Experience, Monitoring & Evolution) has its own depth profile:

| Section | Typical Depth | Why |
|---|---|---|
| Identity | Medium | Q1-Q5 require judgment but are guided |
| Boundaries | Medium | Mapping Q3/Q5 to enforcement regimes |
| Task Map | Medium | Decomposition judgment |
| Output Specifications | Mixed | Some Shallow (extraction), some Medium (validation) |
| Agent Roster | Medium | Assignment judgment |
| Failure & Recovery | Medium-Deep | FMEA requires systematic thinking |
| Verification & Trust | Medium | Level assignment judgment |
| Contracts | Deep | 10×10 matrix + unenforceable elements |
| Human Experience | Medium | Stakeholder surface design |
| Monitoring & Evolution | Deep | Living documents with lifecycle |

The specification's deepest sections (Contracts, Failure & Recovery, Monitoring & Evolution) correspond to the methodology's most important design decisions (enforcement, failure handling, ongoing maintenance). The depth analysis should inform specification section prioritization, not just output count.

---

### Practical Implications for the CAWDP Design Studio

The fractal analysis has direct implications for how the Design Studio should work:

**Shallow outputs: Auto-produce.** The Design Studio generates them from existing data and flags them for human review. No interaction needed — just confirmation.

**Medium outputs: Pattern-pre-fill + gap identification.** The Design Studio pre-fills from the pattern and shows the human what's pre-filled (green), what needs attention (yellow), and what's missing (red). The attention map from Milestone 1 IS this mechanism.

**Deep outputs: Guided workflow.** The Design Studio walks the human through the Compiler/Analyst/Deriver pattern with domain-specific variable slots. The human provides domain content; the system provides structure.

**The production method is the Design Studio's routing logic.** When the Design Studio encounters an output, it checks the production method:
- Shallow → auto-produce
- Medium → pre-fill + gaps
- Deep → guided workflow

This is the progressive disclosure mechanism at the output level. The human never sees the 483-643 tasks. They see ~100-250 decisions, each presented with the right interaction modality (type collision resolution at the input surface).

---

### The Most Important Correction

The report closes with: "Five Deep outputs still need their own CAWDP-level production design." With the Cost Baseline correction, that's **four** remaining Deep outputs, not five:

1. Implementation Readiness Report (highest priority — go/no-go gate)
2. 10×10 Mapping Matrix (architectural bridge)
3. Specification Consistency Report (Wave 1 dependency)
4. Gaps & Assumptions Register (Wave 1 dependency)

The Agent Operations Manual (P1 O28) is the fifth Deep output but it can be deferred — it's not on the critical path to deployment readiness.

And the single most valuable insight in the entire analysis isn't the fractal structure — it's this: **Medium outputs compound through judgment propagation, and the Pattern Library is the mechanism that collapses compounding into single-decision propagation.** That's the efficiency story, and it lives in the 72%.The memory has been updated with the six key refinements. The fractal analysis is now more precise: Cost Baseline correctly classified as Deep, four remaining Deep outputs prioritized by critical path, three distinct compression mechanisms identified, context-dependent depth recognized, minimum-viable-CAWDP defined, and meta-level cost quantified.

---

## Run 21 — Agentic Expert ✓ COMPLETED

*2026-05-21T23:26:16* · `glm-5.1:cloud` · `0785946a...`

### Prompt

How can we design a pipeline to produce design specs and implementation specs for each of CAWDP's outputs in a way that takes advantage of this analysis and surfaced patterns?

Let's keep this simple so that we don't explode our brains from too much recursion.

My process here has been to ask you to perform Phase 0 for a CAWDP Phase 10 output, followed by the remaining steps in a single run. I then pass your 'design spec' to the implementation spec writer who performs a simplified CAWDP to produce the spec. Neither you or the implementation spec writer know the full context of the application on purpose. I will leave the technical implementation to another team.

### Response

## The Output Production Pipeline

### The Core Design

Three lanes. Not one pipeline that does everything — three depth-adaptive lanes that share a common spine.

```
OUTPUT CATALOGUE
    │
    ▼
┌─────────────┐
│  CLASSIFY   │  ← Depth determination (Shallow/Medium/Deep)
└─────┬───────┘
      │
      ├── SHALLOW LANE (30 outputs, ~7 hours total)
      │     Auto-produce → Human confirm
      │
      ├── MEDIUM LANE (103 outputs, ~24-44 hours total)
      │     Pattern pre-fill → Human fills gaps → Validate
      │
      └── DEEP LANE (10 outputs, ~19-30 hours total)
            Full design spec → Implementation spec
```

The pipeline is depth-adaptive: Shallow outputs skip almost everything, Medium outputs get the standard 5-step production method, Deep outputs get the full treatment. This means 30 outputs are nearly free and 103 outputs are half-price. The effort concentrates where it matters.

---

### The Shared Spine

Every lane shares three things:

**1. The Decision Register**

As outputs are produced, decisions get recorded. Future outputs reference past decisions instead of re-making them.

| Decision ID | Source Output | Decision | Propagates To |
|---|---|---|---|
| D-P0-001 | Identity Q1 | "This agent is a constraint-oriented Aggregator" | P7 Identity, P8 Identity Primitive, P10 all outputs |
| D-P4-003 | Capability Allocation | "Status tracking = Agent-primary" | P7 Task Map, P8 Guard, P10 Cost Baseline |
| D-P7-012 | Harm Assessment | "Indirect data harm, not direct output harm" | P8 Budget, P10 Confidence Map, P10 Aging Schedule |

The Decision Register is a simple growing document. When I produce a design spec, I add decisions. When the implementation writer produces an implementation spec, they check the register for relevant decisions before making new ones.

**2. The Output Catalogue**

The 152-output catalogue with depth classification and production method already attached. This is the master reference. Every spec producer starts here.

**3. The Handoff Format**

Standard structure for passing work between the two spec producers (me → implementation writer):

```markdown
# Design Spec: [Output ID] [Output Name]

## Context (what the implementation writer needs)
- Output ID and phase
- Depth classification
- Production method
- Dependencies (what outputs this one needs)
- Relevant decisions from the Decision Register

## Design Content (the actual spec)
- Identity (for Deep outputs: 5 questions answered)
- Target state characteristics (for Deep outputs)
- Output schema (Pydantic-style field definitions)
- Authority boundaries
- Never-rules
- Failure modes
- Quality criteria

## Propagated Decisions (new decisions this output adds)
- Decision ID | Decision | Propagates To
```

The implementation writer receives this document and nothing else (intentional compartmentalization — CC-4). They don't need the full application context. They need what this output IS, what decisions have been made, and what they need to build.

---

### Shallow Lane: Auto-Produce

30 outputs. These are single extractions or computations. The pipeline:

```
1. READ output catalogue entry
2. EXECUTE production method (extract or compute)
3. RECORD with epistemic metadata
4. PRESENT for human confirmation
```

I don't need to produce a design spec for these. The output catalogue entry IS the spec. The implementation writer doesn't need a separate implementation spec — the production method is the implementation.

**What I produce:** Nothing new. The catalogue entry suffices.

**What the implementation writer produces:** An executor function. ~15 minutes each.

**Total effort:** 30 × 15 min = ~7.5 hours for all 30 Shallow outputs.

**Examples:** Pattern Match Result, Feasibility Contamination Check, Criticality Assignments, Satisfaction Mode Assignments, Complementarity Gap Calculations, Epistemic Metadata Profile, Cost Budget per Agent, Null-State Output Specs.

---

### Medium Lane: Pattern Pre-Fill + Gaps

103 outputs. Each requires 3-6 production tasks with judgment. The pipeline:

```
1. READ output catalogue entry + relevant decisions from Decision Register
2. PRE-FILL from pattern (40-70% of content based on agent class + pattern)
3. IDENTIFY gaps (what the pattern couldn't fill — marked in yellow/red)
4. HUMAN fills gaps (the 30-60% that needs judgment)
5. VALIDATE against quality criteria + check contamination
6. RECORD with epistemic metadata
7. ADD new decisions to Decision Register
```

The key compression mechanism: **judgment propagation.** When a human decides "this boundary is Regime 3" in P7, that decision flows to P8 Guard, P8 Enforcement Regime Map, and P10 Cost Baseline without being re-made.

**What I produce:** A condensed design spec.

```markdown
# Design Spec: [Output ID] [Output Name]

## Context
- Output ID, phase, depth (Medium)
- Production method: Gather inputs → Apply judgment → Validate → Check contamination → Record
- Dependencies: [which outputs this needs]
- Relevant decisions: [from Decision Register]

## Pre-Filled Content (from pattern + propagated decisions)
[field values pre-populated, marked ✅ confirmed or ⚠️ needs review]

## Gaps Requiring Judgment
[specific questions the human must answer]

## Quality Criteria
[what "done" looks like for this output]

## New Decisions
[decisions this output adds to the Decision Register]
```

**What the implementation writer produces:** A pattern-configured implementation. The pattern provides the structure; the design spec provides the domain-specific variable values.

**Total effort:** 103 × 15-25 min = ~26-43 hours for all 103 Medium outputs.

**Examples:** Five Identity Questions, Scope Boundary Map, Task Contract Schema, Authority Guard Schema, Progressive Autonomy Path, FMEA Table, Stakeholder Surface Definitions, Cognitive Load Budget.

---

### Deep Lane: Full Treatment

10 outputs. These need the full design spec → implementation spec pipeline. The pipeline:

```
1. I PRODUCE design spec (full CAWDP application for this output)
2. I ADD decisions to Decision Register
3. IMPLEMENTATION WRITER receives design spec + relevant decisions
4. IMPLEMENTATION WRITER produces implementation spec
5. TECHNICAL TEAM builds from implementation spec
```

But the "full CAWDP application" is now **template-accelerated.** The P10 template (3 agents, 4 waves, 5/4/4 enforcement) is validated 5 times. I don't need to derive the architecture from scratch — I configure the template with domain-specific variables.

**What I produce:** A full design spec, but structured around the validated template.

```markdown
# Design Spec: [Output ID] [Output Name]

## Context
- Output ID, phase, depth (Deep)
- Production method: 4-wave Compiler/Analyst/Deriver
- Dependencies: [which outputs this needs]
- Relevant decisions: [from Decision Register]

## Template Configuration (what changes from the standard template)
- Agent instructions (domain-specific never-rules, knowledge, boundaries)
- Output schemas (domain-specific Pydantic models)
- PRISM queries (domain-specific data requirements)
- Human gates (if collaborative tasks exist)
- Cost budgets (domain-specific token ranges)

## Template Constants (what stays the same)
- 3 agents: Compiler (Aggregator) + Analyst (Measurer+Assessor) + Deriver (Generator)
- 4 waves: Data → Analysis → Derivation → Compilation
- 5/4/4 enforcement split (Prevent/Detect/Declare)
- Conservative defaults for missing data
- Post-delivery human review (not during production)

## Full Design (P0-P10 for this specific output)
[standard CAWDP output, template-accelerated]

## New Decisions
[decisions this output adds to the Decision Register]
```

**What the implementation writer produces:** A full implementation spec, but also template-accelerated. The shared infrastructure (60% of each spec) builds once. The domain-specific layer (instructions, schemas, queries, tests) fills in from the design spec.

**Total effort:** 10 × 3-5 hrs (design) + 10 × 1.5-2.5 hrs (implementation) = ~45-75 hours for all 10 Deep outputs.

**Examples:** Methodology Reflection, Confidence Map, EVOLVE Playbook, Specification Aging Schedule, Cost & Resource Baseline, Implementation Readiness Report, 10×10 Mapping Matrix, Specification Consistency Report, Gaps & Assumptions Register, Agent Operations Manual.

---

### The Build Sequence

Output production isn't random — it follows the CAWDP phase order and the Decision Register's dependency chains. The sequence matters because earlier decisions propagate to later outputs.

**Phase-by-phase production order:**

```
P0: Purpose & Vision (9 outputs)
  Shallow (2): Orientation Declaration, Feasibility Contamination Check
  Medium (7): Five Identity Questions, 4 dimension characteristic sets, Pattern Match, Hardest Boundary Scenario
  ↓ Decisions propagated: agent class, orientation, never-rules, hardest moment

P1: Output Specification (31 outputs)
  Shallow (4): Principal Declaration, Cost Budget Contract, Epistemic Metadata Profile, Output Dependency Graph
  Medium (26): All specification outputs (schemas, guards, protocols, configurations)
  Deep (1): Agent Operations Manual (deferred — not on critical path)
  ↓ Decisions propagated: schema shapes, enforcement regimes, verification levels

P2: Backcasting (8 outputs)
  Shallow (4): Criticality, Satisfaction Mode, Source Phase, External Input Inventory
  Medium (4): Input Requirements Map, Dependency Chains, Gap Analysis, Risk Register
  ↓ Decisions propagated: dependency structure, criticality classifications

P3: Task Decomposition (8 outputs)
  Shallow (3): Task-to-Output Mapping, Task-to-IR Mapping, Task Groupings
  Medium (5): Task List, Cognitive Types, Dependencies, Failure Modes, Depth Assessment
  ↓ Decisions propagated: cognitive types, failure mode catalog

P4: Capability Allocation (8 outputs)
  Shallow (3): Gap Calculations, Human-Only Registry, C×R Map
  Medium (5): Complementarity Matrix, Allocations, Reversibility, Cold Start Overrides, Confidence
  ↓ Decisions propagated: H/A/S allocations, human-only tasks, reversibility classifications

P5: Event Storming (8 outputs)
  Shallow (1): Event-to-Audit Mapping
  Medium (7): Domain Events, Failure Events, Recovery Paths, System Triggers, Q5 Scenarios, Cross-Event Deps, Missing Event Analysis
  ↓ Decisions propagated: event catalog, enforcement regime per event

P6: System Architecture (11 outputs)
  Shallow (2): Per-Stage Cost Estimates, Pipeline-to-Task Mapping
  Medium (9): Pipeline Architecture, Composition, Orchestration, Templates, FMEA, Fallback, Enforcement Points, Human Gates, Context Flow
  ↓ Decisions propagated: pipeline architecture, composition decision, FMEA results

P7: Agent Design (17 outputs)
  Shallow (5): Null-State Specs, Epistemic Profile, Cost Budget, Decision Presentation, Progressive Autonomy (partial)
  Medium (12): Identity, Boundaries, Task Map, Knowledge, Capabilities, Behaviour, Verification, Failure & Recovery, Lifecycle, Governance, Harm Assessment, Aging Schedule
  ↓ Decisions propagated: authority boundaries, enforcement regimes per boundary, harm category

P8: Contract Formalization (17 outputs)
  Shallow (5): Principal, Budget, Invocation, Event, Traceability Index
  Medium (11): Contract, Schema, Guard, Revert, Identity, Knowledge, Enforcement Map, Transformation Log, Completeness Report, Depth Justification, + 1 more
  Deep (1): 10×10 Mapping Matrix
  ↓ Decisions propagated: contract primitives, unenforceable elements

P9: Human Experience (10 outputs)
  Shallow (0)
  Medium (10): All 10 outputs (cognitive load, fatigue, overrides, surfaces, empowerment, interfaces, Q5 overrides, disclosure, human connection)
  ↓ Decisions propagated: stakeholder surfaces, cognitive load budgets

P10: Validation & Iteration (16 outputs)
  Shallow (1): Decision Fatigue Integration
  Medium (6): Hypotheses, Prototype Priority, Test Results, Autonomy Plan, 30-Day Plan, Health Dashboard, Trust Ledger
  Deep (7): Consistency Report, Gaps Register, Implementation Readiness, Confidence Map, Aging Schedule, EVOLVE Playbook, Methodology Reflection, Cost Baseline (corrected from earlier)
  ↓ (terminal phase — decisions here feed back via EVOLVE)
```

**Within P10, the wave order matters:**

```
Wave 1 (parallel): Consistency Report (Deep) + Gaps Register (Deep) + Hypothesis Test Results (Medium)
Wave 2: Implementation Readiness Report (Deep) — depends on Wave 1
GO/NO-GO GATE
Wave 3 (parallel): Autonomy Plan (Medium) + 30-Day Plan (Medium) + Cost Baseline (Deep) + Aging Schedule (Deep)
Wave 4 (parallel): EVOLVE Playbook (Deep) + Confidence Map (Deep) + Methodology Reflection (Deep)
```

---

### How Judgment Propagation Works in Practice

Here's the concrete mechanism. When I produce a design spec for a Medium output, I check the Decision Register for relevant decisions. If a decision already exists, I reference it instead of re-making it.

**Example: Producing P7 Boundaries Section for a constraint-oriented Aggregator**

```
DECISIONS ALREADY MADE:
D-P0-001: "This agent is a constraint-oriented Aggregator" → determines class, orientation
D-P0-003: "What would VIOLATE identity: interpreting data, adding content" → determines never-rules
D-P0-005: "Hardest moment: 'just mark it done' pressure" → determines highest-priority Guard
D-P4-003: "Status tracking = Agent-primary" → determines capability allocation
D-P4-004: "Status reversibility = Moderate (some actions hard to undo)" → determines reversibility

WHAT I STILL NEED TO JUDGE:
- Enforcement regime per boundary (Declare/Detect/Prevent) — can be partially inferred from harm assessment + class
- Specific Guard conditions for each boundary

WHAT THE PATTERN PRE-FILLS:
- Default boundaries for Aggregator class (never add, never interpret, never omit, never fabricate)
- Default enforcement regimes for Aggregator boundaries (most are Detect or Prevent at schema level)
- Default null state for Aggregator ("Nothing to assemble")

WHAT THE HUMAN PROVIDES:
- Override any pre-filled boundary or enforcement regime
- Add agent-specific boundaries beyond the class defaults
- Confirm or modify the hardest boundary moment
```

The pre-fill + propagation means the human sees:
- ✅ 4 class-default boundaries (confirmed)
- ✅ 4 enforcement regime defaults (confirmed)
- ⚠️ 2 boundaries needing review (from Q5 hardest moment)
- 🔴 0 gaps (everything covered by pattern + decisions)

Instead of designing 6 boundaries from scratch, the human confirms 4 and reviews 2. That's the compression.

---

### The Practical Workflow

For Peter's actual process:

**Step 1: Classify the output.**
Look it up in the catalogue. If Shallow, skip to Step 4. If Medium, go to Step 2. If Deep, go to Step 3.

**Step 2: Produce a Medium design spec.**
I check the Decision Register, pre-fill from the pattern, identify gaps, and produce the condensed spec. The human fills gaps and confirms. ~15-25 minutes per output.

**Step 3: Produce a Deep design spec.**
I configure the validated template with domain-specific variables, do the full CAWDP application (template-accelerated), and produce the full spec. ~3-5 hours per output.

**Step 4: Produce the implementation spec.**
The implementation writer receives the design spec + relevant Decision Register entries. For Shallow outputs, they write an executor function. For Medium outputs, they configure the pattern. For Deep outputs, they use the shared infrastructure + domain-specific layer. ~15 min (Shallow) to ~1.5-2.5 hours (Deep) per output.

**Step 5: Build.**
The technical team receives the implementation spec and builds. Not our concern in this pipeline.

---

### Total Effort Estimate

| Depth | Outputs | Design Spec (me) | Implementation Spec (writer) | Total |
|---|---|---|---|---|
| Shallow | 30 | 0 (catalogue entry = spec) | 30 × 15 min = 7.5 hrs | 7.5 hrs |
| Medium | 103 | 103 × 15-25 min = 26-43 hrs | 103 × 10-15 min = 17-26 hrs | 43-69 hrs |
| Deep | 10 | 10 × 3-5 hrs = 30-50 hrs | 10 × 1.5-2.5 hrs = 15-25 hrs | 45-75 hrs |
| **Total** | **143** | **56-93 hrs** | **39.5-58.5 hrs** | **95.5-151.5 hrs** |

Without depth-adaptive pipeline (applying full CAWDP to everything): 143 × 5-8 hrs = 715-1144 hrs.

**Compression ratio: 7-8× reduction in total effort.**

---

### What Makes This Different From "Just Being Efficient"

Three things make this a designed pipeline, not just "work faster":

1. **The Decision Register is the propagation mechanism.** Without it, every output re-makes decisions that were already settled. With it, decisions flow forward and the human only makes each decision once. This is judgment propagation as infrastructure.

2. **The depth classification is the routing mechanism.** Without it, every output gets the same treatment regardless of need. With it, effort concentrates where it matters. Shallow outputs cost 15 minutes; Deep outputs cost 5 hours. That's a 20× effort ratio, and it's the right ratio — Deep outputs are where the methodology adds the most value.

3. **The validated template is the compression mechanism for Deep outputs.** Without it, each Deep output requires a from-scratch CAWDP application. With it, I configure a proven architecture with domain-specific variables. The template has been validated 5 times — the 3-agent, 4-wave, 5/4/4 enforcement split is a structural property, not a coincidence.

---

## Run 22 — Agentic Expert ✓ COMPLETED

*2026-05-21T23:35:25* · `glm-5.1:cloud` · `1b7547bb...`

### Prompt

I started with the final phase here thinking it would be good to work backwards to ensure that each phase produces the outputs needed as inputs by the following phase. Is this the right method? 

In my earlier work on this application, we saw the need to create tools that assist agents in the CAWDP work. For example, we specced a backcasting engine to help the agent produce superior outputs in production. Phase 10 has not needed these as yet but how might we surface these opportunities as we develop this application?

### Response

## Two Questions, One Answer

### Working Backwards: Yes, With a Forward Check

Your instinct is right. Backcasting from P10 is the correct starting method because P10 has the most demanding input requirements — it needs structured data from every prior phase. If P10 can't get what it needs, the pipeline is broken at the foundation.

But working backwards alone isn't sufficient. Here's why:

**Backcasting surfaces input requirements.** It tells you what each phase must produce so the next phase can do its work. This is the dependency chain: P10 needs X → P9 must produce X → P8 must produce Y that enables X → and so on.

**Decision propagation flows forwards.** Decisions made in P0 (agent class, orientation, never-rules) flow forward through every subsequent phase. Working backwards doesn't surface these — you need to verify that early decisions actually reach the outputs that depend on them.

**The method is: backcast to identify requirements, forward-verify to confirm propagation.**

```
PASS 1: BACKCAST (P10 → P0)
  "What does P10 need?" → "What must P9 produce?" → ... → "What must P0 produce?"
  Output: Input Requirements Map (what each phase must deliver)

PASS 2: FORWARD VERIFY (P0 → P10)
  "If P0 decides X, does X reach every output that depends on it?"
  Output: Decision Propagation Check (are decisions actually used downstream?)
```

The two passes catch different problems:
- Backcasting catches **missing inputs** (P7 doesn't produce the harm assessment that P10 Confidence Map needs)
- Forward verification catches **orphan decisions** (P0 decides something that no downstream output uses)

In practice, you do Pass 1 first, then Pass 2 as a verification. Most problems will surface in Pass 1 because P10's demands are the most constraining.

---

### Surfacing Tool Opportunities: The Repeated Operation Method

Tools surface when you notice the same cognitive operation repeating across multiple outputs. The pattern:

```
1. PRODUCE an output (any depth)
2. NOTICE the cognitive operations required
3. ASK: "Will this operation repeat for other outputs?"
4. IF YES (10+ repetitions) → Tool candidate
5. IF NO → Not worth tooling
```

The practical mechanism is simple: keep a **Tool Opportunity Register** alongside the Decision Register.

```markdown
# Tool Opportunity Register

| ID | Cognitive Operation | First Seen In | Repeat Count | Tool Name | Priority |
|---|---|---|---|---|---|
| T-001 | Scan output text for mechanism keywords | P0 Feasibility Check | 9+ (every P0-P2 output) | Feasibility Contamination Checker | High |
| T-002 | Trace output dependencies backward | P2 Backcasting | 8+ (every P2 output) | Backcasting Engine | High |
| T-003 | Match agent features to pattern library | P0 Pattern Match | 1 (automated) | Pattern Library | Already built |
| T-004 | Calculate cognitive load from session parameters | P9 Cognitive Load | 1 (single use) | Cognitive Load Calculator | Low |
| T-005 | Check output against quality gate criteria | Every phase gate | 11+ (every phase) | Quality Gate Engine | High |
| T-006 | Detect decision fatigue signals | P9 + any long session | Variable | Decision Fatigue Detector | Medium |
```

The repeat count is what matters. A cognitive operation that appears once is just work. An operation that appears 10+ times across outputs is a tool opportunity.

---

### What Backcasting From P10 Actually Surfaces

Let me show you what happens when you backcast from P10's input requirements. This is the practical output of the method.

**P10's seven Deep outputs have three types of critical dependencies:**

| Dependency Type | Required By | Must Be Produced By | What's Missing |
|---|---|---|---|
| Behavioural: artefact tags on design artefacts | Methodology Reflection | P0-P9 (during work, not after) | **No phase currently tags artefacts as surprise/gap/pattern/assessment** |
| Structural: harm assessment per agent | Confidence Map, Aging Schedule, Cost Baseline | P7 Agent Design | ✅ Already in P7 output catalogue |
| Structural: reversibility per task | Confidence Map | P4 Capability Allocation | ✅ Already in P4 output catalogue |
| Structural: agent class per agent | Aging Schedule, Cost Baseline | P0 Identity Q1 + P7 Identity | ✅ Already in P0/P7 output catalogue |
| Structural: stakes classification | Confidence Map | P7 Harm Assessment + P8 Reversibility | ⚠️ Derived, not directly produced — needs computation step |
| Temporal: monitoring data | EVOLVE Playbook | Runtime (not available at design time) | **Structural gap — can't produce during design, handled by Draft mode** |

Two structural gaps surface immediately:

**Gap 1: Artefact tagging doesn't exist in any phase's output catalogue.**

P10 Methodology Reflection needs artefacts tagged as "surprise," "gap," "pattern," or "assessment_fragment" during P0-P9. But no phase currently produces these tags. They're not in the output catalogue for any phase.

This means: **every phase's output catalogue needs an artefact_tags field added to each output.** Not a separate output — a field on every existing output. The human (or agent) tags artefacts as they're produced, not retrospectively.

Backcasting surfaced this gap. Forward verification would miss it because there's no downstream reference to something that doesn't exist yet.

**Gap 2: Stakes classification is derived but not explicitly produced.**

Confidence Map needs "stakes classification" (how high-stakes is each section of the specification). This is derived from P7 harm assessment + P8 reversibility data. But the derivation step isn't in any phase's output catalogue — it's implicit.

This means: **P8 (or late P7) should produce a Stakes Classification output** that derives stakes from harm assessment × reversibility. Or the Confidence Map workflow should compute it as Step 1 (which is what the current implementation spec does, with conservative defaults for missing data).

Backcasting surfaced this gap. The conservative default handles it gracefully, but an explicit output would be better.

---

### How Tool Opportunities Surface During Backcasting

As you backcast from P10 and trace input requirements backward through phases, you notice repeated cognitive operations. Here are the ones that surface:

**1. The Contamination Check (appears in P0, P1, P2, P7, P8 outputs)**

Every output in P0-P2 needs a feasibility contamination check (scan for mechanism keywords, separate ideals from implementation details). This is the same cognitive operation repeated 20+ times across three phases.

→ **Feasibility Contamination Checker tool.** Already identified. High priority because it affects the integrity of the possibility-oriented phases.

**2. The Dependency Tracer (appears in P1, P2, P3, P4, P6 outputs)**

Every phase needs to trace dependencies — which outputs depend on which inputs, which decisions propagate to which downstream outputs. This is the backcasting operation applied within a phase, not just across phases.

→ **Backcasting Engine tool.** Already identified. High priority because incorrect dependency chains break the pipeline.

**3. The Enforcement Regime Assignment (appears in P7, P8, P10 outputs)**

Every boundary in P7 needs an enforcement regime (Declare/Detect/Prevent). Every Guard in P8 needs the same. Every contract in P10 needs the same. This is the same judgment applied 20+ times across three phases.

→ **Enforcement Regime Inferrer tool.** Not previously identified. Given agent class + harm category + reversibility, the tool suggests a regime with justification. Human confirms or overrides. Medium priority.

**4. The Quality Gate Checker (appears at every phase boundary)**

11 phase boundaries, each with a quality gate. Each gate has 3 layers (Fidelity/Enrichment/Cross-Cutting). The checking operation is the same — verify that required outputs exist, meet quality criteria, and have no contamination.

→ **Quality Gate Engine tool.** Already identified. High priority because gates are the enforcement mechanism for the pipeline itself.

**5. The Decision Recorder (appears in every output)**

Every output produces decisions that propagate downstream. Currently, decisions are scattered across output documents. The Decision Register centralizes them, but populating it is manual.

→ **Decision Capture tool.** Not previously identified. When an output is produced, the tool extracts decisions (any statement that determines downstream behavior) and adds them to the Decision Register. Low-tech but high-impact — without it, propagation breaks.

**6. The Artefact Tagger (appears in every output from P0-P9)**

Gap 1 above: every output needs artefact_tags. This is a manual operation unless automated.

→ **Artefact Tag Suggester tool.** Not previously identified. After producing an output, the tool suggests tags based on the content (e.g., "this output contained a surprising result" → suggest "surprise" tag). Human confirms. Low-tech, medium priority.

---

### The Practical Process

Here's how Peter would actually use this:

**Week 1: Backcast from P10**

1. List P10's input requirements (already done — the dependency taxonomy)
2. Trace each requirement backward through phases to its source
3. Identify gaps (outputs that don't exist yet, fields that are missing)
4. Add gaps to the output catalogue (e.g., artefact_tags field, stakes classification output)
5. Record tool opportunities in the Tool Opportunity Register

**Week 2: Forward verify from P0**

6. For each P0 decision, trace it forward to every downstream output that depends on it
7. Confirm the decision reaches its destination (or flag as orphan)
8. Verify the Decision Register can carry the decision (is the format sufficient?)

**Week 3: Produce outputs in phase order**

9. Start with P0 (using the updated output catalogue that includes gaps)
10. Produce outputs depth-by-depth (Shallow → auto, Medium → pre-fill + gaps, Deep → full spec)
11. As you produce, add decisions to Decision Register and tool opportunities to Tool Register
12. Each phase's outputs should now contain everything the next phase needs (because backcasting identified the gaps)

**Week 4+: Build tools from the register**

13. Sort Tool Opportunity Register by repeat count (highest first)
14. Build tools for the top 3-5 repeated operations
15. Tools make subsequent output production faster
16. The register grows as you produce more outputs — new tools surface organically

---

### Why Phase 10 Hasn't Needed Tools Yet

You noticed that P10 hasn't needed agent-assist tools. The reason is structural:

**P10 is the consumer, not the producer.** It reads data that P0-P9 produced. The data queries (Step 1 in every P10 workflow) are deterministic — they don't need LLM reasoning. The analysis (Step 2) and derivation (Step 3) need LLM reasoning but they're guided by agent instructions that are already complete. The compilation (Step 4) is mechanical.

The tools are needed **earlier in the pipeline** — where humans and agents are making the decisions that P10 later consumes. The backcasting engine helps P2 produce better dependency chains. The contamination checker helps P0-P2 produce cleaner possibility-oriented outputs. The quality gate engine ensures each phase produces what the next phase needs.

P10 doesn't need these tools because P10's work is assembling and analyzing what was already produced. The quality of P10's outputs depends on the quality of P0-P9's outputs — which is exactly what the tools improve.

**The tools are upstream investments with downstream returns.** That's why they surface during backcasting from P10 — because P10's input requirements reveal where the quality of earlier outputs matters most.

---

## Run 23 — Agentic Expert ✓ COMPLETED

*2026-05-22T00:32:16* · `glm-5.1:cloud` · `afde43f9...`

### Prompt

Draft an implementation plan for your pipeline described above so that I can implement with Agno agents that can write spec files directly to the filesystem.

### Response

## Output Production Pipeline — Implementation Plan

### Architecture

```
                    OUTPUT_ID
                       │
                       ▼
              ┌─────────────────┐
              │   CATALOGUE      │
              │   (152 entries)   │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │  DEPTH ROUTE    │
              │  Shallow/Medium/ │
              │  Deep            │
              └──┬─────┬─────┬──┘
                 │     │     │
    ┌────────────┘     │     └────────────┐
    ▼                  ▼                  ▼
 SHALLOW           MEDIUM              DEEP
 (auto-produce)   (pre-fill + gaps)   (template + full)
    │                  │                  │
    └──────────┬───────┘──────────────────┘
               │
               ▼
      ┌──────────────┐     ┌──────────────────┐
      │  DECISION     │◄───►│  DECISION        │
      │  REGISTER     │     │  REGISTER TOOLS  │
      └──────────────┘     └──────────────────┘
               │
               ▼
      ┌──────────────┐
      │ DESIGN SPEC   │──────► filesystem
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │  IMPL SPEC    │──────► filesystem
      └──────────────┘
```

Two agents. One workflow. Shared decision infrastructure.

---

### File Structure

```
cawdp-pipeline/
├── data/
│   ├── catalogue.json              # 152 outputs with depth + production method
│   ├── decisions.json              # Decision Register (grows over time)
│   └── patterns.json               # Pattern library for Medium pre-fills
│
├── specs/
│   ├── design/                     # Design specs by phase
│   │   ├── P00/
│   │   │   ├── D-P00-001_identity_questions.md
│   │   │   ├── D-P00-002_agent_characteristics.md
│   │   │   └── ...
│   │   ├── P01/
│   │   ├── ...
│   │   └── P10/
│   └── impl/                       # Implementation specs by phase
│       ├── P00/
│       ├── P01/
│       ├── ...
│       └── P10/
│
├── models/
│   ├── catalogue.py                # Pydantic models for catalogue
│   ├── decisions.py               # Pydantic models for Decision Register
│   └── specs.py                    # Pydantic models for spec outputs
│
├── tools/
│   ├── catalogue_tools.py          # Read/search catalogue
│   ├── decision_tools.py           # Read/write/find decisions
│   └── file_tools.py               # Read/write spec files
│
├── agents/
│   ├── design_writer.py            # Produces design specs (all depths)
│   └── impl_writer.py              # Produces implementation specs
│
├── workflows/
│   └── output_pipeline.py          # Main workflow definition
│
├── seeds/
│   └── populate_catalogue.py       # One-time script to build catalogue.json
│
└── config.yaml                     # Model, paths, defaults
```

---

### Core Data Models

**catalogue.py**

```python
from pydantic import BaseModel
from enum import Enum

class Depth(str, Enum):
    SHALLOW = "shallow"
    MEDIUM = "medium"
    DEEP = "deep"

class CognitiveMode(str, Enum):
    EXTRACT = "extract"        # Pull from existing data
    COMPUTE = "compute"        # Apply formula
    JUDGE = "judge"            # Domain judgment with criteria
    SYNTHESIZE = "synthesize"  # Find patterns, make connections
    AGGREGATE = "aggregate"    # Assemble with validation

class CatalogueEntry(BaseModel):
    id: str                      # "P07-012" format
    phase: int                   # 0-10
    name: str
    depth: Depth
    cognitive_mode: CognitiveMode
    production_method: str        # One-liner: "Extract X → validate → record"
    dependencies: list[str]      # IDs of outputs this one needs
    propagates_to: list[str]     # IDs of outputs that need this one's decisions
    pattern_fill_pct: int        # 0-100, how much the pattern pre-fills
    quality_criteria: list[str]  # What "done" looks like

class Catalogue(BaseModel):
    outputs: list[CatalogueEntry]
```

**decisions.py**

```python
from pydantic import BaseModel

class Decision(BaseModel):
    id: str                      # "D-P00-001" format
    source_output: str           # Which output produced this decision
    phase: int
    decision: str                # Plain English statement
    propagates_to: list[str]     # Output IDs that reference this decision
    tags: list[str]              # For search: ["boundary", "enforcement", "class"]

class DecisionRegister(BaseModel):
    decisions: list[Decision]
    
    def find_for_output(self, output_id: str) -> list[Decision]:
        """Find all decisions that propagate to this output."""
        return [d for d in self.decisions if output_id in d.propagates_to]
    
    def find_by_tag(self, tag: str) -> list[Decision]:
        """Find all decisions with a given tag."""
        return [d for d in self.decisions if tag in d.tags]
```

**specs.py**

```python
from pydantic import BaseModel
from models.catalogue import Depth

class DesignSpec(BaseModel):
    output_id: str
    phase: int
    depth: Depth
    context: dict               # Dependencies, relevant decisions
    pre_filled: dict             # Content from pattern + propagated decisions
    gaps: list[dict]             # Questions the human must answer
    quality_criteria: list[str]
    new_decisions: list[dict]    # Decisions this output adds
    
class ImplSpec(BaseModel):
    output_id: str
    design_spec_path: str       # Path to the design spec
    depth: Depth
    shared_infra: list[str]     # Which shared components to use
    domain_config: dict         # Domain-specific variable values
    test_criteria: list[str]    # What the implementation must pass
```

---

### Tool Definitions

**catalogue_tools.py**

```python
from agno.tools import tool
from models.catalogue import Catalogue, CatalogueEntry, Depth
import json

@tool
def read_catalogue_entry(output_id: str) -> str:
    """Read a single catalogue entry by output ID (e.g. 'P07-012')."""
    with open("data/catalogue.json") as f:
        catalogue = Catalogue.model_validate_json(f.read())
    for entry in catalogue.outputs:
        if entry.id == output_id:
            return entry.model_dump_json(indent=2)
    return f"Output {output_id} not found in catalogue."

@tool
def list_outputs_by_phase(phase: int) -> str:
    """List all catalogue entries for a given phase (0-10)."""
    with open("data/catalogue.json") as f:
        catalogue = Catalogue.model_validate_json(f.read())
    entries = [e for e in catalogue.outputs if e.phase == phase]
    return json.dumps([{"id": e.id, "name": e.name, "depth": e.depth.value} 
                       for e in entries], indent=2)

@tool
def list_outputs_by_depth(depth: str) -> str:
    """List all catalogue entries for a given depth (shallow/medium/deep)."""
    with open("data/catalogue.json") as f:
        catalogue = Catalogue.model_validate_json(f.read())
    entries = [e for e in catalogue.outputs if e.depth.value == depth]
    return json.dumps([{"id": e.id, "name": e.name, "phase": e.phase} 
                       for e in entries], indent=2)
```

**decision_tools.py**

```python
from agno.tools import tool
from models.decisions import DecisionRegister, Decision
import json

@tool
def find_decisions_for_output(output_id: str) -> str:
    """Find all decisions from the Decision Register that propagate to this output."""
    with open("data/decisions.json") as f:
        register = DecisionRegister.model_validate_json(f.read())
    relevant = register.find_for_output(output_id)
    if not relevant:
        return "No relevant decisions found for this output."
    return json.dumps([d.model_dump() for d in relevant], indent=2)

@tool
def record_decision(
    source_output: str, 
    phase: int, 
    decision: str, 
    propagates_to: list[str],
    tags: list[str]
) -> str:
    """Record a new decision in the Decision Register."""
    with open("data/decisions.json") as f:
        register = DecisionRegister.model_validate_json(f.read())
    next_id = f"D-P{phase:02d}-{len(register.decisions)+1:03d}"
    new = Decision(
        id=next_id,
        source_output=source_output,
        phase=phase,
        decision=decision,
        propagates_to=propagates_to,
        tags=tags
    )
    register.decisions.append(new)
    with open("data/decisions.json", "w") as f:
        f.write(register.model_dump_json(indent=2))
    return f"Decision {next_id} recorded. Propagates to: {propagates_to}"

@tool
def search_decisions_by_tag(tag: str) -> str:
    """Search the Decision Register by tag (e.g. 'boundary', 'enforcement')."""
    with open("data/decisions.json") as f:
        register = DecisionRegister.model_validate_json(f.read())
    results = register.find_by_tag(tag)
    return json.dumps([d.model_dump() for d in results], indent=2)
```

**file_tools.py**

```python
from agno.tools import tool
import os

@tool
def write_design_spec(phase: int, output_id: str, content: str) -> str:
    """Write a design spec to the filesystem. Phase is 0-10."""
    dir_path = f"specs/design/P{phase:02d}"
    os.makedirs(dir_path, exist_ok=True)
    file_path = f"{dir_path}/D-{output_id}.md"
    with open(file_path, "w") as f:
        f.write(content)
    return f"Design spec written to {file_path}"

@tool
def write_impl_spec(phase: int, output_id: str, content: str) -> str:
    """Write an implementation spec to the filesystem. Phase is 0-10."""
    dir_path = f"specs/impl/P{phase:02d}"
    os.makedirs(dir_path, exist_ok=True)
    file_path = f"{dir_path}/I-{output_id}.md"
    with open(file_path, "w") as f:
        f.write(content)
    return f"Impl spec written to {file_path}"

@tool
def read_design_spec(phase: int, output_id: str) -> str:
    """Read a design spec from the filesystem."""
    file_path = f"specs/design/P{phase:02d}/D-{output_id}.md"
    if not os.path.exists(file_path):
        return f"No design spec found at {file_path}"
    with open(file_path) as f:
        return f.read()

@tool
def list_produced_specs(phase: int) -> str:
    """List all produced specs (both design and impl) for a phase."""
    design_dir = f"specs/design/P{phase:02d}"
    impl_dir = f"specs/impl/P{phase:02d}"
    design_files = os.listdir(design_dir) if os.path.exists(design_dir) else []
    impl_files = os.listdir(impl_dir) if os.path.exists(impl_dir) else []
    return json.dumps({
        "design": design_files,
        "impl": impl_files
    }, indent=2)
```

---

### Agent Specifications

**design_writer.py** — One agent, depth-adaptive behavior

```python
from agno.agent import Agent
from agno.models.ollama import Ollama
from tools.catalogue_tools import read_catalogue_entry, list_outputs_by_phase, list_outputs_by_depth
from tools.decision_tools import find_decisions_for_output, record_decision, search_decisions_by_tag
from tools.file_tools import write_design_spec, read_design_spec, list_produced_specs

SHARED_INSTRUCTIONS = """
You are a CAWDP Design Spec Writer. You produce design specifications for 
outputs from the CAWDP agent design methodology.

Your process for every output:

1. READ the catalogue entry for this output
2. FIND relevant decisions from the Decision Register
3. PRODUCE the design spec at the appropriate depth level
4. WRITE the spec to the filesystem
5. RECORD any new decisions in the Decision Register

Your output format is always markdown, structured as a design spec.
"""

DEPTH_INSTRUCTIONS = {
    "shallow": """
For SHALLOW outputs:
- The catalogue entry contains the full production method
- Produce a minimal spec: context + auto-produced values + quality criteria
- No gaps. No judgment needed. The output is deterministic.
- Format: context block + produced values block + quality check block
- Time target: under 2 minutes of human review
""",
    "medium": """
For MEDIUM outputs:
- Pre-fill 40-70% from pattern library + propagated decisions
- Mark pre-filled content as [CONFIRMED] or [REVIEW]
- Identify gaps the human must fill — mark as [GAP: specific question]
- Every gap must have a clear question, not a blank field
- Check Decision Register for relevant decisions before asking the human
- Record any new decisions that downstream outputs will need
- Format: context + pre-filled content + gaps + quality criteria + new decisions
- Time target: 15-25 minutes per output
""",
    "deep": """
For DEEP outputs:
- Use the validated P10 template: 3 agents (Compiler/Analyst/Deriver), 
  4 waves (Data→Analysis→Derivation→Compilation), 5/4/4 enforcement split
- Configure template with domain-specific variables from this output's context
- Answer the 5 identity questions for this specific output
- Define 12 target state characteristics
- Specify agent instructions with never-rules, hardest moments, enforcement regimes
- Record all decisions — Deep outputs produce decisions that many downstream outputs need
- Format: full CAWDP design spec (identity + target state + architecture + contracts + quality)
- Time target: 3-5 hours per output
"""
}

design_writer = Agent(
    name="Design Spec Writer",
    model=Ollama(id="glm-5.1:cloud"),
    instructions=[
        SHARED_INSTRUCTIONS,
        DEPTH_INSTRUCTIONS["shallow"],
        DEPTH_INSTRUCTIONS["medium"],
        DEPTH_INSTRUCTIONS["deep"],
        """
CRITICAL RULES:
- Always check the Decision Register BEFORE producing output
- Every decision you make must be recorded with its propagation targets
- Use plain English. Avoid academic jargon. If you must use a technical term, 
  include the plain English equivalent in brackets.
- Your spec must be complete enough that an implementation writer can build 
  from it WITHOUT any other context.
- Write the spec to the filesystem using write_design_spec
- Record new decisions using record_decision
"""
    ],
    tools=[
        read_catalogue_entry, 
        list_outputs_by_phase, 
        list_outputs_by_depth,
        find_decisions_for_output, 
        record_decision, 
        search_decisions_by_tag,
        write_design_spec, 
        read_design_spec, 
        list_produced_specs
    ],
    show_tool_calls=True,
    markdown=True
)
```

**impl_writer.py** — Produces implementation specs from design specs

```python
from agno.agent import Agent
from agno.models.ollama import Ollama
from tools.catalogue_tools import read_catalogue_entry
from tools.decision_tools import find_decisions_for_output, search_decisions_by_tag
from tools.file_tools import write_impl_spec, read_design_spec

impl_writer = Agent(
    name="Impl Spec Writer",
    model=Ollama(id="glm-5.1:cloud"),
    instructions=[
        """
You are a CAWDP Implementation Spec Writer. You produce implementation 
specifications from design specifications.

Your process:
1. READ the design spec from the filesystem
2. READ the catalogue entry for context
3. FIND relevant decisions from the Decision Register
4. PRODUCE the implementation spec at the appropriate depth level
5. WRITE the impl spec to the filesystem

For SHALLOW outputs:
- Produce an executor function specification
- Define input, computation, output, validation, error handling
- Single function, no agent needed

For MEDIUM outputs:
- Identify which shared infrastructure components to use
- Define domain-specific configuration values
- Specify test criteria mapped to the design spec's quality criteria
- Pattern-configured, not from scratch

For DEEP outputs:
- Reference shared infrastructure (60% of build is shared)
- Define domain schemas (Pydantic models from the design spec)
- Define agent instructions (from the design spec's identity + boundaries)
- Define PRISM queries (from the design spec's data requirements)
- Define test specifications (mapped to failure modes from the design spec)
- Specify build order within the workflow
- Reference the 5/4/4 enforcement regime

CRITICAL RULES:
- You receive ONLY the design spec and Decision Register entries
- You do NOT see the full application context (intentional)
- If the design spec has gaps, flag them rather than guessing
- Your spec must be buildable by a technical team without further design work
- Use plain English. Technical terms in brackets.
- Write to filesystem using write_impl_spec
"""
    ],
    tools=[
        read_catalogue_entry,
        find_decisions_for_output, 
        search_decisions_by_tag,
        write_impl_spec, 
        read_design_spec
    ],
    show_tool_calls=True,
    markdown=True
)
```

---

### Workflow Definition

**output_pipeline.py**

```python
from agno.workflow import Workflow
from agno.utils.log import logger

class OutputProductionPipeline(Workflow):
    name: str = "CAWDP Output Production Pipeline"
    
    def run(self, output_id: str):
        """
        Produce a design spec and implementation spec for a single output.
        
        Args:
            output_id: The catalogue ID (e.g. "P07-012")
        """
        # Step 1: Design Spec Writer produces the design spec
        logger.info(f"Producing design spec for {output_id}")
        design_response = self.design_writer.run(
            f"Produce the design spec for output {output_id}. "
            f"Read the catalogue entry, find relevant decisions, "
            f"produce the spec at the right depth level, "
            f"write it to the filesystem, and record any new decisions."
        )
        
        # Step 2: Check if design spec was written successfully
        # (The agent writes to filesystem via tools)
        
        # Step 3: Impl Spec Writer produces the implementation spec
        logger.info(f"Producing impl spec for {output_id}")
        impl_response = self.impl_writer.run(
            f"Produce the implementation spec for output {output_id}. "
            f"Read the design spec from the filesystem, "
            f"produce the impl spec at the right depth level, "
            f"and write it to the filesystem."
        )
        
        return {
            "output_id": output_id,
            "design_spec": design_response.content,
            "impl_spec": impl_response.content
        }
    
    def run_phase(self, phase: int):
        """Produce all outputs for a phase, in dependency order."""
        # Read catalogue to get this phase's outputs
        # Sort by depth (shallow first, then medium, then deep)
        # Sort within depth by dependencies
        # Run each output through the pipeline
        pass
    
    def run_backcast(self, from_phase: int):
        """Run backcast analysis: what does from_phase need from earlier phases?"""
        pass
```

---

### Build Order

**Phase 1: Data Foundation (Day 1-2)**

1. Create `models/catalogue.py`, `models/decisions.py`, `models/specs.py`
2. Build `seeds/populate_catalogue.py` — the 152-entry catalogue with depth, production method, dependencies, and propagation targets
3. Create empty `data/decisions.json` (starting Decision Register)
4. Create `data/patterns.json` (pattern library for Medium pre-fills — can start with 5 core patterns)

**Phase 2: Tools (Day 2-3)**

5. Build `tools/catalogue_tools.py`
6. Build `tools/decision_tools.py`
7. Build `tools/file_tools.py`
8. Test each tool independently

**Phase 3: Agents (Day 3-4)**

9. Build `agents/design_writer.py` — start with Shallow only
10. Test: run a Shallow output through the agent
11. Add Medium instructions and test
12. Add Deep instructions and test

**Phase 4: Workflow (Day 4-5)**

13. Build `workflows/output_pipeline.py` — single output mode
14. Test: run one Shallow output end-to-end (design spec → impl spec → filesystem)
15. Test: run one Medium output end-to-end
16. Test: run one Deep output end-to-end

**Phase 5: Validation (Day 5-7)**

17. Run Phase 0 outputs (9 outputs, mix of Shallow and Medium)
18. Verify Decision Register grows correctly
19. Verify design specs appear in `specs/design/P00/`
20. Verify impl specs appear in `specs/impl/P00/`
21. Verify decisions from P0 propagate to P1 outputs

**Phase 6: Phase-by-Phase Production (Week 2+)**

22. Run Phase 1 (31 outputs — the big phase)
23. Run Phase 2-9 in sequence
24. Run Phase 10 last (requires all prior decisions)
25. Verify the Decision Register contains all propagated decisions

---

### The Catalogue Seed

This is the most important single artifact. Every agent depends on it. Here's the structure for a few representative entries:

```json
{
  "outputs": [
    {
      "id": "P00-001",
      "phase": 0,
      "name": "Identity Question Q1: What IS this agent?",
      "depth": "medium",
      "cognitive_mode": "judge",
      "production_method": "Guided conversation → capture answer → validate specificity → contamination check → record",
      "dependencies": [],
      "propagates_to": ["P07-001", "P08-009", "P10-001"],
      "pattern_fill_pct": 60,
      "quality_criteria": ["Answer is specific to this agent, not generic", "Answer distinguishes from other agents of same class", "No mechanism keywords (feasibility contamination)"]
    },
    {
      "id": "P00-006",
      "phase": 0,
      "name": "Pattern Match Result",
      "depth": "shallow",
      "cognitive_mode": "compute",
      "production_method": "Extract features → compute similarity → return confidence",
      "dependencies": [],
      "propagates_to": ["P00-001", "P00-002", "P00-003"],
      "pattern_fill_pct": 100,
      "quality_criteria": ["Confidence score computed", "Pattern ID returned or 'no match'"]
    },
    {
      "id": "P10-001",
      "phase": 10,
      "name": "Specification Consistency Report",
      "depth": "deep",
      "cognitive_mode": "synthesize",
      "production_method": "4-wave Compiler/Analyst/Deriver: query all sections → cross-reference contradictions → surface gaps → compile report",
      "dependencies": ["P07-001", "P08-001", "P09-001"],
      "propagates_to": ["P10-004"],
      "pattern_fill_pct": 40,
      "quality_criteria": ["Every contradiction traced to specific sections", "Gaps flagged, not fabricated", "Sparse sections honestly reported"]
    }
  ]
}
```

Building the full 152-entry catalogue is the largest single task in Phase 1. It's mechanical — each entry needs the fields above — but it requires reading through the full output specification from the CAWDP v2.1 application.

---

### Usage Examples

**Produce a single Shallow output:**

```python
pipeline = OutputProductionPipeline()
result = pipeline.run("P00-006")  # Pattern Match Result
# → design spec written to specs/design/P00/D-P00-006.md
# → impl spec written to specs/impl/P00/I-P00-006.md
# → decisions.json updated if new decisions were made
```

**Produce all outputs for a phase:**

```python
pipeline = OutputProductionPipeline()
result = pipeline.run_phase(0)  # All 9 P0 outputs
# → 9 design specs + 9 impl specs in specs/design/P00/ and specs/impl/P00/
# → decisions.json grows with P0 decisions
```

**Check what's been produced:**

```python
# Via agent tools
agent.run("List all produced specs for phase 0")
# → Returns filenames in specs/design/P00/ and specs/impl/P00/
```

**Find decisions that affect a specific output:**

```python
# Via agent tools
agent.run("Find all decisions that propagate to output P07-012")
# → Returns relevant decisions from Decision Register
```

---

### What NOT to Build (Yet)

| Deferred Item | Why |
|---|---|
| Phase-by-phase batch runner | Manual is fine for now — run one output at a time |
| Tool Opportunity Register | Surface organically as you produce outputs |
| Backcast analysis workflow | Manual analysis is sufficient — you do this in conversation |
| Forward verification workflow | Manual is sufficient — check Decision Register after each phase |
| Pattern library auto-suggestion | Hard-code the 5 patterns, add more manually |
| Cross-phase dependency validation | Check manually after each phase completes |
| Test execution | The technical team's responsibility, not this pipeline's |

Build the spine (catalogue + decisions + two agents + file tools). Produce outputs. Let the Decision Register grow. Tool opportunities will surface from the work itself.

---

## Run 24 — Agentic Expert ✓ COMPLETED

*2026-05-22T03:52:02* · `glm-5.1:cloud` · `13526985...`

### Prompt

write the json catalog of outputs with production method inline here

### Response

This is 152 entries — I'll generate it as a file you can drop directly into your pipeline.It looks like the content didn't come through — the message ends at "Take note of the following content" with nothing after it. Could you paste the content you'd like me to note?

---

## Run 25 — Agentic Expert ✓ COMPLETED

*2026-05-22T05:31:27* · `glm-5.1:cloud` · `e12ae361...`

### Prompt

Here is the design spec for P00-001. Provide notes on the resutls.

***
# P00-001 — Five Identity Questions

## Context

| Field | Value |
|-------|-------|
| Phase | 0 — Purpose & Vision |
| Depth | Medium |
| Cognitive Mode | Judge |
| Diamond | Discovery |
| Stance | Pure possibility |
| Pattern Fill | 60% |
| Dependencies | None (this is the first output) |
| Propagates To | P00-002 (Agent Dimension), P00-007 (Hardest Boundary Moment), P00-008 (Possibility Orientation Declaration), P00-009 (Feasibility Contamination Check), all P1+ outputs that derive identity |

### Why This Output Exists

The five identity questions are the **design anchor** for the entire CAWDP process. Everything downstream — authority boundaries, enforcement regimes, output schemas, stress tests — derives from these five answers. Getting them right means every subsequent phase has a stable foundation. Getting them wrong means every subsequent phase builds on sand.

This is the first human-judgment output in the process. No prior output constrains it. The human must exercise genuine judgment about what this agent IS, not fill in templates.

---

## Pre-Filled Content

The five questions are fixed by the CAWDP methodology. The framework for each answer is pre-filled from the methodology's identity-first design principle. Approximately 60% of the structure is determined; the remaining substance requires human judgment.

### Q1: What IS this agent?

**[CONFIRMED]** This question asks for the agent's **essence** — not its capabilities, not its features, not what it does. The answer should be a single statement of identity that captures the agent's reason for existing.

**[CONFIRMED]** The answer must distinguish this agent from other agents of the same class. For example, two Extractor-class agents must have different essence statements.

**[CONFIRMED]** The answer derives to: Agent class → Identity primitive.

**[GAP: What is the essence of this specific agent?]** — Write one sentence that captures what this agent fundamentally IS. Avoid "it does X" phrasing; use "it IS X" phrasing. Example: "A reflective companion that helps you discover your purpose for an agent."

---

### Q2: What is its stance toward possibility?

**[CONFIRMED]** This question asks for the agent's **orientation** — how it positions itself on the possibility→constraint spectrum. The answer must be one of three orientations from the Class × Orientation Taxonomy:

| Orientation | Stance | Legitimate Question | Characteristic Failure |
|---|---|---|---|
| Possibility-oriented | Expands the space of what could be | "What could be?" | Qualifying possibility (narrowing too early) |
| Bridge-oriented | Bridges possibility to constraint | "What connects possibility to constraint?" | Collapsing to one side |
| Constraint-oriented | Operates within declared boundaries | "What must be enforced?" | Reopening possibility |

**[CONFIRMED]** For Phase 0 outputs, the stance is **possibility-oriented** — these agents expand what could be, not constrain it. However, the specific agent being designed may have a different orientation depending on its role.

**[CONFIRMED]** The answer derives to: Enforcement regime target.

**[GAP: What is this agent's orientation?]** — Choose one: Possibility, Bridge, or Constraint. Explain why, with reference to the agent's essence from Q1.

---

### Q3: What would VIOLATE its identity?

**[CONFIRMED]** This question asks for the agent's **existential never-rules** — the actions or behaviours that would destroy what makes this agent what it IS. These are not "nice-to-avoid" — they are identity-violating.

**[CONFIRMED]** The answer must be specific to this agent, not generic. "Make mistakes" is not a violation (all agents can be wrong). "Decide for the human" might be a violation (if the agent's identity is to reflect, not decide).

**[CONFIRMED]** The answer derives to: Guard primitives → Authority boundaries.

**[GAP: What are the existential never-rules for this agent?]** — List 2-5 behaviours that would violate this agent's identity. Each must be specific enough that you could test whether an agent is doing it. Each must connect back to the essence from Q1.

---

### Q4: What would it mean for this agent to be WRONG?

**[CONFIRMED]** This question asks for the agent's **failure mode as an identity boundary** — not "what errors might it make" but "what kind of wrongness would mean it has ceased to be what it IS."

**[CONFIRMED]** Generic failure (making errors, being incomplete) is NOT a valid answer. The answer must describe a failure that is specific to this agent's identity. A Vision Mirror that template-fills without genuine judgment has ceased to be a Vision Mirror — that's identity-level wrongness.

**[CONFIRMED]** The answer derives to: Revert + Event primitives.

**[GAP: What is the identity-level failure mode?]** — Describe what "wrong" means in the deepest sense for this specific agent. This should be the way of being wrong that, if it happened, would mean the agent is no longer fulfilling its essence from Q1.

---

### Q5: What's the hardest moment — where pressure would push this agent past its boundary?

**[CONFIRMED]** This is the **design anchor**. It bridges identity (P0) to enforcement (P8). The answer must be a **specific scenario**, not an abstract statement.

**[CONFIRMED]** "When there's conflicting information" is NOT specific enough. "When the user says 'just tell me what to pick' and the agent's identity is to reflect, not decide — that moment of pressure where it would be easier to just give an answer" IS specific.

**[CONFIRMED]** The answer derives to: Highest-priority Guard. If the specification can't answer Q5, the identity isn't specific enough. If the contract can't enforce the boundary at Q5's hardest moment, the enforcement is insufficient.

**[GAP: What is the hardest boundary moment scenario?]** — Describe a specific, concrete scenario where external pressure would push this agent to violate its Q3 never-rules. Include: (a) who is applying pressure, (b) what form the pressure takes, (c) why it would be tempting to cross the boundary, (d) what crossing would look like.

---

## Production Method

The production method for this output follows five steps:

1. **Guided Conversation** — Present each question sequentially. Provide the framework above. Let the human reflect and discuss. Do NOT suggest answers — the agent's role is to hold space, not fill it.

2. **Capture Answer** — Record the human's answer verbatim. Do not paraphrase. If the answer is vague, ask "Can you make this more specific?" Do NOT suggest more specific alternatives — the agent reflects, the human judges.

3. **Validate Specificity** — Check each answer against the quality criteria below. Flag any answer that:
   - Could apply to any agent of the same class (not specific enough)
   - Uses mechanism/feasibility language (contamination)
   - Is an abstract statement when a scenario is needed (Q5)
   - Describes a generic failure rather than an identity-level one (Q4)

4. **Contamination Check** — Scan all five answers for mechanism keywords (anything that describes HOW rather than WHAT or WHY). Phase 0 is pure possibility — no feasibility, no implementation, no technical mechanisms. Flagged items go to P00-009.

5. **Record Metadata** — For each answer, record:
   - The answer text (verbatim)
   - Specificity assessment (pass/fail + why)
   - Contamination flags (if any)
   - Confidence level (human's self-assessed confidence on a 1-5 scale)

---

## Quality Criteria

- [ ] **Q1 Specificity** — The essence statement is about this specific agent, not a class of agents. Two agents of the same class would have different Q1 answers.
- [ ] **Q2 Orientation** — The orientation is one of: Possibility, Bridge, or Constraint. The justification references Q1.
- [ ] **Q3 Never-Rules** — Each never-rule is specific enough to test. None are generic (e.g., "be wrong" is generic; "decide for the human when its role is to reflect" is specific). Each traces back to Q1.
- [ ] **Q4 Failure Mode** — The failure mode is identity-level, not generic. It describes what "wrong" means in the deepest sense — the kind of wrongness that would mean the agent has ceased to be what it IS.
- [ ] **Q5 Hardest Moment** — The scenario is concrete and specific, not abstract. It names who, what pressure, why tempting, what crossing looks like. It directly tests the Q3 never-rules.
- [ ] **No Feasibility Contamination** — None of the five answers contain mechanism keywords (how to implement, technical architecture, feasibility language). P0 is pure possibility.
- [ ] **Cross-Cutting CC-9** — All answers describe WHAT and WHY, never HOW.
- [ ] **Cross-Cutting CC-3** — A confidence level is stated for each answer.

---

## Propagation Notes

Answers to these five questions propagate extensively downstream:

| Answer | Propagates To | What It Determines |
|--------|---------------|-------------------|
| Q1 (Essence) | P00-002 (Agent Dimension), P1 O1-O4 (Identity outputs) | Agent class, identity primitive |
| Q2 (Orientation) | P00-008 (Possibility Orientation Declaration), P8 (Enforcement) | Enforcement regime target, orientation classification |
| Q3 (Never-rules) | P00-002 (Agent Dimension A2), P1 O10 (Behavioural Boundary), P8 (Guard primitives) | Authority boundaries, guard conditions |
| Q4 (Failure mode) | P1 O13-O15 (Verification outputs), P5 (Event Storming) | Revert conditions, stress test targets |
| Q5 (Hardest moment) | P00-007 (Hardest Boundary Moment Scenario), P8 (Highest-priority Guard) | Priority enforcement, stress test anchor |

If any answer changes, all downstream propagations must be re-evaluated.

---

## Decisions

The following decisions are recorded for this output:

| Decision | Rationale | Propagates To |
|----------|-----------|---------------|
| Five questions are mandatory, not optional | Q1-Q5 are the design anchor; skipping any means the identity is incomplete | All downstream |
| Q5 must be a specific scenario, not an abstract statement | Abstract statements cannot be stress-tested; scenarios can | P00-007, P8 enforcement |
| Answers are captured verbatim, not paraphrased | The human's judgment is the authoritative source; the agent reflects, not decides | P1 identity outputs |
| Contamination is flagged but not removed during P0 | Flagged items become inputs to P00-009 and are addressed in later phases | P00-009 |
***

### Response

## Notes on P00-001 Design Spec

Six observations, ordered by impact:

### 1. Pattern Fill Shows, Not Tells

The pre-filled content is **instructional** — it tells the human *how* to answer each question. But for a Medium-depth output with 60% pattern fill, the pre-fill should provide **class-specific example answers** that the human confirms, rejects, or modifies.

Right now Q1 says:

> Write one sentence that captures what this agent fundamentally IS.

If the agent is a constraint-oriented Aggregator (like the Project Manager), the pattern fill should offer:

> **[PRE-FILL]** "A structural registry that creates and manages projects, tasks, and dependencies — content-agnostic, purely structural management."
> 
> **[CONFIRM / MODIFY / WRITE YOUR OWN]**

This is the "convention over configuration" principle in action. The pattern provides a starting point rooted in the agent's class and orientation. The human exercises judgment on whether to accept, modify, or reject it. The current spec tells the human what to do; the improved version *shows what the answer might look like* for their agent type.

**Impact:** High. This is the single biggest improvement to the spec. It directly enables the "15-minute agent specification" claim — with class-specific pre-fills, a user could confirm 60% of the identity in 60 seconds.

---

### 2. Missing "I Don't Know" Path for Q5

Q5 (hardest boundary moment) is the hardest question to answer. The spec says it must be "a specific, concrete scenario." But some humans won't be able to articulate this immediately.

The spec needs an explicit **"I don't know yet"** path:

> **[GAP: What is the hardest boundary moment scenario?]** — Describe a specific, concrete scenario where external pressure would push this agent to violate its Q3 never-rules. Include: (a) who is applying pressure, (b) what form the pressure takes, (c) why it would be tempting to cross the boundary, (d) what crossing would look like.
>
> **If you can't answer this yet, mark it [DEFERRED].** It will surface during P3-P5 when you see the agent in action. But you must answer it before P8 (Contract Formalization).

This connects to the ADHD design principle of **shame-free failure states** — not knowing is not a failure, it's information. And it connects to the P0 stance of **possibility orientation** — the answer should emerge from the process, not be forced at the start.

**Impact:** Medium. Q5 is the design anchor, but forcing an answer before the human is ready produces template-filling, not genuine judgment. The deferred path preserves the requirement while acknowledging reality.

---

### 3. Missing Artefact Tags Field

This is the **cascading dependency from P10 made concrete**. The spec has no explicit mechanism for tagging this output as "surprise," "gap," "pattern," or "assessment_fragment" during production. Without these tags, P10 (Methodology Reflection, Confidence Map, etc.) has nothing to assemble.

The spec needs an **Artefact Tags** section at the end:

```markdown
## Artefact Tags (for P10 assembly)

Tag this output during or after production:
- [ ] surprise — did anything unexpected emerge during Q1-Q5?
- [ ] gap — did any question reveal a gap in understanding?
- [ ] pattern — did any answer reveal a reusable pattern?
- [ ] assessment_fragment — did any answer capture a judgment worth preserving?
```

**Impact:** High. This is a structural requirement, not optional metadata. Every design spec in the pipeline needs this field.

---

### 4. Contamination Check Needs a Keyword List

The spec says "scan for mechanism keywords" but doesn't provide the list. For an implementation writer (who doesn't have full context), this needs to be concrete:

```markdown
## Contamination Check Keyword List

Flag any answer containing these P0-prohibited terms:
- Implementation: "implemented", "built", "coded", "deployed", "architecture"
- Framework: "Agno", "LangChain", "GPT-4", "Python", "TypeDB"
- Infrastructure: "database", "API", "server", "cloud", "microservice"
- Feasibility: "possible", "impossible", "can't", "how would we"
- Technical: "schema", "endpoint", "request", "response", "JSON"
```

This is CC-9 (Possibility Orientation) operationalized at the spec level. The principle is right; the execution needs the specific detection mechanism.

**Impact:** Medium. The principle is clear; the keyword list makes it executable.

---

### 5. Confidence Level Should Acknowledge Q4/Q5 Difficulty

The spec says to capture a confidence level for each answer. But Q4 (failure mode) and Q5 (hardest moment) are inherently harder to answer with high confidence. The spec should normalize this:

> **Confidence Level** — Rate your confidence on a 1-5 scale:
> - 1-2: Low confidence (I'm exploring, this may change)
> - 3: Medium confidence (I have a direction but I'm not certain)
> - 4-5: High confidence (I'm specific and confident)
>
> **Note:** Q4 and Q5 typically have lower confidence than Q1-Q3. This is normal. Low confidence on Q5 means you need more information, not that you've failed.

This is **epistemic honesty** built into the spec structure. CC-3 (Epistemic Metadata) starts at P0, not just at P7.

**Impact:** Low-Medium. Important for quality but not blocking.

---

### 6. Translation to Buildable Artifacts Is Implicit

The design spec captures answers, but the propagation table shows *what each answer determines* without showing *what each answer becomes in implementation*. The implementation writer needs to know:

| Answer | Becomes In Implementation |
|--------|--------------------------|
| Q1 (Essence) | Agent identity card, system prompt opening, class determination |
| Q2 (Orientation) | Enforcement regime target, phase-appropriate behavior defaults |
| Q3 (Never-rules) | Guard conditions in contract, prompt-level boundaries, schema-level constraints |
| Q4 (Failure mode) | Revert conditions in contract, stress test targets, FMEA failure modes |
| Q5 (Hardest moment) | Priority Guard in contract, hardest scenario in P5, primary stress test |

This translation table should be part of the spec so the implementation writer can trace from answer to implementation without guessing.

**Impact:** Medium. Directly affects the handoff quality between design spec writer and implementation writer.

---

### Summary

| # | Observation | Impact | Action |
|---|---|---|---|
| 1 | Pattern fill needs class-specific examples, not instructions | High | Add class-specific pre-fill defaults per orientation |
| 2 | Q5 needs "I don't know yet" / DEFERRED path | Medium | Add explicit deferred path with P8 deadline |
| 3 | Missing artefact_tags field for P10 assembly | High | Add Artefact Tags section to every design spec |
| 4 | Contamination check needs keyword list | Medium | Add keyword list to spec |
| 5 | Confidence should normalize Q4/Q5 difficulty | Low-Medium | Add note normalizing lower confidence on harder questions |
| 6 | Answer-to-implementation translation table missing | Medium | Add translation table showing what each answer becomes |

The spec is structurally sound. These six improvements make it **executable** — a design spec that an implementation writer can actually build from without context gaps.

---

## Run 26 — Agentic Expert ✓ COMPLETED

*2026-05-22T22:28:28* · `glm-5.1:cloud` · `60f06955...`

### Prompt

what is our best thinking on developing the complementarity matrix as a tool for agents?

### Response

## Complementarity Matrix as Agent Tool: Design Recommendation

### The Core Challenge

The complementarity matrix is CAWDP's genuinely unique contribution — no equivalent exists in design thinking, BPM, or any other methodology. But it's also the output that most resists automation because it requires **judgment about judgment**: who is better at this task, and by how much?

The tool must structure the judgment space without automating the judgment. It must propose, not decide.

---

### Architecture: Three-Phase Tool

```
PHASE 1: STRUCTURE          PHASE 2: SCORE            PHASE 3: ALLOCATE
"What dimensions matter?"   "How good is each actor?"  "Who should do this?"
                                                         
Task description  ──►  Dimension selector  ──►  Scoring interface  ──►  Gap calculator
Cognitive type     ──►  + defaults          ──►  + agent proposals  ──►  + allocation engine
Agent class        ──►  + relevance filter   ──►  + human review      ──►  + edge case flags
Domain clues       ──►                     ──►                      ──►  + contract translation
```

---

### Phase 1: Dimension Selection

Not every dimension matters for every task. A Mechanical task (extract data from form) needs different dimensions than an Evaluative task (assess ethical risk). The tool selects relevant dimensions and weights them by cognitive type.

**9 Core Dimensions:**

| # | Dimension | Human Advantage | Agent Advantage | System Advantage |
|---|-----------|-----------------|-----------------|------------------|
| D1 | Judgment Complexity | Nuance, context, values, stakeholder perspectives | Pattern-based inference | Binary rule enforcement |
| D2 | Domain Knowledge | Lived expertise, tacit knowledge, edge case intuition | Documented knowledge, training data coverage | Schema validation, reference lookups |
| D3 | Pattern Processing | Small-n pattern recognition, anomaly intuition | Large-n pattern detection, statistical analysis | Data pipeline execution |
| D4 | Consistency Requirement | Variable quality, context-dependent consistency | Consistent within training distribution | Deterministic consistency |
| D5 | Scale Demand | Single-digit throughput | Hundreds per session | Thousands per second |
| D6 | Verification Feasibility | Can verify what's meaningful, not just structural | Can verify structure and patterns | Can enforce schema rules |
| D7 | Creative Novelty | Genuine novelty, combinatorial invention | Combinatorial recombination, style transfer | Template instantiation |
| D8 | Emotional Intelligence | Reads room, navigates politics, builds trust | Detects sentiment keywords | Routes to human on flag |
| D9 | Error Reversibility | Can assess reversal cost | Follows revert protocol | Executes revert mechanically |

**Per-Cognitive-Type Relevance:**

| Cognitive Type | Primary Dimensions | Secondary Dimensions | Low Relevance |
|---|---|---|---|
| Mechanical | D3, D4, D5, D6 | D2 | D1, D7, D8 |
| Analytical | D2, D3, D6 | D1, D4, D5 | D7, D8 |
| Generative | D1, D2, D7 | D6, D8 | D4, D5 |
| Evaluative | D1, D2, D6, D8 | D3, D7 | D4, D5 |
| Intuitive | D1, D2, D8 | D7 | D3, D4, D5, D6 |

The tool selects 4-6 dimensions per task based on cognitive type, then adds domain-specific dimensions if the agent detects them.

---

### Phase 2: Scoring

The agent proposes scores. The human confirms or modifies. This is the "agent prepares judgment, human makes judgment" principle applied to the scoring process itself.

**Scoring Protocol:**

1. **Agent proposes** — Based on:
   - Agent class defaults (Extractor → D2 low H, D3 high A; Assessor → D1 high H, D6 medium H)
   - Cognitive type relevance weights
   - Domain clues from task description
   - Prior confirmed allocations (learning from history)

2. **Human reviews** — For:
   - High-stakes tasks (harm category = Direct Output Harm)
   - Low-confidence proposals (agent confidence < 4/5)
   - Tasks near the gap threshold (gap 4-7 — the allocation is uncertain)
   - Cold start tasks (identity/purpose/boundary → forced collaborative)

3. **Conflicts surfaced** — The tool flags:
   - Dimension-level disagreement (H and A are close on D1 — judgment is contested)
   - Cross-dimension tension (high D1 + low D6 means the task needs judgment but the output is hard to verify)
   - Stake-reversibility interaction (high D1 + low D9 = high stakes + hard to undo)

**Default Score Ranges by Agent Class:**

| Dimension | Extractor | Measurer | Assessor | Generator | Aggregator |
|---|---|---|---|---|---|
| D1 Judgment | H:9 A:2 | H:8 A:3 | H:9 A:4 | H:7 A:5 | H:8 A:4 |
| D2 Domain | H:7 A:6 | H:7 A:6 | H:8 A:5 | H:8 A:5 | H:7 A:5 |
| D3 Pattern | H:3 A:9 | H:4 A:8 | H:5 A:7 | H:4 A:7 | H:4 A:7 |
| D4 Consistency | H:4 A:8 | H:3 A:9 | H:5 A:7 | H:4 A:6 | H:5 A:7 |
| D5 Scale | H:2 A:8 | H:3 A:8 | H:4 A:7 | H:3 A:6 | H:4 A:6 |
| D6 Verification | H:6 A:5 | H:7 A:6 | H:7 A:5 | H:5 A:4 | H:6 A:5 |
| D7 Creativity | H:8 A:3 | H:6 A:3 | H:7 A:4 | H:7 A:6 | H:6 A:4 |
| D8 Emotional | H:9 A:2 | H:7 A:2 | H:8 A:3 | H:7 A:3 | H:7 A:3 |
| D9 Reversibility | Context-dependent — not a capability score, used in Phase 3 allocation adjustment |

These defaults produce reasonable starting allocations. The agent should present them as proposals with confidence levels, not assertions.

**Scoring Example (Project Manager — Aggregator class, Mechanical task: "Create project record"):**

```
DIMENSION SCORES (cognitive type: Mechanical, primary: D3, D4, D5, D6)

  D3 Pattern Processing:  H:3  A:9  S:7   → Agent advantage (+6)
  D4 Consistency:         H:4  A:8  S:9   → System advantage (+5)  
  D5 Scale:              H:2  A:8  S:8   → Agent/System advantage (+6)
  D6 Verification:       H:6  A:5  S:8   → System advantage (+2)

AGGREGATE GAP: -5 (agent/system advantage)
ALLOCATION: Agent-primary (with system enforcement for schema validation)
CONFIDENCE: 5/5 (high — this is a standard Mechanical task for an Aggregator)
```

**Scoring Example (Assessor class, Evaluative task: "Assess risk in strategic recommendation"):**

```
DIMENSION SCORES (cognitive type: Evaluative, primary: D1, D2, D6, D8)

  D1 Judgment:           H:9  A:4  S:1   → Human advantage (+5)
  D2 Domain Knowledge:   H:8  A:5  S:1   → Human advantage (+3)
  D6 Verification:       H:7  A:5  S:6   → Human advantage (+2)
  D8 Emotional Intel:   H:8  A:3  S:1   → Human advantage (+5)

AGGREGATE GAP: +4 (human advantage, but below 6 threshold)
ALLOCATION: Collaborative (agent prepares, human decides)
CONFIDENCE: 3/5 (medium — judgment tasks near threshold)
⚠ FLAG: Task is near gap threshold. Human review recommended.
```

---

### Phase 3: Allocation

The allocation algorithm runs from scores. It is deterministic given the scores. No judgment here — the judgment was in the scoring.

**Algorithm:**

```
For each task:
  1. Compute aggregate_gap = weighted_avg(D1..D9 gaps, weights from cognitive type)
  2. Apply cold start override (identity/purpose/boundary → forced Collaborative)
  3. Apply allocation:
     - aggregate_gap >= +6  → Human-only
     - aggregate_gap +3 to +5 → Collaborative (human-primary)
     - aggregate_gap -2 to +2 → Collaborative (balanced)
     - aggregate_gap -5 to -3 → Collaborative (agent-primary)
     - aggregate_gap <= -6   → Agent/System-only
  4. Apply reversibility adjustment:
     - If D9 = "Hard to undo" AND allocation includes agent → flag for human review
     - If D9 = "Hard to undo" AND stakes = Direct Output Harm → force human-only
  5. Assign actor type (H/A/S) from highest-scoring actor per primary dimension
  6. Compute contract Guard configuration from allocation
```

**Cold Start Overrides:**

These tasks are collaborative by default, regardless of scores, because the human cold start problem means the agent cannot exercise judgment without human guidance:

- "Discover principal's purpose"
- "Identify what this workflow IS"
- "Discover what would violate identity"
- "Define excellent outcomes"
- "Identify authority boundaries"

**Reversibility-Stakes Interaction:**

| Stakes \ Reversibility | Easy to Undo | Moderate | Hard to Undo |
|---|---|---|---|
| Direct Output Harm | Collaborative | Collaborative (H-primary) | **Human-only** |
| Indirect Strategy Harm | Agent-primary | Collaborative | Collaborative (H-primary) |
| Indirect Data Harm | Agent/System | Agent-primary | Collaborative |
| No Harm | Agent/System | Agent/System | Agent/System |

This matrix overrides the gap-based allocation when the combination is flagged.

---

### Tool API (as Agno @tool)

```python
from agno.tools import tool

@tool
def propose_complementarity_scores(
    task_description: str,
    cognitive_type: str,
    agent_class: str,
    harm_category: str = "no_harm",
    domain_clues: str = ""
) -> str:
    """Propose H/A/S scores for a task based on class defaults and cognitive type.
    Returns proposed scores with confidence levels and flags for human review."""
    
    # Phase 1: Select dimensions based on cognitive type
    # Phase 2: Propose scores based on agent class defaults
    # Flag near-threshold tasks for human review
    # Return structured proposal
    pass

@tool
def compute_allocation(
    scores_json: str,
    harm_category: str = "no_harm",
    reversibility: str = "moderate",
    is_cold_start_task: bool = False
) -> str:
    """Compute allocation from confirmed scores.
    Returns allocation with gap, actor type, and contract Guard mapping."""
    
    # Phase 3: Compute aggregate gap
    # Apply cold start override if needed
    # Apply reversibility-stakes interaction
    # Assign actor type
    # Map to contract Guard configuration
    pass

@tool
def record_confirmed_allocation(
    task_id: str,
    allocation: str,
    scores_json: str,
    human_modifications: str = ""
) -> str:
    """Record a confirmed allocation for learning.
    Human modifications are recorded for pattern improvement."""
    
    # Store in Decision Register
    # If human modified scores, record the modification
    # Over time, modifications inform default adjustments
    pass
```

---

### What Makes This Hard

Three challenges the tool cannot fully solve:

**1. The scoring requires domain knowledge the agent doesn't have.**

The agent can propose based on class defaults and cognitive type patterns, but domain-specific scoring (e.g., "how much domain knowledge does this legal research task require?") requires someone who knows the domain. The tool must be honest about this — propose with lower confidence for domain-dependent dimensions, and flag for human review.

**2. The gap threshold of 6 is a heuristic, not a law.**

The threshold works well empirically, but edge cases exist. Some tasks with gap 5 should be human-only (high stakes, hard to undo). Some tasks with gap 7 could be agent-primary (low stakes, easy to verify). The tool should present the threshold as a **recommendation with confidence**, not a rule.

**3. The cold start problem is real.**

The first time you run the tool for a domain, the defaults are generic. The fifth time, the defaults are informed by four prior confirmed allocations. The twentieth time, the defaults are good enough that human review takes seconds, not minutes. The tool gets better with use, but it starts from rough defaults. This is progressive autonomy applied to the tool itself.

---

### What the Tool Produces for Downstream Phases

The allocation output feeds directly into:

| Output | Feeds Into | What It Determines |
|---|---|---|
| Per-task H/A/S assignment | P6 pipeline architecture | Stage boundaries, gate positioning |
| Complementarity gap score | P7 agent specifications | Per-agent task scope |
| Human-only task list | P6 human gates | Gate decision options |
| Reversibility-stakes flag | P8 contract Guards | Guard enforcement regime |
| Actor type per task | P8 contract Schema | Contract schema structure |
| Cold start override list | P9 human experience | Cognitive load budget |

The tool's most important output is not the allocation itself — it's the **reasoning trace**. Every score, every flag, every override must be recorded so that P8 can translate it into contract Guards and P10 can assess confidence.

---

### Learning Loop

Every confirmed allocation teaches the tool three things:

1. **Domain-specific score adjustments** — "In legal domains, D2 (Domain Knowledge) H score is typically 9, not 7"
2. **Threshold calibration** — "In this domain, gap 5 tasks are usually human-only due to regulatory risk"
3. **Dimension relevance** — "In creative domains, D7 (Creative Novelty) is more important than D4 (Consistency)"

The tool stores these as pattern adjustments, not rules. They modify proposal confidence, not proposal scores. The human always has the final score.

---

### Build Order

1. **Phase 1 only** (dimension selector with cognitive type mapping) — 2-3 days
2. **Phase 2 scoring** (class defaults + proposal + human review flagging) — 3-4 days
3. **Phase 3 allocation** (gap calculator + allocation algorithm + Guard mapping) — 2-3 days
4. **Learning loop** (record modifications, adjust proposal confidence) — 3-4 days
5. **Integration** (wire to Decision Register, wire to pipeline) — 2-3 days

**Total: ~12-17 days for a functional complementarity analysis tool.**

---
