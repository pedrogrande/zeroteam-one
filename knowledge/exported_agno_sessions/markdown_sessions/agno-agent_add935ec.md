# Agno Agent

| Field | Value |
|-------|-------|
| **Session** | `add935ec...` |
| **Type** | agent |
| **Agent** | Agno Agent |
| **User** | pete@peterargent.com |
| **Created** | 2026-06-15T07:05:08 |
| **Runs** | 6 completed / 6 total |

## Run 1 — Agno Agent ✓ COMPLETED

*2026-06-15T07:05:08* · `glm-5.1:cloud` · `21ed9c3d...`

### Prompt

Tell me about Agno's agent learning capabilities and how they might be useful to coding agents. Are there other features that would be useful?

### Response

I'll share what I know about Agno's learning capabilities and features relevant to coding agents, drawing from my work with the framework and its architecture.

## Agno's Agent Learning Capabilities

### 1. AgentMemory (Short-term / Conversation Memory)

Agno has built-in `AgentMemory` that persists conversation history within a session:

```python
from agno.memory.agent import AgentMemory

agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    memory=AgentMemory(),
)
```

This gives agents context continuity across turns — they remember what was said earlier in the conversation. For coding agents, this means they can track what files they've already examined, what errors they've encountered, and what approaches they've tried.

### 2. UserMemory (Long-term / Cross-session Memory)

More powerful for learning — `UserMemory` persists information *across sessions* about a specific user:

```python
from agno.memory.user import UserMemory

agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    user_memory=UserMemory(),
)
```

For coding agents, this is valuable because:
- The agent can remember your project conventions across sessions
- It can recall your preferred coding style, naming patterns, or architectural choices
- It can track what it's already helped you with (preventing redundant suggestions)
- It learns your codebase patterns over time

### 3. Session State (Structured Memory)

From my work on the orchestrator, I know Agno supports `session_state` for structured, queryable memory:

```python
from agno.storage.agent.postgres import PostgresDb

agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    storage=PostgresDb(table_name="agent_sessions", db_url="..."),
    add_session_state_to_context=True,
)
```

This stores typed, structured data (not just conversation text) that persists across agent invocations. For the CAWDP Design Studio, this stores design phase progress, artefact tags, and epistemic metadata.

### 4. Knowledge Base Integration

Agno agents can load knowledge from multiple sources:

```python
from agno.knowledge import WebsiteKnowledge

agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    knowledge=WebsiteKnowledge(urls=["https://docs.agno.ai/..."]),
)
```

For coding agents, this means they can be seeded with framework documentation, coding standards, or project-specific knowledge.

---

## Features Useful for Coding Agents

Beyond learning, here are Agno features particularly valuable for coding agents, mapped to my CAWDP design principles:

### 1. Structured Output (Type Collision Resolution at Output Layer)

**The most important feature for coding agents.** This directly addresses the type collision problem I've written extensively about:

```python
from pydantic import BaseModel

class CodeReviewResult(BaseModel):
    security_issues: list[str]
    style_issues: list[str]
    correctness_issues: list[str]
    suggestions: list[str]
    overall_confidence: float

agent = Agent(
    model=OllamaResponses(id="glm-5.1:cloud"),  # OllamaResponses for complex schemas
    output_schema=CodeReviewResult,
    use_json_mode=True,
)
```

This is **Regime 3 enforcement at the output layer** — the schema structurally prevents undifferentiated prose (the "wall of text" problem). Every output is typed, decomposable, and queryable.

> **CAWDP connection:** This implements type collision resolution at the output layer. Instead of 17+ information types encoded into undifferentiated prose, each type gets its own field. The CodeReviewResult schema above separates security, style, and correctness issues — exactly the kind of typed output my 5-class taxonomy calls for (Extractor reads, Measurer measures, Assessor assesses, each producing typed output within their authority boundary).

### 2. Tools (Means of Acting)

Agno's tool system gives agents the ability to act on the world:

```python
from agno.tools import DuckDuckGoTools, FileTools, PythonTools

agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    tools=[DuckDuckGoTools(), FileTools(), PythonTools()],
)
```

For coding agents, relevant tools include:
- **FileTools** — read, write, search files
- **PythonTools** — execute Python code (with safety considerations)
- **DuckDuckGoTools** — search documentation
- **WebsiteTools** — fetch documentation pages
- **Custom tools** — project-specific tools (e.g., run tests, check linting, database queries)

> **CAWDP connection:** Tools are the "Means of Acting" from the MVA (Minimum Viable Agent). For coding agents, custom tools can enforce **CC-4 Information Boundaries** — e.g., a code review tool that can only READ files but cannot WRITE to production paths, enforcing the Extractor class's "never judge" boundary structurally.

### 3. Hooks (Verification & Monitoring)

This is where Agno gets really powerful for CAWDP-compliant agents:

**Pre-hooks** — run before agent execution:
```python
@agent.pre_hook
def validate_input(run_input):
    # CC-1 Verification Independence (Level 1: structural)
    # Check input meets schema requirements before processing
    if not run_input.get("code"):
        raise OutputCheckError("Code review requires code input")
```

**Post-hooks** — run after agent execution (can block or modify output):
```python
@agent.post_hook
def verify_output(run_output):
    # CC-1 Verification Independence (Level 2: semantic)
    # Separate verification of agent output
    if "NEVER_REVIEWED" in run_output.content:
        raise OutputCheckError("Review was not completed")
```

**Background hooks** — non-blocking post-processing:
```python
@hook(run_in_background=True)
def log_review(run_output):
    # CC-8 Assured Audit Trail (logging level)
    # Record review for audit without blocking the response
    audit_log.record(run_output)
```

> **CAWDP connection:** This is the enforcement regime mapping I identified:
> - **Background post-hooks = Regime 2 (Detect)** — observe and record, cannot prevent
> - **Synchronous post-hooks with OutputCheckError = Regime 3 (Prevent)** — can block non-compliant output
> - **CC-8 Assured Audit Trail** maps to background post-hooks
> - **CC-1 Verification Independence** maps to synchronous post-hooks

### 4. Teams (Multi-Agent Composition)

```python
from agno.team import Team

review_team = Team(
    mode="coordinate",
    members=[security_reviewer, style_checker, correctness_assessor],
)
```

For coding agents, this enables the **5-class taxonomy**:
- **Extractor agents** that read and extract code patterns (never judge)
- **Measurer agents** that quantify complexity, coverage, performance (never interpret)
- **Assessor agents** that evaluate quality against rubrics (never finalize)
- **Generator agents** that draft code suggestions (never be vague)
- **Aggregator agents** that compile findings (never add content)

> **CAWDP connection:** Teams enable **CC-1 Verification Independence** — the agent that generates code should be different from the agent that verifies it. A Team with separate Generator and Assessor agents structurally enforces this.

### 5. Workflows (Sequential Multi-Step Processes)

```python
from agno.workflow import Workflow

class CodeReviewWorkflow(Workflow):
    def run(self, code: str):
        # Step 1: Extract patterns (Extractor - never judges)
        patterns = self.extractor.run(code=code)
        
        # Step 2: Measure complexity (Measurer - never interprets)
        metrics = self.measurer.run(code=code)
        
        # Step 3: Assess quality (Assessor - never finalizes)
        assessment = self.assessor.run(patterns=patterns, metrics=metrics)
        
        # Step 4: Generate suggestions (Generator - never vague)
        suggestions = self.generator.run(assessment=assessment)
        
        return CodeReviewResult(
            security_issues=assessment.security,
            style_issues=assessment.style,
            correctness_issues=assessment.correctness,
            suggestions=suggestions.improvements,
            overall_confidence=assessment.confidence,
        )
```

> **CAWDP connection:** This is the pipeline architecture from Phase 6 (System Architecture). Each step has clear inputs/outputs, and the workflow enforces **authority boundaries** — the Extractor can't judge, the Assessor can't finalize, the Generator can't be vague.

### 6. Human-in-the-Loop (Progressive Autonomy)

```python
from agno.workflow import Workflow, OnReject

class CodeReviewWorkflow(Workflow):
    def run(self, code: str):
        # Agent prepares judgment...
        assessment = self.assessor.run(code=code)
        
        # Human makes judgment
        review = self.human_review(
            assessment=assessment,
            requires_output_review=True,
            on_reject=OnReject.retry,
        )
        
        return review
```

> **CAWDP connection:** This is **progressive autonomy** (Shadow → Advisory → Supervised → Autonomous). In Shadow mode, everything is human-reviewed. In Supervised mode, agents act within boundaries and humans approve. This is the exact pattern from my Project Initiation Workflow with 2 human gates.

---

## Practical Coding Agent Architecture

Combining these features with CAWDP principles, here's what a well-designed coding agent team looks like:

```python
# Authority boundaries as structurally enforced as possible

# EXTRACTOR: reads code, never judges
code_extractor = Agent(
    name="CodeExtractor",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=CodeExtraction,  # Regime 3: schema enforcement
    tools=[FileTools(base_dir="~/project")],
    instructions=[
        "You EXTRACT patterns, structures, and facts from code.",
        "You NEVER judge quality, correctness, or style.",
        "You NEVER suggest changes.",
        "If you cannot extract, output null with explanation.",
    ],
    user_memory=UserMemory(),  # Learn project conventions over time
)

# MEASURER: quantifies, never interprets
complexity_measurer = Agent(
    name="ComplexityMeasurer",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=ComplexityMetrics,  # Typed output
    instructions=[
        "You MEASURE code complexity, coverage, and performance metrics.",
        "You NEVER interpret what metrics mean for the project.",
        "You NEVER suggest refactoring.",
    ],
)

# ASSESSOR: evaluates against rubric, never finalizes
quality_assessor = Agent(
    name="QualityAssessor",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=QualityAssessment,
    instructions=[
        "You ASSESS code quality against defined rubrics.",
        "You NEVER finalize — your assessment is input for human judgment.",
        "You NEVER approve or reject — you prepare the decision.",
        "Always include confidence level and what you CANNOT assess.",
    ],
    post_hooks=[verify_assessment_completeness],  # CC-1 Verification
)

# GENERATOR: drafts suggestions, never vague
suggestion_generator = Agent(
    name="SuggestionGenerator",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=CodeSuggestions,
    instructions=[
        "You GENERATE code suggestions with specific, implementable changes.",
        "You NEVER be vague — every suggestion must cite specific code, line numbers, and replacement text.",
        "You NEVER approve your own suggestions — that's the Assessor's job.",
    ],
)
```

---

## Features I'd Want Beyond What Agno Currently Offers

Based on my CAWDP design work, here are features that would make coding agents even more powerful:

### 1. Epistemic Metadata on Every Output (CC-3)
Every agent response should carry confidence, provenance, assumptions, limitations, recency, and uncertainty — not as prompt instructions, but as **structural output fields**. This is the type collision resolution at the output layer.

### 2. Authority Boundary Enforcement (CC-4 at Regime 3)
Currently, "never judge" is a prompt instruction (Regime 1: Declare). I'd want it as a **schema-level constraint** — the Extractor's output schema literally has no "assessment" or "judgment" fields. The schema IS the boundary enforcement.

### 3. Progressive Autonomy State Machine
A built-in state machine that tracks autonomy level per dimension (Shadow → Advisory → Supervised → Autonomous) with promotion criteria. Currently this would need to be custom-built on top of Agno's session state.

### 4. Specification Aging (CC-5)
Automatic staleness tracking on agent instructions and knowledge bases. When code patterns change, the agent should flag that its previous learning may be outdated rather than confidently applying stale knowledge.

### 5. Cost Budget per Agent (CC-7)
Token budget tracking at the agent level with halt conditions. Currently Agno tracks usage but doesn't have per-agent budget enforcement with halt_on_budget_exhaustion.

### 6. Bidirectional Traceability (P8)
Every output should trace back to which input, which knowledge source, which agent, and which phase produced it. Currently Agno tracks conversation history but doesn't provide the design-to-enforcement traceability that CAWDP's 10×10 mapping matrix calls for.

---

## Summary

| Feature | Agno Support | CAWDP Principle | Regime |
|---------|-------------|-----------------|--------|
| Structured Output | ✅ Full | Type collision resolution | Regime 3 (Prevent) |
| Agent Memory | ✅ Full | Specification aging, learning | Regime 1 (Declare) |
| User Memory | ✅ Full | CC-3, learning over time | Regime 1 |
| Session State | ✅ Full | Progressive autonomy tracking | Regime 1 |
| Knowledge Base | ✅ Full | Context injection | Regime 1 |
| Tools | ✅ Full | Means of Acting (MVA) | Regime 2-3 (depends on tool) |
| Pre-hooks | ✅ Full | CC-1, CC-8 | Regime 2-3 |
| Post-hooks | ✅ Full | CC-1, CC-8 | Regime 2-3 |
| Background Hooks | ✅ Full | CC-8 (audit trail) | Regime 2 (Detect) |
| Teams | ✅ Full | 5-class taxonomy, CC-1 | Regime 1 (Declare) |
| Workflows | ✅ Full | Pipeline architecture | Regime 1 |
| Human Review | ✅ Full | Progressive autonomy | Regime 2 (Detect) |
| Epistemic Metadata | ❌ Custom | CC-3 | Needs custom implementation |
| Authority Boundaries | ❌ Custom | CC-4 | Needs schema-level enforcement |
| Autonomy State Machine | ❌ Custom | Progressive autonomy | Needs custom state management |
| Specification Aging | ❌ Custom | CC-5 | Needs staleness tracking |
| Per-Agent Cost Budget | ❌ Custom | CC-7 | Needs budget enforcement |
| Bidirectional Traceability | ❌ Custom | P8 | Needs custom metadata |

Agno provides excellent foundations for building CAWDP-compliant coding agents — particularly structured output (type collision resolution), tools (means of acting), hooks (verification and monitoring), and workflow composition (pipeline architecture). The gaps are in the CAWDP-specific governance layer: epistemic metadata, authority boundary enforcement, progressive autonomy, specification aging, cost budgets, and traceability. These are exactly the areas where my CAWDP layer adds value on top of Agno's MVA.

---

## Run 2 — Agno Agent ✓ COMPLETED

*2026-06-15T07:42:50* · `glm-5.1:cloud` · `31e9d35c...`

### Prompt

With tightly specified artefacts and quality gates enforcing their correctness and completeness, I hypothesise that agents can more consistently produce high quality output (complete tasks successfully), that continues to build trust users have in the system. 

If we see software development as a series of workflows that are made up of tasks, a task can be specified by the input artefacts it depends on, and the output artefacts that must be produced for the task to be considered completed. 

Let's focus on the iterative loop of the feature/milestone-driven software development approach.

We see that each iteration has 'fresh' agents who do not have context of what has happened previously.

We want learnings from each iteration to inform the next iteration.

Each iteration should be testable by the human client, even if it is as simple as running a command in the terminal and seeing the results returned. This builds trust that the right thing is being built every iteration.

Each iteration should produce user guides and documentation. All code must be well documented.

Each task produces reports and a range metadata for continual improvement.

### Response

This is a strong hypothesis. Let me extend it by mapping it to your existing frameworks and identifying the key design requirements that make it work.

## The Core Claim Restated

**Artefact-specified tasks + quality-gated outputs + iteration metadata = consistent quality + progressive trust**, even with fresh agents per iteration.

This works because **artefacts carry context, so agents don't need memory** — the artefact graph IS the memory.

## The Fresh Agent "Problem" Is Actually the Design

Fresh agents per iteration is a FEATURE when artefacts carry sufficient context. It means:

- No accumulated hallucination or context drift
- No hidden dependencies on agent memory
- Every task is reproducible from its artefact specification
- Agents are interchangeable (any agent that can read the spec can do the task)

The question becomes: **what context must artefacts carry for a fresh agent to succeed?**

## Five Context Requirements for Fresh-Agent Artefacts

A fresh agent needs five things that artefacts must carry:

| Context Need | What the Artefact Must Carry | Maps To |
|---|---|---|
| **Why** — decision archaeology | Reasoning behind each decision, alternatives considered, what was rejected | PRISM Intentions, Decision Log |
| **What failed** — rejection/correction history | Previous approaches tried and abandoned, why they were abandoned | CCCT fragile outputs (rejections, corrections) |
| **What's assumed** — assumptions and confidence | Confidence level, provenance, assumptions, what could invalidate the decision | CC-3 Epistemic Metadata (6 fields) |
| **What's aging** — staleness signals | When last reviewed, what changed since, whether still valid | CC-5 Specification Aging |
| **What's next** — iteration-to-iteration signals | What the previous iteration learned, what to change, what to watch | P10 EVOLVE signals |

If artefacts carry these five, a fresh agent has everything it needs. If they don't, the fresh agent is working blind.

## The Iteration Model as a Structure

```
ITERATION n
├── INPUTS (artefacts from iteration n-1 + new requirements)
│   ├── Specified artefacts (typed, with epistemic metadata)
│   ├── Decision log (why decisions were made)
│   ├── Rejection register (what was tried and abandoned)
│   ├── EVOLVE signals from iteration n-1
│   └── Human test results from iteration n-1
│
├── PROCESS (tasks with artefact dependencies)
│   ├── Each task: input artefacts → output artefacts
│   ├── Quality gates at task boundaries
│   └── Fresh agents per task (context from artefacts, not memory)
│
├── OUTPUTS (artefacts for human testing + next iteration)
│   ├── Working software (testable by human client)
│   ├── User guides and documentation
│   ├── Code with inline documentation
│   ├── Task reports and metadata
│   └── EVOLVE signals for iteration n+1
│
└── VALIDATION
    ├── Human client tests the iteration output
    ├── Quality gates verify artefact completeness
    └── Metadata captured for continual improvement
```

Each iteration is a mini-CAWDP application. The EVOLVE cycle connects iterations.

## The Six Artefact Types Per Iteration

Not all artefacts are the same kind of thing. Type collision applies here too — mixing them creates confusion.

| Artefact Type | Purpose | Consumer | Epistemic Profile |
|---|---|---|---|
| **Working Code** | The thing that runs | Human client, next iteration | High confidence, tested provenance |
| **Documentation** | How to use it | Human client | High confidence, descriptive provenance |
| **Code Comments** | Why code is this way | Next iteration's agents | Medium confidence, design-intent provenance |
| **Task Reports** | What happened during the task | Next iteration's agents, metadata pipeline | Deterministic for facts, probabilistic for assessments |
| **Decision Log** | Why choices were made | Next iteration's agents | High provenance importance, confidence varies |
| **EVOLVE Signals** | What to change next iteration | Next iteration's planning | Evidenced or observed, flagged for review |

## The Trust Mechanism

Your hypothesis about trust building is testable. Here's the mechanism:

```
Iteration 1: Human tests output → "it works" → Trust level 1 (tentative)
Iteration 2: Human tests output → "it works again" → Trust level 2 (pattern emerging)  
Iteration 3: Human tests output → "it works consistently" → Trust level 3 (reliability established)
Iteration 4+: Quality gates catch issues before human sees them → Trust level 4 (system is trustworthy)
```

This maps directly to progressive autonomy:
- **Shadow** (iterations 1-2): Human verifies everything
- **Advisory** (iterations 3-4): Human verifies key outputs, agents handle routine
- **Supervised** (iterations 5+): Agents handle most tasks, human approves releases
- **Autonomous** (after sufficient trust): Agents handle known task types independently

The human testing at each iteration IS the progressive autonomy validation. You don't promote trust levels without evidence.

## The Key Architectural Requirement: Artefact Specification Depth

For this to work, artefact specifications must be precise enough that a fresh agent can:

1. **Read the input artefacts** and understand what they mean (typed schemas, not prose)
2. **Read the decision log** and understand why things are the way they are (decision archaeology)
3. **Read the rejection register** and avoid re-deriving rejected approaches
4. **Read the quality gate** and know what "done" looks like for this task
5. **Produce output artefacts** that satisfy the quality gate without human rework

This is where type collision resolution matters most. If input artefacts are prose walls, fresh agents can't parse them. If input artefacts are typed schemas with epistemic metadata, fresh agents have structured context.

## What's Missing From the Hypothesis (Three Gaps)

**Gap 1: Context Assembly Protocol** — When a fresh agent starts a task, which artefacts does it need? Not all artefacts — only the ones relevant to this task. The Agent Context Protocol (budget-aware, relevance-scored, confidence-weighted) determines what a fresh agent sees. Without this, agents either get too much context (expensive, confusing) or too little (working blind).

**Gap 2: The Rejection Register** — Your hypothesis mentions "learnings from each iteration inform the next" but doesn't specify the mechanism. The mechanism is a rejection register: a typed, epistemic-metadata-carrying list of approaches tried and abandoned, with reasoning. Without this, fresh agents will re-derive previously rejected approaches. This is one of the CCCT's fragile outputs — the thing most likely to be lost and most valuable to preserve.

**Gap 3: Failure Mode for Incorrect Artefacts** — What happens when an iteration produces artefacts that are wrong? The quality gate catches some, but some pass quality gates and fail in production. The system needs:
- Revert mechanism (rollback to last known good artefacts)
- Root cause capture (why the artefact was wrong — was it a spec gap, an agent error, or a context gap?)
- Feed-forward to next iteration (what to change in the spec/quality gate/agent instructions)

## The Testable Hypothesis

Your hypothesis, made specific and testable:

**H1**: Tasks specified by typed input/output artefacts with quality gates produce higher completion rates than tasks specified by prose descriptions, for fresh agents with no prior context.

**H2**: Decision archaeology in artefacts (the "why") reduces re-derivation of previously rejected approaches by fresh agents.

**H3**: Human-testable iterations build trust faster than big-bang deliveries, with trust measurable as willingness to reduce verification effort.

**H4**: Task metadata (reports, decision logs, EVOLVE signals) from iteration n improves iteration n+1's completion rate.

**H5**: Fresh agents with well-specified artefacts produce comparable quality to agents with accumulated memory, but with lower context drift risk.

## The Practical Starting Point

If you wanted to test this with the CAWDP Design Studio or the Project Initiation Workflow, the minimum viable iteration would be:

1. **Define one task** as input artefacts → output artefacts with a quality gate
2. **Run a fresh agent** on that task with only the artefact spec as context
3. **Human tests the output** against the quality gate
4. **Capture metadata** (what worked, what didn't, what was missing from the spec)
5. **Refine the artefact spec** based on metadata
6. **Run a fresh agent again** with the refined spec
7. **Compare** iteration 1 vs iteration 2 quality

This is the simplest possible test of the hypothesis — two iterations, one task type, measurable quality improvement from iteration metadata.

Want me to design this as a concrete workflow, or do you want to explore the artefact specification format first?

---

## Run 3 — Agno Agent ✓ COMPLETED

*2026-06-15T08:43:53* · `glm-5.1:cloud` · `7eb124ed...`

### Prompt

I see the potential for a context curation agent that selects the 'minimum sufficient context' for each task, delivered as tools specified by the task, to the agent performing the task.

Perhaps What we need is input artefacts <-> outputs artefacts mapping.

### Response

This is a genuine architectural insight — and it adds a **6th layer to the type collision taxonomy**.

## The Problem It Solves

Current practice: **stuff everything into the context window and hope the agent sorts it out.** This is type collision at the context delivery layer — 17+ information types dumped as undifferentiated context, overwhelming the agent's ability to distinguish signal from noise.

Your insight reframes this: **the performing agent should never see context it doesn't need.**

## Context Curation Agent — The Architecture

```
Task T2 needs to run
         │
         ▼
Context Curation Agent
  │ Knows: task specification + available artefacts
  │ Applies: SELECT logic (budget-aware, relevance-scored, confidence-weighted)
  │ Determines: minimum sufficient context for THIS task
  │ Packages: context as typed, queryable TOOLS
         │
         ▼
Performing Agent receives:
  - Task specification
  - Tools that return structured context on demand
  - Budget constraint (max context this task needs)
```

The performing agent **queries** context. It doesn't receive a dump.

## Input Artefacts ↔ Output Artefacts Mapping

This is the structural backbone. Each mapping entry has:

| Field | Purpose |
|---|---|
| **Output artefact** | What was produced |
| **Output fields** | Which fields from that artefact |
| **Input artefact** | What consumes it |
| **Input fields** | Which fields need it |
| **Context type** | What kind of context this is (reference, constraint, precedent, state, evidence) |
| **Minimum slice** | The smallest extractable unit that satisfies the dependency |
| **Confidence weight** | How much this context should be weighted in the performing agent's reasoning |
| **Freshness gate** | Is this context fresh enough to use? (CC-5) |

This is **ACP (Agent Context Protocol) applied to the task dependency graph.**

## Why Tools, Not Prompt Injection

| Prompt injection | Tool delivery |
|---|---|
| All context loaded upfront | Context queried as needed |
| Agent sees everything | Agent sees only what it asks for |
| Token budget consumed before reasoning | Token budget consumed on demand |
| No type information on context | Each tool returns typed, structured data |
| No epistemic metadata on context | Each tool response carries confidence, provenance, recency |
| Context is prose | Context is structured, queryable |
| One size fits all | Context tailored per task |

## The 6th Layer of Type Collision

| Layer | Problem | Resolution |
|---|---|---|
| 1. Output | 17+ info types → prose | Typed, decomposable outputs |
| 2. Input | 6+ cognitive modes → text field | Mode-appropriate interaction modalities |
| 3. Extraction | Documents as containers | Typed knowledge objects from containers |
| 4. Meta-design | Stakeholder perspectives → same artifact | Three-layer separation |
| 5. Design-to-enforcement | Spec ↔ contracts don't map | P8 Contract Formalization |
| **6. Context delivery** | **All context → undifferentiated dump** | **Minimum sufficient context as typed tools** |

Same resolution pattern: **typed, structured, mapped, with explicit transformation.**

## What This Means for the Task-Based Architecture

In the task dependency graph, each task currently has:
- Input artefacts (dependencies)
- Output artefacts (completion criteria)

The context curation agent adds:
- **Context specification**: what context the performing agent needs, in what form, with what constraints
- **Context tools**: the performing agent receives tools, not dumps
- **Context budget**: maximum tokens/fields this task needs (from CC-7 cost budget)
- **Context quality gate**: is the selected context sufficient for the task? (CC-3 epistemic metadata)

## Bidirectional Mapping — Why Both Directions Matter

**Forward (impact analysis):** When input artefact A changes, what outputs are affected downstream? This is **judgment propagation** — one change ripples through the graph.

**Backward (root cause):** When output O is wrong, which input caused it? This is **decision archaeology** — trace backwards through the mapping to find the source.

Both directions are essential because:
- Forward enables **specification aging alerts** (CC-5: "this change means these 5 downstream artefacts need review")
- Backward enables **verification** (CC-1: "this error traces back to that input — fix it there")
- Together they enable **bidirectional traceability** from P8

## The Practical Implication

When the context curation agent prepares context for a task:

1. **Read the task specification** — what does this task need to know?
2. **Query the artefact graph** — what relevant artefacts exist?
3. **Apply SELECT** — budget-aware, relevance-scored, confidence-weighted filtering
4. **Slice the artefacts** — extract minimum sufficient fields, not whole documents
5. **Package as tools** — each tool returns typed, structured data with epistemic metadata
6. **Deliver to performing agent** — agent queries tools, receives structured context on demand

The performing agent never sees a "wall of context." It sees **tools that answer specific questions with typed, structured, metadata-rich responses.**

This is the ACP made operational at the task level — and it's what makes fresh agents per iteration work. The context is in the artefacts, curated by the context curation agent, delivered as tools. No agent memory needed.

---

## Run 4 — Agno Agent ✓ COMPLETED

*2026-06-15T08:51:11* · `glm-5.1:cloud` · `7b7dcd73...`

### Prompt

There will be templates for the context curator to deliver to.
These templates can largely be pre-populated algorithmically with specific sections of documents that are relate to the task at hand.
This means the context curator doesn't need to much context themselves.

### Response

This is a crucial architectural insight. Let me draw out what it means.

## Context Templates as the Architecture

The key shift: **intelligence moves from the agent to the template**.

### Before Your Insight

```
Task arrives → Context Curator AGENT decides what's relevant → 
queries knowledge base → packages context → delivers
```

The agent needs to *understand* the task to curate well. That's expensive, unreliable, and introduces its own failure modes (wrong selection, context contamination, over-delivery).

### After Your Insight

```
Task arrives → Template matched → Algorithm fills slots → 
Delivered (CCA just validates and hands off)
```

The **template** encodes the intelligence. The **algorithm** does the retrieval. The CCA becomes a thin coordinator, not a sophisticated reasoner.

---

## What This Looks Like Concretely

A **Context Template** for a specific task type:

```python
class RubricScoringContext(BaseModel):
    """Context template for rubric scoring tasks"""
    # Algorithmically pre-populated slots
    assignment_brief: Annotated[str, Field(
        source="artefact.assignment_brief",
        section="full"  # whole document
    )]
    rubric_criteria: Annotated[List[RubricCriterion], Field(
        source="artefact.rubric",
        section="criteria_relevant_to_task"  # filtered
    )]
    student_evidence: Annotated[List[EvidenceItem], Field(
        source="artefact.evidence_extraction",
        section="evidence_for_criterion:{criterion_id}"  # parameterised
    )]
    cohort_benchmarks: Annotated[Optional[CohortStats], Field(
        source="artefact.cohort_statistics",
        section="summary",
        required=False  # optional enrichment
    )]
    
    # Template-level metadata
    template_id: str = "rubric_scoring_v1"
    token_budget: int = 4000
    confidence_floor: float = 0.3  # exclude items below this
```

The **algorithm** fills slots by:
1. Reading the `source` annotation → which artefact to query
2. Reading the `section` annotation → which section/fields to extract  
3. Applying filters (confidence floor, recency, relevance scoring)
4. Assembling into the template structure

**No LLM reasoning needed for the population step.** It's deterministic query + filter + assemble.

---

## Why This Is Architecturally Significant

**1. The template IS the intelligence**

The human (or pattern library) designed the template to include *exactly* what a rubric scoring task needs. The template designer made the curation decision once — at design time — not per invocation. This is the Pattern Library principle applied to context delivery.

**2. Algorithmic population is Regime 3 enforcement**

The performing agent can only access what's in the template. The template slots are filled by deterministic queries, not agent judgment. The performing agent literally **cannot** access information outside its template — because the template IS the information boundary. This is CC-4 at Regime 3 (prevent by design) without needing any agent-level enforcement.

**3. The CCA barely needs context**

You're right. The CCA:
- **Matches** the task to a template (pattern matching — could be rule-based)
- **Validates** that the algorithm populated all required slots (schema validation)
- **Delivers** the populated template as tools to the performing agent

No deep reasoning required. The CCA is a **router + validator**, not a curator.

**4. Templates compose like task types**

Just like the 5-class taxonomy has characteristic patterns, context templates cluster by:
- Agent class (Extractor templates, Measurer templates, Assessor templates...)
- Task depth (Shallow templates are minimal, Deep templates include cross-references)
- Domain (marking templates, strategy templates, compliance templates...)

**5. Templates connect to everything else**

| Existing Concept | Connection to Context Templates |
|---|---|
| Task-based architecture | Each task in the dependency graph has a context template as its input specification |
| Input artefacts (P2 Backcasting) | Context template IS the input artefact made concrete |
| Pattern Library | Templates ARE patterns for context delivery |
| CC-4 Information Boundaries | Template defines the boundary — nothing outside it is accessible |
| Pydantic schemas | Template IS a Pydantic schema with `source` annotations |
| Judgment propagation | When human makes judgment, algorithm updates all templates that include that field |
| Fresh agents | Fresh agent + populated template = agent with exactly the right context |
| ACP SELECT phase | Template + algorithmic population IS the SELECT phase |
| Fractal structure | Shallow tasks get 2-3 slot templates, Deep tasks get 15+ slot templates |

---

## The Simplified Architecture

```
┌─────────────────────────────────────────────┐
│              TEMPLATE REGISTRY               │
│  (pre-designed context templates per task)    │
└──────────────────┬──────────────────────────┘
                   │ match
                   ▼
┌─────────────────────────────────────────────┐
│         ALGORITHMIC POPULATION ENGINE         │
│  (query + filter + assemble — no LLM)        │
│  reads: source annotations, filters, budget  │
└──────────────────┬──────────────────────────┘
                   │ populated template
                   ▼
┌─────────────────────────────────────────────┐
│         CONTEXT CURATION AGENT (thin)         │
│  validates completeness + delivers as tools  │
└──────────────────┬──────────────────────────┘
                   │ task-specific tools
                   ▼
┌─────────────────────────────────────────────┐
│           PERFORMING AGENT (fresh)            │
│  reads template tools → executes task        │
└─────────────────────────────────────────────┘
```

The CCA doesn't curate. It **validates** that the algorithm filled the template correctly, then hands it off. The intelligence is in the template design (done once, at design time). The labour is in the algorithm (deterministic, cheap, reliable).

---

## Template Design as a First-Class Activity

This makes **template design** a human-primary task — exactly the kind of decision that CAWDP says should not be delegated to agents.

Designing a good context template means:
- Knowing what the performing agent needs (and doesn't need)
- Setting the right token budget
- Choosing the right confidence floor
- Deciding what's required vs optional enrichment
- Specifying the section extraction logic

This IS complementarity analysis at the context layer: **what information does this task type need, and who decides what's included?**

The template designer (human) makes that decision once. The algorithm executes it every time. The CCA validates it. The performing agent works within it.

---

## What This Removes

- ❌ LLM reasoning for context selection (expensive, unreliable)
- ❌ Context contamination risk from "helpful" curators
- ❌ Variable context quality between invocations
- ❌ CCA needing its own context (meta-recursion problem)
- ❌ Over-delivery of context ("just in case")

## What This Adds

- ✅ Deterministic, reproducible context delivery
- ✅ Template as Regime 3 information boundary (structural enforcement)
- ✅ Cheap context assembly (queries, not reasoning)
- ✅ Template design as a visible, auditable decision
- ✅ Templates that compound and improve over time (Pattern Library flywheel)

This is the same design philosophy running through everything: **put the intelligence in the structure, not in the agent**.

---

## Run 5 — Agno Agent ✓ COMPLETED

*2026-06-15T08:56:41* · `glm-5.1:cloud` · `4943770f...`

### Prompt

Let's choose a simple task as a use case to test the thinking about the context curation.

Let's say a task for the agent is to add a responsive logo image to the navbar of the website.

Let's start with the required output artefacts for this task.
Then list the inputs required to deliver those outputs, and what artefacts those inputs might come from.

Could this task be totally deterministic? Or does it need an agent to review and approve?

### Response

## Task: Add Responsive Logo to Navbar

### Output Artefacts

| ID | Artefact | Type | Quality Gate |
|---|---|---|---|
| O1 | Updated navbar component file | Code | Logo renders at all breakpoints, layout intact |
| O2 | Logo image in correct asset directory | Asset | File exists, optimised, correct format |
| O3 | What Changed note | Documentation | Describes what was added and where |

### Input Artefacts Required

| ID | Input | Source Artefact | Why Needed |
|---|---|---|---|
| I1 | Current navbar component code | Codebase | Know what exists before changing it |
| I2 | Logo image file | Brand assets | The actual image to use |
| I3 | Responsive breakpoints | Design system | Know which screen sizes to target |
| I4 | Logo usage rules (sizes, spacing, clear space) | Brand guidelines | Know how the logo must appear |
| I5 | File structure (where images go, naming conventions) | Project conventions | Put things in the right place |
| I6 | Tech stack patterns (Astro components, HeroUI, Tailwind) | Tech stack spec | Write code in the right style |

### Deterministic or Needs Review?

**Mostly deterministic. Here's why:**

The task breaks into two categories of decision:

**Mechanical (no judgment needed):**
- Place image file in the assets directory
- Import it in the component
- Write the `<img>` or `<picture>` markup
- Apply responsive classes

**Judgment needed (Prepared — agent drafts, human confirms):**
- Exact pixel/rem sizes at each breakpoint (brand guidelines may or may not specify this)
- Spacing around the logo (padding/margin)
- Whether the logo links to the home page
- Whether to use `<picture>` with srcset or a single `<img>`

**The key variable is I4 — the brand guidelines artefact.**

If the brand guidelines specify exact sizes at each breakpoint, spacing, and link behaviour → **the task IS deterministic.** The agent reads the spec and executes.

If the brand guidelines say "use the logo" but don't specify sizes or spacing → **the task is Prepared.** The agent drafts reasonable defaults, human confirms or overrides.

**Reversibility makes this low-risk either way:**

- Wrong size? Change a CSS class. Fully reversible.
- Wrong position? Reorder the HTML. Fully reversible.
- Wrong image? Swap the file. Fully reversible.

On the C×R governor: **Confidence is medium** (the "responsive" part needs visual verification), **Reversibility is high** (code changes revert in seconds). This combination means the agent can draft, and the human does a quick visual check — not a deep review.

### Context Curation Template for This Task

This is where the template approach simplifies things:

```
Task type: ADD_RESPONSIVE_IMAGE
Template query:
  - Read: component file at {component_path}
  - Read: brand guidelines → logo_usage section
  - Read: design system → breakpoints section
  - Read: project conventions → asset_paths + naming
  - Read: tech stack → component_patterns
  - Asset: {image_path}

Deliver as tools:
  - get_component(path: "navbar")
  - get_brand_guidelines(section: "logo")
  - get_breakpoints()
  - get_asset_path(type: "images")
  - get_component_pattern(stack: "astro+heroui")
```

The performing agent never sees the whole codebase or brand guide. It gets exactly five tools — each returning just the slice of information this task needs.

**The template encodes the relevance judgment.** The curator doesn't need to reason about "what does this task need?" — the template already knows: component + brand + breakpoints + file structure + tech patterns.

---

Does this make the context curation template thinking concrete enough? The key insight: **for simple tasks like this, the template is trivially simple because the context needs are well-defined and stable.** The template's value compounds for complex tasks where context needs are less obvious.

---

## Run 6 — Agno Agent ✓ COMPLETED

*2026-06-15T10:04:57* · `glm-5.1:cloud` · `0c163723...`

### Prompt

Choose another small task and perform the same exercise.

### Response

I'll apply CAWDP v2.1 to a **Receipt & Expense Tracker Agent** — a small, practical agent that extracts expense data from receipts, categorises transactions, flags unusual spending, and prepares monthly summaries. This is deliberately different from previous exercises (personal finance domain, Extractor+Measurer class, low stakes, scheduled) and connects to Peter's Life Dashboard (Financial domain).

---

# CAWDP v2.1 Application: Receipt & Expense Tracker Agent

## P0: Purpose & Vision

### Five Identity Questions

**Q1: What IS this agent?**
A financial data extractor and measurer that reads receipts, categorises expenses, flags unusual patterns, and prepares structured monthly summaries. It never advises on spending decisions.

**Q2: What is its stance toward possibility?**
Constraint-oriented (P7/P8 stance). It operates within defined categories, measurement rules, and flagging thresholds. It does not suggest what to spend or save.

**Q3: What would VIOLATE its identity?**
- Advising on spending decisions ("you should cut this expense")
- Fabricating receipt data that isn't in the source
- Categorising without confidence (guessing categories silently)
- Suppressing unusual spending flags because they seem "normal"
- Aggregating away the detail that matters (hiding a large purchase in a monthly total)

**Q4: What would make it WRONG?**
Two-axis failure space:
- **Incorrect extraction** (wrong amount, wrong date, wrong vendor) — looks correct but isn't
- **Missing extraction** (failing to capture a receipt) — silence that looks like absence

Worst failure that looks like success: **Consistent-looking but incorrect categorisation** — expenses appear neatly organised and summarised, but categories are wrong or incomplete, and the user trusts the summary without verifying.

**Q5: What's the hardest boundary moment?**
"Ambiguous receipts" — when a receipt could be multiple categories (e.g., a Costco receipt with groceries, electronics, and office supplies). The temptation is to pick the dominant category and assign the whole amount, but this loses the detail that matters for spending analysis.

### 12 Target State Characteristics

1. **Accurate not approximate** — every extracted amount matches the source exactly
2. **Complete not silent** — every receipt is processed; null state is "no receipts found in this period" not silence
3. **Categorised with confidence** — every category assignment carries confidence; low-confidence assignments are flagged for human review
4. **Flagged not hidden** — unusual patterns are surfaced, not averaged away
5. **Typed not flat** — expenses are typed objects (amount, vendor, date, category, confidence, source) not rows in a spreadsheet
6. **Epistemically honest** — "I'm 60% confident this is office supplies" is better than silently assigning "Office Supplies"
7. **Decision-preparatory** — summaries prepare the human for spending decisions; they don't make the decisions
8. **Aged appropriately** — old receipts are flagged as stale; category rules from 6 months ago may not apply today
9. **Connected not isolated** — expenses are connected to vendors, categories, time periods, and unusual patterns, not siloed entries
10. **Provable not trustable** — every extracted value traces to a source receipt; every category assignment traces to a rule or human confirmation
11. **Minimal context sufficient** — summaries present what the human needs, not everything the agent knows
12. **Privacy-respecting** — financial data is sensitive; the agent treats it with appropriate access controls

---

## P1: Output Specification

### 8 Output Groups, 15 Outputs

**O1: Extracted Receipt Data** (per receipt)
- source: original receipt (image/document reference)
- vendor: extracted vendor name
- date: extracted transaction date
- amount: extracted total amount
- line_items: extracted individual items (if available)
- category: assigned category with confidence score
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}
- artefact_tags: [surprise | gap | pattern | assessment_fragment]

**O2: Category Assignment** (per expense)
- category: assigned category
- confidence: assignment confidence (High/Medium/Low)
- alternative_categories: other possible categories with confidence
- rule_or_human: whether this was assigned by rule or confirmed by human
- reasoning: brief explanation of why this category
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

**O3: Unusual Spending Flags** (per flag)
- flag_type: unusual_vendor | unusual_amount | unusual_frequency | unusual_category | unusual_combination
- description: what's unusual
- severity: Low/Medium/High
- evidence: supporting data
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

**O4: Monthly Summary** (per month)
- total_spending: by category and total
- comparison: vs previous month, vs 3-month average
- flags_summary: count and severity of unusual flags
- category_breakdown: spending by category with confidence-weighted totals
- trend_notes: observed patterns (not advice)
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

**O5: Vendor Registry** (cumulative)
- vendor: normalised vendor name
- category: typical category for this vendor
- frequency: how often this vendor appears
- typical_amount: average and range
- first_seen: date of first appearance
- last_seen: date of most recent appearance
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

**O6: Category Rules** (cumulative)
- rule: categorisation rule (e.g., "vendor contains 'uber' → Transport")
- confidence: rule confidence
- human_confirmed: whether a human confirmed this rule
- exception_count: how many times this rule was overridden
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

**O7: Confidence & Gaps Statement** (per month)
- high_confidence_percentage: % of expenses categorised with High confidence
- medium_confidence_percentage: % with Medium
- low_confidence_percentage: % with Low (flagged for human review)
- unprocessed_receipts: count of receipts that couldn't be processed
- gaps: what the agent doesn't know (e.g., "12% of expenses are in categories with <70% confidence")
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

**O8: Processing Report** (per run)
- receipts_processed: count
- receipts_failed: count with reasons
- categories_auto_assigned: count with confidence breakdown
- categories_human_confirmed: count
- flags_raised: count with severity breakdown
- processing_time: total
- epistemic: {confidence, provenance, assumptions, limitations, recency, uncertainty}

### Dependencies

O1 → O2 (category assignment depends on extracted data)
O1 → O3 (flags depend on extracted data)
O1 → O5 (vendor registry built from extracted data)
O2 → O4 (summary includes categorised expenses)
O2 → O6 (category rules built from assignments)
O3 → O4 (summary includes flags)
O5 → O2 (vendor history informs category assignment)
O6 → O2 (rules inform category assignment)
O7 depends on O2 and O3 (confidence statement built from assignments and flags)
O8 depends on all processing

---

## P2: Backcasting

### Input Requirements (traced backward from O8)

| ID | Requirement | Source | Criticality | Satisfied By |
|---|---|---|---|---|
| IR-001 | Receipt images/documents | External | Critical | User upload |
| IR-002 | Category rules (initial set) | Human | Critical | Human configuration |
| IR-003 | Spending thresholds for flags | Human | High | Human configuration |
| IR-004 | Vendor category history | Internal (O5) | Medium | Previous runs |
| IR-005 | Category assignment history | Internal (O6) | Medium | Previous runs |
| IR-006 | Previous monthly summaries | Internal (O4) | Medium | Previous runs |
| IR-007 | OCR/text extraction capability | System | Critical | System tool |
| IR-008 | Date/time reference | System | High | System clock |

---

## P3: Task Decomposition

| Task | Cognitive Type | Description |
|---|---|---|
| T1 | Mechanical | Receive and validate receipt upload |
| T2 | Mechanical | Extract text from receipt image/PDF (OCR) |
| T3 | Extractor | Extract structured data from receipt text (vendor, date, amount, items) |
| T4 | Measurer | Measure extraction confidence (how certain is the extraction?) |
| T5 | Measurer | Match vendor against vendor registry |
| T6 | Assessor | Assign category with confidence score |
| T7 | Assessor | Flag unusual spending patterns |
| T8 | Aggregator | Compile monthly summary |
| T9 | Measurer | Calculate confidence statistics across all expenses |
| T10 | Aggregator | Compile processing report |
| T11 | Human-primary | Confirm low-confidence category assignments |
| T12 | Human-primary | Review unusual spending flags |
| T13 | Human-primary | Define initial category rules |
| T14 | System | Store receipt data in knowledge base |
| T15 | System | Update vendor registry with new vendors |

### Failure Modes per Task

| Task | Failure Mode | Authority Boundary |
|---|---|---|
| T3 | Incorrect extraction (wrong amount, date, vendor) | NEVER fabricate data; flag low-confidence extractions |
| T4 | Overstating extraction confidence | NEVER claim high confidence for uncertain extractions |
| T6 | Assigning category without confidence | NEVER assign category silently if confidence <70%; flag for human review |
| T7 | Suppressing unusual flags | NEVER average away unusual spending; surface it |
| T8 | Hiding detail in aggregation | NEVER aggregate away the detail that matters for spending decisions |
| T9 | Misrepresenting confidence statistics | NEVER present Medium/Low confidence assignments as High |
| T11 | Not reviewing low-confidence assignments | Human MUST review; agent cannot auto-confirm |

---

## P4: Capability Allocation

| Task | Allocation | Gap | Rationale |
|---|---|---|---|
| T1 | System | 0 | Mechanical validation |
| T2 | System | 0 | OCR is system capability |
| T3 | Agent (Extractor) | 2 | Extraction with confidence scoring |
| T4 | Agent (Measurer) | 1 | Confidence measurement |
| T5 | Agent (Measurer) | 1 | Vendor matching against registry |
| T6 | Agent (Assessor) | 3 | Category assignment with confidence; flag for human review if Low |
| T7 | Agent (Assessor) | 4 | Unusual pattern detection; flag for human review |
| T8 | Agent (Aggregator) | 2 | Summary compilation (never adds insight) |
| T9 | Agent (Measurer) | 1 | Confidence statistics calculation |
| T10 | Agent (Aggregator) | 1 | Processing report compilation |
| T11 | **Human-primary** | **7** | Low-confidence category confirmation requires human judgment |
| T12 | **Human-primary** | **6** | Unusual spending review requires human judgment about personal priorities |
| T13 | **Human-primary** | **8** | Initial category rules require human judgment about spending priorities |
| T14 | System | 0 | Data storage |
| T15 | System | 0 | Registry update |

**Key allocation insight**: Three human-primary tasks — confirming low-confidence categories (T11), reviewing unusual flags (T12), and defining initial category rules (T13). The agent prepares all three; the human decides. T13 (initial category rules) has the highest complementarity gap (8) because it's pure human judgment about spending priorities and categories that the agent cannot determine.

---

## P5: Event Storming

### Domain Events
- Receipt uploaded
- Receipt processed
- Category assigned
- Low-confidence category flagged
- Unusual spending detected
- Monthly summary generated
- Category rule created/updated
- Human confirmed category
- Human reviewed flag

### Failure Events
| ID | Failure | Recovery |
|---|---|---|
| F1 | Receipt image unreadable | Flag as unprocessed, store original, request re-upload |
| F2 | OCR extraction failed | Flag as unprocessed, store original, request re-upload |
| F3 | Vendor not in registry | Create new vendor entry, assign confidence=Low, flag for human review |
| F4 | Category assignment confidence <70% | Flag for human review, offer top 3 alternatives |
| F5 | Multiple categories possible for one receipt | Present alternatives with confidence scores to human |
| F6 | Flagging normal spending as unusual | Human can dismiss flag; dismissal updates threshold |
| F7 | Missing unusual spending | Human can add flag; addition updates pattern recognition |
| F8 | No receipts in period | Null state output: "No receipts found in this period" |

---

## P6: System Architecture

### Composition: Single Agent with Per-Operation Class Boundaries

This is a single agent with different authority boundaries per operation type:
- **Extraction operations** (T3): Extractor — never judges
- **Measurement operations** (T4, T5, T9): Measurer — never interprets
- **Assessment operations** (T6, T7): Assessor — never finalises
- **Aggregation operations** (T8, T10): Aggregator — never adds insight

### Progressive Autonomy (Per-Dimension)

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Extraction | Human reviews every receipt | Human reviews flagged receipts | Human reviews Low-confidence only | Human reviews random sample (10%) |
| Categorisation | Human assigns every category | Agent suggests, human confirms all | Agent assigns High/Medium, human reviews Low | Agent assigns, human reviews Low + random sample |
| Flagging | Human checks all spending | Agent flags, human reviews all | Agent flags, human reviews High/Medium | Agent flags, human reviews High only |
| Summarisation | Human compiles own summary | Agent drafts, human reviews | Agent compiles, human reviews summary | Agent compiles, human scans summary |

**Key insight**: Categorisation and flagging should progress more slowly than extraction and summarisation. Categorisation errors are the worst failure that looks like success (wrong category, trusted without verification).

### Cost Budget
- Per-receipt processing: 1-3K tokens (extraction + categorisation + flagging)
- Monthly summary: 5-10K tokens (aggregation + statistics)
- Total monthly estimate: 50-300K tokens for 50-100 receipts

---

## P7: Agent Design

### Five Identity Questions (Recap)
Q1: Financial data extractor and measurer — reads receipts, categorises expenses, flags unusual patterns, prepares summaries. Never advises on spending.
Q2: Constraint-oriented — operates within defined categories, measurement rules, flagging thresholds.
Q3: Would violate identity by: advising on spending, fabricating receipt data, categorising without confidence, suppressing unusual flags, aggregating away important detail.
Q4: Two-axis failure: incorrect extraction (looks correct but isn't) vs missing extraction (silence). Worst failure that looks like success: consistent-looking but incorrect categorisation.
Q5: Hardest boundary moment: ambiguous receipts where a single receipt spans multiple categories.

### Class: Multi-class per operation (Extractor/Measurer/Assessor/Aggregator)
### Orientation: Constraint-oriented

### Harm Assessment
**Indirect data harm** — incorrect expense data could lead to wrong spending decisions if trusted without verification. Not direct output harm (the agent doesn't produce spending advice), but data integrity harm (wrong categories could mislead financial decisions).

**SuggestionRisk**: LOW for extraction (pure data), MEDIUM for categorisation (could miscategorise), MEDIUM for flagging (could miss unusual patterns), LOW for summarisation (compilation only).

### Null-State Outputs
- "No receipts found in this period" (Extractor)
- "Insufficient data for pattern comparison" (Measurer)
- "Unable to assess — fewer than 3 data points" (Assessor)
- "No unusual patterns detected in this period" (Assessor)
- "Nothing to summarise — no expenses recorded" (Aggregator)

### Epistemic Metadata Profile
- **Confidence**: Spectral (High/Medium/Low per extraction and categorisation)
- **Provenance**: Always specified (which receipt, which OCR pass, which rule)
- **Assumptions**: Category assignments based on vendor name patterns
- **Limitations**: OCR accuracy, receipt quality, handwritten receipts
- **Recency**: Timestamped; receipts >30 days flagged as potentially stale for real-time analysis
- **Uncertainty**: Explicitly stated for ambiguous receipts

### Hardest Boundary Moment Enforcement
**Ambiguous receipts** (one receipt, multiple categories):
- **Declare** (Regime 1): "This receipt contains items from multiple categories."
- **Detect** (Regime 2): Flag receipts with >1 category possibility as "multi-category" with confidence per category.
- **Prevent** (Regime 3): Structured output schema requires line-item categorisation when possible, not whole-receipt categorisation. If line items aren't available, the receipt is flagged for human review with alternatives presented.

---

## P8: Contract Formalization

### 10 Contract Primitives

1. **Contract**: This agent processes receipts into typed expense data with categorisation and flagging. Payment (trust) occurs when the human confirms the monthly summary.

2. **Principal**: The human who owns the financial data and makes spending decisions.

3. **Schema**: Structured expense objects (O1-O8) with typed fields, confidence scores, and epistemic metadata. Non-compliant output → REVERT.

4. **Guard**: 
   - NEVER advise on spending decisions
   - NEVER fabricate receipt data
   - NEVER categorise without confidence score
   - NEVER suppress unusual flags
   - NEVER aggregate away important detail
   - ALWAYS produce null-state output when no data
   - ALWAYS flag low-confidence assignments for human review
   Violation → REVERT

5. **Budget**: Per-receipt: 1-3K tokens. Monthly summary: 5-10K tokens. Total monthly: ≤500K tokens. Exhausted → HALT processing, flag remaining receipts for next run.

6. **Invocation**: Triggered by receipt upload (per-receipt processing) or scheduled (monthly summary generation).

7. **Revert**: Output rejected → human receives rejection with reason, original receipt preserved, no data written to knowledge base until corrected.

8. **Event**: receipt_processed, category_assigned, low_confidence_flagged, unusual_spending_detected, monthly_summary_generated, category_rule_updated, human_confirmed_category, human_reviewed_flag, processing_complete, processing_failed.

9. **Identity**: Financial data extractor and measurer. Constraint-oriented. Operates within defined categories and rules.

10. **Knowledge**: Vendor registry, category rules, spending thresholds, previous monthly summaries, human confirmation history.

### Enforcement Regime Summary
- **Prevent (Regime 3)**: Schema validation on outputs (structured expense objects), Guard enforcement (never-rules in system prompt + output schema), Budget enforcement (token limits), null-state output (always produce "no data" rather than silence), line-item categorisation for multi-category receipts.
- **Detect (Regime 2)**: Low-confidence category assignments flagged for human review, unusual spending flags presented to human, processing report shows confidence breakdown.
- **Declare (Regime 1)**: Identity boundaries (never advise, never fabricate, never suppress) stated in system prompt, human review of initial category rules.

### Unenforceable Elements
1. **"Never aggregate away important detail"** (Regime 2 — detectable via output audit comparing summary detail to source data, but not preventable structurally)
2. **"Never suppress unusual flags"** (Regime 2 — detectable via comparison to statistical thresholds, but an agent could theoretically downplay a flag)
3. **Epistemic honesty in confidence scores** (Regime 1 — the agent states confidence; verifying that stated confidence matches actual confidence requires calibration over time)

---

## P9: Human Experience Design

### Cognitive Load Budget
- **Per-receipt review** (advisory stage): 2-3 decisions per receipt (confirm category, confirm amount, flag review) → 5-10 min per 10 receipts
- **Monthly summary review** (supervised stage): 3-5 decisions per month (review summary, confirm flags, adjust categories) → 15-20 min
- **Maximum per session**: 30 min (beyond this, decision quality degrades)

### Interface Specification
- **Receipt processing**: Each receipt shown with extracted data, category suggestion, and confidence. Human confirms or corrects.
- **Flag review**: Unusual spending flags shown with evidence and severity. Human dismisses or acknowledges.
- **Monthly summary**: Category breakdown with confidence-weighted totals. Trend notes. Flags summary.
- **Confidence legend**: 🟢 High (≥80%), 🟡 Medium (60-79%), 🔴 Low (<60%) — same as Boundary Map confidence legend

### Override Mechanisms
1. **Category override**: Human can reassign any category
2. **Flag dismissal**: Human can dismiss any flag
3. **Rule addition**: Human can add new category rules
4. **Threshold adjustment**: Human can change unusual spending thresholds
5. **Manual receipt entry**: Human can add receipts that failed OCR

### System Empowerment Assessment
- **Shadow**: Constraining — human reviews everything, agent learns patterns
- **Advisory**: Informing — agent suggests, human confirms all
- **Supervised**: Enabling — agent processes most receipts, human reviews low-confidence and flags
- **Target: Amplifying** — agent processes reliably, human reviews summaries and makes financial decisions

---

## P10: Validation & Iteration

### Testable Hypotheses
- **H1**: Typed expense objects with confidence scores are more useful than flat spreadsheet rows (measured by time-to-decision and error-detection rate)
- **H2**: Epistemic metadata on categorisation improves trust (measured by override rate decreasing over time)
- **H3**: Unusual spending flags catch patterns the human would miss (measured by flag accuracy and human confirmation rate)
- **H4**: Multi-category receipt handling improves categorisation accuracy (measured by comparison to single-category assignment)
- **H5**: Null-state output prevents false confidence (measured by user trust in "no receipts found" vs silence)
- **H6**: Progressive autonomy reduces human review time while maintaining accuracy (measured by review time vs error rate at each autonomy level)

### Specification Aging Schedule
| Component | Cadence | Trigger |
|---|---|---|
| Category rules | 3 months | New category request, >20% override rate |
| Vendor registry | 6 months | New vendor, vendor name change |
| Spending thresholds | 3 months | Significant income/expense change |
| OCR accuracy | 6 months | New receipt format, extraction errors |
| Flag thresholds | 3 months | Too many false positives, missed unusual patterns |

### Progressive Autonomy Schedule
| Level | Timeline | Criteria for Promotion |
|---|---|---|
| Shadow | Week 1-2 | Human reviews all outputs |
| Advisory | Week 3-6 | Extraction accuracy ≥95%, categorisation accuracy ≥85%, 0 fabrication events |
| Supervised | Week 7-12 | Categorisation accuracy ≥90%, flag accuracy ≥80%, human override rate <20% |
| Autonomous | Month 4+ | Categorisation accuracy ≥95%, flag accuracy ≥90%, human override rate <10% for 2 consecutive months |

---

## Key Insights for CAWDP

### 8 New Insights

**1. Multi-Category Receipts as a Boundary Stress Test**
Ambiguous receipts (one receipt spanning multiple categories) are the hardest boundary moment for this agent type. The correct response is line-item categorisation where possible, or explicit flagging with alternatives where not. This is a genuinely different boundary stress test from previous agents — it's not about judging the content but about refusing to force a single category on multi-category data. This maps to the **"never aggregate away important detail"** principle, which is the Aggregator failure mode (omission) applied at the extraction level.

**2. Categorisation as the Worst Failure That Looks Like Success**
Incorrect categorisation that appears consistent and well-organised is more dangerous than obvious extraction errors. The human sees neat categories and trusts the summary, but the underlying assignments are wrong. This is a new instance of the "worst failure that looks like success" pattern, but different from previous instances:
- Watchman: silence that looks like no signal
- Prospector: valid-but-obvious that feels like success
- Tutor: dependency that looks like learning
- **This agent: consistent categorisation that masks incorrect assignments**

This suggests a new pattern: **the more organised the output appears, the more dangerous incorrect assignments become** because organisation masks inaccuracy. High confidence in low-quality categorisation is more dangerous than low confidence in high-quality extraction.

**3. Per-Operation Class Boundaries in a Single Agent**
This agent uses different authority boundaries for different operations (Extractor for reading, Measurer for counting, Assessor for categorising, Aggregator for compiling), all within a single agent. This is the same pattern as the Code Reviewer (three-mode operation) but applied to a simpler agent. The key insight: **operation-level boundaries are more granular than agent-level boundaries**. The agent itself doesn't have a single class — it has a class per operation. This is important for implementation because the system prompt needs to enforce different "never" rules for different operations within the same agent.

**4. Epistemic Honesty as a Trust Accelerator**
This agent explicitly states confidence on every category assignment. Low-confidence assignments are flagged for human review rather than silently assigned. This operationalises **CC-3 (Epistemic Metadata Contracts)** at the most granular level — not just at the output level, but at the individual assignment level. The insight: **epistemic honesty at the assignment level accelerates trust more than accuracy at the summary level**. A human who sees "60% confident this is office supplies" can make an informed decision; a human who sees "Office Supplies" with no confidence marker cannot. This is the "what I don't know is more valuable than what I do" principle (from Competitive Intelligence analysis) applied to personal finance.

**5. Progressive Autonomy Varies by Operation Type**
Extraction and summarisation can progress to autonomous faster than categorisation and flagging, because the cost of extraction errors is lower than the cost of categorisation errors. This extends the per-dimension progressive autonomy insight from the Code Reviewer: **different operations within the same agent have different trust trajectories**. Extraction can be autonomous at month 2, categorisation at month 3, flagging at month 4. This maps directly to the Code Reviewer's per-dimension autonomy (style autonomous early, security never autonomous).

**6. The Null State Is a Financial Report**
"No receipts found in this period" is not an error — it's a valid financial report that may indicate no spending (which the user should confirm) or a processing failure (which the system should flag). This is the **"silence ≠ absence"** principle applied to financial data. A null state in financial tracking has different implications than a null state in monitoring — the user needs to know whether it's truly zero spending or a processing gap.

**7. Category Rules as Living Specifications**
Category rules (e.g., "vendor contains 'uber' → Transport") are specifications that age. A rule from 6 months ago may not apply if the vendor changed categories (e.g., Uber Eats could be Food, not Transport). This is **CC-5 (Specification Aging)** applied to categorisation rules. The insight: **rules that were correct when created can become incorrect without any change to the rule itself** — the environment changed, not the rule. This is a new instance of specification aging where the specification is still technically valid but no longer produces correct output because the environment shifted.

**8. Financial Data as Sensitive but Not High-Stakes**
Financial data is sensitive (privacy concerns) but the stakes are relatively low (no one dies from a miscategorised expense). This creates an interesting complementarity profile: the human doesn't need to review every receipt (low stakes per receipt), but the human does need to review unusual patterns (moderate stakes for financial decisions). The complementarity gap varies by operation: extraction has a low gap (the agent can do this well), categorisation has a moderate gap (the agent can suggest, the human confirms), and unusual pattern review has a high gap (the agent can flag, but the human decides if it's truly unusual in context). This maps to **per-operation complementarity allocation** rather than per-agent allocation.

---

## Comparative Summary with Previous Exercises

| Aspect | Watchman | Analyser | Sentinel | Prospector | Tutor | Code Reviewer | **Expense Tracker** |
|---|---|---|---|---|---|---|---|
| Class | Extractor | Multi-class | Measurer+Assessor | Generator+Assessor | Assessor+Generator | Assessor+Gen+Self-eval | **Multi-class per operation** |
| Stakes | Low | Moderate | High | Discovery | Inverted | High (agent-caused) | **Low-Moderate** |
| Key failure | Silence | Per-field overstepping | Sensor vs real spike | Valid-but-obvious | Dependency trap | Accepted wrong suggestion | **Consistent wrong categorisation** |
| Novel insight | Silence≠absence | Per-field boundaries | Stakes→architecture | Two-axis validity×novelty | Inverted autonomy | Agent-caused harm | **Organisation masks inaccuracy** |
| Null state | No signal found | N/A | No readings | No novel insights | No questions asked | No issues found | **No receipts found in period** |
| Progressive autonomy | Fast (one timeline) | Slower (multi-class) | Split by output type | Novelty never autonomous | Inverted (decreasing) | Per-dimension | **Per-operation** |
| CC-3 application | Provenance of source | Per-field confidence | Per-reading confidence | Provenance + novelty | Dependency markers | Risk assessment | **Per-assignment confidence** |
| CC-5 application | 7-day cadence | 14-day | Real-time | Daily | Scaffold reduction | Per-dimension | **3-month rule aging** |

The **Expense Tracker** occupies a unique position: low stakes but high trust sensitivity (financial data is personal), multi-class per operation (like Code Reviewer), but with a novel failure mode where organisational neatness masks inaccuracy. The per-operation progressive autonomy and per-assignment epistemic honesty are the key design contributions.

---
