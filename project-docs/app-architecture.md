# Agno AgentOS — Architecture Review

## 📐 Project Overview

This is an **Agno Agent Platform** — a production-grade multi-agent operating system organized as a **monorepo** with two distinct layers:

| Layer | Path | Role |
|-------|------|------|
| **Framework Library** | `agno/source/agno/` | Reusable `agno` Python package (v2.6.9) — 30+ subpackages |
| **Deployment Application** | `app/`, `agents/`, `teams/`, `db/` | Thin wiring layer that instantiates 3 agents + 1 team against PostgreSQL + pgvector |

The app runs as a **FastAPI server** via `AgentOS`, which orchestrates the full lifecycle of agents, teams, workflows, knowledge bases, MCP tools, and external interfaces (Slack, Telegram, WhatsApp, A2A).

---

## 🏗️ Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│                    Docker / Railway                    │
│  ┌────────────────────┐   ┌────────────────────────┐ │
│  │   zeroedge-api      │   │   zeroedge-db           │ │
│  │   (uvicorn:8000)    │──▶│   (pgvector:18)         │ │
│  │                     │   │   Postgres + vectors     │ │
│  │   AgentOS (FastAPI) │   └────────────────────────┘ │
│  │   ┌───────────────┐ │                              │
│  │   │ Agents        │ │                              │
│  │   │  • WebSearch  │ │──▶ MCP / Parallel (web)     │
│  │   │  • CodeSearch │ │──▶ WorkspaceContext (local)  │
│  │   │  • AgnoSupport│ │──▶ MCP docs (agno docs)     │
│  │   ├───────────────┤ │                              │
│  │   │ Teams         │ │                              │
│  │   │  • EngLeadership│ │─▶ LearningMachine + KB     │
│  │   ├───────────────┤ │                              │
│  │   │ 90+ API routes│ │                              │
│  │   │ Scheduler     │ │                              │
│  │   │ JWT Auth      │ │                              │
│  │   │ Tracing (OTel)│ │                              │
│  │   │ MCP Lifecycle │ │                              │
│  │   └───────────────┘ │                              │
│  └────────────────────┘                              │
└──────────────────────────────────────────────────────┘
```

---

## ✅ Architectural Strengths

### 1. Fresh Model Instances per Agent Call

`settings.py` creates a fresh `Ollama(id="glm-5.1:cloud")` per call rather than caching module-level singletons. In an async FastAPI context, shared mutable LLM state is a common source of session cross-contamination and race conditions. This pattern trades allocation overhead for correctness — the right tradeoff at this layer.

### 2. MCP Lifecycle Bound to App Lifespan

MCP tool `connect`/`disconnect` is tied to FastAPI lifespan events rather than per-request or lazy initialization. Since MCP connections are stateful (tool registries, transport sessions), this avoids cold-start latency and ensures tools are available before the app accepts traffic.

### 3. Defensive Tool Strategy (ParallelTools vs MCP)

The WebSearch agent conditionally uses `ParallelTools` (when `PARALLEL_API_KEY` is set) or falls back to a keyless MCP endpoint. Rather than hard-failing on a missing API key, the agent degrades to an alternative strategy — a pragmatic resilience pattern.

### 4. Framework / Application Separation

The `agno/` library vs `app/agents/teams/db/` split enforces a clean boundary between general-purpose framework code and deployment-specific configuration. This makes the framework independently publishable and allows multiple deployment apps against the same core.

### 5. Rich Learning Subsystem

The Engineering Leadership team configures user profiles, entity memory, session context, decision logs, and learned knowledge. Treating agent teams as *evolving systems* rather than stateless request processors is architecturally ambitious and well-scoped.

### 6. Multi-Backend Flexibility

Supporting 13 database backends and 15+ vector DB backends prevents early infrastructure lock-in and makes the platform viable across deployment environments (air-gapped, cloud-managed, hybrid).

---

## ⚠️ Concerns & Risks

### 🔴 Critical: AgentOS as a 1630-Line God Module

`agno/os/app.py` orchestrates **15+ concerns** in a single file — agents, teams, workflows, knowledge, interfaces, scheduler, DB lifecycle, MCP tools, JWT auth, CORS, tracing, session/memory/metrics/evals/traces/schedules/approvals/components/registry routers, and ~90+ API endpoints.

**Risk**: Merge conflicts, review bottlenecks, and cognitive overload for contributors. A scheduler bug fix shouldn't require touching the same file as knowledge base management. As the endpoint count grows, refactoring becomes exponentially more expensive.

### 🔴 Critical: Default Database Credentials in Source Code

`db/session.py` defaults to `ai/ai/ai` for PostgreSQL credentials:

```python
DB_USER = os.getenv("DB_USER", "ai")  # ← known default
DB_PASS = os.getenv("DB_PASS", "ai")  # ← known default
```

This means **running the app without env vars = running with known credentials**, which routinely escapes into production environments.

### 🟠 High: Cloud-Dependent Default Model

`Ollama(id="glm-5.1:cloud")` means the app **will not start** in an air-gapped/offline environment. Using a cloud endpoint under the `Ollama` namespace is also semantically confusing — Ollama's value proposition is *local* model serving.

### 🟠 High: Dev/Prod Configuration Conflation

`compose.yaml` uses hot-reload (`--reload-dir`) and mounts the project directory — great for dev, but a production hazard if the same file is deployed. There's no separation between dev and prod compose configurations.

### 🟠 High: No Circuit Breakers for External Calls

The platform heavily relies on external services (LLM providers, MCP tools, web search APIs). Without circuit breakers, a degraded provider causes cascading failures across all agent executions.

### 🟡 Medium: Single-Process Orchestrator Under Load

A single FastAPI process handles HTTP routing, agent execution, team coordination, scheduler, MCP mediation, and DB operations. Agent execution is I/O-heavy with variable latency — slow agents can cause head-of-line blocking.

### 🟡 Medium: 30+ Subpackages Without Dependency Graph Validation

The `agno/` library's breadth creates a significant maintenance surface. Without CI-level dependency graph checks, circular imports and framework↔app coupling can creep in silently.

### 🟢 Low: Duplicate Dependency Entry

`"mcp"` is listed twice in `pyproject.toml` — likely a bug, but also a symptom that dependency declarations aren't being validated by CI.

---

## 🎯 Recommendations (Prioritized)

| # | Recommendation | Priority | Effort |
|---|---------------|----------|--------|
| **R1** | **Decompose AgentOS** into `app.py` (factory, <200 lines) + `services/` layer + thin route adapters. Extract one service at a time, starting with the most independent (scheduler, knowledge). | P0 | M-L |
| **R2** | **Eliminate default credentials** — fail fast with a clear error if `DB_USER`/`DB_PASS` are unset. Use `.env.dev` (gitignored) for local development. | P0 | S |
| **R3** | **Separate compose configs** — `compose.yaml` (base), `compose.dev.yaml` (hot-reload, mounts), `compose.prod.yaml` (resource limits, health checks). | P1 | S |
| **R4** | **Add circuit breakers** around all external service calls (LLM providers, MCP tools, search APIs). | P1 | M |
| **R5** | **Default to a local model** (`Ollama(id="llama3.2")`). Make cloud models opt-in via env vars. | P1 | S |
| **R6** | **Add request-level isolation** — asyncio task groups with timeouts for agent execution; consider background workers for team coordination. | P2 | M |
| **R7** | **Validate dependency graph in CI** — check for circular imports between `agno/` subpackages and ensure the framework never imports from `app/`. | P2 | S |
| **R8** | **Validate dependency declarations in CI** — catch duplicates, unpin versions, and audit with `pip-audit`. | P3 | S |

---

## 📊 Risk Summary Matrix

| Area | Current State | Risk | Priority |
|------|--------------|------|----------|
| AgentOS monolith | 1630 lines, 90+ endpoints | 🔴 Critical | P0 |
| Default DB credentials | `ai/ai/ai` in source | 🔴 Critical | P0 |
| Hot-reload in compose | Dev/prod config mixed | 🟠 High | P1 |
| Cloud-dependent default model | Won't work offline | 🟠 High | P1 |
| No circuit breakers | Cascading failure risk | 🟠 High | P1 |
| Single-process orchestration | Head-of-line blocking | 🟡 Medium | P2 |
| Framework coupling risk | 30+ subpackages, no graph check | 🟡 Medium | P2 |
| Duplicate dependency | Symptom of no CI validation | 🟢 Low | P3 |

The architecture shows strong **conceptual design** — the framework/app separation, the defensive tool selection, the learning subsystem, and the MCP lifecycle management are all well-reasoned. The primary risks are in **structural implementation**: the god module, credential handling, and dev/prod conflation. These are all fixable incrementally without rearchitecting, but the cost of fixing them grows with the 90+ endpoint surface area — so sooner is better.
