# CAWDP v2.3

## Complementarity-Driven Agentic Workflow Design Process

*The methodology that gets workflows from pilot to production.*

---

## What Changed in v2.3

This version reframes CAWDP from designing **an agent** to designing **a workflow**. A workflow may contain one agent or many; the methodology applies either way. The key changes:

1. **Core reframing**: CAWDP designs workflows, not agents. A single-agent workflow is a valid outcome, but the methodology starts from the workflow's purpose, not the agent's identity.
2. **P0 identity questions** are about the workflow, not the agent. Q1 asks "What does this workflow DO?" not "What IS this agent?"
3. **Class × Orientation taxonomy** applies to workflow roles (participants), not just standalone agents. A workflow may have multiple roles across different classes.
4. **P7 renamed** from "Agent Design" to "Participant Design" — designing each participant in the workflow, whether human, agent, or system.
5. **P8 contracts** govern workflow participants, not just agents. The contract primitives apply to all actor types symmetrically.
6. **P3 decomposition** gains the Decomposition Quality Standard, conflation test, initiation mode, and the Propose+Validate pattern for Intuitive/Evaluative tasks.
7. **P4 allocation** gains two-pass allocation with adjustment factors, the Human-Primary ≠ Human-Only principle, and allocation rationale requirements.
8. **Cognitive operation taxonomy** expanded with Elicitive type, Initiation Mode dimension, and Experience Dependency dimension.
9. **CC-2 strengthened** to require explicit review of "Human-only" allocations for collaborative potential.

---

## Core Principle

**The agent prepares judgment; the human makes judgment.**

Every agent step produces structured decision inputs. Every human step exercises judgment on those inputs. The system enforces the boundary between them.

This principle applies to workflows, not just individual agents. In a multi-step workflow, each agent step prepares judgment for a human step or for the next agent step. The boundary between preparation and judgment is enforced structurally.

---

## Foundational Concepts

### The Possibility Orientation Principle

A workflow's stance toward possibility must match its position in the CAWDP phase sequence. P0 workflows operate in pure possibility. P3+ workflows progressively introduce feasibility. P8 workflows operate in pure constraint. Getting the orientation wrong corrupts every downstream design decision.

| Phase | Stance | Legitimate Question | Characteristic Failure |
|---|---|---|---|
| P0 | Pure possibility | What could be? | Qualifying possibility (narrowing too early) |
| P1 | Formed possibility | What artefacts must exist? | Constraining outputs to current capability |
| P2 | Transitional | What path connects outputs to inputs? | Introducing feasibility before P3 |
| P3 | Constructive | What work must happen? | Ignoring feasibility constraints |
| P4 | Constructive | Who does what? | Allocating without evidence |
| P5 | Constructive→Adversarial | What could fail? | Assuming happy path only |
| P6 | Structural | How do parts compose? | Over-architecting before requirements |
| P7 | Concrete | What is each participant? | Template-filling without genuine judgment |
| P8 | Pure constraint | What must the system enforce? | Reopening possibility |
| P9 | Partially reopens | How does enforcement feel? | Staying purely constrained |
| P10 | Spirals back | Does it work? What evolves? | Declaring success without evolution |

P0-P2 are possibility-oriented: ideals, framework-neutral, implementation-agnostic. Mechanisms belong in P3+.

P9 partially reopens possibility because human experience design requires empathy, which is expansive.

P10 closes back to P0, creating the spiral. The journey is a spiral, not a line.

### Identity-First Design

Every workflow specification begins with identity, not behavior. Five questions, answered before any capability discussion:

| # | Question | What It Reveals | Derives To |
|---|---|---|---|
| Q1 | What does this workflow DO? | Purpose and scope | Workflow class → Purpose primitive |
| Q2 | What is its orientation toward outcome? | Directional stance | Enforcement regime target |
| Q3 | What would VIOLATE the integrity of this workflow? | Process boundary | Guard primitives |
| Q4 | What does a FAILED run of this workflow look like? | Failure mode as quality boundary | Revert + Event primitives |
| Q5 | What is the hardest moment in this workflow — where pressure would push it past its design boundary? | Stress test that confirms identity | Highest-priority Guard |

Everything derives from identity. Authority boundaries derive from Q3 and Q5. Enforcement regimes derive from Q2. Output schemas derive from Q1 and Q2. Stress tests derive from Q4. The cascade is directional and traceable.

The hardest boundary moment (Q5) is the design anchor. It bridges identity (P0) to enforcement (P8). If the specification can't answer Q5, the identity isn't specific enough. If the contract can't enforce the boundary at Q5's hardest moment, the enforcement is insufficient.

### Class × Orientation Taxonomy

The 5-class taxonomy gains a second dimension: orientation. This taxonomy applies to **workflow roles** — the participants in a workflow, whether they are agents, humans, or system components.

| | Possibility-Oriented | Bridge-Oriented | Constraint-Oriented |
|---|---|---|---|
| **Extractor** | Scout (explores, gathers broadly) | Researcher (gathers with direction) | Monitor (watches specific signals) |
| **Measurer** | Surveyor (measures broadly) | Analyst (measures with criteria) | Auditor (measures against standards) |
| **Assessor** | Vision Mirror (reflects possibility) | Evaluator (bridges possibility to constraint) | Authority Validator (enforces boundaries) |
| **Generator** | Ideator (generates broadly) | Drafter (generates with constraints) | Formalizer (generates enforceable output) |
| **Aggregator** | Explorer (assembles broadly) | Compiler (assembles with structure) | Registrar (assembles with enforcement) |

Same class, different orientation, opposite failure modes. A Vision Mirror (Assessor, possibility-oriented) fails by qualifying possibility. An Authority Validator (Assessor, constraint-oriented) fails by not evaluating strictly enough.

Authority boundaries remain the inverse of failure modes. The class determines the boundary; the orientation determines how strictly it's enforced.

A workflow may have multiple participants across different classes and orientations. A single-agent workflow has one participant; a multi-agent workflow has many. The taxonomy applies to each participant role.

### The Five Identity Questions Determine 40-70% of the Specification

Answering Q1-Q5 produces the workflow's class, orientation, never-rules, failure modes, hardest boundary moment, and enforcement regime targets. These cascade into authority boundaries, output schemas, verification protocols, progressive autonomy dimensions, and contract primitives. The remaining 30-60% is capability-specific detail that varies per workflow.

### The Boundary Is the Product

Every authority boundary ties to a specific failure mode. "Decides for the human" → identity violation. "Generic boundary" → false confidence. "Vanity metric" → decorative assessment. The boundary isn't a capability limit — it's a failure-mode prevention mechanism.

This extends to the enforcement boundary itself. The Unenforceable Elements Register (P8) documents where enforcement ends and trust begins. That boundary IS a boundary that must be drawn, documented, and managed.

---

## Phase Sequence

### Direction → Destination → Path → Work → Enforce → Empathize → Verify

| # | Phase | Cognitive Mode | Diamond | Stance | What It Produces |
|---|---|---|---|---|---|
| P0 | Purpose & Vision | IMAGINE | Discovery | Pure possibility | Target state characteristics, 5 identity questions |
| P1 | Output Specification | SPECIFY | Discovery | Formed possibility | Output schemas, dependencies, quality gates |
| P2 | Backcasting | TRACE | Discovery → Structure | Transitional | Dependency chains, input requirements |
| P3 | Task Decomposition | DECOMPOSE | Structure | Constructive | Tasks, cognitive types, failure modes |
| P4 | Capability Allocation | ALLOCATE | Structure | Constructive | Ternary H/A/S matrix |
| P5 | Event Storming | STRESS-TEST | Structure → Realisation | Adversarial | Domain/failure events, recovery paths |
| P6 | System Architecture | ARCHITECT | Realisation | Structural | Pipeline, composition, FMEA |
| P7 | Participant Design | DESIGN | Realisation | Concrete | Participant specifications (human-readable) |
| P8 | Contract Formalization | FORMALIZE | Realisation | Pure constraint | Contract primitives (machine-enforceable) |
| P9 | Human Experience Design | EMPATHIZE | Realisation | Reopens possibility | Cognitive load, overrides, surfaces |
| P10 | Validation & Iteration | VERIFY → EVOLVE | Realisation → Discovery | Spirals back | Hypotheses, testing, health, EVOLVE cycle |

### Three Diamonds

**Discovery:** IMAGINE → SPECIFY → TRACE

Explore what could be, define what must exist, trace how outputs depend on inputs. The Discovery diamond is expansive. It opens the space of possibilities and defines the destination.

**Structure:** DECOMPOSE → ALLOCATE → STRESS-TEST

Break work into tasks, assign each task to the right actor, stress-test the allocation against failure. The Structure diamond is constructive. It introduces feasibility and builds the work plan.

**Realisation:** ARCHITECT → DESIGN → FORMALIZE → EMPATHIZE → VERIFY

Design the pipeline, specify each participant, formalize the contracts, design the human experience, validate and evolve. The Realisation diamond is constraint-oriented with a partial reopening at EMPATHIZE.

### Two Modes

**DESIGN mode** (DMADV): Create a new workflow from scratch. The 11-phase process runs forward from P0 to P10.

**EVOLVE mode** (DMAIC): Improve an existing workflow using monitoring data. Phase 10 cycles back to Phase 0. Specification aging triggers, capability drift signals, and override patterns feed redesign.

Every CAWDP application starts in DESIGN mode. After deployment, EVOLVE mode maintains and improves the workflow. The journey is a spiral: design → deploy → monitor → evolve → redesign.

---

## Phase 0: Purpose & Vision

**Cognitive Mode:** IMAGINE  
**Diamond:** Discovery  
**Stance:** Pure possibility

### What Happens

Define what this workflow is FOR. Describe the perfect outcome. Answer the five identity questions. Establish the target state that every subsequent phase must produce artifacts aligned with.

### Five Workflow Definition Questions

| #  | Question                                                                                             | What It Reveals                  | Example                                                                                                                             |
| -- | ---------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Q1 | What does this workflow DO?                                                                          | Purpose and scope                | "A structured process that transforms a human's vague intent into a typed, executable workflow specification"                      |
| Q2 | What is its orientation toward outcome?                                                              | Directional stance               | Possibility-expanding — opens design space before narrowing it                                                                      |
| Q3 | What would VIOLATE the integrity of this workflow?                                                   | Process boundary                 | "Skipping discovery steps. Locking outputs before inputs are validated. Deciding without the human."                                |
| Q4 | What does a FAILED run of this workflow look like?                                                   | Failure mode as quality boundary | "A completed artefact that captures structure without exercising genuine judgment — template-filling masquerading as specification" |
| Q5 | What is the hardest moment in this workflow — where pressure would push it past its design boundary? | Stress test                      | "When the human says 'just tell me what to pick' — the workflow must still complete discovery, not skip to output"                  |

### Target State Vision

The four dimensions and their characteristics describes an **ideal property of the workflow and its artefacts**.

***

### Workflow Dimension *(What the workflow DOES)*

- **W1 Purpose-Driven:** Exists to serve a declared human intent; every step traces to that origin
- **W2 Boundary-Aware:** Operates within explicitly declared scope; does not expand autonomously
- **W3 Context-Sensitive:** Carries epistemic metadata through every stage; surfaces what is not yet known
- **W4 Adaptive:** Supports progressive elaboration; earlier stages do not over-constrain later ones
- **W5 Auditable:** Every decision point is witnessed and recoverable; produces an assured audit trail
- **W6 Collaborative:** Structured for human-agent-system participation; roles are declared, not assumed
- **W7 Self-Improving:** Captures execution patterns across runs; improves defaults and templates over time

***

### Specification Dimension *(What the specification IS)*

- **S1 Contract-Native:** Every stage output is a typed contract with enforceable boundaries, not a document
- **S2 Typed Throughout:** Type collision is resolved at every handoff layer
- **S3 Design-to-Code Traceable:** Every downstream code element traces to an upstream design decision
- **S4 Identity-Preserving:** The original intent is preserved and traceable through every transformation
- **S5 Verification-Built-In:** Verification is structural — not a final gate but a property of each stage
- **S6 Artefact Graph Not Document:** Outputs are typed nodes in a navigable graph, not a linear document
- **S7 Committed Not Drifting:** Versioned, locked, and traceable at every stage transition

***

### Human Dimension *(What the human experience IS)*

- **H1 Guided Not Blank:** The workflow never presents an empty canvas — every step has a scaffold
- **H2 Enriched Not Diminished:** The process expands creative freedom; it does not narrow it
- **H3 Recoverable:** Every decision made during the workflow is revisable without restarting from zero
- **H4 Epistemically Honest:** Uncertainty and provenance are surfaced, not hidden
- **H5 Boundaries First:** Authority and scope boundaries are declared before capabilities are explored
- **H6 Progressive Disclosure:** Complexity is revealed as the human's readiness and context grow

***

### Ecosystem Dimension *(What the operating context IS)*

- **E1 Observable:** Every workflow action is witnessed with an assured, tamper-evident audit trail
- **E2 Governed:** Authority boundaries are enforced by structure, not policy alone
- **E3 Trustworthy:** Trust is earned through structural verification, not asserted through declaration
- **E4 Composable:** Workflow outputs are typed contracts that compose cleanly with downstream workflows
- **E5 Cost-Aware:** Budget consumption is tracked per stage and per pipeline run
- **E6 Decision-Archaeological:** Reasoning chains are preserved so any output can be traced to its cause

### Human Cold Start

Humans can't always articulate what they want upfront. Identity/purpose/boundary tasks are collaborative by default, regardless of complementarity gap score. The agent prepares options; the human decides. Making these tasks human-only contradicts the core principle.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | 5 identity questions answered. All 4 dimensions have 5+ characteristics. No mechanism contamination (P0-P2 are possibility-oriented). |
| Enrichment | Hardest boundary moment (Q5) is a specific scenario, not an abstract statement. Each characteristic links to a testable criterion. |
| Cross-Cutting | CC-9: All characteristics are possibility-oriented (no feasibility language). CC-3: Confidence level stated for each characteristic. |

---

## Phase 1: Output Specification

**Cognitive Mode:** SPECIFY  
**Diamond:** Discovery  
**Stance:** Formed possibility

### What Happens

Define what artefacts MUST exist when we're done. Types, schemas, dependencies. This is the DESTINATION that every subsequent phase decomposes toward.

### 8 Output Groups (29 outputs)

| Group | Outputs | Purpose |
|---|---|---|
| **Identity** | O1 Workflow Identity Card, O2 Purpose Statement, O3 Principal Declaration, O4 Scope Boundary Map | What this workflow IS and WHO it serves |
| **Contracts** | O5 Task Contract Schema, O6 Authority Guard Schema, O7 Cost Budget Contract, O8 State Machine Contract | How work is governed |
| **Behaviour** | O9 Directive Template, O10 Behavioural Boundary Specification, O11 Progressive Autonomy Path, O12 Specification Aging Schedule | How the workflow behaves |
| **Verification** | O13 Verification Independence Protocol, O14 Epistemic Metadata Schema, O15 Assurance Level Assignment | How we know it's right |
| **Implementation** | O16 Workflow Configuration, O17 Tool Specification, O18 Knowledge Configuration, O19 Handoff Protocol | How it's built |
| **Human Artefacts** | O20 Cognitive Load Budget, O21 Override Protocol, O22 Interface Specification, O23 Enrichment Assessment | How humans experience it |
| **Ecosystem** | O24 Coalition Specification, O25 Integration Contract, O26 Health Monitoring Dashboard, O29 Workflow Diagram | How it fits in the system |
| **Operational** | O27 Deployment Specification, O28 Operations Manual | How it runs |

### Each Output Has

- Unique ID, purpose statement, PRISM type mapping
- Schema definition (typed, not prose)
- Dependencies (linked to other outputs and input requirements)
- Quality gate (what "complete" looks like)
- Target-state links (traces to P0 characteristics)

### Output Dependency Map

Every output depends on other outputs. The dependency graph is a DAG (directed acyclic graph). Circular dependencies indicate a design error.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Every output has schema, dependencies, and quality gate. Dependency graph is acyclic. No orphan outputs (produced but not used). |
| Enrichment | Every output traces to at least one P0 characteristic. No outputs that serve no purpose. |
| Cross-Cutting | CC-9: Output schemas describe WHAT, not HOW (framework-neutral). CC-3: Dependency confidence stated. CC-1: Verification outputs independent from behavioural outputs. |

---

## Phase 2: Backcasting

**Cognitive Mode:** TRACE  
**Diamond:** Discovery → Structure (transition)  
**Stance:** Transitional

### What Happens

Work backward from output artefacts, tracing dependency chains. For each output, identify what inputs it requires. For each input, identify whether it's external (provided from outside) or internal (produced by an earlier phase). Continue until every dependency traces to an external input or a circular dependency is detected.

This is the PATH that connects the destination (P1 outputs) to the work (P3 tasks).

### Input Requirements

Each input requirement has:

| Field | Purpose |
|---|---|
| ir-id | Unique identifier |
| ir-type | External (provided from outside) or Internal (produced by earlier output) |
| ir-criticality | CRITICAL (final deliverable depends on it), HIGH (quality gate depends on it), MEDIUM (supporting), LOW (optional) |
| ir-satisfaction-mode | DIRECT (must be provided), DERIVED (produced by earlier phase), PARTIAL (produced earlier, refined later) |
| ir-source-phase | Which phase produces this input (if internal) |
| ir-derived-from-dependency | Which output dependency created this requirement |

### Gap Detection

| Gap Type | What It Means |
|---|---|
| Missing input | Something needs to exist that nobody produces |
| Circular dependency | Two outputs depend on each other — phase ordering problem |
| Orphan output | Something is produced that nobody needs |
| Critical path gap | A critical dependency has no satisfaction mode |
| Quality gate gap | A gate references something the pipeline doesn't produce |

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | All final deliverable dependencies traced to external inputs. No circular dependencies. No critical path gaps. |
| Enrichment | Gap detection complete. Every gap has a resolution plan or explicit acceptance. |
| Cross-Cutting | CC-9: Input requirements describe WHAT is needed, not HOW it's produced. CC-3: Criticality confidence stated. CC-5: Staleness risk assessed for time-sensitive inputs. |

---

## Phase 3: Task Decomposition

**Cognitive Mode:** DECOMPOSE  
**Diamond:** Structure  
**Stance:** Constructive

### What Happens

Decompose the work required to produce the outputs identified in P1 and traced in P2. Each task has a cognitive type, failure mode, and dependency chain.

### Task Specification

| Field | Purpose |
|---|---|
| Task ID | Unique identifier |
| Description | What this task does (plain English) |
| Cognitive type | Mechanical, Analytical, Generative, Elicitive, Evaluative, Intuitive |
| Initiation mode | Self-starting, Scaffolded, or Discovery |
| Input requirements | Which IRs this task consumes |
| Output produced | Which outputs this task produces |
| Failure mode | What "wrong" looks like for this task |
| Dependency chain | Which tasks must complete before this one |

### Twelve Cognitive Operation Types

The cognitive operation types include primary operations and two qualifying dimensions:

**Primary Cognitive Operation:**

| Type | Description | Default Actor |
|---|---|---|
| Mechanical | Rule-based, repeatable, no judgment required | System or Agent |
| Analytical | Pattern recognition, data processing, measurement | Agent |
| Generative | Creating new content, suggestions, drafts | Agent (with human review) |
| Elicitive | Drawing out, prompting, reflecting | Collaborative (human has answer, agent elicits) |
| Evaluative | Judgment against criteria, assessment, scoring | Human (agent prepares) |
| Intuitive | Expert judgment without explicit criteria | Human (with adjustment for initiation mode) |

**Initiation Mode:**

| Mode | Meaning | Allocation Impact |
|---|---|---|
| Self-starting | Can begin from own knowledge without prompting | Solo allocation possible if capability gap ≥ 6 |
| Scaffolded | Needs structure, template, or prompt to begin | Always collaborative — agent provides scaffold, human fills in |
| Discovery | Discovers what they want by reacting to options | Always collaborative — agent proposes, human refines |

**Experience Dependency:**

| Level | Meaning | Allocation Impact |
|---|---|---|
| Expert-dependent | Only deep domain experience produces quality output | Human-primary, but agent can prepare |
| Pattern-augmented | Broad pattern recognition genuinely improves output | Collaborative — agent brings patterns, human validates |
| Procedural | Follows known procedures and rules | Agent-primary, human reviews |

### The Decomposition Quality Standard

Every subtask must satisfy five properties. If any property is missing, the subtask is conflated, vague, or incomplete — and will produce a bad allocation downstream.

**Property 1: Single Primary Cognitive Operation**

One verb, one thinking type. If you need "and" to describe what the task does, split it.

| ❌ Conflated | ✅ Decomposed |
|---|---|
| "Discover principal's purpose" | "Elicit the principal's purpose through guided conversation" |
| "Identify what this workflow IS" | "Structure the principal's description into a purpose specification" |
| "Define excellent outcomes" | "Propose outcome criteria based on domain patterns" |
| "Identify authority boundaries" | "Propose boundary candidates based on workflow class failure modes" |

The "and" test: "Elicit the principal's purpose **and** structure it into a specification" → two tasks. "Propose boundary candidates **and** validate them for this domain" → two tasks.

**Property 2: Clear Output Artefact**

What concrete thing does this task produce? A document, a decision, a list, a score, a specification. If the output is vague ("understanding," "clarity," "alignment"), the task is not well-decomposed.

| ❌ Vague Output | ✅ Specific Artefact |
|---|---|
| "Discover purpose" | "Purpose statement — one sentence capturing why this workflow exists" |
| "Identify what this IS" | "Identity specification — four identity questions answered" |
| "Define excellent outcomes" | "Outcome criteria — measurable success conditions with thresholds" |
| "Identify boundaries" | "Boundary map — named boundaries with failure modes and authority assignments" |

**Property 3: Explicit Initiation Mode**

How does the human (or agent) begin this task?

| Mode | Meaning | Allocation Implication |
|---|---|---|
| Self-starting | Can begin from own knowledge without prompting | May be solo if capability gap ≥ 6 |
| Scaffolded | Needs structure, template, or prompt to begin | Always collaborative — agent provides scaffold, human fills in |
| Discovery | Discovers what they want by reacting to options | Always collaborative — agent proposes, human refines |

This is the dimension the original decomposition missed. "Intuitive" tasks are often "Discovery" initiation — the human has superior judgment but cannot begin without prompting. This is why "Human-only" allocation was wrong for five tasks.

**Property 4: Explicit Authority Boundary**

Who has final authority over this task's output?

| Authority | Meaning | When Used |
|---|---|---|
| Human-only | Human produces, agent does not contribute to content | Rare — only when agent preparation would corrupt the output |
| Human-final | Agent prepares, human decides | Common — discovery, scaffolded, and high-reversibility tasks |
| Agent-primary | Agent produces, human reviews | Common — analytical, procedural tasks with moderate reversibility |
| System-enforced | Automated with human override | Low-reversibility, high-consistency tasks |

**Property 5: Explicit Failure Mode**

What does "wrong" look like for this task if the wrong actor is assigned? This is the inverse of the authority boundary — the failure mode IS the reason for the boundary.

| Task | Failure Mode | If Wrong Actor |
|---|---|---|
| Elicit purpose | Generic purpose that misses real intent | Agent suggests purpose → template-filling, not genuine |
| Structure purpose | Purpose stays vague, never becomes specification | Human structures from blank → incomplete, low quality |
| Propose never-rules | Missing boundaries the human hasn't encountered | Human proposes from blank → misses patterns from experience |
| Validate never-rules | Generic boundaries that don't fit the domain | Agent validates → rubber-stamping, not genuine validation |

### The Conflation Test

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

### The Intuitive Task Decomposition Pattern

Tasks typed as "Intuitive" or "Evaluative" frequently decompose into two subtasks following the "agent prepares judgment, human makes judgment" principle:

1. **Propose** — the agent offers options, patterns, or structures (Agent-primary, Generative or Analytical)
2. **Validate** — the human exercises judgment on prepared material (Human-final, Evaluative)

This is not a coincidence — it's the core CAWDP principle applied at decomposition level. When a task is typed as "Intuitive" or "Evaluative" with initiation mode "Discovery" or "Scaffolded," the Decomposer should expect it to split into Propose + Validate.

The decomposition should not automatically split every Intuitive task. The split depends on initiation mode:

| Intuitive Task Initiation | Decomposition |
|---|---|
| Self-starting | May remain one task (human can do it alone) |
| Scaffolded | Split: Propose structure + Validate content |
| Discovery | Split: Propose options + Validate selection |

### Three-Participant Separation for Decompose-Type-Allocate

Task decomposition, cognitive typing, and capability allocation are genuinely different cognitive operations with different failure modes. They should be performed by different participants with different authority boundaries:

| Step | Role Class | Authority Boundary | Failure Mode |
|---|---|---|---|
| Decompose | Generator | Never be vague | Over-decomposition, under-decomposition, conflation |
| Type | Measurer | Never interpret | Misclassification, over-simplification |
| Allocate | Assessor | Never finalize | Overt classification, missing preparation need |

When one participant performs all three steps, each step's errors compound into the next. The decomposition shapes what the typing sees, which shapes what the allocation scores. A conflated task produces a misclassified type, which produces a bad allocation.

Separating the steps creates review points between each stage. The Measurer can flag conflated tasks. The Assessor can flag misclassified types. The human can flag allocations that don't match reality.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Every output from P1 has at least one task that produces it. Every input requirement from P2 has at least one task that consumes it. No orphan tasks. Every subtask passes the conflation test (6 properties). Every subtask has a single primary cognitive operation. Every subtask has a clear output artefact. Every subtask has an explicit initiation mode. Every subtask has an explicit failure mode. Intuitive tasks with Discovery/Scaffolded initiation are split into Propose + Validate. |
| Enrichment | Every task has a failure mode. Every failure mode is specific (not "it doesn't work"). Adjustment factors are assessed for every task initially rated "Human-only". Allocation rationale is documented for every task. Human-primary tasks specify how the agent prepares. |
| Cross-Cutting | CC-1: No task is both producer and verifier of the same output. Decompose, Type, and Allocate are performed by different participants. CC-2: Every "Human-only" allocation is reviewed for collaborative potential. CC-3: Confidence in decomposition depth. CC-4: Information boundaries between task groups identified. CC-9: Decomposition doesn't prematurely constrain possibilities. |

---

## Phase 4: Capability Allocation

**Cognitive Mode:** ALLOCATE  
**Diamond:** Structure  
**Stance:** Constructive

### What Happens

Assign each task to the right actor using complementarity analysis. The ternary model (Human/Agent/System) replaces binary human-vs-automation allocation.

### Ternary Complementarity Matrix

For each task, assess three actor types on a 0-10 scale:

| Dimension | Human | Agent | System |
|---|---|---|---|
| Analytical capability | Score | Score | Score |
| Generative capability | Score | Score | Score |
| Evaluative capability | Score | Score | Score |
| Speed | Score | Score | Score |
| Consistency | Score | Score | Score |
| Ethical judgment | Score | Score | Score |
| Domain expertise | Score | Score | Score |
| Values alignment | Score | Score | Score |
| Decision authority | Score | Score | Score |

### Allocation Algorithm

Priority order: System → Human → Agent → Collaborative

1. **System-first:** If a task is mechanical, deterministic, and reversible → System
2. **Human-required:** If the complementarity gap (highest agent score minus highest human score) is ≥ 6 on Ethical Judgment, Values Alignment, or Decision Authority → Human-only
3. **Agent-suitable:** If the task is analytical, generative, or evaluative with low stakes and low reversibility risk → Agent
4. **Collaborative:** Everything else → Human + Agent working together

### Two-Pass Allocation Process

**Pass 1: Capability Gap (Existing)**

Score each dimension 1-10 for Human, Agent, and System. Calculate gaps. Propose initial allocation based on the highest-scoring actor and gap magnitude.

This is the existing complementarity analysis. It correctly identifies *capability* — who is better at this dimension.

**Pass 2: Adjustment Factors (New)**

For each task, assess five factors that modify the gap-based allocation. Any factor that shifts toward collaboration overrides the gap-based allocation.

| Factor | Low | Medium | High | Allocation Shift |
|---|---|---|---|---|
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

### Reversibility Classification

| Level | Description | Example |
|---|---|---|
| Fully reversible | Can undo with no cost | Draft text revision |
| Moderately reversible | Can undo with some cost | Task status change |
| Hard to reverse | Undo requires significant effort | Contract execution |
| Irreversible | Cannot undo | Data deletion, payment |

### Human-Primary ≠ Human-Only

For all human-primary tasks: the agent PREPARES options → human REFINES, ACCEPTS, or REJECTS → agent CAPTURES decision with reasoning.

The adjustment factors determine *how* the agent prepares:

| Adjustment Factor Dominant | How Agent Prepares |
|---|---|
| Cold Start (Discovery) | Agent proposes options for human to react to |
| Cold Start (Scaffolded) | Agent provides structure/template for human to fill |
| Experience Dependency | Agent surfaces patterns and failure modes for human to validate |
| Preparation Value | Agent prepares analysis or draft for human to review |
| Reversibility (Low) | Agent prepares comprehensive options, human has final authority |

### The Allocation Rationale

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

### Human Cold Start Override

Identity/purpose/boundary tasks are collaborative by default, regardless of complementarity gap score. Humans can't always articulate what they want without guided preparation. The agent prepares options; the human decides.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Every task has an allocation. Every human-only task has gap ≥ 6 on at least one dimension. No agent-only tasks with gap ≥ 6 on ethical judgment. |
| Enrichment | Reversibility classified for every task. Hardest boundary moment (Q5) is human-only or collaborative. Adjustment factors assessed for every task initially rated "Human-only". Allocation rationale documented for every task. Human-primary tasks specify how the agent prepares. |
| Cross-Cutting | CC-9: Allocation respects possibility orientation (identity tasks are collaborative, not human-only). CC-2: Every "Human-only" allocation is reviewed for collaborative potential. CC-3: Allocation confidence stated. CC-4: Information boundaries respected in allocation. |

---

## Phase 5: Event Storming

**Cognitive Mode:** STRESS-TEST  
**Diamond:** Structure → Realisation (transition)  
**Stance:** Adversarial  
**Conditional:** Required for multi-participant workflows. Optional for single-participant workflows.

### What Happens

Identify domain events, failure events, and recovery paths. Stress-test the workflow architecture against failure scenarios.

### Domain Events

Events that occur in the normal flow of work: task started, task completed, output produced, quality gate passed, human decision made.

### Failure Events

Events that occur when something goes wrong: participant exceeds authority boundary, output fails verification, cost budget exhausted, human override triggered, specification aging alert.

### Recovery Paths

For every failure event, define:

- Detection mechanism (how the system detects the failure)
- Recovery action (what the system does)
- Human notification (what the human is told)
- State restoration (what state is restored)
- Prevention mechanism (what prevents recurrence)

### System-Enforced Triggers

Identify which events should trigger system-level enforcement (Regime 3) rather than participant-level compliance (Regime 1) or detection (Regime 2).

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Every failure mode from P3 has a corresponding failure event. Every failure event has a recovery path. |
| Enrichment | System-enforced triggers identified for critical failure events. Recovery paths tested against hardest boundary moment (Q5). |
| Cross-Cutting | CC-1: Detection mechanisms are independent from the participants that produce the outputs being detected. CC-4: Information boundaries respected in event definitions. CC-8: All events recorded in audit trail. |

---

## Phase 6: System Architecture

**Cognitive Mode:** ARCHITECT  
**Diamond:** Realisation  
**Stance:** Structural

### What Happens

Design the workflow architecture, orchestration pattern, composition model, fallback tiers, and template architecture.

### Workflow Architecture

Define the stages of the workflow, the flow between them, and the human gates.

### Composition Decision

| Pattern | When to Use | Characteristic |
|---|---|---|
| Single Agent | Single cognitive function, single class | Simplest, most maintainable |
| Team | Multiple cognitive functions, always-on collaboration | Persistent, shared context |
| Workflow | Sequential stages with human gates | Ordered, pause/resume |

A single-agent workflow is a valid outcome. The methodology doesn't require multiple agents. It requires the right composition for the workflow's purpose.

### Orchestration Design

Define how participants communicate, how context flows between stages, and how the workflow recovers from failures.

### Template Architecture (7 types)

| Template Type | Purpose | Example |
|---|---|---|
| Input | Standardised input format per task | Research brief template |
| Output | Standardised output format per task | Assessment report template |
| Handoff | Standardised inter-participant communication | Review package template |
| Verification | Standardised verification protocol | Spot-check template |
| Decision | Standardised decision record | Approval record template |
| Feedback | Standardised feedback format | Override feedback template |
| Escalation | Standardised escalation path | Authority escalation template |

### Failure Mode and Effects Analysis (FMEA)

For each failure mode:

- Severity (1-10)
- Occurrence likelihood (1-10)
- Detection difficulty (1-10)
- RPN = Severity × Occurrence × Detection
- Recovery path
- Prevention mechanism

### Fallback Model (3 tiers)

| Tier | When | What |
|---|---|---|
| Graceful degradation | Participant produces partial output | Deliver what's available, flag gaps |
| Alternative path | Participant fails completely | Route to backup participant or human |
| Human escalation | System cannot recover | Alert human with full context |

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Workflow covers all P3 tasks. Human gates match P4 human-only allocations. Orchestration respects P5 event definitions. |
| Enrichment | FMEA completed with RPN rankings. Hardest boundary moment (Q5) has dedicated failure mode and recovery path. |
| Cross-Cutting | CC-1: Orchestration separates producing and verifying participants. CC-4: Workflow stages respect information boundaries. CC-7: Per-stage cost estimates. CC-8: Audit trail architecture defined. |

---

## Phase 7: Participant Design

**Cognitive Mode:** DESIGN  
**Diamond:** Realisation  
**Stance:** Concrete

### What Happens

Design each participant in the workflow. Produce the human-readable specification using the 10-section template. A participant may be an agent, a human role, or a system component.

### Participant Specification Template (10 sections)

| Section | Purpose | Primary Question |
|---|---|---|
| **1. Identity** | What IS this participant? | Q1-Q5 identity answers |
| **2. Boundaries** | Where does authority stop? | What never happens? What's the enforcement regime? |
| **3. Task Map** | What work happens? | What inputs, outputs, and dependencies? |
| **4. Knowledge** | What does it need to know? | Sources, quality, aging, access? |
| **5. Capabilities** | What tools does it have? | Tools, access, limits? |
| **6. Behaviour** | How does it act? | Directives, decision presentation? |
| **7. Verification** | How do we know it's right? | Who checks what, how independently? |
| **8. Failure & Recovery** | What goes wrong? What then? | Failure modes, recovery paths? |
| **9. Lifecycle** | When does it run? What events? | Triggers, events, cost limits? |
| **10. Governance** | What contract contains it? | Enforceable boundaries, revert protocol? |

### Five-Class Taxonomy

| Class | Characteristic | Authority Boundary | Characteristic Failure | Null-State Output |
|---|---|---|---|---|
| **Extractor** | Gathers information | Never judges | Hallucination (invents facts) | "No results found" + search parameters |
| **Measurer** | Measures against criteria | Never interprets | Noise-as-signal (measures wrong thing) | "Insufficient data" + what's missing |
| **Assessor** | Evaluates against criteria | Never finalizes | Overconfidence (rates without evidence) | "Unable to assess" + reason |
| **Generator** | Produces new content | Never fabricates, never vague | Fabrication/vagueness | "Cannot generate" + alternatives |
| **Aggregator** | Assembles components | Never adds content | Omission (misses a component) | "Nothing to assemble" + what's missing |

Every null-state output carries epistemic metadata: confidence: 0, provenance: self-report, limitations: complete.

### Per-Dimension Progressive Autonomy (Default)

Every participant has at least one dimension where full autonomy is inappropriate. Single-dimension progression is the exception.

| Dimension | Trust Ceiling | Promotion Criteria | Override Threshold |
|---|---|---|---|
| [Named per participant] | Shadow/Advisory/Supervised/Autonomous | Measurable criteria per dimension | Override rate below X% for Y period |

Default dimensions by participant class:

| Participant Class | Minimum Dimensions | Examples |
|---|---|---|
| Extractor | 2 | Data access, Output format |
| Measurer | 3 | Measurement method, Threshold application, Reporting |
| Assessor | 3 | Evidence evaluation, Recommendation strength, Final judgment (NEVER autonomous) |
| Generator | 4 | Content creation, Safety assessment, Style, Domain expertise |
| Aggregator | 3 | Assembly, Addition detection, Cross-participant coordination |

### Two-Category Harm Assessment

| Category | Mechanism | Design Response |
|---|---|---|
| **Direct output harm** | Participant produces content that causes harm if accepted | SuggestionRisk schema, DO_NOT_SUGGEST mechanism, self-evaluation mode |
| **Indirect data harm** | Participant stores/retrieves wrong data causing wrong decisions | Data integrity enforcement, CC-4 at database layer, verification spot-checks |

Both categories are assessed for every participant. A participant can have neither, one, or both.

### Enforcement Regime per Boundary

Every authority boundary has a target enforcement regime:

| Regime | Mechanism | Example |
|---|---|---|
| **Regime 1: Declare** | Participant is told the rule | Prompt-level behavioural boundary |
| **Regime 2: Detect** | System flags violations after the fact | Output audit, pattern detection |
| **Regime 3: Prevent** | System enforces structurally | Database-level access control, schema validation |

Target regime and justification are required for every boundary. Regime 3 requires evidence of structural enforcement. Regime 2 is the default when Regime 3 is infeasible. Regime 1 is accepted only for boundaries that cannot be detected or prevented — documented in the Unenforceable Elements Register (P8).

### Decision Presentation Pattern

When presenting decisions to humans, the participant presents 2-4 structured options with explicit benefits and risks. The user can always provide a custom option. One decision per turn.

```
Option A: [Title]
  Benefit: [1-2 specific benefits]
  Risk: [1-2 specific risks]

Option B: [Title]
  Benefit: [1-2 specific benefits]
  Risk: [1-2 specific risks]

Option C: [Custom — your own choice]
```

### Epistemic Metadata Profile

Every participant output carries 6 fields of epistemic metadata (CC-3):

| Field | Description | Deterministic Participants (Extractor/Measurer/Aggregator) |
|---|---|---|
| Confidence | How sure the participant is | Binary: data exists or doesn't |
| Provenance | Where the information came from | Critical: who/when/what instruction |
| Assumptions | What the participant assumed | Mostly N/A for structured data |
| Limitations | What the participant can't do | Scope boundaries |
| Recency | When the information was last verified | assessedAt timestamp |
| Uncertainty | What the participant doesn't know | Mostly N/A for structured data |

Deterministic participants (Extractors, Measurers, Aggregators handling structured data) use a simplified profile: confidence is binary, provenance is critical, assumptions and uncertainty are mostly N/A.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | 10 sections completed. 5 identity questions answered. Per-dimension progressive autonomy specified. Harm assessment (both categories) completed. Enforcement regime specified for every boundary. |
| Enrichment | Hardest boundary moment (Q5) has enforcement regime specified. Null-state output defined for all states. Decision presentation pattern used for all human interactions. |
| Cross-Cutting | CC-1: No participant verifies its own output. CC-3: Epistemic metadata profile defined. CC-4: Information boundaries specified with enforcement regime. CC-5: Specification aging schedule defined. CC-7: Per-participant cost budget specified. CC-8: Assurance level assigned. CC-9: Participant orientation matches phase position. |

---

## Phase 8: Contract Formalization

**Cognitive Mode:** FORMALIZE  
**Diamond:** Realisation  
**Stance:** Pure constraint

### What Happens

Transform human-readable specification into machine-enforceable contract primitives. Complete the 10×10 mapping matrix. Document every design decision. Produce the Unenforceable Elements Register.

This phase is the most constraint-oriented in the entire process. It operates in pure enforcement space. No possibility. No "what ifs." Only "what must the system enforce."

### Ten Contract Primitives

| # | Primitive | Purpose | Example |
|---|---|---|---|
| 1 | **Contract** | Overall envelope — what this agreement covers | "Commercial lease review workflow, scope: risk identification only" |
| 2 | **Principal** | Who delegated authority | "Sarah Chen, Principal, Chen Legal" |
| 3 | **Schema** | Typed input/output — what data looks like | Pydantic model for LeaseRiskReport |
| 4 | **Guard** | Authority constraints — who can do what | onlyHumanAuthority(final_approval) |
| 5 | **Budget** | Cost limits with halt condition | max_tokens: 10000, halt_on_exhaustion: true |
| 6 | **Invocation** | Trigger conditions — when does this start | on_task_assigned, scheduled_daily |
| 7 | **Revert** | What happens on violation — output rejected, state restored | per_output, reject_and_flag |
| 8 | **Event** | What gets emitted/recorded — audit trail | task_started, risk_identified, boundary_flagged |
| 9 | **Identity** | Workflow essence and stance — what it IS, what violates it | stance: possibility, violation: decides_for_human |
| 10 | **Knowledge** | What the participant needs to know, quality required, aging | min_accuracy: 3, max_age_days: 30, halt_on_stale: true |

### Ten Specification Sections

| # | Section | Purpose |
|---|---|---|
| 1 | Identity | What IS this participant? |
| 2 | Boundaries | Where does authority stop? |
| 3 | Task Map | What work happens? |
| 4 | Knowledge | What does it need to know? |
| 5 | Capabilities | What tools does it have? |
| 6 | Behaviour | How does it act? |
| 7 | Verification | How do we know it's right? |
| 8 | Failure & Recovery | What goes wrong? What then? |
| 9 | Lifecycle | When does it run? What events? What cost limits? |
| 10 | Governance | What contract contains it? What enforcement regime? What revert protocol? |

### 10×10 Mapping Matrix

|  | Contract | Principal | Schema | Guard | Budget | Invocation | Revert | Event | Identity | Knowledge |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Identity** | ● | ● | ○ | ● | ○ | ○ | ● | ○ | ● | ○ |
| **2. Boundaries** | ● | ○ | ○ | ● | ○ | ○ | ● | ● | ○ | ○ |
| **3. Task Map** | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ● |
| **4. Knowledge** | ○ | ○ | ● | ● | ○ | ○ | ○ | ○ | ○ | ● |
| **5. Capabilities** | ○ | ○ | ● | ● | ● | ● | ○ | ○ | ○ | ○ |
| **6. Behaviour** | ○ | ○ | ○ | ● | ○ | ○ | ● | ● | ● | ○ |
| **7. Verification** | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ○ |
| **8. Failure & Recovery** | ● | ○ | ○ | ○ | ○ | ● | ● | ● | ○ | ○ |
| **9. Lifecycle** | ● | ○ | ○ | ○ | ● | ● | ○ | ● | ○ | ○ |
| **10. Governance** | ● | ● | ○ | ● | ○ | ○ | ● | ● | ● | ○ |

● = direct mapping exists  
○ = weak or no mapping (requires explicit decision)

### Transformation Protocol

For each ● cell, document:

- The specific transformation (how section content becomes primitive content)
- Design decisions made during transformation
- Rationale for each decision
- Bidirectional traceability (section ↔ primitive)

For each ○ cell, document:

- Decision: "not needed," "deferred," or "requires design work"
- Rationale for the decision

### Unenforceable Elements Register

Document every specification element that:

- Has no contract representation
- Can only be enforced at Regime 1 (declare — trust the participant)
- Can only be enforced at Regime 2 (detect — flag after the fact)
- Requires redesign to make Regime 3 enforceable

This register is **honest infrastructure**. It says: "Here's what we can enforce structurally. Here's what we can only detect. Here's what we can only declare and trust."

| Element | Section | Target Regime | Achieved Regime | Rationale | Redesign Path |
|---|---|---|---|---|---|
| "Reflect possibility, don't qualify" | Identity | Regime 3 | Regime 1 | Stance is behavioural, not structural | Add output validation for qualifying language patterns |
| "Never fabricate evidence" | Behaviour | Regime 3 | Regime 2 | Can detect after generation, can't prevent | Add source citation requirement in Schema |
| "Maintain genuine curiosity" | Identity | Regime 2 | Regime 1 | Emotional quality, not enforceable | None — accept Regime 1 |

### Contract Depth Scaling

Not every participant needs a 10-primitive contract. Depth scales with participant class and autonomy level.

| Participant Class | Autonomy | Primitives | Additional |
|---|---|---|---|
| Extractor | Shadow | Schema, Event (2/10) | — |
| Measurer | Supervised | Schema, Event, Guard (3/10) | — |
| Assessor | Supervised | Schema, Event, Guard, Principal (4/10) | — |
| Generator | Autonomous | All 10 | Full enforcement regime map |
| Aggregator | Autonomous | All 10 | Cross-participant contract integration |

### Symmetric Enforcement

The same 10 primitives govern tasks for ALL actor types (Human/Agent/System). One contract per task. The contract is binary, deterministic, actor-agnostic.

| Primitive | Human Behavior | Agent Behavior | System Behavior |
|---|---|---|---|
| Schema | Same validation | Same validation | Same validation |
| Guard | Same constraint | Same constraint | Same constraint |
| Budget | Same halt condition (with pause/resume for slower execution) | Same halt condition | Same halt condition |
| Revert | Same rejection | Same rejection | Same rejection |

The system provides pre-submission support (templates, previews, incremental validation) and post-revert capture (reverted output saved as separate artefact). These are outside the contract, not modifications to it.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Every ● cell in the 10×10 matrix has a completed transformation. Every ○ cell has an explicit decision. All 10 primitives present for participants at appropriate depth. Bidirectional traceability complete. |
| Enrichment | Enforcement regime justified for every Guard. Hardest boundary moment (Q5) has Regime 3 enforcement where possible. Unenforceable elements documented with redesign paths. Contract depth matches participant class and autonomy level. |
| Cross-Cutting | CC-1: Contract verifier ≠ specification author. CC-3: Epistemic metadata on contract completeness. CC-4: Information boundaries enforced at contract level. CC-5: Contract aging schedule defined. CC-7: Contract derivation cost within budget. CC-8: Assurance level assigned to audit trail. CC-9: All contract content is constraint-oriented (no possibility language). |

---

## Phase 9: Human Experience Design

**Cognitive Mode:** EMPATHIZE  
**Diamond:** Realisation  
**Stance:** Partially reopens possibility

### What Happens

Design how the human experiences the workflow. Cognitive load budget, override mechanisms, stakeholder surfaces, and System Empowerment Assessment.

### Cognitive Load Budget

Decision capacity is finite. The budget is adaptive:

```
decisions_per_session = base_capacity
  × domain_weight
  × user_experience_modifier
  × session_sequence_modifier
  × decision_complexity_modifier
```

| Factor | Range | How Set |
|---|---|---|
| Base capacity | 3-8 | Research baseline by user familiarity |
| Domain weight | 0.7-1.3 | P0 stakes classification |
| User experience | 0.8-1.3 | Progressive disclosure level |
| Session sequence | 0.7-1.2 | Position in Boundary Journey |
| Decision complexity | 0.6-1.4 | Average complexity this session |

### Override Mechanisms

Every human decision point has an override mechanism. The override is always available, never penalized, and always recorded.

| Override Type | When | What Happens |
|---|---|---|
| Accept | Participant's recommendation is correct | Proceed with participant output |
| Modify | Participant's recommendation is partially correct | Human edits, participant records changes |
| Reject | Participant's recommendation is wrong | Human provides alternative, participant records reasoning |
| Escalate | Human lacks confidence to decide | Escalate to authority with full context |
| Pause | Human needs more information | Pause workflow, gather context, resume |

### Stakeholder Surfaces

Six surfaces of the same PRISM artefact graph:

| Surface | Audience | Needs | Depth |
|---|---|---|---|
| Decision Maker | Business owner | Boundary clarity, trust data, cost-benefit | Summary |
| Design Participant | Workflow designer | Guided design experience, progressive disclosure | Full specification |
| Implementation Participant | Developer | Workflow configurations, schemas, deployment artefacts | Code-level |
| Operation Participant | Operator | Operations manual, verification protocols, status | Operational |
| Governance Participant | Auditor/insurer | Audit trails, compliance mappings, override analysis | Evidence-level |
| Extension Participant | Methodology contributor | Full methodology, pattern contribution guidelines, schema extension points | Complete |

Each surface is a derived view from the PRISM artefact graph. One graph, many views.

### System Empowerment Assessment

Measure whether the system expands or constrains human creative freedom:

| Level | Description |
|---|---|
| **Liberating** | System enables outcomes impossible without it |
| **Amplifying** | System expands human capability significantly |
| **Enabling** | System makes existing work easier |
| **Informing** | System provides information, human does everything |
| **Constraining** | System limits human options or judgment |

Target: Amplifying or Liberating for all human participants.

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Cognitive load budget calculated per user type. Override mechanisms specified for every human gate. Stakeholder surfaces defined. |
| Enrichment | System Empowerment Assessment ≥ Enabling for all participants. Decision fatigue detection mechanism specified. Hardest boundary moment (Q5) has accessible override. |
| Cross-Cutting | CC-2: System Empowerment Index calculated per participant. CC-6: Enrichment level assessed. CC-9: Human experience design partially reopens possibility (empathy is expansive). |

---

## Phase 10: Validation & Iteration

**Cognitive Mode:** VERIFY → EVOLVE  
**Diamond:** Realisation → Discovery (spiral)  
**Stance:** Spirals back

### What Happens

Define testable hypotheses. Build the prototype. Deploy with progressive autonomy. Monitor health. Iterate based on learnings. EVOLVE back to P0.

### Testable Hypotheses

Every design decision generates a hypothesis. Minimum 3 hypotheses per workflow.

Format:

- H[n]: [Specific claim about what the design produces]
- Measurement: [How to test the claim]
- Success criteria: [What "pass" looks like]
- Failure criteria: [What "fail" looks like]
- Action on fail: [What to change]

### Prototype Priority Matrix

| Axis | Priority | Reason |
|---|---|---|
| Highest-risk hypothesis | Test first | Addresses largest uncertainty |
| Milestone 1 deliverable | Test early | Boundary Map validates core value |
| Cheapest to test | Test early | Fast learning |
| Most learnable | Test early | Informs most downstream decisions |

### Progressive Autonomy Deployment

| Level | What It Means | Promotion Criteria |
|---|---|---|
| **Shadow** | Participants run alongside, human does everything, system tracks what participants would have done | Accuracy rate > 80% over 2 weeks |
| **Advisory** | Participants suggest, human reviews every suggestion | Override rate < 40% over 2 weeks |
| **Supervised** | Participants act, human approves before anything leaves | Override rate < 20% over 4 weeks |
| **Autonomous** | Participants act within boundaries, human monitors the Trust Ledger | Override rate < 10% over 8 weeks |

Per-dimension promotion: each dimension promotes independently based on its own criteria.

### Health Monitoring

**Integrity Diagnostic Score (IDS):** 5 metrics measuring workflow integrity

| Metric | What It Measures | Threshold |
|---|---|---|
| Schema compliance | % outputs matching schema | > 95% |
| Boundary compliance | % actions within authority boundaries | > 98% |
| Cost variance | Actual vs budgeted cost | < 20% |
| Specification freshness | % specifications within aging cadence | > 80% |
| Verification pass rate | % outputs passing verification | > 90% |

**Utilisation Performance Ratio (UPR):** 3 metrics measuring workflow value

| Metric | What It Measures | Threshold |
|---|---|---|
| Time saved | Actual vs fully manual time | > 30% |
| Override rate | % human overrides of participant output | < 30% |
| Output quality | % outputs accepted without modification | > 70% |

### EVOLVE Cycle

P10 cycles back to P0. The journey is a spiral.

| Signal | What It Means | EVOLVE Target |
|---|---|---|
| Guard violation rate > 30% | Enforcement isn't working | P8 — is the enforcement regime right? |
| Unenforceable elements accumulating | Specification has too many meaning-only elements | P7 — can the specification be redesigned for enforcement? |
| Contract derivation cost exceeding budget | 10×10 transformation is too expensive | P6 — can the workflow simplify? |
| Revert rate > 20% | Output is being rejected too often | P8 — is the revert granularity right? |
| Human override rate > 40% | Humans don't trust the enforcement | P9 — does the human understand what's enforced? |
| Capability drift detected | Participant capabilities have changed | P7 — does the specification still match reality? |
| Specification aging alert | Specification is stale | P7 — update specification |
| New failure mode discovered | Something went wrong that wasn't predicted | P5 → P7 → P8 — add failure event, update spec, update contract |

### Quality Gate

| Layer | Check |
|---|---|
| Fidelity | Minimum 3 testable hypotheses defined. Prototype priority matrix completed. Progressive autonomy deployment plan specified. Health monitoring metrics defined. |
| Enrichment | Hardest boundary moment (Q5) is the first test case. EVOLVE triggers defined. Decision fatigue detection integrated into monitoring. |
| Cross-Cutting | CC-1: Validation participants are independent from design participants. CC-5: Specification aging schedule operational. CC-6: System Empowerment Index measured in validation. CC-7: Validation cost within budget. CC-8: Validation audit trail assured. CC-9: EVOLVE cycle closes the possibility-constraint spiral. |

---

## Cross-Cutting Concerns

### CC-1: Verification Independence

The participant that produces an output is never the same participant that verifies it. Three levels of independence:

| Level | Description | Example |
|---|---|---|
| **Structural** | Schema validation, type checking | Output conforms to Pydantic model |
| **Semantic** | Content accuracy, meaning verification | Separate participant reviews factual claims |
| **Authority** | Boundary compliance, judgment verification | Human verifier for high-stakes decisions |

### CC-2: Human Enrichment Assessment

Measure whether the system expands or constrains human creative freedom. System Empowerment Index (5 levels): Constraining → Informing → Enabling → Amplifying → Liberating. Target: Amplifying or Liberating for all participants.

The assessment must explicitly check for "Human-primary ≠ Human-only" at the decomposition level:

- For every task rated "Human-only" by gap score, assess the five adjustment factors
- If two or more factors shift toward collaboration, override to "Collaborative, human-final"
- If initiation mode is Discovery or Scaffolded, always override to "Collaborative"
- Document the preparation method: how does the agent prepare for the human's judgment?
- Verify that the preparation method matches the adjustment factor (Discovery → propose options; Scaffolded → provide structure; Experience → surface patterns)

### CC-3: Epistemic Metadata Contracts

Every participant output carries 6 fields:

| Field | Description | Deterministic Profile |
|---|---|---|
| Confidence | How sure the participant is | Binary: data exists or doesn't |
| Provenance | Where the information came from | Critical: who/when/what instruction |
| Assumptions | What the participant assumed | Mostly N/A for structured data |
| Limitations | What the participant can't do | Scope boundaries |
| Recency | When the information was last verified | assessedAt timestamp |
| Uncertainty | What the participant doesn't know | Mostly N/A for structured data |

### CC-4: Information Boundaries

Participants access only the information their authority boundary permits. Enforcement at three levels:

| Level | Mechanism | Example |
|---|---|---|
| Regime 1 | Prompt-level declaration | Participant told "don't access X" |
| Regime 2 | Post-hoc detection | Output audit flags unauthorized access |
| Regime 3 | Structural enforcement | Private database schema, tool-level access control |

Target: Regime 3 for all data-managing participants. Database-level access control (private schemas, authorized participant tables) is the standard pattern.

### CC-5: Specification Aging

Every specification has a review cadence and trigger-based re-review:

| Trigger | Action |
|---|---|
| Scheduled cadence reached | Review specification for relevance |
| Capability drift detected | Review participant capabilities vs specification |
| Override rate exceeds threshold | Review authority boundaries |
| New failure mode discovered | Review failure model |
| Regulatory change | Review compliance mapping |

### CC-6: System Empowerment Index

5-level scale: Constraining → Informing → Enabling → Amplifying → Liberating. Measured per participant at P9 and P10. Target: Amplifying or Liberating.

### CC-7: Cost Budget

Per-participant and per-workflow cost tracking:

| Level | What | Halt Condition |
|---|---|---|
| Per-task | Token cost of each task | max_tokens per task |
| Per-session | Token cost of user session | max_tokens per session |
| Per-workflow | Token cost of full workflow run | max_tokens per workflow |
| Monthly | Aggregate cost | Monthly budget with alert at 80% |

Halt on exhaustion is the contract behavior. Warning at soft thresholds is the UX behavior. Budget is a contract primitive (Budget), enforced structurally.

### CC-8: Assured Audit Trail

Three assurance levels:

| Level | What | Mechanism |
|---|---|---|
| **Logged** | Event recorded | Standard database insert |
| **Assured** | Event recorded with integrity verification | Hash chain or signed record |
| **Verified** | Event recorded, verified by independent party | Third-party attestation |

Assignment by risk level: Routine operations → Logged. Boundary events → Assured. Compliance-critical events → Verified.

### CC-9: Possibility Orientation

A workflow's stance toward possibility must match its position in the CAWDP phase sequence. Enforced by:

1. Phase-specific legitimate questions (P0: "what could be?", P8: "what must be enforced?")
2. Phase-specific failure modes (P0: qualifying possibility, P8: reopening possibility)
3. Feasibility contamination check (P0-P2: no mechanism keywords)
4. Pattern-first entry (pattern selection determines starting position)

---

## Design Patterns

### Pattern 1: Surface + Engine

One user-facing participant (Surface) routes to multiple specialist participants (Engine). Surface reflects and routes, never decides. CC-1 enforced structurally: producing specialist ≠ verifying specialist.

**When:** Multi-specialist workflows where the user should interact with one conversation.

**Anti-pattern:** Surface participant makes decisions about what the engine should produce.

### Pattern 2: Milestone-as-Exit

Every phase boundary produces a standalone valuable artefact. Users can exit at any milestone with something they can use.

**When:** Any workflow where the user may not complete all phases.

**Anti-pattern:** Milestones that require the next milestone to be useful (dead ends).

### Pattern 3: Possibility Gradient

The workflow starts expansive and tightens toward constraint. Each phase narrows the space of legitimate questions.

**When:** Every CAWDP application.

**Anti-pattern:** Feasibility questions in P0, possibility questions in P8.

### Pattern 4: Contract Depth Scaling

Contract formalization depth scales with participant class and autonomy level. Simple participants get shallow contracts. Complex participants get deep contracts.

**When:** P8 Contract Formalization.

**Anti-pattern:** Full 10-primitive contract for an Extractor in Shadow mode.

### Pattern 5: Identity-to-Enforcement Cascade

Identity questions produce authority boundaries, which produce enforcement regimes, which produce contract primitives. The cascade is directional and traceable.

**When:** P7 → P8 transition.

**Anti-pattern:** Guard primitives without identity traceability. If a Guard can't answer "which identity violation does this prevent?", it's not derived from the specification.

---

## Information Quality Framework

Ten dimensions of information quality, each spectral (1-5 scale):

| # | Plain English | Academic | Who Assesses | When |
|---|---|---|---|---|
| 1 | Is it the right information? | Relevance | System (computed) | Runtime |
| 2 | Is it correct? | Accuracy | Domain expert | Before use |
| 3 | Is it all there? | Completeness | Domain expert | Before use |
| 4 | Is it current? | Recency | System (computed) | Runtime |
| 5 | Where did it come from? | Provenance | System (stored) | Capture time |
| 6 | How sure is the agent? | Confidence | Agent (stored) | Production time |
| 7 | Is it specific enough? | Specificity | Domain expert | Before use |
| 8 | Is it structured? | Structure | System (computed) | Runtime |
| 9 | Is it enough? | Sufficiency | Domain expert | Before use |
| 10 | Does it agree with itself? | Consistency | System (computed) | Runtime |

**Traffic light model:** Red (1-2) = don't run. Amber (3) = run with flags. Green (4-5) = proceed.

**Hard stops:** Accuracy Red → don't run the participant. Sufficiency Red → don't run the participant.

**Key distinction:** Completeness (is every area covered?) ≠ Sufficiency (is there enough to make a judgment?). A complete knowledge base can still be insufficient.

---

## Plain English Requirement

All CAWDP concepts must be expressible in plain English accessible to a 16-year-old. Academic terms in brackets after the plain English primary.

| Plain English | Academic |
|---|---|
| Where should AI stop? | Complementarity boundary |
| Who does what? | Ternary allocation |
| How do we check? | Verification independence |
| How sure is the agent? | Confidence (CC-3) |
| Where did it come from? | Provenance (CC-3) |
| When does it go stale? | Specification aging (CC-5) |
| What happens when it's wrong? | Revert protocol |
| What must the system enforce? | Contract primitive |
| Can the system stop it? | Regime 3 enforcement |
| What can't we enforce? | Unenforceable element |

---

## Pattern-First Entry

Users selecting a pattern don't see 11 phases. They see:

1. Pattern selection (5 patterns, pre-fill 40-70%)
2. Four identity questions (Q1-Q5)
3. Boundary mapping
4. Finished specification

The contract formalization, enforcement regimes, quality gates, and cross-cutting concerns happen in the back office. The methodology is invisible to the user, embedded in the structure.

### Five Core Patterns

| Pattern | Class | Orientation | Pre-fill | Best For |
|---|---|---|---|---|
| **Signal Detector** | Extractor | Constraint | 60% | Monitoring, alerting, scanning |
| **Multi-Lens Analyst** | Measurer+Assessor | Bridge | 50% | Multi-dimensional analysis, reporting |
| **Discovery Explorer** | Generator+Assessor | Possibility | 40% | Research, insight mining, competitive intelligence |
| **Learning Scaffold** | Assessor+Generator | Possibility | 45% | Education, tutoring, skill development |
| **Review Partner** | Assessor | Constraint | 70% | Quality review, compliance, risk assessment |

Pattern pre-fills include identity questions, boundary defaults, progressive autonomy dimensions, contract primitive defaults, and enforcement regime recommendations.

### Progressive Disclosure Levels

| Level | Who | What They See |
|---|---|---|
| **Quick Start** | New user | Pattern + Identity Questions → 15-minute specification |
| **Practitioner** | Trained user | Override defaults, customize boundaries |
| **Architect** | Expert | Design from first principles, create new patterns |
| **Contributor** | Methodology expert | Extend the methodology itself |

---

## Tooling Support

### Priority 1: Pattern Library (2-3 weeks)

Core 5 patterns with pre-fill templates. Pattern matching engine. Validation pipeline after 20+ specifications.

### Priority 2: Cognitive Load Calculator (1-2 weeks)

Adaptive decision budgets per user, domain, and session. Integrates with Mirror Participant for pacing.

### Priority 3: Decision Fatigue Detector (1-2 weeks)

Real-time monitoring of decision velocity, rubber-stamping, consistency drift. Directly addresses FM1 (highest risk).

### Priority 4: Feasibility Contamination Checker (1 week)

Scans P0-P2 specification text for mechanism keywords. Flags for separation into mechanism notes.

### Priority 5: Quality Gate Engine — P7-P8 (2-3 weeks)

Executable quality gate checks for Participant Design and Contract Formalization. Queries PRISM artefact graph.

### Priority 6: Backcasting Engine (3-4 weeks)

Automates dependency tracing from P1 outputs. Gap detection (missing inputs, circular dependencies, orphan outputs).

### Priority 7: Pattern Library Validation (4-6 weeks)

Community flywheel: real specifications validate and refine patterns. Override rates, completion times, satisfaction scores.

### Priority 8: Quality Gate Engine — Full P0-P10 (4-6 weeks)

Complete coverage for all 11 phases. All gate checks executable.

---

## The Boundary Way

This is the opinionated, recommended approach to workflow design. If you follow The Boundary Way, the framework makes most decisions for you. If you deviate, you can still use individual components.

**Convention over configuration at 10 levels:**

| Level | Convention | Override |
|---|---|---|
| Identity | Pattern + Identity Questions | Design from first principles |
| Boundaries | Class-based defaults | Custom boundaries |
| Authority | Inverse of failure mode | Explicit specification |
| Enforcement | Regime 3 where possible, Regime 2 default | Per-boundary justification |
| Autonomy | Per-dimension, class-based ceilings | Custom dimensions |
| Cost | Class-based budget benchmarks | Custom budget |
| Verification | CC-1: separate verifier | Custom verification protocol |
| Metadata | Class-based epistemic profile | Custom metadata fields |
| Aging | Class-based cadences | Custom cadences |
| Contracts | Depth scaled by class and autonomy | Custom contract depth |

---

## Summary Table

| Element | Count | Key Concept |
|---|---|---|
| Phases | 11 | P0 IMAGINE → P10 EVOLVE |
| Cross-cutting concerns | 9 | CC-1 through CC-9 |
| Quality gates | 5 | Three-layer: Fidelity/Enrichment/Cross-Cutting |
| Participant classes | 5 | Extractor/Measurer/Assessor/Generator/Aggregator |
| Orientations | 3 | Possibility/Bridge/Constraint |
| Role archetypes | 15 | 5×3 class×orientation |
| Identity questions | 5 | Q1-Q5, everything derives from identity |
| Specification sections | 10 | Identity through Governance |
| Contract primitives | 10 | Contract through Knowledge |
| Mapping matrix | 10×10 | Specification ↔ Contract bidirectional |
| Design patterns | 5 | Surface+Engine, Milestone-as-Exit, Possibility Gradient, Contract Depth, Identity Cascade |
| Core patterns | 5 | Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner |
| Information quality dimensions | 10 | Relevance through Consistency |
| Enforcement regimes | 3 | Declare/Detect/Prevent |
| Progressive autonomy levels | 4 | Shadow/Advisory/Supervised/Autonomous |
| Harm categories | 2 | Direct output / Indirect data |
| Null-state outputs | 5 | Class-specific with epistemic metadata |
| Progressive disclosure levels | 4 | Quick Start/Practitioner/Architect/Contributor |
| Cognitive operation types | 6 | Mechanical/Analytical/Generative/Elicitive/Evaluative/Intuitive |
| Initiation modes | 3 | Self-starting/Scaffolded/Discovery |
| Experience dependency levels | 3 | Expert-dependent/Pattern-augmented/Procedural |
| Allocation adjustment factors | 5 | Cold Start/Experience/Discovery/Prep Value/Reversibility |
