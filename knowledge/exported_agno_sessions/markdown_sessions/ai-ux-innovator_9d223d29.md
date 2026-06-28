# AI UX Innovator

| Field | Value |
|-------|-------|
| **Session** | `9d223d29...` |
| **Type** | agent |
| **Agent** | AI UX Innovator |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-04T10:21:47 |
| **Runs** | 1 completed / 1 total |

## Run 1 — AI UX Innovator ✓ COMPLETED

*2026-05-04T10:21:47* · `glm-5.1:cloud` · `5e047705...`

### Prompt

below is the output from an ideation around a raw concept.

i'd like your thoughts on UIs for the single human interface agent. I see there being several viewports. The most interesting right now:

1. Desktop workspace for managing decision approvals and directing work
2. Chat tool (eg Telegram) that gives a contact point when the user is on the go

---
---
# Architecting a Small Business Agentic Operating System


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

-------
-------

### Response

Good. This is the right moment for UI thinking — you've got the architecture, now you need the human surface.

Let me start from one principle that changes everything:

**Desktop and chat are not the same app at different sizes. They're two different channels carrying two different signal types.**

Shannon's insight: the channel determines what signals can pass. Desktop carries high-bandwidth, complex signals (strategy, analysis, configuration). Chat carries low-bandwidth, urgent signals (decisions, flags, quick answers). Trying to send the same signal through both is type collision at the viewport layer.

---

## THE TWO MODES OF HUMAN ENGAGEMENT

Desktop = "I'm here to work on the business." You chose to sit down, open the screen, and focus. High cognitive capacity available. Time-rich.

Chat = "I'm living my life, but the business needs me." You're walking, waiting, between things. Low cognitive capacity. Time-poor. Seconds, not minutes.

These are fundamentally different human states. The UI should serve each state, not try to be the same thing in both places.

---

## VIEWPORT 1: THE DESKTOP WORKSPACE

### The Spatial Model

Build on the Accretive Workspace's five zones, but adapted for an agentic OS with 4 concurrent orchestrator streams.

```
┌──────────────────────────────────────────────────────────────┐
│  TRUST HORIZON — autonomy levels, trust trends, cost, last    │
│  override. Ambient. Like a car's fuel gauge.                  │
├────┬─────────────────────────────────────────────┬────────────┤
│    │                                             │            │
│ F  │                                             │  D E C I  │
│ O  │                                             │  S I O N  │
│ U  │          C A N V A S                        │  Q U E U  │
│ R  │                                             │  E        │
│    │   (adapts to what you're doing)              │            │
│ W  │   Lattice / Seedbed / Argument              │  Ranked   │
│ A  │   Decision detail / Configuration           │  by C×R   │
│ T  │                                             │            │
│ C  │                                             │            │
│ H  │                                             │            │
│ T  │                                             │            │
│ O  │                                             │            │
│ W  │                                             │            │
│ E  │                                             │            │
│ R  │                                             │            │
│ S  │                                             │            │
├────┴─────────────────────────────────────────────┴────────────┤
│  THE HELM — capture bar + ONE clear next step                │
└──────────────────────────────────────────────────────────────┘
```

### The Four Watchtowers (Left Rail)

The 4 orchestrators are NOT tabs. They're sensors — always-on indicators showing the state of each concern. You don't "go to" the Commercial Orchestrator. It tells YOU when it needs you.

Each orchestrator gets a compact zone (~60px high):

```
 Commercial    🟡 2 decisions waiting
 Growth        🟢 All clear
 Venture       🟢 1 idea captured
 Stewardship   🔴 Compliance deadline Friday
```

- **Name** (one word)
- **Status**: 🟢 calm / 🟡 brewing / 🔴 needs you now
- **One-line summary**: what's happening right now

Click to expand → see what's happening in that domain without leaving the workspace. The expanded view shows pending decisions, active specialists, recent flags.

**Key UX principle**: The watchtowers answer the question "Do I need to pay attention to anything?" at a glance. This is visibility as memory — you don't have to remember what's happening, the rail tells you.

### The Decision Queue (Right Rail)

This is where the Decision Presentation Pattern lives on desktop. Decisions arrive here, ranked by the C×R governor:

**Sorting rules:**
1. Hard-to-undo decisions rise to the top (reversibility is the primary sort)
2. Time-critical decisions rise to the top (urgency is secondary)
3. Low confidence + hard to undo = highest priority (the agent is unsure AND the stakes are high)

Each decision card:

```
┌─────────────────────────────────┐
│ 🔴 Commercial                  │
│                                 │
│ Approve $4,800 invoice for      │
│ Harding & Park                  │
│                                 │
│ 🎯 High confidence · Xero data  │
│ ⚠️ Hard to undo once approved  │
│ ⏰ Budget holder: you          │
│                                 │
│ [Approve] [Query] [Reject]      │
└─────────────────────────────────┘
```

- **Domain tag** (which orchestrator)
- **What needs deciding** (1 sentence, plain English)
- **Confidence + source** (epistemic metadata as visual signal, not footnote)
- **Reversibility** (how hard to undo — this is what determines priority)
- **Who's responsible** (why this reached you and not someone else)
- **2-4 action buttons** (Decision Presentation Pattern — never open questions)

### The Canvas (Center)

The canvas adapts to what you're doing, using the Accretive Workspace shapes:

| What you're doing | Shape | Why |
|---|---|---|
| Reviewing financial analysis | Lattice | See dependencies and connections |
| Exploring a strategy option | Seedbed | Plant ideas, see what grows |
| Working on a project | Argument | Linear flow, develop deliverables |
| Reviewing a decision in detail | Expanded decision view | Full context, evidence, metadata |

Click a decision card in the right rail → it expands into the canvas. You see full evidence, epistemic metadata, what the agents considered, what they're unsure about, and your options.

The canvas is the ONLY place you need to focus. Everything else (watchtowers, decision queue) is peripheral vision.

### The Trust Horizon (Top Strip)

Ambient system health. You don't actively read it. But you'd notice if something changed.

```
Commercial: Advisory ↑    Growth: Shadow →    Venture: Shadow    Stewardship: Supervised ↑
Cost today: $1.24    Last override: 2h ago (Financial Measurer)
```

Think car dashboard. You glance at it. Something red catches your eye. You don't study it.

### The Helm (Bottom Bar)

Two elements:
1. **Capture bar**: quick commands — "check client pipeline", "what's our MRR", "redirect this to Rifadh"
2. **Next step**: the ONE thing you should do next, if nothing else demands your attention

This is the ADHD design principle "one clear next step" made structural. The workspace always tells you what to do next. You never face a blank moment.

---

## VIEWPORT 2: THE CHAT INTERFACE

### The Core Principle

The chat is NOT a conversation. It's a **decision channel**.

You receive structured messages. You act on them. That's it.

This is fundamentally different from ChatGPT-in-Telegram or any "chat with your AI" tool. Those try to put a full conversational AI in your pocket. This puts **only what needs your judgment** in your pocket.

### Four Message Types

**1. Decision Message** — the core unit

```
🔴 [Commercial] Invoice #1842 overdue 14 days

Client: Harding & Park · Amount: $4,800
Confidence: High (direct from Xero)

What should I do?
[Send reminder] [Escalate] [Mark handled]
```

One decision. 2-4 buttons. Confidence shown. Action-oriented. Takes 5 seconds to read and decide.

**2. Flag Message** — something you should know

```
🟡 [Stewardship] Privacy policy review due in 5 days

Confidence: High · Autonomy: Shadow (I can't act)

[Noted ✓] [Open on desktop]
```

No action needed. Just awareness. "Open on desktop" queues it for when you sit down.

**3. Status Message** — answer to a question you asked

```
[Financial] MRR: $12,400

↑ 3% from last month · Updated today · Xero data

[Anything else?]
```

Typed answer. Not a wall of text. Confidence embedded in the source line.

**4. Escalation Message** — the agent can't handle this

```
🔴 [Growth] Response from Chen Legal doesn't fit any pattern

It might be a complaint, a negotiation, or a request
for information. I don't want to guess wrong.

[Show me] [Queue for desktop]
```

This is the "doubt defaults to human" principle as a message type. The agent explicitly says "I can't handle this" rather than guessing.

### The Interruption Governor

This is the most important design decision for the chat interface: **what deserves to interrupt someone who is living their life?**

The C×R matrix answers this:

| Reversibility | Confidence | Reaches phone? |
|---|---|---|
| Hard to undo | High | **Yes** — decision message |
| Hard to undo | Low | **Yes** — with extra caution flags |
| Easy to undo | High | No — agent handles it, log on desktop |
| Easy to undo | Low | No — agent flags it, you see on desktop |

**Always reaches mobile:**
- Any boundary violation (agent stepped outside its authority)
- Any cost budget exceeded
- Any autonomy level change (agent earned promotion or needs demotion)
- Any escalation (agent can't handle something)

**Never reaches mobile:**
- Routine confirmations (easy to undo, high confidence)
- Status updates (no action needed)
- Complex analysis (needs the desktop canvas)
- Anything the agent is authorized to handle at its current autonomy level

### Configuring the Governor (Desktop Sets Up Mobile)

The desktop workspace includes an "Interruption Rules" panel:

```
┌──────────────────────────────────────────────┐
│  WHAT REACHES YOUR PHONE                      │
│                                              │
│  Commercial                                   │
│  ├─ Approvals over: $2,000                   │
│  ├─ Invoice disputes: always                 │
│  └─ Routine payments: never                   │
│                                              │
│  Growth                                      │
│  ├─ Client escalations: always               │
│  └─ Routine follow-ups: never                 │
│                                              │
│  Stewardship                                 │
│  ├─ Compliance deadlines: always              │
│  ├─ Risk flags: always                        │
│  └─ Security alerts: always                  │
│                                              │
│  Venture                                     │
│  └─ Everything: desktop only (I'll check)     │
│                                              │
│  ALWAYS: boundary violations, cost overruns, │
│  autonomy changes, escalations                │
└──────────────────────────────────────────────┘
```

The human configures what reaches their phone based on what they care about most. This is the desktop SETTING UP how the chat works — governance, not just settings.

---

## THE BRIDGE BETWEEN VIEWPORTS

Desktop and chat are not independent. They're two ends of a bridge.

**Chat → Desktop:**
- Actions you take on mobile sync to desktop (decision + reasoning captured as decision archaeology)
- "Open on desktop" queues items for your next desktop session
- If you say "Show me" on a complex item, it queues the full context for desktop

**Desktop → Chat:**
- Desktop configures what reaches chat (interruption rules, delegation rules, autonomy levels)
- If something on desktop is urgent and you step away, it can push to chat
- Desktop shows you what happened on chat while you were away ("3 decisions approved on mobile: 2 approved, 1 queued")

**The sync point:** Every action — on either viewport — goes to the same audit trail. The Trust Ledger doesn't care which viewport you used. It records what you decided, when, and why.

---

## THE VOICE OF THE SYSTEM

On desktop, the system is a **workspace** — you look at it. On chat, the system is a **contact** — it talks to you.

This changes the voice:

| Aspect | Desktop | Chat |
|---|---|---|
| Tone | Neutral, professional | Brief, warm |
| Detail | Full context available | Only what's needed to decide |
| Agent names | Domain + class ("Financial Measurer") | Domain only ("[Commercial]") |
| Technical terms | Appropriate | None |
| What you see | Everything available | Only what needs you |

**Chat contact name**: the business name (e.g., "Future's Edge"), not "System" or "AgenticOS". It's YOUR business contacting you, not a machine.

**Message length**: never more than 5 lines for the human to read before seeing action buttons. If it needs more than 5 lines, it needs the desktop.

---

## WHAT'S GENUINELY NEW HERE

Three things I haven't seen in any existing product:

**1. The C×R Notification Governor.** No system uses reversibility × confidence to determine what interrupts the human. Current systems use either "notify everything" (notification fatigue) or "let the user configure categories" (too much work, too abstract). The C×R matrix gives the system a principled way to decide what deserves human attention and what doesn't. And the human configures the thresholds on desktop — governance, not guessing.

**2. Two-channel architecture with different signal types.** Every existing approach is "responsive design" — same interface, different sizes. This is type collision at the viewport layer. Desktop and chat should carry fundamentally different information types, optimized for fundamentally different cognitive states. The bridge between them is not "sync" but "governance rules for interruption."

**3. Decision Presentation Pattern in chat.** Every message is a typed decision with 2-4 action buttons. The human NEVER types free-form responses in chat (that's what the desktop capture bar is for). The chat is a decision channel, not a conversation channel. This prevents the "wall of text" problem on mobile and keeps interactions to 5-second decisions.

---

## BUILD ORDER

1. **Chat first.** Counter-intuitive but right. The chat interface is simpler to build (4 message types, inline buttons, a webhook). It proves the C×R governor works. It proves the Decision Presentation Pattern works on mobile. And it delivers value immediately — the human can approve decisions from their phone on day one.

2. **Desktop decision queue second.** Right rail + expanded decision view in canvas. This is the minimum viable desktop — not the full workspace, just the decision workflow.

3. **Watchtowers + Trust Horizon third.** Ambient awareness adds the "at a glance" picture.

4. **Full canvas shapes fourth.** The Accretive Workspace shapes for strategy, exploration, and project work.

Start with the decision channel. Prove that the system can surface the right decisions at the right time in the right place. Then build the workspace around it.

---
