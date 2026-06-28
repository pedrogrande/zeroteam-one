# AI Assisted Learning

---

## Learning Machines

From [/learning/overview](https://docs.agno.com/learning/overview):

> *"Agents that learn and improve with every interaction."*

From [/learning/stores/intro](https://docs.agno.com/learning/stores/intro):

> *"A Learning Machine coordinates multiple stores, each optimized for a specific type of knowledge."*

The `LearningMachine` coordinates **six stores**:

| Store | What it captures | Scope | Relevance to mentor agent |
|---|---|---|---|
| **User Profile** | Structured fields (name, role, preferences) with custom schemas | Per user | ✅ **Core** — structured learner attributes (background, goals, skill level, learning style) |
| **User Memory** | Unstructured observations and facts | Per user | ✅ **Core** — nuanced observations ("struggles with recursion", "motivated by career switch") |
| **Session Context** | Goals, plans, and progress — with optional planning mode | Per session | ✅ **Core** — tracks the learner's current challenge progress within a session |
| **Entity Memory** | Facts about external entities (people, projects, companies) | Configurable | Optional — could track skills/concepts as entities |
| **Learned Knowledge** | Insights that transfer across users | Configurable | ✅ **Valuable** — patterns like "learners who struggle with X also struggle with Y" |
| **Decision Log** | Decisions with reasoning | Per agent | Optional — audit trail of why the agent recommended certain challenges |

### Learning Modes

From [/learning/learning-modes](https://docs.agno.com/learning/learning-modes):

> *"Learning modes control when and how a Learning Machine captures information. Each store can use a different mode."*

| Mode | How it works | Tradeoff |
|---|---|---|
| **Always** | Extraction runs automatically after each response | Extra LLM call per interaction |
| **Agentic** | Agent receives tools and decides what to save | May miss implicit information |
| **Propose** | Agent proposes learnings, user confirms before saving | Requires user interaction |

Each store can use a **different mode** — this is key. From [/learning/learning-modes](https://docs.agno.com/learning/learning-modes):

> *"Use different modes for different stores"*

### What Each Store Replaces in My Earlier Design

| My earlier approach | Learning Machines equivalent | Why it's better |
|---|---|---|
| `update_memory_on_run=True` + `MemoryManager(additional_instructions=...)` | `user_profile=True` (with custom schema) + `user_memory=True` | Structured profile fields + unstructured observations, purpose-built, no manual `additional_instructions` hacking |
| `enable_session_summaries=True` + `add_session_summary_to_context=True` | `session_context=True` (Session Context Store) | Tracks not just a summary but *goals, plan steps, and progress* — purpose-built for multi-step task tracking |
| `add_session_state_to_context=True` + `enable_agentic_state=True` | `session_context=SessionContextConfig(enable_planning=True)` | Planning mode explicitly tracks goal → plan → completed steps. Injected into system prompt as `<session_context>` block. No need for manual session state management. |

---

## Key Feature: Custom User Profile Schema

This is directly relevant to your onboarding concept. From [/learning/stores/user-profile](https://docs.agno.com/learning/stores/user-profile):

> *"Extend the base schema for your domain"*

```python
from dataclasses import dataclass, field
from typing import Optional
from agno.learn.schemas import UserProfile

@dataclass
class LearnerProfile(UserProfile):
    background: Optional[str] = field(
        default=None,
        metadata={"description": "Professional/academic background"}
    )
    experience_level: Optional[str] = field(
        default=None,
        metadata={"description": "Overall experience level: beginner | intermediate | advanced"}
    )
    learning_goals: Optional[str] = field(
        default=None,
        metadata={"description": "What the learner wants to achieve"}
    )
    preferred_specialisation: Optional[str] = field(
        default=None,
        metadata={"description": "Chosen specialisation pathway, if any"}
    )
    preferred_learning_style: Optional[str] = field(
        default=None,
        metadata={"description": "How the learner prefers to learn: visual | hands-on | reading | project-based"}
    )
    available_time: Optional[str] = field(
        default=None,
        metadata={"description": "Time available for learning per week"}
    )
    timeline: Optional[str] = field(
        default=None,
        metadata={"description": "Target completion timeframe"}
    )
    current_skills: Optional[str] = field(
        default=None,
        metadata={"description": "Skills the learner already has"}
    )
```

The docs explain:
> *"The metadata["description"] tells the LLM what each field captures."*

And the profile is **automatically injected** into the system prompt:

> *"Profiles are automatically injected into the system prompt"* — as a `<user_profile>` block ([/learning/stores/user-profile](https://docs.agno.com/learning/stores/user-profile))

No need for `add_memories_to_context` or manual memory injection — the Learning Machine handles it.

### User Profile vs User Memory — both are needed

From [/learning/stores/user-profile](https://docs.agno.com/learning/stores/user-profile):

> | User Profile | User Memory |
> |---|---|
> | Structured fields | Unstructured text |
> | Fixed schema | Flexible observations |
> | Updated in place | Appended over time |
> | Exact recall | Semantic search |

> *"Use User Profile for: name, company, role, preferences with defined values. Use User Memory for: observations like 'prefers detailed explanations' or 'works on ML projects.'"*

For the mentor agent:

- **User Profile**: structured learner attributes (background, goals, skill level, specialisation)
- **User Memory**: nuanced observations ("learner got excited when discussing [topic]", "struggled with [concept] on challenge #3", "prefers concise feedback over detailed explanations")

---

## Key Feature: Session Context with Planning Mode

This directly addresses your challenge progress tracking. From [/learning/stores/session-context](https://docs.agno.com/learning/stores/session-context):

> *"The Session Context Store captures the current state of a conversation: what's been discussed, what the goal is, and what progress has been made."*

**Planning mode** is the key:

```python
from agno.learn import LearningMachine, SessionContextConfig

learning=LearningMachine(
    session_context=SessionContextConfig(enable_planning=True),
)
```

> *"Enable planning to track goals, plan steps, and progress."*

The data model includes:
>
> - `goal`: What user is trying to accomplish
> - `plan`: Steps to achieve goal
> - `progress`: Completed steps

And it's **injected into the system prompt** automatically:

```xml
<session_context>
Summary: Helping user design a REST API for a todo app...

Goal: Design complete REST API for todo application

Plan:
  1. Define resource endpoints
  2. Choose HTTP methods for each operation
  3. Design request/response schemas
  4. Add authentication

Completed:
  ✓ Define resource endpoints
</session_context>
```

This is purpose-built for your challenge workflow — the agent tracks which steps the learner has completed within a challenge session.

The docs note when Session Context is essential:
> *"Message history gets truncated: long conversations lose early context. Sessions are resumed: user returns after a break. Complex multi-step tasks: track progress through long workflows."*

All three apply to your mentor agent.

---

## Key Feature: Learned Knowledge (Cross-Learner Insights)

From the search results, [/learning/stores/learned-knowledge](https://docs.agno.com/learning/stores/learned-knowledge):

> *"Learned Knowledge stores insights that transfer across users."*

> *"Personalized responses drawing on collective knowledge."*

This is valuable for your use case — patterns like "learners who excel at [concept A] often struggle with [concept B]" or "project-based challenges have higher completion rates than reading-based challenges for beginners." These insights benefit *all* learners, not just one.

Learned Knowledge requires a `Knowledge` instance and defaults to **Agentic mode** (the agent decides what insights are worth saving):

```python
from agno.learn import LearningMachine, LearnedKnowledgeConfig

learning=LearningMachine(
    knowledge=knowledge,
    learned_knowledge=LearnedKnowledgeConfig(),  # defaults to Agentic mode
)
```

---

## Revised Agent Configuration

```python
from dataclasses import dataclass, field
from typing import Optional

from agno.agent import Agent
from agno.run import RunContext
from agno.compression.manager import CompressionManager
from agno.db.postgres import PostgresDb
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.learn import (
    LearningMachine,
    LearningMode,
    UserProfileConfig,
    UserMemoryConfig,
    SessionContextConfig,
    LearnedKnowledgeConfig,
)
from agno.learn.schemas import UserProfile
from agno.models.openai import OpenAIResponses
from agno.vectordb.pgvector import PgVector, SearchType

# ─── Database ───────────────────────────────────────────────────────
db = PostgresDb(
    db_url="postgresql+psycopg://user:pass@localhost:5432/mentor_db",
)

# ─── Knowledge Base (domain expertise) ──────────────────────────────
knowledge = Knowledge(
    name="Domain Knowledge Base",
    description="Curated knowledge for [your specific field]",
    vector_db=PgVector(
        table_name="domain_knowledge",
        db_url="postgresql+psycopg://user:pass@localhost:5432/mentor_db",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)
# Pre-load curated domain content with metadata for filtering
# knowledge.insert(file_path="curricula/module1.pdf",
#     metadata={"topic": "...", "level": "beginner", "pathway": "..."})

# ─── Custom Learner Profile Schema ──────────────────────────────────
@dataclass
class LearnerProfile(UserProfile):
    background: Optional[str] = field(
        default=None,
        metadata={"description": "Professional/academic background"}
    )
    experience_level: Optional[str] = field(
        default=None,
        metadata={"description": "Overall level: beginner | intermediate | advanced"}
    )
    learning_goals: Optional[str] = field(
        default=None,
        metadata={"description": "What the learner wants to achieve"}
    )
    preferred_specialisation: Optional[str] = field(
        default=None,
        metadata={"description": "Chosen specialisation pathway, if any"}
    )
    preferred_learning_style: Optional[str] = field(
        default=None,
        metadata={"description": "Visual | hands-on | reading | project-based"}
    )
    available_time: Optional[str] = field(
        default=None,
        metadata={"description": "Time available for learning per week"}
    )
    timeline: Optional[str] = field(
        default=None,
        metadata={"description": "Target completion timeframe"}
    )
    current_skills: Optional[str] = field(
        default=None,
        metadata={"description": "Skills the learner already has"}
    )

# ─── Learning Machine ───────────────────────────────────────────────
learning = LearningMachine(
    # Structured learner attributes — extracted automatically after each run
    user_profile=UserProfileConfig(
        mode=LearningMode.ALWAYS,
        schema=LearnerProfile,
    ),
    # Unstructured observations about the learner — also automatic
    user_memory=UserMemoryConfig(
        mode=LearningMode.ALWAYS,
    ),
    # Session-level goal/plan/progress tracking — with planning mode
    session_context=SessionContextConfig(
        enable_planning=True,
    ),
    # Cross-learner insights — agent decides what's worth saving
    learned_knowledge=LearnedKnowledgeConfig(
        mode=LearningMode.AGENTIC,
    ),
    # Knowledge base for learned insights to be stored in
    knowledge=knowledge,
)

# ─── Compression Manager ────────────────────────────────────────────
compression_manager = CompressionManager(
    model=OpenAIResponses(id="gpt-4o-mini"),
    compress_tool_results_limit=5,
)

# ─── Dynamic Instructions ───────────────────────────────────────────
def get_mentor_instructions(run_context: RunContext):
    state = run_context.session_state or {}
    stage = state.get("onboarding_step", "welcome")
    
    base_instructions = [
        "You are a personal mentor guiding the learner on a personalised learning journey.",
        "Be encouraging, patient, and specific in your guidance.",
        "Always ground your teaching in the knowledge base — search it before answering.",
        "Adapt your language to the learner's current skill level.",
        "When presenting challenges, explain why they're relevant to the learner's goals.",
        "When assessing submissions, be specific about what was good and what needs work.",
        "Never make up information — if you're unsure, search the knowledge base or say so.",
    ]
    
    if stage == "welcome":
        return base_instructions + [
            "Greet the learner warmly. Introduce yourself as their personal mentor.",
            "Ask them to upload their CV or describe their background.",
            "Ask what they want to learn and why — their motivation matters.",
        ]
    elif stage == "goals":
        return base_instructions + [
            "The learner has shared their background. Now explore their goals in depth.",
            "Ask about their preferred learning style, available time, and timeline.",
            "Suggest 2-3 possible learning pathways based on what you know.",
            "Let the learner choose which pathway appeals to them.",
        ]
    elif stage == "active":
        return base_instructions + [
            "The learner is on an active learning journey.",
            "Use their profile, memories, and session context to guide them.",
            "Present challenges appropriate to their current skill level.",
            "When the learner completes a challenge, assess it and suggest the next step.",
            "Celebrate progress — acknowledge completed milestones.",
        ]
    
    return base_instructions

# ─── Custom Tools (challenge system) ────────────────────────────────
# (same as before — create_challenge, get_available_challenges,
#  assess_submission, get_learner_progress)

# ─── The Agent ───────────────────────────────────────────────────────
mentor_agent = Agent(
    # Identity
    name="Mentor",
    description=(
        "You are a personal mentor guiding learners on a personalised "
        "learning journey in [your specific field]. You adapt to each "
        "learner's background, goals, and pace."
    ),
    
    # Model
    model=OpenAIResponses(id="gpt-5.2"),
    
    # Instructions (dynamic — adapts to onboarding stage)
    instructions=get_mentor_instructions,
    add_instruction_tags=True,
    
    # Database
    db=db,
    
    # ─── Learning Machine (replaces memory + session summaries + state) ───
    learning=learning,
    
    # Knowledge base — domain expertise (Agentic RAG)
    knowledge=knowledge,
    search_knowledge=True,
    enable_agentic_knowledge_filters=True,
    
    # Chat history — conversation continuity within a session
    add_history_to_context=True,
    num_history_runs=3,
    max_tool_calls_from_history=3,
    
    # Tools — challenge system
    tools=[
        create_challenge,
        get_available_challenges,
        assess_submission,
        get_learner_progress,
    ],
    tool_call_limit=8,
    
    # Context compression — manage tool result bloat
    compress_tool_results=True,
    compression_manager=compression_manager,
    
    # Context enrichment
    add_datetime_to_context=True,
    add_name_to_context=True,
    markdown=True,
    
    # Debugging during development
    debug_mode=True,
)
```

---

## What Changed vs My Earlier Design

| Earlier (basic memory) | Revised (Learning Machines) | Why it's better |
|---|---|---|
| `update_memory_on_run=True` | `learning=LearningMachine(user_profile=...)` | Structured schema with domain-specific fields (LearnerProfile). Automatically injected as `<user_profile>` block. No need for custom MemoryManager instructions. |
| `memory_manager=MemoryManager(additional_instructions=...)` | `user_profile=UserProfileConfig(schema=LearnerProfile)` | The schema itself tells the LLM what to extract. No manual instruction hacking. |
| `add_memories_to_context=True` | Automatic via Learning Machine | Profile and memories injected automatically — no flag needed. |
| `enable_session_summaries=True` + `add_session_summary_to_context=True` | `session_context=SessionContextConfig(enable_planning=True)` | Purpose-built for tracking goals, plans, and progress. Injected as `<session_context>` block. Far richer than a summary. |
| `add_session_state_to_context=True` + `enable_agentic_state=True` | Session Context with planning mode | Goal → plan steps → completed steps. No need for manual session state or the implicit `update_session_state` tool. |
| *(not included)* | `learned_knowledge=LearnedKnowledgeConfig(mode=AGENTIC)` | Cross-learner insights — patterns that benefit all learners. New capability not available with basic memory. |
| *(not included)* | `user_memory=UserMemoryConfig(mode=ALWAYS)` | Unstructured observations alongside the structured profile. Two complementary stores instead of one. |

### What Stayed the Same

These were correct in my earlier design and remain:

- `knowledge=Knowledge(...)` + `search_knowledge=True` — domain knowledge via Agentic RAG
- `enable_agentic_knowledge_filters=True` — filter by pathway/level
- Custom tools (create_challenge, get_available_challenges, assess_submission, get_learner_progress)
- `tool_call_limit=8` — prevent runaway tool calls
- `compress_tool_results=True` + `CompressionManager` — manage tool result bloat
- `add_history_to_context=True` + `num_history_runs=3` + `max_tool_calls_from_history=3` — conversation continuity
- Dynamic instructions based on onboarding stage
- `add_datetime_to_context`, `add_name_to_context`, `markdown`
- No `enable_agentic_memory` (avoided the token trap — Learning Machines uses Always mode for profile/memory which is the recommended approach)

---

## Revised Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        MENTOR AGENT                               │
│                                                                   │
│  ┌─ Learning Machine ──────────────────────────────────────────┐ │
│  │                                                              │ │
│  │  ┌─ User Profile Store ──────────────────────────────────┐  │ │
│  │  │  Schema: LearnerProfile (custom)                       │  │ │
│  │  │  Fields: background, experience_level, learning_goals, │  │ │
│  │  │          preferred_specialisation, learning_style,      │  │ │
│  │  │          available_time, timeline, current_skills       │  │ │
│  │  │  Mode: ALWAYS (auto-extracted after each run)          │  │ │
│  │  │  Injection: <user_profile> block in system prompt      │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  │                                                              │ │
│  │  ┌─ User Memory Store ───────────────────────────────────┐  │ │
│  │  │  Unstructured observations about the learner           │  │ │
│  │  │  e.g. "struggles with recursion", "motivated by        │  │ │
│  │  │       career switch", "prefers concise feedback"       │  │ │
│  │  │  Mode: ALWAYS (auto-extracted)                         │  │ │
│  │  │  Injection: semantic search + context injection        │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  │                                                              │ │
│  │  ┌─ Session Context Store ────────────────────────────────┐  │ │
│  │  │  Goal: current challenge or learning task               │  │ │
│  │  │  Plan: steps to complete the challenge                  │  │ │
│  │  │  Progress: completed steps (✓ markers)                  │  │ │
│  │  │  Mode: ALWAYS with enable_planning=True                 │  │ │
│  │  │  Injection: <session_context> block in system prompt    │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  │                                                              │ │
│  │  ┌─ Learned Knowledge Store ───────────────────────────────┐  │ │
│  │  │  Cross-learner insights (benefits ALL learners)         │  │ │
│  │  │  e.g. "learners who excel at X often struggle with Y"   │  │ │
│  │  │  Mode: AGENTIC (agent decides what's worth saving)      │  │ │
│  │  │  Storage: vector DB (same Knowledge instance)           │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  │                                                              │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─ Domain Knowledge (Agentic RAG) ────────────────────────────┐ │
│  │  Curated field-specific content in vector DB                 │ │
│  │  search_knowledge=True → search_knowledge_base tool          │ │
│  │  enable_agentic_knowledge_filters=True → filter by pathway   │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─ Tools (4 custom) ──────────────────────────────────────────┐ │
│  │  create_challenge · get_available_challenges                 │ │
│  │  assess_submission · get_learner_progress                    │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─ Conversation ──────────────────────────────────────────────┐ │
│  │  add_history_to_context=True, num_history_runs=3             │ │
│  │  max_tool_calls_from_history=3                               │ │
│  │  Dynamic instructions (by onboarding stage)                   │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─ Compression ───────────────────────────────────────────────┐ │
│  │  CompressionManager (gpt-4o-mini, limit=5)                   │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─ Persistence (PostgresDb) ──────────────────────────────────┐ │
│  │  Sessions + chat history                                     │ │
│  │  Learner profiles (structured)                               │ │
│  │  Learner memories (unstructured)                             │ │
│  │  Session context (goal/plan/progress)                        │ │
│  │  Learned knowledge (vector embeddings)                        │ │
│  │  Domain knowledge (vector embeddings)                        │ │
│  └──────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────────────────────────────────┐
│                     LEARNER DASHBOARD                             │
│  • Available challenges (from get_available_challenges tool)      │
│  • Progress toward goals (from get_learner_progress tool +        │
│    Session Context planning data)                                 │
│  • Completed challenges with assessment scores                    │
│  • Recommended next steps                                         │
│  • Learner profile (from User Profile Store — access via          │
│    agent.get_learning_machine().user_profile_store.get())         │
└──────────────────────────────────────────────────────────────────┘
```

---

## Accessing Learning Data for the Dashboard

The docs show you can programmatically access each store for dashboard rendering. From [/learning/stores/user-profile](https://docs.agno.com/learning/stores/user-profile):

```python
lm = agent.get_learning_machine()

# Get learner profile
profile = lm.user_profile_store.get(user_id="alice@example.com")
print(profile.background)
print(profile.experience_level)
print(profile.learning_goals)
```

From [/learning/stores/session-context](https://docs.agno.com/learning/stores/session-context):

```python
# Get session context (goal, plan, progress)
context = lm.session_context_store.get(session_id="current_session")
if context:
    print(f"Goal: {context.goal}")
    print(f"Plan: {context.plan}")
    print(f"Progress: {context.progress}")
```

This gives your dashboard direct access to structured progress data without needing the `get_learner_progress` custom tool — though you may still want that tool for the agent itself to use during conversations.

---

## Context Budget Re-Estimate

| Context source | Estimated tokens | Change from earlier |
|---|---|---|
| `description` | ~80 | Same |
| `instructions` (dynamic) | ~300 | Same |
| `add_name_to_context` | ~10 | Same |
| `add_datetime_to_context` | ~20 | Same |
| `markdown=True` | ~15 | Same |
| `<user_profile>` (LearnerProfile) | ~150 | Replaces `add_memories_to_context` (~400) — **smaller** because structured fields are compact |
| User Memory (semantic search results) | ~300 (varies) | Similar to before but more targeted |
| `<session_context>` (with planning) | ~200 | Replaces session summary (~200) + session state (~200) — **smaller** combined |
| `enable_agentic_knowledge_filters` | ~300 | Same |
| `search_knowledge` (implicit tool) | ~150 | Same |
| `learned_knowledge` tools (2: search_learnings, save_learning) | ~300 | **New** — but justified by cross-learner value |
| 4 custom tools | ~600 | Same |
| `add_history_to_context` (3 runs) | ~1,500 | Same |
| **Total static overhead** | **~3,900 tokens** | ~5% lower than before |
| Model context window | 128,000 | |
| **Static usage** | **~3.0%** | ✅ Healthy |

The Learning Machine approach is slightly more context-efficient than the basic memory approach, while providing significantly more structured data.

---

Thank you for pointing me to the Learning Machines docs — this is clearly the right abstraction for your use case. The `LearningMachine` with a custom `LearnerProfile` schema, session context with planning mode, and learned knowledge for cross-learner insights is a much more elegant and purpose-built solution than cobbling together basic memory primitives.

**Sources used:**

- [https://docs.agno.com/learning/overview](https://docs.agno.com/learning/overview) — Learning Machines overview
- [https://docs.agno.com/learning/quickstart](https://docs.agno.com/learning/quickstart) — enabling learning, configuring stores
- [https://docs.agno.com/learning/learning-modes](https://docs.agno.com/learning/learning-modes) — Always/Agentic/Propose modes, per-store configuration, defaults
- [https://docs.agno.com/learning/stores/intro](https://docs.agno.com/learning/stores/intro) — six store types overview
- [https://docs.agno.com/learning/stores/user-profile](https://docs.agno.com/learning/stores/user-profile) — custom schemas, context injection, profile vs memory distinction, accessing profile data
- [https://docs.agno.com/learning/stores/session-context](https://docs.agno.com/learning/stores/session-context) — planning mode, goal/plan/progress data model, context injection, accessing session context data
- [https://docs.agno.com/learning/stores/learned-knowledge](https://docs.agno.com/learning/stores/learned-knowledge) — cross-user insights, combining with other stores
