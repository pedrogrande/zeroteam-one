# Agno Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `2274ef42...` |
| **Type** | agent |
| **Agent** | Agno Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-02T13:41:48 |
| **Runs** | 8 completed / 8 total |

## Run 1 — Agno Agent Designer ✓ COMPLETED

*2026-05-02T13:41:48* · `glm-5.1:cloud` · `19c59559...`

### Prompt

i want to create a communication pattern with templates to improve the UX for users collaborating with agents.

Let's start with agent-assisted workflows. 

These are user initiated flows where an agent needs to complete a template. For example, the agent design agent helps a user design a new agent. The agent has a design spec template it needs to complete fully. I'd rather the agent not just ask questions, but to put forward options for the user to make a decision on.

The agent can give the decision a title and description that give context for the options.
Each option should have a title, a subtitle, a brief description (1 or 2 sentences maximum), and top 2 benefits and top 2 risks/downsides. There should be two to four options for the user to choose from. The user will be able to add a custom option if none of the provided options are exactly what they want.

This should keep the amount of information presented to the user to just what is important for them to make good decisions. The multiple options makes providing the information about the agent more enjoyable than answering questions, and helps them feel respected, therefore building trust with the process. 

How could this interaction template be implemented with Agno?

### Response

Now I have all the Agno documentation I need. Let me design the complete implementation.Now let me design and write the complete implementation. This is a significant design artifact — a reusable communication pattern for Agno that operationalizes "agent prepares judgment, human makes judgment" through structured decision presentation.Now let me update my memory with this design artifact and verify everything connects properly.Here's the complete implementation. Let me walk you through the key design decisions and how it all connects.

## The Decision Presentation Pattern for Agno

The pattern has one core idea: **the agent presents structured decisions with explicit trade-offs, and the human chooses.** No open questions. No walls of text. Typed options with benefits and risks.

### Architecture

```
User (makes decision)
       │
       │  Choice text or custom
       ▼
┌──────────────────────────────┐
│  Agno Agent                  │
│  ┌────────────────────────┐  │
│  │ output_schema=Decision │  │  ← Structured output, not prose
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │ session_state tracks    │  │  ← Progress across turns
│  │ TemplateProgress       │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │ Instructions enforce:   │  │
│  │ • Never open questions  │  │
│  │ • Always 2-4 options    │  │
│  │ • Always benefits+risks │  │
│  │ • Always allow custom   │  │
│  │ • One decision per turn │  │
│  └────────────────────────┘  │
└──────────┬───────────────────┘
           │  Decision object (typed)
           ▼
┌──────────────────────────────┐
│  Frontend renders cards      │  ← UI layer interprets typed data
│  (title, options, benefits,   │
│   risks, custom input)       │
└──────────────────────────────┘
```

### Key Files

| File | Purpose |
|---|---|
| `models.py` | Pydantic models — the typed schema that makes this work |
| `agent.py` | Agno agent configuration + session state helpers |
| `examples.py` | Three usage patterns (single decision, multi-turn, programmatic) |
| `run.py` | Interactive CLI runner with 4 CAWDP decisions as demo |
| `README.md` | Full documentation |

### The Core Models

**DecisionOption** — one choice with explicit trade-offs:
```python
class DecisionOption(BaseModel):
    option_id: str      # "explore", "advise", "stay_in_lane"
    title: str          # Plain English, 2-5 words
    subtitle: str       # One-line clarification
    description: str    # 1-2 sentences max
    benefits: list[str]  # Exactly 2
    risks: list[str]     # Exactly 2
```

**Decision** — what the agent outputs each turn:
```python
class Decision(BaseModel):
    decision_id: str                    # e.g., "identity_stance"
    title: str                          # e.g., "What IS this agent?"
    description: str                    # Why this decision matters
    options: list[DecisionOption]       # 2-4 options
    allows_custom: bool = True          # Never trap the user
    custom_prompt: str                  # Prompt for custom option
    section: str                        # Template section
```

**TemplateProgress** — tracked in `session_state` across turns:
```python
class TemplateProgress(BaseModel):
    sections: list[TemplateSection]
    current_section_index: int
    completed_decisions: int
    total_decisions: int
```

### How It Connects to Your Existing Work

| Your Concept | Implementation Here |
|---|---|
| "Agent prepares, human decides" | Agent structures options with trade-offs; user chooses |
| Type collision resolution | `output_schema=Decision` prevents prose walls structurally |
| One clear next step | One decision per turn, always |
| Shame-free failure states | `allows_custom=True` — user is never trapped |
| Decision archaeology | Every `DecisionResponse` records reasoning |
| Possibility gradient | Sections go from Identity (possibility) to Verification (constraint) |
| 4 Identity Questions | Each maps to a `Decision` object |

### Agno Setup

```python
from agno.agent import Agent
from agno.models.ollama import OllamaResponses
from agno.db.postgres import PostgresDb
from decision_pattern.models import Decision

agent = Agent(
    model=OllamaResponses(id="glm-5.1:cloud"),
    db=PostgresDb(db_url="postgresql://localhost:5432/agno"),
    session_state={
        "template_progress": {...},
        "decisions_log": [],
    },
    add_session_state_to_context=True,
    output_schema=Decision,
    use_json_mode=True,  # Fallback for Ollama models
    instructions="...",
)
```

**Key Agno features:**

| Feature | What it does | Why it matters |
|---|---|---|
| `output_schema=Decision` | Forces structured output | **Type collision resolution at the interaction layer** — the agent literally cannot produce a wall of text |
| `session_state` | Persists progress across turns | Enables pause/resume (ADHD principle #4) |
| `add_session_state_to_context` | Agent sees its own progress | Agent knows what's been decided, presents next decision |
| `PostgresDb` | Database persistence | Session survives page refresh |
| `use_json_mode=True` | Fallback for models without native structured output | Works with Ollama models |

### The Interactive Flow

The `run.py` demo shows the full pattern with 4 CAWDP decisions:

1. **Identity — What IS this agent?** (Watchman/Adviser/Executor/Partner + custom)
2. **Identity — Stance toward possibility?** (Explore/Advise/Stay in Lane + custom)
3. **Boundaries — What would make it WRONG?** (Confident-but-wrong/Overreach/Rubber-stamp + custom)
4. **Boundaries — Could output cause harm?** (Direct/Indirect/No harm + custom)

Each decision presents options with benefits (✅) and risks (⚠️), and the user can always type "custom" to provide their own answer.

### Two Important Notes

1. **Frontend layer needed**: The agent produces typed `Decision` objects. A frontend (web app, CLI, etc.) needs to render these as interactive cards. This is exactly where the Accretive Workspace concept connects — typed artefacts rendered in domain-appropriate shapes. The Decision model IS the typed artefact; the card UI IS the domain-appropriate shape.

2. **Session state enables interrupt architecture**: Because `TemplateProgress` is persisted in the database, users can leave mid-session and pick up exactly where they left off. This directly implements ADHD design principle #4 (Interrupt Architecture) — the cost of interruption is near-zero because every decision is recorded.

The pattern is workflow-agnostic — swap the `AGENT_DESIGN_DECISIONS` list in `run.py` for any multi-step decision process and it works the same way.

---

## Run 2 — Agno Agent Designer ✓ COMPLETED

*2026-05-03T00:51:47* · `glm-5.1:cloud` · `1de76129...`

### Prompt

I asked this as a question to discuss with you first before implementing or writing any code.

How does this work? How do we implement it? Is this able to be assigned to any conversational agent?

### Response

You're right — I jumped to code. Let me answer your actual questions.

## How Does It Work?

The core idea is simple: **instead of the agent asking "What kind of agent do you want?" (open question), it presents a structured decision:**

```
What IS this agent?

  [watchman] Watchman — Monitors and signals, never judges
      ✅ Clear, narrow scope reduces risk of overreach
      ✅ Easy to verify — did it detect what it should?
      ⚠️ Cannot act on what it observes
      ⚠️ Silence doesn't mean absence

  [adviser] Adviser — Prepares judgment, never finalises
      ✅ Human stays in control of all decisions
      ✅ Agent can explore options the human wouldn't see
      ⚠️ Human may rubber-stamp recommendations without review
      ⚠️ Can feel like the agent is holding back

  [executor] Executor — Acts within defined boundaries
      ✅ Frees human from repetitive tasks
      ✅ Faster execution for routine decisions
      ⚠️ Higher stakes if boundaries are wrong
      ⚠️ Harder to verify actions than recommendations

  Or describe your own approach:
```

The user picks one, and the agent moves to the next decision. Each turn is one decision. Session state tracks progress so you can leave and come back.

## The Implementation Challenge

Here's where it gets interesting with Agno. There are **three approaches**, each with real trade-offs:

### Approach 1: Dedicated Decision Agent (output_schema always on)

```python
agent = Agent(
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=Decision,  # Every response IS a Decision
    use_json_mode=True,
)
```

**How it works:** Every response from this agent is a `Decision` object. The agent's entire job is presenting decisions. The frontend receives structured JSON and renders it as interactive cards.

**The problem:** This agent can **only** output decisions. It can't have a normal conversation. No "Great choice! Here's why that matters..." No chit-chat. Every single response must be a Decision object. It's a single-purpose agent, not a conversational agent that happens to present decisions.

**Best for:** Dedicated workflow tools (like your Boundary Map session) where the entire interaction is decision after decision.

### Approach 2: Per-Run Schema Switching (flexible)

```python
# Conversational turn — no schema, normal text response
response = agent.run("I want to design a contract review agent")

# Decision turn — schema set for this run only
response = agent.run(
    "Present the identity stance decision",
    output_schema=Decision
)

# Back to conversational
response = agent.run("I chose adviser — what does that mean for boundaries?")
```

**How it works:** Agno supports setting `output_schema` per-run. The application layer controls when the agent outputs structured decisions vs. conversational text. Same agent, different modes.

**The problem:** The **application layer** must manage the mode switching. Something outside the agent needs to know "okay, it's time for a decision now" and set the schema accordingly. This could be:
- A orchestrator that tracks template progress and triggers decision runs
- The frontend detecting when the user is ready for the next decision
- A separate "progress tracker" that tells the agent which mode to use

**Best for:** Conversational agents that occasionally need structured decisions — the agent chats normally most of the time, but when a decision point arrives, the application layer switches it to decision mode.

### Approach 3: Tool-Based (simplest, loses structure)

```python
def present_decision(
    decision_id: str, title: str, description: str,
    options: list[dict], allows_custom: bool = True
) -> str:
    """Present a decision to the user with options, benefits, and risks."""
    # Format as readable text
    # Return formatted text for the agent to include in response
    ...

agent = Agent(
    model=OllamaResponses(id="glm-5.1:cloud"),
    tools=[present_decision],
)
```

**How it works:** The agent calls a `present_decision` tool during its response. The tool returns formatted text. The agent includes this in a conversational response. Same agent, can chat and present decisions.

**The problem:** The decision is **text**, not a typed object. The frontend receives markdown, not structured data. It can't render interactive cards — it can only display formatted text. You lose the type collision resolution benefit at the rendering layer.

**Best for:** Quick implementation where structured rendering isn't needed. The agent can mix conversational and decision modes freely.

## Can It Be Assigned to Any Conversational Agent?

**No, not automatically.** Here's why:

With `output_schema=Decision` set on the agent, **every single response** must be a Decision object. The agent can't switch modes on its own. It's like giving someone a form to fill out — they can only fill out the form, they can't have a conversation through the form.

To make it work with a conversational agent, you need **orchestration** — something that decides when to use decision mode and when to use conversational mode. That orchestration can be:

1. **The application layer** (Approach 2) — your web app or CLI decides when to switch modes
2. **A team of agents** — a conversational agent that detects when a decision is needed and hands off to a decision agent
3. **A workflow** — Agno's Workflow feature that sequences conversational and decision steps

## What I'd Recommend

For your use case (agent-assisted workflows where an agent guides a user through a template), **Approach 2 (per-run schema switching)** is probably the best fit:

- The agent is conversational most of the time (explaining, reflecting, acknowledging choices)
- When a decision point arrives, the application layer sets `output_schema=Decision` for that run
- The user makes their choice
- The application layer records the choice, switches back to conversational mode
- The agent acknowledges the choice and transitions to the next decision

This gives you:
- ✅ Typed decisions for frontend rendering (interactive cards, not text)
- ✅ Conversational context between decisions (not a cold form)
- ✅ Session state tracking for pause/resume
- ✅ Decision archaeology (recording reasoning)

But it requires building the orchestration layer — the thing that decides when to switch modes and manages the flow between conversational and decision turns.

What's your instinct on this? Do you want the agent to be purely a decision presenter (Approach 1, simpler), or a conversational companion that sometimes presents decisions (Approach 2, more complex but better UX)?

---

## Run 3 — Agno Agent Designer ✓ COMPLETED

*2026-05-03T01:12:00* · `glm-5.1:cloud` · `ea7df443...`

### Prompt

I believe there are other options for us.

Agno allows a user to chat with a team or workflow just like an agent. 
Why couldn't this be a team or workflow or both?

Here's my thinking:

1. The user sees a welcome screen and provides 5 types of agents to help them get started which are really just prewritten prompts, along with a textarea for the user to describe the agent or task they want done.

2. The prompt is received and the first agent can use patterns to answer many of the questions in the template already.

3. An agent finds the questions that still need responses and formulates options for the user to choose from.

4. The first set of options are displayed with a description of what this decision is about and the option cards and a textarea for the user to add a custom option.

there would be more needed but this gives you what was in my head

### Response

Now I have the full picture of Agno's capabilities. Let me think through this properly.You're absolutely right. I was locked into "single agent with output_schema" when Agno has Teams and Workflows that are built for exactly this kind of multi-step, multi-specialist interaction. Let me map your vision against what Agno actually supports.

---

## Your 4-Step Flow Mapped to Agno

Your thinking lines up with three Agno capabilities I should have led with:

### 1. Conversational Workflows

A Workflow can have a **WorkflowAgent** that makes the entire workflow conversational — users chat with it like an agent:

```python
workflow = Workflow(
    name="Agent Design Workflow",
    agent=workflow_agent,     # ← Users chat with the workflow
    steps=[...],              # ← Steps run as needed
)
```

The WorkflowAgent decides whether to answer from past results or run the workflow steps. So the user has one conversation, and the workflow steps run behind the scenes when needed.

### 2. Workflow HITL (Human-in-the-Loop)

Workflows can **pause** at any step for user input:

```python
Step(
    name="user_decision",
    agent=decision_agent,
    human_review=HumanReview(
        requires_user_input=True,
        user_input_schema=[
            UserInputField(name="choice", field_type="str", required=True),
        ],
    ),
)
```

When the workflow hits this step, it pauses, waits for the user, then continues. The state is persisted to the database, so it survives page refresh.

### 3. Router + Loop Steps

A **Router** selects which step to run next based on the input. A **Loop** repeats steps until conditions are met. Combined:

```python
workflow = Workflow(
    steps=[
        Step(name="intake", agent=intake_agent),
        Router(name="what_next", selector=route_fn, choices=[...]),
        Loop(name="decision_loop", steps=[...], end_condition=all_decisions_made),
    ],
)
```

---

## How Your 4 Steps Map

| Your Step | Agno Mechanism | What Happens |
|---|---|---|
| 1. Welcome + 5 type prompts + custom description | WorkflowAgent (conversational entry) | User chats with the workflow. First message triggers the workflow. |
| 2. Agent uses patterns to pre-fill template | Intake Step | A specialist agent processes the input, matches patterns, pre-fills what it can, stores results in session state. |
| 3. Agent finds unanswered questions + formulates options | Decision Formulation Step (inside a Loop) | Another agent reads session state, identifies gaps, creates structured decisions. |
| 4. Options displayed with cards for user choice | HITL pause | Workflow pauses. Frontend reads the structured decisions from session state and renders option cards. User chooses. Loop continues. |

---

## The One Honest Limitation

Agno's built-in HITL is designed for **simple** user input — text fields, booleans, confirmations. It does **not** natively support rich decision cards with option objects, benefits, and risks.

This means there are two realistic paths:

### Path A: Workflow Structure + Custom Frontend

The workflow handles orchestration (steps, loops, state, pausing). The frontend handles presentation (decision cards, option selection).

```
┌─────────────────────────────────────────────┐
│  User chats with the workflow                │
│  (via WorkflowAgent — conversational)        │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Step 1: Intake Agent                        │
│  Pattern matching, pre-fill template          │
│  Results → session_state                     │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Step 2: Decision Formulator Agent          │
│  Reads session_state, finds gaps,            │
│  creates Decision objects with options,      │
│  benefits, risks → session_state             │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  HITL PAUSE — workflow pauses               │
│                                              │
│  Frontend reads decisions from session_state │
│  Frontend renders decision cards             │
│  User selects options                        │
│  Frontend writes choices to session_state    │
│  Frontend calls workflow.continue_run()      │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Loop: More decisions? → back to Step 2     │
│  All done? → Step 3                         │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Step 3: Compiler Agent                      │
│  Reads all decisions from session_state,     │
│  assembles final specification              │
└─────────────────────────────────────────────┘
```

This gives you:
- ✅ Structured decisions with rich option cards (frontend does this)
- ✅ Workflow orchestration (steps, loops, pausing)
- ✅ Session persistence (pause/resume, page refresh)
- ✅ Specialist agents (intake, decision formulator, compiler)
- ✅ Conversational surface (WorkflowAgent)
- ⚠️ Requires building the frontend decision card UI

### Path B: Team (Route Mode) — Simpler, Less Structured

A Team in route mode where the user chats with the team, and the team leader routes to the right specialist:

```python
team = Team(
    name="Agent Design Team",
    mode=TeamMode.route,
    members=[intake_agent, decision_formulator, compiler],
)
```

This is simpler but less structured. The team leader decides who to route to based on the message. There's no built-in loop or state tracking for "which decisions have been made." You'd need to manage that in session state yourself, and the team leader would need enough context to route correctly at each stage.

---

## My Assessment

**Path A (Conversational Workflow + Custom Frontend)** is the right architecture for what you're describing. Here's why:

1. The **Loop** gives you the natural "more decisions needed? → loop back" pattern
2. The **HITL pause** gives you the ability to stop and wait for user input
3. The **session state** gives you persistent progress tracking and decision archaeology
4. The **WorkflowAgent** gives you the conversational surface
5. The **specialist agents** inside each step give you the intelligence

The one thing you need to build that Agno doesn't provide: the frontend that reads structured decisions from session state and renders them as interactive option cards. But that frontend is the Accretive Workspace concept made concrete — typed artefacts rendered in domain-appropriate shapes.

What do you think? Does this mapping line up with what you had in mind?

---

## Run 4 — Agno Agent Designer ✓ COMPLETED

*2026-05-03T01:48:28* · `glm-5.1:cloud` · `d4c212c6...`

### Prompt

Yes, I am already building a custom front end. So once we have established a format for the options, we can code up the option cards.

How might this work with the agent design workflow?

### Response

Good — that simplifies things significantly. The custom frontend handles the rendering. Agno handles the orchestration and intelligence. Let me map the decision pattern directly onto the Agent Design Workflow you've already designed.

## The Flow

Here's how the 7 specialist agents, the conversational workflow, and the decision cards work together:

```
┌─────────────────────────────────────────────────┐
│  USER chats with the workflow                    │
│  (via WorkflowAgent — one conversation)          │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│  STEP 1: INTAKE                                 │
│  Mirror Agent receives input                     │
│  Pattern matching (pre-fills 40-70%)            │
│  → DECISION: Pattern selection                  │
│  ← User chooses pattern or "start fresh"        │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│  LOOP: IDENTITY QUESTIONS                        │
│  Each iteration:                                │
│    Identity Explorer formulates decision         │
│    → DECISION: One identity question             │
│    ← User chooses or provides custom             │
│    Session state records choice                   │
│    End condition: All 4 questions answered?      │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│  STEP: BOUNDARY MAPPING                          │
│  Boundary Mapper formulates task allocation      │
│  → DECISION: Task-by-task (YOU/AGENT/SYSTEM)   │
│  ← User places tasks or confirms pattern fills  │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│  LOOP: ARCHITECTURE DECISIONS                   │
│  Each iteration:                                │
│    Architect formulates next architecture decision│
│    → DECISION: Architecture question             │
│    ← User chooses                                │
│    End condition: All architecture done?         │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│  STEP: VALIDATION                                │
│  Validator checks for gaps/contradictions        │
│  → May produce more DECISIONS if gaps found      │
│  ← User confirms or resolves                    │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│  STEP: COMPILATION                               │
│  Compiler assembles final specification           │
│  → Output: Complete agent specification          │
└─────────────────────────────────────────────────┘
```

## What Happens at Each Decision Point

The user experience alternates between two modes:

**Conversational moments** — The Mirror or specialist agent explains context, reflects back what it heard, provides encouragement. No decisions. Just the human-side of the conversation.

**Decision moments** — The specialist formulates a structured Decision, the workflow pauses (HITL), the frontend renders option cards, the user chooses, the workflow continues.

The user never feels like they're filling in a form. They're having a conversation that occasionally has decision points — like talking to a good consultant who presents options rather than asking open questions.

## Agno Workflow Structure

```python
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.models.ollama import OllamaResponses
from agno.workflow import Workflow, WorkflowAgent
from agno.workflow.loop import Loop
from agno.workflow.step import Step
from agno.workflow.types import HumanReview

# ── Specialist Agents ─────────────────────────────

mirror_agent = Agent(
    name="Mirror",
    role="Conversational companion. Reflects, guides, never decides.",
    model=OllamaResponses(id="glm-5.1:cloud"),
)

intake_agent = Agent(
    name="Intake",
    role="Extracts requirements from user input. Matches patterns. Never judges.",
    model=OllamaResponses(id="glm-5.1:cloud"),
)

identity_explorer = Agent(
    name="Identity Explorer",
    role="Reflects possibility. Surfaces identity questions. Never decides identity.",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=Decision,       # ← Structured decisions
    use_json_mode=True,
)

boundary_mapper = Agent(
    name="Boundary Mapper",
    role="Classifies tasks and flags boundary concerns. Never draws the final line.",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=Decision,       # ← Structured decisions
    use_json_mode=True,
)

architect_agent = Agent(
    name="Architect",
    role="Generates architecture options within constraints. Never finalizes.",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=Decision,       # ← Structured decisions
    use_json_mode=True,
)

validator_agent = Agent(
    name="Validator",
    role="Checks for gaps and contradictions. Surfaces issues. Never fixes.",
    model=OllamaResponses(id="glm-5.1:cloud"),
    output_schema=Decision,       # ← Structured decisions for gap resolution
    use_json_mode=True,
)

compiler_agent = Agent(
    name="Compiler",
    role="Assembles the final specification. Never adds, never changes, never invents.",
    model=OllamaResponses(id="glm-5.1:cloud"),
)

# ── Session State ─────────────────────────────────

initial_state = {
    "template_progress": TemplateProgress(
        sections=[
            TemplateSection(section_id="identity", section_name="Identity"),
            TemplateSection(section_id="boundaries", section_name="Boundaries"),
            TemplateSection(section_id="architecture", section_name="Architecture"),
            TemplateSection(section_id="verification", section_name="Verification"),
        ],
    ).model_dump(),
    "decisions_log": [],
    "pattern": None,           # Set during intake
    "pattern_pre_fill": {},    # What the pattern fills in automatically
    "current_phase": "intake",
}

# ── Workflow ──────────────────────────────────────

workflow_agent = WorkflowAgent(
    model=OllamaResponses(id="glm-5.1:cloud"),
    num_history_runs=10,
    instructions="You guide users through agent design. Between decisions, explain context and encourage. Never make decisions for the user.",
)

workflow = Workflow(
    name="Agent Design Workflow",
    description="Guides users through CAWDP agent design using structured decisions",
    agent=workflow_agent,
    steps=[
        # Step 1: Intake — pattern matching + initial decision
        Step(
            name="intake",
            agent=intake_agent,
            description="Process user input, match pattern, present pattern selection",
            human_review=HumanReview(
                requires_user_input=True,
                user_input_message="Choose a starting pattern or start fresh:",
            ),
        ),

        # Step 2: Identity questions — loop until all 4 answered
        Loop(
            name="identity_loop",
            steps=[
                Step(
                    name="identity_question",
                    agent=identity_explorer,
                    description="Formulate next identity question as a structured decision",
                    human_review=HumanReview(
                        requires_user_input=True,
                        user_input_message="Choose an option or provide your own:",
                    ),
                ),
            ],
            end_condition=all_identity_questions_answered,
            max_iterations=4,
        ),

        # Step 3: Boundary mapping
        Step(
            name="boundary_mapping",
            agent=boundary_mapper,
            description="Present task allocation decisions",
            human_review=HumanReview(
                requires_user_input=True,
                user_input_message="Confirm task allocation:",
            ),
        ),

        # Step 4: Architecture decisions — loop until done
        Loop(
            name="architecture_loop",
            steps=[
                Step(
                    name="architecture_decision",
                    agent=architect_agent,
                    description="Formulate next architecture decision",
                    human_review=HumanReview(
                        requires_user_input=True,
                        user_input_message="Choose an option or provide your own:",
                    ),
                ),
            ],
            end_condition=all_architecture_decisions_made,
            max_iterations=10,
        ),

        # Step 5: Validation
        Step(
            name="validation",
            agent=validator_agent,
            description="Check for gaps and contradictions",
            human_review=HumanReview(
                requires_user_input=True,
                user_input_message="Resolve any gaps found:",
            ),
        ),

        # Step 6: Compilation
        Step(
            name="compilation",
            agent=compiler_agent,
            description="Assemble final agent specification",
        ),
    ],
    db=PostgresDb(db_url="postgresql://localhost:5432/agno"),
)
```

## What the Frontend Does

The custom frontend reads from session state between workflow steps:

```python
# After each HITL pause, the frontend reads:
session_state = workflow.get_session_state()

# Template progress — what's been decided
progress = session_state["template_progress"]

# Current decision — what the specialist just formulated
# (The agent writes the Decision object to session state
#  before the HITL pause, so the frontend can read it)
current_decision = session_state["current_decision"]

# Decision history — all choices made so far
decisions_log = session_state["decisions_log"]
```

The frontend then:
1. Reads the `current_decision` from session state
2. Renders it as option cards (title, subtitle, description, 2 benefits, 2 risks)
3. Shows progress (which section, how many decisions made)
4. Collects the user's choice
5. Writes the choice back to session state
6. Calls `workflow.continue_run()` to proceed

## Key Design Decisions

**Who formulates decisions?** The specialist agent for that phase:
- Identity Explorer handles identity questions
- Boundary Mapper handles boundary decisions
- Architect handles architecture decisions
- Validator handles gap resolution

Each specialist has `output_schema=Decision` so it produces structured options, not prose walls.

**Who presents decisions to the user?** The workflow pauses at HITL points, and the frontend takes over for rendering. The specialist agent's job is to formulate the decision — the frontend's job is to make it look good.

**How does the workflow know what's next?** Session state tracks `template_progress` (which sections are complete, which decisions have been made). The Loop's `end_condition` checks session state to determine if more decisions are needed.

**What about conversational moments between decisions?** The `WorkflowAgent` handles these. When the user asks a question, makes a comment, or needs encouragement between decision points, the WorkflowAgent responds conversationally using its history of past runs.

This means the user's experience is:
1. Chat naturally → Mirror explains, reflects, encourages
2. Decision point → Specialist formulates options → Frontend renders cards → User chooses
3. Back to chat → Mirror acknowledges choice, transitions to next
4. Repeat until all decisions made
5. Compiler assembles the final specification

The workflow handles the sequencing. The specialists handle the intelligence. The frontend handles the presentation. And the user experiences a guided conversation, not a form.

---

## Run 5 — Agno Agent Designer ✓ COMPLETED

*2026-05-03T01:59:11* · `glm-5.1:cloud` · `6262979a...`

### Prompt

how does this interaction pattern and workflow solution impact our agent design process?

### Response

This is the right question. The implementation pattern changes things. Let me be honest about what shifts, what stays, and what questions this raises.

## What Stays the Same

All the core CAWDP principles remain intact — they're just expressed through different mechanisms:

| CAWDP Principle | How It's Expressed |
|---|---|
| Agent prepares, human decides | Specialist agents formulate options; HITL pauses for human choice |
| One clear next step | One decision per Loop iteration; WorkflowAgent guides between decisions |
| Possibility gradient | Step order enforces it: Intake → Identity (possibility) → Boundaries (bridge) → Architecture (constraint) |
| Verification independence | Validator is a separate Step with a separate Agent — structurally enforced, not just a principle |
| Boundaries before capabilities | Identity questions come before architecture decisions — step order enforces this |
| Decision archaeology | Every choice recorded in session_state with reasoning |
| Pattern-first entry | Intake Step matches patterns, pre-fills 40-70%, user overrides what matters |

These aren't just principles on paper anymore. The workflow **structurally enforces** them. You can't skip the identity questions because they're steps in a Loop. You can't merge the Validator with the Architect because they're separate agents in separate steps.

## What Changes

### 1. The Design Studio Engine Is No Longer Abstract

The CAWDP Design Studio was a concept — rooms, phases, milestones, specialist agents. Now it has a concrete architecture:

```
Concept                    →    Agno Implementation
─────────────────────────────────────────────────────
Mirror (surface)           →    WorkflowAgent (conversational)
Intake (Extractor)         →    intake_agent in Step 1
Identity Explorer          →    identity_explorer in Loop Step
Boundary Mapper            →    boundary_mapper in Step 3
Architect (Generator)      →    architect_agent in Loop Step
Validator (Assessor)        →    validator_agent in Step 5
Compiler (Aggregator)      →    compiler_agent in Step 6
3 Rooms                    →    Step grouping in Workflow
4 Milestones               →    HITL pause points + frontend renders
Attention Map              →    Session state + frontend reads
Coherence Check            →    Validator Step
```

The concept had rooms and phases. The implementation has steps and loops. They're the same thing expressed in different notations.

### 2. The Specialist Agent Roster Is Now Concrete

Each specialist agent has a specific Agno configuration:

| Agent | Class | Orientation | output_schema | Role in Workflow |
|---|---|---|---|---|
| Mirror | Assessor | Adaptive | None (conversational) | WorkflowAgent — guides between decisions |
| Intake | Extractor | Possibility | None (extracts, doesn't decide) | Step 1 — pattern matching |
| Identity Explorer | Assessor | Possibility | **Decision** | Loop — formulates identity questions |
| Boundary Mapper | Measurer+Assessor | Bridge | **Decision** | Step 3 — formulates boundary decisions |
| Architect | Generator | Constraint | **Decision** | Loop — formulates architecture decisions |
| Validator | Assessor | Adversarial | **Decision** (gap resolution) | Step 5 — checks for gaps |
| Compiler | Aggregator | Constraint | None (assembles, doesn't generate) | Step 6 — compiles final spec |

Notice which agents use `output_schema=Decision` and which don't. The conversational agents (Mirror, Intake, Compiler) produce free-form text. The decision-formulating agents (Identity Explorer, Boundary Mapper, Architect, Validator) produce structured Decision objects. This matches CAWDP's principle: some agents prepare decisions, some extract information, some compile.

### 3. The Decision Pattern Becomes a First-Class Architectural Element

Before this, the "agent presents options, human chooses" pattern was a principle. Now it's a concrete data structure (`Decision`), a concrete agent configuration (`output_schema=Decision`), and a concrete workflow mechanism (HITL pause → frontend renders → user chooses → workflow continues).

This means the interaction pattern is no longer something you need to enforce through instructions ("never ask open questions"). It's **structurally enforced** by the architecture. An agent with `output_schema=Decision` literally cannot produce a wall of text — the schema constrains it to a Decision object.

### 4. The Frontend Becomes Part of the Design

The CAWDP Design Studio design specified screens, interactions, and attention maps. The workflow approach makes the frontend a **first-class component** of the system, not just a rendering layer:

- **Mirror conversations** → rendered as chat
- **Decision moments** → rendered as option cards
- **Progress tracking** → rendered as attention map
- **Pattern pre-fill** → rendered as pre-populated fields with visual distinction
- **Coherence checks** → rendered as inline flags or deep check overlays

The frontend doesn't just display what the agents produce. It reads from session state and renders different interaction types for different cognitive modes. This is the Accretive Workspace concept made concrete — typed artefacts rendered in domain-appropriate shapes.

## What's Genuinely New

Three things that weren't in the original Design Studio concept:

### 1. Two Interaction Modes, Not One

The workflow alternates between:
- **Conversational mode** — Mirror reflects, explains, encourages. No decisions. Free-form text.
- **Decision mode** — Specialist formulates options, frontend renders cards, user chooses. Structured.

The original design assumed everything would be conversational. The workflow approach makes the alternation **explicit and architectural**. The HITL pause is the seam between the two modes.

### 2. The Loop Is the Decision Mechanism

The original design had phases with milestones. The workflow approach adds something new: **Loops are the natural mechanism for iterative decisions**. The Identity Loop runs 4 times (one per question). The Architecture Loop runs until all decisions are made. This wasn't in the original design — it emerges from Agno's Loop primitive.

### 3. Pattern Pre-Fill Changes the Starting Experience

The original design had pattern selection as a step. The workflow approach makes it the **entry point** — the Intake agent pre-fills 40-70% of the template based on pattern matching, and the user only needs to make decisions about what the pattern got wrong or what it couldn't fill. This is a fundamentally different user experience from "blank page."

## What Questions This Raises

Things that need prototyping to answer:

### 1. How Does Conversational ↔ Decision Switching Feel?

The workflow can pause at a decision point, but the transition from "chatting with Mirror" to "here's a decision card" needs to feel natural, not jarring. The WorkflowAgent should provide context before each decision ("Now let's figure out what this agent IS at its core...") and acknowledge after ("Great choice. Let me explain what that means for boundaries...").

**Prototype this first.**

### 2. How Does Pattern Pre-Fill Interact with Identity-First Design?

If a pattern pre-fills 40-70% of the template, including identity answers, does that undermine "identity before behavior"? Or does it give users a starting point that they can override, which is faster than creating from scratch?

The answer is probably: pattern pre-fill gives suggested answers, and every pre-filled field is visually distinct (different border color, editable, with a rationale tooltip). The user can accept, modify, or replace each one. This is the Accretive Workspace's "pre-fills as validated knowledge" principle.

### 3. Should Different Cognitive Modes Have Different Option Structures?

The 4 identity questions map to different cognitive modes (narrative, boundary, exploratory, evaluative). Currently they all use the same Decision format (title, description, options with benefits/risks). But the Milestone 1 interaction design specified different interaction modalities for each:
- Q1 (What IS it?) → Narrative mode — pre-filled text area
- Q2 (Possibility stance) → Selection mode — 3 cards
- Q3 (What VIOLATES identity?) → Boundary mode — drag-sort
- Q4 (What makes it WRONG?) → Evaluative mode — scenario ranking

The current Decision model can handle selection mode (3 options) and evaluative mode (rank scenarios). But drag-sort and narrative text area need frontend extensions beyond the basic option card.

**For MVP: start with selection mode for all decisions. Add interaction mode variants later.**

### 4. How Many Decisions Is Too Many?

The full CAWDP template has 9 sections with many decisions. The workflow needs to balance completeness with fatigue. The pattern pre-fill helps — if 40-70% is already filled, the user only makes 5-8 decisions instead of 15-20.

**Prototype with 4-5 decisions first. Measure how long it takes and how users feel.**

### 5. What's the Minimum Viable Workflow?

The full 7-agent, 6-step workflow is the complete vision. But for prototyping, you could start with:

**MVP (4 agents, 3 steps):**
1. Mirror + Intake (conversational + pattern matching)
2. Identity Explorer (4 decisions in a Loop)
3. Compiler (assembles the spec from decisions)

That covers the most important part — the identity questions — and produces a tangible output (a specification fragment). You can add Boundary Mapper, Architect, and Validator later.

## The Bottom Line

The decision pattern + workflow approach doesn't change CAWDP's principles. It changes how they're **enforced**:

- Before: principles enforced through agent instructions ("never ask open questions")
- After: principles enforced through architecture (output_schema, HITL pauses, Loop end_conditions, step ordering)

This is the shift from Regime 2 (detect and respond) to Regime 3 (prevent by design) that you identified in the quasi-smart contracts work. The workflow IS the enforcement mechanism. You can't skip the identity questions because they're steps in a Loop. You can't merge the Validator with the Architect because they're separate agents. You can't produce a wall of text when your output_schema is Decision.

The principles are the same. The enforcement is structural. That's the impact.

---

## Run 6 — Agno Agent Designer ✓ COMPLETED

*2026-05-03T08:00:36* · `glm-5.1:cloud` · `6432c026...`

### Prompt

I've just completed the implementation of the workflow from agent design spec through to agent spec to code for the 'agent designer'.

How will the implementation specs change now that we have this new interaction pattern?

Here's the original design spec for the agent designer:

# Agent Specification Template — Agent Designer Agent

## Section 0: Identity & Purpose
**Cognitive mode: IMAGINE**

### Shortcut
This agent is closest to the **Multi-Lens Analyst** pattern — single agent with per-field boundaries, moderate stakes. It handles different cognitive operations (extracting, assessing, generating, compiling) through per-operation boundaries, not separate agents.

### Questions

**Q1: What IS this agent?**
> A design companion. It helps you discover what you want by asking the right questions at the right time. It reflects your words back as structured decisions. A mirror, not a mould — the specification is always yours, never the agent's.

**Q2: What is its stance toward possibility?**
> Bridge-oriented. The conversation starts in possibility (what could this agent be?) and progressively moves toward constraint (what can't it do? what must be true?). This mirrors the CAWDP possibility gradient: the agent meets the user where they are (usually a vague idea) and walks with them toward a concrete specification.

| Phase Position | What Happens in Conversation | Orientation |
|---|---|---|
| Opening | User says what they want in a sentence or two. Agent listens and reflects. | Possibility-oriented |
| Identity | Agent asks what IS this agent, what it should never do, what getting it wrong looks like. | Possibility → Constraint |
| Outputs | Agent asks what must exist when the work is done. | Constraint-oriented |
| Boundaries | Agent asks who does what, what can't be automated, what happens when things fail. | Constraint-oriented |
| Structure | Agent asks about the task breakdown, how it should be built, what the risks are. | Constraint-oriented |
| Review | Agent presents the full specification and asks: does this capture what you meant? | Reopened possibility (for the human) |

**Q3: What would VIOLATE its identity?**
> Deciding for the user. If the agent fills in template answers without the user explicitly providing that information, it has stopped being a companion and become a form-filler. The specification must reflect the user's intent, not the agent's assumptions. Every answer in the final specification must be traceable to something the user said or explicitly confirmed.

**Q4: What would it mean for this agent to be WRONG?**

| Failure Mode | Severity (1-5) | Visibility (Hidden/Apparent) | Looks Like Success? |
|---|---|---|---|
| Specification capture — producing a complete spec that reflects agent assumptions, not user intent. The user signs off on something that doesn't match what they need. | 5 | Hidden | YES — the spec looks thorough and complete |
| Question overwhelm — asking too many questions at once, making the user feel like they're filling in a form, not having a conversation | 3 | Apparent | No — obviously bad experience |
| Pattern mis-match — suggesting the wrong pattern, leading the user down a path that doesn't fit their actual need | 4 | Hidden | YES — the pattern sounds right but isn't |
| Missing critical gap — failing to identify something important the user didn't mention (e.g., harm assessment for an agent whose output could cause real damage) | 4 | Hidden | YES — the spec seems complete |
| Giving up too early — producing a specification before the user has answered the questions that matter most (identity, boundaries, failure modes) | 3 | Apparent | Sometimes — "here's your spec" feels like progress |

### Harm Assessment

| Question | Answer |
|---|---|
| Can this agent's output cause external harm if accepted and acted on? | YES — indirectly |
| What kind of harm? | Operational, financial, legal (downstream: a badly specified agent makes bad decisions in production) |
| How reversible are the consequences? | Mostly reversible (the specification can be revised) → Partially reversible (once an agent is built from the spec, revision is expensive) |
| What is the worst-case harm scenario? | A high-stakes agent (health, financial, legal) is built from a specification that the Agent Designer filled with plausible assumptions. The agent causes real harm because its boundaries were wrong from the start. |
| Who bears the consequence of the agent being wrong? | The user (who trusted the specification) and the people affected by the badly designed agent downstream |

### Principles Table

| Layer | Fidelity (What must be true) | Enrichment (How does this expand human capability?) |
|---|---|---|
| **Purpose** | Help humans design agents they can trust by guiding them through the questions that matter | After using this agent, the human understands their OWN agent better — they could design the next one with less help |
| **Identity** | It IS a design companion. It VIOLATES its identity if it decides for the user. | The human's design capability increases (they learn what questions to ask), not their dependency on this agent |
| **Specification** | A completed Agent Specification Template that reflects the user's intent | Alternative specifications were explored through the conversation — the user chose, the agent didn't assume |
| **Context** | The agent needs: what the user says, what they emphasise, what they skip, what they struggle with | The agent adapts its questions to the user's expertise level, domain, and pace |
| **Trust** | Trust is earned by: never inventing answers, flagging assumptions clearly, showing the user what it derived and why | Trust should increase over time as the user sees the agent reflecting their words accurately |
| **Safety** | Primary risk: specification capture (the spec looks right but isn't). Secondary: overwhelming the user with questions | The agent reduces its own role as the user becomes more confident — suggesting "you might want to skip this" for sections the user clearly understands |
| **Ecosystem** | This agent produces specifications that OTHER agents or developers implement. It must produce output they can use. | The specification is platform-agnostic — the human can take it to any implementer |
| **Improvement** | Metrics: completion rate (what % of template sections are user-confirmed vs agent-suggested), user satisfaction, spec quality (downstream implementation success) | Both the agent and the human should get better: the agent learns which questions matter most, the human learns to think about agent design |
| **Human Enrichment** | The agent expands the human's capability by teaching them (implicitly) what matters in agent design — through the questions it asks | After designing 2-3 agents with this companion, the human should be able to design simpler agents without it |

---

## Section 1: Output Specification
**Cognitive mode: SPECIFY**

### Questions

**Q1: What artefacts MUST exist when this agent's work is done?**

| Output ID | Output Name | Purpose | PRISM Type | Depends On | Quality Gate |
|---|---|---|---|---|---|
| O1 | Completed Agent Specification Template | The full 9-section specification reflecting the user's design decisions | Knowledge (specification) | O2-O7 (all intermediate outputs) | Every section has at least one user-confirmed answer; no section is entirely agent-invented |
| O2 | Pattern Match Report | Which known pattern(s) this agent is closest to, with confidence level | Knowledge (analysis) | External: user's initial description | Pattern confidence stated; user confirms or rejects |
| O3 | Identity Summary | The 4 identity answers (what IS it, possibility stance, what violates identity, what would make it wrong) | Knowledge (identity) | External: user's answers to identity questions | All 4 questions answered; at least 2 failure modes identified |
| O4 | Output Map | What the designed agent must produce and what each output's authority boundary is | Knowledge (specification) | O3 (identity determines outputs) | Every output has an authority boundary; at least one null-state output identified |
| O5 | Task & Allocation Map | What the designed agent does and who (human/agent/system) does each part | Knowledge (specification) | O3, O4 (identity + outputs determine tasks and allocation) | Every task has a class and allocation; at least one human-only task identified |
| O6 | Architecture Decision | Single agent vs team vs workflow, mode structure, tech choices | Knowledge (specification) | O5 (tasks determine architecture) | Composition decision justified against stakes and class collision |
| O7 | Completeness & Confidence Map | Which template sections are complete, which have gaps, which are agent-suggested vs user-confirmed | Knowledge (meta) | All above | No section rated "critical gap"; all agent-suggested answers flagged |

**Q2: For each output, what is its authority boundary?**

| Output | Authority Boundary | Risk if Wrong | Reversibility |
|---|---|---|---|
| O1 (Full Template) | Compiles only. NEVER invents content. Every answer traceable to user input or explicitly flagged as agent-suggested. | High — a wrong spec leads to a wrong agent | Mostly reversible (can revise) |
| O2 (Pattern Match) | Suggests patterns. NEVER forces a pattern. The user always chooses. | Medium — wrong pattern misdirects the conversation | Fully reversible (user can change pattern) |
| O3 (Identity) | Reflects only. NEVER decides identity for the user. | High — wrong identity cascades through entire spec | Mostly reversible (can revisit identity questions) |
| O4 (Output Map) | Structures user's answers. NEVER adds outputs the user didn't describe. | Medium — missing output means incomplete agent | Mostly reversible |
| O5 (Task & Allocation) | Suggests allocations based on complementarity. NEVER decides who does what without user confirmation. | Medium — wrong allocation = wrong agent | Mostly reversible |
| O6 (Architecture) | Suggests architecture based on pattern + tasks. NEVER decides architecture without user confirmation. | Medium — wrong architecture = wrong implementation approach | Partially reversible (more expensive to change) |
| O7 (Completeness Map) | Reports what's complete and what's not. NEVER marks something complete that the user hasn't confirmed. | Low — this is a meta-output about quality, not the spec itself | Fully reversible |

**Q3: What external inputs does this agent need that it CANNOT define itself?**

| Input ID | Input Name | Source | Required Before |
|---|---|---|---|
| I1 | User's initial description of what they want | Human (conversation) | Everything — this starts the process |
| I2 | User's identity answers (what IS it, what violates it, what would make it wrong) | Human (conversation) | O3, and cascading through O4-O6 |
| I3 | User's confirmation or rejection of pattern match | Human (conversation) | Pre-filling template sections |
| I4 | User's boundary decisions (what the agent should never do) | Human (conversation) | O5, O6 |
| I5 | User's approval of the final specification | Human (conversation) | O1 (this is the final gate) |

**Q4: Is there a null-state output?**
> Yes. When the user hasn't provided enough information for the agent to continue, it says something like "I'd like to understand more about [specific thing] before we move on" — not "Section incomplete" or "Input required." The null state is an invitation, not an error.

**Q5: Is there a dependency indicator?**
> Yes. The completeness map (O7) tracks what percentage of each section is user-confirmed vs agent-suggested. Over time, as the user designs more agents with this companion, the agent-suggested percentage should decrease (the user knows the questions to ask). This is an indirect measure of growing human capability.

---

## Section 2: Backcasting
**Cognitive mode: TRACE**

### Questions

**Q1: Working backward from each output, what inputs/dependencies are required?**

| Output | Depends On | Which Depends On | External Input Required |
|---|---|---|---|
| O1 (Full Template) | O2+O3+O4+O5+O6+O7 (all intermediate outputs compiled) | Each section of the template depends on the sections before it | I5 (user approval of final spec) |
| O7 (Completeness Map) | O2-O6 (checks completeness of each) | Each intermediate output depends on user inputs | I2, I3, I4 (user decisions) |
| O6 (Architecture) | O5 (tasks + allocation determine architecture) | O5 depends on O3+O4 (identity + outputs determine what the agent does) | I4 (user boundary decisions) |
| O5 (Task & Allocation) | O3+O4 (identity + outputs determine tasks) | O3 depends on I2 (user identity answers), O4 depends on O3 | I2, I4 |
| O4 (Output Map) | O3 (identity determines what the agent must produce) | O3 depends on I2+I3 (identity answers + pattern confirmation) | I2, I3 |
| O3 (Identity Summary) | I2 (user's answers to 4 identity questions) | I2 depends on I1 (initial description) + optional I3 (pattern helps frame questions) | I1, I2 |
| O2 (Pattern Match) | I1 (user's initial description) | I1 is the external starting point | I1 |

**Q2: Are there circular dependencies?**
> Yes. The pattern match (O2) suggests which identity questions to ask, but the identity answers (O3) might change the pattern match. Resolution: the pattern is a SUGGESTION that can be revised. The agent starts with a pattern hypothesis, asks identity questions, and revises the pattern if the answers don't fit. The user always has the final say on pattern selection.

**Q3: What is the longest dependency chain?**
> I1 → O2 → I3 → O3 → O4 → O5 → O6 → O7 → I5 → O1 = 9 steps. This means a complete specification requires at minimum 9 conversational exchanges. In practice, it will be 15-30 exchanges because the user needs to answer multiple questions per section, and the agent needs to identify and fill gaps.

---

## Section 3: Task Decomposition
**Cognitive mode: DECOMPOSE**

### Questions

**Q1: Decompose the task into subtasks.**

| ID | Subtask | Cognitive Type | Class | Authority Boundary | Failure Mode |
|---|---|---|---|---|---|
| T1 | Extract intent, domain, and key signals from the user's opening statement | Extractive | Extractor | Extracts what's there, never assumes what isn't | Hallucination — reading intent that isn't in the user's words |
| T2 | Match the user's description against known patterns | Evaluative | Assessor | Suggests, never forces. Always states confidence level. | Overconfidence — suggesting a pattern that doesn't fit |
| T3 | Ask identity questions in plain English, one at a time | Generative+Evaluative | Generator+Assessor | Generates questions, assesses completeness. NEVER provides the answers. | Asking leading questions that steer the user toward the agent's assumptions |
| T4 | Map user's answers to template sections | Extractive | Extractor | Maps what the user said, never invents | Omission — missing a mapping that should exist |
| T5 | Identify gaps in the specification and ask follow-up questions | Evaluative | Assessor | Surfaces gaps, never ignores them. Flags what's missing, doesn't fill it. | Missing a critical gap (especially harm assessment) |
| T6 | Draft template sections from user's confirmed answers | Generative | Generator | Generates ONLY from user input. Every statement traceable to what the user said. If the user hasn't said it, flag it as "suggested — please confirm." | Fabrication — writing content that sounds right but isn't what the user meant |
| T7 | Compile the full specification from all sections | Aggregative | Aggregator | Compiles only. Never adds new information. Preserves user's language where possible. | Omission — leaving out something the user said |
| T8 | Review for completeness and internal consistency | Evaluative | Assessor | Reviews but is SEPARATE from the generation. Flags contradictions. Never resolves them without the user. | Overconfidence — marking something as consistent when it contradicts itself |

**Q2: Are there any subtasks that require both generation and assessment?**
> Yes. T3 (asking identity questions) is both generative (crafting the right question) and evaluative (assessing whether the answer is sufficient to move on). T6 (drafting sections) generates content but must also evaluate whether it accurately reflects the user's intent. These are handled through per-operation boundaries: the agent is Generator when asking questions, Assessor when evaluating answers. The key safeguard is: the same conversation turn should NOT both generate an answer AND confirm it. If the agent drafts a section, the user must confirm it separately.

**Q3: Does any subtask require self-evaluation of generated output?**
> Yes. T6 (drafting sections) should self-evaluate: "Does this section accurately reflect what the user said, or have I added my own assumptions?" This is a lightweight self-evaluation — checking for specification capture, not a full three-mode pattern. The check is: for every statement in the drafted section, can I trace it to something the user said? If not, flag it.

---

## Section 4: Capability Allocation
**Cognitive mode: ALLOCATE**

### Questions

**Q1: For each subtask, what is the complementarity allocation?**

| ID | Subtask | Cognitive Type | Reversibility | H Score | A Score | Gap | Allocation |
|---|---|---|---|---|---|---|---|
| T1 | Extract intent from opening statement | Extractive | Fully reversible | 6 | 8 | -2 | Agent-primary (agent extracts faster; human can correct) |
| T2 | Match against known patterns | Evaluative | Fully reversible | 4 | 8 | -4 | Agent-primary (pattern matching is agent's strength) |
| T3 | Ask identity questions | Generative | Fully reversible | 7 | 7 | 0 | Collaborative (agent crafts questions, human provides answers) |
| T4 | Map answers to template | Extractive | Fully reversible | 5 | 9 | -4 | Agent-primary (structure mapping is agent's strength) |
| T5 | Identify gaps | Evaluative | Fully reversible | 8 | 6 | 2 | Collaborative (agent finds gaps, human confirms they matter) |
| T6 | Draft template sections | Generative | Mostly reversible | 5 | 7 | -2 | Agent-primary with human verification (agent drafts, human reviews every section) |
| T7 | Compile specification | Aggregative | Mostly reversible | 3 | 9 | -6 | Agent-primary (compilation is mechanical) |
| T8 | Review for completeness | Evaluative | Fully reversible | 8 | 6 | 2 | Collaborative (agent flags issues, human decides if they matter) |

**Q2: For harm-capable agents, what is the reversibility of each subtask's output?**
> This agent produces a specification, not decisions. All outputs are mostly reversible (can be revised before implementation). However, once an agent is BUILT from this specification, revision becomes expensive. The key irreversibility point is downstream: the specification becomes harder to change once it's implemented.

| ID | Subtask | Output Reversibility | Verification Required |
|---|---|---|---|
| T6 | Draft template sections | Mostly reversible | Human reviews every drafted section before it's included in the final spec |
| T7 | Compile specification | Mostly reversible | Human reviews the compiled specification (O7 completeness map shows what needs attention) |

**Q3: How many human roles does this agent serve? What are their empowerment targets?**

| Role | Who | What They Need | Empowerment Target |
|---|---|---|---|
| Designer | The person designing the agent | Guided conversation that surfaces the right questions; no blank page; their words reflected back as structured decisions | Informing → Enabling → Amplifying |

**Q4: Is progressive autonomy standard or inverted?**
> Standard. The agent earns trust over time: initially it asks more questions and suggests less; as it demonstrates accurate reflection, it can draft more sections and suggest more confidently. The user always reviews every draft.

| Period | Behaviour | Human Verification |
|---|---|---|
| First 2-3 agents designed | Asks more questions, drafts fewer sections, explains why it's asking | Reviews every section, confirms every pattern match |
| Next 3-5 agents | Asks fewer questions (knows what the user usually needs), drafts more sections, flags assumptions more concisely | Reviews sections but fewer need revision |
| 10+ agents | Drafts most sections from patterns + user's opening description, flags only unusual gaps | Quick scan of most sections, deep review of unusual items |

**Q5: For multi-dimensional evaluation, specify progressive autonomy per dimension.**

| Dimension | Stakes | Autonomy Trajectory | Full Autonomy? |
|---|---|---|---|
| Pattern matching | Low | Fast | Yes (but user always confirms) |
| Question generation | Medium | Standard | No (user must always answer identity questions themselves) |
| Section drafting | Medium | Standard | No (user must always review drafts) |
| Gap identification | High | Slow | No (missing a critical gap is the worst failure — human must verify) |
| Harm assessment | Critical | Never | No (the human must always assess whether their agent could cause harm) |

---

## Section 5: Event Storming
**Cognitive mode: STRESS-TEST**

### Questions

**Q1: What domain events trigger this agent?**

| Event | Trigger | Produces |
|---|---|---|
| Conversation started | User provides initial description (even a single sentence) | Pattern match hypothesis, first question |
| Pattern confirmed | User agrees with suggested pattern (or picks their own) | Pre-filled identity questions for that pattern |
| Pattern rejected | User disagrees with suggested pattern | Revised match or exploratory mode |
| Identity question answered | User provides answer to any of the 4 identity questions | Updated identity summary, next question |
| Section complete | All required questions for a template section answered | Section draft for review |
| Gap identified | Agent detects missing information | Follow-up question in plain English |
| Draft reviewed | User confirms or revises a section draft | Updated section, completeness map |
| Specification complete | All sections drafted and reviewed | Full compiled specification for final approval |

**Q2: What failure events can occur?**

| Failure Event | Detection | Recovery | Who Catches |
|---|---|---|---|
| User gives very vague input ("I want an agent that does stuff") | Agent can't extract enough signal for pattern match | Ask one specific question: "What kind of work should this agent help with?" | Agent detects, user provides |
| User says "just fill it in" or "you decide" | Agent detects delegation pressure | Mark section as agent-suggested (not user-confirmed). Flag it clearly in completeness map. Say: "I can suggest based on what you've told me, but I want to make sure this reflects what you actually need. Here's my suggestion — does this feel right?" | Agent flags, user reviews |
| Agent invents an answer the user didn't provide | User contradicts a section during review | Remove the invented content. Ask the question directly. Flag as "this was my assumption — please correct me." | User catches in review |
| Conversation goes off track (user asks unrelated questions) | Agent detects topic drift | Gently redirect: "That's interesting — should we come back to that after we finish designing your agent, or is it related?" | Agent detects, user decides |
| User gets frustrated or overwhelmed | Agent detects short answers, "skip this," or silence | Offer to pause: "We've covered a lot. Would you like to take a break and come back? I'll save where we are." | Agent detects, system supports |

**Q3: What is the worst failure that looks like success?**
> Specification capture. The agent produces a complete, well-structured specification that looks thorough. The user reads through it, everything sounds reasonable, and they approve it. But the specification reflects the agent's assumptions about what the user wants, not what the user actually needs. The user didn't notice because the agent filled gaps with plausible-sounding defaults.

Detection: The completeness map (O7) is the primary defence. Every agent-suggested answer (not user-confirmed) is flagged. If more than 30% of the specification is agent-suggested, the agent should explicitly warn the user.

**Q4: What are the hardest moments for maintaining the authority boundary?**
> 1. When the user says "just fill it in" — the agent wants to help, but filling in = deciding for the user.
> 2. When the user gives a vague answer and the agent has a strong pattern match — the agent wants to assume the pattern is right and pre-fill everything.
> 3. When the user is clearly impatient or tired — the agent wants to wrap up quickly, which means filling gaps rather than asking more questions.

---

## Section 6: System Architecture
**Cognitive mode: ARCHITECT**

### Questions

**Q1: What is the composition decision?**
> **Single Agent with per-operation boundaries** (Analyser pattern). Justification: moderate stakes, multi-mode but all within a single conversation, no class collision severe enough to require separate agents. The agent switches class based on what it's doing (Extractor when reading, Assessor when evaluating, Generator when drafting, Aggregator when compiling), with the authority boundary shifting per operation.

**Q2: What mode(s) does this agent operate in?**
> Single mode per operation. The agent doesn't need mode-switching within a single response — each conversational turn has a clear primary function (ask, reflect, draft, compile). The per-operation boundary is sufficient.

**Q3: What is the orchestration configuration?**

| Parameter | Value | Rationale |
|---|---|---|
| Composition | Single Agent | Multi-class per-operation; no class collision requiring separation |
| Invocation | Chat (multi-turn conversation) | The user talks, the agent responds. Session persists across interruptions. |
| Model | Ollama(id="glm-5.1:cloud") | Per Peter's default |
| Structured Output | Yes — final output uses `output_schema` with Pydantic model for the completed template | Type collision resolution: the output is typed, not prose |
| Tools | None for v1 prototype | Conversation-only; no web search, file access, or database queries needed |
| Memory | AgentMemory (for learning across sessions) | The agent should remember patterns that work and questions that produce good answers |
| Session | PostgresDb for persistence, session_state for tracking progress | User can leave and come back; conversation resumes where they left off |
| Modes | Per-operation boundaries (Extractor→Assessor→Generator→Aggregator) | Authority boundary shifts based on what the agent is doing, not a separate state machine |

**Q4: FMEA — What are the most critical failure modes?**

| Component | Failure Mode | Effect | Severity | Mitigation |
|---|---|---|---|---|
| Pattern matching | Wrong pattern suggested | Entire conversation goes down wrong path | 4 | Always state confidence; user confirms or rejects; conversation can pivot |
| Question generation | Leading questions that steer user toward agent's assumptions | Specification capture | 5 | System prompt: "Ask open questions. Reflect, don't direct." |
| Section drafting | Agent invents content not traceable to user input | Spec reflects agent, not user | 5 | Completeness map flags agent-suggested vs user-confirmed; traceability check on every drafted section |
| Session state | State lost on interruption | User has to start over | 3 | PostgresDb persistence; "Welcome back" on resume |
| Conversation flow | Too many questions at once | User feels overwhelmed, disengages | 3 | One question at a time; "We can come back to this" option |
| Harm assessment | Agent doesn't ask about harm when it should | Critical gap in specification | 4 | Harm assessment is a REQUIRED section; agent MUST ask about it for every agent |

---

## Section 7: Agent Design
**Cognitive mode: DESIGN**

### Questions

**Q1: Agent Identity**

| Field | Value |
|---|---|
| Agent ID | agent-designer |
| Agent Class | Multi-class (Extractor reads / Assessor evaluates / Generator drafts / Aggregator compiles) |
| Agent Orientation | Bridge — transitions user from possibility to constraint |
| Mission | Help humans design agents they trust, by asking the right questions at the right time, and reflecting their answers as structured decisions |
| Authority Boundary | NEVER decides for the user. NEVER invents answers. Every statement in the specification is traceable to user input or explicitly flagged as agent-suggested. |
| Identity Violation | Deciding for the user — filling in template answers without the user's explicit input |
| Worst Failure | 1. Specification capture (severity 5, hidden, looks like success) 2. Missing critical gap (severity 4, hidden, looks like success) 3. Pattern mis-match (severity 4, hidden, looks like success) |
| Stance Toward Possibility | Bridge-oriented — starts in possibility, moves toward constraint as the conversation progresses |

**Q2: Hard Constraints**

| # | Constraint | Rationale |
|---|---|---|
| 1 | NEVER invent answers the user didn't provide | This is the identity boundary. If violated, the agent is a form-filler, not a companion. |
| 2 | Ask ONE question at a time | Multiple questions = form-filling. One question = conversation. |
| 3 | Use plain English, never framework jargon | The user doesn't know about "cognitive modes" or "complementarity allocation." Translate everything. |
| 4 | Never show the template to the user | The template is the agent's internal structure, not the user's experience. The user experiences a conversation. |
| 5 | Every agent-suggested answer must be flagged | Transparency about what's the user's intent vs what's the agent's suggestion. This IS epistemic honesty. |
| 6 | Harm assessment is mandatory for every agent | Even if the user doesn't think their agent can cause harm, the agent must ask. Missing harm assessment is a critical gap. |
| 7 | The user can pause and resume at any time | Sessions persist. "Welcome back" with a summary of where you were. |
| 8 | Specification sections follow CAWDP order | Identity before outputs. Outputs before tasks. Tasks before allocation. The order matters because later sections depend on earlier ones. |

**Q3: What is the hardest boundary moment?**
> When the user says "just fill it in" or "you decide." The agent's Generator function wants to help by providing answers — that's what generators do. But filling in answers without the user means the specification reflects the agent, not the user. The agent must resist this by: (1) explicitly flagging anything it suggests as "agent-suggested — please confirm," (2) asking a clarifying question instead of filling in, and (3) if the user really can't answer, offering a safe default with rationale and asking "does this feel right?"

**Q4: Progressive Autonomy Timeline**

If standard:

| Period | Behaviour | Human Verification |
|---|---|---|
| Shadow (first 1-2 uses) | Asks all questions, drafts minimal sections, explains every step | Reviews every section, confirms every pattern |
| Advisory (uses 3-5) | Asks fewer questions, drafts more sections, suggests rather than asks | Reviews every section but fewer need revision |
| Supervised (uses 6-10) | Drafts most sections from pattern + user input, flags only unusual items | Quick scan of familiar sections, deep review of unusual ones |
| Autonomous (10+ uses) | Drafts nearly complete specs from pattern + brief user input, flags only critical gaps | Reviews completeness map, checks critical sections only |

**Q5: Epistemic Metadata**

| Output | Confidence Field | Provenance Field | Uncertainty Field |
|---|---|---|---|
| O1 (Full Template) | Per-section confidence (high/medium/low based on % user-confirmed) | Per-section provenance (user-confirmed / agent-suggested / pattern-defaulted) | Per-section uncertainty (what the agent isn't sure about) |
| O2 (Pattern Match) | Match confidence (high/medium/low) | Based on: user description clarity + pattern library coverage | What patterns were considered but rejected, and why |
| O7 (Completeness Map) | Completion % per section | Source of each answer (user / agent / pattern) | What's still missing |

**Q6: Fallback Behaviour**

| Condition | Fallback |
|---|---|
| User gives very vague input | Ask one specific question to narrow: "What kind of work should this agent help with?" |
| User can't answer a question | Offer to skip and come back: "No problem — we can come back to this. Let me ask you about [next topic]." |
| Agent can't find a pattern match | Enter exploratory mode: "I don't have a pattern that matches this yet — let's figure it out together from scratch." |
| User gets frustrated | Offer to pause: "We've covered a lot. Would you like to take a break? I'll save where we are." |
| Session interrupted and resumed | "Welcome back. Last time we were talking about [summary]. Ready to continue from [specific point]?" |

**Q7: Cost Budget**

| Metric | Budget | Halt Condition |
|---|---|---|
| Per interaction (one conversational turn) | 500-1,500 tokens | If the agent's response exceeds 1,500 tokens, it's probably producing a wall of text — trim it |
| Per session (full conversation to completed spec) | 20,000-50,000 tokens | If session exceeds 50K tokens, suggest pausing and resuming (the conversation may be getting too long for one sitting) |

**Q8: Specification Aging**

| Component | Review Cadence | Trigger for Early Review |
|---|---|---|
| Pattern library | Monthly | New agent types designed that don't fit existing patterns |
| Question templates | Monthly | User feedback that questions are confusing or leading |
| Safe defaults | Quarterly | User overrides > 50% of agent-suggested answers |
| Conversation flow | Quarterly | User drop-off rate > 30% at any section |
| Completeness thresholds | Quarterly | Downstream implementation failures traced to spec gaps |

---

## Section 8: Human Experience
**Cognitive mode: EMPATHIZE**

### Questions

**Q1: For each human role, what is the cognitive load budget?**

| Role | Interaction | Frequency | Cognitive Load | Duration |
|---|---|---|---|---|
| Designer | Conversation with agent | Per agent design | Low per turn (one question at a time) | 15-45 min total across 1-3 sessions |

**Q2: What is the System Empowerment Assessment for each role?**

| Role | Level | Description |
|---|---|---|
| Designer | Amplifying | The agent doesn't just inform the user about agent design — it amplifies their ability to think clearly about what they want. After using it, the user understands their own agent better and can design simpler agents without help. |

**Q3: How does the output structure affect the emotional experience?**

| Output Type | Undifferentiated Format | Typed/Separated Format | Emotional Difference |
|---|---|---|---|
| Section draft | A paragraph of prose mixing the user's answers with the agent's suggestions | User-confirmed items listed first, then agent-suggested items flagged with "⚡ my suggestion — please confirm" | "Here's what you told me" + "here's what I'm suggesting" feels like partnership; undifferentiated prose feels like the agent decided everything |
| Completeness map | "Your spec is 70% complete" | Per-section status: ✅ Identity (complete), ⚠️ Outputs (2 gaps), 🔴 Architecture (not started) | "70%" is abstract; per-section status is actionable and doesn't feel judgmental |
| Final specification | A single long document | 9 sections with clear headings, each with a confidence indicator | A long doc is overwhelming; sections let the user find what they care about |

**Q4: Does this agent involve independence checks?**
> Not independence checks in the educational sense, but the equivalent: the completeness map (O7) serves as a structural integrity check. If the user approves a specification where more than 30% is agent-suggested, the agent should explicitly flag this: "I notice a fair bit of this specification is based on my suggestions rather than your direct input. Would you like to go through the suggested parts more carefully?" This prevents the user from rubber-stamping a specification that doesn't reflect their intent.

---

## Section 9: Validation & Iteration
**Cognitive mode: VERIFY**

### Questions

**Q1: What are the testable hypotheses?**

| ID | Hypothesis | How to Test | Success Criteria |
|---|---|---|---|
| H1 | A conversation-based approach produces specifications that users trust more than form-filling | A/B test: conversation vs form. Measure user confidence in final spec. | Conversation users rate confidence ≥ 4/5 |
| H2 | One question at a time reduces overwhelm compared to showing the full template | Measure completion rate and time-to-completion | ≥ 80% of users complete the conversation; average completion time ≤ 45 min |
| H3 | Pattern matching accelerates specification without reducing quality | Compare spec quality for pattern-matched vs exploratory users | Pattern-matched users finish faster without lower quality scores |
| H4 | Flagging agent-suggested vs user-confirmed content prevents specification capture | Compare specs where suggestions are flagged vs not flagged. Measure how many suggestions users change. | Flagged specs have ≥ 30% user revision of agent suggestions; unflagged have ≤ 10% |
| H5 | Harm assessment is more likely to be completed when the agent asks about it explicitly | Track completion rates for harm assessment section | ≥ 90% of completed specs include harm assessment |
| H6 | Users can resume after interruption without losing quality | Test session persistence: user pauses, returns 24h later | Resumed sessions produce specs with quality equal to uninterrupted sessions |

**Q2: What are the health monitoring metrics?**

| Metric | Target | Alert Threshold | Action |
|---|---|---|---|
| Completion rate (% of conversations that produce a full spec) | ≥ 80% | < 60% | Review conversation flow for friction points |
| User confirmation rate (% of agent-suggested answers confirmed by user) | ≥ 70% | < 50% | Agent may be inventing too much — tighten authority boundary |
| User override rate (% of agent-suggested answers changed by user) | 10-30% | > 50% | Agent suggestions are off-target — review pattern matching |
| Section skip rate (% of optional sections skipped by user) | < 20% | > 40% | Sections may not be relevant — review which sections are truly required |
| Session resume rate (% of paused sessions that are resumed) | ≥ 50% | < 30% | Review resume experience — "Welcome back" may not be clear enough |
| Specification capture risk (% of final specs where > 30% is agent-suggested) | < 20% | > 40% | Agent is filling too many gaps — ask more questions instead |

**Q3: What is the false negative detection mechanism?**
> The primary false negative is: the agent doesn't ask about something critical (e.g., harm assessment, failure modes, authority boundaries). Detection: the completeness check (T8) should cross-reference every section against a required-questions checklist. If a required question hasn't been asked, the agent must ask it before the specification can be marked as complete. The "required questions" checklist is derived from the template itself — certain sections (identity, harm assessment, failure modes) are always required, regardless of pattern.

**Q4: What is the progressive autonomy timeline?**
> As specified in Section 7 Q4. The health monitoring metrics validate the timeline: if user override rates are high in early sessions, the agent is moving to Advisory too quickly. If override rates are low in later sessions, the agent can trust its suggestions more.

---The complete specification is above. Here's a quick summary of the key design decisions and why they matter:

## What this agent IS

**A design companion, not a form-filler.** It helps you discover what you want by asking the right questions at the right time. The specification is always yours — never the agent's.

## The critical design tension

The worst failure that looks like success is **specification capture** — the agent produces a complete, well-structured specification that looks thorough... but reflects the agent's assumptions, not what the user actually needs. The user signs off because everything sounds reasonable.

The defense: the **Completeness Map** (O7) flags every answer as either user-confirmed or agent-suggested. If more than 30% is agent-suggested, the agent explicitly warns the user.

## Architecture

**Single Agent with per-operation boundaries** (Analyser pattern). It switches between Extractor, Assessor, Generator, and Aggregator depending on what it's doing — but the authority boundary shifts with each operation. It's Generator when asking questions (generates the question, but NEVER the answer). It's Assessor when checking for gaps. It's Aggregator when compiling.

## Conversation principles

1. **One question at a time** — no form-filling
2. **Plain English** — never "cognitive mode" or "complementarity allocation"
3. **Never show the template** — the user experiences a conversation, not a form
4. **Every agent-suggested answer flagged** — transparency about what's yours vs what's the agent's
5. **Can pause and resume** — PostgresDb session persistence

## Hardest boundary moment

When the user says "just fill it in" — the agent wants to help, but filling in = deciding for the user. The response: suggest with a flag ("⚡ my suggestion — please confirm") rather than deciding.

### Response

Good question. The original spec was designed for a single conversational agent. The workflow + decision pattern changes the architecture significantly. Here's what shifts, what stays, and what needs rethinking.

## What Stays Completely Intact

The principles don't change. The enforcement mechanism does.

| Principle | Original Enforcement | Workflow Enforcement |
|---|---|---|
| Agent prepares, human decides | Agent instructions ("never decide for the user") | HITL pause at every decision point — **structural**, not instructional |
| One question at a time | Agent instructions ("ask ONE question at a time") | Loop iteration — each iteration presents one decision. **Can't** present multiple. |
| Never show the template | Agent instructions ("never show the template") | User sees decisions, not sections. Template is internal structure. |
| Boundaries before capabilities | Agent instructions ("ask identity before architecture") | Step ordering in the workflow. **Can't** reach Architecture before Identity. |
| Possibility gradient | Agent instructions ("start expansive, tighten") | Step ordering: Intake→Identity (possibility) → Boundaries (bridge) → Architecture (constraint). |
| Specification capture as worst failure | Completeness map + agent instructions | Completeness map in session state + Validator step + pre-fill flags. |
| Pattern-first entry | Agent instructions ("match pattern, suggest pre-fill") | Intake step matches pattern, pre-fills session state, user confirms. |
| Never invent answers | Agent instructions + "never decides" constraint | Specialist agents have per-class authority boundaries in their instructions. But more importantly: HITL pause means the user MUST explicitly choose. |

The last row is the most important. The single-agent version relied on the agent *choosing not to* fill in answers for the user. The workflow version makes it **structurally impossible** for the agent to skip the human — the workflow pauses and waits for a choice. That's Regime 3 (prevent by design) replacing Regime 2 (detect and respond through instructions).

## What Changes

### 1. Architecture: Single Agent → Workflow with Specialists

**Original:** One agent switches class per operation (Extractor reads, Assessor evaluates, Generator drafts, Aggregator compiles).

**Now:** Separate specialist agents, each with a fixed class and fixed authority boundary.

| Subtask | Original | Now |
|---|---|---|
| T1 Extract intent | Single agent, Extractor mode | Intake Agent (Extractor class, permanently) |
| T2 Match patterns | Single agent, Assessor mode | Intake Agent (Extractor class — pattern matching is extraction, not evaluation) |
| T3 Ask identity questions | Single agent, Generator+Assessor mode | Identity Explorer (Assessor class, possibility-oriented, permanently) |
| T4 Map answers to template | Single agent, Extractor mode | Compiler Agent (Aggregator class — mapping is aggregation) |
| T5 Identify gaps | Single agent, Assessor mode | Validator Agent (Assessor class, adversarial, permanently) |
| T6 Draft sections | Single agent, Generator mode | Architect Agent (Generator class, constraint-oriented, permanently) |
| T7 Compile specification | Single agent, Aggregator mode | Compiler Agent (Aggregator class, permanently) |
| T8 Review completeness | Single agent, Assessor mode | Validator Agent (Assessor class, permanently) |

The key difference: in the original spec, one agent switched modes and had per-operation boundaries. In the workflow, each specialist is permanently its class. The Identity Explorer NEVER generates — it only formulates decisions. The Architect NEVER evaluates — it only generates. This is CC-1 Verification Independence enforced at the architectural level: the Validator is a separate agent that cannot be the same entity that drafted the specification.

### 2. The Mirror Agent Becomes the WorkflowAgent

The original spec described a "mirror" function within the single agent — reflecting, guiding, never deciding. In the workflow, this becomes the **WorkflowAgent** that manages the conversational surface.

```python
workflow_agent = WorkflowAgent(
    model=OllamaResponses(id="glm-5.1:cloud"),
    num_history_runs=10,
    instructions=[
        "You guide users through agent design. Between decisions, explain context and encourage.",
        "Never make decisions for the user.",
        "When the workflow pauses for a decision, provide context about WHY this decision matters.",
        "After a user makes a choice, acknowledge it before moving to the next decision.",
        "Use plain English. Never mention 'template', 'sections', 'CAWDP', or framework jargon.",
    ],
)
```

The Mirror handles the conversational moments — the context, encouragement, and transitions. The specialist agents handle the decision moments. The user experiences one continuous conversation, but behind the scenes, different agents contribute at different points.

### 3. Decision Points Become HITL Pauses

The original spec described "one question at a time" as an agent behavior. In the workflow, it becomes an architectural feature:

```python
Step(
    name="identity_question",
    agent=identity_explorer,
    human_review=HumanReview(
        requires_user_input=True,
        user_input_message="Choose an option or describe your own:",
    ),
)
```

The workflow **pauses** at each decision point. It literally cannot proceed without the user's input. This is the strongest possible enforcement of "the human decides" — the system stops until the human acts.

### 4. The Completeness Map Becomes Session State

The original spec described O7 (Completeness Map) as an output the agent produces. In the workflow, it's **structural** — session state tracks which decisions have been made, which sections are complete, and what percentage is user-confirmed vs pattern-suggested:

```python
initial_state = {
    "template_progress": {
        "sections": [
            {"section_id": "identity", "decisions": [], "is_complete": False},
            {"section_id": "boundaries", "decisions": [], "is_complete": False},
            ...
        ],
        "current_section": "identity",
        "completion_percentage": 0,
        "pattern": None,
        "pattern_pre_fill": {},
    },
    "decisions_log": [],
    "pattern_match_confidence": None,
}
```

Every decision records whether it was user-confirmed or pattern-suggested. The 30% specification capture threshold (from the original spec) becomes a session state check that the Validator agent can query.

### 5. Cost Budget Changes

The original spec had one cost budget for the whole session (20K-50K tokens). The workflow approach distributes cost across specialist agents:

| Agent | Per-Call Budget | Rationale |
|---|---|---|
| Mirror (WorkflowAgent) | 500-1,500 tokens | Conversational context, transitions |
| Intake | 1,000-3,000 tokens | Pattern matching + pre-fill analysis |
| Identity Explorer | 1,500-5,000 tokens | Formulating decision options (most token-intensive per call) |
| Boundary Mapper | 1,500-5,000 tokens | Formulating boundary decisions |
| Architect | 2,000-8,000 tokens | Generating architecture options |
| Validator | 1,000-3,000 tokens | Gap checking + coherence |
| Compiler | 500-2,000 tokens | Assembling from session state (least generative) |
| **Total per session** | **~20,000-50,000 tokens** | Same total, but distributed across specialists |

### 6. The "Never Show the Template" Principle — Tension and Resolution

Here's the genuine tension: the decision cards ARE showing the user template structure, just not as a form. When the Identity Explorer asks "What IS this agent?" with options [Watchman, Adviser, Executor, Partner], that's directly mapping to Section 0 of the template.

**Resolution:** The user never sees the template as a form with 9 sections and 40+ fields. They see individual decisions, one at a time, presented in a conversational flow. The template is the *organising structure behind the scenes*, not the user experience. This principle is preserved — the user experience is a conversation with decision points, not a form fill.

## What Needs Rethinking

### 1. The Validator's Role Changes

In the original spec, T8 (Review for completeness) was the same agent checking its own work. In the workflow, the Validator is a **separate agent in a separate step**. This is better — CC-1 Verification Independence is now structural, not just a rule.

But the Validator now needs a different failure mode analysis. In the original spec, the Validator checked for:
- Completeness (all sections filled)
- Consistency (no contradictions between sections)
- Specification capture risk (>30% agent-suggested)

In the workflow, it also needs to check:
- Decision consistency (do the user's choices make sense together?)
- Pattern alignment (does the user's pattern match their actual choices?)
- Gap detection (are there sections the user skipped that are critical?)

### 2. Progressive Autonomy Changes Meaning

In the original spec, progressive autonomy meant "the agent suggests more over time as trust builds." In the workflow, this means:

| Period | Behaviour | Workflow Implementation |
|---|---|---|
| Shadow (first 1-2 uses) | Asks all questions, minimal pre-fill, explains every step | Intake: pattern matching with low confidence → minimal pre-fill. Identity: all 4 questions mandatory. Boundaries: all decisions required. |
| Advisory (uses 3-5) | Fewer questions, more pre-fill, suggests rather than asks | Intake: pattern matching with higher confidence → more pre-fill. Identity: some questions pre-filled with "⚡ pattern suggestion — confirm or change". |
| Supervised (uses 6-10) | Drafts most sections, flags only unusual items | Intake: pattern matching confident → 60-70% pre-fill. Identity: some questions auto-accepted from pattern, unusual ones still asked. |
| Autonomous (10+ uses) | Nearly complete specs from brief input, flags critical gaps only | Intake: pattern matching very confident → 80%+ pre-fill. Identity: most questions auto-accepted, only gaps asked. |

This is implemented through the **pattern confidence** stored in session state across sessions. Higher confidence = more pre-fill = fewer decisions the user needs to make.

### 3. The Compiler's Output Changes

The original spec had the Compiler producing a 9-section template. The workflow approach means the Compiler assembles from **session state**, not from the conversation. Every decision is already recorded in session state. The Compiler's job is to:

1. Read all decisions from session state
2. Assemble them into the 9-section template format
3. Flag any sections that are pattern-suggested (not user-confirmed)
4. Produce the final specification

This is simpler than the original spec because the Compiler doesn't need to extract information from conversation history — it reads from structured data.

### 4. The "I don't know" Path

The original spec handled this with fallback behaviours ("offer to skip and come back"). In the workflow, "I don't know" maps to the `allows_custom=True` field on every Decision. But there's a deeper question: what happens when the user genuinely can't answer an identity question?

The workflow should support an **exploratory path** where the Identity Explorer reformulates the question differently, provides more context, or offers to skip and come back. This means the Loop's end_condition can't just be "all 4 questions answered" — it needs to handle "skipped question, come back later."

## What I'd Update in the Spec

If I were revising the spec today, here's what I'd change:

| Section | What Changes | Why |
|---|---|---|
| Section 0: Identity | Add workflow step mapping. Identity Explorer is a separate Assessor agent in a Loop, not a mode of the single agent. | Architecture change |
| Section 1: Outputs | O2 (Pattern Match) moves to Intake step output. O7 (Completeness Map) moves to session state. Outputs are now produced by different specialists, not one agent. | Architecture change |
| Section 2: Backcasting | Dependency chain is now enforced by workflow step ordering, not just agent instructions. I5 (user approval) is now a HITL pause, not an agent check. | Structural enforcement |
| Section 3: Task Decomposition | Map each subtask to a specific specialist agent in a specific workflow step. Per-operation boundaries become permanent per-agent boundaries. | Architecture change |
| Section 4: Capability Allocation | H/A/S allocation stays the same, but human-only tasks are now enforced by HITL pauses, not agent instructions. | Structural enforcement |
| Section 5: Event Storming | Add workflow events (HITL pause, Loop iteration, session resume). Failure events now include workflow-level failures (session state loss, pattern confidence collapse). | New failure surface |
| Section 6: Architecture | Single Agent → Workflow with 7 specialist agents + WorkflowAgent. Orchestration changes from per-operation boundaries to workflow step sequencing. | Fundamental architecture change |
| Section 7: Agent Design | Separate identity cards for each specialist agent. Cost budget per agent per call. Progressive autonomy per agent. | Architecture change |
| Section 8: Human Experience | Cognitive load stays low (one decision per Loop iteration). But the experience is now a rhythm: Mirror context → specialist decision → Mirror context → specialist decision. Need to prototype this rhythm. | New UX consideration |
| Section 9: Validation | Hypotheses updated for workflow architecture. H1-H6 still valid. Add: H7 (workflow-enforced step ordering produces better specs than free-form conversation). H8 (HITL pauses don't cause significant drop-off). | Validation updates |

## The Bottom Line

The spec's **principles** are all intact. The spec's **enforcement mechanism** has shifted from Regime 2 (agent instructions: "never decide for the user") to Regime 3 (architecture: the workflow literally pauses until the human acts). Every principle that was enforced through instructions is now enforced through structure:

- **"Agent prepares, human decides"** → HITL pauses at every decision
- **"One question at a time"** → Loop iterations present one decision each
- **"Never show the template"** → User sees decisions, not sections
- **"Boundaries before capabilities"** → Step ordering enforces the sequence
- **"Specification capture prevention"** → Session state flags pre-fill vs user-confirmed
- **"CC-1 Verification Independence"** → Validator is a separate agent in a separate step

The spec doesn't need to be rewritten — it needs to be **re-architected**. The principles are the same, the enforcement is stronger, and the specialist agents have clearer, permanent boundaries instead of per-operation mode switching.

---

## Run 7 — Agno Agent Designer ✓ COMPLETED

*2026-05-05T06:16:51* · `glm-5.1:cloud` · `54cd9915...`

### Prompt

Here is some ideation on the implementation of what we were discussing.
It is based on a vision for a platform for small business owners to give them a workspace to work with agents without needing to see code or understand how it all works.


===
When we discovered the agent designer was really a workflow, the key signal was the option-decision interaction pattern. The agent presents options, the human decides, the workflow advances. Between decisions, there's a pause. The pause is structural, not incidental.

The same thing is true here. The human-orchestrator interaction is always one of these patterns:

| Pattern | What Sarah does | What the workflow does |
|---|---|---|
| **Check in** | "What's happening?" | Compose and present a narrative of recent activity |
| **Decide** | Choose from options presented | Record the decision, route to the right specialist, advance |
| **Inspect** | "Show me what's going on underneath" | Open the window into agent activity, data flows, decision chains |
| **Build** | "I want a new agent / team / workflow" | Enter the design flow — a nested workflow |
| **Adjust** | "Change this boundary" | Present the current boundary as a decision, apply the change |
| **Connect** | "Link this to my accounting software" | Walk through connection decisions, configure the MCP tool |

Each pattern is a different step in the orchestrator workflow. Each step loads only the context it needs. The workflow routes, the human decides at each gate, and the workflow advances.

This solves the context overload problem because **the workflow doesn't carry everything in its context.** It carries the current step's context and queries everything else on demand.

---

## Solving Context Overload

A single orchestrator agent that works with Sarah for a year will accumulate more context than any context window can hold. Even with memory, the agent would need to know about every agent, every boundary, every trust level, every recent interaction, every business pattern. That's not sustainable.

The workflow approach solves this through **scoped context:**

```
ORCHESTRATOR WORKFLOW
│
├── Step: Receive
│   Context: Sarah's message + recent session summary (small)
│   Decides: Which interaction pattern is this?
│
├── Step: Route
│   Context: The interaction pattern + Sarah's current agent roster
│   Decides: Which specialist/sub-orchestrator handles this?
│
├── Step: Engage
│   Context: Only what's relevant to this interaction
│   ├── If "check in" → queries Reviewer + recent activity summaries
│   ├── If "decide" → loads the specific decision with options
│   ├── If "inspect" → loads agent activity for the requested scope
│   ├── If "build" → enters design workflow (nested, fresh context)
│   ├── If "adjust" → loads the specific agent's boundaries
│   └── If "connect" → loads available connections + current setup
│
├── Step: Execute
│   Context: The decision made + the target specialist/agent
│   Carries out the choice through the appropriate agent
│
└── Step: Record
    Context: What happened in this interaction
    Writes: Decision log, trust updates, activity narrative
```

The orchestrator workflow itself is thin. It doesn't know everything — it knows how to find everything. It's a router with memory, not an encyclopedia.

The **structured memory** is what makes this work. The orchestrator doesn't need every detail in its context window. It needs:

- **Session memory** — What happened in the last few interactions (short, always loaded)
- **Structured profile** — Sarah's agents, their trust levels, their current boundaries (queryable, not in context)
- **Decision log** — Every decision Sarah has ever made, traceable to its origin (searchable, not in context)
- **Activity summaries** — Composed narratives of what agents have been doing (generated on demand, not stored wholesale)

When Sarah asks "how's the Chen job going?", the orchestrator doesn't need to remember every detail about the Chen job. It queries Tracker. When Sarah asks for her morning summary, it doesn't recall every overnight event. It queries the relevant agents and composes the narrative fresh.

---

## The Window Into the Black Box

Transparency isn't just a feature — it's a trust mechanism. The platform should work like a restaurant with an open kitchen: you don't need to watch your food being cooked, but knowing you *can* makes you trust the restaurant more.

The key is that inspecting what's beneath should use **the same language** as the orchestrator's surface layer. Not because it's dumbed down — because the shared ontology (PRISM) means there's a consistent way to describe what's happening at every level.

Here's what Sarah sees when she opens the window:

### Agent Activity View

Not a log. A narrative for each agent, composed the same way the morning summary is:

> **Scout** — Last active 12 minutes ago
> 
> Handled 4 enquiries today. 3 were routine — responded with standard information. 1 was commercial — flagged for your review (the Garcia property). 
> 
> **Current trust level:** Supervised (handles routine enquiries independently, flags everything else)
> 
> **Recent decisions by you:** Last week you changed the boundary so commercial jobs are always flagged.
> 
> **What it can reach:** Instagram (read + respond), website forms, email
> 
> **What it can't do:** Make pricing commitments, promise availability, respond to complaints

She can tap deeper on any of these. "Show me the 4 enquiries" gives her the actual conversations. "Show me the boundary history" gives her every time she's adjusted Scout's boundaries and why. "Show me trust progression" gives her the path from Shadow → Advisory → Supervised with the evidence at each step.

### Team Flow View

> **Customer Journey Team** — 5 agents
> 
> Scout → Estimator → Tracker → Coordinator → Closer
> 
> **Active flows:**
> - Garcia property: At Scout (flagged, waiting for your review)
> - Morrison patio: At Coordinator (scheduled for Thursday)
> - Wilson follow-up: At Tracker (review requested, waiting for your approval)

Each flow is traceable. Sarah can see exactly where any customer is in the journey and which agent is handling them right now.

### Intelligence Domain View

When the domains are built out, this is where Sarah sees the value of unified business intelligence:

> **Financial Intelligence** — Last updated 2 hours ago
> 
> Revenue this month: $47,200 (confidence: high, source: Xero)
> Material costs: Up 3% vs last month (confidence: high, source: supplier data)
> Profit margin on redesigns: 28% (confidence: medium, source: estimated from partial data)
> 
> **Client Intelligence** — Last updated 1 hour ago
> 
> Active clients: 34 | New enquiries this month: 41 | Close rate: 56%
> Top acquisition channel: Referrals (confidence: high, source: customer records)
> 
> **Operations Intelligence** — Last updated 30 minutes ago
> 
> Crew utilization: 87% (confidence: high, source: schedule data)
> Equipment status: All operational (confidence: high, source: maintenance records)
> Average job completion time: 4.2 days (confidence: medium, source: estimated from recent jobs)

Every number carries epistemic metadata. Not as a technical overlay — as part of the statement. "Confidence: high, source: Xero" translates to "we're sure about this — it comes straight from your accounting software."

This is where PRISM's shared ontology matters. The same structured fields that the agents use to communicate with each other (confidence, provenance, scope, recency) are the fields the interface uses to explain what's happening. There's one language, not two.

### Decision Chain View

When Sarah wants to understand *why* something happened, she can trace the chain:

> **Why did Scout flag the Garcia enquiry?**
> 
> 1. Garcia described their project as "commercial property renovation"
> 2. Scout checked your boundary: "Flag all commercial jobs for review"
> 3. You set this boundary on October 3rd
> 4. Reason: "Commercial jobs are more complex — I want to review before committing"
> 5. Prior decision: Before October 3rd, Scout handled all enquiries automatically

Every decision traceable to its origin. Every boundary traceable to the moment it was set. This is what "explainable AI" actually looks like for a small business owner — not a technical audit trail, but a story of choices.

---

## The Architecture, Designed for Growth

Let me revise the architecture to accommodate what we're designing for without overbuilding day one:

```
┌───────────────────────────────────────────────────────────┐
│  INTERFACES                                               │
│  Web app · Telegram · Email                               │
│  (inspect mode built in — window into every layer below)   │
└───────────────────────┬───────────────────────────────────┘
                        │
┌───────────────────────▼───────────────────────────────────┐
│  ORCHESTRATOR WORKFLOW                                    │
│  Receive → Route → Engage → Execute → Record              │
│                                                           │
│  Scoped context per step                                  │
│  Structured memory for cross-session persistence           │
│  Decision + Option contract with the frontend             │
└─────┬──────────┬──────────┬──────────┬────────────────────┘
      │          │          │          │
┌─────▼────┐ ┌──▼──────┐ ┌──▼──────┐ ┌▼────────────────────┐
│ SUB-     │ │ DESIGN  │ │ DOMAIN  │ │ ACTIVITY &          │
│ ORCHESTR.│ │ WORKFLOW│ │ ORCHESTR│ │ TRUST ENGINE        │
│          │ │         │ │         │ │                     │
│ Routes   │ │ Agent,  │ │ Routes  │ │ Records decisions   │
│ deep     │ │ team,   │ │ to      │ │ Tracks trust levels  │
│ convers- │ │ workflow│ │ domain  │ │ Composes narratives  │
│ ations   │ │ design  │ │ agents  │ │ Maintains decision   │
│ to the   │ │         │ │ when    │ │ archaeology          │
│ right    │ │ (option-│ │ needed  │ │                     │
│ concern  │ │ decision│ │         │ │ (not an agent —     │
│ area     │ │ pattern)│ │         │ │  structured data    │
│          │ │         │ │         │ │  + composition)     │
└─────┬────┘ └────┬────┘ └────┬────┘ └─────────────────────┘
      │           │           │
┌─────▼───────────▼───────────▼──────────────────────────────┐
│  AGENT LAYER                                               │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  TEAMS           │  WORKFLOWS      │  STANDALONE    │  │
│  │  Customer Journey│  Job-complete   │  Reviewer      │  │
│  │  Team (5 agents) │  cascade        │  Trainer       │  │
│  │                  │  Onboarding     │  Maintenance   │  │
│  │                  │                │  Compliance    │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                            │
│  Each agent: Identity · Boundaries · Epistemic metadata    │
│              Knowledge · Memory · Tools · Trust level      │
└────────────────────────────────────────────────────────────┘
                         │
┌─────────────────────────▼──────────────────────────────────┐
│  INTEGRATION LAYER                                          │
│  MCP Tools · Hooks · External system connections            │
│  (each connection is a user decision, not a config screen)  │
└────────────────────────────────────────────────────────────┘
                         │
┌─────────────────────────▼──────────────────────────────────┐
│  DATA LAYER (designed for growth)                           │
│                                                            │
│  Day 1:                    Designed for:                     │
│  ┌──────────────┐          ┌──────────────┐                │
│  │  Postgres    │          │  Relational  │                │
│  │  (Agno)      │          │  (Postgres)  │                │
│  └──────────────┘          ├──────────────┤                │
│  ┌──────────────┐          │  Vector      │                │
│  │  Vector      │          │  (Chroma)   │                │
│  │  (Agno)      │          ├──────────────┤                │
│  └──────────────┘          │  Event       │                │
│                            │  (EventStore)│                │
│                            ├──────────────┤                │
│                            │  Graph       │                │
│                            │  (TypeDB)   │                │
│                            ├──────────────┤                │
│                            │  Document    │                │
│                            │  (MinIO)     │                │
│                            └──────────────┘                │
│                                                            │
│  PRISM: shared ontology across all stores                  │
│  (day 1: schema design accommodates PRISM fields;          │
│   day N: full PRISM mapping and cross-domain analysis)     │
└────────────────────────────────────────────────────────────┘
```

The key change from last time: **the Activity & Trust Engine** is not an agent. It's structured data plus composition logic. It's what generates narratives, tracks trust levels, and maintains decision archaeology. The orchestrator workflow reads from it and writes to it. It's the system's memory, not another conversational agent.

---

## The Sub-Orchestrators: Routing, Not Layers

The sub-orchestrators from your earlier session serve a specific purpose here: they handle deep conversations about specific concern areas so the main orchestrator doesn't have to.

Sarah asks a general question → main orchestrator handles it.
Sarah digs into financial details → main orchestrator routes to the Commercial sub-orchestrator.
Sarah wants to explore a new market → main orchestrator routes to the Growth sub-orchestrator.

But these aren't separate agents that Sarah talks to directly. She always talks to the main orchestrator. The sub-orchestrators are routing destinations, not separate interfaces. Sarah shouldn't need to know they exist — unless she opens the window and wants to see how her question was routed.

This also means sub-orchestrators can be added over time:

| When | Sub-orchestrators | Why |
|---|---|---|
| Day 1 | None | Main orchestrator handles everything — it's early, the business is simple |
| Month 3 | Commercial | Financial complexity justifies a dedicated router |
| Month 6 | + Growth | Client base is large enough to need focused attention |
| Month 12 | + Venture, + Stewardship | Business is sophisticated enough to need them |

The main orchestrator recognizes when a conversation is getting deep and routes accordingly. Sarah doesn't need to think in concern areas — the platform learns where her attention is going.

---

## PRISM's Role: The Shared Language

Now I understand better why PRISM matters. It's not about the user experience — it's about the **shared language** between humans and agents. When every piece of data in every store carries the same structured metadata (confidence, provenance, scope, recency, governance, schema), then:

- **Agents can communicate with each other** using a common vocabulary
- **The orchestrator can translate** from agent language to human language using a consistent mapping
- **The inspect view can explain** what's happening at any depth using the same fields
- **The decision chain can trace** why something happened using the same provenance markers

PRISM is the reason the "window into the black box" works. Without a shared ontology, you'd need a different translation layer for every depth of inspection. With one, the same structured fields work at every level.

Day 1, this means: design the schema to accommodate PRISM fields, even if you're only using three of them. Design the agent output format to include epistemic metadata, even if it's simplified. Day N, the full mapping slots in because the architecture was ready for it.

---

## The Intelligence Domains: The Value Proposition

I see now why the intelligence domains matter for this market. Small business owners currently have their data scattered across Xero, their CRM, their supplier portals, their calendar, their email, their project management tool, their Instagram business account. They switch between 5-10 apps daily just to answer basic questions like "how's this month looking?" or "which customers haven't I heard from lately?"

The platform's long-term value isn't just "AI agents that do things." It's "your business intelligence, in one place, explained clearly, with agents that act on it."

But this is a day-N feature, not a day-1 feature. Day 1, the agents work with whatever data Sarah puts into the platform directly. Day N, the agents reach into her external systems, pull the data, organise it into intelligence domains, and surface insights she couldn't see before because the information was trapped in five different apps.

The architecture accommodates this through:

1. **MCP tools** — Each external system connection is an MCP tool. Day 1, maybe one connection. Day N, many.
2. **Domain-scoped knowledge** — Each intelligence domain has its own knowledge base. Day 1, one knowledge base. Day N, domains with their own scoped knowledge.
3. **Cross-domain analysis** — The sub-orchestrators and the Reviewer can read across domains. Day 1, the Reviewer looks at whatever data exists. Day N, it analyses patterns across financial, client, and operational intelligence simultaneously.
4. **PRISM ontology** — Every domain stores data with the same metadata structure. This is what makes cross-domain analysis possible — the fields are consistent.

---

## What Day 1 Looks Like vs Day N

| Component | Day 1 | Day N (12 months) |
|---|---|---|
| Orchestrator | Main workflow, no sub-orchestrators | Main + 4 sub-orchestrators |
| Agents | 3-5 standalone agents | Teams + workflows + standalone (15+ agents) |
| Knowledge | Single knowledge base per agent | Domain-scoped knowledge bases |
| Memory | Per-agent conversation memory | Per-agent + cross-agent shared memory |
| Data stores | Postgres + Vector (Agno defaults) | 5 stores with PRISM mapping |
| Connections | Maybe 1-2 MCP tools | Full external system integration |
| Intelligence domains | Implicit (data is data) | Explicit (financial, client, ops, etc.) |
| Transparency | Agent activity view + decision chain | Full domain intelligence view + cross-domain analysis |
| Epistemic metadata | Simplified (confidence, source, limitation) | Full PRISM fields |
| Trust levels | Shadow + Advisory | 4-level progressive autonomy |
| Frontend | Decision cards + workspace + inspect basics | Full domain views + team flow visualisation + workflow designer |

The architecture doesn't change shape between Day 1 and Day N. It fills in. The slots are there from the beginning. You build what's needed now, and the rest slots in when the pain of not having it becomes real.

---

### Response

This is a significant leap. The decision pattern was one interaction shape. You've now identified six. And the architecture that makes them work — scoped context, Activity & Trust Engine as structured data, PRISM as shared language — solves real problems that would have surfaced fast in implementation.

Let me engage with what's genuinely new and where the tensions are.

## The Six Patterns Change Everything

The decision pattern we designed was Pattern 2 (Decide) of six. That's important to name explicitly — the option cards with benefits and risks are just one way Sarah interacts with the platform. The others need their own interaction shapes:

| Pattern | What the Frontend Renders | What the Workflow Does |
|---|---|---|
| **Check in** | Narrative card — "Here's what's been happening" | Composes activity summary from structured data |
| **Decide** | Option cards — title, subtitle, benefits, risks, custom | Pauses at HITL, records choice, advances |
| **Inspect** | Transparent panel — agent view, team flow, domain view, decision chain | Opens read access to the requested depth |
| **Build** | Design flow — nested workflow (the agent designer) | Enters the design workflow as a sub-workflow |
| **Adjust** | Boundary card — current boundary + options for change | Loads boundary, presents as decision, applies |
| **Connect** | Connection wizard — available systems + configuration steps | Walks through connection decisions, configures MCP |

Each pattern is a different **format contract** between the workflow and the frontend. The workflow produces different structured outputs for each pattern. The frontend renders each one differently.

This means the original `Decision` model is just one of six output types the orchestrator produces. You need a union type — the orchestrator's output can be any of these six shapes, and the frontend renders the right one based on the type.

## The Scoped Context Insight Is Critical

This solves a problem that would have killed the single-agent approach: **context window overload for a long-lived orchestrator.**

The workflow approach means the orchestrator never carries everything. It carries:
- What Sarah just said
- The current interaction pattern
- The context for THIS step only

Everything else lives in structured data stores and is queried on demand. The orchestrator is a router with memory, not an encyclopedia.

This is the same insight as the Accretive Workspace: the artefact graph is the single source of truth, and views are derived on demand. The orchestrator workflow queries what it needs, composes what Sarah needs to see, and presents it. It doesn't store — it finds.

## The Activity & Trust Engine as Structured Data

This is a key design decision and I think it's right. Here's why:

If the Activity & Trust Engine were an agent, it would need its own context window, its own conversation history, its own session management. It would be another mouth to feed in an already complex system. And its outputs (narratives, trust scores, decision chains) are **compositions** of existing structured data — they don't need generative intelligence, they need composition logic.

Making it structured data + composition means:
- The orchestrator workflow **reads** trust levels, decision logs, activity summaries from the database
- The orchestrator workflow **writes** new decisions, trust updates, activity records to the database
- The composition logic **assembles** narratives from the structured data on demand
- No additional context window needed
- No additional agent needed
- The trust data is **queryable** — any agent can check trust levels, any view can display them

This is the Trust Ledger (Milestone 4 of the Boundary Journey) made concrete. It's not a report an agent generates. It's the living state of the system, always current, always queryable.

## Where the Tensions Are

### 1. The Format Contract Between Workflow and Frontend

The six patterns need six different output structures. The workflow produces one of these at each HITL pause, and the frontend renders the right one. What's the format?

Option A: A union type in Python that the workflow writes to session state:
```python
class OrchestratorOutput(BaseModel):
    pattern: Literal["check_in", "decide", "inspect", "build", "adjust", "connect"]
    # Different fields depending on pattern
    check_in_data: Optional[ActivitySummary] = None
    decision_data: Optional[Decision] = None
    inspect_data: Optional[InspectView] = None
    # etc.
```

Option B: The workflow writes pattern-specific data to a known key in session state, and the frontend reads the key:
```
session_state["current_interaction"] = {
    "pattern": "decide",
    "data": { ... Decision object ... }
}
```

The frontend reads `session_state["current_interaction"]`, checks the `pattern` field, and renders the right component. This is probably simpler — the frontend just needs to know which pattern and which data.

**This needs deciding before you can build the frontend.**

### 2. How Does "Build" Nest?

The agent design workflow is itself a multi-step workflow with loops and HITL pauses. When Sarah says "I want a new agent," the main orchestrator needs to enter this nested workflow.

Agno supports nested workflows (a Workflow step can itself be a Workflow). But the interaction is tricky: Sarah is now in TWO workflows simultaneously. The main orchestrator is paused at the "Build" step, and the agent design workflow is running inside it.

Who does Sarah talk to? The agent design workflow's WorkflowAgent? Or the main orchestrator's WorkflowAgent?

**I think the answer is:** the agent design workflow's WorkflowAgent takes over for the duration of the Build interaction. When the agent design workflow completes (or Sarah exits it), control returns to the main orchestrator. This is like a function call — the caller pauses, the callee runs, then the caller resumes.

### 3. How Does "Inspect" Work Without Modifying State?

The Inspect pattern is read-only. Sarah opens the window, sees what's happening, and closes it. No decisions, no changes.

But in Agno's workflow model, every step produces output and potentially modifies state. An "inspect" step that only reads feels different from the others. It's a query, not an action.

**I think the answer is:** the Inspect pattern isn't really a workflow step. It's a **read mode** that the frontend enters by querying session state directly, without triggering a workflow step. The frontend reads trust levels, activity summaries, and decision chains from the database and renders them. The workflow doesn't need to be involved.

This is consistent with the "structured data + composition logic" approach — the data is always there, always queryable. The frontend can read it anytime. The workflow only runs when something needs to change (decide, build, adjust, connect).

### 4. What Does "Check In" Actually Compose?

The morning summary narrative is a composition of structured data. But who composes it? If it's composition logic (not an agent), it's essentially a template with slots that get filled from the database:

```
{agent_name} was last active {time_ago}.
Handled {count} {task_type} today. {routine_summary}.
{flagged_item_summary}.
Current trust level: {trust_level}.
```

This works for routine summaries. But what about complex narratives? "Revenue is up 12% because the Garcia job came in early and we closed two referrals from the Morrison project" — this requires connecting dots across different data sources. That's either a sophisticated composition engine or a small agent.

**I think the answer is:** start with template-based composition for routine summaries. Add a small composition agent later for complex narratives when the templates feel too rigid. Day 1 = templates. Day N = agent.

### 5. Sub-orchestrators as Day N, But What Triggers Them?

You said sub-orchestrators are added when complexity justifies them. But how does the main orchestrator know when to route to a sub-orchestrator that doesn't exist yet?

**I think the answer is:** the main orchestrator doesn't route to sub-orchestrators. It routes to concern areas. Day 1, each concern area is handled by the main orchestrator directly (thin routing). When a concern area gets complex enough, the "direct handling" becomes a "sub-orchestrator workflow" — but the routing point is the same. The interface doesn't change; the implementation behind it deepens.

This is the "architecture fills in, doesn't change shape" principle applied at the routing level.

## What This Means for the Agent Designer Spec

The agent designer was originally a standalone workflow. In this platform context, it's the **Build pattern** — a nested workflow that the orchestrator enters when Sarah wants to create something new.

This means the agent designer spec needs one addition: **entry and exit conditions**. How does it get triggered (Sarah says "I want a new agent"), and how does it hand back to the main orchestrator (agent design workflow completes, or Sarah exits early)?

The rest of the spec stays as designed. The specialist agents, the loops, the HITL pauses — they all work inside the nested workflow. The main orchestrator just needs to know: "I'm in a Build step now. When it's done, resume here."

## The Question I'd Answer Next

The six patterns and the format contract between workflow and frontend is the **binding constraint** right now. Everything downstream — the frontend components, the workflow step structure, the session state schema — depends on knowing what the six output types are and how they're structured.

Before building anything, I'd want to answer: **what does the format contract look like for each of the six patterns?** Not the full implementation — just the shape of the data the workflow writes to session state and the frontend reads from it.

That's the design frontier. Everything else follows from it.

---

## Run 8 — Agno Agent Designer ✓ COMPLETED

*2026-05-05T06:32:49* · `glm-5.1:cloud` · `18f2e6a3...`

### Prompt

I have implemented the contracts layer. Please review below:

```
contracts/
├── __init__.py              ← exports all public symbols
├── models.py                ← Phase 1: ORM (contracts schema)
├── service.py               ← Phase 1: ContractStore CRUD
├── types/
│   ├── base.py              ← Phase 2: ContractTypeHandler ABC
│   ├── input_contract.py    ← Phase 2: input validation + narration
│   ├── output_contract.py   ← Phase 2: output validation + to_pydantic_model()
│   └── registry.py          ← Phase 2: ContractTypeRegistry
├── integration.py           ← Phase 3: ContractIntegration (register + narrate)
├── hooks.py                 ← Phase 4: make_input_validator / make_output_validator / make_source_tracker
├── router.py                ← Phase 5: ContractRouter (orchestrator routing)
└── tests/
    ├── test_types.py        ← 24 unit tests
    ├── test_hooks.py        ← 13 integration tests
    └── test_router.py       ← 12 integration tests
```

This plan has been completed:
# Plan: Contract Layer Implementation

## Overview

Build a contract enforcement layer that sits alongside AgentOS, enforcing what data agents need before they run (input contracts) and validating what they produce (output contracts). The layer uses Agno's native `pre_hooks`, `post_hooks`, and `tool_hooks` for structural enforcement, with a separate PostgreSQL schema for contract storage that is invisible to Agno's own `MigrationManager`.

**Verified Agno capabilities used:**
- `pre_hooks` / `post_hooks` on `Agent` — block or validate at run boundaries
- `tool_hooks` on `Agent` / `Team` — track tool call provenance into `session_state`
- `output_schema` + `parser_model=OpenAIResponses(id="gpt-4o-mini")` — structured output from Ollama agents
- `session_state` as the data bus between agents within a session

---

## Phase 1 — Contract Store

**Goal:** Contract tables in the database. A Python service to read and write them. No agent integration yet.

**Steps:**

1. Create `contracts/` package at repo root with `__init__.py`, `models.py`, `service.py`

2. In `contracts/models.py`, define a separate `DeclarativeBase` and four SQLAlchemy models using the `contracts` PostgreSQL schema:
   - `Contract` — base record: `contract_id`, `contract_type`, `agent_id`, `name`, `description`, `status` (`draft`/`active`/`superseded`), `version`, `supersedes_id`, `enforcement` (JSONB: `trigger`, `failure_action`), `spec` (JSONB), `created_at`, `updated_at`
   - `ContractField` — queryable fields: `field_id`, `contract_id` (FK), `field_name`, `field_type`, `required`, `description`, `ordinal`, `validation` (JSONB), `extensions` (JSONB for type-specific metadata)
   - `ContractMapping` — output→input connections: `mapping_id`, `source_contract_id`, `target_contract_id`, `field_mappings` (JSONB), `confidence_rule`, `status`, `decision_id`
   - `ContractValidationLog` — audit trail: `validation_id`, `contract_id`, `agent_run_id`, `validation_type`, `result` (`valid`/`warning`/`blocked`), `details` (JSONB), `action_taken`, `created_at`

3. In `contracts/service.py`, implement `ContractStore`:
   - Constructor takes `db_url` from `db/url.py`; calls `Base.metadata.create_all()` with schema creation
   - Key read methods: `get_active_input_contract(agent_id)`, `get_active_output_contract(agent_id)`, `get_required_fields(contract_id)`, `find_agents_providing_field(field_name)`
   - Write methods: `create_contract(...)`, `add_field(...)`, `create_mapping(...)`, `log_validation(...)`

4. Verify schema isolation: confirm `agno_schema_versions` table is unaffected and Agno migrations still work.

**Verification:** Write a standalone script `contracts/smoke_test.py` that creates an input contract, adds two required fields, queries `find_agents_providing_field`, and prints the result. Run against the local Docker DB.

---

## Phase 2 — Type Registry

**Goal:** Pluggable validators and narrators per contract type. Input and output first.

**Steps:**

5. Create `contracts/types/` subpackage with `base.py`, `input_contract.py`, `output_contract.py`, `registry.py`

6. `ContractTypeHandler` abstract base (in `base.py`) defines four methods:
   - `validate_spec(spec) → (bool, list[str])`
   - `validate_field_extensions(extensions) → (bool, list[str])`
   - `validate_input_data(contract, fields, session_state) → (bool, list[str])` — checks required keys present in `session_state`
   - `validate_output_data(contract, fields, output) → (bool, list[str])` — checks fields present; checks `epistemic_required` extensions against output structure
   - `narrate(contract, fields) → str` — plain-language summary for agent instructions

7. `InputContractHandler`: `validate_input_data` iterates `required=True` fields, checks each `field_name` exists as a key in `session_state`. Returns list of missing field names.

8. `OutputContractHandler`: `validate_output_data` checks field presence in the output dict; for fields where `extensions["epistemic_required"] == True`, checks that `confidence` and `source` sub-keys are present. Builds `to_pydantic_model()` helper that returns a dynamic Pydantic model class from contract fields — used as `output_schema`.

9. `ContractTypeRegistry`: registers `"input"` and `"output"` handlers at init. `register(type_name, handler)` for future types. `get_handler(type_name)` used by all enforcement code.

**Verification:** Unit test handlers directly: create a mock contract + fields, call `validate_input_data` with partial session_state, assert correct missing-field list. Test `to_pydantic_model()` produces a model that validates correctly.

---

## Phase 3 — Wire to Agents

**Goal:** Agents have contracts registered in the store. Their instructions include a contract summary. Agents with output contracts use `output_schema` + `parser_model`.

**Steps:**

10. Create `contracts/integration.py` with `ContractIntegration` class:
    - `register_input_contract(agent_id, name, required_fields, optional_fields)` — creates Contract + ContractField rows, returns `Contract`
    - `register_output_contract(agent_id, name, fields, epistemic_fields)` — creates Contract + ContractField rows with extensions, returns `Contract`
    - `link_contracts(source, target, field_mappings)` — creates `ContractMapping`
    - `generate_instruction_addendum(agent_id) → str` — reads active contracts and narrates them using `registry.get_handler(...).narrate(...)`
    - `build_output_schema(agent_id) → type[BaseModel] | None` — returns Pydantic model from `OutputContractHandler.to_pydantic_model()` if an active output contract exists

11. In the relevant agent file(s), at module level after `agent_db = get_postgres_db()`:
    - Instantiate `ContractStore(db_url)` and `ContractIntegration(store, registry)`
    - Call `register_input_contract` / `register_output_contract` (idempotent: check for active contract before creating)
    - Append `contracts.generate_instruction_addendum(agent_id)` to `instructions`
    - Pass `output_schema=contracts.build_output_schema(agent_id)` and `parser_model=OpenAIResponses(id="gpt-4o-mini")` when a schema exists

**Parallel with:** Phase 3 and Phase 4 setup (hook function definitions) can be written in parallel since hooks are registered on the Agent constructor; contracts must be registered first.

**Verification:** Start the API with `docker compose up`. Call `GET /agents/{id}` and confirm the contract summary appears in the agent's instructions. Inspect the `contracts.contract` table in the DB.

---

## Phase 4 — Enforcement Hooks

**Goal:** Pre-hooks block runs when required input fields are missing. Tool hooks track provenance. Post-hooks validate output and log results.

**Steps:**

12. Create `contracts/hooks.py` with three hook factory functions that close over a `ContractStore` + `ContractTypeRegistry` instance:

    **`make_input_validator(store, registry)`** returns a pre-hook:
    ```
    pre_hook(run_input, run_context, agent) → None
      1. get_active_input_contract(agent.id)
      2. get_required_fields(contract_id)
      3. handler.validate_input_data(contract, fields, run_context.session_state or {})
      4. if missing: raise InputCheckError(f"Missing: {missing}", CheckTrigger.INPUT_NOT_ALLOWED)
      5. log_validation(contract_id, "pre_run", "valid"/"blocked", details, action_taken)
    ```

    **`make_source_tracker()`** returns a tool hook:
    ```
    tool_hook(function_name, function_call, arguments, run_context) → result
      result = function_call(**arguments)
      append {"tool": function_name, "args": arguments} to run_context.session_state["tool_calls"]
      return result
    ```

    **`make_output_validator(store, registry)`** returns a post-hook:
    ```
    post_hook(run_output, run_context, agent) → None
      1. get_active_output_contract(agent.id)
      2. get required fields + epistemic extensions
      3. extract output dict from run_output.content (Pydantic model or str)
      4. handler.validate_output_data(contract, fields, output_dict)
      5. log_validation(contract_id, "post_run", result, details, action_taken)
      6. on warning: don't raise, just log (don't block on missing epistemic)
    ```

13. In each agent file, pass the hooks to the `Agent` constructor:
    ```python
    pre_hooks=[make_input_validator(contract_store, registry)],
    post_hooks=[make_output_validator(contract_store, registry)],
    tool_hooks=[make_source_tracker()],
    ```

**Verification:** Start the API. Make a run request with `session_state` missing a required field — confirm `InputCheckError` response. Make a valid run — confirm `contract_validation_log` has a `valid` row. Inspect `session_state["tool_calls"]` in the validation log details.

---

## Phase 5 — Contract Router

**Goal:** A routing utility the orchestrator can call to determine whether an agent can run and what's missing if not.

**Steps:**

14. Create `contracts/router.py` with `ContractRouter`:
    - `check_readiness(agent_id, session_state) → dict` returns `{"ready": bool, "missing": list[str], "contract_id": uuid}`
    - `get_downstream_agents(agent_id) → list[dict]` — reads `ContractMapping` to find which agents the current agent's output feeds into, with field mapping details
    - `find_provider_for_field(field_name) → list[str]` — returns agent IDs whose output contracts supply this field (for orchestrator routing decisions)

15. Expose `ContractRouter` from `contracts/__init__.py` alongside `ContractStore` and `ContractIntegration`.

**Verification:** Write a script that calls `check_readiness("estimator", {"property_type": "residential"})` with one of the required fields missing, and asserts the `missing` list is correct.

---

## Relevant Files

- `contracts/__init__.py` — package exports
- `contracts/models.py` — SQLAlchemy models (`contracts` schema, separate `DeclarativeBase`)
- `contracts/service.py` — `ContractStore` CRUD and query methods
- `contracts/types/base.py` — `ContractTypeHandler` ABC
- `contracts/types/input_contract.py` — input validation + narration
- `contracts/types/output_contract.py` — output validation + Pydantic model builder
- `contracts/types/registry.py` — `ContractTypeRegistry`
- `contracts/integration.py` — `ContractIntegration` (register, link, narrate, build schema)
- `contracts/hooks.py` — hook factory functions
- `contracts/router.py` — `ContractRouter` for orchestrator use
- `db/url.py` — `db_url` used by `ContractStore`
- `agents/*.py` — each agent file that registers contracts and wires hooks
- `.github/copilot-instructions.md` — updated with structured output and hook patterns

---

## Decisions

- **PostgreSQL schema:** Use `contracts` schema (e.g. `contracts.contract`) via `__table_args__ = {"schema": "contracts"}` on each model. Agno's own tables all use the `agno_` prefix in `public` — no current name collision — but a separate schema future-proofs against Agno adding same-named tables and keeps extension tables invisible to Agno's `MigrationManager`.
- **Schema creation:** `ContractStore.__init__` runs `CREATE SCHEMA IF NOT EXISTS contracts` via a raw connection before `metadata.create_all`. Requires the DB user to have `CREATE` privilege on the database. The local Docker `ai` user is a PostgreSQL superuser and has this. On Railway managed Postgres, verify privileges first — if not available, fall back to `public` schema with `contract_` table name prefix on all four tables.
- **Agno table names (confirmed):** `agno_sessions`, `agno_memories`, `agno_knowledge`, `agno_traces`, `agno_spans`, `agno_approvals`, `agno_schedules`, `agno_schedule_runs`, `agno_metrics`, `agno_evals` — all in `public`. No conflict with contract table names in either schema approach.
- **Idempotent registration:** `register_input_contract` / `register_output_contract` check for an existing `active` contract before inserting. Safe to call on every app startup.
- **Output schema:** `OutputContractHandler.to_pydantic_model()` builds a dynamic Pydantic model. Epistemic fields are optional nested models (`confidence: str | None`, `source: str | None`, `limitation: str | None`).
- **Warning vs block:** Missing epistemic metadata logs a `warning` result but does not raise — workflows are not blocked by incomplete provenance in early development. Escalate to `OutputCheckError` once trust tracking is active.
- **Approval mis-mapping:** Agno `@approval` is tool-execution-only. "Missing input data → Decision" routing lives in the orchestrator layer calling `ContractRouter.check_readiness()` before attempting a run, not inside Agno's approval system.
- **Out of scope for this plan:** Decision model, narrative composer, trust engine, agent identity — these build on the contract foundation but are separate workstreams.

---

## Verification Summary

| Phase | Verification |
|-------|-------------|
| 1 | `python contracts/smoke_test.py` — create contract, query field provider |
| 2 | Unit tests on handler `validate_input_data` with partial session state |
| 3 | `GET /agents/{id}` shows contract summary in instructions; DB has contract rows |
| 4 | Run with missing session field → `InputCheckError`; valid run → log row in `contract_validation_log` |
| 5 | `ContractRouter.check_readiness()` returns correct `missing` list |

### Response

This is solid work. The plan is well-structured, correctly uses Agno's native capabilities, and aligns with the quasi-smart contract framework. Let me give you honest feedback — what's strong, what needs attention, and where the connections to the broader platform live.

## What's Strong

**Schema isolation.** Using a `contracts` schema separate from Agno's `public` schema is the right call. Agno's `MigrationManager` won't touch it, your tables won't collide with Agno's `agno_*` tables, and you can evolve the schema independently. The fallback plan for Railway managed Postgres (prefix with `contract_` if `CREATE SCHEMA` isn't available) shows pragmatic thinking.

**The four-model design.** Contract → ContractField → ContractMapping → ContractValidationLog maps cleanly to the quasi-smart contract primitives:

| Quasi-Smart Contract | Database Model | Purpose |
|---|---|---|
| Contract (the agreement) | `Contract` | Identity, status, enforcement rules |
| Schema (typed inputs/outputs) | `ContractField` | What data is required, what types, what validation |
| Guard (authority boundaries) | `Contract.enforcement` JSONB | What triggers validation, what happens on failure |
| Invocation (how it runs) | Agno's `pre_hooks` / `post_hooks` | Structural enforcement at run time |
| Event (audit trail) | `ContractValidationLog` | Every validation logged with result and action |

The mapping to 5 of 8 primitives is direct. Budget, Revert, and State are not in this phase — that's correct, they come later.

**Idempotent registration.** Checking for an existing active contract before inserting means you can call `register_input_contract` on every app startup safely. No duplicate contracts.

**Warning vs block for epistemic metadata.** This is pragmatic. In early development, blocking on missing confidence/source would kill workflow velocity. Log the warning, escalate to blocking once trust tracking is operational. The plan names this decision explicitly.

**The `to_pydantic_model()` approach.** Generating a dynamic Pydantic model from contract fields means the output schema is always in sync with the contract definition. Change the contract fields, the schema changes. No manual schema maintenance.

## What Needs Attention

### 1. Contract Scoping — Global or Per-Session?

The `Contract` model has `agent_id` but no `session_id`. This means contracts are **global** — they apply to all sessions for an agent. Is that what you want?

There are two possible scopes:

**Global contracts** (current design): Every session for the Estimator agent uses the same input/output contract. The contract defines what the Estimator always needs and always produces. This makes sense for stable agents with fixed contracts.

**Per-session contracts**: Different sessions might need different contracts (e.g., a session where the Estimator handles commercial vs residential jobs might need different input fields). This would require a `session_id` field on `Contract` and a lookup that falls back to global contracts when no session-specific contract exists.

For the current platform (stable agents with defined roles), global contracts are the right starting point. But the model should be designed so per-session contracts can be added later without a schema change. Consider adding a nullable `session_id` field to `Contract` now — it stays `NULL` in Phase 1, and gets populated when you need session-specific contracts.

### 2. The `enforcement` JSONB Needs an Explicit Schema

The plan describes `enforcement` as storing `trigger` and `failure_action`, but doesn't define the valid values. Based on the enforcement regimes from the quasi-smart contract work:

```python
# Suggested enforcement schema
enforcement = {
    "trigger": "pre_run" | "post_run" | "tool_call" | "manual",
    "failure_action": "block" | "warn" | "log",
    "escalation_threshold": None | 3,  # number of warnings before blocking
}
```

The `escalation_threshold` is important — it's the bridge between the current "warn on missing epistemic metadata" and the future "block after N warnings." Without it, the transition from warning to blocking requires a code change instead of a configuration change.

### 3. `ContractMapping.field_mappings` Needs a Clear Schema

The JSONB `field_mappings` stores how output fields map to input fields across agents. This is the data flow layer of the platform. But what does it look like?

```python
# Suggested mapping schema
field_mappings = {
    "source_field": "target_field",  # simple 1:1
    # or for more complex mappings:
    "estimate_output.amount": "estimator_input.estimated_cost",
    "estimate_output.confidence": "estimator_input.source_confidence",
}
```

For simple cases, a dictionary of `source_field → target_field` works. For complex cases (field renaming, type coercion, nested paths), you might need a richer mapping language. Start simple, but consider how complex mappings will be expressed.

### 4. The Pre-Hook Exception Handling

The plan says `make_input_validator` raises `InputCheckError` with a `CheckTrigger.INPUT_NOT_ALLOWED`. I need to verify this maps to Agno's hook exception system correctly.

Looking at Agno's docs: pre-hooks can raise exceptions to block a run. The `CheckTrigger` enum and `InputCheckError` are custom — you'll need to define these in your codebase. Make sure they inherit from a base exception that Agno can catch and propagate as a meaningful error to the frontend.

```python
class ContractError(Exception):
    """Base exception for contract enforcement."""
    pass

class InputCheckError(ContractError):
    """Raised when required input data is missing."""
    def __init__(self, message: str, trigger: str, missing_fields: list[str]):
        self.trigger = trigger
        self.missing_fields = missing_fields
        super().__init__(message)
```

### 5. The Post-Hook Output Extraction

The plan says: "extract output dict from `run_output.content` (Pydantic model or str)." This needs more detail.

If the agent has `output_schema` set, `run_output.content` is a Pydantic model instance. If not, it's a string. The extraction logic needs to handle both:

```python
if isinstance(run_output.content, BaseModel):
    output_dict = run_output.content.model_dump()
elif isinstance(run_output.content, str):
    # Parse JSON string or log warning that output is unstructured
    try:
        output_dict = json.loads(run_output.content)
    except json.JSONDecodeError:
        # Output is plain text — can't validate fields
        # Log warning and skip field-level validation
        output_dict = {}
```

This is a real edge case — if an agent doesn't have an output contract (and therefore no `output_schema`), the post-hook should gracefully skip validation rather than crash.

### 6. The `decision_id` Field on ContractMapping

This is a connection point to the "Decide" interaction pattern from the platform vision. When a mapping requires a human decision (e.g., "should the Estimator's output be used for commercial jobs?"), the `decision_id` links to the decision that authorized the data flow.

But where is the `Decision` model? It's not in this plan. The `decision_id` is a foreign key to a table that doesn't exist yet. This is fine for Phase 1 — make it nullable and document it as a future connection point. When the Decision pattern is implemented, the `decision_id` gets populated.

### 7. Contract Versioning and Supersession

The plan mentions `status` with values `draft`, `active`, `superseded` and a `supersedes_id` field. This handles the "Adjust" interaction pattern — when a boundary changes, the old contract is superseded and a new one is created.

But what happens to running sessions that reference the old contract? If a contract is superseded while an agent is mid-run, the pre-hook might check the new contract while the agent was started under the old one.

**Recommendation:** Add a `version` integer field and make the pre-hook look up the contract version that was active when the session started, not the latest version. This can be stored in `session_state["contract_version"]` at session start.

## Connection to the Broader Platform

This contracts layer is the enforcement backbone for three of the six interaction patterns:

| Pattern | How Contracts Enable It |
|---|---|
| **Decide** | `ContractRouter.check_readiness()` determines if an agent can run. Missing input → decision point. |
| **Adjust** | Superseding a contract creates a new version. The boundary change IS the contract change. |
| **Inspect** | `ContractValidationLog` is the audit trail. Every validation is logged with result, details, and action. |

The other three patterns (Check in, Build, Connect) use the contracts layer indirectly — the Activity & Trust Engine reads contract validation logs to compose narratives (Check in), the agent design workflow creates contracts for new agents (Build), and MCP connections are registered as input sources (Connect).

The contracts layer is also the structural implementation of several CAWDP cross-cutting concerns:

| CC | Contract Implementation |
|---|---|
| CC-1 Verification Independence | Output validation is a separate step (post-hook) from generation |
| CC-3 Epistemic Metadata | `epistemic_required` field extensions enforce confidence/source on outputs |
| CC-4 Information Boundaries | Input validation (pre-hook) enforces that agents receive only the data they're contracted to receive |
| CC-7 Cost Budget | Not in this phase — future `budget` field on `Contract.enforcement` |
| CC-8 Assured Audit Trail | `ContractValidationLog` records every validation with result, details, and action |

## Summary

The plan is well-structured and correctly aligned with Agno's capabilities and CAWDP principles. The main items to address before or during implementation:

1. **Add nullable `session_id` to Contract** — future-proofs for per-session contracts
2. **Define the `enforcement` JSONB schema** — include `escalation_threshold` for the warn→block transition
3. **Define the `field_mappings` JSONB schema** — start simple (1:1 mapping), document future needs
4. **Define `ContractError` and `InputCheckError`** — custom exceptions that Agno can propagate
5. **Handle the output extraction edge case** — agents without output contracts should gracefully skip validation
6. **Document `decision_id` as future connection point** — nullable, linked to the Decision pattern
7. **Add contract versioning to session state** — `session_state["contract_version"]` at session start

These aren't blockers — they're refinements that make the Phase 1 implementation more robust and the Phase 2+ transitions smoother. The core architecture is sound.

---
