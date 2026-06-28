# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `f63f7f68...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-06-15T22:48:10 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-06-15T22:48:10* · `glm-5.1:cloud` · `8975ea10...`

### Prompt

Have we talked about 'task contracts'? If so, remind me about them

### Response

Yes — we've discussed task contracts extensively, across several interconnected contexts. Here's the synthesis:

## Task Contracts in CAWDP

### Core Concept: The Contract IS the Specification

The foundational insight is that the **8 contract primitives** (later expanded to **10** with Identity and Knowledge added in P8 Contract Formalization) govern tasks for **ALL actor types** (Human/Agent/System). **ONE CONTRACT PER TASK** — not one per actor. The contract is the enforcement boundary: binary, deterministic, actor-agnostic.

### The 10 Contract Primitives

| # | Primitive | What It Does |
|---|-----------|-------------|
| 1 | **Contract** | The membrane — binary pass/fail for the task |
| 2 | **Principal** | Who delegated this task (human IS the authority source for certain actions) |
| 3 | **Schema** | Typed input/output validation — non-compliant output → REVERT for ALL actors |
| 4 | **Guard** | Authority boundaries — violation → REVERT for ALL actors |
| 5 | **Budget** | Cost ceiling — exhausted → HALT for ALL actors |
| 6 | **Invocation** | How the task is triggered (can include PAUSE/RESUME for human actors) |
| 7 | **Revert** | What happens when output is rejected — binary rejection, no scaffolding at the gate |
| 8 | **Event** | Event emission — same types regardless of actor enables cross-actor comparison |
| 9 | **Identity** | *(Added in P8)* — Agent identity, class, orientation, never-rules |
| 10 | **Knowledge** | *(Added in P8)* — Context boundaries, information the task can/cannot access |

### Three Enforcement Regimes

The critical insight: the contract itself is the **same** for all actors. But there are **two separate layers**:

- **CONTRACT layer** = enforcement boundary — binary, deterministic, actor-agnostic. No exceptions.
- **SYSTEM layer** = support layer — adaptive, actor-aware, operating PRE-CONTRACT and POST-REVERT.

This means:
- Pre-submission support (schema preview, templates, incremental validation) helps humans produce compliant output **before** the contract validates
- Post-revert support (capturing rejected output as a separate artifact) is OUTSIDE the contract, not a contract modification
- The contract validates the same way for everyone — no scaffolding at the gate

### Per-Task Contract Fields (from Project Initiation Workflow)

Applied concretely, each task contract includes:

- **Task identity** — what this task is
- **Phase** — which workflow phase
- **Dependencies** — what must complete first
- **Assignment** — Human/Agent/System/Collaborative
- **Authority boundary** — what this role CAN decide
- **Never-rules** — what this role NEVER does (tied to failure modes)
- **Effort estimate** — range + confidence, never single-point
- **Priority score** — Impact × Urgency × Dependency weight
- **Success criteria** — measurable completion definition
- **State machine** — task lifecycle states
- **Epistemic metadata** — CC-3 fields on every output

### Contract Depth Scales by Agent Class

Not every task needs all 10 primitives:
- **Extractors**: 2/10 (Contract + Schema) — simple extraction contracts
- **Aggregators**: 10/10 + cross-agent integration — full contracts with all enforcement

### The 10×10 Mapping Matrix

P8 Contract Formalization created an explicit mapping between the 10 specification sections (for humans, meaning space) and the 10 contract primitives (for systems, enforcement space). Every specification element traces to contract primitives, and every contract primitive traces back to specification sections. This resolves the **5th layer of type collision** (design-to-enforcement boundary).

### Key Connections to Other Frameworks

- **Contract-Native DAO**: Every task is a contract invocation. CAWDP determines what those contracts should be. The DAO runs contracts; CAWDP designs them.
- **Iterative Artefact-Driven Development**: Each iteration is a contract — input artefacts as pre-conditions, output artefacts as post-conditions, quality gates as contract guards.
- **CC-4 Information Boundaries**: Contracts enforce information boundaries at Regime 3 (prevent by design). The contract defines what the task CAN access, not what it's asked not to access.
- **CC-7 Cost Budgets**: Budget primitives with `halt_on_budget_exhaustion` — the missing primitive that prevents cost overruns structurally.
- **Quasi-smart contracts**: All attributes of a smart contract but NOT deployed to blockchain. Deterministic, self-executing, composability, guards, gas metering → applied to agentic system governance without requiring blockchain infrastructure.

### The Deepest Insight

The contract IS the specification — unifying design specification and enforcement mechanism into a **single deployable artifact** eliminates the class of governance failures where spec and enforcement diverge. This is the same insight that made smart contracts revolutionary in blockchain, now applied to agentic systems.

Want me to dive deeper into any specific aspect — the enforcement regimes, the 10×10 mapping matrix, the contract-native DAO application, or how task contracts connect to the iterative artefact-driven development model?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-06-15T23:29:15* · `glm-5.1:cloud` · `cfec02eb...`

### Prompt

do you remember us talking about the different contracts associated with a task like a handover contract? I forget the others

### Response

Yes! The **7 template types** from CAWDP Phase 3 (System Architecture). These are the distinct contractual artefacts that structure every task's lifecycle:

## The 7 Contract Types

| # | Type | Plain English | What It Governs |
|---|------|--------------|-----------------|
| 1 | **Input** | "What goes in" | What data, context, and prerequisites a task needs before it can start |
| 2 | **Output** | "What comes out" | What the task must produce — typed schemas, quality criteria, epistemic metadata |
| 3 | **Handoff** | "How work passes" | How work transfers between actors/stages — who receives what, in what format, with what authority |
| 4 | **Verification** | "How you check it" | How outputs are verified — structural/semantic/authority checks (CC-1 verification independence) |
| 5 | **Decision** | "How you decide" | How decisions are made and recorded — who decides, what options were considered, what reasoning |
| 6 | **Feedback** | "How you improve it" | How feedback flows back — from human review, from downstream consumers, from monitoring |
| 7 | **Escalation** | "How you raise the alarm" | How issues get escalated — trigger conditions, escalation path, responsible party, recovery |

## Why These Are Separate (Not One Big Contract)

Each type solves a **different type collision problem**:

- **Input/Output** = type collision at the data boundary (what goes in vs what comes out — different schemas, different quality requirements)
- **Handoff** = type collision at the actor boundary (human produces X, agent consumes Y — different representations, different authority)
- **Verification** = type collision at the trust boundary (creator says "done," verifier needs to check independently — CC-1)
- **Decision** = type collision at the judgment boundary (multiple options with different trade-offs need structured capture)
- **Feedback** = type collision at the learning boundary (qualitative reactions need to become typed improvement signals)
- **Escalation** = type collision at the failure boundary (different failure modes need different response paths)

## How They Connect to the Task Lifecycle

A task doesn't need all 7 at all times. The pattern is:

```
Input Contract → (task executes) → Output Contract
                                      ↓
                              Verification Contract
                                      ↓
                              Handoff Contract → (next task)
                                      ↓
                              Decision Contract (if human gate)
                                      ↓
                              Feedback Contract (if issues found)
                                      ↓
                              Escalation Contract (if unresolvable)
```

## Contract Depth Varies by Task

Not every task needs every contract type:
- **Simple Extractor tasks**: Input + Output only
- **Collaborative tasks**: All 7 — handoffs are complex, verification is critical, decisions need human gates
- **Human-only tasks**: Simplified — Decision is the primary contract, Input/Output support it

## In the Professional Services Toolkit

These were translated for Sarah Chen's world:
- **Handoff** → "Handoff Contract Templates (quasi-smart contracts in their language)"
- **Verification** → "Verification Protocol Templates (3-level: structural/semantic/authority)"
- **Escalation** → "What happens when it fails" in the Failure & Recovery Register

## Key Design Principle

The handoff contract is the **most architecturally important** of the 7 because it's where type collision is most acute — the producing actor and consuming actor often have fundamentally different representations, authority levels, and quality requirements. The handoff contract bridges these differences explicitly rather than assuming both sides "just understand" the transfer.

Want me to dive deeper into any specific contract type — particularly the handoff contract structure?

---
