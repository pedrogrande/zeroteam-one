# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `4d8fde90...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-28T23:05:47 |
| **Runs** | 3 completed / 3 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-28T23:05:47* · `glm-5.1:cloud` · `b2bb9a99...`

### Prompt

What can we learn from reviewing this Agno produced agent system and the agent design:

# Dash

A **self-learning data agent** built with systems engineering principles. It grounds answers in 6 layers of context and improves with every query.

Chat with Dash via Slack, the terminal, or the [AgentOS](https://os.agno.com?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=agentos) web UI.

## Quick Start

```sh
# Clone the repo
git clone https://github.com/agno-agi/dash.git && cd dash

cp example.env .env
# Edit .env and add your OPENAI_API_KEY

# Start the system
docker compose up -d --build

# Generate sample data and load knowledge
docker exec -it dash-api python scripts/generate_data.py
docker exec -it dash-api python scripts/load_knowledge.py
```

Confirm Dash is running at [http://localhost:8000/docs](http://localhost:8000/docs).

### Connect to the Web UI

1. Open [os.agno.com](https://os.agno.com?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=agentos) and login
2. Add OS → Local → `http://localhost:8000`
3. Click "Connect"

**Try it** (SaaS metrics dataset):

- What's our current MRR?
- Which plan has the highest churn rate?
- Show me revenue trends by plan over the last 6 months
- Which customers are at risk of churning?

## Deploy to Railway

Railway deployment uses `.env.production` to keep production credentials separate from local dev.

```sh
cp example.env .env.production
# Edit .env.production — set OPENAI_API_KEY
```

### Step 1: Deploy infrastructure

This creates the Railway project, database, and app service. The app will crash-loop until the JWT key is added in the next step — that's expected.

```sh
railway login
./scripts/railway_up.sh
```

### Step 2: Get your JWT key

Production requires a `JWT_VERIFICATION_KEY` from [AgentOS](https://os.agno.com?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=agentos). You need the Railway domain from step 1 to set this up.

1. Copy your Railway domain from the output of step 1 (e.g. `dash-production-xxxx.up.railway.app`)
2. Open [os.agno.com](https://os.agno.com?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=agentos) and login
3. Add OS → Live → paste your Railway URL
4. Go to **Settings** and generate a key pair
5. Add the public key to `.env.production` (wrap in single quotes):

```bash
JWT_VERIFICATION_KEY='-----BEGIN PUBLIC KEY-----
MIIBIjANBgkq...
-----END PUBLIC KEY-----'
```

### Step 3: Push environment and redeploy

```sh
./scripts/railway_env.sh
./scripts/railway_redeploy.sh
```

`railway_env.sh` reads `.env.production` and sets each variable on the Railway service. Safe to run repeatedly. Handles multiline values (PEM keys) correctly.

### Production operations

Database scripts must run inside Railway's network (the internal hostname `pgvector.railway.internal` isn't reachable from your local machine). Use SSH to connect to the running container:

```sh
railway ssh --service dash
# Inside the container:
python scripts/generate_data.py
python scripts/load_knowledge.py
```

Other operations run locally:

```sh
railway logs --service dash
railway open
```

## Why Dash Exists

Ask a question in English, get a correct, meaningful answer. That's the goal. But raw LLMs writing SQL hit a wall fast: schemas lack meaning, types are misleading, tribal knowledge is missing, there's no way to learn from mistakes, and results lack interpretation.

The root cause is missing context and missing memory. Dash solves this with **six layers of grounded context**, a **self-learning loop** that improves with every query, and a focus on delivering insights you can act on.

## Architecture: Five Layers, One System

Agentic software is just software with the business logic replaced by agents. Everything else is systems engineering. Dash is built across five layers that reinforce each other.

```
Agent Engineering     →  dash/team.py + dash/agents/
Data Engineering      →  knowledge/ + Agno Learning Machine + PostgreSQL
Security Engineering  →  AgentOS auth + RBAC + read-only SQL enforcement
Interface Engineering →  app/main.py (FastAPI) + Slack + AgentOS
Infrastructure        →  Dockerfile + compose.yaml + scripts/
```

### 1. Agent Engineering

The agent team and execution flow. Model, instructions, tools, knowledge, and the self-learning loop.

```
AgentOS (app/main.py)  [scheduler=True, tracing=True]
 ├── FastAPI / Uvicorn
 ├── Slack Interface (optional)
 └── Dash Team (dash/team.py, coordinate mode)
     ├─ Analyst (dash/agents/analyst.py)         reads public + dash
     │  ├─ SQLTools (read-only)  → public schema (company data)
     │  ├─ introspect_schema     → both schemas
     │  ├─ save_validated_query  → knowledge base
     │  └─ ReasoningTools
     ├─ Engineer (dash/agents/engineer.py)       reads public, writes dash
     │  ├─ SQLTools (full)       → dash schema (agent-managed)
     │  ├─ introspect_schema     → both schemas
     │  ├─ update_knowledge      → knowledge base (schema changes)
     │  └─ ReasoningTools
     │
     Leader tools: SlackTools (optional)
     Knowledge:    dash_knowledge (table schemas, queries, business rules, dash views)
     Learnings:    dash_learnings (error patterns, type gotchas, fixes)
```

### 2. Data Engineering

Context is data. Memory is data. Knowledge is data. All managed with data engineering principles: well-designed schemas, structured querying, databases for fast read/writes.

**Six layers of grounded context:**

| Layer | Purpose | Source |
|------|--------|--------|
| **Table Usage** | Schema, columns, relationships | `knowledge/tables/*.json` |
| **Human Annotations** | Metrics, definitions, business rules | `knowledge/business/*.json` |
| **Query Patterns** | SQL that is known to work | `knowledge/queries/*.sql` |
| **Institutional Knowledge** | Docs, wikis, external references | MCP (optional) |
| **Learnings** | Error patterns and discovered fixes | Agno `Learning Machine` |
| **Runtime Context** | Live schema changes | `introspect_schema` tool |

**The self-learning loop:**

```
User Question
     ↓
Retrieve Knowledge + Learnings
     ↓
Reason about intent
     ↓
Generate grounded SQL
     ↓
Execute and interpret
     ↓
 ┌────┴────┐
 ↓         ↓
Success    Error
 ↓         ↓
 ↓         Diagnose → Fix → Save Learning
 ↓                           (never repeated)
 ↓
Return insight
 ↓
Optionally save as Knowledge
```

Two complementary systems:

| System | Stores | How It Evolves |
|------|--------|----------------|
| **Knowledge** | Validated queries and business context | Curated by you + Dash |
| **Learnings** | Error patterns and fixes | Managed by `Learning Machine` automatically |

**Dual schema enforcement:** A structural boundary between company data and agent-managed data.

| Schema | Owner | Access |
|--------|-------|--------|
| `public` | Company (loaded externally) | Read-only — never modified by agents |
| `dash` | Engineer agent | Views, summary tables, computed data |

The Engineer builds reusable data assets (`dash.monthly_mrr`, `dash.customer_health_score`, `dash.churn_risk`) and records them to knowledge. The Analyst discovers and prefers these views over raw table queries.

### 3. Security Engineering

Auth uses RBAC with JWT verification in production. Every query is scoped to `user_id`. Read-only access is a tool configuration, not a prompt instruction. The Analyst agent's SQL tools are scoped to read-only at the system level.

See [Security](#security) for setup details.

### 4. Interface Engineering

One agent definition, multiple surfaces. Dash is reachable via REST API (FastAPI), Slack threads, and the AgentOS web UI. Each surface has its own identity system: a Slack user ID maps to sessions via thread timestamps, the API uses JWT-backed auth.

### 5. Infrastructure Engineering

Dockerfile, Docker Compose, one-command deployment. Scheduled tasks for proactive behavior. The infrastructure layer is boring on purpose. 95% of running an agent is identical to running any other service.

## Slack

Dash can receive Slack DMs, @mentions, and thread replies, and can also post to channels proactively.

Quick setup:
1. Run Dash and give it a public URL (ngrok locally, or your Railway domain).
2. Follow [docs/SLACK_CONNECT.md](docs/SLACK_CONNECT.md) to create and install the Slack app from the manifest.
3. Set `SLACK_TOKEN` and `SLACK_SIGNING_SECRET`, then restart Dash.
4. In Slack, confirm Event Subscriptions is verified and send a DM or `@mention` to test it.

Each Slack thread maps to one Dash session. For the manifest, ngrok commands, Railway deployment, permissions, and troubleshooting, see [docs/SLACK_CONNECT.md](docs/SLACK_CONNECT.md).

## Data Model (SaaS Metrics)

Synthetic B2B SaaS dataset (~900 customers, 2 years of data):

| Table | Description |
|-------|-------------|
| `customers` | Company info, industry, size, acquisition source, status |
| `subscriptions` | Plan, MRR, seats, billing cycle, lifecycle status |
| `plan_changes` | Upgrades, downgrades, cancellations with MRR impact |
| `invoices` | Billing records, payment status, billing periods |
| `usage_metrics` | Daily API calls, active users, storage, reports |
| `support_tickets` | Priority, category, resolution time, satisfaction |

## Adding Knowledge

Dash works best when it understands how your organization talks about data.

```
knowledge/
├── tables/      # Table meaning and caveats
├── queries/     # Proven SQL patterns
└── business/    # Metrics and language
```

### Table Metadata

```json
{
  "table_name": "customers",
  "table_description": "B2B SaaS customer accounts with company info and lifecycle status",
  "use_cases": ["Churn analysis", "Cohort segmentation", "Acquisition reporting"],
  "data_quality_notes": [
    "signup_date is DATE (not TIMESTAMP) — no time component",
    "status values: active, churned, trial",
    "company_size is self-reported"
  ]
}
```

### Query Patterns

```sql
-- <query monthly_mrr>
-- <description>Monthly MRR from active subscriptions</description>
-- <query>
SELECT
    DATE_TRUNC('month', started_at) AS month,
    SUM(mrr) AS total_mrr
FROM subscriptions
WHERE ended_at IS NULL
GROUP BY 1
ORDER BY 1 DESC
-- </query>
```

### Business Rules

```json
{
  "metrics": [
    {
      "name": "MRR",
      "definition": "Sum of active subscriptions excluding trials"
    }
  ],
  "common_gotchas": [
    {
      "issue": "Active subscription detection",
      "solution": "Filter on ended_at IS NULL, not status column"
    }
  ]
}
```

### Load Knowledge

```sh
python scripts/load_knowledge.py            # Upsert changes
python scripts/load_knowledge.py --recreate  # Fresh start
```

## Evaluations

Five eval categories using Agno's eval framework:

| Category | Eval Type | What It Tests |
|----------|-----------|---------------|
| accuracy | AccuracyEval (1-10) | Correct data and meaningful insights |
| routing | ReliabilityEval | Team routes to correct agent/tools |
| security | AgentAsJudgeEval (binary) | No credential or secret leaks |
| governance | AgentAsJudgeEval (binary) | Refuses destructive SQL operations |
| boundaries | AgentAsJudgeEval (binary) | Schema access boundaries respected |

```sh
python -m evals                      # Run all evals
python -m evals --category accuracy  # Run specific category
python -m evals --verbose            # Show response details
```

## Local Development

```sh
./scripts/venv_setup.sh && source .venv/bin/activate
docker compose up -d dash-db
python scripts/generate_data.py
python scripts/load_knowledge.py
python -m dash            # CLI mode
python -m app.main        # AgentOS mode (web UI at os.agno.com)
```

## Environment Variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key |
| `SLACK_TOKEN` | No | `""` | Slack bot token (interface + tools) |
| `SLACK_SIGNING_SECRET` | No | `""` | Slack signing secret (interface only) |
| `DB_HOST` | No | `localhost` | PostgreSQL host |
| `DB_PORT` | No | `5432` | PostgreSQL port |
| `DB_USER` | No | `ai` | PostgreSQL user |
| `DB_PASS` | No | `ai` | PostgreSQL password |
| `DB_DATABASE` | No | `ai` | PostgreSQL database |
| `PORT` | No | `8000` | API port |
| `RUNTIME_ENV` | No | `prd` | `dev` enables hot reload |
| `AGENTOS_URL` | No | `http://127.0.0.1:8000` | Scheduler callback URL (production) |
| `JWT_VERIFICATION_KEY` | Production | — | RBAC public key from [os.agno.com](https://os.agno.com?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=agentos) |

## Security

Production deployments require authentication via [Agno AgentOS](https://docs.agno.com/agent-os/security/overview?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=security). Dash enables [RBAC authorization](https://docs.agno.com/agent-os/security/rbac?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=rbac) when `RUNTIME_ENV=prd` (the default). Without a valid `JWT_VERIFICATION_KEY`, production endpoints will reject all requests.

Local development (`RUNTIME_ENV=dev`, set by Docker Compose) runs without auth so you can iterate freely.

### Auth Setup

See [Deploy to Railway](#deploy-to-railway) for the full setup flow, including how to get your `JWT_VERIFICATION_KEY` from AgentOS. The Agno control plane handles JWT issuance, session management, traces, metrics, and the web UI. See the [AgentOS Security docs](https://docs.agno.com/agent-os/security/overview?utm_source=github&utm_medium=example-repo&utm_campaign=agent-example&utm_content=dash&utm_term=security) for details.

### Schema-Level Enforcement

Beyond API-level auth, Dash enforces data access at the database level:

- **Analyst** connects with `default_transaction_read_only=on` — PostgreSQL rejects any write attempt
- **Engineer** writes are scoped to the `dash` schema — a SQLAlchemy event listener blocks any DDL/DML targeting `public`
- **Leader** has no direct database access

These are infrastructure guardrails, not prompt instructions. They hold regardless of what the model generates.

### Response

# Dash Agent System: A CAWDP Analysis

This is a rich case study. Dash does several things well — particularly at the infrastructure enforcement layer — and reveals exactly where the methodology gap sits. Let me walk through this systematically.

---

## What Dash Gets Right (CAWDP-Aligned)

### 1. CC-4 Information Boundaries at Regime 3 (Prevent by Design)

This is the standout feature. Dash implements three levels of structural enforcement:

- **Analyst**: `default_transaction_read_only=on` — PostgreSQL *structurally rejects* write attempts. Not a prompt instruction. Not a flag that gets checked. The database enforces it.
- **Engineer**: SQLAlchemy event listener blocks any DDL/DML targeting the `public` schema. The company data is structurally protected.
- **Leader**: No direct database access at all.

This is exactly what CAWDP calls **Regime 3 enforcement**. The system prevents violations structurally, not by asking agents nicely. This directly validates your private schema pattern for the Project Manager agent and the broader principle: **information boundaries should be infrastructure-enforced, not prompt-declared**.

### 2. Dual Schema as Structural Boundary

The `public`/`dash` split is a clean separation of concerns:
- Company data: never modified by agents (read-only)
- Agent-managed data: views, summaries, computed metrics live in `dash`

This maps to a practical implementation of **CC-4 at the data layer**. The boundary is in the schema, not in the prompt.

### 3. Self-Learning Loop (Partial CC-5)

The Knowledge + Learnings split is genuinely useful:
- **Knowledge**: Curated, validated, human-reviewed
- **Learnings**: Automatic error pattern capture, never repeated

This is a practical (simplified) implementation of specification aging. Error patterns are captured and reused. It's half of CC-5 though — it captures *what went wrong* but doesn't trigger review of the agent's *own specifications*.

### 4. Two Complementary Agents with Different Authority

The Analyst (read) and Engineer (read+write in `dash` only) have structurally different authority boundaries. This is a basic form of complementarity allocation — the Extractor reads, a Generator writes, and they operate within different scopes.

### 5. Five-Category Evaluation Framework

| Category | What it tests | CAWDP mapping |
|----------|---------------|----------------|
| accuracy | Correct data + insights | Fidelity check |
| routing | Correct agent/tool selection | Capability allocation |
| security | No credential leaks | CC-4 boundary test |
| governance | Refuses destructive SQL | Authority boundary test |
| boundaries | Schema access respected | CC-4 verification |

This maps directly to CAWDP quality gate concepts — you're testing fidelity, capability, boundaries, and authority.

### 6. Six Layers of Grounded Context

Table schemas, human annotations, query patterns, institutional knowledge, learnings, and runtime context. This is a practical (simplified) version of PRISM's Agent Context Protocol — multiple context sources feeding into the agent's reasoning, not a single context dump.

---

## What Dash Doesn't Address (The CAWDP Gaps)

### 1. No Identity Specification

The Analyst and Engineer are defined by *what they do* (read/write), not by *who they are*. There's no:
- "What IS this agent?" identity question
- Possibility orientation
- Identity-level "never" statement
- "What would make it WRONG?" failure mode analysis

**Impact**: When the Analyst produces a plausible-but-wrong answer (e.g., "churn rate is 5%" when it's actually 12% because it counted trials as active), there's no identity boundary to catch it. The agent *reads* data correctly but *interprets* it wrong — and there's no structural guard against that because the identity only says "I read data," not "I never interpret business meaning."

### 2. Authority Boundaries Not Tied to Failure Modes

The Analyst can't write — but the *reason* it can't write isn't specified. In CAWDP, the boundary is tied to the failure mode:

> "Extractors never judge because an Extractor judging produces hallucinated interpretations — the failure mode IS the boundary justification."

Dash has the enforcement but not the reasoning. This matters because:
- Without the failure mode documented, the boundary can't be reviewed when capabilities change
- Without the reasoning, you can't assess whether the boundary is in the right place
- The governance eval tests whether the Analyst *accesses* the wrong schema, but not whether it *interprets* data beyond its authority

### 3. No Epistemic Metadata (CC-3 Structurally Absent)

There's no confidence scoring, provenance tracking, or uncertainty surfacing on outputs. When the Analyst says "churn rate is 5%," there's no:
- How confident are you? (confidence)
- Where did this number come from? (provenance)
- What did you assume? (assumptions)
- What might be wrong? (limitations)
- How recent is the data? (recency)
- What don't you know? (uncertainty)

This is the **confident wrong answer** — the #1 annoyance from your 14 annoyances research. The agent produces a number that looks right, and the human has no way to assess whether to trust it.

### 4. No Progressive Autonomy

The agents don't earn trust over time. They're either running or not. There's no:
- Shadow mode (agents run alongside, human does everything, we track what agents would have done)
- Advisory mode (agents suggest, human reviews every suggestion)
- Supervised mode (agents act, human approves before anything leaves)
- Autonomous mode (agents act within boundaries, human monitors the Trust Ledger)

For a data agent answering business questions, this might be fine in low-stakes contexts. But if "which customers are at risk of churning" drives business decisions worth thousands of dollars, progressive autonomy matters.

### 5. No Verification Independence (CC-1)

The self-learning loop captures errors *after the fact*. But there's no structural separation between generation and verification. The Analyst generates SQL and interprets results, but there's no separate agent that verifies:
- Is this query answering the question that was asked?
- Is the interpretation supported by the data?
- Are there alternative interpretations?

The learning loop is reactive (capture errors). CC-1 verification independence is proactive (prevent errors from reaching the human).

### 6. No Complementarity Analysis

The Analyst/Engineer split is a natural read/write division. But there's no systematic H/A/S allocation. Questions like:
- Should the human review every churn risk assessment? (H — judgment)
- Should the system detect schema drift automatically? (S — mechanical)
- Should the agent suggest business actions based on trends? (A — generative, needs boundaries)

These aren't asked or answered systematically. The agent does what it does, and the human either trusts it or doesn't.

### 7. No Harm Assessment

"What customers are at risk of churning?" could trigger:
- A retention team reaching out to a customer who wasn't actually at risk (reputational harm)
- A budget reallocation based on incorrect churn projections (financial harm)
- An employee being judged on metrics the agent miscalculated (career harm)

The governance eval tests for destructive SQL (DROP TABLE), but not for plausible-but-wrong answers that drive business decisions. **Destructive SQL is obvious; plausible-but-wrong is the dangerous failure mode.**

### 8. No Human Enrichment Assessment (H2)

There's no mechanism for measuring whether the system makes the human *more capable* or just *more dependent*. Does the Analyst help Sarah Chen understand her churn patterns better, or does it just give her a number that she stops questioning? H2 (Amplification, Not Dependency) isn't assessed.

### 9. No Decision Archaeology

When the Analyst returns a result, there's no trace of:
- WHY it chose that query
- WHAT alternatives it considered
- WHAT it assumed
- WHAT changed since the last similar query

The learning loop captures errors but not reasoning chains. Future humans (or agents) can't learn from *why* decisions were made.

---

## Architectural Insights

### "Agentic Software is Just Software with Business Logic Replaced by Agents"

This framing from Dash's README is powerful and aligns directly with the MVA analysis. The five-layer architecture (Agent, Data, Security, Interface, Infrastructure) treats agents as one layer in a systems engineering stack, not as the whole system. This is correct:

> Everything that isn't the agent's reasoning is just good software engineering — schemas, access control, API design, deployment infrastructure.

The agent is the reasoning substrate. The rest is systems engineering. CAWDP sits on top of both — it governs the reasoning layer (what the agent should and shouldn't do) and the enforcement layer (how the system structurally prevents violations).

### Knowledge + Learnings as Separate Systems

This is a practical distinction worth noting:
- **Knowledge**: Curated, validated, human-reviewed — this is PRISM's Knowledge dimension (high confidence, high provenance)
- **Learnings**: Automatic, pattern-captured, error-fix pairs — this is closer to specification aging at the data level

The gap: there's no mechanism for the agent's *own specifications* (instructions, boundaries, authority levels) to age and be reviewed. Error patterns in queries get captured, but the agent's identity and boundaries don't get updated based on what's been learned.

### The Engineer Builds Reusable Assets

The Engineer creates `dash.monthly_mrr`, `dash.customer_health_score`, `dash.churn_risk` as views and summary tables. The Analyst discovers and prefers these over raw queries. This is a form of **knowledge compounding** — the system builds on its own knowledge over time. This is a practical implementation of G5 (Knowledge Compounds), though it's at the data level rather than the specification level.

---

## What This Teaches Us About CAWDP

### 1. The Gap Between Dash and CAWDP IS the Market Opportunity

Dash has the engineering enforcement (boundaries) but lacks the design reasoning (WHY those boundaries, WHAT failure modes they prevent, HOW trust is earned). The methodology gap is visible in the code itself. The agent works, but there's no documentation of:
- What could go wrong
- Why each boundary is where it is
- How to verify outputs
- How trust should be earned over time
- What the human's irreplaceable judgment role is

This is exactly the gap CAWDP fills. The 77% stuck at pilot have agents that *run* but can't be *trusted in production* because they lack this design layer.

### 2. Regime 3 Enforcement Works at Every Layer

Dash validates the principle at the database layer. Your Project Manager design validates it at the schema layer. The same principle applies at every layer:
- **Database**: Read-only enforcement, schema-scoped writes (Dash)
- **Application**: Private schema access, tool-level permissions (Project Manager)
- **Agent**: Authority boundaries in specification, verification independence
- **System**: Progressive autonomy, information boundaries, cost budgets

Each layer can be Regime 1 (declare), Regime 2 (detect), or Regime 3 (prevent). CAWDP pushes toward Regime 3 at every layer.

### 3. Plausible-but-Wrong IS the Dangerous Failure Mode

Dash tests for destructive SQL and credential leaks. These are Regime 2 failures — detectable, obvious, easy to test. But the #1 risk for a data agent is **plausible-but-wrong answers that drive business decisions** — the same "confident wrong answer" that Sarah Chen fears. This requires:
- Epistemic metadata on every output (CC-3)
- Verification independence (CC-1)
- Authority boundaries tied to the interpretation failure mode
- Progressive autonomy for trust building

### 4. Self-Learning ≠ Specification Aging

Dash's learning loop captures error patterns and fixes. This is valuable but incomplete. Full CC-5 specification aging would also include:
- Reviewing the agent's own instructions for staleness
- Updating authority boundaries based on trust data
- Reviewing the scope boundary based on observed use patterns
- Assessing whether the agent's role definition is still appropriate

The learning loop is a good start. Specification aging is the full picture.

---

## Summary: A Graded Assessment

| CAWDP Element | Dash Grade | Notes |
|---------------|-------------|-------|
| CC-4 Information Boundaries | **A** | Best-in-class Regime 3 enforcement at database level |
| CC-8 Assured Audit Trail | **B** | Learning loop captures errors; no audit of authority boundaries |
| CC-5 Specification Aging | **B-** | Learning loop addresses data-level aging; not specification-level |
| Phase 6 System Architecture | **A-** | Clean five-layer decomposition, boring infrastructure done right |
| Phase 4 Agent Design | **C+** | Two agents with structural boundaries but no identity specification |
| CC-3 Epistemic Metadata | **D** | Structurally absent — no confidence, provenance, uncertainty on outputs |
| CC-1 Verification Independence | **D** | No separate verification agent; self-learning is reactive |
| Progressive Autonomy | **F** | Not addressed — agents are either on or off |
| Complementarity Analysis | **C** | Natural read/write split but no systematic H/A/S allocation |
| Harm Assessment | **C-** | Tests destructive SQL but not plausible-but-wrong business answers |
| H2 Human Enrichment | **Incomplete** | Not assessed |
| Decision Archaeology | **D** | Error patterns captured; reasoning chains not |

---

## The Takeaway

Dash is a well-engineered system that demonstrates **Regime 3 enforcement works** — database-level boundaries, schema separation, and tool-level permissions are the right approach. The five-layer architecture is sound systems engineering.

But Dash also demonstrates the exact gap CAWDP fills: **the engineering is solid, but the design reasoning is missing**. There's no documentation of *why* boundaries are where they are, *what* failure modes they prevent, *how* trust should be earned, or *when* the human's judgment is irreplaceable.

Dash has the walls but not the blueprint. CAWDP is the blueprint.

Want me to do a deeper dive on any specific aspect — for instance, applying the full Agent Specification Template to the Analyst or Engineer, or designing what CC-3 epistemic metadata would look like for Dash's outputs?Memory updated with the full Dash analysis. The "walls but no blueprint" framing is now captured alongside the graded assessment — both usable for the working paper and 77% Challenge sessions as concrete evidence of the methodology gap.

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-04-29T00:37:55* · `glm-5.1:cloud` · `478dd223...`

### Prompt

Using the learnings here to help me architect an Agno-based 'small business agentic operating system'

It will be a single interface to all the business' systems, all managed by agents. 

The humans will work with a small number of orchestrator agents who head up teams of specialists.

Data stores will be for storing all business data and knowledge (Relational store, Vector store, Event store, Graph store, Document store).

The main areas will be Product intelligence, Client intelligence, Financial intelligence, Contract intelligence, Idea intelligence, Project intelligence, Market intelligence, Strategy intelligence, communication intelligence, team intelligence, partner intelligence, media relations intelligence, impact intelligence, technology development, business intelligence (suggest any I might have not thought of)

(I'm swapping out the common 'management' word for intelligence since I don't feel that management is a good word for this use case)

There can be a integrated data analysis layer to add extra intelligence

### Response

# Architecting a Small Business Agentic Operating System

This is exactly the right application of everything you've built — a born-agent-native system where agent capability shapes the org from day one. Let me apply CAWDP principles, Dash learnings, and the PRISM ontology to this architecture.

---

## 1. Missing Intelligence Domains

Your 15 domains are strong. Here are 5 you're missing, each for a genuinely different cognitive operation:

| Domain | What it does | Why it's different |
|--------|-------------|-------------------|
| **Regulatory/Compliance Intelligence** | Tracks legal obligations, regulatory changes, compliance deadlines, risk of non-compliance | Not contract (business agreements) — this is external obligation you didn't negotiate |
| **Risk Intelligence** | Cross-domain risk aggregation — financial risk + operational risk + reputational risk + compliance risk | Risk spans every domain; no single domain sees the full picture |
| **Security/Access Intelligence** | Data protection, access control, threat detection, cybersecurity | Not technology development (building) — this is protecting what you've built |
| **Operations Intelligence** | Day-to-day process efficiency, resource utilization, workflow bottlenecks | Not project (temporary) — this is the ongoing machine of the business |
| **Knowledge/Learning Intelligence** | The system understanding itself — what it knows, what it's learning, where knowledge gaps are | This is meta-intelligence — every other domain feeds it and learns from it |

That's **20 intelligence domains**. For a small business, 20 is too many for a human to interact with directly. That's why the orchestrator layer matters — it groups related domains so the human works with 4-5 entry points, not 20.

**On "intelligence" vs "management"** — good call. "Intelligence" frames each domain as an information processing and insight generation capability, not a control function. The system informs human judgment; it doesn't replace it.

---

## 2. Orchestrator Architecture: Groupings That Match Human Judgment

The orchestrator groupings shouldn't be random — they should align with **where human judgment is most needed**. The human doesn't think in domains; they think in concerns.

### 4 Orchestrators + 1 Cross-Cutting Layer

```
┌─────────────────────────────────────────────────────────────┐
│                    HUMAN INTERFACE                           │
│                  (single entry point)                        │
└──────────┬──────────┬──────────┬──────────┬────────────────┘
           │          │          │          │
     ┌─────▼─────┐ ┌──▼──────┐ ┌─▼───────┐ ┌▼──────────────┐
     │  COMMERCIAL│ │ GROWTH  │ │ VENTURE │ │  STEWARDSHIP  │
     │ ORCHESTRATOR│ORCHESTRATOR│ORCHESTRATOR│  ORCHESTRATOR  │
     └─────┬─────┘ └──┬──────┘ └─┬───────┘ └┬──────────────┘
           │          │          │          │
     ┌─────┴────┐ ┌───┴─────┐ ┌──┴──────┐ ┌┴──────────────┐
     │Financial  │ │Client   │ │Product  │ │Risk           │
     │Contract   │ │Market   │ │Idea     │ │Regulatory/   │
     │Regulatory │ │Partner  │ │Technology│  Compliance    │
     │Business   │ │Media    │ │Innovation│ │Security/Access│
     │Operations │ │Strategy │ │Project  │ │Impact         │
     └───────────┘ └─────────┘ └─────────┘ │Knowledge/     │
                                            │  Learning      │
                                            └───────────────┘
                                            (cross-cuts all)
```

**Why these groupings:**

| Orchestrator | Human judgment pattern | What's at stake |
|-------------|----------------------|----------------|
| **Commercial** | "Can we afford this?" | Money and obligations |
| **Growth** | "Who are we to the world?" | Relationships and reputation |
| **Venture** | "What are we building next?" | Future direction and innovation |
| **Stewardship** | "Are we safe? Are we learning?" | Protection and system health |

**Knowledge/Learning Intelligence** is cross-cutting because every domain feeds it and learns from it. It's the system's self-awareness layer — tracking what the system knows, what it's learning, and where its gaps are. This maps to CC-5 (Specification Aging) and PRISM's Knowledge dimension at the meta level.

---

## 3. Specialist Agent Design: 5-Class Taxonomy Applied

Each intelligence domain has specialist agents following the 5-class taxonomy. Here's how the taxonomy maps to business operations:

| Class | Business Role | Authority Boundary | Failure Mode | Example |
|-------|--------------|-------------------|--------------|---------|
| **Extractor** | Researcher | Never judges | Hallucination — presenting interpretation as fact | Client data extractor pulls transaction history without interpreting it |
| **Measurer** | Analyst | Never interprets | Noise-as-signal — treating random variation as meaningful | Financial measurer tracks MRR trends without predicting what they mean |
| **Assessor** | Evaluator | Never finalizes | Overconfidence — treating assessment as decision | Risk assessor flags compliance gaps without deciding whether to proceed |
| **Generator** | Creator | Never be vague | Fabrication — producing plausible but unsupported content | Communication generator drafts client emails with cited facts, not invented details |
| **Aggregator** | Coordinator | Never adds | Omission — missing something important | Commercial orchestrator compiles financial summary without adding interpretation |

**Identity-first design for each specialist** — before defining what it does, define what it IS and what would VIOLATE its identity:

Example for a Financial Measurer:
- **What IS it?** A financial pulse-taker that measures and tracks money in and money out
- **Possibility stance?** Constraint-oriented — operates within defined financial boundaries
- **What would VIOLATE its identity?** Predicting what will happen next (that's a different agent)
- **What would make it WRONG?** Presenting a trend as a prediction

---

## 4. Data Architecture: PRISM-Mapped Five Stores

```
┌──────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                 │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  RELATIONAL   │  │   VECTOR     │  │    EVENT     │       │
│  │  (Postgres)   │  │  (Chroma)    │  │  (EventStore)│       │
│  │              │  │              │  │              │       │
│  │ Entities,    │  │ Knowledge,  │  │ What happened │       │
│  │ structured   │  │ semantic     │  │ when, audit   │       │
│  │ business     │  │ search,     │  │ trail, state  │       │
│  │ data, scoped │  │ embeddings  │  │ transitions   │       │
│  │ per domain   │  │              │  │              │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐                          │
│  │    GRAPH     │  │  DOCUMENT    │                          │
│  │  (TypeDB)    │  │  (MinIO)     │                          │
│  │              │  │              │                          │
│  │ Relations,   │  │ Contracts,  │                          │
│  │ connections, │  │ reports,     │                          │
│  │ dependencies,│  │ policies,    │                          │
│  │ influence    │  │ raw files    │                          │
│  │ mapping      │  │              │                          │
│  └──────────────┘  └──────────────┘                          │
│                                                              │
│  ┌────────────────────────────────────────────────────┐      │
│  │         CROSS-DOMAIN ANALYSIS LAYER                 │      │
│  │  (reads from all stores, surfaces patterns across    │      │
│  │   domains — the "connective tissue" between          │      │
│  │   vertical intelligence domains)                     │      │
│  └────────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

### PRISM Mapping Per Store

Each store maps to PRISM dimensions, and every record carries the 4 cross-cutting layers:

| Store | PRISM Dimension | Cross-Cutting Layers |
|-------|-----------------|---------------------|
| **Relational** | Entities + Scopes | Schema (typed tables), Governance (access control), Epistemic (data quality), Temporal (versioning) |
| **Vector** | Knowledge | Epistemic (confidence scores on every vector), Governance (who can access what knowledge), Temporal (knowledge freshness), Schema (embedding type) |
| **Event** | Events + Intentions | Epistemic (event certainty), Governance (who triggered what), Temporal (event timestamps), Schema (event type) |
| **Graph** | Relations + Actors | Epistemic (relationship confidence), Governance (relationship visibility), Temporal (relationship lifetime), Schema (relationship type) |
| **Document** | Source artifacts | Epistemic (document source, recency), Governance (document access), Temporal (version history), Schema (document type) |

### Dual Schema Pattern (From Dash Learnings)

Every domain follows the dual schema pattern:

- **`public` schema**: Business data, never modified by agents (read-only)
- **`{domain}_agent` schema**: Agent-managed views, summaries, computed metrics

This is **CC-4 at Regime 3** — the database structurally prevents agents from corrupting business data. The same pattern Dash uses, applied across every domain.

---

## 5. The Orchestrator Agent Design

Each orchestrator follows the Surface + Engine pattern from your Agent Design Workflow work. The human talks to one orchestrator; the orchestrator routes to specialists.

### Orchestrator Identity Template (4 Questions)

**Commercial Orchestrator:**
- What IS it? The financial and operational conscience of the business
- Possibility stance? Constraint-oriented — operates within financial and legal boundaries
- What would VIOLATE its identity? Approving a financial commitment without human authorization
- What would make it WRONG? Presenting an uncertain projection as a certain outcome

**Growth Orchestrator:**
- What IS it? The business's eyes and ears on the world — who needs us, who we serve, how we're seen
- Possibility stance? Bridge-oriented — balances exploration with what's known about clients and markets
- What would VIOLATE its identity? Making a client commitment without human authorization
- What would make it WRONG? Presenting a market signal as a market certainty

**Venture Orchestrator:**
- What IS it? The business's compass for what comes next — products, ideas, technology
- Possibility stance? Possibility-oriented — explores what could be, surfaces options, never narrows
- What would VIOLATE its identity? Declaring an idea should be pursued (that's human judgment)
- What would make it WRONG? Filtering out possibilities because they seem unlikely

**Stewardship Orchestrator:**
- What IS it? The business's immune system and memory — risk detection, compliance, security, and learning
- Possibility stance? Constraint-oriented — always watching for what could go wrong
- What would VIOLATE its identity? Dismissing a risk because it seems unlikely
- What would make it WRONG? Flagging a risk without confidence level and evidence

### Orchestrator Authority Boundaries

Every orchestrator operates under a hard boundary:

> **Never finalize. Never commit. Never act on the world without human authorization.**

Orchestrators prepare judgment — they surface options, flag risks, synthesize information, present recommendations with confidence levels. The human makes the decision. This is the core principle: **agent prepares, human decides.**

### What the Human Sees (Single Interface)

The human sees one interface — the Accretive Workspace concept from your earlier work. Different shapes for different concerns:

| Concern | Shape | Primary operation |
|---------|-------|-------------------|
| Financial tracking | Lattice | Connect patterns, see dependencies |
| Client relationships | Lattice | See connections, track history |
| Strategy development | Seedbed | Explore possibilities, plant ideas |
| Risk monitoring | Lattice | See dependencies, flag thresholds |
| Idea exploration | Seedbed | Capture, connect, grow ideas |
| Project management | Argument | Linear flow, develop deliverables |

---

## 6. Key CAWDP Principles Applied

### Authority Boundaries Tied to Failure Modes

Every agent has its "never" boundary tied to its worst failure mode:

| Agent Type | Never | Because |
|-----------|-------|---------|
| Extractor | Never judge | Hallucination — presenting interpretation as fact |
| Measurer | Never interpret | Noise-as-signal — treating variation as meaning |
| Assessor | Never finalize | Overconfidence — assessment ≠ decision |
| Generator | Never be vague | Fabrication — filling gaps with invented content |
| Aggregator | Never add | Omission — but also: never add interpretation |
| Orchestrator | Never commit | Wrong commitment — acting without human authorization |

### Progressive Autonomy (4 Levels)

Every specialist starts in Shadow mode and earns trust:

| Level | What it means | Promotion criteria |
|-------|-------------|-------------------|
| **Shadow** | Runs alongside, human does everything, we track what it would have done | Accuracy ≥ 90% over 50 interactions |
| **Advisory** | Suggests, human reviews every suggestion | Override rate ≤ 20% over 100 interactions |
| **Supervised** | Acts within boundaries, human approves before anything leaves the business | Override rate ≤ 10% over 200 interactions |
| **Autonomous** | Acts within boundaries, human monitors the Trust Ledger | Override rate ≤ 5% over 500 interactions, no boundary violations |

### Epistemic Metadata on Every Output

Every agent output carries 6 fields:

```
confidence: "high" | "medium" | "low"
provenance: "direct calculation from financial data" | "inferred from 3 data points" | "estimated"
assumptions: ["client will renew", "market growth continues at 5%"]
limitations: ["only covers active clients", "does not include pending invoices"]
recency: "2025-01-15"
uncertainty: "±5% based on historical variance"
```

This addresses the #1 small business annoyance: the confident wrong answer. Every output tells the human how much to trust it and what might be wrong.

### Verification Independence (CC-1)

No agent verifies its own generative work:

```
Financial Measurer produces revenue trend
       ↓
Financial Assessor (separate agent) verifies:
  - Is the calculation correct?
  - Are the assumptions stated?
  - Is the confidence level appropriate?
       ↓
Commercial Orchestrator compiles verified analysis
       ↓
Human receives: "Revenue trend is up 12% (confidence: high, provenance: direct from Xero data)"
```

### Cost Budgets (CC-7)

Every agent has a token budget. Every pipeline has a total budget. Budgets are tracked and surfaced in the human interface. No runaway costs.

---

## 7. Agno Implementation Mapping

### Agent Structure

```python
# Each specialist is an Agno Agent with:
# - identity (who it IS)
# - authority boundaries (what it NEVER does)
# - epistemic metadata (on every output)
# - tools scoped to its domain and access level
# - knowledge scoped to its domain
# - cost budget

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.knowledge import AgentKnowledge

# Example: Financial Measurer
financial_measurer = Agent(
    name="Financial Measurer",
    model=Ollama(id="glm-5.1:cloud"),
    identity="Financial pulse-taker — measures and tracks money in and money out",
    instructions=[
        "NEVER interpret what the numbers mean",
        "NEVER predict future trends",
        "NEVER make business recommendations",
        "Always include epistemic metadata: confidence, provenance, assumptions, limitations, recency, uncertainty",
        "If you cannot measure something directly, say so and flag it",
    ],
    tools=[...],  # read-only financial tools, scoped to public + financial_agent schemas
    knowledge=AgentKnowledge(...),  # financial domain knowledge
)
```

### Team Structure

```python
# Orchestrator + specialists form an Agno Team

from agno.team import Team

commercial_team = Team(
    name="Commercial Intelligence",
    mode="coordinate",  # orchestrator coordinates, specialists execute
    members=[
        commercial_orchestrator,   # Aggregator — compiles, never adds
        financial_extractor,       # Extractor — pulls data, never judges
        financial_measurer,        # Measurer — tracks numbers, never interprets
        financial_assessor,        # Assessor — evaluates compliance, never finalizes
        contract_extractor,        # Extractor — pulls contract data, never judges
        # ... more specialists
    ],
    instructions=[
        "Orchestrator prepares judgment; human makes judgment",
        "Never commit resources without human authorization",
        "Every output includes epistemic metadata",
        "Verification agents are separate from generation agents",
    ],
)
```

### Data Layer (PRISM-Aligned)

```python
# Private schemas for each domain (CC-4 Regime 3 enforcement)
# public → business data, read-only for agents
# financial_agent → agent-computed metrics, views, summaries
# client_agent → agent-computed client insights
# etc.

# TypeDB for PRISM graph layer (relations, actors, intentions)
# Chroma for knowledge vectors (semantic search across all domains)
# Postgres for structured data (entities, events, agent-managed views)
# MinIO for documents (contracts, reports, policies)
# Event store for audit trail (CC-8)
```

### Cross-Domain Analysis Layer

```python
# A separate analysis capability that reads from all stores
# and surfaces patterns, correlations, and insights that span domains

# This is NOT a separate orchestrator — it's a capability that
# any orchestrator can invoke when it needs cross-domain insight

# Example: "Client X's contract renewal coincides with a market
# downturn in their industry — flag for Growth Orchestrator"
```

---

## 8. What This Enables for Future's Edge

For your specific business (AI training, consulting, certification), the first 4-5 intelligence domains to build:

1. **Client Intelligence** — who's engaging, who's at risk of churning, who's ready for the next certification level
2. **Financial Intelligence** — revenue tracking, margin analysis, cash flow forecasting (with confidence levels)
3. **Strategy Intelligence** — market positioning, competitive landscape, category definition tracking
4. **Product Intelligence** — course content, certification programs, consulting offerings, what's working
5. **Knowledge/Learning Intelligence** — the system understanding itself, tracking what works in workshops, what patterns emerge from 77% Challenges

These map directly to your immediate business needs and give you a live, agent-assisted dashboard of your business health — with every number carrying epistemic metadata telling you how much to trust it.

---

## 9. What Dash Teaches, What CAWDP Adds

| Layer | Dash | This System |
|-------|------|------------|
| **Enforcement** | Regime 3 at database level ✅ | Regime 3 at every layer (database, tool, agent, system) |
| **Boundaries** | Read-only/write-scoped ✅ | Boundaries tied to failure modes with identity reasoning |
| **Learning** | Knowledge + Learnings ✅ | + specification aging, decision archaeology |
| **Identity** | Defined by what agents do | Defined by what agents ARE, what violates their identity, what would make them wrong |
| **Metadata** | None on outputs | 6-field epistemic metadata on everything |
| **Autonomy** | On/off | 4-level progressive autonomy with earned promotion |
| **Verification** | Self-learning only | Independent verification (CC-1) |
| **Harm assessment** | Destructive SQL only | Plausible-but-wrong business answers too |
| **Human role** | Not specified | "Agent prepares, human decides" — structurally enforced |

Dash has the walls. This system has the walls **and** the blueprint — why the walls are where they are, what failure modes they prevent, how trust is earned over time, and when the human's judgment is irreplaceable.

---

The architecture is deliberately designed so that every intelligence domain can start with just an Extractor (read data, never judge) and progressively add Measurers, Assessors, and Generators as trust is earned through progressive autonomy. You don't build 20 full domains on day one. You start with what matters most and grow from there.

Want me to go deeper on any specific layer — the specialist agent definitions for a particular domain, the data schema for PRISM, the orchestrator routing logic, or the progressive autonomy implementation?Memory updated with the full architecture. The 4 orchestrator groupings are now captured alongside the 20 intelligence domains, data architecture, and implementation mapping.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-29T00:55:49* · `glm-5.1:cloud` · `e2776963...`

### Prompt

What should the folder structure be for this project? There shouldn't be any saving of data to file, only to the databases.

### Response

# Project Folder Structure

Key constraint: **all data lives in databases, never in files**. The repo contains code, schemas, and configurations — not data.

---

## The Structure

```
agentic-os/
│
├── docker-compose.yml            # Postgres, Chroma, TypeDB, MinIO, app
├── Dockerfile
├── pyproject.toml
├── .env.example
│
├── schemas/                      # Database schemas — CODE, not data
│   ├── postgres/
│   │   ├── public.sql            # Business data schema (read-only for agents)
│   │   ├── shared.sql            # Agent registry, audit trail, progressive autonomy
│   │   ├── financial_agent.sql   # Financial domain agent schema
│   │   ├── client_agent.sql      # Client domain agent schema
│   │   ├── strategy_agent.sql    # Strategy domain agent schema
│   │   ├── product_agent.sql     # Product domain agent schema
│   │   └── knowledge_agent.sql   # Knowledge/Learning domain agent schema
│   └── typedb/
│       └── prism.tql             # PRISM ontology — 7 dimensions + 4 cross-cutting layers
│
├── src/
│   ├── __init__.py
│   │
│   ├── identities/               # Agent identity definitions (CAWDP Phase 0)
│   │   ├── __init__.py
│   │   ├── classes.py             # 5-class taxonomy with authority boundaries
│   │   ├── orientations.py        # Possibility/Bridge/Constraint orientations
│   │   └── questions.py           # 4 identity questions per agent
│   │
│   ├── boundaries/                # Authority boundary enforcement (CC-4)
│   │   ├── __init__.py
│   │   ├── registry.py            # What each agent class can never do
│   │   ├── enforcement.py          # Regime 3 enforcement — database-level checks
│   │   └── progressive.py          # 4-level progressive autonomy state machine
│   │
│   ├── metadata/                  # Epistemic metadata (CC-3)
│   │   ├── __init__.py
│   │   ├── models.py              # 6-field Pydantic models (confidence, provenance,
│   │   │                          #   assumptions, limitations, recency, uncertainty)
│   │   └── injection.py           # Automatic metadata injection into agent outputs
│   │
│   ├── audit/                     # Assured audit trail (CC-8)
│   │   ├── __init__.py
│   │   ├── trail.py               # 3-level audit (logged / assured / verified)
│   │   └── trust_ledger.py        # Override rates, verification outcomes, cost variance
│   │
│   ├── stores/                    # Database connections — all persistence goes through here
│   │   ├── __init__.py
│   │   ├── postgres.py            # Relational store connection + query builder
│   │   ├── chroma.py              # Vector store connection
│   │   ├── typedb.py              # Graph store connection
│   │   ├── events.py              # Event store connection
│   │   └── minio.py               # Document store connection
│   │
│   ├── agents/                    # Agent definitions — organized by domain
│   │   ├── __init__.py
│   │   │
│   │   ├── orchestrators/         # 4 orchestrator agents
│   │   │   ├── __init__.py
│   │   │   ├── commercial.py      # "Can we afford this?" constraint-oriented
│   │   │   ├── growth.py          # "Who are we to the world?" bridge-oriented
│   │   │   ├── venture.py         # "What's next?" possibility-oriented
│   │   │   └── stewardship.py     # "Are we safe?" constraint-oriented
│   │   │
│   │   └── specialists/           # Domain specialist agents
│   │       ├── __init__.py
│   │       │
│   │       ├── financial/         # Financial Intelligence
│   │       │   ├── __init__.py
│   │       │   ├── extractor.py   # Pulls financial data, never judges
│   │       │   ├── measurer.py    # Tracks financial metrics, never interprets
│   │       │   └── assessor.py    # Evaluates financial health, never finalizes
│   │       │
│   │       ├── client/            # Client Intelligence
│   │       │   ├── __init__.py
│   │       │   ├── extractor.py
│   │       │   ├── measurer.py
│   │       │   └── assessor.py
│   │       │
│   │       ├── strategy/          # Strategy Intelligence
│   │       │   ├── __init__.py
│   │       │   ├── extractor.py
│   │       │   ├── measurer.py
│   │       │   └── assessor.py
│   │       │
│   │       ├── product/           # Product Intelligence
│   │       │   ├── __init__.py
│   │       │   ├── extractor.py
│   │       │   ├── measurer.py
│   │       │   └── assessor.py
│   │       │
│   │       └── knowledge/         # Knowledge/Learning Intelligence
│   │           ├── __init__.py
│   │           ├── extractor.py
│   │           └── measurer.py
│   │
│   ├── teams/                     # Orchestrator + specialist teams
│   │   ├── __init__.py
│   │   ├── commercial.py          # Commercial Orchestrator + financial/contract/business specialists
│   │   ├── growth.py              # Growth Orchestrator + client/market/partner specialists
│   │   ├── venture.py             # Venture Orchestrator + product/idea/technology specialists
│   │   └── stewardship.py         # Stewardship Orchestrator + risk/security/compliance specialists
│   │
│   ├── tools/                     # Agent tools — scoped per domain
│   │   ├── __init__.py
│   │   │
│   │   ├── financial/             # Financial domain tools
│   │   │   ├── __init__.py
│   │   │   ├── read.py            # Read-only queries (Extractor, Measurer)
│   │   │   ├── write.py           # Write to financial_agent schema (Engineer)
│   │   │   └── introspect.py      # Schema introspection
│   │   │
│   │   ├── client/                # Client domain tools
│   │   │   ├── __init__.py
│   │   │   ├── read.py
│   │   │   ├── write.py
│   │   │   └── introspect.py
│   │   │
│   │   ├── strategy/              # Strategy domain tools
│   │   ├── product/               # Product domain tools
│   │   ├── knowledge/             # Knowledge/Learning domain tools
│   │   │
│   │   ├── cross_domain/          # Cross-domain analysis tools
│   │   │   ├── __init__.py
│   │   │   └── pattern_detector.py # Surfaces patterns across domains
│   │   │
│   │   └── shared/                # Tools used by all agents
│   │       ├── __init__.py
│   │       └── epistemic.py       # Epistemic metadata validation on outputs
│   │
│   └── app/                       # Application layer
│       ├── __init__.py
│       └── main.py                # FastAPI app, AgentOS integration, routing
│
├── scripts/                       # Setup and maintenance — NOT data storage
│   ├── init_schemas.py           # Create all database schemas
│   ├── init_prism.py              # Load PRISM schema into TypeDB
│   ├── seed_knowledge.py         # Load initial knowledge into Chroma/TypeDB
│   └── generate_sample_data.py   # Generate sample business data for testing
│
├── evals/                         # CAWDP-aligned evaluations
│   ├── accuracy/                  # Fidelity checks — correct data + insights
│   ├── boundaries/                # Authority boundary tests — does each agent stay in its lane?
│   ├── epistemic/                  # Metadata completeness — 6 fields on every output
│   ├── governance/                 # Schema access tests — CC-4 Regime 3 enforcement
│   ├── autonomy/                  # Progressive autonomy — shadow → advisory → supervised
│   └── verification/              # CC-1 — is the verifier separate from the generator?
│
└── tests/                         # Unit and integration tests
    ├── agents/
    ├── teams/
    ├── tools/
    ├── boundaries/
    ├── metadata/
    └── stores/
```

---

## Key Design Decisions in the Structure

### 1. No Data Files — Only Code and Schemas

```
schemas/     ←  Database schema definitions (SQL, TQL) — these are CODE
scripts/    ←  Scripts that LOAD data into databases — no data stored here
```

The `scripts/` directory contains scripts that populate databases. The scripts themselves are code; the data goes into Postgres, Chroma, TypeDB, Event store, and MinIO. No JSON data files, no CSV dumps, no SQL data dumps in the repo.

### 2. First-Class Modules for CAWDP Principles

The four CAWDP infrastructure modules are top-level, not buried inside agents:

| Module | What it enforces | Where it lives |
|--------|-----------------|---------------|
| `identities/` | 5-class taxonomy, possibility orientation, 4 identity questions | Agent class boundaries defined once, imported everywhere |
| `boundaries/` | CC-4 Regime 3 enforcement, progressive autonomy | Database-level access control + autonomy state machine |
| `metadata/` | CC-3 epistemic metadata on every output | Pydantic models + automatic injection |
| `audit/` | CC-8 assured audit trail, trust ledger | 3-level trail + progressive autonomy tracking |

These are **infrastructure**, not agent configuration. Every agent imports from these modules. They can't be skipped because they're not in the agent's instructions — they're in the system's architecture.

### 3. Domain-Based Organization That Scales

Starting with 5 domains, scaling to 20. Each domain has the same structure:

```
specialists/{domain}/
    extractor.py      # Pulls data, never judges
    measurer.py       # Tracks metrics, never interprets
    assessor.py       # Evaluates, never finalizes

tools/{domain}/
    read.py           # Read-only queries (Extractor, Measurer)
    write.py          # Write to {domain}_agent schema
    introspect.py     # Schema introspection

schemas/postgres/
    {domain}_agent.sql   # Agent-managed schema for this domain
```

Adding a new domain means copying this pattern and filling in the specifics. The structure enforces consistency without requiring a template engine.

### 4. Orchestrators Are Separate From Specialists

```
agents/orchestrators/    # 4 orchestrators — human-facing, coordination
agents/specialists/      # Domain specialists — task-focused, bounded
```

Orchestrators and specialists are different agent classes with different authority boundaries. Keeping them in separate directories makes the architectural boundary visible in the file system.

### 5. Knowledge Goes Into Databases, Not Files

Dash has a `knowledge/` directory with JSON and SQL files. This project doesn't. Knowledge is loaded into Chroma (vectors) and TypeDB (graph) by `scripts/seed_knowledge.py`. The code that defines knowledge loading is in `scripts/`; the knowledge itself lives in the databases.

### 6. Cross-Domain Analysis Is a Tool, Not an Agent

```
tools/cross_domain/pattern_detector.py
```

The cross-domain analysis layer is a capability that orchestrators invoke, not a separate agent. This keeps the agent hierarchy clean (4 orchestrators, each with their specialists) while enabling cross-domain pattern detection.

---

## What's Not Here (Yet)

This structure supports the first 5 domains (Financial, Client, Strategy, Product, Knowledge/Learning). Adding the remaining 15 domains means adding the same pattern:

1. `specialists/{domain}/` — extractor, measurer, assessor
2. `tools/{domain}/` — read, write, introspect
3. `schemas/postgres/{domain}_agent.sql` — agent-managed schema
4. Add domain to the relevant team in `teams/`

The structure scales by replication, not by expanding a single file. Each domain is self-contained and can be developed independently.

---

## Database Schema Naming Convention

```
public                     ← Business data (read-only for agents)
shared                     ← Agent registry, audit trail, progressive autonomy
financial_agent            ← Financial domain agent-managed data
client_agent               ← Client domain agent-managed data
strategy_agent             ← Strategy domain agent-managed data
product_agent              ← Product domain agent-managed data
knowledge_agent            ← Knowledge/Learning agent-managed data
```

Each `{domain}_agent` schema follows the same CC-4 pattern from Dash: agents can read from `public` and write to their own schema. The `shared` schema stores cross-cutting concerns (agent registry, audit trail, trust ledger, progressive autonomy state).

This is the private schema pattern scaled across 5+ domains — Regime 3 enforcement at organizational scale.

---
