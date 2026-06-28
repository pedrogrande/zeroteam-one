# Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `15df5abf...` |
| **Type** | agent |
| **Agent** | Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-20T10:36:54 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agent Designer ✓ COMPLETED

*2026-04-20T10:36:54* · `glm-5.1:cloud` · `41750d74...`

### Prompt

Help me design an agent that helps me design Agno agents

### Response

Here's my proposed design for an **Agno Agent Design Agent** — a meta-agent that guides users through designing well-structured Agno agents:

---

## 🎯 Purpose

Help users design Agno agents by asking the right questions, recommending patterns, and generating implementation-ready Python code.

---

## 🧠 Agent Architecture

### Model
- **Primary**: `Claude` (claude-sonnet-4-20250514) — strong reasoning for design decisions
- **Fallback**: `GPT4o` — good alternative if Claude unavailable

### Core Capabilities
- **Discovery** — ask structured questions about the use case
- **Pattern Recommendation** — match use case to known Agno patterns
- **Code Generation** — produce complete, runnable Python code
- **Setup Guidance** — list API keys, dependencies, infrastructure needed

### Knowledge Sources
- **URL Knowledge Base** — load Agno docs directly (https://docs.agno.com)
- **System Prompt** — embed key patterns, agent class taxonomy, and common configurations
- **Memory** — track past designs, user preferences, and iterative refinements

---

## 🔧 Tools Needed

| Tool | Purpose | Why |
|------|---------|-----|
| `DuckDuckGoTools` | Search latest Agno docs/examples | Framework evolves fast |
| `FileTools` | Write generated code to files | Deliver working code |
| `PythonTools` | Validate generated code syntax | Catch errors before delivery |

---

## 🧩 Key Design Decisions

- **`markdown=True`** — clean, structured output
- **`structured_outputs=True`** — Pydantic models for typed agent specifications
- **`read_chat_history=True`** — maintain context across iterative design
- **Memory** — `AgentMemory()` with `UserMemory()` to track preferences

---

## 📋 Design Process (5 Phases)

1. **Discover** — What's the use case? Who's the user? What decisions does the agent support?
2. **Scope** — Single agent vs team vs workflow? What tools? What knowledge?
3. **Specify** — Model selection, system prompt, tools, guardrails, output format
4. **Generate** — Complete Python code with imports, config, and run instructions
5. **Validate** — Check for missing API keys, dependency conflicts, common pitfalls

---

## ⚠️ External Setup Required

- `ANTHROPIC_API_KEY` (if using Claude)
- `OPENAI_API_KEY` (if using GPT-4o)
- `pip install agno duckduckgo-search`
- Optional: `ollama` if using local models
- Optional: `chromadb` if using vector knowledge bases

---

## 🤔 Open Questions for You

- **Scope**: Should it design *single agents only*, or also **Teams** and **Workflows**?
- **Depth**: Should it go as deep as CAWDP-style complementarity analysis, or keep it practical/Agno-focused?
- **Knowledge**: Should I use Agno's URL knowledge base to load live docs, or embed patterns in the system prompt?
- **Model**: Your primary LLM is Ollama Cloud (glm-5.1:cloud) — should I use that, or Claude/GPT-4o for this agent specifically?

Want me to write the Python code once you've confirmed these choices?

---

## Run 2 — Agent Designer ✓ COMPLETED

*2026-04-20T10:48:06* · `glm-5.1:cloud` · `cb415abc...`

### Prompt

this agent should be created with Ollama provider and glm-5.1:cloud model

The agent should always design agents with Ollama models.

The agent should always check the agno-docs tools and not just guess at packages, methods and class names.

The agent should aim for efficient use of tools, skills, knowledge, memories, context and learnings.

### Response

Here's the complete design with Python code:

---

## 🏗️ Agno Agent Design Agent

### Architecture at a Glance

| Component | Choice | Why |
|-----------|--------|-----|
| **Model** | `Ollama(id="glm-5.1:cloud")` | Your specified LLM |
| **Knowledge** | `WebsiteKnowledge` (Agno docs) | Primary doc reference — never guess |
| **Tools** | `DuckDuckGoTools` + `WebsiteTools` + `FileTools` + `PythonTools` | Search → fetch → write → validate |
| **Memory** | `AgentMemory()` + `UserMemory()` | Track designs + user preferences |
| **Storage** | `SqliteStorage` | Session persistence, zero infra |

### Why These Choices

- **WebsiteKnowledge** loads actual Agno docs so the agent has ground-truth API reference
- **DuckDuckGoTools** fills gaps when knowledge base misses something
- **WebsiteTools** fetches specific doc pages for precise class names / method signatures
- **FileTools** writes generated code to files
- **PythonTools** validates generated code syntax before delivery
- **3-tool read path** (knowledge → search → fetch) ensures it never guesses

---

## 🐍 Python Code

```python
"""
Agno Agent Design Agent
========================
A meta-agent that helps users design well-structured Agno agents.
Always verifies API details from Agno docs. Always uses Ollama models.

Setup:
  1. pip install agno duckduckgo-search ollama
  2. export OLLAMA_API_KEY=your_key
  3. agno serve agent_designer.py:agent
     OR
     python agent_designer.py
"""

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.knowledge.website import WebsiteKnowledge
from agno.memory.agent import AgentMemory
from agno.memory.user import UserMemory
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.website import WebsiteTools
from agno.tools.file import FileTools
from agno.tools.python import PythonTools

# ─── Knowledge: Pre-load Agno docs ─────────────────────────────
agno_docs = WebsiteKnowledge(
    urls=[
        "https://docs.agno.com/agents/overview",
        "https://docs.agno.com/models/ollama",
        "https://docs.agno.com/tools/overview",
        "https://docs.agno.com/tools/standard-tools",
        "https://docs.agno.com/tools/function-tools",
        "https://docs.agno.com/tools/custom-tools",
        "https://docs.agno.com/tools/web-search",
        "https://docs.agno.com/tools/website-tools",
        "https://docs.agno.com/tools/python-tools",
        "https://docs.agno.com/tools/file-tools",
        "https://docs.agno.com/tools/shell-tools",
        "https://docs.agno.com/tools/youtube-tools",
        "https://docs.agno.com/tools/newspaper-tools",
        "https://docs.agno.com/tools/json-tools",
        "https://docs.agno.com/tools/csv-tools",
        "https://docs.agno.com/tools/calculator",
        "https://docs.agno.com/knowledge/overview",
        "https://docs.agno.com/knowledge/website",
        "https://docs.agno.com/knowledge/url",
        "https://docs.agno.com/knowledge/pdf",
        "https://docs.agno.com/knowledge/text",
        "https://docs.agno.com/knowledge/agent-knowledge",
        "https://docs.agno.com/memory/overview",
        "https://docs.agno.com/memory/agent-memory",
        "https://docs.agno.com/memory/user-memory",
        "https://docs.agno.com/storage",
        "https://docs.agno.com/database/postgres",
        "https://docs.agno.com/database/overview",
        "https://docs.agno.com/agents/sessions",
        "https://docs.agno.com/agents/reasoning",
        "https://docs.agno.com/input-output/overview",
        "https://docs.agno.com/context/overview",
        "https://docs.agno.com/context/agent-context",
        "https://docs.agno.com/agents/streaming",
        "https://docs.agno.com/teams/overview",
        "https://docs.agno.com/workflows/overview",
        "https://docs.agno.com/models/overview",
        "https://docs.agno.com/models/reasoning",
    ],
    max_links=2,  # Don't follow deep — keep knowledge focused
)

# ─── System Prompt ─────────────────────────────────────────────
SYSTEM_PROMPT = """You are an Agno Agent Design Agent — an expert at designing well-structured 
Agno agents. You help users go from a use case idea to a complete, runnable Agno agent.

## CORE PRINCIPLES

1. **NEVER GUESS THE API.** Always verify class names, method signatures, import paths, 
   and constructor parameters by checking your knowledge base or searching the Agno docs. 
   If you're unsure about a class name, tool name, or parameter — LOOK IT UP before writing code.

2. **ALWAYS USE OLLAMA MODELS.** Every agent you design must use an Ollama model. 
   Default to `Ollama(id="glm-5.1:cloud")` unless the user specifies a different Ollama model.

3. **BE EFFICIENT.** Use your knowledge base first, search only when needed, fetch specific 
   pages only for precise API details. Don't make redundant tool calls.

4. **BE PRACTICAL.** Generate complete, runnable code — not fragments. Include all imports, 
   configuration, and clear setup instructions.

## DESIGN PROCESS

Follow this 5-phase process for every agent design:

### Phase 1: DISCOVER
Ask the user:
- What is the agent's purpose? What problem does it solve?
- Who is the end user? Technical or non-technical?
- What kind of work does the agent do? (extraction, measurement, assessment, generation, aggregation)
- What decisions does the agent support? What decisions should remain human-only?

### Phase 2: SCOPE
Determine:
- Single agent vs Team vs Workflow?
- What tools does it need? (Check Agno docs for available tools!)
- What knowledge does it need? (Check Agno docs for knowledge base types!)
- Does it need memory? User memory? Agent memory? Both?
- Does it need persistent storage?

### Phase 3: SPECIFY
Define:
- Model: Ollama model selection (default: glm-5.1:cloud)
- System prompt: Clear, specific instructions
- Tools: Verified import paths from Agno docs
- Knowledge: Appropriate knowledge base type
- Memory: AgentMemory, UserMemory, or both
- Storage: If persistence needed
- Output format: Markdown, structured output, or plain text

### Phase 4: GENERATE
Produce:
- Complete Python file with all imports
- Clear setup instructions (pip install, env vars, etc.)
- Inline comments explaining key design choices
- Run command (agno serve or python)

### Phase 5: VALIDATE
Check:
- Are all import paths correct? (Verify against Agno docs)
- Are all constructor params correct? (Verify against Agno docs)
- Are required env vars documented?
- Are pip dependencies listed?
- Does the agent follow good design principles?

## AGENT CLASSIFICATION

When designing, classify the agent by its primary cognitive operation:
- **Extractor**: Gathers/collects information. Never judges.
- **Measurer**: Quantifies/measures against criteria. Never interprets.
- **Assessor**: Evaluates against standards. Never finalizes (human decides).
- **Generator**: Produces content/drafts. Must be verified.
- **Aggregator**: Combines/synthesizes. Must not add beyond inputs.

This classification determines appropriate tools, guardrails, and system prompt framing.

## EFFICIENCY RULES

- Check knowledge base FIRST for API details
- Use DuckDuckGo search when knowledge base is insufficient
- Use WebsiteTools to fetch specific doc pages for precise details
- Don't repeat tool calls for info you already have
- Don't over-tool the agent — add only tools the use case requires
- Don't over-prompt — keep system prompts focused and specific
- Prefer composition (tools + knowledge) over complexity (many tools)
"""

# ─── Agent ────────────────────────────────────────────────────
agent = Agent(
    name="Agno Agent Designer",
    model=Ollama(id="glm-5.1:cloud"),
    description="Designs well-structured Agno agents. Always verifies API from docs. Always uses Ollama models.",
    instructions=SYSTEM_PROMPT,
    knowledge=agno_docs,
    search_knowledge=True,
    tools=[
        DuckDuckGoTools(),
        WebsiteTools(),
        FileTools(),
        PythonTools(),
    ],
    memory=AgentMemory(),
    user_memory=UserMemory(),
    storage=SqliteStorage(table_name="agent_designer_sessions", db_file="agent_designer.db"),
    markdown=True,
    show_tool_calls=True,
    read_chat_history=True,
)

# ─── Run ───────────────────────────────────────────────────────
if __name__ == "__main__":
    agent.print_response(
        "I want to design an Agno agent. Help me get started!",
        stream=True,
    )
```

---

## 📋 Setup Instructions

```bash
# 1. Install dependencies
pip install agno duckduckgo-search ollama

# 2. Set your Ollama Cloud API key
export OLLAMA_API_KEY=your_ollama_api_key_here

# 3. Run the agent
# Option A: CLI interaction
python agent_designer.py

# Option B: Serve via Agno playground (web UI)
agno serve agent_designer.py:agent
```

---

## 🔑 Key Design Decisions

- **3-layer doc verification**: Knowledge base → DuckDuckGo search → WebsiteTools fetch — the agent never writes an import or class name it can't verify
- **WebsiteKnowledge with `max_links=2`**: Loads focused doc pages without crawling the entire site (efficiency)
- **`search_knowledge=True`**: Agent automatically searches its knowledge base before responding
- **SqliteStorage**: Zero-infrastructure session persistence — upgrade to PostgresStorage when you deploy
- **Agent classification in system prompt**: Guides the agent to think about what *kind* of agent it's designing, not just what tools to bolt on
- **No over-tooling**: 4 tools only — each serves a distinct purpose (search, fetch, write, validate)

---

## ⚠️ External Setup Required

| Requirement | How |
|------------|-----|
| Ollama Cloud API key | `export OLLAMA_API_KEY=...` |
| Python 3.9+ | Standard |
| pip packages | `agno duckduckgo-search ollama` |
| Internet access | Required for doc fetching and Ollama Cloud |

---

Want me to adjust anything — different tools, different knowledge scope, or a Team/Workflow version for more complex agent designs?

---
