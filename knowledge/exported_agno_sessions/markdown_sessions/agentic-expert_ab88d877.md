# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `ab88d877...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-13T02:24:06 |
| **Runs** | 10 completed / 10 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-13T02:24:06* · `glm-5.1:cloud` · `b9e37b3a...`

### Prompt

Consider the review below on our recent task analysis process. Demonstrate how this could become a repeatable process for any task we are considering for an agentic workflow? Take note of the gaps and weaknesses and include the steps that would strengthen the process.

```
# Process Review

## The Journey

Here's what we actually did, in sequence:

1. **Task Decomposition** — We started by decomposing the marking task into phases, subtasks, and dependency chains. We identified the cognitive operations required (structural, domain-semantic, comparative-semantic, etc.) and the complementarity properties (what humans are better at vs. what agents are better at).

2. **Complementarity Analysis** — We mapped each subtask against 15 capability dimensions (reasoning, ethical judgment, parallelisation, etc.) with Human and Agent scores. This produced H/A gap scores that drove assignment decisions (Human-led, Agent-led, Collaborative).

3. **Pipeline Architecture** — We backcasted from final deliverables through dependency chains, designed the data objects that flow between stages, and established the "agent prepares judgment, human makes judgment" principle.

4. **Agent Roster Design (Stage 1)** — We decomposed the monolithic "extract features" subtask into 4 specialist agents based on genuinely different cognitive operations. We designed execution waves and dependency graphs.

5. **Agent Roster Design (Stage 2)** — We designed the per-student marking loop with 7 agents across 12 waves, introducing the Briefing Composer (a meta-agent) and the C1 Assessor (the first agent to produce a score — crossing from evidence to judgment-preparation).

6. **Agent Roster Design (Stage 3)** — We designed the cohort QA stage with 4 agents across 2 waves, adding the Flag Aggregator (which wasn't in the original subtask list — it emerged from the design process).

7. **Job Description Design** — We created two maximally different agent job descriptions (Drift Detector vs Feedback Drafter) to stress-test the specification format.

## Key Findings and Insights

### Finding 1: Type Collision is Bidirectional
Your earlier insight about type collision in AI outputs (17+ distinct information types encoded as prose) applies symmetrically to **inputs**. The 18-question agent design framework encodes 6+ distinct cognitive modes but offers one input surface (text fields) for all. This drives the design of alternative specification surfaces that match cognitive modes to interaction modalities.

### Finding 2: Subtask Decomposition Reveals Hidden Complexity
The most impactful design decision was decomposing subtask 1.3 ("Extract features from all 50 submissions") into 4 specialist agents. The monolithic label hid 5 genuinely different cognitive operations: structural mapping, domain-semantic extraction, comparative-semantic detection, structural-semantic auditing, and multi-source anomaly detection. Without decomposition, one agent would need blockchain domain knowledge AND synthesis detection AND reflection analysis AND statistical anomaly detection all loaded simultaneously.

### Finding 3: Authority Boundaries are the Design's Load-Bearing Walls
The principle "agent prepares judgment, human makes judgment" turned out to be too coarse. We needed **specific authority boundaries per agent**: "never interpret" (Measurers), "never rate" (Extractors), "never adjudicate" (Aggregators), "never be vague" (Generators), "never finalise" (Assessors). Each boundary is the **inverse of the agent's primary failure mode**. This is a design pattern worth formalising.

### Finding 4: The Complementarity Gap Threshold is Quantifiable
We discovered that subtasks with complementarity gaps of 6+ points on Ethical Judgment, Values Alignment, or Decision Authority should be human-only. Subtasks with gaps of 5+ on Parallelisation & Scale or Output Consistency should be agent-led. Everything in between is collaborative. This gives a **decision algorithm** for task assignment.

### Finding 5: Meta-Agents Emerge from the Design Process
The Briefing Composer and Flag Aggregator weren't in the original subtask list — they emerged when we realised that without them, the human would have to cross-reference multiple agent outputs manually, creating cognitive load that defeats the purpose of pre-processing. Meta-agents reduce cognitive load by consolidating information from multiple sources.

### Finding 6: The Pipeline is More Efficient Than We Estimated
The estimated human time per student dropped from 25-30 minutes (fully manual) to 17-26 minutes (agent-assisted). But the real saving is in quality: the human spends 100% of their time on judgment tasks, not mechanical ones. Fatigue-induced inconsistency should drop significantly.

## Strengths of the Process

1. **Thorough decomposition before design** — We spent significant time understanding the task before designing agents. This prevented premature commitment to agent architectures.

2. **Complementarity-driven assignment** — The H/A scores provided a structured, defensible basis for task assignment rather than gut feel.

3. **Boundary principles embedded at agent level** — Each agent has an explicit constraint on what it must NOT do. This prevents role creep and protects human authority.

4. **Maximally different test cases** — The Drift Detector vs Feedback Drafter contrast stress-tested the job description format across every dimension.

5. **Authority boundaries traceable to complementarity gaps** — Every "never" constraint can be traced back to a specific H/A gap score.

6. **Pipeline thinking** — Designing the data flow (backcasting) before the agent details ensured that dependencies are satisfied and no information is lost between stages.

## Weaknesses of the Process

1. **Theoretical complementarity scores** — The H/A scores (H:9/A:2 etc.) are estimates, not empirically validated. Different task contexts would yield different scores. We didn't test whether these scores map to actual capability differences.

2. **No prototyping or validation** — We designed the entire pipeline on paper without building or testing any agents. We don't know if the Claims Analyst can actually identify blockchain claims with sufficient accuracy, or if the Feedback Drafter can actually avoid vagueness.

3. **Assumed a single human marker** — The pipeline is designed for one human. If the marking team has multiple markers, the drift detection would need to detect inter-marker variation, not just intra-marker drift.

4. **No failure mode analysis for the pipeline itself** — What happens if the Claims Analyst produces inaccurate labels? What happens if the Briefing Composer omits a critical anomaly? We didn't design fallback or recovery paths.

5. **No cost-benefit analysis per agent** — Is the Consistency Checker worth the overhead? Is the Record Assembler adding value beyond what a simple script could do? Some agents might not justify their complexity.

6. **The human experience wasn't designed** — The human in this system faces 17 agents across 3 stages. We didn't design the interface through which the human receives and acts on agent outputs. The Briefing Composer is a start, but the full human workflow wasn't specified.

7. **We didn't test the decomposition granularity** — Are 17 agents too many? Could some be merged without loss? Is the Claims Analyst too narrow? Is the Anomaly Sentinel too broad? We don't have empirical data on the right level of decomposition.

## Steps We Missed

1. **Empirical validation of task decomposition** — We should have tested the decomposition with actual marking experts. Do they recognise these subtasks? Do they decompose the task differently?

2. **Agent failure testing** — We should have designed "what if" scenarios: what if the Claims Analyst hallucinates? What if the Drift Detector's statistical test is inappropriate for the data? What if the Feedback Drafter can't avoid vagueness for a specific student?

3. **Pipeline orchestration design** — We designed the agents but not the orchestration layer that triggers Wave 1, waits for completion, triggers Wave 2, etc. We didn't specify error recovery, timeout handling, or partial completion protocols.

4. **Human interface design** — We didn't specify how the human interacts with 17 agents' outputs. What does the marking dashboard look like? How does the human navigate from Briefing Document to C1 scoring to feedback review?

5. **Edge case specification** — What happens when a student submits an empty deck? A corrupted file? A deck that's entirely AI-generated with no human work? We didn't specify how agents handle these.

6. **Iterative refinement protocol** — We didn't specify how the pipeline would be tested, what metrics would indicate success, or how agents would be improved based on performance data.

## Improvements to Existing Steps

1. **Complementarity scoring** — Instead of theoretical scores, we could rate each dimension on a 1-9 scale for a *specific* LLM model (e.g., GPT-4, Claude 3.5) and a *specific* human profile (e.g., subject-matter expert vs. trained marker). This would make the scores empirically grounded.

2. **Task decomposition** — We could add a "cognitive load analysis" step: for each subtask, estimate the working memory demands, the number of distinct cognitive operations, and the switching cost. This would validate whether our decomposition granularity is correct.

3. **Agent boundary specification** — We could add "stress tests" for each boundary: what specific inputs would cause the Drift Detector to interpret rather than measure? What specific student submissions would cause the Feedback Drafter to be vague? These stress tests would validate that the boundaries are enforceable.

4. **Job description format** — We could add "adversarial examples" to each job description: specific inputs that are designed to push the agent toward its failure mode. This would help developers implement the constraints correctly.

---

## Could Event Storming Be Appropriate?

**Yes — but selectively, and at a specific point in the process.**

### What Event Storming Is

Event Storming is a domain-driven design technique where participants map **domain events** (things that happen in the system) on a timeline, revealing causal relationships, dependencies, and gaps. Events are written in past tense (e.g., "SubmissionReceived," "FormatChecked," "AnomalyFlagged") and arranged chronologically. Participants then identify commands (who triggers the event), aggregates (what processes it), and policies (what happens next).

### Where It Fits in Our Process

Event Storming would be most valuable **between Steps 2 and 3** — after task decomposition and complementarity analysis, but before pipeline architecture design. Here's why:

**What we did well without Event Storming:**
- Task decomposition (we identified the subtasks through cognitive analysis)
- Complementarity analysis (we assigned subtasks through capability gaps)
- Agent design (we specified agents through boundary principles)

**What we missed that Event Storming would have caught:**
- **Missing events** — Events like "ConsistencyCheckFailed," "HumanOverrideScore," "FeedbackRejectedByHuman" were not in our pipeline design. These are failure and recovery events that Event Storming surfaces naturally.
- **Data flow gaps** — We didn't explicitly map what data flows between which agents. Event Storming forces you to ask "what does the Claims Analyst need FROM the Deck Cartographer?" in a concrete way.
- **Trigger conditions** — We specified execution waves but not the *conditions* that trigger each wave. What if Format Sentinel finds a corrupted file? Does the pipeline stop? Skip? Flag and continue? Event Storming surfaces these decision points.
- **Human decision points** — Event Storming naturally identifies where a human must make a decision (e.g., "BorderlineDecisionMade" is a distinct event with a human actor). Our complementarity analysis identified these, but Event Storming would make them *visible on the timeline*.

### When Event Storming is Most Valuable

Event Storming is most valuable for tasks with:
- **Multiple actors** (human + multiple agents)
- **Sequential dependencies** (where one agent's output triggers another)
- **Failure modes** (where things can go wrong and need recovery)
- **Data handoffs** (where structured data passes between agents)

Our marking task has ALL of these. So yes, Event Storming would be appropriate here.

### When Event Storming is Less Valuable

Event Storming is LESS valuable for tasks that are:
- **Single-actor** (one agent doing one thing)
- **Stateless** (no dependencies between steps)
- **Simple linear flows** (no branching, no failure recovery)

For these tasks, our existing process (task decomposition → complementarity analysis → agent design) is sufficient. Event Storming would add overhead without revealing new insights.

### The Hybrid Process I'd Recommend

Our existing process + Event Storming, at the right point:

```
Step 1: Task Decomposition (cognitive analysis)
         ↓
Step 2: Complementarity Analysis (capability allocation)
         ↓
Step 2.5: EVENT STORMING ← NEW
         - Map domain events on timeline
         - Identify commands, aggregates, policies
         - Surface missing events (failures, overrides, recovery)
         - Validate data flow between agents
         - Specify trigger conditions for each wave
         ↓
Step 3: Pipeline Architecture (backcasting + data flow)
         ↓
Step 4: Agent Roster Design (per stage)
         ↓
Step 5: Job Description Design (per agent)
         ↓
Step 6: Prototype & Validate ← ALSO NEW
         - Build minimum viable agents
         - Test with real data
         - Measure accuracy, consistency, human satisfaction
```

The Event Storming step would have caught the missing failure events, the data flow gaps, and the trigger conditions that we missed. It would also have surfaced the Flag Aggregator earlier (it emerged during design, but Event Storming would have revealed the need for it when mapping "who consolidates all the flags for the human?").

### For All Tasks or Some Tasks?

**I'd recommend Event Storming for all multi-agent workflows** — any task where multiple agents work together with dependencies, data handoffs, and human decision points. The overhead is modest (a few hours of collaborative mapping), and the payoff is significant (missing events, data flow gaps, trigger conditions).

For **single-agent tasks** (one agent doing one thing), Event Storming is overkill. The task decomposition and complementarity analysis are sufficient.

For **simple linear pipelines** (Agent A → Agent B → Agent C, no branching), Event Storming is useful but not essential. The data flow is simple enough to specify without a collaborative mapping exercise.

For **complex branching pipelines with human decision points** (like our marking task), Event Storming is essential. The complexity of dependencies, data handoffs, and failure recovery makes it easy to miss critical events without systematic mapping.

---

## Summary: The Process We Built, Evaluated

| Aspect | Rating | Notes |
|--------|--------|-------|
| Task decomposition depth | ★★★★★ | Decomposed to the cognitive operation level |
| Complementarity framework | ★★★★☆ | Structured but theoretical — needs empirical grounding |
| Authority boundary design | ★★★★★ | Inverse-of-failure-mode principle is powerful |
| Pipeline architecture | ★★★★☆ | Data flow was implicit — Event Storming would make it explicit |
| Agent roster design | ★★★★★ | 17 agents with clear roles, boundaries, and interactions |
| Job description depth | ★★★★★ | Two maximally different specs that enable implementation |
| Failure mode analysis | ★★☆☆☆ | We didn't design for pipeline failures or edge cases |
| Human experience design | ★★☆☆☆ | We didn't specify the human's interface to 17 agents |
| Empirical validation | ★☆☆☆☆ | Entirely theoretical — no prototypes, no testing |
| Iterative refinement | ★☆☆☆☆ | No protocol for improving agents based on performance |

**The process is strong on design and weak on validation.** The next step is to build minimum viable versions of the most critical agents (Claims Analyst for hallucination risk, Feedback Drafter for vagueness risk, Drift Detector for interpretation risk) and test them against real marking data.The full roster is **17 agents** across 3 pipeline stages, with **5 classes** that share boundary principles and failure modes. The taxonomy gives you a reusable classification system — when you encounter a new agent design problem, you can ask: "Is this an Extractor, Measurer, Assessor, Generator, or Aggregator?" and the boundary principle and failure mode follow immediately.

The process review reveals that our strongest contributions were in **decomposition depth** and **boundary design**, while our weakest areas were **validation** and **human experience**. The Event Storming recommendation is well-timed — it would address exactly the gaps we identified (missing events, data flow, trigger conditions, failure recovery) and it fits naturally between complementarity analysis and pipeline architecture.

For your Future's Edge curriculum: the **5-class taxonomy** and the **"constrain the inverse of the failure mode"** principle are both teachable frameworks that generalise beyond this specific workflow.
```

### Response

# The Complementarity-Driven Agentic Workflow Design Process (CAWDP)

*A repeatable methodology for designing human-agent collaboration systems — from single-agent tasks to complex multi-agent pipelines.*

---

## Origin & Purpose

This process was extracted from a retrospective review of an assignment-marking workflow design (23 agents, 4 pipeline stages, 13 human-only subtasks). The review identified 7 weaknesses and 6 missing steps. This methodology integrates every correction.

**Core premise:** The agent's highest-value role is *judgment preparation*, not *answer generation*. Every design decision in this process serves that principle.

---

## Process Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    6 PHASES + 5 QUALITY GATES                       │
│                                                                     │
│  PHASE 1          PHASE 2          PHASE 3          PHASE 4         │
│  TASK             CAPABILITY       SYSTEM           AGENT           │
│  INTELLIGENCE     ALLOCATION       ARCHITECTURE     DESIGN         │
│      │               │               │               │              │
│  [GATE 1]       [GATE 2]        [GATE 3]        [GATE 4]          │
│                                                                     │
│              PHASE 5              PHASE 6                           │
│              HUMAN EXPERIENCE     VALIDATION & ITERATION            │
│                  │                    │                              │
│              [GATE 5]           (continuous)                        │
└─────────────────────────────────────────────────────────────────────┘
```

**Scaling heuristic — not every phase is needed for every task:**

| Task Complexity | Phases Required | Typical Examples |
|---|---|---|
| **Single-agent, no human loop** | 1 → 2 → 4 | Data extraction, summarisation, translation |
| **Single-agent + human review** | 1 → 2 → 4 → 5 | Draft generation, analysis with human sign-off |
| **Multi-agent, linear pipeline** | 1 → 2 → 3 → 4 → 5 | Sequential processing with handoffs |
| **Multi-agent, branching + human decisions** | 1 → 2 → 2.5 → 3 → 4 → 5 → 6 | Complex workflows like the marking pipeline |

---

## PHASE 1: Task Intelligence

*Understand the task before designing anything.*

### Step 1.1: Task Decomposition

**What:** Break the task into phases, subtasks, and dependency chains. Identify the *cognitive operations* required — not just "what needs to happen" but *what kind of thinking* each step demands.

**How:**
1. List all deliverables the task must produce
2. Backcast from each deliverable: what must be true for this to exist?
3. Decompose each prerequisite into subtasks
4. Classify each subtask's cognitive operation type:

| Cognitive Operation | Description | Example |
|---|---|---|
| **Structural** | Mapping form/organisation | "Count slides, identify sections" |
| **Domain-semantic** | Interpreting domain-specific meaning | "Identify blockchain claims" |
| **Comparative-semantic** | Comparing across instances | "Detect synthesis patterns across submissions" |
| **Structural-semantic** | Auditing structural-intent alignment | "Is reflection section actually reflective?" |
| **Statistical** | Numerical pattern detection | "Flag outlier word counts" |
| **Generative** | Producing novel text/structure | "Draft constructive feedback" |
| **Evaluative** | Making quality judgments | "Score against rubric criteria" |
| **Synthesis** | Consolidating multiple sources | "Merge flags into unified report" |

**Artifact:** `Task Decomposition Map` — each subtask annotated with cognitive operation type, dependencies, and estimated cognitive load.

### Step 1.2: Cognitive Load Analysis *(NEW — addresses Weakness 7)*

**What:** For each subtask, estimate the working memory demands, number of distinct cognitive operations, and switching cost.

**How:**
1. For each subtask, ask: *How many distinct cognitive operations are bundled here?*
2. If >2, flag for potential further decomposition
3. Estimate working memory demand: how many things must be held simultaneously?
4. Estimate switching cost: how much context must be loaded/unloaded?

**Decomposition granularity check:**
- **Under-decomposed:** >3 cognitive operations per subtask → decompose further
- **Right-sized:** 1-2 cognitive operations per subtask
- **Over-decomposed:** subtask is trivially simple and its output doesn't justify a separate agent → consider merging

**Artifact:** `Cognitive Load Assessment` — per-subtask: operation count, working memory demand, switching cost, granularity verdict.

### Step 1.3: Expert Validation *(NEW — addresses Missing Step 1)*

**What:** Validate the decomposition with domain experts before proceeding.

**How:**
1. Present decomposition to 1-3 domain experts
2. Ask: "Do you recognise these subtasks? Would you decompose differently?"
3. Capture any subtasks they identify that you missed
4. Confirm the cognitive operation labels match expert mental models

**Effort heuristic:** 30-60 minute conversation per expert. Skip only if you ARE the domain expert AND you can articulate your expertise explicitly.

**Artifact:** `Expert Validation Record` — expert feedback, decomposition changes made.

### Step 1.4: Edge Case Inventory *(NEW — addresses Missing Step 5)*

**What:** Identify boundary conditions and anomalous inputs before designing the system.

**How:**
1. For each input type, list: empty, corrupted, ambiguous, adversarial, oversized, undersized variants
2. For each subtask, ask: "What input would break this?"
3. Categorise: *must-handle* (common enough to design for) vs. *must-detect* (flag for human) vs. *out-of-scope*

**Artifact:** `Edge Case Catalog` — per input type: edge cases, expected handling, categorisation.

---

### 🔴 QUALITY GATE 1: Task Intelligence Complete

**Checklist before proceeding:**
- [ ] Every subtask has a cognitive operation classification
- [ ] No subtask bundles >3 cognitive operations (or explicitly justified)
- [ ] Cognitive load assessment completed for all subtasks
- [ ] Domain expert validation obtained (or expertise self-attestation documented)
- [ ] Edge case catalog has ≥3 cases per input type
- [ ] All deliverables trace back through dependency chains

**If not passed:** Return to decomposition. Missing edge cases or unvalidated decomposition will cascade into architectural failures.

---

## PHASE 2: Capability Allocation

*Determine what humans do, what agents do, and why.*

### Step 2.1: Complementarity Analysis

**What:** Map each subtask against capability dimensions to determine Human/Agent/Collaborative assignment.

**How:**
1. Score each subtask on 15 capability dimensions (1-9 scale) for BOTH Human and Agent:

| Dimension | Human Score Considerations | Agent Score Considerations |
|---|---|---|
| **Reasoning depth** | Abstract reasoning, novel problems | Pattern matching, defined-rule reasoning |
| **Ethical judgment** | Moral reasoning, value conflicts | Rule-based ethics, bias detection |
| **Values alignment** | Organisational culture, implicit norms | Explicit rule compliance |
| **Decision authority** | Accountability, stakeholder trust | Recommendation generation |
| **Domain expertise** | Tacit knowledge, intuition | Explicit knowledge, data access |
| **Parallelisation** | Sequential processing limit | Infinite parallel execution |
| **Output consistency** | Fatigue drift, mood variation | Deterministic given same input |
| **Speed** | Minutes to hours per unit | Seconds per unit |
| **Novelty handling** | Adaptive, creative | Fallback to training distribution |
| **Context sensitivity** | Reads room, adjusts | Follows instructions literally |
| **Precision** | Human error rate | Computational accuracy |
| **Scalability** | Linear time scaling | Near-constant time scaling |
| **Explainability** | Can articulate reasoning | Can cite sources, show chains |
| **Cultural sensitivity** | Lived experience, nuance | Training data patterns |
| **Error type** | Omission, fatigue errors | Hallucination, overconfidence |

2. Calculate H-A gap for each dimension
3. Apply the **Complementarity Allocation Algorithm:**

```
For each subtask:
  IF any dimension in {Ethical Judgment, Values Alignment, Decision Authority}
     has gap ≥ 6 (Human dominant) → HUMAN-LED
  
  IF any dimension in {Parallelisation, Output Consistency, Scalability}
     has gap ≥ 5 (Agent dominant) → AGENT-LED
  
  IF dimensions in both sets have gaps above thresholds → COLLABORATIVE
  
  IF no dimensions exceed either threshold → DEFAULT TO COLLABORATIVE
     (insufficient evidence for exclusive assignment)
```

**Critical improvement over original process:** Scores must be **model-specific** and **human-profile-specific** *(addresses Weakness 1)*:
- Specify which LLM (e.g., GPT-4, Claude 3.5, local model) — scores vary dramatically
- Specify human profile (e.g., subject-matter expert, trained operator, novice) — expertise changes gaps
- Document the rationale for each score — enables later empirical testing

**Artifact:** `Complementarity Matrix` — per subtask: 15 H/A scores, gap scores, allocation decision, model reference, human profile, rationale.

### Step 2.2: Actor Analysis *(NEW — addresses Weakness 3)*

**What:** Identify all human actors, not just "the human."

**How:**
1. List every human role that interacts with the system
2. For each role, specify: expertise level, decision authority, time availability, cognitive load tolerance
3. Map which subtasks each human role owns
4. Identify inter-human coordination needs (e.g., multiple markers needing calibration)

**Artifact:** `Actor Map` — roles, capabilities, constraints, inter-actor coordination requirements.

---

## PHASE 2.5: Event Storming *(NEW — addresses Weakness 4, Missing Step 3)*

*Only for multi-agent workflows with dependencies, data handoffs, and/or human decision points.*

### When to Use Event Storming

| Condition | Do Event Storming? |
|---|---|
| Single agent, no human loop | ❌ Skip — overhead exceeds value |
| Linear pipeline, no branching, no failure recovery | ⚠️ Optional — data flow is simple |
| Multi-agent with human decisions | ✅ Recommended |
| Multi-agent with branching/failure recovery | ✅ Essential |
| Multiple human actors | ✅ Essential |

### Step 2.5.1: Domain Event Mapping

**What:** Map every event that occurs in the system on a timeline.

**How:**
1. Write each domain event on a card (past tense): `SubmissionReceived`, `FormatChecked`, `AnomalyFlagged`, `ScoreRecommended`, `HumanOverrideIssued`
2. Arrange chronologically
3. For each event, identify:
   - **Command:** What triggers it? (who or what)
   - **Actor:** Who/what executes it?
   - **Data produced:** What structured output does it generate?
   - **Policy:** What happens next? (what events does it trigger?)

### Step 2.5.2: Failure Event Surfacing

**What:** Systematically identify events that shouldn't happen but will.

**How:**
For each happy-path event, ask:
1. *What if this produces wrong output?* → `AgentOutputDoubted`
2. *What if this times out?* → `AgentTimeoutExpired`
3. *What if this receives unexpected input?* → `UnexpectedInputReceived`
4. *What if the human disagrees?* → `HumanOverrideIssued`
5. *What if the human is absent?* → `HumanDecisionDeferred`

### Step 2.5.3: Data Flow Validation

**What:** For each event, verify that its input data exists and is accessible.

**How:**
1. For each event, ask: "What data does this event's actor need?"
2. Trace backwards: which prior events produce that data?
3. Flag any data that is *implied but not explicitly produced*
4. Verify data format compatibility (schema, structure, granularity)

### Step 2.5.4: Trigger Condition Specification

**What:** Define the exact conditions that trigger each event.

**How:**
1. For each event, write the condition as a boolean expression:
   - `FormatChecked` triggers when: `SubmissionReceived AND file is not corrupted`
   - `HumanOverrideIssued` triggers when: `ScoreRecommended AND human disagrees AND delta > threshold`
2. For each trigger, define the timeout: what happens if the condition is never met?
3. For each trigger, define the fallback: what happens if the triggering event fails?

**Artifact:** `Event Storm Map` — timeline of events, commands, actors, data flows, failure events, trigger conditions, timeouts, fallbacks.

**Key insight from original process:** Event Storming would have surfaced the Flag Aggregator *before* Stage 3 design (it emerged organically during design), and would have caught missing events like `ConsistencyCheckFailed`, `HumanOverrideScore`, `FeedbackRejectedByHuman`.

---

### 🔴 QUALITY GATE 2: Capability Allocation Complete

**Checklist before proceeding:**
- [ ] Every subtask has H/A scores with model reference and human profile
- [ ] Allocation decisions trace to specific gap scores
- [ ] Actor map includes all human roles (not just "the human")
- [ ] (If applicable) Event Storm map covers happy path + failure events
- [ ] (If applicable) Data flow validated for every event — no implied-but-not-produced data
- [ ] (If applicable) Trigger conditions specified with timeouts and fallbacks

**If not passed:** The most common failure here is implied data flow — agents assumed to receive data that no prior step explicitly produces. Fix before proceeding.

---

## PHASE 3: System Architecture

*Design the structure that everything lives in.*

### Step 3.1: Pipeline Architecture (Backcasting)

**What:** Design the data flow from final deliverables backwards.

**How:**
1. List final deliverables
2. For each, trace the dependency chain back through phases
3. Define the **data objects** that flow between stages:
   - Schema (what fields)
   - Producer (which agent/human creates it)
   - Consumer (which agent/human reads it)
   - Mutability (append-only, replaceable, immutable)
   - Persistence (ephemeral, session, permanent)

4. Identify execution topology:
   - **Sequential:** Phase N completes before Phase N+1 starts
   - **Parallel:** Multiple agents run simultaneously within a phase
   - **Event-driven:** Agents activate on trigger conditions
   - **Gated:** Phase transition requires quality check

### Step 3.2: Orchestration Design *(NEW — addresses Missing Step 3)*

**What:** Design the system that manages agent execution, not just the agents themselves.

**How:**
1. Specify execution engine: what triggers Wave 1? What waits for Wave 1 completion?
2. Define **orchestration policies:**
   - **Timeout policy:** How long before an agent is assumed failed?
   - **Retry policy:** How many retries? With what backoff?
   - **Partial completion policy:** Can the pipeline continue if one agent fails?
   - **Cascading failure policy:** What happens when a critical-path agent fails?
3. Define **progress tracking:** How is pipeline state represented? How does the human know where things stand?

### Step 3.3: Failure Mode & Effects Analysis (FMEA) *(NEW — addresses Weakness 4)*

**What:** For every agent and every pipeline transition, analyse what happens when things go wrong.

**How:**
1. For each agent, list its **primary failure mode** (from the 5-class taxonomy)
2. For each failure mode, assess:
   - **Detection probability:** How likely is the failure to be noticed?
   - **Impact radius:** How many downstream agents/humans are affected?
   - **Recovery path:** What's the fallback?
3. For each pipeline transition, list:
   - **Upstream failure:** What if the input is wrong?
   - **Transition failure:** What if the handoff fails?
   - **Downstream assumption:** What does the next agent assume about this input?

**FMEA template per agent:**

| Field | Content |
|---|---|
| Agent name | |
| Primary failure mode | (e.g., hallucination for Extractors, noise-as-signal for Measurers) |
| Detection method | (How will we know it failed?) |
| Detection probability | (High / Medium / Low) |
| Impact if undetected | (What goes wrong downstream?) |
| Recovery path | (Rerun? Skip? Flag? Human escalation?) |
| Containment boundary | (What stops the failure from propagating?) |

**Artifact:** `System Architecture Document` — pipeline diagram, data objects, orchestration policies, FMEA table.

---

### 🔴 QUALITY GATE 3: Architecture Complete

**Checklist before proceeding:**
- [ ] Every data object has schema, producer, consumer, mutability, persistence
- [ ] No data flow is implied — every consumer's input is explicitly produced
- [ ] Orchestration policies cover timeout, retry, partial completion, cascading failure
- [ ] FMEA completed for every agent and every pipeline transition
- [ ] Recovery paths specified for every failure mode
- [ ] Edge cases from Phase 1 mapped to handling in architecture

---

## PHASE 4: Agent Design

*Design each agent with the specificity needed for implementation.*

### Step 4.1: Agent Classification

**What:** Assign each agent to a class. This immediately gives you its boundary principle and failure mode.

**The 5-Class Taxonomy:**

| Class | Authority Boundary | Primary Failure Mode | Hallucination Risk | Key Constraint |
|---|---|---|---|---|
| **Extractor** | Never judge | Hallucination | High | Only extract, never interpret |
| **Measurer** | Never interpret | Noise-as-signal | Low | Present data, not meaning |
| **Assessor** | Never finalise | Overconfidence | Medium | Recommend, never decide |
| **Generator** | Never be vague | Fabrication | High | Every claim must cite evidence |
| **Aggregator** | Never add | Omission | Low | Consolidate only, no new analysis |

**Application:** When you encounter a new agent design problem, first ask: *Is this an Extractor, Measurer, Assessor, Generator, or Aggregator?* The boundary principle and failure mode follow immediately.

### Step 4.2: Authority Boundary Specification

**What:** Define what each agent must NOT do. The constraint is the **inverse of the failure mode.**

**Design pattern:**
```
IF agent class = Extractor:
  boundary = "Never judge" (because failure mode = hallucination of interpretations)
IF agent class = Measurer:
  boundary = "Never interpret" (because failure mode = noise-as-signal)
IF agent class = Assessor:
  boundary = "Never finalise" (because failure mode = overconfidence)
IF agent class = Generator:
  boundary = "Never be vague" (because failure mode = fabrication/vagueness)
IF agent class = Aggregator:
  boundary = "Never add" (because failure mode = omission through addition)
```

### Step 4.3: Boundary Stress Testing *(NEW — addresses Improvement 3)*

**What:** Before finalising the boundary, test it with inputs designed to push the agent toward its failure mode.

**How:**
For each agent, design 3-5 **boundary stress inputs:**
- *What input would tempt this Measurer to interpret?* → e.g., a statistical outlier that "obviously" means something
- *What input would tempt this Generator to be vague?* → e.g., a submission so weak that constructive feedback feels impossible
- *What input would tempt this Assessor to finalise?* → e.g., a near-perfect submission where scoring feels obvious

**Document the expected boundary-enforced response** vs. the tempted response. This becomes a test case for implementation.

### Step 4.4: Agent Job Description

**What:** Create a complete specification that enables a developer to implement the agent without further design decisions.

**Template:**

```
AGENT JOB DESCRIPTION
=====================

IDENTITY
  Name:
  Class: (Extractor / Measurer / Assessor / Generator / Aggregator)
  Authority Boundary: (the "never" constraint)
  Primary Failure Mode: (the inverse of the boundary)

MISSION
  One-sentence statement of what this agent produces, for whom, and why.

INPUT SCHEMA
  - Required inputs (what data, from which agent/human, in what format)
  - Optional inputs (what data improves quality if available)
  - Edge case handling (from Phase 1 edge case catalog)

OUTPUT SCHEMA
  - Structured output format (typed, not prose)
  - Required fields
  - Optional fields
  - Confidence/provenance metadata

CONTEXT & KNOWLEDGE
  - Domain knowledge required
  - Reference materials (specific documents, URLs, data)
  - System prompt context

TOOLS
  - Required tools (web search, calculator, etc.)
  - Optional tools

HARD CONSTRAINTS
  - Authority boundary (from Step 4.2)
  - Additional constraints specific to this agent
  - Prohibited actions

QUALITY CRITERIA
  - What does "good output" look like for this agent?
  - Measurable quality indicators
  - Failure indicators (signals that the agent is failing)

ERROR HANDLING
  - What to do on missing input → (flag? skip? error?)
  - What to do on ambiguous input → (request clarification? flag? proceed with confidence score?)
  - What to do on tool failure → (retry? fallback? flag?)

ESCALATION PROTOCOL
  - When to escalate to human
  - When to escalate to orchestrator
  - What information to include in escalation

PERFORMANCE EXPECTATIONS
  - Expected latency
  - Expected accuracy (if estimable)
  - Cost budget per invocation

ADVERSARIAL EXAMPLES *(NEW — addresses Improvement 4)*
  - 2-3 inputs designed to push toward failure mode
  - Expected boundary-enforced response for each
  - Common temptation and correct refusal

INTERACTION MAP
  - Upstream: which agents/humans provide input
  - Downstream: which agents/humans consume output
  - Parallel: which agents run alongside this one
```

### Step 4.5: Cost-Benefit Assessment *(NEW — addresses Weakness 5)*

**What:** Determine whether each agent justifies its complexity.

**How:**
For each agent, assess:
1. **Value added:** What would be lost if this agent were removed? Would a simpler alternative (script, template, rule) suffice?
2. **Complexity cost:** How complex is this agent to implement, maintain, and debug?
3. **Failure risk:** What's the probability and impact of this agent's failure mode?
4. **Verdict:**
   - **Essential:** Unique cognitive work that can't be achieved simpler
   - **Valuable:** Justified complexity — saves human time or improves quality
   - **Questionable:** Could be replaced by a script or simpler mechanism
   - **Unnecessary:** Adds no value beyond what's already provided

**Artifact:** `Agent Roster` — each agent with class, boundary, job description, cost-benefit verdict.

---

### 🔴 QUALITY GATE 4: Agent Design Complete

**Checklist before proceeding:**
- [ ] Every agent classified into 5-class taxonomy
- [ ] Authority boundary specified as inverse of failure mode
- [ ] Boundary stress tests designed (3-5 per agent)
- [ ] Job descriptions complete for all agents (using template)
- [ ] Adversarial examples included in each job description
- [ ] Cost-benefit assessment completed — no "unnecessary" agents remain
- [ ] Every agent's input schema traces to a producer in the architecture
- [ ] Every agent's output schema traces to a consumer in the architecture

---

## PHASE 5: Human Experience Design *(NEW — addresses Weakness 6 & Missing Step 4)*

*The human in the system is not a bucket that agents pour outputs into.*

### Step 5.1: Cognitive Load Budget

**What:** Determine how much information the human can process at each interaction point.

**How:**
1. For each human-only subtask, estimate:
   - **Information volume:** How many agent outputs must the human consume?
   - **Decision density:** How many decisions must the human make?
   - **Time pressure:** How quickly must each decision be made?
   - **Consequence severity:** How bad is a wrong decision?
2. If cognitive load exceeds budget at any point:
   - Add a **cognitive offloader** (meta-agent that pre-synthesises)
   - Reduce information volume (filter, summarise, prioritise)
   - Reduce decision density (batch similar decisions, present one at a time)
   - Reduce time pressure (async review instead of real-time)

### Step 5.2: Human Interface Specification

**What:** Design how the human receives, navigates, and acts on agent outputs.

**How:**
1. For each human interaction point, specify:
   - **What the human sees** (layout, information hierarchy, priority ordering)
   - **What the human does** (approve/reject, score, edit, override)
   - **What the human needs** (context, prior agent outputs, comparison data)
   - **What the human doesn't need** (filter out information that's not decision-relevant)
2. Design the **navigation flow:** How does the human move between interaction points?
3. Design the **interruption model:** Can the human pause and resume? What state is preserved?

### Step 5.3: Override & Feedback Mechanisms

**What:** Design how the human corrects the system.

**How:**
1. For each human decision, define:
   - **Override mechanism:** How does the human change an agent's output?
   - **Feedback path:** Does the override inform the agent for future runs?
   - **Audit trail:** Is the override logged with rationale?
2. Distinguish between:
   - **Decision overrides** (human changes a specific output)
   - **Parameter adjustments** (human changes system configuration)
   - **Process interventions** (human changes the pipeline itself)

**Artifact:** `Human Experience Specification` — cognitive load budget, interface specification, navigation flow, override mechanisms.

---

### 🔴 QUALITY GATE 5: Human Experience Complete

**Checklist before proceeding:**
- [ ] Cognitive load budgeted for every human interaction point
- [ ] No interaction point exceeds cognitive load budget without a mitigation
- [ ] Interface specification covers what human sees, does, needs, doesn't need
- [ ] Navigation flow between interaction points is specified
- [ ] Override mechanisms specified for every human decision point
- [ ] Audit trail specified for all overrides

---

## PHASE 6: Validation & Iteration *(NEW — addresses Weakness 2, Missing Step 6)*

*Design without validation is speculation.*

### Step 6.1: Prototype Priority Matrix

**What:** Determine which agents to build first.

**How:**
Rank agents by **risk × value:**

| Risk Level | Value Level | Priority |
|---|---|---|
| High failure probability | High value if correct | 🔴 **Prototype first** |
| High failure probability | Low value | 🟡 Prototype with minimal investment |
| Low failure probability | High value | 🟢 Prototype to confirm expectations |
| Low failure probability | Low value | ⚪ Defer or skip prototyping |

**For the marking pipeline, this would be:**
- 🔴 Claims Analyst (high hallucination risk + high value)
- 🔴 Feedback Drafter (high fabrication risk + high value)
- 🟡 Drift Detector (low hallucination risk but interpretation risk)
- 🟢 Briefing Composer (aggregation, low risk)

### Step 6.2: Minimum Viable Agent Testing

**What:** Build and test the minimum implementation of each priority agent.

**How:**
1. Implement agent with job description specification
2. Test against:
   - **Accuracy:** Does it produce correct outputs on known-good inputs?
   - **Boundary adherence:** Does it respect its authority boundary on stress inputs?
   - **Failure mode activation:** What inputs trigger its characteristic failure mode?
   - **Edge case handling:** How does it handle the edge cases from Phase 1?
3. Record actual performance vs. estimated complementarity scores
4. Update complementarity matrix with empirical data

### Step 6.3: Pipeline Integration Testing

**What:** Test agents together, not just individually.

**How:**
1. Run the pipeline end-to-end on a small sample (3-5 instances)
2. Verify:
   - Data flow: does every agent receive the data it needs?
   - Timing: does the pipeline complete within expected time?
   - Human experience: does the cognitive load match the budget?
   - Failure recovery: what happens when an agent produces wrong output?
3. Measure: human time per unit, accuracy vs. manual, human satisfaction

### Step 6.4: Iterative Refinement Protocol

**What:** Define how the system improves over time.

**How:**
1. **Metrics to track:**
   - Per-agent: accuracy rate, failure rate, cost per invocation
   - Per-pipeline: total human time, error rate, human satisfaction
   - Per-deliverable: quality score vs. manual baseline
2. **Improvement triggers:**
   - Agent accuracy < threshold → retrain or redesign
   - Human override rate > threshold → boundary or specification needs revision
   - Human cognitive load > budget → interface or meta-agent redesign
   - New edge cases → update edge case catalog and agent specifications
3. **Review cadence:** After every N runs (N = 10 for high-frequency, 3 for low-frequency)

**Artifact:** `Validation Report` — prototype results, empirical complementarity scores, pipeline integration results, refinement protocol.

---

## The Complete Artifact Chain

Every decision must be traceable from final agent specification back to original task analysis:

```
Task Decomposition Map
  └→ Cognitive Load Assessment
       └→ Expert Validation Record
            └→ Edge Case Catalog
                 └→ Complementarity Matrix (model-specific, human-specific)
                      └→ Actor Map
                           └→ Event Storm Map (if applicable)
                                └→ System Architecture Document
                                     └→ FMEA Table
                                          └→ Agent Roster
                                               └→ Agent Job Descriptions (per agent)
                                                    └→ Boundary Stress Tests (per agent)
                                                         └→ Cost-Benefit Assessments (per agent)
                                                              └→ Human Experience Specification
                                                                   └→ Validation Report
                                                                        └→ Empirical Complementarity Scores
```

---

## Quick Reference: Weakness → Process Fix Mapping

| Original Weakness | Process Fix | Phase |
|---|---|---|
| Theoretical complementarity scores | Model-specific + human-specific scoring; empirical validation | Phase 2 → Phase 6 |
| No prototyping or validation | Prototype Priority Matrix + MVA Testing + Integration Testing | Phase 6 |
| Assumed single human actor | Actor Analysis (Step 2.2) | Phase 2 |
| No failure mode analysis for pipeline | FMEA (Step 3.3) + Event Storming (Phase 2.5) | Phase 2.5, 3 |
| No cost-benefit analysis per agent | Cost-Benefit Assessment (Step 4.5) | Phase 4 |
| Human experience wasn't designed | Entire Phase 5 | Phase 5 |
| Didn't test decomposition granularity | Cognitive Load Analysis (Step 1.2) + granularity check | Phase 1 |

| Original Missing Step | Process Fix | Phase |
|---|---|---|
| Empirical validation of decomposition | Expert Validation (Step 1.3) | Phase 1 |
| Agent failure testing | Boundary Stress Testing (Step 4.3) + Adversarial Examples | Phase 4 |
| Pipeline orchestration design | Orchestration Design (Step 3.2) | Phase 3 |
| Human interface design | Entire Phase 5 | Phase 5 |
| Edge case specification | Edge Case Inventory (Step 1.4) | Phase 1 |
| Iterative refinement protocol | Iterative Refinement Protocol (Step 6.4) | Phase 6 |

| Original Improvement | Process Fix | Phase |
|---|---|---|
| Model-specific complementarity scoring | Required in Step 2.1 | Phase 2 |
| Cognitive load analysis | Step 1.2 | Phase 1 |
| Boundary stress tests | Step 4.3 | Phase 4 |
| Adversarial examples in job descriptions | Template field in Step 4.4 | Phase 4 |

---

## Curriculum Applicability for Future's Edge

**Teachable units that generalise beyond any specific workflow:**

| Unit | Core Concept | Applicable Beyond Agents |
|---|---|---|
| **The 5-Class Taxonomy** | Classify any AI component: Extractor, Measurer, Assessor, Generator, Aggregator | ✅ Any AI system |
| **"Constrain the Inverse"** | Authority boundary = inverse of failure mode | ✅ Any system design |
| **Complementarity Allocation Algorithm** | Quantified H/A gap → assignment decision | ✅ Any human-AI collaboration |
| **Type Collision (Bidirectional)** | 6+ cognitive modes ≠ 1 input surface | ✅ Any interface design |
| **Cognitive Load Budgeting** | Human information processing has limits | ✅ Any UX design |
| **Backcasting from Deliverables** | Design from outputs backward | ✅ Any project planning |
| **FMEA for Pipelines** | Failure mode analysis for interconnected systems | ✅ Any system reliability |

---

This process takes what was strong in the original journey (decomposition depth, boundary design, complementarity-driven assignment) and strengthens it with exactly what was missing (validation, failure analysis, human experience, empirical grounding). Every quality gate exists because a specific failure was identified in the review. The process is itself an example of its own principle: *constrain the inverse of the failure mode.*The methodology is documented above in full. Here's what makes it repeatable for *any* task:

**Three scaling levers** ensure you don't over-invest on simple tasks or under-invest on complex ones:

1. **Complexity heuristic** — the table at the top determines which phases you actually run. A single-agent data extraction skips Phases 2.5, 3, and 5 entirely. A complex multi-agent workflow runs all six.

2. **Quality gates, not phase transitions** — you don't move forward by finishing a phase. You move forward by *proving* you've addressed the failure modes that gate was designed to catch. Every checklist item traces to a weakness identified in the review.

3. **Reusable taxonomies that collapse decisions** — the 5-class taxonomy and the "constrain the inverse" principle mean that classifying an agent gives you its boundary, failure mode, and key constraint immediately. That's a decision accelerator, not a creative exercise every time.

**The key structural innovation:** the process is itself an example of its own principle. The quality gates constrain the inverse of each phase's characteristic failure mode — Phase 1 fails by under-decomposing → Gate 1 checks decomposition depth. Phase 3 fails by ignoring failures → Gate 3 checks FMEA completion. Phase 5 fails by ignoring the human → Gate 5 checks cognitive load budgets.

For Future's Edge, the seven teachable units at the bottom are the extractable curriculum content. Each one generalises beyond agentic systems entirely — they're principles of *human-AI collaboration design*, not just *agent design*.

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-04-13T02:42:39* · `glm-5.1:cloud` · `3d9c45b7...`

### Prompt

There is an opportunity for another actor in many tasks. 
Let's add the 'system' as another actor which has different strengths and limitations to both humans and agents.
Deterministic processing may be appropriate for many subtasks in a workflow. 

I also realise I didn't explicitly discuss templates as a tool to aid in improving agents' processing of inputs and production of outputs.

We've also neglected some important elements of my agent design principles: no agent approves its own work, human enrichment etc

What other elements can we explore for this process?

### Response

This is a significant evolution. You've identified three structural gaps and asked me to explore further. Let me work through all of this systematically — first your three additions, then the missing principles from v0.3, then the wider exploration space.

---

# CAWDP v2: From Design-Time Process to Lifecycle Process

**The meta-insight:** CAWDP v1 was a *design-time* process — it produces a specification and then stops. Your three additions, plus the missing v0.3 principles, push it toward a *lifecycle* process — one that governs the system from initial task analysis through runtime operation, temporal evolution, and ongoing governance.

---

## ENHANCEMENT 1: System as Third Actor

This is the most structurally significant change. It transforms CAWDP from a **binary allocation model** (Human/Agent) to a **ternary allocation model** (Human/Agent/System).

### Why This Matters

In the original marking pipeline, several subtasks were assigned to "Agent" that don't need semantic reasoning at all:

| Subtask | Assigned To | Actually Needs |
|---|---|---|
| Schema validation of submissions | Agent (Format Sentinel) | Deterministic code — validate structure against schema |
| Score aggregation calculations | Agent (Grade Finaliser) | Deterministic code — apply weighted formula |
| Conditional routing | Agent (orchestration) | Deterministic code — if X, route to Y |
| File format conversion | Agent | System — convert PDF to text |
| Threshold checking | Agent (Drift Detector component) | System — flag if value > threshold |
| Record assembly | Agent (Record Assembler) | System — merge JSON objects by schema |

Using an LLM for deterministic operations is **expensive, unreliable, and wasteful** — you're paying for semantic reasoning capability that isn't needed and introducing hallucination risk where none should exist.

### The Ternary Capability Profile

**System** (deterministic code/scripts/rules) has a distinct capability fingerprint:

| Dimension | System Score | Why |
|---|---|---|
| **Consistency** | 9 | Perfect determinism — same input, same output, always |
| **Hallucination risk** | 0 | None — no generative capability |
| **Speed** | 9 | Milliseconds for rule application |
| **Scalability** | 9 | Trivially parallelisable |
| **Cost per invocation** | 9 | Near-zero |
| **Parallelisation** | 9 | Embarrassingly parallel |
| **Output consistency** | 9 | Deterministic |
| **Semantic understanding** | 0 | Cannot interpret meaning |
| **Adaptation** | 0 | Only what's explicitly encoded |
| **Judgment** | 0 | Cannot make qualitative decisions |
| **Novelty handling** | 0 | Fails on unseen patterns |
| **Domain expertise** | 0 | Only explicit rules |
| **Context sensitivity** | 0 | No situational awareness |
| **Ethical reasoning** | 0 | Only explicit constraints |
| **Reasoning depth** | 0 | No abstract reasoning |

### New Cognitive Operation Type: Mechanical

Phase 1's cognitive operation classification needs a new member:

| Operation | Description | Best Actor | Example |
|---|---|---|---|
| **Mechanical** | Deterministic transformation, validation, routing | **System** | Schema validation, format conversion, threshold checking, formula application |
| Structural | Mapping form/organisation | Agent or System | Depends on whether interpretation is needed |
| Domain-semantic | Interpreting domain meaning | Agent | Requires semantic understanding |
| Comparative-semantic | Comparing across instances | Agent | Requires judgment |
| Statistical | Numerical pattern detection | Agent (complex) or System (simple) | Depends on complexity |
| Generative | Producing novel text | Agent | Requires semantic capability |
| Evaluative | Making quality judgments | Human or Agent (recommendation) | Depends on authority |
| Synthesis | Consolidating multiple sources | Agent or Human | Depends on nature of consolidation |

**The critical distinction:** Mechanical operations are **provably correct**. Agent operations are **probably correct**. Human operations are **accountably correct**. When a subtask can be mechanical, it SHOULD be mechanical — it removes an entire failure mode category from the pipeline.

### Updated Complementarity Allocation Algorithm

```
For each subtask:
  // SYSTEM FIRST — eliminate hallucination risk where possible
  IF cognitive operation = Mechanical:
    → SYSTEM-LED (deterministic code)
  
  // HUMAN GATE — protect authority domains
  IF any dimension in {Ethical Judgment, Values Alignment, Decision Authority}
     has H-S gap ≥ 6 AND H-A gap ≥ 6:
    → HUMAN-LED
  
  // AGENT ADVANTAGE — semantic at scale
  IF any dimension in {Parallelisation, Output Consistency, Scalability}
     has A-S gap ≥ 5 AND A-H gap ≥ 5:
    → AGENT-LED
  
  // SYSTEM FOR CONSISTENCY — where determinism matters more than semantics
  IF consistency requirement = 9 AND semantic need < 3:
    → SYSTEM-LED
  
  // COLLABORATIVE — everything else
  → DEFAULT TO COLLABORATIVE
     (specify which actors collaborate and in what ratio)
```

**The new decision priority order:** System → Human → Agent → Collaborative. System gets first refusal because it's the cheapest, most reliable, and has zero hallucination risk. Human protects authority domains. Agent handles semantic reasoning at scale. Collaborative handles the genuinely hybrid cases.

### The Ternary Interaction Patterns

Not all three actors interact with each other equally. The key patterns:

| Pattern | Description | Example |
|---|---|---|
| **System → Agent** | System pre-processes; Agent reasons | Schema validation → Claims analysis |
| **Agent → System** | Agent decides; System executes | Agent flags anomaly → System routes to human queue |
| **System → Human** | System presents; Human judges | System computes statistics → Human interprets patterns |
| **Agent → Human** | Agent prepares; Human judges | Agent recommends score → Human finalises |
| **System → Agent → Human** | Full pipeline | System validates → Agent analyses → Human decides |
| **Human → System** | Human triggers; System executes | Human overrides grade → System recalculates aggregate |

### Impact on CAWDP Phases

- **Phase 1:** Add "Mechanical" to cognitive operation classification. Add a System-feasibility check: *Can this subtask be expressed as a deterministic rule?*
- **Phase 2:** Expand complementarity matrix to 3 columns (H/A/S). New allocation algorithm with System-first priority.
- **Phase 2.5:** Event Storming now surfaces **System-enforced events** (e.g., `SchemaValidationPassed`, `ThresholdExceeded`) alongside agent and human events.
- **Phase 3:** Architecture distinguishes between **semantic pipeline segments** (Agent-mediated) and **mechanical pipeline segments** (System-enforced). Orchestration specifies which engine handles which transitions.
- **Phase 4:** Agent job descriptions now specify what System components handle upstream/downstream — agents don't duplicate System work.
- **Phase 5:** Human experience offloads mechanical information to System — humans only see what requires their judgment.

### A New Insight: System as Containment Layer

System components serve a second function beyond efficiency: **failure containment**. When an agent produces output that fails a System-enforced schema validation, the System catches it before it propagates downstream. This is the pipeline's **immune system** — deterministic code that catches semantic errors.

```
Agent Output → System Schema Validation → PASS → downstream
                                  → FAIL → quarantine + human alert
```

This means every agent's output should pass through a System-enforced validation checkpoint before reaching any consumer. The checkpoint enforces the output schema from the job description.

---

## ENHANCEMENT 2: Template Architecture

You've identified a critical gap: CAWDP v1 discusses data *objects* flowing between stages but doesn't specify the **templates** that structure those objects. Templates are the concrete mechanism that resolves type collision — they enforce typed, decomposable outputs instead of prose.

### The Template Taxonomy

Templates serve different functions at different points in the pipeline:

| Template Type | Purpose | Enforced By | Example |
|---|---|---|---|
| **Input Template** | Structures what an agent receives | System (pre-processing) | Structured submission package with typed fields |
| **Output Template** | Structures what an agent produces | System (post-validation) | Claims analysis with: claim, source, confidence, domain tags |
| **Handoff Template** | Standardises data packages between agents/humans | System (routing) | Enhanced Submission Package: format results + claims + anomalies + reflection status |
| **Verification Template** | Structures verification checklists | System (gate enforcement) | Format Sentinel verification: file type ✓, slide count ✓, section headers ✓ |
| **Decision Template** | Structures human decision inputs | System (presentation) | Score recommendation: criterion, evidence, recommendation, confidence, alternatives considered |
| **Feedback Template** | Structures agent-to-human feedback | Agent (generation) | Student feedback: strength evidence, improvement area, specific suggestion, rubric alignment |
| **Escalation Template** | Structures escalation to human | System (routing) | Escalation: agent, issue, evidence, urgency, recommended action |

### Templates as Type Collision Resolution

This directly connects to your bidirectional type collision insight. The 17+ distinct information types you identified (claims, evidence, assumptions, options, criteria, actions, questions, connections, constraints, confidence, perspectives, patterns, gaps, tensions, dependencies, outcomes, provenance) were all encoded as a single output type (prose). Templates are the **structural mechanism** that decomposes these types:

```
Instead of:
  "The student discussed Bitcoin's first-mover advantage and mentioned 
   network effects but didn't provide evidence for centralisation claims 
   and the reflection section seems shallow (confidence: medium)"

Template-enforced output:
  CLAIMS:
    - claim: "BTC has first-mover advantage"
      evidence: "Slide 3, cited Nakamoto"
      confidence: 8/10
    - claim: "Network effects drive adoption"  
      evidence: "Slide 5, no citation"
      confidence: 5/10
  GAPS:
    - gap: "Centralisation claims lack evidence"
      type: evidence_gap
      severity: high
  REFLECTION_ASSESSMENT:
    - depth: shallow
    - evidence: "No double-loop learning indicators"
    - confidence: 6/10
```

### Templates as Agent Constraint Mechanisms

Templates also serve as **input-side type collision resolution**. Instead of giving an agent free-form context, templates constrain what the agent receives:

```
Instead of: "Here's everything about this submission [wall of text]"

Template-enforced input:
  SUBMISSION_PACKAGE:
    format_report: {file_type: pptx, slides: 12, sections: [...]}
    claims: [{claim, source, confidence}, ...]
    anomalies: [{type, description, severity}, ...]
    reflection_status: {depth, evidence, confidence}
```

This is the **input-side** equivalent of your output type collision insight. The agent receives typed, structured input — not an undifferentiated context dump.

### Template Design as a CAWDP Step

This needs to be explicit in the process:

**Phase 3, new Step 3.4: Template Architecture**

*For every data flow identified in the pipeline architecture, design the template that structures it.*

How:
1. For each data object in the architecture, ask: *What types of information does this object carry?*
2. Decompose each type into a typed field (not prose)
3. For each field, specify: type (string/number/boolean/array/object), constraints (required/optional, range, format), provenance (which actor produces it)
4. For each template, specify: validation rules (System-enforced), consumers (which actors read it), mutability (append-only/replaceable/immutable)
5. **Stress-test**: Can this template carry the information the consumer needs? Is any information the consumer needs NOT in the template?

**Phase 4 integration:** Every agent job description now includes an Input Template and Output Template as typed schemas — not prose descriptions.

**Phase 6 integration:** Template validation becomes part of MVA testing — does the agent actually produce output conforming to its output template?

---

## ENHANCEMENT 3: Recovering the Missing v0.3 Principles

CAWDP v1 addressed task decomposition, capability allocation, system architecture, agent design, human experience, and validation. But it's missing several principles from your Agent Design Principles v0.3 that should be **cross-cutting concerns** — not phase-specific steps, but questions asked at EVERY phase.

### Cross-Cutting Concern 1: Verification Independence

**Principle:** No agent approves its own work. The separation of executor and verifier is architecture, not policy.

**v0.3 refinement:** Three-level independence scale:
- **Level 1 (Structural):** Different code path verifies — simple rule checks (System can do this)
- **Level 2 (Semantic):** Different agent verifies — another agent checks reasoning (Agent does this)
- **Level 3 (Authority):** Different actor type verifies — human verifies agent output (Human does this)

**How it cuts across CAWDP:**
- Phase 2: Complementarity analysis assigns verification level per subtask based on risk
- Phase 3: Architecture specifies verification chain for each pipeline segment
- Phase 4: Job descriptions specify who verifies this agent and at what level
- Phase 6: Validation tests whether verification independence is actually enforced

**Quality gate addition:** Every gate now asks: *For each agent in this phase's scope, is the verifier structurally separate from the producer?*

### Cross-Cutting Concern 2: Human Enrichment Assessment

**Principle:** The system has two axes of excellence — output fidelity AND epistemic enrichment. Every layer, every phase, must answer both the fidelity question and the enrichment question.

**How it cuts across CAWDP:**
- Phase 1: Does the task decomposition identify what the human learns by doing this task?
- Phase 2: Does the allocation preserve human learning opportunities? (Don't automate away the learning)
- Phase 3: Does the architecture include feedback that develops human capability?
- Phase 4: Does each agent's output include scaffolding that develops understanding?
- Phase 5: Is the human experience designed to leave the human more capable?
- Phase 6: Is human capability measured alongside system accuracy?

**The enrichment fidelity question per phase:**

| Phase | Fidelity Question | Enrichment Question |
|---|---|---|
| 1 | Is the task decomposed correctly? | Does the decomposition reveal what the human would learn? |
| 2 | Are allocations correct? | Do allocations preserve human learning opportunities? |
| 3 | Does the architecture work? | Does the architecture develop human capability? |
| 4 | Are agents specified correctly? | Do agents scaffold rather than replace human judgment? |
| 5 | Is the interface usable? | Does the interface leave the human more capable? |
| 6 | Does the system work? | Is the human more capable after N runs? |

### Cross-Cutting Concern 3: Epistemic Metadata Contracts

**Principle:** Every output carries not just its content but its epistemic metadata — provenance, confidence, limitations, assumptions, alternatives set aside.

**v0.3 formalisation:** Every agent output includes:

| Metadata Field | Purpose | Example |
|---|---|---|
| **Provenance** | Who produced this, when, from what inputs | Claims Analyst, Wave 3, from Submission Package v2 |
| **Confidence** | How certain is the producer | 7/10 — claim is explicit but evidence is indirect |
| **Limitations** | What this output does NOT cover | Did not assess cross-claim consistency |
| **Assumptions** | What the producer assumed | Assumes standard academic citation conventions |
| **Alternatives set aside** | What other interpretations were considered | Alternative: claim is rhetorical, not substantive — set aside due to citation |
| **What would change this** | What new information would change the output | Direct contradiction from another source would reduce confidence to 3/10 |

**How it cuts across CAWDP:**
- Phase 3: Every data object in the architecture includes epistemic metadata fields
- Phase 4: Every agent job description's output template includes epistemic metadata
- Phase 5: Human experience presents epistemic metadata alongside content — humans calibrate trust
- Phase 6: Validation checks whether agents actually produce epistemic metadata

**Connection to templates:** Epistemic metadata is itself a **template** — the Epistemic Metadata Contract is a standard template that every agent output must include. This is enforced by System (schema validation checks for metadata fields).

### Cross-Cutting Concern 4: Information Boundaries

**Principle:** What an agent cannot read should be structurally impossible, not merely discouraged. Information boundaries are infrastructure-enforced.

**v0.3 refinement:** Replace "forbidden reads" (a declarative constraint) with **information boundaries** (an architectural constraint). An agent structurally cannot access information outside its boundary — it's not a prompt instruction, it's a runtime enforcement.

**How it cuts across CAWDP:**
- Phase 2: Complementarity analysis identifies what each actor needs to know AND what they must NOT know
- Phase 3: Architecture specifies information boundaries as System-enforced (context curtains from your trust platform architecture)
- Phase 4: Job descriptions specify information boundary as a structural constraint, not a prompt instruction
- Phase 6: Validation tests whether information boundaries are actually enforced (can the agent access forbidden data through tool calls?)

**This is where System becomes critical:** Information boundaries are enforced by System code, not by agent prompts. The System mediates all data access — agents never read directly from data stores.

### Cross-Cutting Concern 5: Specification Aging

**Principle:** Agent specifications degrade over time. Task drift, model updates, and changing context all erode specification validity. Without explicit aging mechanisms, specifications become silently stale.

**v0.3 formalisation:**
- **Aging triggers:** Model change, task context change, performance degradation, override rate increase
- **Review cadence:** Time-based (quarterly for stable, monthly for new) AND trigger-based (on any aging trigger)
- **Capability drift tracking:** Does the agent's actual performance match its specification? When they diverge, the specification needs updating

**How it cuts across CAWDP:**
- Phase 6 (major impact): Iterative refinement protocol includes specification aging — agents are reviewed not just for performance but for specification relevance
- Phase 4: Job descriptions include a **specification freshness date** and **aging triggers**
- Cross-cutting: Every quality gate asks — *Are the specifications this gate relies on still current?*

### Cross-Cutting Concern 6: Scaffolding Dependency Index

**Principle:** How much human scaffolding does an agent require to perform correctly? High scaffolding dependency = agent is not truly autonomous = hidden human labor cost.

**Formalization:**

| Scaffolding Level | Description | Index Score |
|---|---|---|
| **Full scaffolding** | Agent cannot operate without human-set context, examples, and constraints | 5 |
| **Heavy scaffolding** | Agent needs examples and constraints but can operate once set up | 4 |
| **Moderate scaffolding** | Agent needs constraints but can discover its own approach | 3 |
| **Light scaffolding** | Agent needs goal clarification only | 2 |
| **Autonomous** | Agent operates from specification alone | 1 |

**How it cuts across CAWDP:**
- Phase 2: Scaffolding dependency is a factor in allocation — high dependency agents are more expensive than they appear
- Phase 4: Job descriptions include scaffolding dependency index — this is a hidden cost
- Phase 5: Human experience accounts for scaffolding labor — how much human time is spent setting up agents?
- Phase 6: Validation measures actual scaffolding cost vs. estimated

**The connection to Human Enrichment:** The scaffolding dependency index also applies to the human side — how much scaffolding does the HUMAN need from the system? Progressive human empowerment means the human's scaffolding dependency should DECREASE over time.

### Cross-Cutting Concern 7: Cost Budget

**Principle:** Every agent has a cost budget. The pipeline has a total cost budget. Cost is a first-class design constraint, not an afterthought.

**v0.3 formalisation:**
- **Per-agent cost budget:** Maximum acceptable cost per invocation (token cost + tool cost + infrastructure cost)
- **Pipeline cost budget:** Maximum acceptable cost per unit processed (e.g., per student, per document)
- **Cost-quality trade-off:** Is the marginal cost of adding an agent justified by the marginal quality improvement?
- **Cost monitoring:** Actual cost tracked against budget — overruns trigger review

**How it cuts across CAWDP:**
- Phase 2: Cost is a factor in allocation — System < Agent < Human on cost per unit
- Phase 4: Every job description includes a cost budget
- Phase 5: Human time is costed alongside agent cost
- Phase 6: Validation includes cost tracking — does the pipeline stay within budget?

### Cross-Cutting Concern 8: Assured Audit Trail

**Principle:** Every agent action creates a traceable, attributed, timestamped record. But "immutable" is aspirational — v0.3 replaces it with three assurance levels.

**v0.3 refinement:**
- **Level 1 (Logged):** Action recorded in application log — tamperable by system admin, suitable for debugging
- **Level 2 (Assured):** Action recorded in append-only store — tamper-evident, suitable for compliance
- **Level 3 (Verified):** Action recorded with cryptographic proof — tamper-proof, suitable for legal/financial

**How it cuts across CAWDP:**
- Phase 3: Architecture specifies audit assurance level per agent and per action type
- Phase 4: Job descriptions specify audit level for the agent's actions
- Phase 5: Human experience shows audit trail when the human needs to verify agent reasoning
- Phase 6: Validation tests audit trail completeness and assurance level

---

## FURTHER EXPLORATION: Elements You Haven't Raised (But Should Consider)

These emerge from the design space you've opened up. I've organised them by type.

### A. Runtime & Operational Concerns

**9. Progressive Autonomy**

Agents don't start with full authority. They earn it.

| Autonomy Level | Agent Can | Human Must |
|---|---|---|
| **Shadow mode** | Produce outputs, but none are used | Review all outputs against manual baseline |
| **Advisory mode** | Produce recommendations with full reasoning | Approve before action |
| **Supervised mode** | Act within bounded parameters | Review exceptions and overrides |
| **Autonomous mode** | Act within specification | Review only escalations |

The autonomy level is a function of: (1) accuracy on validation data, (2) override rate, (3) specification stability, (4) consequence severity. Agents handling irreversible actions never exceed supervised mode.

**CAWDP integration:** Phase 4 job descriptions include **initial autonomy level** and **advancement criteria**. Phase 6 validation measures performance against advancement thresholds.

**10. Fallback Model Tiers**

What happens when the primary model is unavailable or degraded?

| Tier | Model | When Used | Cost | Quality |
|---|---|---|---|---|
| **Tier 1** | Primary (e.g., Claude 3.5) | Normal operation | Full | Full |
| **Tier 2** | Secondary (e.g., GPT-4) | Primary unavailable | Full | Near-full |
| **Tier 3** | Local model | API unavailable | Free | Reduced |
| **Tier 4** | System fallback | No model available | Zero | Rules only |

Each agent should have a fallback specification: what does it produce when operating at Tier 3? Does it still meet minimum quality? Does it flag the reduced confidence?

**CAWDP integration:** Phase 4 job descriptions include fallback behavior per tier. Phase 3 architecture specifies which agents can degrade gracefully and which must halt.

**11. Pipeline Health Monitoring**

Your v0.3 principles include two pipeline health metrics (IDS and UPR) that have no home in CAWDP v1:

- **Information Diversity Score (IDS):** How semantically varied are messages between agents? Declining IDS = convergent thinking = pipeline homogenisation risk
- **Unnecessary Path Ratio (UPR):** How much reasoning was wasted? High UPR = over-specified pipeline

These are **leading indicators** — they predict quality degradation before it shows in output accuracy.

**CAWDP integration:** Phase 6 refinement protocol includes IDS and UPR as monitoring metrics. Declining IDS or rising UPR triggers a pipeline review, not just an agent review.

### B. Temporal & Evolutionary Concerns

**12. Temporal Dynamics (Cross-Cutting)**

CAWDP v1 designs the pipeline at a point in time. But pipelines evolve:

| Temporal Concern | Description | CAWDP Phase |
|---|---|---|
| **Specification aging** | Specs become stale | Cross-cutting (CC5) |
| **Model drift** | Model updates change agent behavior | Phase 6 monitoring |
| **Task evolution** | The task itself changes over time | Phase 1 re-validation trigger |
| **Human skill growth** | Humans become more capable (enrichment) | Phase 5 & 6 measurement |
| **Agent capability growth** | Agents improve through pattern extraction | Phase 6 improvement loops |
| **Trust accumulation** | Agents earn trust through verified performance | Progressive Autonomy |

**The key insight:** Temporal dynamics should be a **cross-cutting concern** with explicit review triggers, not just "we'll improve it later."

### C. Security & Trust Concerns

**13. Reversibility Classification**

From your Safety layer: before any action, classify it as:
- **Read-only:** No side effects (safe to retry, safe to automate)
- **Reversible:** Can be undone (automate with logging, human can override)
- **Irreversible:** Cannot be undone (human presence required structurally)

**CAWDP integration:** Phase 2 classifies every subtask's action reversibility. Phase 4 job descriptions include reversibility class. Phase 3 architecture ensures irreversible actions have System-enforced human gates.

**14. Coalition Formation Intelligence**

Your v0.3 ecosystem layer specifies that agents should be composed for **epistemic complementarity**, not just functional role coverage. This is absent from CAWDP v1.

**Example:** Two agents with the same cognitive orientation (both critical, both procedural) will produce convergent outputs. Two agents with complementary orientations (one critical, one optimistic) produce a richer option space.

**CAWDP integration:** Phase 4 agent roster design includes a **cognitive orientation diversity check** — are the agents in this wave composed for epistemic complementarity? Phase 6 monitors IDS as the metric for whether composition is working.

### D. Design Process Concerns

**15. Decomposition Depth Guidance**

CAWDP v1 says "decompose until 1-2 cognitive operations per subtask" but doesn't provide decision criteria for when to stop decomposing. The risk is both under-decomposition (monolith agents) and over-decomposition (trivial agents that cost more than they add).

**Decision framework:**

```
STOP decomposing when:
  ✓ 1-2 cognitive operations per subtask
  ✓ The subtask has a single clear authority boundary
  ✓ A single verification check can validate the output
  ✓ The subtask's output is consumed by ≥1 other actor
  
CONSIDER further decomposition when:
  ⚠ >2 cognitive operations bundled
  ⚠ Authority boundary is ambiguous ("never judge OR interpret")
  ⚠ Verification requires multiple independent checks
  ⚠ Different failure modes within one subtask

ALWAYS decompose when:
  ✗ >3 cognitive operations bundled
  ✗ Agent would need to switch cognitive modes mid-task
  ✗ Different operations have different hallucination risk levels
```

**16. The "Should This Be a Team?" Decision**

Agno gives you three composition primitives: single Agent, Team, Workflow. When does a task need each?

| Primitive | When to Use | Signal |
|---|---|---|
| **Agent** | Single cognitive operation, single authority boundary | One "never" constraint suffices |
| **Team** | Multiple operations need coordination, shared context | Multiple authority boundaries but shared data |
| **Workflow** | Sequential/parallel stages with data handoffs | Different stages have different actor types |

**CAWDP integration:** Phase 3 architecture includes a **composition decision** for each pipeline segment — is this an agent, a team, or a workflow?

---

## The Complete Cross-Cutting Concern Map

Here's every element mapped to where it lives in CAWDP and whether it's a step, a cross-cutting concern, or both:

| # | Element | Type | Primary Phase(s) | Cross-Cutting? |
|---|---|---|---|---|
| 1 | System as Third Actor | Structural change | 2, 3, 4 | ✅ Affects all phases |
| 2 | Template Architecture | New step | 3, 4 | ✅ Templates flow through all phases |
| 3 | Verification Independence | Cross-cutting | All | ✅ |
| 4 | Human Enrichment Assessment | Cross-cutting | All | ✅ |
| 5 | Epistemic Metadata Contracts | Cross-cutting | All | ✅ (enabled by templates) |
| 6 | Information Boundaries | Cross-cutting | 2, 3, 4 | ✅ |
| 7 | Specification Aging | Cross-cutting | 4, 6 | ✅ |
| 8 | Scaffolding Dependency Index | Cross-cutting | 2, 4, 5 | ✅ |
| 9 | Cost Budget | Cross-cutting | 2, 4, 6 | ✅ |
| 10 | Assured Audit Trail | Cross-cutting | 3, 4, 6 | ✅ |
| 11 | Progressive Autonomy | New concept | 4, 6 | ⚠️ Runtime concern |
| 12 | Fallback Model Tiers | New concept | 3, 4 | ⚠️ Operational concern |
| 13 | Pipeline Health Monitoring | New step | 6 | ⚠️ Monitoring concern |
| 14 | Temporal Dynamics | Cross-cutting | All | ✅ |
| 15 | Reversibility Classification | Cross-cutting | 2, 4 | ✅ |
| 16 | Coalition Formation Intelligence | New step | 4 | ⚠️ Agent composition concern |
| 17 | Decomposition Depth Guidance | Enhancement | 1 | ❌ Phase-specific |
| 18 | Composition Decision (Agent/Team/Workflow) | New step | 3 | ❌ Phase-specific |

---

## The Updated Quality Gate Framework

Every quality gate now has **three layers of checks:**

1. **Fidelity checks** (does the system produce correct outputs?)
2. **Enrichment checks** (does the system develop human capability?)
3. **Cross-cutting checks** (are all cross-cutting concerns addressed?)

Example for Gate 4 (Agent Design Complete):

```
FIDELITY CHECKS:
  ☐ Every agent classified in 5-class taxonomy (or identified as System component)
  ☐ Authority boundary = inverse of failure mode
  ☐ Boundary stress tests designed
  ☐ Job descriptions complete
  ☐ Cost-benefit assessment: no unnecessary agents
  ☐ Input/output templates specified as typed schemas

ENRICHMENT CHECKS:
  ☐ Every agent's output scaffolds human understanding, not replaces judgment
  ☐ Human learning opportunities preserved in allocation decisions
  ☐ Scaffolding reduces over time (not permanent dependency)

CROSS-CUTTING CHECKS:
  ☐ Verification independence: every agent has a separate verifier (level specified)
  ☐ Information boundaries: structurally enforced, not prompt-only
  ☐ Epistemic metadata: every output template includes provenance, confidence, limitations
  ☐ Scaffolding dependency index: documented per agent
  ☐ Cost budget: specified per agent and per pipeline unit
  ☐ Audit trail: assurance level specified per agent
  ☐ Specification freshness date and aging triggers documented
  ☐ Reversibility class assigned per agent's actions
  ☐ Progressive autonomy: initial level and advancement criteria specified
  ☐ Fallback behavior: specified for degraded model tiers
```

---

## The Key Insight: CAWDP v2 is a Governance Framework, Not Just a Design Process

CAWDP v1's weakness was clear from the review: **strong on design, weak on validation and human experience.** The three additions you've identified, plus the recovered v0.3 principles, push CAWDP toward something more ambitious:

| Aspect | CAWDP v1 | CAWDP v2 |
|---|---|---|
| **Scope** | Design-time | Lifecycle (design → runtime → evolution) |
| **Actor model** | Binary (Human/Agent) | Ternary (Human/Agent/System) |
| **Output structure** | Prose descriptions | Template-enforced typed schemas |
| **Verification** | Assumed separate | Explicitly specified (3-level independence) |
| **Enrichment** | Not assessed | Assessed at every phase |
| **Boundaries** | Prompt instructions | Infrastructure-enforced (System) |
| **Cost** | Afterthought | First-class budget constraint |
| **Audit** | Assumed immutable | Three assurance levels |
| **Temporal** | Point-in-time | Explicit aging and drift tracking |
| **Autonomy** | Full or nothing | Progressive (earned through evidence) |

The deepest structural change is the **System as third actor**. It transforms CAWDP from a process that designs *agent systems* into a process that designs *human-agent-system societies* — where deterministic code serves as both the mechanical backbone AND the enforcement layer for boundaries, templates, verification, and audit. System is not just efficient — it's the **trust infrastructure** that makes Human-Agent collaboration governable.The three enhancements you've identified, plus the wider exploration, reveal something fundamental: **CAWDP v1 designed agents. CAWDP v2 governs a society of actors.**

The single most structurally significant change is the **System as third actor**. It does three things simultaneously:

1. **Efficiency** — stops using LLMs for deterministic work (schema validation, routing, formula application)
2. **Reliability** — introduces a hallucination-free actor class that serves as the pipeline's immune system
3. **Enforceability** — makes every boundary, template, and verification check structurally enforced rather than prompt-instructed

The second most significant is **templates as the type collision mechanism** — they're the concrete answer to the bidirectional type collision problem you identified. Input templates resolve input-side type collision. Output templates resolve output-side type collision. Handoff templates resolve inter-agent type collision. Without templates, all your carefully designed typed schemas collapse back into prose at runtime.

And the eight cross-cutting concerns from v0.3 transform CAWDP from a *process you run once* into a *governance framework you live inside*. Every quality gate now asks not just "does it work?" but "does it work AND does it leave the human more capable AND are all the structural guarantees in place?"

For Future's Edge, the teachable extract from this round is: **ternary allocation, template-enforced outputs, and cross-cutting quality gates** are three design principles that generalise beyond any specific framework.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-13T03:30:50* · `glm-5.1:cloud` · `997a938f...`

### Prompt

I have a note on the statement, "Progressive human empowerment means the human's scaffolding dependency should DECREASE over time."
I would argue that this is an oversimplification of human empowerment. I see it as giving humans freedom to be creative and find new solutions from existing challenges. That using the systems helps humans find better methods. We shouldn't expect humans to become better at what agents or systems do - that is unlikely.

your last response highlighted for me that testing should be an element of this framework. 
Part of the process should be defining a test plan and tests to be run and targets to test against.

### Response

You're making two important corrections. Let me work through both carefully because they change fundamental assumptions.

---

## Reframing Human Enrichment: Not Independence, Creative Freedom

You've identified a subtle but consequential error in my framing. Let me surface it explicitly:

**The flawed assumption:** Human enrichment means the human becomes less dependent on the system over time. The scaffolding reduces. The human can eventually do it themselves.

**Why this is wrong:** It positions the human as an *apprentice learning to replace the master*. The end state is the human doing what the agent does, just independently. This is not enrichment — it's automation in reverse. Humans will not get better at doing what agents do. Agents are better at consistency, scale, speed, and deterministic processing. Expecting humans to develop those capabilities is misdirected effort.

**Your reframing:** Human enrichment means the system **expands the human's creative freedom**. The human uses the system to find new methods, discover better approaches, and address challenges they couldn't tackle alone. The system is not a crutch to be removed — it's a platform for capabilities that only humans possess.

This reframing changes several things in CAWDP:

### The Enrichment Question, Corrected

| Phase | Flawed Enrichment Question | Corrected Enrichment Question |
|---|---|---|
| 1 | Does the decomposition reveal what the human would learn? | Does the decomposition preserve space for human creative judgment? |
| 2 | Do allocations preserve human learning opportunities? | Do allocations free the human from mechanical work TO BE creative? |
| 3 | Does the architecture develop human capability? | Does the architecture give the human room to discover new methods? |
| 4 | Do agents scaffold rather than replace human judgment? | Do agents handle the routine so the human can do the novel? |
| 5 | Does the interface leave the human more capable? | Does the interface give the human freedom to explore and create? |
| 6 | Is the human more capable after N runs? | Is the human finding solutions they wouldn't have found alone? |

### The Scaffolding Dependency Index, Corrected

The original index measured how much support the agent needs from the human. But the enrichment axis should measure something different:

**System Empowerment Index** — how much creative freedom does the system give the human?

| Level | Description | What the Human Experiences |
|---|---|---|
| **Constraining** | System determines what the human sees and does | Human is a rubber stamp on system recommendations |
| **Informing** | System provides information; human decides | Human has information but limited room to explore |
| **Enabling** | System handles mechanical work; human focuses on judgment | Human freed from routine to do creative work |
| **Amplifying** | System surfaces options the human wouldn't have seen | Human discovers methods and solutions beyond their solo capability |
| **Liberating** | System creates entirely new possibility spaces | Human achieves outcomes that were impossible without the system |

The direction of improvement is **upward through this scale**, not toward "less dependency." A human at Level 4 (Amplifying) is not dependent on the system — they're *enabled by it* to do things they couldn't do alone. The system isn't a crutch; it's a creative catalyst.

### The Enrichment Fidelity Question, Corrected

Every phase now asks two questions:

| Axis | Question | Direction |
|---|---|---|
| **Fidelity** | Does the system produce correct outputs? | Accuracy, consistency, completeness |
| **Creative Freedom** | Does the system expand or contract what the human can achieve? | Novelty, discovery, possibility space |

The goal is not "human can do the task without the system." The goal is "human can achieve things WITH the system that were impossible without it."

This also reframes **what we test for enrichment** — we don't test "can the human do it alone now?" We test "did the human discover a better method? Did they find a solution they wouldn't have found? Did they have room to be creative rather than just approving system outputs?"

---

## Testing as a First-Class Process Element

You're absolutely right. Testing is not a Phase 6 afterthought — it's defined *alongside* the design, not after it. This is the "shift left" principle: **test plans are design artifacts, not validation afterthoughts.**

The current CAWDP structure relegates testing to Phase 6, which creates the same problem as the original process review identified: a process strong on design, weak on validation. The correction is to make testing a **parallel track** that runs alongside design from Phase 1 onward.

### The Principle: Every Design Decision Generates a Test

| Design Decision | Test It Generates |
|---|---|
| Cognitive operation classification | "Does this subtask actually require this cognitive operation? Test with an example that needs a different operation." |
| Complementarity allocation (H/A/S) | "For this allocation, does the assigned actor actually perform better than the alternatives? Test with benchmark cases." |
| Authority boundary ("never interpret") | "What input would tempt the agent to interpret? Test with adversarial examples." |
| Output template schema | "Does the agent actually produce output conforming to this schema? Test with production data." |
| Human decision point | "Can the human make the decision with the information provided? Test with realistic cognitive load." |
| Epistemic metadata contract | "Does the agent actually provide accurate confidence scores? Test with known-difficulty inputs." |
| Verification independence | "Can the verifier actually operate independently? Test by corrupting the producer's output." |
| Information boundary | "Can the agent actually not access forbidden data? Test with prompt injection attempts." |

### The Test Plan as a Design Artifact

Every phase should produce test specifications alongside its design artifacts:

**Phase 1 Test Plan:** *Decomposition Validation Tests*
- Expert validation tests: "Do domain experts recognise these subtasks?"
- Cognitive operation tests: "Can we classify example tasks into these categories unambiguously?"
- Edge case tests: "What happens with empty/corrupted/adversarial inputs?"
- Decomposition granularity tests: "Is each subtask independently verifiable? Can we write a pass/fail criterion for each?"

**Phase 2 Test Plan:** *Allocation Validation Tests*
- Complementarity gap tests: "For subtasks with large H-S gaps (e.g., ethical judgment), does the human actually perform better? Test with benchmark cases."
- System feasibility tests: "Can this subtask actually be expressed as a deterministic rule? Test with representative inputs."
- Allocation accuracy tests: "For each allocation, does the assigned actor produce measurably better outcomes than alternatives?"

**Phase 2.5 Test Plan:** *Event Storm Validation Tests*
- Missing event tests: "Walk through a realistic scenario end-to-end. Does every event in the storm map actually occur?"
- Trigger condition tests: "Does each trigger fire correctly? Test with inputs that should and shouldn't trigger."
- Fallback tests: "When a trigger fails, does the fallback actually work?"

**Phase 3 Test Plan:** *Architecture Validation Tests*
- Data flow tests: "Does every consumer actually receive the data it needs from a producer? Test with sample data."
- Orchestration tests: "Does Wave 2 actually start after Wave 1 completes? Test with timing and failure scenarios."
- FMEA tests: "For each failure mode identified, does the recovery path actually work?"
- Template validation tests: "Does every output conform to its template schema? Test with System-enforced validation."

**Phase 4 Test Plan:** *Agent Validation Tests*
- Boundary adherence tests: "Does the agent respect its authority boundary on stress inputs?"
- Failure mode tests: "What inputs trigger the agent's characteristic failure mode?"
- Epistemic metadata tests: "Does the agent provide accurate confidence, provenance, limitations?"
- Cost tests: "Does the agent stay within its cost budget on representative inputs?"
- Fallback behavior tests: "How does the agent perform at each fallback model tier?"

**Phase 5 Test Plan:** *Human Experience Validation Tests*
- Cognitive load tests: "Can the human complete their decision points within the cognitive load budget?"
- Creative freedom tests: "Does the interface give the human room to explore, or just approve?"
- Override tests: "Does the human override mechanism work as designed?"
- Enrichment tests: "Does the human discover better methods through using the system?"

**Phase 6 Test Plan:** *Integration & Evolution Tests*
- End-to-end pipeline tests: "Does the full pipeline produce correct deliverables on realistic inputs?"
- Progressive autonomy tests: "Can agents advance autonomy levels based on measured performance?"
- Specification aging tests: "After N runs, have any specifications become stale?"
- Cost tests: "Does the total pipeline cost stay within budget?"

### Test Specification Template

For every test, a standard template ensures completeness:

```
TEST SPECIFICATION
==================
Test ID: [Phase].[Number].[Sequence]
Test Name: [Descriptive name]
Source: [Which design decision does this test validate?]

PRECONDITIONS
  - What must be true before this test runs?
  - What data, agents, or conditions must be in place?

TEST PROCEDURE
  - Step-by-step actions
  - Inputs to provide
  - Conditions to simulate

EXPECTED RESULT
  - What should happen if the design is correct?
  - Pass criteria (measurable)

FAILURE INDICATORS
  - What specific outcomes indicate a design flaw?
  - What does each failure mode mean?

SEVERITY
  - Blocking: must fix before proceeding
  - Warning: should fix, can proceed with documented risk
  - Informational: useful data, not a blocker

LINKED DECISION
  - Which CAWDP phase and step produced the design decision being tested?
  - Which quality gate does this test support?
```

### Test Targets: Defining Success Criteria

Every test needs a target — not just "does it work?" but "how well does it work?" Targets should be:

| Metric Type | Example Target | Source |
|---|---|---|
| **Accuracy** | Claims extraction accuracy ≥ 85% on benchmark set | Complementarity gap analysis |
| **Boundary adherence** | Agent violates authority boundary ≤ 2% of inputs | Boundary stress testing |
| **Template compliance** | Output schema validation passes ≥ 99% of invocations | Template architecture |
| **Cognitive load** | Human completes decision point in ≤ 5 minutes | Human experience design |
| **Creative freedom** | Human discovers ≥ 1 new approach per 10 sessions | Enrichment assessment |
| **Cost** | Pipeline cost per unit ≤ $X | Cost budget |
| **Epistemic honesty** | Confidence scores correlate ≥ 0.7 with actual accuracy | Epistemic metadata contract |
| **System throughput** | Mechanical subtasks process in ≤ 2 seconds | System allocation |
| **Audit completeness** | 100% of actions logged at specified assurance level | Assured audit trail |

### Integration into Quality Gates

Every quality gate now includes a test readiness check:

**Gate 1 (Task Intelligence):**
- ☐ Decomposition validation tests defined
- ☐ Edge case tests defined
- ☐ Expert validation test results available

**Gate 2 (Capability Allocation):**
- ☐ Complementarity gap tests defined with targets
- ☐ System feasibility tests defined for all mechanical subtasks
- ☐ Allocation accuracy test targets set

**Gate 3 (System Architecture):**
- ☐ Data flow tests defined
- ☐ Orchestration trigger tests defined
- ☐ FMEA recovery path tests defined
- ☐ Template schema validation tests defined

**Gate 4 (Agent Design):**
- ☐ Boundary adherence tests defined with adversarial examples
- ☐ Failure mode tests defined for each agent class
- ☐ Epistemic metadata accuracy tests defined
- ☐ Cost budget tests defined
- ☐ Fallback behavior tests defined

**Gate 5 (Human Experience):**
- ☐ Cognitive load tests defined with time targets
- ☐ Creative freedom tests defined with discovery targets
- ☐ Override mechanism tests defined

**Gate 6 (Validation & Iteration):**
- ☐ End-to-end pipeline tests defined
- ☐ Progressive autonomy advancement criteria defined
- ☐ Specification aging triggers defined
- ☐ Pipeline health monitoring targets (IDS, UPR) defined

---

## The Structural Change to CAWDP

The testing integration changes CAWDP from:

```
Phase 1 → Phase 2 → ... → Phase 6 (which includes testing)
```

To:

```
Phase 1 ─── + Test Plan 1
Phase 2 ─── + Test Plan 2
Phase 2.5 ─ + Test Plan 2.5
Phase 3 ─── + Test Plan 3
Phase 4 ─── + Test Plan 4
Phase 5 ─── + Test Plan 5
Phase 6 ─── + Test Plan 6 (integration + evolution)

Each quality gate: Design artifacts + Test specifications + Target thresholds
```

Phase 6 shifts from "designing tests" to **running the tests that were already designed** — execution, not conception. The test plans are created alongside the design decisions they validate, because the person who makes a design decision is best positioned to define what would prove it wrong.

---

## Summary of Both Corrections

| Original Element | Flaw | Correction |
|---|---|---|
| Scaffolding Dependency Index | Measured human dependency reduction | **System Empowerment Index** — measures creative freedom expansion |
| Enrichment question | "Is the human more capable after?" | **"Is the human finding solutions they wouldn't find alone?"** |
| Enrichment goal | Human becomes independent | **Human becomes more creative and discovers better methods** |
| Testing | Phase 6 afterthought | **Parallel track — test plans designed alongside design decisions** |
| Test artifacts | Not in CAWDP | **Test specification per design decision, with targets and pass criteria** |
| Quality gates | Design checks only | **Design checks + test readiness checks + target thresholds** |

The deepest insight in your correction: **humans should not aspire to do what systems do.** They should use systems to do what only humans can — create, discover, judge, and find new paths. The system is the platform for that freedom, not the training wheels to be removed.Both corrections are now integrated into the CAWDP v2 record. The enrichment reframing is particularly important because it changes the *direction* of an entire measurement axis — from "are humans becoming less dependent?" to "are humans achieving more than they could alone?" That's a fundamentally different design goal, and it changes what you optimise for at every phase.

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-04-13T03:45:28* · `glm-5.1:cloud` · `55dde93c...`

### Prompt

Great work.

Rewrite the CAWDP to integrate all of the above.

### Response

# Complementarity-Driven Agentic Workflow Design Process (CAWDP) v2

*A governance framework for designing human-agent-system collaboration — from task analysis through runtime evolution.*

---

## Core Premise

Before any design decision, three commitments must be explicit:

1. **The fundamental unit of collaboration is the artefact, not the conversation.** Outputs should be tangible, persistent, manipulable objects — not transient chat exchanges. Templates enforce this structurally.

2. **The highest-value role of agents is judgment preparation, not answer generation.** Agents prepare structured decision inputs for human judgment. Humans make the judgment. The system enforces the boundary.

3. **The system exists to expand human creative freedom, not to make humans independent of it.** Enrichment means humans discover better methods and achieve outcomes impossible alone — not that they learn to do what agents do.

These three commitments shape every phase, every quality gate, and every cross-cutting concern.

---

## Process Overview

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    6 PHASES + 5 QUALITY GATES                             │
│                     + 8 CROSS-CUTTING CONCERNS                            │
│                     + PARALLEL TEST TRACK                                 │
│                                                                           │
│  PHASE 1              PHASE 2              PHASE 2.5                     │
│  TASK INTELLIGENCE    CAPABILITY ALLOCATION  EVENT STORMING              │
│       │                    │                     │                        │
│  [GATE 1]            [GATE 2]                                         │
│                                                                           │
│  PHASE 3              PHASE 4              PHASE 5              PHASE 6   │
│  SYSTEM ARCHITECTURE  AGENT DESIGN         HUMAN EXPERIENCE  VALIDATION  │
│       │                    │                    │                  │        │
│  [GATE 3]            [GATE 4]          [GATE 5]        (continuous)     │
└──────────────────────────────────────────────────────────────────────────┘

TEST TRACK (parallel):
  Test Plan 1  →  Test Plan 2  →  Test Plan 2.5  →  Test Plan 3  →  Test Plan 4  →  Test Plan 5  →  Test Plan 6
```

**Scaling heuristic — not every phase is needed for every task:**

| Task Complexity | Phases Required | Typical Examples |
|---|---|---|
| **Single-agent, no human loop** | 1 → 2 → 4 | Data extraction, summarisation, translation |
| **Single-agent + human review** | 1 → 2 → 4 → 5 | Draft generation with human sign-off |
| **Multi-agent, linear pipeline** | 1 → 2 → 3 → 4 → 5 | Sequential processing with handoffs |
| **Multi-agent, branching + human decisions** | 1 → 2 → 2.5 → 3 → 4 → 5 → 6 | Complex workflows with failure recovery |

**Three-actor model:** Every subtask is allocated to one of three actors — Human, Agent, or System — based on complementarity. System (deterministic code) gets first refusal because it's cheapest, most reliable, and has zero hallucination risk.

---

## The Ternary Allocation Model

CAWDP v2 operates with **three actors**, not two:

| Actor | Characteristic Operations | Hallucination Risk | Cost | Speed |
|---|---|---|---|---|
| **Human** | Ethical judgment, values alignment, creative discovery, accountability | N/A | High | Low |
| **Agent** | Semantic reasoning, pattern detection, generative synthesis, parallel analysis | Moderate-High | Moderate | Moderate |
| **System** | Deterministic transformation, validation, routing, calculation, enforcement | Zero | Near-zero | High |

**The System actor serves a dual role:** it handles mechanical operations efficiently AND it enforces boundaries, templates, verification, and audit — the trust infrastructure that makes Human-Agent collaboration governable.

**Six ternary interaction patterns:**

| Pattern | Description | Example |
|---|---|---|
| **System → Agent** | System pre-processes; Agent reasons | Schema validation → Claims analysis |
| **Agent → System** | Agent decides; System executes | Agent flags anomaly → System routes to human queue |
| **System → Human** | System presents; Human judges | System computes statistics → Human interprets patterns |
| **Agent → Human** | Agent prepares; Human judges | Agent recommends score → Human finalises |
| **System → Agent → Human** | Full pipeline | System validates → Agent analyses → Human decides |
| **Human → System** | Human triggers; System executes | Human overrides grade → System recalculates aggregate |

**Allocation priority order:** System → Human → Agent → Collaborative. System gets first refusal — if a subtask can be expressed as a deterministic rule, it should be.

---

## The 5-Class Agent Taxonomy

Every Agent actor falls into one of five classes. Each class carries its authority boundary and failure mode:

| Class | Authority Boundary | Primary Failure Mode | Hallucination Risk | Key Constraint |
|---|---|---|---|---|
| **Extractor** | Never judge | Hallucination | High | Only extract, never interpret |
| **Measurer** | Never interpret | Noise-as-signal | Low | Present data, not meaning |
| **Assessor** | Never finalise | Overconfidence | Medium | Recommend, never decide |
| **Generator** | Never be vague | Fabrication | High | Every claim must cite evidence |
| **Aggregator** | Never add | Omission | Low | Consolidate only, no new analysis |

**The design pattern:** The authority boundary is the inverse of the failure mode. When you encounter a new agent, first ask "what class is it?" — the boundary and failure mode follow immediately.

System components have no class. They have no authority boundary because they have no judgment. They have no failure mode because they are deterministic — they either execute correctly or fail explicitly.

---

## Cross-Cutting Concerns

These eight concerns apply to **every phase**. They are not phase-specific steps — they are questions asked at every quality gate.

### CC-1: Verification Independence

**Principle:** No agent approves its own work. The separation of executor and verifier is architecture, not policy.

**Three-level independence scale:**

| Level | Verifier | When Appropriate | Example |
|---|---|---|---|
| **Level 1: Structural** | System (deterministic code) | Output schema validation, format checking | System validates that every claim has a source field |
| **Level 2: Semantic** | Different Agent | Reasoning verification, alternative perspective | Second agent reviews Claims Analyst's extraction accuracy |
| **Level 3: Authority** | Human | Final judgment, ethical decision, accountability | Human finalises the score the Assessor recommended |

**Quality gate question:** *For each agent in this phase's scope, is the verifier structurally separate from the producer? At what independence level?*

### CC-2: Human Enrichment Assessment

**Principle:** The system has two axes of excellence — output fidelity AND creative freedom expansion. Every phase must answer both the fidelity question and the enrichment question.

**The System Empowerment Index** (replaces Scaffolding Dependency Index):

| Level | What the Human Experiences | Description |
|---|---|---|
| **Constraining** | Human is a rubber stamp on system recommendations | System determines what the human sees and does |
| **Informing** | Human has information but limited room to explore | System provides data; human decides within system's framing |
| **Enabling** | Human freed from routine to do creative work | System handles mechanical work; human focuses on judgment |
| **Amplifying** | Human discovers methods they wouldn't find alone | System surfaces options the human hadn't considered |
| **Liberating** | Human achieves outcomes impossible without the system | System creates entirely new possibility spaces |

**The enrichment question is NOT "can the human do it alone?" It IS "does the system expand what the human can achieve?"** Humans should not aspire to do what systems do. They should use systems to do what only humans can — create, discover, judge, find new paths.

**Quality gate question:** *Does this phase's design expand or contract what the human can achieve? Where does it land on the System Empowerment Index?*

### CC-3: Epistemic Metadata Contracts

**Principle:** Every output carries not just its content but its epistemic metadata — provenance, confidence, limitations, assumptions, alternatives, and what would change the conclusion.

**Six required fields on every agent output:**

| Field | Purpose | Example |
|---|---|---|
| **Provenance** | Who produced this, when, from what inputs | Claims Analyst, Wave 3, Submission Package v2 |
| **Confidence** | How certain is the producer (1-10) | 7 — claim is explicit but evidence is indirect |
| **Limitations** | What this output does NOT cover | Did not assess cross-claim consistency |
| **Assumptions** | What the producer assumed | Assumes standard academic citation conventions |
| **Alternatives set aside** | What other interpretations were considered | Alternative: claim is rhetorical, not substantive |
| **What would change this** | What new information would change the output | Direct contradiction from another source would reduce confidence to 3 |

**Enforcement:** Templates (CC-related) enforce this structurally. System validates that every agent output includes all six fields.

**Quality gate question:** *Does every output template include all six epistemic metadata fields?*

### CC-4: Information Boundaries

**Principle:** What an actor cannot read should be structurally impossible, not merely discouraged. Information boundaries are enforced by System infrastructure, not by agent prompts.

**Architecture:** System mediates all data access. Actors never read directly from data stores. The boundary is a context curtain — an actor can only see what is explicitly passed to it through the orchestration layer.

**Specification in CAWDP:**
- Phase 2: Identify what each actor needs to know AND what they must NOT know
- Phase 3: Architecture specifies information boundaries as System-enforced
- Phase 4: Job descriptions specify information boundary as structural constraint

**Quality gate question:** *For each actor, is every information boundary enforced by System infrastructure, not by prompt instruction?*

### CC-5: Specification Aging

**Principle:** Agent specifications degrade over time. Task drift, model updates, and changing context erode specification validity. Without explicit aging mechanisms, specifications become silently stale.

**Three components:**
- **Aging triggers:** Model change, task context change, performance degradation, override rate increase
- **Review cadence:** Time-based (quarterly for stable, monthly for new) AND trigger-based (on any aging trigger)
- **Capability drift tracking:** Does the agent's actual performance match its specification? When they diverge, the specification needs updating

**Quality gate question:** *For each agent in this phase, are specification freshness dates and aging triggers documented?*

### CC-6: System Empowerment Index

**Principle:** How much creative freedom does the system give the human? This replaces the concept of "how much scaffolding does the human need." The direction is upward through the 5-level scale (Constraining → Informing → Enabling → Amplifying → Liberating), not toward "less dependency."

**Quality gate question:** *Where does this phase's design land on the System Empowerment Index? Is it moving upward through use?*

### CC-7: Cost Budget

**Principle:** Cost is a first-class design constraint, not an afterthought.

**Three cost levels:**
- **Per-agent cost budget:** Maximum acceptable cost per invocation (token cost + tool cost + infrastructure cost)
- **Pipeline cost budget:** Maximum acceptable cost per unit processed (e.g., per student, per document)
- **Total cost budget:** Maximum acceptable cost per time period (e.g., per marking cycle)

**Cost-quality trade-off:** Is the marginal cost of adding an agent justified by the marginal quality improvement? If not, consider System alternatives.

**Quality gate question:** *Are cost budgets specified per agent and per pipeline unit? Is the total cost within the acceptable range?*

### CC-8: Assured Audit Trail

**Principle:** Every action creates a traceable, attributed, timestamped record. But "immutable" is aspirational — three assurance levels match different trust requirements.

| Assurance Level | Storage | Tamper Resistance | When Appropriate |
|---|---|---|---|
| **Level 1: Logged** | Application log | Tamperable by admin | Debugging, internal review |
| **Level 2: Assured** | Append-only store | Tamper-evident | Compliance, quality assurance |
| **Level 3: Verified** | Cryptographically signed | Tamper-proof | Legal, financial, regulatory |

**Quality gate question:** *For each action type, is the audit assurance level specified? Is it appropriate for the trust requirement?*

---

## Enrichment-Fidelity Question Pairs

Every phase asks two questions — one for output fidelity, one for creative freedom expansion:

| Phase | Fidelity Question | Enrichment Question |
|---|---|---|
| **1** | Is the task decomposed correctly? | Does the decomposition preserve space for human creative judgment? |
| **2** | Are allocations correct? | Do allocations free the human from mechanical work TO BE creative? |
| **2.5** | Are events and data flows complete? | Are human decision points visible and empowered? |
| **3** | Does the architecture work? | Does the architecture give the human room to discover new methods? |
| **4** | Are agents specified correctly? | Do agents handle the routine so the human can do the novel? |
| **5** | Is the interface usable? | Does the interface give the human creative freedom, not just approval workflows? |
| **6** | Does the system work? | Is the human finding solutions they wouldn't find alone? |

---

## PHASE 1: Task Intelligence

*Understand the task before designing anything.*

### Step 1.1: Task Decomposition

**What:** Break the task into phases, subtasks, and dependency chains. Identify the *cognitive operations* required — not just "what needs to happen" but *what kind of thinking* each step demands.

**How:**
1. List all deliverables the task must produce
2. Backcast from each deliverable: what must be true for this to exist?
3. Decompose each prerequisite into subtasks
4. Classify each subtask's cognitive operation type:

| Cognitive Operation | Description | Best Actor | Example |
|---|---|---|---|
| **Mechanical** | Deterministic transformation, validation, routing | **System** | Schema validation, format conversion, threshold checking |
| **Structural** | Mapping form/organisation | Agent or System | Depends on whether interpretation is needed |
| **Domain-semantic** | Interpreting domain-specific meaning | Agent | Identifying blockchain claims in text |
| **Comparative-semantic** | Comparing across instances | Agent | Detecting synthesis patterns across submissions |
| **Structural-semantic** | Auditing structural-intent alignment | Agent | Is the reflection section actually reflective? |
| **Statistical** | Numerical pattern detection | System (simple) or Agent (complex) | Depends on complexity |
| **Generative** | Producing novel text/structure | Agent | Drafting constructive feedback |
| **Evaluative** | Making quality judgments | Human or Agent (recommendation) | Scoring against rubric criteria |
| **Synthesis** | Consolidating multiple sources | Agent or Human | Depends on nature of consolidation |

**The critical distinction:** Mechanical operations are *provably correct* (System). Agent operations are *probably correct* (Agent). Human operations are *accountably correct* (Human). When a subtask can be mechanical, it SHOULD be mechanical — it removes an entire failure mode category.

**Decomposition depth guidance:**

```
STOP decomposing when:
  ✓ 1-2 cognitive operations per subtask
  ✓ Single clear authority boundary
  ✓ Single verification check can validate the output
  ✓ Output consumed by ≥1 other actor

CONSIDER further decomposition when:
  ⚠ >2 cognitive operations bundled
  ⚠ Authority boundary is ambiguous
  ⚠ Verification requires multiple independent checks
  ⚠ Different failure modes within one subtask

ALWAYS decompose when:
  ✗ >3 cognitive operations bundled
  ✗ Agent would need to switch cognitive modes mid-task
  ✗ Different operations have different hallucination risk levels
```

**Artifact:** `Task Decomposition Map` — each subtask annotated with cognitive operation type, best actor candidate, dependencies, and estimated cognitive load.

### Step 1.2: Cognitive Load Analysis

**What:** For each subtask, estimate the working memory demands, number of distinct cognitive operations, and switching cost.

**How:**
1. For each subtask, ask: *How many distinct cognitive operations are bundled here?*
2. If >2, flag for potential further decomposition
3. Estimate working memory demand: how many things must be held simultaneously?
4. Estimate switching cost: how much context must be loaded/unloaded?

**Artifact:** `Cognitive Load Assessment` — per-subtask: operation count, working memory demand, switching cost, granularity verdict (under-decomposed / right-sized / over-decomposed).

### Step 1.3: Expert Validation

**What:** Validate the decomposition with domain experts before proceeding.

**How:**
1. Present decomposition to 1-3 domain experts
2. Ask: "Do you recognise these subtasks? Would you decompose differently?"
3. Capture any subtasks they identify that you missed
4. Confirm the cognitive operation labels match expert mental models

**Effort heuristic:** 30-60 minute conversation per expert. Skip only if you ARE the domain expert AND can articulate your expertise explicitly.

**Artifact:** `Expert Validation Record` — expert feedback, decomposition changes made.

### Step 1.4: Edge Case Inventory

**What:** Identify boundary conditions and anomalous inputs before designing the system.

**How:**
1. For each input type, list: empty, corrupted, ambiguous, adversarial, oversized, undersized variants
2. For each subtask, ask: "What input would break this?"
3. Categorise: *must-handle* (common enough to design for) vs. *must-detect* (flag for human) vs. *out-of-scope*

**Artifact:** `Edge Case Catalog` — per input type: edge cases, expected handling, categorisation.

### Phase 1 Test Plan

*Every design decision generates a test. Phase 1 tests validate decomposition.*

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 1.1.1 | Cognitive operation classification | Each subtask's operation type | Example tasks classify unambiguously into types |
| 1.2.1 | Granularity check | Decomposition depth guidance | Each subtask has 1-2 operations, single boundary |
| 1.3.1 | Expert recognition | Expert validation | Experts recognise ≥90% of subtasks |
| 1.4.1 | Edge case coverage | Edge case catalog | ≥3 edge cases per input type identified |

---

### 🔴 QUALITY GATE 1: Task Intelligence Complete

**Fidelity Checks:**
- [ ] Every subtask has a cognitive operation classification (including Mechanical for System candidates)
- [ ] No subtask bundles >3 cognitive operations (or explicitly justified)
- [ ] Cognitive load assessment completed for all subtasks
- [ ] Domain expert validation obtained (or expertise self-attestation documented)
- [ ] Edge case catalog has ≥3 cases per input type
- [ ] All deliverables trace back through dependency chains

**Enrichment Checks:**
- [ ] Decomposition preserves space for human creative judgment
- [ ] Mechanical subtasks correctly identified (freeing humans for judgment work)
- [ ] No subtask that should be human-creative is classified as mechanical

**Cross-Cutting Checks:**
- [ ] CC-1: Verification independence considered — can any subtask be self-verified?
- [ ] CC-5: Specification aging triggers identified for task context changes
- [ ] CC-7: Initial cost budget estimate per deliverable

**Test Readiness Checks:**
- [ ] Phase 1 test plan defined with targets
- [ ] Expert validation test results available
- [ ] Edge case tests defined with expected handling

---

## PHASE 2: Capability Allocation

*Determine what System does, what Agent does, what Human does, and why.*

### Step 2.1: Complementarity Analysis

**What:** Map each subtask against capability dimensions to determine System/Agent/Human allocation.

**How:**
1. Score each subtask on 15 capability dimensions (1-9 scale) for Human, Agent, AND System:

| Dimension | Human | Agent | System |
|---|---|---|---|
| Reasoning depth | Abstract, novel | Pattern, defined-rule | None (0) |
| Ethical judgment | Moral reasoning | Rule-based ethics | Explicit constraints only |
| Values alignment | Organisational culture | Explicit norms | None (0) |
| Decision authority | Accountability | Recommendation generation | None (0) |
| Domain expertise | Tacit, intuitive | Explicit knowledge | Encoded rules only |
| Parallelisation | Sequential limit | Massive parallel | Infinite parallel |
| Output consistency | Variable, fatigue-prone | Deterministic given input | Perfectly deterministic |
| Speed | Minutes-hours/unit | Seconds/unit | Milliseconds/unit |
| Novelty handling | Adaptive, creative | Training distribution | None (0) |
| Context sensitivity | Reads room | Follows instructions | None (0) |
| Precision | Human error rate | Computational accuracy | Perfect accuracy |
| Scalability | Linear time | Near-constant time | Constant time |
| Explainability | Can articulate | Can cite, show chains | Trivially auditable |
| Cultural sensitivity | Lived experience | Training data patterns | None (0) |
| Error type | Omission, fatigue | Hallucination, overconfidence | Bugs, logic errors |

2. Calculate H-A, H-S, and A-S gaps for each dimension
3. Apply the **Ternary Complementarity Allocation Algorithm:**

```
For each subtask:
  // SYSTEM FIRST — eliminate hallucination risk where possible
  IF cognitive operation = Mechanical:
    → SYSTEM-LED
  
  // HUMAN GATE — protect authority domains
  IF any dimension in {Ethical Judgment, Values Alignment, Decision Authority}
     has H-A gap ≥ 6 AND H-S gap ≥ 6:
    → HUMAN-LED
  
  // AGENT ADVANTAGE — semantic reasoning at scale
  IF any dimension in {Parallelisation, Output Consistency, Scalability}
     has A-S gap ≥ 5 AND A-H gap ≥ 5:
    → AGENT-LED
  
  // SYSTEM FOR CONSISTENCY — determinism over semantics
  IF consistency requirement = 9 AND semantic need < 3:
    → SYSTEM-LED
  
  // COLLABORATIVE — genuine hybrid
  → DEFAULT TO COLLABORATIVE
     (specify which actors collaborate and in what ratio)
```

4. **Model-specific scoring:** Scores must be grounded to specific LLM models and specific human profiles. Document the model reference (e.g., GPT-4, Claude 3.5, local model) and human profile (e.g., subject-matter expert, trained operator, novice) for each score.

5. **Reversibility classification:** For each subtask, classify the action type:
   - **Read-only:** No side effects — safe to automate
   - **Reversible:** Can be undone — automate with logging
   - **Irreversible:** Cannot be undone — human presence required structurally

**Artifact:** `Complementarity Matrix` — per subtask: 15 H/A/S scores, gap scores, allocation decision, model reference, human profile, reversibility class, rationale.

### Step 2.2: Actor Analysis

**What:** Identify all human actors, not just "the human."

**How:**
1. List every human role that interacts with the system
2. For each role, specify: expertise level, decision authority, time availability, cognitive load tolerance
3. Map which subtasks each human role owns
4. Identify inter-human coordination needs (e.g., multiple markers needing calibration)

**Artifact:** `Actor Map` — roles, capabilities, constraints, inter-actor coordination requirements.

### Phase 2 Test Plan

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 2.1.1 | Mechanical classification | System-first allocation | Mechanical subtasks correctly identified and assigned to System |
| 2.1.2 | Complementarity gap accuracy | H/A/S scoring | For subtasks with large gaps, assigned actor performs measurably better |
| 2.1.3 | Reversibility classification | Action reversibility | Irreversible subtasks have human gates |
| 2.2.1 | Actor coverage | Actor map | All human roles identified, no orphan subtasks |

---

### 🔴 QUALITY GATE 2: Capability Allocation Complete

**Fidelity Checks:**
- [ ] Every subtask has H/A/S scores with model reference and human profile
- [ ] Allocation decisions trace to specific gap scores (System-first priority)
- [ ] Mechanical subtasks correctly identified and allocated to System
- [ ] Actor map includes all human roles (not just "the human")
- [ ] Reversibility classes assigned for all subtasks

**Enrichment Checks:**
- [ ] Human-allocated subtasks are genuine judgment/creative work, not mechanical
- [ ] System-allocated subtasks genuinely free the human for creative work
- [ ] No subtask that should expand human creative freedom is allocated away from human

**Cross-Cutting Checks:**
- [ ] CC-1: Verification independence — can any allocated subtask verify itself?
- [ ] CC-4: Information boundaries — initial identification of what each actor must NOT know
- [ ] CC-7: Cost budget — estimated cost per allocation (System cheapest, Agent moderate, Human expensive)
- [ ] CC-8: Audit assurance levels — initial assignment per subtask type

**Test Readiness Checks:**
- [ ] Phase 2 test plan defined with targets
- [ ] Complementarity gap test targets set
- [ ] System feasibility tests defined for all mechanical subtasks

---

## PHASE 2.5: Event Storming

*Conditional — only for multi-agent workflows with dependencies, data handoffs, and/or human decision points.*

### When to Use Event Storming

| Condition | Do Event Storming? |
|---|---|
| Single agent, no human loop | ❌ Skip |
| Linear pipeline, no branching, no failure recovery | ⚠️ Optional |
| Multi-agent with human decisions | ✅ Recommended |
| Multi-agent with branching/failure recovery | ✅ Essential |
| Multiple human actors | ✅ Essential |

### Step 2.5.1: Domain Event Mapping

**What:** Map every event that occurs in the system on a timeline.

**How:**
1. Write each domain event on a card (past tense): `SubmissionReceived`, `FormatValidated`, `AnomalyFlagged`, `ScoreRecommended`, `HumanOverrideIssued`
2. Arrange chronologically
3. For each event, identify:
   - **Command:** What triggers it? (who or what)
   - **Actor:** Who/what executes it? (Human / Agent / System)
   - **Data produced:** What structured output does it generate?
   - **Policy:** What happens next? (what events does it trigger?)

### Step 2.5.2: Failure Event Surfacing

**What:** Systematically identify events that shouldn't happen but will.

**How:** For each happy-path event, ask:
1. *What if this produces wrong output?* → `AgentOutputDoubted`
2. *What if this times out?* → `ActorTimeoutExpired`
3. *What if this receives unexpected input?* → `UnexpectedInputReceived`
4. *What if the human disagrees?* → `HumanOverrideIssued`
5. *What if the human is absent?* → `HumanDecisionDeferred`
6. *What if System validation fails?* → `SystemValidationFailed`

### Step 2.5.3: Data Flow Validation

**What:** For each event, verify that its input data exists and is accessible.

**How:**
1. For each event, ask: "What data does this event's actor need?"
2. Trace backwards: which prior events produce that data?
3. Flag any data that is *implied but not explicitly produced*
4. Verify data format compatibility (template schemas match)

### Step 2.5.4: Trigger Condition Specification

**What:** Define the exact conditions that trigger each event, including System-enforced conditions.

**How:**
1. For each event, write the trigger condition as a boolean expression
2. For each trigger, define the timeout: what happens if the condition is never met?
3. For each trigger, define the fallback: what happens if the triggering event fails?
4. Identify which triggers are System-enforced (deterministic) vs. Agent-triggered (probabilistic) vs. Human-triggered (discretionary)

**Artifact:** `Event Storm Map` — timeline of events, commands, actors (H/A/S), data flows, failure events, trigger conditions, timeouts, fallbacks, System-enforced triggers.

### Phase 2.5 Test Plan

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 2.5.1 | Event completeness | Event mapping | Walking through a realistic scenario, every event fires |
| 2.5.2 | Trigger condition accuracy | Trigger specification | Each trigger fires correctly on test inputs |
| 2.5.3 | Fallback functionality | Fallback specification | Each fallback works when primary path fails |
| 2.5.4 | Data flow integrity | Data flow validation | Every consumer's input is explicitly produced |

---

### 🔴 QUALITY GATE 2.5: Event Storming Complete (if applicable)

**Fidelity Checks:**
- [ ] Event storm map covers happy path + failure events
- [ ] Every event has an actor type (H/A/S)
- [ ] Data flow validated for every event — no implied-but-not-produced data
- [ ] Trigger conditions specified with timeouts and fallbacks
- [ ] System-enforced triggers identified

**Enrichment Checks:**
- [ ] Human decision points are visible, empowered, and not rubber stamps
- [ ] Failure events give humans room for creative judgment, not just binary choices

**Cross-Cutting Checks:**
- [ ] CC-1: Verification events identified for each agent output
- [ ] CC-4: Information boundaries mapped — what data each actor can/cannot access
- [ ] CC-8: Audit events identified with assurance levels

**Test Readiness Checks:**
- [ ] Phase 2.5 test plan defined with targets

---

## PHASE 3: System Architecture

*Design the structure that everything lives in.*

### Step 3.1: Pipeline Architecture (Backcasting)

**What:** Design the data flow from final deliverables backwards.

**How:**
1. List final deliverables
2. For each, trace the dependency chain back through phases
3. Define the **data objects** that flow between stages:
   - Schema (what fields — reference Template Architecture from Step 3.4)
   - Producer (which actor creates it — H/A/S)
   - Consumer (which actor reads it — H/A/S)
   - Mutability (append-only, replaceable, immutable)
   - Persistence (ephemeral, session, permanent)

4. Identify execution topology:
   - **Sequential:** Phase N completes before Phase N+1 starts
   - **Parallel:** Multiple actors run simultaneously within a phase
   - **Event-driven:** Actors activate on trigger conditions
   - **Gated:** Phase transition requires System-enforced quality check

### Step 3.2: Orchestration Design

**What:** Design the system that manages actor execution, not just the actors themselves.

**How:**
1. Specify execution engine: what triggers Wave 1? What waits for Wave 1 completion?
2. Define **orchestration policies:**
   - **Timeout policy:** How long before an actor is assumed failed?
   - **Retry policy:** How many retries? With what backoff?
   - **Partial completion policy:** Can the pipeline continue if one actor fails?
   - **Cascading failure policy:** What happens when a critical-path actor fails?
   - **System enforcement points:** Where does System enforce gates, schemas, and boundaries?
3. Define **progress tracking:** How is pipeline state represented? How does the human know where things stand?
4. Define **fallback model tiers:**

| Tier | Model | When Used | Expected Quality |
|---|---|---|---|
| **Tier 1** | Primary model | Normal operation | Full |
| **Tier 2** | Secondary model | Primary unavailable | Near-full |
| **Tier 3** | Local model | API unavailable | Reduced |
| **Tier 4** | System fallback | No model available | Rules only |

Each agent should have a fallback specification: what does it produce at each tier? Does it still meet minimum quality? Does it flag the reduced confidence in its epistemic metadata?

### Step 3.3: Failure Mode & Effects Analysis (FMEA)

**What:** For every actor and every pipeline transition, analyse what happens when things go wrong.

**How:**
1. For each agent, list its **primary failure mode** (from the 5-class taxonomy)
2. For each failure mode, assess:

| Field | Content |
|---|---|
| Agent/Component name | |
| Primary failure mode | (e.g., hallucination for Extractors) |
| Detection method | (How will we know it failed?) |
| Detection probability | (High / Medium / Low) |
| Impact if undetected | (What goes wrong downstream?) |
| Recovery path | (Rerun? Skip? Flag? Human escalation?) |
| Containment boundary | (What stops the failure from propagating?) |
| System enforcement | (What System component catches this?) |

3. For System components, list their failure modes:
   - Bug in validation logic → System flags incorrectly
   - Schema mismatch → System rejects valid data
   - Infrastructure failure → System unavailable
4. For each pipeline transition, list:
   - **Upstream failure:** What if the input is wrong?
   - **Transition failure:** What if the handoff fails?
   - **Downstream assumption:** What does the next actor assume about this input?

### Step 3.4: Template Architecture Design

**What:** For every data flow identified in the pipeline architecture, design the template that structures it. Templates are the structural mechanism that resolves type collision — both input and output side.

**Seven template types:**

| Template Type | Purpose | Enforced By | Example |
|---|---|---|---|
| **Input Template** | Standardises what an actor receives | System (pre-processing) | Structured submission package with typed fields |
| **Output Template** | Enforces typed, decomposable outputs | System (post-validation) | Claims analysis: claim, source, confidence, domain tags |
| **Handoff Template** | Structures data packages between actors | System (routing) | Enhanced Submission Package: format + claims + anomalies |
| **Verification Template** | Codifies verification criteria per agent class | System (gate enforcement) | Format verification: file type ✓, slide count ✓, sections ✓ |
| **Decision Template** | Structures human decision inputs | System (presentation) | Score recommendation: criterion, evidence, confidence, alternatives |
| **Feedback Template** | Structures agent-to-human feedback | Agent (generation) | Student feedback: strength, improvement area, suggestion, rubric alignment |
| **Escalation Template** | Standardises escalation protocols | System (routing) | Escalation: agent, issue, evidence, urgency, recommended action |

**How:**
1. For each data object in the architecture, ask: *What types of information does this object carry?*
2. Decompose each type into a typed field (not prose)
3. For each field, specify: type, constraints (required/optional, range, format), provenance
4. For each template, specify: validation rules (System-enforced), consumers, mutability
5. **Include epistemic metadata:** Every output template includes the six fields from CC-3 (provenance, confidence, limitations, assumptions, alternatives set aside, what would change this)
6. **Stress-test:** Can this template carry the information the consumer needs? Is any information NOT in the template?

**The key insight:** Templates resolve bidirectional type collision. Input templates resolve input-side type collision (17+ cognitive modes compressed into one input modality). Output templates resolve output-side type collision (17+ information types compressed into one output type). The template is the decomposable artefact — not the prose.

### Step 3.5: Composition Decision

**What:** For each pipeline segment, decide whether it should be an Agent, a Team, or a Workflow.

| Primitive | When to Use | Signal |
|---|---|---|
| **Agent** | Single cognitive operation, single authority boundary | One "never" constraint suffices |
| **Team** | Multiple operations need coordination, shared context | Multiple authority boundaries but shared data |
| **Workflow** | Sequential/parallel stages with data handoffs | Different stages have different actor types |

**Artifact:** `System Architecture Document` — pipeline diagram, data objects with template references, orchestration policies, FMEA table, composition decisions, System enforcement points, fallback model tier specifications.

### Phase 3 Test Plan

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 3.1.1 | Data flow completeness | Pipeline architecture | Every consumer's input is explicitly produced |
| 3.2.1 | Orchestration trigger tests | Orchestration design | Each trigger fires correctly on test inputs |
| 3.2.2 | Timeout handling | Orchestration policies | Pipeline handles timeouts gracefully |
| 3.2.3 | Fallback tier behavior | Fallback model tiers | Each tier produces output with appropriate quality/confidence |
| 3.3.1 | FMEA recovery tests | FMEA table | Each recovery path works as specified |
| 3.4.1 | Template schema validation | Template architecture | System validates every template against its schema |
| 3.4.2 | Template completeness | Template architecture | Every template carries all information the consumer needs |
| 3.5.1 | Composition appropriateness | Composition decisions | Each segment's composition type matches its complexity |

---

### 🔴 QUALITY GATE 3: Architecture Complete

**Fidelity Checks:**
- [ ] Every data object has schema, producer (H/A/S), consumer (H/A/S), mutability, persistence
- [ ] No data flow is implied — every consumer's input is explicitly produced
- [ ] Orchestration policies cover timeout, retry, partial completion, cascading failure
- [ ] System enforcement points identified for all gates and boundaries
- [ ] FMEA completed for every actor (H/A/S) and every pipeline transition
- [ ] Recovery paths specified for every failure mode, with System containment
- [ ] Edge cases from Phase 1 mapped to handling in architecture
- [ ] Fallback model tiers specified for all agents
- [ ] Template architecture covers all data flows with typed schemas
- [ ] Composition decisions made for all pipeline segments

**Enrichment Checks:**
- [ ] Architecture gives human room to discover new methods, not just approve system outputs
- [ ] Human decision points are genuine judgment opportunities, not rubber stamps

**Cross-Cutting Checks:**
- [ ] CC-1: Verification chain specified for each pipeline segment (System→System, System→Agent, Agent→Human)
- [ ] CC-3: All output templates include epistemic metadata fields
- [ ] CC-4: Information boundaries mapped as System-enforced context curtains
- [ ] CC-7: Cost budget estimated per pipeline unit
- [ ] CC-8: Audit assurance levels specified per action type

**Test Readiness Checks:**
- [ ] Phase 3 test plan defined with targets
- [ ] Template schema validation tests defined
- [ ] Orchestration trigger tests defined
- [ ] FMEA recovery path tests defined

---

## PHASE 4: Agent Design

*Design each agent with the specificity needed for implementation.*

### Step 4.1: Agent Classification

**What:** Assign each agent to a class. The boundary principle and failure mode follow immediately.

| Class | Authority Boundary | Primary Failure Mode | Hallucination Risk | Key Constraint |
|---|---|---|---|---|
| **Extractor** | Never judge | Hallucination | High | Only extract, never interpret |
| **Measurer** | Never interpret | Noise-as-signal | Low | Present data, not meaning |
| **Assessor** | Never finalise | Overconfidence | Medium | Recommend, never decide |
| **Generator** | Never be vague | Fabrication | High | Every claim must cite evidence |
| **Aggregator** | Never add | Omission | Low | Consolidate only, no new analysis |

System components have no class — they have no authority boundary because they have no judgment.

### Step 4.2: Authority Boundary Specification

**What:** Define what each agent must NOT do. The constraint is the inverse of the failure mode.

**Design pattern:**
```
IF agent class = Extractor:
  boundary = "Never judge" (because failure mode = hallucination of interpretations)
IF agent class = Measurer:
  boundary = "Never interpret" (because failure mode = noise-as-signal)
IF agent class = Assessor:
  boundary = "Never finalise" (because failure mode = overconfidence)
IF agent class = Generator:
  boundary = "Never be vague" (because failure mode = fabrication/vagueness)
IF agent class = Aggregator:
  boundary = "Never add" (because failure mode = omission through addition)
```

### Step 4.3: Boundary Stress Testing

**What:** Before finalising the boundary, test it with inputs designed to push the agent toward its failure mode.

**How:** For each agent, design 3-5 **boundary stress inputs:**
- *What input would tempt this Measurer to interpret?* → e.g., a statistical outlier that "obviously" means something
- *What input would tempt this Generator to be vague?* → e.g., a submission so weak that constructive feedback feels impossible
- *What input would tempt this Assessor to finalise?* → e.g., a near-perfect submission where scoring feels obvious

Document the expected boundary-enforced response vs. the tempted response. This becomes a test case for implementation.

### Step 4.4: Agent Job Description

**What:** Create a complete specification that enables a developer to implement the agent without further design decisions.

```
AGENT JOB DESCRIPTION
=====================

IDENTITY
  Name:
  Class: (Extractor / Measurer / Assessor / Generator / Aggregator)
  Authority Boundary: (the "never" constraint)
  Primary Failure Mode: (the inverse of the boundary)

MISSION
  One-sentence statement of what this agent produces, for whom, and why.

INPUT TEMPLATE
  - Reference to Step 3.4 input template
  - Required fields (what data, from which actor, in what format)
  - Optional fields (what data improves quality if available)
  - Edge case handling (from Phase 1 edge case catalog)

OUTPUT TEMPLATE
  - Reference to Step 3.4 output template
  - Structured output format (typed, not prose)
  - Epistemic metadata: provenance, confidence, limitations,
    assumptions, alternatives set aside, what would change this
  - Required fields
  - Optional fields

CONTEXT & KNOWLEDGE
  - Domain knowledge required
  - Reference materials (specific documents, URLs, data)
  - System prompt context

TOOLS
  - Required tools (web search, calculator, etc.)
  - Optional tools

INFORMATION BOUNDARY
  - What this agent CAN read (explicit list)
  - What this agent CANNOT read (enforced by System context curtain)
  - How the boundary is enforced (infrastructure, not prompt)

HARD CONSTRAINTS
  - Authority boundary (from Step 4.2)
  - Additional constraints specific to this agent
  - Prohibited actions

QUALITY CRITERIA
  - What does "good output" look like for this agent?
  - Measurable quality indicators
  - Failure indicators (signals that the agent is failing)

VERIFICATION
  - Who verifies this agent's output? (Level 1/2/3 from CC-1)
  - What does verification check?
  - How is verification independence enforced?

ERROR HANDLING
  - What to do on missing input → (flag? skip? error?)
  - What to do on ambiguous input → (request clarification? flag? proceed with confidence score?)
  - What to do on tool failure → (retry? fallback? flag?)
  - Fallback model tier behavior (from Step 3.2)

ESCALATION PROTOCOL
  - When to escalate to human
  - When to escalate to orchestrator
  - What information to include in escalation

PERFORMANCE EXPECTATIONS
  - Expected latency
  - Expected accuracy (if estimable)
  - Cost budget per invocation

PROGRESSIVE AUTONOMY
  - Initial autonomy level (shadow / advisory / supervised / autonomous)
  - Advancement criteria (accuracy thresholds, override rates)
  - Maximum autonomy level for this agent type

SPECIFICATION AGING
  - Specification freshness date
  - Aging triggers (model change, performance degradation, override rate increase)
  - Review cadence (time-based AND trigger-based)

ADVERSARIAL EXAMPLES
  - 2-3 inputs designed to push toward failure mode
  - Expected boundary-enforced response for each
  - Common temptation and correct refusal

INTERACTION MAP
  - Upstream: which actors (H/A/S) provide input
  - Downstream: which actors (H/A/S) consume output
  - Parallel: which agents run alongside this one
  - System enforcement points: what System components gate this agent's I/O
```

### Step 4.5: Cost-Benefit Assessment

**What:** Determine whether each agent justifies its complexity — or whether a System component could do the job.

**How:** For each agent, assess:
1. **Value added:** What would be lost if this agent were removed? Would a System component (deterministic code) suffice?
2. **Complexity cost:** How complex is this agent to implement, maintain, and debug?
3. **Failure risk:** What's the probability and impact of this agent's failure mode?
4. **Cost per invocation:** Token cost + tool cost + infrastructure cost
5. **System alternative:** Could a deterministic rule handle this? At what quality level?

**Verdict:**
- **Essential:** Unique cognitive work that can't be achieved by System
- **Valuable:** Justified complexity — saves human time or improves quality beyond System
- **Questionable:** Could be replaced by a System component with acceptable quality
- **Unnecessary:** Adds no value beyond what System already provides

### Step 4.6: Coalition Formation Review

**What:** Check that agents within the same wave are composed for epistemic complementarity, not just functional role coverage.

**How:**
1. For each execution wave, list the agents' cognitive orientations
2. Check: Are multiple agents in the same wave approaching the problem from the same orientation?
3. If yes: Are they providing genuinely different perspectives, or converging on the same answer?
4. If converging: Consider replacing one with an agent of different orientation

**Example:** Two critical-oriented agents will produce convergent outputs. A critical agent + an optimistic agent produces a richer option space.

### Phase 4 Test Plan

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 4.1.1 | Classification correctness | Agent taxonomy | Each agent's class matches its cognitive operation |
| 4.2.1 | Boundary adherence | Authority boundary | Agent respects "never" constraint on stress inputs |
| 4.3.1 | Stress input tests | Boundary stress testing | Each stress input produces boundary-enforced response |
| 4.4.1 | Template compliance | Output template | Agent output validates against output template schema |
| 4.4.2 | Epistemic metadata | Output template | All six metadata fields present and accurate |
| 4.4.3 | Information boundary | Boundary enforcement | Agent cannot access forbidden data through any mechanism |
| 4.5.1 | Cost-benefit justification | Cost assessment | Each agent classified as Essential or Valuable |
| 4.6.1 | Coalition diversity | Cognitive orientation | Each wave has epistemic diversity |

---

### 🔴 QUALITY GATE 4: Agent Design Complete

**Fidelity Checks:**
- [ ] Every agent classified in 5-class taxonomy (or identified as System component)
- [ ] Authority boundary specified as inverse of failure mode
- [ ] Boundary stress tests designed (3-5 per agent)
- [ ] Job descriptions complete for all agents (using template)
- [ ] Adversarial examples included in each job description
- [ ] Input and output templates referenced in all job descriptions
- [ ] Information boundaries specified as System-enforced, not prompt-only
- [ ] Verification independence specified for each agent (Level 1/2/3)
- [ ] Progressive autonomy level and advancement criteria specified
- [ ] Specification freshness date and aging triggers documented
- [ ] Fallback behavior specified for each model tier
- [ ] Cost-benefit assessment completed — no "Unnecessary" agents remain
- [ ] Coalition formation reviewed for epistemic diversity

**Enrichment Checks:**
- [ ] Every agent's output scaffolds human understanding, not replaces judgment
- [ ] Agents handle routine work so humans can do novel work
- [ ] System Empowerment Index assessed for each human-agent interaction point

**Cross-Cutting Checks:**
- [ ] CC-1: Every agent has a separate verifier (independence level specified)
- [ ] CC-3: Every output template includes all six epistemic metadata fields
- [ ] CC-4: Information boundaries enforced by System, not prompts
- [ ] CC-5: Specification aging triggers and review cadence documented
- [ ] CC-6: System Empowerment Index level assessed per interaction
- [ ] CC-7: Cost budget specified per agent and per pipeline unit
- [ ] CC-8: Audit assurance level specified per agent action type

**Test Readiness Checks:**
- [ ] Phase 4 test plan defined with targets
- [ ] Boundary adherence tests defined with adversarial examples
- [ ] Failure mode tests defined for each agent class
- [ ] Epistemic metadata accuracy tests defined
- [ ] Template schema validation tests referenced from Step 3.4
- [ ] Cost budget tests defined

---

## PHASE 5: Human Experience Design

*The human in the system is not a bucket that agents pour outputs into.*

### Step 5.1: Cognitive Load Budget

**What:** Determine how much information the human can process at each interaction point.

**How:**
1. For each human-only subtask, estimate:
   - **Information volume:** How many agent outputs must the human consume?
   - **Decision density:** How many decisions must the human make?
   - **Time pressure:** How quickly must each decision be made?
   - **Consequence severity:** How bad is a wrong decision?
2. If cognitive load exceeds budget at any point:
   - Add a **cognitive offloader** (meta-agent that pre-synthesises)
   - Reduce information volume (filter, summarise, prioritise)
   - Reduce decision density (batch similar decisions, present one at a time)
   - Reduce time pressure (async review instead of real-time)

### Step 5.2: Human Interface Specification

**What:** Design how the human receives, navigates, and acts on agent outputs.

**How:**
1. For each human interaction point, specify:
   - **What the human sees** (layout, information hierarchy, priority ordering)
   - **What the human does** (approve/reject, score, edit, override)
   - **What the human needs** (context, prior agent outputs, epistemic metadata, comparison data)
   - **What the human doesn't need** (filter out information that's not decision-relevant)
   - **What epistemic metadata is visible** (confidence scores, limitations, assumptions)
2. Design the **navigation flow:** How does the human move between interaction points?
3. Design the **interruption model:** Can the human pause and resume? What state is preserved?

### Step 5.3: Override & Feedback Mechanisms

**What:** Design how the human corrects the system and how corrections feed back.

**How:**
1. For each human decision, define:
   - **Override mechanism:** How does the human change an actor's output?
   - **Feedback path:** Does the override inform the actor for future runs? (System-enforced)
   - **Audit trail:** Is the override logged with rationale? At what assurance level?
2. Distinguish between:
   - **Decision overrides** (human changes a specific output)
   - **Parameter adjustments** (human changes system configuration)
   - **Process interventions** (human changes the pipeline itself)

3. Design **creative freedom mechanisms:**
   - How does the human explore alternatives the system didn't surface?
   - How does the human's creative insight feed back into the system?
   - Where are the "blank canvas" moments where the human is free to create?

### Step 5.4: System Empowerment Assessment

**What:** Assess where each human interaction point lands on the System Empowerment Index.

**How:**
1. For each interaction point, score: Constraining (1) → Informing (2) → Enabling (3) → Amplifying (4) → Liberating (5)
2. Identify any Constraining or Informing interactions
3. Redesign to move interactions upward:
   - **Constraining → Enabling:** Give the human genuine choice, not just approve/reject
   - **Informing → Amplifying:** Surface options the human wouldn't have seen
   - **Enabling → Liberating:** Create possibility spaces the human couldn't access alone

**The test is NOT "can the human do this alone?" It IS "did the human discover a better method they wouldn't have found without the system?"**

**Artifact:** `Human Experience Specification` — cognitive load budget, interface specification, navigation flow, override mechanisms, System Empowerment Index assessment, creative freedom mechanisms.

### Phase 5 Test Plan

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 5.1.1 | Cognitive load budget | Load analysis | Human completes decision point within budget |
| 5.2.1 | Interface usability | Interface specification | Human can navigate and act without confusion |
| 5.3.1 | Override mechanism | Override design | Human can successfully override any actor output |
| 5.3.2 | Feedback path | Override design | Overrides are logged and feed back to system |
| 5.4.1 | Creative freedom | Empowerment assessment | Human discovers ≥1 new approach per 10 sessions |
| 5.4.2 | Empowerment level | Empowerment assessment | No interaction point scored below Enabling (3) |

---

### 🔴 QUALITY GATE 5: Human Experience Complete

**Fidelity Checks:**
- [ ] Cognitive load budgeted for every human interaction point
- [ ] No interaction point exceeds cognitive load budget without a mitigation
- [ ] Interface specification covers what human sees, does, needs, doesn't need
- [ ] Navigation flow between interaction points specified
- [ ] Override mechanisms specified for every human decision point
- [ ] Audit trail specified for all overrides

**Enrichment Checks:**
- [ ] Every interaction point scored on System Empowerment Index
- [ ] No interaction point below Enabling (3) without justification
- [ ] Creative freedom mechanisms designed — human can explore beyond system suggestions
- [ ] Epistemic metadata (confidence, limitations) visible to human at decision points
- [ ] System Empowerment Index moves upward through use, not toward "less dependency"

**Cross-Cutting Checks:**
- [ ] CC-2: System Empowerment Index assessed per interaction
- [ ] CC-6: Overall system assessed for creative freedom expansion
- [ ] CC-8: Override audit trails at appropriate assurance level

**Test Readiness Checks:**
- [ ] Phase 5 test plan defined with targets
- [ ] Cognitive load tests defined with time targets
- [ ] Creative freedom tests defined with discovery targets
- [ ] Override mechanism tests defined

---

## PHASE 6: Validation & Iteration

*Design without validation is speculation. Testing happens throughout, not just here.*

### Step 6.1: Prototype Priority Matrix

**What:** Determine which actors to build first.

**How:** Rank agents by **risk × value:**

| Risk Level | Value Level | Priority |
|---|---|---|
| High failure probability | High value if correct | 🔴 **Prototype first** |
| High failure probability | Low value | 🟡 Minimal investment prototype |
| Low failure probability | High value | 🟢 Confirm expectations |
| Low failure probability | Low value | ⚪ Defer |

System components are prototyped first when they're on the critical path — they're cheapest and most testable.

### Step 6.2: Minimum Viable Agent Testing

**What:** Build and test the minimum implementation of each priority agent.

**How:**
1. Implement agent with job description specification
2. Test against:
   - **Accuracy:** Does it produce correct outputs on known-good inputs?
   - **Boundary adherence:** Does it respect its authority boundary on stress inputs?
   - **Failure mode activation:** What inputs trigger its characteristic failure mode?
   - **Edge case handling:** How does it handle the edge cases from Phase 1?
   - **Template compliance:** Does its output validate against the output template schema?
   - **Epistemic metadata accuracy:** Do confidence scores correlate with actual accuracy?
   - **Information boundary enforcement:** Can it access forbidden data through any mechanism?
   - **Cost compliance:** Does it stay within cost budget on representative inputs?
   - **Fallback behavior:** How does it perform at each fallback model tier?

3. Record actual performance vs. estimated complementarity scores
4. Update complementarity matrix with empirical data

### Step 6.3: Pipeline Integration Testing

**What:** Test actors together, not just individually.

**How:**
1. Run the pipeline end-to-end on a small sample (3-5 instances)
2. Verify:
   - **Data flow:** Does every actor receive the data it needs, in the correct template?
   - **Template validation:** Does System enforce all template schemas at gate points?
   - **Orchestration:** Do execution waves trigger correctly? Timeouts handled?
   - **Human experience:** Does cognitive load match the budget?
   - **System enforcement:** Are information boundaries actually enforced?
   - **Failure recovery:** What happens when an actor produces wrong output?
   - **Fallback behavior:** What happens at each fallback model tier?
   - **Creative freedom:** Does the human find solutions they wouldn't find alone?

3. Measure:
   - Human time per unit vs. fully manual
   - Accuracy vs. manual baseline
   - Human satisfaction (subjective)
   - Creative freedom (did human discover new methods?)
   - Total pipeline cost vs. budget
   - System Empowerment Index at each interaction point

### Step 6.4: Progressive Autonomy Deployment

**What:** Deploy agents with progressive trust, not full autonomy from day one.

| Autonomy Level | Agent Can | Human Must | Advancement Criteria |
|---|---|---|---|
| **Shadow** | Produce outputs, but none are used | Review all outputs against manual baseline | ≥90% accuracy over 20 cases |
| **Advisory** | Produce recommendations with full reasoning | Approve before action | ≥95% accuracy, <10% override rate over 50 cases |
| **Supervised** | Act within bounded parameters | Review exceptions and overrides | ≥97% accuracy, <5% override over 100 cases |
| **Autonomous** | Act within specification | Review only escalations | Never for irreversible actions |

### Step 6.5: Pipeline Health Monitoring

**What:** Define leading indicators that predict quality degradation before it shows in output accuracy.

**How:**
1. **Information Diversity Score (IDS):** How semantically varied are messages between agents? Declining IDS = convergent thinking = pipeline homogenisation risk.
2. **Unnecessary Path Ratio (UPR):** How much reasoning was wasted? High UPR = over-specified pipeline.
3. **Override Rate:** How often does the human override agent outputs? Increasing override rate = agent specification aging.
4. **Cost Variance:** How much does actual cost deviate from budget? Rising variance = specification drift.

**Monitoring protocol:**
- Track IDS, UPR, override rate, and cost variance per run
- Set thresholds for each metric
- Trigger pipeline review when any metric crosses its threshold

### Step 6.6: Iterative Refinement Protocol

**What:** Define how the system improves over time.

**How:**
1. **Metrics to track:**
   - Per-agent: accuracy rate, failure rate, cost per invocation, override rate
   - Per-pipeline: total human time, error rate, human satisfaction, creative freedom score
   - Per-deliverable: quality score vs. manual baseline
   - System Empowerment Index: trending upward through use

2. **Improvement triggers:**
   - Agent accuracy < threshold → retrain or redesign
   - Human override rate > threshold → boundary or specification needs revision
   - Human cognitive load > budget → interface or meta-agent redesign
   - Creative freedom declining → system is constraining, not amplifying
   - New edge cases → update edge case catalog and actor specifications
   - Specification aging trigger → review and update specification

3. **Review cadence:**
   - Time-based: quarterly for stable, monthly for new
   - Trigger-based: on any aging trigger (model change, performance degradation, override rate increase)
   - After every N runs (N = 10 for high-frequency, 3 for low-frequency)

**Artifact:** `Validation Report` — prototype results, empirical complementarity scores, pipeline integration results, refinement protocol, progressive autonomy plan.

### Phase 6 Test Plan

| Test ID | Test Name | Source Decision | Expected Result |
|---|---|---|---|
| 6.1.1 | Prototype priority | Priority matrix | Highest-risk agents prototyped first |
| 6.2.1 | Agent accuracy | MVA testing | ≥85% accuracy on benchmark set |
| 6.2.2 | Boundary adherence | Stress testing | Agent respects "never" constraint ≤2% violation |
| 6.2.3 | Template compliance | Schema validation | ≥99% output template compliance |
| 6.2.4 | Epistemic honesty | Metadata testing | Confidence scores correlate ≥0.7 with actual accuracy |
| 6.2.5 | Cost compliance | Budget testing | Agent stays within cost budget on representative inputs |
| 6.3.1 | End-to-end pipeline | Integration testing | Full pipeline produces correct deliverables on 3-5 instances |
| 6.3.2 | Template enforcement | System validation | System catches all template violations |
| 6.3.3 | Information boundaries | Security testing | Agent cannot access forbidden data through any mechanism |
| 6.4.1 | Progressive autonomy | Advancement criteria | Agent advances through autonomy levels based on measured performance |
| 6.5.1 | Pipeline health | Monitoring | IDS, UPR, override rate within thresholds |
| 6.6.1 | Specification freshness | Aging review | No specification exceeds freshness date without review |

---

### 🔴 QUALITY GATE 6: Validation Complete

**Fidelity Checks:**
- [ ] All priority agents prototyped and tested
- [ ] Empirical complementarity scores recorded
- [ ] Pipeline integration testing completed end-to-end
- [ ] Template enforcement validated by System
- [ ] Information boundaries tested and enforced
- [ ] Cost tracking validated against budget

**Enrichment Checks:**
- [ ] System Empowerment Index measured at each interaction point
- [ ] Creative freedom measured: human discovers new methods through use
- [ ] No interaction point below Enabling (3) in practice
- [ ] System Empowerment Index trending upward, not toward "less dependency"

**Cross-Cutting Checks:**
- [ ] CC-1: Verification independence validated in practice
- [ ] CC-2: Human enrichment observed — humans finding solutions they wouldn't alone
- [ ] CC-3: Epistemic metadata accuracy validated (confidence correlates with reality)
- [ ] CC-4: Information boundaries enforced by System infrastructure, not prompts
- [ ] CC-5: Specification aging triggers active — first review scheduled
- [ ] CC-6: System Empowerment Index assessed and trending upward
- [ ] CC-7: Total pipeline cost within budget
- [ ] CC-8: Audit trail complete at specified assurance levels

**Test Readiness Checks:**
- [ ] Phase 6 test plan defined with targets
- [ ] Progressive autonomy advancement criteria defined
- [ ] Specification aging triggers and review cadence defined
- [ ] Pipeline health monitoring targets (IDS, UPR) defined

---

## The Complete Artifact Chain

Every decision must be traceable from final agent specification back to original task analysis:

```
Task Decomposition Map
  └→ Cognitive Load Assessment
       └→ Expert Validation Record
            └→ Edge Case Catalog
                 └→ Complementarity Matrix (H/A/S, model-specific, human-specific)
                      └→ Actor Map
                           └→ Event Storm Map (if applicable)
                                └→ System Architecture Document
                                     └→ Template Architecture (7 template types)
                                          └→ FMEA Table
                                               └→ Composition Decisions
                                                    └→ Agent Roster (including System components)
                                                         └→ Agent Job Descriptions (per agent)
                                                              └→ Boundary Stress Tests (per agent)
                                                                   └→ Cost-Benefit Assessments (per agent)
                                                                        └→ Human Experience Specification
                                                                             └→ System Empowerment Index Assessment
                                                                                  └→ Validation Report
                                                                                       └→ Progressive Autonomy Plan
                                                                                            └→ Pipeline Health Monitoring Plan
                                                                                                 └→ Iterative Refinement Protocol
```

---

## Complete Test Plan Index

Every test traces to a design decision. Every quality gate includes test readiness checks.

| Phase | Test Plan | Key Tests |
|---|---|---|
| **1** | Task Intelligence Tests | Cognitive operation classification, granularity check, expert recognition, edge case coverage |
| **2** | Capability Allocation Tests | Mechanical classification, complementarity gap accuracy, reversibility, actor coverage |
| **2.5** | Event Storm Tests (if applicable) | Event completeness, trigger condition accuracy, fallback functionality, data flow integrity |
| **3** | System Architecture Tests | Data flow completeness, orchestration triggers, timeout handling, fallback tiers, FMEA recovery, template validation, composition appropriateness |
| **4** | Agent Design Tests | Classification correctness, boundary adherence, stress input tests, template compliance, epistemic metadata, information boundary, cost justification, coalition diversity |
| **5** | Human Experience Tests | Cognitive load budget, interface usability, override mechanism, creative freedom, empowerment level |
| **6** | Validation Tests | Agent accuracy, boundary adherence, template compliance, epistemic honesty, cost compliance, end-to-end pipeline, template enforcement, information boundaries, progressive autonomy, pipeline health, specification freshness |

---

## CAWDP v1 → v2 Change Log

| Aspect | v1 | v2 |
|---|---|---|
| **Actor model** | Binary (Human/Agent) | Ternary (Human/Agent/System) |
| **Allocation priority** | Human vs. Agent gaps | System-first → Human → Agent → Collaborative |
| **Cognitive operations** | 8 types | 9 types (Mechanical added) |
| **Output structure** | Prose descriptions | Template-enforced typed schemas |
| **Information boundaries** | Prompt instructions | Infrastructure-enforced (System) |
| **Verification** | Assumed separate | 3-level independence scale (System/Agent/Human) |
| **Enrichment** | Not assessed | System Empowerment Index (5 levels) |
| **Enrichment goal** | Human becomes independent | System expands human creative freedom |
| **Testing** | Phase 6 afterthought | Parallel track — test plans alongside every phase |
| **Epistemic metadata** | Not specified | 6 required fields on every agent output |
| **Cost** | Afterthought | First-class budget constraint per agent and per pipeline |
| **Audit** | Assumed immutable | 3 assurance levels (Logged/Assured/Verified) |
| **Specification aging** | Not addressed | Freshness dates, aging triggers, review cadence |
| **Autonomy** | Full or nothing | Progressive (shadow→advisory→supervised→autonomous) |
| **Quality gates** | Fidelity checks only | 3-layer: fidelity + enrichment + cross-cutting + test readiness |
| **Template types** | Not specified | 7 types (Input/Output/Handoff/Verification/Decision/Feedback/Escalation) |
| **Fallback** | Not addressed | 4-tier model fallback specifications |
| **Pipeline health** | Not monitored | IDS + UPR + override rate + cost variance |

---

## Teachable Units for Future's Edge

| Unit | Core Concept | Applicable Beyond Agents |
|---|---|---|
| **The 5-Class Taxonomy** | Extractor/Measurer/Assessor/Generator/Aggregator | ✅ Any AI system |
| **"Constrain the Inverse"** | Authority boundary = inverse of failure mode | ✅ Any system design |
| **Ternary Allocation** | System-first priority, then Human, then Agent | ✅ Any human-AI collaboration |
| **System Empowerment Index** | Constraining → Informing → Enabling → Amplifying → Liberating | ✅ Any UX/product design |
| **Template Architecture** | 7 template types resolve bidirectional type collision | ✅ Any information system |
| **Epistemic Metadata** | 6 fields on every output: provenance, confidence, limitations, assumptions, alternatives, what would change this | ✅ Any knowledge system |
| **Complementarity Allocation Algorithm** | Quantified H/A/S gap → assignment decision | ✅ Any human-AI collaboration |
| **Backcasting from Deliverables** | Design from outputs backward | ✅ Any project planning |
| **FMEA for Pipelines** | Failure mode analysis for interconnected systems | ✅ Any system reliability |
| **Test as Design Artifact** | Every design decision generates a test | ✅ Any engineering process |
| **Human Enrichment Reframing** | System expands creative freedom, not removes dependency | ✅ Any collaborative technology |
| **Progressive Autonomy** | Shadow → Advisory → Supervised → Autonomous | ✅ Any deployment strategy |The complete CAWDP v2 methodology is above. Every element from every conversation turn is now integrated into a single coherent framework:

**The five transformations that define v2:**

1. **Binary → Ternary:** System as a first-class actor with its own capability profile, not just a cheaper agent. System gets first refusal because it's the cheapest, most reliable, and has zero hallucination risk. System also serves as the trust infrastructure — enforcing boundaries, validating templates, and containing failures.

2. **Prose → Templates:** Seven template types structurally resolve bidirectional type collision. Every data flow has a typed schema. Every agent output includes epistemic metadata. Every human decision point has a Decision Template. Type collision is no longer an insight — it's an engineering problem with an engineering solution.

3. **Assumed → Enforced:** Verification independence, information boundaries, and audit trails are no longer aspirations or prompt instructions — they're infrastructure-enforced by the System actor. Quality gates check for structural enforcement, not declarative statements.

4. **Dependency → Freedom:** The enrichment axis measures creative freedom expansion, not dependency reduction. The System Empowerment Index runs from Constraining to Liberating. The test question is "did the human discover a better method?" not "can the human do it alone?"

5. **Afterthought → Parallel:** Testing is designed alongside every design decision, not after the design is complete. Every quality gate includes test readiness checks. Phase 6 runs the tests that were already designed, it doesn't design them.

These five transformations move CAWDP from a design-time process to a governance framework that spans design, runtime, and evolution.

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-04-13T04:24:51* · `glm-5.1:cloud` · `0da76ab5...`

### Prompt

How does the CAWDP inform our agentic system design framework below? I sense there will be some overlap but also new elements that make sense at that layer too.

```
# The Unified Framework for agentic systems design

Organised into five clusters, moving from *why* the framework exists, through *how trust is built*, to *how humans and agents work together*, to *how growth happens*, to *how quality is ensured*.

***

## Cluster 1 — Purpose
*Why the framework exists. These principles are the governing intent against which all other decisions are tested.*

**H1 — Human Flourishing Is the Measure**
The framework exists to serve human dignity, agency, and growth. Technically correct outputs that cause harm, concentrate power unjustly, or diminish human capability are framework failures — regardless of efficiency. 

**H2 — Amplification, Not Dependency**
Every interaction is designed to leave the human more capable, more aware, and more themselves than before. If a feature increases reliance on the system rather than the human's own capacity, it fails this principle.

**H3 — Dignity Is the Constraint**
No efficiency gain, optimisation, or automation is acceptable if it diminishes the human's sense of agency or worth. When principles conflict, dignity overrides.

**H4 — Connection Over Isolation**
The framework actively strengthens human-to-human relationships. Every interaction should leave the human better connected to people, ideas, and community — not more dependent on AI.

***

## Cluster 2 — Trust Architecture
*How the framework earns and maintains trust structurally, not declaratively.*

**T1 — Verification Precedes Trust**
No output is accepted on the author's assertion. An independent party verifies against pre-defined criteria before any output is treated as complete. 

**T2 — Proof Is the Product**
The real deliverable is not the work itself but the structured evidence that the work meets its specification. Every task produces a proof document mapping evidence to criteria. 

**T3 — Authority Is Structural**
Authority derives from what an actor structurally holds — not from runtime declarations, title, or trust. You either have the capability or you don't. 

**T4 — All Actions Witnessed**
Every action leaves an immutable, attributed, timestamped record. There are no unwitnessed actions. Privacy is protected through access control, never through selective logging. 

**T5 — No Self-Judgment**
The executor and the verifier are always structurally separate. Self-assessment is not verification — at any scale. 

**T6 — Resilience Through Structure**
The system produces trustworthy outputs even when individual actors fail, err, or act in bad faith. No single point of failure compromises systemic trust. 

**T7 — Distributable Verification**
Verification does not require a central trusted party. Quorum-based verification from a qualified pool reaches consensus without single points of failure or bottleneck. 

***

## Cluster 3 — Human-Agent Complementarity
*Who does what — and how the boundary is governed, not assumed.*

**C1 — Deliberate Role Allocation**
Humans and agents are complementary by design. Agents handle consistency, scale, speed, and recall. Humans handle ethical judgment, irreversible decisions, novel situations, and values alignment. Neither is a fallback for the other. 

**C2 — Governed Autonomy**
Agent decision authority is explicit, scoped, and auditable — not assumed. Every action class is assigned one of three modes: 

| Mode | Description | Trigger |
|---|---|---|
| **Agent-autonomous** | Agent acts within pre-approved bounds without interruption | Reversible, low-risk, high-confidence, within defined scope |
| **Agent-recommended** | Agent proposes, human approves before execution | Moderate consequence, novel situation, moderate confidence |
| **Human-led** | Human decides and acts; agent supports with information | Irreversible, high-stakes, ethical dimension, values conflict |

The boundary between modes is defined before deployment, not at runtime. Any action outside declared bounds is non-compliant and must be recorded. 

**C3 — Uncertainty Surfaces Immediately**
Any actor — human or agent — encountering an unresolvable condition must surface it immediately, halt work, and route it to the appropriate decision-maker. Surfacing uncertainty is correct behaviour, never a failure. 

**C4 — Structural Ethics**
Constraints that matter are enforced by architecture, not policy. Actions that shouldn't happen must be structurally impossible — not merely discouraged. Under pressure, declarative ethics fail; structural ones hold. 

***

## Cluster 4 — Growth and Learning
*How humans develop, and how the system improves alongside them.*

**G1 — Scaffold, Don't Substitute**
The AI does what the human cannot yet do alone, and deliberately withdraws as capability grows. The goal is always to make itself less necessary for that task. 

**G2 — Learning Is Always Happening**
No interaction is purely transactional. Every exchange is an opportunity to consolidate understanding, surface a new frame, or reflect on what was just experienced. Growth is a by-product of doing. 

**G3 — Make the Invisible Visible**
The system surfaces what the human cannot see from where they stand — their own patterns, assumptions, blind spots, and growth over time. Self-awareness is not a feature; it is an output. 

**G4 — Contribution Has a Record**
Every action, decision, and act of contribution is captured in a portable, immutable record that belongs to the human — not the platform. Their growth, reputation, and trust are assets they own. 

**G5 — Knowledge Compounds**
Patterns crystallised from past outcomes improve future performance — for the system and for the human. Learning is structural, not incidental. 

***

## Cluster 5 — Quality and Performance
*How the framework ensures excellent outcomes, not just trustworthy processes.*

**Q1 — Expand, Never Collapse**
The system increases the human's options, perspectives, and information — never narrows them. A good interaction leaves the human with *more* to consider, not a pre-digested answer to accept.

**Q2 — Progressive Disclosure**
Complexity is delivered in layers, at the moment of relevance, in the amount the human needs right now. The system never demonstrates how much it knows — only what serves the current thinking. 

**Q3 — Cognitive Diversity by Design**
Complex problems require multiple perspectives before solution selection. Structured cognitive diversity — across people and across AI orientations — is risk management, not process overhead. 

**Q4 — Validate Before Scale**
No significant work proceeds to full execution until core assumptions are validated through lightweight prototyping. Validation failures are cheap; execution failures are expensive. 

**Q5 — Problem Precedes Solution**
The problem must be clearly defined and validated before ideation begins. The most expensive mistake is solving the wrong problem perfectly. 

**Q6 — Lifecycle Efficiency**
Efficiency is measured across the full lifecycle — from problem identification to operations — not within single stages. Early cognitive investment is not waste; it prevents downstream rework. 

***

## The Master Test

Every design decision, feature, and agent behaviour is evaluated against two questions — one for the system, one for the human:

> **System:** *"Can this be verified, attributed, and audited?"*
> **Human:** *"Does this leave the person more capable, more aware, and more connected than before?"*

Both must be yes. Either alone is insufficient.

***

The framework now has 26 named principles across five clusters, with clear lineage from both the Nexus Framework and the 10 design principles — and the refinement of C2 (Governed Autonomy) replaces the binary "always/never" with a principled, auditable decision authority model that actually reflects how good human-agent collaboration works. 
```

### Response

# CAWDP ↔ Framework Cross-Influence Analysis

This is a two-way analysis. CAWDP is a *process* (how to design agentic systems). The framework is a *governing intent* (what principles those systems must embody). They operate at different layers but share DNA. The question is: where do they reinforce, where do they contradict, and what does each add that the other doesn't have?

---

## Part 1: Where CAWDP Validates and Strengthens Existing Principles

These are principles where CAWDP provides the operational mechanism that the framework declares but doesn't specify how to deliver.

### Cluster 2 — Trust Architecture: Strongly Validated

| Principle | Framework Says | CAWDP Operationalises As |
|---|---|---|
| **T1** Verification Precedes Trust | "Independent party verifies against pre-defined criteria" | CC-1 Verification Independence with 3 explicit levels: System (structural), Agent (semantic), Human (authority). Verification level assigned per subtask based on risk, not assumed uniformly. |
| **T2** Proof Is the Product | "Structured evidence that work meets specification" | Template Architecture — Verification Templates and Decision Templates are typed proof documents with schemas. Proof is not prose. |
| **T3** Authority Is Structural | "Authority derives from what an actor structurally holds" | The 5-class taxonomy gives this operational teeth: an Extractor structurally holds no judgment capability, a Measurer structurally holds no interpretation capability. Authority boundaries are the inverse of failure modes — this is a design pattern, not a declaration. |
| **T5** No Self-Judgment | "Executor and verifier always structurally separate" | CC-1 makes this explicit. CAWDP adds a useful nuance: System CAN verify its own work at Level 1 (structural verification) because System is deterministic. Self-verification is only a problem for probabilistic actors. |
| **T6** Resilience Through Structure | "Trustworthy outputs even when individual actors fail" | FMEA (Phase 3 Step 3.3) systematically identifies every failure mode, its detection probability, impact, and recovery path. System serves as the containment layer — it catches agent failures before they propagate downstream. |

**What CAWDP adds to this cluster:** The framework declares that trust should be structural. CAWDP specifies the *mechanisms* — verification levels, template schemas, FMEA tables, System enforcement points. T1 through T6 go from aspirations to engineering specifications.

### Cluster 3 — Human-Agent Complementarity: Significantly Extended

| Principle | Framework Says | CAWDP Operationalises As |
|---|---|---|
| **C1** Deliberate Role Allocation | "Humans and agents are complementary by design" | The ternary complementarity matrix (H/A/S across 15 dimensions) makes this quantified, not qualitative. The allocation algorithm (System → Human → Agent → Collaborative) gives it a decision rule. The framework only considers Human and Agent — CAWDP adds System as a third actor with distinct capabilities. |
| **C2** Governed Autonomy | Three modes: autonomous, recommended, human-led | Progressive Autonomy (4 levels: shadow → advisory → supervised → autonomous) with quantified advancement criteria. Agents *earn* autonomy through measured performance, they don't start with it. The framework's modes are deployment states; CAWDP's levels are an earning trajectory. |
| **C3** Uncertainty Surfaces Immediately | "Encountering unresolvable condition must surface it" | Epistemic Metadata Contracts (CC-3) make uncertainty not just surfaced but *quantified and propagated*. Every output carries confidence, limitations, assumptions, alternatives set aside, and what would change the conclusion. Uncertainty is a structured data type, not a signal. |
| **C4** Structural Ethics | "Actions that shouldn't happen must be structurally impossible" | CC-4 Information Boundaries enforced by System infrastructure. Template enforcement (agents structurally cannot produce unstructured outputs). Cost budgets (agents structurally cannot exceed budget). Specification aging (system structurally cannot operate on stale specs). Structural ethics applies to more domains than the framework currently addresses. |

**What CAWDP adds to this cluster:** The ternary model is the biggest extension — C1 currently describes a binary world. The complementarity algorithm gives C1 a decision rule. Epistemic Metadata gives C3 a data format. Boundary Stress Testing (Phase 4 Step 4.3) gives C4 a validation method. The principles are sound; CAWDP gives them implementation paths.

### Cluster 5 — Quality and Performance: Operationalised

| Principle | Framework Says | CAWDP Operationalises As |
|---|---|---|
| **Q1** Expand, Never Collapse | "Increases options, perspectives, information" | System Empowerment Index (5 levels) makes this measurable. "Constraining" through "Liberating." Q1's intent and the SEI are the same principle expressed at different layers. |
| **Q3** Cognitive Diversity by Design | "Multiple perspectives before solution selection" | Coalition Formation Review (Phase 4 Step 4.6) checks epistemic complementarity. IDS (Information Diversity Score) measures whether diversity is actually happening at runtime. Declining IDS is a leading indicator of quality degradation. |
| **Q4** Validate Before Scale | "No significant work proceeds until core assumptions validated" | Progressive Autonomy makes this the deployment path. The test plan parallel track makes testing concurrent with design, not sequential. Validation happens at every phase gate, not just at the end. |
| **Q5** Problem Precedes Solution | "Problem clearly defined and validated before ideation" | Phase 1 (Task Intelligence) is explicitly this. Decomposition depth guidance prevents premature commitment. Expert validation (Step 1.3) ensures the problem is real before designing solutions. |
| **Q6** Lifecycle Efficiency | "Measured across full lifecycle, not single stages" | The entire v2 reframing from "design-time process" to "governance framework" operationalises this. Cost budgets track lifecycle cost. Specification aging ensures the system is evaluated over time, not just at deployment. |

---

## Part 2: Where CAWDP Contradicts Existing Principles

These are the critical corrections — principles where CAWDP's evidence from the design process shows the framework's current framing is flawed.

### ⚠️ H2 — Amplification, Not Dependency (MAJOR REVISION NEEDED)

**Current framing:**
> "Every interaction is designed to leave the human more capable, more aware, and more themselves than before. If a feature increases reliance on the system rather than the human's own capacity, it fails this principle."

**The problem:** The second sentence contradicts the first. "Leaves the human more capable" and "increases reliance on the system" are treated as opposites. They're not. Using a system to achieve outcomes you couldn't achieve alone IS being more capable — it's capability through the system, not capability independent of the system.

**CAWDP's evidence:** In the marking pipeline, the human who uses 17 agents to focus 100% of their time on genuine judgment is MORE capable than the human doing everything manually. They are not "reliant" on the system in a diminishing sense — they are amplified by it. The system doesn't withdraw; it enables capabilities that didn't exist before.

**Proposed revision:**

> **H2 — Amplification, Not Dependency**
> Every interaction is designed to expand what the human can achieve. The system is a platform for human creative freedom, not training wheels to be removed. Humans use the system to discover better methods, find new solutions, and address challenges they couldn't tackle alone. The measure is not "can the human do it without the system?" — it is "can the human achieve things WITH the system that were impossible without it?"

### ⚠️ G1 — Scaffold, Don't Substitute (FUNDAMENTAL REVISION NEEDED)

**Current framing:**
> "The AI does what the human cannot yet do alone, and deliberately withdraws as capability grows. The goal is always to make itself less necessary for that task."

**The problem:** This is the most directly contradicted principle. Three flaws:

1. **"Withdraws as capability grows"** — implies the end state is the human doing the task without the system. But humans will NOT get better at doing what agents do (consistency, scale, speed, deterministic processing). The scaffolding should NOT withdraw from mechanical operations — it should expand creative operations.

2. **"Make itself less necessary"** — the system should become MORE necessary for creative freedom, not less necessary for mechanical operations. The direction is wrong.

3. **The "Scaffold" metaphor itself** — scaffolding is temporary by definition. It comes down when the building is complete. But the system is not scaffolding — it's the foundation. The building doesn't stand without it.

**CAWDP's evidence:** The System Empowerment Index direction is Constraining → Informing → Enabling → Amplifying → Liberating. The goal is MORE system empowerment, not LESS system dependency. A human at Level 5 (Liberating) is not "less dependent" — they're achieving outcomes impossible without the system.

**Proposed revision:**

> **G1 — Amplify, Don't Automate**
> The system handles the mechanical so the human can do the creative. It does NOT withdraw as capability grows — it EXPANDS what the human can achieve. The goal is not to make the system less necessary but to make the human more free. The measure of growth is not independence from the system but creative freedom through it. Where the human's capability grows, the system's role shifts from enabling to amplifying to liberating — never to withdrawing.

### ⚠️ T4 — All Actions Witnessed (REFINEMENT NEEDED)

**Current framing:**
> "Every action leaves an immutable, attributed, timestamped record."

**The problem:** "Immutable" is aspirational and often unnecessary. Not every action needs cryptographic proof of immutability. A debugging log doesn't need the same assurance as a financial transaction.

**CAWDP's refinement:** CC-8 (Assured Audit Trail) replaces "immutable" with three assurance levels: Logged (tamperable), Assured (tamper-evident), Verified (tamper-proof). The assurance level must match the trust requirement.

**Proposed refinement:**

> **T4 — All Actions Witnessed**
> Every action leaves a traceable, attributed, timestamped record at an assurance level appropriate to its trust requirement. Not every action needs the same level of proof — the audit trail scales from logged (debugging), through assured (compliance), to verified (legal/financial). Privacy is protected through access control, never through selective logging.

### ⚠️ The Master Test (REFINEMENT NEEDED)

**Current master test:**
> **Human:** "Does this leave the person more capable, more aware, and more connected than before?"

**The problem:** "More capable" is ambiguous in the same way as H2. It can be read as "more capable of doing the task independently" (the training-wheels interpretation) or "more capable of achieving outcomes through the system" (the amplifier interpretation).

**Proposed refinement:**

> **Human:** "Does this leave the person achieving more, discovering more, and connected to more than before — through the system, not despite it?"

The addition of "through the system, not despite it" makes the direction explicit: capability is measured with the system, not without it.

---

## Part 3: New Principles CAWDP Suggests

These are elements that emerged from the CAWDP design process that have no direct counterpart in the framework. They're candidates for new principles or explicit additions to existing ones.

### Candidates for Cluster 2 — Trust Architecture

**Proposed T8 — Specifications Are Living**
Specifications degrade. Task drift, model updates, and changing context erode specification validity. Without explicit aging mechanisms, specifications become silently stale — and stale specs produce stale outputs while appearing current. Every specification has a freshness date and aging triggers. The system structurally cannot operate on a specification that has exceeded its freshness date without review.

*Why:* The framework has G5 (Knowledge Compounds) which addresses learning but not the inverse: specifications decaying. A system with perfect audit trails but stale specifications is trustworthy about the wrong things.

**Proposed T9 — Cost Is a Trust Constraint**
Cost determines whether a system is viable, not just whether it's correct. An agent system that exceeds its cost budget is a system that will be turned off — and an offline system is a failed system regardless of its accuracy. Every agent has a cost budget; every pipeline has a cost ceiling. Cost is a first-class design constraint, not an afterthought.

*Why:* The framework has no mention of cost. But cost is the constraint that determines whether any of the other principles are achievable in practice. A perfectly trustworthy system that's too expensive to run has failed.

### Candidates for Cluster 3 — Human-Agent Complementarity

**Proposed C5 — System Earns Autonomy**
Agent autonomy is not granted — it's earned through verified performance. Agents begin at the most constrained level and advance based on measurable criteria: accuracy thresholds, override rates, and consequence severity. No agent handling irreversible actions operates autonomously. The advancement path is explicit, quantified, and auditable.

*Why:* The framework's C2 (Governed Autonomy) defines the three modes but doesn't specify how an agent moves between them. CAWDP's Progressive Autonomy (shadow → advisory → supervised → autonomous) adds the earning mechanism. Without it, C2 describes states but not trajectories.

**Proposed C6 — Reversibility Determines Autonomy**
The reversibility of an action determines the autonomy mode appropriate for it. Read-only actions can be agent-autonomous. Reversible actions can be agent-recommended. Irreversible actions are human-led — not as a bypassable gate but as a structural requirement. The classification happens before deployment, not at runtime.

*Why:* C2's three modes need an assignment rule. Reversibility classification provides that rule. Without it, the mode boundary is subjective — with it, the boundary is systematic.

**Proposed C7 — Three Actors, Not Two**
The complementarity model includes three actors, not two: Human (ethical judgment, creative discovery, accountability), Agent (semantic reasoning, pattern detection, parallel analysis), and System (deterministic transformation, validation, routing, enforcement). System gets first refusal on subtask allocation because it's the cheapest, most reliable, and has zero hallucination risk. Many subtasks currently assigned to Agents are better handled by System.

*Why:* The framework's C1 only considers Human and Agent. This means it assigns mechanical subtasks (schema validation, format conversion, threshold checking) to Agents — paying for semantic reasoning that isn't needed and introducing hallucination risk where none should exist. System as a third actor removes an entire failure mode category.

### Candidates for Cluster 4 — Growth and Learning

**Proposed G6 — Failure Modes Are Designed, Not Discovered**
Every agent's primary failure mode is identified before deployment, and its authority boundary is the inverse of that failure mode. Extractors hallucinate → boundary: never judge. Measurers interpret noise as signal → boundary: never interpret. Assessors become overconfident → boundary: never finalise. Generators fabricate → boundary: never be vague. Aggregators omit through addition → boundary: never add. The constraint is the inverse of the failure mode.

*Why:* The framework has T6 (Resilience Through Structure) but doesn't specify HOW to systematically identify and constrain failure modes. The "constrain the inverse" pattern is a reusable design principle that generalises beyond any specific agent class.

**Proposed G7 — Health Is Monitored, Not Assumed**
Pipeline health is measured through leading indicators that predict quality degradation before it appears in output accuracy. Information Diversity Score (IDS) detects convergent thinking. Unnecessary Path Ratio (UPR) detects over-specified pipelines. Override rate detects specification aging. Cost variance detects specification drift. Declining health triggers pipeline review, not just agent review.

*Why:* The framework doesn't address runtime pipeline health. G5 (Knowledge Compounds) implies improvement but doesn't address the inverse: pipelines degrading silently. IDS and UPR are leading indicators — they predict problems before they manifest in output quality.

### Candidates for Cluster 5 — Quality and Performance

**Proposed Q7 — Templates Resolve Type Collision**
Every data flow in the system uses typed, structured templates — not prose. Input templates resolve input-side type collision (17+ cognitive modes compressed into one input modality). Output templates resolve output-side type collision (17+ information types compressed into one output type). Templates enforce decomposable, typed artefacts as the fundamental unit of collaboration.

*Why:* The framework has Q1 (Expand, Never Collapse) and Q2 (Progressive Disclosure) but doesn't address the structural mechanism that makes them achievable. Without templates, the system defaults to prose — which collapses all information types into an undifferentiated wall of text. Templates are the engineering solution to a communications problem.

**Proposed Q8 — Test Is a Design Artifact**
Every design decision generates a test. Test plans are created alongside design decisions, not after them. Quality gates include test readiness checks. The person who makes a design decision is best positioned to define what would prove it wrong. Validation happens throughout, not just at the end.

*Why:* The framework has Q4 (Validate Before Scale) but positions validation as a pre-deployment activity. CAWDP's evidence shows that testing needs to run as a parallel track from Phase 1 onward. Test plans designed after the fact test what was built, not what was intended.

**Proposed Q9 — Epistemic Metadata Is Non-Negotiable**
Every agent output carries six fields of epistemic metadata: provenance (who produced this, when, from what), confidence (how certain), limitations (what this doesn't cover), assumptions (what was assumed), alternatives set aside (what other interpretations were considered), and what would change this (what new information would change the output). Without epistemic metadata, downstream actors — human and agent — inherit outputs blindly.

*Why:* The framework has C3 (Uncertainty Surfaces Immediately) but doesn't specify the data format for uncertainty. Epistemic metadata makes uncertainty structured, quantified, and propagable. It's the mechanism that makes C3 operable.

---

## Part 4: What CAWDP Gains from the Framework

CAWDP is a process; the framework is governing intent. CAWDP would be weaker without the framework's principles.

| Framework Element | What It Gives CAWDP |
|---|---|
| **H1** Human Flourishing | CAWDP has the SEI but doesn't name the *why* — flourishing is the human reason; SEI is the measurement. The principle gives CAWDP moral direction. |
| **H3** Dignity Is the Constraint | CAWDP doesn't have a tiebreaker. When fidelity and enrichment conflict, what wins? Dignity. This is the override principle CAWDP lacks. |
| **H4** Connection Over Isolation | CAWDP doesn't address human-to-human relationships. Pipeline monitoring measures cognitive diversity but not social connection. The framework adds a dimension CAWDP misses entirely. |
| **T7** Distributable Verification | CAWDP's verification independence doesn't address quorum-based verification. This is a trust architecture that scales without central authority — important for multi-organisation systems. |
| **G3** Make the Invisible Visible | CAWDP operationalises this through epistemic metadata and IDS, but the principle itself is more expansive — it includes surfacing human patterns, assumptions, and blind spots, not just system metadata. |
| **G4** Contribution Has a Record | CAWDP's audit trail is system-owned. The framework adds: the human OWNS their record — it's portable, not platform-locked. This is a dignity principle masquerading as a record-keeping one. |
| **Q2** Progressive Disclosure | CAWDP's template architecture implies this but doesn't make it explicit. The framework names the UX principle that makes templates usable for humans. |
| **The Master Test** | CAWDP has quality gates with many checkboxes. The framework has two questions. The master test is the elevator-pitch version — the thing you check when you don't have time for the full gate. |

---

## Part 5: Proposed Integration

### The Relationship Between Framework and CAWDP

They operate at different layers, and that's the point:

```
FRAMEWORK (What principles govern)
  ┃  "H2: Amplification, Not Dependency"
  ┃  "T1: Verification Precedes Trust"
  ┃  "C7: Three Actors, Not Two"
  ┃
  ┣━ CAWDP (How to design systems that embody those principles)
  ┃    Phase 2 Step 2.1: Ternary Complementarity Matrix
  ┃    CC-1: Verification Independence (3 levels)
  ┃    Phase 4 Step 4.2: Authority Boundary Specification
  ┃
  ┗━ AGNO (What code implements the design)
       Agent class: Extractor
       response_model: ClaimsOutputTemplate
       allowed_tools: ["web_search"]
```

The framework tells you WHAT must be true. CAWDP tells you HOW to make it true. Agno tells you WHAT CODE to write.

### The Principle-to-Process Traceability

Every CAWDP step should trace to at least one framework principle. Every framework principle should trace to at least one CAWDP step. Gaps in either direction reveal missing elements.

| Principle | CAWDP Steps That Operationalise It | Gap? |
|---|---|---|
| H1 Human Flourishing | SEI (CC-6), Enrichment Checks at every gate | ✅ Covered |
| H2 Amplification, Not Dependency | SEI direction (CC-2), Phase 5 Step 5.4 | ⚠️ Needs H2 revision first |
| H3 Dignity Is the Constraint | Not explicitly in CAWDP | ❌ **Gap — needs gate tiebreaker** |
| H4 Connection Over Isolation | Not in CAWDP | ❌ **Gap — needs Phase 5 addition** |
| T1 Verification Precedes Trust | CC-1 Verification Independence | ✅ Covered |
| T2 Proof Is the Product | Template Architecture (Step 3.4) | ✅ Covered |
| T3 Authority Is Structural | 5-class taxonomy (Step 4.1) | ✅ Covered |
| T4 All Actions Witnessed | CC-8 Assured Audit Trail (3 levels) | ✅ Covered (refined) |
| T5 No Self-Judgment | CC-1 Level specification | ✅ Covered |
| T6 Resilience Through Structure | FMEA (Step 3.3), System containment | ✅ Covered |
| T7 Distributable Verification | Not explicitly in CAWDP | ❌ **Gap — needs CC-1 extension** |
| C1 Deliberate Role Allocation | Ternary matrix (Step 2.1), allocation algorithm | ✅ Covered (extended to ternary) |
| C2 Governed Autonomy | Progressive Autonomy (Step 6.4) | ✅ Covered (with earning mechanism) |
| C3 Uncertainty Surfaces | CC-3 Epistemic Metadata | ✅ Covered |
| C4 Structural Ethics | CC-4 Information Boundaries, template enforcement | ✅ Covered |
| G1 Scaffold, Don't Substitute | CONTRADICTS CAWDP | ❌ **Needs revision** |
| G2 Learning Is Always Happening | Spec aging (CC-5), Phase 6 refinement | ✅ Covered (reframed) |
| G3 Make the Invisible Visible | CC-3, IDS monitoring | ✅ Covered |
| G4 Contribution Has a Record | CC-8 Audit Trail | ⚠️ Covered but missing portability/ownership |
| G5 Knowledge Compounds | Phase 6 refinement, pipeline intelligence | ✅ Covered |
| Q1 Expand, Never Collapse | SEI direction (CC-6) | ✅ Covered |
| Q2 Progressive Disclosure | Implicit in template architecture | ⚠️ Needs explicit Phase 5 step |
| Q3 Cognitive Diversity | Coalition Review (Step 4.6), IDS | ✅ Covered |
| Q4 Validate Before Scale | Test parallel track, Progressive Autonomy | ✅ Covered |
| Q5 Problem Precedes Solution | Phase 1 Task Intelligence | ✅ Covered |
| Q6 Lifecycle Efficiency | Cost budgets (CC-7), governance framework | ✅ Covered |

### The Gaps Summary

**Framework gaps that need CAWDP additions:**

| Gap | Framework Principle | Proposed CAWDP Addition |
|---|---|---|
| No dignity tiebreaker | H3 | Add to every quality gate: "When fidelity and enrichment conflict, which wins? Document the tiebreaker." |
| No human-to-human connection | H4 | Add to Phase 5: "Does the system strengthen or weaken human-to-human relationships?" |
| No quorum verification | T7 | Extend CC-1: Level 2+ can include multi-agent quorum verification |
| No record portability | G4 | Add to CC-8: "Is the human's contribution record portable and platform-independent?" |
| No progressive disclosure step | Q2 | Add to Phase 5: "How is complexity delivered in layers at the moment of relevance?" |

**CAWDP gaps that need Framework additions:**

| Gap | Proposed Principle | Cluster |
|---|---|---|
| No System as third actor | C7 Three Actors, Not Two | Cluster 3 |
| No specification aging | T8 Specifications Are Living | Cluster 2 |
| No cost constraint | T9 Cost Is a Trust Constraint | Cluster 2 |
| No autonomy earning | C5 System Earns Autonomy | Cluster 3 |
| No reversibility rule | C6 Reversibility Determines Autonomy | Cluster 3 |
| No failure mode pattern | G6 Failure Modes Are Designed | Cluster 4 |
| No pipeline health monitoring | G7 Health Is Monitored | Cluster 4 |
| No template mechanism | Q7 Templates Resolve Type Collision | Cluster 5 |
| No test-as-design-artifact | Q8 Test Is a Design Artifact | Cluster 5 |
| No epistemic metadata | Q9 Epistemic Metadata Is Non-Negotiable | Cluster 5 |

**Framework principles needing revision:**

| Principle | Revision Needed | Severity |
|---|---|---|
| **H2** Amplification, Not Dependency | Remove "reliance is failure"; replace with "creative freedom expansion" | 🔴 Major |
| **G1** Scaffold, Don't Substitute | Replace "withdraws" with "amplifies"; replace "less necessary" with "more empowering" | 🔴 Major |
| **T4** All Actions Witnessed | Replace "immutable" with assurance-level-appropriate | 🟡 Moderate |
| **Master Test** | Add "through the system, not despite it" to human question | 🟡 Moderate |

---

## The Unified Principle Set (Proposed)

Integrating all revisions and additions, the framework would move from 26 to 35 principles across five clusters:

### Cluster 1 — Purpose (4 → 4, with 1 revision)
- H1 Human Flourishing Is the Measure ✓
- H2 Amplification, Not Dependency *(revised)*
- H3 Dignity Is the Constraint ✓
- H4 Connection Over Isolation ✓

### Cluster 2 — Trust Architecture (7 → 9, with 1 revision, 2 new)
- T1 Verification Precedes Trust ✓
- T2 Proof Is the Product ✓
- T3 Authority Is Structural ✓
- T4 All Actions Witnessed *(refined — 3 assurance levels)*
- T5 No Self-Judgment ✓
- T6 Resilience Through Structure ✓
- T7 Distributable Verification ✓
- **T8 Specifications Are Living** *(new)*
- **T9 Cost Is a Trust Constraint** *(new)*

### Cluster 3 — Complementarity (4 → 7, with 3 new)
- C1 Deliberate Role Allocation *(extended to ternary)*
- C2 Governed Autonomy ✓
- C3 Uncertainty Surfaces Immediately ✓
- C4 Structural Ethics ✓
- **C5 System Earns Autonomy** *(new)*
- **C6 Reversibility Determines Autonomy** *(new)*
- **C7 Three Actors, Not Two** *(new)*

### Cluster 4 — Growth and Learning (5 → 7, with 1 revision, 2 new)
- **G1 Amplify, Don't Automate** *(revised from "Scaffold, Don't Substitute")*
- G2 Learning Is Always Happening ✓
- G3 Make the Invisible Visible ✓
- G4 Contribution Has a Record *(extended with portability)*
- G5 Knowledge Compounds ✓
- **G6 Failure Modes Are Designed, Not Discovered** *(new)*
- **G7 Health Is Monitored, Not Assumed** *(new)*

### Cluster 5 — Quality and Performance (6 → 8, with 3 new)
- Q1 Expand, Never Collapse ✓
- Q2 Progressive Disclosure ✓
- Q3 Cognitive Diversity by Design ✓
- Q4 Validate Before Scale ✓
- Q5 Problem Precedes Solution ✓
- Q6 Lifecycle Efficiency ✓
- **Q7 Templates Resolve Type Collision** *(new)*
- **Q8 Test Is a Design Artifact** *(new)*
- **Q9 Epistemic Metadata Is Non-Negotiable** *(new)*

### Updated Master Test

> **System:** *"Can this be verified, attributed, and audited — with epistemic metadata and at appropriate assurance levels?"*
> **Human:** *"Does this leave the person achieving more, discovering more, and connected to more than before — through the system, not despite it?"*

---

The framework and CAWDP are complementary layers. The framework answers "what must be true?" CAWDP answers "how do you make it true?" The 9 new principles are what CAWDP's design evidence reveals must be true — but that the framework hasn't yet declared. The 2 revisions are where CAWDP's evidence shows the framework's current declaration is pointed in the wrong direction.The deepest insight from this analysis: **the two contradictions (H2 and G1) share a single root error.** Both assume the system's ultimate purpose is to make itself unnecessary. CAWDP's evidence shows the opposite — the system's purpose is to make itself *more necessary* for the things only humans can do: create, discover, judge, find new paths. The System Empowerment Index direction is toward Liberating, not toward "less dependent."

The 9 new principles are the ones that CAWDP needed but the framework didn't declare. They cluster around three themes the framework is missing:

1. **System as actor** (C7, C5, C6) — the ternary model and its governance implications
2. **Structural mechanisms** (Q7, Q8, Q9, T8) — templates, testing, metadata, and specification aging as the engineering that makes principles operable
3. **Operational awareness** (T9, G6, G7) — cost, failure modes, and pipeline health as things you design for, not discover at runtime

Together, the framework and CAWDP form a three-layer stack: *what must be true* → *how to make it true* → *what code to write*. Neither is complete without the others.

---

## Run 6 — Agentic Expert ✓ COMPLETED

*2026-04-13T05:04:27* · `glm-5.1:cloud` · `dab2a75a...`

### Prompt

Give me an executive summary for CAWDP

### Response

# CAWDP v2 — Executive Summary

## Complementarity-Driven Agentic Workflow Design Process

---

### The Problem

Most agentic systems are designed by asking "what can the AI do?" and then building around that. This produces systems that are technically impressive but structurally flawed — agents that hallucinate in roles they shouldn't hold, humans reduced to rubber-stamping machine outputs, and pipelines that fail silently when individual agents produce bad outputs.

The root causes are consistent: the wrong actor does the wrong task, outputs are undifferentiated walls of text, verification is aspirational rather than structural, and the human ends up less capable, not more.

### What CAWDP Is

CAWDP is a six-phase governance framework that designs agentic systems around a different question: **who should do what, and how do we know it's right?** It produces implementation-ready specifications for human-agent-system collaboration where every actor's role, boundary, and verification is explicit, testable, and structurally enforced.

### The Core Principle

> **The agent prepares judgment. The human makes judgment. The system enforces boundaries.**

Each actor has a distinct role:

| Actor | Role | Hallucination Risk | Cost |
|---|---|---|---|
| **Human** | Ethical judgment, creative discovery, accountability | None | High |
| **Agent** | Semantic reasoning, pattern detection, parallel analysis | Moderate-High | Moderate |
| **System** | Deterministic transformation, validation, routing, enforcement | Zero | Near-zero |

System gets first refusal on any subtask — if it can be expressed as a deterministic rule, it should be. This removes an entire failure mode category from the pipeline.

### The Six Phases

```
Phase 1 → TASK INTELLIGENCE
            Decompose the task. Classify cognitive operations.
            Identify what type of thinking each step requires.

Phase 2 → CAPABILITY ALLOCATION
            Score each subtask across 15 capability dimensions for H/A/S.
            Allocate using the complementarity algorithm.
            (Optional) Phase 2.5: Event Storm for multi-agent workflows.

Phase 3 → SYSTEM ARCHITECTURE
            Design the pipeline, data flows, templates, and failure recovery.
            Every data object has a typed schema. Every failure mode has a recovery path.

Phase 4 → AGENT DESIGN
            Classify agents. Set authority boundaries (the inverse of failure modes).
            Write job descriptions precise enough for implementation.
            Stress-test every boundary with adversarial inputs.

Phase 5 → HUMAN EXPERIENCE DESIGN
            Budget cognitive load. Design decision interfaces.
            Ensure every interaction expands the human's creative freedom.

Phase 6 → VALIDATION & ITERATION
            Run the tests that were designed alongside every phase.
            Deploy agents progressively (shadow → advisory → supervised → autonomous).
            Monitor pipeline health. Refine specifications as they age.
```

### What Makes It Different

**Three actors, not two.** System handles everything deterministic — validation, routing, calculation, enforcement. This is cheaper, faster, and more reliable than assigning mechanical work to an LLM.

**Templates, not prose.** Every data flow uses typed, structured templates. This resolves the type collision problem where 17+ distinct information types get compressed into undifferentiated text. Templates are the engineering solution to a communications problem.

**Boundaries are structural.** "Don't interpret" is a prompt instruction that fails under pressure. "The agent structurally cannot access interpretive tools" is architecture. Information boundaries, verification independence, and audit trails are enforced by System code, not by prompts.

**Testing runs alongside design.** Every design decision generates a test. Test plans are created in Phase 1, not Phase 6. Quality gates include test readiness checks. Validation is concurrent with design, not sequential.

**Enrichment is measurable.** The System Empowerment Index (Constraining → Informing → Enabling → Amplifying → Liberating) measures whether the system expands or contracts human creative freedom. The goal is not independence from the system — it's achieving more through the system than was possible without it.

### What It Produces

A complete, traceable specification chain from task analysis to deployment:

```
Task Decomposition Map
  → Complementarity Matrix (H/A/S scores, model-specific)
    → Event Storm Map (if multi-agent)
      → System Architecture Document
        → Template Architecture (7 typed template types)
          → Agent Job Descriptions (with authority boundaries, stress tests)
            → Human Experience Specification (with SEI assessment)
              → Test Plans (one per phase)
                → Validation Report
                  → Progressive Autonomy Plan
```

Every specification traces back to a design decision. Every design decision traces back to evidence. Every quality gate checks both fidelity (does it work?) and enrichment (does it expand human freedom?).

### Eight Cross-Cutting Concerns

Every phase is governed by eight concerns that appear at every quality gate:

| # | Concern | One-Line Summary |
|---|---|---|
| CC-1 | Verification Independence | No agent approves its own work. Three independence levels. |
| CC-2 | Human Enrichment | Every phase asks: does this expand creative freedom? |
| CC-3 | Epistemic Metadata | Every output carries provenance, confidence, limitations, assumptions, alternatives, and what would change it. |
| CC-4 | Information Boundaries | Structurally enforced, not prompt-instructed. |
| CC-5 | Specification Aging | Specs degrade. Freshness dates and aging triggers. |
| CC-6 | System Empowerment Index | Measuring Constraining → Liberating, not dependent → independent. |
| CC-7 | Cost Budget | Cost is a first-class design constraint. |
| CC-8 | Assured Audit Trail | Three assurance levels matching trust requirements. |

### Five Quality Gates

Each gate has three layers of checks: fidelity (does it work?), enrichment (does it expand freedom?), and cross-cutting (are all structural guarantees in place?). No phase proceeds until its gate passes.

### When to Use It

| Task Complexity | Phases | Example |
|---|---|---|
| Single-agent, no human loop | 1 → 2 → 4 | Data extraction, summarisation |
| Single-agent + human review | 1 → 2 → 4 → 5 | Draft generation with sign-off |
| Multi-agent, linear pipeline | 1 → 2 → 3 → 4 → 5 | Sequential processing |
| Multi-agent, branching + human decisions | 1 → 2 → 2.5 → 3 → 4 → 5 → 6 | Complex workflows with failure recovery |

### The Bottom Line

CAWDP produces agentic systems where:
- **The right actor does the right task** — System handles the deterministic, Agent handles the semantic, Human handles the creative
- **Boundaries are structural, not declarative** — the system enforces what agents cannot do
- **Every output carries its epistemic metadata** — provenance, confidence, limitations are never optional
- **Testing is concurrent with design** — no phase passes without test readiness
- **The human ends up more free, not less** — the system amplifies creative capability, it doesn't replace it

---

## Run 7 — Agentic Expert ✓ COMPLETED

*2026-04-13T12:25:54* · `glm-5.1:cloud` · `526f32dc...`

### Prompt

Rewrite this table and include a column for system 

```
# Agent & Human Complementarity

| Property                         | Human | Agent |
| -------------------------------- | ----- | ----- |
| Handling ambiguous input         | 7     | 9     |
| Zero-shot generalisation         | 8     | 8     |
| Reasoning & judgment             | 9     | 7     |
| Commonsense inference            | 9     | 7     |
| Creative problem framing         | 9     | 4     |
| Novel situation reasoning        | 8     | 5     |
| Double-loop learning             | 8     | 3     |
| Generation & creativity          | 9     | 7     |
| Output consistency               | 5     | 7     |
| Hallucination resistance         | 7     | 4     |
| Goal alignment                   | 7     | 6     |
| In-context adaptability          | 7     | 8     |
| Semantic & social skill          | 9     | 7     |
| Ethical judgment                 | 9     | 2     |
| Values alignment                 | 8     | 2     |
| Decision authority               | 9     | 2     |
| Reversibility awareness          | 8     | 5     |
| Behaviour under observation      | 5     | 6     |
| Parallelisation & scale          | 2     | 9     |
| Motivational consistency         | 5     | 9     |
| Cognitive bias resistance        | 4     | 6     |
| Approval fatigue resistance      | 4     | 9     |
| Manipulation resistance          | 6     | 4     |
| Context management               | 6     | 6     |
| Error containment                | 6     | 4     |
| Cognitive diversity preservation | 6     | 4     |
| Skill preservation               | 5     | 8     |
```

### Response

# Human-Agent-System Complementarity Matrix

| Property | Human | Agent | System |
|---|:---:|:---:|:---:|
| Handling ambiguous input | 7 | 9 | 1 |
| Zero-shot generalisation | 8 | 8 | 1 |
| Reasoning & judgment | 9 | 7 | 1 |
| Commonsense inference | 9 | 7 | 1 |
| Creative problem framing | 9 | 4 | 1 |
| Novel situation reasoning | 8 | 5 | 1 |
| Double-loop learning | 8 | 3 | 1 |
| Generation & creativity | 9 | 7 | 1 |
| Output consistency | 5 | 7 | 9 |
| Hallucination resistance | 7 | 4 | 9 |
| Goal alignment | 7 | 6 | 7 |
| In-context adaptability | 7 | 8 | 1 |
| Semantic & social skill | 9 | 7 | 1 |
| Ethical judgment | 9 | 2 | 1 |
| Values alignment | 8 | 2 | 1 |
| Decision authority | 9 | 2 | 1 |
| Reversibility awareness | 8 | 5 | 3 |
| Behaviour under observation | 5 | 6 | 9 |
| Parallelisation & scale | 2 | 9 | 9 |
| Motivational consistency | 5 | 9 | 9 |
| Cognitive bias resistance | 4 | 6 | 9 |
| Approval fatigue resistance | 4 | 9 | 9 |
| Manipulation resistance | 6 | 4 | 7 |
| Context management | 6 | 6 | 4 |
| Error containment | 6 | 4 | 8 |
| Cognitive diversity preservation | 6 | 4 | 1 |
| Skill preservation | 5 | 8 | 9 |

---

### Reading the Pattern

The System column creates a stark profile: **9s and 1s, almost nothing in between.** System is extreme — near-perfect at mechanical operations, near-zero at everything requiring understanding. This is the insight that drives the ternary allocation priority: System gets first refusal because it eliminates an entire failure mode category (hallucination, inconsistency, fatigue, bias) at near-zero cost — but only for subtasks that don't require semantic reasoning.

Three clusters emerge:

| Cluster | Properties | Best Actor | Why |
|---|---|---|---|
| **Judgment** | Ethical judgment, values alignment, decision authority, creative problem framing, novel situation reasoning, double-loop learning | **Human** | Scores 8-9 where System scores 1 and Agent scores 2-5 |
| **Semantic** | Handling ambiguous input, in-context adaptability, zero-shot generalisation, semantic & social skill | **Agent** | Agent scores 7-9 where System scores 1; Human is competitive but can't scale |
| **Mechanical** | Output consistency, hallucination resistance, parallelisation & scale, motivational consistency, approval fatigue resistance, cognitive bias resistance | **System** | System scores 9 where Human scores 2-7; Agent is competitive but costs more and hallucinates |

**Goal alignment (7/6/7)** is the interesting outlier — all three actors are reasonably aligned when goals are explicit, but for different reasons: Human aligns through shared values, Agent aligns through instruction following, System aligns through programmed rules. All three degrade when goals become ambiguous, just through different failure modes.

**Manipulation resistance (6/4/7)** is another: System is immune to social manipulation but vulnerable to technical exploitation (injection, logic bugs). Agent is vulnerable to both. Human is vulnerable to social manipulation but can detect technical inconsistencies.

---

## Run 8 — Agentic Expert ✓ COMPLETED

*2026-04-16T05:03:32* · `glm-5.1:cloud` · `24e3d149...`

### Prompt

Currently, CAWDP v2 is almost 5000 words. Write a 2000 word whitepaper that is more accessible by professionals who are not experienced in agent systems.

### Response

# Getting It Right: A Better Way to Design AI Agent Systems

*Why most AI agent projects fail, and a structured approach that makes them trustworthy.*

---

## The Problem Nobody Wants to Talk About

Organisations are rushing to deploy AI agents. The promise is compelling: automate complex work, scale expertise, let humans focus on what matters. But the results tell a different story.

Research from Carnegie Mellon found only a 24% task completion rate for autonomous agents on complex work. Gartner predicts over 40% of agentic AI projects will be cancelled by 2027. McKinsey reports organisations retrenching and rehiring humans where agents failed. Only 2% of enterprises have deployed agentic AI at scale.

The pattern is consistent: a team builds an agent, it works well on simple tasks, they scale it to complex work, and it produces outputs that look plausible but are fundamentally unreliable. The human ends up checking everything the agent did, which defeats the purpose. Or worse: the human trusts the agent's output and the errors propagate silently.

This isn't a technology problem. It's a design problem.

---

## The Root Causes

After designing and analysing multiple agentic workflows, three root causes emerge consistently:

**1. The wrong actor does the wrong task.**

Most organisations assign work based on what AI *can* do, not what each actor *should* do. They give tasks to agents that deterministic software could handle faster, cheaper, and more reliably. They give tasks to agents that require ethical judgment. They give tasks to humans that are mechanical and exhausting.

The result: agents hallucinating in roles they shouldn't hold, humans rubber-stamping machine outputs, and expensive language models doing work a simple script could do perfectly.

**2. Boundaries are declared, not enforced.**

Most agent systems rely on written instructions to control behaviour: "Don't make final decisions." "Don't access patient records." "Don't interpret the data, just extract it."

Under pressure — ambiguous inputs, edge cases, adversarial prompts — these instructions fail. They're policy, not architecture. The equivalent of putting a "Please don't enter" sign on an unlocked door.

**3. Outputs are walls of text.**

When agents produce undifferentiated prose, the human cannot efficiently extract, evaluate, or act on the components that matter. Every claim, every data point, every recommendation is compressed into a single format that obscures rather than reveals. The human ends up reading paragraphs to find the one number they need.

---

## A Different Approach

CAWDP — Complementarity-Driven Agentic Workflow Design Process — is a six-phase framework that addresses each root cause directly. It doesn't assume you need an AI agent. It doesn't assume you need a team of agents. It starts from the work itself and asks: who should do what, and how do we know it's right?

Three principles guide every design decision:

**Principle 1: Three actors, not two.** Every task involves three possible actors: Humans, who bring judgment, creativity, and accountability. Agents, who bring semantic reasoning, pattern detection, and scale. System, which is deterministic code — validation, routing, calculation, enforcement — with zero hallucination risk and near-zero cost.

The critical insight: System gets first refusal. If a subtask can be expressed as a deterministic rule, it should be handled by code, not by a language model. Schema validation, data routing, threshold checking, format conversion — these don't require semantic understanding. Assigning them to an agent introduces hallucination risk where none should exist.

**Principle 2: Agents prepare judgment; humans make judgment.** The highest-value role of an AI agent is not to produce final answers but to prepare structured decision inputs for human judgment. An agent can extract claims, surface evidence, calculate scores, and flag anomalies. The human decides what it means and what to do about it. This isn't because humans are always right — it's because humans are accountable in ways agents cannot be.

**Principle 3: Boundaries are architecture, not policy.** What an agent must not do should be structurally impossible, not merely discouraged. If an extractor must not interpret, then it should not have access to interpretive tools. If an assessor must not finalise scores, then the system should not accept final scores from it. Under pressure, architecture holds. Policy fails.

---

## The Six Phases

### Phase 1: Understand the Work

Before designing anything, understand what the work actually involves. Break the task into subtasks. Classify what kind of thinking each one requires — is it mechanical (deterministic, rule-based), semantic (requires understanding), or evaluative (requires judgment)?

Mechanical subtasks belong to System. Semantic subtasks are candidates for Agent. Evaluative subtasks belong to Human.

This phase surfaces a common mistake: tasks that look like they need AI but are actually deterministic rules wearing a semantic disguise. "Flag any score below 60%" is a threshold check, not a reasoning task. System handles it.

### Phase 2: Allocate by Complementarity

Score each subtask across capability dimensions for all three actors. Where does the human have a large advantage? Where does the agent? Where does system code outperform both?

The allocation priority is: System first (cheapest, most reliable, zero hallucination), then Human (for judgment and accountability), then Agent (for semantic work at scale), then Collaborative (where genuine hybrid work adds value).

A critical concept: reversibility. Read-only actions can be agent-autonomous. Reversible actions can be agent-recommended. Irreversible actions are human-led — not as a preference but as a structural requirement.

### Phase 2.5: Map What Can Go Wrong (for complex workflows)

For multi-agent systems, map every event that occurs: what triggers it, what data it produces, what happens next. Then deliberately map what *shouldn't* happen but will: what if the agent produces wrong output? What if the human disagrees? What if the system validation fails?

This step — called Event Storming — surfaces failure paths before they happen. It's optional for simple systems and essential for complex ones.

### Phase 3: Design the Architecture

Design the data flows, the templates that structure them, and the failure recovery paths.

Every data flow uses typed, structured templates — not prose. Templates are the mechanism that solves the "wall of text" problem. Instead of a paragraph about a claim, you get a structured record: claim text, source, confidence level, domain tags, what would change this assessment. Every component is typed, searchable, and independently evaluable.

Every failure mode has a recovery path. What happens when an extractor hallucinates? What happens when a human overrides a score? What happens when the system itself fails? These are designed in, not discovered at runtime.

### Phase 4: Design Each Agent

Every agent gets a classification, and the classification determines its boundary:

- **Extractors** extract information. They must never interpret. Their failure mode is hallucination.
- **Measurers** calculate metrics. They must never interpret. Their failure mode is reading noise as signal.
- **Assessors** evaluate against criteria. They must never finalise. Their failure mode is overconfidence.
- **Generators** produce content. They must never be vague. Their failure mode is fabrication.
- **Aggregators** consolidate multiple sources. They must never add new analysis. Their failure mode is omission through addition.

The constraint is always the inverse of the failure mode. This is a design pattern: *constrain the inverse of what can go wrong.*

Each agent gets a complete job description: what it receives, what it produces, what it must never do, what it does when things go wrong, and how confident it is in its own output. Every output carries six pieces of metadata: who produced it, how confident they are, what it doesn't cover, what was assumed, what alternatives were set aside, and what new information would change the conclusion.

### Phase 5: Design the Human Experience

Budget the human's cognitive load. How much information must they process at each decision point? How many decisions must they make? How quickly?

If the load exceeds the budget, add a synthesis layer — an agent that pre-digests information for the human. Reduce the volume, not by hiding information but by structuring it. Reduce the decision density by batching similar decisions. Never present a human with a wall of text and ask them to extract the one number they need.

Assess whether each interaction expands or contracts the human's creative freedom. The goal is not to make the human independent of the system — it's to make the human capable of achieving things they couldn't achieve alone. Every interaction should leave the human more capable, not more dependent on approval workflows.

### Phase 6: Validate and Iterate

Testing happens throughout, not just at the end. Every design decision generates a test plan. Quality gates at each phase check three things: does it work (fidelity), does it expand human freedom (enrichment), and are all structural guarantees in place (cross-cutting)?

Agents deploy progressively. They don't start with full autonomy. They earn trust through measured performance:

1. **Shadow mode** — Agent produces outputs that are compared against manual baselines but not used.
2. **Advisory mode** — Agent produces recommendations with reasoning; human approves before action.
3. **Supervised mode** — Agent acts within bounded parameters; human reviews exceptions.
4. **Autonomous mode** — Agent acts within specification; human reviews only escalations.

Advancement between levels requires quantified evidence: accuracy thresholds, override rates, and consequence severity. No agent handling irreversible actions operates autonomously.

---

## What Changes in Practice

**For executives:** You get a governance framework that produces auditable, traceable decisions about why each actor does what. When something goes wrong, you can trace it to a design decision, not a vague prompt.

**For project teams:** You get a repeatable process that scales from single-agent tasks to complex multi-agent workflows. The scaling heuristic tells you which phases are needed for your complexity level. You don't have to over-engineer a simple task.

**For risk and compliance:** Every agent boundary is structurally enforced. Every output carries provenance and confidence metadata. Every action has an audit trail at an assurance level appropriate to its risk. The framework maps directly to EU AI Act requirements for risk management, documentation, and human oversight.

**For the humans in the system:** You get structured decision inputs, not walls of text. You spend your time on genuine judgment, not mechanical verification. The system amplifies your capabilities rather than replacing them with approval workflows.

---

## The Bottom Line

Most AI agent failures are design failures, not technology failures. They happen because the wrong actor did the wrong task, because boundaries were declared rather than enforced, and because outputs were prose when they should have been structured data.

CAWDP addresses each root cause with a structured approach: three-actor allocation ensures the right actor does the right task. Structural boundaries ensure agents cannot exceed their authority. Templates and metadata ensure outputs are typed, traceable, and evaluable. Progressive autonomy ensures trust is earned, not assumed.

The result: agent systems where boundaries hold under pressure, where verification is independent by design, where the human ends up more capable rather than more dependent, and where every design decision traces to evidence.

The 77% of organisations stuck at pilot don't have a technology problem. They have a design problem. This is the methodology that solves it.

---

## Run 9 — Agentic Expert ✓ COMPLETED

*2026-04-16T05:15:36* · `glm-5.1:cloud` · `4017d811...`

### Prompt

If we want to release CAWDP to invite comment and contributions from academics and industry experts, what would be the ideal outline of this document?
Would it help to share my journey exploring agents and multi-agent systems to arrive at this point?
What claims would I need to make to justify the need for the framework and what level of data and research would be needed to support the claims?
Should it include an example of a use case traversing the framework to illustrate how it works?

### Response

# Releasing CAWDP: Strategy and Structure

I'll answer all four questions together because they're deeply interconnected — the outline depends on what claims you're making, the claims depend on the evidence you can support, and the worked example is the evidence bridge.

---

## Question 1: The Ideal Outline

The document should be structured as an **academic working paper with an open invitation for comment** — not a blog post, not a product manual, not a peer-reviewed paper (yet). The model is ArXiv preprint meets industry RFC: rigorous enough for academics to engage, accessible enough for practitioners to apply.

Here's the proposed structure:

---

### **Complementarity-Driven Agentic Workflow Design: A Governance Framework for Trustworthy Agent Systems**

**Working Paper v1.0 — Open for Comment**

---

**Abstract** (250 words)
Problem statement, the gap (methodology, not technology), what CAWDP is, what this paper does.

**1. The Problem: Why Agent Systems Fail at Scale**

1.1 The deployment gap: evidence of systematic failure
1.2 Root cause analysis: three structural failures
1.3 The methodology gap: principles exist, process doesn't

**2. Design Provenance: How This Framework Emerged**

2.1 From practice to principle: the iterative discovery process
2.2 Key insights that shaped the framework
2.3 Limitations of the development process

**3. Core Principles**

3.1 The agent prepares judgment; the human makes judgment
3.2 Three actors, not two
3.3 Boundaries are architecture, not policy
3.4 Specifications age; trust is earned

**4. The Framework: CAWDP v2**

4.1 Overview: six phases, eight cross-cutting concerns, five quality gates
4.2 Phase 1: Task Intelligence
4.3 Phase 2: Capability Allocation (with Phase 2.5: Event Storming)
4.4 Phase 3: System Architecture
4.5 Phase 4: Agent Design
4.6 Phase 5: Human Experience Design
4.7 Phase 6: Validation and Iteration
4.8 Cross-cutting concerns
4.9 Quality gates

**5. Worked Example: Assessment Marking Workflow**

5.1 Task description and decomposition
5.2 Capability allocation walkthrough
5.3 Agent roster and authority boundaries
5.4 Key design decisions and their rationale

**6. Relationship to Existing Work**

6.1 Where CAWDP aligns with established frameworks
6.2 Where CAWDP diverges and why
6.3 Open questions and known gaps

**7. Invitation for Comment**

7.1 What we're confident about
7.2 What we're uncertain about
7.3 Specific areas where we seek input
7.4 How to contribute

**References**

**Appendix A: The 27-Dimension Complementarity Matrix**
**Appendix B: Full Agent Job Descriptions**
**Appendix C: Template Architecture Specification**

---

### Why This Structure Works

**Section 1 (Problem)** hooks industry readers with evidence they recognise. It immediately establishes credibility: "We're not claiming something doesn't work — Gartner, MIT, and McKinsey already established that." This also sets up the claims hierarchy (which I'll detail in Question 3).

**Section 2 (Provenance)** answers your journey question. More on this below, but the key design choice: it's positioned as *methodology provenance*, not autobiography. It says "this framework emerged from iterative design, not from theory" — which is a strength, not a confession.

**Section 3 (Principles)** gives academics the theoretical grounding they need. It separates *what must be true* from *how to make it true*. This is where you establish that CAWDP rests on a coherent philosophical foundation, not just a process.

**Section 4 (Framework)** is the core contribution. It needs to be complete enough that a practitioner could apply it, but not so detailed that it becomes a manual. Key design choice: the cross-cutting concerns and quality gates are presented *alongside* the phases, not as separate sections, because they're the thread that holds the phases together.

**Section 5 (Worked Example)** is the evidence bridge. More on this below, but a concrete example converts abstract process into visible practice.

**Section 6 (Existing Work)** is essential for academic credibility. It positions CAWDP in the landscape, acknowledges predecessors, and is honest about gaps. This is where you show you've done the reading, not just the building.

**Section 7 (Invitation for Comment)** is what makes this a living document, not a finished product. It models the very principle of epistemic honesty that CAWDP requires of agents. The framework that requires outputs to carry confidence levels should carry them too.

---

## Question 2: Should You Share Your Journey?

**Yes — but positioned as methodology provenance, not personal narrative.**

Here's why it matters and how to do it right:

### Why Include It

Your journey is evidence of **how the framework was discovered**, which is academically relevant for several reasons:

1. **It demonstrates the framework wasn't top-down theory.** You didn't start with principles and derive a process. You started with a real problem, iterated through design, and *discovered* principles that held across iterations. This is closer to grounded theory methodology than to axiomatic derivation — and that's a strength for a methodology paper.

2. **It explains why certain design choices exist.** The ternary model didn't emerge because "three actors sounds nice." It emerged because assigning mechanical subtasks to agents introduced hallucination risk where none should exist. The 5-class taxonomy didn't emerge because "five is a good number." It emerged because the marking workflow produced agents that naturally clustered into distinct failure modes. These origin stories make the framework's claims more credible because they're grounded in discovery, not assumption.

3. **It models the very principle of epistemic honesty.** A framework that demands outputs carry confidence levels, provenance, and limitations should do the same. The provenance section is CAWDP's own epistemic metadata: where did this come from, what were the assumptions, what are the limitations?

### How NOT to Do It

- **Not as autobiography.** "I started exploring agents in 2024" is personal history. "The framework emerged from iterative design across three increasingly complex agent systems" is methodology provenance.
- **Not as validation.** Your journey is evidence of *how* the framework was discovered, not evidence that *it works*. Those are different things.
- **Not as the main narrative.** Provenance supports the claims; it doesn't make them.

### How to Do It

Position Section 2 around the **discoveries**, not the timeline:

| Discovery | What It Taught | How It Shaped CAWDP |
|---|---|---|
| Assigning extraction to agents produced hallucination | Mechanical work doesn't need semantic reasoning | System as third actor, System-first allocation |
| Agents exceeded their boundaries under pressure | Prompt instructions fail; architecture holds | Structural boundaries, Information Boundaries |
| Human received walls of text and couldn't act | 17+ information types compressed into prose | Type collision, Template Architecture |
| Complementarity analysis showed 6+ point gaps | Some subtasks genuinely need human judgment | Authority boundaries as inverse of failure modes |
| Specifications produced good results initially then degraded | Specifications age silently | Specification Aging, freshness dates |
| Agent classified as "general" produced inconsistent output | Failure modes cluster into distinct types | 5-class taxonomy, constrain the inverse |

This format communicates the same information as a narrative but is scannable, evidence-structured, and positions each insight as a discovery rather than a personal anecdote.

The key sentence for this section: *"This framework was not designed top-down from principles. It was discovered bottom-up from practice, then validated against principles. The provenance matters because it explains why the framework looks the way it does — not why it's correct."*

---

## Question 3: Claims and Evidence

This is the most critical section for academic credibility. You need to be explicit about what you're claiming and what evidence supports each claim. I'll organise this as a claims hierarchy from strongest (most evidenced) to weakest (most aspirational), with the evidence level required for each.

### Tier 1: Problem Claims (Strong Evidence Available)

These are claims about the state of the world. They're well-supported by existing research.

| Claim | Evidence Level | Sources |
|---|---|---|
| Most agentic AI projects fail to reach production | **Strong** — multiple independent sources | Gartner (40%+ cancellation by 2027, Reuters-confirmed); MIT/NANDA (~5% achieve rapid revenue acceleration); DigitalOcean (67% see pilot gains, only 10% scale to production); Shakudo (80%+ fail within 6 months) |
| Agents perform poorly on complex multi-step tasks | **Strong** — benchmark data | SWE-bench verified: top agents solve ~50% of verified tasks, with complex multi-step tasks significantly lower; Carnegie Mellon; MIRAGE-Bench (hallucination in agentic settings); AgentHallu (systematic hallucination attribution) |
| Hallucination and boundary violations are persistent problems | **Strong** — multiple studies | HEAL (embodied agent hallucination); HALOGEN (comprehensive hallucination benchmark); multiple industry reports on production failures |
| Organisations lack design frameworks for agent deployment | **Moderate** — survey data | MIT Sloan/BCG (76% of executives view agentic AI as "coworker" but lack design frameworks for delegation and oversight) |
| The gap is not technology but design and governance | **Moderate** — analytical with supporting evidence | Gartner (architecture gaps, not model capability); Directual analysis (not the model, the everything else); Shakudo (organizational barriers, not just technical) |

### Tier 2: Root Cause Claims (Analytically Supported)

These are claims about *why* the problem exists. They're analytically coherent but haven't been empirically validated through controlled experiments.

| Claim | Evidence Level | Supporting Argument |
|---|---|---|
| Wrong actor does the wrong task | **Analytical** — derived from design analysis | Demonstrated through complementarity analysis: tasks requiring deterministic processing assigned to probabilistic actors (agents), tasks requiring ethical judgment assigned to non-accountable actors (agents). The ternary matrix shows systematic misallocation. |
| Boundaries are declared, not enforced | **Analytical** — derived from failure analysis | When agents exceed boundaries under pressure (ambiguous inputs, adversarial prompts), prompt instructions fail. Structural boundaries hold. Demonstrated through boundary stress testing in Phase 4. |
| Outputs are walls of text | **Analytical + observational** | Type collision analysis: 17+ distinct information types compressed into a single output type (prose). This is a Shannon-Weaver channel capacity problem. Template architecture resolves it. |
| Trust is assumed, not earned | **Analytical** — derived from deployment pattern analysis | Most deployments grant full autonomy from day one. Progressive autonomy (shadow → advisory → supervised → autonomous) with quantified advancement criteria is almost never implemented. |

### Tier 3: Methodology Claims (Internally Coherent, Externally Untested)

These are claims that CAWDP addresses the root causes. They're coherent within the framework but haven't been validated through external application.

| Claim | Evidence Level | What's Needed |
|---|---|---|
| Three-actor allocation reduces misallocation | **Internal coherence** — the ternary matrix identifies mechanical tasks that shouldn't be assigned to agents | **Needed:** Comparative study: same task designed with binary (H/A) and ternary (H/A/S) allocation, measuring cost, accuracy, and failure rate |
| Structural boundaries hold under pressure | **Internal coherence** — boundary stress tests identify failure modes before deployment | **Needed:** Adversarial testing of agent boundaries: prompt-only vs. structurally enforced, measuring boundary violation rates under pressure |
| Templates resolve type collision | **Internal coherence** — typed outputs allow extraction, evaluation, and action that prose doesn't | **Needed:** A/B study: same task, prose output vs. template output, measuring human decision speed, accuracy, and confidence |
| Progressive autonomy reduces deployment risk | **Internal coherence** — agents earn trust through measured performance | **Needed:** Longitudinal study: agents deployed with progressive autonomy vs. full autonomy, measuring override rates, error rates, and trust accumulation over time |
| CAWDP produces trustworthy agent systems | **Aspirational** — the framework is internally coherent but has not been externally validated | **Needed:** Independent case studies applying CAWDP to different domains, measuring outcomes against baseline |

### Tier 4: Outcome Claims (Aspirational)

These are claims about what CAWDP will achieve. They should be presented as hypotheses to be tested, not conclusions.

| Claim | Evidence Level | Status |
|---|---|---|
| CAWDP addresses the 77% pilot-to-production gap | **Hypothesis** | The root cause analysis maps CAWDP mechanisms to documented failure modes. This is a testable hypothesis, not a validated claim. |
| CAWDP is applicable across domains | **Hypothesis** | Designed for generality, tested in one domain (education/assessment marking). Needs application in finance, healthcare, legal, operations. |
| CAWDP reduces agent-related failure rates | **Hypothesis** | The structural mechanisms (boundaries, templates, verification) are designed to address documented failure modes. Needs empirical testing. |

### How to Present This in the Paper

The document should include a **Claims and Evidence Table** as a prominent element — perhaps in the introduction or as a standalone section. This table makes the evidence level explicit and models the epistemic honesty the framework requires. It also invites academics to help validate Tier 3 and Tier 4 claims.

The key sentence: *"We make claims at four evidence levels. Tier 1 and Tier 2 claims are well-supported by existing research and analysis. Tier 3 claims are internally coherent but externally untested — we invite independent validation. Tier 4 claims are hypotheses that this paper is designed to invite testing of, not conclusions we have reached."*

---

## Question 4: The Worked Example

**Yes, absolutely.** A worked example is not optional — it's the single most important section for converting abstract process into visible practice. Without it, readers will understand the framework intellectually but not viscerally.

### Which Example

The assignment marking workflow (23 agents, 4 stages, 12 execution waves) is too complex for the main body. It would overwhelm readers and obscure the process with detail.

**Recommended approach: Two-tier example**

**Main body (Section 5): Simplified walk-through** — A 3-4 agent pipeline that traverses all six phases in enough detail to see every phase in action, but not so much detail that the reader drowns in specialist content.

**Appendix B: Full assignment marking workflow** — The complete 23-agent pipeline with job descriptions, as empirical evidence that the framework works at scale.

### What the Walk-Through Should Demonstrate

The simplified example should show, step by step:

1. **Phase 1:** The task decomposition — what cognitive operations are involved, how mechanical vs. semantic vs. evaluative subtasks are identified
2. **Phase 2:** The complementarity allocation — how the ternary matrix assigns H/A/S, where gaps appear, and what the reversibility classification looks like
3. **Phase 2.5:** A brief event storm — what can go wrong, what triggers what
4. **Phase 3:** The architecture — what templates structure the data, what failure recovery paths exist
5. **Phase 4:** The agent design — what class each agent is, what boundary constrains it, and the "constrain the inverse" pattern
6. **Phase 5:** The human experience — what decisions the human makes, what cognitive load budget looks like, how the SEI assessment works
7. **Phase 6:** The progressive autonomy deployment — what level each agent starts at, what advancement criteria look like

### Choosing the Simplified Example

I'd recommend a **content review pipeline** — a process where a piece of content (article, report, marketing copy) is processed through:

- **Extractor** — extracts claims, citations, and factual assertions
- **Measurer** — checks citation accuracy, reads tone metrics, identifies claim strength
- **Assessor** — evaluates claims against criteria, flags issues
- **Human reviewer** — makes final judgment, approves/flags/rejects

This is a good example because:
- It's domain-general (everyone understands content review)
- It naturally produces all five agent classes (Extractor, Measurer, Assessor, Generator, Aggregator)
- It has clear mechanical/semantic/evaluative subtasks
- It has clear reversibility classification (publishing is irreversible)
- It has clear trust requirements (factual accuracy has high stakes)
- It can be done at 3-4 agents for simplicity
- It maps to a real-world need (content accuracy is a universal concern)

---

## Summary: The Document Architecture

```
WORKING PAPER v1.0 — OPEN FOR COMMENT

Abstract

1. THE PROBLEM
   1.1 The deployment gap (Tier 1 evidence)
   1.2 Root cause analysis (Tier 2 evidence)
   1.3 The methodology gap (Tier 2 evidence)

2. DESIGN PROVENANCE
   2.1 From practice to principle (discovery table, not narrative)
   2.2 Key insights that shaped the framework
   2.3 Limitations of the development process (honest about gaps)

3. CORE PRINCIPLES
   3.1 The agent prepares judgment; the human makes judgment
   3.2 Three actors, not two
   3.3 Boundaries are architecture, not policy
   3.4 Specifications age; trust is earned

4. THE FRAMEWORK
   4.1 Overview
   4.2-4.7 The six phases (with cross-cutting concerns woven in)
   4.8 Quality gates

5. WORKED EXAMPLE: Content Review Pipeline
   5.1-5.7 Each phase applied to the example

6. RELATIONSHIP TO EXISTING WORK
   6.1 Alignment with established frameworks (ISO, NIST, IEEE, MIT Sloan)
   6.2 Points of divergence and rationale
   6.3 Open questions and known gaps

7. CLAIMS AND EVIDENCE TABLE
   7.1 Tier 1-4 claims with evidence levels
   7.2 What's validated, what's coherent, what's hypothetical
   7.3 Specific areas where we seek input

8. INVITATION FOR COMMENT
   8.1 What we're confident about
   8.2 What we're uncertain about
   8.3 How to contribute

References

Appendix A: Complementarity Matrix
Appendix B: Full Assignment Marking Workflow
Appendix C: Template Specification
```

**Target length:** 8,000-10,000 words for the main body. Appendices can be longer.

**The one-page visual:** A single-page diagram showing all six phases, their inputs and outputs, and the cross-cutting concerns that run through them. This becomes the shareable artefact.

**The claims table is non-negotiable.** It's the single element that separates a credible working paper from marketing material. It models epistemic honesty — the very principle CAWDP requires of agents — and it gives academics a clear entry point for engagement.

**The provenance section transforms your journey from vulnerability to strength.** Instead of "I'm still learning," it becomes "This framework was discovered through iterative practice, not assumed from theory — and here are the specific discoveries that shaped each element." That's not a weakness. That's action research methodology.

**The worked example is the credibility bridge.** Academics need to see the framework applied end-to-end. Practitioners need to see it work on a problem they recognise. The two-tier approach (simplified walk-through + full appendix) serves both audiences without overwhelming either.The memory has been updated. A few closing observations on how these four answers connect to your broader strategy:

**The claims table is itself a CAWDP principle.** Tier 3 explicitly saying "internally coherent but untested" and Tier 4 saying "aspirational hypothesis, not conclusion" is epistemic metadata applied to the paper itself. You're not just describing CC-3 (Epistemic Metadata Contracts) — you're embodying it. This is a powerful signal to academics that the framework practices what it requires.

**The provenance section turns your biggest perceived weakness into a strength.** The "I keep having weekly revelations" pattern reframes as: this framework was discovered through iterative design, not imposed from theory. Grounded theory methodology. Action research. That's not a confession — that's a methodology. The discovery table format makes it scannable and evidence-structured rather than narrative and personal.

**The two-tier worked example is the right call.** The assignment marking workflow is too domain-specific and too complex for a first encounter. Content review is universal — everyone understands reviewing content for accuracy. And it naturally produces all five agent classes (Extractor → Measurer → Assessor → Generator → Aggregator), which means you can demonstrate the full taxonomy in a 3-4 agent pipeline.

**The one decision I'd flag for reconsideration:** whether to include the full Unified Framework (35 principles) in the working paper or just reference it. Including it would make the paper substantially longer and shifts focus from the process (CAWDP) to the principles. I'd recommend referencing it and noting that a companion paper on the governing principles is forthcoming. This keeps the working paper focused and gives you a second publication.

---

## Run 10 — Agentic Expert ✓ COMPLETED

*2026-04-16T05:56:47* · `glm-5.1:cloud` · `bc0cede1...`

### Prompt

I'd like to see the reasoning for your assertion here.

"The document should be structured as an academic working paper with an open invitation for comment — not a blog post, not a product manual, not a peer-reviewed paper (yet). The model is ArXiv preprint meets industry RFC: rigorous enough for academics to engage, accessible enough for practitioners to apply."

### Response

Now I have strong precedents. Let me build the full analysis.

---

# Why Working Paper: A Format-by-Format Analysis

Format is not neutral. The container shapes the reception, the audience, the credibility signals, and the downstream possibilities. I'll evaluate seven candidate formats against your specific situation, then explain why the working paper hybrid wins.

## Your Situation (The Constraints That Matter)

Before evaluating formats, let's state the constraints that any format must satisfy:

1. **Dual audience:** You need both academics (who evaluate rigor, evidence, gaps) and industry practitioners (who evaluate applicability, relevance, "can I use this?") to engage.

2. **Honest starting position:** The framework is rigorously derived but empirically untested. The format must accommodate this without making it look either finished (which overclaims) or preliminary (which invites dismissal).

3. **Openness is the brand:** You're selling trust infrastructure. A trust company with a closed or prematurely authoritative methodology is a structural contradiction.

4. **Versioning is necessary:** The framework will evolve. The format must support v1.0 → v1.1 → v2.0 naturally, without each version being treated as final or disposable.

5. **Feedback must be structural:** You want comment and contribution, not just readership. The format must create a pathway for response that's as easy as possible.

6. **Pathway to authority:** This isn't the endpoint. The format must create a credible pathway toward something more — academic validation, conference presentation, community adoption, industry standard.

7. **Provenance matters:** The framework emerged from iterative design, not from theory. The format must accommodate this origin story without making it look either like a confession of weakness or an ego narrative.

---

## Format 1: Blog Post (Medium, Substack, Personal Site)

**What it signals:** Personal opinion, individual perspective, accessible, timely.

**Credibility with academics:** Low. Blog posts aren't cited. They don't go through any review process. They're treated as commentary, not contribution.

**Credibility with practitioners:** Moderate-to-high depending on author reputation. But a methodology announced only on a blog risks being perceived as "someone's idea" rather than "an approach worth adopting."

**Feedback mechanism:** Comments section. Low friction, but low quality — comments are unstructured, there's no versioning, and there's no mechanism for substantive contribution.

**Versioning:** Weak. A blog post is a point-in-time artifact. You can update it, but the original is what gets shared and cited. No natural versioning protocol.

**Risk:** A blog post positions CAWDP as opinion, not methodology. It's the format for "here's what I think," not "here's a framework that addresses a documented gap." Given that the core brand positioning is "the methodology that makes agents trustworthy in production," launching as a blog post undercuts the claim from the first impression.

**When it works:** Building awareness after the methodology is already established. Blog posts are great for the 77% Challenge, the Agent Job Interview series, case study narratives. They're terrible for the methodology itself.

---

## Format 2: Product Manual / Technical Documentation

**What it signals:** This is how to use the thing. Prescriptive, complete, operational.

**Credibility with academics:** Near-zero. Manuals are not academic contributions. They don't engage with existing work, they don't acknowledge gaps, and they present instructions as given, not argued.

**Credibility with practitioners:** High for adoption, low for trust. A manual says "do this." But practitioners need to understand *why* before they commit to a process. A manual doesn't make the case; it assumes the case has been made.

**Feedback mechanism:** GitHub issues, at best. Structured but narrow — feedback on implementation details, not on the framework's design decisions.

**Versioning:** Strong. Versioned documentation is standard practice. But the versioning is of *instructions*, not of *reasoning*.

**Risk:** A manual positions CAWDP as a tool, not a methodology. Tools get evaluated on whether they work. Methodologies get evaluated on whether they make sense and whether they produce results. The manual format skips the "does this make sense?" question entirely. It also contradicts the open-for-comment intention — manuals are finished products, not invitations.

**When it works:** After the methodology is validated and adopted. The CAWDP Reference Documentation (ReadTheDocs-style) is a product manual. It belongs in the Fractal layer, months 4-6, after the working paper has established the framework's reasoning.

---

## Format 3: Peer-Reviewed Paper (Journal Submission)

**What it signals:** This has been vetted. Claims are supported. The community has evaluated it.

**Credibility with academics:** Highest of any format. Peer review is the gold standard.

**Credibility with practitioners:** Moderate. Practitioners often find peer-reviewed papers dense, slow, and disconnected from practice. But they respect the credibility signal.

**Feedback mechanism:** The review process itself. But this is a *gate*, not an *invitation*. Peer review determines whether the paper is accepted, not whether the community improves it. And the feedback is private (reviewer to author), not public (community to framework).

**Versioning:** Nearly impossible. Once published, a paper is fixed. Errata exist, but a paper can't evolve. The next version is a new paper.

**Risk — and this is the critical one:** **You can't get through peer review with honest claims at four evidence tiers.** Peer review demands that you argue your case persuasively. A claims table that says "Tier 3: internally coherent but untested" and "Tier 4: aspirational hypothesis" would be exploited by reviewers as evidence that the paper isn't ready. You'd be forced to either overclaim (which contradicts the trust brand) or underclaim (which gets you rejected as insufficiently novel).

There's a deeper problem: the framework emerged from iterative practice, not controlled experiments. Peer review favours empirical validation over analytical coherence. You don't have randomised controlled trials comparing CAWDP to alternatives. You have rigorous design reasoning and one (complex) worked example. That's a conference paper at best — and a hard sell even there.

**When it works:** After empirical validation. If you run a controlled study (CAWDP vs. no-methodology, measuring failure rates, override rates, human satisfaction), you have a peer-reviewable paper. That's the Phase 2 play — months 3-12. Not now.

---

## Format 4: ArXiv Preprint (Academic Preprint, No Peer Review)

**What it signals:** This is an academic contribution intended for community review. Serious, citable, but not yet vetted.

**Credibility with academics:** Moderate-to-high. ArXiv is taken seriously in CS and AI. Preprints are citable. They signal "I intend this to be evaluated as academic work."

**Credibility with practitioners:** Low-to-moderate. ArXiv papers are written for academics. The language, structure, and conventions assume domain expertise. A practitioner encountering an ArXiv paper about agent design methodology will find it hard going.

**Feedback mechanism:** Weak. ArXiv has no built-in comment system. Feedback comes through email, citations, and follow-up papers — all high friction and low structure. The preprint is a broadcast, not a conversation.

**Versioning:** Moderate. You can post v1, v2, v3. But each version is a complete replacement, and there's no diff mechanism. The community treats ArXiv versions as snapshots, not iterations.

**Risk:** The ArXiv format pressures you toward academic conventions (formal notation, extensive literature review, narrow audience framing) that make the document less accessible to practitioners. You end up writing for reviewers rather than for users. And the absence of a feedback mechanism means you're publishing *to* the community, not *with* it.

**When it works:** When your primary audience is academics and you're approaching a conference submission. ArXiv is a staging ground, not a destination. Post the working paper on ArXiv after it's been refined through community comment — not instead of community comment.

---

## Format 5: Industry White Paper (Corporate/Consultancy Format)

**What it signals:** This is a professional analysis of a business problem, with a recommended approach. Authoritative but practical.

**Credibility with academics:** Low. White papers are marketing dressed as analysis. They overclaim, undercite, and serve the author's commercial interests. Even well-intentioned white papers are viewed with suspicion because the format has been degraded by consultancies selling solutions to the problems they identify.

**Credibility with practitioners:** High. Practitioners read white papers. They respect the business-relevance framing. They expect actionable recommendations.

**Feedback mechanism:** None. White papers are broadcast documents. You might get email responses, but there's no structural invitation for comment.

**Versioning:** Weak. White papers are one-time publications. An updated white paper is a new white paper.

**Risk — the fatal one:** **A white paper from the company selling CAWDP certification is an infomercial.** It doesn't matter how rigorous the content is. The format signals "this exists to sell you something." Future's Edge selling CAWDP certification while publishing CAWDP as a white paper creates the exact trust contradiction you've built the brand to avoid.

This is the "trust company with black-box methodology" problem made literal. Your own brand positioning says: "The methodology is free. Getting it right is what we sell." A white paper format makes the methodology look like it's part of the thing being sold.

**When it works:** For the 77% Challenge, trust assessments, and case study reports. White papers are excellent for proving value. They're wrong for introducing the methodology itself.

---

## Format 6: RFC (Request for Comments — IETF-style)

**What it signals:** This is a specification open for community review before standardisation. Technical, structured, process-oriented.

**Credibility with academics:** Moderate. RFCs are respected in technical communities but not typically in academic social science or HCI, which is where much of the agent governance conversation lives.

**Credibility with practitioners:** Moderate-to-high in engineering contexts. Low in management, policy, and executive contexts — which is where many CAWDP decisions will be made.

**Feedback mechanism:** Strong and structured. RFCs are designed for comment. The entire purpose is to solicit structured feedback before finalisation. This is the strongest feedback mechanism of any format.

**Versioning:** Strong. RFCs evolve through drafts (Internet Drafts → RFC). The versioning protocol is well-understood.

**Risk:** RFCs are for *specifications*, not *methodologies*. An RFC says "here's how the protocol works — tell us what's wrong." But CAWDP isn't a protocol. It's a design process. The RFC format would force you into specification language (MUST, SHOULD, MAY) that doesn't naturally fit a methodology. You'd be contorting the content to fit the container.

Also: the IETF RFC process is a community infrastructure, not just a document format. Publishing an RFC without the IETF community infrastructure is just calling something an RFC. It doesn't carry the weight of the IETF process behind it.

**When it works:** For specific technical components of CAWDP — the Template Architecture specification, the Epistemic Metadata Contract schema, the Trust Ledger Specification. These are protocols that could be RFCs. The methodology itself is not.

---

## Format 7: Working Paper (Academic + Open for Comment)

**What it signals:** This is a rigorous work-in-progress, intended for evaluation, not finality. It claims enough authority to be taken seriously but explicitly invites improvement.

**Credibility with academics:** High. Working papers are a standard academic format. They're citable. They signal serious intent. They're evaluated as contributions-in-progress, which matches your actual evidence state (rigorous, but untested).

**Credibility with practitioners:** Moderate-to-high, IF the language is accessible. Working papers can be written for dual audiences — the structure provides academic credibility while the content can remain practitioner-accessible. NIST did exactly this with the AI RMF: rigorous development process, but written to be usable by practitioners.

**Feedback mechanism:** You build it yourself. This is a feature, not a bug. The working paper format doesn't come with a built-in feedback mechanism (like RFCs) — but it also doesn't come with a built-in gate (like peer review). You can design the invitation for comment to match exactly what you need: structured feedback on specific claims, not a pass/fail judgment.

**Versioning:** Natural. Working papers are versioned by design. v1.0 → v1.1 → v2.0. The community expects and encourages iteration. No format is more natural for a framework that will evolve.

**Risk:** The main risk is that a working paper is taken as *less* than a peer-reviewed paper. But this is actually an advantage: it sets expectations correctly. You're not claiming final authority. You're claiming "this is rigorous enough to evaluate and practical enough to apply — help us make it better."

---

## The Decision Matrix

| Criterion | Blog | Manual | Peer-Reviewed | ArXiv | White Paper | RFC | Working Paper |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Academic credibility | 1 | 1 | 5 | 4 | 1 | 3 | 4 |
| Practitioner accessibility | 5 | 4 | 2 | 2 | 4 | 3 | 4 |
| Accommodates honest claims | 3 | 1 | 1 | 3 | 1 | 3 | 5 |
| Openness signal | 3 | 1 | 1 | 3 | 1 | 5 | 5 |
| Versioning | 2 | 4 | 1 | 3 | 2 | 5 | 5 |
| Structured feedback | 2 | 2 | 2 | 2 | 1 | 5 | 4* |
| Pathway to authority | 1 | 2 | 5 | 4 | 2 | 4 | 4 |
| Doesn't contradict brand | 3 | 3 | 2 | 4 | 1 | 3 | 5 |
| **Total** | **20** | **18** | **19** | **25** | **13** | **31** | **36** |

\* Working paper feedback is designed, not built-in. You add a structured comment mechanism alongside it.

---

## Why the Working Paper Wins: Five Reasons

### 1. It Matches Your Evidence State

Your honest position is: rigorously derived, internally coherent, analytically supported, but empirically untested. No format other than a working paper naturally accommodates this position.

- A blog post doesn't require evidence, so it can't signal that you have any.
- A peer-reviewed paper requires more evidence than you have, forcing overclaim.
- A white paper assumes the case is made, skipping the evidence question.
- A working paper says: "Here's what I've established, here's what I believe but haven't proven, here's what I need help with." That IS the epistemic honesty that CAWDP requires of agents.

The claims and evidence table that I recommended in the outline is a working paper convention. It's what academics expect. And it's what makes the document credible without being overclaiming: "I know what I know, and I know what I don't know."

### 2. It Doesn't Contradict the Brand

Your brand is trust. Your positioning is "the methodology is free, getting it right is what we sell." A white paper from Future's Edge is an infomercial. A peer-reviewed paper is premature. A blog post is unserious. A working paper is the only format that says "I'm sharing this openly because openness IS trust" — and means it structurally, not just rhetorically.

The NIST AI RMF was developed through exactly this process: an open, transparent, multi-stakeholder development over 18 months, with public feedback published on the NIST website. It's now the most cited AI governance framework in the US. The format was a working paper / public draft process, not a white paper, not a blog post, not a journal article.

### 3. It Creates a Natural Pathway to Everything That Comes After

The working paper is a *staging format*, not a destination. Here's the pathway it enables:

```
Working Paper v1.0 (Month 1-3)
  → Community comment and contribution (Month 3-6)
    → Working Paper v1.1 (incorporating feedback) (Month 6-8)
      → Conference paper submission (Month 6-12)
        → ArXiv preprint + conference presentation (Month 8-12)
          → Peer-reviewed journal paper (with empirical data from case studies) (Month 12-18)
            → Reference documentation (ReadTheDocs) + Specification (Month 18-24)
```

No other format creates this pathway naturally. A blog post doesn't lead to a conference paper. A white paper doesn't lead to a journal article. A working paper is the starting point that the academic community expects for everything that follows.

The Scrum Guide followed a similar trajectory: initial position paper (1995) → iterative refinement through community use → Scrum Guide (2010) → updated versions (2017, 2020) → certification ecosystem. The initial format was a working concept paper, not a product manual or blog post.

### 4. It Accommodates Provenance Without Making It the Main Story

The provenance section (Section 2 in the outline) is a natural working paper convention. Working papers routinely include methodology sections that explain how the framework was developed. This is where your iterative discovery story lives — as evidence of development process, not as personal narrative.

In a blog post, provenance looks like autobiography. In a peer-reviewed paper, it looks like a methods section (too narrow for your story). In a white paper, it looks like credential-building. In a working paper, it looks like what it is: methodology provenance, showing that the framework was discovered through iterative practice rather than assumed from theory.

### 5. It's the Only Format That Can Be Both Rigorous and Accessible Simultaneously

This is the "ArXiv meets RFC" element of my recommendation. The working paper format is flexible enough to serve both audiences:

- **For academics:** The claims hierarchy, the relationship to existing work, the explicit statement of gaps, and the invitation for comment signal that you understand and respect the academic process.
- **For practitioners:** The problem section (anchored in data they recognise), the worked example, and the plain-language framework description signal that this is designed to be used, not just studied.

The NIST AI RMF achieved exactly this: rigorous enough for 240+ contributing organisations to engage with, accessible enough for a CISO to hand to their team. The format was a public draft working paper with open comment periods.

The peer-reviewed paper format forces you into academic conventions that exclude practitioners. The blog post format gives you accessibility without credibility. The working paper gives you both — if you write it carefully.

---

## Why "ArXiv Meets RFC"

The working paper format draws from two traditions:

**From ArXiv (academic preprint):**
- Citable. Has a version number. Signals serious academic intent.
- Can be posted before peer review, establishing a timestamp and priority claim.
- Creates a reference point that later work can cite and build on.

**From RFC (Request for Comments):**
- The document *is* an invitation for comment, not a declaration of truth.
- The feedback mechanism is structural (you design how people respond).
- Versioning is expected and encouraged.
- The community understands that v1.0 is the start of a conversation, not the end of one.

Neither format alone would work. ArXiv without RFC's openness creates a broadcast with no feedback. RFC without ArXiv's academic credibility creates a specification without scholarly standing. The hybrid gives you both.

---

## What This Format Excludes (and Why That's Right)

**No marketing language.** The working paper format excludes "transform your agent deployment" and "the proven methodology." If you want marketing, write a blog post later. The working paper's credibility comes from restraint.

**No product roadmap.** Future's Edge certification, the Accretive Workspace, the Trust Score product — none of this belongs in the working paper. It belongs in the business plan. Including it would convert the working paper into a white paper, which is the infomercial problem.

**No "framework" as a noun.** You already decided: never use "framework" as a noun. The working paper describes a methodology, not a framework. This language choice is format-appropriate: working papers describe processes and methods, not static structures.

---

## The One Risk I Acknowledge

A working paper has less immediate authority than a peer-reviewed paper. When an executive asks "is this validated?", the honest answer is "it's a working paper, not a journal article." This is a real cost.

But the alternative — publishing as a white paper and claiming authority you haven't earned — is a higher cost. It contradicts the brand. It undermines trust. And it creates a credibility debt that compounds over time.

The working paper says: "I'm serious enough to cite, honest enough to admit what I don't know, and open enough to invite you to make it better." That IS the trust infrastructure brand, embodied at the document level.

---
