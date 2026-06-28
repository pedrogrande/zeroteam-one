"""
Studio Knowledge Bases
======================

Domain knowledge bases registered with the AgentOS Studio Registry so they
are selectable when building agents, teams, and workflows in Studio.

Each knowledge base uses PgVector (hybrid search) with OpenAI
``text-embedding-3-small`` embeddings and a ``contents_db`` (required for
Studio resolution and the Knowledge UI). PDF uploads are chunked with
:class:`AgenticChunking` via a pre-seeded ``PDFReader``.

Pass ``STUDIO_KNOWLEDGE_BASES`` to ``AgentOS(knowledge=...)`` — AgentOS
auto-discovers them and mirrors them into its internal Registry.
"""

from agno.knowledge.knowledge import Knowledge

from db.session import create_studio_knowledge

# ---------------------------------------------------------------------------
# Domain knowledge bases
# ---------------------------------------------------------------------------
ai_assisted_learning_kb: Knowledge = create_studio_knowledge(
    name="AI Assisted Learning",
    table_name="ai_assisted_learning",
    description=(
        "Research, methods, and practice for using AI to accelerate learning — "
        "study techniques, tutoring patterns, and curriculum design."
    ),
)

agent_design_kb: Knowledge = create_studio_knowledge(
    name="Agent Design",
    table_name="agent_design",
    description=(
        "Patterns and guidance for designing agents — instructions, tool "
        "selection, context management, guardrails, and evaluation."
    ),
)

agentic_workflow_design_kb: Knowledge = create_studio_knowledge(
    name="Agentic Workflow Design",
    table_name="agentic_workflow_design",
    description=(
        "Patterns for orchestrating multi-step agentic pipelines — loops, "
        "conditions, routers, human-in-the-loop gates, and step composition."
    ),
)

user_profile_information_kb: Knowledge = create_studio_knowledge(
    name="User Profile Information",
    table_name="user_profile_information",
    description=(
        "User-specific context — preferences, goals, history, and traits "
        "that personalise agent and team responses."
    ),
)

agentos_lab_kb: Knowledge = create_studio_knowledge(
    name="AgentOS Lab",
    table_name="agentos_lab",
    description=(
        "Operational knowledge for the AgentOS platform itself — setup, "
        "deployment, integrations, and internal tooling."
    ),
)

task_contract_kb: Knowledge = create_studio_knowledge(
    name="Task Contract",
    table_name="task_contract",
    description=(
        "The task contract data model and lifecycle — fields, state machine, "
        "actors, and the API for creating and transitioning contracts."
    ),
)

agno_sessions_kb: Knowledge = create_studio_knowledge(
    name="Agno Sessions",
    table_name="agno_session_transcripts",
    description=(
        "Exported Agno agent/team session transcripts, chunked into "
        "prompt+response runs with enriched metadata (agent name, date, "
        "model, run index). Source for pattern surfacing, decision "
        "archaeology, and cross-session connection."
    ),
)

# ---------------------------------------------------------------------------
# Registry payload — pass to ``AgentOS(knowledge=...)``
# ---------------------------------------------------------------------------
STUDIO_KNOWLEDGE_BASES: list[Knowledge] = [
    ai_assisted_learning_kb,
    agent_design_kb,
    agentic_workflow_design_kb,
    user_profile_information_kb,
    agentos_lab_kb,
    task_contract_kb,
    agno_sessions_kb,
]

# Dict keyed by table_name for agents that need to pick a specific KB
# by table name (e.g. ThinkingPartner uses "user_profile_information").
STUDIO_KNOWLEDGE_BASES_BY_TABLE: dict[str, Knowledge] = {
    kb.vector_db.table_name: kb  # type: ignore[union-attr]
    for kb in STUDIO_KNOWLEDGE_BASES
    if kb.vector_db is not None
}
