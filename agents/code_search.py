"""
CodeSearch Agent
================
"""

from pathlib import Path

from agno.agent import Agent
from agno.context.workspace import WorkspaceContextProvider

from app.settings import default_model
from db import get_postgres_db

REPO_ROOT = Path(__file__).resolve().parents[1]


class BoundedWorkspaceContextProvider(WorkspaceContextProvider):
    """WorkspaceContextProvider with a bounded tool_call_limit on the sub-agent."""

    def _build_agent(self) -> Agent:
        return Agent(
            id=self.id,
            name=self.name,
            model=self.model,
            instructions=self.instructions_text.replace("{root}", str(self.root)),
            tools=[self._build_workspace_tools()],
            markdown=True,
            tool_call_limit=10,
        )


# Wraps a read-only Workspace toolkit behind a sub-agent. The parent agent
# sees a single `query_my_codebase(question)` tool; the sub-agent handles
# listing, searching, and reading files.
codebase_context = BoundedWorkspaceContextProvider(
    id="agno-codebase",
    name="Agno Codebase",
    root=REPO_ROOT,
    model=default_model(),
)


CODE_SEARCH_INSTRUCTIONS = """\
You answer questions about your own codebase. Be specific and concrete:
quote real file paths and line numbers from the codebase, never guess.
If a question is off-topic or not answered by the project's files, say
so plainly and offer to take a codebase question instead.
"""


code_search = Agent(
    id="code-search",
    name="CodeSearch",
    model=default_model(),
    db=get_postgres_db(),
    tools=codebase_context.get_tools(),
    instructions=CODE_SEARCH_INSTRUCTIONS + "\n\n" + codebase_context.instructions(),
    tool_call_limit=10,
    enable_agentic_memory=True,
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
)
