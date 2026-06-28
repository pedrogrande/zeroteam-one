# Agno Learning Capability Use Cases (Exploration)

---

## 1. 🧑‍💼 Personal Assistant

An assistant that gets more useful over time by learning about the user, their relationships, and their ongoing tasks.

**Best stores & modes:**

```python
from agno.learn import (
    LearningMachine, LearningMode,
    UserProfileConfig, SessionContextConfig, EntityMemoryConfig,
)

agent = Agent(
    model=OpenAIResponses(id="gpt-5.2"),
    db=db,
    instructions="You are a helpful personal assistant. Remember preferences without being asked.",
    learning=LearningMachine(
        user_profile=UserProfileConfig(mode=LearningMode.ALWAYS),          # Name, preferences, routines
        session_context=SessionContextConfig(enable_planning=True),          # Track multi-step tasks
        entity_memory=EntityMemoryConfig(
            mode=LearningMode.ALWAYS,
            namespace=f"user:{user_id}:personal",                            # Private per user
        ),
    ),
    user_id=user_id,
)
```

| Store | Why | Mode | Namespace |
|---|---|---|---|
| **User Profile** | Remember name, preferred name, timezone, role — structured, always capture | Always | `user` |
| **User Memory** | "Prefers concise responses", "Working on ML project" — unstructured preferences | Always | `user` |
| **Session Context** | Track planning progress ("help me plan Sarah's visit") across a conversation | Always | per-session |
| **Entity Memory** | Track Sarah (sister), Acme Corp (employer), events — relationships that persist | Always | `user:{id}:personal` (private) |

> **Why Always mode?** Personal details like names, preferences, and relationship facts should be captured consistently — you don't want the agent to miss that someone said "call me Ali."

📚 [Pattern: Personal Assistant](/examples/learning/patterns/personal-assistant)

---

## 2. 🎧 Customer Support Agent

An agent that learns from every resolved ticket, building a shared knowledge base so future customers get faster answers.

**Best stores & modes:**

```python
from agno.knowledge import Knowledge
from agno.learn import (
    LearningMachine, LearningMode,
    UserProfileConfig, SessionContextConfig,
    EntityMemoryConfig, LearnedKnowledgeConfig,
)

knowledge = Knowledge(vector_db=PgVector(...))  # Required for Learned Knowledge

agent = Agent(
    model=OpenAIResponses(id="gpt-5.2"),
    db=db,
    instructions="Check if similar issues have been solved before. Save successful solutions.",
    learning=LearningMachine(
        knowledge=knowledge,
        user_profile=UserProfileConfig(mode=LearningMode.ALWAYS),        # Customer history
        session_context=SessionContextConfig(enable_planning=True),       # Track ticket resolution
        entity_memory=EntityMemoryConfig(
            mode=LearningMode.ALWAYS,
            namespace=f"org:{org_id}:support",                            # Shared across org
        ),
        learned_knowledge=LearnedKnowledgeConfig(mode=LearningMode.AGENTIC),  # Agent decides what's worth saving
    ),
)
```

| Store | Why | Mode | Namespace |
|---|---|---|---|
| **User Profile** | Customer's history, plan tier, preferences | Always | `user` |
| **Session Context** | Track ticket resolution progress | Always | per-ticket |
| **Entity Memory** | Products, past tickets, known bugs — shared across the support org | Always | `org:{id}:support` |
| **Learned Knowledge** | "Chrome cache clears resolve login errors" — insights reusable across all customers | **Agentic** | `global` |
| **Decision Log** | Audit trail: why did the agent escalate? What solution was chosen? | Agentic or Always | per-agent |

> **Why Agentic for Learned Knowledge?** You don't want to auto-save every trivial fact. The agent should decide when a solution is genuinely insightful enough to share. This avoids polluting the knowledge base with noise.

> **Why namespaces?** Entity Memory uses `org:acme:support` so all support agents share knowledge about products and known bugs. Learned Knowledge uses `global` so insights benefit every customer.

📚 [Pattern: Support Agent](/examples/learning/patterns/support-agent)

---

## 3. 🏗️ Engineering Team / Project Management

A team of agents tracking projects, people, and technical decisions across an organization.

**Best stores & modes:**

```python
from agno.team import Team
from agno.learn import (
    LearningMachine, LearningMode,
    UserProfileConfig, EntityMemoryConfig,
    DecisionLogConfig, LearnedKnowledgeConfig,
)

team = Team(
    name="Engineering Leadership",
    members=[project_manager, technical_lead],
    learning=LearningMachine(
        user_profile=UserProfileConfig(mode=LearningMode.ALWAYS),
        entity_memory=EntityMemoryConfig(
            mode=LearningMode.ALWAYS,
            namespace="engineering",                   # Shared across the team
        ),
        decision_log=DecisionLogConfig(mode=LearningMode.AGENTIC),  # Explicit decision logging
        learned_knowledge=LearnedKnowledgeConfig(mode=LearningMode.AGENTIC),
        knowledge=knowledge,
    ),
)
```

| Store | Why | Mode | Namespace |
|---|---|---|---|
| **Entity Memory** | Track projects (Atlas, Beacon, Compass), people (Dave, Eve), relationships (Dave → leads → Atlas) | Always | `engineering` (shared) |
| **Decision Log** | "Chose microservices over monolith for Project Atlas" — with reasoning and alternatives considered | **Agentic** | per-agent |
| **Learned Knowledge** | "Always check egress costs when comparing cloud providers" — cross-user reusable insights | **Agentic** | `engineering` |

> **Why Agentic for Decision Log?** Not every interaction is a significant decision. The agent should use its judgment to log only meaningful choices — e.g., "chose Python over JavaScript" — not every tool call. However, you *can* use Always mode (`DecisionLogConfig()`) if you want every tool call automatically logged for auditing.

> **Entity Memory is the star here.** It captures facts (Project Atlas is a backend rewrite), events (Atlas is behind schedule), and relationships (Dave leads Atlas) — giving the team a living knowledge graph.

📚 [Team Learning: Entity Memory](/examples/teams/learning/team-entity-memory) | [Decision Logs](/learning/stores/decision-log)

---

## 4. 🏥 Regulated / Compliance-Sensitive Agent

An agent in healthcare, finance, or legal domains where you need human approval before saving learned knowledge.

**Best stores & modes:**

```python
from agno.learn import (
    LearningMachine, LearningMode,
    UserProfileConfig, LearnedKnowledgeConfig,
    DecisionLogConfig,
)

agent = Agent(
    model=OpenAIResponses(id="gpt-5.2"),
    db=db,
    learning=LearningMachine(
        knowledge=knowledge,
        user_profile=UserProfileConfig(mode=LearningMode.ALWAYS),          # Still auto-capture who they are
        learned_knowledge=LearnedKnowledgeConfig(mode=LearningMode.PROPOSE), # Agent proposes, human confirms
        decision_log=DecisionLogConfig(),                                    # Always log decisions (audit trail)
    ),
)
```

| Store | Why | Mode | Namespace |
|---|---|---|---|
| **User Profile** | Still auto-capture — names and roles are low-risk | Always | `user` |
| **Learned Knowledge** | High-stakes insights must be **reviewed by a human** before being saved | **Propose** | `global` or `engineering` |
| **Decision Log** | Full audit trail of every decision — required for compliance | Always | per-agent |

> **Why Propose mode?** In regulated environments, you can't let the agent save whatever it wants. The agent proposes an insight ("This patient interaction suggests X"), and a human must confirm before it's persisted. This is critical for quality control and auditability.

📚 [Learning Modes](/learning/learning-modes)

---

## 5. 📚 Research / Knowledge Discovery Agent

An agent that builds a shared institutional knowledge base from research conversations.

**Best stores & modes:**

```python
from agno.learn import (
    LearningMachine, LearningMode,
    LearnedKnowledgeConfig, EntityMemoryConfig,
    SessionContextConfig,
)

agent = Agent(
    model=OpenAIResponses(id="gpt-5.2"),
    db=db,
    learning=LearningMachine(
        knowledge=knowledge,
        session_context=SessionContextConfig(enable_planning=True),    # Track research progress
        entity_memory=EntityMemoryConfig(
            mode=LearningMode.ALWAYS,
            namespace="research_team",                                  # Shared across researchers
        ),
        learned_knowledge=LearnedKnowledgeConfig(mode=LearningMode.AGENTIC),  # Agent curates insights
    ),
)
```

| Store | Why | Mode | Namespace |
|---|---|---|---|
| **Session Context** | Track research goals and progress within a session (planning mode) | Always | per-session |
| **Entity Memory** | Build a knowledge graph of papers, researchers, institutions, datasets | Always | `research_team` |
| **Learned Knowledge** | "Token bucket rate limiting handles bursts better than fixed windows" — reusable across all users | **Agentic** | `global` |

> **Why Agentic for Learned Knowledge?** Research conversations contain a mix of raw data and genuine insights. The agent should actively decide what's worth saving as reusable knowledge, rather than auto-extracting noise.

📚 [Learned Knowledge store](/learning/stores/learned-knowledge)

---

## Quick Reference: Mode Selection Guide

| Use Case | Recommended Stores | Key Modes |
|---|---|---|
| **Personal Assistant** | Profile + Memory + Entity + Session | All Always |
| **Customer Support** | Profile + Session + Entity + Learned Knowledge + Decision Log | Agentic for Learned Knowledge |
| **Project Management Team** | Entity + Decision Log + Learned Knowledge | Agentic for Decisions & Knowledge |
| **Regulated/Compliance** | Profile + Learned Knowledge + Decision Log | **Propose** for Learned Knowledge, Always for Decisions |
| **Research/Knowledge Discovery** | Session + Entity + Learned Knowledge | Agentic for Knowledge, Always for Entity |

---

## Key Design Principles

1. **Always mode** is best for "passive" information that should be captured without explicit action — names, preferences, entity facts, session state. The tradeoff is an extra LLM call per interaction.

2. **Agentic mode** is best for "judgment calls" — insights worth saving, significant decisions. The agent gets tools and decides when to use them. The tradeoff is that the agent may miss implicit information.

3. **Propose mode** is best for "high-stakes" knowledge — the agent suggests, a human confirms. Essential for compliance and quality control.

4. **Namespaces** control sharing scope. Use `user` for private data, `global` for organizational knowledge, and custom namespaces (like `engineering` or `sales_team`) for team-scoped data.

5. **Combine stores** for full coverage. A personal assistant needs Profile + Memory + Entity. A support agent needs all of those plus Learned Knowledge. Don't rely on a single store.

6. **Use the Curator** for long-running agents — prune stale memories and deduplicate to keep the knowledge base healthy over time.
