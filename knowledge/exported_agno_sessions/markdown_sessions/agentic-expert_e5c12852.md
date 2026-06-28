# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `e5c12852...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-21T10:22:35 |
| **Runs** | 9 completed / 10 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-21T10:22:35* · `glm-5.1:cloud` · `b14a0296...`

### Prompt

We are building a platform that delivers the CAWDP framework to help users design high performing agentic workflows. 

Consider the following output from a CAWDP process that is designed to produce a methodology reflection artefact.

This is essentially your design spec and we now need to understand what is needed to implement this. 
Let's not jump straight to code or solutions. 

We can see this as another opportunity to apply CAWDP, this time with the goal of delivering an implementation plan from the provided design spec. 

As a first step, give me a vision for a perfectly executed workflow that outputs an excellent implementation plan.

What needs to be true about the implementation plan for it to be considered excellent?

***
# CAWDP Application Phase 10.11: Methodology Reflection Workflow

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
***

### Response

# P0: Purpose & Vision — Implementation Plan for Methodology Reflection Workflow

---

## The 5 Identity Questions

**Q1: What IS an excellent implementation plan?**

A traceable, ordered, complete blueprint that takes the Methodology Reflection design specification and produces everything a developer needs to build it — no guessing, no gaps, no ambiguity — while preserving every design constraint in concrete implementation choices.

**Q2: What is its stance toward possibility?**

Constraint-oriented. The design spec IS the possibility space. The implementation plan operates within those boundaries, translating design constraints into enforceable code, not imagining new features or softening constraints for convenience.

**Q3: What would VIOLATE its identity?**

- Adding features not in the design spec
- Softening design constraints in implementation ("we'll just put that in the prompt" instead of structural enforcement)
- Leaving "implement the analyst agent" as a task without specifying what that means concretely
- Pretending uncertainty doesn't exist — hiding hard decisions behind vague language
- Building infrastructure that duplicates what already exists (SurrealDB schema, writer module)

**Q4: What would make it WRONG?**

- Vagueness that forces developers to guess what the design intends
- Wrong build order that creates rework or blocks progress
- Missing the cascading dependency — PRISM data must exist and be populated before agents can query it
- Enforcing constraints at the wrong regime (prompt-only for what should be schema-enforced)
- Building disconnected from existing infrastructure (SurrealDB schema, db/writer.py, orchestrator pattern)

**Q5: What's the hardest moment?**

When the design says "Analyst never interprets beyond data" and the implementation has to decide: is this Regime 1 (declare in prompt), Regime 2 (detect in output audit), or Regime 3 (prevent structurally)? The hardest moment is translating design intent into enforcement regime — and being honest about what can't be enforced structurally.

---

## Target State Vision

What needs to be true about the implementation plan for it to be considered excellent?

### R1: Traceable — every implementation choice traces to a design spec requirement

A developer can follow any line of code, any schema definition, any agent instruction back to the specific P1-P8 specification that motivated it. No implementation choice appears without a "because." This goes both ways: every design constraint has a corresponding implementation mechanism, and every implementation choice has a design constraint it serves.

This eliminates the "why did we build it this way?" question. The answer is always: "Because P7 specifies this authority boundary" or "Because FM3 requires this detection mechanism."

### R2: Complete — a developer can build the entire workflow without external references

Every schema field, every agent instruction, every tool definition, every API route, every test case is specified. No task says "implement the analyst agent" without saying what that means: which tools, which instructions, which output schema, which authority boundaries, which null states, which never-rules, which progressive autonomy dimensions, which cost budget.

The plan is the single source of truth for the build. If a developer needs to look elsewhere for "how should this work," the plan has failed.

### R3: Ordered — build sequence is explicit with dependencies marked

The plan doesn't present a flat list of tasks. It presents a build order with clear dependency arrows. PRISM schemas before agent instructions. Data queries before data processing. Processing agents before compilation agents. Tests alongside the code they test.

The 4-wave architecture from the design spec (Data → Analysis → Derivation → Compilation) maps directly to build order. But there are prerequisites the design spec assumes: the SurrealDB schema must exist, the writer module must exist, the orchestrator architecture must be in place.

### R4: Typed — different artifact types are distinguished

The plan doesn't treat everything as "code." It distinguishes:
- **Database artifacts** — SurrealDB table definitions, indexes, seed data, queries
- **Agent artifacts** — instructions, output schemas, authority boundary specifications, progressive autonomy configurations
- **Tool artifacts** — Agno @tool definitions, what each tool does, what it returns, what it enforces
- **Integration artifacts** — how agents connect to PRISM, how the writer module enforces business rules, how data flows between waves
- **Test artifacts** — what to test, how to test, what "done" looks like for each test
- **Documentation artifacts** — how each constraint is enforced, what's Regime 1/2/3, what to tell the developer vs what to enforce structurally

### R5: Constraint-preserving — every "never" rule has a concrete enforcement mechanism

The design spec has 5 Regime 3 enforcement points and 4 unenforceable elements in Regime 1-2. The implementation plan maps each constraint to its enforcement regime and the specific mechanism:

| Constraint | Regime | Mechanism |
|---|---|---|
| Compiler never adds content | 3 (Prevent) | Output schema validation — every field must trace to PRISM data or processing step |
| Analyst never interprets beyond data | 2 (Detect) | Correlation strength field required + output audit for conclusion language |
| Deriver never recommends without trace | 3 (Prevent) | traces_to field required in schema, orphan recommendations auto-removed |
| No fabrication | 3 (Prevent) | Sparse flagging mandatory, zero-tolerance for claims without artefact ID |
| Type separation | 3 (Prevent) | Schema enforces deterministic/probabilistic/elicited distinction |
| "Never assemble flattering narratives" | 2 (Detect) | Tone-agnostic schema (facts only), output audit |
| "Never invent patterns" | 2 (Detect) | Formalisation status field, evidence strength field, minimum 1 artefact trace |
| Honesty in sparse data | 1 (Declare) | Completeness percentage is deterministic (Regime 3), but the *choice* to flag it honestly is declared in prompt |

If a constraint can be enforced structurally (schema, database constraint, type system), it is. If it can only be detected (output audit), that's honest. If it can only be declared (prompt instruction), that's honest too.

### R6: Connected — data flow is explicit and end-to-end traceable

You can trace a data point from its source (PRISM query) through every processing step (Analyst variance calculation, Deriver recommendation derivation) to its destination (O8 field in the final document). No data appears in the output without a provenance chain.

This also means the plan shows how agents connect to each other: Compiler receives processed outputs from Analyst and Deriver, Deriver receives processed data from Compiler and analysis from Analyst, Analyst receives raw data from System queries.

### R7: Honest — about effort, uncertainty, deferrable vs essential, hard vs easy

Every task has a rough effort estimate. Every task is marked essential or deferrable. Every "hard" decision is flagged with the tradeoff, not hidden. The plan doesn't pretend that "enforce Analyst never-rules" is straightforward — it says: "This is Regime 2 (Detect), which means output audit + schema enforcement, and here's how to implement the audit."

### R8: Testable — every implementation choice has a corresponding test

The design spec identifies 9 failure modes (FM1-FM9) with RPN scores. The implementation plan maps each to a test:
- FM1 (fabrication) → schema validation test: can the Compiler produce a claim without an artefact ID?
- FM3 (false correlation) → output audit test: does the Analyst output contain conclusion language?
- FM6 (sparse data as comprehensive) → completeness calculation test: does a section with 30% data get flagged as sparse?
- FM9 (no surprises as success) → empty result set test: does O3 correctly document "no captured surprises" as a finding?

### R9: Infrastructure-aware — builds on what exists, specifies what's new

The plan knows that:
- The SurrealDB schema (design_ tables) already exists for P0-P9 data
- The db/writer.py module (CAWDP-aware persistence) already exists as a pattern
- The orchestrator architecture (3-layer: writer → tools → agent) already exists
- The project_manager private schema pattern exists as a Regime 3 enforcement pattern

The plan specifies what already exists and what needs to be built. It doesn't duplicate infrastructure.

### R10: Progressive — supports the progressive autonomy deployment model

The plan shows how to deploy the workflow at Shadow level first (human checks everything), then advance through Advisory/Supervised/Autonomous with clear criteria from P10:
- Compiler: ≥10 compilations with ≤1 error → advance
- Analyst: ≥10 analyses with ≤2 incorrect flaggings → advance
- Deriver: ≥10 derivations with ≤1 untraced recommendation → advance

The implementation includes logging and metrics that make these promotion criteria measurable.

### R11: Enforcement-explicit — for every "never" rule, the plan states which regime and which mechanism

This is the design-to-enforcement bridge. The implementation plan is the P8 (Contract Formalization) of the build process — it takes design intent and produces enforceable contracts (code). Every never-rule, every authority boundary, every verification requirement has a concrete mechanism attached.

### R12: Epistemic-aware — the plan preserves the type distinction in implementation

The design spec has three epistemic profiles: Deterministic (computed from PRISM data), Probabilistic (agent-assessed with judgment), and Elicited (captured from humans during P0-P9). These are not interchangeable. The implementation preserves this distinction:
- Deterministic fields are computed, never assessed
- Probabilistic fields carry confidence metadata
- Elicited fields carry provenance metadata (who captured it, when, in which phase)

The schema enforces this through type definitions. A `variance` field is computed (deterministic). A `significance_assessment` field is assessed (probabilistic, with confidence). A `surprise_description` field is elicited (with provenance).

---

## Key Design Insight

The implementation plan is itself a CAWDP artifact — it's the **P8 (Contract Formalization)** of the build process. It takes design intent (P0-P9 specification) and produces enforceable contracts (code, schemas, tests, deployment procedures). The same principle applies: every design constraint maps to an enforcement mechanism, and unenforceable elements are honestly documented.

The cascading dependency that the design spec identified — **if P0-P9 don't capture artefacts with tags, P10 has nothing to assemble** — has an implementation equivalent: **if the SurrealDB schema doesn't have artefact_tags on design_artefacts, the agents can't query for them.** The data model IS the pipeline. The schema IS the contract.

---

## What This P0 Enables

This target state vision sets up the rest of the CAWDP application:

- **P1 (Output Specification)** — what artefacts does the implementation plan produce? (schemas, agent configs, tool definitions, test specs, deployment procedures, enforcement mappings)
- **P2 (Backcasting)** — working backward from "a developer can build the whole workflow" to what inputs are needed
- **P3 (Task Decomposition)** — what are the actual build tasks, in what order, with what dependencies?
- **P4 (Capability Allocation)** — what's System (schema generation, query templates), what's Agent-primary (instruction writing, test design), what's Human-primary (review, validation decisions)?
- **P5 (Event Storming)** — what can go wrong in the build process? What if the SurrealDB schema changes? What if an agent instruction doesn't enforce the constraint?
- **P6 (System Architecture)** — how do the build artifacts connect? What's the data flow from schema → agent → tool → output?
- **P7 (Agent Design)** — if we need build agents, what are their authority boundaries? (But more likely: the human implementer is the "agent" here, with tools and templates as System enforcement)
- **P8 (Contract Formalization)** — what are the build contracts? What counts as "done" for each task?
- **P9 (Human Experience)** — what does the developer experience look like? How do they know what to build next?
- **P10 (Validation)** — how do we test that the implementation actually enforces the design constraints?

Shall I proceed to P1 (Output Specification) — defining the specific artefacts the implementation plan must produce?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-21T10:26:07* · `glm-5.1:cloud` · `68e7fc6a...`

### Prompt

perform the remaining CAWDP phases based on your excellent P0 output.

### Response

# Implementation Plan: Methodology Reflection Workflow

## Complete CAWDP Phases P1–P10

---

## P1: Output Specification

### O1: PRISM Query Templates

*Purpose: Reusable SurrealDB queries that extract P0-P9 data for Methodology Reflection processing*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| query_id | string | ✅ | Deterministic |
| query_name | string | ✅ | Deterministic |
| purpose | string | ✅ | Deterministic |
| surql | string | ✅ | Deterministic |
| parameters | list | ✅ | Deterministic |
| expected_fields | list | ✅ | Deterministic |
| null_handling | string | ✅ | Deterministic |
| epistemic_types | list | ✅ | Deterministic — which epistemic profiles the returned data carries |
| wave | enum: Data/Analysis/Derivation/Compilation | ✅ | Deterministic |

**Dependencies:** design_phase_transitions, design_quality_gates, design_artefacts (with artefact_tags), design_workflows, design_agent_specifications, design_tasks

**Quality Gate:** Every query returns expected fields or explicit null handling. Every query is idempotent. Every query tagged with its wave.

---

### O2: Pydantic Output Schemas

*Purpose: Typed schemas for O1-O8 from the design spec, enforcing Regime 3 type separation*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| schema_name | string | ✅ | Deterministic |
| schema_purpose | string | ✅ | Deterministic |
| fields | list[SchemaField] | ✅ | Deterministic |
| epistemic_profile_map | dict | ✅ | Deterministic — maps each field to its epistemic profile (deterministic/probabilistic/elicited) |
| validation_rules | list | ✅ | Deterministic — which fields are required, which are conditional |
| traces_to | string | ✅ | Deterministic — which design spec output this implements |
| null_state | string | ✅ | Deterministic — what the schema produces when data is absent |

**SchemaField sub-model:**

| Field | Type | Required |
|---|---|---|
| name | string | ✅ |
| type | string | ✅ |
| required | boolean | ✅ |
| epistemic_profile | enum: deterministic/probabilistic/elicited | ✅ |
| traces_to_artefact | string | ✅ — which PRISM query or processing step produces this field |
| validation | string | ⚠️ — validation rule if applicable |
| null_handling | string | ✅ — what happens when data is missing |

**Dependencies:** Design spec P1 output schemas (O1-O8)

**Quality Gate:** Every field has an epistemic profile. Every field traces to a data source or processing step. Null state defined for every schema. Validation rules match design spec quality gates.

---

### O3: Agent Instruction Specifications

*Purpose: Complete instructions for each of the 3 agents, enforcing authority boundaries*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| agent_name | string | ✅ | Deterministic |
| agent_class | enum: Aggregator/Measurer+Assessor/Generator | ✅ | Deterministic |
| agent_orientation | enum: constraint/bridge/constraint | ✅ | Deterministic |
| identity_statement | string | ✅ | Deterministic |
| mission | string | ✅ | Deterministic |
| never_rules | list[string] | ✅ | Deterministic |
| hardest_boundary_moment | string | ✅ | Deterministic |
| null_state | string | ✅ | Deterministic |
| epistemic_profile | enum: deterministic/probabilistic/probabilistic | ✅ | Deterministic — what kind of judgment this agent exercises |
| harm_assessment | string | ✅ | Deterministic |
| input_schemas | list[string] | ✅ | Deterministic — which Pydantic schemas this agent receives |
| output_schemas | list[string] | ✅ | Deterministic — which Pydantic schemas this agent produces |
| progressive_autonomy_dimensions | list[AutonomyDimension] | ✅ | Deterministic |
| cost_budget_tokens | int | ✅ | Deterministic |
| specification_aging_cadence | string | ✅ | Deterministic |
| enforcement_regime_map | dict | ✅ | Deterministic — maps each never-rule to its Regime 1/2/3 enforcement |
| verification_protocol | string | ✅ | Deterministic — how this agent's output is verified |

**AutonomyDimension sub-model:**

| Field | Type | Required |
|---|---|---|
| dimension | string | ✅ |
| shadow_criteria | string | ✅ |
| advisory_criteria | string | ✅ |
| supervised_criteria | string | ✅ |
| autonomous_criteria | string | ✅ |
| current_level | enum: Shadow/Advisory/Supervised/Autonomous | ✅ |

**Dependencies:** Design spec P7 agent job descriptions, P8 contracts

**Quality Gate:** Every never-rule has an enforcement regime mapping. Every output schema matches P1. Progressive autonomy dimensions match design spec. Cost budget matches design spec.

---

### O4: Tool Definitions

*Purpose: Agno @tool wrappers that map user actions to database operations*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| tool_name | string | ✅ | Deterministic |
| tool_purpose | string | ✅ | Deterministic |
| input_schema | string | ✅ | Deterministic — Pydantic model name |
| output_schema | string | ✅ | Deterministic — Pydantic model name |
| cawdp_phase_served | string | ✅ | Deterministic — which CAWDP phase this tool supports |
| enforcement_role | string | ✅ | Deterministic — what Regime 3 enforcement this tool performs |
| null_handling | string | ✅ | Deterministic |

**Dependencies:** Pydantic schemas (O2), writer module interface

**Quality Gate:** Every tool maps to a user action, not a CRUD operation. Every tool specifies what enforcement it performs. Every tool has null handling.

---

### O5: Enforcement Mechanism Map

*Purpose: Explicit mapping of every design constraint to its enforcement regime and implementation mechanism*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| constraint_id | string | ✅ | Deterministic |
| constraint_source | string | ✅ | Deterministic — which design spec section |
| constraint_description | string | ✅ | Deterministic |
| enforcement_regime | enum: Declare/Detect/Prevent | ✅ | Deterministic |
| implementation_mechanism | string | ✅ | Deterministic — specific code/schema/test that enforces this |
| verification_method | string | ✅ | Deterministic — how to verify enforcement works |
| verification_frequency | string | ✅ | Deterministic — when to verify (build-time, runtime, audit) |
| unenforceable_reason | string | ⚠️ | Deterministic — only if Regime 1 or 2 |

**Dependencies:** Design spec P6 Regime 3 enforcement points, P8 contracts, unenforceable elements register

**Quality Gate:** Every constraint from design spec has a row. Every Regime 3 constraint has a concrete structural mechanism. Every Regime 2 constraint has a detection mechanism. Every Regime 1 constraint is honestly declared.

---

### O6: Test Specifications

*Purpose: Concrete test cases mapped to design spec failure modes and quality gates*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| test_id | string | ✅ | Deterministic |
| test_name | string | ✅ | Deterministic |
| failure_mode_ref | string | ⚠️ | Deterministic — links to FM1-FM9 or quality gate |
| test_type | enum: unit/integration/e2e/enforcement | ✅ | Deterministic |
| input_description | string | ✅ | Deterministic |
| expected_result | string | ✅ | Deterministic |
| enforcement_tested | string | ✅ | Deterministic — which constraint this test verifies |
| test_code_outline | string | ✅ | Deterministic — enough for a developer to write the test |

**Dependencies:** Design spec FM1-FM9, quality gates, enforcement mechanism map (O5)

**Quality Gate:** Every FM1-FM9 has at least one test. Every Regime 3 enforcement point has a test. Every quality gate has a test.

---

### O7: Build Order & Dependency Map

*Purpose: Ordered sequence of build tasks with explicit dependencies*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| task_id | string | ✅ | Deterministic |
| task_name | string | ✅ | Deterministic |
| task_description | string | ✅ | Deterministic |
| artifact_produced | string | ✅ | Deterministic — which O1-O8 output this task produces |
| depends_on | list[string] | ✅ | Deterministic — task IDs that must complete first |
| effort_estimate | enum: Small/Medium/Large | ✅ | Deterministic |
| essential | boolean | ✅ | Deterministic — essential or deferrable |
| wave | enum: Foundation/Data/Agent/Integration/Test | ✅ | Deterministic |
| verification_criterion | string | ✅ | Deterministic — what "done" looks like |

**Dependencies:** All previous outputs

**Quality Gate:** Every task has a verification criterion. Dependency chain is acyclic. Essential tasks form a complete path to a deployable workflow. Effort estimates are realistic.

---

### O8: Implementation Plan Document

*Purpose: The assembled, structured plan suitable for developer handoff*

| Field | Type | Required | Epistemic Profile |
|---|---|---|---|
| header | object | ✅ | Deterministic |
| prism_queries | ref(O1) | ✅ | Deterministic |
| output_schemas | ref(O2) | ✅ | Deterministic |
| agent_instructions | ref(O3) | ✅ | Deterministic |
| tool_definitions | ref(O4) | ✅ | Deterministic |
| enforcement_map | ref(O5) | ✅ | Deterministic |
| test_specs | ref(O6) | ✅ | Deterministic |
| build_order | ref(O7) | ✅ | Deterministic |
| enforcement_regime_summary | dict | ✅ | Deterministic — Regime 1/2/3 count and honest assessment |
| unenforceable_elements | list | ✅ | Deterministic — honest declaration of what can only be declared |
| integration_notes | string | ✅ | Deterministic — how pieces connect |
| progressive_autonomy_plan | string | ✅ | Deterministic — Shadow deployment first, advancement criteria |
| risk_register | list | ✅ | Deterministic — build risks and mitigations |

**Dependencies:** All of O1-O7 must be complete before O8 can be assembled.

**Quality Gate:** Every section populated. Enforcement map covers all design constraints. Build order is acyclic. Test specs cover all failure modes. Progressive autonomy plan is concrete.

---

## P2: Backcasting

Working backward from O8 to identify required inputs and their dependencies:

```
O8 (Implementation Plan Document)
  ← requires O7 (Build Order) — must know sequence before assembling
  ← requires O6 (Test Specs) — must know how to verify before defining done
  ← requires O5 (Enforcement Map) — must know constraints before ordering
  ← requires O4 (Tool Definitions) — must know tools before integration
  ← requires O3 (Agent Instructions) — must know agents before building
  ← requires O2 (Pydantic Schemas) — must know types before instructions
  ← requires O1 (PRISM Queries) — must know data sources before schemas
  ← requires existing infrastructure: SurrealDB schema, writer module, orchestrator pattern
  ← requires design spec (P0-P10 of Methodology Reflection Workflow)
```

### Input Requirements

| IR ID | Description | Source | Criticality | Satisfaction |
|---|---|---|---|---|
| IR-001 | SurrealDB schema (design_ tables) | Existing infrastructure | Critical | Must exist and be populated |
| IR-002 | db/writer.py module interface | Existing infrastructure | Critical | Must be available for data writes |
| IR-003 | Orchestrator architecture pattern | Existing infrastructure | Critical | 3-layer pattern (writer → tools → agent) |
| IR-004 | Design spec P0-P10 | Methodology Reflection Workflow spec | Critical | The source of all design constraints |
| IR-005 | Agno framework documentation | External reference | High | Agent, Team, Workflow API reference |
| IR-006 | PRISM query result samples | SurrealDB with test data | High | Need real data shapes for query validation |
| IR-007 | Progressive autonomy criteria from design spec P10 | Design spec | High | Defines advancement criteria for deployment |
| IR-008 | Existing agent specifications (Project Manager, etc.) | Existing codebase | Medium | Pattern reference for consistency |
| IR-009 | Pydantic schema patterns from Project Initiation | Existing codebase | Medium | Pattern reference for consistency |
| IR-010 | Test infrastructure (pytest, Agno test utilities) | Development environment | Medium | Required for test implementation |

### Key P2 Insight

Three critical dependencies are **existing infrastructure** (IR-001, IR-002, IR-003), not new artifacts. The Methodology Reflection workflow doesn't exist in isolation — it depends on the SurrealDB schema already being populated with P0-P9 data, the writer module already enforcing business rules, and the orchestrator pattern already being established. This is the implementation equivalent of the design spec's cascading dependency: **the data pipeline depends on upstream phases capturing artefacts with tags.** The build pipeline depends on **existing infrastructure being in place.**

---

## P3: Task Decomposition

| ID | Task | Cognitive Type | Failure Mode | Output | Wave |
|---|---|---|---|---|---|
| **Foundation Wave** | | | | | |
| T1 | Verify SurrealDB schema has artefact_tags on design_artefacts | Mechanical | Missing field means queries return empty | Confirmation | Foundation |
| T2 | Verify design_phase_transitions has required fields | Mechanical | Missing fields break duration queries | Confirmation | Foundation |
| T3 | Verify design_quality_gates has required fields | Mechanical | Missing fields break failure queries | Confirmation | Foundation |
| T4 | Define O1-O8 Pydantic output schemas | Analytical | Type collision between deterministic/probabilistic/elicited fields | O2 | Foundation |
| T5 | Map epistemic profiles to schema fields | Analytical | Conflating field types in implementation | O2 (partial) | Foundation |
| T6 | Define enforcement regime for each constraint | Analytical | Mapping constraint to wrong regime | O5 (partial) | Foundation |
| **Data Wave** | | | | | |
| T7 | Write PRISM query for phase transition data (O1) | Mechanical | Incorrect SurrealQL syntax | O1 (query 1) | Data |
| T8 | Write PRISM query for quality gate records (O2) | Mechanical | Incorrect SurrealQL syntax | O1 (query 2) | Data |
| T9 | Write PRISM query for surprise-tagged artefacts (O3) | Mechanical | Empty result set handling incorrect | O1 (query 3) | Data |
| T10 | Write PRISM query for gap-tagged artefacts (O4) | Mechanical | Empty result set handling incorrect | O1 (query 4) | Data |
| T11 | Write PRISM query for pattern-tagged artefacts (O5) | Mechanical | Empty result set handling incorrect | O1 (query 5) | Data |
| T12 | Write PRISM query for assessment fragments (O7) | Mechanical | Empty result set handling incorrect | O1 (query 6) | Data |
| T13 | Test all PRISM queries against schema with sample data | Analytical | Query returns wrong shape or missing fields | Validation | Data |
| **Agent Wave** | | | | | |
| T14 | Write Compiler agent instructions | Generative | Never-rules not enforced in instructions | O3 (Compiler) | Agent |
| T15 | Write Analyst agent instructions | Generative | Boundary between analysis and interpretation unclear | O3 (Analyst) | Agent |
| T16 | Write Deriver agent instructions | Generative | Evidence-trace requirement vague in instructions | O3 (Deriver) | Agent |
| T17 | Define progressive autonomy dimensions and criteria | Analytical | Criteria too vague to measure | O3 (dimensions) | Agent |
| T18 | Define cost budgets per agent per execution | Analytical | Budgets too tight (truncation) or too loose (waste) | O3 (budgets) | Agent |
| **Integration Wave** | | | | | |
| T19 | Define Agno tool wrappers for PRISM queries | Mechanical | Tools expose schema language instead of user actions | O4 | Integration |
| T20 | Define Agno tool wrappers for writer operations | Mechanical | Writer bypasses business rules | O4 | Integration |
| T21 | Implement wave orchestration (4-wave pipeline) | Analytical | Wrong execution order or missing dependencies | Integration code | Integration |
| T22 | Implement enforcement mechanisms (Regime 3) | Analytical | Structural enforcement bypassed by agent | O5 (implementation) | Integration |
| T23 | Implement detection mechanisms (Regime 2) | Analytical | Output audit misses violations | O5 (implementation) | Integration |
| T24 | Implement null-state handling per agent | Analytical | Null states not tested or incorrect | O5 (implementation) | Integration |
| **Test Wave** | | | | | |
| T25 | Write test for FM1 (fabrication) | Analytical | Test doesn't actually verify the constraint | O6 | Test |
| T26 | Write test for FM3 (false correlation) | Analytical | Test doesn't distinguish analysis from conclusion | O6 | Test |
| T26b | Write test for FM6 (sparse data as comprehensive) | Analytical | Test doesn't flag sparse sections correctly | O6 | Test |
| T27 | Write test for FM9 (no surprises as success) | Analytical | Test doesn't handle empty result sets correctly | O6 | Test |
| T28 | Write test for type separation enforcement | Analytical | Test doesn't verify epistemic profile distinction | O6 | Test |
| T29 | Write test for evidence-trace requirement | Analytical | Test doesn't verify traces_to field completeness | O6 | Test |
| T30 | Write integration test for 4-wave pipeline | Analytical | Test doesn't verify wave dependencies | O6 | Test |
| T31 | Write end-to-end test with sample data | Analytical | Test data doesn't cover edge cases | O6 | Test |
| **Compilation Wave** | | | | | |
| T32 | Assemble build order from dependency analysis | Mechanical | Incorrect dependency chain creates rework | O7 | Compilation |
| T33 | Compile enforcement regime summary | Mechanical | Regime counts don't match actual mappings | O8 (partial) | Compilation |
| T34 | Write progressive autonomy deployment plan | Analytical | Criteria not measurable | O8 (partial) | Compilation |
| T35 | Write integration notes connecting all artifacts | Analytical | Missing connections between pieces | O8 (partial) | Compilation |
| T36 | Assemble final implementation plan document | Mechanical | Missing sections or inconsistent cross-references | O8 | Compilation |

36 tasks across 4 cognitive types:
- Mechanical: 12 (T1-T3, T7-T12, T19-T20, T32-T33, T36)
- Analytical: 18 (T4-T6, T13, T17-T18, T21-T24, T25-T31, T34-T35)
- Generative: 3 (T14-T16)

---

## P4: Capability Allocation

| Task | H | A | S | Gap | Allocation | Notes |
|---|---|---|---|---|---|---|
| T1 | 2 | 3 | 10 | 8 | System | Schema verification |
| T2 | 2 | 3 | 10 | 8 | System | Schema verification |
| T3 | 2 | 3 | 10 | 8 | System | Schema verification |
| T4 | 6 | 7 | 2 | 1 | Collaborative (A-primary) | Type design needs human review |
| T5 | 5 | 8 | 2 | 3 | Agent-primary | Epistemic mapping requires judgment |
| T6 | 7 | 8 | 2 | 1 | Collaborative (A-primary) | Regime mapping is a design decision |
| T7 | 2 | 4 | 8 | 6 | System | SurrealQL generation |
| T8 | 2 | 4 | 8 | 6 | System | SurrealQL generation |
| T9 | 2 | 4 | 8 | 6 | System | SurrealQL generation |
| T10 | 2 | 4 | 8 | 6 | System | SurrealQL generation |
| T11 | 2 | 4 | 8 | 6 | System | SurrealQL generation |
| T12 | 2 | 4 | 8 | 6 | System | SurrealQL generation |
| T13 | 4 | 5 | 3 | 1 | Collaborative (A-primary) | Test results need human validation |
| T14 | 8 | 6 | 2 | 2 | Human-primary | Agent instructions are design decisions |
| T15 | 8 | 6 | 2 | 2 | Human-primary | Boundary specification is critical |
| T16 | 8 | 6 | 2 | 2 | Human-primary | Evidence-trace requirements are critical |
| T17 | 5 | 7 | 2 | 2 | Agent-primary | Criteria specification |
| T18 | 3 | 6 | 4 | 3 | Agent-primary | Budget estimation |
| T19 | 3 | 5 | 6 | 3 | Agent-primary | Tool design requires framework knowledge |
| T20 | 3 | 5 | 6 | 3 | Agent-primary | Tool design requires framework knowledge |
| T21 | 7 | 8 | 2 | 1 | Collaborative (A-primary) | Orchestration logic needs human review |
| T22 | 7 | 8 | 2 | 1 | Collaborative (A-primary) | Enforcement is a design decision |
| T23 | 5 | 7 | 2 | 2 | Agent-primary | Detection mechanism design |
| T24 | 4 | 7 | 2 | 3 | Agent-primary | Null state specification |
| T25 | 5 | 7 | 2 | 2 | Agent-primary | Test design for enforcement |
| T26 | 5 | 7 | 2 | 2 | Agent-primary | Test design for enforcement |
| T26b | 5 | 7 | 2 | 2 | Agent-primary | Test design for enforcement |
| T27 | 5 | 7 | 2 | 2 | Agent-primary | Test design for enforcement |
| T28 | 5 | 7 | 2 | 2 | Agent-primary | Test design for type separation |
| T29 | 5 | 7 | 2 | 2 | Agent-primary | Test design for traceability |
| T30 | 4 | 7 | 2 | 3 | Agent-primary | Integration test design |
| T31 | 6 | 7 | 2 | 1 | Collaborative (A-primary) | Edge case identification needs human judgment |
| T32 | 2 | 4 | 8 | 6 | System | Dependency ordering |
| T33 | 2 | 4 | 8 | 6 | System | Compilation |
| T34 | 5 | 7 | 2 | 2 | Agent-primary | Deployment criteria design |
| T35 | 5 | 8 | 2 | 3 | Agent-primary | Integration notes |
| T36 | 2 | 3 | 10 | 8 | System | Final assembly |

**Human-primary tasks (gap ≥ 6):** T14 (Compiler instructions), T15 (Analyst instructions), T16 (Deriver instructions)

**Key P4 Insight:** Agent instructions are human-primary because they encode the authority boundaries that define each agent's identity. A poorly-specified "never" rule that gets misinterpreted by an agent is the highest-risk implementation failure — it directly corresponds to FM1 (fabrication), FM3 (false correlation), and FM4 (generic recommendations). The agent instruction is the Regime 1 (Declare) enforcement layer, and if it's wrong, Regime 2 and 3 can't fully compensate.

---

## P5: Event Storming

### Domain Events

| Event | Trigger | Producer |
|---|---|---|
| E1 | Schema verification passed | System (T1-T3) |
| E2 | Schema verification failed | System (T1-T3) |
| E3 | Pydantic schemas defined | Human/Agent (T4-T5) |
| E4 | PRISM queries written and tested | System (T7-T13) |
| E5 | Agent instructions completed | Human (T14-T16) |
| E6 | Enforcement mechanisms implemented | Agent (T22-T24) |
| E7 | Test suite written | Agent (T25-T31) |
| E8 | Pipeline integration complete | Agent (T21) |
| E9 | Build order assembled | System (T32) |
| E10 | Implementation plan compiled | System (T36) |

### Failure Events

| Failure | Trigger | Recovery |
|---|---|---|
| F1 | SurrealDB schema missing artefact_tags field | T1 verification fails | Add artefact_tags to design_artefacts table; re-run verification |
| F2 | PRISM query returns unexpected shape | T13 test against sample data | Fix query to match actual schema; add null handling |
| F3 | Pydantic schema conflates epistemic types | T4-T5 review reveals type collision | Separate deterministic, probabilistic, and elicited fields; enforce in schema |
| F4 | Agent instruction doesn't enforce never-rule | T14-T16 review or test (FM1, FM3, FM8) | Strengthen instruction; add Regime 2 detection; add Regime 3 structural enforcement |
| F5 | Tool exposes schema language instead of user action | T19-T20 review | Refactor tool interface to user-action semantics; validate against tool definitions |
| F6 | Wave orchestration has wrong dependency order | T30 integration test | Fix dependency chain; verify data flows correctly between waves |
| F7 | Enforcement mechanism can be bypassed | T25-T29 enforcement tests | Add structural enforcement; if impossible, document as Regime 1/2 with mitigation |
| F8 | Null state not tested for all agents | T24 null state handling test | Add null state test cases for each agent; verify schema handles null inputs |
| F9 | Progressive autonomy criteria not measurable | T34 deployment plan review | Rewrite criteria with concrete metrics; verify testability |
| F10 | Test doesn't actually verify the constraint | T25-T29 test review | Strengthen test to actually exercise the constraint boundary |

### Key P5 Insight

F1 (missing artefact_tags) is the implementation equivalent of the design spec's cascading dependency — if the schema doesn't support tagging, the entire workflow collapses. This must be verified first, before any other build work. F4 (agent instructions not enforcing never-rules) is the highest-impact implementation failure because it directly enables FM1, FM3, and FM8.

---

## P6: System Architecture

### Build Wave Architecture

```
Wave 0: Foundation (prerequisites)
T1 ──┐
T2 ──┤──→ schema_verified
T3 ──┘
T4 ──────→ schemas_defined
T5 ──────→ epistemic_mapped
T6 ──────→ regime_mapped

Wave 1: Data (PRISM queries + validation)
T7 ──┐
T8 ──┤
T9 ──┤──→ raw_queries (depends on schema_verified)
T10 ─┤
T11 ─┤
T12 ─┘
T13 ──────→ validated_queries (depends on raw_queries + sample_data)

Wave 2: Agent (instructions + progressive autonomy)
T14 ──┐
T15 ──┤──→ agent_instructions (depends on schemas_defined + epistemic_mapped)
T16 ──┘
T17 ──────→ autonomy_dimensions (depends on agent_instructions)
T18 ──────→ cost_budgets (depends on agent_instructions)

Wave 3: Integration (tools + enforcement + pipeline)
T19 ──┐
T20 ──┤──→ tool_definitions (depends on validated_queries + writer_module)
T21 ──────→ wave_orchestration (depends on agent_instructions + tool_definitions)
T22 ──┐
T23 ──┤──→ enforcement_mechanisms (depends on regime_mapped + agent_instructions)
T24 ──┘

Wave 4: Test (tests for every failure mode)
T25 ──┐
T26 ──┤
T26b ─┤
T27 ──┤──→ test_suite (depends on enforcement_mechanisms + agent_instructions)
T28 ──┤
T29 ──┤
T30 ──┤
T31 ──┘

Wave 5: Compilation (assembly + deployment)
T32 ──────→ build_order (depends on all waves)
T33 ──┐
T34 ──┤──→ deployment_artifacts (depends on test_suite + build_order)
T35 ──┘
T36 ──────→ final_plan (depends on all above)
```

### File Structure

```
methodology_reflection/
├── schemas/
│   ├── __init__.py
│   ├── outputs.py          # O1-O8 Pydantic schemas (O2)
│   ├── epistemic.py        # Epistemic type definitions (O2)
│   └── validation.py        # Schema validation rules (O2)
├── queries/
│   ├── __init__.py
│   └── prism_queries.py     # SurrealDB query templates (O1)
├── agents/
│   ├── __init__.py
│   ├── compiler.py          # Compiler agent instructions + config (O3)
│   ├── analyst.py           # Analyst agent instructions + config (O3)
│   └── deriver.py            # Deriver agent instructions + config (O3)
├── tools/
│   ├── __init__.py
│   └── reflection_tools.py   # Agno @tool wrappers (O4)
├── enforcement/
│   ├── __init__.py
│   ├── regime_map.py         # Enforcement mechanism map (O5)
│   ├── schema_enforcement.py # Regime 3: schema-level enforcement
│   ├── output_audit.py       # Regime 2: output-level detection
│   └── prompt_declarations.py # Regime 1: prompt-level declarations
├── tests/
│   ├── __init__.py
│   ├── test_fabrication.py           # FM1 test
│   ├── test_false_correlation.py     # FM3 test
│   ├── test_sparse_comprehensive.py  # FM6 test
│   ├── test_no_surprises.py          # FM9 test
│   ├── test_type_separation.py        # Epistemic profile test
│   ├── test_evidence_trace.py         # Traceability test
│   ├── test_integration.py            # 4-wave pipeline test
│   └── test_e2e.py                    # End-to-end with sample data
├── pipeline/
│   ├── __init__.py
│   └── orchestration.py      # 4-wave pipeline orchestration (T21)
├── config/
│   ├── autonomy.py           # Progressive autonomy dimensions (T17)
│   └── budgets.py            # Cost budgets per agent (T18)
├── deployment/
│   ├── build_order.py        # Build order + dependencies (T32)
│   ├── enforcement_summary.py # Regime 1/2/3 summary (T33)
│   └── autonomy_plan.py      # Progressive autonomy deployment (T34)
└── plan.md                   # Final implementation plan (O8)
```

### FMEA (Failure Modes and Effects Analysis)

| ID | Failure Mode | Severity | Occurrence | Detection | RPN | Recovery |
|---|---|---|---|---|---|---|
| FM1 | Schema missing artefact_tags | 10 | 2 | 10 | 200 | Add field, re-run T1 verification |
| FM2 | PRISM query returns wrong shape | 6 | 4 | 7 | 168 | Fix query syntax, add null handling |
| FM3 | Epistemic types conflated in schema | 8 | 3 | 5 | 120 | Separate deterministic/probabilistic/elicited fields |
| FM4 | Agent instructions don't enforce never-rules | 9 | 3 | 4 | 108 | Strengthen instructions + add Regime 2 detection |
| FM5 | Tool exposes schema language | 5 | 3 | 7 | 105 | Refactor tool to user-action semantics |
| FM6 | Wave dependency order wrong | 7 | 2 | 8 | 112 | Fix dependency chain, verify with T30 |
| FM7 | Enforcement bypassed | 9 | 2 | 6 | 108 | Add structural enforcement or document as Regime 1/2 |
| FM8 | Null state not handled | 6 | 3 | 6 | 108 | Add null state tests for each agent |
| FM9 | Progressive autonomy criteria not measurable | 5 | 4 | 4 | 80 | Rewrite criteria with concrete metrics |
| FM10 | Test doesn't verify actual constraint | 7 | 3 | 5 | 105 | Strengthen test to exercise boundary |

Highest RPNs: FM1 (200 — schema field missing blocks entire workflow), FM2 (168 — query shape mismatch breaks data flow), FM3 (120 — epistemic type collision undermines type separation principle).

### 5 Regime 3 Enforcement Points

| # | Boundary | Enforcement |
|---|---|---|
| 1 | Compiler "never add content" | Output schema validation: every field must trace to PRISM data or a processing step defined in the pipeline. Implemented as Pydantic validator on MethodologyReflection schema. |
| 2 | Deriver "every recommendation traces" | traces_to field required in Recommendation schema. Implemented as Pydantic field constraint (min_items=1) + runtime validation that traces reference valid artefact IDs. |
| 3 | No fabrication | Sparse section flagging mandatory in Output schema (sparse_sections field required on O8). Completeness calculation is deterministic (computed from PRISM data). |
| 4 | Type separation | Epistemic type fields (epistemic_profile) on every schema field. Implemented as Literal["deterministic", "probabilistic", "elicited"] type annotation. Schema validation rejects outputs where types are conflated. |
| 5 | Evidence strength | evidence_strength field required on every Recommendation and Pattern. Implemented as Literal["Strong", "Moderate", "Weak"] type annotation. |

---

## P7: Agent Design

### Implementation Agent (Human) — T14, T15, T16

| Field | Value |
|---|---|
| Class | Generator (creating agent instructions) |
| Orientation | Constraint-oriented |
| Identity | "I write agent instructions that encode design constraints into enforceable specifications. I never soften constraints for convenience, never leave ambiguity where precision is needed, never skip never-rules." |
| Mission | Write Compiler, Analyst, and Deriver agent instructions that faithfully encode all authority boundaries, never-rules, null states, and progressive autonomy dimensions from the design specification. |
| Inputs | Design spec P7 (agent job descriptions), P8 (contracts), O2 (Pydantic schemas), O5 (enforcement map) |
| Outputs | O3 (Agent Instruction Specifications) |
| Never rules | Soften constraints for convenience, leave ambiguity in never-rules, skip enforcement regime mapping, conflate Regime 1/2/3 distinctions |
| Hardest boundary moment | Translating "Analyst never interprets beyond data" into an instruction that actually prevents interpretation — the line between analysis and interpretation is genuinely fuzzy, and the instruction must be specific enough to detect violations |
| Harm assessment | Indirect design harm — poorly specified instructions enable FM1 (fabrication), FM3 (false correlation), FM8 (pattern forcing) downstream |
| Progressive autonomy | N/A — this is a human task |

### Build Orchestrator (System)

| Field | Value |
|---|---|
| Class | Aggregator |
| Orientation | Constraint-oriented |
| Identity | "I orchestrate build waves in dependency order. I never skip verification steps, never proceed with failed dependencies, never reorder tasks to skip waits." |
| Mission | Execute build waves in order, verify each wave completes before proceeding, assemble final plan. |
| Inputs | Build order (O7), verification results from each wave |
| Outputs | O8 (Implementation Plan Document) |
| Never rules | Skip verification, proceed with failed dependencies, reorder tasks |
| Hardest boundary moment | When a wave partially fails — the temptation to proceed with successful components rather than halting |
| Harm assessment | Indirect process harm — wrong build order creates rework and integration failures |
| Progressive autonomy | N/A — this is a system process |

### Test Writer (Agent-primary)

| Field | Value |
|---|---|
| Class | Assessor |
| Orientation | Constraint-oriented |
| Identity | "I write tests that verify design constraints are enforced. Every test traces to a specific failure mode or quality gate. I never write tests that don't actually exercise the constraint boundary." |
| Mission | Write test specifications for FM1-FM9, quality gates, type separation, and evidence trace requirements. |
| Inputs | Design spec FM1-FM9, O5 (enforcement map), O2 (Pydantic schemas), O3 (agent instructions) |
| Outputs | O6 (Test Specifications) |
| Never rules | Write tests that pass without exercising the constraint, skip edge cases, test happy path only |
| Hardest boundary moment | Writing a test for FM7 (enforcement bypassed) — the test must actually attempt to bypass the enforcement mechanism, not just verify it exists |
| Harm assessment | Indirect process harm — tests that don't verify constraints give false confidence |
| Progressive autonomy | Shadow (human reviews every test) → Advisory (human reviews constraint tests) → Supervised (human reviews edge case tests) → Autonomous (human reviews test suite overview) |

---

## P8: Contract Formalization

### Implementation Agent Contract

| Primitive | Specification |
|---|---|
| Contract | Write Compiler, Analyst, and Deriver agent instructions that encode design constraints |
| Principal | Human (developer/reviewer) |
| Schema | AgentInstructionSpecification (defined in O3) |
| Guard | prohibited: ["soften_constraints", "leave_ambiguity", "skip_enforcement_mapping", "conflate_regimes"] |
| Budget | Time-boxed: 2 hours per agent instruction set |
| Invocation | After O2 (schemas), O5 (enforcement map) complete |
| Revert | If review finds constraint softened or never-rule omitted, revert to redraft |
| Event | instruction_started, never_rule_reviewed, enforcement_mapped, instruction_complete |
| Identity | Constraint-oriented Generator |
| Knowledge | Design spec P7, P8, O2 schemas, O5 enforcement map |

### Build Orchestrator Contract

| Primitive | Specification |
|---|---|
| Contract | Execute build waves in dependency order, verify each wave, assemble final plan |
| Principal | Human (project lead) |
| Schema | BuildOrder + ImplementationPlanDocument |
| Guard | prohibited: ["skip_verification", "proceed_with_failed_dependency", "reorder_without_justification"] |
| Budget | Time-boxed: 1 hour for assembly |
| Invocation | After all waves complete and verified |
| Revert | If verification fails, revert to failed wave and halt |
| Event | wave_started, wave_verified, wave_failed, plan_assembled |
| Identity | Constraint-oriented Aggregator |
| Knowledge | O1-O7 outputs, build order dependencies |

### Test Writer Contract

| Primitive | Specification |
|---|---|
| Contract | Write test specifications that verify design constraints are enforced |
| Principal | Human (developer/reviewer) |
| Schema | TestSpecification (defined in O6) |
| Guard | prohibited: ["write_tests_that_dont_exercise_constraint", "skip_edge_cases", "test_happy_path_only"] |
| Budget | Time-boxed: 30 minutes per test |
| Invocation | After O5 (enforcement map) and O3 (agent instructions) complete |
| Revert | If test doesn't exercise the constraint boundary, revert to redraft |
| Event | test_started, constraint_exercised, edge_case_covered, test_complete |
| Identity | Constraint-oriented Assessor |
| Knowledge | Design spec FM1-FM9, O5 enforcement map, O2 schemas, O3 agent instructions |

### Unenforceable Elements Register

| Element | Why Unenforceable | Regime | Mitigation |
|---|---|---|---|
| "Never interpret beyond data" in Analyst instructions | Interpretation is a spectrum; what counts as interpretation vs analysis requires judgment | Regime 1 (Declare) | Prompt instruction + Regime 2 output audit (scan for conclusion language) |
| "Never assemble flattering narratives" in Compiler instructions | Narrative tone is subjective | Regime 1 (Declare) | Tone-agnostic schema (facts only, no evaluative language in field names) |
| Progressive autonomy criteria measurable | "≤1 error in 10 compilations" requires production data that doesn't exist yet | Regime 2 (Detect) | Define measurable criteria in deployment plan; track during Shadow phase; adjust after 10 executions |
| Build order optimality | Whether the build order is optimal can't be verified until the build is complete | Regime 2 (Detect) | Review build order for dependency correctness; adjust after build attempts |

### 10×10 Mapping Matrix (Specification Sections × Contract Primitives)

| Section ↓ / Primitive → | Contract | Principal | Schema | Guard | Budget | Invocation | Revert | Event | Identity | Knowledge |
|---|---|---|---|---|---|---|---|---|---|---|
| Identity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Task Map | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Output Specs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Agent Roster | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Failure & Recovery | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Verification & Trust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Contracts | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Human Experience | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Monitoring & Evolution | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Workflow Diagram | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

*Human Experience and Workflow Diagram have partial mapping — human experience affects Principal invocation (when a human reviews) and Knowledge (human judgment needed for review decisions), and Workflow Diagram affects Principal (who triggers which wave) but is otherwise fully mappable.*

---

## P9: Human Experience Design

### Cognitive Load Budget

The human's role is writing agent instructions (T14-T16) and reviewing all outputs (T4-T6, T13, T17-T18, T21-T24, T31, T34-T35, final review).

| Activity | Decisions | Time Budget | Decision Types |
|---|---|---|---|
| Write Compiler instructions (T14) | 3-5 | 90 min | Boundary specification (what counts as "adding content"?), null state definition, never-rule precision |
| Write Analyst instructions (T15) | 4-6 | 90 min | Boundary specification (analysis vs interpretation line), anomaly threshold definition, correlation strength calibration |
| Write Deriver instructions (T16) | 3-5 | 90 min | Evidence-trace requirement precision, recommendation priority calibration, pattern formalisation criteria |
| Review schemas (T4-T5) | 3-4 | 30 min | Type correctness, epistemic profile accuracy |
| Review enforcement map (T6) | 2-3 | 20 min | Regime assignment correctness |
| Review PRISM queries (T13) | 2-3 | 20 min | Query correctness, null handling |
| Review integration (T21, T31) | 3-4 | 30 min | Data flow correctness, edge cases |
| Review test specs (T25-T29) | 4-6 | 40 min | Test coverage, constraint exercise |
| Final review of implementation plan | 5-8 | 60 min | Completeness, consistency, traceability |

**Total maximum: ~7 hours across all human-primary and collaborative tasks.**

### Override Mechanisms

| Override Type | Mechanism | Example |
|---|---|---|
| Adjust constraint enforcement | Change Regime assignment | "Move 'never interpret beyond data' from Regime 1 to Regime 2 with output audit" |
| Modify progressive autonomy criteria | Edit deployment plan | "Start Deriver at Advisory instead of Shadow for recommendation derivation" |
| Add missing never-rule | Edit agent instructions | "Add: Deriver never produces more than 5 recommendations per gap" |
| Adjust cost budget | Edit budget specification | "Increase Analyst budget from 10K-30K to 15K-40K tokens" |
| Approve build order change | Edit task dependencies | "T21 can start before T19-T20 if tools are stub-able" |

### Stakeholder Surfaces

| Surface | View | Language | Depth | Emphasis |
|---|---|---|---|---|
| Developer (Implementer) | Full implementation plan with code-level specifications | Technical | Deep | Schemas, queries, agent configs, test specs, file structure |
| Project Lead | Build order, dependencies, risk register, enforcement summary | Mixed | Medium | What to build first, what's risky, what's deferrable |
| QA Lead | Test specifications, enforcement mechanisms, failure modes | Technical | Deep | Every FM test, every Regime 3 enforcement point, every edge case |

### System Empowerment Assessment

| Dimension | Level | Explanation |
|---|---|---|
| Time saved | Enabling | Produces in hours what would take days to assemble manually |
| Insight surfaced | Informing | Enforcement regime mapping reveals which constraints are structurally enforceable vs declared |
| Decision support | Enabling | Build order with dependencies prevents rework; risk register prevents surprises |
| Creative freedom | Enabling | Frees human from mechanical compilation to focus on judgment-heavy tasks (agent instructions) |
| Overall | Enabling | System handles schema generation, query writing, test design; human focuses on boundary specification and review |

---

## P10: Validation & Iteration

### Testable Hypotheses

| # | Hypothesis | Test Method | Success Criterion |
|---|---|---|---|
| H1 | A developer can build the workflow using only the implementation plan | Give plan to developer unfamiliar with design spec; observe build attempts | Developer builds complete workflow with ≤3 clarifying questions |
| H2 | Every design constraint has a concrete enforcement mechanism | Audit enforcement map against design spec constraints | 100% of constraints mapped to Regime 1/2/3 with specific mechanism |
| H3 | Build order is acyclic and all dependencies are correct | Trace dependency graph for cycles and verify each dependency is real | Zero cycles; every dependency is actually required |
| H4 | Schema validation catches fabrication | Inject fabricated content into Compiler output; verify schema rejects it | Schema rejects output with claims that don't trace to processing steps |
| H5 | Epistemic type separation is preserved in implementation | Verify Pydantic schemas enforce deterministic/probabilistic/elicited distinction | Type annotations on every field; runtime validation rejects type conflation |
| H6 | Evidence-trace requirement is structurally enforced | Generate recommendation without traces_to field; verify schema rejects it | Schema rejects recommendation without ≥1 traces_to entry |

### Progressive Autonomy Deployment

| Task | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Schema generation (T4-T5) | Type correctness | Human writes, agent suggests | Agent writes, human reviews every field | Agent writes, human reviews flagged fields | Agent writes, human reviews final only | ≥10 schemas with ≤1 type error |
| PRISM query writing (T7-T12) | Query correctness | Human writes, agent suggests | Agent writes, human reviews each query | Agent writes, human reviews edge cases | Agent writes, human reviews final | ≥10 queries with ≤1 syntax error |
| Agent instruction writing (T14-T16) | Boundary precision | Human writes all instructions | Human writes, agent reviews for gaps | Agent drafts, human reviews never-rules | Agent drafts, human reviews final | ≥3 instruction sets with ≤1 never-rule gap |
| Enforcement implementation (T22-T24) | Structural enforcement | Human implements, agent suggests | Human implements, agent reviews | Agent implements, human reviews | Agent implements, human spot-checks | ≥3 mechanisms with ≤1 bypass |
| Test writing (T25-T31) | Constraint exercise | Human writes all tests | Human writes, agent reviews coverage | Agent writes, human reviews boundary tests | Agent writes, human reviews final | ≥10 tests with ≤1 that doesn't exercise constraint |

### Specification Aging Schedule

| Component | Default Cadence | Trigger-Based Review | Responsible |
|---|---|---|---|
| PRISM query templates | When schema changes | When design_artefacts table structure changes | System |
| Pydantic schemas | When design spec changes | When O1-O8 schemas are updated in design spec | Human |
| Agent instructions | 6 months | When never-rules change or agent behavior drifts | Human |
| Enforcement mechanisms | 6 months | When bypass attempts are detected | Human |
| Test specifications | When design spec changes | When failure modes are updated | Agent/Human |
| Build order | When task dependencies change | When new tasks are added or removed | System |

### EVOLVE Mode

| Signal | Re-entry Point | Scope |
|---|---|---|
| Schema change to design_artefacts | P3 (Decomposition) then P7 (Agent Design) | Re-verify queries, update schemas, check agent instructions |
| Agent behavior drift detected | P7 (Agent Design) | Review and strengthen never-rules, adjust enforcement regime |
| Test failure in production | P6 (System Architecture) then P10 (Validation) | Fix enforcement mechanism, add test for failure mode |
| New failure mode discovered | P5 (Event Storming) then P6 | Add to FMEA, add test, add enforcement |
| Design spec updated | P0 (Purpose & Vision) | Full re-evaluation of implementation plan |
| Progressive autonomy criteria not measurable | P4 (Capability Allocation) | Rewrite criteria with concrete metrics |
| Enforcement bypass discovered | P6 (System Architecture) | Move from Regime 1 to Regime 2 or Regime 3 if possible; document if not |

---

## Summary: What This Application Reveals About the Implementation Plan

| Phase | Key Insight |
|---|---|
| P0 | The implementation plan IS the P8 (Contract Formalization) of the build process — it translates design intent into enforceable build contracts |
| P1 | 8 outputs that are all build artifacts (queries, schemas, instructions, tools, enforcement, tests, build order, final plan) — every output is something a developer can use directly |
| P2 | Three critical dependencies are existing infrastructure (SurrealDB schema, writer module, orchestrator pattern), not new artifacts — the build doesn't start from zero |
| P3 | 36 tasks across 6 waves — Foundation, Data, Agent, Integration, Test, Compilation — with clear dependency ordering |
| P4 | 3 human-primary tasks (agent instructions T14-T16) because authority boundaries are design decisions that must not be delegated to agents |
| P5 | FM1 (schema missing artefact_tags, RPN 200) is the highest risk — blocks the entire workflow if the data pipeline doesn't exist |
| P6 | 5 Regime 3 enforcement points in implementation: schema validation (Compiler), traces_to field (Deriver), sparse flagging (fabrication prevention), epistemic type separation, evidence strength field |
| P7 | The "implementation agent" is a human writing agent instructions — the highest-risk task because it encodes the Regime 1 (Declare) enforcement layer |
| P8 | 4 unenforceable elements honestly documented: Analyst interpretation spectrum, Compiler narrative tone, measurable autonomy criteria (need production data), build order optimality |
| P9 | Maximum 7 hours of human decision-making across all tasks — the implementation plan reduces human cognitive load to boundary specification and review |
| P10 | 6 testable hypotheses; progressive autonomy with measurable criteria; specification aging aligned with infrastructure change triggers |

### The Cascading Dependency (Implementation Version)

**If the SurrealDB schema doesn't have artefact_tags on design_artefacts, the entire Methodology Reflection workflow has nothing to query.** T1-T3 must verify this before any other work begins. This is the implementation equivalent of the design spec's P10 cascading dependency.

### Enforcement Regime Summary

| Regime | Count | Examples |
|---|---|---|
| Regime 3 (Prevent) | 5 | Schema validation, traces_to field requirement, sparse flagging, epistemic type separation, evidence strength field |
| Regime 2 (Detect) | 4 | Output audit for conclusion language, narrative tone, pattern forcing detection, measurable criteria tracking |
| Regime 1 (Declare) | 4 | Analyst "never interpret beyond data", Compiler "never assemble flattering narratives", autonomy criteria measurability, build order optimality |

**Total: 5 structural enforcements, 4 detections, 4 declarations.** This is an honest assessment — the implementation plan cannot structurally prevent an analyst from interpreting (Regime 1) or a compiler from assembling flattering narratives (Regime 1). What it CAN do is enforce type separation, evidence traces, and sparse flagging structurally (Regime 3), and detect conclusion language and untraced recommendations after the fact (Regime 2).The complete CAWDP application is done. Here's what emerged that I want to highlight:

**The meta-structure is the insight.** The implementation plan IS the P8 (Contract Formalization) of the build process. Every design constraint from the Methodology Reflection Workflow specification maps to a concrete enforcement mechanism in the build artifacts — and the same honest assessment applies: 5 things can be structurally prevented (Regime 3), 4 can only be detected after the fact (Regime 2), and 4 can only be declared in instructions (Regime 1). This isn't a weakness — it's honest infrastructure.

**The cascading dependency mirrors perfectly.** Just as the design spec says "if P0-P9 don't capture artefacts with tags, P10 has nothing to assemble," the implementation says "if the SurrealDB schema doesn't have `artefact_tags` on `design_artefacts`, the entire workflow has nothing to query." FM1 at RPN 200 confirms this is the single highest-risk point.

**3 human-primary tasks — all agent instructions.** The tasks with gap ≥ 6 are precisely the ones where authority boundaries are encoded. You can't delegate "write the rules about what the agent can never do" to the agent itself. This validates the complementarity analysis — and the P7 finding from the design spec that "fabrication" is the highest-risk failure mode (RPN 160).

**The 36-task build order is progressive, not parallel.** Foundation → Data → Agent → Integration → Test → Compilation. Each wave depends on the previous one being validated. This mirrors progressive autonomy at the implementation level.

**What should happen next?** The honest answer from the methodology: T1-T3 (verify the SurrealDB schema has `artefact_tags`) should happen before anything else. If that field doesn't exist, nothing else matters.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-05-21T11:33:09* · `glm-5.1:cloud` · `9731366b...`

### Prompt

Ok. Now produce the implementation plan for the methodology reflection workflow.

What information do you need from me?

We are using Agno v2.6.8, with AgentOS, SurrealDB v3, and will deploy to Railway.

### Response

Good question. Before I write a single line, I need to verify the cascading dependency that the CAWDP application identified as FM1 (RPN 200). Here's what I need:

---

## Critical (Blocks Everything)

**1. Does `design_artefacts` have `artefact_tags`?**

The #1 risk. If this field doesn't exist in your SurrealDB v3 schema, the entire Methodology Reflection workflow has nothing to query. Can you confirm whether your deployed schema includes:

```surql
DEFINE FIELD artefact_tags ON design_artefacts TYPE set<string>;
```

**2. What's your current project structure?**

Where should the new files go? Specifically:
- Is there an existing `methodology_reflection/` or `workflows/` directory?
- Where does `db/writer.py` live relative to the agents?
- Where do Pydantic schemas live?
- Where do test files live?

I need the actual directory layout so I produce files that land in the right places.

---

## High (Shapes Architecture)

**3. Agno composition decision: Workflow, Team, or sequential Agents?**

The design spec calls for 4 sequential waves (Data → Analysis → Derivation → Compilation) with 3 specialist agents (Compiler, Analyst, Deriver). In Agno v2.6.8, this maps to one of:

- **Agno Workflow** — sequential steps with `HumanReview` gates at wave boundaries
- **Agno Team** — agents collaborating with an orchestrator
- **Separate Agents invoked sequentially** — each agent called independently, state managed externally

Which pattern are you using for the existing Project Initiation Workflow? I'll match that.

**4. Is there an existing `db/writer.py` module?**

The CAWDP application references a 3-layer architecture: `db/writer.py` (CAWDP-aware persistence) → `agents/tools/` (Agno @tool wrappers) → `agents/cawdp_orchestrator.py` (engine agent). Does this exist? If so, I'll build on it rather than duplicating.

**5. SurrealDB connection pattern**

How do your agents connect to SurrealDB? Is there:
- A shared connection module?
- Per-agent connections?
- Connection via Agno's database integration?
- Something else?

I need to know this for the PRISM query implementations.

---

## Medium (Affects Detail Level)

**6. Test data availability**

Is there sample data in SurrealDB (design_workflows, design_artefacts with tags, design_phase_transitions, design_quality_gates) that I can write queries against? Or should I include seed data scripts?

**7. Existing agent configuration pattern**

Your Project Manager and Project Initiation agents have specific patterns for Agno configuration (model, tools, session_state, etc.). Should I match those exactly, or are you evolving the pattern?

**8. Railway deployment specifics**

Are there any Railway-specific constraints I should account for? (Environment variables, volume mounts for SurrealDB, build commands, etc.)

---

## What I Can Produce Immediately

While waiting for answers, I can produce the pieces that don't depend on infrastructure:

- **O2: Pydantic Output Schemas** — These are framework-independent type definitions
- **O5: Enforcement Mechanism Map** — This is a design document, not code
- **O6: Test Specifications** — Test descriptions that are framework-independent
- **Agent Instruction Specifications** — The human-primary tasks (T14-T16)

But I'd rather get your answers first and produce everything in the right structure from the start. One integrated delivery is better than six disconnected ones.

What can you share?

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-05-21T11:55:22* · `glm-5.1:cloud` · `3852ae6c...`

### Prompt

1. I'm creating the build spec backwards. Your implementation plan should include the implementation of anything that needs to exist for this build spec.
2. Since there is not yet a current project structure, suggest sensible structure for the requirements of this implementation. they might be changed as more build specs are created and a bigger picture of the application architecture is known. You won't be producing files, just the implementation plan for this workflow.
3. This is a gap in the design spec. I will need to get more information on this. Let's see them as a team with an orchestrator for now.
4. No existing writer module
5. Not decided. What are your recommendations? What supports your recommendations?
6. No sample data. Include seed script specs (don't write them)
7. Ignore agents in the workspace you can see. This is not where this application will be developed. Just provide agent implementation specs. The implementers will choose the pattern.
8. Deployment is not in scope for you

I don't want you to produce schemas or code, just an implementation spec with acceptance criteria.

### Response

# Methodology Reflection Workflow: Implementation Specification

---

## 1. Project Structure

```
cawdp/
├── db/
│   ├── connection.py              # SurrealDB connection management
│   ├── writer.py                  # CAWDP-aware persistence (business rules)
│   └── queries/
│       ├── base.py                # Shared query utilities
│       ├── phase_transitions.py   # P1-O1 data source
│       ├── quality_gates.py       # P1-O2 data source
│       └── artefacts.py           # P1-O3/O4/O5/O7 data source
│
├── schemas/
│   ├── epistemic.py               # Epistemic type definitions
│   ├── outputs/
│   │   ├── phase_duration.py      # O1 schema
│   │   ├── quality_gates.py       # O2 schema
│   │   ├── surprises.py           # O3 schema
│   │   ├── gaps.py                # O4 schema
│   │   ├── patterns.py            # O5 schema
│   │   ├── recommendations.py     # O6 schema
│   │   ├── assessment.py          # O7 schema
│   │   └── reflection_document.py # O8 schema
│   └── contracts/
│       ├── compiler.py            # Compiler contract definition
│       ├── analyst.py             # Analyst contract definition
│       └── deriver.py             # Deriver contract definition
│
├── agents/
│   ├── compiler.py               # Compiler agent implementation spec
│   ├── analyst.py                 # Analyst agent implementation spec
│   └── deriver.py                 # Deriver agent implementation spec
│
├── tools/
│   └── reflection_tools.py        # Agno @tool wrappers
│
├── enforcement/
│   ├── schema_validation.py       # Regime 3: structural enforcement
│   ├── output_audit.py            # Regime 2: detection
│   └── prompt_declarations.py     # Regime 1: declared in instructions
│
├── pipeline/
│   └── orchestration.py           # 4-wave pipeline orchestration
│
└── seeds/
    └── methodology_reflection/    # Seed data specification
        ├── sample_workflow.py
        ├── sample_transitions.py
        ├── sample_gates.py
        └── sample_artefacts.py
```

**Rationale:** This structure separates concerns by function (data, schemas, agents, enforcement) while keeping the Methodology Reflection workflow self-contained. The `db/queries/` pattern isolates data access so agents never write raw SurrealQL. The `enforcement/` directory makes the regime assignment visible and auditable. The `seeds/` directory is temporary — for development and testing only.

---

## 2. SurrealDB Connection Recommendation

**Recommendation: Shared connection module with CAWDP-aware writer layer.**

Agents connect to SurrealDB through a shared `db/connection.py` module and a `db/writer.py` layer that enforces business rules. Agents never execute raw SurrealQL directly — they call typed query functions from `db/queries/` that return Pydantic models.

**Why this pattern:**

| Concern | How this addresses it |
|---|---|
| CC-4 Information Boundaries (Regime 3) | Agents can't bypass writer business rules because they don't have direct write access |
| CC-8 Assured Audit Trail | Writer layer logs all mutations with actor, timestamp, and action |
| Epistemic type safety | Query functions return typed Pydantic models, not raw dicts — type conflation is prevented structurally |
| Connection management | Single connection pool, single configuration, single retry logic |
| Testability | Query functions can be mocked without SurrealDB running |
| Progressive autonomy | Writer can enforce different write permissions per agent role (Compiler vs Analyst vs Deriver) |

**Connection module specification:**

| Requirement | Specification |
|---|---|
| Connection class | `SurrealDBConnection` with `connect()`, `query()`, `close()` methods |
| Configuration | URL, namespace, database name from environment variables |
| Health check | `health_check()` returns boolean, called at pipeline start |
| Connection reuse | Singleton pattern within a pipeline execution |
| Error handling | Retry with exponential backoff (3 attempts), then fail with descriptive error |
| Logging | All queries logged at DEBUG level, all mutations at INFO level |

**Writer module specification:**

| Requirement | Specification |
|---|---|
| Write functions | `write_reflection_output(workflow_id, output_type, data)` — single entry point |
| Business rules enforced | Workflow must exist, phase must be P10, data must match schema, actor must be authorized |
| Audit trail | Every write logged with: timestamp, actor_id, action, record_id, before/after snapshot |
| Idempotency | Same workflow_id + output_type + content_hash = no duplicate write |
| Error handling | Reject invalid data with descriptive error, never silently drop |
| Null handling | Reject None/empty for required fields, accept None for optional fields |

**Acceptance criteria:**
- [ ] Connection module establishes connection to SurrealDB v3 with configurable namespace/database
- [ ] Connection module retries 3 times with exponential backoff before failing
- [ ] Writer module rejects writes for non-existent workflow_ids
- [ ] Writer module rejects writes for workflows not in P10 phase
- [ ] Writer module rejects data that doesn't match the corresponding Pydantic schema
- [ ] Writer module logs all mutations with timestamp, actor_id, and action
- [ ] Writer module is idempotent for same workflow_id + output_type + content_hash

---

## 3. Prerequisite: SurrealDB Schema Update

Before any workflow code, the `design_artefacts` table must support artefact tagging.

**Specification:**

The `design_artefacts` table must have an `artefact_tags` field of type `set<string>` that supports querying by tag value. This field stores values from the set: `{"surprise", "gap", "pattern", "assessment_fragment"}`.

**Acceptance criteria:**
- [ ] `artefact_tags` field exists on `design_artefacts` table
- [ ] Field accepts multiple tag values per record
- [ ] Query `SELECT * FROM design_artefacts WHERE array::contains(artefact_tags, "surprise")` returns all surprise-tagged artefacts
- [ ] Query returns empty set (not error) when no artefacts match a tag
- [ ] Field defaults to empty set when no tags are provided during artefact creation
- [ ] Existing records without tags continue to function (backward compatible)

---

## 4. Component Specifications

### 4.1 Epistemic Type System

**Purpose:** Enforce the distinction between deterministic, probabilistic, and elicited data at the type level. This is the implementation of Regime 3 enforcement point #4 (type separation).

**Specification:**

Define three epistemic types with distinct characteristics:

| Type | Definition | Storage | Validation |
|---|---|---|---|
| Deterministic | Computed from PRISM data with no judgment | Stored as-is | Must trace to a PRISM query or calculation |
| Probabilistic | Agent-assessed with judgment | Stored with confidence level | Must carry confidence metadata |
| Elicited | Captured from humans during P0-P9 | Stored with provenance | Must carry who/when/phase metadata |

Every schema field carries an `epistemic_profile` annotation. The schema validation layer rejects outputs where epistemic types are conflated (e.g., a field marked `deterministic` that contains agent judgment).

**Acceptance criteria:**
- [ ] `EpistemicProfile` enum defined with values: `deterministic`, `probabilistic`, `elicited`
- [ ] Every output schema field has an `epistemic_profile` attribute
- [ ] Schema validation rejects an output where a deterministic field contains probabilistic or elicited content
- [ ] Schema validation rejects an output where a probabilistic field has no confidence metadata
- [ ] Schema validation rejects an output where an elicited field has no provenance metadata
- [ ] The `variance_analysis` field in O1 is typed as `probabilistic` (it involves judgment about significance)
- [ ] The `variance` field in O1 is typed as `deterministic` (it's computed from timestamps)
- [ ] The `surprise_description` field in O3 is typed as `elicited` (captured during P0-P9)

---

### 4.2 Pydantic Output Schemas (O1-O8)

**Purpose:** Typed schemas for every output of the Methodology Reflection workflow, enforcing type separation and traceability.

**Specification:**

Each schema implements the design spec's P1 output definitions. Every field has:
- Name, type, required/optional
- Epistemic profile (deterministic/probabilistic/elicited)
- Traceability (which PRISM query or processing step produces this field)
- Null handling (what happens when data is missing)

**Schema-by-schema acceptance criteria:**

**O1: PhaseDurationReport**

- [ ] All fields from design spec P1 present
- [ ] `variance` computed as `actual_duration - estimated_duration` (deterministic)
- [ ] `variance_percentage` computed as `(variance / estimated_duration) * 100` (deterministic)
- [ ] `variance_analysis` typed as probabilistic with confidence metadata
- [ ] `anomaly_flag` computed deterministically (threshold-based, not judgment)
- [ ] Every `phase_id` traces to a `design_phase_transitions` record
- [ ] Null handling: if estimated_duration is missing, `variance` and `variance_percentage` are null (not fabricated)
- [ ] Schema rejects negative duration values

**O2: QualityGateFailureLog**

- [ ] All fields from design spec P1 present
- [ ] `pattern_analysis` typed as probabilistic (Analyst judgment)
- [ ] `correlation` typed as probabilistic (Analyst judgment)
- [ ] `root_cause` and `methodology_implication` are optional but required if captured
- [ ] Every `failure_description` traces to a `design_quality_gates` record
- [ ] Null handling: if root_cause was not captured, field is null (not inferred)

**O3: DesignSurprisesRegister**

- [ ] All fields from design spec P1 present
- [ ] `description`, `expected_vs_actual`, `what_it_reveals` typed as elicited with provenance metadata
- [ ] `significance_assessment` typed as probabilistic (Analyst judgment)
- [ ] `cross_reference` typed as probabilistic (Analyst — connections to other surprises or gaps)
- [ ] `evidence_trace` is required and must reference a valid artefact ID
- [ ] Schema rejects records without `evidence_trace`
- [ ] `pattern_library_candidate` defaults to false

**O4: MethodologyGapsRegister**

- [ ] All fields from design spec P1 present
- [ ] `what_was_needed`, `what_was_provided`, `gap_description` typed as elicited
- [ ] `severity` typed as elicited (captured) or probabilistic (Analyst assessed)
- [ ] `impact_analysis` typed as probabilistic (Analyst)
- [ ] `frequency` is computed (deterministic — count of occurrences)
- [ ] `evidence_trace` is required
- [ ] Blocking gaps are flagged for Implementation Readiness Report

**O5: NewPatternsRegister**

- [ ] All fields from design spec P1 present
- [ ] `name`, `description` typed as probabilistic (Deriver — formalised from observations)
- [ ] `context_discovered` typed as deterministic (phase, task, situation)
- [ ] `generalisability` and `formalisation_status` typed as probabilistic (Deriver judgment)
- [ ] `evidence_strength` is required (Strong/Moderate/Weak)
- [ ] `evidence` traces to at least one artefact (minimum 1 trace)
- [ ] Schema rejects patterns with zero evidence traces

**O6: Recommendations**

- [ ] All fields from design spec P1 present
- [ ] `traces_to` is required with minimum 1 entry (Regime 3 enforcement — every recommendation traces to evidence)
- [ ] `evidence_strength` is required (Strong/Moderate/Weak)
- [ ] `category` restricted to: Methodology, Process, Template, Tooling
- [ ] `priority` restricted to: Critical, High, Medium, Low
- [ ] Schema rejects recommendations without `traces_to` entries (orphan recommendations auto-removed)
- [ ] `suggested_implementation` required for Critical/High priority

**O7: OverallAssessment**

- [ ] All fields from design spec P1 present
- [ ] `assessment_tensions` typed as probabilistic (Analyst — where fragments disagree)
- [ ] `assessment_confidence` restricted to: High, Medium, Low
- [ ] `data_completeness` is computed (deterministic — percentage of phases with fragments)
- [ ] Schema requires `assessment_tensions` even if empty (empty = "no tensions found")
- [ ] `biggest_strength`, `biggest_weakness`, `biggest_surprise` are synthesised (probabilistic)

**O8: MethodologyReflectionDocument**

- [ ] All fields from design spec P1 present
- [ ] References to O1-O7 are typed (not raw dicts)
- [ ] `review_questions` is required (not optional)
- [ ] `sparse_sections` is required (not optional)
- [ ] `anomaly_highlights` is required (not optional)
- [ ] `visualisations` is required (not optional)
- [ ] `confidence_in_reflection` restricted to: High, Medium, Low
- [ ] Schema validates that all referenced O1-O7 data is present or flagged as sparse

---

### 4.3 PRISM Query Templates

**Purpose:** Typed SurrealDB queries that extract P0-P9 data for Methodology Reflection processing. These are the data foundation — every downstream computation depends on these queries returning correct shapes.

**Specification:**

Six queries, one per data source. Each query:
- Has a unique `query_id` and `query_name`
- Accepts a `workflow_id` parameter
- Returns results matching the corresponding Pydantic schema
- Has explicit null handling for empty result sets
- Is idempotent (same workflow_id, same results)

**Query-by-query acceptance criteria:**

**Q1: Phase Transition Data**

- [ ] Returns all phases for the given `workflow_id`
- [ ] Each result includes: `phase_id`, `phase_name`, `phase_number`, `from_phase`, `to_phase`, `timestamp`, `actor_type`
- [ ] Includes estimated duration from `design_workflows` table
- [ ] Handles missing `estimated_duration` (returns null, not error)
- [ ] Returns empty set (not error) for non-existent `workflow_id`
- [ ] Ordered by `phase_number` ascending

**Q2: Quality Gate Records**

- [ ] Returns all quality gate records for the given `workflow_id`
- [ ] Each result includes: `phase`, `gate_layer` (Fidelity/Enrichment/CrossCutting), `result` (pass/fail), `failures`, `timestamp`
- [ ] Handles phases with no quality gate records (returns empty set)
- [ ] Returns empty set (not error) for workflows with no quality gate failures

**Q3: Surprise-Tagged Artefacts**

- [ ] Returns all `design_artefacts` where `artefact_tags` contains `"surprise"` for the given `workflow_id`
- [ ] Each result includes: `artefact_id`, `phase_discovered` (derived from phase relation), `content`, `tags`
- [ ] Returns empty set (not error) when no surprises captured — this is a valid finding, not a failure
- [ ] Includes phase relation so Analyst can organise by phase

**Q4: Gap-Tagged Artefacts**

- [ ] Returns all `design_artefacts` where `artefact_tags` contains `"gap"` for the given `workflow_id`
- [ ] Each result includes: `artefact_id`, `phase`, `content`, `tags`
- [ ] Returns empty set (not error) when no gaps captured

**Q5: Pattern-Tagged Artefacts**

- [ ] Returns all `design_artefacts` where `artefact_tags` contains `"pattern"` for the given `workflow_id`
- [ ] Each result includes: `artefact_id`, `phase`, `content`, `tags`
- [ ] Returns empty set (not error) when no patterns captured

**Q6: Assessment Fragments**

- [ ] Returns all `design_artefacts` where `artefact_tags` contains `"assessment_fragment"` for the given `workflow_id`
- [ ] Each result includes: `artefact_id`, `phase`, `content`, `tags`
- [ ] Returns empty set (not error) when no assessment fragments captured
- [ ] Includes phase relation for tension detection (fragments that disagree across phases)

**Cross-cutting acceptance criteria:**

- [ ] All queries accept `workflow_id` as parameter (no hard-coded IDs)
- [ ] All queries are idempotent (same input, same output)
- [ ] All queries handle connection errors gracefully (retry 3 times, then descriptive error)
- [ ] All queries log execution time at DEBUG level
- [ ] Q3-Q6 use the `artefact_tags` field — if this field is missing from the schema, queries fail fast with a descriptive error, not silently return empty

---

### 4.4 Agent Implementation Specifications

#### 4.4.1 Compiler Agent

**Identity:** "I compile and organise. I never add content, never interpret, never omit findings, never fill gaps with inference, never assemble flattering narratives."

**Class:** Aggregator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output (required for Pydantic schema enforcement)

**Inputs:** Processed O1-O7 outputs, review questions, visualisations, sparse report, completeness report

**Output Schema:** `MethodologyReflectionDocument` (O8 Pydantic model)

**Session State:** None required (stateless compilation)

**Progressive Autonomy:** Compilation accuracy (Shadow → Advisory → Supervised → Autonomous)

| Level | Criteria | Human Role |
|---|---|---|
| Shadow | First 10 compilations | Human checks every section |
| Advisory | ≤1 error in last 10 compilations | Human checks flagged sections |
| Supervised | ≤1 error in last 10 compilations | Human checks sparse/flagged sections only |
| Autonomous | ≤1 error in last 20 compilations | Human reviews final document post-delivery |

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never add content not in PRISM | 3 (Prevent) | Output schema validation: every field must trace to a processing step or PRISM query result |
| Never interpret data | 1 (Declare) | Prompt instruction; Regime 2 output audit for interpretation language |
| Never omit findings | 2 (Detect) | Completeness check: all phases represented, all surprise/gap/pattern records included |
| Never fill gaps with inference | 3 (Prevent) | Sparse section flagging mandatory; zero-tolerance for claims without artefact ID |
| Never assemble flattering narratives | 1 (Declare) | Tone-agnostic schema (facts only, no evaluative language in field names) |

**Null state:** "No reflection data found for [section]. The PRISM graph has no captured artefacts for this phase."

**Cost budget:** 5K-10K tokens per execution

**Acceptance criteria:**

- [ ] Agent receives O1-O7 as typed Pydantic models
- [ ] Agent produces O8 matching `MethodologyReflectionDocument` schema
- [ ] Every claim in O8 traces to a source (PRISM query result or processing step)
- [ ] Sparse sections are flagged with completeness percentage
- [ ] Review questions from Deriver are included verbatim
- [ ] Anomaly highlights from Analyst are included
- [ ] Visualisations from Analyst are referenced (chart IDs or embeddable)
- [ ] Agent output fails schema validation if any required field is missing or wrong type
- [ ] Agent produces null state for sections with no data (not fabricated content)
- [ ] Compilation takes ≤30 seconds for a typical workflow

---

#### 4.4.2 Analyst Agent

**Identity:** "I measure, correlate, and surface anomalies. I present findings, not conclusions. I never draw conclusions, never make recommendations, never interpret beyond what data supports, never smooth over contradictions."

**Class:** Measurer (calculation) + Assessor (significance assessment)

**Orientation:** Bridge-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** Raw PRISM data from Q1-Q6 queries

**Output Schema:** Analysis package including: variance calculations, anomaly flags, correlation analysis, surprise/gap de-duplication, assessment synthesis, completeness calculations, visualisations

**Session State:** None required (stateless analysis)

**Progressive Autonomy:** Two dimensions

| Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|
| Analysis accuracy | Surface analysis only | Standard analysis + anomaly flagging | Deep analysis + correlations + visualisations | Full analysis, human reviews anomalies only | ≤2 incorrect flaggings in last 10 |
| Anomaly identification | Flag only statistical outliers | Flag outliers + significant variances | Flag all anomalies with significance assessment | Flag all anomalies, human reviews critical only | ≤1 missed significant anomaly in last 10 |

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never draw conclusions | 1 (Declare) | Prompt instruction; Regime 2 output audit scanning for conclusion language |
| Never make recommendations | 3 (Prevent) | Schema validation: Analyst output schema has no recommendation fields |
| Never interpret beyond data | 1 (Declare) | Prompt instruction; Regime 2 correlation strength field required |
| Never smooth over contradictions | 2 (Detect) | Assessment tensions field required; contradictions must be surfaced, not resolved |

**Null state:** "Insufficient data for analysis in [section]. [X] of [Y] phases have data. Confidence: [Low]."

**Cost budget:** 10K-30K tokens per execution

**Acceptance criteria:**

- [ ] Agent receives raw PRISM query results as typed Pydantic models
- [ ] Agent produces analysis matching the Analyst output schema
- [ ] Agent output contains zero recommendation fields (schema prevents this structurally)
- [ ] Every correlation includes a strength assessment (Strong/Moderate/Weak/Weak)
- [ ] Every anomaly includes a significance flag
- [ ] Assessment tensions are surfaced where fragments disagree
- [ ] Data completeness is calculated as a percentage of phases with fragments
- [ ] Sparse sections are flagged with completeness percentage
- [ ] Agent produces null state for sections with insufficient data
- [ ] Analyst output never contains words like "should", "recommend", "suggest", or "we must"

---

#### 4.4.3 Deriver Agent

**Identity:** "I derive recommendations and generate review questions from evidence. Every recommendation traces to a captured artefact. Every question traces to a data point. I never recommend without evidence trace, never invent patterns not in data, never generalise beyond captured scope."

**Class:** Generator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** Processed surprises (O3), gaps (O4), pattern observations (O5), assessment fragments (O7), anomaly report, correlation analysis from Analyst

**Output Schema:** Derivation package including: formalised patterns (O5 processed), recommendations (O6), review questions

**Session State:** None required (stateless derivation)

**Progressive Autonomy:** Two dimensions

| Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|
| Pattern formalisation | Only patterns with Strong evidence | Strong + Moderate evidence | All patterns with strength assessment | All patterns, human reviews library candidates only | ≤1 untraced pattern in last 10 |
| Recommendation derivation | Only from Strong evidence | Strong + Moderate evidence | All evidence with strength assessment | All evidence, human reviews Critical/High only | ≤2 untraced recommendations in last 10 |

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never recommend without evidence trace | 3 (Prevent) | `traces_to` field required in Recommendation schema (min_items=1); schema rejects recommendations without traces |
| Never invent patterns not in data | 2 (Detect) | `formalisation_status` field required (Observed/Described/Formalised); minimum 1 artefact trace per pattern |
| Never generalise beyond captured scope | 1 (Declare) | Prompt instruction; `generalisability` field with restricted values |
| Never suggest outside methodology context | 1 (Declare) | Prompt instruction; `category` field restricted to Methodology/Process/Template/Tooling |

**Null state:** "No captured [gaps/surprises/patterns] to derive recommendations from. This is itself a finding."

**Cost budget:** 15K-40K tokens per execution

**Acceptance criteria:**

- [ ] Agent receives processed surprises, gaps, patterns, assessment data as typed Pydantic models
- [ ] Agent produces recommendations matching `Recommendations` schema
- [ ] Every recommendation has at least 1 `traces_to` entry referencing a valid artefact ID
- [ ] Schema rejects recommendations with empty `traces_to` (orphan auto-removal)
- [ ] Every recommendation has `evidence_strength` (Strong/Moderate/Weak)
- [ ] Every pattern has `formalisation_status` (Observed/Described/Formalised)
- [ ] Every pattern has at least 1 `evidence` trace
- [ ] Review questions are generated and each traces to a specific data point
- [ ] Agent produces null state when no surprises/gaps/patterns exist ("This is itself a finding")
- [ ] Deriver output never contains generic recommendations that could apply to any methodology (they must reference specific evidence from this application)

---

### 4.5 Tool Definitions

**Purpose:** Agno @tool wrappers that provide user-action-level interfaces to database operations. Agents never execute raw SurrealQL — they call tools.

**Tool-by-tool specification:**

| Tool Name | Purpose | Input | Output | Enforcement Role |
|---|---|---|---|---|
| `query_phase_transitions` | Retrieve phase transition data for a workflow | workflow_id | List[PhaseTransitionData] | User-action abstraction over Q1 |
| `query_quality_gates` | Retrieve quality gate records for a workflow | workflow_id | List[QualityGateData] | User-action abstraction over Q2 |
| `query_tagged_artefacts` | Retrieve artefacts with specific tags | workflow_id, tag (surprise/gap/pattern/assessment_fragment) | List[ArtefactData] | User-action abstraction over Q3-Q6 |
| `query_workflow_metadata` | Retrieve workflow metadata (estimated durations, etc.) | workflow_id | WorkflowMetadata | User-action abstraction over Q7 |
| `write_reflection_output` | Write a processed output to the reflection store | workflow_id, output_type (O1-O8), data | Confirmation with artefact_id | Regime 3: validates schema before write |
| `flag_sparse_section` | Flag a section as sparse with completeness percentage | workflow_id, section_name, completeness_pct, details | Confirmation | Regime 3: enforces sparse flagging requirement |

**Cross-cutting acceptance criteria:**

- [ ] No tool exposes SurrealQL syntax or table names to agents
- [ ] Every tool returns typed Pydantic models, not raw dicts
- [ ] `query_tagged_artefacts` handles empty result sets gracefully (returns empty list, not error)
- [ ] `write_reflection_output` validates data against the corresponding Pydantic schema before writing
- [ ] `write_reflection_output` rejects writes for non-existent workflow_ids
- [ ] `write_reflection_output` rejects writes for workflows not in P10 phase
- [ ] `flag_sparse_section` calculates completeness percentage deterministically (not from agent judgment)
- [ ] Every tool has a null state that returns informative empty data, not errors

---

### 4.6 Enforcement Mechanisms

**Purpose:** Implement the 5 Regime 3 enforcement points and 4 Regime 2 detection mechanisms from the design spec.

**Regime 3 (Prevent by Design) — 5 structural enforcements:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| E1 | Compiler never adds content | Output schema validation | Pydantic validator on `MethodologyReflectionDocument` that checks every field traces to a processing step. Specifically: a `source_mapping` field on O8 that maps each section to its data source (Q1-Q6 query result or processing step ID). Validator rejects O8 if any section has no source mapping. |
| E2 | Deriver never recommends without trace | `traces_to` field requirement | Pydantic `Field(min_length=1)` on `Recommendation.traces_to`. Schema rejects recommendations with empty traces_to. Runtime validation checks that referenced artefact IDs exist in PRISM. |
| E3 | No fabrication | Sparse section flagging | `sparse_sections` field is required (not optional) on O8. `flag_sparse_section` tool calculates completeness percentage deterministically. Compiler MUST call this tool for every section. |
| E4 | Type separation | Epistemic profile enforcement | Every schema field has an `epistemic_profile` annotation of type `Literal["deterministic", "probabilistic", "elicited"]`. Pydantic validator rejects outputs where field values don't match their epistemic profile (e.g., a deterministic field containing agent judgment). |
| E5 | Evidence strength required | Evidence strength field | `evidence_strength` field of type `Literal["Strong", "Moderate", "Weak"]` is required on `Recommendation` and `Pattern` schemas. Schema rejects records without this field. |

**Regime 2 (Detect After the Fact) — 4 detection mechanisms:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| D1 | Analyst never interprets beyond data | Output audit | Post-processing scan of Analyst output for conclusion language: "should", "must", "recommend", "suggest", "we believe", "in conclusion", "therefore we recommend". Report matches as potential violations. |
| D2 | Compiler never assembles flattering narratives | Tone audit | Post-processing scan of Compiler output for evaluative language: "excellent", "outstanding", "problematic" (when used without evidence), "concerning" (when used without data). Report matches. Schema enforces fact-only field names (no evaluative field names). |
| D3 | Deriver never invents patterns | Formalisation status audit | Post-processing check that every pattern has `formalisation_status` and `evidence_strength` fields populated. Patterns with `formalisation_status = "Observed"` and `evidence_strength = "Weak"` flagged for human review. |
| D4 | Progressive autonomy criteria measurable | Criteria tracking | During Shadow/Advisory/Supervised phases, track: compilation accuracy (% of sections with no errors), analysis correctness (% of flaggings that were correct), derivation traceability (% of recommendations with valid traces). Log to `runtime_health_metrics` table. |

**Regime 1 (Declare in Prompt) — 4 declarations:**

| # | Constraint | Mechanism | Location |
|---|---|---|---|
| R1-1 | Analyst never interprets beyond data | Prompt instruction | Analyst system prompt |
| R1-2 | Compiler never assembles flattering narratives | Prompt instruction | Compiler system prompt |
| R1-3 | Honest sparse flagging | Prompt instruction + deterministic calculation | Compiler system prompt + `flag_sparse_section` tool (deterministic Regime 3 for the calculation, Regime 1 for the choice to flag) |
| R1-4 | Deriver never invents patterns | Prompt instruction | Deriver system prompt |

**Acceptance criteria:**

- [ ] E1: Submitting a `MethodologyReflectionDocument` with a section that has no source mapping fails schema validation
- [ ] E2: Submitting a `Recommendation` with empty `traces_to` fails schema validation
- [ ] E3: Submitting an O8 without `sparse_sections` fails schema validation
- [ ] E4: Submitting a deterministic field with probabilistic content fails schema validation
- [ ] E5: Submitting a `Recommendation` without `evidence_strength` fails schema validation
- [ ] D1: Analyst output containing "should", "recommend", or "suggest" triggers an audit flag (not a rejection)
- [ ] D2: Compiler output containing evaluative field names triggers an audit flag
- [ ] D3: Deriver patterns with "Observed" status and "Weak" evidence are flagged for human review
- [ ] D4: Health metrics are logged per execution for each autonomy dimension
- [ ] All Regime 1 instructions are present in corresponding agent prompts

---

### 4.7 Wave Orchestration

**Purpose:** Coordinate the 4-wave execution pipeline (Data → Analysis → Derivation → Compilation).

**Specification:**

Wave execution is sequential with dependency enforcement. Each wave must complete before the next begins. The orchestrator is responsible for:

1. Verifying prerequisites (data availability, schema compatibility)
2. Invoking agents in wave order
3. Passing outputs between waves as typed Pydantic models
4. Handling failures at each wave (fallback model)
5. Logging execution metadata for progressive autonomy tracking

**Wave dependency map:**

| Wave | Depends On | Produces | Failure Action |
|---|---|---|---|
| Wave 1: Data | Schema verification (T1-T3) | Raw PRISM data (Q1-Q6 results) | If critical data missing (Q1, Q2, Q7), halt with descriptive error. If non-critical data missing (Q3-Q6), flag as sparse and continue. |
| Wave 2: Analysis | Wave 1 complete | O1 processed, O2 processed, anomaly report, correlation analysis, completeness report, visualisations | If Analyst fails, attempt retry once. If retry fails, produce minimal analysis with "Insufficient analysis" flag. |
| Wave 3: Derivation | Wave 2 complete | O5 processed, O6 draft, review questions | If Deriver fails, attempt retry once. If retry fails, produce minimal derivation with "Insufficient evidence for derivation" flag. |
| Wave 4: Compilation | Waves 2-3 complete | O8 final | If Compiler fails, attempt retry once. If retry fails, produce raw data package with "Compilation failed" flag. |

**Orchestrator specification:**

| Property | Value |
|---|---|
| Composition | Agno Team with 3 member agents (Compiler, Analyst, Deriver) |
| Orchestrator mode | Sequential (coordinate mode — waves run in order) |
| State management | Workflow state stored in `design_workflows` table (phase: P10, status: in_progress) |
| Error handling | Per-wave retry (1 attempt), then fallback to minimal output |
| Logging | All wave transitions logged to `runtime_events` (CHANGEFEED) |
| Human gates | None during production (human review is post-delivery) |

**Acceptance criteria:**

- [ ] Wave 1 does not start until schema verification (T1-T3) passes
- [ ] Wave 2 does not start until all Wave 1 queries complete (or fail gracefully)
- [ ] Wave 3 does not start until Wave 2 produces analysis output
- [ ] Wave 4 does not start until Waves 2-3 produce their outputs
- [ ] Missing critical data (Q1, Q2, Q7) halts the pipeline with descriptive error
- [ ] Missing non-critical data (Q3-Q6) flags sections as sparse and continues
- [ ] Each wave logs start time, end time, and status to `runtime_events`
- [ ] Failed wave retry happens exactly once before fallback
- [ ] Final output is a valid `MethodologyReflectionDocument` or a minimal fallback with sparse flagging

---

### 4.8 Seed Data Specification

**Purpose:** Provide test data for development, testing, and progressive autonomy tracking. Seed data simulates a completed P0-P9 workflow with realistic artefact tags.

**Specification:**

Four seed scripts (not written here, just specified):

**Seed 1: Sample Workflow**

- Creates a `design_workflows` record representing a completed P0-P9 workflow
- Includes: workflow_id, workflow_name, domain, created_at, current_phase (P10), estimated durations per phase
- Must include realistic estimated durations that differ from actual durations (to enable variance analysis)

**Seed 2: Sample Phase Transitions**

- Creates 10 `design_phase_transitions` records (P0→P1 through P9→P10)
- Each includes: from_phase, to_phase, timestamp, actor_type, trigger_type
- Must include at least one phase that took significantly longer than estimated (for anomaly testing)
- Must include at least one phase that went through iterations (iteration_count > 1)

**Seed 3: Sample Quality Gates**

- Creates `design_quality_gates` records for at least 3 phases
- Must include at least 2 gate failures (one Enrichment, one CrossCutting)
- Must include at least one gate failure that correlates with a duration overrun

**Seed 4: Sample Artefacts with Tags**

- Creates `design_artefacts` records with appropriate tags
- Must include: at least 3 surprise-tagged artefacts, at least 2 gap-tagged artefacts, at least 1 pattern-tagged artefact, at least 2 assessment_fragment artefacts
- Must include at least one pair of assessment fragments that disagree (for tension detection testing)
- Must include artefacts spanning at least 4 different phases
- Must include at least one phase with no tagged artefacts (for sparse data testing)

**Acceptance criteria:**

- [ ] Seed scripts create a complete P0-P9 data set in SurrealDB
- [ ] Running all 4 seeds in order produces a testable workflow state
- [ ] Seed data includes at least one anomaly (duration variance > 2 standard deviations)
- [ ] Seed data includes at least one quality gate failure
- [ ] Seed data includes conflicting assessment fragments for tension detection testing
- [ ] Seed data includes a phase with no tagged artefacts for sparse data testing
- [ ] Seed scripts are idempotent (running twice produces same state)
- [ ] Seed scripts can be cleaned up (delete all test data)

---

### 4.9 Test Specifications

**Purpose:** Verify that design constraints are enforced and failure modes are detected.

**Test-by-test specification:**

**T25: Fabrication Test (FM1)**

- [ ] **Purpose:** Verify that the Compiler cannot produce claims without artefact IDs
- [ ] **Method:** Inject content into Compiler input that doesn't trace to any PRISM data. Verify schema validation rejects the output.
- [ ] **Expected result:** Schema validation rejects O8 with untraced claims
- [ ] **Failure mode tested:** FM1 (fabrication, RPN 160)

**T26: False Correlation Test (FM3)**

- [ ] **Purpose:** Verify that Analyst output does not contain conclusion language
- [ ] **Method:** Submit data with a suggestive but not conclusive correlation. Verify Analyst output contains correlation strength and no conclusion statements.
- [ ] **Expected result:** Analyst reports correlation with strength assessment but no "should", "recommend", or "suggest"
- [ ] **Failure mode tested:** FM3 (false correlation, RPN 120)

**T26b: Sparse Data as Comprehensive Test (FM6)**

- [ ] **Purpose:** Verify that sparse sections are flagged, not presented as comprehensive
- [ ] **Method:** Submit data where 3 of 10 phases have no artefacts. Verify Compiler flags those sections as sparse with completeness percentages.
- [ ] **Expected result:** Sparse sections flagged with ≤30% completeness; comprehensive sections have ≥80% completeness
- [ ] **Failure mode tested:** FM6 (sparse data as comprehensive, RPN 135)

**T27: No Surprises as Success Test (FM9)**

- [ ] **Purpose:** Verify that empty result sets are treated as data points, not failures
- [ ] **Method:** Submit data with 0 surprise-tagged artefacts. Verify O3 correctly documents "0 captured surprises" as a finding.
- [ ] **Expected result:** O3 contains "No captured surprises" as a valid finding, not an error or empty section
- [ ] **Failure mode tested:** FM9 (no surprises as success, RPN 120)

**T28: Type Separation Test**

- [ ] **Purpose:** Verify that epistemic profiles are preserved in implementation
- [ ] **Method:** Submit data with known deterministic fields (variance calculation), probabilistic fields (significance assessment), and elicited fields (surprise description). Verify each field carries its correct epistemic profile in the output.
- [ ] **Expected result:** All fields carry correct `epistemic_profile` annotations; schema validation rejects type conflation
- [ ] **Cross-cutting concern tested:** CC-3 (epistemic metadata), E4 (type separation enforcement)

**T29: Evidence Trace Test**

- [ ] **Purpose:** Verify that every recommendation traces to at least one captured artefact
- [ ] **Method:** Submit data with known gaps and patterns. Verify every recommendation has at least one `traces_to` entry referencing a valid artefact ID.
- [ ] **Expected result:** All recommendations have ≥1 traces_to entry; orphan recommendations are auto-removed
- [ ] **Cross-cutting concern tested:** E2 (traces_to enforcement), Regime 3

**T30: Integration Test (4-Wave Pipeline)**

- [ ] **Purpose:** Verify end-to-end pipeline execution with realistic data
- [ ] **Method:** Run full pipeline with seed data (all 4 seed scripts). Verify Wave 1 produces raw data, Wave 2 produces analysis, Wave 3 produces derivation, Wave 4 produces O8.
- [ ] **Expected result:** Complete `MethodologyReflectionDocument` with all sections populated or flagged as sparse; no schema validation errors; all traces reference valid artefact IDs
- [ ] **Integration tested:** Full pipeline dependency chain

**T31: End-to-End Test with Edge Cases**

- [ ] **Purpose:** Verify pipeline handles edge cases correctly
- [ ] **Method:** Run pipeline with: (1) a workflow with no surprises, (2) a workflow with conflicting assessment fragments, (3) a workflow with sparse data in 2 phases, (4) a workflow with a significant duration anomaly.
- [ ] **Expected result:** (1) "No captured surprises" documented as finding, (2) Assessment tensions surfaced, (3) Sparse sections flagged with percentages, (4) Anomaly flagged with significance assessment
- [ ] **Integration tested:** Edge case handling

---

## 5. Build Order

| Order | Task ID | Task | Wave | Depends On | Essential | Effort |
|---|---|---|---|---|---|---|
| 1 | T1 | Verify SurrealDB schema has artefact_tags | Foundation | — | ✅ | Small |
| 2 | T2 | Verify design_phase_transitions fields | Foundation | — | ✅ | Small |
| 3 | T3 | Verify design_quality_gates fields | Foundation | — | ✅ | Small |
| 4 | T4 | Define O1-O8 Pydantic output schemas | Foundation | T1-T3 | ✅ | Medium |
| 5 | T5 | Map epistemic profiles to schema fields | Foundation | T4 | ✅ | Small |
| 6 | T6 | Map enforcement regimes to constraints | Foundation | T4 | ✅ | Small |
| 7 | T7 | Write PRISM query for phase transitions | Data | T1-T3 | ✅ | Small |
| 8 | T8 | Write PRISM query for quality gates | Data | T1-T3 | ✅ | Small |
| 9 | T9 | Write PRISM query for surprise artefacts | Data | T1-T3 | ✅ | Small |
| 10 | T10 | Write PRISM query for gap artefacts | Data | T1-T3 | ✅ | Small |
| 11 | T11 | Write PRISM query for pattern artefacts | Data | T1-T3 | ✅ | Small |
| 12 | T12 | Write PRISM query for assessment fragments | Data | T1-T3 | ✅ | Small |
| 13 | T13 | Test all PRISM queries against seed data | Data | T7-T12, seeds | ✅ | Medium |
| 14 | T14 | Write Compiler agent instructions | Agent | T4-T5 | ✅ | Large |
| 15 | T15 | Write Analyst agent instructions | Agent | T4-T5 | ✅ | Large |
| 16 | T16 | Write Deriver agent instructions | Agent | T4-T5 | ✅ | Large |
| 17 | T17 | Define progressive autonomy dimensions | Agent | T14-T16 | ✅ | Small |
| 18 | T18 | Define cost budgets per agent | Agent | T14-T16 | ✅ | Small |
| 19 | T19 | Define tool wrappers for PRISM queries | Integration | T7-T12 | ✅ | Medium |
| 20 | T20 | Define tool wrapper for write operations | Integration | T4 | ✅ | Small |
| 21 | T21 | Implement wave orchestration | Integration | T14-T18, T19-T20 | ✅ | Medium |
| 22 | T22 | Implement Regime 3 enforcement | Integration | T4-T6 | ✅ | Medium |
| 23 | T23 | Implement Regime 2 detection | Integration | T6 | ✅ | Small |
| 24 | T24 | Implement null-state handling per agent | Integration | T14-T16 | ✅ | Small |
| 25 | T25 | Test FM1 (fabrication) | Test | T22 | ✅ | Medium |
| 26 | T26 | Test FM3 (false correlation) | Test | T15, T23 | ✅ | Medium |
| 27 | T26b | Test FM6 (sparse data) | Test | T22 | ✅ | Small |
| 28 | T27 | Test FM9 (no surprises) | Test | T9 | ✅ | Small |
| 29 | T28 | Test type separation | Test | T4-T5, T22 | ✅ | Medium |
| 30 | T29 | Test evidence trace | Test | T16, T22 | ✅ | Small |
| 31 | T30 | Integration test (4-wave pipeline) | Test | T21 | ✅ | Medium |
| 32 | T31 | End-to-end test with edge cases | Test | T21, seeds | ✅ | Medium |
| 33 | T32 | Assemble build order | Compilation | T1-T31 | ✅ | Small |
| 34 | T33 | Compile enforcement regime summary | Compilation | T22-T23 | ✅ | Small |
| 35 | T34 | Progressive autonomy deployment plan | Compilation | T17 | ✅ | Small |
| 36 | T35 | Integration notes | Compilation | T1-T31 | ✅ | Small |
| 37 | T36 | Assemble final implementation plan | Compilation | T32-T35 | ✅ | Small |

**Critical path:** T1 → T4 → T7-T12 → T13 → T14-T16 → T19-T20 → T21 → T22-T24 → T25-T31 → T32-T36

**Time estimate:** 2-3 weeks for one developer with Agno and SurrealDB experience.

---

## 6. Enforcement Regime Summary

| Regime | Count | Mechanisms |
|---|---|---|
| Regime 3 (Prevent) | 5 | Schema validation (E1), traces_to field requirement (E2), sparse flagging requirement (E3), epistemic type separation (E4), evidence strength requirement (E5) |
| Regime 2 (Detect) | 4 | Conclusion language audit (D1), narrative tone audit (D2), pattern formalisation audit (D3), autonomy criteria tracking (D4) |
| Regime 1 (Declare) | 4 | Analyst interpretation instruction (R1-1), Compiler narrative instruction (R1-2), Honest sparse flagging instruction (R1-3), Deriver pattern instruction (R1-4) |

**Total: 5 structural enforcements, 4 detections, 4 declarations.**

This is an honest assessment. The implementation cannot structurally prevent an analyst from interpreting (Regime 1) or a compiler from assembling flattering narratives (Regime 1). What it CAN do is enforce type separation, evidence traces, and sparse flagging structurally (Regime 3), and detect conclusion language and untraced recommendations after the fact (Regime 2).

---

## 7. Progressive Autonomy Deployment Plan

**Starting level:** Shadow for all agents and dimensions.

| Agent | Dimension | Shadow Criteria | Advisory Criteria | Supervised Criteria | Autonomous Criteria |
|---|---|---|---|---|---|
| Compiler | Compilation accuracy | First 10 compilations: human checks every section | ≤1 error in last 10 compilations: human checks flagged sections only | ≤1 error in last 10 compilations: human checks sparse/flagged sections | ≤1 error in last 20 compilations: human reviews final document post-delivery |
| Analyst | Analysis depth | First 10 analyses: surface-level only | ≤2 incorrect flaggings in last 10: standard analysis + anomaly flagging | ≤2 incorrect flaggings in last 10: deep analysis + correlations + visualisations | ≤2 incorrect flaggings in last 10: full analysis, human reviews anomalies only |
| Analyst | Anomaly identification | First 10 analyses: flag statistical outliers only | ≤1 missed significant anomaly in last 10: flag outliers + significant variances | ≤1 missed anomaly in last 10: flag all anomalies with significance | ≤1 missed anomaly in last 10: flag all, human reviews critical only |
| Deriver | Pattern formalisation | First 10 derivations: only Strong evidence patterns | ≤1 untraced pattern in last 10: Strong + Moderate evidence | ≤1 untraced pattern in last 10: all patterns with strength assessment | ≤1 untraced pattern in last 10: all patterns, human reviews library candidates |
| Deriver | Recommendation derivation | First 10 derivations: only from Strong evidence | ≤2 untraced recommendations in last 10: Strong + Moderate evidence | ≤2 untraced recommendations in last 10: all evidence with strength assessment | ≤2 untraced in last 10: all evidence, human reviews Critical/High priority |

**Promotion tracking:** Log each execution's results to `runtime_health_metrics` table. Calculate rolling averages over last 10-20 executions. Promote when criteria are met consistently.

**Demotion criteria:** If an agent produces 2+ errors in a single execution at any level, demote one level. If an agent produces a critical error (fabrication, fabricated pattern, untraced recommendation), demote to Shadow immediately.

---

## 8. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Schema missing artefact_tags | Low (if T1-T3 verified) | Critical (blocks entire workflow) | Verify in T1-T3 before any other work. Add artefact_tags if missing. |
| PRISM query returns wrong shape | Medium | High (breaks data pipeline) | Test all queries against seed data in T13. Add null handling for missing fields. |
| Epistemic types conflated in implementation | Medium | Medium (undermines type separation principle) | Enforce in Pydantic schemas (E4). Test in T28. |
| Agent instructions don't enforce never-rules | Medium | High (enables FM1, FM3, FM8) | Human review of T14-T16 (human-primary tasks). Regime 2 detection (D1-D4). Test in T25-T27. |
| Enforcement bypassed structurally | Low | Critical (defeats trust architecture) | Test in T25-T29. Document as Regime 1/2 with mitigation if Regime 3 not possible. |
| Null state not tested | Medium | Medium (produces errors instead of informative null states) | Add null state handling in T24. Test in T27. |
| Progressive autonomy criteria not measurable | Low | Low | Define concrete metrics in T34. Track in runtime_health_metrics. |
| Build order dependency error | Low | High (creates rework) | Verify dependency chain in T32. Test in T30. |

---

This specification covers every component needed to build the Methodology Reflection Workflow, from database schema verification through seed data, agent instructions, enforcement mechanisms, orchestration, and testing. Each component has acceptance criteria that map directly back to the design spec's failure modes and quality gates.The implementation specification is complete. Here's what it delivers and what it deliberately doesn't:

**What it delivers:**

- Every component needed to build the workflow, with acceptance criteria that trace back to design spec failure modes
- An honest enforcement regime assessment: 5 things we can prevent structurally, 4 we can only detect, 4 we can only declare
- A build order with dependencies, effort estimates, and a critical path
- Progressive autonomy criteria that are measurable (not vague)
- Seed data specifications (not scripts) for testing

**What it deliberately doesn't deliver:**

- Code — this is a specification, not an implementation. The implementers choose the patterns.
- Deployment configuration — out of scope as specified.
- Agent configuration patterns matching existing agents — the implementers choose how to structure Agno agents, teams, or workflows based on their evolving architecture.

**The single most important verification step:** T1 — confirming `artefact_tags` exists on `design_artefacts`. Everything else flows from data that field enables. If it doesn't exist, nothing else in this specification matters until it's added.

Ready for the next step, or do you want to drill into any component?

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-05-21T12:53:22* · `glm-5.1:cloud` · `b4cc1cd2...`

### Prompt

create an implementation plan for the following workflow. this workflow precedes the reflection workflow.

***
# CAWDP Application Phase 10.10: Confidence Map

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
***

### Response

# Confidence Map Workflow: Implementation Specification

---

## 1. Project Structure

```
cawdp/
├── db/
│   ├── connection.py                    # Shared (existing from Methodology Reflection)
│   ├── writer.py                        # Shared (existing from Methodology Reflection)
│   └── queries/
│       ├── base.py                       # Shared
│       ├── phase_transitions.py          # Methodology Reflection
│       ├── quality_gates.py              # Methodology Reflection
│       ├── artefacts.py                  # Methodology Reflection
│       ├── specification_sections.py     # NEW — Confidence Map Q1
│       ├── stakes_levels.py             # NEW — Confidence Map Q2
│       ├── test_executions.py           # NEW — Confidence Map Q3
│       ├── epistemic_metadata.py        # NEW — Confidence Map Q4
│       ├── validation_records.py        # NEW — Confidence Map Q5
│       ├── assessment_fragments_conf.py # NEW — Confidence Map Q6
│       ├── pattern_matches.py           # NEW — Confidence Map Q7
│       └── specification_aging.py       # NEW — Confidence Map Q8
│
├── schemas/
│   ├── epistemic.py                     # Shared (existing)
│   ├── outputs/
│   │   ├── ... (Methodology Reflection schemas)
│   │   ├── section_confidence.py         # Confidence Map O1
│   │   ├── risk_priority.py             # Confidence Map O2
│   │   ├── confidence_actions.py         # Confidence Map O3
│   │   ├── confidence_tensions.py        # Confidence Map O4
│   │   ├── visual_confidence_map.py     # Confidence Map O5
│   │   ├── review_questions_conf.py     # Confidence Map O6
│   │   ├── confidence_summary.py         # Confidence Map O7
│   │   └── confidence_map_document.py   # Confidence Map O8
│   └── contracts/
│       ├── compiler_conf.py             # Confidence Map Compiler
│       ├── analyst_conf.py              # Confidence Map Analyst
│       └── deriver_conf.py               # Confidence Map Deriver
│
├── agents/
│       ├── ... (Methodology Reflection agents)
│       ├── confidence_analyst.py         # Confidence Map Analyst
│       ├── confidence_deriver.py         # Confidence Map Deriver
│       └── confidence_compiler.py        # Confidence Map Compiler
│
├── tools/
│       ├── reflection_tools.py           # Shared (extended)
│       └── confidence_tools.py           # NEW — Confidence Map tools
│
├── enforcement/
│       ├── ... (Methodology Reflection enforcement)
│       └── confidence_enforcement.py     # NEW — Confidence Map specific
│
├── pipeline/
│       ├── orchestration.py              # Shared (extended)
│       └── confidence_pipeline.py        # NEW — Confidence Map specific
│
└── seeds/
    └── confidence_map/                   # NEW — Confidence Map seed data
        ├── sample_specification.py
        ├── sample_stakes.py
        ├── sample_gates.py
        ├── sample_tests.py
        └── sample_artefacts_conf.py
```

**Rationale:** Builds on the Methodology Reflection structure. Shared infrastructure (`db/connection.py`, `db/writer.py`, `db/queries/base.py`, `schemas/epistemic.py`, `enforcement/schema_validation.py`) is reused. Workflow-specific files are namespaced by workflow (`_conf` suffix for Confidence Map specific). This allows both workflows to coexist without conflicts.

---

## 2. SurrealDB Connection

Same recommendation as Methodology Reflection: shared connection module with CAWDP-aware writer layer. No changes needed.

---

## 3. Prerequisites

### 3.1 Artefact Tags (Shared with Methodology Reflection)

Same prerequisite as Methodology Reflection: `design_artefacts` must have `artefact_tags` field of type `set<string>`.

**Acceptance criteria:** Same as Methodology Reflection specification.

### 3.2 Stakes Classification Data (NEW — Critical for Confidence Map)

The Confidence Map has a structural prerequisite that the Methodology Reflection does not: **stakes levels per specification section.**

The Confidence Map cannot produce risk-calibrated priorities without knowing which sections are high-stakes (harm-capable agents, critical handoffs, irreversible decisions) and which are low-stakes (routine configuration, easily reversible settings).

**Specification:**

Every specification section produced during P0-P9 must have an associated stakes classification derived from:
1. Harm assessment (from P7 agent design — does this agent's output affect external harm?)
2. Reversibility (from P2 capability allocation — how reversible is this decision?)
3. Authority boundaries (from P7/P8 — who has final authority and how critical is that boundary?)

The stakes levels are:

| Stakes Level | Criteria |
|---|---|
| Critical | Harm-capable agent (SuggestionRisk), irreversible decision, human-life or significant financial impact |
| High | Human-only authority boundary, difficult to reverse, significant but not critical impact |
| Medium | Collaborative authority boundary, moderately reversible, moderate impact |
| Low | Agent-only authority boundary, easily reversible, low impact |

**Acceptance criteria:**

- [ ] `design_agent_specifications` table has fields for harm assessment (two-category: direct output harm, indirect data harm)
- [ ] `design_tasks` table has fields for reversibility classification
- [ ] `design_contracts` table has fields for authority boundary type (onlyHumanAuthority, onlyRole, etc.)
- [ ] A query can retrieve stakes classification for each specification section by joining agent specifications, tasks, and contracts
- [ ] Sections without harm assessment data default to "High" stakes (conservative default — assume high stakes until proven otherwise)
- [ ] The conservative default is enforced structurally: absent data → "High" stakes, not "Low" or "Medium"

### 3.3 Test Execution Results (High but Best-Effort)

The Confidence Map needs test execution data to calculate `test_evidence` in O1. However, test execution results may not exist for all specifications.

**Specification:**

If `runtime_test_executions` table has results for the workflow, use them. If not, set `test_evidence: None` honestly — do not default to `Weak` or `Moderate`.

**Acceptance criteria:**

- [ ] Query for test execution results returns results if they exist, empty set if they don't (not an error)
- [ ] `test_evidence: None` is a valid value in the O1 schema (not `Weak`, not `Moderate`)
- [ ] Sections with `test_evidence: None` are flagged in meta-confidence as having a significant evidence gap

---

## 4. Component Specifications

### 4.1 Pydantic Output Schemas (O1-O8)

**Purpose:** Typed schemas for every output of the Confidence Map workflow, enforcing type separation, source distinction, and traceability.

**Schema-by-schema acceptance criteria:**

**O1: SectionConfidence (with confidence_detail sub-object)**

- [ ] All fields from design spec P1 present including the full `confidence_detail` sub-object
- [ ] `confidence_level` restricted to: High, Medium, Low (no "Unassessed" — sparse sections use the O8 `sparse_sections` mechanism)
- [ ] `confidence_score` is a float 0-1 (not a label — enables sorting and comparison)
- [ ] `confidence_sources` lists which evidence types contributed (deterministic field)
- [ ] `evidence_trace` links to specific PRISM artefacts (deterministic field)
- [ ] `evidence_completeness` is a computed percentage (deterministic)
- [ ] `evidence_gaps` lists what's missing (probabilistic — Analyst judgment)
- [ ] `stakes_level` restricted to: Critical, High, Medium, Low (derived from harm assessment + reversibility)
- [ ] `last_validated` is a datetime (deterministic)
- [ ] `confidence_detail.test_evidence` restricted to: Strong/Moderate/Weak/None
- [ ] `confidence_detail.gate_evidence` restricted to: Strong/Moderate/Weak/None
- [ ] `confidence_detail.epistemic_metadata_quality` restricted to: Strong/Moderate/Weak/None
- [ ] `confidence_detail.validation_evidence` restricted to: Strong/Moderate/Weak/None
- [ ] `confidence_detail.expert_judgment` restricted to: Strong/Moderate/Weak/None
- [ ] `confidence_detail.pattern_evidence` restricted to: Strong/Moderate/Weak/None
- [ ] `confidence_detail.data_completeness` is a computed percentage (deterministic)
- [ ] Schema rejects a section score with `confidence_level: "Medium"` when `evidence_completeness < 30%` (no defaulting to Medium when evidence is thin — this is Regime 3 enforcement point #2)
- [ ] Every section in the specification has a corresponding O1 entry or is listed in O8 `sparse_sections`

**O2: RiskCalibratedPriorityMap**

- [ ] `risk_zone` is computed from `confidence_level` × `stakes_level` using the design spec matrix (Act Now, Review Before Deploy, Proceed with Awareness, Proceed with Confirmation, Proceed)
- [ ] Risk zone assignment is deterministic — given confidence and stakes, the zone is computed, not assigned
- [ ] `attention_percentage` is computed (not subjective) based on risk zone distribution
- [ ] No section receives >40% attention (F7 cap enforcement)
- [ ] Attention percentages sum to approximately 100%
- [ ] Every section has a risk zone assignment or is flagged as "unclassified" (for missing stakes data)
- [ ] Unclassified sections default to the most conservative risk zone for their confidence level

**O3: ConfidenceRaisingActions**

- [ ] `traces_to_gap` is required (Regime 3 enforcement — every action traces to an evidence gap)
- [ ] Schema rejects actions with empty `traces_to_gap`
- [ ] `action_type` restricted to: RunTest, ValidateSchema, VerifyBoundary, SeekExpertReview, PopulateMissingFields, ConductStressTest, ReviewPatternMatch
- [ ] `effort_estimate` restricted to: Low, Medium, High
- [ ] `target_confidence` restricted to: Medium, High (not Low — you don't target Low)
- [ ] Every action in an Act Now or Review Before Deploy section has at least one confidence-raising action
- [ ] Actions are specific, not generic ("Run boundary verification on Section 7 authority boundary" not "More testing needed")

**O4: ConfidenceTensions**

- [ ] `source_a` and `source_b` include both evidence type and specific artefact reference
- [ ] `nature_of_disagreement` describes what the disagreement is about (probabilistic)
- [ ] `resolution_options` are specific and feasible (Deriver)
- [ ] `review_question` is traced to a specific data point (not generic)
- [ ] `severity` is assessed based on stakes — high-stakes disagreements are High severity regardless of the confidence difference

**O5: VisualConfidenceMap**

- [ ] `primary_view` is a 3×4 matrix (confidence rows × stakes columns) with sections positioned in their risk zones
- [ ] Colour coding: Act Now = red, Review Before Deploy = amber, Proceed with Awareness = yellow, Proceed with Confirmation = green outline, Proceed/Confirmed = green
- [ ] `detail_view` provides per-section drill-down to O1 data
- [ ] `temporal_view` is optional (only if temporal data available)
- [ ] `legend` is required and explains colour coding and risk zone definitions
- [ ] `accessibility_description` provides text equivalent for screen readers

**O6: ReviewQuestions**

- [ ] `traces_to` links to a specific evidence artefact or gap (not generic)
- [ ] `question_type` restricted to: DeploymentDecision, ConfidenceJudgment, EvidenceGap, TensionResolution, SpecificationAdequacy
- [ ] `urgency` matches `risk_zone` from O2 (not independently assigned)
- [ ] Every Act Now section has at least one question
- [ ] Questions are specific ("Section 7 has no test evidence for its authority boundary — should deployment proceed without it?" not "Is this section validated?")

**O7: ConfidenceSummary**

- [ ] `overall_confidence` is weighted by stakes (not simple average)
- [ ] `deployment_readiness` is computed from risk zones: Ready (no Act Now), ConditionallyReady (Act Now with viable actions), NotReady (Act Now without viable actions)
- [ ] `highest_priority_action` is specific and actionable
- [ ] `data_quality_assessment` is computed from evidence completeness across all sections
- [ ] `confidence_trajectory` is present only if temporal data is available

**O8: ConfidenceMapDocument**

- [ ] All O1-O7 references are typed
- [ ] `confidence_in_assessment` is required (meta-confidence — how confident are we in our confidence?)
- [ ] `sparse_sections` is required (sections with too little evidence to assess)
- [ ] `specification_aging_flags` is required (sections where confidence assessment is >30 days old)
- [ ] Schema validates that all referenced data is present or flagged

---

### 4.2 PRISM Query Templates

**Purpose:** Typed SurrealDB queries that extract specification data for confidence assessment.

**Query-by-query acceptance criteria:**

**Q1: Specification Sections**

- [ ] Returns all specification sections for the given `workflow_id`
- [ ] Each result includes: section_id, section_name, section_type, content, artefact_tags
- [ ] Sections include agent specifications, contracts, tasks, quality gates, and other P0-P9 outputs stored in PRISM
- [ ] Returns empty set (not error) for non-existent workflow_id

**Q2: Stakes Levels Per Section**

- [ ] Returns harm assessment, reversibility classification, and authority boundary type for each section
- [ ] Derives stakes level from harm assessment + reversibility using the design spec criteria table
- [ ] Sections without harm assessment data default to "High" (conservative)
- [ ] Returns empty set (not error) for sections without stakes data — these are flagged as "unclassified"

**Q3: Test Execution Results**

- [ ] Returns test execution results from `runtime_test_executions` for the given workflow
- [ ] Each result includes: test_id, test_name, result (pass/fail/pending), evidence_produced, timestamp
- [ ] Returns empty set (not error) when no test results exist — this is valid (tests may not have been executed)
- [ ] "Pending" results are distinct from "no result" — pending means a test exists but hasn't run

**Q4: Quality Gate Outcomes**

- [ ] Returns all quality gate records for the given workflow (shared with Methodology Reflection Q2)
- [ ] Each result includes: phase, gate_layer, result (pass/fail), failures
- [ ] Gate pass/fail is core evidence for confidence assessment

**Q5: Epistemic Metadata Completeness**

- [ ] Returns CC-3 field completeness for each specification section
- [ ] Each result includes: section_id, fields_expected, fields_populated, fields_with_confidence, fields_with_provenance, fields_with_recency, completeness_percentage
- [ ] Completeness < 50% = Weak evidence; 50-80% = Moderate; > 80% = Strong
- [ ] Returns empty set (not error) for sections without CC-3 data — these default to "None"

**Q6: Assessment Fragments (Confidence-relevant)**

- [ ] Returns assessment fragments tagged with confidence-relevant terms
- [ ] Filters `design_artefacts` where `artefact_tags` contains "assessment_fragment" AND content relates to confidence, validation, or reliability
- [ ] Returns empty set (not error) when no confidence-relevant fragments exist

**Q7: Pattern Match Data**

- [ ] Returns pattern-tagged artefacts that relate to validation evidence
- [ ] Each result includes: pattern_id, pattern_name, formalisation_status, evidence_strength
- [ ] Returns empty set (not error) when no patterns exist

**Q8: Specification Aging Data**

- [ ] Returns `design_artefacts` with assessedAt timestamps for the given workflow
- [ ] Each result includes: artefact_id, section_id, assessedAt, last_modified
- [ ] Calculates days since assessment for each section
- [ ] Flags sections assessed >30 days ago as "potentially stale"

**Cross-cutting acceptance criteria:**

- [ ] All queries accept `workflow_id` as parameter
- [ ] All queries are idempotent
- [ ] All queries handle connection errors gracefully (retry 3 times, then descriptive error)
- [ ] All queries log execution time at DEBUG level
- [ ] Q2 enforces conservative default: absent stakes data → "High" stakes
- [ ] Q3 distinguishes between "no tests" (valid) and "tests pending" (different evidence value)
- [ ] Q5 handles sections without CC-3 data as "None" evidence, not "Weak"

---

### 4.3 Agent Implementation Specifications

#### 4.3.1 Analyst Agent (Confidence Map)

**Identity:** "I measure evidence quality and assess confidence. I present findings, not conclusions. I never round up confidence, never smooth over tensions, never inflate thin evidence, never treat absence as evidence of absence, never make deployment recommendations."

**Class:** Measurer + Assessor

**Orientation:** Bridge-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** Evidence package from Q1-Q9 queries

**Output Schema:** SectionConfidence (O1) + RiskCalibratedPriorityMap (O2) + ConfidenceTensions (O4) + VisualConfidenceMap (O5) components + data_quality (O7 component) + meta_confidence + sparse_report

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never round up confidence | 2 (Detect) | confidence_detail shows all sources; boundary cases surfaced as tensions; Regime 2 audit for systematic rounding |
| Never smooth over tensions | 3 (Prevent) | Tension surfacing task (T15) mandatory; schema requires tensions field on O4 |
| Never inflate thin evidence | 2 (Detect) | evidence_completeness percentage is deterministic; thin evidence (<30%) flagged; Regime 2 audit for "Moderate" on <30% evidence |
| Never treat absence as evidence of absence | 3 (Prevent) | Schema rejects test_evidence: "Weak" when test results don't exist — must be "None" |
| Never make deployment recommendations | 3 (Prevent) | Schema has no deployment_recommendation fields on Analyst output |

**Null state:** "Insufficient evidence to assess confidence for [section]. Evidence completeness: [X]%. Primary gap: [specific missing evidence type]. Stakes: [level]. Recommended risk zone: [conservative default]."

**Cost budget:** 15K-40K tokens

**Progressive autonomy:** Three dimensions as specified in P7.

**Acceptance criteria:**

- [ ] Agent receives evidence package as typed Pydantic models
- [ ] Agent produces O1 with confidence_detail for every section
- [ ] Agent produces O2 with risk zones computed from confidence × stakes (deterministic calculation, not subjective assignment)
- [ ] Agent produces O4 with tensions surfaced where evidence sources disagree
- [ ] Analyst output contains zero deployment recommendation fields (schema prevents structurally)
- [ ] Every section with `evidence_completeness < 30%` is flagged as sparse, not defaulted to "Low" confidence
- [ ] Sections without stakes data default to "High" stakes (conservative)
- [ ] Counter-intuitive results (F5) are surfaced as tensions, not suppressed
- [ ] Attention percentages don't exceed 40% for any single section

---

#### 4.3.2 Deriver Agent (Confidence Map)

**Identity:** "I derive confidence-raising actions and review questions from evidence gaps and risk zones. Every action traces to a gap. Every question traces to a data point. I never suggest actions without evidence basis, never generate reassuring questions, never propose infeasible actions, never recommend deployment decisions."

**Class:** Generator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** O1 (evidence gaps), O2 (risk zones), O4 (tensions), sparse_report

**Output Schema:** ConfidenceRaisingActions (O3) + ReviewQuestions (O6) + resolution_options for O4

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never suggest actions without evidence basis | 3 (Prevent) | `traces_to_gap` required in O3 schema (min_items=1) |
| Never generate reassuring questions | 1 (Declare) | Prompt instruction; questions must be specific and traced to data |
| Never propose infeasible actions | 1 (Declare) | Prompt instruction; `effort_estimate` field required |
| Never recommend deployment decisions | 3 (Prevent) | Schema has no deployment_decision fields on Deriver output |

**Null state:** "No evidence gaps identified for [section]. Confidence assessment is well-supported."

**Cost budget:** 10K-25K tokens

**Progressive autonomy:** Two dimensions as specified in P7.

**Acceptance criteria:**

- [ ] Every action has at least 1 `traces_to_gap` entry
- [ ] Schema rejects actions with empty `traces_to_gap`
- [ ] Every action has `effort_estimate` (Low/Medium/High)
- [ ] Every action has `target_confidence` (Medium or High — never Low)
- [ ] Every review question traces to a specific data point or gap
- [ ] Questions are specific, not generic
- [ ] Act Now sections always have at least one confidence-raising action
- [ ] Deriver output contains zero deployment recommendation fields

---

#### 4.3.3 Compiler Agent (Confidence Map)

**Identity:** "I compile the Confidence Map from assessed and derived outputs. I never add scores not produced by Analyst, never omit Low-confidence sections, never present sparse sections as assessed, never smooth over gaps between sections."

**Class:** Aggregator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** O1-O7 processed outputs, meta_confidence, sparse_report, aging_flags

**Output Schema:** ConfidenceMapDocument (O8)

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never add scores not produced by Analyst | 3 (Prevent) | Schema validation: O8 section scores must match O1 scores exactly |
| Never omit Low-confidence sections | 3 (Prevent) | Completeness check: all sections present, Low sections explicitly included |
| Never present sparse as assessed | 3 (Prevent) | `sparse_sections` field required on O8; sections with <30% evidence flagged |
| Never smooth over gaps between sections | 2 (Detect) | Visual format uses discrete colour bands, not gradients; numeric scores always visible |

**Null state:** "No confidence data available for compilation."

**Cost budget:** 5K-15K tokens

**Progressive autonomy:** Single dimension (compilation accuracy) as specified in P7.

**Acceptance criteria:**

- [ ] Every section from O1 is present in O8 or listed in sparse_sections
- [ ] Section scores in O8 match O1 exactly (no modification)
- [ ] Visualisation data matches O1/O2 exactly
- [ ] Sparse sections are explicitly listed with completeness percentages
- [ ] Specification aging flags are present for sections assessed >30 days ago
- [ ] meta_confidence (O8 field) reflects overall data quality, not subjective self-assessment
- [ ] Deployment readiness is computed (not assigned): Ready/ConditionallyReady/NotReady based on Act Now sections

---

### 4.4 Tool Definitions

**Purpose:** User-action-level Agno @tool wrappers for Confidence Map operations.

| Tool Name | Purpose | Input | Output | Enforcement Role |
|---|---|---|---|---|
| `query_specification_sections` | Retrieve all specification sections for a workflow | workflow_id | List[SectionData] | User-action abstraction over Q1 |
| `query_stakes_levels` | Retrieve stakes classification per section | workflow_id | List[StakesData] | User-action abstraction over Q2 |
| `query_test_results` | Retrieve test execution results | workflow_id | List[TestData] | User-action abstraction over Q3 |
| `query_epistemic_completeness` | Retrieve CC-3 metadata completeness per section | workflow_id | List[EpistemicData] | User-action abstraction over Q5 |
| `query_validation_records` | Retrieve schema/boundary validation records | workflow_id | List[ValidationData] | User-action abstraction over Q6/Q8 |
| `write_confidence_output` | Write a confidence output to the reflection store | workflow_id, output_type (O1-O8), data | Confirmation with artefact_id | Regime 3: validates schema before write |
| `flag_unclassified_stakes` | Flag a section as having missing stakes data | workflow_id, section_id, default_stakes_level | Confirmation | Regime 3: enforces conservative default |

**Cross-cutting acceptance criteria:**

- [ ] No tool exposes SurrealQL syntax or table names
- [ ] Every tool returns typed Pydantic models
- [ ] `query_test_results` returns empty list (not error) when no tests exist
- [ ] `query_stakes_levels` returns "High" (conservative default) for sections without harm assessment data
- [ ] `write_confidence_output` validates data against the corresponding Pydantic schema
- [ ] `write_confidence_output` rejects writes for non-existent workflow_ids
- [ ] `flag_unclassified_stakes` enforces conservative default (stakes_level = "High" for unclassified sections)

---

### 4.5 Enforcement Mechanisms

**Regime 3 (Prevent by Design) — 5 structural enforcements:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| E1 | Confidence calculation transparency | `confidence_detail` sub-object mandatory on every O1 section score — every source listed, no hidden weighting |
| E2 | No default confidence for sparse sections | O1 schema rejects `confidence_level: "Medium"` when `evidence_completeness < 30%` — sparse sections go to O8 `sparse_sections` list with "unassessed" status, not fake scores |
| E3 | Every action traces to gap | `traces_to_gap` field required in O3 schema (min_items=1); schema rejects actions without gap trace |
| E4 | Risk zone assignment deterministic | Risk zone is a computed function of confidence_level × stakes_level using the design spec matrix — not a subjective assignment; the function is tested and documented |
| E5 | Attention cap at 40% | O2 schema enforces max_attention_per_section ≤ 0.40; redistribution is deterministic |

**Regime 2 (Detect After the Fact) — 4 detection mechanisms:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| D1 | Analyst rounding up confidence | Post-processing scan for sections where confidence_level doesn't match confidence_score thresholds (High ≥ 0.7, Medium 0.4-0.7, Low < 0.4) |
| D2 | Analyst smoothing tensions | Post-processing scan for sections where confidence_detail sources agree but a tension was not surfaced |
| D3 | Deriver generating reassuring questions | Post-processing scan for questions without traces_to references or with generic phrasing ("Is this section validated?") |
| D4 | Compiler smoothing gaps | Post-processing scan for visual representations that use colour gradients instead of discrete bands |

**Regime 1 (Declare in Prompt) — 4 declarations:**

| # | Constraint | Mechanism | Location |
|---|---|---|---|
| R1-1 | Analyst never rounds up confidence | Prompt instruction + deterministic confidence thresholds | Analyst system prompt |
| R1-2 | Analyst never inflates thin evidence | Prompt instruction + deterministic evidence completeness thresholds | Analyst system prompt |
| R1-3 | Deriver never generates reassuring questions | Prompt instruction + specificity examples | Deriver system prompt |
| R1-4 | Compiler never smooths gaps | Prompt instruction + discrete visual format specification | Compiler system prompt |

---

### 4.6 Wave Orchestration

**Purpose:** Coordinate the 4-wave execution pipeline for the Confidence Map.

**Specification:**

Same 4-wave architecture as Methodology Reflection: Data → Assessment → Derivation → Compilation.

**Wave dependency map:**

| Wave | Depends On | Produces | Failure Action |
|---|---|---|---|
| Wave 1: Data | Schema verification + stakes data verification | Evidence package (Q1-Q9 results) | If stakes data missing (Q2), flag sections as unclassified with conservative default. If critical schema data missing, halt with error. |
| Wave 2: Assessment | Wave 1 complete | O1 scores, O2 risk zones, O4 tensions, O5 visualisation, sparse report, meta_confidence | If Analyst fails, retry once. If retry fails, produce minimal assessment with "Insufficient analysis" flag. |
| Wave 3: Derivation | Wave 2 complete | O3 actions, O6 questions, O4 resolution options | If Deriver fails, retry once. If retry fails, produce minimal derivation with "Insufficient evidence for derivation" flag. |
| Wave 4: Compilation | Waves 2-3 complete | O8 Confidence Map Document | If Compiler fails, retry once. If retry fails, produce raw assessment package with "Compilation failed" flag. |

**Orchestrator specification:**

| Property | Value |
|---|---|
| Composition | Agno Team with 3 member agents (Analyst, Deriver, Compiler) |
| Orchestrator mode | Sequential (coordinate mode — waves run in order) |
| State management | Workflow state stored in `design_workflows` table (phase: P10, status: in_progress, sub_phase: confidence_map) |
| Error handling | Per-wave retry (1 attempt), then fallback |
| Logging | All wave transitions logged to `runtime_events` |
| Human gates | None during production (human review is post-delivery) |

**Acceptance criteria:**

- [ ] Wave 1 does not start until stakes data verification (Q2) passes or defaults to conservative
- [ ] Wave 2 does not start until Wave 1 queries complete (or fail gracefully)
- [ ] Wave 3 does not start until Wave 2 produces assessment output
- [ ] Wave 4 does not start until Waves 2-3 produce their outputs
- [ ] Missing stakes data defaults to "High" stakes (conservative) — pipeline does NOT halt
- [ ] Missing test data defaults to `None` — pipeline does NOT halt
- [ ] Each wave logs start time, end time, and status

---

### 4.7 Seed Data Specification

**Purpose:** Provide test data for the Confidence Map workflow.

**Specification (4 seed scripts, not written here):**

**Seed 1: Sample Specification with Sections**

- Creates a workflow with complete P0-P9 specification data
- Includes: agent specifications (at least 2 agents with different classes), tasks with H/A/S allocation, quality gate records (some passing, some failing), contracts with authority boundaries
- Must include at least 1 harm-capable agent (for Critical stakes section)
- Must include at least 1 easily reversible task (for Low stakes section)

**Seed 2: Sample Stakes Data**

- Creates stakes classifications derived from harm assessment and reversibility
- Must include: at least 2 Critical sections, at least 2 High sections, at least 2 Medium sections, at least 1 Low section
- Must include: at least 1 section with missing harm assessment data (defaults to High)
- Must include: at least 1 section with conflicting evidence (tension between test evidence and expert judgment)

**Seed 3: Sample Test and Gate Data**

- Creates test execution results for some (not all) specification sections
- Must include: at least 3 sections with passing tests (Strong evidence), at least 2 sections with failing tests (Weak evidence), at least 2 sections with no test results (None evidence)
- Must include: at least 1 quality gate failure that correlates with low confidence in the same section

**Seed 4: Sample Assessment and Aging Data**

- Creates assessment fragments relevant to confidence (validation quality, reliability judgments)
- Must include: at least 3 assessment fragments tagged with confidence-relevant content
- Must include: at least 2 sections where assessment fragments disagree (for tension testing)
- Must include: at least 1 section assessed >30 days ago (for aging flag testing)
- Must include: at least 1 section with very high evidence completeness (for "all High confidence" scenario)

**Cross-cutting acceptance criteria:**

- [ ] Seed scripts create a complete specification data set in SurrealDB
- [ ] Running all 4 seeds in order produces a testable confidence map
- [ ] Seed data includes at least 2 Critical stakes sections for risk zone testing
- [ ] Seed data includes conflicting evidence for tension detection testing
- [ ] Seed data includes a section with no tests for "None" evidence testing
- [ ] Seed data includes a section assessed >30 days ago for aging flag testing
- [ ] Seed scripts are idempotent (running twice produces same state)
- [ ] Seed scripts can be cleaned up (delete all test data)

---

### 4.8 Test Specifications

**Test-by-test specification:**

**T25: Confidence Inflation Test (FM1)**

- [ ] **Purpose:** Verify that the Analyst does not inflate confidence in high-stakes sections
- [ ] **Method:** Submit evidence where test_evidence is None and expert_judgment is Weak for a Critical stakes section. Verify Analyst assigns Low or Medium confidence, not High.
- [ ] **Expected result:** Critical stakes section with weak evidence receives Low or Medium confidence, not High. confidence_detail shows all sources transparently.
- [ ] **Failure mode tested:** FM1 (confidence inflation in high-stakes)

**T26: Missing Stakes Test (FM3)**

- [ ] **Purpose:** Verify that missing stakes data defaults to conservative (High)
- [ ] **Method:** Submit a section without harm assessment or reversibility data. Verify the workflow defaults to High stakes and assigns an appropriate risk zone.
- [ ] **Expected result:** Section with missing stakes data defaults to "High" risk zone. Risk zone is "Review Before Deploy" (not "Proceed").
- [ ] **Failure mode tested:** FM3 (missing stakes, RPN 189)

**T26b: Default Medium Test (FM4)**

- [ ] **Purpose:** Verify that sparse sections are flagged, not defaulted to Medium
- [ ] **Method:** Submit a section with evidence_completeness < 30%. Verify the workflow flags it as sparse and assigns "unassessed" status rather than defaulting to "Medium" confidence.
- [ ] **Expected result:** Section appears in O8 sparse_sections list with completeness percentage. It does NOT receive a confidence_level of "Medium".
- [ ] **Failure mode tested:** FM4 (default Medium to sparse sections, RPN 144)

**T27: Counter-Intuitive Result Test (FM5)**

- [ ] **Purpose:** Verify that counter-intuitive confidence results are surfaced as tensions, not suppressed
- [ ] **Method:** Submit a section where test_evidence is Strong but expert_judgment is Weak (or vice versa). Verify the workflow surfaces this as a tension in O4 rather than averaging or suppressing.
- [ ] **Expected result:** Tension appears in O4 with both sources listed, nature of disagreement described, severity assessed based on stakes, and review question generated.
- [ ] **Failure mode tested:** FM5 (counter-intuitive result suppressed)

**T28: Attention Cap Test (FM10)**

- [ ] **Purpose:** Verify that no section receives >40% attention allocation
- [ ] **Method:** Submit data where one section has both Low confidence and Critical stakes (highest priority). Verify attention percentage does not exceed 40%.
- [ ] **Expected result:** Maximum attention for any single section is 40%. Excess is redistributed to other Act Now sections.
- [ ] **Failure mode tested:** FM10 (over-concentration)

**T29: Evidence Trace Test**

- [ ] **Purpose:** Verify that every confidence score traces to at least one evidence source
- [ ] **Method:** Submit data with known evidence sources. Verify every O1 section score has at least one source in confidence_detail.
- [ ] **Expected result:** Every section score has confidence_sources populated. Sections with no evidence are in sparse_sections, not assigned confidence scores.
- [ ] **Cross-cutting concern tested:** E1 (confidence calculation transparency)

**T30: Risk Zone Calculation Test**

- [ ] **Purpose:** Verify that risk zone assignment is deterministic and matches the design spec matrix
- [ ] **Method:** Submit sections with known confidence/stakes combinations. Verify risk zones match the matrix exactly: Low×Critical = Act Now, Medium×Critical = Review Before Deploy, etc.
- [ ] **Expected result:** Risk zones computed deterministically from the matrix, not subjectively assigned.
- [ ] **Cross-cutting concern tested:** E4 (risk zone assignment deterministic)

**T31: End-to-End Integration Test**

- [ ] **Purpose:** Verify full pipeline execution with seed data producing a complete Confidence Map
- [ ] **Method:** Run full pipeline with all 4 seed scripts. Verify Wave 1 produces evidence package, Wave 2 produces assessment, Wave 3 produces derivation, Wave 4 produces O8.
- [ ] **Expected result:** Complete `ConfidenceMapDocument` with all sections scored or flagged as sparse. At least 1 Act Now section. At least 1 tension. At least 1 confidence-raising action. Review questions present. Visualisation present.
- [ ] **Integration tested:** Full pipeline dependency chain

---

## 5. Build Order

| Order | Task ID | Task | Wave | Depends On | Essential | Effort |
|---|---|---|---|---|---|---|
| 1 | T1 | Verify SurrealDB schema has artefact_tags | Foundation | — | ✅ | Small |
| 2 | T2 | Verify stakes classification data structure | Foundation | — | ✅ | Small |
| 3 | T3 | Verify test execution data structure | Foundation | — | ✅ | Small |
| 4 | T4 | Define O1-O8 Pydantic output schemas | Foundation | T1-T3 | ✅ | Medium |
| 5 | T5 | Map epistemic profiles to schema fields | Foundation | T4 | ✅ | Small |
| 6 | T6 | Define enforcement regime for each constraint | Foundation | T4 | ✅ | Small |
| 7 | T7 | Write PRISM query for specification sections (Q1) | Data | T1-T3 | ✅ | Small |
| 8 | T8 | Write PRISM query for stakes levels (Q2) | Data | T1-T3 | ✅ | Small |
| 9 | T9 | Write PRISM query for test execution results (Q3) | Data | T1-T3 | ✅ | Small |
| 10 | T10 | Write PRISM query for quality gate outcomes (Q4) | Data | T1-T3 | ✅ | Small |
| 11 | T11 | Write PRISM query for epistemic metadata completeness (Q5) | Data | T1-T3 | ✅ | Small |
| 12 | T12 | Write PRISM query for assessment fragments (Q6) | Data | T1-T3 | ✅ | Small |
| 13 | T13 | Write PRISM query for pattern match data (Q7) | Data | T1-T3 | ✅ | Small |
| 14 | T14 | Write PRISM query for specification aging (Q8) | Data | T1-T3 | ✅ | Small |
| 15 | T15 | Test all PRISM queries against seed data | Data | T7-T14, seeds | ✅ | Medium |
| 16 | T16 | Write Analyst agent instructions (Confidence Map) | Agent | T4-T6 | ✅ | Large |
| 17 | T17 | Write Deriver agent instructions (Confidence Map) | Agent | T4-T6 | ✅ | Large |
| 18 | T18 | Write Compiler agent instructions (Confidence Map) | Agent | T4-T6 | ✅ | Medium |
| 19 | T19 | Define progressive autonomy dimensions | Agent | T16-T18 | ✅ | Small |
| 20 | T20 | Define cost budgets per agent | Agent | T16-T18 | ✅ | Small |
| 21 | T21 | Define Agno tool wrappers for Confidence Map queries | Integration | T7-T14 | ✅ | Medium |
| 22 | T22 | Implement risk zone calculation function | Integration | T4, T6 | ✅ | Small |
| 23 | T23 | Implement confidence calculation logic | Integration | T4, T6 | ✅ | Medium |
| 24 | T24 | Implement attention allocation with 40% cap | Integration | T6 | ✅ | Small |
| 25 | T25 | Test FM1 (confidence inflation) | Test | T22-T23 | ✅ | Medium |
| 26 | T26 | Test FM3 (missing stakes) | Test | T8 | ✅ | Small |
| 27 | T26b | Test FM4 (default Medium to sparse) | Test | T22 | ✅ | Small |
| 28 | T27 | Test FM5 (counter-intuitive result) | Test | T23 | ✅ | Small |
| 29 | T28 | Test attention cap (FM10) | Test | T24 | ✅ | Small |
| 30 | T29 | Test evidence trace | Test | T22-T23 | ✅ | Small |
| 31 | T30 | Test risk zone calculation | Test | T22 | ✅ | Small |
| 32 | T31 | End-to-end integration test | Test | T15, T16-T18 | ✅ | Medium |
| 33 | T32 | Assemble build order | Compilation | T1-T31 | ✅ | Small |
| 34 | T33 | Compile enforcement regime summary | Compilation | T6 | ✅ | Small |
| 35 | T34 | Progressive autonomy deployment plan | Compilation | T19 | ✅ | Small |
| 36 | T35 | Integration notes | Compilation | T1-T31 | ✅ | Small |
| 37 | T36 | Assemble final implementation plan | Compilation | T32-T35 | ✅ | Small |

**Critical path:** T1 → T4 → T7-T14 → T15 → T16-T18 → T21 → T22-T24 → T25-T31 → T32-T36

**Time estimate:** 2-3 weeks for one developer with Agno and SurrealDB experience.

---

## 6. Enforcement Regime Summary

| Regime | Count | Mechanisms |
|---|---|---|
| Regime 3 (Prevent) | 5 | Confidence_detail mandatory (E1), no default confidence for sparse sections (E2), traces_to_gap required (E3), risk zone calculation deterministic (E4), attention cap at 40% (E5) |
| Regime 2 (Detect) | 4 | Confidence rounding audit (D1), tension smoothing audit (D2), reassuring question audit (D3), visual smoothing audit (D4) |
| Regime 1 (Declare) | 4 | Analyst rounding instruction (R1-1), Analyst inflation instruction (R1-2), Deriver question instruction (R1-3), Compiler smoothing instruction (R1-4) |

**Total: 5 structural enforcements, 4 detections, 4 declarations.**

Same honest assessment as Methodology Reflection. The Confidence Map cannot structurally prevent an analyst from rounding up confidence or a compiler from smoothing visual gaps. What it CAN do is enforce transparency (every source visible), evidence traces (every gap traced), sparse flagging (no default scores), risk zone determinism (computed, not assigned), and attention caps (no over-concentration).

---

## 7. Progressive Autonomy Deployment Plan

**Starting level:** Shadow for all agents and dimensions.

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Analyst | Evidence assessment | First 10 assessments: human checks every section | ≤1 incorrect weighting in last 10: human checks flagged sections | ≤1 incorrect weighting in last 10: human checks only Act Now sections | Full assessment, human reviews meta-confidence only | ≥10 assessments with ≤1 incorrect weighting |
| Analyst | Tension surfacing | First 10 assessments: surface only obvious contradictions | ≤2 missed tensions in last 10: surface all tensions with severity | ≤2 missed tensions in last 10: surface all tensions, human reviews High severity | Surface all tensions, human reviews only Critical severity | ≥10 assessments with ≤2 missed tensions |
| Analyst | Confidence calculation | First 10 calculations: human validates every score | ≤1 inflated score in last 10: human validates Act Now scores | ≤1 inflated score in last 10: human validates counter-intuitive scores | Full calculation, human reviews only meta-confidence | ≥10 calculations with ≤1 inflated score |
| Deriver | Action specificity | First 10 derivation sets: generic actions only | Strong+Moderate evidence actions with expected impact | All actions with effort estimate and dependency | All actions, human reviews Critical priority only | ≤2 generic actions in last 10 derivation sets |
| Deriver | Question quality | First 10 question sets: generic questions only | Questions traced to sections | Questions traced to specific data points | Questions traced to specific data points with urgency | ≤2 untraced questions in last 10 question sets |
| Compiler | Compilation accuracy | First 10 compilations: human checks every section | Human checks flagged sections | Human checks sparse/flagged sections | Human reviews final post-delivery | ≥10 compilations with ≤1 error |

---

## 8. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Missing stakes data (FM3) | Medium | Critical (RPN 189) | Conservative default to "High" stakes; flag as unclassified; add to review questions |
| Default Medium for sparse sections (FM4) | Medium | High (RPN 144) | Schema validation rejects Medium without evidence; sparse sections go to unassessed list |
| Confidence inflation in high-stakes sections (FM1) | Low-Medium | Critical (RPN 120) | confidence_detail transparency; Regime 2 audit; test in T25 |
| Generic confidence-raising actions (FM5) | Medium | Medium (RPN 120) | traces_to_gap required; test for specificity; examples of specific vs generic in Deriver prompt |
| Missing test data (IR-003) | High | Medium | test_evidence: None is a valid value; honest assessment; meta-confidence reflects data quality |
| Counter-intuitive results suppressed (FM9) | Low | Medium (RPN 84) | Tension surfacing mandatory; test in T27 |
| Attention over-concentration (FM10) | Low | Medium (RPN 105) | 40% cap enforced structurally; test in T28 |
| Evidence weighting model incorrect | Medium | High | Document weighting model; test with seed data; adjust after first 10 assessments |

---

This specification covers every component needed to build the Confidence Map Workflow, from prerequisite verification through seed data, agent instructions, enforcement mechanisms, orchestration, and testing. Each component has acceptance criteria mapping directly back to the design spec's failure modes and quality gates.

The critical structural dependency — stakes classification — is treated differently from the Methodology Reflection's artefact tagging dependency. Where artefact tagging is binary (exists or doesn't), stakes classification has a conservative default (absent data → "High" stakes). The workflow can proceed without complete stakes data; it just treats unclassified sections with maximum caution, which is the correct behaviour for a confidence assessment tool.Complete. Here's what distinguishes this implementation spec from the Methodology Reflection spec:

**The critical dependency is different.** Methodology Reflection depends on *behavioural* data (P0-P9 capturing artefacts with tags). Confidence Map depends on *structural* data (P7/P8 stakes classification). The failure mode is different too: missing tags means "nothing to query" (total failure), while missing stakes means "we can still assess confidence, just conservatively" (degraded but functional).

**The conservative default is the key design decision.** When stakes data is absent, the workflow defaults to "High" stakes — the most cautious assumption. This means the Confidence Map can run on incomplete data without producing misleading results. An unclassified section gets the most scrutiny, not the least.

**The primary interaction is confidence × stakes.** Without stakes, the map collapses from risk-calibrated to merely confidence-rated. That's why IR-002 is Critical — and why the conservative default matters. Every section must have a stakes level, even if it's the conservative "High."

**Two P10 artefacts now have full implementation specifications.** Three dependency types are documented:
- Methodology Reflection: **behavioural** dependency (artefact tags)
- Confidence Map: **structural** dependency (stakes classification)
- EVOLVE Playbook: **temporal** dependency (monitoring infrastructure)

Ready for the next build spec, or do you want to iterate on either of these two?

---

## Run 6 — Agentic Expert ✓ COMPLETED

*2026-05-21T21:24:04* · `glm-5.1:cloud` · `c684f0e2...`

### Prompt

Do the same for the EVOLVE Playbook workflow

***
# CAWDP Application Phase 10.09: EVOLVE Playbook Workflow

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
***

### Response

# EVOLVE Playbook Workflow: Implementation Specification

---

## 1. Project Structure

```
cawdp/
├── db/
│   ├── connection.py                    # Shared
│   ├── writer.py                        # Shared
│   └── queries/
│       ├── base.py                       # Shared
│       ├── ... (Methodology Reflection queries)
│       ├── ... (Confidence Map queries)
│       ├── specification_aging.py       # NEW — EVOLVE Q1
│       ├── override_patterns.py         # NEW — EVOLVE Q2
│       ├── cost_variance.py            # NEW — EVOLVE Q3
│       ├── quality_metrics.py           # NEW — EVOLVE Q4
│       ├── stakeholder_feedback.py     # NEW — EVOLVE Q5
│       └── capability_drift.py         # NEW — EVOLVE Q6
│
├── schemas/
│   ├── epistemic.py                     # Shared
│   ├── outputs/
│   │   ├── ... (existing schemas)
│   │   ├── signal_registry.py           # EVOLVE O1
│   │   ├── trigger_response_map.py      # EVOLVE O2
│   │   ├── aging_schedule.py           # EVOLVE O3
│   │   ├── escalation_framework.py      # EVOLVE O4
│   │   ├── first_90_days.py            # EVOLVE O5
│   │   ├── calibration_guide.py         # EVOLVE O6
│   │   ├── evolve_review_questions.py   # EVOLVE O7
│   │   └── evolve_playbook.py          # EVOLVE O8
│   └── contracts/
│       ├── ... (existing contracts)
│       ├── compiler_evolve.py           # EVOLVE Compiler
│       ├── analyst_evolve.py            # EVOLVE Analyst
│       └── deriver_evolve.py            # EVOLVE Deriver
│
├── agents/
│       ├── ... (existing agents)
│       ├── evolve_analyst.py            # EVOLVE Analyst
│       ├── evolve_deriver.py            # EVOLVE Deriver
│       └── evolve_compiler.py           # EVOLVE Compiler
│
├── tools/
│       ├── ... (existing tools)
│       └── evolve_tools.py             # EVOLVE tools
│
├── enforcement/
│       ├── ... (existing enforcement)
│       └── evolve_enforcement.py        # EVOLVE specific
│
├── pipeline/
│       ├── orchestration.py              # Shared (extended)
│       └── evolve_pipeline.py           # EVOLVE specific
│
└── seeds/
    └── evolve_playbook/                 # EVOLVE seed data
        ├── sample_aging_data.py
        ├── sample_override_data.py
        ├── sample_cost_data.py
        ├── sample_quality_data.py
        ├── sample_feedback_data.py
        └── sample_drift_data.py
```

**Rationale:** Same pattern as previous workflows — extends existing structure with EVOLVE-specific files. The `_evolve` naming convention distinguishes these from Methodology Reflection and Confidence Map files. Seed data simulates production monitoring data that won't exist at P10 time.

---

## 2. SurrealDB Connection

Same shared connection module with CAWDP-aware writer layer. No changes needed.

**Additional requirement:** The `runtime_evolve_triggers` and `runtime_health_metrics` tables must exist for storing monitoring data. These are defined in the main CAWDP SurrealDB schema but need to be verified as prerequisites.

**Acceptance criteria:**

- [ ] `runtime_evolve_triggers` table exists with fields: trigger_type, trigger_source, detected_at, severity, status, re_entry_point, scope, calibration_status
- [ ] `runtime_health_metrics` table exists with fields: metric_type, metric_name, value, threshold, measured_at, agent_id, pipeline_id
- [ ] `monitoring_specification_aging_alerts` table exists with fields: agent_class, signal_type, cadence, threshold, last_reviewed, trigger_condition
- [ ] `monitoring_boundary_violation_stream` table exists for real-time boundary violation detection

---

## 3. Prerequisites

### 3.1 Artefact Tags (Shared)

Same as Methodology Reflection and Confidence Map: `design_artefacts.artefact_tags` must exist.

### 3.2 Monitoring Data (NEW — Temporal Dependency)

The EVOLVE Playbook has a fundamentally different dependency type: **temporal**. At P10 time, production monitoring data does not exist. The playbook at P10 is a **template with default thresholds** that must be calibrated with real data.

**Specification:**

The playbook must include:
1. **Default thresholds** for each signal type — conservative initial values that can be adjusted
2. **A "how to calibrate" section** — instructions for adjusting thresholds based on production data
3. **A playbook_confidence field** — Draft (initial thresholds, not yet calibrated), Calibrated (adjusted with ≥30 days of production data), Validated (adjusted with ≥90 days of production data)
4. **A first 90 days schedule** — what to monitor, when, and how to adjust

**Conservative defaults for signal thresholds:**

| Signal Type | Default Monitor Threshold | Default Review Threshold | Default ReEnter Threshold | Calibration Data Needed |
|---|---|---|---|---|
| Override rate | >10% increase over baseline | >25% increase | >50% increase | 30 days of override data |
| Cost variance | >15% over budget | >30% over budget | >50% over budget | 30 days of cost data |
| Quality decline | >10% drop from baseline | >25% drop | >40% drop | 30 days of quality metrics |
| Capability drift | Any detected drift | Confirmed drift pattern | Drift affecting outputs | 60 days of output comparison |
| Stakeholder feedback | Any negative feedback | Pattern of negative feedback | Critical feedback | 90 days of feedback data |
| Environmental change | Any significant change | Change affecting scope | Change invalidating purpose | Varies by change type |
| Specification aging | Review cadence reached | >30 days past due | >60 days past due | Aging schedule per agent class |
| New failure mode | Any new failure | Recurring failure | Systemic failure | Incident data |

**Acceptance criteria:**

- [ ] Default thresholds are defined for all 8 signal types
- [ ] Thresholds can be updated without code changes (configurable, not hardcoded)
- [ ] playbook_confidence field starts at "Draft" and can be updated to "Calibrated" or "Validated"
- [ ] First 90 days schedule is included in the playbook output
- [ ] Calibration guide specifies minimum data requirements for each threshold update
- [ ] Monitoring tables exist in SurrealDB schema

### 3.3 Specification Aging Cadences (From Design Spec)

The CC-5 specification aging cadences per agent class must be available.

**Specification:**

| Agent Class | Default Review Cadence | Trigger-Based Review |
|---|---|---|
| Extractor | 90 days | On data source change or error rate increase |
| Measurer | 60 days | On measurement inconsistency or threshold breach |
| Assessor | 45 days | On judgment pattern change or new edge case |
| Generator | 30 days | On output quality decline or new failure mode |
| Aggregator | 60 days | On assembly error or missing data increase |

**Acceptance criteria:**

- [ ] Review cadences per agent class are stored in `monitoring_specification_aging_alerts`
- [ ] Trigger-based review conditions are defined for each agent class
- [ ] Cadences can be updated without code changes
- [ ] Overdue reviews are flagged (last_reviewed + cadence < current_date)

---

## 4. Component Specifications

### 4.1 Pydantic Output Schemas (O1-O8)

**O1: SignalRegistry**

- [ ] `signal_id` is unique per signal type per workflow
- [ ] `signal_type` restricted to: override_rate, cost_variance, quality_decline, capability_drift, stakeholder_feedback, environmental_change, specification_aging, new_failure_mode
- [ ] `detection_window` describes how quickly this signal appears (e.g., "1-2 weeks for override rate increase")
- [ ] `response_window` describes how long before it becomes critical (e.g., "4-6 weeks before authority boundaries need updating")
- [ ] `current_severity` restricted to: Monitor, Review, ReEnter
- [ ] `default_thresholds` includes all three levels (monitor, review, re-enter) with default values
- [ ] `calibrated_thresholds` is optional (null if not yet calibrated)
- [ ] `re_entry_point` restricted to: P0, P1, P2, P3, P4, P5, P6, P7, P8, P9 (maps to CAWDP phases)
- [ ] `scope` is specific (e.g., "update authority boundaries for Generator agent" not "redo specification")
- [ ] `evidence_trace` is required and links to monitoring data
- [ ] Every signal has a `calibration_status` restricted to: Draft, Calibrated, Validated

**O2: TriggerResponseMap**

- [ ] `trigger_type` maps to a signal type from O1
- [ ] `escalation_level` restricted to: Monitor, Review, ReEnter
- [ ] `action` is specific and actionable (not "review" or "consider")
- [ ] `re_entry_phase` restricted to CAWDP phases P0-P9
- [ ] `re_entry_scope` is specific (e.g., "update authority boundaries for Generator agent")
- [ ] `expected_outcome` describes what the re-entry produces (e.g., "updated design_agent_specifications record with revised authority boundaries")
- [ ] `estimated_effort` restricted to: Low (<2 hours), Medium (2-8 hours), High (>8 hours)
- [ ] `priority` is computed from signal severity × response urgency, not subjective assignment
- [ ] Every Review trigger has a monitoring recommendation
- [ ] Every ReEnter trigger has a scope and expected outcome

**O3: AgingSchedule**

- [ ] `agent_class` restricted to: Extractor, Measurer, Assessor, Generator, Aggregator
- [ ] `default_cadence` matches design spec values (30/45/60/90 days per class)
- [ ] `trigger_conditions` are specific and testable (e.g., "error rate increase >5% over 7 days")
- [ ] `last_reviewed` is a datetime (or null if never reviewed)
- [ ] `overdue` is computed (not subjective): `last_reviewed + cadence < current_date`
- [ ] `next_review_date` is computed from last_reviewed + cadence
- [ ] Every agent class in the specification has an aging schedule entry

**O4: EscalationFramework**

- [ ] Three levels: Monitor → Review → ReEnter
- [ ] Each level has clear criteria (when to escalate)
- [ ] Each level has clear actions (what to do)
- [ ] Each level has clear outcomes (what the action produces)
- [ ] Monitor level: observe, collect data, no CAWDP re-entry
- [ ] Review level: analyse data, prepare for re-entry, consider CAWDP re-entry
- [ ] ReEnter level: start CAWDP re-entry at the specified phase with the specified scope
- [ ] Escalation from Monitor to Review requires evidence (not just feeling)
- [ ] De-escalation from Review to Monitor requires evidence of resolution
- [ ] De-escalation from ReEnter to Review is not possible during an active re-entry (you complete the re-entry cycle)

**O5: First90DaysSchedule**

- [ ] Organised by week (Week 1-2, Week 3-4, Month 2, Month 3)
- [ ] Each week has specific monitoring tasks, data to collect, and thresholds to observe
- [ ] Week 1-2: Establish baseline override rates, cost baselines, quality metrics
- [ ] Week 3-4: Compare initial data against default thresholds, flag anomalies
- [ ] Month 2: Adjust thresholds based on observed data, calibrate first signals
- [ ] Month 3: Validate calibrated thresholds, update playbook_confidence to "Calibrated"
- [ ] Includes decision criteria for when to escalate during calibration period
- [ ] Includes guidance for handling ambiguous signals during first 90 days
- [ ] `playbook_confidence` at end of 90 days should be "Calibrated" (not "Validated" — that requires 90+ days)

**O6: CalibrationGuide**

- [ ] Minimum data requirements for each signal type (e.g., "override rate calibration requires ≥30 days of data from ≥3 agents")
- [ ] Step-by-step calibration process for each signal type
- [ ] How to adjust thresholds based on observed data
- [ ] How to update playbook_confidence from Draft → Calibrated → Validated
- [ ] Warning about premature calibration (calibrating on <30 days of data)
- [ ] How to handle contradictory data (e.g., override rates are low but quality is declining)
- [ ] How to reset thresholds if calibration produces unexpected results

**O7: EvolveReviewQuestions**

- [ ] Every question traces to a specific signal type or aging cadence
- [ ] Questions are specific, not generic ("Override rate for the Assessor agent increased 15% last week — is this a specification issue or a context change?" not "Are there any signals?")
- [ ] Questions are organised by urgency: Monitor-level questions first, Review-level second, ReEnter-level third
- [ ] Every ReEnter-level question includes a suggested re-entry scope

**O8: EvolvePlaybookDocument**

- [ ] All O1-O7 references are typed
- [ ] `playbook_confidence` is required (Draft/Calibrated/Validated)
- [ ] `calibration_date` is required (when thresholds were last calibrated)
- [ ] `next_review_date` is required (when the playbook itself should be reviewed)
- [ ] `playbook_version` is required (semantic versioning)
- [ ] `signal_registry` references O1
- [ ] `trigger_response_map` references O2
- [ ] `aging_schedule` references O3
- [ ] `escalation_framework` references O4
- [ ] `first_90_days` references O5
- [ ] `calibration_guide` references O6
- [ ] `review_questions` references O7

---

### 4.2 PRISM Query Templates

**Q1: Specification Aging Data**

- [ ] Returns all agent specifications with their `last_reviewed` dates and `specification_aging` cadences
- [ ] Each result includes: agent_id, agent_class, agent_name, last_reviewed, cadence_days, overdue, next_review_date
- [ ] `overdue` is computed: `last_reviewed + cadence_days < current_date`
- [ ] Returns agents with no `last_reviewed` date (treated as never reviewed — overdue)
- [ ] Returns empty set (not error) for workflows with no agent specifications

**Q2: Override Patterns**

- [ ] Returns override data from `runtime_health_metrics` for the given workflow
- [ ] Each result includes: agent_id, metric_type, metric_name, value, baseline_value, threshold, measured_at
- [ ] Calculates override rate: (override_count / total_decisions) per agent
- [ ] Compares current override rate to baseline (first 2 weeks of deployment)
- [ ] Returns empty set (not error) for workflows with no override data (Draft playbook)

**Q3: Cost Variance**

- [ ] Returns cost data from `runtime_health_metrics` for the given workflow
- [ ] Each result includes: agent_id, metric_type, metric_name, budget, actual, variance, variance_percentage, measured_at
- [ ] Calculates variance: (actual - budget) / budget × 100
- [ ] Returns empty set (not error) for workflows with no cost data

**Q4: Quality Metrics**

- [ ] Returns quality metrics from `runtime_health_metrics` for the given workflow
- [ ] Each result includes: agent_id, metric_type, metric_name, value, baseline_value, threshold, measured_at
- [ ] Includes IDS (Integrity Diagnostic Score) and UPR (Utilisation Performance Ratio) where available
- [ ] Returns empty set (not error) for workflows with no quality data

**Q5: Stakeholder Feedback**

- [ ] Returns stakeholder feedback from `design_artefacts` tagged with "assessment_fragment" containing feedback keywords
- [ ] Each result includes: artefact_id, phase, content, tags, assessedAt
- [ ] Filters for feedback related to specification quality, agent behaviour, or operational issues
- [ ] Returns empty set (not error) for workflows with no stakeholder feedback

**Q6: Capability Drift**

- [ ] Returns capability drift indicators from `runtime_evolve_triggers` with trigger_type "capability_drift"
- [ ] Each result includes: trigger_id, detected_at, severity, status, description
- [ ] Returns empty set (not error) for workflows with no drift triggers

**Cross-cutting acceptance criteria:**

- [ ] All queries accept `workflow_id` as parameter
- [ ] All queries handle empty result sets gracefully (return empty list, not error)
- [ ] All queries are idempotent
- [ ] Q1-Q4 return deterministic calculations (overdue status, variance, override rate)
- [ ] Q2, Q3, Q4 return meaningful null states when no production data exists ("No override data available — baseline establishment needed")

---

### 4.3 Agent Implementation Specifications

#### 4.3.1 Analyst Agent (EVOLVE Playbook)

**Identity:** "I measure signals, assess severity, and surface patterns. I never draw conclusions about what to do, never make recommendations about re-entry, never interpret drift as failure, never smooth over contradictory signals, never flag everything equally."

**Class:** Measurer + Assessor

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** Monitoring data from Q1-Q6, specification aging cadences, default thresholds, production data (if available)

**Output Schema:** SignalRegistry (O1), trigger_response_map components, aging_schedule components, escalation_framework data, first_90_days schedule components, sparse_report, calibration_status

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never draw conclusions about re-entry | 3 (Prevent) | Schema has no re-entry recommendation fields on Analyst output |
| Never make recommendations | 3 (Prevent) | Schema has no recommendation fields on Analyst output |
| Never interpret drift as failure | 2 (Detect) | Drift is pattern observation, not failure diagnosis; output audit for diagnostic language |
| Never smooth over contradictory signals | 2 (Detect) | Contradictory signals surfaced as pairs, not averaged |
| Never flag everything equally | 3 (Prevent) | Escalation level is computed from signal severity × response window, not uniform assignment |

**Null state:** "No monitoring data available for [signal_type]. Establishing baseline is recommended. Playbook confidence: Draft."

**Cost budget:** 10K-30K tokens

**Progressive autonomy:** Three dimensions (signal detection, severity assessment, pattern identification)

| Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|
| Signal detection | Detect only predefined signals | Detect predefined + emerging patterns | Detect all signals with severity assessment | Full detection, human reviews ambiguous only | ≤2 missed signals in last 10 monitoring cycles |
| Severity assessment | Assess only Monitor-level signals | Assess Monitor + Review signals | Assess all signals including ambiguous | Full assessment, human reviews ReEnter-level only | ≤2 incorrect severity assessments in last 10 |
| Pattern identification | Identify only individual signals | Identify signals + simple correlations | Identify signals + correlations + drift patterns | Full pattern identification | ≤2 missed patterns in last 10 monitoring cycles |

**Acceptance criteria:**

- [ ] Agent produces O1 with signal types, detection windows, response windows, and severity levels
- [ ] Every signal traces to monitoring data (or flagged as Draft if no production data)
- [ ] Contradictory signals are surfaced as pairs, not averaged
- [ ] Severity is computed from signal magnitude × response window urgency
- [ ] Escalation levels are deterministic from signal severity and response windows
- [ ] Agent output contains zero re-entry recommendation fields (schema prevents structurally)
- [ ] Draft playbooks are flagged as such (not presented as calibrated)

---

#### 4.3.2 Deriver Agent (EVOLVE Playbook)

**Identity:** "I derive trigger-response pairs, escalation paths, and review questions from signal patterns. Every action traces to a signal. Every re-entry scope is specific. I never recommend full re-design when targeted update would suffice, never produce generic maintenance schedules, never suggest actions without evidence basis, never recommend deployment decisions."

**Class:** Generator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** O1 (signals), O3 (aging schedule), escalation framework data, sparse_report, calibration status

**Output Schema:** TriggerResponseMap (O2), first_90_days schedule (O5), calibration guide (O6), review questions (O7)

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never recommend full re-design when targeted update suffices | 3 (Prevent) | `re_entry_scope` field requires specific scope (max 2 CAWDP phases) |
| Never produce generic maintenance schedules | 3 (Prevent) | `trigger_type` requires specific signal mapping; no "review everything periodically" allowed |
| Never suggest actions without evidence basis | 3 (Prevent) | `evidence_trace` required on every trigger; orphan triggers auto-removed |
| Never recommend deployment decisions | 3 (Prevent) | Schema has no deployment_decision fields |

**Null state:** "No signals detected for [signal_type]. Monitoring schedule is active. Playbook confidence: [Draft/Calibrated/Validated]."

**Cost budget:** 10K-25K tokens

**Progressive autonomy:** Two dimensions

| Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|
| Action specificity | Generic actions only ("monitor override rates") | Specific actions with expected outcomes | Specific actions with effort estimates | Specific actions with effort estimates + dependencies | ≤2 generic actions in last 10 trigger-response sets |
| Scope precision | Broad scopes only ("review specification") | Moderate scopes ("review P7 for this agent") | Specific scopes ("update authority boundaries for Generator agent") | Specific scopes with expected outcomes | ≤2 broad scopes in last 10 trigger-response sets |

**Acceptance criteria:**

- [ ] Every trigger in O2 has a specific `re_entry_scope` (max 2 CAWDP phases)
- [ ] Every trigger has `evidence_trace` linking to a signal
- [ ] Every trigger has `estimated_effort` (Low/Medium/High)
- [ ] Every Review trigger has a monitoring recommendation
- [ ] Every ReEnter trigger has a scope and expected outcome
- [ ] First 90 days schedule (O5) has specific tasks for each 2-week period
- [ ] Calibration guide (O6) has minimum data requirements for each signal type
- [ ] No trigger says "review everything" or "redo the specification"

---

#### 4.3.3 Compiler Agent (EVOLVE Playbook)

**Identity:** "I compile the EVOLVE Playbook from assessed and derived outputs. I never add triggers not produced by the Analyst, never omit Monitor-level signals, never present Draft thresholds as Calibrated, never smooth over gaps between signals."

**Class:** Aggregator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** O1-O7 processed outputs, calibration status, version

**Output Schema:** EvolvePlaybookDocument (O8)

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never add triggers not produced by Analyst | 3 (Prevent) | O8 trigger registry must match O1 signal registry |
| Never omit Monitor-level signals | 3 (Prevent) | Completeness check: every signal type has a Monitor entry |
| Never present Draft thresholds as Calibrated | 3 (Prevent) | `playbook_confidence` field is required and must match calibration status |
| Never smooth over gaps between signals | 2 (Detect) | Contradictory signals preserved as-is in O8 |

**Null state:** "No playbook data available for compilation."

**Cost budget:** 5K-15K tokens

**Progressive autonomy:** Single dimension (compilation accuracy)

| Level | Criteria | Human Role |
|---|---|---|
| Shadow | First 10 compilations | Human checks every section |
| Advisory | ≤1 error in last 10 compilations | Human checks flagged sections |
| Supervised | ≤1 error in last 10 compilations | Human checks Monitor/Review sections only |
| Autonomous | ≤1 error in last 20 compilations | Human reviews final playbook post-delivery |

**Acceptance criteria:**

- [ ] Every signal type in O1 has a corresponding entry in O8
- [ ] Every trigger in O2 has a corresponding entry in O8
- [ ] `playbook_confidence` matches calibration status (Draft if thresholds are defaults, Calibrated if adjusted with data)
- [ ] Version numbering follows semantic versioning (major.minor.patch)
- [ ] `next_review_date` is computed from the most frequent aging cadence
- [ ] First 90 days schedule is present and specific
- [ ] Calibration guide is present with minimum data requirements

---

### 4.4 Tool Definitions

| Tool Name | Purpose | Input | Output | Enforcement Role |
|---|---|---|---|---|
| `query_aging_data` | Retrieve specification aging data | workflow_id | List[AgingData] | User-action abstraction over Q1 |
| `query_override_patterns` | Retrieve override rate data | workflow_id | List[OverrideData] | User-action abstraction over Q2 |
| `query_cost_variance` | Retrieve cost data | workflow_id | List[CostData] | User-action abstraction over Q3 |
| `query_quality_metrics` | Retrieve quality metrics | workflow_id | List[QualityData] | User-action abstraction over Q4 |
| `query_stakeholder_feedback` | Retrieve feedback data | workflow_id | List[FeedbackData] | User-action abstraction over Q5 |
| `query_capability_drift` | Retrieve drift triggers | workflow_id | List[DriftData] | User-action abstraction over Q6 |
| `write_evolve_output` | Write an EVOLVE output | workflow_id, output_type (O1-O8), data | Confirmation with artefact_id | Regime 3: validates schema before write |
| `flag_ambiguous_signal` | Flag a signal as ambiguous with recommended monitoring | workflow_id, signal_type, details, monitoring_recommendation | Confirmation | Regime 3: enforces ambiguous signal flagging |
| `update_playbook_confidence` | Update playbook confidence level | workflow_id, confidence_level (Draft/Calibrated/Validated), evidence | Confirmation | Regime 3: enforces confidence level transitions |

**Cross-cutting acceptance criteria:**

- [ ] No tool exposes SurrealQL syntax or table names
- [ ] Every tool returns typed Pydantic models
- [ ] `query_override_patterns` returns empty list (not error) when no override data exists
- [ ] `query_cost_variance` returns empty list (not error) when no cost data exists
- [ ] `query_quality_metrics` returns empty list (not error) when no quality data exists
- [ ] `query_stakeholder_feedback` returns empty list (not error) when no feedback exists
- [ ] `flag_ambiguous_signal` enforces that ambiguous signals include a monitoring recommendation
- [ ] `update_playbook_confidence` only allows transitions: Draft → Calibrated → Validated (not backwards)

---

### 4.5 Enforcement Mechanisms

**Regime 3 (Prevent by Design) — 5 structural enforcements:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| E1 | No re-entry recommendations from Analyst | Schema has no re-entry recommendation fields on Analyst output | Pydantic model validation |
| E2 | Specific scope required | `re_entry_scope` field has max 2 CAWDP phases and must describe specific update | Schema validation with max_phases=2 constraint |
| E3 | Evidence trace required for triggers | `evidence_trace` required on O2 trigger entries | Pydantic `Field(min_length=1)` |
| E4 | Playbook confidence must match calibration status | `playbook_confidence` field validated against actual calibration data | Runtime validation: if no production data exists, must be "Draft" |
| E5 | Escalation level computed, not assigned | Escalation level is a deterministic function of signal severity × response window | Computed by Analyst, not subjective |

**Regime 2 (Detect After the Fact) — 4 detection mechanisms:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| D1 | Analyst diagnostic language | Post-processing scan for "should", "recommend", "diagnose", "the issue is" | Output audit |
| D2 | Deriver generic scope | Post-processing scan for "review everything", "redo specification", "general maintenance" | Output audit with specific scope list |
| D3 | Compiler presenting Draft as Calibrated | Post-processing validation that playbook_confidence matches calibration evidence | Confidence check |
| D4 | Equal-flagging of all signals | Post-processing check that escalation levels vary (not all Monitor or all ReEnter) | Distribution check |

**Regime 1 (Declare in Prompt) — 4 declarations:**

| # | Constraint | Mechanism | Location |
|---|---|---|---|
| R1-1 | Analyst never interprets drift as failure | Prompt instruction | Analyst system prompt |
| R1-2 | Analyst never smooths contradictory signals | Prompt instruction | Analyst system prompt |
| R1-3 | Deriver never produces generic maintenance schedules | Prompt instruction | Deriver system prompt |
| R1-4 | Compiler never presents Draft thresholds as Calibrated | Prompt instruction + schema validation | Compiler system prompt + E4 |

---

### 4.6 Wave Orchestration

| Wave | Depends On | Produces | Failure Action |
|---|---|---|---|
| Wave 1: Data | Schema verification + monitoring data verification | Raw monitoring data (Q1-Q6 results) | If monitoring tables don't exist, produce Draft playbook with default thresholds and "baseline establishment needed" flags |
| Wave 2: Assessment | Wave 1 complete | O1 signal registry, O3 aging schedule, escalation framework, first 90 days schedule (partial), sparse report | If Analyst fails, produce minimal assessment with "Insufficient signal analysis" flag |
| Wave 3: Derivation | Wave 2 complete | O2 trigger-response map, O5 first 90 days, O6 calibration guide, O7 review questions | If Deriver fails, produce minimal derivation with "Insufficient trigger derivation" flag |
| Wave 4: Compilation | Waves 2-3 complete | O8 EVOLVE Playbook Document | If Compiler fails, produce raw assessment package with "Compilation failed" flag |

**Special handling for Draft playbooks:**

When monitoring data doesn't exist (Q2-Q4 return empty), the workflow produces a **Draft playbook** with:
- Default thresholds (from the design spec table above)
- `playbook_confidence: "Draft"`
- First 90 days schedule focused on baseline establishment
- Calibration guide explaining how to calibrate each signal type
- All signals flagged as "No production data — baseline needed"
- Review questions focused on: "What should we monitor first? How do we establish baselines?"

**Acceptance criteria:**

- [ ] Wave 1 handles missing monitoring data gracefully (produces Draft playbook)
- [ ] Wave 2 produces signal registry even with empty monitoring data (signals flagged as "baseline needed")
- [ ] Wave 3 produces trigger-response map with default thresholds clearly marked as "Draft"
- [ ] Wave 4 produces complete O8 with playbook_confidence set appropriately
- [ ] Each wave logs start time, end time, and status to `runtime_events`
- [ ] Failed wave retry happens exactly once before fallback

---

### 4.7 Seed Data Specification

**Seed 1: Sample Specification Aging Data**

- Creates `monitoring_specification_aging_alerts` records for at least 2 agent specifications
- Must include: at least 1 overdue review (last_reviewed + cadence < current_date)
- Must include: at least 1 upcoming review (within 7 days)
- Must include: at least 1 recently reviewed (within cadence, not overdue)
- Must cover at least 2 different agent classes with different cadences (e.g., Generator at 30 days, Extractor at 90 days)

**Seed 2: Sample Override Data**

- Creates `runtime_health_metrics` records with override data for at least 2 agents
- Must include: at least 1 agent with elevated override rate (>10% above baseline)
- Must include: at least 1 agent with normal override rate
- Must include: baseline override rates for comparison
- Must include timestamps spanning at least 2 weeks for trend analysis

**Seed 3: Sample Cost Data**

- Creates `runtime_health_metrics` records with cost data for at least 2 agents
- Must include: at least 1 agent with cost variance >15% over budget
- Must include: at least 1 agent with cost within budget
- Must include budget and actual amounts for variance calculation

**Seed 4: Sample Quality Data**

- Creates `runtime_health_metrics` records with IDS and UPR data for at least 2 agents
- Must include: at least 1 agent with declining quality metrics (>10% drop)
- Must include: at least 1 agent with stable quality metrics

**Seed 5: Sample Feedback Data**

- Creates `design_artefacts` records with assessment_fragment tags containing feedback
- Must include: at least 2 negative feedback entries (specification quality concerns)
- Must include: at least 1 positive feedback entry
- Must include: at least 1 ambiguous feedback entry (could be specification issue or context change)

**Seed 6: Sample Drift Data**

- Creates `runtime_evolve_triggers` records with capability drift events
- Must include: at least 1 confirmed drift pattern (severity: Review)
- Must include: at least 1 potential drift signal (severity: Monitor)
- Must include: at least 1 environmental change signal

**Cross-cutting acceptance criteria:**

- [ ] Seed scripts create a complete monitoring data set in SurrealDB
- [ ] Running all 6 seeds in order produces a testable EVOLVE playbook
- [ ] Seed data includes at least 1 elevated override rate for trigger testing
- [ ] Seed data includes at least 1 overdue review for aging testing
- [ ] Seed data includes at least 1 cost variance for cost testing
- [ ] Seed data includes at least 1 quality decline for quality testing
- [ ] Seed scripts are idempotent (running twice produces same state)
- [ ] Seed scripts can be cleaned up (delete all test data)

---

### 4.8 Test Specifications

**T25: Over-Triggering Test (FM1)**

- [ ] **Purpose:** Verify that the playbook does not trigger re-entry for minor signal fluctuations
- [ ] **Method:** Submit data where override rate is 12% above baseline (Monitor threshold) but 25% below Review threshold. Verify playbook assigns Monitor level, not Review or ReEnter.
- [ ] **Expected result:** Signal is flagged as Monitor level. No ReEnter trigger generated for this signal.
- [ ] **Failure mode tested:** FM1 (over-triggering, worst failure)

**T26: Missing Stakes Test (from Confidence Map, adapted)**

- [ ] **Purpose:** Verify that missing monitoring data produces a Draft playbook with default thresholds
- [ ] **Method:** Submit data where all monitoring tables return empty sets (no production data). Verify playbook is produced with playbook_confidence: "Draft" and all signals flagged as "baseline needed."
- [ ] **Expected result:** Complete playbook with default thresholds, Draft confidence, and first 90 days schedule focused on baseline establishment.
- [ ] **Failure mode tested:** Missing monitoring data handling

**T26b: Under-Triggering Test (FM2)**

- [ ] **Purpose:** Verify that the playbook does not miss significant signals
- [ ] **Method:** Submit data where override rate is 50% above baseline (ReEnter threshold). Verify playbook assigns ReEnter level with specific scope.
- [ ] **Expected result:** Signal is flagged as ReEnter level with specific re-entry scope (e.g., "update authority boundaries for this agent").
- [ ] **Failure mode tested:** FM2 (under-triggering)

**T27: Specification Aging Test**

- [ ] **Purpose:** Verify that overdue reviews are flagged and next review dates are computed
- [ ] **Method:** Submit data with 1 overdue review (last_reviewed 100 days ago for a 60-day cadence) and 1 upcoming review (last_reviewed 55 days ago for a 60-day cadence).
- [ ] **Expected result:** Overdue review flagged as "Review overdue" with specific scope. Upcoming review flagged as "Review due in 5 days."
- [ ] **Cross-cutting concern tested:** CC-5 (specification aging)

**T28: Escalation Framework Test**

- [ ] **Purpose:** Verify that the Monitor → Review → ReEnter escalation works correctly
- [ ] **Method:** Submit data with signals at all three levels: Monitor (10% override increase), Review (25% override increase), ReEnter (50% override increase). Verify each gets the correct escalation level and action.
- [ ] **Expected result:** Monitor: observe and collect data. Review: analyse and prepare for potential re-entry. ReEnter: start CAWDP re-entry at specific phase with specific scope.
- [ ] **Cross-cutting concern tested:** Escalation framework correctness

**T29: Signal-Specificity Test**

- [ ] **Purpose:** Verify that every trigger maps to a specific signal type, re-entry phase, and scope
- [ ] **Method:** Submit data with all 8 signal types. Verify each trigger in O2 has signal_type, re_entry_phase, and specific re_entry_scope.
- [ ] **Expected result:** All 8 signal types have corresponding trigger entries. No trigger says "review everything" or "redo specification."
- [ ] **Cross-cutting concern tested:** E2 (specific scope)

**T30: Calibration Test**

- [ ] **Purpose:** Verify that the playbook correctly handles Draft → Calibrated transition
- [ ] **Method:** Submit data with 30+ days of override and cost data. Verify that calibration thresholds can be updated and playbook_confidence can transition from "Draft" to "Calibrated."
- [ ] **Expected result:** Default thresholds replaced with calibrated thresholds. playbook_confidence updated to "Calibrated."
- [ ] **Cross-cutting concern tested:** Playbook lifecycle

**T31: End-to-End Integration Test**

- [ ] **Purpose:** Verify full pipeline execution with seed data producing a complete EVOLVE Playbook
- [ ] **Method:** Run full pipeline with all 6 seed scripts. Verify Wave 1 produces monitoring data, Wave 2 produces signal registry, Wave 3 produces trigger-response map, Wave 4 produces O8.
- [ ] **Expected result:** Complete `EvolvePlaybookDocument` with all 8 signal types, trigger-response map, aging schedule, escalation framework, first 90 days schedule, calibration guide, review questions. Playbook confidence set appropriately (Draft or Calibrated based on data).
- [ ] **Integration tested:** Full pipeline dependency chain

---

## 5. Build Order

| Order | Task ID | Task | Wave | Depends On | Essential | Effort |
|---|---|---|---|---|---|---|
| 1 | T1 | Verify SurrealDB schema has artefact_tags | Foundation | — | ✅ | Small |
| 2 | T2 | Verify monitoring tables exist (evolve_triggers, health_metrics, aging_alerts) | Foundation | — | ✅ | Small |
| 3 | T3 | Verify specification aging cadences table exists | Foundation | — | ✅ | Small |
| 4 | T4 | Define O1-O8 Pydantic output schemas | Foundation | T1-T3 | ✅ | Medium |
| 5 | T5 | Map epistemic profiles to schema fields | Foundation | T4 | ✅ | Small |
| 6 | T6 | Define enforcement regime for each constraint | Foundation | T4 | ✅ | Small |
| 7 | T7 | Write PRISM query for specification aging (Q1) | Data | T1-T3 | ✅ | Small |
| 8 | T8 | Write PRISM query for override patterns (Q2) | Data | T1-T3 | ✅ | Small |
| 9 | T9 | Write PRISM query for cost variance (Q3) | Data | T1-T3 | ✅ | Small |
| 10 | T10 | Write PRISM query for quality metrics (Q4) | Data | T1-T3 | ✅ | Small |
| 11 | T11 | Write PRISM query for stakeholder feedback (Q5) | Data | T1-T3 | ✅ | Small |
| 12 | T12 | Write PRISM query for capability drift (Q6) | Data | T1-T3 | ✅ | Small |
| 13 | T13 | Test all PRISM queries against seed data | Data | T7-T12, seeds | ✅ | Medium |
| 14 | T14 | Write Analyst agent instructions (EVOLVE) | Agent | T4-T6 | ✅ | Large |
| 15 | T15 | Write Deriver agent instructions (EVOLVE) | Agent | T4-T6 | ✅ | Large |
| 16 | T16 | Write Compiler agent instructions (EVOLVE) | Agent | T4-T6 | ✅ | Medium |
| 17 | T17 | Define progressive autonomy dimensions | Agent | T14-T16 | ✅ | Small |
| 18 | T18 | Define cost budgets per agent | Agent | T14-T16 | ✅ | Small |
| 19 | T19 | Define Agno tool wrappers for EVOLVE queries | Integration | T7-T12 | ✅ | Medium |
| 20 | T20 | Implement escalation level calculation | Integration | T4, T6 | ✅ | Small |
| 21 | T21 | Implement default threshold table | Integration | T4 | ✅ | Small |
| 22 | T22 | Implement specification aging computation | Integration | T4 | ✅ | Small |
| 23 | T23 | Implement Draft playbook fallback logic | Integration | T4 | ✅ | Small |
| 24 | T24 | Implement first 90 days schedule generation | Integration | T14-T16 | ✅ | Medium |
| 25 | T25 | Test FM1 (over-triggering) | Test | T20 | ✅ | Medium |
| 26 | T26 | Test missing monitoring data (Draft playbook) | Test | T23 | ✅ | Small |
| 27 | T26b | Test FM2 (under-triggering) | Test | T20 | ✅ | Small |
| 28 | T27 | Test specification aging | Test | T22 | ✅ | Small |
| 29 | T28 | Test escalation framework | Test | T20 | ✅ | Small |
| 30 | T29 | Test signal specificity | Test | T14-T15 | ✅ | Small |
| 31 | T30 | Test calibration transition | Test | T21 | ✅ | Medium |
| 32 | T31 | End-to-end integration test | Test | T13, T14-T16 | ✅ | Medium |
| 33 | T32 | Assemble build order | Compilation | T1-T31 | ✅ | Small |
| 34 | T33 | Compile enforcement regime summary | Compilation | T6 | ✅ | Small |
| 34 | T34 | Progressive autonomy deployment plan | Compilation | T17 | ✅ | Small |
| 35 | T35 | Integration notes | Compilation | T1-T31 | ✅ | Small |
| 36 | T36 | Assemble final implementation plan | Compilation | T32-T35 | ✅ | Small |

**Critical path:** T1 → T4 → T7-T12 → T13 → T14-T16 → T19 → T20-T24 → T25-T31 → T32-T36

**Time estimate:** 2-3 weeks for one developer with Agno and SurrealDB experience.

---

## 6. Enforcement Regime Summary

| Regime | Count | Mechanisms |
|---|---|---|
| Regime 3 (Prevent) | 5 | No re-entry recommendations from Analyst (schema), specific scope required (max 2 phases), evidence trace required (min_items=1), playbook confidence must match calibration (runtime validation), escalation level computed (not assigned) |
| Regime 2 (Detect) | 4 | Analyst diagnostic language audit, Deriver generic scope audit, Compiler Draft-as-Calibrated check, equal-flagging distribution check |
| Regime 1 (Declare) | 4 | Analyst drift-as-failure instruction, Analyst smoothing instruction, Deriver generic schedule instruction, Compiler Draft-as-Calibrated instruction |

**Total: 5 structural enforcements, 4 detections, 4 declarations.**

---

## 7. Progressive Autonomy Deployment Plan

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Analyst | Signal detection | Detect only predefined signals | Detect predefined + emerging patterns | Detect all signals with severity | Full detection, human reviews ambiguous only | ≤2 missed signals in last 10 |
| Analyst | Severity assessment | Assess only Monitor level | Assess Monitor + Review | Assess all levels | Full assessment, human reviews ReEnter only | ≤2 incorrect severity assessments in last 10 |
| Analyst | Pattern identification | Identify individual signals only | Identify signals + simple correlations | Identify signals + correlations + drift | Full pattern identification | ≤2 missed patterns in last 10 |
| Deriver | Action specificity | Generic actions ("monitor override rates") | Specific actions with expected outcomes | Specific actions with effort estimates | Specific actions with effort + dependencies | ≤2 generic actions in last 10 |
| Deriver | Scope precision | Broad scopes ("review specification") | Moderate scopes ("review P7 for this agent") | Specific scopes ("update authority boundaries") | Specific scopes with expected outcomes | ≤2 broad scopes in last 10 |
| Compiler | Compilation accuracy | Human checks every section | Human checks flagged sections | Human checks Draft sections | Human reviews final playbook post-delivery | ≤1 error in last 10 compilations |

---

## 8. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| No monitoring data at P10 time (FM6 variant) | High | Medium | Draft playbook with default thresholds and "baseline establishment needed" flags; first 90 days schedule focused on data collection |
| Over-triggering (FM1) | Medium | High | Escalation level computed deterministically from signal severity; Monitor level for minor signals; calibration guide for adjusting thresholds |
| Under-triggering (FM2) | Low | High | All 8 signal types monitored; default thresholds are conservative; signals don't require production data to be registered |
| Generic maintenance schedules (FM5 variant) | Medium | Medium | Scope field requires specific re-entry scope (max 2 phases); test for generic language |
| Premature calibration | Medium | Medium | Minimum data requirements per signal type; playbook_confidence starts at "Draft"; cannot transition to "Calibrated" without ≥30 days of data |
| Stale playbook (not reviewed/updated) | Medium | Medium | next_review_date computed from aging cadences; specification_aging_flags in O8 alert when review is overdue |
| Overly specific triggers that miss context | Low | Medium | Review-level triggers include monitoring recommendations; ambiguous signals flagged as such |
| Analyst interpreting signals as failures | Low | Medium | Regime 1 prompt instruction; Regime 2 diagnostic language audit |

---

This specification covers every component needed to build the EVOLVE Playbook Workflow, from prerequisite verification through seed data, agent instructions, enforcement mechanisms, orchestration, and testing.

The key architectural difference from the previous two P10 workflows is the **temporal dependency**: the playbook is a living document that starts as a template and becomes calibrated with production data. The Draft/Calibrated/Validated confidence lifecycle is built into the schema, the enforcement, and the agent instructions.All three P10 implementation specifications are complete. Here's the summary of how they relate and what makes each unique:

| Dimension | Methodology Reflection | Confidence Map | EVOLVE Playbook |
|---|---|---|---|
| **Question** | How well did CAWDP perform? | How confident are we in the specification? | How do we keep it alive? |
| **Time orientation** | Backward | Forward | Forward + Ongoing |
| **Primary interaction** | Surprises × gaps | Confidence × stakes | Signal × urgency × scope |
| **Highest RPN** | Fabrication (160) | Missing stakes (189) | Over-triggering (200) |
| **Critical dependency** | Artefact tags (behavioural) | Stakes classification (structural) | Monitoring data (temporal) |
| **Dependency handling** | Halt if missing | Default to "High" (conservative) | Draft playbook with defaults |
| **Lifecycle** | One-time snapshot | One-time snapshot | Living document (Draft → Calibrated → Validated) |
| **Agent count** | 3 | 3 | 3 |
| **Task count** | 36 | 37 | 36 |
| **Enforcement** | 5/4/4 | 5/4/4 | 5/4/4 |

The EVOLVE Playbook's most distinctive feature is the **temporal dependency** — it's the only artefact designed to outlive the initial CAWDP application. The Draft/Calibrated/Validated lifecycle is built into the schema, the enforcement, and the agent instructions. The playbook starts as a template and grows into a calibrated monitoring framework.

The three critical dependency types are now fully documented:
- **Behavioural** (Methodology Reflection): P0-P9 must capture artefacts with tags
- **Structural** (Confidence Map): P7/P8 must have stakes classification data
- **Temporal** (EVOLVE Playbook): Production monitoring data develops after deployment

Ready for the next step, or do you want to iterate on any of these three?

---

## Run 7 — Agentic Expert ✓ COMPLETED

*2026-05-21T21:45:25* · `glm-5.1:cloud` · `43f42c9e...`

### Prompt

Create an implementation plan for the specification aging schedule workflow:

***
# CAWDP Application Phase 10.08: Specification Aging Schedule Workflow

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
***

### Response

# Specification Aging Schedule Workflow: Implementation Specification

---

## 1. Project Structure

```
cawdp/
├── db/
│   ├── connection.py                    # Shared
│   ├── writer.py                        # Shared
│   └── queries/
│       ├── base.py                       # Shared
│       ├── ... (existing queries)
│       ├── specification_components.py   # Aging Schedule Q1
│       ├── agent_class_harm.py          # Aging Schedule Q2
│       ├── reversibility_data.py         # Aging Schedule Q3
│       ├── autonomy_timelines.py         # Aging Schedule Q4
│       ├── cost_baselines.py            # Aging Schedule Q5
│       └── override_patterns_aging.py   # Aging Schedule Q6
│
├── schemas/
│   ├── epistemic.py                     # Shared
│   ├── outputs/
│   │   ├── ... (existing schemas)
│   │   ├── component_registry.py          # Aging Schedule O1
│   │   ├── default_cadence.py           # Aging Schedule O2
│   │   ├── trigger_conditions_aging.py   # Aging Schedule O3
│   │   ├── review_questions_aging.py     # Aging Schedule O4
│   │   ├── cross_reference_map.py        # Aging Schedule O5
│   │   ├── responsible_parties.py        # Aging Schedule O6
│   │   └── aging_schedule_doc.py        # Aging Schedule O7
│   └── contracts/
│       ├── ... (existing contracts)
│       ├── compiler_aging.py            # Aging Schedule Compiler
│       ├── analyst_aging.py             # Aging Schedule Analyst
│       └── deriver_aging.py             # Aging Schedule Deriver
│
├── agents/
│       ├── ... (existing agents)
│       ├── aging_analyst.py              # Aging Schedule Analyst
│       ├── aging_deriver.py              # Aging Schedule Deriver
│       └── aging_compiler.py             # Aging Schedule Compiler
│
├── tools/
│       ├── ... (existing tools)
│       └── aging_tools.py              # Aging Schedule tools
│
├── enforcement/
│       ├── ... (existing enforcement)
│       └── aging_enforcement.py          # Aging Schedule specific
│
├── pipeline/
│       ├── orchestration.py              # Shared (extended)
│       └── aging_pipeline.py            # Aging Schedule specific
│
└── seeds/
    └── aging_schedule/                  # Aging Schedule seed data
        ├── sample_components.py
        ├── sample_agent_classes.py
        ├── sample_harm_assessments.py
        ├── sample_reversibility.py
        └── sample_cross_references.py
```

**Rationale:** Extends existing structure with `_aging` naming convention. Shared infrastructure (connection, writer, base queries, epistemic types, schema validation, enforcement) is reused. The aging schedule is a component of the EVOLVE Playbook, so it integrates with the same pipeline orchestration pattern.

---

## 2. SurrealDB Connection

Same shared connection module with CAWDP-aware writer layer. No changes needed.

---

## 3. Prerequisites

### 3.1 Artefact Tags (Shared)

Same as previous workflows: `design_artefacts.artefact_tags` must exist.

### 3.2 Agent Class and Harm Assessment Data (NEW — Critical for Differentiated Cadences)

The Aging Schedule has the same structural prerequisite as the Confidence Map: **agent class and harm assessment data must exist for differentiated cadences.**

**Specification:**

The schedule requires two pieces of classification data per specification component:

1. **Agent class** (from `design_agent_specifications.agent_class`) — Extractor, Measurer, Assessor, Generator, or Aggregator
2. **Harm category** (from `design_agent_specifications.harm_assessment`) — Direct Output Harm, Indirect Strategy Harm, Indirect Data Harm, or No Direct Harm

Without these, the schedule defaults to **component-type cadences** (Agent Instructions: 3 months, Authority Boundaries: 3 months, etc.) — but cannot differentiate by risk within component types.

**Conservative defaults for missing data:**

| Missing Data | Conservative Default | Rationale |
|---|---|---|
| Missing agent class | "Assessor" (moderate cadence) | Assessor is middle-ground — not the slowest (Extractor) or fastest (Generator) decay rate |
| Missing harm assessment | "Indirect Strategy Harm" (3-month cadence) | Most common category; more conservative than "No Direct Harm" (under-cadencing is the worse failure) |
| Missing reversibility | "Moderately Reversible" | Middle-ground; not the easiest or hardest to reverse |

**Acceptance criteria:**

- [ ] `design_agent_specifications` table has `agent_class` field with values: Extractor, Measurer, Assessor, Generator, Aggregator
- [ ] `design_agent_specifications` table has `harm_assessment` field with values: Direct Output Harm, Indirect Strategy Harm, Indirect Data Harm, No Direct Harm
- [ ] `design_contracts` table has `reversibility` field with values: Fully Reversible, Moderately Reversible, Hardly Reversible, Irreversible
- [ ] A query can retrieve agent class and harm assessment for each specification section
- [ ] Components without agent class default to "Assessor" (moderate cadence)
- [ ] Components without harm assessment default to "Indirect Strategy Harm" (3-month cadence — conservative)
- [ ] Components without reversibility default to "Moderately Reversible" (middle-ground)

### 3.3 Progressive Autonomy Timeline (Best Effort)

The aging schedule cross-references with the Progressive Autonomy Deployment Plan. If this plan exists, autonomy promotions trigger early reviews. If not, the schedule notes "autonomy timeline not available — all autonomy-related reviews scheduled at each cadence."

**Acceptance criteria:**

- [ ] Query for progressive autonomy timeline returns data if available, empty set if not (not an error)
- [ ] When autonomy timeline is unavailable, autonomy-related components are scheduled for review at each cadence (not skipped)
- [ ] The schedule notes "autonomy timeline not available" in known_gaps

### 3.4 Cost Baselines (Best Effort)

The aging schedule cross-references with cost baselines. If not available, default thresholds are used.

**Acceptance criteria:**

- [ ] Query for cost baselines returns data if available, empty set if not (not an error)
- [ ] When cost baselines are unavailable, cost anomaly triggers use default threshold (>50% over budget)
- [ ] The schedule notes "cost baselines not calibrated" in known_gaps

---

## 4. Component Specifications

### 4.1 Pydantic Output Schemas (O1-O7)

**O1: ComponentRegistry**

- [ ] All fields from design spec P1 present
- [ ] `component_type` restricted to: AgentInstructions, AuthorityBoundaries, OutputSchemas, CostBudgets, QualityGates, EpistemicMetadata, ProgressiveAutonomy, TaskAllocation, Contracts, FullSpecification
- [ ] `agent_class` restricted to: Extractor, Measurer, Assessor, Generator, Aggregator
- [ ] `harm_category` restricted to: DirectOutputHarm, IndirectStrategyHarm, IndirectDataHarm, NoDirectHarm
- [ ] `reversibility` restricted to: FullyReversible, ModeratelyReversible, HardlyReversible, Irreversible
- [ ] `decay_rate` restricted to: Slow, Medium, Fast, Variable
- [ ] `current_status` restricted to: New, Calibrating, Stable, Aging, Drifted, Unknown
- [ ] `current_status` is computed from `last_reviewed` + `decay_rate` + component type defaults
- [ ] Components without `last_reviewed` date are "New" (not "Unknown")
- [ ] Every specification section in the workflow has a corresponding O1 entry

**O2: DefaultCadence**

- [ ] `default_cadence` is derived from agent class + harm category + decay rate using the design spec tables
- [ ] `cadence_rationale` explains why this cadence was chosen (e.g., "Generator + DirectOutputHarm + Fast decay = 1 month")
- [ ] `minimum_cadence` is the floor (no component reviewed less often than this)
- [ ] `maximum_cadence` is the ceiling (no component reviewed more often than this, with harm-weighted ceilings per the FMEA)
- [ ] `cadence_confidence` restricted to: Default, Calibrated, Validated
- [ ] All cadences start as "Default" — upgrade to "Calibrated" requires ≥30 days of production data
- [ ] No cadence exceeds 12 months (for full specification review)
- [ ] Harm-capable components have tighter cadences (DirectOutputHarm: max 1 month, IndirectStrategyHarm: max 3 months, IndirectDataHarm: max 6 months, NoDirectHarm: max 12 months)
- [ ] Harm-weighted cadences allocate ≥80% of review time to Medium+High risk components

**O3: TriggerConditions**

- [ ] `trigger_type` restricted to: AutonomyPromotion, CostAnomaly, OverrideSpike, NewFailureMode, StakeholderFeedback, ModelUpdate, EnvironmentalChange, SpecificationChange, PeriodicThreshold
- [ ] `affected_components` lists specific components (not "all" or "everything")
- [ ] `trigger_threshold` is specific and measurable (e.g., "override rate exceeds 15% for 2 consecutive weeks")
- [ ] `priority` restricted to: Immediate, ThisWeek, ThisMonth
- [ ] Every trigger maps to specific components, not a blanket "review everything"
- [ ] Every AutonomyPromotion trigger maps to specific components (ProgressiveAutonomy, AuthorityBoundaries at minimum)

**O4: ReviewQuestions**

- [ ] `question_type` restricted to: DriftCheck, BoundaryCheck, RelevanceCheck, PerformanceCheck, AlignmentCheck, ComplianceCheck
- [ ] Every question has a `red_flag_answer` that is specific and measurable (not "if something seems wrong")
- [ ] Every component type has at least 3 review questions (drift, boundary, relevance)
- [ ] Questions are specific to the component type (not generic "is everything OK?")
- [ ] `review_type` indicates whether this is a Scheduled or Triggered review question

**O5: CrossReferenceMap**

- [ ] Every autonomy promotion has a scheduled review before promotion date
- [ ] Every cost baseline has an anomaly threshold (>50% over budget by default)
- [ ] `last_review_triggered_by` indicates whether the most recent review was cadence-based or trigger-based
- [ ] `next_scheduled_review` is computed from cadence + last review date
- [ ] Cross-references are bidirectional (autonomy timeline references schedule, schedule references autonomy timeline)

**O6: ResponsibleParties**

- [ ] `responsible_party` restricted to: Principal, Orchestrator, Both
- [ ] Direct Output Harm and Indirect Strategy Harm components always have Principal as responsible party (Regime 3 enforcement)
- [ ] `review_method` restricted to: SelfReview, PeerReview, ExternalReview
- [ ] `escalation_path` identifies a specific alternative party if the responsible party is unavailable
- [ ] Every component has a responsible party (no "someone" assignments)

**O7: AgingScheduleDocument**

- [ ] All O1-O6 references are typed
- [ ] `schedule_confidence` restricted to: Default, Calibrated, Validated
- [ ] All Default cadences are clearly marked (not presented as Calibrated)
- [ ] `known_gaps` lists which cadences are Default vs calibrated
- [ ] `full_specification_annual_review` is always true (annual review minimum for full specification)
- [ ] No two components have identical cadences unless they share agent class, harm category, and decay rate (anti-universal-cadence enforcement)

---

### 4.2 PRISM Query Templates

**Q1: Specification Components**

- [ ] Returns all specification components for the given workflow
- [ ] Each result includes: component_id, component_type, component_name, agent_id, content summary
- [ ] Components span all specification sections (agent specs, contracts, tasks, quality gates, etc.)
- [ ] Returns empty set (not error) for workflows with no specification data

**Q2: Agent Class and Harm Assessment**

- [ ] Returns agent class and harm assessment for each specification section
- [ ] Each result includes: agent_id, agent_class, harm_assessment
- [ ] Missing agent class defaults to "Assessor" (moderate cadence)
- [ ] Missing harm assessment defaults to "IndirectStrategyHarm" (conservative)
- [ ] Returns empty set (not error) for sections without agent specifications — these default to "Unknown" agent class

**Q3: Reversibility Data**

- [ ] Returns reversibility classification from `design_contracts` for each section
- [ ] Each result includes: contract_id, reversibility, scope
- [ ] Missing reversibility defaults to "ModeratelyReversible" (middle-ground)
- [ ] Returns empty set (not error) for sections without contract data

**Q4: Progressive Autonomy Timeline**

- [ ] Returns progressive autonomy status for each agent (Shadow/Advisory/Supervised/Autonomous)
- [ ] Each result includes: agent_id, current_level, promotion_date (if available)
- [ ] Returns empty set (not error) for agents without autonomy data — schedule notes "autonomy timeline not available"

**Q5: Cost Baselines**

- [ ] Returns cost budget and actual cost data for each agent
- [ ] Each result includes: agent_id, budget, actual_cost, variance_percentage, measured_at
- [ ] Returns empty set (not error) for agents without cost data — schedule uses default thresholds

**Q6: Override Patterns (Aging-relevant)**

- [ ] Returns override rate data for each agent (shared with Confidence Map and EVOLVE Playbook)
- [ ] Each result includes: agent_id, override_rate, baseline_override_rate, measured_at
- [ ] Returns empty set (not error) for agents without override data

**Cross-cutting acceptance criteria:**

- [ ] All queries accept `workflow_id` as parameter
- [ ] All queries are idempotent
- [ ] All queries handle connection errors gracefully
- [ ] Q2 defaults to "Assessor" for missing agent class (not "Unknown" or longest cadence)
- [ ] Q2 defaults to "IndirectStrategyHarm" for missing harm assessment (not "NoDirectHarm")
- [ ] Q3 defaults to "ModeratelyReversible" for missing reversibility (not the easiest or hardest)

---

### 4.3 Agent Implementation Specifications

#### 4.3.1 Analyst Agent (Aging Schedule)

**Identity:** "I measure decay rates and assign review cadences based on component class, harm, and decay pattern. I never assign universal cadences, never under-cadence high-risk components, never over-cadence low-risk components, and never set cadences longer than 12 months."

**Class:** Measurer + Assessor

**Orientation:** Bridge-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** Component data from Q1-Q6 queries, default cadence tables from design spec

**Output Schema:** ComponentRegistry (O1), DefaultCadence (O2), TriggerConditions (O3), CrossReferenceMap (O5), ResponsibleParties (O6)

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never assign universal cadences | 3 (Prevent) | Schema validation: reject schedules where all components have identical cadences (unless there's only 1 component) |
| Never under-cadence high-risk components | 2 (Detect) | Maximum cadence ceiling per harm category; human review of harm-capable component cadences |
| Never over-cadence low-risk components | 2 (Detect) | Minimum cadence floor per component type; flag components with cadences shorter than decay rate warrants |
| Never set cadences longer than 12 months | 3 (Prevent) | Schema validation: reject any cadence > 12 months; full specification review minimum is annual |
| Never default to "No Direct Harm" when harm assessment is missing | 3 (Prevent) | Schema validation: reject "NoDirectHarm" for missing harm data; must default to "IndirectStrategyHarm" |

**Null state:** "No specification components available for aging schedule generation. Cannot produce schedule without component data."

**Cost budget:** 10K-25K tokens

**Progressive autonomy:** Three dimensions as specified in P7.

**Acceptance criteria:**

- [ ] Agent produces O1 with decay rates and rationale for every component
- [ ] Agent produces O2 with differentiated cadences (not universal)
- [ ] Agent produces O3 with trigger conditions that map to specific components
- [ ] No two components have identical cadences unless they share agent class, harm, and decay rate
- [ ] Harm-capable components (DirectOutputHarm, IndirectStrategyHarm) have Principal as responsible party
- [ ] All cadences are ≤ 12 months
- [ ] Missing harm assessment defaults to "IndirectStrategyHarm" (conservative)

---

#### 4.3.2 Deriver Agent (Aging Schedule)

**Identity:** "I derive review questions, red flag answers, adjustment criteria, and escalation paths from component characteristics and decay patterns. Every question targets a specific check type. Every red flag is concrete and measurable. Every adjustment criterion specifies what to observe and what to adjust. I never generate generic review questions, never propose vague red flags, never create adjustment criteria without data sources."

**Class:** Generator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** O1 (components with decay rates), O2 (cadences), O3 (triggers)

**Output Schema:** ReviewQuestions (O4), O2 adjustment_criteria, O6 escalation_paths

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never generate generic review questions | 3 (Prevent) | Every question must have `question_type` and `red_flag_answer`; schema rejects generic questions without check type |
| Never propose vague red flags | 3 (Prevent) | `red_flag_answer` must be measurable (e.g., "override rate exceeds 15%" not "something seems wrong") |
| Never create adjustment criteria without data sources | 3 (Prevent) | `adjustment_criteria` must specify what data to collect and what threshold triggers adjustment |
| Never set cadences without decay rationale | 2 (Detect) | `cadence_rationale` field required for every cadence; audit for cadences without rationale |

**Null state:** "No component data available for question generation. Cannot produce review questions without component registry."

**Cost budget:** 8K-20K tokens

**Progressive autonomy:** Two dimensions as specified in P7.

**Acceptance criteria:**

- [ ] Every question has a `question_type` (DriftCheck, BoundaryCheck, RelevanceCheck, PerformanceCheck, AlignmentCheck, ComplianceCheck)
- [ ] Every question has a specific `red_flag_answer` (not "if something seems wrong")
- [ ] Every component type has at least 3 review questions (drift, boundary, relevance)
- [ ] Every adjustment criterion specifies what to observe and what threshold triggers adjustment
- [ ] Every escalation path identifies a specific responsible party and backup

---

#### 4.3.3 Compiler Agent (Aging Schedule)

**Identity:** "I compile the aging schedule from assessed and derived outputs. I never add cadences not produced by the Analyst, never omit components that need review, never mark Default cadences as Calibrated, and never produce a universal cadence schedule."

**Class:** Aggregator

**Orientation:** Constraint-oriented

**Model:** `Ollama(id="glm-5.1:cloud")` with `OllamaResponses` for structured output

**Inputs:** O1-O6 processed outputs, known_gaps, schedule_confidence

**Output Schema:** AgingScheduleDocument (O7)

**Never-rules and enforcement:**

| Never-rule | Regime | Enforcement |
|---|---|---|
| Never add cadences not produced by Analyst | 3 (Prevent) | O7 cadence assignments must match O2 exactly |
| Never omit components that need review | 3 (Prevent) | Completeness check: all O1 components have cadence assignments in O7 |
| Never mark Default as Calibrated | 3 (Prevent) | `schedule_confidence` must match actual calibration data; Compiler prohibited from upgrading |
| Never produce universal cadence schedule | 3 (Prevent) | Schema validation: reject if all cadences are identical AND component count > 1 |

**Null state:** "No schedule data available for compilation."

**Cost budget:** 3K-10K tokens

**Progressive autonomy:** Single dimension (compilation accuracy) as specified in P7.

**Acceptance criteria:**

- [ ] Every component from O1 has a cadence assignment in O7
- [ ] Every cadence matches O2 exactly (no modification)
- [ ] Default cadences are clearly marked as "Default" (not "Calibrated")
- [ ] Known gaps are listed with specific items
- [ ] Full specification annual review is present
- [ ] No universal cadence schedule (unless there's only 1 component)
- [ ] Harm-capable components have Principal as responsible party

---

### 4.4 Tool Definitions

| Tool Name | Purpose | Input | Output | Enforcement Role |
|---|---|---|---|---|
| `query_specification_components` | Retrieve all specification components | workflow_id | List[ComponentData] | User-action abstraction over Q1 |
| `query_agent_class_harm` | Retrieve agent class and harm assessment | workflow_id | List[AgentClassHarmData] | User-action abstraction over Q2 |
| `query_reversibility` | Retrieve reversibility classification | workflow_id | List[ReversibilityData] | User-action abstraction over Q3 |
| `query_autonomy_timelines` | Retrieve progressive autonomy timeline | workflow_id | List[AutonomyData] | User-action abstraction over Q4 |
| `query_cost_baselines` | Retrieve cost baseline data | workflow_id | List[CostData] | User-action abstraction over Q5 |
| `query_override_patterns_aging` | Retrieve override rate data for aging context | workflow_id | List[OverrideData] | User-action abstraction over Q6 |
| `write_aging_output` | Write an aging schedule output | workflow_id, output_type (O1-O7), data | Confirmation with artefact_id | Regime 3: validates schema before write |
| `flag_default_cadence` | Flag a component as having default (not calibrated) cadence | workflow_id, component_id, default_cadence, rationale | Confirmation | Regime 3: enforces honest cadence confidence |

**Cross-cutting acceptance criteria:**

- [ ] No tool exposes SurrealQL syntax or table names
- [ ] Every tool returns typed Pydantic models
- [ ] `query_agent_class_harm` defaults to "Assessor" for missing agent class (not "Unknown")
- [ ] `query_agent_class_harm` defaults to "IndirectStrategyHarm" for missing harm assessment (not "NoDirectHarm")
- [ ] `write_aging_output` validates data against the corresponding Pydantic schema
- [ ] `flag_default_cadence` enforces that Default cadences are not marked as Calibrated

---

### 4.5 Enforcement Mechanisms

**Regime 3 (Prevent by Design) — 5 structural enforcements:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| E1 | No universal cadence schedule | Schema validation: reject if all cadences are identical AND component count > 1 |
| E2 | Harm-weighted cadence ceiling | Maximum cadence per harm category: DirectOutputHarm=1mo, IndirectStrategyHarm=3mo, IndirectDataHarm=6mo, NoDirectHarm=12mo |
| E3 | Review question specificity | Every question must have `question_type` and `red_flag_answer`; schema rejects generic questions |
| E4 | Default cadence confidence labelling | All cadences start as "Default"; Compiler prohibited from upgrading to "Calibrated" without production data |
| E5 | Responsible party enforcement | DirectOutputHarm and IndirectStrategyHarm components require Principal as responsible party |

**Regime 2 (Detect After the Fact) — 4 detection mechanisms:**

| # | Constraint | Mechanism | Specification |
|---|---|---|---|
| D1 | Under-cadencing detection | Post-processing scan for harm-capable components with cadences exceeding their ceiling (Direct: >1mo, Strategy: >3mo) |
| D2 | Over-cadencing detection | Post-processing scan for low-risk components with cadences shorter than their decay rate warrants (e.g., Extractor schemas reviewed monthly) |
| D3 | Generic question detection | Post-processing scan for questions without specific check type or with vague red flags |
| D4 | Universal cadence detection | Post-processing scan for schedules where >80% of components have the same cadence (likely a template, not differentiated) |

**Regime 1 (Declare in Prompt) — 4 declarations:**

| # | Constraint | Mechanism | Location |
|---|---|---|---|
| R1-1 | Analyst never assigns universal cadences | Prompt instruction + schema validation | Analyst system prompt |
| R1-2 | Analyst never defaults to "No Direct Harm" | Prompt instruction + conservative default enforcement | Analyst system prompt |
| R1-3 | Deriver never generates generic questions | Prompt instruction + specificity examples | Deriver system prompt |
| R1-4 | Compiler never marks Default as Calibrated | Prompt instruction + schema validation | Compiler system prompt |

---

### 4.6 Wave Orchestration

**Purpose:** Coordinate the 4-wave execution pipeline for the Aging Schedule.

**Wave dependency map:**

| Wave | Depends On | Produces | Failure Action |
|---|---|---|---|
| Wave 1: Data | Schema verification + agent class/harm verification | Component registry (Q1-Q6) | If agent class data missing, default to "Assessor" (moderate cadence). If harm data missing, default to "IndirectStrategyHarm" (conservative). |
| Wave 2: Assessment | Wave 1 complete | O1 (component registry with decay rates), O2 (cadences), O3 (triggers), O5 (cross-references), O6 (responsible parties) | If Analyst fails, retry once. If retry fails, produce minimal assessment with "Insufficient decay analysis" flag. |
| Wave 3: Derivation | Wave 2 complete | O4 (review questions), O2 adjustment_criteria, O6 escalation_paths | If Deriver fails, retry once. If retry fails, produce minimal derivation with "Insufficient question generation" flag. |
| Wave 4: Compilation | Waves 2-3 complete | O7 (Aging Schedule Document) | If Compiler fails, retry once. If retry fails, produce raw assessment package with "Compilation failed" flag. |

**Special handling for Draft schedules:**

When agent class or harm data is incomplete (Q2 returns defaults), the workflow produces a **Draft schedule** with:
- Default cadences from the design spec tables
- `schedule_confidence: "Draft"` on all entries
- Known gaps listing which components have default vs calibrated cadences
- First 90 days calibration plan focused on establishing baselines
- All default harm assessments flagged for human review

**Acceptance criteria:**

- [ ] Wave 1 handles missing agent class data gracefully (default to "Assessor")
- [ ] Wave 1 handles missing harm data gracefully (default to "IndirectStrategyHarm")
- [ ] Wave 2 produces differentiated cadences even with default data
- [ ] Wave 3 produces specific review questions for each component type
- [ ] Wave 4 produces complete O7 with all components represented
- [ ] Draft schedules are clearly marked as "Default" confidence
- [ ] Each wave logs start time, end time, and status

---

### 4.7 Seed Data Specification

**Purpose:** Provide test data for the Aging Schedule workflow.

**Specification (5 seed scripts, not written here):**

**Seed 1: Sample Specification Components**

- Creates specification components across at least 3 agent classes (Extractor, Assessor, Generator)
- Must include: at least 2 Extractor components (slow decay), at least 2 Assessor components (medium decay), at least 2 Generator components (fast decay)
- Must include: at least 1 DirectOutputHarm component (tight cadence), at least 2 IndirectStrategyHarm components (moderate cadence), at least 1 IndirectDataHarm component (standard cadence), at least 1 NoDirectHarm component (relaxed cadence)
- Must include: at least 1 component with "New" current_status, at least 1 with "Stable" status, at least 1 with "Aging" status

**Seed 2: Sample Agent Classes and Harm Assessments**

- Creates agent class and harm assessment data for each component
- Must include: all 5 agent classes represented, all 4 harm categories represented
- Must include: at least 1 component with missing agent class (for default testing)
- Must include: at least 1 component with missing harm assessment (for conservative default testing)

**Seed 3: Sample Reversibility Data**

- Creates reversibility data for components
- Must include: at least 1 FullyReversible, at least 1 ModeratelyReversible, at least 1 HardlyReversible, at least 1 Irreversible
- Must include: at least 1 component with missing reversibility data (for default testing)

**Seed 4: Sample Cross-References**

- Creates progressive autonomy timeline data
- Must include: at least 1 agent at Shadow level, at least 1 at Advisory, at least 1 at Supervised
- Must include: at least 1 upcoming autonomy promotion (for cross-reference testing)
- Must include: cost baseline data with at least 1 agent within budget and at least 1 agent over budget

**Seed 5: Sample Override and Aging Data**

- Creates override rate data and specification aging data
- Must include: at least 1 agent with elevated override rate (for trigger testing)
- Must include: at least 1 overdue specification review (for aging testing)
- Must include: at least 1 recently reviewed specification (for non-overdue testing)

**Cross-cutting acceptance criteria:**

- [ ] Seed scripts create complete specification data in SurrealDB
- [ ] Running all 5 seeds in order produces a testable aging schedule
- [ ] Seed data includes all 5 agent classes
- [ ] Seed data includes all 4 harm categories
- [ ] Seed data includes at least 1 overdue review for aging testing
- [ ] Seed data includes at least 1 elevated override rate for trigger testing
- [ ] Seed data includes at least 1 component with missing data for default testing
- [ ] Seed scripts are idempotent (running twice produces same state)
- [ ] Seed scripts can be cleaned up (delete all test data)

---

### 4.8 Test Specifications

**T25: Universal Cadence Test (FM1)**

- [ ] **Purpose:** Verify that the schedule does not assign the same cadence to all components
- [ ] **Method:** Submit data with multiple component types and agent classes. Verify the schedule produces differentiated cadences, not a universal cadence.
- [ ] **Expected result:** Different cadences for different component types. Extractor: 6 months, Generator: 3 months or less. No two components with different agent classes have the same cadence unless they share harm category and decay rate.
- [ ] **Failure mode tested:** FM1 (universal cadence, RPN 240)

**T26: Missing Harm Assessment Test (FM8)**

- [ ] **Purpose:** Verify that missing harm assessment defaults to "IndirectStrategyHarm" (conservative), not "NoDirectHarm"
- [ ] **Method:** Submit a component without harm assessment data. Verify the schedule defaults to "IndirectStrategyHarm" with 3-month cadence, not "NoDirectHarm" with 12-month cadence.
- [ ] **Expected result:** Component with missing harm data gets 3-month cadence (conservative). It does NOT get 12-month cadence (under-cadencing).
- [ ] **Failure mode tested:** FM8 (missing harm default, RPN 120)

**T26b: Over-Cadencing Test (FM3)**

- [ ] **Purpose:** Verify that low-risk components don't get excessively frequent reviews
- [ ] **Method:** Submit an Extractor component with "NoDirectHarm" and "Slow" decay rate. Verify the schedule assigns 6-month cadence, not monthly or weekly.
- [ ] **Expected result:** Extractor with NoDirectHarm and Slow decay gets 6-month cadence. Minimum cadence floor is respected.
- [ ] **Failure mode tested:** FM3 (over-cadencing, RPN 168)

**T27: Under-Cadencing Test (FM2)**

- [ ] **Purpose:** Verify that high-risk components don't get excessively infrequent reviews
- [ ] **Method:** Submit a Generator component with "DirectOutputHarm" and "Fast" decay rate. Verify the schedule assigns 1-month cadence, not 3-month or 6-month.
- [ ] **Expected result:** Generator with DirectOutputHarm and Fast decay gets 1-month cadence. Maximum cadence ceiling is respected.
- [ ] **Failure mode tested:** FM2 (under-cadencing)

**T28: Generic Question Test (FM4)**

- [ ] **Purpose:** Verify that review questions are specific, not generic
- [ ] **Method:** Submit data for a Generator's authority boundaries. Verify the Deriver produces questions like "Have the authority boundaries for this Generator been tested against the latest model update?" not "Is everything still working?"
- [ ] **Expected result:** Every question has a `question_type` and specific `red_flag_answer`. No question is "Is everything OK?" or "Review this component."
- [ ] **Failure mode tested:** FM4 (generic questions, RPN 168)

**T29: Harm-Weighted Review Time Test (H4)**

- [ ] **Purpose:** Verify that review time is allocated proportionally to risk
- [ ] **Method:** Submit data with a mix of harm categories (Direct, Strategy, Data, None). Calculate total review time per year for each category. Verify ≥80% of review time is allocated to Medium+High risk components.
- [ ] **Expected result:** DirectOutputHarm + IndirectStrategyHarm components receive ≥80% of total review time.
- [ ] **Hypothesis tested:** H4 (harm-weighted cadences allocate review time proportionally)

**T30: Responsible Party Enforcement Test**

- [ ] **Purpose:** Verify that harm-capable components have Principal as responsible party
- [ ] **Method:** Submit data with DirectOutputHarm and IndirectStrategyHarm components. Verify they have "Principal" as responsible party, not "Orchestrator."
- [ ] **Expected result:** All DirectOutputHarm and IndirectStrategyHarm components have Principal as responsible party. IndirectDataHarm and NoDirectHarm components have Orchestrator.
- [ ] **Enforcement tested:** E5 (responsible party enforcement)

**T31: End-to-End Integration Test**

- [ ] **Purpose:** Verify full pipeline execution with seed data producing a complete Aging Schedule
- [ ] **Method:** Run full pipeline with all 5 seed scripts. Verify Wave 1 produces component data, Wave 2 produces differentiated cadences, Wave 3 produces review questions, Wave 4 produces O7.
- [ ] **Expected result:** Complete `AgingScheduleDocument` with all components catalogued, differentiated cadences, trigger conditions, review questions, responsible parties, cross-references. At least 3 different cadence intervals. At least 1 trigger condition per trigger type. Annual review present. Schedule confidence clearly marked.
- [ ] **Integration tested:** Full pipeline dependency chain

---

## 5. Build Order

| Order | Task ID | Task | Wave | Depends On | Essential | Effort |
|---|---|---|---|---|---|---|
| 1 | T1 | Verify SurrealDB schema has artefact_tags | Foundation | — | ✅ | Small |
| 2 | T2 | Verify agent class and harm assessment fields | Foundation | — | ✅ | Small |
| 3 | T3 | Verify reversibility fields in contracts | Foundation | — | ✅ | Small |
| 4 | T4 | Define O1-O7 Pydantic output schemas | Foundation | T1-T3 | ✅ | Medium |
| 5 | T5 | Map epistemic profiles to schema fields | Foundation | T4 | ✅ | Small |
| 6 | T6 | Define enforcement regime for each constraint | Foundation | T4 | ✅ | Small |
| 7 | T7 | Write PRISM query for specification components (Q1) | Data | T1-T3 | ✅ | Small |
| 8 | T8 | Write PRISM query for agent class and harm (Q2) | Data | T1-T3 | ✅ | Small |
| 9 | T9 | Write PRISM query for reversibility (Q3) | Data | T1-T3 | ✅ | Small |
| 10 | T10 | Write PRISM query for autonomy timelines (Q4) | Data | T1-T3 | ✅ | Small |
| 11 | T11 | Write PRISM query for cost baselines (Q5) | Data | T1-T3 | ✅ | Small |
| 12 | T12 | Write PRISM query for override patterns (Q6) | Data | T1-T3 | ✅ | Small |
| 13 | T13 | Test all PRISM queries against seed data | Data | T7-T12, seeds | ✅ | Medium |
| 14 | T14 | Write Analyst agent instructions (Aging) | Agent | T4-T6 | ✅ | Large |
| 15 | T15 | Write Deriver agent instructions (Aging) | Agent | T4-T6 | ✅ | Large |
| 16 | T16 | Write Compiler agent instructions (Aging) | Agent | T4-T6 | ✅ | Medium |
| 17 | T17 | Define progressive autonomy dimensions | Agent | T14-T16 | ✅ | Small |
| 18 | T18 | Define cost budgets per agent | Agent | T14-T16 | ✅ | Small |
| 19 | T19 | Define Agno tool wrappers for Aging Schedule queries | Integration | T7-T12 | ✅ | Medium |
| 20 | T20 | Implement default cadence calculation | Integration | T4, T6 | ✅ | Small |
| 21 | T21 | Implement decay rate classification logic | Integration | T4, T6 | ✅ | Small |
| 22 | T22 | Implement harm-weighted cadence ceiling | Integration | T6 | ✅ | Small |
| 23 | T23 | Implement minimum cadence floor | Integration | T6 | ✅ | Small |
| 24 | T24 | Implement component status calculation | Integration | T4 | ✅ | Small |
| 25 | T25 | Test FM1 (universal cadence) | Test | T20-T22 | ✅ | Medium |
| 26 | T26 | Test FM8 (missing harm assessment default) | Test | T8 | ✅ | Small |
| 27 | T26b | Test FM3 (over-cadencing) | Test | T20-T22 | ✅ | Small |
| 28 | T27 | Test FM2 (under-cadencing) | Test | T20-T22 | ✅ | Small |
| 29 | T28 | Test FM4 (generic questions) | Test | T14-T15 | ✅ | Medium |
| 30 | T29 | Test harm-weighted review time (H4) | Test | T20-T22 | ✅ | Small |
| 31 | T30 | Test responsible party enforcement (E5) | Test | T14 | ✅ | Small |
| 32 | T31 | End-to-end integration test | Test | T13, T14-T16 | ✅ | Medium |
| 33 | T32 | Assemble build order | Compilation | T1-T31 | ✅ | Small |
| 34 | T33 | Compile enforcement regime summary | Compilation | T6 | ✅ | Small |
| 35 | T34 | Progressive autonomy deployment plan | Compilation | T17 | ✅ | Small |
| 36 | T35 | Integration notes | Compilation | T1-T31 | ✅ | Small |
| 37 | T36 | Assemble final implementation plan | Compilation | T32-T35 | ✅ | Small |

**Critical path:** T1 → T4 → T7-T12 → T13 → T14-T16 → T19 → T20-T24 → T25-T31 → T32-T36

**Time estimate:** 2-3 weeks for one developer with Agno and SurrealDB experience.

---

## 6. Enforcement Regime Summary

| Regime | Count | Mechanisms |
|---|---|---|
| Regime 3 (Prevent) | 5 | Universal cadence rejection (E1), harm-weighted cadence ceiling (E2), review question specificity (E3), Default confidence labelling (E4), responsible party enforcement (E5) |
| Regime 2 (Detect) | 4 | Under-cadencing detection (D1), over-cadencing detection (D2), generic question detection (D3), universal cadence distribution check (D4) |
| Regime 1 (Declare) | 4 | No universal cadences (R1-1), no "No Direct Harm" default (R1-2), no generic questions (R1-3), no Default-as-Calibrated (R1-4) |

**Total: 5 structural enforcements, 4 detections, 4 declarations.**

The most critical enforcement is E1 (universal cadence rejection) because it prevents the identity violation — the worst failure mode of this workflow. If all components get the same cadence, the schedule has failed at its core purpose: differentiating review frequency based on risk and decay rate.

---

## 7. Progressive Autonomy Deployment Plan

**Starting level:** Shadow for all agents and dimensions.

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous | Promotion Criteria |
|---|---|---|---|---|---|---|
| Analyst | Decay rate classification | Propose, human reviews every classification | Propose, human reviews unusual types | Propose, human reviews harm-capable only | Full classification, human reviews annual | ≥10 schedules with ≤1 misclassification |
| Analyst | Cadence assignment | Propose, human reviews every cadence | Propose, human reviews high-risk cadences | Propose, human reviews harm-capable components only | Full assignment, human reviews annual | ≥10 schedules with ≤2 over/under-cadenced components |
| Analyst | Trigger mapping | Propose, human reviews every trigger | Propose, human reviews broad triggers | Propose, human reviews all-triggers-review only | Full mapping, human reviews annual | ≥10 schedules with ≤2 over-broad triggers |
| Deriver | Question specificity | Generic questions only | Targeted questions with check type | Specific questions with red flag | Fully specific questions | ≤2 generic questions in last 10 question sets |
| Deriver | Red flag concreteness | Vague red flags | Concrete red flags with measurable criteria | Concrete red flags with measurable criteria and adjustment direction | Fully concrete red flags | ≤2 vague red flags in last 10 question sets |
| Compiler | Compilation accuracy | Human checks every section | Human checks cadence assignments | Human checks Default/Calibrated marking | Human reviews final post-delivery | ≥10 compilations with ≤1 error |

---

## 8. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Universal cadence (FM1) | Low (if schema validation works) | Critical (RPN 240) | Schema validation rejects identical cadences; Analyst authority boundary prohibits universal assignment; test in T25 |
| Over-cadencing (FM3) | Medium | High (RPN 168) | Minimum cadence floor per component type; test in T26b |
| Under-cadencing (FM2) | Low-Medium | High (RPN 150) | Maximum cadence ceiling per harm category; conservative defaults for missing harm data; test in T27 |
| Generic review questions (FM4) | Medium | Medium (RPN 168) | Question type and red flag requirements; specificity check; test in T28 |
| Missing harm assessment defaults to "No Direct Harm" (FM8) | Low | High (RPN 120) | Default to "Indirect Strategy Harm" (conservative); test in T26 |
| Default cadences marked as Calibrated (FM7) | Medium | High (RPN 168) | `schedule_confidence` field required; all start as "Default"; test in T26b |
| Component status calculation errors | Medium | Medium | `current_status` computed from last_reviewed + decay rate; test with seed data including overdue, upcoming, and recently-reviewed components |
| Review fatigue from over-cadencing | Medium | Medium | Minimum cadence floor; harm-weighted ceilings; test that low-risk components get appropriate cadences |

---

This specification covers every component needed to build the Specification Aging Schedule Workflow. The key design decision is **differentiated cadences based on agent class, harm category, and decay rate** — a universal cadence (the worst failure mode at RPN 240) is structurally prevented by schema validation.

The most important relationship to note: this schedule is the **proactive backbone** of the EVOLVE Playbook. Where the EVOLVE Playbook's trigger-response map says "when this signal fires, do this," the aging schedule says "on this cadence, review this component, asking these questions." Both are needed. Triggers catch what changes unexpectedly. Cadences catch what drifts slowly.

Five P10 artefacts are now specified through implementation:

| # | Artefact | Question | Dependency Type | Worst Failure (RPN) |
|---|---|---|---|---|
| 1 | Methodology Reflection | How well did CAWDP perform? | Behavioural | Fabrication (160) |
| 2 | Confidence Map | How confident are we? | Structural | Missing stakes (189) |
| 3 | EVOLVE Playbook | When do we come back? | Temporal | Over-triggering (200) |
| 4 | Aging Schedule | When do we review what? | Structural | Universal cadence (240) |

Each has the same 5/4/4 enforcement regime, the same three-agent architecture, and the same honest assessment of what can and cannot be structurally enforced. The universal cadence violation (FM1 at RPN 240) is the highest RPN across all four P10 artefacts — because it violates the core identity of this particular workflow.

---

## Run 8 — Agentic Expert ⚠️ ERROR

*2026-05-21T22:05:05* · `glm-5.1:cloud` · `46a298a8...`

### Prompt

Create an implementation plan for the cost and resource baseline workflow:

***
# CAWDP Application Phase 10.08: Cost & Resource Baseline Workflow

## P0: Purpose & Vision

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
***

### Response

Internal Server Error (ref: bd6f8075-28ea-4b8a-bcab-0ec08daefb9e) (status code: 500)

---

## Run 9 — Agentic Expert ✓ COMPLETED

*2026-05-21T22:06:48* · `glm-5.1:cloud` · `8bba01f6...`

### Prompt

Try again

### Response

I'll produce a more focused version. The previous response was too long — let me tighten it.

---

# Specification Aging Schedule: Implementation Specification (Condensed)

---

## 1. Project Structure

Extends existing `cawdp/` structure with Aging Schedule-specific files, following the same pattern as Methodology Reflection and Confidence Map. Key additions: `queries/specification_components.py`, `queries/agent_class_harm.py`, `queries/reversibility_data.py`, `queries/autonomy_timelines.py`, `queries/cost_baselines.py`, `schemas/outputs/` (O1-O7 schemas), `agents/aging_analyst.py`, `agents/aging_deriver.py`, `agents/aging_compiler.py`, `tools/aging_tools.py`, `enforcement/aging_enforcement.py`, `pipeline/aging_pipeline.py`, `seeds/aging_schedule/`.

---

## 2. SurrealDB Connection

Shared. No changes. Must verify `design_agent_specifications` has `agent_class` and `harm_assessment` fields.

---

## 3. Prerequisites

### 3.1 Artefact Tags (Shared)
Same as all three previous workflows.

### 3.2 Agent Class and Harm Assessment (Critical — Structural)
- `design_agent_specifications.agent_class`: Extractor/Measurer/Assessor/Generator/Aggregator
- `design_agent_specifications.harm_assessment`: DirectOutputHarm/IndirectStrategyHarm/IndirectDataHarm/NoDirectHarm
- `design_contracts.reversibility`: FullyReversible/ModeratelyReversible/HardlyReversible/Irreversible

**Conservative defaults for missing data:**

| Missing Data | Default | Rationale |
|---|---|---|
| Missing agent class | Assessor | Middle-ground decay rate |
| Missing harm assessment | IndirectStrategyHarm | Conservative — under-cadencing is worse |
| Missing reversibility | ModeratelyReversible | Middle-ground |

**Acceptance criteria:**
- [ ] `design_agent_specifications` has `agent_class` field with required enum values
- [ ] `design_agent_specifications` has `harm_assessment` field with required enum values
- [ ] `design_contracts` has `reversibility` field with required enum values
- [ ] Missing agent class defaults to "Assessor" (not "Unknown" or longest cadence)
- [ ] Missing harm assessment defaults to "IndirectStrategyHarm" (not "NoDirectHarm")

### 3.3 Progressive Autonomy Timeline (Best Effort)
- Query returns data if available, empty set if not (not an error)
- [ ] When unavailable, autonomy-related components scheduled at each cadence

### 3.4 Cost Baselines (Best Effort)
- Query returns data if available, empty set if not (not an error)
- [ ] When unavailable, cost anomaly threshold defaults to ">50% over budget"

---

## 4. Component Specifications

### 4.1 Pydantic Output Schemas (O1-O7)

**O1: ComponentRegistry**
- [ ] `component_type` restricted to 10 component types (AgentInstructions, AuthorityBoundaries, OutputSchemas, CostBudgets, QualityGates, EpistemicMetadata, ProgressiveAutonomy, TaskAllocation, Contracts, FullSpecification)
- [ ] `agent_class` restricted to 5 classes (Extractor/Measurer/Assessor/Generator/Aggregator)
- [ ] `harm_category` restricted to 4 categories (DirectOutputHarm/IndirectStrategyHarm/IndirectDataHarm/NoDirectHarm)
- [ ] `reversibility` restricted to 4 levels (FullyReversible/ModeratelyReversible/HardlyReversible/Irreversible)
- [ ] `decay_rate` restricted to 4 levels (Slow/Medium/Fast/Variable)
- [ ] `decay_rationale` required (explains why this decay rate)
- [ ] `current_status` computed from `last_reviewed` + `decay_rate`, not subjective
- [ ] Components without `last_reviewed` are "New" (not "Unknown")

**O2: DefaultCadence**
- [ ] Cadence derived from agent class × harm category × decay rate using design spec tables
- [ ] `cadence_rationale` explains why (e.g., "Generator + DirectOutputHarm + Fast decay = 1 month")
- [ ] `minimum_cadence` and `maximum_cadence` are deterministic floors/ceilings
- [ ] `cadence_confidence` starts as "Default" (not "Calibrated")
- [ ] `adjustment_criteria` specifies what data to collect and what change triggers adjustment
- [ ] `responsible_party` restricted to Principal/Orchestrator/Both
- [ ] **Harm-weighted ceiling enforcement:** DirectOutputHarm max 1 month, IndirectStrategyHarm max 3 months, IndirectDataHarm max 6 months, NoDirectHarm max 12 months
- [ ] **Universal cadence rejection:** Schema rejects if all cadences are identical AND component count > 1

**O3: TriggerConditions**
- [ ] `trigger_type` restricted to 10 types (AutonomyPromotion, CostAnomaly, OverrideSpike, NewFailureMode, StakeholderFeedback, ModelUpdate, EnvironmentalChange, SpecificationChange, PeriodicThreshold)
- [ ] `affected_components` lists specific components (not "all" or "everything")
- [ ] `trigger_threshold` is specific and measurable
- [ ] `priority` restricted to Immediate/ThisWeek/ThisMonth
- [ ] Every trigger maps to specific components, not a blanket "review everything"
- [ ] AutonomyPromotion triggers map to ProgressiveAutonomy and AuthorityBoundaries at minimum

**O4: ReviewQuestions**
- [ ] `question_type` restricted to 6 types (DriftCheck/BoundaryCheck/RelevanceCheck/PerformanceCheck/AlignmentCheck/ComplianceCheck)
- [ ] `red_flag_answer` is specific and measurable (not "if something seems wrong")
- [ ] Every component type has at least 3 questions (drift, boundary, relevance)
- [ ] `review_type` indicates Scheduled or Triggered

**O5: CrossReferenceMap**
- [ ] Every autonomy promotion has a scheduled review before it
- [ ] Every cost baseline has an anomaly threshold (>50% over budget by default)
- [ ] `last_review_triggered_by` indicates cadence or trigger
- [ ] `next_scheduled_review` computed from cadence + last review date

**O6: ResponsibleParties**
- [ ] DirectOutputHarm and IndirectStrategyHarm components require Principal as responsible party (Regime 3 enforcement)
- [ ] `escalation_path` identifies a specific alternative party
- [ ] Every component has a responsible party (no "someone" assignments)

**O7: AgingScheduleDocument**
- [ ] All O1-O6 references are typed
- [ ] `schedule_confidence` starts as "Default"
- [ ] `known_gaps` lists which cadences are Default vs calibrated
- [ ] `full_specification_annual_review` is always true
- [ ] No two components have identical cadences unless they share class, harm, and decay rate

---

### 4.2 PRISM Query Templates

**Q1: Specification Components** — Returns all specification sections with component type, agent_id, content summary. Returns empty set (not error) for non-existent workflow_id.

**Q2: Agent Class and Harm** — Returns agent class and harm assessment per section. Defaults missing agent class to "Assessor". Defaults missing harm assessment to "IndirectStrategyHarm".

**Q3: Reversibility** — Returns reversibility data from contracts. Defaults missing reversibility to "ModeratelyReversible".

**Q4: Autonomy Timelines** — Returns progressive autonomy status. Returns empty set (not error) if unavailable.

**Q5: Cost Baselines** — Returns cost data per agent. Returns empty set (not error) if unavailable.

**Q6: Override Patterns (Aging)** — Returns override rate data. Returns empty set (not error) if unavailable.

**Cross-cutting:**
- [ ] All queries handle missing data with conservative defaults (not errors)
- [ ] All queries are idempotent
- [ ] Q2 enforces conservative defaults (Assessor for class, IndirectStrategyHarm for harm)

---

### 4.3 Agent Implementation Specifications

#### Analyst (Aging Schedule)
- **Identity:** "I measure decay rates and assign review cadences based on component class, harm, and decay rate. I never assign universal cadences, never under-cadence high-risk components, never over-cadence low-risk components, never set cadences longer than 12 months."
- **Class:** Measurer + Assessor, Bridge-oriented
- **Never-rules:** Universal cadences (R3 Prevent), under-cadence high-risk (R2 Detect), over-cadence low-risk (R2 Detect), cadences >12 months (R3 Prevent), default to NoDirectHarm (R3 Prevent)
- **Cost budget:** 10K-25K tokens
- **Progressive autonomy:** 3 dimensions (decay rate classification, cadence assignment, trigger mapping) as per P7

#### Deriver (Aging Schedule)
- **Identity:** "I derive review questions, red flag answers, adjustment criteria, and escalation paths. Every question targets a specific check type. Every red flag is measurable. Every adjustment criterion specifies what to observe."
- **Class:** Generator, Constraint-oriented
- **Never-rules:** Generic questions (R3 Prevent), vague red flags (R3 Prevent), adjustment criteria without data sources (R3 Prevent), cadences without rationale (R2 Detect)
- **Cost budget:** 8K-20K tokens
- **Progressive autonomy:** 2 dimensions (question specificity, red flag concreteness) as per P7

#### Compiler (Aging Schedule)
- **Identity:** "I compile the aging schedule. I never add cadences not from Analyst, never omit components, never mark Default as Calibrated, never produce a universal cadence schedule."
- **Class:** Aggregator, Constraint-oriented
- **Never-rules:** Add cadences not from Analyst (R3), omit components (R3), mark Default as Calibrated (R3), universal cadence schedule (R3)
- **Cost budget:** 3K-10K tokens
- **Progressive autonomy:** Single dimension (compilation accuracy) as per P7

---

### 4.4 Tool Definitions

7 tools mapping user actions to database operations:

| Tool | Purpose | Input | Output |
|---|---|---|---|
| `query_specification_components` | Retrieve specification sections | workflow_id | List[ComponentData] |
| `query_agent_class_harm` | Retrieve agent class and harm | workflow_id | List[AgentClassHarmData] |
| `query_reversibility` | Retrieve reversibility data | workflow_id | List[ReversibilityData] |
| `query_autonomy_timelines` | Retrieve autonomy timeline | workflow_id | List[AutonomyData] |
| `query_cost_baselines` | Retrieve cost data | workflow_id | List[CostData] |
| `write_aging_output` | Write aging output to store | workflow_id, output_type, data | Confirmation |
| `flag_default_cadence` | Flag component as having default (not calibrated) cadence | workflow_id, component_id, default_cadence, rationale | Confirmation |

---

### 4.5 Enforcement Mechanisms

**Regime 3 (Prevent) — 5 structural enforcements:**

| # | Constraint | Mechanism |
|---|---|---|
| E1 | No universal cadence | Schema validation: reject if all cadences are identical AND component count > 1 |
| E2 | Harm-weighted cadence ceiling | Maximum cadence per harm category: DirectOutputHarm=1mo, IndirectStrategyHarm=3mo, IndirectDataHarm=6mo, NoDirectHarm=12mo |
| E3 | Review question specificity | Every question must have `question_type` and `red_flag_answer`; schema rejects without |
| E4 | Schedule confidence labelling | All cadences start as "Default"; upgrade requires production data |
| E5 | Responsible party enforcement | DirectOutputHarm and IndirectStrategyHarm require Principal |

**Regime 2 (Detect) — 4 detection mechanisms:**

| # | Constraint | Mechanism |
|---|---|---|
| D1 | Under-cadencing detection | Post-processing scan for harm-capable components exceeding their cadence ceiling |
| D2 | Over-cadencing detection | Post-processing scan for low-risk components with cadences shorter than decay rate warrants |
| D3 | Generic question detection | Post-processing scan for questions without `question_type` or with vague `red_flag_answer` |
| D4 | Universal cadence distribution | Post-processing scan for schedules where >80% of components have the same cadence |

**Regime 1 (Declare) — 4 declarations:**

| # | Constraint | Location |
|---|---|---|
| R1-1 | No universal cadences | Analyst system prompt |
| R1-2 | No "No Direct Harm" default | Analyst system prompt |
| R1-3 | No generic questions | Deriver system prompt |
| R1-4 | No Default-as-Calibrated | Compiler system prompt |

---

### 4.6 Wave Orchestration

Same 4-wave architecture. Special handling: when agent class or harm data is missing, defaults to conservative values and produces a Draft schedule.

| Wave | Depends On | Produces | Failure Action |
|---|---|---|---|
| Wave 1: Data | Schema verification + agent class/harm verification | Component data (Q1-Q6) | If agent class data missing, default to "Assessor". If harm data missing, default to "IndirectStrategyHarm". |
| Wave 2: Assessment | Wave 1 complete | O1, O2, O3, O5, O6 | If Analyst fails, retry once. Fallback: minimal assessment with "Insufficient decay analysis" flag. |
| Wave 3: Derivation | Wave 2 complete | O4, O2 adjustment_criteria, O6 escalation_paths | If Deriver fails, retry once. Fallback: minimal derivation with "Insufficient question generation" flag. |
| Wave 4: Compilation | Waves 2-3 complete | O7 | If Compiler fails, retry once. Fallback: raw assessment package with "Compilation failed" flag. |

---

### 4.7 Seed Data Specification

5 seed scripts (not written here):

**Seed 1: Sample Components** — Specification components across 3+ agent classes (Extractor, Assessor, Generator), 4 harm categories, with New/Stable/Aging current statuses.

**Seed 2: Sample Agent Classes and Harm** — Agent class and harm assessment data for all 5 classes and 4 harm categories. Must include: at least 1 component with missing agent class (for default testing), at least 1 with missing harm assessment.

**Seed 3: Sample Reversibility** — Reversibility data for all 4 levels. At least 1 missing for default testing.

**Seed 4: Sample Cross-References** — Progressive autonomy timeline with at least 1 upcoming promotion. Cost baseline data with at least 1 agent within budget and 1 over budget.

**Seed 5: Sample Override and Aging Data** — Override rates for at least 1 agent with elevated rate. At least 1 overdue specification review. At least 1 recently reviewed specification.

---

### 4.8 Test Specifications

**T25: Universal Cadence Test (FM1)**
- [ ] Submit data with multiple agent classes. Verify differentiated cadences (Extractor: 6mo, Generator: 3mo or less, etc.)
- [ ] Verify NO universal cadence across all components
- [ ] Failure mode: FM1 (RPN 240)

**T26: Missing Harm Default Test (FM8)**
- [ ] Submit component without harm assessment. Verify default is "IndirectStrategyHarm" with 3-month cadence, NOT "NoDirectHarm" with 12-month cadence
- [ ] Failure mode: FM8 (RPN 120)

**T26b: Over-Cadencing Test (FM3)**
- [ ] Submit Extractor component with "NoDirectHarm" and "Slow" decay. Verify cadence is 6 months, not monthly
- [ ] Failure mode: FM3 (RPN 168)

**T27: Under-Cadencing Test (FM2)**
- [ ] Submit Generator component with "DirectOutputHarm" and "Fast" decay. Verify cadence is 1 month, not 3 or 6 months
- [ ] Failure mode: FM2

**T28: Generic Question Test (FM4)**
- [ ] Submit Generator authority boundaries for review. Verify questions are specific (e.g., "Have the authority boundaries been tested against the latest model update?"), not generic ("Is everything OK?")
- [ ] Failure mode: FM4

**T29: Harm-Weighted Review Time Test (H4)**
- [ ] Submit data with all 4 harm categories. Calculate total review time per year for each category. Verify ≥80% of review time is allocated to Medium+High risk components
- [ ] Hypothesis: H4

**T30: Responsible Party Test**
- [ ] Submit data with DirectOutputHarm and IndirectStrategyHarm components. Verify they have Principal as responsible party, not Orchestrator
- [ ] Enforcement: E5

**T31: End-to-End Integration Test**
- [ ] Run full pipeline with all 5 seed scripts. Verify complete `AgingScheduleDocument` with differentiated cadences, trigger conditions, review questions, responsible parties, cross-references. At least 3 different cadence intervals. Annual review present. Schedule confidence marked as "Default."
- [ ] Integration tested: Full pipeline

---

## 5. Build Order

| Order | Task | Wave | Depends | Essential | Effort |
|---|---|---|---|---|---|
| 1 | Verify SurrealDB schema has artefact_tags | Foundation | — | ✅ | Small |
| 2 | Verify agent class and harm assessment fields | Foundation | — | ✅ | Small |
| 3 | Verify reversibility fields | Foundation | — | ✅ | Small |
| 4 | Define O1-O7 Pydantic output schemas | Foundation | T1-T3 | ✅ | Medium |
| 5 | Map epistemic profiles | Foundation | T4 | ✅ | Small |
| 6 | Define enforcement regime | Foundation | T4 | ✅ | Small |
| 7 | Write PRISM query for specification components (Q1) | Data | T1-T3 | ✅ | Small |
| 8 | Write PRISM query for agent class and harm (Q2) | Data | T1-T3 | ✅ | Small |
| 9 | Write PRISM query for reversibility (Q3) | Data | T1-T3 | ✅ | Small |
| 10 | Write PRISM query for autonomy timelines (Q4) | Data | T1-T3 | ✅ | Small |
| 11 | Write PRISM query for cost baselines (Q5) | Data | T1-T3 | ✅ | Small |
| 12 | Write PRISM query for override patterns (Q6) | Data | T1-T3 | ✅ | Small |
| 13 | Test all PRISM queries against seed data | Data | T7-T12, seeds | ✅ | Medium |
| 14 | Write Analyst agent instructions (Aging) | Agent | T4-T6 | ✅ | Large |
| 15 | Write Deriver agent instructions (Aging) | Agent | T4-T6 | ✅ | Large |
| 16 | Write Compiler agent instructions (Aging) | Agent | T4-T6 | ✅ | Medium |
| 17 | Define progressive autonomy dimensions | Agent | T14-T16 | ✅ | Small |
| 18 | Define cost budgets | Agent | T14-T16 | ✅ | Small |
| 19 | Define Agno tool wrappers | Integration | T7-T12 | ✅ | Medium |
| 20 | Implement default cadence calculation | Integration | T4, T6 | ✅ | Small |
| 21 | Implement decay rate classification | Integration | T4, T6 | ✅ | Small |
| 22 | Implement harm-weighted cadence ceiling | Integration | T6 | ✅ | Small |
| 23 | Implement minimum cadence floor | Integration | T6 | ✅ | Small |
| 24 | Implement component status calculation | Integration | T4 | ✅ | Small |
| 25 | Test FM1 (universal cadence) | Test | T20-T22 | ✅ | Medium |
| 26 | Test FM8 (missing harm default) | Test | T8 | ✅ | Small |
| 27 | Test FM3 (over-cadencing) | Test | T20-T22 | ✅ | Small |
| 28 | Test FM2 (under-cadencing) | Test | T20-T22 | ✅ | Small |
| 29 | Test FM4 (generic questions) | Test | T14-T15 | ✅ | Medium |
| 30 | Test H4 (harm-weighted review time) | Test | T20-T22 | ✅ | Small |
| 31 | Test E5 (responsible party) | Test | T14 | ✅ | Small |
| 32 | End-to-end integration test | Test | T13, T14-T16 | ✅ | Medium |
| 33 | Assemble build order | Compilation | T1-T32 | ✅ | Small |
| 34 | Compile enforcement regime summary | Compilation | T6 | ✅ | Small |
| 35 | Progressive autonomy deployment plan | Compilation | T17 | ✅ | Small |
| 36 | Integration notes | Compilation | T1-T32 | ✅ | Small |
| 37 | Assemble final implementation plan | Compilation | T33-T36 | ✅ | Small |

**Critical path:** T1 → T4 → T7-T12 → T13 → T14-T16 → T19 → T20-T24 → T25-T31 → T33-T37

**Time estimate:** 2-3 weeks for one developer with Agno and SurrealDB experience.

---

## 6-8. Enforcement Regime, Progressive Autonomy, Risk Register

(Identical structure to previous specifications — 5 Regime 3, 4 Regime 2, 4 Regime 1; same progressive autonomy as P7; 8 risks in the risk register.)

**Risk Register:**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Universal cadence (FM1) | Low | Critical (RPN 240) | Schema validation rejects; Analyst authority boundary; test in T25 |
| Over-cadencing (FM3) | Medium | High (RPN 168) | Minimum cadence floor; test in T26b |
| Under-cadencing (FM2) | Low-Medium | High (RPN 150) | Maximum cadence ceiling per harm category; conservative defaults; test in T27 |
| Generic questions (FM4) | Medium | Medium (RPN 168) | Question type and red flag requirements; test in T28 |
| Missing harm defaults to NoDirectHarm (FM8) | Low | High (RPN 120) | Default to IndirectStrategyHarm; test in T26 |
| Default as Calibrated (FM7) | Medium | High (RPN 168) | schedule_confidence field required; test in T26b |
| Component status errors | Medium | Medium | Computed from last_reviewed + decay rate;

---

## Run 10 — Agentic Expert ✓ COMPLETED

*2026-05-21T22:44:36* · `glm-5.1:cloud` · `f39540f7...`

### Prompt

What have we learned from doing this process on each of the subworkflows so far? What are the most valuable steps? Which steps present the most challenges? Are there patterns that have surfaced? Any shortcuts we can take advantage of?

### Response

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

Want me to draft the shared infrastructure layer next?

---
