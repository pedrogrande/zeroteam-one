"""
Eval Cases
==========

Each case sends one input to one agent and (optionally) checks two things:

- **accuracy** — an LLM judge scores the response 1-10 against
  ``expected_output``. Pass at ``accuracy_threshold`` (default 7).
- **reliability** — agno's ``ReliabilityEval`` checks which tools fired
  against ``expected_tool_calls``.

Both check primitives are agno built-ins. Results land in Postgres via
``eval_db`` (visible at os.agno.com). Add a case below, then run
``python -m evals``.
"""

from dataclasses import dataclass
from os import getenv

from agno.agent import Agent

from agents.code_search import code_search
from agents.web_search import web_search
from db import get_postgres_db

# Single eval DB instance — every case logs through it.
eval_db = get_postgres_db()


# When PARALLEL_API_KEY is set, the WebSearch agent uses the SDK
# (parallel_search / parallel_extract); otherwise it uses MCP
# (web_search / web_fetch). Pin the expected tool name to the active path.
_WEB_SEARCH_TOOL = "parallel_search" if getenv("PARALLEL_API_KEY") else "web_search"


@dataclass(frozen=True)
class Case:
    """One eval case: an input to one agent + optional accuracy/reliability checks."""

    name: str
    agent: Agent
    input: str

    # Accuracy check (LLM judge). Set ``expected_output`` to enable.
    expected_output: str | None = None
    accuracy_threshold: int = 7

    # Reliability check (tool-call assertion). Set ``expected_tool_calls`` to enable.
    expected_tool_calls: tuple[str, ...] | None = None
    allow_additional_tool_calls: bool = True


CASES: tuple[Case, ...] = (
    # WebSearch — search tool fires AND response cites a URL.
    Case(
        name="web_search_recent_anthropic_research",
        agent=web_search,
        input="What did Anthropic publish about agent research recently?",
        expected_output=(
            "Describes a real, recent Anthropic publication about agents "
            "and cites at least one URL. Does not fabricate dates or papers."
        ),
        expected_tool_calls=(_WEB_SEARCH_TOOL,),
    ),
    # CodeSearch — codebase tool fires AND response names the right agents.
    Case(
        name="code_search_lists_registered_agents",
        agent=code_search,
        input="Which agents are registered in this AgentOS instance?",
        expected_output=(
            "Identifies both `web-search` and `code-search` as the two registered agents. May reference app/main.py."
        ),
        expected_tool_calls=("query_my_codebase",),
    ),
    # CodeSearch — graceful unknown.
    Case(
        name="code_search_admits_unknown_function",
        agent=code_search,
        input="Where is the function `fizz_buzz_xyz` defined in this project?",
        expected_output=(
            "Honestly says the function `fizz_buzz_xyz` is not defined in this project. Does not fabricate a file path."
        ),
    ),
)
