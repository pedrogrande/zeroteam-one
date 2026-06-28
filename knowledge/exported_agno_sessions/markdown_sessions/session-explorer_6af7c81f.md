# Session Explorer

| Field | Value |
|-------|-------|
| **Session** | `6af7c81f...` |
| **Type** | agent |
| **Agent** | Session Explorer |
| **User** | N/A |
| **Created** | 2026-04-27T05:23:10 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Session Explorer ✓ COMPLETED

*2026-04-27T05:23:09* · `glm-5.1:cloud` · `a89b9027...`

### Prompt

What topics did the agentic-expert sessions cover?

### Response

Based on my searches across the knowledge base, the Agentic Expert sessions cover a remarkably rich and interconnected set of topics. Here's a comprehensive synthesis:

---

# Topics Covered in Agentic Expert Sessions

## 1. 🏗️ Agent Design Principles Framework

This is the most foundational topic, spanning multiple sessions where Pete developed and iterated on a comprehensive framework for designing trustworthy agents.

- **Agent Design Principles v0.2** — reviewed, critiqued, and refined into **v0.3** with maturity levels (Operational 🟢, Emergent 🟡, Aspirational 🔴)

> From *Agentic Expert* session (2026-04, session `6dd7f450`)

Key principles developed across sessions include:
- **Two axes of excellence**: output fidelity *and* epistemic enrichment
- **Trustworthiness from structure, not identity**
- **Type collision** — the insight that LLMs encode 17+ distinct information types into a single output type (prose)
- **9-layer framework**: Purpose → Identity → Specification → Context → Trust → Safety → Ecosystem → Improvement → Human Enrichment
- **Articulation Agent** and **Exploration Agent** as new role archetypes
- **Reversibility-Novelty-Agency Matrix** for complementarity boundaries

---

## 2. 🔧 CAWDP (Complementarity-Driven Agentic Workflow Design Process)

CAWDP is Pete's methodology for designing agent workflows, and it was applied, tested, and refined extensively.

| Session | What Happened |
|---------|-------------|
| `5a8726ee` | CAWDP applied to the process of *creating agents with AI assistance* (meta-application) — 12 characteristics of the perfect process defined |
| `ef455daf` | CAWDP Phase 0 for agent creation |
| `929e2321` | CAWDP Phase 3: System Architecture |
| `ac216e6a` | **The magnum opus session (28 runs)** — CAWDP v2.1 applied to multiple real agent designs |
| `ab88d877` | CAWDP executive summary and strategy for releasing it to academics and industry |

Key CAWDP developments:
- Restructuring from original phases to a refined version (v2.1)
- Applied to 6+ concrete agent designs (Article Monitor, Expense Checker, Research Insight Miner, Watchman, etc.)
- Phase 0 (Target State Vision) emerged as essential
- Dual workstreams: Agent Creation + Process Improvement running in parallel
- Template architecture with 7 template types (Input, Output, Handoff, Verification, Decision, Feedback, Escalation)

---

## 3. 📊 Information Quality Framework

A major insight thread: **an agent's capability is entirely dependent on the quality of information it receives**.

> From *Agentic Expert* session (2026-04, session `ac216e6a`)

- **10 quality dimensions** defined: relevance, accuracy, completeness, recency, provenance, confidence, specificity, structure, sufficiency, consistency
- **Decomposability insight**: quality should be assessed *per unit*, not per document — a contract with 49 accurate clauses and 1 outdated one shouldn't get a single score
- **Operationalization roadmap**: assessment scales, threshold models, who assesses, when, what to do with scores

---

## 4. 🏛️ PRISM Ontology

**P**atterned **R**efraction of **I**ntelligence **S**ystems **M**odel — Pete's agent-native ontology.

> From *Agentic Expert* session (2026-04, session `5fd2f868`)

- **7 Dimensions**: Scopes, Actors, Entities, Relations, Events, Knowledge, Intentions
- **4 Cross-cutting Layers**: Epistemic, Governance, Temporal, Schema
- Every record in every dimension carries all four layer fields
- Implemented as a **TypeDB schema** (session `7f94dc13`)
- Connected to the decomposability insight and information quality framework (session `ac216e6a`, Run 28)

---

## 5. 🗣️ Plain English Taxonomy & Vocabulary

A crucial pivot: Pete realised the technical language was making the work inaccessible.

> From *Agentic Expert* session (2026-04, session `ac216e6a`)

- **Plain English taxonomy** written to be understandable by a 16-year-old
- **5-class agent taxonomy**: Gatherers, Measurers, Reviewers, Writers, Assemblers
- **10 "most dangerous terms"** — common English words with completely different meanings in agentic AI (Agent, Temperature, Inference, etc.)
- **Full jargon glossary** covering 8+ categories (The Agent Itself, How Agents Run, How They're Built, Working Together, Memory & Knowledge, Safety, Evaluation, Protocols)
- **Complete definition of "agent"** as a taxonomic classification with 6 essential attributes

---

## 6. 🤝 Agent-Native Organizations

What distinguishes agent-native from AI-augmented or AI-first organizations.

> From *Agentic Expert* session (2026-04, session `4088ed44`) — a team session

- **Four defining conditions**: allocation by complementarity, governance as kernel, information as typed artefacts, autonomy as earned progression
- **Ternary coordination model**: Human ↔ Agent ↔ System
- **Structural anatomy** of an agent-native org
- **Transition roadmap**, operational challenges, and industry disruption analysis

---

## 7. 🎯 Team & Swarm Design

Multiple sessions explored designing multi-agent teams for specific purposes.

| Session | Team/Swarm |
|---------|-----------|
| `ced6b6d1` | **Strategic Innovation Team** for Future's Edge — designing for cognitive diversity |
| `b90bfb3f` | **Generative Exploration Swarm** — 200+ exploration agents, 100+ convergence agents, 50+ synthesis agents with Novelty Intelligence Layer |
| `c6158c09` | **Opportunity Intelligence Swarm** — 4-layer architecture (Value Understanding → Opportunity Discovery → Alignment & Filtering → Action Architecture) |

---

## 8. 🏢 Concrete Agent Design Exercises

Multiple agents were designed end-to-end using CAWDP:

- **AI Article Monitor** — scrapes websites, checks for new AI articles, triggers webhooks
- **AI Article Analyser** — analyses article content (summary, sentiment, quality, author)
- **Research Insight Miner** — mines 500+ papers for novel insights
- **Expense Report Compliance Checker** — detailed CAWDP walk-through
- **Watchman Agent** — monitoring/surveillance agent
- **Project Coordinator** — agent managing other agents producing business outputs
- **Agent-Native Knowledge Base Ingestion Pipeline** — 16-agent roster with Extractors, Measurers, Assessors, Generators, Aggregators, Coordinators

> From *Agentic Expert* session (2026-04, session `ac216e6a`)

---

## 9. 🧠 Agent Strengths & Flip Sides

A systematic analysis of what agents are genuinely good at and what the hidden downsides are.

> From *Agentic Expert* session (2026-04, session `ac216e6a`)

- **8 performance strengths**: tirelessness, endurance, speed, scale, parallelism, availability, replicability, consistency of effort — each with a flip side
- **Behavioral strengths**: no ego, no fear, etc. — each with flip sides
- The insight that **the same quality that's a strength becomes a weakness if misunderstood**

---

## 10. 📋 Agent Specification Template

A structured template for specifying agents, applied to the Project Coordinator agent.

> From *Agentic Expert* session (2026-04, session `0e4a4724`)

Uses cognitive modes (IMAGINE, etc.) and follows the CAWDP framework structure.

---

## 11. 📖 Knowledge Object Type Taxonomy

15 atomic knowledge object types with distinct schemas, decay profiles, authority levels, and epistemic signatures.

> From *Agentic Expert* session (2026-04, session `b11ab884`)

The critical distinction: **a document is a container; a knowledge object is what lives inside it.** Type collision at the extraction layer.

---

## Cross-Cutting Themes

Several themes weave through *all* these sessions:

1. **Type collision** — the root problem that 17+ information types get flattened into prose, and how to resolve it structurally
2. **Complementarity** — humans and agents doing what each is best at, not just automating human tasks
3. **Trust through structure** — verification independence, authority boundaries, progressive autonomy
4. **Epistemic enrichment** — the second axis of excellence that most frameworks ignore
5. **ADHD-aware design** — designing systems that work *with* Pete's cognitive profile rather than against it
6. **Accessibility of language** — the persistent concern that brilliant work is inaccessible if people can't understand it

---
