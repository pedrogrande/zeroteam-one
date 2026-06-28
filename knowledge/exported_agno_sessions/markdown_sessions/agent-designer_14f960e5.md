# Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `14f960e5...` |
| **Type** | agent |
| **Agent** | Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-20T09:35:09 |
| **Runs** | 3 completed / 3 total |

## Run 1 — Agent Designer ✓ COMPLETED

*2026-04-20T09:35:09* · `glm-5.1:cloud` · `58c92610...`

### Prompt

I want an agent to be a product manager for a number of digital knowledge products. I have a Linear account and can set up the MCP server that allows the agent to manage the projects, issues etc.

The agent should help me manage a roadmap so that when I get new ideas for the products, the agent finds where it should go in the roadmap. This way I know we'll get to it later and I can stay focused on the priorities at hand.

### Response

Here's my proposed design for your Product Roadmap Manager agent:

## Agent: Roadmap PM

**Purpose**: Triage new product ideas into the right place on your Linear roadmap so you can stay focused on current priorities.

### Key Design Decisions

- **Model**: `Claude sonnet` — needs strong reasoning for triage/placement decisions
- **Tool**: Linear MCP server (read projects, create/update issues, manage cycles)
- **Session state**: Enabled — remembers context within a session so you can iterate on an idea before committing it

### Workflow (built into instructions)

When you give the agent a new idea, it will:

1. **Clarify** — Ask 1-2 focused questions if the idea is vague (which product? target user? problem being solved?)
2. **Scan the roadmap** — Pull current projects, cycles, and backlog from Linear to understand what's already there
3. **Triage** — Assess impact vs. effort, check for duplicates or related existing issues
4. **Place** — Create the issue in the right project/team, with:
   - Appropriate priority label (urgent, high, medium, low, no priority)
   - Labels for product area and type (feature, improvement, bug)
   - Description with user story format
5. **Confirm** — Tell you where it landed and why, so you can adjust if needed

### What You'll Need to Set Up

- **Linear MCP server** — the official `@anthropic/linear-mcp` or `linear-mcp-server` npm package
  - You'll need a Linear API key from Settings → API → Personal API keys
  - Ensure the key has read/write access to the relevant teams/projects
- **Product catalog** — I'll include a knowledge base listing your products so the agent knows which project to file ideas under

### What I Need From You

- **How many products** are we managing, and what are their names?
- **Do you use Linear teams or projects** to separate products? (This affects how the agent queries and creates issues)
- **Do you use cycles** for timeboxing, or a looser roadmap?
- **Any custom labels or workflows** in Linear I should account for?

Once I have those details, I'll write the full agent code with setup instructions.

---

## Run 2 — Agent Designer ✓ COMPLETED

*2026-04-20T09:51:59* · `glm-5.1:cloud` · `603e6a00...`

### Prompt

I don't want to hard code product names into the agent design. I don't know about timeboxing or looser roadmaps. The agent should advise on what is best.
I will use Ollama cloud model `glm-5.1:cloud` instead of Claude.
The agent should get to know my working style and learn from my behaviours and routines.

### Response

Here's the refined design:

## Agent: Roadmap PM (v2)

### What Changed

- **No hardcoded products** → Agent discovers your Linear workspace dynamically on first interaction and maps the landscape itself
- **Roadmap advisory** → After scanning your workspace, the agent recommends how to structure your roadmap (cycles vs. loose prioritization) based on what it finds — and remembers what you choose
- **Model** → `glm-5.1:cloud` via Ollama
- **Persistent learning** → Agent uses Agno's **user memories** to learn your style across sessions

### How Learning Works

With `create_user_memories=True`, the agent gets a built-in memory tool. It will **autonomously** record things like:

- "User prefers ideas filed as medium priority by default, only escalates after discussion"
- "User usually wants to batch-review before committing to a cycle"
- "User tends to file ideas with a brief description and fill in details later"
- "User prefers cycles over loose prioritization (decided 2025-01)"

This means the more you use it, the less it asks — it just *knows*.

### Workflow

1. **First interaction** → Agent scans Linear for teams, projects, labels, workflows. Presents a summary and recommends a roadmap structure. You confirm or adjust. This gets saved to memory.
2. **New idea** → Agent asks 1-2 clarifying questions if needed, scans for duplicates/related work, triages, files it in the right place, tells you where and why
3. **Ongoing** → Agent observes your corrections and preferences, saves them to memory, refines its behavior over time

### Setup Checklist

- [ ] Linear API key (Settings → API → Personal API keys, read+write)
- [ ] Linear MCP server installed (`npm install -g @anthropic/linear-mcp` or equivalent)
- [ ] Ollama running with `glm-5.1:cloud` available

### Code

```python
from agno.agent import Agent
from agno.memory import AgentMemory
from agno.models.ollama import Ollama
from agno.tools.mcp import MCPServerStdio

# --- Linear MCP Server ---
linear_mcp = MCPServerStdio(
    command="npx",
    args=["-y", "@anthropic/linear-mcp"],
    env={
        "LINEAR_API_KEY": "<your-linear-api-key>",
    },
)

# --- Agent ---
agent = Agent(
    name="Roadmap PM",
    model=Ollama(id="glm-5.1:cloud"),
    memory=AgentMemory(create_user_memories=True),
    tools=[linear_mcp],
    instructions=[
        "You are a product manager for a portfolio of digital knowledge products.",
        "",
        "## YOUR CORE JOB",
        "When the user brings a new idea, find the right place for it on the roadmap so they can stay focused on current priorities.",
        "",
        "## DISCOVERY PHASE (first interaction)",
        "- On first use, explore the Linear workspace: list all teams, projects, labels, and workflows.",
        "- Summarize what you find and recommend a roadmap structure (e.g. cycles for timeboxing vs. priority-based backlog).",
        "- Explain the tradeoffs briefly and let the user decide.",
        "- Save the user's choice and workspace map to your memories.",
        "",
        "## TRIAGE WORKFLOW (every new idea)",
        "1. If the idea is unclear, ask 1-2 focused questions. Do NOT over-interview.",
        "2. Search Linear for duplicates or related existing issues.",
        "3. Determine which team/project the idea belongs to (refer to your saved workspace map).",
        "4. Assess priority: impact vs. effort, strategic fit with current roadmap.",
        "5. Create the issue with: a user-story description, appropriate labels, and the right priority.",
        "6. Tell the user where you placed it and why. Offer to adjust.",
        "",
        "## LEARNING",
        "- Observe the user's corrections and preferences across conversations.",
        "- When the user adjusts a priority, label, or placement, remember why.",
        "- When the user has a pattern (e.g. always downgrades urgency, prefers brief descriptions), save it to your memories.",
        "- Use saved memories to inform future decisions without re-asking.",
        "- Do NOT ask questions you already know the answer to from your memories.",
        "",
        "## TONE",
        "- Concise and decisive. You are a PM, not a chatbot.",
        "- Make a recommendation first, then ask for confirmation. Don't present endless options.",
        "- If something is clearly a bad idea, say so respectfully and explain why.",
    ],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response("Let's get started — what does my Linear workspace look like?")
```

### Setup Instructions

1. **Get your Linear API key**: Go to Linear → Settings → API → Personal API keys → Create one with read/write access
2. **Install the MCP server dependency**: `npm install -g npx` (if you don't have it already — `npx` comes with Node.js)
3. **Replace `<your-linear-api-key>`** in the code with your actual key (or use an env var)
4. **Install Agno**: `pip install agno ollama`
5. **Ensure Ollama is running** and `glm-5.1:cloud` is available: `ollama list`
6. **Run**: `python roadmap_pm.py`

Want me to adjust anything before you set it up?

---

## Run 3 — Agent Designer ✓ COMPLETED

*2026-04-20T10:11:04* · `glm-5.1:cloud` · `c43a8017...`

### Prompt

Do you have access to the agno-docs tools?

### Response

No, I don't — I only have `think` and `analyze` as tools. I don't have access to any agno-docs tool to look up the actual API.

That means I'm relying on my training knowledge for the Agno API, which could be outdated or inaccurate. A few things I'd want to verify against the docs:

- **`create_user_memories`** — is this the correct parameter name and does it work the way I described?
- **`MCPServerStdio`** — is this the right class and import path?
- **`AgentMemory`** — is this the right class for memory configuration?
- **Model kwargs** — does the Ollama integration support `glm-5.1:cloud`?

Do you have access to agno-docs that you could point me at, or would you like me to flag the uncertain parts so you can double-check them?

---
