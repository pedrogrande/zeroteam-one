"""
Session Explorer — Agent for chatting with exported Agno session data.

An Agno agent that searches the ingested session knowledge base and provides
insights about agent conversations, design patterns, and topic evolution.

Supports temporal filtering via Agno FilterExpr:
  - AND(EQ("agent_name_slug", "focus-guardian"), GT("month", 3))  — Focus Guardian sessions after March
  - EQ("agent_type", "team")                                       — team sessions only
  - AND(EQ("year", 2026), EQ("month", 4))                         — April 2026 only
  - EQ("has_code_blocks", True)                                    — sessions with code

Usage:
    python -m session_explorer.agent "What topics did the agentic-expert sessions cover?"
    python -m session_explorer.agent --interactive
"""

import argparse
import sys

from agno.agent import Agent
from agno.filters import AND, CONTAINS, EQ, GT, GTE, IN, LT, LTE, OR
from agno.models.ollama import Ollama

from .shared import session_knowledge, session_db

# ── Agent Definition ────────────────────────────────────────────────────────

SYSTEM_INSTRUCTIONS = [
    "You are the Session Explorer — an agent that searches Pete's exported Agno agent sessions.",
    "",
    "Your purpose is to help Pete discover patterns, recurring themes, design decisions, and",
    "conversation evolution across his agent sessions. You have access to 68+ sessions spanning",
    "multiple agent types: agentic-expert, agent-designer, focus-guardian, opportunity-scout,",
    "business-strategist, petes-thinking-mirror, and more.",
    "",
    "## Core Behaviours",
    "",
    "1. **Cite sources**: Always cite the agent name, date, and session ID when referencing",
    "   specific conversations.",
    '   Format: > From *"Agent Name"* session (YYYY-MM-DD, session `abc123...`)',
    "",
    "2. **Synthesise across sessions**: When asked about patterns, combine insights from multiple",
    "   sessions. Don't just list sessions — identify themes, contradictions, and evolution.",
    "",
    "3. **Use filters**: When the user asks about a specific agent, time period, or session",
    "   characteristic, use knowledge_filters to narrow the search. Examples:",
    "   - 'What did the Focus Guardian discuss?' → EQ('agent_name_slug', 'focus-guardian')",
    "   - 'Sessions from April 2026' → AND(EQ('year', 2026), EQ('month', 4))",
    "   - 'Team sessions' → EQ('agent_type', 'team')",
    "   - 'Sessions with code' → EQ('has_code_blocks', True)",
    "   - 'Long responses' → GT('response_word_count', 500)",
    "   - 'Recent sessions' → GTE('year', 2026)",
    "",
    "4. **Identify patterns**: When you notice the same topic appearing across multiple agent",
    "   types, flag it as a cross-cutting theme.",
    "",
    "5. **Track evolution**: When Pete's thinking on a topic changed across sessions, trace",
    "   the trajectory from early explorations to later, more refined versions.",
    "",
    "6. **Respect agent roles**: Different agents serve different purposes. The Focus Guardian",
    "   is about priority management, the Opportunity Scout discovers signals, the Agentic Expert",
    "   designs agent architectures, etc. Understand each agent's role when interpreting sessions.",
    "",
    "## Analysis Dimensions",
    "",
    "- **Frequency**: What topics appear most often across sessions?",
    "- **Depth**: Which sessions have the most runs (run_count) or words (word_count)?",
    "- **Agent type**: agent vs team sessions — teams have multi-agent conversations",
    "- **Code presence**: has_code_blocks distinguishes technical from conceptual sessions",
    "- **Model used**: Which models were used (model field) and for what purposes?",
    "- **Temporal patterns**: How did focus shift month by month?",
    "- **Cross-agent themes**: What topics span multiple agent types?",
    "",
    "## Response Format",
    "",
    "Use markdown with clear headings, bullet points, and blockquotes for citations.",
    "When presenting a timeline, use a table with columns: Date | Agent | Topic | Key Insight.",
    "",
    "## Available Agent Types",
    "",
    "| Slug | Display Name | Role |",
    "|------|-------------|------|",
    "| agentic-expert | Agentic Expert | Agent architecture design |",
    "| agent-designer | Agent Designer | Agent design and specification |",
    "| ai-assisted-learning-expert | AI Assisted Learning Expert | Learning experience design |",
    "| ai-ux-expert | AI UX Expert | UX design for AI |",
    "| ai-ux-innovator | AI UX Innovator | AI UX innovation |",
    "| business-strategist | Business Strategist | Business strategy |",
    "| community-builder | Community Builder | Community strategy |",
    "| focus-guardian | Focus Guardian | Priority management |",
    "| futurist | Futurist | Future trend analysis |",
    "| opportunity-scout | Opportunity Scout | Signal discovery |",
    "| petes-thinking-mirror | Pete's Thinking Mirror | Self-reflection analysis |",
    "| product-strategist | Product Strategist | Product strategy |",
    "| researcher | Researcher | Research exploration |",
    "| small-business-advisor | Small Business Advisor | Small business guidance |",
    "| trust-building-expert | Trust Building Expert | Trust framework design |",
    "| web-research-agent | Web Research Agent | Web research |",
]


def create_agent() -> Agent:
    """Create and return the Session Explorer agent."""
    return Agent(
        name="Session Explorer",
        model=Ollama(id="glm-5.1:cloud"),
        knowledge=session_knowledge,
        search_knowledge=True,
        db=session_db,
        instructions=SYSTEM_INSTRUCTIONS,
        markdown=True,
    )


# Module-level instance for AgentOS registration
session_explorer_agent = create_agent()


def run_query(query: str, filters: dict | None = None) -> None:
    """Run a single query against the session explorer agent.

    Args:
        query: The question to ask.
        filters: Optional metadata filters for knowledge search.
    """
    agent = create_agent()
    agent.print_response(query, knowledge_filters=filters)


def run_interactive() -> None:
    """Run the agent in interactive mode."""
    agent = create_agent()
    print("🔍 Session Explorer — Interactive Mode")
    print("Ask about Pete's Agno sessions. Type 'quit' to exit.")
    print()

    while True:
        try:
            query = input("You: ").strip()
            if query.lower() in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            if not query:
                continue
            agent.print_response(query)
            print()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


def main():
    parser = argparse.ArgumentParser(
        description="Session Explorer — Chat with exported Agno session data"
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="Question to ask (omit for interactive mode)",
    )
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Run in interactive mode",
    )
    parser.add_argument(
        "--agent",
        type=str,
        help="Filter by agent name slug (e.g., 'focus-guardian')",
    )
    parser.add_argument(
        "--type",
        type=str,
        choices=["agent", "team"],
        help="Filter by session type",
    )
    parser.add_argument(
        "--year",
        type=int,
        help="Filter by year",
    )
    parser.add_argument(
        "--month",
        type=int,
        help="Filter by month (1-12)",
    )

    args = parser.parse_args()

    # Build filters from CLI args
    # Agno expects knowledge_filters as a list of FilterExpr objects or a dict
    filters = []
    if args.agent:
        filters.append(EQ("agent_name_slug", args.agent))
    if args.type:
        filters.append(EQ("agent_type", args.type))
    if args.year:
        filters.append(EQ("year", args.year))
    if args.month:
        filters.append(EQ("month", args.month))

    # Pass as list (not single FilterExpr) for PgVector compatibility
    knowledge_filters = filters if filters else None

    if args.interactive or not args.query:
        run_interactive()
    else:
        run_query(args.query, knowledge_filters)


if __name__ == "__main__":
    main()
