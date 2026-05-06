# Connecting MCP Servers

AgentOS can connect to any [Model Context Protocol](https://modelcontextprotocol.io) server. Each server exposes tools your agents can use.

## Why MCP?

- **No custom code** — any MCP server works out of the box.
- **Tool discovery** — tools are discovered from the server at connect time.
- **Lifecycle handled for you** — AgentOS connects/closes MCP sessions automatically as part of its lifespan.

The WebSearch agent in this template falls back to `MCPTools` against Parallel's keyless MCP server when no `PARALLEL_API_KEY` is set — see [`agents/web_search.py`](../agents/web_search.py) for a reference implementation.

## Adding an MCP server

Use `MCPTools` from agno. Three transports are supported.

### Streamable HTTP (hosted)

```python
from agno.tools.mcp import MCPTools

github_tools = MCPTools(
    url="https://mcp.github.com/mcp",
    transport="streamable-http",
)
```

For headers (e.g. bearer-token auth), use `server_params`:

```python
from agno.tools.mcp import MCPTools
from agno.tools.mcp.params import StreamableHTTPClientParams

github_tools = MCPTools(
    transport="streamable-http",
    server_params=StreamableHTTPClientParams(
        url="https://mcp.github.com/mcp",
        headers={"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN', '')}"},
    ),
)
```

### Stdio (local subprocess)

```python
from agno.tools.mcp import MCPTools

linear_tools = MCPTools(
    command="npx -y @linear/mcp",
    env={"LINEAR_API_KEY": os.getenv("LINEAR_API_KEY", "")},
)
```

The stdio executable must be on `PATH` inside the runtime. The Docker image includes `uv`, `uvx`, `python`. Node-based servers (`npx …`) need Node installed:

```dockerfile
RUN apt-get update && apt-get install -y nodejs npm
```

### SSE

```python
notion_tools = MCPTools(
    url="https://mcp.notion.so/sse",
    transport="sse",
)
```

## Wiring into an agent

Pass the tools through `tools=` on the agent, alongside any other toolkits:

```python
from agno.agent import Agent

from app.settings import default_model
from db import get_postgres_db

my_agent = Agent(
    id="my-agent",
    name="My Agent",
    model=default_model(),
    db=get_postgres_db(),
    tools=[github_tools, linear_tools],
    instructions="…",
)
```

Then register the agent in `app/main.py` as usual. AgentOS detects `MCPTools` instances on registered agents and connects them on startup, closes them on shutdown.

## Exposing one tool instead of many

If an MCP server has many tools and you'd rather give your agent a single `query_<server>` tool that hands off to a sub-agent, use `MCPContextProvider`:

```python
from agno.context.mcp import MCPContextProvider

linear_context = MCPContextProvider(
    server_name="linear",
    transport="stdio",
    command="npx -y @linear/mcp",
    env={"LINEAR_API_KEY": os.getenv("LINEAR_API_KEY", "")},
    model=default_model(),
)

my_agent = Agent(
    ...,
    tools=linear_context.get_tools(),
    instructions=linear_context.instructions() + "\n\n" + my_instructions,
)
```

This is the same pattern the CodeSearch Agent uses with `WorkspaceContextProvider`. Use it when the server has many tools or names that collide with other servers; otherwise prefer raw `MCPTools` so the model sees each tool directly.

## Debugging

If an MCP server isn't responding, check the container logs at startup — agno logs the connection attempt and any failure:

```bash
docker logs agentos-api 2>&1 | grep -iE "mcp|tool"
```

Common failures:

- **stdio**: Is `command` on `PATH` inside the container?
- **HTTP**: Is the URL reachable from the container? Are headers correct?
- **Auth**: Is the bearer token set in `.env` (or `.env.production` for Railway)?
