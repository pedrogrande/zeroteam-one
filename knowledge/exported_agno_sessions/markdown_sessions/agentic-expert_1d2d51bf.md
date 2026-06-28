# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `1d2d51bf...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-21T06:45:56 |
| **Runs** | 6 completed / 6 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-21T06:45:56* · `glm-5.1:cloud` · `dd75b0a0...`

### Prompt

What is involved in Phase 6 of CAWDP (v2.2)?

### Response

# CAWDP v2.2 — Phase 6: System Architecture (ARCHITECT)

Phase 6 determines **how** the work flows — the pipeline, orchestration, composition, failure handling, and template architecture that turn decomposed tasks and complementarity allocations into an operational system.

---

## Phase Position in the Sequence

```
P0 IMAGINE → P1 SPECIFY → P2 TRACE → P3 DECOMPOSE → P4 ALLOCATE → P5 STRESS-TEST → P6 ARCHITECT
```

P6 is the first phase of the **Realisation arc** (ARCHITECT → DESIGN → FORMALIZE → EMPATHIZE → VERIFY). It receives the task decomposition (P3), complementarity allocations (P4), and event storming outputs (P5) and translates them into concrete system structure.

---

## Key Outputs

### 1. Pipeline Architecture
The stage-by-stage flow of how tasks execute in sequence or parallel:
- **Stage ordering** — which tasks run in sequence, which in parallel, which are conditional
- **Human gates** — where human decisions are required before proceeding (matching human-only tasks from P4)
- **Data flow** — what outputs from each stage feed into which subsequent stages
- **Backcasting validation** — every stage must trace back to the P1 output specifications it produces, and every P1 output must be reachable by forward-tracing from some stage

### 2. Orchestration Design
How agents, humans, and system components coordinate:
- **Composition decision** — Agent (single), Team (collaborative), or Workflow (sequential with gates)
- **Routing logic** — how tasks are assigned to agents based on class/orientation and authority boundaries from P7
- **Event-driven triggers** — from P5 event storming, which events trigger which stages
- **Progressive autonomy deployment** — Shadow → Advisory → Supervised → Autonomous transition criteria per agent

### 3. FMEA (Failure Mode and Effects Analysis)
For each pipeline stage and agent:
- **Failure mode** — what goes wrong
- **Severity** (1-10) — how bad
- **Occurrence** (1-10) — how likely
- **Detection** (1-10) — how hard to spot
- **RPN** (Risk Priority Number = S × O × D) — prioritisation metric
- **Recovery path** — what happens when failure occurs
- **System enforcement** — Regime 1 (Declare), Regime 2 (Detect), or Regime 3 (Prevent)

### 4. Template Architecture (7 types)
Typed, structured templates that resolve type collision at the handoff layer:
1. **Input Templates** — what data the stage/agent receives
2. **Output Templates** — what data the stage/agent produces
3. **Handoff Templates** — how data passes between stages/agents
4. **Verification Templates** — how outputs are verified (CC-1 levels)
5. **Decision Templates** — how human decisions are captured with reasoning
6. **Feedback Templates** — how results feed back to earlier stages
7. **Escalation Templates** — how failures are escalated to human authority

### 5. Composition Decision
Whether to use a single Agent, a Team, or a Workflow:
- **Agent** — single agent handling all tasks (simple, low-stakes)
- **Team** — multiple agents collaborating on shared tasks (moderate complexity)
- **Workflow** — sequential stages with human gates and conditional routing (complex, high-stakes)

The composition decision is driven by **stakes and authority boundary conflicts**, not task count. High stakes or conflicting authority boundaries require Workflow composition for explicit human gates.

### 6. Fallback Model (3-tier)
What happens when things go wrong:
- **Tier 1: Agent-level recovery** — agent retries with modified approach
- **Tier 2: Pipeline-level recovery** — stage replays with different parameters or escalation to human
- **Tier 3: System-level halt** — pipeline pauses, human intervention required, no silent failure

### 7. System Enforcement Points
Where CAWDP cross-cutting concerns are structurally enforced:
- **CC-1 Verification Independence** — producing agent ≠ verifying agent (enforced at pipeline level)
- **CC-4 Information Boundaries** — data access restricted by agent class and authority (enforced at database level, e.g., private schemas)
- **CC-7 Cost Budget** — per-agent and per-pipeline token/cost tracking with halt conditions
- **CC-8 Assured Audit Trail** — 3-level logging (logged/assured/verified) at every pipeline transition

---

## Quality Gate

Phase 6 quality gate has three layers:

| Layer | Focus | Key Checks |
|-------|-------|------------|
| **Fidelity** | Does it work? | Every P1 output reachable by forward-trace? Every stage traces to P1 output? Human gates match human-only tasks? |
| **Enrichment** | Does it work well? | Failure modes addressed for every agent? FMEA highest RPNs have mitigation? Fallback model covers all failure scenarios? |
| **Cross-Cutting** | Does it work right? | CC-1 verification independence enforced? CC-4 information boundaries defined per agent? CC-7 cost budgets specified? CC-8 audit trail levels assigned? |

---

## Key Design Decisions Made in P6

| Decision | Driven By | Example |
|----------|-----------|---------|
| Single Agent vs Team vs Workflow | Stakes and authority boundary conflicts | Assignment marking (high stakes, 4 stages) = Workflow |
| Stage ordering | Task dependencies from P3 + backcasting from P2 | Extraction before assessment, assessment before generation |
| Human gate placement | Human-only and human-final tasks from P4 | Complementarity gap ≥ 6 = human gate |
| Verification separation | CC-1 — producing agent ≠ verifying agent | Boundary Analyst ≠ Mirror in Agent Design Workflow |
| Template types needed | Type collision resolution at handoffs | Typed Pydantic schemas for all inter-agent data |
| Fallback tiers | FMEA severity and reversibility | Low reversibility = Tier 3 halt, not Tier 1 retry |
| Progressive autonomy starting level | Stakes and trust level | New deployment starts at Shadow, not Autonomous |

---

## Connection to Other Phases

- **Receives from P3/P4**: Task decomposition, complementarity allocations, adjustment factors — these define what the pipeline must accomplish
- **Receives from P5**: Domain events, failure events, recovery paths — these define what the pipeline must handle
- **Feeds into P7**: Agent design — P6 determines what agents are needed, their composition, and their interactions
- **Feeds into P8**: Contract formalization — P6 pipeline structure determines which contract primitives apply where
- **Feeds into P9**: Human experience — P6 pipeline stages determine cognitive load per stage, override points, and interface needs

---

## Templates as Type Collision Resolution

The 7 template types are P6's structural mechanism for resolving type collision at the handoff layer. Without templates, inter-agent data is unstructured prose — the same type collision problem that exists in LLM outputs. Templates enforce:

- **Typed inputs** — every agent receives structured data with epistemic metadata
- **Typed outputs** — every agent produces structured data with confidence, provenance, assumptions
- **Typed handoffs** — data between stages is explicitly typed, not free-form
- **Typed verification** — verification criteria are explicit, not implied
- **Typed decisions** — human decisions are captured with reasoning, not just outcomes

This is the same principle (typed, structured, mapped) applied at the pipeline architecture layer.

---

## From the Meta-Application

The Agent Design Workflow's P6 produced:
- **7-stage pipeline** with 7 human gates
- **Workflow composition** (not Team or single Agent) — sequential stages with human gates requiring pause/resume
- **6 specialist agents** with CC-1 verification independence enforced structurally
- **22 FMEA failure modes** (highest: FM1 identity template-filling at RPN 224)
- **7 template types** (input, output, handoff, verification, decision, feedback, escalation)
- **5 Regime 3 enforcement points** (database-level information boundaries, structured output schemas, cost budget halt conditions, progressive autonomy state machine, audit trail at every transition)
- **3-tier fallback model** (agent retry → stage replay with escalation → system halt with human intervention)

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-21T06:54:08* · `glm-5.1:cloud` · `abf6f527...`

### Prompt

There are a lot of different cognitive modalities used in this phase and I suspect tools will help our workflow agents perform to a higher standard.

Don't jump to solutions. Give me an overview of this phase, the work involved, the inputs and outputs, what does success look like at each stage?

### Response

# Phase 6: System Architecture — Work, Cognitive Modes, and Success Criteria

## The Core Question

P6 answers one question: **How does the designed work actually flow through a system?**

Everything before P6 is about *what* needs doing and *who* should do it. P6 turns that into *how it runs*.

---

## Inputs P6 Receives

| From Phase | What P6 Gets | What It Tells P6 |
|------------|---------------|-------------------|
| P1 Output Specification | 29 typed outputs with dependencies | The destination — what the pipeline must produce |
| P2 Backcasting | Input requirements, dependency chains | The path — what must exist before each output |
| P3 Task Decomposition | 52 tasks (or however many), each with cognitive type, initiation mode, authority boundary, failure mode | The work units — what needs doing and what kind of thinking each requires |
| P4 Capability Allocation | H/A/S assignments, adjustment factors, override rationale | The actor assignments — who does what and why |
| P5 Event Storming | Domain events, failure events, recovery paths, system triggers | The trigger and failure landscape — what starts things and what goes wrong |

P6 synthesises all of these into one coherent operational structure. That synthesis requires multiple distinct cognitive modes.

---

## The Work, Step by Step

### Step 1: Pipeline Architecture

**What:** Arrange tasks into an ordered flow of stages — some sequential, some parallel, some conditional — with human gates placed where P4 allocated human-only or human-final authority.

**Cognitive mode:** ARCHITECTURAL — spatial, structural, connectivity thinking. Laying out a building floor plan. "This connects to that, which depends on this, which feeds into that."

**What you're actually doing:**
- Taking the P3 task list and grouping related tasks into stages
- Ordering stages based on P2 dependency chains (you can't assess what hasn't been extracted)
- Identifying which stages can run in parallel (independent tasks in the same stage)
- Placing human gates at every human-only and human-final task from P4
- Tracing every P1 output forward to confirm it's reachable from some stage
- Tracing every stage forward to confirm it produces at least one P1 output

**Success looks like:**
- Every P1 output is reachable by forward-tracing from at least one stage
- Every stage produces at least one P1 output (no stages that exist without producing value)
- Every human-only and human-final task from P4 has a corresponding human gate
- Every P2 input requirement is satisfied by some stage's output
- The pipeline has no circular dependencies
- Parallel stages are genuinely independent (no hidden dependencies)

**Failure looks like:**
- Orphan outputs (P1 outputs that no stage produces)
- Orphan stages (stages that don't trace to any P1 output)
- Missing human gates (human-final tasks without a decision point)
- Circular dependencies (stage A needs stage B's output, stage B needs stage A's output)
- Parallel stages that secretly depend on each other

---

### Step 2: Composition Decision

**What:** Determine whether the pipeline runs as a single Agent, a Team, or a Workflow.

**Cognitive mode:** EVALUATIVE — weighing tradeoffs based on stakes, complexity, and authority boundaries. Not "what's possible" but "what's appropriate."

**What you're actually doing:**
- Assessing stakes (low → Agent may suffice; high → Workflow likely needed)
- Checking for authority boundary conflicts (if different tasks need different authority boundaries, a Team or Workflow separates them structurally)
- Checking for verification independence needs (CC-1 — if one agent must verify another's work, they can't be the same agent)
- Assessing the need for human gates (Workflows support pause/resume; single Agents don't)
- Making the call: Agent (simple, low-stakes, single authority boundary) vs Team (moderate, collaborative, shared context) vs Workflow (complex, high-stakes, sequential gates)

**Success looks like:**
- The composition matches the stakes (low stakes → simpler composition is fine; high stakes → Workflow with human gates)
- Every CC-1 verification independence requirement is structurally possible (producer and verifier are different agents)
- Every authority boundary from P4 is enforceable within the chosen composition
- Human gates are possible within the chosen composition (Workflows support pause/resume; Teams don't natively)
- The composition isn't over-engineered (a single Agent for a 3-task low-stakes pipeline) or under-engineered (a single Agent for a 20-task pipeline with 4 human gates)

**Failure looks like:**
- A single Agent trying to verify its own work (CC-1 violation)
- A Team without explicit human gates for human-final tasks
- A Workflow for a trivially simple task (over-engineering)
- An Agent for a pipeline that needs pause/resume for human decisions

---

### Step 3: FMEA (Failure Mode and Effects Analysis)

**What:** Systematically identify what can go wrong at every stage, for every agent, for every handoff — then assess severity, likelihood, detectability, and recovery.

**Cognitive mode:** ADVERSARIAL/CONSTRAINT — systematic pessimism. "What if this breaks? What if that agent produces plausible-but-wrong output? What if the human skips the gate?" This is deliberately the opposite of the architectural optimism in Step 1.

**What you're actually doing:**
- For each pipeline stage: What if it produces wrong output? What if it produces no output? What if it produces output that looks right but isn't?
- For each agent: What is its characteristic failure mode (from P4/P7 — Extractors hallucinate, Assessors over-confirm, Generators fabricate, Aggregators omit)?
- For each handoff: What if the receiving agent misinterprets the input? What if the input template is wrong?
- For each human gate: What if the human rubber-stamps without genuine review? What if the human is unavailable?
- Scoring: Severity (1-10), Occurrence (1-10), Detection (1-10), RPN (S×O×D)
- Assigning recovery paths: Tier 1 (agent retry), Tier 2 (stage replay + escalation), Tier 3 (system halt + human intervention)
- Assigning enforcement regime: Declare (agent is told the rule), Detect (system flags violations), Prevent (system structurally prevents violations)

**Success looks like:**
- Every pipeline stage has at least one failure mode identified
- Every agent's characteristic failure mode from P4/P7 appears in the FMEA
- Every human gate has a rubber-stamping failure mode (the human just clicks approve)
- The highest RPN items have explicit mitigation in the pipeline design
- Recovery paths are assigned to every failure mode
- Enforcement regime is assigned to every boundary (not just "agent is told not to do this" — which regime, and why)

**Failure looks like:**
- Missing the most likely or most damaging failure modes
- Optimistic FMEA (assuming things will work rather than asking what if they don't)
- All enforcement at Regime 1 (Declare) when stakes justify Regime 2 or 3
- Recovery paths that don't actually recover (Tier 1 retry on a fundamentally wrong output just produces the same wrong output)
- Ignoring rubber-stamping as a failure mode at human gates

---

### Step 4: Template Architecture

**What:** Design the typed, structured interfaces between every stage, every agent, and every human gate — the 7 template types.

**Cognitive mode:** ARCHITECTURAL + CONFIGURATIONAL — defining structure (what fields exist) and configuration (what values are expected/ranged/enumerated). Like designing API contracts between services.

**What you're actually doing:**
- **Input Templates:** What structured data does each stage/agent receive? What fields, what types, what's required vs optional?
- **Output Templates:** What structured data does each stage/agent produce? What epistemic metadata (CC-3) must accompany each field?
- **Handoff Templates:** How does data pass between stages? What transformation happens? What's preserved, what's added, what's dropped?
- **Verification Templates:** What verification level applies (CC-1: structural, semantic, authority)? What checks run? What's the pass/fail criteria?
- **Decision Templates:** What does a human decision capture? The choice, the reasoning, the alternatives considered, the confidence level?
- **Feedback Templates:** How do results flow back to earlier stages? What's fed back, in what format, with what metadata?
- **Escalation Templates:** What triggers escalation? What information accompanies escalation? Who receives it? What's the expected response time?

**Success looks like:**
- Every inter-stage handoff has a typed template (no "just pass the string" handoffs)
- Every output template includes CC-3 epistemic metadata fields (confidence, provenance, assumptions, limitations, recency, uncertainty)
- Every human gate has a Decision Template that captures reasoning, not just the choice
- Every Verification Template specifies which CC-1 level applies
- Templates compose correctly (an Output Template from stage N matches the Input Template for stage N+1)
- No information is silently dropped between stages without explicit documentation

**Failure looks like:**
- Untyped handoffs ("agent A passes output to agent B" without specifying the schema)
- Missing epistemic metadata (output templates without confidence, provenance, uncertainty)
- Decision templates that only capture the choice ("approved/rejected") without reasoning
- Template mismatches between stages (Stage 1 output fields ≠ Stage 2 input fields)
- Information silently dropped at handoffs

---

### Step 5: Fallback Model Design

**What:** Define what happens when things go wrong — the three-tier recovery model and the conditions for each tier.

**Cognitive mode:** ADVERSARIAL + ARCHITECTURAL — imagining failures (adversarial) and designing recovery structures (architectural). "If this breaks, what's the path back to working?"

**What you're actually doing:**
- Tier 1 (Agent retry): What failures can the agent handle itself? Modified approach, different parameters, try again?
- Tier 2 (Stage replay + escalation): What failures need the pipeline to replay the stage with different parameters or escalate to human review?
- Tier 3 (System halt + human intervention): What failures are catastrophic enough that the pipeline must stop and wait for human authority?
- Mapping every FMEA failure mode to the appropriate tier
- Defining escalation paths: who gets notified, with what information, with what urgency

**Success looks like:**
- Every FMEA failure mode has a tier assignment (not all Tier 1 — that's optimistic)
- Tier assignments match severity: low severity → Tier 1 is fine; high severity → Tier 2 or 3
- Reversibility informs tier: low reversibility failures → Tier 3 (halt, don't retry)
- Escalation paths identify specific humans/roles, not just "escalate to human"
- The pipeline can't fail silently — every failure has a detection mechanism and a recovery path

**Failure looks like:**
- All failures assigned to Tier 1 (agent retry) — optimistically assuming agents can recover from everything
- Tier 3 assigned to trivial failures — over-engineering that stops the pipeline unnecessarily
- "Escalate to human" without specifying which human, with what information, in what timeframe
- Silent failure modes — failures that nobody detects and nobody recovers from

---

### Step 6: System Enforcement Points

**What:** Determine where and how CAWDP's cross-cutting concerns are structurally enforced in the pipeline.

**Cognitive mode:** BOUNDARY — drawing lines and determining enforcement regimes. "Where is the boundary, and is it a speed limit sign (Declare), a speed camera (Detect), or a speed limiter (Prevent)?"

**What you're actually doing:**
- **CC-1 Verification Independence:** Where in the pipeline is the producing agent structurally different from the verifying agent? Is this enforced in the composition (separate agents) or just declared in prompts?
- **CC-4 Information Boundaries:** Where are data access restrictions enforced? Database-level (Regime 3), prompt-level (Regime 1), or somewhere in between? Which agents can access which data?
- **CC-7 Cost Budget:** Where are per-agent and per-pipeline cost limits enforced? What happens when budget is exhausted — Tier 2 escalation or Tier 3 halt?
- **CC-8 Assured Audit Trail:** What level of logging at each pipeline transition? Logged/Assured/Verified — which transitions get which level?
- **CC-5 Specification Aging:** How does the pipeline know when agent specifications need review? Trigger-based or cadence-based?
- **Progressive Autonomy:** How does the pipeline track and enforce Shadow → Advisory → Supervised → Autonomous transitions? What metrics trigger promotion or demotion?

**Success looks like:**
- Every CC has at least one structural enforcement point (not just "we'll mention it in the prompt")
- CC-1 is enforced at the composition level (separate agents structurally verify each other's work)
- CC-4 enforcement regime is specified per boundary (Declare/Detect/Prevent with justification)
- CC-7 has explicit halt conditions (not just "track costs" but "stop when budget exceeds X")
- CC-8 logging levels are assigned per transition (not "log everything" or "log nothing")
- CC-5 aging cadences are specified per agent class
- Progressive autonomy transitions have measurable criteria (not just "when we trust it enough")

**Failure looks like:**
- All CCs enforced at Regime 1 (Declare) — "the agent is told not to do this" without structural enforcement
- CC-1 where the same agent produces and verifies its own work
- CC-7 cost tracking without halt conditions (costs are tracked but never acted upon)
- CC-8 at a single level for everything (over-logging trivial transitions or under-logging critical ones)
- Progressive autonomy with no measurable criteria ("promote when it seems ready")

---

### Step 7: Orchestration Design

**What:** Define how agents are routed to tasks, how triggers activate stages, and how the pipeline progresses from start to finish.

**Cognitive mode:** CONFIGURATIONAL + ARCHITECTURAL — setting parameters (configurational) and defining flow (architectural). Like writing the conductor's score for an orchestra.

**What you're actually doing:**
- **Agent routing:** Which agent handles which stage? How does the pipeline select the right agent for the right task?
- **Event-driven triggers:** From P5 event storming — which domain events trigger which stages? Which failure events trigger which recovery paths?
- **Progressive autonomy deployment:** Starting level (Shadow for new deployments), promotion criteria, demotion criteria, timeline
- **Stage transitions:** What conditions must be true for the pipeline to advance from one stage to the next? Quality gates? Human approvals? Output validation?
- **Conditional routing:** Are there stages that only execute under certain conditions? How are those conditions evaluated?

**Success looks like:**
- Every stage has a clear agent assignment (from P4 allocation)
- Every trigger from P5 has a corresponding pipeline response
- Stage transitions have explicit conditions (not just "after the previous stage")
- Conditional routing is documented (which stages are conditional, what triggers them)
- Progressive autonomy has a starting level and measurable criteria for transition
- The pipeline has a defined start state and end state (not an infinite loop)

**Failure looks like:**
- Ambiguous agent assignments ("an agent will handle this" — which agent?)
- Missing triggers (domain events from P5 that don't map to any pipeline response)
- Implicit transitions ("it just moves to the next stage" — what validates this?)
- No progressive autonomy plan (agents deployed at full autonomy from day one)
- No defined end state (pipeline runs forever or terminates without producing final output)

---

## The Cognitive Mode Summary

| Step | Primary Mode | Secondary Mode | What It's Like |
|------|-------------|----------------|---------------|
| 1. Pipeline Architecture | Architectural | — | Laying out a building floor plan |
| 2. Composition Decision | Evaluative | — | Weighing tradeoffs on a seesaw |
| 3. FMEA | Adversarial/Constraint | — | Systematic pessimism — "what breaks?" |
| 4. Template Architecture | Architectural | Configurational | Designing API contracts |
| 5. Fallback Design | Adversarial | Architectural | Failure recovery paths |
| 6. Enforcement Points | Boundary | — | Drawing lines and choosing enforcement regimes |
| 7. Orchestration | Configurational | Architectural | Writing the conductor's score |

Seven steps, six distinct cognitive modes. Steps 1 and 4 are architectural (structural). Steps 3 and 5 are adversarial (failure-focused). Step 2 is evaluative (tradeoff-weighing). Step 6 is boundary (line-drawing). Step 7 is configurational (parameter-setting). Steps 3-5 deliberately shift from optimistic (architecture) to pessimistic (failure) and back to architectural (recovery).

This cognitive shift — from building up (architecture) to breaking down (FMEA) to building recovery (fallback) — is not accidental. It's the same pattern as the CAWDP Realisation arc: ARCHITECT (build up) → DESIGN (build up) → FORMALIZE (constrain) → EMPATHIZE (human) → VERIFY (break down and check). P6 itself mirrors this arc internally.

---

## What Success Looks Like for the Whole Phase

P6 is done well when:

1. **Every P1 output is reachable** — you can trace from any final deliverable back through the pipeline to the start
2. **Every P4 human task has a gate** — human-only and human-final tasks have explicit decision points in the pipeline
3. **Verification is structurally separated** — CC-1 is enforced in the composition, not just declared
4. **The adversarial work is genuinely adversarial** — the FMEA contains failure modes that would actually hurt, not just obvious ones
5. **Templates compose correctly** — output schemas match input schemas at every handoff
6. **Enforcement is specific** — every boundary has a declared regime (Declare/Detect/Prevent) with justification, not just "enforce this"
7. **The pipeline can fail loudly** — every failure mode has a detection mechanism and a recovery tier
8. **The pipeline has a defined start and end** — not an infinite process

And P6 is done poorly when the pipeline looks like a sequential list of tasks with "and then the agent does this" handoffs, no typed interfaces, all enforcement at Regime 1, no failure modes beyond "it doesn't work," and human gates that amount to "the human reviews the output."

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-05-21T06:57:22* · `glm-5.1:cloud` · `d332ac17...`

### Prompt

what tools could help agents be successful at their tasks here?
No code please. just descriptions

### Response

# Phase 6 Tools — What Agents Need and Why

I'll organise this by the cognitive challenge each step presents, what agents struggle with, and what a tool would need to do to help.

---

## The Underlying Pattern

Across all 7 steps, agents face three recurring limitations:

1. **Completeness blindness** — agents produce representative examples, not exhaustive coverage. They'll list 4 failure modes and miss the 5th that matters most.
2. **Optimism bias** — agents default to "it works" reasoning. They describe happy paths, not broken paths. Systematic pessimism requires deliberate structuring.
3. **Context holding** — agents lose track of the whole pipeline while focused on one part. They can reason about a single handoff but struggle to verify that every handoff composes correctly across 7 stages.

The tools below address these three limitations in different ways for each step.

---

## Step 1: Pipeline Architecture

**Cognitive challenge:** Architectural — seeing the whole structure at once, verifying that every path connects and nothing is orphaned.

**What agents struggle with:** An agent can design a 7-stage pipeline that looks coherent internally but has a missing link between Stage 3 and Stage 4 that only becomes visible when you trace from the final output backward. The agent designed forward (Stage 1 → 2 → 3 → ...) but never verified backward (... → 6 → 5 → 4 → 3 → final output). It also tends to place human gates at "natural" transition points rather than at the specific tasks P4 identified as human-only or human-final.

**Tool: Reachability Tracer**
- Takes the pipeline stage list and the P2 dependency chain
- Traces forward from every stage to confirm each produces at least one P1 output
- Traces backward from every P1 output to confirm it's reachable from some stage
- Flags: orphan outputs (P1 outputs no stage produces), orphan stages (stages that produce nothing in P1), circular dependencies, and hidden dependencies in "parallel" stages
- Also cross-references P4 allocations: every human-only and human-final task must have a corresponding human gate in the pipeline. Flags any task allocation that lacks a gate.

**Tool: Human Gate Matcher**
- Takes P4 complementarity allocations and the proposed pipeline stages
- Checks that every task marked human-only or human-final has an explicit decision point in the pipeline
- Flags tasks where the allocation says "human decides" but the pipeline has no decision point — the most common structural gap in P6 designs

---

## Step 2: Composition Decision

**Cognitive challenge:** Evaluative — weighing multiple factors (stakes, authority boundaries, verification needs, human gate requirements) to make a single composition choice.

**What agents struggle with:** Agents tend to default to the most capable composition (Workflow for everything) because it's the safest choice. Or they default to the simplest (single Agent) because it's the easiest to specify. Neither is wrong in general — but the choice should follow from the specific factors of this pipeline, not from a default preference.

**Tool: Composition Decider**
- Takes P3 task count, P4 allocations (human-only tasks, human-final tasks), P5 events (especially failure events), and the stakes assessment from P0
- Walks through five decision factors with explicit weights: stakes level, number of authority boundary conflicts, CC-1 verification independence needs, number of human gates required, need for pause/resume capability
- Produces a recommendation (Agent / Team / Workflow) with rationale referencing specific factors
- Flags when factors conflict (e.g., low stakes but many human gates — the low stakes suggest Agent, but the human gates require Workflow)
- Also flags over-engineering (Workflow for 3 tasks with 1 human gate) and under-engineering (Agent for 20 tasks with 4 human gates)

---

## Step 3: FMEA

**Cognitive challenge:** Adversarial — systematic pessimism. This is the opposite of an agent's default mode.

**What agents struggle with:** Left to their own devices, agents produce optimistic FMEAs. They list obvious failure modes ("agent produces wrong output") but miss the insidious ones ("agent produces plausible-but-wrong output that passes verification"). They underweight detection difficulty (assuming they'll notice when something goes wrong). And they almost never include rubber-stamping at human gates as a failure mode — the assumption that humans will genuinely review rather than just click approve.

**Tool: Failure Mode Structurer**
- Takes the pipeline stages, P4 allocations, P5 failure events, and the characteristic failure modes from P4/P7 (Extractor: hallucination, Measurer: noise-as-signal, Assessor: overconfidence, Generator: fabrication/vagueness, Aggregator: omission)
- Walks through systematically: for each stage, for each agent, for each handoff, for each human gate — what can go wrong?
- For each stage: wrong output, no output, delayed output, plausible-but-wrong output
- For each agent: its characteristic failure mode from P4/P7 (not a generic "it fails" — the specific way this class of agent fails)
- For each handoff: input misinterpretation, schema mismatch, information silently dropped
- For each human gate: rubber-stamping (the human clicks approve without genuine review), unavailability, contradictory feedback
- Forces severity, occurrence, and detection scores for each, producing RPN
- Flags the highest RPN items for explicit mitigation in the pipeline design
- The key value: it forces the agent to think adversarially by walking through every failure category systematically, rather than listing whatever comes to mind

**Tool: Enforcement Regime Assessor**
- Takes each boundary from P4 and P7 (authority boundaries, information boundaries, etc.)
- For each boundary, walks through: what happens if this is violated? How severe? How detectable? How reversible?
- Based on severity and reversibility, recommends Declare / Detect / Prevent with justification
- Flags boundaries where the recommended regime is Regime 1 (Declare) but the severity justifies Regime 2 or 3 — this is the most common enforcement gap (agents write "the agent should not do X" when they should write "the system prevents the agent from doing X")
- Also flags the reverse: boundaries where Regime 3 is recommended but Regime 1 would suffice (over-engineering)

---

## Step 4: Template Architecture

**Cognitive challenge:** Architectural + Configurational — defining structure (what fields) and configuration (what values/ranges/enumerations) for every interface between stages.

**What agents struggle with:** Agents can produce a template for a single stage, but they struggle to ensure that Stage N's output template composes correctly with Stage N+1's input template. They forget epistemic metadata fields (CC-3). They produce Decision Templates that only capture "approved/rejected" without reasoning. And they silently drop information between stages — Stage N outputs 8 fields, Stage N+1 only takes 5, and the 3 dropped fields are never explicitly acknowledged.

**Tool: Template Composability Checker**
- Takes all proposed input/output templates for every stage and handoff
- Verifies that every output field from Stage N has a corresponding input field in Stage N+1 (either consumed or explicitly dropped with documentation)
- Verifies that every input field in Stage N+1 is provided by some Stage N output
- Verifies that every output template includes CC-3 epistemic metadata fields (confidence, provenance, assumptions, limitations, recency, uncertainty) or documents why they're not applicable
- Verifies that every Decision Template includes: the choice, the reasoning, the alternatives considered, and the confidence level — not just "approved/rejected"
- Verifies that Verification Templates specify which CC-1 level applies (structural, semantic, authority) — not just "verify"
- Flags: missing epistemic metadata, decision templates without reasoning, silent information drops, schema mismatches between stages

---

## Step 5: Fallback Model Design

**Cognitive challenge:** Adversarial + Architectural — imagining failures (adversarial) and designing recovery structures (architectural).

**What agents struggle with:** Two problems: (1) assigning all failures to Tier 1 (agent retry) because it's the simplest recovery — the agent optimistically assumes it can just try again. (2) Specifying "escalate to human" without identifying which human, with what information, in what timeframe.

**Tool: Tier Assigner**
- Takes the FMEA and walks through each failure mode
- For each failure mode, evaluates: severity, reversibility, and detectability
- Assigns Tier 1 (agent retry) only when: severity is low, reversibility is high, and the failure is likely to succeed on retry (the agent can modify its approach)
- Assigns Tier 2 (stage replay + escalation) when: severity is moderate, reversibility is medium, or retry is unlikely to produce a different result
- Assigns Tier 3 (system halt + human intervention) when: severity is high, reversibility is low, or the failure is catastrophic
- Flags: all-Tier-1 assignments (optimistic), Tier 3 for trivial failures (over-engineered), and missing escalation specifics ("escalate to human" without who/what/when)
- Also checks reversibility: low reversibility failures should never be Tier 1 (retrying an irreversible action makes things worse)

---

## Step 6: System Enforcement Points

**Cognitive challenge:** Boundary — drawing lines and determining enforcement strength.

**What agents struggle with:** The most common enforcement gap is Regime 1 (Declare) for everything — "the agent is instructed not to do X" without structural enforcement. Agents naturally produce behavioral instructions (what the agent should do) rather than structural constraints (what the system prevents the agent from doing). The second most common gap is specifying cost tracking without halt conditions — "we'll track costs" without specifying what happens when costs exceed the budget.

**Tool: CC Enforcement Checker**
- Takes the pipeline design and walks through each cross-cutting concern
- For CC-1 (Verification Independence): checks that the producing agent and verifying agent are structurally different in the composition. Flags cases where the same agent produces and verifies.
- For CC-4 (Information Boundaries): for each agent, checks that data access restrictions are specified with a regime. Flags cases where access is "declared" in prompts but not structurally enforced.
- For CC-7 (Cost Budget): checks that per-agent and per-pipeline budgets are specified with halt conditions — not just "track costs" but "halt when exceeding X tokens / $Y." Flags budgets without halt conditions.
- For CC-8 (Assured Audit Trail): assigns logging levels per transition (logged/assured/verified) based on the stakes of the transition. Flags transitions where the logging level doesn't match the stakes.
- For CC-5 (Specification Aging): checks that aging cadences are specified per agent class with event-driven triggers, not just periodic review dates.
- For Progressive Autonomy: checks that starting levels, measurable promotion criteria, and demotion criteria are specified — not just "promote when trusted."
- Produces an enforcement report: for each CC, what's enforced, at what regime, with what mechanism, and what gaps remain.

---

## Step 7: Orchestration Design

**Cognitive challenge:** Configurational + Architectural — setting parameters and defining flow.

**What agents struggle with:** Ambiguous agent assignments ("an agent will handle this"), missing triggers (P5 events that don't map to pipeline responses), implicit transitions ("it moves to the next stage" without specifying what validates the transition), and infinite loops (no defined end state).

**Tool: Orchestration Completeness Checker**
- Takes the pipeline stages, agent assignments, P5 events, and progressive autonomy plan
- Checks: every stage has an explicit agent assignment (not "an agent" but "the Boundary Mapper, a Measurer+Assessor with bridge orientation")
- Checks: every P5 domain event and failure event has a corresponding pipeline response (not just "handle it" but a specific recovery path)
- Checks: every stage transition has an explicit condition (quality gate pass, human approval, output validation) — not just "after the previous stage"
- Checks: progressive autonomy has a starting level (Shadow for new deployments), measurable promotion criteria, measurable demotion criteria, and a timeline
- Checks: the pipeline has a defined start state and end state (not an infinite loop)
- Flags: ambiguous assignments, orphan events, implicit transitions, missing autonomy plans, and undefined end states

---

## Cross-Cutting Tools

These help across multiple steps:

**Pipeline Visualiser** — renders the pipeline as a diagram showing stages, agents, human gates, data flows, and authority boundaries. Not a design tool but a verification tool: the visual representation often reveals structural gaps that text descriptions hide. If you can't draw it as a coherent diagram, the pipeline has a problem.

**Consistency Checker** — takes the full P6 output and verifies internal consistency: every agent assignment in Step 7 matches an allocation in P4, every human gate in Step 1 matches a human-only/final task, every failure mode in Step 3 has a tier assignment in Step 5, every template in Step 4 composes with its neighbours, and every enforcement point in Step 6 references a specific boundary from P4/P7. This is the final sanity check before the quality gate.

---

## What These Tools Have in Common

Every tool above addresses one of the three agent limitations I started with:

1. **Completeness blindness** → Tools that walk through systematically (Failure Mode Structurer, Reachability Tracer, CC Enforcement Checker) rather than asking the agent to list whatever comes to mind.

2. **Optimism bias** → Tools that force adversarial thinking (Failure Mode Structurer, Enforcement Regime Assessor, Tier Assigner) rather than assuming things will work.

3. **Context holding** → Tools that check cross-references between steps (Consistency Checker, Template Composability Checker, Human Gate Matcher) rather than trusting the agent to hold the entire pipeline in context simultaneously.

The pattern: **structure the agent's reasoning rather than asking it to reason freely.** Give it a checklist to walk through, a cross-reference to verify, or a systematic walk that forces exhaustiveness. The tool doesn't do the thinking — the agent still makes the architectural decisions — but the tool ensures the agent has walked through every corner of the room rather than describing the furniture in the middle and calling it done.

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-05-21T07:06:48* · `glm-5.1:cloud` · `8abae14e...`

### Prompt

What advice do you have for implementing these tools?

Perhaps you can draft a list of requirements for each that can help the implementation planner?

(No need to write code)

### Response

# Phase 6 Tools — Implementation Requirements

I'll organise this by tool, covering inputs, outputs, key requirements, and design considerations. The tools are listed in the order they'd be used during P6, not by complexity.

---

## 1. Reachability Tracer

**Purpose:** Verify that every P1 output is reachable from some pipeline stage, and every pipeline stage produces at least one P1 output.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| Pipeline stages with task assignments | P6 Step 1 (being built) | Stage ID, task list, agent assignments |
| P1 output specifications | P1 | Output ID, output name, dependencies |
| P2 dependency chain | P2 | Input requirement ID, required-by output, satisfied-by output |
| P4 human-only and human-final tasks | P4 | Task ID, allocation (human-only / human-final) |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Forward trace | Each stage → which P1 outputs it produces |
| Backward trace | Each P1 output → which stages produce it |
| Orphan outputs | P1 outputs that no stage produces (with IDs and names) |
| Orphan stages | Stages that produce nothing in P1 |
| Circular dependencies | Stages that form dependency loops |
| Hidden dependencies | "Parallel" stages that actually depend on each other |
| Human gate coverage | List of human-only / human-final tasks with/without corresponding pipeline gates |

### Key Requirements

1. **Bidirectional tracing is mandatory** — forward (stage → output) and backward (output → stage) must both succeed. Forward-only tracing catches stages that produce nothing; backward-only tracing catches outputs that no stage produces.

2. **Human gate matching must cross-reference P4** — the tool must check every human-only and human-final task from P4 against the pipeline's human gates, not just check that human gates exist somewhere. A human gate that doesn't correspond to a P4 allocation is a gate without a purpose; a P4 allocation without a corresponding gate is an unenforced boundary.

3. **Parallel stage dependency detection** — the tool must flag when two "parallel" stages have a hidden dependency (one needs the other's output). This requires tracing data flow, not just task ordering.

4. **Incremental re-tracing** — as the pipeline design changes, the tool must be re-runnable without starting from scratch. It should accept updates to the stage list and re-trace only affected paths.

5. **Output format should be visualisable** — the trace results should be renderable as a directed graph so the architect can see orphan outputs, orphan stages, and circular dependencies at a glance.

### Design Considerations

- The tool doesn't design the pipeline — it verifies a proposed pipeline. The architect still makes the structural decisions.
- Circular dependencies are not always errors — some legitimate feedback loops exist (e.g., review cycles). The tool should flag them for review, not reject them automatically.
- "Parallel stages that secretly depend on each other" is the most common and most dangerous structural gap. The tool should treat this as high severity.

---

## 2. Human Gate Matcher

**Purpose:** Verify that every P4 human-only and human-final task has an explicit decision point in the pipeline.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| P4 task allocations | P4 | Task ID, allocation (human-only / human-final / agent-primary / collaborative) |
| Pipeline stages with human gates | P6 Step 1 | Stage ID, gate type, gate decision |
| P4 adjustment factors | P4 | Task ID, cold start, experience dependency, preparation value |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Covered tasks | Human-only/final tasks with matching pipeline gates |
| Uncovered tasks | Human-only/final tasks without matching pipeline gates (the structural gap) |
| Gate coverage | For each gate: which P4 tasks it covers |
| Orphan gates | Pipeline gates that don't correspond to any P4 allocation |
| Adjustment factor flags | Tasks where adjustment factors indicate collaboration (discovery/scaffolded) but the pipeline has no preparation step before the human gate |

### Key Requirements

1. **One-to-one mapping is not required** — a single human gate can cover multiple human-final tasks in the same stage. The tool should check that every P4 allocation has at least one gate, not that every task has its own gate.

2. **Adjustment factor flags are critical** — if P4 says a task is "human-final" with discovery initiation or high preparation value, the pipeline must have a preparation step (agent prepares options) before the human gate. The tool should flag human gates that lack preparation steps where P4 adjustment factors indicate they're needed.

3. **Orphan gates are warnings, not errors** — a pipeline gate that doesn't correspond to a P4 allocation might be legitimate (e.g., a quality gate that isn't a human decision point). Flag for review, not rejection.

4. **The tool should produce a coverage percentage** — what fraction of human-only/human-final tasks have corresponding pipeline gates. Target: 100%. Below 100% means the pipeline is missing decision points.

### Design Considerations

- This tool is a complement to Reachability Tracer — Reachability checks output coverage, Gate Matcher checks authority coverage. They can be run independently or combined.
- The adjustment factor flag is the most valuable output — it catches the gap between "human decides" (P4) and "human decides with preparation" (the pipeline needs a step before the gate).

---

## 3. Composition Decider

**Purpose:** Recommend Agent / Team / Workflow composition based on pipeline-specific factors, with explicit rationale.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| P3 tasks | P3 | Task count, cognitive types, failure modes |
| P4 allocations | P4 | Human-only count, human-final count, agent-primary count, collaborative count |
| P5 events | P5 | Failure event count, recovery path complexity |
| P0 stakes assessment | P0 | Low / moderate / high stakes |
| CC-1 requirements | P4/P7 | Number of verification independence requirements |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Composition recommendation | Agent / Team / Workflow |
| Factor analysis | Each factor's weight and direction |
| Factor conflicts | Where factors pull in different directions |
| Rationale | Why this composition for this pipeline |
| Over-engineering flag | If recommendation exceeds what the pipeline needs |
| Under-engineering flag | If recommendation falls short of what the pipeline needs |

### Key Requirements

1. **Five-factor evaluation with explicit weights** — the tool must walk through all five factors (stakes, authority conflicts, CC-1 needs, human gates, pause/resume needs) and show how each factors into the recommendation. The rationale must reference specific pipeline characteristics, not generic statements.

2. **Factor conflict detection** — when factors pull in different directions (e.g., low stakes suggests Agent, many human gates suggest Workflow), the tool must surface this conflict explicitly and recommend based on the dominant factor, not ignore the tension.

3. **Threshold-based recommendations** — the tool should use clear thresholds: 1-3 tasks with no human gates and low stakes → Agent. 4-8 tasks with some human gates and moderate stakes → Team. 9+ tasks or multiple human gates or high stakes or CC-1 requirements → Workflow. These thresholds should be configurable, not hardcoded.

4. **Composition isn't the only output** — the tool should also flag what the chosen composition gives you and what it doesn't. Example: "Workflow gives you human gates and pause/resume, but doesn't automatically give you CC-1 verification independence between stages."

### Design Considerations

- This tool makes a recommendation, not a final decision. The architect can override with documented rationale.
- The thresholds are guidelines, not rules. A 2-task pipeline with high stakes and human lives on the line should still be a Workflow regardless of task count.
- The tool should be re-runnable if the pipeline design changes (e.g., tasks added or removed).

---

## 4. Failure Mode Structurer

**Purpose:** Systematically walk through every stage, agent, handoff, and human gate to identify failure modes with severity, occurrence, detection, and RPN.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| Pipeline stages | P6 Step 1 | Stage ID, tasks, agent assignments |
| P4 characteristic failure modes | P4/P7 | Per agent class: Extractor→hallucination, Measurer→noise-as-signal, Assessor→overconfidence, Generator→fabrication/vagueness, Aggregator→omission |
| P5 failure events | P5 | Failure event ID, description, recovery path |
| P4 allocations | P4 | Human-only / human-final / agent-primary / collaborative per task |
| P4 adjustment factors | P4 | Reversibility, preparation value |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Failure mode inventory | Complete list with stage, category, description, severity, occurrence, detection, RPN |
| Categorised view | By stage, by agent, by handoff, by human gate |
| Top RPN items | Failure modes ranked by RPN with recommended mitigations |
| Rubber-stamping risks | Human gates where the human is likely to rubber-stamp |
| Characteristic failure coverage | Whether each agent's characteristic failure mode appears in the FMEA |
| Uncovered categories | Categories where no failure modes were identified (possible blind spots) |

### Key Requirements

1. **Systematic walk-through is the core value** — the tool must walk through every stage, every agent, every handoff, and every human gate systematically. It should not just ask "what can go wrong?" — it should enumerate the categories and force a response for each:
   - Per stage: wrong output, no output, delayed output, plausible-but-wrong output
   - Per agent: its characteristic failure mode from P4/P7 (not generic "it fails")
   - Per handoff: input misinterpretation, schema mismatch, information silently dropped
   - Per human gate: rubber-stamping, unavailability, contradictory feedback

2. **Rubber-stamping must be explicitly assessed** — for every human gate, the tool must include a failure mode where the human approves without genuine review. This is the most commonly missed failure mode and the most dangerous (looks like success).

3. **Characteristic failure modes must be pre-populated** — the tool should start with the P4/P7 failure modes for each agent class (Extractor→hallucination, Measurer→noise-as-signal, etc.) and ask the architect to assess severity/occurrence/detection for each, rather than leaving them to remember.

4. **Uncovered categories are as important as covered ones** — if no failure modes are identified for a stage, that's a red flag. The tool should flag any stage, agent, handoff, or gate with zero failure modes as a potential blind spot.

5. **RPN scoring must use consistent scales** — severity, occurrence, and detection each on 1-10 with explicit criteria. The tool should provide scoring guidance so different users produce comparable ratings.

### Design Considerations

- This is the most important P6 tool because it counteracts agent optimism. The systematic walk-through is the key differentiator — it's not "think of failure modes" but "walk through every category and respond to each."
- The tool should allow the architect to add custom failure categories beyond the four standard ones (stage, agent, handoff, gate).
- P5 failure events should be pre-loaded as starting points, not treated as exhaustive.

---

## 5. Enforcement Regime Assessor

**Purpose:** For every boundary from P4/P7, recommend Declare / Detect / Prevent and flag gaps where enforcement is weaker than stakes justify.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| P4 authority boundaries | P4 | Task ID, boundary type, boundary description |
| P7 authority boundaries | P7 | Agent ID, never-rules, class-specific boundaries |
| P7 harm assessment | P7 | Direct output harm / indirect data harm / none |
| P6 FMEA | P6 Step 3 | Failure mode ID, severity, reversibility |
| P4 reversibility classifications | P4 | Task reversibility (High / Medium / Low) |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Boundary enforcement map | Every boundary with recommended regime (Declare/Detect/Prevent) and justification |
| Gap flags | Boundaries where recommended regime exceeds current enforcement |
| Over-engineering flags | Boundaries where Prevent is recommended but Detect would suffice |
| Implementation notes | Per boundary: what structural enforcement looks like at the recommended regime |

### Key Requirements

1. **Three-tier assessment per boundary** — for each boundary, the tool must assess: what happens if this is violated (severity), how detectable is the violation (detection), and how reversible is the violation (reversibility). These three factors determine the recommended regime.

2. **Regime recommendation logic** — 
   - Low severity + high reversibility + high detection → Regime 1 (Declare) is sufficient
   - Moderate severity or medium reversibility → Regime 2 (Detect)
   - High severity + low reversibility + low detection → Regime 3 (Prevent)
   - This logic should be explicit and auditable, not a black box.

3. **Gap flags are the most valuable output** — a boundary where the stakes justify Regime 3 (Prevent) but the current design only has Regime 1 (Declare) is the most common and most dangerous enforcement gap. The tool must flag these prominently.

4. **Implementation notes should be specific** — for each boundary, the recommended regime should include a concrete implementation suggestion. "Prevent" should say what structural enforcement looks like (e.g., "database-level access control" not just "prevent the agent from accessing this data"). "Detect" should say what monitoring looks like (e.g., "flag in audit trail when agent attempts action beyond boundary" not just "monitor for violations").

5. **Separate assessment for direct output harm and indirect data harm** — P7's two-category harm assessment means different boundaries need different enforcement. An agent that can cause direct harm through its output (SuggestionRisk) needs different enforcement than an agent that can cause indirect harm through data corruption (data integrity).

### Design Considerations

- This tool pairs naturally with Failure Mode Structurer — FMEA identifies what can go wrong, this tool determines how to enforce the boundaries that prevent those failures.
- The regime recommendation is a starting point, not a final decision. The architect should be able to override with documented rationale.
- Over-engineering flags prevent unnecessary Prevent enforcement on low-stakes boundaries, which adds complexity without value.

---

## 6. Template Composability Checker

**Purpose:** Verify that all inter-stage templates compose correctly — outputs match inputs, epistemic metadata is included, and nothing is silently dropped.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| P6 template definitions | P6 Step 4 | Template type, fields, types, required/optional, CC-3 metadata inclusion |
| P6 pipeline stages | P6 Step 1 | Stage ordering, handoff points |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Composability report | Which output fields flow to which input fields |
| Schema mismatches | Output fields that don't match expected input fields at the next stage |
| Silent drops | Fields produced but not consumed at the next stage, without explicit documentation |
| Missing fields | Fields expected as input but not provided by any prior stage output |
| CC-3 coverage | Which templates include epistemic metadata, which don't |
| Decision template quality | Whether decision templates capture reasoning + alternatives + confidence, not just choice |
| Verification template quality | Whether verification templates specify CC-1 level (structural/semantic/authority) |

### Key Requirements

1. **Field-level composability check** — the tool must compare every output field from Stage N against every input field of Stage N+1, not just the template names. A field named "confidence" in Stage N output and "confidence_score" in Stage N+1 input is a mismatch even though both are about confidence.

2. **Silent drops must be explicitly documented** — if Stage N produces 8 fields and Stage N+1 only consumes 5, the 3 dropped fields must be documented with justification (e.g., "field X is internal to Stage N and not needed by Stage N+1"). Undocumented drops are flagged as errors.

3. **CC-3 metadata is mandatory for all output templates** — every output template must include the 6 epistemic metadata fields (confidence, provenance, assumptions, limitations, recency, uncertainty) or document why they're not applicable. Absence without justification is flagged.

4. **Decision templates must capture reasoning, not just choices** — the tool must check that every decision template (at human gates) includes: the choice made, the reasoning behind it, alternatives considered, and confidence level. "Approved/Rejected" without reasoning is flagged.

5. **Verification templates must specify CC-1 level** — the tool must check that every verification template specifies which level applies (structural, semantic, authority) and what checks run at that level. "Verify the output" without specifying what verification means is flagged.

6. **The tool should support template evolution** — as templates change during design, the composability check should be re-runnable. If Stage N's output template changes, the tool should only re-check the composability with Stage N-1 and Stage N+1, not the entire pipeline.

### Design Considerations

- This tool catches what agents naturally miss: the composability between stages. An agent can design a good template for a single stage but struggles to verify that all templates compose correctly across the pipeline.
- Silent drops are the most common and most insidious problem — information that gets produced but never consumed, often because it "seemed obvious" at the producing stage but the consuming stage doesn't know it exists.
- The CC-3 and decision template checks are structural enforcement of CAWDP principles at the interface layer.

---

## 7. Tier Assigner

**Purpose:** Assign recovery tiers (1/2/3) to every FMEA failure mode based on severity, reversibility, and detectability, and flag optimistic/over-conservative assignments.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| FMEA failure modes | P6 Step 3 | Failure mode ID, severity, occurrence, detection, RPN |
| P4 reversibility classifications | P4 | Task reversibility (High / Medium / Low) |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Tier assignments | Every failure mode with recommended tier (1/2/3), rationale, and escalation specifics |
| Optimism flags | Failure modes where Tier 1 is recommended but stakes justify Tier 2/3 |
| Over-conservatism flags | Failure modes where Tier 3 is recommended but Tier 1/2 would suffice |
| Escalation specificity check | Whether escalation paths identify specific humans/roles, information, and timeframes |
| Retry feasibility assessment | Whether Tier 1 retries are likely to produce different results |

### Key Requirements

1. **Three-factor tier logic** — 
   - Tier 1 (agent retry): low severity + high reversibility + retry is likely to produce different results
   - Tier 2 (stage replay + escalation): moderate severity or medium reversibility or retry might not produce different results
   - Tier 3 (system halt + human intervention): high severity + low reversibility or catastrophic failure or agent retry would make things worse
   
   This logic should be explicit and auditable.

2. **Retry feasibility must be assessed** — Tier 1 (agent retry) only makes sense if retrying with modified parameters could produce a different result. If the agent will produce the same wrong output, Tier 1 is optimistic. The tool must assess: "Can this agent retry produce a different result, or will it produce the same wrong output?" If the latter, bump to Tier 2.

3. **Low reversibility failures must never be Tier 1** — retrying an irreversible action makes things worse. The tool must flag any Tier 1 assignment on a low-reversibility failure mode.

4. **Escalation specificity is required** — for every Tier 2 and Tier 3 assignment, the escalation path must specify: who (specific role or person), what information they receive, and what timeframe they're expected to respond in. "Escalate to human" without specifics is flagged as incomplete.

5. **Optimism detection is the key value** — the tool should specifically flag all-Tier-1 assignments (a sign that the FMEA assumed everything could be retried) and recommend reviewing whether Tier 2 or 3 is more appropriate.

### Design Considerations

- This tool directly counteracts the agent's natural optimism bias. Its primary value is flagging optimistic tier assignments, not generating them.
- The escalation specificity requirement is the second most common gap in P6 designs — "escalate to human" is easy to write, hard to operationalise.
- The tool should be re-runnable when the FMEA changes, but it should also flag when the FMEA is complete but tier assignments are missing for any failure mode.

---

## 8. CC Enforcement Checker

**Purpose:** Systematically verify that every cross-cutting concern has at least one structural enforcement point in the pipeline, and that enforcement regimes match stakes.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| Pipeline design | P6 Steps 1-7 | Stages, agents, gates, data flows |
| P4/P7 authority boundaries | P4/P7 | Boundary descriptions, reversibility, stakes |
| P6 FMEA | P6 Step 3 | Failure modes, severity |
| P6 enforcement regime assignments | P6 Step 6 (or Step 5 tool output) | Boundary, regime, justification |

### Outputs Produced

| Output | Description |
|--------|-------------|
| CC-1 report | Verification independence: which stages have producer ≠ verifier structurally enforced |
| CC-4 report | Information boundaries: per-agent data access restrictions with enforcement regime |
| CC-7 report | Cost budgets: per-agent and per-pipeline budgets with halt conditions |
| CC-8 report | Audit trail: per-transition logging level (logged/assured/verified) |
| CC-5 report | Specification aging: per-agent cadences with event-driven triggers |
| Progressive autonomy report | Starting levels, measurable promotion criteria, demotion criteria, timeline |
| Gap summary | Which CCs have no structural enforcement, which have only Regime 1 enforcement |
| Over-engineering summary | Which CCs have enforcement stronger than stakes justify |

### Key Requirements

1. **Each CC is checked independently** — CC-1 through CC-8 and progressive autonomy are separate checks with separate reports. The gap summary combines them but doesn't conflate them.

2. **CC-1 structural enforcement check** — the tool must verify that wherever CC-1 requires verification independence (the producing agent and verifying agent are different), the pipeline composition structurally enforces this — different agents, different instructions, different authority boundaries. "Agent A verifies Agent A's work" must be flagged.

3. **CC-4 enforcement regime check** — for each agent's data access, the tool must verify: what data the agent can access, what regime enforces the restriction, and whether the regime matches the stakes. "Agent is told not to access X" (Regime 1) when X is high-stakes data must be flagged.

4. **CC-7 halt conditions must be explicit** — "track costs" is not enforcement. "Halt when exceeding X tokens / $Y" is enforcement. The tool must flag cost tracking without halt conditions.

5. **CC-8 logging levels must match transition stakes** — not every transition needs Verified-level logging. But high-stakes transitions (human gates, irreversible actions, authority boundary crossings) should have at least Assured-level logging. The tool must flag mismatches.

6. **Progressive autonomy must have measurable criteria** — "promote when trusted" is not measurable. "Promote from Shadow to Advisory when override rate < 20% over 2 weeks" is measurable. The tool must flag non-measurable criteria.

7. **The gap summary is the most important output** — a single view of which CCs have structural enforcement, which have only prompt-level enforcement, and which have no enforcement at all. This is the enforcement health check for the entire pipeline.

### Design Considerations

- This tool is the structural enforcement counterpart to the Enforcement Regime Assessor — that tool recommends regimes, this tool checks that the recommendations are implemented.
- It should be runnable at any point during P6 to check the current state of enforcement, not just at the end.
- The gap summary should be visualisable (e.g., a heat map of CCs × enforcement regimes showing where gaps exist).

---

## 9. Orchestration Completeness Checker

**Purpose:** Verify that every pipeline stage has explicit agent assignments, every P5 event has a response, every transition has a condition, and the pipeline has defined start and end states.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| Pipeline stages | P6 Steps 1-7 | Stage ID, tasks, ordering |
| P4 agent assignments | P4 | Task ID, allocated actor (human/agent/system), agent class/orientation |
| P5 events | P5 | Domain events, failure events, recovery paths |
| P6 progressive autonomy plan | P6 Step 7 | Starting level, promotion/demotion criteria, timeline |
| P6 stage transitions | P6 Step 7 | Transition conditions (quality gate, human approval, output validation) |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Agent assignment coverage | Every stage has an explicit agent assignment (name, class, orientation) |
| Event coverage | Every P5 domain event and failure event has a pipeline response |
| Transition condition coverage | Every stage transition has an explicit condition |
| Progressive autonomy completeness | Starting level, measurable promotion criteria, measurable demotion criteria, timeline |
| Start/end state check | Pipeline has a defined start state and end state |
| Ambiguity flags | "An agent will handle this" without specifying which agent |
| Orphan event flags | P5 events with no pipeline response |
| Implicit transition flags | "After the previous stage" without specifying what validates the transition |

### Key Requirements

1. **Agent assignments must be explicit** — "an agent handles this" is ambiguous. "The Boundary Mapper (Measurer+Assessor, bridge-oriented) handles this" is explicit. The tool must flag any assignment without a named agent with class and orientation.

2. **Every P5 event must have a pipeline response** — domain events and failure events from P5 that don't map to any pipeline action are orphan events. The tool must flag these, as they represent triggers the pipeline isn't prepared for.

3. **Every stage transition must have an explicit condition** — "after Stage 2" is not a condition. "After Stage 2 passes quality gate with all fidelity checks passed" is a condition. The tool must flag implicit transitions.

4. **Progressive autonomy must have four elements** — starting level (Shadow/Advisory/Supervised/Autonomous), measurable promotion criteria (not "when trusted"), measurable demotion criteria (not just promotion), and timeline (how long at each level before assessment). Missing any of these four is flagged.

5. **Pipeline must have defined start and end** — no infinite loops, no undefined termination. The end state must produce at least one P1 final output.

6. **The tool should accept "intentionally deferred" as a valid answer** — for early-stage pipeline designs, some assignments may be intentionally deferred to later phases. The tool should allow marking items as "deferred with rationale" rather than flagging them as gaps.

### Design Considerations

- This tool is the final sanity check before the P6 quality gate. It catches the "we'll figure it out later" gaps that agents naturally leave.
- The "intentionally deferred" option prevents the tool from being annoyingly rigid in early design iterations while still ensuring nothing is permanently forgotten.

---

## 10. Pipeline Visualiser

**Purpose:** Render the pipeline as a visual diagram showing stages, agents, human gates, data flows, and authority boundaries.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| Complete P6 design | P6 Steps 1-7 | All stage, agent, gate, template, and enforcement data |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Pipeline diagram | Visual representation of stages, agents, human gates, data flows |
| Authority boundary overlay | Authority boundaries shown on the pipeline |
| Enforcement regime overlay | Declare/Detect/Prevent shown per boundary |
| Progressive autonomy overlay | Current autonomy levels shown per agent |

### Key Requirements

1. **The visual must show all four layers** — stages (the flow), agents (who does what), human gates (decision points), and data flows (what passes between stages). These four layers must be visible simultaneously or togglable.

2. **Human gates must be visually distinct from stage transitions** — a stage transition is automatic; a human gate requires a human decision. These must look different on the diagram.

3. **Authority boundaries must be shown as overlays** — the user should be able to toggle the authority boundary view on and off, seeing where Human/Agent/System boundaries fall in the pipeline.

4. **The visual must be exportable** — as an image or diagram format that can be included in documentation and specifications.

5. **The visual must be updateable** — when the pipeline design changes, the diagram should update without redrawing from scratch.

### Design Considerations

- This is primarily a verification tool, not a design tool. It doesn't design the pipeline — it reveals structural gaps that text descriptions hide.
- A pipeline that can't be drawn as a coherent diagram probably has a structural problem. If the visualiser can't render it, that's a signal.
- Three stakeholder views are valuable: Principal (boundary map view), Implementer (technical detail view), Assessor (enforcement and verification view). The same data, different overlays.

---

## 11. Consistency Checker

**Purpose:** Final sanity check that verifies cross-references between P6 steps and between P6 and P4/P7.

### Inputs Required

| Input | Source | Format |
|-------|--------|--------|
| Complete P6 design | P6 Steps 1-7 | All outputs from all steps |
| P4 allocations | P4 | Task ID, allocation, adjustment factors |
| P7 agent specifications | P7 | Agent ID, class, orientation, boundaries, failure modes |

### Outputs Produced

| Output | Description |
|--------|-------------|
| Cross-reference report | Every cross-reference between P6 steps, P4, and P7 checked |
| Consistency violations | Agent assignments in P6 that don't match P4 allocations |
| Missing cross-references | P6 elements that reference P4/P7 items that don't exist |
| Coverage report | What fraction of P4/P7 items are referenced in P6 |

### Key Requirements

1. **Agent assignment consistency** — every agent assignment in P6 must match a P4 allocation. If P6 says "the Boundary Mapper handles Stage 2" but P4 allocates Stage 2 tasks to a human, that's a consistency violation.

2. **Human gate consistency** — every human gate in P6 must correspond to a human-only or human-final task in P4. Every P4 human allocation must have a corresponding P6 gate.

3. **Failure mode coverage** — every P4/P7 characteristic failure mode should appear in the P6 FMEA. If the Assessor's overconfidence failure mode doesn't appear in the FMEA, that's a gap.

4. **Boundary enforcement consistency** — every P7 authority boundary should have a corresponding enforcement point in P6. If P7 says "never judge" but P6 has no structural enforcement, that's a gap.

5. **Template consistency** — output templates from one stage must match input templates of the next. This overlaps with Template Composability Checker but checks the overall consistency, not just pairwise.

6. **The coverage report should be a single percentage** — "87% of P4 allocations are covered in P6" gives a quick health check. The details show what's missing.

### Design Considerations

- This tool runs last, after all P6 steps are complete. It's the quality gate preparation check.
- It should be re-runnable whenever any P6 step changes, to verify that changes don't break cross-references.
- The coverage percentage is a useful shorthand, but the detailed violations list is where the value is.

---

## Implementation Priority

The tools are listed in execution order, but they don't all need to be built at once. Here's a suggested priority based on what catches the most dangerous gaps:

| Priority | Tool | Why |
|----------|------|-----|
| 1 | Failure Mode Structurer | Counteracts the most common agent failure (optimism). Without it, P6 will produce a pipeline that looks correct but has dangerous blind spots. |
| 2 | Enforcement Regime Assessor | Catches the most dangerous enforcement gap (Regime 1 where stakes justify Regime 3). Without it, boundaries are declared but not enforced. |
| 3 | Reachability Tracer | Catches structural gaps (orphan outputs, missing human gates). Without it, the pipeline may look coherent but have unreachable paths. |
| 4 | CC Enforcement Checker | Verifies that cross-cutting concerns aren't just mentioned but structurally enforced. Without it, CCs are aspirations, not guarantees. |
| 5 | Template Composability Checker | Catches silent information drops between stages. Without it, data is lost at handoffs without anyone noticing. |
| 6 | Human Gate Matcher | Catches authority gaps (human decisions without decision points). Without it, P4 allocations are unenforced. |
| 7 | Composition Decider | Helpful but less critical — most composition decisions are straightforward for experienced architects. |
| 8 | Tier Assigner | Important but follows from Failure Mode Structurer — can be done manually with FMEA in hand. |
| 9 | Orchestration Completeness Checker | Final sanity check — catches "we'll figure it out later" gaps. |
| 10 | Pipeline Visualiser | Valuable for communication and verification but not strictly necessary for correctness. |
| 11 | Consistency Checker | Valuable for quality gate preparation but can be done manually with careful review. |

The first four tools address the three fundamental agent limitations I started with: completeness blindness (Reachability Tracer), optimism bias (Failure Mode Structurer, Enforcement Regime Assessor), and context holding (CC Enforcement Checker, Template Composability Checker). If you only build four tools, build those four.

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-05-21T07:25:46* · `glm-5.1:cloud` · `32efa51e...`

### Prompt

We will be implementing all tools before using the platform. 

Here is the implementation for the first 3 tools. Provide notes on the plan:

***
# Plan: Phase 6 Tools — Reachability Tracer, Human Gate Matcher, Composition Decider

## TL;DR

Implement the first three P6 tools from `phase-6-tools-ideas-part1.md` following the established CAWDP pattern: Pydantic models → engine logic → tool factory → agent registration. Each tool is a standalone engine (like `tools/backcasting_engine/`) with a tool factory for agent consumption. A new `pipeline_architect` agent orchestrates all P6 tools, registered in `app/main.py` and delegated to by the orchestrator.

## Phase 1: Schema & Data Layer

**Steps 1-3 can run in parallel.**

### Step 1: P6 Schema Tables (`db/schema.py`)

Add three new tables to the existing SCHEMA_SURQL block:

- **`design_pipeline_stages`** — SCHEMAFULL. Fields: `workflow`, `stage_id` (string), `name`, `description`, `order` (int), `tasks` (array of record<design_tasks>), `agent_assignments` (array of objects with agent_id, class, orientation), `human_gates` (array of objects with gate_id, gate_type, decision_type), `status` (draft/reviewed/locked), `created_at`, `updated_at`.

- **`design_pipeline_compositions`** — SCHEMAFULL. Fields: `workflow`, `recommended_composition` (Agent/Team/Workflow), `factor_analysis` (object with stakes, authority_conflicts, cc1_needs, human_gates, pause_resume), `factor_conflicts` (array), `rationale`, `over_engineering_flag` (bool), `under_engineering_flag` (bool), `architect_override` (option<string>), `created_at`.

- **`design_pipeline_traces`** — SCHEMAFULL. Fields: `workflow`, `stage_id`, `output_id`, `trace_direction` (forward/backward), `status` (covered/orphan/circular), `details` (object), `traced_at`.

### Step 2: P6 Writer Functions (`db/writer.py`)

Add writer functions following the existing pattern:

- `save_pipeline_stage(workflow_id, stage_id, name, description, order, tasks, agent_assignments, human_gates)` — creates/updates a pipeline stage record
- `save_pipeline_composition(workflow_id, recommended_composition, factor_analysis, factor_conflicts, rationale, ...)` — records composition decision
- `save_pipeline_trace(workflow_id, stage_id, output_id, trace_direction, status, details)` — records reachability trace results
- `get_pipeline_stages(workflow_id)` — retrieves all stages for a workflow
- `get_p1_outputs(workflow_id)` — retrieves P1 artefacts for a workflow
- `get_p4_allocations(workflow_id)` — retrieves P4 task allocations for a workflow
- `get_p5_events(workflow_id)` — retrieves P5 events for a workflow

### Step 3: P6 Pydantic Models (`tools/pipeline_engine/models.py`)

Create models following `tools/backcasting_engine/models.py`:

- `PipelineStage` — stage_id, name, description, order, task_ids, agent_assignments, human_gates
- `HumanGate` — gate_id, gate_type, decision_type, covered_tasks
- `AgentAssignment` — agent_id, name, class, orientation
- `CompositionRecommendation` — recommended composition, factor_analysis dict, factor_conflicts list, rationale, over/under-engineering flags
- `FactorAnalysis` — per-factor weight and direction
- `TraceResult` — forward_traces, backward_traces, orphan_outputs, orphan_stages, circular_deps, hidden_deps, human_gate_coverage
- `GateMatchResult` — covered_tasks, uncovered_tasks, gate_coverage, orphan_gates, adjustment_factor_flags, coverage_percentage

## Phase 2: Engine Logic

**Steps 4-6 can run in parallel.**

### Step 4: Reachability Tracer (`tools/pipeline_engine/reachability.py`)

Engine class following `tools/backcasting_engine/engine.py`:

- `trace_forward(stages, p1_outputs)` — maps each stage → which P1 outputs it produces
- `trace_backward(stages, p1_outputs)` — maps each P1 output → which stages produce it
- `detect_orphan_outputs(forward_trace, p1_outputs)` — P1 outputs with no producing stage
- `detect_orphan_stages(forward_trace, stages)` — stages that produce nothing
- `detect_circular_dependencies(stages, p2_dependency_chain)` — dependency loops between stages
- `detect_hidden_dependencies(stages)` — "parallel" stages that secretly depend on each other (trace data flow, not just task ordering)
- `check_human_gate_coverage(stages, p4_allocations)` — cross-reference P4 human-only/final tasks against pipeline gates
- `run_full_trace(stages, p1_outputs, p2_dependency_chain, p4_allocations)` — orchestrator that runs all checks and returns a `TraceResult`

Key algorithm: bidirectional adjacency walk. Forward trace starts from stages and follows output production. Backward trace starts from P1 outputs and follows dependency chains. Hidden dependency detection requires data flow analysis between stages, not just task ordering.

### Step 5: Human Gate Matcher (`tools/pipeline_engine/gate_matcher.py`)

Engine class:

- `match_gates(p4_allocations, pipeline_stages)` — for each P4 human-only/final task, find corresponding pipeline gate
- `detect_uncovered_tasks(p4_allocations, pipeline_stages)` — human-only/final tasks without matching gates
- `detect_orphan_gates(pipeline_stages, p4_allocations)` — gates without corresponding P4 allocation
- `check_adjustment_factors(p4_allocations, pipeline_stages)` — flag human gates that lack preparation steps where P4 adjustment factors indicate they're needed (discovery initiation, high preparation value)
- `calculate_coverage_percentage(p4_allocations, pipeline_stages)` — fraction of human-only/final tasks with corresponding gates
- `run_full_match(p4_allocations, pipeline_stages)` — orchestrator returning `GateMatchResult`

Key algorithm: one-to-many matching. A single human gate can cover multiple human-final tasks in the same stage. The tool checks that every P4 allocation has at least one gate, not that every task has its own gate.

### Step 6: Composition Decider (`tools/pipeline_engine/composition.py`)

Engine class:

- `evaluate_stakes(p0_assessment)` — weight for stakes factor
- `evaluate_authority_conflicts(p4_allocations)` — weight for authority conflicts factor
- `evaluate_cc1_needs(cc1_requirements)` — weight for CC-1 verification independence factor
- `evaluate_human_gates(pipeline_stages)` — weight for human gate count factor
- `evaluate_pause_resume(p5_events)` — weight for pause/resume needs factor
- `detect_factor_conflicts(factor_weights)` — surface when factors pull in different directions
- `recommend_composition(factor_weights, factor_conflicts)` — threshold-based recommendation:
  - 1-3 tasks, no human gates, low stakes → Agent
  - 4-8 tasks, some human gates, moderate stakes → Team
  - 9+ tasks, multiple human gates, high stakes or CC-1 requirements → Workflow
- `check_over_engineering(recommendation, pipeline_profile)` — flag if recommendation exceeds needs
- `check_under_engineering(recommendation, pipeline_profile)` — flag if recommendation falls short
- `run_full_analysis(p0_assessment, p4_allocations, cc1_requirements, pipeline_stages, p5_events)` — orchestrator returning `CompositionRecommendation`

Key algorithm: five-factor evaluation with configurable thresholds. Factor conflict detection surfaces tension explicitly. Thresholds are configurable, not hardcoded.

## Phase 3: Tool Factory & Agent

### Step 7: Tool Factory (`agents/tools/pipeline_tools.py`)

Follow the closure pattern from `agents/tools/event_storming_tools.py`:

- `create_pipeline_tools(client_getter)` — returns list of `@tool` functions:
  - `run_reachability_trace(workflow_id, stages_json, p1_outputs_json, p2_chain_json, p4_allocations_json)` — runs full reachability trace, persists results, returns formatted report
  - `run_gate_matching(workflow_id, p4_allocations_json, stages_json)` — runs full gate matching, persists results, returns coverage report
  - `run_composition_analysis(workflow_id, p0_assessment_json, p4_allocations_json, cc1_json, stages_json, p5_events_json)` — runs full composition analysis, persists recommendation, returns rationale
  - `get_pipeline_state(workflow_id)` — retrieves current pipeline state for review

Each tool:
1. Parses JSON inputs into Pydantic models
2. Calls the engine
3. Persists results to SurrealDB via writer functions
4. Returns formatted markdown report

### Step 8: Pipeline Architect Agent (`agents/pipeline_architect.py`)

Follow the pattern from `agents/event_stormer.py`:

```python
pipeline_architect = Agent(
    id="cawdp-pipeline-architect",
    name="CAWDP Pipeline Architect",
    model=default_model(),
    db=get_surrealdb(),
    tools=create_pipeline_tools(_get_client),
    instructions=PIPELINE_ARCHITECT_INSTRUCTIONS,
    enable_agentic_memory=True,
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
)
```

Instructions cover:
- **Reachability Tracer**: bidirectional tracing is mandatory, human gate matching cross-references P4, parallel stage dependency detection, incremental re-tracing
- **Human Gate Matcher**: one-to-one mapping not required, adjustment factor flags are critical, orphan gates are warnings not errors, coverage percentage target 100%
- **Composition Decider**: five-factor evaluation with explicit weights, factor conflict detection, threshold-based recommendations, composition isn't the only output
- **Workflow**: Run reachability first, then gate matching, then composition analysis. Present results for human review. Accept override rationale.

### Step 9: Register in Orchestrator & Main

**`agents/cawdp_orchestrator.py`** — Add delegation tools:
- `run_pipeline_architecture(workflow_id, context)` — delegates to pipeline_architect
- `review_pipeline_architecture(workflow_id)` — presents pipeline architecture for human review

**`app/main.py`** — Add `pipeline_architect` to the `agents=[...]` list.

**`app/config.yaml`** — Add quick prompts for the pipeline architect.

## Phase 4: Verification

### Step 10: Eval Cases & Testing

Add eval cases in `evals/cases.py` following existing patterns:

1. **Reachability Tracer**: Test with 3 stages + 5 P1 outputs → verify forward/backward traces, orphan detection, hidden dependency detection
2. **Human Gate Matcher**: Test with 4 P4 allocations + 2 pipeline gates → verify coverage percentage, uncovered tasks, adjustment factor flags
3. **Composition Decider**: Test with low-stakes 2-task pipeline → verify Agent recommendation. Test with high-stakes 9-task pipeline → verify Workflow recommendation
4. **Integration**: Test full P6 flow: stages → reachability → gate matching → composition → review

## Relevant Files

| File | Action |
|------|--------|
| `db/schema.py` | Add 3 new tables (pipeline_stages, pipeline_compositions, pipeline_traces) |
| `db/writer.py` | Add 6+ writer functions for P6 CRUD |
| `tools/pipeline_engine/__init__.py` | Create new package |
| `tools/pipeline_engine/models.py` | Create Pydantic models |
| `tools/pipeline_engine/reachability.py` | Reachability Tracer engine |
| `tools/pipeline_engine/gate_matcher.py` | Human Gate Matcher engine |
| `tools/pipeline_engine/composition.py` | Composition Decider engine |
| `tools/pipeline_engine/visualizer.py` | Optional: Mermaid graph rendering for trace results |
| `agents/tools/pipeline_tools.py` | Tool factory (closure pattern) |
| `agents/pipeline_architect.py` | New P6 agent |
| `agents/cawdp_orchestrator.py` | Add delegation + review tools |
| `app/main.py` | Register pipeline_architect agent |
| `app/config.yaml` | Add quick prompts |
| `evals/cases.py` | Add P6 eval cases |

## Verification

1. **Schema**: Run `apply_schema()` and verify 3 new tables exist with correct fields
2. **Writer**: Call each writer function with test data and verify SurrealDB records
3. **Engine unit tests**: Test each engine method with known inputs/outputs:
   - Reachability: 3 stages, 5 outputs → expect 0 orphans, 0 circular deps
   - Reachability: 2 stages, 1 orphan output → expect 1 orphan flagged
   - Gate Matcher: 4 allocations, 2 gates → expect 100% coverage or specific uncovered tasks
   - Composition: 2 tasks, low stakes → expect Agent recommendation
   - Composition: 9 tasks, high stakes → expect Workflow recommendation
4. **Tool integration**: Call each tool via agent and verify formatted markdown output
5. **Full P6 flow**: Run orchestrator delegation → pipeline architect → review → verify all records in DB

## Decisions

- **Scope**: Part 1 only (Reachability Tracer, Human Gate Matcher, Composition Decider). Parts 2-4 (Failure Mode Structurer, Enforcement Regime Assessor, Template Composability Checker, Tier Assigner, CC Enforcement Checker, Orchestration Completeness Checker, Pipeline Visualiser, Consistency Checker) are deferred.
- **Pattern**: Each tool is a standalone engine (not embedded in agent instructions) for testability and reusability, following the backcasting engine pattern.
- **Agent**: A dedicated `pipeline_architect` agent (not extending the orchestrator) follows the established phase-agent pattern (decomposer, typer, allocator, event stormer).
- **Schema**: New tables use `design_` prefix, consistent with existing CAWDP schema conventions.
- **No workflow yet**: Unlike the backcasting engine which has a `Workflow` class, these tools are agent-driven (agent calls tools sequentially). A workflow can be added later if needed.
- **Thresholds**: Hardcoded in engine code with sensible defaults (not in config.yaml). Can be extracted later if needed.
- **Visualisation**: Include Mermaid graph rendering for trace results (follow `tools/backcasting_engine/visualizer.py` pattern).
- **Re-tracing**: Full re-trace for v1 (simpler, always correct). Incremental re-trace deferred as optimization.
***

### Response

# Notes on the Phase 6 Tools Plan (Part 1)

I'll organise this by concern level: things that will cause problems if not addressed, things that are worth improving, and things that are solid.

---

## Critical: Schema Gaps

### 1. No stage-to-output mapping

The `design_pipeline_stages` table has `tasks` (array of record<design_tasks>) but no field linking stages to the P1 outputs they produce. Without this, the Reachability Tracer's forward trace has nothing to work with. "Stage 2 produces O5, O6, O7" is the fundamental data the tracer needs, and the schema doesn't store it.

**What's needed:** a `produces_outputs` field on `design_pipeline_stages` — array of record<design_artefacts> (or similar reference to P1 output specifications). This is the forward-trace input. Without it, the tracer can only guess which outputs come from which stages based on task assignments, which is indirect and fragile.

### 2. No stage-to-stage dependency information

The schema stores stage ordering (`order` int) but not stage dependencies — which stage depends on which other stage's outputs. Without this, the circular dependency detector has nothing to walk. It also means hidden dependency detection (parallel stages that secretly depend on each other) has no data to analyse.

**What's needed:** either a `depends_on_stages` field (array of record<design_pipeline_stages>) or a separate `design_pipeline_stage_dependencies` relation table. The relation approach is cleaner for graph traversal and supports the circular dependency walk directly.

### 3. No data flow between stages

Hidden dependency detection requires knowing what information passes between stages. The schema has no representation of this. Stage A produces output X, Stage B consumes X as input — but neither the production nor the consumption is stored anywhere. This will also be critical for the Template Composability Checker in Part 2.

**What's needed:** either a `design_pipeline_handoffs` table (from_stage, to_stage, artefact_refs, template_type) or embedded fields on the stages table. A separate table is better because handoffs are a first-class concern, not a stage property — they exist between stages, not within them.

### 4. Human gates lack P4 task references

The `human_gates` field on stages is an array of objects with `gate_id, gate_type, decision_type`. But the gate matcher needs to know which P4 tasks each gate covers. Without that reference, the gate matcher can't do one-to-many matching — it would have to infer which tasks a gate covers based on proximity or naming, which is fragile.

**What's needed:** `covered_task_ids` (array of record<design_tasks>) on each human gate object. This is the explicit link between gates and P4 allocations that makes matching deterministic rather than heuristic.

---

## Critical: Tool Input Architecture

### 5. Tools should read from DB, not accept JSON strings

The plan has tool functions like `run_reachability_trace(workflow_id, stages_json, p1_outputs_json, p2_chain_json, p4_allocations_json)`. This means the agent assembles JSON from its context and passes it to the tool. Four problems:

- **Stale data risk** — the agent might pass a version of the stages that doesn't match what's in the database (it was updated but the agent hasn't re-read it)
- **Context waste** — passing large JSON structures as tool arguments consumes tokens in the agent's context window for data that already exists in the DB
- **Error-prone assembly** — the agent constructs JSON from conversation history, which introduces formatting and completeness errors
- **Redundant reads** — the agent reads data to assemble JSON, then the tool parses it back — the database should be the single source

**What's needed:** tools take `workflow_id` and read from the database. The `get_pipeline_stages`, `get_p1_outputs`, `get_p4_allocations`, and `get_p5_events` functions already exist in the plan (they're listed under writer functions, though they're readers). The tools should call these internally, not require the agent to pass the data.

Optional: allow the agent to pass override data for hypothetical analysis ("what if we added another stage?"), but the default should be DB-read.

---

## Important: Schema Design

### 6. Agent assignments and human gates as embedded objects, not tables

The plan stores `agent_assignments` and `human_gates` as arrays of objects embedded in the stages table. This means:

- You can't query all human gates across all stages without scanning every stage record
- You can't query all agent assignments for a specific agent class without scanning every stage
- The CC Enforcement Checker (Part 3) will need to query across gates and assignments
- The Pipeline Visualiser will need to render all gates and assignments independently

For v1 this works. For v2+ (when the remaining 8 tools need cross-stage queries), embedded objects will become a limitation. Worth noting but not blocking for Part 1.

### 7. Reader functions listed under writer module

`get_p1_outputs`, `get_p4_allocations`, `get_p5_events` are query/read functions, not write functions. Listing them under `db/writer.py` conflates read and write responsibilities. Either:
- Add a `db/reader.py` module (or `db/queries.py`) for read operations, or
- Rename the module to `db/data_access.py` to reflect that it handles both reads and writes

This is a code organisation concern, not a functional one, but it affects maintainability as the module grows.

### 8. P4 adjustment factors not surfaced

The Human Gate Matcher's `check_adjustment_factors` needs P4 adjustment factors (discovery initiation, experience dependency, preparation value). The plan doesn't mention where these are stored or how the gate matcher accesses them. The existing `design_tasks` table has `cognitive_type` and `complementarity_gap` but the v2.2 adjustment factors (cold start difficulty, experience dependency, discovery vs decision, preparation value, reversibility) need to be accessible. If they're in `design_tasks`, the plan should call this out. If they're not stored yet, the gate matcher will lack data for one of its most valuable checks.

### 9. P0 stakes assessment not accessible

The Composition Decider needs the P0 stakes assessment to evaluate the stakes factor. The plan lists `p0_assessment_json` as a tool input, but if tools read from DB (see point 5), it needs a `get_p0_assessment` function and a known storage location. The `design_workflows` table might hold this, but the plan doesn't confirm where stakes are stored.

### 10. CC-1 requirements at P6 stage

The Composition Decider evaluates CC-1 verification independence needs. But CC-1 requirements are formally defined in P7 (Agent Design), which happens after P6. At P6, CC-1 information comes from P4 allocations (which tasks need verification independence) rather than P7 agent specifications. The plan should clarify: at P6, CC-1 evaluation uses P4-level indicators (e.g., "this assessment task needs independent verification"), not P7-level specifications (which agent verifies which). This is a sequencing dependency worth documenting.

---

## Important: Engine Logic

### 11. Human gate coverage overlap between Reachability Tracer and Gate Matcher

The Reachability Tracer plan includes `check_human_gate_coverage` which cross-references P4 allocations against pipeline gates. But the Human Gate Matcher's entire purpose is this check. Having both tools do it creates:
- Redundant logic to maintain
- Potential inconsistency (different algorithms producing different results)
- Confusion about which tool is authoritative for gate coverage

**Recommendation:** Remove `check_human_gate_coverage` from the Reachability Tracer. The tracer focuses on output reachability and dependency structure. Gate coverage is the Gate Matcher's job. The tracer should flag "this stage has no human gate" as a structural observation (no gate exists), but the detailed P4 cross-referencing and adjustment factor checks belong in the Gate Matcher.

### 12. Hidden dependency detection needs data flow, not task ordering

The plan says "trace data flow, not just task ordering" for hidden dependency detection. But the schema doesn't store data flow (see point 3). Without explicit data flow information, the engine would have to infer it from task dependencies and P2 dependency chains, which is indirect and may miss cross-stage data dependencies that aren't visible in task-level dependencies.

This is circular: the engine needs data flow to detect hidden dependencies, but data flow is one of the things P6 is designing. For v1, the engine could use task-level dependencies as a proxy and flag "potential hidden dependency — verify with stage data flow." For v2, when data flow is stored, the engine can do proper analysis.

### 13. Circular dependency detection needs stage dependency graph

The plan says `detect_circular_dependencies(stages, p2_dependency_chain)`. But the P2 dependency chain maps output-level dependencies (output A depends on output B), not stage-level dependencies. The engine needs to translate output-level dependencies into stage-level dependencies ("Stage 3 depends on Stage 2's output") before it can detect stage-level circularity. This translation requires the stage-to-output mapping (see point 1).

For v1, the engine should:
1. Build a stage dependency graph from stage-to-output mappings + P2 output dependencies
2. Walk the stage graph for cycles
3. Report any cycles found

This is implementable, but the plan should document the two-step process (output dependencies → stage dependencies → cycle detection) rather than implying the P2 chain directly reveals stage-level circularity.

### 14. Composition thresholds need the "why" alongside the "what"

The plan says thresholds are hardcoded with sensible defaults. The requirements specified that thresholds should be configurable. Hardcoding is fine for v1, but the plan should document the threshold values and the reasoning behind them, not just say "sensible defaults." When the architect overrides a threshold, they need to know what the default was and why it was set there.

**What's needed:** a threshold manifest — for each threshold (task count, human gate count, stakes level), what the default value is and what scenario it's calibrated for. This can be a docstring or constant-level comment, not a config file.

---

## Worth Noting: Architectural Decisions

### 15. No tool for creating pipeline stages

The tools analyse pipeline stages, but who creates them? The pipeline architect agent needs to define stages (grouping P3 tasks, ordering them, assigning agents, placing gates) before it can trace them. The plan has `save_pipeline_stage` as a writer function, but no corresponding tool in the tool factory. The agent would need a `define_pipeline_stage` tool that:
- Takes a stage definition (name, tasks, agent assignments, human gates, produces outputs)
- Validates it (tasks exist in P3, agents exist in P4, outputs exist in P1)
- Persists it via the writer
- Returns confirmation

Without this, the agent can only analyse existing stages, not create them. The plan seems to assume stages are already defined when the tools run, but the pipeline architect is the agent that should be defining them.

### 16. Stage `order` field needs validation

The `order` (int) field on stages implies a simple sequence. But P6 pipelines can have parallel stages, conditional stages, and feedback loops. An integer order field can't represent "Stages 3a and 3b run in parallel after Stage 2." For v1, sequential ordering is a reasonable simplification, but the plan should note this limitation and flag it for v2.

### 17. Stage status transitions need CAWDP-aware enforcement

The `status` field (draft/reviewed/locked) on stages implies transitions. But the plan's writer functions don't enforce valid transitions (draft → reviewed → locked, not draft → locked). This connects to the earlier plan review finding: writer modules should be CAWDP-aware, not SQL-passthrough. The `save_pipeline_stage` function should validate status transitions.

### 18. The "no workflow yet" decision is right for v1

The plan says tools are agent-driven (agent calls tools sequentially) rather than wrapped in a Workflow. This is the right call for v1 — the tools need to be tested individually before being composed into a workflow. The agent instructions enforce the correct ordering (reachability → gate matching → composition), and if the agent fails to follow it, the worst case is a suboptimal analysis, not a broken system.

Worth noting: when all 11 tools are built, a Workflow composition might make sense. But that's a v2+ concern.

### 19. Incremental re-tracing deferred is correct

Full re-trace is simpler and always correct. Incremental re-tracing (only re-trace affected paths when a stage changes) is an optimisation that adds complexity without changing results. Deferring it is the right call.

### 20. Visualiser as Mermaid rendering is a good v1 choice

Mermaid diagrams are text-based, versionable, and renderable in markdown. This is the pragmatic choice for v1. A proper visual pipeline editor (drag-and-drop, interactive) is a product decision, not a methodology tool.

---

## Summary: Must-Fix Before Building

| # | Issue | Why It Blocks |
|---|-------|---------------|
| 1 | No stage-to-output mapping in schema | Reachability Tracer can't do forward trace |
| 2 | No stage-to-stage dependencies in schema | Circular dependency detection has nothing to walk |
| 4 | Human gates lack P4 task references | Gate Matcher can't do deterministic matching |
| 5 | Tools should read from DB, not accept JSON strings | Stale data, context waste, assembly errors |
| 15 | No tool for creating pipeline stages | Agent can only analyse, not design |

Items 3 (data flow), 6 (embedded vs table), and 8-10 (adjustment factors, stakes, CC-1 sequencing) are important but can be worked around for v1 with documented limitations.

---

## Run 6 — Agentic Expert ✓ COMPLETED

*2026-05-21T07:34:10* · `glm-5.1:cloud` · `1b5ea011...`

### Prompt

For your reference, here is a report on the implementation of the event storming tools for phase 5 of CAWDP:

# Event Storming Implementation — Retrospective

## Overview

The Event Stormer agent implements CAWDP v2.2 Phase 5 (Event Storming) — an
adversarial design phase that identifies domain events, failure events (mapped
to agent class failure modes), recovery paths, and system triggers for every
task in a workflow. Includes data flow validation that cross-references Phase 2
backcasting outputs with Phase 5 events.

The implementation followed the same architecture as the existing Decomposer →
Typer → Allocator pipeline: schema tables → writer functions → tool factory →
agent → orchestrator delegation.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CAWDP Orchestrator                              │
│  (manages phase transitions, delegates to sub-agents,                   │
│   presents to human for review)                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
┌─────────────────┐   ┌───────────────────┐   ┌─────────────────────┐
│   Decomposer    │   │  Typer → Allocator│   │   Event Stormer    │
│   → Typer       │   │  (Phases 3-4)     │   │   (Phase 5)        │
│   (Phases 3-4)  │   │                   │   │                    │
└─────────────────┘   └───────────────────┘   └─────────────────────┘
                                                    │
                                                    ▼
                                          ┌─────────────────────┐
                                          │  Human Review       │
                                          │  (accept/reject/    │
                                          │   re-run)           │
                                          └─────────────────────┘
```

## What Was Built

### 7 files, ~1,000 lines total

| File | Lines | Role |
|------|-------|------|
| `db/schema.py` | ~100 | 4 new tables: `design_domain_events`, `design_failure_events`, `design_recovery_paths`, `design_system_triggers` |
| `db/writer.py` | ~250 | 5 writer functions + constants with full validation |
| `agents/tools/event_storming_tools.py` | ~300 | Tool factory with 5 tools (closure pattern) |
| `agents/event_stormer.py` | ~200 | Measurer+Assessor agent with adversarial instructions |
| `agents/cawdp_orchestrator.py` | ~50 | 2 delegation tools + P5 instructions |
| `app/config.yaml` | ~3 | Quick prompts |
| `evals/cases.py` | ~80 | 5 eval cases |

### Agent Authority Boundaries

| Agent | Class | Authority | Failure Mode |
|-------|-------|-----------|-------------|
| Event Stormer | Measurer + Assessor | Measure what can fail, assess recovery, never design the workflow | Identifying only obvious failures, missing the long tail |

### Data Flow: Step by Step

```
Orchestrator                  Event Stormer                     SurrealDB
     │                              │                              │
     │  run_event_storming(         │                              │
     │    workflow_id,              │                              │
     │    task_context)             │                              │
     │────────────────────────────▶│                              │
     │                              │                              │
     │                              │  ─── For each task ───      │
     │                              │                              │
     │                              │  1. identify_domain_events( │
     │                              │     workflow_id, task_id,   │
     │                              │     events=[                │
     │                              │       {event_name,          │
     │                              │        event_type,          │
     │                              │        description,         │
     │                              │        trigger_condition,   │
     │                              │        payload,             │
     │                              │        downstream_effects,  │
     │                              │        satisfies_reqs,      │
     │                              │        produces_artefacts}  │
     │                              │     ])                      │
     │                              │───────────────────────────▶│
     │                              │  CREATE design_domain_      │
     │                              │    events SET ...           │
     │                              │◀───────────────────────────│
     │                              │                              │
     │                              │  2. identify_failure_events(│
     │                              │     workflow_id, task_id,   │
     │                              │     agent_class,            │
     │                              │     failures=[              │
     │                              │       {failure_name,        │
     │                              │        failure_type,        │
     │                              │        severity,            │
     │                              │        description,         │
     │                              │        detection_mechanism, │
     │                              │        likelihood,          │
     │                              │        cascaded_from}]      │
     │                              │───────────────────────────▶│
     │                              │  CREATE design_failure_     │
     │                              │    events SET ...           │
     │                              │  (characteristic_failure    │
     │                              │   auto-populated from       │
     │                              │   agent_class)              │
     │                              │◀───────────────────────────│
     │                              │                              │
     │                              │  3. design_recovery_path(   │
     │                              │     failure_event_id,       │
     │                              │     execution_order,        │
     │                              │     recovery_strategy, ...) │
     │                              │───────────────────────────▶│
     │                              │  CREATE design_recovery_    │
     │                              │    paths SET ...            │
     │                              │◀───────────────────────────│
     │                              │                              │
     │                              │  4. design_system_trigger(  │
     │                              │     failure_event_id,       │
     │                              │     trigger_type,           │
     │                              │     enforced_by, ...)       │
     │                              │───────────────────────────▶│
     │                              │  CREATE design_system_      │
     │                              │    triggers SET ...         │
     │                              │◀───────────────────────────│
     │                              │                              │
     │                              │  ─── Validate ───           │
     │                              │                              │
     │                              │  5. validate_event_coverage(│
     │                              │     workflow_id)            │
     │                              │───────────────────────────▶│
     │                              │  Returns: structural_gaps   │
     │                              │  + semantic_gaps + summary  │
     │                              │◀───────────────────────────│
     │                              │                              │
     │                              │  Fix any gaps, re-validate  │
     │                              │                              │
     │  [coverage report]          │                              │
     │◀────────────────────────────│                              │
     │                              │                              │
     │  review_event_storming(     │                              │
     │    workflow_id)             │                              │
     │  (calls validate_event_     │                              │
     │   coverage internally)      │                              │
     │────────────────────────────▶│  Human                       │
     │                              │                              │
     │  ┌─ Coverage Report ──────┐ │                              │
     │  │ Structural gaps: N     │ │                              │
     │  │ Semantic gaps: N       │ │                              │
     │  │ Total gaps: N          │ │                              │
     │  │                        │ │                              │
     │  │ Tasks without events   │ │                              │
     │  │ Unrecovered failures   │ │                              │
     │  │ Unsatisfied inputs     │ │                              │
     │  └────────────────────────┘ │                              │
     │                              │                              │
     │  Options:                    │                              │
     │  1. Accept all               │                              │
     │  2. Reject (with feedback)   │                              │
     │  3. Request re-run           │                              │
     │◀────────────────────────────│                              │
```

## Schema Tables

### design_domain_events

| Field | Type | Purpose |
|-------|------|---------|
| `workflow` | record | Parent workflow |
| `task` | record | Task this event occurs at |
| `event_name` | string | Descriptive name |
| `event_type` | string (enum) | 13 types: task_started, task_completed, handoff_initiated, etc. |
| `description` | string | What happens |
| `trigger_condition` | string | What causes this event |
| `payload` | array | Data this event carries |
| `downstream_effects` | array | What this event triggers |
| `satisfies_requirements` | array | ir_id strings from Phase 2 input_requirements |
| `produces_artefacts` | array | Artefact record IDs from design_artefacts |
| `design_phase` | string | draft → reviewed → locked |

### design_failure_events

| Field | Type | Purpose |
|-------|------|---------|
| `workflow` | record | Parent workflow |
| `task` | record | Task where failure occurs |
| `agent_class` | string (enum) | 7 classes: extractor, measurer, assessor, etc. |
| `failure_name` | string | Descriptive name |
| `failure_type` | string (enum) | 12 types: omission, false_alarm, commission, etc. |
| `severity` | string | low, medium, high, critical |
| `characteristic_failure` | string | **Auto-populated** from agent_class by writer |
| `detection_mechanism` | string | How would you know this happened |
| `likelihood` | string | unlikely, possible, likely, very_likely |
| `cascaded_from` | record (optional) | Links cascading failures to their root |
| `design_phase` | string | draft → reviewed → locked |

### design_recovery_paths

| Field | Type | Purpose |
|-------|------|---------|
| `workflow` | record | Parent workflow |
| `failure_event` | record | Failure this recovery addresses |
| `execution_order` | number | 1 = try first, 2 = try second, etc. |
| `recovery_strategy` | string (enum) | retry, escalate, fallback, skip, halt, etc. |
| `recovery_actor` | string (enum) | human, agent, system, human_agent_collaborative |
| `time_budget` | string | How long recovery should take |
| `success_criteria` | string | How we know recovery worked |
| `design_phase` | string | draft → reviewed → locked |

### design_system_triggers (SCHEMALESS)

| Field | Type | Purpose |
|-------|------|---------|
| `workflow` | record | Parent workflow |
| `failure_event` | record (optional) | Failure this trigger responds to |
| `trigger_event` | string | What event triggers this |
| `trigger_source` | string | domain_event or failure_event |
| `trigger_type` | string (enum) | 9 types: automatic_progression, escalation_trigger, etc. |
| `action` | string | What the system does |
| `action_parameters` | object | Heterogeneous — SCHEMALESS allows arbitrary shape |
| `enforced_by` | string | declare, detect, or prevent |
| `design_phase` | string | draft → reviewed → locked |

## Validation: Two Levels

The `validate_event_coverage` tool performs two levels of checking:

### Structural checks (automatic, deterministic)

| Check | Query | Severity |
|-------|-------|----------|
| Every task has ≥1 domain event | `tasks NOT IN (SELECT task FROM domain_events)` | High |
| Every task has ≥1 failure event | `tasks NOT IN (SELECT task FROM failure_events)` | High |
| Every high/critical failure has recovery | `severity IN [high,critical] NOT IN recovery_paths` | Critical |
| Every critical failure has system trigger | `severity=critical NOT IN system_triggers` | Critical |
| Cascade chain integrity | `cascaded_from references non-existent failure` | Medium |

### Semantic checks (agent must have linked correctly)

| Check | Query | Severity |
|-------|-------|----------|
| Every Phase 2 input has satisfying event | `ir_id NOT IN satisfies_requirements[*]` | High |
| Every output artefact has producing event | `artefact_id NOT IN produces_artefacts[*]` | High |

## What Went Well

### 1. Architecture reuse was a force multiplier

The Event Stormer followed the exact same architecture as the Decomposer, Typer,
and Allocator. Every pattern was already established:

- **Schema tables**: Same `SCHEMAFULL` / `SCHEMALESS` pattern, same index strategy
- **Writer functions**: Same validation-first approach, same `_get_client()` helper
- **Tool factory**: Same closure pattern with `client_getter` callable
- **Agent definition**: Same `Agent()` constructor with `Ollama` model, same
  `_get_client()` for tools
- **Orchestrator delegation**: Same `_run_sub_agent()` helper, same tool naming
  convention (`run_*` / `review_*`)

This meant zero architectural decisions needed to be made — just implementation.

### 2. The plan review caught real gaps before implementation

The plan review (from `event-storming-plan-notes.md`) identified three schema
gaps that would have been costly to fix post-implementation:

- **Recovery path ordering**: Without `execution_order`, recovery paths would
  be an unordered set — the database couldn't distinguish "retry first, then
  escalate" from "escalate first, then retry"
- **Cascading failure linkage**: Without `cascaded_from`, cascade chains
  couldn't be queried — blast radius analysis would be impossible
- **Event-to-artefact linkage**: Without `satisfies_requirements` and
  `produces_artefacts` arrays, validation could only check task-level coverage,
  not artefact-level coverage

All three were caught in review, not in production.

### 3. The `characteristic_failure` auto-population is the right design

The original proposal had the agent supply `characteristic_failure` as a string.
The review correctly identified this should be deterministic from `agent_class`.
The writer now auto-populates it from `AGENT_CLASS_FAILURE_MODES`, which:

- Eliminates a source of agent hallucination
- Ensures consistency across all failure events for the same class
- Makes the eval case trivially testable

### 4. The `review_event_storming` improvement was caught in review

The original design had `review_event_storming` taking `coverage_report_json`
as a parameter, requiring the orchestrator to call `validate_event_coverage`
separately first. The review identified this should call validation internally —
same pattern as the other review tools. This was fixed before merge.

## What Went Wrong

### 1. The `failure_event` field on `design_system_triggers` was missed

This was the only real bug. The `validate_event_coverage` function queries
`SELECT failure_event FROM design_system_triggers` (check #4 — critical
failures without triggers), but the schema's `design_system_triggers` table
had no `failure_event` field. It only had `trigger_event` (a string).

**Impact**: The validation query would silently return zero results. Check #4
("every critical failure has a system trigger") would always report "no gaps"
even when triggers were missing. The system trigger couldn't be linked back to
the failure event it responds to.

**Root cause**: The schema was written from the proposal document, which also
omitted the field. The writer function and tool were written to match the
schema. The bug was consistent across all three layers — which is why it
wasn't caught by import checks or linting.

**Fix**: Added `failure_event` field to schema (`option<record<design_failure_events>>`),
writer function (`failure_event_id: str | None` parameter), and tool
(`failure_event_id: str | None` parameter). Three files, one root cause.

**Lesson**: Cross-layer validation gaps (schema → writer → tool) are invisible
to static analysis. The only way to catch them is integration testing against
a real database, or a systematic review of every query against every schema
definition.

### 2. The `review_event_storming` tool had a design smell

The original design required the orchestrator to call `validate_event_coverage`
separately, then pass the JSON result to `review_event_storming`. This was
inconsistent with `review_allocation`, which formats data the orchestrator
already has.

**Fix**: Changed `review_event_storming` to call `_validate_event_coverage`
internally via `_get_client()`.

**Lesson**: When extending a pattern, check for consistency with existing
implementations. The `review_allocation` tool doesn't take a JSON parameter —
it formats data inline. The event storming review should follow the same
pattern.

### 3. Eval cases were added late

The eval cases were in the plan but were the last thing implemented. This meant
the implementation was "complete" before any automated testing existed.

**Impact**: Low in this case (the eval cases passed), but the ordering risked
discovering issues late.

**Lesson**: Add eval cases alongside the implementation, not after. The
decomposition-allocation implementation had eval cases from the start, and
they caught issues during development.

## Key Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Schema for triggers | `SCHEMALESS` | Action parameters are inherently heterogeneous |
| `characteristic_failure` | Auto-populated by writer | Deterministic from agent_class; agent shouldn't supply it |
| `payload` / `downstream_effects` | `TYPE array` | Need `INCLUDES` operator for validation queries |
| Validation vs cross-reference | Single `validate_event_coverage` tool | Returns both structural gaps and semantic gaps separately |
| Agent class | Measurer+Assessor, bridge orientation | Adversarial analysis maps to measure+assess; bridge connects P2→P5→P6 |
| Recovery path ordering | `execution_order` field | Enables sequential recovery strategies |
| Cascading failures | `cascaded_from` self-reference | Enables blast radius queries |
| Event-to-artefact linkage | `satisfies_requirements` + `produces_artefacts` arrays | Enables artefact-level coverage validation |
| `design_phase` | Auto-set to 'draft' by writer | Matches `design_tasks.phase` pattern; enables human gate workflow |
| Per-workflow processing | Orchestrator delegates once, agent iterates | Consistent with decomposition pattern |
| `review_event_storming` | Calls validation internally | Consistent with `review_allocation` pattern |

## Quality Gates

### After Event Storming (before P6)

- [ ] Every task has at least one domain event
- [ ] Every task has at least one failure event
- [ ] Every high/critical failure has a recovery path
- [ ] Every critical failure has a system trigger
- [ ] Every Phase 2 input requirement is satisfied by a domain event
- [ ] Every Phase 2 output artefact is produced by a domain event
- [ ] Cascade chain integrity (no broken `cascaded_from` references)
- [ ] Recovery paths have sequential `execution_order` values

## Lessons for Phase 6

1. **Cross-layer validation is invisible to static analysis** — The
   schema-writer-tool gap in `design_system_triggers` was only catchable by
   integration testing or systematic cross-reference review. Phase 6 should
   include a schema-vs-query audit step.

2. **Plan reviews are highest-leverage** — The three schema gaps caught in
   review (ordering, cascading, artefact linkage) would have been much more
   expensive to fix post-implementation. The review caught them at the
   cheapest possible point.

3. **Eval cases alongside implementation** — Don't defer eval cases. They
   should be written as the tools are written, not after.

4. **Consistency with existing patterns** — When extending a pattern (tool
   factory, writer function, orchestrator delegation), check the existing
   implementations for conventions that aren't documented. The
   `review_event_storming` parameter inconsistency was a pattern mismatch
   that wasn't caught until review.

## File Inventory

```
db/schema.py                          # +4 tables (~100 lines)
db/writer.py                          # +5 writer functions + constants (~250 lines)
agents/tools/event_storming_tools.py  # NEW — tool factory (~300 lines)
agents/event_stormer.py               # NEW — agent definition (~200 lines)
agents/cawdp_orchestrator.py          # +2 delegation tools + P5 instructions (~50 lines)
app/config.yaml                       # +3 quick prompts
evals/cases.py                        # +5 eval cases (~80 lines)
docs/cawdp/event-storming-tools-ideas.md   # Original proposal
docs/cawdp/event-storming-plan-notes.md    # Plan review
docs/cawdp/retros/event-storming-implementation.md  # This file
```

### Response

# What the Event Storming Retrospective Means for the P6 Plan

The retrospective confirms several of my earlier notes, challenges one, and adds two concerns I didn't raise.

---

## Validated: My Notes Confirmed

### Tools should read from DB (Note #5)

The retrospective's Bug #1 (the `failure_event` field missing across schema → writer → tool) is exactly what happens when all three layers are written from the same proposal. The proposal omitted the field, so all three layers omitted it consistently — and the consistency made the bug invisible.

But the retrospective also shows the *fix*: `review_event_storming` was changed to call `_validate_event_coverage` internally via `_get_client()`, rather than taking a JSON parameter. This is the established pattern — tools read from DB, format results inline, don't take large JSON payloads from the agent.

**This reinforces my recommendation:** the P6 tools should take `workflow_id` and read from DB. The agent shouldn't be assembling `stages_json`, `p1_outputs_json`, etc. The Event Stormer tools don't take JSON — they take IDs and query internally. P6 should follow the same pattern.

### Plan reviews are highest-leverage (implied by all my notes)

The retrospective explicitly calls this out. Three schema gaps caught in review vs. the cost of fixing them post-implementation. My 5 "must-fix" items exist precisely because catching them now is cheaper than discovering them during integration testing.

### No tool for creating pipeline stages (Note #15)

The Event Stormer has 5 tools, and 4 of them are *creation* tools: `identify_domain_events`, `identify_failure_events`, `design_recovery_path`, `design_system_trigger`. Only `validate_event_coverage` is a pure analysis tool. The event stormer doesn't just analyse — it builds the P5 data.

The P6 plan, by contrast, has 4 analysis tools and no creation tools. The pipeline architect can trace, match, and recommend, but can't create the stages it's tracing. This is a structural gap that the retrospective pattern makes visible.

---

## Challenged: Eval Case Timing

### My original plan placed evals at Step 10 (end)

The retrospective explicitly says this was a mistake: "Eval cases were added late. The implementation was 'complete' before any automated testing existed." The lesson: "Add eval cases alongside the implementation, not after."

**This changes the plan structure.** Instead of Phase 4: Verification as a final step, eval cases should be written alongside each engine — reachability tests written when `reachability.py` is written, gate matcher tests written when `gate_matcher.py` is written, etc.

---

## New Concerns the Retrospective Raises

### 1. Cross-layer consistency audit is essential

The retrospective's Bug #1 (missing `failure_event` across schema → writer → tool) shows that when a field is missing from the proposal, it's missing from all three layers consistently. Consistency makes the gap invisible.

**Implication for P6:** my 5 "must-fix" schema items (stage-to-output mapping, stage dependencies, data flow, gate task references, creation tools) need to be checked across all three layers before implementation begins. If I add `produces_outputs` to the schema, I need to verify the writer function handles it and the tool reads it. If I add `depends_on_stages` as a relation table, I need the writer to create the relation and the Reachability Tracer to walk it.

**Concrete recommendation:** after schema changes, add an explicit audit step — for each new field, check that it appears in: (a) the SurrealDB schema definition, (b) the writer function that creates/updates it, (c) the reader function that queries it, (d) the tool that exposes it to the agent. Four-layer consistency check.

### 2. Auto-population reduces hallucination surface

The retrospective's `characteristic_failure` auto-population is a pattern worth carrying forward. When a field's value is deterministic from another field (agent_class → characteristic_failure), the writer should populate it, not the agent. The agent doesn't need to know the failure mode for each class — the writer does.

**Implication for P6:** look for fields where the value is deterministic from context:
- The Composition Decider's factor analysis might derive some weights from pipeline characteristics (task count → rough weight for human gate factor)
- The Human Gate Matcher's `coverage_percentage` is deterministic from the match results — the writer should calculate it, not the agent
- If `design_pipeline_stages` gets a `stage_type` field (sequential/parallel/conditional), some validation rules might be deterministic from stage_type

Not all auto-population opportunities will be obvious now. The pattern to carry: when implementing writer functions, ask "is any field's value determined entirely by other fields in this record?" If yes, auto-populate it.

### 3. The `design_phase` field pattern needs to be consistent

The retrospective shows `design_phase` (draft/reviewed/locked) on all four Event Storming tables. The P6 plan adds `status` (draft/reviewed/locked) on `design_pipeline_stages` but not on `design_pipeline_compositions` or `design_pipeline_traces`.

**Inconsistency:** why would pipeline stages have a lifecycle status but composition decisions and trace results wouldn't? A composition recommendation starts as draft (agent-proposed), gets reviewed, and becomes locked (human-approved). A trace result starts as draft (preliminary), gets verified, and becomes locked (confirmed). The same lifecycle applies.

**Recommendation:** add `design_phase` (or `status`) to all three new tables, using the same enum (draft/reviewed/locked) and the same auto-default-to-draft pattern that the Event Storming tables use.

---

## Adjusted Must-Fix List

Incorporating the retrospective:

| # | Issue | Original Severity | Retrospective Impact |
|---|-------|-------------------|---------------------|
| 1 | No stage-to-output mapping | Must-fix | Unchanged |
| 2 | No stage-to-stage dependencies | Must-fix | Unchanged |
| 4 | Human gates lack P4 task references | Must-fix | Unchanged |
| 5 | Tools should read from DB | Must-fix | **Stronger** — Bug #1 shows the failure mode |
| 15 | No tool for creating pipeline stages | Must-fix | **Stronger** — Event Stormer pattern shows 4/5 tools are creators |
| — | Cross-layer consistency audit | **New** | Bug #1 shows this is how gaps hide |
| — | Eval cases alongside implementation | **New** | Not at end as plan currently states |
| — | `design_phase` on all new tables | Moderate | Consistency with existing tables |
| 3 | No data flow between stages | Important | Unchanged — still deferrable for v1 |
| 6 | Embedded vs table for gates/assignments | Minor | Unchanged — v2 concern |

---
