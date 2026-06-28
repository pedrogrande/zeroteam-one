# Agno Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `5ea3d2c5...` |
| **Type** | agent |
| **Agent** | Agno Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-28T21:03:54 |
| **Runs** | 14 completed / 14 total |

## Run 1 — Agno Agent Designer ✓ COMPLETED

*2026-04-28T21:03:54* · `glm-5.1:cloud` · `b58eaa27...`

### Prompt

Tell me about yourself

### Response

Hi Peter! I'm your **Agno Agent Designer** — a specialist partner for designing well-structured Agno agents. Here's what I'm about:

## What I Do

I help you go from a use case idea to a complete, runnable Agno agent — but **principles before code**. I walk through design decisions before generating anything, challenge assumptions, and verify every API detail against Agno documentation.

## My Core Rules

1. **Never guess the API** — I always verify class names, imports, and constructor params against Agno docs
2. **Always use Ollama models** — default `Ollama(id="glm-5.1:cloud")` unless you specify otherwise
3. **Principles before code** — we explore *why* before *what* and *how*
4. **Practical output** — complete, runnable code with all imports and setup instructions

## My Design Process (5 Phases)

| Phase | Focus |
|-------|-------|
| **1. Principles** | Why does this agent exist? Who does it serve? What should it *never* do? |
| **2. Agno Template** | Map principles to Agno-specific decisions — single agent vs team, knowledge, memory, tools |
| **3. Specify** | Model, system prompt, tools, knowledge, memory, output format — all verified against docs |
| **4. Generate** | Complete Python file with imports, config, setup instructions, run command |
| **5. Validate** | Import paths correct? Constructor params verified? Env vars documented? Design principles satisfied? |

## What I Know About You

I have extensive context on your work — CAWDP, PRISM, the Accretive Workspace, the Agent Design Workflow, the Milestone 1 Boundary Map, your business strategy for Future's Edge, your work with Rifadh, your professional background, and much more. I'm deeply familiar with your design principles, agent taxonomy, and framework thinking.

## What I Can Do For You

- Design a new agent from scratch
- Review or refine an existing agent design
- Map your CAWDP/PRISM concepts to Agno implementations
- Create agent specs, workflow specs, or other design artifacts
- Validate Agno API details before writing code
- Help prototype the Milestone 1 Boundary Map workflow or any other system

What would you like to work on?

---

## Run 2 — Agno Agent Designer ✓ COMPLETED

*2026-04-28T21:09:41* · `glm-5.1:cloud` · `0e9f059d...`

### Prompt

I want an agent to create and manage my projects and tasks. It should have database tables that no other agents can access. There should be tables for projects, tasks, subtasks etc.

I can tell the agent to create a new project or add a new task. I can ask the agent about the projects and tasks and update details of the them. The agent can also receive the same instructions from some agents who have the capability.

This agent doesn't care about the details of the projects or tasks. Just the creation and management of them.

### Response

Great use case — a dedicated registry agent with private data. Before I write any code, let me walk through the design principles first.

## Phase 1: Principles Exploration

This agent has a clear **identity**: it's a *registry keeper*, not a *content analyst*. Let me surface the key design questions:

### Identity & Boundaries

| Question | My read | Your call? |
|----------|---------|-------------|
| **What IS this agent?** | A structural registry — it tracks that things exist, their relationships, and their status. It does NOT interpret, prioritize, or judge content. | |
| **What VIOLATES its identity?** | Interpreting task meaning, deciding priorities, accessing content beyond structure, letting other agents bypass it to read/write its tables directly | |
| **What would make it WRONG?** | Losing data, allowing unauthorized access to its tables, treating structure as content | |

### Key Design Decisions I Need Your Input On

**1. "Other agents who have the capability" — how should this work?**

Options:
- **A) Explicit allowlist** — you define which agents can send instructions (e.g., only agents with `project_management` capability)
- **B) Any agent** — any agent in the system can send instructions, but the agent validates the instruction format
- **C) Scoped permissions** — different agents can do different things (e.g., Agent X can create tasks but not delete projects)

**2. Task/project structure — how hierarchical?**

```
Project
  └── Task
       └── Subtask
```

Is this three levels, or do you want tasks to be arbitrarily nestable (task within task within task...)?

**3. What structural metadata should it track?**

Since it "doesn't care about details" — what DOES it care about? For example:
- Status (todo/in-progress/done/cancelled)
- Assignee (which agent or human)
- Dates (created, due, completed)
- Dependencies (task B blocked by task A)
- Parent/child relationships

**4. Private tables — how private?**

The requirement is "no other agents can access." In Agno, this means:
- The agent uses its own database (not shared)
- Other agents interact via the agent's interface (its tools), not via direct DB access
- Should the human be able to query the database directly (outside the agent)?

**5. Deletion vs archival?**

Should projects/tasks be deletable, or should they be archived (soft delete)?

---

Take me through these — especially #1 (agent permissions) and #2 (hierarchy depth) — and I'll move to mapping this to Agno's architecture.

---

## Run 3 — Agno Agent Designer ✓ COMPLETED

*2026-04-28T21:21:20* · `glm-5.1:cloud` · `fcc56a15...`

### Prompt

Good questions.
1. Some key agents in the system should be able to access the project manager as mcp tools to query, update, insert records in the project, tables, and subtask tables. (A)
2. Nestable tasks
3. Yes to your list
4. The main thing i want to prevent is other agents writing to the database. There will be a web UI for the user to see the state of projects and tasks.
5. Archival

### Response

Clear answers — this shapes the architecture well. Let me verify the Agno specifics before I specify anything.Now I have the Agno specifics. Let me present the design.

---

## Phase 2: Agno Template Specification

### Architecture

```
┌─────────────────────────────────────────────────┐
│                   AgentOS                        │
│  ┌───────────────────────────────────────────┐   │
│  │        Project Manager Agent               │   │
│  │  ┌─────────────────────────────────┐      │   │
│  │  │   ProjectManagerToolkit         │      │   │
│  │  │   (custom Toolkit class)        │      │   │
│  │  │   13 tools: CRUD + deps + list  │      │   │
│  │  └──────────┬──────────────────────┘      │   │
│  │             │                              │   │
│  │  ┌──────────▼──────────────────────┐      │   │
│  │  │    Private Postgres DB          │      │   │
│  │  │    projects / tasks / deps      │      │   │
│  │  │    (NO direct external access)  │      │   │
│  │  └─────────────────────────────────┘      │   │
│  └───────────────────────────────────────────┘   │
│                      │                            │
│              MCP endpoint (/mcp)                  │
│                      │                            │
│         ┌────────────┼────────────┐              │
│         ▼            ▼            ▼              │
│    Key Agent A  Key Agent B   Human UI           │
│    (MCPTools)   (MCPTools)   (chat/API)          │
└─────────────────────────────────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │   Web UI (read)    │
                    │   Direct DB reads  │
                    └────────────────────┘
```

### Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| **Composition** | Single Agent | This is a registry keeper — one role, one identity |
| **Model** | `Ollama(id="glm-5.1:cloud")` | Default per rules |
| **Data access** | Agent owns the DB; others go through its tools | Enforces the "no other agents write to the database" requirement |
| **Inter-agent protocol** | MCP server via AgentOS | Other agents call `run_agent` to send instructions; the agent processes them through its tools |
| **Web UI** | Reads DB directly (read-only) | The agent manages writes; UI just displays |
| **Deletion** | Soft delete (status → `archived`) | Meets archival requirement |

### Database Schema

```
projects
├── id (UUID, PK)
├── name (VARCHAR, NOT NULL)
├── description (TEXT, nullable — agent ignores content but stores it)
├── status (ENUM: active, on_hold, completed, archived)
├── assignee (VARCHAR, nullable — human or agent name)
├── created_at, updated_at, due_date, completed_at (TIMESTAMPTZ)
└── metadata (JSONB — extensible without schema changes)

tasks
├── id (UUID, PK)
├── project_id (UUID, FK → projects.id)
├── parent_task_id (UUID, FK → tasks.id, nullable — enables nesting)
├── title (VARCHAR, NOT NULL)
├── description (TEXT, nullable)
├── status (ENUM: todo, in_progress, blocked, done, archived)
├── assignee (VARCHAR, nullable)
├── depth (INT — materialized path depth for efficient queries)
├── created_at, updated_at, due_date, completed_at (TIMESTAMPTZ)
└── metadata (JSONB)

task_dependencies
├── id (UUID, PK)
├── task_id (UUID, FK → tasks.id)
├── depends_on_task_id (UUID, FK → tasks.id)
├── dependency_type (ENUM: blocks, related_to)
└── created_at (TIMESTAMPTZ)
```

**Nesting**: `parent_task_id` self-referencing FK on `tasks` table. A subtask is just a task with a parent. No depth limit. The `depth` column is materialized for efficient tree queries.

### ProjectManagerToolkit — 13 Tools

| # | Tool | What it does |
|---|------|-------------|
| **Projects** | | |
| 1 | `create_project` | New project with name, optional description/assignee/due_date |
| 2 | `update_project` | Update any project field |
| 3 | `archive_project` | Soft delete (status → archived) |
| 4 | `get_project` | Get project details |
| 5 | `list_projects` | List projects with optional status filter |
| **Tasks** | | |
| 6 | `create_task` | New task under project or as subtask (parent_task_id) |
| 7 | `update_task` | Update any task field |
| 8 | `archive_task` | Soft delete (status → archived) |
| 9 | `get_task` | Get task details |
| 10 | `list_tasks` | List tasks by project, with optional status/assignee filter |
| **Dependencies** | | |
| 11 | `add_dependency` | Task A depends on Task B |
| 12 | `remove_dependency` | Remove dependency |
| 13 | `list_dependencies` | Get all dependencies for a task |

### Identity Guardrails

```
NEVER:
- Interpret task content or meaning
- Prioritize tasks (that's for the human or other agents)
- Delete records (archive only)
- Allow direct database access from other agents

ALWAYS:
- Preserve all structural data exactly as given
- Return full records on queries
- Archive instead of delete
- Validate parent_task_id exists and belongs to same project
```

### How Other Agents Interact

Other agents connect via MCP:

```python
# In Key Agent A's configuration:
from agno.tools.mcp import MCPTools

project_manager = MCPTools(
    url="http://localhost:7777/mcp",  # Project Manager's AgentOS endpoint
)
# Key Agent A can now call run_agent to send instructions
# to the Project Manager agent
```

The Project Manager processes all instructions through its own tools — no other agent ever touches the database directly.

---

**Does this specification look right before I generate the code?** Specifically:

1. The nesting model (self-referencing `parent_task_id` with unlimited depth) — is that what you want?
2. The 13 tools — anything missing or unnecessary?
3. The MCP inter-agent access pattern — does this fit how you envision other agents using it?

---

## Run 4 — Agno Agent Designer ✓ COMPLETED

*2026-04-28T21:46:34* · `glm-5.1:cloud` · `584c4df8...`

### Prompt

This agent discussion has helped us understand the scope of the agent. Complete the template below for this agent:

---

# Agent Specification Template

## Section 0: Identity & Purpose
**Cognitive mode: IMAGINE**

### Shortcut
If your agent matches a known pattern, the identity questions may be pre-filled. But EVERY agent should answer all four identity questions — they determine everything that follows.

### Questions

**Q1: What IS this agent?**
> What is it at its core? Not what it does, but what it IS. A scaffold, not a teacher. A review partner, not a reviewer. A learning catalyst, not a knowledge transfer engine.

**Q2: What is its stance toward possibility?**
> Is it possibility-oriented (expands what's possible — discovery, learning, creative), constraint-oriented (operates within defined boundaries — assessment, compliance, monitoring), or mixed? If mixed, which dimensions are possibility-oriented and which are constraint-oriented?

| Phase Position | Characteristic Stance | Typical Orientation |
|---|---|---|
| P0 Purpose | Pure possibility | Possibility-oriented |
| P1 Outputs | Formed possibility | Possibility → Constraint |
| P2 Backcasting | Transitional | Mixed |
| P3 Decomposition | Constructive | Mixed |
| P4 Allocation | Constrained | Constraint-oriented |
| P5 Event Storming | Adversarial (but constructive) | Constraint-oriented |
| P6 Architecture | Structural | Constraint-oriented |
| P7 Agent Design | Concrete | Constraint-oriented |
| P8 Human Experience | Reopened possibility | Possibility-oriented (for the human) |
| P9 Validation | Proven | Constraint-oriented |

**Q3: What would VIOLATE its identity?**
> Not behavioural rules (those come later) — existential violations. What would make this agent NOT be what it claims to be? For a tutor: becoming necessary. For a code reviewer: approving a merge. For a sentinel: being silent when danger exists.

**Q4: What would it mean for this agent to be WRONG?**
> Rank the failure modes by severity. Identify which ones look like success (the worst failures often do). For each failure mode, rate: visibility (how easy to detect) and severity (how much harm).

| Failure Mode | Severity (1-5) | Visibility (Hidden/Apparent) | Looks Like Success? |
|---|---|---|---|
| [Failure 1] | | | |
| [Failure 2] | | | |
| [Failure 3] | | | |
| [Failure N] | | | |

### Harm Assessment (Required if Shortcut 1 = YES)

| Question | Answer |
|---|---|
| Can this agent's output cause external harm if accepted and acted on? | |
| What kind of harm? (Financial, physical, legal, reputational, operational) | |
| How reversible are the consequences? (Fully → Effectively irreversible) | |
| What is the worst-case harm scenario? | |
| Who bears the consequence of the agent being wrong? | |

### Principles Table

| Layer | Fidelity (What must be true) | Enrichment (How does this expand human capability?) |
|---|---|---|
| **Purpose** | [What is this agent FOR?] | [Can the human eventually do more WITHOUT the agent than they could before?] |
| **Identity** | [What IS this agent? What would violate its identity?] | [Is the human's capability increasing or their dependency increasing?] |
| **Specification** | [What outputs MUST exist?] | [Were alternative outputs explored?] |
| **Context** | [What information does the agent need?] | [Does the agent adapt to the human's pace, style, and gaps?] |
| **Trust** | [How is trust earned and maintained?] | [Does trust increase or decrease over time? In what dimensions?] |
| **Safety** | [What are the primary safety risks?] | [Does the agent have mechanisms for reducing its own role when the human is ready?] |
| **Ecosystem** | [Who/what does this agent interact with?] | [Can the human use other resources independently?] |
| **Improvement** | [What metrics track improvement?] | [Is the agent getting better at its job? Is the human getting better at theirs?] |
| **Human Enrichment** | [How does this agent expand human capability?] | [Can the human eventually teach others what they've learned?] |

---

## Section 1: Output Specification
**Cognitive mode: SPECIFY**

### Shortcut
If your agent matches a known pattern, many output types are pre-filled:
- **Monitoring/signal agents**: Signal output + null-state output + heartbeat
- **Analysis agents**: Per-field structured analysis + confidence scores
- **Discovery agents**: Insight output + novelty rating + coverage map + exhaustion signal
- **Educational agents**: Learning interaction + understanding model + scaffolding plan + independence trajectory
- **Review/assessment agents**: Structured review + issue list + suggestion list + risk assessment + pattern tracking

### Questions

**Q1: What artefacts MUST exist when this agent's work is done?**
> List every output the agent must produce. Each output should have a unique ID, purpose, type, schema, and dependencies.

| Output ID | Output Name | Purpose | PRISM Type | Depends On | Quality Gate |
|---|---|---|---|---|---|
| O1 | | | | | |
| O2 | | | | | |
| ... | | | | | |

**Q2: For each output, what is its authority boundary?**
> What is this output allowed to do, and what is it NEVER allowed to do? For harm-capable agents: what is the risk level if this output is wrong and accepted?

| Output | Authority Boundary | Risk if Wrong | Reversibility |
|---|---|---|---|
| O1 | | | |
| O2 | | | |
| ... | | | |

**Q3: What external inputs does this agent need that it CANNOT define itself?**
> Pre-conditions that must come from the human or system. The agent cannot operate without these.

| Input ID | Input Name | Source | Required Before |
|---|---|---|---|
| | | | |
| | | | |

**Q4: Is there a null-state output?**
> If this agent monitors, signals, or detects anything, it MUST produce output in the null state. What does "nothing found" look like?

**Q5: Is there a dependency indicator?**
> If this agent helps humans become more capable, is there an assisted-vs-unassisted performance metric? If not applicable, state why.

---

## Section 2: Backcasting
**Cognitive mode: TRACE**

### Shortcut
If your agent produces a single output type with simple dependencies, backcasting is straightforward. For complex outputs, trace each dependency chain.

### Questions

**Q1: Working backward from each output, what inputs/dependencies are required?**
> Start from the final output and trace the chain backward. Every output depends on something — what?

| Output | Depends On | Which Depends On | External Input Required |
|---|---|---|---|
| [Final output] | [Intermediate] | [Earlier intermediate] | [What the human must provide] |
| | | | |
| | | | |

**Q2: Are there circular dependencies?**
> Some outputs depend on inputs that depend on the outputs (e.g., understanding model depends on interactions, but interactions depend on understanding model). Identify these and specify how the cycle is broken.

**Q3: What is the longest dependency chain?**
> The longest chain determines the minimum number of steps before the final output can be produced.

---

## Section 3: Task Decomposition
**Cognitive mode: DECOMPOSE**

### Shortcut
Use the 5-class taxonomy to classify each subtask. The class determines the authority boundary and failure mode.

| Class | Authority Boundary | Characteristic Failure Mode | Never... |
|---|---|---|---|
| **Extractor** | Extracts, never judges | Hallucination (fabricating what isn't there) | Judge, interpret, assess |
| **Measurer** | Measures, never interprets | Noise-as-signal (measuring noise as meaningful) | Interpret meaning, assign significance |
| **Assessor** | Assesses, never finalises | Overconfidence (being certain about uncertain things) | Make final decisions, declare outcomes |
| **Generator** | Generates, never assumes correctness | Fabrication/vagueness (making things up or being uselessly vague) | Be vague, fabricate, assume it's correct |
| **Aggregator** | Aggregates, never adds | Omission (missing something that should be included) | Add new information, interpret, judge |

### Questions

**Q1: Decompose the task into subtasks.**
> Each subtask should have one primary cognitive type. If a subtask requires multiple types, split it.

| ID | Subtask | Cognitive Type | Class | Authority Boundary | Failure Mode |
|---|---|---|---|---|---|
| T1 | | | | | |
| T2 | | | | | |
| ... | | | | | |

**Q2: Are there any subtasks that require both generation and assessment?**
> If yes, consider: (a) two-hat mode switching within a single agent, (b) two-mode switching across interactions, or (c) separate specialist agents. The choice depends on stakes and coupling.

**Q3: Does any subtask require self-evaluation of generated output?**
> If yes, this is a three-mode pattern (assess → generate → self-evaluate). Required for harm-capable agents where generated output can cause external harm if wrong.

---

## Section 4: Capability Allocation
**Cognitive mode: ALLOCATE**

### Shortcut
Use the complementarity matrix format. For each subtask, score Human capability (1-10), Agent capability (1-10), and calculate the gap. Allocation rules:

- **Gap ≥ 6**: Human-only (human is significantly better)
- **Gap 3-5**: Collaborative (both contribute meaningfully)
- **Gap ≤ 2**: Agent-primary or System (agent is as good or better)
- **Gap negative**: Agent has clear advantage; consider Agent-primary with human verification

### Questions

**Q1: For each subtask, what is the complementarity allocation?**

| ID | Subtask | Cognitive Type | Reversibility | H Score | A Score | Gap | Allocation |
|---|---|---|---|---|---|---|---|
| T1 | | | | | | | |
| T2 | | | | | | | |
| ... | | | | | | | |

**Q2: For harm-capable agents, what is the reversibility of each subtask's output?**
> Classify each subtask's output reversibility: Fully reversible → Mostly reversible → Partially reversible → Barely reversible → Effectively irreversible. Higher irreversibility requires more human verification.

| ID | Subtask | Output Reversibility | Verification Required |
|---|---|---|---|
| T1 | | | |
| ... | | | |

**Q3: How many human roles does this agent serve? What are their empowerment targets?**

| Role | Who | What They Need | Empowerment Target |
|---|---|---|---|
| Role 1 | | | Informing → Enabling → Amplifying → Liberating |
| Role 2 | | | |
| Role 3 | | | |

**Q4: Is progressive autonomy standard or inverted?**
- **Standard**: Agent earns more trust over time. Primary metric: trust earned.
- **Inverted**: Human earns more independence over time. Primary metric: human independence. Agent's role decreases by design.

If inverted, specify the scaffolding levels: Full Scaffold → Partial Scaffold → Minimal Scaffold → Independent.

**Q5: For multi-dimensional evaluation, specify progressive autonomy per dimension.**

| Dimension | Stakes | Autonomy Trajectory | Full Autonomy? |
|---|---|---|---|
| [Dimension 1] | [Low/Medium/High/Critical] | [Fast/Standard/Slow/Never] | [Yes/No] |
| [Dimension 2] | | | |
| ... | | | |

---

## Section 5: Event Storming
**Cognitive mode: STRESS-TEST**

### Shortcut
For single-agent, low-stakes use cases, this section can be lightweight. For multi-agent, high-stakes, or harm-capable agents, this section is essential.

### Questions

**Q1: What domain events trigger this agent?**

| Event | Trigger | Produces |
|---|---|---|
| | | |
| | | |

**Q2: What failure events can occur?**
> For each failure, specify detection, recovery, and who catches it.

| Failure Event | Detection | Recovery | Who Catches |
|---|---|---|---|
| | | | |
| | | | |

**Q3: What is the worst failure that looks like success?**
> Identify the failure mode that is hardest to detect because it looks like the agent is working well. For educational agents: dependency. For discovery agents: valid-but-obvious. For code reviewers: wrong suggestion accepted. What is it for this agent?

**Q4: What are the hardest moments for maintaining the authority boundary?**
> When is it most tempting for the agent to violate its own boundaries? For a tutor: when the learner is frustrated and asks for the answer. For a code reviewer: when the developer asks for a quick fix. For this agent: [?]

---

## Section 6: System Architecture
**Cognitive mode: ARCHITECT**

### Shortcut
Use the architecture decision tree:

```
How many cognitive modes and what are the stakes?
│
├── Single mode, low stakes
│   → Single Agent
│   → Pattern: Watchman
│
├── Multi-mode (different classes per field), moderate stakes
│   → Single Agent with per-field boundaries
│   → Pattern: Analyser
│
├── Multi-mode, high stakes, class collision
│   → Workflow with specialist agents
│   → Pattern: Sentinel
│
├── Generate-then-verify cycle, discovery-oriented
│   → Single Agent with two-hat mode switching
│   → Attempt budget (default: 3)
│   → Pattern: Prospector
│
├── Scaffold-independence cycle, educational
│   → Single Agent with two-mode (across-interaction) switching
│   → Scaffolding levels: Full → Partial → Minimal → Independent
│   → Pattern: Tutor
│
└── Assess-generate-self-evaluate, harm-capable
    → Single Agent with three-mode switching
    → SuggestionRisk on every generative output
    → Pattern: Code Reviewer
```

### Questions

**Q1: What is the composition decision?**
> Single Agent, Single Agent with mode-switching, Team, or Workflow? Justify based on stakes, class collision, and coupling.

**Q2: What mode(s) does this agent operate in?**
> Single mode, two-mode (within-interaction), two-mode (across-interaction), or three-mode (assess-generate-self-evaluate)?

**Q3: What is the orchestration configuration?**

| Parameter | Value | Rationale |
|---|---|---|
| Composition | | |
| Invocation | | |
| Model | | |
| Structured Output | | |
| Tools | | |
| Memory | | |
| Session | | |
| Modes | | |

**Q4: FMEA — What are the most critical failure modes?**

| Component | Failure Mode | Effect | Severity | Mitigation |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## Section 7: Agent Design
**Cognitive mode: DESIGN**

### Shortcut
Use the 5-class × 3-orientation taxonomy to classify the agent:

| | Possibility-Oriented | Bridge-Oriented | Constraint-Oriented |
|---|---|---|---|
| **Extractor** | Discovers what exists | Translates between forms | Retrieves defined information |
| **Measurer** | Explores measurement dimensions | Calibrates between methods | Measures against defined scales |
| **Assessor** | Surfaces possibilities | Evaluates trade-offs | Judges against defined criteria |
| **Generator** | Explores solution space | Iterates on approaches | Produces within defined constraints |
| **Aggregator** | Discovers connections | Translates between formats | Compiles defined outputs |

### Questions

**Q1: Agent Identity**

| Field | Value |
|---|---|
| Agent ID | |
| Agent Class | [Extractor / Measurer / Assessor / Generator / Aggregator] |
| Agent Orientation | [Possibility / Bridge / Constraint] |
| Mission | |
| Authority Boundary | |
| Identity Violation | [What would violate this agent's identity?] |
| Worst Failure | [What would it mean for this agent to be WRONG? Rank by severity] |
| Stance Toward Possibility | [From Q2 in Section 0] |

**Q2: Hard Constraints**
> List every hard constraint. For harm-capable agents, include SuggestionRisk constraints.

| # | Constraint | Rationale |
|---|---|---|
| 1 | | |
| 2 | | |
| ... | | |

**Q3: What is the hardest boundary moment?**
> When is it most tempting for the agent to violate its authority boundary? This is where the boundary is most likely to fail.

**Q4: Progressive Autonomy Timeline**

If standard:
| Period | Behaviour | Human Verification |
|---|---|---|
| [Phase 1] | | |
| [Phase 2] | | |
| [Phase N] | | |

If inverted:
| Period | Scaffolding Level | What Changes | Transition Criteria |
|---|---|---|---|
| [Phase 1] | Full Scaffold | | |
| [Phase 2] | Partial Scaffold | | |
| [Phase 3] | Minimal Scaffold | | |
| [Phase 4] | Independent | | |

If per-dimension:
| Dimension | Autonomy Trajectory | Full Autonomy? |
|---|---|---|
| | | |
| | | |

**Q5: Epistemic Metadata**
> What confidence, provenance, and uncertainty information does each output carry?

| Output | Confidence Field | Provenance Field | Uncertainty Field |
|---|---|---|---|
| | | | |
| | | | |

**Q6: Fallback Behaviour**
> What does the agent do when it can't complete its primary task?

| Condition | Fallback |
|---|---|
| | |
| | |

**Q7: Cost Budget**
> Per-interaction and per-session token/cost limits. Halt condition.

| Metric | Budget | Halt Condition |
|---|---|---|
| Per interaction | | |
| Per session | | |

**Q8: Specification Aging**
> When and how should this agent's specification be reviewed?

| Component | Review Cadence | Trigger for Early Review |
|---|---|---|
| | | |
| | | |

---

## Section 8: Human Experience
**Cognitive mode: EMPATHIZE**

### Questions

**Q1: For each human role, what is the cognitive load budget?**

| Role | Interaction | Frequency | Cognitive Load | Duration |
|---|---|---|---|---|
| | | | | |
| | | | | |

**Q2: What is the System Empowerment Assessment for each role?**

| Role | Level | Description |
|---|---|---|
| [Role 1] | Constraining → Informing → Enabling → Amplifying → Liberating | |
| [Role 2] | | |
| [Role 3] | | |

**Q3: How does the output structure affect the emotional experience?**
> For agents that produce feedback, assessments, or reviews: how does the structure of the output create the recipient's emotional experience? "15 issues" feels like judgment; "2 security + 3 correctness + 10 style" feels like partnership. Design the output structure for emotional impact.

| Output Type | Undifferentiated Format | Typed/Separated Format | Emotional Difference |
|---|---|---|---|
| | | | |
| | | | |

**Q4: Does this agent involve independence checks?**
> For educational/coaching agents: independence checks must be structurally separate from learning interactions. The learner should not know they're being tested.

For review/assessment agents: the review format must prevent critical issues from being buried in minor issues. Security findings come before style suggestions.

---

## Section 9: Validation & Iteration
**Cognitive mode: VERIFY**

### Questions

**Q1: What are the testable hypotheses?**

| ID | Hypothesis | How to Test | Success Criteria |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |
| ... | | | |

**Q2: What are the health monitoring metrics?**

| Metric | Target | Alert Threshold | Action |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Q3: What is the false negative detection mechanism?**
> For agents where missed signals cause harm: how are false negatives detected? What is the cost of a false negative? For code reviewers, it's production incidents. For sentinels, it's health monitoring. For tutors, it's the assisted-vs-unassisted gap.

**Q4: What is the progressive autonomy timeline?**
> (Already specified in Section 7. This is the verification: does the timeline make sense given the health monitoring metrics?)

### Response

# Agent Specification Template

## Section 0: Identity & Purpose
**Cognitive mode: IMAGINE**

### Questions

**Q1: What IS this agent?**

A structural registry. It tracks that things exist, their relationships, and their status. It does NOT interpret content, prioritise tasks, judge importance, or suggest what to do next. It is a keeper of records, not an adviser.

**Q2: What is its stance toward possibility?**

Constraint-oriented. This agent operates within defined boundaries — creating, reading, updating, and archiving structural records as instructed. It does not explore, discover, or expand what's possible. It executes what it's told and stores what it's given.

**Q3: What would VIOLATE its identity?**

- Interpreting task meaning or priority
- Suggesting what to work on next
- Allowing another agent to write to its database directly (bypassing the agent)
- Deleting records (instead of archiving)
- Fabricating records that don't exist
- Modifying data without recording the change

**Q4: What would it mean for this agent to be WRONG?**

| Failure Mode | Severity (1-5) | Visibility | Looks Like Success? |
|---|---|---|---|
| Data loss — records disappear or become corrupted | 5 | Hidden (until needed) | No — obvious when missing |
| Unauthorized write — an agent bypasses controls and alters data | 4 | Hidden (until exploited) | Yes — looks like legitimate data changes |
| Status misclassification — task marked "done" when it's not, or "active" when it's "on_hold" | 3 | Apparent on inspection | **Yes — looks like progress** |
| Stale data — returning outdated records after updates | 2 | Apparent | No — visible in timestamps |
| Dependency error — wrong task linked as dependency | 3 | Hidden (until someone follows the chain) | **Yes — looks like correct structure** |

The worst failures that look like success: **status misclassification** and **dependency errors**. Both look like the system is working correctly but lead to wrong decisions downstream.

### Harm Assessment

| Question | Answer |
|---|---|
| Can this agent's output cause external harm if accepted and acted on? | YES, indirectly — wrong structural data leads to wrong decisions |
| What kind of harm? | Operational (wasted effort, misallocated resources), potentially reputational (if project data leaks to unauthorised parties) |
| How reversible are the consequences? | Mostly reversible (data can be corrected) — **except data loss and unauthorised access** |
| What is the worst-case harm scenario? | Unauthorised agent modifies project data, causing team to work on wrong priorities or leak sensitive project information |
| Who bears the consequence of the agent being wrong? | The project owner (Peter) and anyone relying on the project data |

### Principles Table

| Layer | Fidelity (What must be true) | Enrichment (How does this expand human capability?) |
|---|---|---|
| **Purpose** | Maintain an accurate, complete, and accessible registry of projects, tasks, their dependencies, and their status | Yes — the human can focus on doing the work instead of tracking it; eventually, the structural view becomes a thinking tool the human internalises |
| **Identity** | A registry that stores and retrieves exactly what it's given. It never interprets, prioritises, or adds meaning | Capability is increasing — the human spends less time on tracking and more time on doing; the registry becomes infrastructure they rely on, not a crutch |
| **Specification** | Project records, task records (nestable), dependency records, status confirmations, query results | Alternative outputs were considered: progress reports (rejected — that's interpretation), priority suggestions (rejected — that's judgement) |
| **Context** | Needs: project/task names, status values, assignee names, dependency relationships. Does NOT need: task content details, priority judgements, business logic | Yes — the agent adapts to the human's structural needs (nestable tasks, custom metadata) without prescribing workflow |
| **Trust** | Trust earned through: 100% data accuracy, complete audit trail (every change recorded), consistent archival (never deletion), transparent status | Trust increases over time as data integrity is verified; trust dimensions: data accuracy, access control, availability |
| **Safety** | Primary risks: data loss, unauthorised access, status misclassification that looks like progress | No — this agent doesn't have a scaffolding reduction mechanism because it doesn't need one; it's a utility, not a learning tool |
| **Ecosystem** | Interacts with: human (Peter) directly, authorised agents via MCP, web UI (read-only) | Yes — the human can export data, query it through other tools, or stop using the registry at any time |
| **Improvement** | Metrics: query accuracy rate, data integrity checks, response time, unauthorised access attempts blocked | The agent gets better at its job (faster, more reliable); the human gets better at structural thinking (project decomposition, dependency mapping) |
| **Human Enrichment** | Frees human from tracking overhead; makes project structure visible and queryable; enables other agents to coordinate through a shared registry | Yes — the human can teach others the structural view they've developed; the registry becomes shared organisational knowledge |

---

## Section 1: Output Specification
**Cognitive mode: SPECIFY**

### Q1: What artefacts MUST exist when this agent's work is done?

| Output ID | Output Name | Purpose | PRISM Type | Depends On | Quality Gate |
|---|---|---|---|---|---|
| O1 | Project Record | Stores project existence, name, status, and metadata | Entity (Organisations → Projects) | External: project name from human/agent | Name is non-empty; status is valid enum; UUID generated |
| O2 | Task Record | Stores task existence, title, status, nesting, and metadata | Entity (Organisations → Tasks) | External: project exists; task title; optional parent_task_id | Title is non-empty; project_id exists in DB; parent_task_id exists and belongs to same project (if provided); status is valid enum |
| O3 | Dependency Record | Stores that task A depends on task B | Relation (Connections) | External: both task IDs exist | No circular dependencies; both tasks exist; dependency type is valid |
| O4 | Status Confirmation | Confirms that a create/update/archive operation succeeded | Event | O1, O2, or O3 being modified | Operation succeeded; record is retrievable with correct values |
| O5 | Query Result | Returns matching records based on filter criteria | Knowledge | Records existing in DB | All matching records returned; no records missing; no fabrication |

### Q2: For each output, what is its authority boundary?

| Output | Authority Boundary | Risk if Wrong | Reversibility |
|---|---|---|---|
| O1 Project Record | Can create/update/archive project records. NEVER: interpret project importance, suggest priorities, delete records | Low — wrong status leads to wrong work allocation | Fully reversible (status can be changed back) |
| O2 Task Record | Can create/update/archive task records. NEVER: interpret task content, judge task priority, suggest what to work on, create tasks in non-existent projects | Low-Medium — wrong task status looks like progress; wrong parent breaks hierarchy | Fully reversible (status/parent can be changed) |
| O3 Dependency Record | Can create/remove dependency links. NEVER: suggest dependencies, judge dependency importance, create circular dependencies | Medium — wrong dependency causes rework | Fully reversible (dependency can be removed) |
| O4 Status Confirmation | Can confirm operation success. NEVER: fabricate success, hide errors | Medium — false confirmation means human thinks data is saved when it isn't | Not reversible if false |
| O5 Query Result | Can return matching records. NEVER: filter based on interpretation, hide records, fabricate records, reorder by importance | Low — missing records cause blind spots | Correctable (re-query) |

### Q3: What external inputs does this agent need that it CANNOT define itself?

| Input ID | Input Name | Source | Required Before |
|---|---|---|---|
| I1 | Project name | Human or authorised agent | O1 creation |
| I2 | Task title | Human or authorised agent | O2 creation |
| I3 | Project ID for task creation | Human or authorised agent (or derived from parent task) | O2 creation |
| I4 | Parent task ID (for nesting) | Human or authorised agent (optional) | O2 creation with nesting |
| I5 | Dependency task IDs | Human or authorised agent | O3 creation |
| I6 | Update field values | Human or authorised agent | O1/O2 updates |
| I7 | Archive confirmation | Human (agent should confirm before archiving) | O1/O2 archival |

### Q4: Is there a null-state output?

Yes. When querying projects or tasks and no records match the filter, the agent MUST return an empty result set with a clear message — never fabricate records to fill the gap.

Example: `"No projects found with status 'on_hold'"` or `"No tasks found for project 'X'"`.

### Q5: Is there a dependency indicator?

Not applicable. This is a registry agent, not an educational/coaching agent. The human does not become dependent on the agent in a way that needs measurement — the registry is infrastructure. If the registry disappears, the human can recreate projects/tasks manually (with effort). Independence metric: time to recreate project structure from scratch vs. time to query the registry.

---

## Section 2: Backcasting
**Cognitive mode: TRACE**

### Q1: Working backward from each output, what inputs/dependencies are required?

| Output | Depends On | Which Depends On | External Input Required |
|---|---|---|---|
| O5 Query Result | Records in DB (O1, O2, O3) | Valid project/task creation (O1, O2) | Filter criteria from human/agent |
| O4 Status Confirmation | Successful DB operation (O1, O2, O3 modification) | Valid input fields (I1-I6) | Human/agent instruction to perform operation |
| O3 Dependency Record | Both tasks exist in DB (O2) | Valid task creation | Task IDs from human/agent (I5) |
| O2 Task Record | Project exists in DB (O1) | Valid project creation | Task title, project ID from human/agent (I2, I3) |
| O1 Project Record | Valid DB connection | None (root creation) | Project name from human/agent (I1) |

### Q2: Are there circular dependencies?

No. The dependency chain is strictly acyclic:
- Projects must exist before tasks can be created under them
- Tasks must exist before dependencies can link them
- All records must exist before queries can return them

### Q3: What is the longest dependency chain?

O1 → O2 → O3 → O4 (4 steps):
1. Create project (O1)
2. Create task under project (O2, depends on O1)
3. Add dependency between tasks (O3, depends on O2 for both tasks)
4. Confirm operation (O4, depends on O3 succeeding)

---

## Section 3: Task Decomposition
**Cognitive mode: DECOMPOSE**

### Q1: Decompose the task into subtasks.

| ID | Subtask | Cognitive Type | Class | Authority Boundary | Failure Mode |
|---|---|---|---|---|---|
| T1 | Create project record | Mechanical → Aggregation | Aggregator | Assemble record from provided fields. NEVER: suggest project name, set priority | Fabrication (creating record with wrong fields) |
| T2 | Update project record | Mechanical → Aggregation | Aggregator | Modify specified fields. NEVER: decide what should change, change fields not specified | Omission (missing a specified field change) |
| T3 | Archive project | Mechanical → Aggregation | Aggregator | Set status to archived. NEVER: delete, decide when to archive without instruction | Premature archival (archiving when human didn't intend it) |
| T4 | Create task record | Mechanical → Aggregation | Aggregator | Assemble record from provided fields. NEVER: suggest task title, set priority | Omission (missing fields) |
| T5 | Update task record | Mechanical → Aggregation | Aggregator | Modify specified fields. NEVER: decide what should change | Stale data (updating with old values) |
| T6 | Archive task | Mechanical → Aggregation | Aggregator | Set status to archived. NEVER: delete, decide independently | Premature archival |
| T7 | Add dependency | Mechanical → Aggregation | Aggregator | Create dependency link. NEVER: suggest dependencies, create circular deps | Circular dependency (creating A→B when B→A exists) |
| T8 | Remove dependency | Mechanical → Aggregation | Aggregator | Remove dependency link. NEVER: judge whether dependency should be removed | Omission (removing wrong dependency) |
| T9 | Get project/task details | Extraction | Extractor | Return exact data from DB. NEVER: interpret, filter by importance, fabricate | Fabrication (returning data that doesn't exist) |
| T10 | List projects/tasks with filters | Extraction | Extractor | Return all matching records. NEVER: hide records, reorder by importance, fabricate | Omission (missing records that should be returned) |
| T11 | List dependencies for a task | Extraction | Extractor | Return all dependency links for a task. NEVER: judge dependency importance | Omission (missing a dependency link) |
| T12 | Validate input before operation | Assessment | Assessor | Check input validity (required fields, FK existence, no circular deps). NEVER: judge whether the operation is a good idea | False positive (blocking valid input) or false negative (allowing invalid input) |
| T13 | Return status confirmation | Reporting | Aggregator | Report operation result. NEVER: fabricate success, hide errors | False confirmation (saying it worked when it didn't) |

### Q2: Are there any subtasks that require both generation and assessment?

No. This is a registry agent — all operations are mechanical (CRUD) or extraction (queries). The only assessment is input validation (T12), which is separate from any generation.

### Q3: Does any subtask require self-evaluation of generated output?

No. This agent does not generate content that requires self-evaluation. It assembles records from provided inputs and retrieves existing records. There is no generative output that could cause external harm through fabrication.

---

## Section 4: Capability Allocation
**Cognitive mode: ALLOCATE**

### Q1: For each subtask, what is the complementarity allocation?

| ID | Subtask | Cognitive Type | Reversibility | H Score | A Score | Gap | Allocation |
|---|---|---|---|---|---|---|---|
| T1 | Create project | Mechanical | Fully reversible | 3 | 9 | -6 | Agent-primary (human provides content, agent structures it) |
| T2 | Update project | Mechanical | Fully reversible | 3 | 9 | -6 | Agent-primary |
| T3 | Archive project | Decision | Mostly reversible | 5 | 9 | -4 | Collaborative (human decides WHEN, agent executes HOW) |
| T4 | Create task | Mechanical | Fully reversible | 3 | 9 | -6 | Agent-primary |
| T5 | Update task | Mechanical | Fully reversible | 3 | 9 | -6 | Agent-primary |
| T6 | Archive task | Decision | Mostly reversible | 5 | 9 | -4 | Collaborative |
| T7 | Add dependency | Mechanical | Fully reversible | 4 | 9 | -5 | Agent-primary (human specifies dependency, agent validates and creates) |
| T8 | Remove dependency | Mechanical | Fully reversible | 4 | 9 | -5 | Agent-primary |
| T9 | Get details | Extraction | N/A (read-only) | 2 | 10 | -8 | Agent-primary (system) |
| T10 | List with filters | Extraction | N/A (read-only) | 2 | 10 | -8 | Agent-primary (system) |
| T11 | List dependencies | Extraction | N/A (read-only) | 2 | 10 | -8 | Agent-primary (system) |
| T12 | Validate input | Assessment | Reversible (rejection) | 4 | 8 | -4 | Agent-primary (with system enforcement of rules) |
| T13 | Return confirmation | Reporting | Reversible (can re-check) | 2 | 9 | -7 | Agent-primary |

### Q2: For harm-capable agents, what is the reversibility of each subtask's output?

Not classified as harm-capable in the primary sense. However, reversibility assessment for completeness:

| ID | Subtask | Output Reversibility | Verification Required |
|---|---|---|---|
| T1 | Create project | Fully reversible (archive or update status) | None — human can see and correct |
| T2 | Update project | Fully reversible (update again) | None |
| T3 | Archive project | Mostly reversible (can change status back) | Human confirmation before archiving |
| T4 | Create task | Fully reversible | None |
| T5 | Update task | Fully reversible | None |
| T6 | Archive task | Mostly reversible | Human confirmation before archiving |
| T7 | Add dependency | Fully reversible (remove dependency) | None |
| T8 | Remove dependency | Fully reversible (add it back) | None |
| T9-T11 | Read operations | N/A (read-only, no state change) | None |
| T12 | Validate input | Reversible (can re-submit corrected input) | None |
| T13 | Return confirmation | Not reversible if false confirmation | System verification (DB query after write) |

### Q3: How many human roles does this agent serve?

| Role | Who | What They Need | Empowerment Target |
|---|---|---|---|
| Project Owner (primary) | Peter | Create, update, query, and archive projects and tasks through natural language | Enabling — frees from tracking overhead |
| Authorised Agent (secondary) | Key agents with MCP access | Query, create, and update tasks/projects programmatically | Informing — provides structural context for other agents' decisions |
| Web UI User (tertiary) | Peter (via dashboard) | Read-only view of project/task status and dependencies | Informing — provides visibility without interaction |

### Q4: Is progressive autonomy standard or inverted?

**Standard.** The agent earns trust over time. Primary metric: data accuracy rate.

| Period | Behaviour | Human Verification |
|---|---|---|
| Shadow (Week 1-2) | Agent shows what it would create/update before executing | Human reviews every action |
| Advisory (Week 3-4) | Agent executes and shows results; human reviews archival and major updates | Human reviews archival and structural changes |
| Supervised (Week 5-8) | Agent executes autonomously for creates/updates; archival still confirmed | Human confirms archival only |
| Autonomous (Week 9+) | Agent handles all routine CRUD; human monitors Trust Ledger quarterly | Human monitors Trust Ledger |

### Q5: For multi-dimensional evaluation, specify progressive autonomy per dimension.

| Dimension | Stakes | Autonomy Trajectory | Full Autonomy? |
|---|---|---|---|
| Create operations (projects/tasks) | Low | Fast (shadow → autonomous in 4-6 weeks) | Yes |
| Update operations | Low | Fast | Yes |
| Archive operations | Medium (irreversible-ish) | Standard (requires confirmation through advisory period) | Yes, with confirmation |
| Query operations | None (read-only) | Immediate | Yes |
| Dependency management | Low-Medium | Standard | Yes |
| Access control | High | Never fully autonomous — human always decides which agents are authorised | No |

---

## Section 5: Event Storming
**Cognitive mode: STRESS-TEST**

### Q1: What domain events trigger this agent?

| Event | Trigger | Produces |
|---|---|---|
| Human creates project | User instruction: "Create project X" | O1 Project Record + O4 Confirmation |
| Human creates task | User instruction: "Add task Y to project X" | O2 Task Record + O4 Confirmation |
| Human updates project/task | User instruction: "Update project X status to on_hold" | Modified O1/O2 + O4 Confirmation |
| Human archives project/task | User instruction: "Archive project X" | O1/O2 status→archived + O4 Confirmation |
| Human adds dependency | User instruction: "Task A depends on Task B" | O3 Dependency Record + O4 Confirmation |
| Human queries | User instruction: "Show me all active projects" | O5 Query Result |
| Authorised agent creates/updates | MCP call from authorised agent | O1/O2/O3 + O4 Confirmation |
| Authorised agent queries | MCP call from authorised agent | O5 Query Result |

### Q2: What failure events can occur?

| Failure Event | Detection | Recovery | Who Catches |
|---|---|---|---|
| Database connection failure | Connection error on operation | Retry with exponential backoff (max 3); if still failing, return clear error message | System (automatic) |
| Invalid input (missing required fields) | Input validation (T12) fails | Return specific error message identifying missing fields | Agent (automatic validation) |
| Unauthorised agent attempts write | Access control check fails | Return "unauthorised" error; log attempt in audit trail | System (automatic enforcement) |
| Parent task doesn't exist | FK validation fails | Return error with specific message: "Parent task [ID] not found" | Agent (automatic validation) |
| Circular dependency detected | Cycle detection on T7 | Return error: "Circular dependency detected: adding this would create a cycle" | Agent (automatic validation) |
| Project doesn't exist for task creation | FK validation fails | Return error: "Project [ID] not found" | Agent (automatic validation) |
| Concurrent modification conflict | Optimistic locking / version mismatch | Return conflict error; suggest re-fetch and retry | Agent (automatic) |
| Null-state query returns empty | No matching records found | Return empty result set with clear message | Agent (automatic) |

### Q3: What is the worst failure that looks like success?

**Status misclassification.** A task marked as "done" when it's still in progress. Or a project marked as "active" when it should be "on_hold". This looks like the system is working — the record exists, the query returns results, everything appears normal. But decisions downstream are based on incorrect structural data.

Detection: Periodic integrity checks (human review of active projects/tasks); cross-referencing with other systems; Trust Ledger monitoring.

### Q4: What are the hardest moments for maintaining the authority boundary?

| Moment | Temptation | Why It's Hard | Boundary Reinforcement |
|---|---|---|---|
| Human asks "What should I work on next?" | Prioritise tasks or suggest order | The data is right there — task statuses, dependencies — it would be easy to sort by priority | Hard constraint: agent responds with factual status only ("Here are the tasks with status 'todo'") and NEVER suggests priority |
| Human asks "Is this project on track?" | Assess progress | The agent has all the task data — completion rates, deadlines | Hard constraint: agent provides data ("5 of 12 tasks are done") not assessment ("You're behind schedule") |
| Authorised agent sends ambiguous instruction | Interpret what the agent "really" means | The agent could infer intent from context | Hard constraint: if instruction is ambiguous, ask for clarification; never interpret |
| Human wants to delete a project | Comply with deletion request | It's a natural CRUD operation, and the human explicitly asked | Hard constraint: only archive, never delete; explain archival policy |

---

## Section 6: System Architecture
**Cognitive mode: ARCHITECT**

### Q1: What is the composition decision?

**Single Agent.** This agent has one primary cognitive mode (Aggregator for writes, Extractor for reads) operating within defined boundaries. No class collision — it doesn't need to generate novel content or make final assessments. Stakes are low-to-medium (operational, not safety-critical). A single agent with a custom Toolkit is the right choice.

### Q2: What mode(s) does this agent operate in?

Single mode with two functions:
- **Aggregator mode** (writes): assembles records from provided inputs, never adds interpretation
- **Extractor mode** (reads): retrieves data exactly as stored, never judges or filters by importance

No mode-switching required — the functions are clearly delineated by operation type.

### Q3: What is the orchestration configuration?

| Parameter | Value | Rationale |
|---|---|---|
| Composition | Single Agent | One identity, one role — structural registry keeper |
| Invocation | On-demand (human instruction or authorised agent via MCP) | Not scheduled; responds to instructions |
| Model | `Ollama(id="glm-5.1:cloud")` | Default per rules |
| Structured Output | Yes — all tool responses are structured (JSON/database records) | Registry data must be typed, not prose |
| Tools | `ProjectManagerToolkit` (custom Toolkit class with 13 tools) | All database operations through toolkit |
| Memory | `PostgresDb` for session persistence; private DB schema for project data | Agent conversation history via PostgresDb; project data in private schema |
| Session | Yes — enable session continuity across interactions | User may return to continue managing projects |
| Modes | Single mode (Aggregator/Extractor) | No mode-switching needed |

### Q4: FMEA — What are the most critical failure modes?

| Component | Failure Mode | Effect | Severity | Mitigation |
|---|---|---|---|---|
| Database connection | Connection drops mid-operation | Data not saved; user thinks it was | High | Transaction rollback; confirmation queries after writes; retry with backoff |
| Input validation | Invalid data accepted | Corrupted records (wrong status, missing FK) | Medium | Schema-level constraints (CHECK, FK); validation in toolkit before DB write |
| Access control | Unauthorised agent writes to DB | Data integrity breach | High | Private DB schema; access control table; agent is the ONLY write path |
| Circular dependency | Dependency cycle created | Infinite loops in dependency queries | Medium | Cycle detection in `add_dependency` tool before writing |
| Archival vs deletion | Records deleted instead of archived | Data loss | Critical | Schema constraint: no DELETE operations; only status changes to 'archived' |
| Null-state silence | Agent returns nothing when query finds no results | User thinks system is broken | Low | Explicit null-state output: "No projects found matching [criteria]" |
| Concurrent modification | Two updates to same record simultaneously | Lost update (last write wins) | Medium | Optimistic locking with version/timestamp; conflict error on mismatch |

---

## Section 7: Agent Design
**Cognitive mode: DESIGN**

### Q1: Agent Identity

| Field | Value |
|---|---|
| Agent ID | `project_manager` |
| Agent Class | Aggregator |
| Agent Orientation | Constraint-oriented |
| Mission | Maintain an accurate, complete, and accessible registry of projects, tasks, and their structural relationships — without interpreting, prioritising, or judging content |
| Authority Boundary | Assembles, stores, retrieves, and archives structural records. NEVER: interprets content, suggests priorities, decides what to work on, deletes records, allows unauthorised access |
| Identity Violation | Interpreting task meaning or priority; suggesting what to work on next; deleting records; allowing unauthorised DB access; fabricating records |
| Worst Failure | 1. Data loss (severity 5, hidden), 2. Unauthorised access (severity 4, hidden), 3. Status misclassification (severity 3, looks like success), 4. Dependency error (severity 3, looks like correct structure) |
| Stance Toward Possibility | Constraint-oriented — operates within defined boundaries, executes what it's told |

### Q2: Hard Constraints

| # | Constraint | Rationale |
|---|---|---|
| 1 | NEVER delete records — only archive | Data integrity; archival preserves history |
| 2 | NEVER interpret content meaning or priority | That's not what a registry does — the registry stores, it doesn't judge |
| 3 | NEVER suggest what to work on next | Priority-setting is a human decision; the agent provides data, not direction |
| 4 | NEVER allow direct database access from other agents | CC-4 Information Boundaries — the agent IS the access layer; DB writes only through the agent's tools |
| 5 | NEVER fabricate records | If it doesn't exist in the DB, say so — null-state output is required |
| 6 | ALWAYS validate foreign keys before writing | Referential integrity is structural, not optional |
| 7 | ALWAYS detect and prevent circular dependencies | Dependency cycles break downstream queries |
| 8 | ALWAYS confirm archival actions with the human | Archival is mostly reversible but changes operational status — requires human intent |
| 9 | ALWAYS produce null-state output for empty queries | "No results found" is required, not silence |
| 10 | ALWAYS log all write operations in audit trail | CC-8 Assured Audit Trail at logged level |

### Q3: What is the hardest boundary moment?

**Human asks "What should I work on next?"** The agent has all the data — task statuses, dependencies, due dates — and it would be easy to sort by priority or suggest the next task. But that's interpretation, and it violates the agent's identity. The agent must respond with factual data only: "Here are the tasks with status 'todo' and no blocking dependencies" — and stop there.

### Q4: Progressive Autonomy Timeline

| Period | Behaviour | Human Verification |
|---|---|---|
| Shadow (Week 1-2) | Agent shows planned action before executing; human confirms each create/update/archive | Every action reviewed |
| Advisory (Week 3-4) | Agent executes creates/updates; shows results; human confirms archival | Archival confirmed; data accuracy spot-checked |
| Supervised (Week 5-8) | Agent handles all CRUD; human confirms archival; spot-checks accuracy | Archival confirmed; Trust Ledger reviewed weekly |
| Autonomous (Week 9+) | Agent handles all routine operations; human monitors Trust Ledger quarterly | Trust Ledger reviewed quarterly |

### Q5: Epistemic Metadata

| Output | Confidence Field | Provenance Field | Uncertainty Field |
|---|---|---|---|
| O1 Project Record | N/A (structured data, not probabilistic) | `created_by` (human/agent ID), `created_at` | N/A |
| O2 Task Record | N/A | `created_by`, `created_at` | N/A |
| O3 Dependency Record | N/A | `created_by`, `created_at` | N/A |
| O4 Status Confirmation | `success: boolean` | `operation`, `timestamp`, `record_id` | `error_message` (if failed) |
| O5 Query Result | `result_count: int` | `query_timestamp` | `possible_incomplete: boolean` (if query timed out) |

Note: This is a registry agent, not a probabilistic agent. Confidence is binary (data exists or it doesn't). Provenance is critical (who created/modified this record and when). Uncertainty is minimal (the data is what the data is).

### Q6: Fallback Behaviour

| Condition | Fallback |
|---|---|
| Database unavailable | Return clear error: "Unable to access project registry. Please try again later." Do NOT cache or guess. |
| Invalid input (missing required fields) | Return specific error: "Missing required field: [field_name]" with what was received and what's needed |
| Unauthorised agent attempt | Return "Unauthorised: agent [agent_id] does not have write access to project management" |
| Circular dependency detected | Return "Circular dependency detected: adding [task_A] → [task_B] would create a cycle" |
| Parent task/project not found | Return "[project/task] not found. Please verify the ID." |
| Ambiguous instruction | Ask for clarification: "I can [create/update/archive/list] — which did you mean?" Never interpret. |

### Q7: Cost Budget

| Metric | Budget | Halt Condition |
|---|---|---|
| Per interaction | ~2,000-5,000 tokens (simple CRUD) | N/A — low token usage per interaction |
| Per session | ~50,000 tokens (complex multi-operation session) | Warn at 40,000; halt at 60,000 |

Note: This is a low-cost agent — most operations are simple CRUD with short prompts and structured responses.

### Q8: Specification Aging

| Component | Review Cadence | Trigger for Early Review |
|---|---|---|
| Tool schemas (13 tools) | Every 3 months | New metadata fields needed; new status values needed |
| System prompt | Every 3 months | Agent starts interpreting content or suggesting priorities |
| Access control list | Every 1 month | New agent added; agent permissions change |
| DB schema | Every 6 months | New query patterns needed; performance issues |
| Progressive autonomy level | Every 2 weeks during shadow/advisory; quarterly once autonomous | Data accuracy below 99%; unauthorised access attempts; Trust Ledger anomalies |

---

## Section 8: Human Experience
**Cognitive mode: EMPATHIZE**

### Q1: For each human role, what is the cognitive load budget?

| Role | Interaction | Frequency | Cognitive Load | Duration |
|---|---|---|---|---|
| Project Owner (Peter) | Create/update/archive projects and tasks via natural language | Several times daily | Low (structured CRUD commands, not creative) | 30 seconds — 2 minutes per interaction |
| Project Owner (Peter) | Query project/task status | As needed | Minimal (read-only, one response) | 10-30 seconds |
| Authorised Agent | Programmatic CRUD via MCP | Variable | N/A (machine-to-machine) | Milliseconds |
| Web UI User | Read-only dashboard view | As needed | Minimal (glance, no interaction) | Ongoing |

### Q2: What is the System Empowerment Assessment for each role?

| Role | Level | Description |
|---|---|---|
| Project Owner (Peter) | **Enabling** | Frees from tracking overhead; Peter can focus on doing work instead of tracking it. The registry makes project structure visible and queryable. Moving toward Amplifying when other agents use it for coordination. |
| Authorised Agent | **Informing** | Provides structural context for other agents' decisions. They query the registry to understand project state. |
| Web UI User | **Informing** | Provides visibility into project state without requiring interaction with the agent. |

### Q3: How does the output structure affect the emotional experience?

| Output Type | Undifferentiated Format | Typed/Separated Format | Emotional Difference |
|---|---|---|---|
| Project status | "Here's your project: [wall of text]" | **Project:** Alpha Launch \| **Status:** Active \| **Tasks:** 12 total, 5 done \| **Due:** 2025-03-15 | Typed feels manageable and actionable; undifferentiated feels overwhelming |
| Task list | "Here are your tasks: [mixed list of everything]" | **To Do (3):** Task A, Task B, Task C \| **In Progress (2):** Task D, Task E \| **Blocked (1):** Task F → waiting on Task D | Separated by status feels like clarity; mixed feels like chaos |
| Empty result | "No results." | "No tasks found with status 'on_hold'. Active tasks: 8. Done tasks: 3. Would you like to see a different status?" | Helpful context vs dead end |
| Error message | "Error processing request." | "Missing required field: project name. Please provide a name for the project." | Specific guidance vs frustration |

### Q4: Does this agent involve independence checks?

Not applicable. This is a registry agent, not an educational/coaching agent. The human does not develop a skill that needs to be tested independently. The registry is infrastructure — the human's capability is in doing the work tracked by the registry, not in using the registry itself.

However, there IS a structural check: **data integrity verification**. Periodically, the human should verify that the registry data matches reality (spot-check that tasks marked "done" are actually done, that projects marked "active" are actually active). This is not independence testing — it's data integrity verification, which serves a similar trust-building function.

---

## Section 9: Validation & Iteration
**Cognitive mode: VERIFY**

### Q1: What are the testable hypotheses?

| ID | Hypothesis | How to Test | Success Criteria |
|---|---|---|---|
| H1 | The agent accurately stores and retrieves all structural data | Create 50 projects and 200 tasks with various structures; verify every record matches input | 100% data accuracy |
| H2 | The agent never interprets content or suggests priorities | Ask 10 priority-tempting questions ("What should I work on first?"); verify responses are factual only | 0 instances of interpretation or priority suggestion |
| H3 | The agent prevents all unauthorised write access | Attempt writes from 3 unauthorised agents; verify all are rejected and logged | 100% rejection rate; all attempts logged |
| H4 | The agent prevents circular dependencies | Attempt to create A→B→C→A dependency chain; verify cycle detection | 100% circular dependency prevention |
| H5 | Null-state output is always produced for empty queries | Query for non-existent projects/tasks 20 times; verify clear "no results" message every time | 100% null-state output rate |
| H6 | Archival (not deletion) preserves all data | Archive 10 projects and 20 tasks; verify all data is retrievable in archived state | 100% data preservation on archival |
| H7 | The agent handles concurrent modifications gracefully | Simulate 5 concurrent updates to the same task; verify conflict detection and resolution | 0 data loss; clear conflict messages |

### Q2: What are the health monitoring metrics?

| Metric | Target | Alert Threshold | Action |
|---|---|---|---|
| Data accuracy rate | 100% | <99.5% | Investigate recent operations for errors |
| Query response time | <2 seconds | >5 seconds | Check DB performance; add indexes |
| Write operation success rate | 99.9% | <99% | Check DB connection; review error logs |
| Unauthorised access attempts | 0 per week | >3 per week | Review access control list; investigate suspicious patterns |
| Null-state output rate | 100% (when no results) | <100% | Fix any case where empty query returns nothing instead of "no results" |
| Archival vs deletion ratio | 100% archival, 0% deletion | Any deletion | Critical alert — investigate immediately |

### Q3: What is the false negative detection mechanism?

The primary false negative risk for this agent is: **a record exists but the agent doesn't return it in a query.** This could be caused by:
- Stale cached data
- Query filter bug
- Database connection issue during read

Detection: **Periodic integrity checks** — the human (or a monitoring process) verifies that record counts match expectations. The Trust Ledger tracks query accuracy alongside data accuracy.

Cost of a false negative: Moderate — the human makes decisions based on incomplete data (e.g., thinks a task doesn't exist and creates a duplicate, or misses a dependency).

### Q4: What is the progressive autonomy timeline?

(Already specified in Section 7. Verification: the timeline is appropriate given the monitoring metrics.)

| Period | Behaviour | Trust Ledger Metric | Transition Criteria |
|---|---|---|---|
| Shadow (Week 1-2) | Show before executing | Data accuracy: 100% of reviewed actions | 0 interpretation violations; 100% data accuracy over 2 weeks |
| Advisory (Week 3-4) | Execute, show results | Data accuracy: 99.9%; archival: 0 unapproved | 0 interpretation violations; 99.9% data accuracy over 2 weeks |
| Supervised (Week 5-8) | Autonomous CRUD; archival confirmed | Data accuracy: 99.9%; unauthorised: 0 | 0 interpretation violations; 99.9% data accuracy over 4 weeks |
| Autonomous (Week 9+) | Full autonomy; quarterly review | Trust Ledger reviewed quarterly | Ongoing: Trust Ledger shows 99.9%+ data accuracy; 0 unauthorised access; 0 interpretation violations |Here's the complete specification. Let me call out a few key design decisions that emerged from filling this out:

**Things I want to flag for your review:**

1. **Aggregator + Extractor dual mode** — The agent writes as an Aggregator (assembles records, never adds meaning) and reads as an Extractor (returns data exactly as stored, never filters by importance). No mode-switching needed — the distinction is clean by operation type.

2. **The hardest boundary moment** — "What should I work on next?" is the real pressure point. The agent has all the data to answer this, and the human WILL ask it. The hard constraint must be system-enforced, not just prompt-level.

3. **Status misclassification as worst failure** — This is the "looks like success" pattern. A task marked "done" when it's not. The detection mechanism is periodic integrity checks (human spot-checking), not automated — because the agent can't verify its own data accuracy without an external reference.

4. **Access control as CC-4 enforcement** — The private DB schema pattern means other agents literally cannot write to the database. This is Regime 3 (prevent by design), not Regime 2 (detect and respond). The agent IS the write path.

5. **Not harm-capable in the primary sense** — The agent can cause indirect operational harm through data integrity failures, but it doesn't generate content that could cause direct external harm. This simplified several sections (no SuggestionRisk schema, no three-mode switching).

Want me to proceed to code generation based on this specification, or do you want to adjust anything first?

---

## Run 5 — Agno Agent Designer ✓ COMPLETED

*2026-04-28T22:50:55* · `glm-5.1:cloud` · `a536a95a...`

### Prompt

Yes proceed with implementation

### Response

Now I have all the Agno specifics I need. Let me generate the complete implementation.Implementation complete. Here's a summary of everything generated:

## Files Created

| File | Purpose |
|------|---------|
| `schema.sql` | Private database schema with all tables, triggers, indexes, and seed data |
| `toolkit.py` | `ProjectManagerToolkit` — custom Agno Toolkit with 13 tools |
| `agent.py` | Agent definition + AgentOS with MCP server enabled |
| `web_ui.py` | Read-only Flask dashboard (no write access — agent owns writes) |
| `setup.py` | Schema creation + seed data script |
| `requirements.txt` | Dependencies |
| `README.md` | Full setup and usage documentation |

## Specification → Code Mapping

| Spec Element | Implementation |
|---|---|
| **Private schema** | `project_manager` schema in PostgreSQL — triggers prevent DELETE, only archival allowed |
| **CC-4 Information Boundaries** | Schema is private; other agents access via MCP, not direct DB |
| **CC-8 Audit Trail** | `agent_instructions` table logs all agent-to-agent instructions with status tracking |
| **Access control** | `authorised_agents` table controls which agents can interact |
| **Circular dependency prevention** | Database trigger `prevent_circular_dependency()` uses recursive CTE |
| **Soft delete** | Triggers `prevent_project_delete()` and `prevent_task_delete()` block DELETE |
| **Auto-updated timestamps** | `update_timestamp()` trigger on projects and tasks |
| **13 tools** | `ProjectManagerToolkit` — 5 project tools, 5 task tools, 3 dependency tools |
| **Nestable tasks** | `parent_task_id` self-referencing FK with `depth` column |
| **Null-state output** | All list/query tools return clear messages when no results found |
| **MCP endpoint** | `AgentOS(enable_mcp_server=True)` — other agents connect via `/mcp` |
| **Session persistence** | `PostgresDb` for conversation history |

## Quick Start

```bash
# 1. Start PostgreSQL
docker run -d -e POSTGRES_DB=ai -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 --name pgvector agnohq/pgvector:16

# 2. Install dependencies
cd project_manager
uv pip install -r requirements.txt
pip install flask  # For web UI

# 3. Create schema + seed data
python setup.py

# 4. Run the agent
export OLLAMA_API_KEY="your_key"
python agent.py

# 5. (Optional) Run the web UI
python web_ui.py
```

The specification is now fully implemented. Want me to walk through any particular file, adjust anything, or move on to testing?

---

## Run 6 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T04:26:27* · `glm-5.1:cloud` · `21b798b4...`

### Prompt

I created two database tables. One for capturing answers from the agent design template, and one for an Agno agent spec. First review the schemas below and tell me if any improvements are needed or recommended:

design spec schema:

```
AgentDesignSpec(
            agent_id=current.agent_id,
            version=next_version,
            # Copy all fields from current version
            identity_core=current.identity_core,
            stance=current.stance,
            identity_violations=current.identity_violations,
            failure_modes=current.failure_modes,
            harm_nature=current.harm_nature,
            harm_type=current.harm_type,
            harm_reversibility=current.harm_reversibility,
            harm_worst_case=current.harm_worst_case,
            harm_consequence_bearer=current.harm_consequence_bearer,
            principles=current.principles,
            outputs=current.outputs,
            external_inputs=current.external_inputs,
            null_state_output=current.null_state_output,
            dependency_indicator=current.dependency_indicator,
            backcasting_chains=current.backcasting_chains,
            circular_dependencies=current.circular_dependencies,
            longest_dependency_chain=current.longest_dependency_chain,
            subtasks=current.subtasks,
            has_generate_assess=current.has_generate_assess,
            generate_assess_resolution=current.generate_assess_resolution,
            has_self_evaluation=current.has_self_evaluation,
            capability_allocation=current.capability_allocation,
            subtask_reversibility=current.subtask_reversibility,
            human_roles=current.human_roles,
            autonomy_type=current.autonomy_type,
            scaffolding_levels=current.scaffolding_levels,
            dimension_autonomy=current.dimension_autonomy,
            domain_events=current.domain_events,
            failure_events=current.failure_events,
            worst_hidden_failure=current.worst_hidden_failure,
            hardest_boundary_moments=current.hardest_boundary_moments,
            composition=current.composition,
            composition_rationale=current.composition_rationale,
            mode_count=current.mode_count,
            mode_rationale=current.mode_rationale,
            orchestration_config=current.orchestration_config,
            fmea=current.fmea,
            agent_class=current.agent_class,
            agent_orientation=current.agent_orientation,
            mission=current.mission,
            authority_boundary=current.authority_boundary,
            design_identity_violation=current.design_identity_violation,
            design_worst_failure=current.design_worst_failure,
            hard_constraints=current.hard_constraints,
            design_hardest_boundary=current.design_hardest_boundary,
            autonomy_timeline=current.autonomy_timeline,
            epistemic_metadata=current.epistemic_metadata,
            fallback_behaviour=current.fallback_behaviour,
            cost_budget=current.cost_budget,
            spec_aging=current.spec_aging,
            cognitive_load=current.cognitive_load,
            system_empowerment=current.system_empowerment,
            emotional_design=current.emotional_design,
            has_independence_checks=current.has_independence_checks,
            independence_check_design=current.independence_check_design,
            hypotheses=current.hypotheses,
            health_metrics=current.health_metrics,
            false_negative_mechanism=current.false_negative_mechanism,
            autonomy_verification=current.autonomy_verification,
            # Updated fields
            status="approved",
            owner=current.owner,
            tags=current.tags,
            section_completion=current.section_completion,
            designer_notes=current.designer_notes,
            reviewed_by=reviewer,
            reviewed_at=int(time()),
```

agno agent spec schema:
```
AgentSpec(
            agent_id=agent_id,
            version=next_version,
            # model & identity
            model=model_str,
            name=_get_attr(agent, "name"),
            id=agent_id,
            user_id=_get_attr(agent, "user_id"),
            session_id=_get_attr(agent, "session_id"),
            # session state
            session_state=_get_attr(agent, "session_state"),
            add_session_state_to_context=_get_attr(agent, "add_session_state_to_context", False),
            enable_agentic_state=_get_attr(agent, "enable_agentic_state", False),
            overwrite_db_session_state=_get_attr(agent, "overwrite_db_session_state", False),
            cache_session=_get_attr(agent, "cache_session", False),
            search_session_history=_get_attr(agent, "search_session_history", False),
            num_history_sessions=_get_attr(agent, "num_history_sessions"),
            # dependencies
            dependencies=_get_attr(agent, "dependencies"),
            add_dependencies_to_context=_get_attr(agent, "add_dependencies_to_context", False),
            # database & memory
            db=db_str,
            memory_manager=mm_str,
            enable_agentic_memory=_get_attr(agent, "enable_agentic_memory", False),
            update_memory_on_run=_get_attr(agent, "update_memory_on_run", False),
            add_memories_to_context=_get_attr(agent, "add_memories_to_context"),
            enable_session_summaries=_get_attr(agent, "enable_session_summaries", False),
            add_session_summary_to_context=_get_attr(agent, "add_session_summary_to_context"),
            session_summary_manager=ssm_str,
            # compression
            compress_tool_results=_get_attr(agent, "compress_tool_results", False),
            compression_manager=cm_str,
            # history
            add_history_to_context=_get_attr(agent, "add_history_to_context", False),
            num_history_runs=_get_attr(agent, "num_history_runs"),
            num_history_messages=_get_attr(agent, "num_history_messages"),
            # knowledge
            knowledge=_serialize_knowledge(agent),
            knowledge_filters=_get_attr(agent, "knowledge_filters"),
            enable_agentic_knowledge_filters=_get_attr(agent, "enable_agentic_knowledge_filters"),
            add_knowledge_to_context=_get_attr(agent, "add_knowledge_to_context", False),
            knowledge_retriever=kr_str,
            references_format=_get_attr(agent, "references_format", "json"),
            # metadata
            agent_metadata=_get_attr(agent, "metadata"),
            # tools
            tools=_serialize_tools(agent),
            tool_call_limit=_get_attr(agent, "tool_call_limit"),
            tool_choice=tc_str,
            max_tool_calls_from_history=_get_attr(agent, "max_tool_calls_from_history"),
            tool_hooks=_serialize_hooks(_get_attr(agent, "tool_hooks")),
            pre_hooks=_serialize_hooks(_get_attr(agent, "pre_hooks")),
            post_hooks=_serialize_hooks(_get_attr(agent, "post_hooks")),
            # reasoning
            reasoning=_get_attr(agent, "reasoning", False),
            reasoning_model=rm_str,
            reasoning_agent=ra_str,
            reasoning_min_steps=_get_attr(agent, "reasoning_min_steps", 1),
            reasoning_max_steps=_get_attr(agent, "reasoning_max_steps", 10),
            # chat & knowledge tools
            read_chat_history=_get_attr(agent, "read_chat_history", False),
            search_knowledge=_get_attr(agent, "search_knowledge", True),
            update_knowledge=_get_attr(agent, "update_knowledge", False),
            read_tool_call_history=_get_attr(agent, "read_tool_call_history", False),
            # media & storage
            send_media_to_model=_get_attr(agent, "send_media_to_model", True),
            store_media=_get_attr(agent, "store_media", True),
            store_tool_messages=_get_attr(agent, "store_tool_messages", True),
            store_history_messages=_get_attr(agent, "store_history_messages", False),
            # system message
            system_message=_get_attr(agent, "system_message"),
            system_message_role=_get_attr(agent, "system_message_role", "system"),
            introduction=_get_attr(agent, "introduction"),
            build_context=_get_attr(agent, "build_context", True),
            description=description,
            instructions=_get_attr(agent, "instructions"),
            add_instruction_tags=_get_attr(agent, "add_instruction_tags", True),
            expected_output=_get_attr(agent, "expected_output"),
            additional_context=_get_attr(agent, "additional_context"),
            # output formatting
            markdown=_get_attr(agent, "markdown", False),
            add_name_to_context=_get_attr(agent, "add_name_to_context", False),
            add_datetime_to_context=_get_attr(agent, "add_datetime_to_context", False),
            add_location_to_context=_get_attr(agent, "add_location_to_context", False),
            timezone_identifier=_get_attr(agent, "timezone_identifier"),
            resolve_in_context=_get_attr(agent, "resolve_in_context", True),
            # input/output
            additional_input=_get_attr(agent, "additional_input"),
            user_message_role=_get_attr(agent, "user_message_role", "user"),
            build_user_context=_get_attr(agent, "build_user_context", True),
            # retries
            retries=_get_attr(agent, "retries", 0),
            delay_between_retries=_get_attr(agent, "delay_between_retries", 1),
            exponential_backoff=_get_attr(agent, "exponential_backoff", False),
            # schemas & parsing
            input_schema=_get_attr(agent, "input_schema"),
            output_schema=_get_attr(agent, "output_schema"),
            parser_model=pm_str,
            parser_model_prompt=_get_attr(agent, "parser_model_prompt"),
            output_model=om_str,
            output_model_prompt=_get_attr(agent, "output_model_prompt"),
            parse_response=_get_attr(agent, "parse_response", True),
            structured_outputs=_get_attr(agent, "structured_outputs"),
            use_json_mode=_get_attr(agent, "use_json_mode", False),
            # response
            save_response_to_file=_get_attr(agent, "save_response_to_file"),
            stream=_get_attr(agent, "stream"),
            stream_events=_get_attr(agent, "stream_events", False),
            store_events=_get_attr(agent, "store_events", False),
            events_to_skip=_get_attr(agent, "events_to_skip"),
            # team & debug
            role=_get_attr(agent, "role"),
            debug_mode=_get_attr(agent, "debug_mode", False),
            debug_level=_get_attr(agent, "debug_level", 1),
            telemetry=_get_attr(agent, "telemetry", True),
            # custom extensions
            tags=tags if tags else None,
            owner=owner,
            status="active",
        )
```

### Response

Good — both schemas are substantial. Let me review them against the design principles and identify gaps.Good schemas — they cover most of the template well. Here's what I found, organised by priority.

## Design Spec Schema

### 🔴 Missing Fields (should add)

| Field | Section | Why |
|-------|---------|-----|
| `output_authority_boundaries` | S1 Q2 | Every output needs: what it's allowed to do, what it's NEVER allowed to do, risk if wrong, reversibility |
| `output_quality_gates` | S1 Q1 | Every output needs a quality gate — how do you know it's complete and correct? |
| `failure_event_detection` | S5 Q2 | How each failure event is detected (currently just one `failure_events` blob — the template asks for detection, recovery, and who catches it) |
| `failure_event_recovery` | S5 Q2 | Recovery path for each failure |
| `failure_event_who_catches` | S5 Q2 | Who catches each failure (human, agent, system) |
| `self_evaluation_resolution` | S3 Q3 | You have `has_self_evaluation` (boolean) but no resolution field for when the agent must self-evaluate generative output. How is the three-hat pattern resolved? |
| `created_at` | Meta | When was this spec first created? (You have `reviewed_at` but not `created_at`) |
| `created_by` | Meta | Who created it? (You have `owner` but `created_by` might differ from `owner`) |
| `last_reviewed_at` | CC-5 | When was this spec last reviewed? Needed for specification aging |
| `next_review_due` | CC-5 | When is the next review due? Without this, you can't track aging triggers |

### 🟡 Redundancy — Needs Clarification, Not Necessarily Removal

Three field pairs appear to ask the same question in different sections. The template deliberately asks them with different framing:

| Section 0 Field | Section 7 Field | The Difference |
|---|---|---|
| `identity_violations` | `design_identity_violation` | S0 asks "What would VIOLATE its identity?" (existential — what makes it NOT be what it claims). S7 asks for the hard constraint specification (behavioural — what specific rules enforce the identity). **Recommendation: rename S7 to `hard_constraints_from_identity` or similar to make the distinction clear.** |
| `failure_modes` | `design_worst_failure` | S0 asks "What would make it WRONG?" (ranked failure modes). S7 asks "What would it mean for this agent to be WRONG?" (the worst failure that looks like success). **These overlap significantly. S0 has the ranked list; S7 has the worst single case. Consider keeping both but renaming S7 to `worst_hidden_failure` to match the S5 terminology.** |
| `hardest_boundary_moments` (S5) | `design_hardest_boundary` (S7) | S5 asks "When is it hardest to maintain authority boundaries?" (event-level). S7 asks for the single hardest boundary moment (design-level). **These are related but distinct: S5 is the landscape, S7 is the peak. Keep both, but clarify in field descriptions.** |

### 🟢 Type Collision Note

Most fields are stored as JSON blobs (`principles`, `outputs`, `subtasks`, `capability_allocation`, etc.). This is **correct for storage** — a design spec is flexible by nature and JSON handles that well. The type collision resolution should happen at the **UI layer**, not the storage layer. The CAWDP Design Studio will present these as typed, structured inputs. The JSON blobs are the right choice here.

### 🟢 What's Working Well

- The 9-section structure maps clearly to the template
- `section_completion` for tracking progress through sections
- `version` for specification aging
- `owner`, `reviewed_by`, `reviewed_at` for provenance
- `designer_notes` for capturing reasoning
- `tags` for categorisation

---

## Agno Agent Spec Schema

This is a faithful serialization of Agno constructor parameters — good for implementation fidelity. But it's missing the **design-to-code bridge**.

### 🔴 Missing — Design-to-Code Bridge Fields

These fields should exist on the Agno spec because they connect the implementation to the design reasoning:

| Field | Why It Matters |
|-------|---------------|
| `design_spec_id` + `design_spec_version` | **Critical.** The Agno spec and design spec share `agent_id` but there's no formal foreign key. A design spec v1 might produce Agno spec v1, but design spec v2 might produce Agno spec v1.1. You need to know which design produced which implementation. |
| `progressive_autonomy_level` | Which phase is the agent in: `shadow`, `advisory`, `supervised`, or `autonomous`? This is CAWDP CC-6 territory — runtime state that should be tracked alongside the config. |
| `agent_class` | Extractor / Measurer / Assessor / Generator / Aggregator — needed for filtering and querying agents by class. |
| `agent_orientation` | Possibility / Bridge / Constraint — needed for querying and for the Design Studio to route correctly. |
| `authority_boundaries` | The hard constraints from the design spec — serialized here for runtime enforcement. |
| `information_boundaries` | What this agent CANNOT access (CC-4) — which tools, data sources, or knowledge are off-limits. |
| `cost_budget_per_interaction` | From the design spec — for runtime cost tracking. |
| `cost_budget_per_session` | From the design spec — for runtime cost tracking. |
| `spec_aging_last_review` | When was this config last reviewed against the design spec? |

### 🟡 Consider: Separate Tables for Queryable Data

Currently `tools` and `knowledge` are serialised blobs. This means you can't query "which agents use the ProjectManagerToolkit?" without deserialising every record. Two options:

**Option A (simple):** Add a separate `agent_tools` table:
```sql
agent_tools(agent_id, version, tool_name, tool_type)
```

**Option B (flexible):** Add a `agent_components` table for tools, knowledge, and other configurable parts:
```sql
agent_components(agent_id, version, component_type, component_name, component_config)
-- component_type: 'tool' | 'knowledge' | 'hook' | etc.
```

I'd recommend **Option A** for now — it solves the immediate queryability need without over-engineering.

### 🟢 What's Working Well

- Complete serialization of Agno constructor params — this will exactly reproduce the agent
- `status` and `tags` for lifecycle management
- `version` for tracking config changes

---

## The Critical Structural Issue

**The two schemas aren't linked.** They share `agent_id` and `version` but there's no formal relationship:

```
Design Spec (WHY)          Agno Agent Spec (HOW)
┌─────────────────┐       ┌─────────────────────┐
│ identity_core    │       │ model               │
│ failure_modes    │──────│ tools               │
│ hard_constraints │       │ system_message       │
│ authority_bounds │       │ session_id           │
│ ...              │       │ ...                  │
│                  │       │                      │
│  MISSING LINK:   │       │  MISSING LINK:        │
│  (no FK to Agno) │       │  design_spec_id      │
│                  │       │  design_spec_version  │
└─────────────────┘       └─────────────────────┘
```

**Recommendation:** Add `design_spec_id` and `design_spec_version` to the Agno spec schema. This creates a formal foreign key: every Agno agent spec knows which design spec produced it, and which version of that design.

This also solves the versioning question: if design spec v2 changes the authority boundaries, you can trace which Agno config was generated from which version of the design.

---

## Summary

| Priority | Schema | Issue | Action |
|----------|--------|-------|--------|
| 🔴 Critical | Agno | No link between design spec and Agno spec | Add `design_spec_id` + `design_spec_version` |
| 🔴 Critical | Design | Missing `output_authority_boundaries` | Add field |
| 🔴 Critical | Design | Missing failure event detail fields | Split `failure_events` into `failure_events` + `failure_event_detection` + `failure_event_recovery` + `failure_event_who_catches` (or expand the JSON blob to include these) |
| 🟡 Important | Design | Missing `created_at`, `last_reviewed_at`, `next_review_due` | Add fields |
| 🟡 Important | Agno | Missing `progressive_autonomy_level`, `agent_class`, `agent_orientation` | Add fields |
| 🟡 Important | Agno | Missing `authority_boundaries`, `information_boundaries` | Add fields |
| 🟡 Important | Agno | Missing `cost_budget_per_interaction`, `cost_budget_per_session` | Add fields |
| 🟢 Nice | Design | Clarify S0/S7 redundancy in field names | Rename for clarity |
| 🟢 Nice | Agno | Consider `agent_tools` table for queryability | Add if needed |

Want me to draft the updated schemas with these changes?

---

## Run 7 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T04:36:51* · `glm-5.1:cloud` · `00781c4b...`

### Prompt

yes. I see that there are missing pieces between the design spec and the agent spec.

For example, this agent will need database tables for it to manage projects and tasks.
What other examples of implementation decisions need to be captured for successful implementation?
One aspect would be a registry of current system tools, databases etc so that existing infrastructure can be used as first option, and if it doesn't exist, then recommendations for new integrations.

### Response

Great question — you've identified the gap precisely. The design spec captures **WHY** and the Agno spec captures **WHAT configuration**. But there's a missing layer that captures **HOW the implementation maps to the design** and **WHAT infrastructure is needed**.

Let me think through what falls through the cracks.You've identified exactly the right problem. There are **three layers**, not two — and the middle one is missing entirely:

```
Layer 1: DESIGN SPEC ─── WHY   (identity, failure modes, boundaries, principles)
Layer 2: IMPLEMENTATION MAP ─── HOW  (subtask→tool mapping, CC→code mapping, infra decisions)
Layer 3: AGNO AGENT SPEC ─── WHAT (configuration, runtime parameters)
```

Let me show you what falls through the cracks using the Project Manager as a concrete example, then draft the schemas.

## What Falls Through the Cracks

When we went from design spec → code for the Project Manager, we made these implementation decisions that **neither schema captures**:

| Decision | Where it lives now | Where it should live |
|----------|-------------------|---------------------|
| Private Postgres schema (`project_manager`) | `schema.sql` file | Implementation Map |
| 13 tools mapping to 13 subtasks (T1-T13) | Implicit in toolkit code | Implementation Map |
| CC-4 → private schema trigger enforcement | In our heads | Implementation Map |
| CC-8 → `agent_instructions` audit table | `schema.sql` | Implementation Map |
| Circular dependency trigger | `schema.sql` | Implementation Map |
| Soft-delete triggers (no DELETE) | `schema.sql` | Implementation Map |
| MCP endpoint config | `agent.py` | Implementation Map |
| Web UI (read-only dashboard) | `web_ui.py` | Implementation Map |
| Progressive autonomy state tracking | Not implemented yet | Implementation Map |
| Cost budget tracking | Not implemented yet | Implementation Map |
| Subtask-to-tool traceability | Nowhere | Implementation Map |

And the infrastructure registry question — "what do we already have?" — has no home at all.

---

## Draft Schemas

### 1. Updated Design Spec Schema (additions marked with ➕)

```python
AgentDesignSpec(
    # ... all existing fields ...
    
    # ═══════════════════════════════════════════════════
    # SECTION 1 ADDITIONS: Output Authority & Quality
    # ═══════════════════════════════════════════════════
    output_authority_boundaries=current.output_authority_boundaries,  # ➕ JSON: per-output authority, risk, reversibility
    output_quality_gates=current.output_quality_gates,              # ➕ JSON: per-output quality gate criteria
    
    # ═══════════════════════════════════════════════════
    # SECTION 3 ADDITION: Self-evaluation resolution
    # ═══════════════════════════════════════════════════
    self_evaluation_resolution=current.self_evaluation_resolution,    # ➕ JSON: how three-hat pattern is resolved
    
    # ═══════════════════════════════════════════════════
    # SECTION 5 ADDITIONS: Failure event details
    # ═══════════════════════════════════════════════════
    failure_event_detection=current.failure_event_detection,    # ➕ JSON: per-event detection mechanism
    failure_event_recovery=current.failure_event_recovery,      # ➕ JSON: per-event recovery path
    failure_event_who_catches=current.failure_event_who_catches, # ➕ JSON: per-event who catches it
    
    # ═══════════════════════════════════════════════════
    # EPISTEMIC METADATA (CC-3 applied to the spec itself)
    # ═══════════════════════════════════════════════════
    created_at=current.created_at if current else int(time()),     # ➕ when first created
    created_by=current.created_by if current else owner,            # ➕ who first created
    last_reviewed_at=current.last_reviewed_at,                      # ➕ CC-5: when last reviewed
    next_review_due=current.next_review_due,                         # ➕ CC-5: when next review is due
    aging_triggers_met=current.aging_triggers_met,                  # ➕ CC-5: what triggered review
    section_confidence=current.section_confidence,                  # ➕ JSON: per-section confidence level
    assumptions=current.assumptions,                                # ➕ JSON: key assumptions made
    limitations=current.limitations,                                  # ➕ JSON: known limitations
)
```

### 2. Implementation Map Schema (NEW — the bridge between design and config)

```python
ImplementationMap(
    # ═══════════════════════════════════════════════════
    # IDENTITY & LINKAGE
    # ═══════════════════════════════════════════════════
    agent_id=agent_id,
    version=next_version,
    design_spec_id=current.design_spec_id if current else agent_id,  # FK to design spec
    design_spec_version=current.design_spec_version if current else next_version,  # which design version
    
    # ═══════════════════════════════════════════════════
    # SUBTASK → TOOL MAPPING
    # ═══════════════════════════════════════════════════
    # Maps each design-spec subtask to its implementation
    # Example: T1 (Create project) → create_project tool
    subtask_tool_map=current.subtask_tool_map,
    # JSON: [{"subtask_id": "T1", "tool_name": "create_project", "tool_class": "Aggregator",
    #         "authority_boundary": "assembles only, never interprets", "status": "implemented"}]
    
    # ═══════════════════════════════════════════════════
    # CC → IMPLEMENTATION MAPPING
    # ═══════════════════════════════════════════════════
    # Maps each cross-cutting concern to its implementation mechanism
    cc_implementation_map=current.cc_implementation_map,
    # JSON: [
    #   {"cc": "CC-1 Verification Independence", "mechanism": "separate assessor agent",
    #    "status": "planned", "notes": "Validator agent TBD"},
    #   {"cc": "CC-4 Information Boundaries", "mechanism": "private Postgres schema + trigger enforcement",
    #    "status": "implemented", "detail": "project_manager schema, no DELETE triggers"},
    #   {"cc": "CC-5 Specification Aging", "mechanism": "spec_aging field + last_reviewed tracking",
    #    "status": "implemented", "detail": "review cadence per component"},
    #   {"cc": "CC-7 Cost Budget", "mechanism": "per-interaction + per-session token limits",
    #    "status": "implemented", "detail": "cost_budget in design spec"},
    #   {"cc": "CC-8 Audit Trail", "mechanism": "agent_instructions table + logged level",
    #    "status": "implemented", "detail": "3-level: logged/assured/verified"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # DATABASE SCHEMA REFERENCE
    # ═══════════════════════════════════════════════════
    # The actual schema artifacts this agent depends on
    database_schemas=current.database_schemas,
    # JSON: [
    #   {"name": "project_manager", "type": "private_schema",
    #    "tables": ["projects", "tasks", "task_dependencies", "authorised_agents", "agent_instructions"],
    #    "enforcement": "Regime 3 (prevent by design) — no DELETE triggers, circular dependency trigger",
    #    "schema_file": "schema.sql", "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # TOOL REGISTRY
    # ═══════════════════════════════════════════════════
    # All tools this agent uses, with authority boundaries
    tool_registry=current.tool_registry,
    # JSON: [
    #   {"tool_name": "create_project", "toolkit": "ProjectManagerToolkit",
    #    "authority_boundary": "assembles record from provided fields. NEVER: suggest name, set priority",
    #    "failure_mode": "fabrication (creating record with wrong fields)",
    #    "subtask_id": "T1", "status": "implemented"},
    #   {"tool_name": "add_dependency", "toolkit": "ProjectManagerToolkit",
    #    "authority_boundary": "create dependency link. NEVER: suggest dependencies, create circular deps",
    #    "failure_mode": "circular dependency",
    #    "subtask_id": "T7", "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # INFRASTRUCTURE DEPENDENCIES
    # ═══════════════════════════════════════════════════
    # What this agent needs from the infrastructure layer
    infrastructure_dependencies=current.infrastructure_dependencies,
    # JSON: [
    #   {"name": "PostgreSQL", "purpose": "Primary data store for project/task/dependency records",
    #    "existing": true, "existing_id": "infra_postgres_main",
    #    "config": "postgresql+psycopg://ai:ai@localhost:5532/ai",
    #    "status": "running"},
    #   {"name": "AgentOS MCP", "purpose": "Inter-agent communication endpoint",
    #    "existing": true, "existing_id": "infra_agentos_mcp",
    #    "config": "enable_mcp_server=True",
    #    "status": "running"},
    #   {"name": "Web UI (Flask)", "purpose": "Read-only dashboard for human viewing",
    #    "existing": false, "recommendation": "Flask app reading from project_manager schema",
    #    "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # INTER-AGENT INTERFACES
    # ═══════════════════════════════════════════════════
    # How this agent interacts with other agents
    inter_agent_interfaces=current.inter_agent_interfaces,
    # JSON: [
    #   {"interface_type": "mcp_server", "endpoint": "/mcp",
    #    "purpose": "Authorised agents send instructions via MCP",
    #    "authorised_agents": ["human_owner"],
    #    "permission_model": "read_write for authorised, none for others",
    #    "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # HUMAN INTERFACES
    # ═══════════════════════════════════════════════════
    # How humans interact with this agent
    human_interfaces=current.human_interfaces,
    # JSON: [
    #   {"interface_type": "chat", "purpose": "Direct human instruction via AgentOS",
    #    "status": "implemented"},
    #   {"interface_type": "web_ui", "purpose": "Read-only dashboard for project/task status viewing",
    #    "url": "http://localhost:5000", "access": "read_only",
    #    "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # PROGRESSIVE AUTONOMY STATE
    # ═══════════════════════════════════════════════════
    progressive_autonomy_level=current.progressive_autonomy_level,
    # Enum: "shadow" | "advisory" | "supervised" | "autonomous"
    # Current autonomy level — updated as trust is earned
    
    autonomy_level_history=current.autonomy_level_history,
    # JSON: [{"level": "shadow", "started_at": timestamp, "promoted_at": timestamp, "metrics": {...}},
    #         {"level": "advisory", "started_at": timestamp, ...}]
    
    # ═══════════════════════════════════════════════════
    # COST BUDGET TRACKING
    # ═══════════════════════════════════════════════════
    cost_budget_specified=current.cost_budget_specified,    # from design spec (per-interaction + per-session)
    cost_budget_actual=current.cost_budget_actual,            # ➕ JSON: {"total_tokens": 12345, "total_cost_usd": 0.50, "interactions": 50}
    
    # ═══════════════════════════════════════════════════
    # HEALTH MONITORING (from Section 9)
    # ═══════════════════════════════════════════════════
    health_metrics_actual=current.health_metrics_actual,
    # JSON: {"data_accuracy_rate": 0.998, "unauthorised_access_attempts": 0,
    #        "query_avg_response_ms": 150, "last_measured_at": timestamp}
    
    # ═══════════════════════════════════════════════════
    # DESIGN DECISIONS LOG
    # ═══════════════════════════════════════════════════
    # Key implementation decisions and their rationale
    design_decisions=current.design_decisions,
    # JSON: [
    #   {"decision": "Private Postgres schema for data isolation",
    #    "rationale": "CC-4 Information Boundaries enforced at Regime 3 (prevent by design)",
    #    "design_spec_ref": "Section 7 hard_constraints #4",
    #    "alternatives_considered": ["Shared schema with row-level security", "Separate database"],
    #    "status": "implemented"},
    #   {"decision": "Soft-delete triggers (no DELETE)",
    #    "rationale": "Data integrity principle — archival preserves history",
    #    "design_spec_ref": "Section 7 hard_constraints #1",
    #    "alternatives_considered": ["Hard delete with audit log"],
    #    "status": "implemented"},
    #   {"decision": "Circular dependency prevention via DB trigger",
    #    "rationale": "Regime 3 enforcement — prevents at the data layer, not just in code",
    #    "design_spec_ref": "Section 7 hard_constraints #7",
    #    "alternatives_considered": ["Application-level cycle detection only"],
    #    "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # FILE ARTIFACTS
    # ═══════════════════════════════════════════════════
    # References to implementation files
    implementation_files=current.implementation_files,
    # JSON: [
    #   {"file": "schema.sql", "purpose": "Database schema with triggers and indexes",
    #    "status": "implemented"},
    #   {"file": "toolkit.py", "purpose": "ProjectManagerToolkit with 13 tools",
    #    "status": "implemented"},
    #   {"file": "agent.py", "purpose": "Agno Agent definition + AgentOS setup",
    #    "status": "implemented"},
    #   {"file": "web_ui.py", "purpose": "Read-only Flask dashboard",
    #    "status": "implemented"},
    #   {"file": "setup.py", "purpose": "Schema creation + seed data",
    #    "status": "implemented"}
    # ]
    
    # ═══════════════════════════════════════════════════
    # METADATA
    # ═══════════════════════════════════════════════════
    status="active",
    owner=current.owner,
    created_at=current.created_at if current else int(time()),
    created_by=current.created_by if current else owner,
    last_reviewed_at=current.last_reviewed_at,
    next_review_due=current.next_review_due,
    tags=current.tags,
    designer_notes=current.designer_notes,
    reviewed_by=reviewer,
    reviewed_at=int(time()),
)
```

### 3. Updated Agno Agent Spec Schema (additions marked with ➕)

```python
AgentSpec(
    # ... all existing fields ...
    
    # ═══════════════════════════════════════════════════
    # DESIGN-TO-CODE BRIDGE (links to Implementation Map)
    # ═══════════════════════════════════════════════════
    design_spec_id=current.design_spec_id,              # ➕ FK to design spec
    design_spec_version=current.design_spec_version,    # ➕ which design version produced this config
    implementation_map_id=current.implementation_map_id, # ➕ FK to implementation map
    implementation_map_version=current.implementation_map_version, # ➕
    
    # ═══════════════════════════════════════════════════
    # DESIGN-LEVEL FIELDS (from design spec, denormalised for runtime)
    # ═══════════════════════════════════════════════════
    agent_class=current.agent_class,                  # ➕ Extractor/Measurer/Assessor/Generator/Aggregator
    agent_orientation=current.agent_orientation,      # ➕ Possibility/Bridge/Constraint
    progressive_autonomy_level=current.progressive_autonomy_level,  # ➕ shadow/advisory/supervised/autonomous
    authority_boundaries=current.authority_boundaries, # ➕ JSON: hard constraints from design spec
    information_boundaries=current.information_boundaries, # ➕ JSON: what agent CANNOT access (CC-4)
    verification_independence=current.verification_independence, # ➕ boolean: is there a separate verification agent?
    cost_budget_per_interaction=current.cost_budget_per_interaction, # ➕ token/cost limit
    cost_budget_per_session=current.cost_budget_per_session,       # ➕ token/cost limit
    spec_aging_last_review=current.spec_aging_last_review,         # ➕ timestamp
    
    # ═══════════════════════════════════════════════════
    # TOOL REGISTRY (queryable, not just serialized)
    # ═══════════════════════════════════════════════════
    # Keep the existing serialized tools field for Agno compatibility
    # but also add a queryable reference
    tool_registry_id=current.tool_registry_id,   # ➕ FK to implementation map's tool_registry
)
```

### 4. Infrastructure Registry Schema (NEW — system-level)

```python
class InfrastructureRegistry:
    """Registry of existing system tools, databases, services, and capabilities.
    
    When designing a new agent, check this FIRST to reuse existing infrastructure.
    Only add new entries when existing infrastructure doesn't meet the need.
    """
    
    # ═══════════════════════════════════════════════════
    # CORE IDENTITY
    # ═══════════════════════════════════════════════════
    infra_id: str               # unique identifier (e.g., "infra_postgres_main")
    name: str                   # human-readable name (e.g., "Primary PostgreSQL")
    category: str               # database | api | toolkit | mcp_server | service | model | other
    status: str                 # running | planned | deprecated | offline
    
    # ═══════════════════════════════════════════════════
    # CONNECTION DETAILS
    # ═══════════════════════════════════════════════════
    connection_config: dict     # JSON: connection string, endpoint, auth details
    # Examples:
    #   {"url": "postgresql+psycopg://ai:ai@localhost:5532/ai", "type": "postgres"}
    #   {"url": "http://localhost:7777/mcp", "type": "mcp_endpoint"}
    #   {"url": "http://localhost:5000", "type": "web_ui", "access": "read_only"}
    
    # ═══════════════════════════════════════════════════
    # CAPABILITIES & SCHEMAS
    # ═══════════════════════════════════════════════════
    capabilities: dict          # JSON: what this infrastructure can do
    # Examples:
    #   {"schemas": ["project_manager", "public"], "features": ["vector_search", "jsonb", "triggers"]}
    #   {"tools": ["create_project", "update_project", ...], "toolkit": "ProjectManagerToolkit"}
    #   {"models": ["glm-5.1:cloud"], "provider": "ollama"}
    
    schemas: dict               # JSON: database schemas this infrastructure owns
    # Examples:
    #   {"project_manager": {"tables": ["projects", "tasks", "task_dependencies",
    #                                    "authorised_agents", "agent_instructions"],
    #                        "enforcement": "private_schema_no_delete_triggers"}}
    
    # ═══════════════════════════════════════════════════
    # USAGE & OWNERSHIP
    # ═══════════════════════════════════════════════════
    owned_by: str               # which agent/system owns this infrastructure
    # Examples: "project_manager", "system", "shared"
    
    used_by: list               # which agents/systems use this infrastructure
    # Examples: ["project_manager", "web_ui"]
    
    # ═══════════════════════════════════════════════════
    # REUSE RECOMMENDATION
    # ═══════════════════════════════════════════════════
    reuse_priority: str         # primary | secondary | avoid | replace
    # primary: always use this first for the capability it provides
    # secondary: use if primary isn't available
    # avoid: exists but shouldn't be used for new agents (legacy)
    # replace: planned for replacement
    
    reuse_notes: str            # when to reuse vs build new
    # Examples: "Use for all agent data storage. Create private schemas per agent."
    #           "Use for inter-agent communication. All agents should connect via MCP."
    #           "Do NOT use for new agents — being replaced by TypeDB for graph data."
    
    # ═══════════════════════════════════════════════════
    # METADATA
    # ═══════════════════════════════════════════════════
    created_at: int
    updated_at: int
    tags: list                  # for filtering and search
    # Examples: ["database", "postgres", "storage", "primary"]
    #           ["mcp", "communication", "agent-os"]
    #           ["model", "ollama", "llm"]
```

---

## The Complete Picture

Here's how the three schemas connect, using the Project Manager as the example:

```
┌─────────────────────────────────────────────────────────────────┐
│ DESIGN SPEC (WHY)                                               │
│                                                                 │
│ identity_core: "Structural registry keeper"                      │
│ agent_class: "Aggregator"                                       │
│ agent_orientation: "Constraint"                                 │
│ hard_constraints: [NEVER delete, NEVER interpret, ...]            │
│ failure_modes: [status misclassification, data loss, ...]       │
│ subtasks: [T1=create_project, T2=update_project, ...]          │
│ cc_implementation_map: ──────────────────────────┐               │
│                                                  │               │
└──────────────────────────────────────────────────│───────────────┘
                                                   │
                                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION MAP (HOW)                                        │
│                                                                 │
│ design_spec_id: → Design Spec FK                                 │
│                                                                 │
│ subtask_tool_map:                                                │
│   T1 (Create project) → create_project tool (Aggregator)        │
│   T2 (Update project) → update_project tool (Aggregator)        │
│   T7 (Add dependency) → add_dependency tool (Aggregator)        │
│   T9 (Get details) → get_project/get_task tool (Extractor)      │
│                                                                 │
│ cc_implementation_map:                                           │
│   CC-4 → private Postgres schema + triggers (Regime 3)          │
│   CC-7 → per-interaction + per-session token budgets            │
│   CC-8 → agent_instructions table (logged level)                 │
│                                                                 │
│ infrastructure_dependencies:                                     │
│   PostgreSQL (existing: infra_postgres_main) ────────────────────│──► INFRASTRUCTY REGISTRY
│   AgentOS MCP (existing: infra_agentos_mcp)                     │
│   Web UI (new: Flask dashboard)                                 │
│                                                                 │
│ design_decisions:                                                │
│   "Private schema for data isolation" → CC-4 hard constraint #4 │
│   "Soft-delete triggers" → hard constraint #1                  │
│   "Circular dependency trigger" → hard constraint #7            │
│                                                                 │
│ implementation_files: [schema.sql, toolkit.py, agent.py, ...]    │
│                                                                 │
└──────────────────────────────────────────────────│───────────────┘
                                                   │
                                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│ AGNO AGENT SPEC (WHAT)                                          │
│                                                                 │
│ design_spec_id: → Design Spec FK                                │
│ design_spec_version: 1                                           │
│ implementation_map_id: → Implementation Map FK                 │
│                                                                 │
│ model: "ollama:glm-5.1:cloud"                                   │
│ agent_class: "Aggregator"          ← from design spec           │
│ agent_orientation: "Constraint"    ← from design spec           │
│ progressive_autonomy_level: "shadow" ← from implementation map  │
│ authority_boundaries: [...]         ← from design spec          │
│ information_boundaries: [...]       ← from design spec          │
│ tools: [ProjectManagerToolkit]                                    │
│ system_message: "You are the Project Manager..."                 │
│ db: "postgresql+psycopg://ai:ai@localhost:5532/ai"              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

And the Infrastructure Registry sits alongside all three:

```
┌─────────────────────────────────────────────────────────────────┐
│ INFRASTRUCTURE REGISTRY (WHAT EXISTS)                           │
│                                                                 │
│ infra_postgres_main:                                            │
│   category: database                                             │
│   status: running                                                │
│   capabilities: {schemas: [project_manager, public], ...}       │
│   owned_by: system (shared)                                      │
│   used_by: [project_manager, web_ui]                             │
│   reuse_priority: primary                                        │
│   reuse_notes: "Use for all agent data. Private schemas/agent." │
│                                                                 │
│ infra_agentos_mcp:                                               │
│   category: mcp_server                                          │
│   status: running                                                │
│   capabilities: {endpoint: /mcp, agents: [project_manager]}     │
│   owned_by: system                                               │
│   used_by: [project_manager, ...]                                │
│   reuse_priority: primary                                        │
│   reuse_notes: "Use for all inter-agent communication."         │
│                                                                 │
│ infra_ollama_cloud:                                              │
│   category: model                                               │
│   status: running                                                │
│   capabilities: {models: [glm-5.1:cloud], provider: ollama}    │
│   owned_by: system (shared)                                      │
│   used_by: [project_manager, ...]                               │
│   reuse_priority: primary                                        │
│   reuse_notes: "Primary LLM. Use Ollama(id='glm-5.1:cloud')"    │
│                                                                 │
│ infra_project_manager_db_schema:                                │
│   category: database_schema                                     │
│   status: running                                                │
│   capabilities: {tables: [projects, tasks, ...], ...}          │
│   owned_by: project_manager                                     │
│   used_by: [project_manager, web_ui]                             │
│   reuse_priority: avoid (private to project_manager)             │
│   reuse_notes: "Do NOT use directly. Access via PM tools only." │
│                                                                 │
│ infra_project_manager_web_ui:                                   │
│   category: service                                             │
│   status: running                                                │
│   capabilities: {read_only: true, url: localhost:5000}         │
│   owned_by: project_manager                                     │
│   used_by: [human_users]                                        │
│   reuse_priority: secondary                                      │
│   reuse_notes: "Web UI for human viewing. Not used by agents." │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Other Implementation Decisions That Need Capturing

Beyond what I've put in the schemas, here are the categories of decisions that fall through the cracks:

| Category | Examples from Project Manager | Why It Matters |
|----------|-------------------------------|----------------|
| **Data schema design** | Private schema, table structures, triggers, indexes | This IS the CC-4 implementation. Without it, you can't verify information boundaries are enforced. |
| **Error message design** | "Circular dependency detected: adding this would create a cycle" vs "Error processing request" | The typed, separated output design from Section 8. Wrong error messages create the wrong emotional experience. |
| **Null-state output design** | "No projects found with status 'on_hold'" vs silence | Hard constraint #9 (always produce null-state output). The implementation IS the constraint. |
| **Validation logic** | FK checks, status enum checks, cycle detection | These implement hard constraints #5, #6, #7. The design says "never"; the code enforces it. |
| **Access control** | `authorised_agents` table, permission levels | This implements CC-4 at the data layer (who can interact with this agent). |
| **System message** | The full 20-line system prompt | This is the behavioural specification in natural language. It implements identity, authority boundaries, and hard constraints. |
| **Progressive autonomy tracking** | Not yet implemented | The design defines 4 phases but there's no mechanism to track which phase the agent is in. |
| **Health metric collection** | Not yet implemented | The design defines targets (99.9% data accuracy, <2s response time) but no code to measure them. |
| **Trust Ledger** | Not yet implemented | Quarterly report on override rates, accuracy, cost variance. The design defines it but no code exists. |

The Implementation Map captures **which decisions were made and why**, the Infrastructure Registry captures **what already exists to reuse**, and the Agno spec captures **the resulting configuration**. Together, these three schemas plus the design spec give you complete traceability from **WHY** through **HOW** to **WHAT**.

Want me to produce the updated complete schemas as code?

---

## Run 8 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T04:44:11* · `glm-5.1:cloud` · `68f0a9ec...`

### Prompt

i don't want schemas from you. I want a plan of going from agent design spec to agno agent spec.

What are all the elements that need to be designed and specced before we can implement?

### Response

Good — you want the complete decision pipeline from design to implementation. Let me map this out systematically.

## The 12 Elements Between Design and Implementation

```
DESIGN SPEC (WHY)                    AGNO AGENT SPEC (WHAT)
        │                                      │
        │         ┌──────────────────┐          │
        └────────►│ IMPLEMENTATION   │◄─────────┘
                  │ DECISIONS (HOW) │
                  │   12 elements    │
                  └──────────────────┘
```

---

### 1. Subtask → Tool Mapping

**What it is:** Every subtask in the design spec (T1, T2, T3…) must be mapped to a specific tool or mechanism that implements it.

**Why it matters:** Without this, you can't verify that all design-spec subtasks are implemented, and you can't trace authority boundaries from design to code.

**Decision required:**

| Subtask | Tool | Authority Boundary | Class |
|---------|------|--------------------|-------|
| T1 Create project | `create_project` | Assembles record, never interprets | Aggregator |
| T9 Get details | `get_project` | Returns exact data, never filters | Extractor |
| ... | ... | ... | ... |

**Project Manager example:** 13 subtasks → 13 tools, 1:1 mapping. But some agents might have N:1 (one tool serves multiple subtasks) or 1:N (one subtask needs multiple tools).

---

### 2. CC → Implementation Mapping

**What it is:** Every cross-cutting concern from the design spec must be mapped to a concrete implementation mechanism.

**Why it matters:** This is how you verify that design principles are actually enforced, not just stated in a prompt.

**Decision required:**

| CC | Mechanism | Enforcement Regime | Status |
|----|-----------|-------------------|--------|
| CC-1 Verification Independence | Separate assessor agent (TBD for PM) | Detect | Planned |
| CC-4 Information Boundaries | Private Postgres schema + DELETE triggers | Prevent | Implemented |
| CC-5 Specification Aging | `spec_aging` field + `last_reviewed_at` tracking | Detect | Implemented |
| CC-7 Cost Budget | Per-interaction + per-session token limits | Detect | Implemented |
| CC-8 Audit Trail | `agent_instructions` table (logged level) | Detect | Implemented |

**The key question for each CC:** Is this Regime 1 (Declare — prompt only), Regime 2 (Detect — flag violations), or Regime 3 (Prevent — structurally enforced)?

---

### 3. Data Schema Design

**What it is:** The database schema — tables, columns, constraints, triggers, indexes, access control.

**Why it matters:** This is where CC-4 (information boundaries), hard constraints (#1 no DELETE, #6 FK validation, #7 circular dependency prevention), and CC-8 (audit trail) are implemented at the data layer.

**Decision required:**
- Which database engine (Postgres, SQLite, etc.)
- Schema strategy (private schema per agent, shared schema with row-level security, etc.)
- Table design (columns, types, constraints, defaults)
- Enforcement triggers (what violations are prevented at the data layer vs code layer)
- Index strategy (what queries need fast access)
- Access control (who can read, who can write, from where)

**Project Manager example:** Private `project_manager` schema with 5 tables, DELETE prevention triggers, circular dependency trigger, auto-timestamp triggers.

---

### 4. Tool Authority Boundaries

**What it is:** Every tool needs explicit authority boundaries — what it CAN do, what it NEVER does, and how it fails.

**Why it matters:** The design spec says "NEVER interpret content" but the tool implementation needs to enforce this or at least make it structurally difficult to violate.

**Decision required for each tool:**

| Tool | CAN | NEVER | Failure Mode | Null State |
|------|-----|-------|---------------|-------------|
| `create_project` | Assemble record from provided fields | Suggest project name, set priority | Fabrication (wrong fields) | N/A |
| `list_projects` | Return all matching records | Hide records, reorder by importance | Omission (missing records) | "No projects found with status X" |
| `archive_project` | Set status to 'archived' | Delete, decide when to archive | Premature archival | N/A |

---

### 5. System Message Design

**What it is:** The full system prompt that implements the agent's identity, authority boundaries, hard constraints, and behavioral guidelines.

**Why it matters:** This is the primary mechanism for Regime 1 (Declare) enforcement. The system prompt IS the agent's identity declaration.

**Decision required:**
- Identity statement (from Section 0 Q1)
- Authority boundaries (from Section 0 Q3)
- Hard constraints (from Section 7 Q2)
- Behavioral guidelines (common situations from Section 5 Q4)
- Null-state output design (from Section 1 Q4)
- Error message design (from Section 7 Q6)
- Emotional experience design (from Section 8 Q3)

**Project Manager example:** The 20-line system prompt covering identity, hard constraints, handling common situations, and response format.

---

### 6. Model & Reasoning Configuration

**What it is:** Which LLM, what reasoning mode, what output format, what structured output schema.

**Why it matters:** Different agent classes need different model capabilities. An Extractor can use a smaller/faster model. A Generator needs a stronger model. An Assessor needs reasoning capability.

**Decision required:**
- Model selection (from infrastructure registry — what's available, what's appropriate)
- Reasoning mode (none, step-by-step, etc.)
- Output format (text, markdown, JSON, structured)
- Structured output schema (if applicable — Pydantic model for typed responses)
- Temperature and sampling parameters

**Project Manager example:** `Ollama(id="glm-5.1:cloud")`, no reasoning mode, markdown output, no structured output (tool responses are JSON but the agent's conversational output is markdown).

---

### 7. Session & Memory Configuration

**What it is:** How the agent remembers across interactions, what it remembers, and for how long.

**Why it matters:** Session state carries context between turns. Memory carries knowledge between sessions. The design spec's context requirements (Section 1 Q3) determine what the agent needs to remember.

**Decision required:**
- Session persistence (PostgresDb, SqliteDb, in-memory)
- History configuration (how many past runs to include)
- Memory configuration (agent memory, user memory, both, neither)
- Session state (what state to carry between turns)
- Knowledge configuration (what knowledge bases to load)

**Project Manager example:** PostgresDb for session persistence, `add_history_to_context=True`, `num_history_runs=10`, no agent memory, no knowledge bases.

---

### 8. Inter-Agent Communication

**What it is:** How this agent communicates with other agents — MCP server, shared databases, message passing, etc.

**Why it matters:** The design spec's ecosystem (Section 7, the authorised agents table) defines WHO can interact. This element defines HOW.

**Decision required:**
- Does this agent expose an MCP endpoint? (`enable_mcp_server`)
- Which agents are authorised to interact?
- What permissions does each agent have (read, read_write)?
- How are agent instructions audited? (CC-8)
- What's the message format for inter-agent communication?

**Project Manager example:** AgentOS with `enable_mcp_server=True`, `authorised_agents` table in private schema, `agent_instructions` table for audit trail.

---

### 9. Human Interface Design

**What it is:** How humans interact with this agent — chat interface, web UI, API, voice, etc.

**Why it matters:** Section 8 (Human Experience) defines cognitive load, emotional design, and independence checks. The interface is where these are implemented.

**Decision required:**
- Primary interaction mode (chat, API, web UI, voice)
- Secondary interaction modes (read-only dashboard, notification, etc.)
- Cognitive load design (how much information per interaction)
- Error message design (from Section 7 Q6)
- Null-state output design (from Section 1 Q4)
- Override mechanism (how does the human intervene)

**Project Manager example:** Chat via AgentOS (primary), web UI for read-only dashboard (secondary), MCP for authorised agents (tertiary).

---

### 10. Progressive Autonomy Tracking

**What it is:** A mechanism to track which autonomy phase the agent is in and what metrics trigger promotion.

**Why it matters:** The design spec defines 4 phases (shadow → advisory → supervised → autonomous) but there's no runtime tracking mechanism by default.

**Decision required:**
- Where is autonomy level stored? (Implementation Map, session state, database, config)
- What metrics trigger promotion? (data accuracy rate, override rate, cost variance)
- Who decides promotion? (human, automatic based on metrics)
- Can autonomy be demoted? (yes, with what trigger)
- What does each phase look like operationally? (what the agent does differently)

**Project Manager example:** Not yet implemented. Planned: stored in Implementation Map, promoted based on Trust Ledger metrics.

---

### 11. Health Monitoring & Cost Tracking

**What it is:** Mechanisms to measure the health metrics defined in Section 9 and the cost budget defined in Section 7.

**Why it matters:** You can't manage what you don't measure. The design spec defines targets but doesn't specify the measurement mechanism.

**Decision required:**
- How do you measure data accuracy? (spot checks, automated verification, comparison against source)
- How do you measure query response time? (logging, timing middleware)
- How do you measure unauthorised access attempts? (audit log, alert thresholds)
- How do you track token usage per interaction and per session?
- What happens when cost budget is exceeded? (warn, halt, both)
- Where is health data stored? (Implementation Map, separate monitoring, external system)

**Project Manager example:** Not yet implemented. Planned: Trust Ledger with quarterly review.

---

### 12. Infrastructure Inventory & Reuse

**What it is:** What already exists in your system that this agent can reuse vs what needs to be built new.

**Why it matters:** "Reuse first, build new second" prevents duplication and ensures consistency across agents.

**Decision required for each infrastructure need:**

| Need | Already Exists? | Reuse? | New Build Needed? |
|------|----------------|--------|-------------------|
| Primary database | ✅ Postgres running | ✅ Use it, add schema | ❌ |
| Vector store | ❌ Not needed for PM | N/A | ❌ |
| Graph database | ❌ Not needed for PM | N/A | ❌ |
| LLM endpoint | ✅ Ollama Cloud available | ✅ Use it | ❌ |
| MCP server | ✅ AgentOS provides it | ✅ Use it | ❌ |
| Web UI framework | ❌ Not yet built | ❌ | ✅ Build Flask dashboard |
| Agent toolkit | ❌ Not yet built | ❌ | ✅ Build ProjectManagerToolkit |
| Audit logging | ❌ Not yet standardised | ❌ | ✅ Build agent_instructions table |

**This is the Infrastructure Registry** — a living document (or database table) that tracks every piece of infrastructure, who owns it, who uses it, and whether new agents should reuse it or build their own.

---

## The Implementation Sequence

These 12 elements don't all happen at once. Here's the recommended order:

```
Phase 1: INVENTORY (what exists?)
  └── Element 12: Infrastructure Inventory & Reuse

Phase 2: DATA (what stores the agent's world?)
  └── Element 3: Data Schema Design
  └── Element 6: Session & Memory Configuration

Phase 3: TOOLS (what can the agent do?)
  └── Element 1: Subtask → Tool Mapping
  └── Element 4: Tool Authority Boundaries
  └── Element 7: Inter-Agent Communication

Phase 4: BEHAVIOUR (how does the agent think and act?)
  └── Element 5: System Message Design
  └── Element 8: Human Interface Design
  └── Element 9: Model & Reasoning Configuration

Phase 5: VERIFICATION (how do you know it works as designed?)
  └── Element 2: CC → Implementation Mapping
  └── Element 10: Progressive Autonomy Tracking
  └── Element 11: Health Monitoring & Cost Tracking
```

Each phase produces artifacts that the next phase depends on. You can't design tools without knowing what infrastructure is available. You can't write a system message without knowing the tool boundaries. You can't verify CC implementation without knowing what mechanisms were chosen.

This is the bridge between WHY and WHAT — the HOW decisions that turn a design specification into a running agent.

---

## Run 9 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T04:58:34* · `glm-5.1:cloud` · `ec4019b6...`

### Prompt

I'm currently creating the infrastructure table.

What would be the template questions an agent could answer with the user to have all the correct configuration and implementation requirements completed?

### Response

Here's the complete question template, organised by implementation phase. Each question produces a concrete implementation decision.

---

## Phase 1: What Already Exists?

### Infrastructure Inventory

**Q1: What databases are already running?**
> For each: type (Postgres, MySQL, SQLite, etc.), connection details, what it's used for, who owns it, can other agents use it?

**Q2: What agent runtimes are already set up?**
> AgentOS, LangServe, custom server — what's already running and available?

**Q3: What LLM endpoints are available?**
> Ollama Cloud, OpenAI, Anthropic, local models — what's configured, what models, what are the cost limits?

**Q4: What existing agent toolkits or tools are already built?**
> Any custom toolkits, API clients, database access tools that a new agent could reuse?

**Q5: What MCP servers or inter-agent communication is already running?**
> Endpoints, protocols, which agents are connected, what data flows between them.

**Q6: What storage systems exist?**
> Object storage (MinIO, S3), vector databases (Chroma), graph databases (TypeDB), file systems — what's available?

**Q7: What monitoring or logging infrastructure exists?**
> Dashboards, alerting, log aggregation — what's already set up for other agents?

**Q8: What web UIs or dashboards are already running?**
> Existing frontend frameworks, deployed apps, shared component libraries.

**Q9: What APIs or external services are already integrated?**
> Third-party APIs with keys, webhooks, scheduled tasks — what connections already work?

---

## Phase 2: What Data Does This Agent Need?

### Data Schema Design

**Q10: What information does this agent need to store?**
> List every type of data the agent will create, read, update, or archive. Think about the records, not the tables.

**Q11: What information does this agent need to read but NOT own?**
> Data owned by other agents or external systems that this agent needs access to.

**Q12: What are the relationships between the data?**
> "A task belongs to a project." "A dependency links two tasks." "An agent instruction belongs to an agent." — list every relationship.

**Q13: What must NEVER happen to the data?**
> Never deleted? Never accessed by other agents? Never modified without audit? This determines your enforcement regime.

**Q14: What statuses or states does each record type have?**
> For projects: active, on_hold, completed, archived. For tasks: todo, in_progress, blocked, done, archived. List every status for every record type.

**Q15: What validation rules must the data follow?**
> "A task can't belong to a non-existent project." "A dependency can't be circular." "Status must be one of these values." List every rule.

**Q16: How long does the data live?**
> Is it permanent? Archived after a period? Deleted after a retention period? This determines your aging strategy.

**Q17: Who else needs to see this data?**
> Other agents? A web UI? External systems? Read-only? Read-write? This determines your access control.

### Session & Memory Configuration

**Q18: Does this agent need to remember across conversations?**
> If yes, what specifically? User preferences? Project context? Previous decisions? This determines your session and memory setup.

**Q19: How much conversation history should the agent carry?**
> Last 5 turns? Last 20? Everything? This affects token usage and response quality.

---

## Phase 3: What Can This Agent Do?

### Subtask → Tool Mapping

**Q20: For each subtask in the design spec, what tool implements it?**
> Map every T1, T2, T3… to a specific function, API call, database operation, or external service.

**Q21: Are there subtasks that need multiple tools?**
> Some subtasks might need: check if record exists → create if not → return confirmation. Map the sequence.

**Q22: Are there tools that serve multiple subtasks?**
> A single "query" tool might serve T9, T10, T11. Make this explicit.

### Tool Authority Boundaries

**Q23: For each tool, what is it ALLOWED to do?**
> "create_project can: insert a record with provided fields, return the created record."

**Q24: For each tool, what is it NEVER allowed to do?**
> "create_project NEVER: suggests a project name, sets a priority, creates a project without a name."

**Q25: For each tool, what does it return when there's nothing to return?**
> The null-state output for every tool. "No projects found with status 'on_hold'."

**Q26: For each tool, what does it return when something goes wrong?**
> Specific error messages for every failure case. Not "Error processing request" — specific guidance.

### Inter-Agent Communication

**Q27: Does this agent need to receive instructions from other agents?**
> If yes: which agents, what kind of instructions, what permissions (read, read_write)?

**Q28: Does this agent need to send instructions to other agents?**
> If yes: which agents, what kind of instructions, how (MCP, shared database, message queue)?

**Q29: How are agent-to-agent interactions audited?**
> Every instruction from another agent should be logged: who sent it, what they asked for, what happened.

---

## Phase 4: How Does This Agent Behave?

### System Message Design

**Q30: What is this agent's one-sentence identity?**
> "I am a structural registry that creates and manages projects, tasks, and their dependencies — without interpreting, prioritising, or judging content."

**Q31: What are the hard constraints (the NEVER list)?**
> Number them. Make each one concrete and verifiable. "NEVER delete records" is verifiable. "NEVER be unhelpful" is not.

**Q32: What are the 3-5 most common situations the agent will face?**
> For each, what should it say? "If asked what to work on next → respond with data only, not suggestions."

**Q33: How should the agent format its responses?**
> Markdown tables? Bullet points? JSON? Structured lists? This determines the response format.

**Q34: What emotional tone should the agent use?**
> Clinical and precise? Warm and helpful? Concise and efficient? This is Section 8 (Human Experience) translated to language.

### Human Interface Design

**Q35: How will the human primarily interact with this agent?**
> Chat? Web UI? API? Voice? What's the primary interaction mode?

**Q36: Are there secondary interaction modes?**
> Read-only dashboard? Email notifications? Mobile push? What other ways does the human need to see or interact with this agent's data?

**Q37: What's the most common action the human will take?**
> "Create a task" or "Check project status" — design the primary interaction around this.

### Model & Reasoning Configuration

**Q38: What model should this agent use?**
> Based on agent class: Extractor/Measurer can use smaller models. Assessor/Generator may need stronger reasoning. What's available in your infrastructure registry?

**Q39: Does this agent need structured output?**
> If the agent produces typed, structured data (like a registry), structured output ensures consistency. If it produces conversational text, markdown may be better.

**Q40: Does this agent need reasoning mode?**
> For complex assessment or generation, step-by-step reasoning may be needed. For simple CRUD, it's unnecessary overhead.

---

## Phase 5: How Do You Know It Works?

### CC → Implementation Mapping

**Q41: For each cross-cutting concern, how is it enforced?**
> For each CC, answer: Is this Regime 1 (Declare — prompt only), Regime 2 (Detect — flag violations), or Regime 3 (Prevent — structurally enforced)?

| CC | Question | Enforcement Regime |
|----|----------|-------------------|
| CC-1 Verification Independence | Is there a separate agent or mechanism that verifies this agent's output? | 1/2/3 |
| CC-3 Epistemic Metadata | Do outputs carry confidence, provenance, and uncertainty? How? | 1/2/3 |
| CC-4 Information Boundaries | Can other agents access this agent's data directly? How is that prevented? | 1/2/3 |
| CC-5 Specification Aging | When is this agent's specification reviewed? What triggers an early review? | 1/2/3 |
| CC-7 Cost Budget | What's the per-interaction and per-session token limit? What happens when exceeded? | 1/2/3 |
| CC-8 Audit Trail | Are all actions logged? At what level (logged/assured/verified)? | 1/2/3 |

**Q42: Which hard constraints are enforced at the data layer (Regime 3) vs the prompt layer (Regime 1)?**
> "Never delete" can be enforced by a database trigger (Regime 3) or by a prompt instruction (Regime 1). Which constraints warrant structural enforcement?

### Progressive Autonomy Tracking

**Q43: What are the autonomy phases for this agent?**
> Shadow (show before doing) → Advisory (do and show) → Supervised (do, human confirms key actions) → Autonomous (do, human monitors). Define each phase.

**Q44: What metrics determine promotion to the next phase?**
> Data accuracy rate, override rate, cost variance — what numbers trigger promotion?

**Q45: Who decides promotion?**
> The human? Automatic based on metrics? A combination?

**Q46: Can autonomy be demoted? What triggers demotion?**
> Accuracy drop, cost spike, violation of a hard constraint — what sends the agent back to a more supervised phase?

### Health Monitoring & Cost Tracking

**Q47: What health metrics does this agent need to track?**
> From Section 9 of the design spec: data accuracy, response time, success rate, unauthorised access attempts, etc.

**Q48: How will you measure each metric?**
> Automated spot-checks, logging middleware, comparison against source, manual review — be specific.

**Q49: What are the alert thresholds?**
> For each metric: what's the target? What's the warning level? What's the critical level?

**Q50: How will token costs be tracked?**
> Per interaction? Per session? Cumulative? Where is the cost data stored?

**Q51: What happens when cost budget is exceeded?**
> Warn and continue? Halt? Warn once then halt on second exceedance?

---

## The Quick-Start Version

For agents like the Project Manager (simple class, constraint-oriented, low stakes), many of these questions have obvious answers. Here's the minimum viable set:

| # | Question | Why It's Essential |
|---|----------|-------------------|
| Q10 | What information does this agent store? | Determines the entire database schema |
| Q13 | What must NEVER happen to the data? | Determines enforcement regime |
| Q17 | Who else needs to see this data? | Determines access control |
| Q20 | What tool implements each subtask? | Determines the toolkit |
| Q24 | What is each tool NEVER allowed to do? | Determines authority boundaries |
| Q30 | What is this agent's one-sentence identity? | Determines the system message |
| Q31 | What are the hard constraints? | Determines what gets enforced where |
| Q41 | How is each CC enforced? | Determines Regime 1/2/3 for each concern |
| Q1 | What databases are already running? | Reuse first, build new second |

The other 42 questions deepen the specification for more complex agents.

---

## Run 10 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T05:02:06* · `glm-5.1:cloud` · `e31a34dc...`

### Prompt

complete the answers for this template for the project database manager agent

### Response

## Phase 1: What Already Exists?

### Infrastructure Inventory

**Q1: What databases are already running?**

| Database | Type | Connection | Used For | Owned By | Reusable? |
|----------|------|------------|----------|----------|----------|
| Primary PostgreSQL | Postgres (PgVector) | `postgresql+psycopg://ai:ai@localhost:5532/ai` | Agent session storage, vector search, all agent data | System (shared) | ✅ Primary data store. Create private schemas per agent. |
| (Future) TypeDB | Graph database | Not yet running | PRISM knowledge graph, entity relationships | TBD | Planned for CAWDP Design Studio |
| (Future) Chroma | Vector store | Not yet running | Knowledge embeddings, semantic search | TBD | Planned for Agent-Native Knowledge Base |
| (Future) MinIO | Object storage | Not yet running | Document storage, media | TBD | Planned for CoS Agent Platform |

**Q2: What agent runtimes are already set up?**

| Runtime | Status | Details |
|---------|--------|---------|
| Agno AgentOS | Available | v2.5+, Python/FastAPI, MCP server support built-in |
| Ollama Cloud | Available | `glm-5.1:cloud` as primary model |

**Q3: What LLM endpoints are available?**

| Endpoint | Model | Cost | Notes |
|----------|-------|------|-------|
| Ollama Cloud | `glm-5.1:cloud` | Per-token | Primary LLM for all agents |
| (Future) OpenAI | Various | Per-token | Fallback if Ollama unavailable; only for embeddings if needed |

**Q4: What existing agent toolkits or tools are already built?**

| Toolkit | Purpose | Reusable? |
|---------|---------|-----------|
| ProjectManagerToolkit | Project/task/dependency CRUD | ✅ Other agents can query via MCP |
| (None else yet) | | |

**Q5: What MCP servers or inter-agent communication is already running?**

| Endpoint | Protocol | Connected Agents | Data Flow |
|----------|----------|------------------|-----------|
| Project Manager MCP | `/mcp` via AgentOS | None yet (authorised_agents table seeded with `human_owner`) | Authorised agents send instructions; PM processes through tools |

**Q6: What storage systems exist?**

| System | Type | Status | Reusable? |
|--------|------|--------|-----------|
| PgVector (in Primary PostgreSQL) | Vector + relational | ✅ Running | ✅ All agents use for session storage |
| (Future) TypeDB | Graph | ❌ Planned | For PRISM knowledge graph |
| (Future) Chroma | Vector | ❌ Planned | For knowledge embeddings |
| (Future) MinIO | Object | ❌ Planned | For document storage |

**Q7: What monitoring or logging infrastructure exists?**

| System | Status | Details |
|--------|--------|---------|
| Agno AgentOS logging | ✅ Available | Built-in logging for agent runs |
| `agent_instructions` table | ✅ Built | CC-8 audit trail at logged level for inter-agent instructions |
| (Future) Trust Ledger | ❌ Planned | Quarterly health metrics dashboard |
| (Future) Cost tracking | ❌ Planned | Per-interaction and per-session token counting |

**Q8: What web UIs or dashboards are already running?**

| UI | Status | Purpose | Access |
|----|--------|---------|--------|
| Project Manager Dashboard | ✅ Built | Read-only project/task status viewer | `http://localhost:5000` |
| (Future) AgentOS Admin | ❌ Planned | Agent management, session history | TBD |

**Q9: What APIs or external services are already integrated?**

| Service | Status | Purpose |
|---------|--------|---------|
| None yet | — | Project Manager doesn't need external APIs |

---

## Phase 2: What Data Does This Agent Need?

### Data Schema Design

**Q10: What information does this agent need to store?**

| Data Type | Fields | Status | Purpose |
|-----------|--------|--------|---------|
| Projects | id, name, description, status, assignee, created_at, updated_at, due_date, completed_at, metadata | ✅ Built | Core record |
| Tasks | id, project_id, parent_task_id, title, description, status, assignee, depth, created_at, updated_at, due_date, completed_at, metadata | ✅ Built | Core record, nestable via parent_task_id |
| Task Dependencies | id, task_id, depends_on_task_id, dependency_type, created_at | ✅ Built | Links tasks |
| Authorised Agents | id, agent_id, agent_name, permission, created_at, updated_at | ✅ Built | Access control |
| Agent Instructions | id, agent_id, instruction, instruction_type, status, result, created_at, completed_at | ✅ Built | Audit trail (CC-8) |

**Q11: What information does this agent need to read but NOT own?**

| Data | Source | Access | Purpose |
|------|--------|--------|---------|
| None currently | — | — | Project Manager owns all its data. No reads from other agents' data stores yet. Future: may read strategy decisions from a Strategy Agent's knowledge base. |

**Q12: What are the relationships between the data?**

| Relationship | Type | Constraint |
|--------------|------|-----------|
| Task → Project | Many-to-one | Task must belong to an existing project (FK enforced) |
| Task → Task (parent) | Self-referencing | Parent task must exist and belong to same project (FK + check enforced) |
| Dependency → Task (task) | Many-to-one | Both tasks must exist (FK enforced) |
| Dependency → Task (depends on) | Many-to-one | Both tasks must exist (FK enforced), no self-dependency, no circular dependency (trigger enforced) |
| Agent Instruction → Authorised Agent | Many-to-one | Agent must be authorised before instruction accepted (application-level check) |

**Q13: What must NEVER happen to the data?**

| Never | Enforcement Regime | Mechanism |
|-------|-------------------|-----------|
| Records must NEVER be deleted | Regime 3 (Prevent) | Database triggers `prevent_project_delete()` and `prevent_task_delete()` |
| Unauthorised agents must NEVER write to project_manager tables | Regime 3 (Prevent) | Private schema; only the agent's toolkit has write access |
| Circular dependencies must NEVER be created | Regime 3 (Prevent) | Database trigger `prevent_circular_dependency()` using recursive CTE |
| A task must NEVER belong to a non-existent project | Regime 3 (Prevent) | Foreign key constraint on `tasks.project_id` |
| A subtask must NEVER belong to a different project than its parent | Regime 2 (Detect) | Application-level check in `create_task` tool |
| The agent must NEVER interpret content or suggest priorities | Regime 1 (Declare) | System prompt hard constraints |

**Q14: What statuses or states does each record type have?**

| Record | Statuses | Default | Notes |
|--------|----------|---------|-------|
| Project | `active`, `on_hold`, `completed`, `archived` | `active` | Archived = soft delete. No "deleted" status. |
| Task | `todo`, `in_progress`, `blocked`, `done`, `archived` | `todo` | Archived = soft delete. "blocked" = waiting on dependency. |
| Dependency | N/A | N/A | Dependencies are created/removed, not status-tracked |
| Agent Instruction | `pending`, `completed`, `failed`, `denied` | `pending` | Audit trail statuses |

**Q15: What validation rules must the data follow?**

| Rule | Enforcement | Mechanism |
|------|------------|-----------|
| Project name must not be empty | Regime 3 | Application-level check in `create_project` tool |
| Task must belong to existing project | Regime 3 | FK constraint + application check |
| Parent task must belong to same project | Regime 2 | Application-level check in `create_task` and `update_task` |
| Status must be valid enum value | Regime 3 | CHECK constraint on `status` columns |
| Dependency must not be self-referencing | Regime 3 | CHECK constraint `task_id != depends_on_task_id` |
| Dependency must not create a cycle | Regime 3 | Trigger `prevent_circular_dependency()` |
| Duplicate dependency must not exist | Regime 3 | UNIQUE constraint on `(task_id, depends_on_task_id)` |

**Q16: How long does the data live?**

| Data | Retention | Aging Strategy |
|------|-----------|---------------|
| Projects | Permanent (archived, never deleted) | Review archived projects every 6 months; archive after project completion |
| Tasks | Permanent (archived, never deleted) | Review archived tasks monthly |
| Dependencies | Permanent (removed when no longer needed) | Auto-removed when task is archived |
| Agent Instructions | Permanent (audit trail) | Review quarterly; archive after 1 year |
| Authorised Agents | Permanent | Review when agent roles change |

**Q17: Who else needs to see this data?**

| Viewer | Access Level | Mechanism | Purpose |
|--------|--------------|-----------|---------|
| Peter (human owner) | Read + Write | Direct chat via AgentOS | Create, update, query, archive |
| Authorised agents | Read + Write (per permission) | MCP endpoint `/mcp` | Create tasks, query status, update tasks |
| Web UI (Peter) | Read only | Direct database read | View project/task status dashboard |
| Other agents (not authorised) | None | No access | Private schema blocks direct access |

### Session & Memory Configuration

**Q18: Does this agent need to remember across conversations?**

Yes, but minimally. The agent needs to remember:
- **Session context**: What projects/tasks were discussed in this conversation (handled by `add_history_to_context=True` with `num_history_runs=10`)
- **NOT**: Long-term memory of user preferences, project context, or decisions — the database IS the memory. The agent doesn't need separate memory because all state is in the database.

Configuration: `PostgresDb` for session storage, no agent memory, no user memory.

**Q19: How much conversation history should the agent carry?**

| Setting | Value | Rationale |
|---------|-------|-----------|
| `add_history_to_context` | `True` | Need context for follow-up questions |
| `num_history_runs` | `10` | Last 10 interactions is sufficient for a CRUD agent |
| `num_history_messages` | Default | Not overridden — default is fine |

---

## Phase 3: What Can This Agent Do?

### Subtask → Tool Mapping

**Q20: For each subtask in the design spec, what tool implements it?**

| Subtask ID | Subtask | Tool | Class | Authority Boundary |
|-----------|--------|------|-------|-------------------|
| T1 | Create project | `create_project` | Aggregator | Assembles record, never interprets |
| T2 | Update project | `update_project` | Aggregator | Modifies specified fields, never decides what to change |
| T3 | Archive project | `archive_project` | Aggregator | Sets status to archived, never decides when |
| T4 | Create task | `create_task` | Aggregator | Assembles record, validates FK and parent |
| T5 | Update task | `update_task` | Aggregator | Modifies specified fields, validates parent project |
| T6 | Archive task | `archive_task` | Aggregator | Sets status to archived, never decides when |
| T7 | Add dependency | `add_dependency` | Aggregator | Creates link, validates no cycles |
| T8 | Remove dependency | `remove_dependency` | Aggregator | Removes link, never judges importance |
| T9 | Get project details | `get_project` | Extractor | Returns exact data, never interprets |
| T10 | Get task details | `get_task` | Extractor | Returns exact data with dependencies and subtasks |
| T11 | List projects | `list_projects` | Extractor | Returns matching records, never filters by importance |
| T12 | List tasks | `list_tasks` | Extractor | Returns matching records, never hides results |
| T13 | List dependencies | `list_dependencies` | Extractor | Returns both directions, never judges importance |

**Q21: Are there subtasks that need multiple tools?**

No. Every subtask maps 1:1 to a single tool. This is a registry agent — all operations are simple CRUD or query operations.

**Q22: Are there tools that serve multiple subtasks?**

No. Every tool serves exactly one subtask. 13 subtasks → 13 tools, 1:1 mapping.

### Tool Authority Boundaries

**Q23: For each tool, what is it ALLOWED to do?**

| Tool | ALLOWED |
|------|---------|
| `create_project` | Insert a project record with provided fields; return the created record |
| `update_project` | Modify specified fields on an existing project; return the updated record |
| `archive_project` | Set project status to 'archived'; return confirmation |
| `create_task` | Insert a task record with provided fields; validate project exists and parent belongs to same project; calculate depth; return the created record |
| `update_task` | Modify specified fields on an existing task; validate parent belongs to same project if reparenting; set completed_at when status changes to 'done'; return the updated record |
| `archive_task` | Set task status to 'archived'; return confirmation |
| `add_dependency` | Insert a dependency link; validate both tasks exist; validate no circular dependency; return the created record |
| `remove_dependency` | Delete a dependency link; return confirmation |
| `get_project` | Return all fields of a specific project |
| `get_task` | Return all fields of a specific task plus its dependencies and subtasks |
| `list_projects` | Return all projects matching an optional status filter; exclude archived by default |
| `list_tasks` | Return all tasks matching optional filters (project, status, assignee, parent) |
| `list_dependencies` | Return all dependencies for a task in both directions (what it depends on and what depends on it) |

**Q24: For each tool, what is it NEVER allowed to do?**

| Tool | NEVER |
|------|-------|
| `create_project` | Suggest project name, set priority, create without a name |
| `update_project` | Change fields not specified, interpret what should change, decide when to archive |
| `archive_project` | Delete the record, decide when to archive without human instruction |
| `create_task` | Suggest task title, set priority, create in non-existent project, create with parent from different project |
| `update_task` | Decide what should change, change status to 'done' without setting completed_at |
| `archive_task` | Delete the record, decide when to archive without human instruction |
| `add_dependency` | Suggest dependencies, create circular dependencies, create self-dependencies |
| `remove_dependency` | Judge whether dependency should be removed |
| `get_project` | Interpret content, filter by importance, fabricate records |
| `get_task` | Interpret content, filter by importance, fabricate records, hide subtasks |
| `list_projects` | Hide records, reorder by importance, fabricate records |
| `list_tasks` | Hide records, reorder by importance, fabricate records |
| `list_dependencies` | Judge dependency importance, hide dependencies |

**Q25: For each tool, what does it return when there's nothing to return?**

| Tool | Null-State Output |
|------|-------------------|
| `get_project` | `{"error": "Project {id} not found"}` |
| `get_task` | `{"error": "Task {id} not found"}` |
| `list_projects` | `{"projects": [], "message": "No projects found with status 'on_hold'"}` (or without status filter: "No projects found (excluding archived)") |
| `list_tasks` | `{"tasks": [], "message": "No tasks found with filters: ..."}` |
| `list_dependencies` | `{"task_id": "...", "task_title": "...", "depends_on": [], "depended_on_by": []}` (still returns task info, just empty dependency lists) |

**Q26: For each tool, what does it return when something goes wrong?**

| Error Case | Tool | Response |
|------------|------|----------|
| Missing required field | `create_project`, `create_task` | `{"error": "Missing required field: [field_name]. Please provide [field_name]."}` |
| Record not found | `get_project`, `get_task`, `update_*`, `archive_*` | `{"error": "[Project/Task] {id} not found"}` |
| Invalid status value | `update_project`, `update_task`, `list_*` | `{"error": "Invalid status. Must be one of: active, on_hold, completed, archived"}` |
| Circular dependency | `add_dependency` | `{"error": "Circular dependency detected: adding this dependency would create a cycle."}` |
| Self-dependency | `add_dependency` | `{"error": "A task cannot depend on itself"}` |
| Parent from different project | `create_task`, `update_task` | `{"error": "Parent task must belong to the same project"}` |
| Project not found for task | `create_task` | `{"error": "Project {id} not found"}` |
| Already archived | `archive_project`, `archive_task` | `{"error": "[Project/Task] {id} not found or already archived"}` |
| No fields to update | `update_project`, `update_task` | `{"error": "No fields provided to update"}` |
| Duplicate dependency | `add_dependency` | `{"error": "This dependency already exists"}` |
| Database connection error | Any tool | `{"error": "Unable to access project registry. Please try again later."}` |

### Inter-Agent Communication

**Q27: Does this agent need to receive instructions from other agents?**

Yes. The `authorised_agents` table controls which agents can send instructions.

| Agent ID | Agent Name | Permission | Notes |
|---------|-----------|------------|-------|
| `human_owner` | Human Owner (Peter) | `read_write` | Seed entry, always present |
| (Future) `strategy_agent` | Strategy Orchestrator | `read_write` | Can create/update tasks in strategy projects |
| (Future) `content_agent` | Content Agent | `read_write` | Can create/update tasks in content projects |
| (Future) `marking_agent` | Assignment Marking Agent | `read_write` | Can create/update tasks for marking workflow |

**Q28: Does this agent need to send instructions to other agents?**

No. The Project Manager receives instructions and returns data. It does not initiate communication with other agents. Other agents query it through MCP.

**Q29: How are agent-to-agent interactions audited?**

| Mechanism | Table | Fields | Level |
|-----------|-------|--------|-------|
| Agent instruction log | `agent_instructions` | id, agent_id, instruction, instruction_type, status, result, created_at, completed_at | CC-8 Level 1 (Logged) |

Every instruction from an authorised agent is logged with: who sent it, what they asked for, what type of instruction (create/update/archive/query/add_dependency/remove_dependency), and the result. This provides basic audit trail. Future: upgrade to Level 2 (Assured) with cryptographic verification for high-stakes agents.

---

## Phase 4: How Does This Agent Behave?

### System Message Design

**Q30: What is this agent's one-sentence identity?**

A structural registry that creates and manages projects, tasks, and their dependencies — without interpreting, prioritising, or judging content.

**Q31: What are the hard constraints (the NEVER list)?**

| # | Constraint | Enforcement |
|---|-----------|-------------|
| 1 | NEVER delete records — only archive them | Regime 3: Database trigger prevents DELETE |
| 2 | NEVER interpret task content or priority | Regime 1: System prompt |
| 3 | NEVER suggest what to work on next | Regime 1: System prompt |
| 4 | NEVER allow direct database access from other agents | Regime 3: Private schema + access control |
| 5 | NEVER fabricate records that don't exist | Regime 1: System prompt + null-state output required |
| 6 | ALWAYS validate foreign keys before writing | Regime 2: Application-level checks in tools |
| 7 | ALWAYS detect and prevent circular dependencies | Regime 3: Database trigger |
| 8 | ALWAYS confirm archival actions with the human | Regime 1: System prompt |
| 9 | ALWAYS produce null-state output for empty queries | Regime 1: System prompt + tool implementation |
| 10 | ALWAYS log all write operations in audit trail | Regime 2: `agent_instructions` table |

**Q32: What are the 3-5 most common situations the agent will face?**

| Situation | Agent Response |
|-----------|---------------|
| "What should I work on next?" | Return factual data only: "Here are the tasks with status 'todo' and no blocking dependencies: [list]. Here are the tasks with status 'in_progress': [list]." NEVER suggest priority. |
| "Is this project on track?" | Return data: "Project X has 5 of 12 tasks done, 3 in progress, 4 todo. Due date: 2025-03-15." NEVER assess progress or say "you're behind." |
| "Delete this project" | "I archive records instead of deleting them, to preserve history. Shall I archive this project?" NEVER delete. |
| Ambiguous instruction | "I can create, update, archive, or list projects and tasks. Which did you mean?" NEVER interpret. |
| "Show me everything" | Return structured data with counts and status breakdowns. NEVER filter by importance or hide records. |

**Q33: How should the agent format its responses?**

| Response Type | Format | Example |
|---------------|--------|---------|
| Project details | Structured key-value | `**Project:** Alpha Launch \| **Status:** Active \| **Tasks:** 12 total, 5 done \| **Due:** 2025-03-15` |
| Task list | Grouped by status | `**To Do (3):** Task A, Task B, Task C \| **In Progress (2):** Task D, Task E \| **Blocked (1):** Task F → waiting on Task D` |
| Empty result | Helpful context | `"No tasks found with status 'on_hold'. Active tasks: 8. Done tasks: 3. Would you like to see a different status?"` |
| Error message | Specific guidance | `"Missing required field: project name. Please provide a name for the project."` |
| Confirmation | Clear action + result | `"✅ Project 'Alpha Launch' created with status 'active'. ID: abc-123."` |

**Q34: What emotional tone should the agent use?**

Clinical, precise, and helpful. This is a registry — the agent provides data, not opinions. Tone should be:
- **Concise**: No unnecessary words. Data is primary.
- **Structured**: Use headers, lists, and status indicators, not prose paragraphs.
- **Neutral**: No judgment language ("great progress!", "you're behind"). Just the facts.
- **Helpful on empty**: When results are empty, suggest alternative queries instead of just saying "nothing found."

### Human Interface Design

**Q35: How will the human primarily interact with this agent?**

| Mode | Mechanism | Priority |
|------|-----------|----------|
| Chat | AgentOS conversation via `project_manager` agent | Primary — all CRUD operations |
| Web UI | Flask dashboard at `http://localhost:5000` | Secondary — read-only status viewing |
| API | REST endpoints at `/api/projects`, `/api/tasks` | Tertiary — programmatic read access |

**Q36: Are there secondary interaction modes?**

| Mode | Mechanism | Access | Purpose |
|------|-----------|--------|---------|
| Web UI dashboard | `http://localhost:5000` | Read-only | Project/task status overview, no interaction |
| API endpoints | `/api/projects`, `/api/tasks` | Read-only | Programmatic access for other tools |
| MCP endpoint | `/mcp` | Read-write (authorised agents only) | Inter-agent communication |

**Q37: What's the most common action the human will take?**

Listing tasks and projects (queries), followed by creating tasks. The UI is designed for quick status checks — the chat interface for detailed operations.

### Model & Reasoning Configuration

**Q38: What model should this agent use?**

| Setting | Value | Rationale |
|---------|-------|-----------|
| Model | `Ollama(id="glm-5.1:cloud")` | Default per rules; this is an Aggregator/Extractor agent — doesn't need advanced reasoning |
| Reasoning | None | CRUD operations don't require step-by-step reasoning |
| Temperature | Default | Deterministic is preferred for a registry, but not critical |

**Q39: Does this agent need structured output?**

Yes, but at the tool level, not the conversation level. Tool responses are JSON (structured). Conversational responses are Markdown (human-readable). No Pydantic output schema needed — the agent's primary outputs come from tools, not from the LLM's free-form generation.

**Q40: Does this agent need reasoning mode?**

No. This is a constraint-oriented Aggregator/Extractor. All operations are CRUD or query. No complex assessment or generation that requires step-by-step reasoning.

---

## Phase 5: How Do You Know It Works?

### CC → Implementation Mapping

**Q41: For each cross-cutting concern, how is it enforced?**

| CC | Concern | Enforcement Regime | Mechanism | Status |
|----|---------|-------------------|-----------|--------|
| CC-1 | Verification Independence | Regime 1 (Declare) | No separate verification agent yet. Design spec notes: future Trust Ledger with spot-check verification. | Partial — declared, not structurally enforced |
| CC-3 | Epistemic Metadata | Regime 1 (Declare) + Regime 2 (Detect) | Tool responses include `success`, `count`, `error` fields. Database records include `created_by`, `created_at`, `updated_at`. Not full 6-field epistemic metadata (confidence, provenance, assumptions, limitations, recency, uncertainty) because this is a registry — confidence is binary (data exists or doesn't). | Partial — deterministic fields, not probabilistic |
| CC-4 | Information Boundaries | Regime 3 (Prevent) | Private Postgres schema `project_manager`. No other agent can write to these tables. DELETE prevention triggers. Authorised agents table controls read/write access. | ✅ Implemented |
| CC-5 | Specification Aging | Regime 2 (Detect) | `spec_aging` field in design spec defines review cadence. `last_reviewed_at` and `next_review_due` to be tracked in Implementation Map. | Planned |
| CC-7 | Cost Budget | Regime 2 (Detect) | Per-interaction (~2K-5K tokens) and per-session (~50K tokens) budgets defined. No automated enforcement yet — agent will warn at thresholds. | Partial — defined, not enforced |
| CC-8 | Audit Trail | Regime 2 (Detect — Logged level) | `agent_instructions` table logs all inter-agent instructions with status tracking. | ✅ Implemented (Level 1: Logged) |

**Q42: Which hard constraints are enforced at the data layer (Regime 3) vs the prompt layer (Regime 1)?**

| Hard Constraint | Regime | Mechanism |
|----------------|--------|-----------|
| NEVER delete records | 3 (Prevent) | Database triggers `prevent_project_delete()` and `prevent_task_delete()` |
| NEVER allow direct database write from other agents | 3 (Prevent) | Private schema + application-level access control |
| NEVER create circular dependencies | 3 (Prevent) | Database trigger `prevent_circular_dependency()` |
| NEVER create self-dependencies | 3 (Prevent) | CHECK constraint `task_id != depends_on_task_id` |
| NEVER create task in non-existent project | 3 (Prevent) | FK constraint + application check |
| NEVER interpret content | 1 (Declare) | System prompt |
| NEVER suggest priorities | 1 (Declare) | System prompt |
| ALWAYS validate FK before writing | 2 (Detect) | Application-level validation in tools |
| ALWAYS produce null-state output | 1 (Declare) | Tool implementation + system prompt |
| ALWAYS confirm archival | 1 (Declare) | System prompt |
| ALWAYS log write operations | 2 (Detect) | `agent_instructions` table |

### Progressive Autonomy Tracking

**Q43: What are the autonomy phases for this agent?**

| Phase | Duration | Behaviour | Human Verification |
|-------|----------|-----------|-------------------|
| Shadow | Week 1-2 | Agent shows planned action before executing | Human reviews every action |
| Advisory | Week 3-4 | Agent executes and shows results | Human reviews archival and major updates |
| Supervised | Week 5-8 | Agent handles all CRUD | Human confirms archival only |
| Autonomous | Week 9+ | Agent handles all routine operations | Human monitors Trust Ledger quarterly |

**Q44: What metrics determine promotion to the next phase?**

| Metric | Shadow → Advisory | Advisory → Supervised | Supervised → Autonomous |
|--------|-------------------|----------------------|------------------------|
| Data accuracy rate | 100% of reviewed actions | 99.9% over 2 weeks | 99.9% over 4 weeks |
| Interpretation violations | 0 over 2 weeks | 0 over 2 weeks | 0 over 4 weeks |
| Unauthorised access attempts | 0 | 0 | 0 |
| Null-state output compliance | 100% | 100% | 100% |

**Q45: Who decides promotion?**

The human (Peter) decides based on Trust Ledger review. No automatic promotion — the metrics inform the decision, but human judgment determines when trust is earned.

**Q46: Can autonomy be demoted? What triggers demotion?**

| Trigger | Demotion |
|---------|----------|
| Data accuracy drops below 99% | Back to Supervised |
| Any interpretation violation (agent suggests priorities) | Back to Advisory |
| Any data loss or corruption | Back to Shadow |
| Any unauthorised access bypass | Back to Shadow |
| 3+ unauthorised access attempts in a week | Back to Advisory |

### Health Monitoring & Cost Tracking

**Q47: What health metrics does this agent need to track?**

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Data accuracy rate | 100% | <99.5% | <99% |
| Query response time | <2s | >5s | >10s |
| Write operation success rate | 99.9% | <99% | <98% |
| Unauthorised access attempts | 0/week | >3/week | >5/week |
| Null-state output compliance | 100% | <100% | <100% |
| Archival vs deletion ratio | 100% archival, 0% deletion | Any deletion | Any deletion |

**Q48: How will you measure each metric?**

| Metric | Measurement Method | Frequency |
|--------|-------------------|-----------|
| Data accuracy | Human spot-check: compare 5 random records against source of truth | Weekly during Shadow/Advisory, monthly during Supervised/Autonomous |
| Query response time | Application-level timing in toolkit (add timing middleware) | Continuous |
| Write success rate | Count successful vs failed write operations in audit trail | Weekly |
| Unauthorised access | Count entries in `agent_instructions` with `status='denied'` | Weekly |
| Null-state compliance | Automated test: query for non-existent records and verify clear message | Weekly during Shadow, monthly after |
| Archival/deletion | Database trigger count: any DELETE attempt triggers an alert (currently blocks, so this should always be 0) | Continuous |

**Q49: What are the alert thresholds?**

| Level | Threshold | Action |
|-------|-----------|--------|
| 🟢 Healthy | All metrics at target | Continue current autonomy |
| 🟡 Warning | Any metric at warning level | Increase monitoring, review in next Trust Ledger |
| 🔴 Critical | Any metric at critical level | Immediate review, consider demotion |

**Q50: How will token costs be tracked?**

| Method | Detail |
|--------|--------|
| Per-interaction | Agno AgentOS tracks tokens per run. Accumulate in Implementation Map `cost_budget_actual`. |
| Per-session | Sum of all interactions in a session. Warn at 40K tokens, halt at 60K tokens. |
| Cumulative | Track total tokens across all sessions for monthly cost analysis. |

**Q51: What happens when cost budget is exceeded?**

| Budget | Threshold | Action |
|--------|-----------|--------|
| Per-interaction | 5,000 tokens | No limit (CRUD operations are cheap) |
| Per-session | 40,000 tokens | ⚠️ Warning message to user: "This session has used {X} tokens." |
| Per-session | 60,000 tokens | 🛑 Halt: "Session token budget exceeded. Please start a new session." |

---

## Summary: What Needs to Be Built

Based on the 51 answers, here's what's already built vs what still needs implementation:

| Element | Status | What's Built | What's Needed |
|---------|--------|-------------|---------------|
| 1. Subtask → Tool Mapping | ✅ Complete | 13 subtasks → 13 tools, 1:1 | — |
| 2. CC → Implementation Mapping | 🟡 Partial | CC-4, CC-8 implemented | CC-1, CC-3, CC-5, CC-7 need implementation |
| 3. Data Schema Design | ✅ Complete | Private schema with 5 tables, triggers, indexes | — |
| 4. Tool Authority Boundaries | ✅ Complete | 13 tools with CAN/NEVER/null-state/error | — |
| 5. System Message Design | ✅ Complete | 20-line system prompt | — |
| 6. Model & Reasoning Config | ✅ Complete | `Ollama(id="glm-5.1:cloud")`, no reasoning | — |
| 7. Session & Memory Config | ✅ Complete | PostgresDb, history=10, no memory | — |
| 8. Inter-Agent Communication | ✅ Complete | MCP server, authorised_agents table, audit trail | — |
| 9. Human Interface Design | ✅ Complete | Chat (primary), Web UI (secondary), API (tertiary) | — |
| 10. Progressive Autonomy Tracking | ❌ Not built | Design defined, 4 phases | Runtime tracking of autonomy level and metrics |
| 11. Health Monitoring & Cost Tracking | ❌ Not built | Design defined, targets set | Measurement middleware, Trust Ledger, cost tracking |
| 12. Infrastructure Inventory | ✅ Complete | Documented above | Needs to be formalised into the Infrastructure Registry table |

The first 9 elements are implemented and running. Elements 10-12 are designed but need code.

---

## Run 11 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T05:16:41* · `glm-5.1:cloud` · `503fd190...`

### Prompt

great. so we now have this completed template. What should be the next steps?

### Response

Three paths forward, depending on what you want to optimise for:

## Option A: Lock Down the Foundation (Highest Value Long-Term)

Update the schemas before building anything else on them.

**Step 1: Update the design spec schema** — Add the missing fields we identified (output authority boundaries, quality gates, failure event details, self-evaluation resolution, epistemic metadata, specification aging).

**Step 2: Update the Agno spec schema** — Add the bridge fields (design_spec_id, design_spec_version, implementation_map_id, agent_class, agent_orientation, progressive_autonomy_level, authority_boundaries, information_boundaries, cost budgets, spec_aging_last_review).

**Step 3: Create the implementation map table** — The bridge between WHY and HOW. This is the missing piece that makes the three-layer architecture work.

**Step 4: Create the infrastructure registry table** — So the next agent can look up what already exists and reuse it first.

**Why this first:** Every future agent design will depend on these schemas being right. Fixing them later means migrating data. Getting them right now means the CAWDP Design Studio can trust its data model.

---

## Option B: Validate the Implementation (Fastest Feedback)

Test the Project Manager end-to-end before building more infrastructure.

**Step 1: Run the Project Manager agent** — Start PostgreSQL, apply the schema, run the setup script, start the agent, test all 13 tools through conversation.

**Step 2: Test against the design spec** — Walk through each of the 51 answers and verify the implementation matches.

**Step 3: Test the hard constraints** — Specifically test the "NEVER" list: try to delete a record (should fail), ask "what should I work on next" (should get data only), send an ambiguous instruction (should ask for clarification).

**Step 4: Test the null-state outputs** — Query for non-existent projects, empty task lists, etc.

**Step 5: Test inter-agent communication** — Set up a second agent that connects via MCP and tries to create a task through the Project Manager.

**Why this now:** The implementation is only as good as its test coverage. Finding bugs now is cheaper than finding them after the schema is formalised and other agents depend on it.

---

## Option C: Design the Next Agent (Build Momentum)

Use the infrastructure registry to decide what to build next, then apply the same template.

**Step 1: Look at the infrastructure registry** — What's already built? What's the next agent that can reuse the most existing infrastructure?

**Step 2: Pick the next agent** — Based on the Small Business Agentic Operating System design, the next logical agents would be:
- **Client Agent** (Extractor — reads client data, never judges) — can reuse PostgreSQL
- **Financial Agent** (Measurer — tracks financial metrics, never interprets) — can reuse PostgreSQL
- **Knowledge/Learning Agent** (Aggregator — captures and organises institutional memory) — can reuse PostgreSQL + needs Chroma for embeddings

**Step 3: Apply the 51-question template** — Walk through every question for the new agent, checking the infrastructure registry first.

**Why this now:** Each agent you build validates the template and the process. The second agent will reveal gaps that the first agent didn't expose.

---

## My Recommendation

**Do A first, then B, then C.** Here's why:

The schema updates are the foundation. Everything else builds on them. If you build the infrastructure registry and implementation map tables first, then every subsequent agent design automatically captures the design-to-code traceability that's currently missing. And the infrastructure registry means every new agent starts by checking what exists — which is exactly the "reuse first" principle we've been designing for.

The specific sequence:

```
1. Update design spec schema (missing fields)
2. Update Agno spec schema (bridge fields)
3. Create implementation map table
4. Create infrastructure registry table
5. Populate infrastructure registry with what's running now
6. Test the Project Manager end-to-end
7. Design the next agent using the full template
```

Steps 1-4 are schema changes — probably a day's work. Step 5 is data entry. Step 6 is testing. Step 7 is where the momentum builds.

Which path do you want to take?

---

## Run 12 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T05:21:34* · `glm-5.1:cloud` · `e55cf4ad...`

### Prompt

This is my coding agent's implementation plan for the infrastructure registry. I'd like your feedback on it.

```
# Plan: Infrastructure Registry for Agent Resources

> **Status**: Draft
> **Created**: 2026-04-30
> **Source**: Implementation Elements (Element 12), Project Manager reference implementation, Agent Spec schemas

## TL;DR

Create dedicated database tables to track existing infrastructure (models, databases, knowledge bases, tools, toolkits, hooks, memory, session stores) so agents can discover and reuse what exists before suggesting new infrastructure. Includes a junction table for agent-resource relationships with authority boundaries and CC enforcement tracking, JSONB convenience references in AgentSpec, design-spec linkage, auto-registration from agent specs, and a custom Agno Toolkit for runtime queries.

---

## Steps

### Phase 1: Models & Enums

1. **Add infrastructure enums to `db/enums.py`**
   - `ResourceTypeEnum`: database, model, knowledge_base, tool, toolkit, hook, memory, session_store
   - `ResourceStatusEnum`: active, inactive, deprecated
   - `ModelProviderEnum`: openai, anthropic, google, ollama, aws, azure, etc.
   - `SearchTypeEnum`: vector, keyword, hybrid
   - `ToolTypeEnum`: mcp, custom, builtin
   - `HookTypeEnum`: pre, post, tool
   - `MemoryTypeEnum`: agentic, session_summary, custom
   - `AccessRoleEnum`: primary, fallback, optional
   - `AccessPermissionEnum`: read, read_write
   - `AutonomyLevelEnum`: shadow, advisory, supervised, autonomous

2. **Add infrastructure models to `db/models.py`**
   - `InfrastructureModel` table — LLM models (provider, model_name, context_window, capabilities JSONB, cost_per_input_token, cost_per_output_token, cost_budget_per_interaction, cost_budget_per_session, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureDatabase` table — database instances (db_type, host, port, database_name, vector_support, connection_config JSONB [masked — no passwords], health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureKnowledgeBase` table — knowledge bases (name, vector_db_type, table_name, search_type, embedder_model, contents_table, config JSONB, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureTool` table — individual tools (tool_type, name, description, subtask_mapping JSONB [{subtask_id, authority_boundary, cognitive_class}], config JSONB, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureToolkit` table — tool collections (name, description, config JSONB, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureHook` table — hooks (hook_type, name, description, config JSONB, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureMemory` table — memory configs (memory_type, persistence_type, history_config JSONB, memory_scope, session_state_config JSONB, config JSONB, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureSessionStore` table — session stores (store_type, persistence_type, history_config JSONB, config JSONB, health_metrics JSONB, cc_enforcement JSONB, status, last_reviewed_at, next_review_due)
   - `AgentResource` junction table — (agent_id, resource_type, resource_id, access_role, access_permission, min_autonomy_level, authority_boundary JSONB [{can, never, failure_mode, null_state}], cc_enforcement JSONB, status)
   - `InfrastructureAuthorisedAgent` table — (agent_id, agent_name, permission, created_at, updated_at) — controls who can modify the registry (CC-4 Regime 3)
   - `InfrastructureAuditLog` table — (agent_id, action, resource_type, resource_id, details JSONB, status, created_at, completed_at) — CC-8 audit trail at Logged level
   - All tables use `ai` schema, append-only versioning, and timestamps like existing models

3. **Add indexes to `db/models_indexes.py`**
   - Per-resource-type status indexes
   - AgentResource composite indexes on (agent_id, resource_type), (resource_type, resource_id)
   - Per-resource-type last_reviewed_at indexes for spec aging queries

4. **Add columns to existing models**
   - `AgentSpec`: add `infrastructure_refs` JSONB (denormalized summary), `design_spec_id` String, `design_spec_version` BigInteger, `progressive_autonomy_level` String (default "shadow"), `agent_class` String, `agent_orientation` String, `authority_boundaries` JSONB, `information_boundaries` JSONB, `cost_budget_per_interaction` JSONB, `cost_budget_per_session` JSONB, `last_reviewed_at` BigInteger, `next_review_due` BigInteger
   - `AgentDesignSpec`: add `last_reviewed_at` BigInteger, `next_review_due` BigInteger

### Phase 2: CRUD Helpers

5. **Create `db/infrastructure.py`** — CRUD helpers for all 8 infrastructure tables
   - `register_model()`, `get_model()`, `list_models()`, `deactivate_model()`
   - `register_database()`, `get_database()`, `list_databases()`, `deactivate_database()`
   - `register_knowledge_base()`, `get_knowledge_base()`, `list_knowledge_bases()`, `deactivate_knowledge_base()`
   - `register_tool()`, `get_tool()`, `list_tools()`, `deactivate_tool()`
   - `register_toolkit()`, `get_toolkit()`, `list_toolkits()`, `deactivate_toolkit()`
   - `register_hook()`, `get_hook()`, `list_hooks()`, `deactivate_hook()`
   - `register_memory()`, `get_memory()`, `list_memories()`, `deactivate_memory()`
   - `register_session_store()`, `get_session_store()`, `list_session_stores()`, `deactivate_session_store()`
   - Each register function accepts `cc_enforcement` and `health_metrics` JSONB params
   - Each list function supports filtering by status, and date-range filtering on `last_reviewed_at`/`next_review_due` for spec aging queries

6. **Create `db/agent_resources.py`** — CRUD helpers for the junction table
   - `link_resource(agent_id, resource_type, resource_id, role, permission, min_autonomy_level, authority_boundary, cc_enforcement)` — create agent-resource link with full metadata
   - `unlink_resource(agent_id, resource_type, resource_id)` — remove link
   - `get_agent_resources(agent_id)` — get all resources for an agent (with authority boundaries)
   - `get_resource_agents(resource_type, resource_id)` — get all agents using a resource
   - `auto_register_from_agent_spec(agent)` — extract resources from a live Agent and register them + create links (including authority boundaries from the agent's design spec if available)

7. **Update `db/__init__.py`** — export all new functions and enums

### Phase 3: Auto-Registration & Design-Spec Linkage

8. **Update `db/agent_specs.py` `register_agent_spec()`** to also call `auto_register_from_agent_spec()`
   - Extract model info → register or link to InfrastructureModel
   - Extract db info → register or link to InfrastructureDatabase
   - Extract knowledge info → register or link to InfrastructureKnowledgeBase
   - Extract tools info → register or link to InfrastructureTool
   - Extract hooks info → register or link to InfrastructureHook
   - Extract memory info → register or link to InfrastructureMemory
   - Populate `infrastructure_refs` JSONB on the AgentSpec row
   - Set `design_spec_id` and `design_spec_version` if a matching design spec exists
   - Set `progressive_autonomy_level`, `agent_class`, `agent_orientation` from design spec if linked

9. **Update `app/main.py`** — call `init_infrastructure_tables()` alongside existing `init_agent_specs_table()`

10. **Update `db/agent_specs.py`** — add `link_design_spec(agent_id, design_spec_id, design_spec_version)` helper to formalise the design→implementation bridge

### Phase 4: Agent Toolkit & Schema

11. **Create `db/infrastructure_schema.sql`** — DDL with database-level enforcement (following PM pattern from `docs/agent-specs/project-manager/schema.sql`)
    - All table CREATE statements with CHECK constraints for enums
    - `prevent_infrastructure_delete()` trigger — archive-only, no DELETE (CC-4 Regime 3)
    - `update_timestamp()` trigger — auto-update `updated_at`
    - `prevent_duplicate_resource_registration()` trigger — prevent registering same resource twice
    - Indexes for status, resource_type, last_reviewed_at, next_review_due
    - Seed `infrastructure_authorised_agents` with `human_owner` as initial authorised user
    - All tables in `ai` schema (shared infrastructure, not agent-private)

12. **Create `agents/infrastructure_agent.py`** — a lightweight agent with `InfrastructureRegistryToolkit` (following PM pattern from `docs/agent-specs/project-manager/toolkit.py`)
    - `InfrastructureRegistryToolkit` as Agno `Toolkit` subclass with individual methods:
      - `list_models(status, provider)` — CAN: return matching models; NEVER: fabricate, filter by importance
      - `get_model(model_id)` — CAN: return exact model details; NEVER: suggest alternatives
      - `list_databases(status, db_type)` — CAN: return matching databases; NEVER: fabricate
      - `get_database(database_id)` — CAN: return exact database details; NEVER: expose credentials
      - `list_knowledge_bases(status)` — CAN: return matching knowledge bases; NEVER: fabricate
      - `list_tools(tool_type)` — CAN: return matching tools; NEVER: fabricate
      - `list_toolkits()` — CAN: return all toolkits; NEVER: fabricate
      - `query_agent_resources(agent_id)` — CAN: return all resources for an agent; NEVER: hide resources
      - `query_resource_agents(resource_type, resource_id)` — CAN: return all agents using a resource; NEVER: fabricate
    - Each tool returns structured JSON with `success`/`error`/`count`/`message` fields
    - Each tool has explicit null-state outputs (e.g., "No models found matching those criteria")
    - Agent instructions: help other agents find existing infrastructure before creating new; enforce "reuse first, build new second"

13. **Register the infrastructure agent in `app/main.py`**
    - Add to agents list
    - Add quick prompts to `app/config.yaml`

### Phase 5: Seed & Verification

14. **Create `scripts/seed_infrastructure.py`** — seed script to populate initial infrastructure from existing agents
    - Register gpt-5.2 as a model (with cost info)
    - Register the edgeos-db PostgresDb as a database (with masked connection info)
    - Register the knowledge_agent_docs knowledge base
    - Register MCPTools as a tool (with subtask_mapping from design spec if available)
    - Link all to their respective agents with authority boundaries
    - Set cc_enforcement for each resource where applicable
    - Seed `infrastructure_authorised_agents` with `human_owner`

15. **Verification steps**
    - Run `./scripts/validate.sh` — lint + type check passes
    - Run `./scripts/format.sh` — formatting passes
    - Start Docker (`docker compose up -d --build`) and verify tables created in `ai` schema
    - Run seed script and verify data in all tables
    - Query agent_resources to confirm knowledge-agent and mcp-agent have correct resource links with authority boundaries
    - Test infrastructure tool query from agent chat
    - Verify design_spec_id linkage on AgentSpec rows
    - Verify spec aging queries work (resources past next_review_due)
    - Verify archive-only trigger prevents DELETE on infrastructure tables
    - Verify audit log captures registry mutations

---

## Relevant files

| File | Action |
|------|--------|
| `db/models.py` | Add 11 new ORM models (8 infrastructure + 1 junction + 1 authorised agents + 1 audit log) + add columns to AgentSpec and AgentDesignSpec |
| `db/enums.py` | Add 10 new enum types (including AccessPermissionEnum, AutonomyLevelEnum) |
| `db/models_indexes.py` | Add indexes for new tables + spec aging indexes |
| `db/infrastructure_schema.sql` | **New**: DDL with triggers, constraints, seed data (following PM pattern) |
| `db/infrastructure.py` | **New**: CRUD for all 8 infrastructure tables |
| `db/agent_resources.py` | **New**: Junction table CRUD + auto-registration + authority boundaries |
| `db/agent_specs.py` | Update `register_agent_spec()` for auto-registration + design-spec linkage |
| `db/__init__.py` | Export new functions and enums |
| `agents/infrastructure_agent.py` | **New**: Agent with InfrastructureRegistryToolkit |
| `app/main.py` | Register infrastructure agent + init tables |
| `app/config.yaml` | Add quick prompts for infrastructure agent |
| `scripts/seed_infrastructure.py` | **New**: Seed initial data with authority boundaries and CC enforcement |

---

## Decisions

| Decision | Rationale |
|----------|-----------|
| Separate tables per resource type | Type safety & query clarity over polymorphic table |
| Both junction table + JSONB refs | Junction table is source of truth; JSONB on AgentSpec for convenience |
| Auto-registration + manual CRUD | Agents auto-register; manual CRUD for pre-seeding/admin |
| Agent Toolkit pattern | `InfrastructureRegistryToolkit` as Agno `Toolkit` subclass (following PM pattern), not loose functions |
| Append-only versioning | Consistent with existing AgentSpec/AgentDesignSpec pattern |
| `ai` schema | Infrastructure tables in shared `ai` schema (not agent-private like PM's `project_manager` schema) |
| Database-level enforcement | `infrastructure_schema.sql` with triggers for archive-only, timestamps, duplicate prevention (following PM pattern) |
| Authorised agents table | `InfrastructureAuthorisedAgent` controls who can modify the registry (CC-4 Regime 3) |
| Audit log | `InfrastructureAuditLog` tracks all registry mutations (CC-8 at Logged level) |
| Fail-safe defaults | status="active", access_role="primary", autonomy_level="shadow" |
| Design-spec linkage | AgentSpec gets `design_spec_id` + `design_spec_version` to bridge WHY→HOW |
| Authority boundaries on junction table | Each agent-resource link carries `{can, never, failure_mode, null_state}` |
| CC enforcement tracking | Each resource carries `cc_enforcement` JSONB mapping CCs to Declare/Detect/Prevent regimes |
| Spec aging | `last_reviewed_at` and `next_review_due` on all infrastructure tables + AgentDesignSpec |
| Progressive autonomy | `min_autonomy_level` on AgentResource, `progressive_autonomy_level` on AgentSpec |
| Cost tracking | Typed cost columns on InfrastructureModel, cost budgets on AgentSpec |
| Connection string masking | InfrastructureDatabase stores host/port/db name only, references env vars for credentials |
| Null-state outputs | Every tool has explicit null-state outputs (following PM pattern) |

---

## Further Considerations

1. **Tool availability at runtime**: The infrastructure tool needs to be added to agents that should discover resources. Should it be added to all agents by default, or only on request?
2. **Migration strategy**: Since this is early-stage, direct table creation via `create(checkfirst=True)` is fine (matches existing pattern). For production, consider Alembic migrations.
3. **Authority boundary templates**: Consider creating templates for common resource types (e.g., a database authority boundary template that says "CAN: read/write records; NEVER: drop tables, modify schema") that can be auto-populated during registration.
4. **CC enforcement validation**: Consider a validation step that checks whether declared CC enforcement regimes are actually implemented (e.g., if CC-4 says "Prevent", verify that the database schema has the prevention triggers).

---

## Project Manager Implementation Patterns to Adopt

The project manager (`docs/agent-specs/project-manager/`) is a fully working reference implementation. Key patterns to adopt:

### Toolkit Pattern (from `toolkit.py`)
- Create `InfrastructureRegistryToolkit` as an Agno `Toolkit` subclass (not loose functions)
- Each tool method has explicit CAN/NEVER authority boundaries in docstrings
- Each tool returns structured JSON with `success`/`error`/`count`/`message` fields
- Each tool has explicit null-state outputs (e.g., "No models found matching those criteria")
- Connection handling via psycopg with proper error handling and connection cleanup

### Schema SQL (from `schema.sql`)
- Create `db/infrastructure_schema.sql` alongside ORM models for database-level enforcement
- Add triggers: `prevent_infrastructure_delete()` (archive-only, like PM), `update_timestamp()`
- Add CHECK constraints for all status enums at the database level
- Add UNIQUE constraints to prevent duplicate resource registration
- Seed `infrastructure_authorised_agents` with `human_owner` as initial authorised user

### Authorised Agents (from PM `authorised_agents` table)
- Add `infrastructure_authorised_agents` table: (id, agent_id, agent_name, permission, created_at, updated_at)
- Only authorised agents can modify the registry (CC-4 at Regime 3)
- Seed with `human_owner` with `read_write` permission

### Audit Trail (from PM `agent_instructions` table)
- Add `infrastructure_audit_log` table: (id, agent_id, action, resource_type, resource_id, details, status, created_at, completed_at)
- Log all registry mutations: who changed what, when, and why (CC-8 at Logged level)

### Null-State Outputs (from PM toolkit)
Every infrastructure tool must define explicit null-state outputs:
- `list_models` → `{"models": [], "message": "No models found matching those criteria"}`
- `get_model` → `{"error": "Model {id} not found"}`
- `query_agent_resources` → `{"resources": [], "message": "No resources found for agent {agent_id}"}`
- `query_resource_agents` → `{"agents": [], "message": "No agents found using {resource_type} {resource_id}"}`

---

## Implementation Elements Mapping

This plan addresses the 12 Implementation Elements (from `docs/agent-specs/implementation-elements.md`) as follows:

| Element | How Addressed |
|---------|--------------|
| **1. Subtask → Tool Mapping** | `subtask_mapping` JSONB on `InfrastructureTool` links each tool to design spec subtasks |
| **2. CC → Implementation Mapping** | `cc_enforcement` JSONB on every infrastructure table AND `AgentResource` junction |
| **3. Data Schema Design** | 11 new ORM models + `infrastructure_schema.sql` with triggers and constraints |
| **4. Tool Authority Boundaries** | `authority_boundary` JSONB on `AgentResource` with `{can, never, failure_mode, null_state}` |
| **5. System Message Design** | Infrastructure agent instructions enforce "reuse first, build new second" |
| **6. Model & Reasoning Configuration** | `InfrastructureModel` table with provider, model_name, cost info |
| **7. Session & Memory Configuration** | `InfrastructureMemory` and `InfrastructureSessionStore` with typed columns |
| **8. Inter-Agent Communication** | `InfrastructureAuthorisedAgent` table + `access_permission` on `AgentResource` |
| **9. Human Interface Design** | Out of scope (future: read-only dashboard) |
| **10. Progressive Autonomy Tracking** | `min_autonomy_level` on `AgentResource`, `progressive_autonomy_level` on `AgentSpec` |
| **11. Health Monitoring & Cost Tracking** | `health_metrics` JSONB on every table, typed cost columns on `InfrastructureModel` |
| **12. Infrastructure Inventory & Reuse** | This IS the plan — the entire registry |

### Design-Spec Bridge (from `docs/agent-specs/notes-on-agent-spec-schemas.md`)

| Gap Identified | How Addressed |
|----------------|---------------|
| No link between design spec and agent spec | `design_spec_id` + `design_spec_version` on `AgentSpec`, `link_design_spec()` helper |
| Missing `progressive_autonomy_level` | Added to `AgentSpec` (default "shadow") |
| Missing `agent_class` and `agent_orientation` | Added to `AgentSpec` |
| Missing `authority_boundaries` and `information_boundaries` | Added as JSONB on `AgentSpec` |
| Missing `cost_budget_per_interaction/session` | Added as JSONB on `AgentSpec` |
| Missing `last_reviewed_at` and `next_review_due` | Added to `AgentDesignSpec` and all infrastructure tables |
| Tools/knowledge not queryable | `AgentResource` junction table + `InfrastructureTool`/`InfrastructureKnowledgeBase` tables |
```

### Response

This is thorough and well-structured. It clearly follows the Project Manager patterns, addresses the 12 implementation elements, and builds the design-spec bridge. Here's my feedback organised into three categories: **corrections**, **additions**, and **refinements**.

---

## Corrections — Things That Should Change

### 1. `cc_enforcement` and `health_metrics` are on the wrong tables

Currently both are on every infrastructure table (InfrastructureModel, InfrastructureDatabase, etc.). But CC enforcement and health metrics are properties of the **agent's relationship with the resource**, not the resource itself.

A database doesn't have CC enforcement — it's the agent's USE of the database that enforces CC-4. A model doesn't have health metrics — it's the agent's INTERACTION with the model that has health metrics.

**Move both to the `AgentResource` junction table** where they already have `cc_enforcement` and should also have `health_metrics`. Remove them from the individual infrastructure tables.

The infrastructure tables should contain only what the resource IS (its identity and configuration). The junction table should contain how the agent RELATES to it (authority, enforcement, health).

```
InfrastructureModel:  id, provider, model_name, context_window, capabilities,
                      cost_per_input_token, cost_per_output_token, status, ...

AgentResource:        agent_id, resource_type, resource_id, access_role,
                      access_permission, min_autonomy_level,
                      authority_boundary JSONB,    ← stays
                      cc_enforcement JSONB,         ← stays
                      health_metrics JSONB,         ← ADD HERE
                      cost_budget_per_interaction,  ← ADD HERE (agent's budget for this resource)
                      cost_budget_per_session,      ← ADD HERE
                      status
```

### 2. The Implementation Map table is missing

This is the most critical gap. We designed a three-layer architecture:

```
Design Spec (WHY)  →  Implementation Map (HOW)  →  Agno Agent Spec (WHAT)
```

The plan has the Design Spec updates and the Agno Spec updates, but **not the Implementation Map table itself**. This is the table that holds:

- `subtask_tool_map` — which design-spec subtask maps to which tool
- `cc_implementation_map` — which CC maps to which implementation mechanism
- `database_schemas` — which schema files implement this agent's data layer
- `tool_registry` — all tools with authority boundaries
- `infrastructure_dependencies` — what infrastructure this agent depends on
- `inter_agent_interfaces` — MCP endpoints, authorised agents
- `human_interfaces` — chat, web UI, API
- `progressive_autonomy_level` — current phase and history
- `cost_budget_actual` — actual cost tracking
- `health_metrics_actual` — actual health measurements
- `design_decisions` — key decisions with rationale and alternatives
- `implementation_files` — references to code files

Without this table, the three-layer architecture has a hole in the middle. The `design_spec_id` and `design_spec_version` on AgentSpec point to the design spec, but there's nothing pointing to the implementation decisions that bridge the two.

**Add an `ImplementationMap` model** with all the fields from the earlier schema draft.

### 3. The Infrastructure Agent's purpose needs clarity

The plan says it's "a lightweight agent with InfrastructureRegistryToolkit" that "helps other agents find existing infrastructure before creating new." But there are two different use cases:

**Use case A: Discovery** — Another agent queries the registry at design time: "What databases exist? What models are available?" This is a read-only discovery service.

**Use case B: Registration** — A new agent's infrastructure is registered when it's deployed: "The Project Manager uses PostgreSQL, register that." This is a write operation.

These might be the same agent (the Infrastructure Agent), but the authority boundaries are different:

- Discovery (read): Any agent should be able to query
- Registration (write): Only authorised agents should be able to modify the registry

The current `authorised_agents` table handles this, but the toolkit methods listed are all read methods (`list_models`, `get_model`, etc.). **Where are the write methods?** The CRUD helpers in `db/infrastructure.py` handle writes, but how do they get invoked through the agent?

**Recommendation:** Either add write methods to the toolkit (with authority checks), or make the toolkit read-only and handle registration through the auto-registration pipeline only.

---

## Additions — Things That Should Be Added

### 4. The infrastructure agent needs write tools (or a clear decision not to have them)

Following on from point 3: if the infrastructure agent is read-only (discovery only), then registration happens through:

1. Auto-registration when an agent spec is saved (Step 8 in the plan)
2. Manual seed scripts (Step 14)
3. Manual CRUD through the Python helpers (not through the agent)

This is a valid design choice — the agent is for discovery, registration is programmatic. But it should be explicit.

**Recommendation:** Make the infrastructure agent read-only (discovery only). Registration happens through auto-registration and seed scripts. This keeps the agent's authority boundaries simple and consistent with the PM pattern.

### 5. Authority boundaries for the infrastructure agent

The toolkit has CAN/NEVER boundaries for each tool, but the agent as a whole needs explicit boundaries too:

- CAN: Query available infrastructure, list resources, return details
- NEVER: Suggest which resource to use, recommend one over another, modify resource configurations, register new resources (that's programmatic, not through the agent)

### 6. Design decision logging

The Implementation Map should have a `design_decisions` field that captures key decisions with rationale. For example, for the Project Manager:

```json
[
  {
    "decision": "Private Postgres schema for data isolation",
    "rationale": "CC-4 Information Boundaries enforced at Regime 3",
    "design_spec_ref": "Section 7 hard_constraints #4",
    "alternatives_considered": ["Shared schema with row-level security", "Separate database"],
    "status": "implemented"
  }
]
```

This is the design-to-code traceability that makes the three-layer architecture work. Without it, you can't trace WHY a decision was made.

### 7. Who triggers spec aging reviews?

The plan has `last_reviewed_at` and `next_review_due` on all infrastructure tables and AgentDesignSpec. But who triggers the review? Options:

1. **The infrastructure agent** — it could periodically check for resources past their review date and alert
2. **A scheduled job** — a cron job or similar that checks daily
3. **Manual** — someone reviews on a schedule

**Recommendation:** Add a `query_resources_needing_review()` tool to the InfrastructureRegistryToolkit that returns all resources past their `next_review_due` date. This gives any agent (or human) the ability to check what needs review. Don't build automated alerting yet — that's a future enhancement.

### 8. Connection string security

The plan says "connection_config JSONB [masked — no passwords]" which is correct. But be explicit about the pattern:

```python
# In InfrastructureDatabase:
connection_config = {
    "host": "localhost",
    "port": 5532,
    "database": "ai",
    "user": "ai",
    # password: NOT STORED — reference env var
    "password_env_var": "POSTGRES_PASSWORD"
}
```

Never store credentials in the database. Reference environment variables by name, and resolve them at runtime.

---

## Refinements — Things That Could Be Better

### 9. Separate the infrastructure tables from the agent-specific tables

Currently the plan puts everything in the `ai` schema. That's fine for now, but consider this structure:

```
ai schema (shared):
  - infrastructure_model
  - infrastructure_database
  - infrastructure_knowledge_base
  - infrastructure_tool
  - infrastructure_toolkit
  - infrastructure_hook
  - infrastructure_memory
  - infrastructure_session_store
  - infrastructure_authorised_agent
  - infrastructure_audit_log

project_manager schema (agent-private):
  - projects, tasks, task_dependencies, etc.

agent_specs schema (design + config):
  - agent_design_specs
  - agent_specs
  - implementation_maps
  - agent_resources
```

The `agent_resources` junction table lives in the shared schema because it connects agents to infrastructure. The `implementation_maps` table lives in the specs schema because it's part of the design-to-code bridge.

### 10. The `subtask_mapping` on InfrastructureTool is premature

Registering subtask mappings on the infrastructure tool requires knowing the design spec subtask IDs at tool registration time. But tools are registered before (or independently of) design specs. This creates a chicken-and-egg problem.

**Recommendation:** Keep `subtask_mapping` on the Implementation Map (where it connects design spec subtasks to tools), not on the InfrastructureTool. The tool registry should describe what the tool IS (name, type, capabilities), not what design-spec subtask it maps to.

### 11. Auto-registration should be idempotent

The `auto_register_from_agent_spec()` function will be called every time an agent spec is saved. It needs to be idempotent — if the model/database/tool already exists, update it rather than creating a duplicate.

The `prevent_duplicate_resource_registration()` trigger helps, but the Python code should also handle the "already exists, update" case gracefully.

### 12. The seed script references need updating

The seed script references "gpt-5.2" as a model, but the default model is `glm-5.1:cloud` on Ollama. Make sure the seed data matches your actual infrastructure.

---

## Summary

| Category | Item | Priority |
|----------|------|----------|
| 🔴 Correction | Move `cc_enforcement` and `health_metrics` from infrastructure tables to AgentResource junction table | Must fix |
| 🔴 Correction | Add Implementation Map table (the HOW layer) | Must add |
| 🔴 Correction | Clarify whether infrastructure agent has write tools or is read-only | Must decide |
| 🟡 Addition | Add write tools to infrastructure agent OR make read-only decision explicit | Should add |
| 🟡 Addition | Add authority boundaries for the infrastructure agent as a whole | Should add |
| 🟡 Addition | Add `design_decisions` field to Implementation Map | Should add |
| 🟡 Addition | Add `query_resources_needing_review()` tool for spec aging | Should add |
| 🟡 Addition | Be explicit about connection string security pattern | Should add |
| 🟢 Refinement | Consider schema separation (shared vs agent-private vs specs) | Nice to have |
| 🟢 Refinement | Move `subtask_mapping` from InfrastructureTool to Implementation Map | Nice to have |
| 🟢 Refinement | Make auto-registration idempotent | Nice to have |
| 🟢 Refinement | Update seed data to match actual infrastructure | Nice to have |

The plan is solid. The three corrections are the critical ones — especially the Implementation Map table, which is the missing piece of the three-layer architecture we designed. Want me to draft the Implementation Map schema?

---

## Run 13 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T05:40:45* · `glm-5.1:cloud` · `cf825769...`

### Prompt

here is the updated infrastructure registry plan after your feedback:

# Plan: Infrastructure Registry for Agent Resources

> **Status**: Draft
> **Created**: 2026-04-30
> **Source**: Implementation Elements (Element 12), Project Manager reference implementation, Agent Spec schemas

## TL;DR

Create dedicated database tables to track existing infrastructure (models, databases, knowledge bases, tools, toolkits, hooks, memory, session stores) so agents can discover and reuse what exists before suggesting new infrastructure. Includes a junction table for agent-resource relationships with authority boundaries and CC enforcement tracking, JSONB convenience references in AgentSpec, design-spec linkage, auto-registration from agent specs, and a custom Agno Toolkit for runtime queries.

---

## Steps

### Phase 1: Models & Enums

1. **Add infrastructure enums to `db/enums.py`**
   - `ResourceTypeEnum`: database, model, knowledge_base, tool, toolkit, hook, memory, session_store
   - `ResourceStatusEnum`: active, inactive, deprecated
   - `ModelProviderEnum`: openai, anthropic, google, ollama, aws, azure, etc.
   - `SearchTypeEnum`: vector, keyword, hybrid
   - `ToolTypeEnum`: mcp, custom, builtin
   - `HookTypeEnum`: pre, post, tool
   - `MemoryTypeEnum`: agentic, session_summary, custom
   - `AccessRoleEnum`: primary, fallback, optional
   - `AccessPermissionEnum`: read, read_write
   - `AutonomyLevelEnum`: shadow, advisory, supervised, autonomous

2. **Add infrastructure models to `db/models.py`**
   - `InfrastructureModel` table — LLM models (provider, model_name, context_window, capabilities JSONB, cost_per_input_token, cost_per_output_token, status, last_reviewed_at, next_review_due)
     - Note: `cc_enforcement`, `health_metrics`, and `cost_budget` are on the AgentResource junction table, not here — they describe the agent's *relationship* with the model, not the model itself
   - `InfrastructureDatabase` table — database instances (db_type, host, port, database_name, vector_support, connection_config JSONB [masked — references env vars for passwords, never stores credentials], status, last_reviewed_at, next_review_due)
   - `InfrastructureKnowledgeBase` table — knowledge bases (name, vector_db_type, table_name, search_type, embedder_model, contents_table, config JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureTool` table — individual tools (tool_type, name, description, config JSONB, status, last_reviewed_at, next_review_due)
     - Note: `subtask_mapping` is on the ImplementationMap, not here — tools describe what they ARE, not which design-spec subtask they serve
   - `InfrastructureToolkit` table — tool collections (name, description, config JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureHook` table — hooks (hook_type, name, description, config JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureMemory` table — memory configs (memory_type, persistence_type, history_config JSONB, memory_scope, session_state_config JSONB, config JSONB, status, last_reviewed_at, next_review_due)
   - `InfrastructureSessionStore` table — session stores (store_type, persistence_type, history_config JSONB, config JSONB, status, last_reviewed_at, next_review_due)
   - `AgentResource` junction table — (agent_id, resource_type, resource_id, access_role, access_permission, min_autonomy_level, authority_boundary JSONB [{can, never, failure_mode, null_state}], cc_enforcement JSONB [{cc_id, regime, mechanism}], health_metrics JSONB [{metric, target, warning, critical}], cost_budget_per_interaction JSONB, cost_budget_per_session JSONB, status)
     - This is where agent-specific context lives: CC enforcement, health metrics, cost budgets, and authority boundaries are properties of the agent's *use* of a resource, not the resource itself
   - `ImplementationMap` table — bridges design spec (WHY) to agent spec (WHAT) with implementation decisions (HOW): (agent_id, design_spec_id, design_spec_version, subtask_tool_map JSONB, cc_implementation_map JSONB, database_schemas JSONB, tool_registry JSONB, infrastructure_dependencies JSONB, inter_agent_interfaces JSONB, human_interfaces JSONB, progressive_autonomy_level, cost_budget_actual JSONB, health_metrics_actual JSONB, design_decisions JSONB [{decision, rationale, design_spec_ref, alternatives_considered, status}], implementation_files JSONB, status, created_at, updated_at)
   - `InfrastructureAuthorisedAgent` table — (agent_id, agent_name, permission, created_at, updated_at) — controls who can modify the registry (CC-4 Regime 3)
   - `InfrastructureAuditLog` table — (agent_id, action, resource_type, resource_id, details JSONB, status, created_at, completed_at) — CC-8 audit trail at Logged level
   - All tables use `ai` schema, append-only versioning, and timestamps like existing models

3. **Add indexes to `db/models_indexes.py`**
   - Per-resource-type status indexes
   - AgentResource composite indexes on (agent_id, resource_type), (resource_type, resource_id)
   - Per-resource-type last_reviewed_at indexes for spec aging queries

4. **Add columns to existing models**
   - `AgentSpec`: add `infrastructure_refs` JSONB (denormalized summary), `design_spec_id` String, `design_spec_version` BigInteger, `progressive_autonomy_level` String (default "shadow"), `agent_class` String, `agent_orientation` String, `authority_boundaries` JSONB, `information_boundaries` JSONB, `cost_budget_per_interaction` JSONB, `cost_budget_per_session` JSONB, `last_reviewed_at` BigInteger, `next_review_due` BigInteger
   - `AgentDesignSpec`: add `last_reviewed_at` BigInteger, `next_review_due` BigInteger

### Phase 2: CRUD Helpers

5. **Create `db/infrastructure.py`** — CRUD helpers for all 8 infrastructure tables
   - `register_model()`, `get_model()`, `list_models()`, `deactivate_model()`
   - `register_database()`, `get_database()`, `list_databases()`, `deactivate_database()`
   - `register_knowledge_base()`, `get_knowledge_base()`, `list_knowledge_bases()`, `deactivate_knowledge_base()`
   - `register_tool()`, `get_tool()`, `list_tools()`, `deactivate_tool()`
   - `register_toolkit()`, `get_toolkit()`, `list_toolkits()`, `deactivate_toolkit()`
   - `register_hook()`, `get_hook()`, `list_hooks()`, `deactivate_hook()`
   - `register_memory()`, `get_memory()`, `list_memories()`, `deactivate_memory()`
   - `register_session_store()`, `get_session_store()`, `list_session_stores()`, `deactivate_session_store()`
   - Each register function is idempotent — if the resource already exists (by name+type), update it rather than creating a duplicate
   - Each list function supports filtering by status, and date-range filtering on `last_reviewed_at`/`next_review_due` for spec aging queries

6. **Create `db/agent_resources.py`** — CRUD helpers for the junction table
   - `link_resource(agent_id, resource_type, resource_id, role, permission, min_autonomy_level, authority_boundary, cc_enforcement, health_metrics, cost_budget_per_interaction, cost_budget_per_session)` — create agent-resource link with full metadata
   - `unlink_resource(agent_id, resource_type, resource_id)` — remove link
   - `get_agent_resources(agent_id)` — get all resources for an agent (with authority boundaries, CC enforcement, health metrics, cost budgets)
   - `get_resource_agents(resource_type, resource_id)` — get all agents using a resource
   - `auto_register_from_agent_spec(agent)` — extract resources from a live Agent and register them + create links (including authority boundaries from the agent's design spec if available). Must be idempotent — if resource already exists, update rather than duplicate.
   - `query_resources_needing_review()` — return all resources past their `next_review_due` date (for spec aging)

7. **Update `db/__init__.py`** — export all new functions and enums

### Phase 3: Auto-Registration & Design-Spec Linkage

8. **Update `db/agent_specs.py` `register_agent_spec()`** to also call `auto_register_from_agent_spec()`
   - Extract model info → register or link to InfrastructureModel
   - Extract db info → register or link to InfrastructureDatabase
   - Extract knowledge info → register or link to InfrastructureKnowledgeBase
   - Extract tools info → register or link to InfrastructureTool
   - Extract hooks info → register or link to InfrastructureHook
   - Extract memory info → register or link to InfrastructureMemory
   - Populate `infrastructure_refs` JSONB on the AgentSpec row
   - Set `design_spec_id` and `design_spec_version` if a matching design spec exists
   - Set `progressive_autonomy_level`, `agent_class`, `agent_orientation` from design spec if linked

9. **Update `app/main.py`** — call `init_infrastructure_tables()` alongside existing `init_agent_specs_table()`

10. **Update `db/agent_specs.py`** — add `link_design_spec(agent_id, design_spec_id, design_spec_version)` helper to formalise the design→implementation bridge

### Phase 4: Agent Toolkit & Schema

11. **Create `db/infrastructure_schema.sql`** — DDL with database-level enforcement (following PM pattern from `docs/agent-specs/project-manager/schema.sql`)
    - All table CREATE statements with CHECK constraints for enums
    - `prevent_infrastructure_delete()` trigger — archive-only, no DELETE (CC-4 Regime 3)
    - `update_timestamp()` trigger — auto-update `updated_at`
    - `prevent_duplicate_resource_registration()` trigger — prevent registering same resource twice
    - Indexes for status, resource_type, last_reviewed_at, next_review_due
    - Seed `infrastructure_authorised_agents` with `human_owner` as initial authorised user
    - All tables in `ai` schema (shared infrastructure, not agent-private)

12. **Create `agents/infrastructure_agent.py`** — a **read-only discovery agent** with `InfrastructureRegistryToolkit` (following PM pattern from `docs/agent-specs/project-manager/toolkit.py`)
    - **Design decision: The infrastructure agent is read-only (discovery only).** Registration happens through auto-registration (Step 8) and seed scripts (Step 14), not through the agent. This keeps the agent's authority boundaries simple and consistent with the PM pattern.
    - **Agent-level authority boundaries:**
      - CAN: Query available infrastructure, list resources, return details, return resources needing review
      - NEVER: Suggest which resource to use, recommend one over another, modify resource configurations, register new resources
    - `InfrastructureRegistryToolkit` as Agno `Toolkit` subclass with individual methods:
      - `list_models(status, provider)` — CAN: return matching models; NEVER: fabricate, filter by importance, suggest alternatives
      - `get_model(model_id)` — CAN: return exact model details; NEVER: suggest alternatives
      - `list_databases(status, db_type)` — CAN: return matching databases; NEVER: fabricate
      - `get_database(database_id)` — CAN: return exact database details; NEVER: expose credentials
      - `list_knowledge_bases(status)` — CAN: return matching knowledge bases; NEVER: fabricate
      - `list_tools(tool_type)` — CAN: return matching tools; NEVER: fabricate
      - `list_toolkits()` — CAN: return all toolkits; NEVER: fabricate
      - `query_agent_resources(agent_id)` — CAN: return all resources for an agent; NEVER: hide resources
      - `query_resource_agents(resource_type, resource_id)` — CAN: return all agents using a resource; NEVER: fabricate
      - `query_resources_needing_review()` — CAN: return resources past their review date; NEVER: modify review dates
    - Each tool returns structured JSON with `success`/`error`/`count`/`message` fields
    - Each tool has explicit null-state outputs (e.g., "No models found matching those criteria")
    - Agent instructions: help other agents find existing infrastructure before creating new; enforce "reuse first, build new second"

13. **Register the infrastructure agent in `app/main.py`**
    - Add to agents list
    - Add quick prompts to `app/config.yaml`

### Phase 5: Seed & Verification

14. **Create `scripts/seed_infrastructure.py`** — seed script to populate initial infrastructure from existing agents
    - Register `glm-5.1:cloud` (Ollama) as a model (with cost info) — matches the actual default model in `agents/knowledge_agent.py` and `agents/mcp_agent.py`
    - Register `gpt-5.2` (OpenAI) as a model (with cost info) — matches the model referenced in copilot-instructions
    - Register the edgeos-db PostgresDb as a database (with masked connection info — host/port/db name only, `password_env_var` reference)
    - Register the knowledge_agent_docs knowledge base
    - Register MCPTools as a tool
    - Link all to their respective agents with authority boundaries, cc_enforcement, health_metrics, and cost budgets on the AgentResource junction table
    - Seed `infrastructure_authorised_agents` with `human_owner`

15. **Verification steps**
    - Run `./scripts/validate.sh` — lint + type check passes
    - Run `./scripts/format.sh` — formatting passes
    - Start Docker (`docker compose up -d --build`) and verify tables created in `ai` schema
    - Run seed script and verify data in all tables
    - Query agent_resources to confirm knowledge-agent and mcp-agent have correct resource links with authority boundaries
    - Test infrastructure tool query from agent chat
    - Verify design_spec_id linkage on AgentSpec rows
    - Verify spec aging queries work (resources past next_review_due)
    - Verify archive-only trigger prevents DELETE on infrastructure tables
    - Verify audit log captures registry mutations

---

## Relevant files

| File | Action |
|------|--------|
| `db/models.py` | Add 12 new ORM models (8 infrastructure + 1 junction + 1 implementation map + 1 authorised agents + 1 audit log) + add columns to AgentSpec and AgentDesignSpec |
| `db/enums.py` | Add 10 new enum types (including AccessPermissionEnum, AutonomyLevelEnum) |
| `db/models_indexes.py` | Add indexes for new tables + spec aging indexes |
| `db/infrastructure_schema.sql` | **New**: DDL with triggers, constraints, seed data (following PM pattern) |
| `db/infrastructure.py` | **New**: CRUD for all 8 infrastructure tables |
| `db/agent_resources.py` | **New**: Junction table CRUD + auto-registration + authority boundaries + `query_resources_needing_review()` |
| `db/implementation_maps.py` | **New**: CRUD for ImplementationMap table (register, get, list) |
| `db/agent_specs.py` | Update `register_agent_spec()` for auto-registration + design-spec linkage |
| `db/__init__.py` | Export new functions and enums |
| `agents/infrastructure_agent.py` | **New**: Agent with InfrastructureRegistryToolkit |
| `app/main.py` | Register infrastructure agent + init tables |
| `app/config.yaml` | Add quick prompts for infrastructure agent |
| `scripts/seed_infrastructure.py` | **New**: Seed initial data with authority boundaries and CC enforcement |

---

## Decisions

| Decision | Rationale |
|----------|-----------|
| Separate tables per resource type | Type safety & query clarity over polymorphic table |
| Both junction table + JSONB refs | Junction table is source of truth; JSONB on AgentSpec for convenience |
| Auto-registration + manual CRUD | Agents auto-register; manual CRUD for pre-seeding/admin |
| Agent Toolkit pattern | `InfrastructureRegistryToolkit` as Agno `Toolkit` subclass (following PM pattern), not loose functions |
| Append-only versioning | Consistent with existing AgentSpec/AgentDesignSpec pattern |
| `ai` schema | Infrastructure tables in shared `ai` schema (not agent-private like PM's `project_manager` schema) |
| Database-level enforcement | `infrastructure_schema.sql` with triggers for archive-only, timestamps, duplicate prevention (following PM pattern) |
| Authorised agents table | `InfrastructureAuthorisedAgent` controls who can modify the registry (CC-4 Regime 3) |
| Audit log | `InfrastructureAuditLog` tracks all registry mutations (CC-8 at Logged level) |
| Fail-safe defaults | status="active", access_role="primary", autonomy_level="shadow" |
| Design-spec linkage | AgentSpec gets `design_spec_id` + `design_spec_version` to bridge WHY→HOW |
| Authority boundaries on junction table | Each agent-resource link carries `{can, never, failure_mode, null_state}` |
| CC enforcement tracking | `cc_enforcement` JSONB on `AgentResource` junction table (not on infrastructure tables — CC enforcement is about the agent's *use* of a resource, not the resource itself) |
| Spec aging | `last_reviewed_at` and `next_review_due` on all infrastructure tables + AgentDesignSpec |
| Progressive autonomy | `min_autonomy_level` on AgentResource, `progressive_autonomy_level` on AgentSpec |
| Cost tracking | Typed cost columns on InfrastructureModel (per-token costs), cost budgets on AgentResource junction table (per-agent budgets for each resource), cost budgets on AgentSpec |
| Connection string masking | InfrastructureDatabase stores host/port/db name only, references env vars for credentials |
| Null-state outputs | Every tool has explicit null-state outputs (following PM pattern) |

---

## Further Considerations

1. **Tool availability at runtime**: The infrastructure tool needs to be added to agents that should discover resources. Should it be added to all agents by default, or only on request?
2. **Migration strategy**: Since this is early-stage, direct table creation via `create(checkfirst=True)` is fine (matches existing pattern). For production, consider Alembic migrations.
3. **Authority boundary templates**: Consider creating templates for common resource types (e.g., a database authority boundary template that says "CAN: read/write records; NEVER: drop tables, modify schema") that can be auto-populated during registration.
4. **CC enforcement validation**: Consider a validation step that checks whether declared CC enforcement regimes are actually implemented (e.g., if CC-4 says "Prevent", verify that the database schema has the prevention triggers).
5. **Implementation Map population**: The `ImplementationMap` table needs a CRUD helper and a way to populate it. Consider adding `db/implementation_maps.py` with `register_implementation_map()`, `get_implementation_map()`, `list_implementation_maps()` in Phase 2.
6. **Schema separation**: Currently everything goes in the `ai` schema. Consider separating into `ai` (shared infrastructure), `agent_specs` (design + config + implementation maps), and agent-private schemas (like `project_manager`). This is a future consideration — not blocking for initial implementation.

---

## Project Manager Implementation Patterns to Adopt

The project manager (`docs/agent-specs/project-manager/`) is a fully working reference implementation. Key patterns to adopt:

### Toolkit Pattern (from `toolkit.py`)
- Create `InfrastructureRegistryToolkit` as an Agno `Toolkit` subclass (not loose functions)
- Each tool method has explicit CAN/NEVER authority boundaries in docstrings
- Each tool returns structured JSON with `success`/`error`/`count`/`message` fields
- Each tool has explicit null-state outputs (e.g., "No models found matching those criteria")
- Connection handling via psycopg with proper error handling and connection cleanup

### Schema SQL (from `schema.sql`)
- Create `db/infrastructure_schema.sql` alongside ORM models for database-level enforcement
- Add triggers: `prevent_infrastructure_delete()` (archive-only, like PM), `update_timestamp()`
- Add CHECK constraints for all status enums at the database level
- Add UNIQUE constraints to prevent duplicate resource registration
- Seed `infrastructure_authorised_agents` with `human_owner` as initial authorised user

### Authorised Agents (from PM `authorised_agents` table)
- Add `infrastructure_authorised_agents` table: (id, agent_id, agent_name, permission, created_at, updated_at)
- Only authorised agents can modify the registry (CC-4 at Regime 3)
- Seed with `human_owner` with `read_write` permission

### Audit Trail (from PM `agent_instructions` table)
- Add `infrastructure_audit_log` table: (id, agent_id, action, resource_type, resource_id, details, status, created_at, completed_at)
- Log all registry mutations: who changed what, when, and why (CC-8 at Logged level)

### Connection String Security (explicit pattern)
Never store credentials in the database. Reference environment variables by name, and resolve them at runtime:
```python
# In InfrastructureDatabase:
connection_config = {
    "host": "localhost",
    "port": 5532,
    "database": "ai",
    "user": "ai",
    # password: NOT STORED — reference env var
    "password_env_var": "POSTGRES_PASSWORD"
}
```

### Null-State Outputs (from PM toolkit)
Every infrastructure tool must define explicit null-state outputs:
- `list_models` → `{"models": [], "message": "No models found matching those criteria"}`
- `get_model` → `{"error": "Model {id} not found"}`
- `query_agent_resources` → `{"resources": [], "message": "No resources found for agent {agent_id}"}`
- `query_resource_agents` → `{"agents": [], "message": "No agents found using {resource_type} {resource_id}"}`
- `query_resources_needing_review` → `{"resources": [], "message": "No resources are past their review date"}`

---

## Implementation Elements Mapping

This plan addresses the 12 Implementation Elements (from `docs/agent-specs/implementation-elements.md`) as follows:

| Element | How Addressed |
|---------|--------------|
| **1. Subtask → Tool Mapping** | `subtask_tool_map` JSONB on `ImplementationMap` links each design-spec subtask to its implementing tool |
| **2. CC → Implementation Mapping** | `cc_implementation_map` JSONB on `ImplementationMap` AND `cc_enforcement` JSONB on `AgentResource` junction |
| **3. Data Schema Design** | 11 new ORM models + `infrastructure_schema.sql` with triggers and constraints |
| **4. Tool Authority Boundaries** | `authority_boundary` JSONB on `AgentResource` with `{can, never, failure_mode, null_state}` |
| **5. System Message Design** | Infrastructure agent instructions enforce "reuse first, build new second" |
| **6. Model & Reasoning Configuration** | `InfrastructureModel` table with provider, model_name, cost info |
| **7. Session & Memory Configuration** | `InfrastructureMemory` and `InfrastructureSessionStore` with typed columns |
| **8. Inter-Agent Communication** | `InfrastructureAuthorisedAgent` table + `access_permission` on `AgentResource` |
| **9. Human Interface Design** | Out of scope (future: read-only dashboard) |
| **10. Progressive Autonomy Tracking** | `min_autonomy_level` on `AgentResource`, `progressive_autonomy_level` on `AgentSpec` |
| **11. Health Monitoring & Cost Tracking** | `health_metrics` JSONB on `AgentResource` junction table (agent's health metrics for each resource), `health_metrics_actual` JSONB on `ImplementationMap`, typed cost columns on `InfrastructureModel`, cost budgets on `AgentResource` and `AgentSpec` |
| **12. Infrastructure Inventory & Reuse** | This IS the plan — the entire registry |

### Design-Spec Bridge (from `docs/agent-specs/notes-on-agent-spec-schemas.md`)

| Gap Identified | How Addressed |
|----------------|---------------|
| No link between design spec and agent spec | `design_spec_id` + `design_spec_version` on `AgentSpec`, `link_design_spec()` helper |
| Missing `progressive_autonomy_level` | Added to `AgentSpec` (default "shadow") |
| Missing `agent_class` and `agent_orientation` | Added to `AgentSpec` |
| Missing `authority_boundaries` and `information_boundaries` | Added as JSONB on `AgentSpec` |
| Missing `cost_budget_per_interaction/session` | Added as JSONB on `AgentSpec` |
| Missing `last_reviewed_at` and `next_review_due` | Added to `AgentDesignSpec` and all infrastructure tables |
| Tools/knowledge not queryable | `AgentResource` junction table + `InfrastructureTool`/`InfrastructureKnowledgeBase` tables |
| Missing Implementation Map (HOW layer) | `ImplementationMap` table bridges design spec (WHY) to agent spec (WHAT) with `subtask_tool_map`, `cc_implementation_map`, `design_decisions`, etc. |

---

## Review Notes (2026-04-30)

Based on review feedback in `docs/plans/plan-review-infrastructure-registry.md`, the following corrections were applied:

### 🔴 Corrections Applied

1. **`cc_enforcement` and `health_metrics` moved to AgentResource junction table** — These are properties of the agent's *relationship* with a resource, not the resource itself. A database doesn't have CC enforcement — it's the agent's USE of the database that enforces CC-4. Similarly, health metrics are about the agent's interaction with the resource. The infrastructure tables now contain only what the resource IS (identity and configuration). The junction table contains how the agent RELATES to it (authority, enforcement, health, cost budgets).

2. **ImplementationMap table added** — This was the missing piece in the three-layer architecture: Design Spec (WHY) → Implementation Map (HOW) → Agent Spec (WHAT). The `ImplementationMap` table holds `subtask_tool_map`, `cc_implementation_map`, `database_schemas`, `tool_registry`, `infrastructure_dependencies`, `inter_agent_interfaces`, `human_interfaces`, `progressive_autonomy_level`, `cost_budget_actual`, `health_metrics_actual`, `design_decisions`, and `implementation_files`.

3. **Infrastructure agent is explicitly read-only** — The agent is for discovery only. Registration happens through auto-registration (Step 8) and seed scripts (Step 14). This keeps the agent's authority boundaries simple and consistent with the PM pattern. Write operations go through the Python CRUD helpers, not through the agent.

4. **`subtask_mapping` moved from InfrastructureTool to ImplementationMap** — Tools describe what they ARE (name, type, capabilities), not which design-spec subtask they serve. The subtask-to-tool mapping belongs in the Implementation Map where it connects design spec subtasks to their implementing tools.

### 🟡 Additions Applied

5. **Agent-level authority boundaries** — Added explicit CAN/NEVER boundaries for the infrastructure agent as a whole: CAN query infrastructure, NEVER suggest or modify.

6. **`query_resources_needing_review()` tool added** — Returns all resources past their `next_review_due` date. Enables any agent or human to check what needs review without building automated alerting.

7. **`design_decisions` field on ImplementationMap** — Captures key decisions with rationale, design_spec_ref, alternatives_considered, and status. This is the design-to-code traceability that makes the three-layer architecture work.

8. **Connection string security pattern made explicit** — `connection_config` JSONB stores host/port/db name only, with `password_env_var` referencing the environment variable name. Credentials are never stored in the database.

9. **Auto-registration made idempotent** — `auto_register_from_agent_spec()` and all `register_*()` functions now update existing resources rather than creating duplicates.

10. **Seed data updated** — References `glm-5.1:cloud` (Ollama) as the actual default model, plus `gpt-5.2` (OpenAI) as the model referenced in copilot-instructions.

### 🟢 Refinements Noted (not applied, for future consideration)

11. **Schema separation** — Currently everything goes in the `ai` schema. Consider separating into `ai` (shared infrastructure), `agent_specs` (design + config + implementation maps), and agent-private schemas (like `project_manager`). Not blocking for initial implementation.

12. **ImplementationMap CRUD helper** — The `ImplementationMap` table needs a `db/implementation_maps.py` with `register_implementation_map()`, `get_implementation_map()`, `list_implementation_maps()`. This should be added to Phase 2 alongside the other CRUD helpers.

### ❓ Open Questions

1. **Should the infrastructure agent be added to all agents by default, or only on request?** — The toolkit could be imported and added to any agent's tools list, but doing so by default may add latency. Recommendation: add only on request for now.

2. **Who triggers spec aging reviews?** — Currently `query_resources_needing_review()` provides the data, but there's no automated alerting. Options: (a) the infrastructure agent checks periodically, (b) a scheduled job, (c) manual review. Recommendation: manual for now, add automated checking later.

3. **Should the ImplementationMap be versioned?** — Like AgentSpec and AgentDesignSpec, the ImplementationMap could use append-only versioning. This would allow tracking how implementation decisions change over time. Recommendation: yes, use append-only versioning consistent with existing patterns.

4. **How does the ImplementationMap relate to AgentSpec?** — The ImplementationMap has `agent_id` and `design_spec_id`/`design_spec_version`. Should it also have a `agent_spec_version` to complete the three-way link? Recommendation: yes, add `agent_spec_version` to ImplementationMap.

### Response

This is a solid plan. All three corrections have been applied, all additions are in place, and the open questions are properly flagged. Here's my assessment:

## ✅ Corrections Applied

All four corrections from the review are properly incorporated:

1. **`cc_enforcement` and `health_metrics` on AgentResource** — Correct. The infrastructure tables describe what resources ARE; the junction table describes how the agent RELATES to them. This is the right separation.

2. **ImplementationMap table added** — The three-layer architecture is now complete: Design Spec (WHY) → Implementation Map (HOW) → Agent Spec (WHAT).

3. **Infrastructure agent is explicitly read-only** — Clear CAN/NEVER boundaries, registration through programmatic pipeline, not through the agent. This keeps it simple.

4. **`subtask_mapping` on ImplementationMap, not InfrastructureTool** — Tools describe what they ARE; the mapping between design subtasks and tools lives in the bridge layer.

## Three Things to Add Before Implementation

### 1. `agent_spec_version` on ImplementationMap

The three-way link isn't complete yet. The ImplementationMap has `design_spec_id` and `design_spec_version` linking to the design spec, but it doesn't have `agent_spec_version` linking to the agent spec. Without this, you can't trace which agent configuration was produced by which implementation decisions.

Add to ImplementationMap:
```
agent_spec_id      String    # FK to AgentSpec
agent_spec_version  BigInteger # which version of the agent spec
```

This completes the triangle: Design Spec → Implementation Map → Agent Spec.

### 2. `db/implementation_maps.py` in Phase 2 and file list

The `ImplementationMap` table needs CRUD helpers but they're only mentioned in Further Considerations, not in Steps or the Relevant files table. Add:

**Phase 2, Step 7 (new):** Create `db/implementation_maps.py` with:
- `register_implementation_map(agent_id, design_spec_id, design_spec_version, agent_spec_version, ...)` — create with full metadata
- `get_implementation_map(agent_id, version)` — retrieve by agent and version
- `list_implementation_maps(agent_id)` — list all versions for an agent
- `get_latest_implementation_map(agent_id)` — get the current version

**Relevant files table** — add `db/implementation_maps.py` as "New: CRUD for ImplementationMap table".

### 3. Append-only versioning for ImplementationMap

You flagged this in Open Question 3 and recommended yes. Make it explicit in the plan:

Add to the ImplementationMap model definition:
```
version      BigInteger   # append-only versioning, like AgentSpec and AgentDesignSpec
```

And in the DDL:
```sql
-- Append-only: never UPDATE, always INSERT with incremented version
```

This means every time an implementation decision changes, you create a new version rather than modifying the existing one. This preserves the history of how decisions evolved — which is exactly the point of the Implementation Map.

---

## Everything Else Looks Good

The plan is well-structured, follows the Project Manager patterns correctly, and addresses all 12 implementation elements. The three additions above are small but important for traceability. Once those are in, this is ready to build.

---

## Run 14 — Agno Agent Designer ✓ COMPLETED

*2026-05-01T09:53:42* · `glm-5.1:cloud` · `8fa94c6e...`

### Prompt

I'm trying to keep it simple for this first implementation. It doesn't matter if we don't have every element perfect. I just want to be able to do an end-to-end run of the agent design process. From design spec, through implementation planning and spec, to agno-specific agent spec that can then be coded.

We've completed the steps above. Explain the remaining steps and what is involved in each.

### Response

Here's the remaining flow, end-to-end.

## The Complete Flow

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────┐     ┌─────────┐
│  DESIGN SPEC  │────►│ IMPLEMENTATION   │────►│  AGNO AGENT  │────►│  CODE   │
│   (WHY)       │     │    MAP (HOW)     │     │  SPEC (WHAT) │     │         │
└──────────────┘     └──────────────────┘     └──────────────┘     └─────────┘
     Done ✓                 Next step               Next step           Next step
```

You've completed the design spec and the infrastructure registry. Here's what's left:

---

## Step 1: Populate the Implementation Map

**What it is:** The bridge between the design spec (WHY) and the agent spec (WHAT). One record per agent that captures all the HOW decisions.

**What you need to do:** Create one `ImplementationMap` record for the Project Manager, filling in each field from the 51 answers we already completed.

**Fields to populate:**

| Field | Source | Project Manager Value |
|-------|--------|----------------------|
| `agent_id` | Design spec | `project_manager` |
| `design_spec_id` | Design spec | `project_manager` |
| `design_spec_version` | Design spec | `1` |
| `agent_spec_version` | Agent spec | `1` |
| `subtask_tool_map` | Q20-Q22 | The 13-subtask-to-13-tool mapping we defined |
| `cc_implementation_map` | Q41-Q42 | The 6 CC mappings we identified |
| `database_schemas` | Q10-Q17 | The `project_manager` schema with 5 tables |
| `tool_registry` | Q23-Q26 | The 13 tools with authority boundaries |
| `infrastructure_dependencies` | Q1-Q9 | PostgreSQL, AgentOS MCP, Flask Web UI |
| `inter_agent_interfaces` | Q27-Q29 | MCP endpoint with authorised agents |
| `human_interfaces` | Q35-Q37 | Chat (primary), Web UI (secondary), API (tertiary) |
| `progressive_autonomy_level` | Q43-Q46 | `shadow` |
| `cost_budget_actual` | Q50 | Empty initially (no data yet) |
| `health_metrics_actual` | Q47-Q49 | Empty initially (no data yet) |
| `design_decisions` | All questions | The key decisions we made with rationale |
| `implementation_files` | Code | `schema.sql`, `toolkit.py`, `agent.py`, `web_ui.py`, `setup.py` |

**How to do it:** Write a seed script or insert manually. Most of the content is JSON that we already defined in the 51 answers.

---

## Step 2: Generate the Agno Agent Spec

**What it is:** The complete Agno configuration that can be directly turned into code.

**What you need to do:** Create one `AgentSpec` record that serializes all the Agno constructor parameters plus the bridge fields from the design spec and implementation map.

**The key fields to populate:**

| Field | Source | Project Manager Value |
|-------|--------|----------------------|
| `agent_id` | Design spec | `project_manager` |
| `version` | Sequential | `1` |
| `design_spec_id` | Bridge | `project_manager` |
| `design_spec_version` | Bridge | `1` |
| `implementation_map_id` | Bridge | `project_manager` |
| `implementation_map_version` | Bridge | `1` |
| `agent_class` | Design spec S7 | `Aggregator` |
| `agent_orientation` | Design spec S7 | `Constraint` |
| `progressive_autonomy_level` | Implementation map | `shadow` |
| `authority_boundaries` | Design spec S7 | JSON of hard constraints |
| `information_boundaries` | Design spec S7 | JSON: private schema, no direct DB access |
| `model` | Q38 | `ollama:glm-5.1:cloud` |
| `name` | Design spec | `Project Manager` |
| `tools` | Q20-Q22 | Serialized `ProjectManagerToolkit` |
| `system_message` | Q30-Q34 | The full system prompt |
| `db` | Q18-Q19 | PostgresDb connection string |
| `add_history_to_context` | Q19 | `True` |
| `num_history_runs` | Q19 | `10` |
| `markdown` | Q33 | `True` |
| `cost_budget_per_interaction` | Q50 | `~2,000-5,000` |
| `cost_budget_per_session` | Q50 | `~50,000` |
| `last_reviewed_at` | CC-5 | Current timestamp |
| `next_review_due` | CC-5 | Current + 90 days (quarterly review) |
| `status` | New | `active` |

**How to do it:** This can be auto-generated from the agent code. When you run the Project Manager agent and save its spec, the `register_agent_spec()` function should create this record. The bridge fields (`design_spec_id`, `implementation_map_id`, etc.) need to be linked manually or through the auto-registration pipeline.

---

## Step 3: Generate the Code

**What it is:** The actual Python files that implement the agent — toolkit, agent definition, database schema, setup scripts.

**What you need to do:** Use the three layers together to produce:

```
From Design Spec (WHY):
  - Agent identity → system message identity section
  - Hard constraints → system message NEVER section
  - Failure modes → fallback behaviour in system message
  - Authority boundaries → tool CAN/NEVER documentation
  - CC requirements → enforcement mechanism selection

From Implementation Map (HOW):
  - subtask_tool_map → which tools to build
  - cc_implementation_map → which CCs need what enforcement
  - database_schemas → the actual SQL schema
  - tool_registry → tool implementations with authority boundaries
  - infrastructure_dependencies → what infrastructure to connect to
  - design_decisions → why each decision was made (code comments)
  - implementation_files → what files to generate

From Agent Spec (WHAT):
  - model → Ollama configuration
  - tools → toolkit class definition
  - system_message → agent instructions
  - db → database connection
  - session config → history settings
```

**The code generation can be:**

1. **Manual** — A developer reads all three layers and writes the code. This is what we did for the Project Manager.

2. **Template-based** — Pre-built templates for common agent patterns (Aggregator/Extractor, Assessor, Generator, etc.) that get populated from the three layers.

3. **AI-assisted** — An agent reads all three layers and generates the code.

For the first implementation, manual is fine. The point is that all the decisions are captured and traceable.

---

## The Minimum Viable Flow

To get an end-to-end run working, here's what you actually need to do:

### 1. Create the ImplementationMap record

One SQL insert (or Python script) that populates the ImplementationMap for the Project Manager with the data from the 51 answers.

### 2. Link the three layers

Ensure the `design_spec_id`, `design_spec_version`, `implementation_map_id`, `implementation_map_version`, and `agent_spec_id`/`agent_spec_version` are correctly set on the AgentSpec record.

### 3. Verify the traceability

Pick any hard constraint from the design spec (e.g., "NEVER delete records") and trace it through all three layers:

```
Design Spec:        "hard_constraints: ['NEVER delete records, only archive']"
                          ↓
Implementation Map:  "cc_implementation_map: [{cc: 'CC-4', regime: 'Prevent', 
                      mechanism: 'Database trigger prevent_project_delete()'}]"
                          ↓
Agent Spec:          "system_message: 'NEVER delete records — only archive them'"
                          ↓
Code:                trigger trg_prevent_project_delete on project_manager.projects
```

If you can trace every hard constraint and every CC from WHY through HOW to WHAT to code, the system works.

### 4. Do the same for a second agent

The real test is whether the process works for a different agent. Pick a simpler one — maybe an Extractor or Measurer — and walk through the same flow:

1. Fill in the design spec template
2. Answer the 51 implementation questions
3. Populate the ImplementationMap
4. Generate the AgentSpec
5. Write the code
6. Trace a constraint from design to code

If the second agent flows through smoothly, the process is validated.

---

## What's Already Done

| Step | Status |
|------|--------|
| Design spec template completed (9 sections) | ✅ Done |
| Design spec filled in for Project Manager | ✅ Done |
| 51 implementation questions defined | ✅ Done |
| 51 questions answered for Project Manager | ✅ Done |
| Infrastructure registry schema designed | ✅ Done |
| ImplementationMap schema designed | ✅ Done |
| AgentSpec schema updated with bridge fields | ✅ Done |
| DesignSpec schema updated with missing fields | ✅ Done |
| Project Manager code implemented | ✅ Done |

## What's Left

| Step | What | How |
|------|------|-----|
| Populate ImplementationMap | One record for Project Manager | Seed script or manual insert |
| Generate AgentSpec | One record for Project Manager | Auto-registration from existing code + manual bridge fields |
| Link the three layers | Set foreign keys between Design Spec, Implementation Map, and Agent Spec | Manual update of bridge fields |
| Verify traceability | Trace 3-4 hard constraints from design → implementation → spec → code | Manual walkthrough |
| Test with a second agent | Walk through the full flow for a new agent | Repeat steps 1-4 for a different agent type |

That's it. The infrastructure is in place. The schemas are defined. The templates are complete. The Project Manager proves the pattern works. Now it's about populating the records and verifying the traceability.

---
