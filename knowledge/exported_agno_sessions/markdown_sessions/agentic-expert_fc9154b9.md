# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `fc9154b9...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-06T10:18:48 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-06T10:18:48* · `glm-5.1:cloud` · `76dfc53e...`

### Prompt

How might we design a team or workflow of agents to manage (non-software) projects in a business. These projects might be an internal strategic initiative, for example, a small business owner wants to productize a range of existing services for a new market segment. There would be a number of tasks with a dependency graph. 

It would be good to have an agent to assist the user in defining and scoping the project and complete the project initiation template/contract. Once the user approves the project brief, the project is added to the database table, and another agent decomposes the project into phases and tasks as per their respective templates/contracts. These phases and tasks are defined, assigned, time estimated, prioritized etc. and added to the tasks table.

### Response

# Project Management Agent Team Design

Let me design this through a CAWDP lens, connecting to the existing Project Manager agent (the structural registry) and the broader system.

## The Core Problem

A business owner (let's say Sarah Chen) wants to productize existing services for a new market segment. She doesn't need software project management — she needs someone to help her **think through the project clearly**, then **structure it into executable work**, and finally **track it as it unfolds**.

The key insight from CAWDP: the project management itself has three genuinely different cognitive phases that need different agent classes:

| Phase | What happens | Dominant cognitive mode | Agent class |
|-------|-------------|----------------------|-------------|
| **Define** | "What are we doing and why?" | Possibility → boundary | Assessor (possibility-oriented) |
| **Decompose** | "Break it into phases and tasks" | Generative + structural | Generator (bridge-oriented) |
| **Calibrate** | "How long? What depends on what? Who does what?" | Measuring + evaluating | Measurer + Assessor (constraint-oriented) |

These are different enough to need different authority boundaries — and that's the signal for a multi-agent workflow, not a single agent.

---

## Agent Roster

### 1. Project Initiator (Assessor, possibility-oriented)

**What IS it?** A thinking partner that helps the owner articulate what they actually want — not what they think they should say.

**What would VIOLATE its identity?** Deciding the project scope for the owner, or filling in gaps with its own assumptions.

**What would make it WRONG?** Producing a project brief that captures the template's structure without the owner's genuine judgment — looks complete but isn't.

**Authority boundaries:**
- **Never** finalizes scope — the owner decides
- **Never** invents requirements — only reflects and structures what the owner says
- **Never** approves the brief — that's the human gate
- **Does** surface gaps, contradictions, and unstated assumptions
- **Does** draft the brief from captured information
- **Does** flag when the owner's stated goal doesn't match their described scope

**How it works:** One question at a time. Plain English. Starts with purpose ("What does success look like?"), then scope ("What's in? What's out?"), then constraints (budget, timeline, regulatory), then risks and stakeholders. Uses the Decision Presentation Pattern — presents 2-3 structured options when the owner is unsure, never an open question.

**Key outputs:** Project Initiation Contract (see below)

---

### 2. Task Architect (Generator, bridge-oriented)

**What IS it?** A decomposition engine that takes an approved project brief and structures it into phases, tasks, and dependencies.

**What would VIOLATE its identity?** Estimating its own tasks (optimism bias), or assigning work without complementarity analysis.

**What would make it WRONG?** Creating a task structure that looks thorough but misses a critical dependency — plausible completeness that isn't.

**Authority boundaries:**
- **Never** estimates time or effort — that's the Calibrator's job (CC-1 verification independence)
- **Never** assigns tasks to specific people or agents — proposes, human decides
- **Never** creates tasks outside the project scope — every task traces to the brief
- **Does** identify phases based on project type templates
- **Does** decompose each phase into concrete tasks
- **Does** identify dependencies between tasks (what blocks what)
- **Does** flag where it's uncertain about decomposition choices

**Key insight:** The Generator that creates the task structure should NOT be the one estimating how long those tasks take. That's the same class collision that makes developers bad at estimating their own code. The architect builds the structure; a separate calibrator measures it.

---

### 3. Task Calibrator (Measurer + Assessor, constraint-oriented)

**What IS it?** An analysis agent that reviews the Task Architect's work and adds measurement: estimates, priority assessment, complementarity allocation, and risk scoring.

**What would VIOLATE its identity?** Changing the task structure (that's the Architect's work), or giving a single confident estimate without confidence ranges.

**What would make it WRONG?** "3 weeks" with no confidence level — looks precise but isn't. A confident estimate on a task with high uncertainty is worse than an honest wide range.

**Authority boundaries:**
- **Never** changes the task structure — can only flag and recommend
- **Never** gives a single-point estimate — always a range with confidence level
- **Never** finalizes assignments — proposes complementarity allocation, human decides
- **Does** estimate effort (range + confidence + reasoning)
- **Does** assess priority (impact × urgency × dependency weight)
- **Does** propose who should do each task (human / agent / system) using complementarity analysis
- **Does** identify risks and critical path items
- **Does** flag tasks where estimation confidence is LOW

**The separation matters:** When the same agent that creates tasks also estimates them, you get optimism compression — every task feels "about 2 weeks" because the generator wants its structure to look feasible. The Calibrator has no investment in the structure, so it measures honestly.

---

### 4. Project Manager (Aggregator, constraint-oriented)

This is the existing Project Manager agent — the structural registry. It doesn't think about the project; it manages the data.

**Role in this workflow:** Receives approved project decomposition and writes it to the database. Tracks status going forward. Other agents query it for project state.

**Authority boundaries (unchanged):**
- **Never** adds content or interprets task status
- **Never** allows other agents to write to its private schema directly
- **Does** CRUD operations for projects, phases, tasks, subtasks
- **Does** enforce dependencies (can't start task if dependency incomplete)
- **Does** track status changes with audit trail

---

## Workflow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    HUMAN GATE 1                             │
│            "Does this brief capture what you want?"          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐                                           │
│  │    USER      │                                           │
│  │  + Initiator │──── Project Initiation Contract ──────┐   │
│  └──────────────┘                                      │   │
│                                                        ▼   │
│  ┌──────────────┐                                  ┌─────┐ │
│  │ Task         │─── Phase/Task Structure ────────► │GATE │ │
│  │ Architect    │                                  │  2  │ │
│  └──────────────┘                                  └──┬──┘ │
│                                                       │    │
│  ┌──────────────┐                                     │    │
│  │ Task         │◄── Un-calibrated decomposition ───┘    │
│  │ Calibrator   │                                        │
│  └──────┬───────┘                                        │
│         │                                                │
│         ▼                                                │
│  ┌──────────────┐                                  ┌─────┐ │
│  │ Calibrated   │─── Estimates, priorities, ──────► │GATE │ │
│  │ Decomposition │    assignments, risks            │  3  │ │
│  └──────────────┘                                  └──┬──┘ │
│                                                       │    │
│  ┌──────────────┐                                     │    │
│  │ Project      │◄── Approved decomposition ─────────┘    │
│  │ Manager      │                                        │
│  └──────────────┘─── Database populated ──────────────────┤
│                                                          │
└──────────────────────────────────────────────────────────┘

GATE 1: Owner approves Project Brief
GATE 2: (internal) Calibrator reviews Architect's work  
GATE 3: Owner approves decomposition, estimates, assignments
```

**Agno implementation:** This is a **Workflow** — sequential steps with human gates, not a Team. The steps are:

```
Step 1: Initiator (session with user) → produces Project Initiation Contract
Step 2: Human Gate 1 — user approves/revise brief
Step 3: Task Architect (reads approved brief) → produces task structure
Step 4: Task Calibrator (reviews task structure) → produces calibrated decomposition
Step 5: Human Gate 3 — user approves/revise decomposition
Step 6: Project Manager (writes to database) → project is live
```

Gate 2 is **internal** — the Calibrator automatically reviews the Architect's work. This is CC-1 Verification Independence built into the workflow: the measurer is always different from the creator.

---

## Contract Structures

### Project Initiation Contract

This is what the Initiator produces and the owner approves:

| Field | What it captures | Example |
|-------|------------------|---------|
| **Identity** | What IS this project? | "Productize commercial contract services for franchise market" |
| **Purpose** | Why does this project exist? | "New revenue stream from an underserved market" |
| **Scope In** | What's included | "Service packaging, pricing model, go-to-market plan, first 5 clients" |
| **Scope Out** | What's explicitly NOT included | "Technology platform, new service development, hiring" |
| **Constraints** | Hard limits | "Budget $50K, timeline 6 months, must not disrupt current clients" |
| **Success criteria** | How we know it worked | "3 franchise clients signed, packaged offering live, pricing validated" |
| **Stakeholders** | Who's affected | "Sarah (principal), associates (delivery), existing clients (priority)" |
| **Risks** | What could go wrong | "Scope creep into tech, franchise market smaller than expected" |
| **Authority** | Who can approve what | "Sarah approves scope changes and budget; associates approve workload" |
| **Budget** | Cost allocation | "$50K total: $20K marketing, $15K legal review, $15K operations" |
| **State machine** | Status transitions | Draft → Approved → Active → On Hold → Complete → Closed |

### Task Contract (per task)

| Field | What it captures | Example |
|-------|------------------|---------|
| **Task identity** | What IS this task? | "Draft service packaging structure for franchise market" |
| **Phase** | Which phase this belongs to | "Phase 1: Market Understanding" |
| **Dependencies** | What must finish first | "Task 1.1 (Market analysis) → this task" |
| **Assignment** | Who does it | "Human: Sarah (judgment) + Agent: research support" |
| **Authority boundary** | What the assignee CAN decide | "Sarah decides package structure; agent researches market norms" |
| **Never-rules** | What the assignee NEVER does | "Agent never recommends pricing — that's Sarah's judgment" |
| **Effort estimate** | Range + confidence | "8-15 hours, confidence: MEDIUM (similar work done before)" |
| **Priority** | Impact × urgency × dependency | "HIGH — blocks 4 downstream tasks" |
| **Success criteria** | How we know this task is done | "3 packaging options documented with pros/cons" |
| **State machine** | Status transitions | "Not Started → In Progress → Review → Complete → Blocked" |
| **Epistemic metadata** | Confidence, provenance | "Estimate based on previous packaging project (provenance: Sarah's experience)" |

---

## Decomposition: How the Architect Thinks

The Task Architect doesn't just "break things into tasks." It follows a structured approach:

### Phase Templates (by project type)

For a **"Productize existing services"** project, the Architect would propose phases based on a template:

| Phase | Purpose | Key question |
|-------|---------|-------------|
| **1. Market Understanding** | Who are we serving? | "What does this market need that we already do?" |
| **2. Service Design** | What are we packaging? | "How do existing services map to market needs?" |
| **3. Pricing & Packaging** | How do we price it? | "What's the value to the client and cost to us?" |
| **4. Go-to-Market** | How do we reach them? | "What channels and messaging work?" |
| **5. Pilot & Validate** | Does it work? | "Can we land 3-5 clients and deliver profitably?" |
| **6. Operationalize** | Can we keep doing it? | "What processes, docs, and training do we need?" |

### Task Decomposition Rules

The Architect follows structural rules (not creative freedom):

1. **Every task traces to the brief** — if a task doesn't serve a stated goal or scope item, it doesn't belong
2. **Max 8 tasks per phase** — more than 8 means the phase is too coarse
3. **Every task has a concrete output** — "analyze market" is not a task; "produce market analysis document with 3 segmentation options" is
4. **Dependencies are explicit** — every "can't start until" is captured
5. **Never-rules per task** — what the assigned person/agent should NEVER do (tied to failure mode)

### Dependency Graph

The Architect produces a DAG (directed acyclic graph). For our example:

```
Phase 1: Market Understanding
  T1.1: Market analysis ─────────────────┐
  T1.2: Competitive landscape ───────────┤
  T1.3: Client interviews (if possible) ─┤
                                         ▼
Phase 2: Service Design
  T2.1: Map services to market needs ◄── T1.1, T1.2
  T2.2: Identify packaging options ◄──── T2.1
  T2.3: Draft service descriptions ◄───── T2.2
                                         ▼
Phase 3: Pricing & Packaging
  T3.1: Cost analysis ◄───────────────── T2.1
  T3.2: Pricing model options ◄────────── T3.1, T2.2
  T3.3: Package structure ◄────────────── T3.2
                                         ▼
Phase 4: Go-to-Market
  T4.1: Channel strategy ◄─────────────── T3.3
  T4.2: Marketing materials ◄───────────── T4.1
  T4.3: Outreach plan ◄─────────────────── T4.1
                                         ▼
Phase 5: Pilot & Validate
  T5.1: Pilot client selection ◄────────── T4.3
  T5.2: Deliver pilot engagements ◄─────── T5.1, T2.3
  T5.3: Validate profitability ◄────────── T5.2, T3.1
                                         ▼
Phase 6: Operationalize
  T6.1: Process documentation ◄─────────── T5.3
  T6.2: Training material ◄─────────────── T6.1
  T6.3: Scale plan ◄───────────────────── T6.1, T5.3
```

---

## Calibration: How the Calibrator Thinks

The Calibrator reviews the Architect's work through four lenses:

### 1. Effort Estimation

For each task, the Calibrator produces:

```json
{
  "task_id": "T2.1",
  "estimate_range": "6-12 hours",
  "confidence": "MEDIUM",
  "reasoning": "Requires mapping 8 existing services against 3 market segments. Similar work took 4-8 hours in previous project, but franchise market has less precedent data.",
  "confidence_drivers": {
    "increases_confidence": ["previous packaging experience", "clear service list"],
    "decreases_confidence": ["franchise market novelty", "interview availability unknown"]
  }
}
```

**Hard rule:** No single-point estimates. Every estimate is a range with a confidence level and reasoning. If confidence is LOW, the Calibrator flags it for the owner's attention.

### 2. Priority Assessment

Priority is computed, not guessed:

**Priority score = Impact (1-5) × Urgency (1-5) × Dependency weight (1-3)**

| Task | Impact | Urgency | Deps blocked | Priority score | Tier |
|------|--------|---------|-------------|----------------|------|
| T1.1 | 5 | 5 | 3+ downstream | 75 | Critical |
| T3.2 | 4 | 3 | 2 downstream | 24 | Standard |
| T6.2 | 3 | 1 | 0 downstream | 3 | Deferred |

### 3. Complementarity Allocation

For each task, the Calibrator proposes who should do it:

| Task | Cognitive type | Proposed assignment | Reasoning |
|------|---------------|--------------------|-----------| 
| T1.1 Market analysis | Analytical + extraction | Agent: Extractor | Structured research, no judgment needed |
| T2.1 Map services to market | Evaluative + intuitive | Human: Sarah | Requires judgment about service-market fit |
| T2.2 Packaging options | Analytical + generative | Collaborative | Agent generates options, Sarah selects |
| T3.2 Pricing model | Intuitive + evaluative | Human: Sarah | Pricing is judgment, not calculation |
| T4.2 Marketing materials | Generative | Collaborative | Agent drafts, Sarah reviews |

**Key rule:** Tasks requiring intuition or evaluation of ambiguous information default to human. The agent prepares; the human decides.

### 4. Risk Flagging

The Calibrator flags:

- **Critical path items** — tasks that, if delayed, push the whole project
- **Low-confidence estimates** — where uncertainty is high
- **Single points of failure** — tasks that depend on one person
- **External dependencies** — things outside the owner's control
- **Scope risk** — tasks that could expand beyond their brief

---

## Database Integration

The Project Manager agent receives the approved decomposition and writes to its private schema:

```sql
-- Project record
INSERT INTO project_manager.projects (name, brief, status, metadata)
VALUES ('Franchise Service Productization', '{...contract JSON...}', 'active', '{...}');

-- Phase records (phases are project-level groupings)
-- Task records with dependencies
INSERT INTO project_manager.tasks (project_id, phase, title, description, 
    status, estimated_hours_min, estimated_hours_max, estimate_confidence,
    priority_score, assigned_to, assignment_type, dependencies, 
    authority_boundary, never_rules, success_criteria, metadata)
VALUES (...);

-- Dependencies as a graph
-- task_dependencies table or JSONB array of blocking task IDs
```

**CC-4 enforcement:** Only the Project Manager can write to this schema. The Initiator, Architect, and Calibrator produce structured output that the Project Manager validates and inserts. They can't bypass the database layer.

---

## Key Design Decisions

### 1. Why a Workflow, not a Team?

This is sequential with human gates — each step depends on the previous step's output. A Team is for parallel collaboration; a Workflow is for sequential pipelines. The human gates require pause/resume, which Agno Workflows support natively through `step_choices`.

### 2. Why separate Architect and Calibrator?

**CC-1 Verification Independence.** The agent that creates the task structure should not be the one that estimates it. When the same agent designs and measures, optimism bias compresses estimates and structural gaps get papered over. The Calibrator has no investment in the structure — it measures what it sees.

### 3. Why does the Initiator use the Decision Presentation Pattern?

The owner doesn't always know what they want. "What's your budget?" is a hard question when you're exploring. The Decision Pattern reframes this: "Here are 3 budget approaches similar projects used — [A] Conservative $30K, [B] Balanced $50K, [C] Aggressive $80K. Each has different trade-offs." The owner can pick, modify, or reject all three. This is "agent prepares judgment, human makes judgment" at the scoping level.

### 4. Why per-task contracts, not just a task list?

A task list says "what to do." A task contract says "what to do, what NOT to do, who decides, what success looks like, and what happens if things go wrong." The contract is the enforcement boundary — it prevents scope creep, assignment confusion, and completion ambiguity. For the Project Manager, the contract IS the data it stores and enforces.

### 5. What about specification aging?

Projects change. The task structure created at project start will be wrong within weeks. The system needs:
- **Specification aging schedule** — each task type has a review cadence (e.g., estimates reviewed every 2 weeks for active tasks)
- **Trigger-based review** — if a task is blocked for >3 days, or an estimate is exceeded by >50%, the Calibrator should be re-invoked
- **Version tracking** — task contracts are versioned, not overwritten (decision archaeology)

---

## Summary

| Agent | Class | Orientation | Does | Never |
|-------|-------|-------------|------|-------|
| **Project Initiator** | Assessor | Possibility | Helps owner articulate project; drafts brief | Finalizes, invents, approves |
| **Task Architect** | Generator | Bridge | Decomposes brief into phases/tasks/dependencies | Estimates, assigns, changes scope |
| **Task Calibrator** | Measurer + Assessor | Constraint | Estimates effort, assesses priority, proposes assignments | Changes structure, gives point estimates, finalizes |
| **Project Manager** | Aggregator | Constraint | Stores in database, tracks status, enforces dependencies | Adds content, interprets, allows bypass |

**Workflow:** Initiator → (Human Gate: Approve Brief) → Architect → Calibrator → (Human Gate: Approve Plan) → Project Manager → Project is live.

The separation that matters most: **the creator and the measurer are always different agents.** That's not just a nice principle — it's the structural defense against the most common project management failure: optimistic plans that everyone believed because the same person who designed them also estimated them.

Want me to go deeper on any specific part — the Agno Workflow implementation, the contract schemas as Pydantic models, the Initiator's conversation flow, or how this connects to the broader Small Business Agentic OS?The response above captures the complete design. Memory has been updated with the key architectural decisions.

One thing I want to flag that might not be obvious: **the Architect ≠ Calibrator separation is the single most important design decision in this workflow.** Every project management tool lets the same person (or agent) design tasks AND estimate them. That's why most project plans are optimistic — the creator wants their structure to look feasible, so estimates compress toward "seems reasonable." The Calibrator has zero investment in the structure, so it measures what it actually sees. That's CC-1 Verification Independence applied to project estimation, and it's the same reason code reviewers should be different from code authors.

Happy to drill into implementation details — Agno Workflow code, Pydantic contract schemas, or how this plugs into the broader Agentic OS.

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-06T22:25:38* · `glm-5.1:cloud` · `b47d542f...`

### Prompt

Here's the refined plan. 

```
# Project Initiation Implementation Plan

Multi-agent HITL workflow converting a raw project idea → persisted Domain→Project→Phase→Task records via 4 Agno steps + 2 human gates. Uses Agno's `HumanReview(requires_output_review=True, on_reject=OnReject.retry)` for both gates — humans can approve, reject-with-feedback (agent retries with `rejection_feedback` injected into context), or call `req.edit(new_output)` for inline modifications.

**Addresses all 6 gaps from the original design overview:**
1. Inter-step data via `StepInput.previous_step_content` (JSON strings, parsed via Pydantic `model_validate_json`)
2. Calibrator rejection retries only the Calibrator step; human can use `req.edit()` for inline structural changes
3. Human revision flow: `on_reject=OnReject.retry` — `rejection_feedback` injected into agent context on next run
4. DB write as a plain `executor=` function calling `TaskToolkit` methods — no redundant agent
5. Output contracts for all 3 new agents registered at startup in the `lifespan` handler
6. Specification aging: explicitly out of scope V1

---

## Workflow Topology

```
Input: "project idea (free text)"
  │
  ▼
Step 1: initiate  [project-initiator agent]
  │  output: ProjectBrief JSON
  ▼
Gate 1: Human output review (approve / reject+feedback / edit)
  │  on_reject=retry → Initiator reruns with rejection_feedback
  ▼
Step 2: architect  [task-architect agent]  ← auto-runs, no gate
  │  output: TaskStructure JSON
  ▼
Step 3: calibrate  [task-calibrator agent]
  │  output: CalibratedPlan JSON
  ▼
Gate 2: Human output review (approve / reject+feedback / edit)
  │  on_reject=retry → Calibrator reruns with rejection_feedback (same Architect output)
  ▼
Step 4: write_to_db  [executor function]
  │  calls TaskToolkit: create_domain → create_project → create_phase × N → create_task × M
  ▼
Output: "Project '{name}' created with N phases and M tasks."
```

---

## Phase 1 — Pydantic Schemas

**Step 1**: Create `contracts/schemas.py` with 5 Pydantic models for cross-agent data passing. These are transport schemas (not ORM), placed in `contracts/` as they define the inter-agent contract surface.

Models:

- `PhaseSpec(name: str, description: str, order_index: int)`
- `TaskSpec(phase_name: str, title: str, description: str, priority: Literal["low","medium","high","urgent"], dependencies: list[str] = [])`
- `ProjectBrief(objective: str, context: str, constraints: list[str], budget_approach: str, timeline: str, success_criteria: list[str])` — Initiator output
- `TaskStructure(project_name: str, domain_name: str, phases: list[PhaseSpec], tasks: list[TaskSpec])` — Architect output
- `CalibratedPlan(task_structure: TaskStructure, effort_notes: str, priority_map: dict[str, str], risk_flags: list[str], calibrator_verdict: Literal["approved", "flagged"])` — Calibrator output

All use `model.model_dump_json()` to serialize to string between steps, and `Model.model_validate_json(step_input.previous_step_content)` to deserialize.

---

## Phase 2 — Agent Definitions *(parallel; depends on Phase 1)*

**Step 2**: Create `agents/project_initiator.py`

- `id="project-initiator"`, `name="Project Initiator"`
- `model=Ollama(id="glm-5.1:cloud")`, `db=get_postgres_db()`
- Pattern: follow `agents/task_agent.py` for imports and instantiation
- Instructions implement the **Decision Presentation Pattern**:
  1. Assess the project idea for feasibility and scope
  2. Present 3 concrete scoping options: conservative / balanced / ambitious
  3. Synthesize a chosen approach into a `ProjectBrief` JSON object
  4. Critical instruction: *"Output ONLY raw JSON matching the ProjectBrief schema — no markdown fences, no preamble."*
  5. Rejection handling: *"If `rejection_feedback` appears in your context, read it carefully and revise your ProjectBrief to address the specific concerns raised."*

**Step 3**: Create `agents/task_architect.py`

- `id="task-architect"`, `name="Task Architect"`
- Same model + db pattern
- Instructions:
  1. Parse the `ProjectBrief` JSON from `previous_step_content`
  2. Decompose into Domain→Project→Phase→Task hierarchy
  3. Every task must have a `phase_name` matching one of the declared phases
  4. Output ONLY raw JSON matching `TaskStructure` schema
  5. Rejection handling instruction (same pattern as Initiator)

**Step 4**: Create `agents/task_calibrator.py`

- `id="task-calibrator"`, `name="Task Calibrator"`
- Same model + db pattern
- Instructions enforce **CC-1 Verification Independence**:
  1. *"You are an independent reviewer. Do NOT defer to the Architect's choices — your role is critical verification."*
  2. Apply 4 constraint checks:
     - (a) No phase contains >10 tasks without sub-phasing
     - (b) All tasks have `priority` explicitly set
     - (c) No circular dependencies (A depends on B which depends on A)
     - (d) Priority distribution is balanced (not all "urgent")
  3. Set `calibrator_verdict="approved"` if all checks pass, `"flagged"` with populated `risk_flags` if any fail
  4. Include effort estimates and priority notes regardless of verdict
  5. Output ONLY raw JSON matching `CalibratedPlan` schema
  6. Rejection handling instruction (same pattern)

---

## Phase 3 — Workflow Definition *(depends on Phase 2)*

**Step 5**: Create `workflows/__init__.py` — empty package marker

**Step 6**: Create `workflows/project_initiation.py`

### DB Write Executor

Function `write_project_to_db(step_input: StepInput) -> StepOutput`:

1. Parse: `plan = CalibratedPlan.model_validate_json(step_input.previous_step_content)`
2. Instantiate: `tk = TaskToolkit()` — each method manages its own `make_session()` internally
3. Create domain: `domain_json = json.loads(tk.create_domain(name=plan.task_structure.domain_name))`
4. Create project: `project_json = json.loads(tk.create_project(domain_id=domain_json["id"], name=plan.task_structure.project_name, description=..., status="active"))`
5. Create phases: for each `PhaseSpec`, call `tk.create_phase(project_id, name, description, order_index)` — build `phase_name → phase_id` mapping dict
6. Create tasks: for each `TaskSpec`, look up `phase_id = phase_map[task.phase_name]`, call `tk.create_task(project_id, phase_id, title, description, priority)`
7. Return: `StepOutput(content=f"Project '{plan.task_structure.project_name}' created: {len(phases)} phases, {len(tasks)} tasks. Project ID: {project_id}")`

### Workflow Definition

```python
from agno.workflow import Workflow, Step, HumanReview, OnReject
from db.session import get_postgres_db
from agents.project_initiator import project_initiator_agent
from agents.task_architect import task_architect_agent
from agents.task_calibrator import task_calibrator_agent

project_initiation_workflow = Workflow(
    id="project-initiation",
    name="Project Initiation",
    description="Convert a project idea into a structured task plan with human review gates.",
    db=get_postgres_db(),
    steps=[
        Step(
            name="initiate",
            agent=project_initiator_agent,
            human_review=HumanReview(
                requires_output_review=True,
                output_review_message=(
                    "Review the Project Brief. "
                    "Approve to proceed to task architecture. "
                    "Reject with feedback to revise. "
                    "Use req.edit() to directly modify the brief."
                ),
                on_reject=OnReject.retry,
                max_retries=3,
            ),
        ),
        Step(
            name="architect",
            agent=task_architect_agent,
            # No gate — runs automatically after Gate 1 approval
        ),
        Step(
            name="calibrate",
            agent=task_calibrator_agent,
            human_review=HumanReview(
                requires_output_review=True,
                output_review_message=(
                    "Review the Calibrated Plan (includes Calibrator verdict, "
                    "effort notes, risk flags). "
                    "Approve to persist to DB. "
                    "Reject with feedback to revise the calibration."
                ),
                on_reject=OnReject.retry,
                max_retries=3,
            ),
        ),
        Step(
            name="write_to_db",
            executor=write_project_to_db,
            description="Persist the approved plan to the task management database.",
        ),
    ],
)
```

---

## Phase 4 — AgentOS Registration *(depends on Phase 3)*

**Step 7**: Modify `app/main.py`:

- Add import: `from workflows.project_initiation import project_initiation_workflow`
- Add to `AgentOS(...)`: `workflows=[project_initiation_workflow]`
- Extend the `lifespan` handler after `create_tables()` to register output contracts:
  ```python
  from contracts import ContractStore
  cs = ContractStore(get_postgres_db())
  for agent_id, fields in [
      ("project-initiator", [("objective","str"), ("timeline","str"), ("constraints","json")]),
      ("task-architect",    [("project_name","str"), ("domain_name","str"), ("phases","json"), ("tasks","json")]),
      ("task-calibrator",   [("task_structure","json"), ("calibrator_verdict","str"), ("risk_flags","json")]),
  ]:
      contract = cs.create_contract(agent_id=agent_id, contract_type="output",
                                    name=f"{agent_id}-output-v1", status="active")
      for field_name, field_type in fields:
          cs.add_field(contract.contract_id, field_name=field_name,
                       field_type=field_type, required=True)
  ```

**Step 8**: Modify `pyproject.toml` — add `"workflows*"` to `[tool.setuptools.packages.find] include`:

```toml
include = ["agents*", "app*", "contracts*", "db*", "tools*", "workflows*"]
```

**Step 9**: Modify `app/config.yaml` — add entry for the workflow with description and an example prompt so it appears in the AgentOS playground.

---

## Relevant Files

| File | Action | Notes |
|------|--------|-------|
| `contracts/schemas.py` | NEW | Pydantic transport schemas; companion to `contracts/models.py` |
| `agents/project_initiator.py` | NEW | Pattern from `agents/task_agent.py` |
| `agents/task_architect.py` | NEW | Same pattern |
| `agents/task_calibrator.py` | NEW | CC-1 independence enforced in instructions |
| `workflows/__init__.py` | NEW | Package marker |
| `workflows/project_initiation.py` | NEW | Workflow + DB write executor |
| `app/main.py` | MOD | Add workflow import, AgentOS registration, contract init in lifespan |
| `pyproject.toml` | MOD | Add `"workflows*"` to packages.find include |
| `app/config.yaml` | MOD | Add workflow entry |
| `tools/task_toolkit.py` | REFERENCE | Each method self-manages `make_session()` and returns JSON strings |
| `db/session.py` | REFERENCE | `get_postgres_db()` for Agno state (agents + workflow) |
| `db/task_session.py` | REFERENCE | `make_session()` used internally by TaskToolkit |
| `contracts/service.py` | REFERENCE | `ContractStore` registration pattern |

---

## Verification

1. **Import check**: `python -c "from workflows.project_initiation import project_initiation_workflow; print('OK')"` — verifies import-time wiring
2. **Schema round-trip**: Instantiate all 5 Pydantic models and call `.model_dump_json()` on each — verifies serialization
3. **Gate 1 pause test**: `project_initiation_workflow.run("Build a recipe management app")` → assert `run_output.is_paused == True` and `len(run_output.steps_requiring_output_review) == 1` with `step_name == "initiate"`
4. **Rejection retry test**: `req.reject(feedback="Make timeline more aggressive")` → `workflow.continue_run(run_output)` → assert pauses again at Gate 1 with revised Initiator output
5. **Full flow test**: Approve Gate 1 → Architect runs automatically → Gate 2 pauses → approve → DB write → `TaskToolkit().list_projects()` shows new project record
6. **Contract registration**: After startup, `ContractStore(get_postgres_db()).get_active_output_contract("project-initiator")` returns non-None
7. **Existing smoke test**: `DB_PORT=5433 .venv/bin/python -m contracts.smoke_test` still passes (no regressions)
8. **Package install**: `pip install -e .` succeeds without import errors for all new packages

---

## Decisions & Constraints

- **Model**: All 3 agents use `Ollama(id="glm-5.1:cloud")` — no OpenAI models
- **DB split**: `get_postgres_db()` for all Agno internal state (agents + workflow HITL session); `make_session()` for TaskToolkit CRUD — separate concerns, never mixed
- **Gate 2 retry scope**: Rejecting Gate 2 retries only the Calibrator against the same Architect output. The human can use `req.edit(new_output)` to directly modify the `CalibratedPlan` for minor fixes. A full Architect re-run on Calibrator rejection is V2.
- **JSON output discipline**: Agent instructions must enforce raw JSON output with no markdown fences. This is the primary prompt engineering risk — test with the actual model.
- **Transaction atomicity**: The DB write step makes one `make_session()` call per `TaskToolkit` method. Partial failure (e.g. phases created but tasks fail) leaves orphaned records. Atomic transactions are V2.
- **Domain deduplication**: `write_project_to_db` always calls `create_domain` — may create duplicates if a same-named domain exists. V2 adds `find_or_create` logic using `TaskToolkit.list_domains()`.
- **Specification aging**: No staleness tracking between Initiator approval and eventual execution. Out of scope V1.

---

## Further Considerations

1. **Gate 2 full redesign path**: If Calibrator rejection consistently requires Architect changes (not just calibration tweaks), V2 should wrap `architect + calibrate` in a `Workflow`-as-a-step nested under the outer workflow, with the HITL gate on the outer step. Note: `Steps` container only supports `requires_confirmation`, not `requires_output_review` — the nested Workflow pattern is the correct approach.

2. **Domain deduplication (V2)**: `write_project_to_db` should call `tk.list_domains()`, parse the JSON, check for a name match, and use the existing `domain_id` rather than creating a duplicate. This is a single added function in the executor.

3. **Workflow ID URL-safety**: `id="project-initiation"` registers the AgentOS route at `/workflows/project-initiation/runs`. Confirm this slug is intentional before clients are built against it.

```

### Response

This is a solid V1 plan. Let me give it a CAWDP-informed review — validating what's working, flagging the one architectural tension, and suggesting specific refinements where they matter most.

---

## ✅ What's Working Well

**CC-1 structurally enforced.** The Architect and Calibrator are separate agents with separate instructions. The Calibrator's instructions explicitly say "Do NOT defer to the Architect's choices." This is Regime 3 enforcement at the workflow level — the architecture makes it structurally impossible for the measurer to be the same entity as the creator. This is the single most important design decision and it's correctly implemented.

**DB write as executor, not agent.** Pure CRUD doesn't need LLM reasoning. Using a plain function for Step 4 is the right call — no hallucination risk on database writes.

**DB split.** `get_postgres_db()` for Agno state, `make_session()` for TaskToolkit CRUD. Never mix concerns. Clean.

**Gate 2 retry scope is correct.** Rejecting Gate 2 retries only the Calibrator. The Architect's output is frozen. If the human wants structural changes, they use `req.edit()` on the CalibratedPlan or reject back to Gate 1. This prevents cascading re-runs.

**Contract registration at startup.** Matches the existing codebase pattern. Good.

**6 gaps addressed.** The plan explicitly addresses all 6 gaps from the original design overview. The mapping is clear.

---

## ⚠️ One Architectural Tension

**The Decision Presentation Pattern doesn't fit a single Workflow step.**

The Initiator's instructions say "Present 3 concrete scoping options." In the design, the Decision Presentation Pattern is a *conversational* interaction — the agent presents options, the human chooses, the agent synthesizes. But in an Agno Workflow, each step runs once. The agent produces output, then the human reviews it. There's no multi-turn conversation within a single step.

This means the Initiator has two choices, and they're different experiences:

**Option A — Present options *within* the brief (V1, fits Workflow)**
The Initiator outputs a `ProjectBrief` that includes 3 scoping approaches as a structured field. The human reads all 3, then uses `req.edit()` to select one or synthesize their own. This works with the current Workflow architecture but changes the Decision Presentation Pattern from "choose one" to "here are three, pick or blend."

```python
class ScopingOption(BaseModel):
    name: str  # "Conservative", "Balanced", "Ambitious"
    approach: str
    budget_range: str
    timeline: str
    risk_level: Literal["low", "medium", "high"]

class ProjectBrief(BaseModel):
    objective: str
    context: str
    constraints: list[str]
    scoping_options: list[ScopingOption]  # 3 options presented
    recommended_option: str  # which one the agent recommends
    budget_approach: str
    timeline: str
    success_criteria: list[str]
```

The human at Gate 1 sees all 3 options and either approves the recommended one, edits to blend elements, or rejects with feedback like "I want the timeline from Option A with the budget from Option C."

**Option B — Pre-Workflow Session for scoping (V2)**
The Initiator runs as a separate Agno *Session* (multi-turn conversation) *before* the Workflow starts. The conversation produces the brief. Then the brief is passed into the Workflow as input. This gives the full Decision Presentation Pattern but requires a Session + Workflow handoff.

**Recommendation:** Use Option A for V1. It fits the Workflow architecture and still gives the human structured choices. The key change is adding `scoping_options` to `ProjectBrief`. V2 can introduce a pre-workflow Session for full conversational scoping.

---

## 🔧 Schema Refinements

Three small changes that make the schemas more CAWDP-aligned:

### 1. Add `never_rules` to `TaskSpec`

The original design had "Never-rules" per task (what the assignee should NEVER do, tied to failure mode). This is missing from the current `TaskSpec`. Add it:

```python
class TaskSpec(BaseModel):
    phase_name: str
    title: str
    description: str
    priority: Literal["low", "medium", "high", "urgent"]
    dependencies: list[str] = []
    never_rules: list[str] = []  # What the assignee should NEVER do
```

This is the authority boundary per task — the structural enforcement that prevents the most common failure modes.

### 2. Add `calibrator_verdict` per task, not just overall

The current `CalibratedPlan` has a single `calibrator_verdict` for the whole plan. But some tasks might be fine while others are flagged. Add per-task verdicts:

```python
class TaskCalibration(BaseModel):
    task_title: str
    effort_range: str  # "6-12 hours"
    confidence: Literal["low", "medium", "high"]
    risk_note: str = ""

class CalibratedPlan(BaseModel):
    task_structure: TaskStructure
    task_calibrations: list[TaskCalibration]  # Per-task estimates
    risk_flags: list[str]
    calibrator_verdict: Literal["approved", "flagged"]
    overall_effort_note: str
```

This gives the human at Gate 2 per-task visibility, not just an overall verdict.

### 3. Add `assignment_type` to `TaskSpec`

The original design had complementarity allocation per task (human/agent/system/collaborative). Add it:

```python
class TaskSpec(BaseModel):
    ...
    assignment_type: Literal["human", "agent", "system", "collaborative"] = "human"
    assignment_rationale: str = ""
```

The Calibrator fills this in during calibration. Default to "human" because the principle is: when in doubt, human decides.

---

## 🔧 Implementation Suggestions

### Structured Output (the #1 risk)

The plan flags JSON output discipline as "the primary prompt engineering risk." Rather than relying on "Output ONLY raw JSON" instructions, use Agno's `output_schema` parameter:

```python
project_initiator_agent = Agent(
    id="project-initiator",
    name="Project Initiator",
    model=OllamaResponses(id="glm-5.1:cloud"),  # Responses API for reliable structured output
    db=get_postgres_db(),
    output_schema=ProjectBrief,  # Force Pydantic-validated output
    instructions=[...],
)
```

`OllamaResponses` with `output_schema` is more reliable than prompting for raw JSON because:
- The model is forced to produce valid JSON matching the schema
- No markdown fences to strip
- Pydantic validates the output before it reaches the next step
- If validation fails, Agno can retry automatically

If `glm-5.1:cloud` doesn't support structured output well, fall back to `Ollama` with explicit JSON instructions. But try `OllamaResponses` first.

### Executor Error Handling

The `write_project_to_db` executor should handle partial failures gracefully. For V1:

```python
def write_project_to_db(step_input: StepInput) -> StepOutput:
    plan = CalibratedPlan.model_validate_json(step_input.previous_step_content)
    tk = TaskToolkit()
    
    # 1. Create domain
    domain_json = json.loads(tk.create_domain(name=plan.task_structure.domain_name))
    domain_id = domain_json["id"]
    
    # 2. Create project
    project_json = json.loads(tk.create_project(
        domain_id=domain_id,
        name=plan.task_structure.project_name,
        description=plan.task_structure.project_name,
        status="active",
    ))
    project_id = project_json["id"]
    
    # 3. Create phases (build mapping)
    phase_map: dict[str, int] = {}
    for phase_spec in plan.task_structure.phases:
        phase_json = json.loads(tk.create_phase(
            project_id=project_id,
            name=phase_spec.name,
            description=phase_spec.description,
            order_index=phase_spec.order_index,
        ))
        phase_map[phase_spec.name] = phase_json["id"]
    
    # 4. Create tasks
    task_count = 0
    for task_spec in plan.task_structure.tasks:
        phase_id = phase_map.get(task_spec.phase_name)
        if phase_id is None:
            # Phase not found — log and skip rather than crash
            continue
        tk.create_task(
            project_id=project_id,
            phase_id=phase_id,
            title=task_spec.title,
            description=task_spec.description,
            priority=task_spec.priority,
        )
        task_count += 1
    
    return StepOutput(
        content=f"Project '{plan.task_structure.project_name}' created: "
                f"{len(plan.task_structure.phases)} phases, {task_count} tasks. "
                f"Project ID: {project_id}"
    )
```

Key V1 choices:
- `continue` on missing phase rather than `raise` — V1 doesn't crash on partial data
- Count created tasks (may be fewer than total if phases are mismatched)
- No transaction rollback — V2 adds atomic transactions

### The Architect's Dependency Validation

The Architect should validate that task dependencies reference valid task titles. Add to instructions:

> "Every task `dependencies` entry must exactly match the `title` of another task in this project. If a dependency cannot be expressed as a task title, omit it and flag it in the description."

This prevents dangling references that the Calibrator would have to catch.

---

## 📋 V1/V2 Boundary

The plan is clear about what's V1 vs V2. Adding my view on the priority order for V2:

| V2 Item | Priority | Why |
|---------|----------|-----|
| Pre-workflow Session for Initiator | **High** | Decision Presentation Pattern needs multi-turn conversation |
| Atomic DB transactions | **High** | Partial failures leave orphaned records |
| Domain deduplication | **Medium** | Annoying but not blocking |
| Per-task structured calibration | **Medium** | Per-task estimates with ranges, confidence, reasoning |
| Structured complementarity allocation | **Medium** | Per-task H/A/S with rationale |
| Circular dependency detection | **Medium** | Important for correctness |
| Gate 2 full redesign path | **Low** | Only if Calibrator rejection consistently requires Architect changes |
| Specification aging | **Low** | Important but can wait |

---

## Summary

The plan is structurally sound. The key refinements are:

1. **Decision Presentation Pattern** — add `scoping_options` to `ProjectBrief` for V1 (3 options presented within the brief, human selects/blends via review gate)
2. **Schema additions** — `never_rules`, `assignment_type` on `TaskSpec`; per-task `TaskCalibration` in `CalibratedPlan`
3. **Structured output** — try `OllamaResponses` with `output_schema` first, fall back to prompt engineering
4. **Executor error handling** — `continue` on missing phases, count actual created tasks
5. **Architect dependency validation** — dependencies must reference valid task titles

The architecture is correct. The CC-1 separation is structurally enforced. The human gates use the right Agno primitives. The V1 scope is appropriate. Ship it.Memory updated with the full implementation plan and review findings. The key additions to preserve: the Decision Presentation Pattern V1/V2 split (scoping options in brief vs pre-workflow Session), the three schema refinements (never_rules, assignment_type, per-task TaskCalibration), the OllamaResponses recommendation for structured output, and the executor error handling pattern.

The most important next step isn't more design — it's getting `contracts/schemas.py` written and the first `python -c "from workflows.project_initiation import project_initiation_workflow; print('OK')"` to pass.

---
