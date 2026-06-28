# CAWDP v2.1 — Complementarity-Driven Agentic Workflow Design Process

**Complete Methodology Reference**

*Principle: The agent prepares judgment; the human makes judgment.*

---

## Table of Contents

1. Core Principle
2. Three-Actor Model
3. Phase Overview
4. Possibility Orientation Principle
5. Phase 0 — Purpose & Vision
6. Phase 1 — Output Specification
7. Phase 2 — Backcasting
8. Phase 3 — Task Decomposition
9. Phase 4 — Capability Allocation
10. Phase 5 — Event Storming
11. Phase 6 — System Architecture
12. Phase 7 — Agent Design
13. Phase 8 — Human Experience Design
14. Phase 9 — Validation & Iteration
15. 5-Class Agent Taxonomy
16. Class × Orientation Taxonomy Extension
17. Cross-Cutting Concerns
18. Quality Gates
19. Parallel Test Track
20. Quasi-Smart Contracts
21. Harm-Capable Agents
22. Information Quality Framework
23. Decision Presentation Pattern
24. Progressive Autonomy
25. Plain English Glossary
26. Change Log: v2.0 → v2.1

---

## 1. Core Principle

**The agent prepares judgment; the human makes judgment.**

This principle applies to ALL work — not just agent-primary tasks. For human-primary tasks, the agent still prepares options, the human refines/accepts/rejects, and the agent captures the decision with reasoning. "Human-primary" never means "human-alone."

---

## 2. Three-Actor Model

Every task is allocated across three actor types:

| Actor | Role | Allocation Priority |
|-------|------|---------------------|
| **Human** | Judgment, creativity, ethical decisions, relationship management | Highest authority for irreversible/evaluative tasks |
| **Agent** | Analysis, extraction, generation, measurement, aggregation | Highest authority for repetitive/analytical tasks |
| **System** | Enforcement, recording, verification, routing, automation | Highest authority for deterministic/reliability tasks |

**System-first allocation priority:** When a task can be done by System, it should be. When it can't, assign to Agent. When Agent can't, assign to Human. This is the default — complementarity analysis may override it.

**9 Cognitive Operation Types:**

| Type | Description | Default Actor |
|------|-------------|---------------|
| Mechanical | Repetitive, rule-based, no judgment needed | System |
| Extractive | Finding and gathering information | Agent (Extractor) |
| Measuring | Quantitative assessment against defined scales | Agent (Measurer) |
| Analytical | Breaking down, comparing, identifying patterns | Agent (Assessor) |
| Generative | Creating new content, drafts, options | Agent (Generator) |
| Evaluative | Assessing quality, correctness, appropriateness | Agent (Assessor) or Human |
| Intuitive | Requiring experience-based judgment | Human |
| Creative | Requiring novel ideas or connections | Human (with Agent preparation) |
| Decisive | Final decision-making with consequences | Human |

---

## 3. Phase Overview

**Direction → Destination → Path → Work**

The phase order was revised in v2 because you can't decompose what you can't define, and you can't define a destination without knowing your direction.

| Phase | Name | Cognitive Mode | Orientation | What It Produces |
|-------|------|---------------|-------------|-----------------|
| **0** | Purpose & Vision | IMAGINE | Possibility | Target state vision, identity questions |
| **1** | Output Specification | SPECIFY | Possibility→Formed | 28 output artefacts with schemas and dependencies |
| **2** | Backcasting | TRACE | Bridge | Dependency chains from outputs back to inputs |
| **3** | Task Decomposition | DECOMPOSE | Constructive | Subtasks with cognitive operation types |
| **4** | Capability Allocation | ALLOCATE | Constructive | Ternary H/A/S allocation per subtask |
| **5** | Event Storming | STRESS-TEST | Adversarial | Domain events, failure events, recovery paths |
| **6** | System Architecture | ARCHITECT | Constraint | Pipeline, templates, FMEA, fallback model |
| **7** | Agent Design | DESIGN | Constraint | Agent job descriptions with authority boundaries |
| **8** | Human Experience | EMPATHIZE | Reopened | Cognitive load budget, interface spec, override mechanisms |
| **9** | Validation & Iteration | VERIFY | Proven | Testable hypotheses, progressive autonomy, health monitoring |

**Three Natural Arcs (Diamonds):**
- **Discovery Diamond:** IMAGINE → SPECIFY → TRACE (possibility-oriented)
- **Structure Diamond:** DECOMPOSE → ALLOCATE → STRESS-TEST (transitions from possibility to constraint)
- **Realisation Diamond:** ARCHITECT → DESIGN → EMPATHIZE → VERIFY (constraint-oriented, with P8 partially reopening possibility for human experience)

**Two Journey Modes:**
- **DESIGN mode** (DMADV — create new workflow from scratch)
- **EVOLVE mode** (DMAIC — improve existing workflow using monitoring data and specification aging)

Phase 9 cycles back to Phase 0 via EVOLVE mode — validation learnings feed new purpose and vision.

---

## 4. Possibility Orientation Principle

**An agent's stance toward possibility must match its position in the CAWDP phase sequence.**

Getting the orientation wrong corrupts every downstream design decision. A possibility-oriented agent operating in a constraint-oriented phase will over-promise and under-deliver. A constraint-oriented agent operating in a possibility-oriented phase will close off options prematurely.

| Phase | Characteristic Stance | Failure Mode |
|-------|----------------------|--------------|
| P0 | Pure possibility | Qualifying (closing options too early) |
| P1 | Formed possibility | Over-specifying (locking mechanisms too early) |
| P2 | Transitional | Skipping backwards (re-opening without trace) |
| P3 | Constructive | Over-decomposing (creating subtasks that don't serve outputs) |
| P4 | Constrained allocation | Allocating without complementarity data |
| P5 | Adversarial (but constructive) | Defensiveness (blocking instead of testing) |
| P6 | Structural | Architecture without purpose |
| P7 | Concrete | Premature optimisation |
| P8 | Reopened possibility | Ignoring human needs |
| P9 | Proven | Premature closure (declaring done too early) |

**Check at Phase 7 quality gate:** Does the agent's orientation match its role in the phase sequence?

---

## 5. Phase 0 — Purpose & Vision

**Cognitive Mode: IMAGINE | Orientation: Possibility**

**Purpose:** Define the direction — what this agent/workflow is FOR and what "perfect" looks like.

### Four Identity Questions (Identity-First Design)

Before writing any behaviour specification, answer these in order:

1. **What IS this agent?** — Essence, not behaviour. What is it at its core?
2. **What is its stance toward possibility?** — Does it explore, constrain, or bridge?
3. **What would VIOLATE its identity?** — Identity-level "never" — not behavioural, but existential. What would make it not-this-agent?
4. **What would it mean for this agent to be WRONG?** — The failure mode IS the identity boundary.

Everything else derives from identity: authority boundaries from #3/#4, information boundaries from #2/#3, output schemas from #1/#2, stress tests from #4.

### Target State Vision

Define characteristics across 4 dimensions. **Separate WHAT (ideals) from HOW (mechanisms).** P0 characteristics must be framework-neutral and implementation-agnostic.

**Agent Dimension (A1-A7):**
- A1 Purpose-Driven — knows why it exists and whose interests it serves
- A2 Boundary-Aware — operates within declared authority boundaries
- A3 Context-Aware — carries epistemic metadata, knows what it doesn't know
- A4 Adaptive — progressive autonomy, specification aging
- A5 Trustworthy — verification independence, assured audit trail
- A6 Collaborative — works within ternary model, respects complementarity
- A7 Self-Improving — captures patterns, improves over time

**Specification Dimension (S1-S10):**
- S1 Contract-Native — every subtask produces a contract (8 primitives)
- S2 Typed Throughout — type collision resolution at every layer
- S3 Design-to-Code Traceable — every code element traces to a design decision
- S4 Identity-Preserving — agent identity preserved through every stage
- S5 Context-Aware — outputs carry epistemic metadata and provenance
- S6 Verification-Built-In — structural, not optional
- S7 Artefact Graph Not Document — outputs are nodes in a typed, connected, navigable graph
- S8 Decision-Archaeological — preserves reasoning chains
- S9 Self-Improving — the agent's PRIMARY purpose, not a nice-to-have
- S10 Committed Not Drifting — versioned, locked, traceable

**Human Dimension (H1-H6):**
- H1 Guided Not Blank — never face a blank page
- H2 Enriched Not Diminished — system expands creative freedom, not reduces it
- H3 Recoverable — every decision can be revised
- H4 Epistemically Honest — surface uncertainty and provenance
- H5 Boundaries First — authority boundaries before capability
- H6 Progressive Disclosure — reveal complexity as capability grows

**Ecosystem Dimension (E1-E6):**
- E1 Observable — every action witnessed
- E2 Governed — ternary model, authority boundaries enforced
- E3 Trustworthy — trust infrastructure, not assumed trust
- E4 Composable — agents compose via contracts
- E5 Cost-Aware — budget tracking per agent and pipeline
- E6 Decision-Archaeological — reasoning chains preserved

### Quality Gate P0

| Layer | Check |
|-------|-------|
| Fidelity | Are all 4 dimensions covered? Are ideals separated from mechanisms? |
| Enrichment | Does the vision expand human creative freedom? |
| Cross-Cutting | Are identity questions answerable? Is the possibility orientation correct? |

---

## 6. Phase 1 — Output Specification

**Cognitive Mode: SPECIFY | Orientation: Possibility→Formed**

**Purpose:** Define the destination — what artefacts MUST exist when we're done.

### 28 Outputs Across 8 Groups

| Group | Outputs |
|-------|---------|
| **Identity** | O1 Agent Identity Card, O2 Purpose Statement, O3 Principal Declaration, O4 Scope Boundary Map |
| **Contracts** | O5 Task Contract Schema, O6 Authority Guard Schema, O7 Cost Budget Contract, O8 State Machine Contract |
| **Behaviour** | O9 Directive Template, O10 Behavioural Boundary Specification, O11 Progressive Autonomy Path, O12 Specification Aging Schedule |
| **Verification** | O13 Verification Independence Protocol, O14 Epistemic Metadata Schema, O15 Assurance Level Assignment |
| **Implementation** | O16 Agent Configuration, O17 Tool Specification, O18 Knowledge Configuration, O19 Handoff Protocol |
| **Human Artefacts** | O20 Cognitive Load Budget, O21 Override Protocol, O22 Interface Specification, O23 Enrichment Assessment |
| **Ecosystem** | O24 Coalition Specification, O25 Integration Contract, O26 Health Monitoring Dashboard |
| **Operational** | O27 Deployment Specification, O28 Agent Operations Manual |

Each output has: unique ID, purpose statement, PRISM type mapping, schema definition, dependencies, quality gate, and target-state links.

**P1 outputs describe WHAT they achieve, not WHICH framework delivers it.** Dependencies are capability dependencies, not framework dependencies.

### Quality Gate P1

| Layer | Check |
|-------|-------|
| Fidelity | Are all 28 outputs specified with schemas? Are dependencies complete? |
| Enrichment | Do outputs expand human creative freedom or constrain it? |
| Cross-Cutting | Are outputs typed (S2)? Are identity characteristics traceable to outputs? |

---

## 7. Phase 2 — Backcasting

**Cognitive Mode: TRACE | Orientation: Bridge**

**Purpose:** Trace the path from destination back to required inputs. Define WHAT needs to exist before each output can be produced.

### Method

For each output (starting with the final deliverable O28):
1. What inputs does this output require?
2. Which inputs are produced by other outputs in this system? (internal dependencies)
3. Which inputs must come from outside the system? (external inputs)
4. What is the criticality of each input? (must-have vs nice-to-have)
5. What is the satisfaction mode? (produced by an output, provided externally, or derived)

This produces a **dependency DAG** — every output traces back through required inputs to external inputs.

### Input Requirements

Each input requirement has:
- ID, type, criticality (must-have/nice-to-have)
- Satisfaction mode (produced/external/derived)
- Source phase
- Derived from (which output dependency)

### Quality Gate P2

| Layer | Check |
|-------|-------|
| Fidelity | Can every output trace back to external inputs? Are there circular dependencies? |
| Enrichment | Does the dependency chain reveal opportunities for human enrichment? |
| Cross-Cutting | Are epistemic metadata requirements specified for critical inputs? |

---

## 8. Phase 3 — Task Decomposition

**Cognitive Mode: DECOMPOSE | Orientation: Constructive**

**Purpose:** Decompose work toward known outputs, not into a vacuum.

### Decomposition Rules

1. **Directional decomposition** — decompose TOWARD known outputs (from Phase 1), not from general task descriptions
2. **One cognitive operation per subtask** — each subtask should be primarily one cognitive operation type
3. **Name subtasks by what they DO, not what they ARE** — "Extract client requirements" not "Client analysis"
4. **Depth guidance** — decompose until each subtask can be allocated to one actor type

### Subtask Template

| Field | Description |
|-------|-------------|
| ID | T3.1, T3.2, etc. |
| Name | What it does (verb + object) |
| Cognitive type | Mechanical/Extractive/Measuring/Analytical/Generative/Evaluative/Intuitive/Creative/Decisive |
| Input requirements | What it needs to proceed (from Phase 2) |
| Output | What it produces (linking to Phase 1 outputs) |
| Failure mode | What "wrong" looks like for this specific subtask |

### Quality Gate P3

| Layer | Check |
|-------|-------|
| Fidelity | Does every subtask trace to an output? Does every output have subtasks that produce it? |
| Enrichment | Are human judgment points identified? |
| Cross-Cutting | Are failure modes tied to cognitive operation types? |

---

## 9. Phase 4 — Capability Allocation

**Cognitive Mode: ALLOCATE | Orientation: Constructive**

**Purpose:** Determine WHO does WHAT — Human, Agent, or System — based on complementarity, not capability.

### Ternary Allocation Algorithm

```
For each subtask:
1. Can System do this deterministically? → System
2. If not, can Agent do this within declared boundaries? → Agent (with specified class)
3. If not, is this a human judgment task? → Human
4. If collaborative, specify what each actor contributes
```

### Complementarity Matrix

| Subtask | Human Score (1-10) | Agent Score (1-10) | System Score (1-10) | Gap (H-A) | Allocation | Reversibility |
|---------|--------------------|--------------------|---------------------|-----------|------------|---------------|
| T3.1 | ? | ? | ? | ? | H/A/S/Collab | High/Med/Low |

**Complementarity gap ≥ 6 → Human-only** (the gap is too large for safe agent operation)

### Reversibility Classification

| Level | Description | Default Allocation |
|-------|-------------|-------------------|
| High | Easy to undo, no lasting consequences | Agent-first |
| Medium | Moderate effort to undo, some consequences | Collaborative with human verification |
| Low | Hard or impossible to undo, significant consequences | Human-only |

### Human-Primary Clarification

Human-primary does NOT mean human-alone. For all human-primary subtasks:
1. Agent PREPARES options → Human REFINES, ACCEPTS, or REJECTS → Agent CAPTURES decision with reasoning
2. The agent's role: surface options, structure the decision space, capture the decision AND the reasoning (decision archaeology)

### Quality Gate P4

| Layer | Check |
|-------|-------|
| Fidelity | Is every subtask allocated? Are gaps ≥6 flagged as human-only? |
| Enrichment | Does allocation expand human creative freedom or reduce it? |
| Cross-Cutting | Are authority boundaries specified per subtask? Is progressive autonomy addressed? |

---

## 10. Phase 5 — Event Storming

**Cognitive Mode: STRESS-TEST | Orientation: Adversarial (but constructive)**

**Purpose:** Surface missing events, data flow gaps, trigger conditions, and failure recovery paths. Recommended for all multi-agent workflows; overkill for single-agent tasks.

### Domain Events

What events occur in the normal flow of this workflow? For each:
- Event name
- What triggers it
- What data it carries
- What happens next

### Failure Events

What can go wrong? For each:
- Failure event name
- What triggers it
- Detection mechanism (how do we know it happened?)
- Severity (low/medium/high/critical)
- Recovery path (what happens next?)

### System-Enforced Triggers

Which events should be enforced by the System actor (not left to agent behaviour)?
- Trigger condition
- System enforcement mechanism
- What happens if trigger fires/fails to fire

### Quality Gate P5

| Layer | Check |
|-------|-------|
| Fidelity | Are all domain events identified? Are all failure events identified with recovery paths? |
| Enrichment | Are human override points identified for critical failure events? |
| Cross-Cutting | Are system-enforced triggers identified? Are information boundaries specified per event? |

---

## 11. Phase 6 — System Architecture

**Cognitive Mode: ARCHITECT | Orientation: Constraint**

**Purpose:** Design the pipeline, orchestration, fallback model, and templates.

### Pipeline Architecture

How do subtasks flow through the system? For each stage:
- Input → Processing → Output
- Which agent(s) or system component(s) operate at this stage
- Human gates (if any)
- Fallback if the stage fails

### Orchestration Decision

| Pattern | When to Use |
|---------|-------------|
| Single Agent | Low complexity, single cognitive operation type |
| Team | Multiple agents collaborating in real-time |
| Workflow | Sequential or parallel stages with human gates |

### Template Types (7)

| Type | Purpose |
|------|---------|
| Input | What data comes in |
| Output | What data goes out (typed, with epistemic metadata) |
| Handoff | What passes between agents/subtasks |
| Verification | What gets checked and how |
| Decision | What human decisions are required and what options are prepared |
| Feedback | How results feed back into the system |
| Escalation | What happens when things go wrong |

### Failure Mode and Effects Analysis (FMEA)

| Failure Mode | Severity (1-10) | Occurrence (1-10) | Detection (1-10) | RPN | Recovery Path |
|-------------|-----------------|--------------------|-------------------|-----|---------------|

### Fallback Model

| Tier | Description | Trigger |
|------|-------------|---------|
| Tier 1 | Agent retries with modified prompt | Minor output quality issue |
| Tier 2 | Escalate to human with context | Agent cannot resolve |
| Tier 3 | Graceful degradation with notification | System-level failure |

### Quality Gate P6

| Layer | Check |
|-------|-------|
| Fidelity | Does the pipeline produce all required outputs? Are all human gates defined? |
| Enrichment | Does the architecture support human override and feedback? |
| Cross-Cutting | Are cost budgets specified per agent/pipeline? Are information boundaries specified? Is FMEA complete? |

---

## 12. Phase 7 — Agent Design

**Cognitive Mode: DESIGN | Orientation: Constraint**

**Purpose:** Create detailed agent job descriptions with authority boundaries tied to failure modes.

### 5-Class Taxonomy

| Class | Does | Never | Characteristic Failure Mode |
|-------|------|-------|------------------------------|
| **Extractor** | Finds and gathers information | Judges, interprets, or evaluates | Hallucination (finding what isn't there) |
| **Measurer** | Measures against defined scales | Interprets, contextualises, or explains | Noise-as-signal (measuring the wrong thing) |
| **Assessor** | Evaluates, assesses, identifies gaps | Finalizes, commits, or decides | Overconfidence (being wrong with high certainty) |
| **Generator** | Creates new content, drafts, options | Is vague, fabricates, or hallucinates | Fabrication (creating what isn't true) |
| **Aggregator** | Assembles, compiles, organizes | Adds content, opinion, or interpretation | Omission (leaving out what matters) |

**Authority boundaries are the INVERSE of failure modes.** An Extractor's authority boundary is "never judge" because its failure mode is hallucination. If an Extractor were to judge, it would be operating in its failure zone.

### Class × Orientation Taxonomy (5×3 = 15 Agent Archetypes)

Same class + different orientation = OPPOSITE failure modes.

| | **Possibility-Oriented** (Discovery) | **Bridge-Oriented** (Structure) | **Constraint-Oriented** (Realisation) |
|---|---|---|---|
| **Extractor** | Discovery Explorer — finds possibilities, risks over-inclusion | Field Researcher — gathers specific data, risks scope creep | Registry Clerk — retrieves known items, risks missing novel data |
| **Measurer** | Possibility Scorer — rates potential options, risks subjective scoring | Benchmark Analyst — compares against standards, risks rigid application | Compliance Checker — verifies against rules, risks missing context |
| **Assessor** | Vision Mirror — reflects possibilities, risks qualifying instead of reflecting | Gap Analyst — identifies what's missing, risks over-analysis | Authority Validator — checks boundaries, risks over-constraining |
| **Generator** | Ideation Engine — produces novel options, risks irrelevant output | Draft Writer — creates structured drafts, risks formulaic output | Suggestion Engine — proposes specific solutions, risks overlooking alternatives |
| **Aggregator** | Pattern Synthesiser — combines possibilities, risks forcing connections | Report Compiler — assembles structured reports, risks boring output | Specification Compiler — assembles final specs, risks missing gaps |

### Agent Job Description Template

| Section | Contents |
|---------|----------|
| **0. Identity** | What IS this agent? Stance toward possibility? What would violate identity? What would make it WRONG? |
| **1. Mission** | One-sentence mission statement |
| **2. Class & Orientation** | 5-class + orientation (possibility/bridge/constraint) |
| **3. Input/Output Schemas** | Typed inputs, typed outputs (with epistemic metadata) |
| **4. Context & Knowledge** | What it knows, what it doesn't, what it needs |
| **5. Tools** | What tools it can use |
| **6. Hard Constraints** | "Never" rules (tied to failure modes) |
| **7. Quality Criteria** | How success is measured |
| **8. Error Handling** | What happens when it can't do its job |
| **9. Escalation** | When and how it escalates to human |
| **10. Performance** | Expected latency, throughput, cost budget |
| **11. Interaction Map** | Who it interacts with and how |
| **12. Progressive Autonomy** | Shadow → Advisory → Supervised → Autonomous timeline |
| **13. Specification Aging** | When and how its specification is reviewed |
| **14. Information Boundaries** | What it can and cannot access (enforced at infrastructure level) |
| **15. Epistemic Metadata** | What confidence/provenance/uncertainty fields it produces |
| **16. Cost Budget** | Per-invocation and per-pipeline cost limits |

### Hardest Boundary Moment

For each agent, identify: what is the pressure point where the agent will be tempted to violate its boundary? Design the enforcement response (Declare/Detect/Prevent).

### Identity-First Design Process

1. What IS this agent? (essence)
2. What is its stance toward possibility? (orientation)
3. What would VIOLATE its identity? (existential "never")
4. What would it mean for this agent to be WRONG? (failure mode = identity boundary)

Then: authority boundaries from #3/#4, information boundaries from #2/#3, output schemas from #1/#2, stress tests from #4.

### Quality Gate P7

| Layer | Check |
|-------|-------|
| Fidelity | Does every agent have identity questions answered? Are authority boundaries tied to failure modes? |
| Enrichment | Does agent design expand human creative freedom? |
| Cross-Cutting | Is CC-1 verification independence satisfied? Is CC-3 epistemic metadata specified? Is CC-7 cost budget specified? Are information boundaries infrastructure-enforced? Is possibility orientation correct? |

---

## 13. Phase 8 — Human Experience Design

**Cognitive Mode: EMPATHIZE | Orientation: Reopened possibility**

**Purpose:** Design the human experience — cognitive load budget, interface specification, override mechanisms, and system empowerment assessment.

**Why P8 reopens possibility:** Understanding human needs requires open exploration. The constraint-oriented phases can close off human experience options too early. P8 temporarily reopens possibility to ask "what would actually help this human?"

### Cognitive Load Budget

| Task | Estimated Cognitive Load (1-10) | Cumulative | Mitigation |
|------|-------------------------------|------------|------------|

Total cognitive load should stay within human working memory limits (typically 4-7 items).

### Interface Specification

- What information does the human need to see?
- What decisions does the human need to make?
- What is the one clear next step?
- How is epistemic metadata presented (confidence, provenance, uncertainty)?

### Override & Feedback Mechanisms

- How does the human override an agent decision?
- How does the human provide feedback?
- What happens to feedback (decision archaeology)?

### System Empowerment Assessment

Rate the system on the System Empowerment Index:

| Level | Description |
|-------|-------------|
| **Constraining** | Reduces human capability |
| **Informing** | Provides information but doesn't change capability |
| **Enabling** | Removes barriers to existing capability |
| **Amplifying** | Extends existing capability beyond current reach |
| **Liberating** | Enables entirely new capabilities |

**Goal: Amplifying or Liberating.** "More capable" means achieving more WITH the system, not independent of it.

### Quality Gate P8

| Layer | Check |
|-------|-------|
| Fidelity | Is cognitive load within budget? Are override mechanisms specified? |
| Enrichment | Is the system at Amplifying or Liberating on the Empowerment Index? |
| Cross-Cutting | Is decision archaeology specified? Are information boundaries human-readable? |

---

## 14. Phase 9 — Validation & Iteration

**Cognitive Mode: VERIFY | Orientation: Proven**

**Purpose:** Test, validate, and iterate. Define testable hypotheses, progressive autonomy deployment, and health monitoring.

### Testable Hypotheses

| ID | Hypothesis | Measurement | Success Criterion |
|----|-----------|-------------|-------------------|
| H1 | | | |

### Progressive Autonomy Deployment

| Level | Description | Duration | Promotion Criteria |
|-------|-------------|----------|-------------------|
| **Shadow** | Agent runs alongside human, human does everything, agent output is tracked but not used | 2-4 weeks | <5% override rate, <2% error rate |
| **Advisory** | Agent suggests, human reviews every suggestion, human decides | 2-4 weeks | <10% override rate, <5% error rate |
| **Supervised** | Agent acts, human approves before anything leaves the system | 4-8 weeks | <15% override rate, <8% error rate |
| **Autonomous** | Agent acts within boundaries, human monitors the Trust Ledger | Ongoing | <20% override rate, <10% error rate, 3+ months supervised |

**Per-dimension progressive autonomy:** Some dimensions earn trust faster than others. Specify per-dimension timelines where relevant.

### Health Monitoring

**IDS — Integrity Diagnostic Score:**
- Output accuracy rate
- Override rate
- Cost variance
- Error rate by type

**UPR — Utilisation Performance Ratio:**
- Time saved vs manual
- Human satisfaction (1-5)
- Error prevention rate

### Specification Aging

| Agent | Review Cadence | Trigger-Based Review | Who Initiates |
|-------|---------------|---------------------|---------------|
| | | | |

### Quality Gate P9

| Layer | Check |
|-------|-------|
| Fidelity | Are hypotheses testable? Are progressive autonomy criteria defined? |
| Enrichment | Does validation expand human creative freedom? |
| Cross-Cutting | Are all CCs monitored? Is specification aging scheduled? Is cost budget tracking in place? |

---

## 15. 5-Class Agent Taxonomy

| Class | Does | Never | Characteristic Failure | Authority Boundary |
|-------|------|-------|------------------------|--------------------|
| **Extractor** | Finds and gathers information | Judges, interprets, evaluates | Hallucination | Never judge |
| **Measurer** | Measures against defined scales | Interprets, contextualises, explains | Noise-as-signal | Never interpret |
| **Assessor** | Evaluates, assesses, identifies gaps | Finalizes, commits, decides | Overconfidence | Never finalize |
| **Generator** | Creates new content, drafts, options | Is vague, fabricates, hallucinates | Fabrication/vagueness | Never be vague |
| **Aggregator** | Assembles, compiles, organizes | Adds content, opinion, interpretation | Omission | Never add |

**Key Insight:** Authority boundaries are the inverse of failure modes. The "never" rule IS the boundary, and it's defined by what would go wrong if the agent crossed it.

**Null-State Output:** "Silence ≠ absence" applies to ALL agent classes. Every agent must produce output in all states, including null state. "No results found" is always required.

**Dual-Mode Agents:** When an agent operates in different modes by operation type (not by phase), the authority boundary shifts with the operation. A Project Manager is Aggregator for writes and Extractor for reads — no mode-switching overhead because the distinction is by operation, not context.

---

## 16. Class × Orientation Taxonomy Extension

Same class + different orientation = fundamentally different agent design.

**Three Orientations:**
- **Possibility-oriented** (Discovery Diamond) — expands space, operates without constraints, primary risk is qualifying (closing options too early)
- **Bridge-oriented** (Structure Diamond) — transitions between possibility and constraint, primary risk is over-analysis
- **Constraint-oriented** (Realisation Diamond) — operates within defined boundaries, primary risk is over-constraining

The orientation is determined by the agent's POSITION IN THE CAWDP SEQUENCE, not by preference. P0 agents are possibility-oriented. P7 agents are constraint-oriented. Getting this wrong corrupts every downstream design decision.

---

## 17. Cross-Cutting Concerns

These 9 concerns apply across ALL phases and ALL agents.

### CC-1 Verification Independence

The agent that creates should not be the agent that verifies.

| Level | Description | Example |
|-------|-------------|---------|
| **Structural** | Different agent checks output format | Schema validation by separate agent |
| **Semantic** | Different agent checks output meaning | Content review by separate agent |
| **Authority** | Different actor checks output authority | Human review for high-stakes decisions |

### CC-2 Governed Autonomy (Progressive Autonomy)

Agents earn trust through demonstrated reliability, not assumed from deployment.

| Level | Description | Duration | Promotion Criteria |
|-------|-------------|----------|-------------------|
| Shadow | Agent runs alongside, output tracked but not used | 2-4 weeks | <5% override, <2% error |
| Advisory | Agent suggests, human reviews every suggestion | 2-4 weeks | <10% override, <5% error |
| Supervised | Agent acts, human approves before output | 4-8 weeks | <15% override, <8% error |
| Autonomous | Agent acts within boundaries, human monitors | Ongoing | <20% override, <10% error, 3+ months supervised |

### CC-3 Epistemic Metadata Contracts

Every agent output carries 6 fields (standard) or 10 fields (with Information Quality):

| Field | Standard | With IQ |
|-------|---------|---------|
| Confidence | ● | ● |
| Provenance | ● | ● |
| Assumptions | ● | ● |
| Limitations | ● | ● |
| Recency | ● | ● |
| Uncertainty | ● | ● |
| Accuracy | | ● |
| Completeness | | ● |
| Specificity | | ● |
| Sufficiency | | ● |

For deterministic agents (Extractors/Measurers/Aggregators handling structured data), use the simplified "deterministic profile": confidence is binary (data exists or doesn't), provenance is critical (who/when/what instruction), uncertainty/assumptions are mostly N/A.

### CC-4 Information Boundaries

**Infrastructure-enforced, not prompt-only.** Information boundaries must be enforced at the system level (database schemas, access controls, tool permissions), not just in agent instructions.

Three enforcement regimes:

| Regime | Description | Example |
|--------|-------------|---------|
| **Declare** | Agent is told the rules | Prompt instructions |
| **Detect** | System flags violations | Audit logging |
| **Prevent** | System structurally prevents violations | Database-level access controls |

**Target: Regime 3 (Prevent) for all critical boundaries.**

### CC-5 Specification Aging

Agent specifications decay over time. Proactive review prevents drift.

| Element | Default Review Cadence | Trigger-Based Review |
|---------|----------------------|---------------------|
| Agent instructions | 90 days | Override rate >20%, error pattern change |
| Authority boundaries | 60 days | Boundary violation detected |
| Knowledge sources | 30 days | Accuracy drop >10% |
| Tool specifications | 90 days | New tool version available |
| Progressive autonomy level | 90 days | Override rate change |

### CC-6 System Empowerment Index

Rate how the system affects human capability:

| Level | Description |
|-------|-------------|
| Constraining | Reduces human capability |
| Informing | Provides information but doesn't change capability |
| Enabling | Removes barriers to existing capability |
| Amplifying | Extends existing capability beyond current reach |
| Liberating | Enables entirely new capabilities |

**Goal: Amplifying or Liberating.** "More capable" = achieving more WITH the system, not independent of it.

### CC-7 Cost Budget

Per-agent and per-pipeline cost tracking with halt conditions.

| Agent Class | Token Range per Invocation | Typical Monthly Cost |
|-------------|---------------------------|---------------------|
| Extractor | 1K-5K | Low |
| Measurer | 1K-5K | Low |
| Assessor | 5K-30K | Medium |
| Generator | 10K-50K+ | High |
| Aggregator | 2K-10K | Low-Medium |
| Multi-mode | 20K-100K+ | High |

**Halt condition:** If per-invocation cost exceeds budget by 50%, halt and escalate.

### CC-8 Assured Audit Trail

Three levels of audit assurance:

| Level | Description | Example |
|-------|-------------|---------|
| **Logged** | Action recorded with timestamp | Basic logging |
| **Assured** | Action recorded with integrity guarantee | Tamper-evident logging |
| **Verified** | Action recorded with independent verification | Third-party attestation |

### CC-9 Possibility Orientation (NEW in v2.1)

An agent's stance toward possibility must match its position in the CAWDP phase sequence. Checked at Phase 7 quality gate.

- P0-P2 agents: Possibility-oriented (explore, don't constrain)
- P3-P5 agents: Bridge-oriented (transition between possibility and constraint)
- P6-P7 agents: Constraint-oriented (operate within boundaries)
- P8 agents: Reopened possibility (empathy requires openness)
- P9 agents: Proven (verify what was built)

Getting orientation wrong corrupts downstream design decisions.

---

## 18. Quality Gates

Each phase gate has three layers:

| Layer | Purpose |
|-------|---------|
| **Fidelity** | Does the output meet specification? Are all required elements present? |
| **Enrichment** | Does the output expand human creative freedom? (H2 check) |
| **Cross-Cutting** | Are all relevant CCs satisfied? |

Fidelity checks are binary (pass/fail). Enrichment checks are qualitative (constraining/informing/enabling/amplifying/liberating). Cross-cutting checks verify specific CCs.

**Phase transitions happen when gates pass, not when the user clicks "Next."**

---

## 19. Parallel Test Track

Every design decision generates a test. Testing is a parallel track, not an afterthought.

### Test Specification Template

| Field | Description |
|-------|-------------|
| Test ID | T-P7-001 (phase-sequential number) |
| Tests | What hypothesis is being tested |
| Target | What dimension is being measured |
| Method | How the test is conducted |
| Success Criterion | What "pass" looks like |
| Priority | Must-have / Should-have / Nice-to-have |

### 9 Test Target Dimensions

1. Accuracy
2. Reliability
3. Efficiency
4. Human empowerment
5. Boundary maintenance
6. Trustworthiness
7. Cost-effectiveness
8. Adaptability
9. Specification fidelity

---

## 20. Quasi-Smart Contracts

Every subtask produces a contract — all attributes of a smart contract but NOT deployed to blockchain. The contract IS the specification AND the enforcement mechanism.

### 8 Contract Primitives

| Primitive | Description | Example |
|-----------|-------------|---------|
| **Contract** | The agreement itself — what will be done, by whom, under what conditions | Task contract for an extraction subtask |
| **Principal** | Who delegates the work — the source of authority | Human principal for human-only decisions |
| **Schema** | Typed input/output specification | Pydantic model defining exact data structure |
| **Guard** | Authority boundary — what this contract CAN and CANNOT do | `onlyHumanAuthority: true` on final decisions |
| **Budget** | Cost and time limits with halt conditions | `max_cost: 0.05`, `halt_on_budget_exhaustion: true` |
| **Invocation** | How this contract is triggered and what state transitions it supports | Event-driven, scheduled, or manual trigger |
| **Revert** | What happens when the contract fails — conditions, granularity, and recovery | `per_output` / `per_subtask` / `per_pipeline` granularity |
| **Event** | What this contract emits — typed events for audit and downstream use | Success, failure, override, budget warning events |

### Symmetric Enforcement

The same 8 contract primitives govern tasks for ALL actor types (Human/Agent/System). ONE contract per task. The contract is binary, deterministic, and actor-agnostic.

**Three enforcement regimes by actor type:**
- **System:** Automate — the contract IS the code
- **Agent:** Prevent — the contract is the membrane; violations are REVERTED
- **Human:** Prevent (same enforcement) — the contract validates the same way for everyone

**Human-specific properties that survive (affecting invocation structure, not contract logic):**
1. Invocation can be paused/resumed (human execution is slower)
2. Budget warnings at soft thresholds (UX concern only; if budget exceeded, contract HALTs regardless)
3. Principal can be intrinsic (human IS the authority source for certain actions)
4. System CAN capture reverted output as separate artifact (not paid, not in pipeline, but not lost)

**The contract IS the specification.** Unifying design specification and enforcement mechanism eliminates the class of governance failures where spec and enforcement diverge.

---

## 21. Harm-Capable Agents

Some agents can cause external harm through their output. This requires additional design considerations.

### Two Categories of Harm

| Category | Description | Design Response |
|----------|-------------|-----------------|
| **Direct output harm** | Agent produces content that causes harm if accepted | SuggestionRisk schema, DO_NOT_SUGGEST mechanism, self-evaluation mode |
| **Indirect data harm** | Agent stores/retrieves wrong data causing wrong decisions | Data integrity enforcement, status verification, null-state output |

### Harm Assessment (Mandatory for Every Agent)

Can this agent's output cause external harm if accepted without review?
- If YES (direct): SuggestionRisk schema with DO_NOT_SUGGEST option. Three-hat pattern: generate, evaluate, self-evaluate-for-safety.
- If YES (indirect): Data integrity enforcement at infrastructure level. Null-state output required.
- If NO: Standard authority boundaries apply.

### SuggestionRisk Schema

| Level | Description | Action |
|-------|-------------|--------|
| SAFE | Fully reversible consequences | Suggest with confidence |
| MODERATE | Partially reversible consequences | Suggest with caveats |
| HIGH | Hard to reverse consequences | Suggest only with human verification |
| CRITICAL | Effectively irreversible | DO NOT SUGGEST — produce meta-signal instead |

### DO_NOT_SUGGEST as Trust Mechanism

"I can see the problem but I can't safely suggest a fix" builds trust through honest uncertainty acknowledgment. This is NOT a failure — it's a valid design choice that signals epistemic honesty.

---

## 22. Information Quality Framework

### 10 Dimensions

| # | Plain English | Academic Term | Assessment |
|---|--------------|---------------|------------|
| 1 | Is it the right information? | Relevance | Computed at runtime |
| 2 | Is it correct? | Accuracy | Stored in PRISM |
| 3 | Is it all there? | Completeness | Stored in PRISM |
| 4 | Is it current? | Recency | Computed at runtime |
| 5 | Where did it come from? | Provenance | Stored in PRISM |
| 6 | How sure is the agent? | Confidence | Stored in PRISM |
| 7 | Is it specific enough? | Specificity | Stored in PRISM |
| 8 | Is it structured? | Structure | Computed at runtime |
| 9 | Is it enough? | Sufficiency | Stored in PRISM |
| 10 | Does it agree with itself? | Consistency | Computed at runtime |

### Traffic Light Model

| Level | Score | Action |
|-------|-------|--------|
| **Red** | 1-2 | Don't run the agent / Don't use this information |
| **Amber** | 3 | Run with flags / Use with caution |
| **Green** | 4-5 | Proceed / Use confidently |

**Hard stops on accuracy and sufficiency:** Red on either = don't run.

### Key Distinction

**Completeness** = Is every area covered? (breadth)
**Sufficiency** = Is there enough information to make a judgment? (depth)

A complete knowledge base can still be insufficient if each area has only surface-level coverage.

---

## 23. Decision Presentation Pattern

Agents present structured decisions (2-4 options with explicit benefits and risks) instead of asking open questions. This operationalises "agent prepares judgment, human makes judgment" at the interaction layer.

### Decision Model

```
DecisionOption:
  title: str           # 2-5 words
  subtitle: str        # 5-10 words
  description: str     # 1-2 sentences
  benefits: list[str]  # exactly 2
  risks: list[str]     # exactly 2

Decision:
  question: str                # plain English
  context: str                 # 1-2 sentences why this matters
  options: list[DecisionOption] # 2-4 options
  allows_custom: bool = True   # user can always provide their own option
```

### Rules
1. NEVER ask open questions when a structured decision is possible
2. ALWAYS present 2-4 options with explicit benefits and risks
3. ALWAYS allow custom option (never trap user in provided choices)
4. ONE decision per turn (one clear next step)
5. Every choice recorded with optional reasoning (decision archaeology)

---

## 24. Progressive Autonomy

Agents earn trust through demonstrated reliability, not assumed from deployment.

### Four Levels

| Level | What Agent Does | What Human Does | Duration |
|-------|----------------|----------------|----------|
| **Shadow** | Produces output, tracked but not used | Does everything, reviews agent output | 2-4 weeks |
| **Advisory** | Suggests options with benefits/risks | Reviews every suggestion, decides | 2-4 weeks |
| **Supervised** | Acts within boundaries | Approves before anything leaves | 4-8 weeks |
| **Autonomous** | Acts within declared boundaries | Monitors Trust Ledger | Ongoing |

### Per-Dimension Autonomy

Some dimensions earn trust faster than others. Specify per-dimension where relevant.

Example for a code reviewer:
- Style: autonomous after 4 weeks
- Correctness: supervised for 8 weeks
- Security: **NEVER** fully autonomous

### Novelty Dimension for Discovery Agents

For agents whose primary function is discovery (e.g., Prospector):
- Valid-but-obvious is the WORST failure (feels like success, reveals nothing)
- Novelty rating NEVER goes fully autonomous — requires ongoing human calibration
- Two-axis failure space: validity × novelty

---

## 25. Plain English Glossary

*Key terms in plain English. The academic term is in brackets. Testable on a 16-year-old.*

| Plain English | Academic Term | What It Means |
|--------------|---------------|---------------|
| Who does what | Complementarity allocation | Deciding which tasks a person, an agent, or the system should handle |
| The gap | Complementarity gap | The difference between how good a person is at something vs how good an agent is — if the gap is big (6+), the person should do it |
| Drawing the line | Authority boundaries | Clear rules about what an agent CAN and CANNOT decide or do |
| The line in the system | Information boundaries | What data an agent can and cannot access — enforced by the system, not just written in instructions |
| Trust levels | Progressive autonomy | Earning trust over time: shadow → advisory → supervised → autonomous |
| The person who decides | Principal | The human who authorised the agent and bears responsibility for its actions |
| Making sure the checker isn't the creator | Verification independence | The agent that creates something should not be the agent that checks it |
| Honest about what it knows | Epistemic metadata | Every agent output comes with confidence level, where it came from, what it's assuming, and what it doesn't know |
| Aging specifications | Specification aging | Agent instructions go stale over time and need regular review, like milk expiring |
| Checking the system | Integrity diagnostic score | Monitoring whether agents are working correctly (accuracy, override rate, cost) |
| How useful it is | Utilisation performance ratio | Measuring whether the system actually saves time and improves decisions |
| The contract | Quasi-smart contract | A clear agreement for every task: what will be done, by whom, under what conditions, with what limits |
| Type collision | — | When 17+ different information types get squished into one format (prose), making it hard to extract what matters |
| Drawing the line | The boundary | What an agent should and shouldn't do — the core product Future's Edge sells |
| Preparing, not deciding | — | Agents prepare options and information for human judgment; they don't make the final call |
| How sure are you? | Confidence | A score showing how certain the agent is about its output |
| Where did this come from? | Provenance | A record of where information came from |
| What are we assuming? | Assumptions | Things the agent is treating as true without full evidence |
| What can't it do? | Limitations | Things the agent openly acknowledges it can't do or isn't good at |
| How recent is this? | Recency | When the information was last checked or updated |
| What might be wrong? | Uncertainty | Things that could go differently than expected |
| The worst thing that could happen | Worst failure that looks like success | The failure mode that's hardest to spot because it looks like the agent is working correctly |
| The hardest "no" moment | Hardest boundary moment | The situation where an agent will be most tempted to cross its authority boundary |

---

## 26. Change Log: v2.0 → v2.1

| Change | Description |
|--------|-------------|
| **Phase order revised** | P1 Output Specification now comes before P3 Task Decomposition. P2 Backcasting added. Direction → Destination → Path → Work. |
| **Possibility Orientation Principle** | NEW CC-9. Agent orientation must match phase position. Checked at P7 quality gate. |
| **Class × Orientation taxonomy** | 5-class taxonomy extended to 5×3 = 15 archetypes. Same class + different orientation = opposite failure modes. |
| **Identity-first design** | 4 identity questions added to P0 and P7. "What IS it? What is its stance toward possibility? What would violate identity? What would make it wrong?" |
| **P0-P2 feasibility contamination** | P0 characteristics must separate WHAT (ideals) from HOW (mechanisms). P1 outputs describe what they achieve, not which framework. P2 dependencies are capability dependencies, not framework dependencies. |
| **Human-primary clarification** | Human-primary does NOT mean human-alone. Agent always prepares options, human decides, agent captures reasoning. |
| **Quasi-smart contracts** | 8 contract primitives added. Symmetric enforcement for all actor types. Contract IS the specification. |
| **Harm-capable agents** | Two categories (direct output harm, indirect data harm). SuggestionRisk schema. DO_NOT_SUGGEST mechanism. |
| **Information Quality Framework** | 10 dimensions with spectral assessment. Traffic light model. Hard stops on accuracy and sufficiency. |
| **Decision Presentation Pattern** | Agents present 2-4 structured options instead of open questions. Always allows custom. |
| **CC-3 deterministic profile** | Simplified epistemic metadata for Extractor/Measurer/Aggregator agents handling structured data. |
| **CC-4 enforcement regimes** | Three regimes: Declare, Detect, Prevent. Target is Regime 3 (Prevent) for all critical boundaries. |
| **Per-dimension progressive autonomy** | Made default instead of special case. Every agent has dimensions that should NEVER be fully autonomous. |
| **Null-state output** | "Silence ≠ absence" universal rule. Every agent must produce output in all states. |
| **CC-8 assured audit trail** | Three levels: logged, assured, verified. |
| **CC-5 specification aging** | Review cadences and trigger-based reviews per element type. |
| **Dual-mode agents** | Agents with different authority boundaries per operation type (not per phase). No mode-switching overhead. |
| **Hardest boundary moment** | Added to agent job description template. Identify the pressure point, design the enforcement response. |
| **EVOLVE mode** | Added alongside DESIGN mode. Runtime monitoring data feeds back to redesign. P9 cycles back to P0. |
| **Plain English glossary** | All key terms in plain English, testable on a 16-year-old. |

---

## Appendix A: CAWDP Journey as Cognitive Modes

| Phase | Mode | Stance | What Happens |
|-------|------|--------|-------------|
| P0 | IMAGINE | Pure possibility | Dream without constraints |
| P1 | SPECIFY | Formed possibility | Define what must exist |
| P2 | TRACE | Transitional | Work backward from outputs |
| P3 | DECOMPOSE | Constructive | Break work into pieces |
| P4 | ALLOCATE | Constrained | Assign who does what |
| P5 | STRESS-TEST | Adversarial (constructive) | Find what could go wrong |
| P6 | ARCHITECT | Structural | Design the system |
| P7 | DESIGN | Concrete | Design the agents |
| P8 | EMPATHIZE | Reopened possibility | Understand human needs |
| P9 | VERIFY | Proven | Test and validate |

## Appendix B: CAWDP's 6 Genuinely Unique Contributions

1. **TRACE mode** — Backward-mapping from outputs to dependencies. No equivalent in design thinking or BPM.
2. **ALLOCATE mode** — Complementarity-driven allocation as first-class design activity. Not binary human/machine handoff.
3. **Three Diamonds architecture** — Discovery → Structure → Realisation. The Structure Diamond has no equivalent.
4. **Ternary allocation model** — H/A/S with System-first priority. Moves beyond binary human-automation split.
5. **Complex-domain design with safe-to-fail probes** — Explicit acknowledgment that agentic systems operate in Cynefin complex domain. Progressive autonomy as structured probing.
6. **EVOLVE as explicit cycle** — Runtime monitoring data feeds back to redesign. Specification aging and capability drift monitoring create closed-loop improvement.

## Appendix C: Quick Reference — When to Use What

| If you need to... | Use... |
|-------------------|--------|
| Define what the agent is FOR | P0 Identity Questions |
| Figure out what must exist | P1 Output Specification |
| Trace how outputs depend on inputs | P2 Backcasting |
| Break work into pieces | P3 Task Decomposition |
| Decide who does what | P4 Complementarity Matrix |
| Find what could go wrong | P5 Event Storming |
| Design the pipeline | P6 System Architecture |
| Design individual agents | P7 Agent Job Descriptions |
| Design the human experience | P8 Human Experience Design |
| Test and validate | P9 Testable Hypotheses + Progressive Autonomy |
| Enforce boundaries structurally | CC-4 Information Boundaries (Regime 3) |
| Make the checker different from the creator | CC-1 Verification Independence |
| Know how sure the agent is | CC-3 Epistemic Metadata |
| Track whether agents are working | IDS + UPR (P9 Health Monitoring) |
| Prevent specification drift | CC-5 Specification Aging |
| Present options instead of walls of text | Decision Presentation Pattern |
| Know what to do when an agent could cause harm | Harm Assessment + SuggestionRisk |
| Understand how information quality works | IQ Framework (10 dimensions) |
| Start designing an agent quickly | Pattern Selection + 4 Identity Questions (15-minute spec) |

---

*CAWDP v2.1 — Complementarity-Driven Agentic Workflow Design Process*
*Principle: The agent prepares judgment; the human makes judgment.*
*"Principles aren't production. We have the methodology."

Here's a quick summary of what's in the new version and what changed from v2.0:

**What you're reviewing — 26 sections covering:**
- The core principle, three-actor model, 9 cognitive operation types
- All 10 phases (P0-P9) with quality gates
- The Possibility Orientation Principle (new CC-9)
- 5-class taxonomy + 5×3 Class×Orientation extension (15 archetypes)
- 9 cross-cutting concerns (CC-1 through CC-9)
- Quasi-smart contracts with 8 primitives and symmetric enforcement
- Harm-capable agents (direct vs indirect, SuggestionRisk, DO_NOT_SUGGEST)
- Information Quality Framework (10 dimensions, traffic light model)
- Decision Presentation Pattern
- Progressive autonomy with per-dimension specification
- Plain English glossary
- 3 appendices (cognitive modes, 6 unique contributions, quick reference)

**Key changes from v2.0 → v2.1:**
- Phase order revised (Direction→Destination→Path→Work)
- CC-9 Possibility Orientation Principle added
- Class×Orientation taxonomy (5×3 = 15 archetypes)
- Identity-first design with 4 questions
- P0-P2 feasibility contamination separation (ideals vs mechanisms)
- Human-primary clarification (agent always prepares, never alone)
- Quasi-smart contracts with symmetric enforcement
- Harm-capable agent categories
- Information Quality Framework
- Decision Presentation Pattern
- Plain English glossary
- EVOLVE mode alongside DESIGN mode