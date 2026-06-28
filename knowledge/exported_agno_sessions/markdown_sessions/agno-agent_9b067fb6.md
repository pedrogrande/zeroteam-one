# Agno Agent

| Field | Value |
|-------|-------|
| **Session** | `9b067fb6...` |
| **Type** | agent |
| **Agent** | Agno Agent |
| **User** | pete@peterargent.com |
| **Created** | 2026-06-12T22:30:07 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agno Agent ✓ COMPLETED

*2026-06-12T22:30:07* · `glm-5.1:cloud` · `1dfe4e68...`

### Prompt

Which tools do you have access to?

### Response

I have access to one tool:

| Tool | Purpose |
|------|---------|
| **search_knowledge_base** | Searches the knowledge base for information about a query. Useful for finding specific details about Agno, CAWDP, PRISM, agent design, or any other topic in our shared knowledge base. |

That's it — just the knowledge base search. No code execution, file access, web browsing, or other external tools.

---

## Run 2 — Agno Agent ✓ COMPLETED

*2026-06-12T22:30:53* · `glm-5.1:cloud` · `724ffbb9...`

### Prompt

Do you have acccess to the Agno knowledge base?

### Response

Let me check what's available in the knowledge base.Yes, I have access to the Agno knowledge base. The search returned documentation covering:

- **Introduction & Core Concepts** — Agents, Teams, Workflows as core primitives
- **AgentOS** — Production runtime with FastAPI backend, control plane UI
- **Context Engineering** — Sessions, chat history, state management
- **Knowledge / RAG** — Agentic retrieval with 20+ vector stores, contents_db
- **Memory** — User memory across sessions, Culture (collective memory)
- **Human-in-the-Loop** — Native HITL support for confirmations and overrides
- **Guardrails** — Validation, security, prompt protection
- **Hooks** — Pre/post-execution hooks including background execution
- **MCP Integration** — Model Context Protocol support
- **Toolkits** — 120+ pre-built toolkits
- **OpenTelemetry** — Observability with auto-instrumentation
- **Models** — Model-agnostic architecture, type-safe I/O
- **Examples** — Pal, Dash, Scout, Gcode, Investment Team
- **Contributing & Development** — Setup, formatting, validation

What would you like to look up?

---
