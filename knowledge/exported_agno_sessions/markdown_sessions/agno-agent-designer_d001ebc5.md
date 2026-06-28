# Agno Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `d001ebc5...` |
| **Type** | agent |
| **Agent** | Agno Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-30T05:48:52 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agno Agent Designer ✓ COMPLETED

*2026-04-30T05:48:52* · `glm-5.1:cloud` · `3e3c81b6...`

### Prompt

Give me a list of all the types of tools that can be given to agents

### Response

Here's a complete breakdown of all the types of tools you can give to Agno agents:

---

## 1. Custom Python Functions

**Any Python function can be a tool.** This is the simplest and most flexible option — write a function with a docstring and type hints, and Agno automatically converts it into a tool definition (JSON schema) for the model.

```python
from agno.tools import tool

def get_weather(city: str) -> str:
    """Get the weather for a given city.

    Args:
        city (str): The city to get the weather for.
    """
    return f"The weather in {city} is sunny."

agent = Agent(tools=[get_weather], ...)
```

You can also use the `@tool` decorator to modify what happens before/after a tool call.

---

## 2. Pre-Built Toolkits (120+)

Agno provides **120+ pre-built toolkits** organised into 8 categories:

### 🔍 Search (15 tools)
| Tool | Purpose |
|------|---------|
| DuckDuckGo | Web search |
| Google/Bing/SerperAPI/SerpAPI | Web search |
| Exa / Tavily / Perplexity | AI-powered web search |
| HackerNews | Tech news |
| Wikipedia | Encyclopedia search |
| Arxiv | Academic papers |
| PubMed | Medical/biomedical literature |
| BaiduSearch | Chinese web search |
| SearxNG | Self-hosted meta-search |
| Linkup / Valyu | Web + academic content |
| Parallel | Multi-search aggregation |

### 💬 Social (11 tools)
Discord, Email, Gmail, Slack, Telegram, Twilio, WhatsApp, Webex, X (Twitter), Reddit, Zoom

### 🌐 Web Scraping (11 tools)
AgentQL, BrowserBase, Crawl4AI, Firecrawl, Jina Reader, Newspaper/Newspaper4k, Spider, Trafilatura, BrightData, Oxylabs, Website

### 🗄️ Database (9 tools)
Postgres, DuckDB, SQL, CSV, Pandas, Google BigQuery, Neo4j, Redshift, Zep (+ MCP Toolbox for databases)

### 💻 Local (7 tools)
Calculator, Docker, File, Local File System, Python, Shell, Sleep

### 🎨 Model-Native (5 tools)
Azure OpenAI (DALL-E image gen), Groq, Morph (code modification), Nebius (image gen), Gemini (image gen)

### 📄 File Generation
File generation toolkit for creating documents

### 🧩 Additional (70+ specialized tools)
Airflow, Apify, AWS Lambda, AWS SES, Bitbucket, Brandfetch, CalCom, Cartesia, ClickUp, Composio, Confluence, Custom API, DALL-E, Daytona, Desi Vocal, Docling, E2B, ElevenLabs, EVM (Ethereum), Fal, Financial Datasets, Giphy, GitHub, GitLab, Google Maps/Sheets/Slides/Calendar, Jira, Linear, Lumalabs, MLX Transcribe, ModelsLabs, MoviePy, Nano Banana, Notion, OpenBB, OpenCV, OpenWeather, Replicate, Resend, Salesforce, Scheduler, Shopify, Spotify, Todoist, Trello, User Control Flow, Visualization, Web Browser, WebTools, YFinance, YouTube, Zendesk, Knowledge, Mem0, Reasoning

---

## 3. Reasoning Tools

A special toolkit that gives the agent structured reasoning as a tool call — not just generating text, but explicitly using `think` and `analyze` steps:

```python
from agno.tools.reasoning import ReasoningTools

agent = Agent(
    tools=[ReasoningTools(add_instructions=True)],
)
```

- **`think`** — scratchpad for step-by-step reasoning
- **`analyze`** — evaluate results and determine next actions

This enables the agent to reflect after each step, question assumptions, and adjust its approach mid-execution.

---

## 4. Knowledge Tools

For searching and analysing knowledge bases with a **Think → Search → Analyze** cycle:

```python
from agno.tools.knowledge import KnowledgeTools

knowledge_tools = KnowledgeTools(
    knowledge=my_knowledge_base,
    think=True,    # Plan search queries
    search=True,   # Execute queries
    analyze=True,  # Evaluate sufficiency
)
```

---

## 5. Memory Tools

For persistent user memory management (create, update, delete) with a **Think → Operate → Analyze** cycle:

```python
from agno.tools.memory import MemoryTools

memory_tools = MemoryTools(db=my_database)
```

Tools: `think`, `get_memories`, `add_memory`, `update_memory`, `delete_memory`, `analyze`

---

## 6. Workflow Tools

For agents that need to execute, monitor, and reason about multi-step workflows:

```python
from agno.tools.workflow import WorkflowTools

workflow_tools = WorkflowTools(workflow=my_workflow)
```

Tools: `think`, `run_workflow`, `analyze` — with a **Think → Run → Analyze** cycle.

---

## 7. MCP (Model Context Protocol) Tools

Connect agents to **any MCP-compatible server** for external system access:

```python
from agno.tools.mcp import MCPTools

mcp_tools = MCPTools(
    transport="streamable-http",
    url="https://docs.agno.com/mcp"
)
await mcp_tools.connect()

agent = Agent(tools=[mcp_tools])
```

This lets you connect to filesystems, databases, APIs, and any other service that exposes an MCP interface.

---

## Summary

| Type | Count | Key Use |
|------|-------|---------|
| **Custom Python Functions** | ∞ | Any logic you need |
| **Pre-built Toolkits** | 120+ | External services, data, computation |
| **Reasoning Tools** | 2 | Structured thinking & analysis |
| **Knowledge Tools** | 3 | Search & analyse knowledge bases |
| **Memory Tools** | 6 | Persistent user memory CRUD |
| **Workflow Tools** | 3 | Execute & reason about workflows |
| **MCP Tools** | ∞ | Connect to any MCP server |

The key principle: **any Python function can be a tool**, and Agno automatically converts it. Pre-built toolkits handle the common cases, custom functions handle everything else, and MCP lets you connect to the entire ecosystem of MCP-compatible services.

---
