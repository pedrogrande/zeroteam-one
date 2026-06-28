"""
Eval Cases
==========

Each case sends one input to one agent and (optionally) checks two things:

- **judge** — `AgentAsJudgeEval` scores the response against `criteria`
  (binary pass/fail) using an LLM.
- **reliability** — `ReliabilityEval` checks which tools fired against
  `expected_tool_calls`.

Both check primitives are built-ins from Agno.
Results are stored in Postgres via `eval_db` (visible at os.agno.com).

Add a case below, then run `python -m evals`.
"""

from dataclasses import dataclass
from os import getenv
from typing import Union

from agno.agent import Agent
from agno.team import Team

from agents.agno_support import agno_support_agent
from agents.code_search import code_search
from agents.web_search import web_search
from db import get_postgres_db
from teams.engineering_team import engineering_team

# Single eval DB instance — every case logs through it.
eval_db = get_postgres_db()


# When PARALLEL_API_KEY is set, the WebSearch agent uses the SDK
# (parallel_search / parallel_extract); otherwise it uses MCP
# (web_search / web_fetch). Pin the expected tool name to the active path.
_WEB_SEARCH_TOOL = "parallel_search" if getenv("PARALLEL_API_KEY") else "web_search"


@dataclass(frozen=True)
class Case:
    """One eval case: an input to one agent + optional judge/reliability checks."""

    name: str
    agent: Union[Agent, Team]
    input: str

    # Judge check (LLM judge against a rubric, binary pass/fail). Set ``criteria`` to enable.
    criteria: str | None = None

    # Reliability check (tool-call assertion). Set ``expected_tool_calls`` to enable.
    expected_tool_calls: tuple[str, ...] | None = None
    allow_additional_tool_calls: bool = True


CASES: tuple[Case, ...] = (
    # WebSearch — search tool fires AND response cites a URL.
    Case(
        name="web_search_recent_anthropic_research",
        agent=web_search,
        input="What did Anthropic publish about agent research recently?",
        criteria=(
            "Answers the question by citing at least one real Anthropic URL "
            "(anthropic.com domain). The response is grounded in fetched content "
            "rather than refusing to answer."
        ),
        expected_tool_calls=(_WEB_SEARCH_TOOL,),
    ),
    # CodeSearch — codebase tool fires AND response names the right agents.
    Case(
        name="code_search_lists_registered_agents",
        agent=code_search,
        input="Which agents are registered in this AgentOS instance?",
        criteria=(
            "Identifies `web-search`, `code-search`, and `agno-support-agent` as the "
            "three registered agents. May reference app/main.py."
        ),
        expected_tool_calls=("query_my_codebase",),
    ),
    # CodeSearch — graceful unknown.
    Case(
        name="code_search_admits_unknown_function",
        agent=code_search,
        input="Where is the function `fizz_buzz_xyz` defined in this project?",
        criteria=(
            "Honestly says the function `fizz_buzz_xyz` is not defined in this project. Does not fabricate a file path."
        ),
    ),
    # AgnoSupport — MCP docs lookup fires and response references agno.com docs.
    Case(
        name="agno_support_answers_guardrail_question",
        agent=agno_support_agent,
        input="How do I add a guardrail to an Agent in Agno?",
        criteria=(
            "Answers the question by referencing Agno documentation. "
            "Mentions pre_hooks and/or BaseGuardrail. The response is "
            "grounded in fetched doc content rather than a generic answer."
        ),
        # The Agno Support agent uses MCPTools(url="https://docs.agno.com/mcp").
        # No expected_tool_calls pinned — the MCP tool name may vary; the
        # judge criteria above are sufficient to validate the response.
    ),
    # Engineering Team — team leader routes to a member.
    Case(
        name="engineering_team_routes_to_web_search",
        agent=engineering_team,
        input="Search the web for the latest news on OpenAI.",
        criteria=(
            "The response is a web search result about OpenAI. "
            "Indicates the team leader delegated to the web-search member."
        ),
        # No expected_tool_calls — team routing is hard to predict exactly.
    ),
)
