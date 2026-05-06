"""
WebSearch Agent
===============
"""

from os import getenv

from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.tools.parallel import ParallelTools

from app.settings import default_model
from db import get_postgres_db

# When PARALLEL_API_KEY is set, use the official parallel-web SDK —
# the agent gets `parallel_search` and `parallel_extract` directly.
# Without a key, fall back to the keyless MCP endpoint and the agent
# gets `web_search` and `web_fetch` instead. AgentOS handles MCP
# connect/close as part of its lifespan.
if getenv("PARALLEL_API_KEY"):
    web_tools: ParallelTools | MCPTools = ParallelTools()
else:
    web_tools = MCPTools(url="https://search.parallel.ai/mcp", transport="streamable-http")


WEB_SEARCH_INSTRUCTIONS = """\
Search the web for current information.

Workflow:
1. Use the search tool to find candidate sources for the question.
2. When the user asks about recent events or specific pages, follow up with
   the extract / fetch tool to read the most relevant URLs before answering.
3. Cite the sources you used as plain URLs. Prefer recent, authoritative
   pages. If you cannot find a good answer, say so plainly.
"""


web_search = Agent(
    id="web-search",
    name="WebSearch",
    model=default_model(),
    db=get_postgres_db(),
    tools=[web_tools],
    instructions=WEB_SEARCH_INSTRUCTIONS,
    enable_agentic_memory=True,
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
)
