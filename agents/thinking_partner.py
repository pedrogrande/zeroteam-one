"""
ThinkingPartner Agent
=====================

Wires the rewritten instructions module into a full Agent with
LearningMachine, knowledge, and tools.

Architecture
------------
1. Instructions  — from prompts/thinking_partner_instructions.py
   (progressive disclosure: always-loaded core → on-demand skills)
2. Learning      — LearningMachine with 5 stores:
   - UserProfile (Always)       → PeterCognitiveProfile
   - EntityMemory (Always)      → IntellectualEntityMemory
   - DecisionLog (Agentic)      → agent decides what's significant
   - LearnedKnowledge (Propose) → agent proposes, user confirms
   - SessionContext (Always+Planning) → director/explorer mode detection
3. Knowledge     — "User Profile Information" knowledge base
   (CV, interests, projects) + learned knowledge sink
4. Tools         — minimum sufficient set (3 total):
   - get_skill_instructions  → loads behaviour specs on-demand
   - ParallelTools            → web search (GA API)
   - search_knowledge_base    → implicit (added when knowledge is set)

Key API facts verified against Agno docs (June 2026):
- LearningMachine(db, model, knowledge, ...) — but when passed to Agent
  via learning=, the Agent injects its own db and model automatically.
  Source: https://docs.agno.com/learning/overview
- GoogleDriveTools has NO folder_id constructor parameter. Removed
  from this version. Will be added later with a custom wrapper tool
  for hard enforcement at the tool level.
- Agent.learning accepts Union[bool, LearningMachine]
  Source: https://docs.agno.com/reference/agents/agent
- add_learnings_to_context defaults to True — learnings auto-injected
  Source: https://docs.agno.com/reference/agents/agent (line 80)
- search_knowledge=True is the default when knowledge is set on Agent
  Source: https://docs.agno.com/reference/agents/agent
- add_session_summary_to_context defaults to None, NOT True — must
  be set explicitly. Source: https://docs.agno.com/reference/agents/agent
- LearnedKnowledgeConfig supports namespace param ("global"|"user"|custom)
  Source: https://docs.agno.com/learning/stores/learned-knowledge
- EntityMemoryConfig supports namespace param ("global"|"user"|custom)
  Source: https://docs.agno.com/learning/stores/entity-memory
- DecisionLog AGENTIC mode adds 3 tools: log_decision, record_outcome,
  search_decisions
  Source: https://docs.agno.com/learning/stores/decision-log
- LearnedKnowledge PROPOSE mode: agent proposes, user confirms before
  saving. Available tools: search_learnings, save_learning (propose flow)
  Source: https://docs.agno.com/learning/stores/learned-knowledge
- SessionContext default mode is Always; enable_planning=True adds
  goal/plan/progress tracking.
  Source: https://docs.agno.com/learning/stores/session-context
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from agno.agent import Agent
from agno.learn import (
    LearningMachine,
    LearningMode,
    UserProfileConfig,
    EntityMemoryConfig,
    DecisionLogConfig,
    LearnedKnowledgeConfig,
    SessionContextConfig,
)
from agno.learn.schemas import UserProfile
from agno.tools.parallel import ParallelTools

from app.settings import default_model
from db import get_postgres_db
from db.knowledge_context_provider import KnowledgeContextProvider
from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES_BY_TABLE
from prompts.thinking_partner_instructions import (
    INSTRUCTIONS,
    EXPECTED_OUTPUT,
    ADDITIONAL_CONTEXT,
)

# ---------------------------------------------------------------------------
# Configuration constants
# ---------------------------------------------------------------------------

SKILLS_DIR = Path(__file__).parent / "skills"

# User ID — personal thinking partner. All learning stores scoped to this
# user. Override at run() time for multi-user scenarios.
DEFAULT_USER_ID = "pete@peterargent.com"

# Knowledge base — "User Profile Information" contains the user's CV,
# interests, projects, and background. This serves dual purpose:
# 1. Agent-level: searchable via implicit search_knowledge_base tool
#    (search_knowledge=True is the default when knowledge is set)
# 2. LearningMachine-level: sink for LearnedKnowledge store (agent-curated
#    insights, proposed then confirmed by user)
# Table name of the knowledge base to use. Must match a key in
# STUDIO_KNOWLEDGE_BASES_BY_TABLE (db/knowledge_bases.py).
KNOWLEDGE_BASE_KEY = "user_profile_information"


# ---------------------------------------------------------------------------
# Custom user profile schema
# ---------------------------------------------------------------------------
# Extends the base UserProfile with fields relevant to a thinking partner.
# The metadata["description"] tells the LLM what each field captures.
# Source: https://docs.agno.com/learning/stores/user-profile


@dataclass
class ThinkingPartnerProfile(UserProfile):
    """Extended user profile for the ThinkingPartner agent."""

    role: Optional[str] = field(
        default=None, metadata={"description": "Job title or professional role"}
    )
    company: Optional[str] = field(
        default=None, metadata={"description": "Company or organization"}
    )
    timezone: Optional[str] = field(
        default=None, metadata={"description": "User's timezone, e.g. Australia/Sydney"}
    )
    disclosure_level: Optional[str] = field(
        default=None,
        metadata={
            "description": "Preferred disclosure level: gentle | direct | provocative"
        },
    )
    stakes_level: Optional[str] = field(
        default=None,
        metadata={
            "description": "What's at stake in current work: low | medium | high"
        },
    )
    phase_orientation: Optional[str] = field(
        default=None,
        metadata={
            "description": "Current work phase: explorer | architect | builder | optimizer"
        },
    )


# ---------------------------------------------------------------------------
# Tool: get_skill_instructions
# ---------------------------------------------------------------------------
# Progressive disclosure mechanism. The agent calls this to load behaviour
# specifications on-demand when a trigger fires, rather than having all
# specs in the always-loaded instructions.
#
# Cost: ~100 tokens for the tool definition (always present).
# Saves: ~2,500 tokens when no trigger fires (skill not loaded).
#
# Skills are at agents/skills/<skill_name>/SKILL.md


def get_skill_instructions(skill_name: str) -> str:
    """Load the full instruction content from a skill's SKILL.md file.

    Use this to load detailed behaviour specifications, examples, or
    tool guidance when a behaviour trigger fires or when you need
    reference material that is not in your always-loaded instructions.

    Args:
        skill_name: The skill directory name. Available skills:
            - "thinking-partner-core": Governing delivery rules, energy
              calibration, pattern portfolio, self-check, priority matrix.
              Load whenever ANY behaviour trigger fires.
            - "thinking-partner-contextual": The four contextual behaviours
              (assumption excavation, version awareness, decision
              archaeology, blind spot mirroring).
            - "thinking-partner-expansions": The six expansion behaviours
              (premature convergence, connection surfacing, contrast
              seeding, explorer mode, spark timing, diminishing returns).
            - "thinking-partner-examples": Few-shot examples for each
              behaviour. Load when calibrating response style.
            - "pattern-surfacing": Surface patterns across sessions.
            - "project-tracking": Track projects by name.
            - "google-drive-collab001": Drive operations guidance
              for the collab001 folder.
            - "google-calendar": Delegate calendar tasks to the
              CalendarAgent via AgentOS MCP.

    Returns:
        The full text content of the skill's SKILL.md file.
    """
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_path.exists():
        return f"Skill '{skill_name}' not found at {skill_path}"
    return skill_path.read_text()


# ---------------------------------------------------------------------------
# Agent construction
# ---------------------------------------------------------------------------


def create_thinking_partner(
    user_id: str = DEFAULT_USER_ID,
    debug: bool = False,
) -> Agent:
    """Construct the ThinkingPartner agent.

    All parameters are constructor-locked (cannot be overridden per-run)
    except user_id, which is overridable at run() time.

    Args:
        user_id: The user this thinking partner serves. Scopes all
            learning stores. Override per-run: agent.run(user_id=...).
        debug: Enable debug mode for execution inspection.
    """
    db = get_postgres_db()
    model = default_model()

    # Knowledge — two distinct concerns:
    #
    # 1. learning_sink — "User Profile Information" KB. Passed to
    #    LearningMachine as the LearnedKnowledge store's write sink
    #    (agent proposes, user confirms). Must be a real Knowledge with
    #    insert(); the provider is read-only.
    # 2. knowledge_provider — KnowledgeContextProvider over ALL Studio
    #    KBs. Exposes ONE query_knowledge(question, scope?) tool that
    #    fans out across all KBs (or targets one via scope). Replaces
    #    the former 7 per-KB search_* tools + 1 implicit
    #    search_knowledge_base. The provider's instructions() is
    #    appended to the agent's system prompt (domain index).
    #
    # No knowledge= on the Agent — the provider replaces the
    # KnowledgeProtocol path entirely (no implicit
    # search_knowledge_base tool, no build_context injection).
    learning_sink = STUDIO_KNOWLEDGE_BASES_BY_TABLE[KNOWLEDGE_BASE_KEY]
    knowledge_provider = KnowledgeContextProvider()

    # LearningMachine — 5 stores, each mapped to a ThinkingPartner
    # capability:
    #
    # | Store            | Mode       | Serves                                      |
    # |------------------|------------|---------------------------------------------|
    # | UserProfile      | Always     | PeterCognitiveProfile (disclosure/stakes)   |
    # | EntityMemory     | Always     | IntellectualEntityMemory (concepts, ideas)  |
    # | DecisionLog      | Agentic    | Decision Archaeology + Assumption Excav.    |
    # | LearnedKnowledge | Propose    | Cross-session insights (agent proposes,     |
    # |                  |            | user confirms before saving)                |
    # | SessionContext   | Always+Pln | Director/explorer mode detection            |
    #
    # db and model are NOT passed here — the Agent injects them
    # automatically via _init.set_learning_machine(self) during
    # initialization. See agent.py source.
    #
    # knowledge IS passed here — the LearnedKnowledge store needs it
    # as a sink for agent-curated insights.
    # Source: https://docs.agno.com/learning/stores/learned-knowledge
    learning = LearningMachine(
        knowledge=learning_sink,
        user_profile=UserProfileConfig(
            mode=LearningMode.ALWAYS,
            schema=ThinkingPartnerProfile,
        ),
        entity_memory=EntityMemoryConfig(
            mode=LearningMode.ALWAYS,
            namespace="user",
        ),
        decision_log=DecisionLogConfig(
            mode=LearningMode.AGENTIC,
        ),
        learned_knowledge=LearnedKnowledgeConfig(
            mode=LearningMode.PROPOSE,
        ),
        session_context=SessionContextConfig(
            mode=LearningMode.ALWAYS,
            enable_planning=True,
        ),
    )

    agent = Agent(
        # --- Identity ---
        model=model,
        name="Mind Partner",
        description=(
            "A thinking partner that helps users think more powerfully "
            "by answering questions fully, surfacing patterns, and "
            "expanding frames."
        ),
        # --- Prompt layer (attention-aware ordering) ---
        # INSTRUCTIONS: Role → Principles → Triggers → Skill bridge → Boundaries
        # EXPECTED_OUTPUT: reinforces two most critical constraints
        # ADDITIONAL_CONTEXT: reference appendix (consultative, not active)
        # Provider instructions appended: domain index for query_knowledge.
        instructions=INSTRUCTIONS + "\n\n" + knowledge_provider.instructions(),
        expected_output=EXPECTED_OUTPUT,
        additional_context=ADDITIONAL_CONTEXT,
        # --- Knowledge ---
        # No knowledge= on the Agent — the KnowledgeContextProvider
        # replaces the KnowledgeProtocol path. The provider exposes one
        # query_knowledge(question, scope?) tool (added to tools=[]
        # below) and its instructions() is appended above. This removes
        # the implicit search_knowledge_base tool and the
        # build_context() system-prompt injection — both now handled by
        # the provider.
        # update_knowledge defaults to False — the LearningMachine's
        # LearnedKnowledge store handles knowledge writes via PROPOSE
        # mode (agent proposes, user confirms). Two write paths
        # would conflict.
        # --- Learning ---
        # LearningMachine manages all 5 stores. The older memory_manager /
        # enable_agentic_memory system is NOT used — LearningMachine
        # supersedes it. Using both creates duplicate memory paths.
        # add_learnings_to_context defaults to True — learnings from
        # the LearningMachine are automatically injected into context.
        db=db,
        learning=learning,
        user_id=user_id,
        # --- Tools ---
        # 2 explicit task tools + 1 context-provider tool (query_knowledge)
        # = 3 task tools.
        # Learning stores add their own tools:
        #   DecisionLog (Agentic):     +3 tools (log_decision, record_outcome,
        #                              search_decisions)
        #   LearnedKnowledge (Propose): +2 tools (search_learnings, save_learning
        #                               with propose-then-confirm flow)
        #   UserProfile (Always):       no tools (automatic extraction)
        #   EntityMemory (Always):     no tools (automatic extraction)
        #   SessionContext (Always):   no tools (automatic tracking)
        # Total: 3 task + 5 learning = 8 tools.
        #
        # The single query_knowledge tool replaces the former 7 per-KB
        # search_* tools + 1 implicit search_knowledge_base (8 → 1).
        # An optional scope parameter lets the model target a domain
        # without a separate tool.
        # - get_skill_instructions → behaviour specs (on-demand)
        # - ParallelTools → web search (factual questions, research)
        # - query_knowledge → unified RAG across all Studio KBs (scoped
        #   via optional scope arg)
        tools=[
            get_skill_instructions,
            ParallelTools(max_results=5),
            *knowledge_provider.get_tools(),
        ],
        # Hard enforcement: prevents runaway tool loops.
        # 10 is sufficient for: 1-2 skill loads + 1-2 knowledge searches +
        # 1 web lookup + 2-3 learning tool calls (log decision, search
        # learnings, propose learning) + buffer. Restored from 15 now
        # that the 8 per-KB search tools collapsed into 1.
        tool_call_limit=10,
        # --- Conversation memory ---
        # 5 runs of history — enough to detect 5+ turn patterns (Explorer
        # Mode trigger, Diminishing Returns trigger) without excessive
        # context bloat. DB stores full history regardless.
        add_history_to_context=True,
        num_history_runs=5,
        # Hard enforcement: bounds tool-result tokens from history.
        # Only the 3 most recent tool calls enter context. The DB
        # retains the full record.
        max_tool_calls_from_history=3,
        # --- Cross-session memory ---
        # Search past session conversations for Decision Archaeology and
        # Connection Surfacing. Learning stores (entity_memory,
        # decision_log) provide structured cross-session knowledge;
        # search_session_history provides raw conversation context.
        # Keep at 2 per docs: "advisable to keep this number to 2 or 3."
        # Source: https://docs.agno.com/reference/agents/agent
        search_session_history=True,
        num_history_sessions=2,
        # --- Session summaries ---
        # Provides context about previous sessions without loading full
        # history. Complementary to learning stores — summaries give
        # narrative context, stores give structured facts.
        # FIX: add_session_summary_to_context defaults to None, NOT True.
        # Must be set explicitly — otherwise summaries are generated
        # (costing an LLM call) but never injected into context.
        # Source: https://docs.agno.com/reference/agents/agent (line 25)
        enable_session_summaries=True,
        add_session_summary_to_context=True,
        # --- Compression ---
        # Tool results (web search, knowledge search) can be verbose.
        # Compression summarises results after a threshold, reducing
        # token cost while preserving key facts.
        compress_tool_results=True,
        # --- Context enrichment ---
        # Agent name in the system message — reinforces identity.
        add_name_to_context=True,
        # Datetime supports energy calibration (session duration inference)
        # and temporal references in responses.
        add_datetime_to_context=True,
        # timezone_identifier — adjust to user's actual timezone.
        # timezone_identifier="Australia/Sydney",
        # --- Output ---
        markdown=True,
        # --- Resilience ---
        retries=1,
        exponential_backoff=True,
        # --- Observability ---
        debug_mode=debug,
    )

    return agent


# ---------------------------------------------------------------------------
# Module-level instance for AgentOS registration
# ---------------------------------------------------------------------------
# Constructed at import time, matching the pattern in agents/web_search.py.
# AgentOS handles DB connections and MCP lifecycle as part of its lifespan.

thinking_partner = create_thinking_partner()
