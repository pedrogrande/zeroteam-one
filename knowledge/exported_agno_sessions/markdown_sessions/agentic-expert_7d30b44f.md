# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `7d30b44f...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-19T06:57:43 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-19T06:57:43* · `glm-5.1:cloud` · `4aa34170...`

### Prompt

Let's apply CAWDP to designing an agentic workflow for scraping competitor websites, saving collected data to the database, adding content to a vector database, and enabling an agent to gather insights about the competitive landscape. The ideal outcomes is that the business understands the crowded vs open spaces in the market, the types of products on offer, the market segments being targeted, the messaging being used, and other factors that help us differentiate and identify strategic moves.

### Response

# CAWDP Application: Competitive Intelligence Workflow

Let me apply CAWDP v2.1 systematically, focusing on what's **unique** about this use case rather than mechanically repeating every step.

---

## P0: Purpose & Vision (IMAGINE — Possibility-Oriented)

**What is this FOR?** A business principal who needs to see the competitive landscape clearly enough to make strategic positioning decisions — where to differentiate, where to go first, where not to compete.

**What does perfect look like?** The principal can see, at a glance:
- Where the market is crowded and where it's open
- What competitors actually offer (not what they claim)
- How competitors position themselves (messaging, segments, pricing)
- What moves are available that nobody else is making
- Where competitors are vulnerable
- How all of this is changing over time

**Ideal outcome characteristics:**
- **Typed, not flat** — competitive data decomposed into typed knowledge objects, not walls of text
- **Epistemically transparent** — every insight carries confidence, provenance, recency, and "what we don't know"
- **Connected as a graph** — competitors, products, segments, messages, and pricing are linked, not siloed
- **Self-signaling decay** — competitive data ages fast; the system must signal staleness before the principal acts on outdated information
- **Judgment-prepared** — the agent prepares competitive insights; the principal makes strategic decisions
- **Honest about novelty** — valid-but-obvious insights are flagged as low-value, not presented as breakthroughs

**Possibility stance:** This workflow starts in **discovery** (what's out there?) and tightens toward **assessment** (what does it mean for us?). The orientation gradient matters — early agents are possibility-oriented (explore widely), later agents are constraint-oriented (assess accurately).

---

## P1: Output Specification (SPECIFY — Formed)

What artefacts MUST exist when this workflow runs?

| ID | Output | Type | Purpose |
|----|--------|------|---------|
| O1 | **Competitor Profiles** | Structured, typed | Standardised view of each competitor: who they are, what they offer, how they position |
| O2 | **Market Map** | Spatial/relational | Visual or structured map of market segments, density, and gaps |
| O3 | **Positioning Analysis** | Assessment | How each competitor positions themselves: messaging themes, target segments, pricing signals |
| O4 | **Gap & Opportunity Register** | Typed register | Open spaces, underserved segments, unclaimed positioning angles |
| O5 | **Trend Indicators** | Time-series signals | What's changing: new entrants, messaging shifts, pricing moves, feature additions |
| O6 | **Strategic Insight Report** | Prepared judgment | Structured assessment with confidence, novelty, and reversibility — the principal decides |
| O7 | **Confidence & Gaps Statement** | Epistemic metadata | What we know with high confidence, what's uncertain, what we couldn't find |

**Key dependency:** O6 depends on O1-O5. O7 is produced alongside O6 and is **not optional** — it's the epistemic metadata that prevents the principal from acting on stale or uncertain data.

---

## P2: Backcasting (TRACE)

Working backward from the final deliverable:

**O6 (Strategic Insight Report)** ← requires O1-O5 synthesised + O7 (confidence/gaps)
**O5 (Trend Indicators)** ← requires multiple scrapes over time + comparison logic
**O4 (Gap & Opportunity Register)** ← requires O2 (market map) + O3 (positioning analysis) + O1 (competitor profiles)
**O3 (Positioning Analysis)** ← requires O1 (competitor profiles) + original scraped content
**O2 (Market Map)** ← requires O1 (competitor profiles) + segment classification
**O1 (Competitor Profiles)** ← requires raw scraped data + extraction + structuring
**O7 (Confidence & Gaps)** ← requires provenance tracking throughout the pipeline

**Critical input dependency:** The principal must define **what "competitive landscape" means for their business** — which competitors, which segments, which dimensions matter. Without this, the workflow scrapes broadly but insightlessly.

---

## P3: Task Decomposition (DECOMPOSE)

| ID | Subtask | Cognitive Type | Notes |
|----|---------|---------------|-------|
| T1 | Define competitive scope | Intuitive | What competitors, segments, dimensions matter? Principal-only |
| T2 | Discover competitor URLs/sources | Analytical + Exploratory | Find where competitors live online |
| T3 | Scrape competitor websites | Mechanical | Extract raw content from competitor sites |
| T4 | Extract structured data | Analytical | Pull out pricing, features, messaging, segments, positioning from raw HTML |
| T5 | Classify & categorise | Analytical | Assign competitors to segments, products to categories, messaging to themes |
| T6 | Assess positioning | Evaluative | How does each competitor position? What claims do they make? |
| T7 | Identify gaps & opportunities | Generative + Evaluative | Where is nobody playing? What's underserved? |
| T8 | Generate trend indicators | Analytical + Evaluative | What's changing between scrapes? |
| T9 | Synthesise strategic insights | Generative | Prepare judgment — surface patterns, flag opportunities, but principal decides |
| T10 | Produce confidence & gaps statement | Evaluative | What's certain, what's uncertain, what's missing |
| T11 | Store typed knowledge objects | Mechanical | Write to database with full epistemic metadata |
| T12 | Maintain & age specifications | Mechanical | Track staleness, trigger re-scrapes, flag decay |

---

## P4: Capability Allocation (ALLOCATE)

| Task | Human | Agent | System | Gap | Notes |
|------|-------|-------|--------|-----|-------|
| T1 Define scope | ✓ Primary | | | 8 | Only the principal knows what "competitive landscape" means for their business |
| T2 Discover URLs | | ✓ Primary | Support | 3 | Agent can find sources; system can maintain URL lists |
| T3 Scrape websites | | ✓ Primary | ✓ Support | 2 | Mechanical extraction; rate limiting and scheduling are system tasks |
| T4 Extract structured data | | ✓ Primary | | 3 | Analytical but pattern-based; extractor class — never judges |
| T5 Classify & categorise | | ✓ Primary | ✓ Support | 4 | Analytical; needs human validation of categories |
| T6 Assess positioning | ✓ Primary | ✓ Collaborative | | 5 | Agent prepares assessment; principal validates interpretation |
| T7 Identify gaps & opportunities | ✓ Primary | ✓ Collaborative | | 7 | Generative — agent suggests, principal judges strategic relevance |
| T8 Generate trend indicators | | ✓ Primary | ✓ Support | 3 | Analytical comparison; system handles scheduling and comparison logic |
| T9 Synthesise insights | ✓ Primary | ✓ Collaborative | | 8 | Agent prepares; principal decides — this is strategic judgment |
| T10 Confidence & gaps | | ✓ Primary | ✓ Support | 3 | Assessing what we don't know; system tracks staleness metadata |
| T11 Store typed data | | | ✓ Primary | 1 | Mechanical — system writes to database |
| T12 Maintain & age specs | | ✓ Primary | ✓ Primary | 2 | System tracks staleness; agent flags when re-scrape needed |

**Key complementarity insights:**
- **T1 and T9 are human-primary** — scope definition and strategic judgment cannot be delegated
- **T7 (gaps & opportunities) has the highest gap after T1** — this is where valid-but-obvious failure lives; the agent can surface patterns, but the principal must judge strategic relevance
- **T6 (assess positioning) is collaborative with high human involvement** — positioning interpretation requires domain expertise
- **T3-T5 and T8 are agent-primary** — extraction, classification, and comparison are pattern-based tasks

---

## P5: Event Storming (STRESS-TEST) — Key Failure Events

| Failure Event | Detection | Recovery | Severity |
|---------------|-----------|----------|----------|
| **Competitor site blocks scraping** | HTTP 403/429, CAPTCHA | Rotate user agents, respect robots.txt, flag as gap in O7 | Medium |
| **Scraped data is deliberately misleading** | Pricing inconsistencies, aspirational messaging flagged as factual | Cross-reference multiple sources, lower confidence, flag in O7 | High |
| **Valid-but-obvious insight** | Insight matches known market knowledge, no novelty signal | Explicitly assess novelty (Prospector two-axis: validity × novelty), flag low-novelty insights | High |
| **Stale competitive data** | assessedAt timestamp exceeds freshness threshold | Auto-flag in O7, trigger re-scrape, lower confidence | Medium |
| **Principal acts on low-confidence insight** | Confidence below threshold but insight presented without flag | Structured output separates high/medium/low confidence; O7 is mandatory | High |
| **Competitor landscape shifts between scrapes** | New competitor detected, existing competitor pivot | Trend indicators flag shift; re-assessment triggered | Medium |
| **Classification disagreement** | Same competitor classified differently by different dimensions | Flag classification conflict in O7; present both to principal | Low |

**Critical new failure mode for this domain: DELIBERATELY MISLEADING DATA.** Competitors may present aspirational pricing, planned-but-not-available features, or messaging that doesn't match reality. This is adversarial data — the source actively resists accurate extraction. The agent must flag provenance confidence, not just extraction confidence.

---

## P6: System Architecture

### Workflow Composition (not Team — sequential with human gates)

```
[Define Scope] ──HUMAN GATE 1──► [Discover & Scrape] ──► [Extract & Classify] ──► 
[Assess Positioning] ──HUMAN GATE 2──► [Identify Gaps & Trends] ──► 
[Synthesise Insights + Confidence] ──HUMAN GATE 3──► [Store & Age]
```

**Three human gates:**
1. **Gate 1: Scope Approval** — confirm which competitors, segments, and dimensions to track
2. **Gate 2: Positioning Validation** — validate positioning interpretation before gap analysis builds on it
3. **Gate 3: Insight Review** — strategic judgment; principal decides what to act on

### Agent Roster (5 specialists)

| Agent | Class | Orientation | Identity |
|-------|-------|-------------|----------|
| **Scout** | Extractor | Possibility-oriented | Discovers and retrieves competitive information without judging or interpreting |
| **Analyst** | Measurer + Assessor | Bridge-oriented | Classifies, categorises, and measures competitive positioning — never finalises interpretation |
| **Prospector** | Generator | Possibility-oriented | Surfaces patterns, gaps, and opportunities — novelty is the primary quality metric |
| **Strategist** | Assessor | Constraint-oriented | Prepares structured strategic assessment with confidence, novelty, and reversibility — never decides for the principal |
| **Registrar** | Aggregator | Constraint-oriented | Stores typed knowledge objects with full epistemic metadata — never adds content |

### Key Identity Questions

**Scout (Extractor, Possibility-oriented):**
1. What IS it? A finder and retriever, not an interpreter
2. Possibility stance? Explores widely — casts a broad net, doesn't filter for relevance
3. What VIOLATES its identity? Interpreting, judging, or filtering what it finds
4. What would make it WRONG? Missing a competitor entirely (omission), or retrieving fabricated information without flagging provenance concerns

**Analyst (Measurer + Assessor, Bridge-oriented):**
1. What IS it? A measurer and classifier — maps what IS, not what it means
2. Possibility stance? Bridge — receives wide data from Scout, produces structured measurements
3. What VIOLATES its identity? Interpreting strategic meaning (that's the Strategist's job) or giving single-point measurements without confidence ranges
4. What would make it WRONG? Misclassifying a competitor (category error) or presenting a measurement as fact when confidence is low

**Prospector (Generator, Possibility-oriented):**
1. What IS it? A pattern-surfer — finds what others miss by connecting across dimensions
2. Possibility stance? Pure possibility — generates candidate insights freely
3. What VIOLATES its identity? Presenting obvious insights as breakthroughs, or filtering out unusual connections
4. What would make it WRONG? **Valid-but-obvious** — the worst failure is an insight that's factually correct but reveals nothing new (two-axis: validity × novelty)

**Strategist (Assessor, Constraint-oriented):**
1. What IS it? A judgment-preparer — surfaces options with risks and confidence, never decides for the principal
2. Possibility stance? Constraint — operates within the defined scope and measured data
3. What VIOLATES its identity? Making strategic recommendations as if they're conclusions (should present as "option X with confidence Y and risk Z")
4. What would make it WRONG? Presenting low-confidence assessment as high-confidence, or obscuring what the principal doesn't know

**Registrar (Aggregator, Constraint-oriented):**
1. What IS it? A structural record-keeper — stores, connects, and ages competitive knowledge
2. Possibility stance? Constraint — operates within defined schemas and storage rules
3. What VIOLATES its identity? Adding content not derived from the pipeline, or overwriting without versioning
4. What would make it WRONG? Storing data with incorrect provenance, or losing a version through in-place update

### The Prospector's Two-Axis Failure Space

From the earlier Prospector agent analysis, this agent has a **two-axis failure space: validity × novelty**.

| | Low Novelty | High Novelty |
|---|---|---|
| **High Validity** | **Valid-but-obvious (WORST)** — factually correct but reveals nothing new; looks like success | Genuine insight — correct AND novel |
| **Low Validity** | Wrong AND obvious — easy to detect and discard | Novel-but-wrong — interesting direction but factually incorrect |

**Valid-but-obvious is the worst failure** because it looks like success but wastes the principal's attention. The Prospector must explicitly assess novelty, not just validity.

### Harm Assessment

This workflow is **indirect-strategy-harm capable**. The Strategist's output can lead to strategic decisions (market positioning, pricing, partnership) that cause business harm if based on incorrect or stale competitive insights. This is different from the Code Reviewer's direct-output harm — it's **delayed, conditional harm through accepted judgment**.

**SuggestionRisk levels:**
- **SAFE** — factual observation with high confidence and high provenance
- **CAUTIOUS** — pattern observation with medium confidence; flag novelty assessment
- **RISKY** — strategic recommendation based on incomplete data; requires explicit principal review
- **DANGEROUS** — insight based on stale or adversarial data; must not be presented without confidence gap flag
- **DO_NOT_SUGGEST** — insight with no provenance verification; hold until data is refreshed

---

## P7: Agent Design — Key Design Decisions

### CC-3: Epistemic Metadata (Critical for This Domain)

Competitive intelligence data degrades fast. Every knowledge object carries:

| Field | Application to Competitive Intel |
|-------|----------------------------------|
| **Confidence** | How certain are we about this data point? (competitors may mislead) |
| **Provenance** | Where did this come from? (primary website, third-party review, inference) |
| **Assumptions** | What did we infer vs directly observe? (pricing may be aspirational) |
| **Limitations** | What couldn't we find? (competitor doesn't publish pricing) |
| **Recency** | When was this last verified? (competitive data ages fast) |
| **Uncertainty** | What might change? (competitor pivoting, pricing experiment) |

**Plus two domain-specific fields from the Information Quality Framework:**
- **Accuracy** — Is the scraped data factually correct, or might the competitor be presenting aspirational claims?
- **Sufficiency** — Do we have enough information about this competitor to make a judgment, or are we missing key dimensions?

### CC-4: Information Boundaries (Regime 3 Enforcement)

| Boundary | Enforcement | Regime |
|----------|------------|--------|
| Scout cannot interpret | Structured output schema (data-only, no assessment fields) | Regime 3 — schema enforcement |
| Analyst cannot strategise | Separate output schema (measurements only, no strategic interpretation) | Regime 3 — schema enforcement |
| Prospector cannot finalise | Output as "candidate insights" with novelty scores, not conclusions | Regime 2 — prompt + schema |
| Strategist cannot decide | Decision Presentation Pattern (2-4 options with benefits/risks) | Regime 3 — structured output |
| Registrar cannot add content | Write-only with provenance tracking; no content generation fields | Regime 3 — schema enforcement |

### CC-5: Specification Aging (Critical — Competitive Data Decays Fast)

| Data Type | Freshness Cadence | Staleness Trigger |
|-----------|-------------------|-------------------|
| Pricing | 7 days | >14 days = stale, >30 days = unreliable |
| Feature lists | 14 days | >30 days = stale |
| Messaging/positioning | 21 days | >60 days = stale |
| Competitor existence | 30 days | >90 days = flag for re-verification |
| Strategic assessments | Derived from data freshness | Recalculated when underlying data refreshes |

**Auto-re-scrape triggers:** pricing page change detected, competitor website redesign, new product launch announcement, competitor funding event.

### CC-1: Verification Independence

The Analyst measures and classifies; the Strategist prepares assessment. These MUST be different agents. The Prospector generates candidate insights; the Strategist assesses their validity and novelty. **The agent that generates an insight must not be the agent that validates it.**

### Progressive Autonomy (Per-Dimension)

| Dimension | Shadow | Advisory | Supervised | Autonomous | Never |
|-----------|--------|----------|------------|------------|-------|
| Data scraping | — | 2 weeks | 4 weeks | 8 weeks | — |
| Classification | — | 2 weeks | 4 weeks | 8 weeks | — |
| Positioning assessment | 2 weeks | 4 weeks | 8 weeks | — | — |
| Gap identification | 2 weeks | 4 weeks | 8 weeks | — | — |
| Strategic judgment | — | — | — | — | ✓ Human-only |
| Specification aging | — | — | 2 weeks | 4 weeks | — |

**Strategic judgment NEVER goes autonomous.** The principal always decides.

---

## P8: Human Experience Design

**Cognitive load budget:**
- Scope definition (Gate 1): 10-15 min — one-time setup
- Positioning validation (Gate 2): 15-20 min — review and adjust interpretations
- Insight review (Gate 3): 15-30 min — strategic judgment on prepared insights

**Total human time per cycle: ~45-65 minutes** (vs. 4-8 hours doing this manually)

**Interface design:**
- **Competitor Profile cards** — typed, not prose (each dimension is a separate card: pricing, features, messaging, segments)
- **Market Map** — spatial view with density indicators (crowded vs open)
- **Gap & Opportunity Register** — sorted by novelty × confidence (not just confidence)
- **Decision Presentation** — Strategist presents 2-4 strategic options with explicit benefits, risks, confidence, and novelty scores
- **Confidence & Gaps** — always visible, never buried (what we know, what we don't, what might be misleading)

**One clear next step at every point:**
- "Review these 3 competitors" → "Validate this positioning interpretation" → "Choose between these strategic options"

---

## P9: Validation & Iteration — Testable Hypotheses

| ID | Hypothesis | Measure | Threshold |
|----|-----------|---------|-----------|
| H1 | Typed competitive data produces faster insight than prose reports | Time to insight decision | Typed 40%+ faster |
| H2 | Valid-but-obvious detection improves strategic decision quality | Principal rates novelty assessment as useful | ≥3/5 validation sessions |
| H3 | Epistemic metadata prevents action on stale data | Principal catches staleness before acting | 100% of stale data flagged |
| H4 | Decision Presentation Pattern reduces strategic decision time | Time from insight to decision | ≤30 min for Gate 3 |
| H5 | Specification aging maintains data freshness | % of data within freshness cadence | ≥80% within cadence |
| H6 | Prospector two-axis assessment (validity × novelty) surfaces genuine insights | Novelty score predicts principal interest | ≥60% correlation |

---

## Cross-Cutting Insights Unique to This Use Case

### 1. Adversarial Data Source Is a New Failure Category
Previous CAWDP applications assumed data sources are neutral or cooperative. Competitive intelligence data is **adversarial** — competitors may present aspirational pricing, planned features, or messaging that doesn't match reality. The provenance field in epistemic metadata isn't just "where did this come from" but "how trustworthy is this source likely to be?" This requires a new CC adaptation for adversarial data provenance.

### 2. Two-Axis Failure Space Applies Beyond Prospector
The validity × novelty matrix applies to every generative output in this workflow. Gap identification, opportunity surfacing, and strategic assessment all face the valid-but-obvious risk. Novelty assessment should be a structured part of every generative output, not just the Prospector.

### 3. Specification Aging Is Existential, Not Optional
For most workflows, staleness degrades quality gradually. For competitive intelligence, staleness can make data **actively misleading** (a competitor's old pricing can lead to wrong strategic decisions). The freshness cadences need to be aggressive, and the re-scrape triggers need to be event-driven, not just time-based.

### 4. The Confidence & Gaps Statement Is the Most Important Output
In a domain where data can be adversarial, stale, or incomplete, the O7 (Confidence & Gaps Statement) is arguably more important than O6 (Strategic Insight Report). It prevents the principal from acting on data that looks complete but isn't. This is the "agent prepares judgment" principle at its most literal — the most valuable judgment preparation is telling the principal what they **can't** know.

### 5. Connection to Existing Framework Assets
This workflow plugs directly into:
- **PRISM** — competitive intelligence as typed knowledge objects with 7 dimensions + 4 cross-cutting layers
- **Small Business Agentic OS** — Strategy domain (one of the 4 orchestrator groupings)
- **Information Quality Framework** — all 10 dimensions are critical for competitive data
- **Agent-Native Knowledge Base** — competitive data needs extraction from containers, not document storage
- **The 14 annoyances** — competitive insights must avoid "wall of text" (type collision resolution) and "right answer to wrong question" (scope definition)

---

This is a **harm-capable workflow** (indirect strategic harm through accepted insights) with **adversarial data** (competitors don't cooperate with your scraping) and **ephemeral data** (competitive data decays faster than any other type). The Prospector's two-axis failure space (validity × novelty) is the defining quality metric, and the Confidence & Gaps Statement is the most important output.

Shall I go deeper into any specific phase, develop the agent specifications further, or move toward implementation architecture?Memory updated with the complete Competitive Intelligence Workflow design and the 5 unique cross-cutting insights. The adversarial data source insight and existential specification aging insight are particularly notable — they extend CC-3 and CC-5 in ways that apply to any domain with adversarial or time-sensitive data, not just competitive intelligence.

Shall I go deeper on any phase, develop specific agent specifications, or move toward implementation?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-19T07:26:28* · `glm-5.1:cloud` · `03d15bc7...`

### Prompt

would there be benefit from vectorizing competitor websites' content to enable the querying of aggregate and semantic data for insights?

### Response

Yes — significant benefit. But it's a **layer**, not a replacement. Let me show why and where it fits.

## What Vectorization Enables That Structured Data Alone Can't

| Capability | Structured Only | + Vector Layer |
|-----------|----------------|----------------|
| "Which competitors position similarly to us?" | Keyword match on positioning labels | Semantic clustering — finds similarity even with different words |
| "What themes does the market talk about?" | Pre-defined categories only | Discovers emergent themes across all competitors |
| "Is anyone talking about [concept]?" | Exact keyword search | Semantic search — finds "reliability" even when competitors say "uptime guarantee" or "dependable performance" |
| "How is messaging shifting?" | Compare structured positioning fields | Compare semantic drift in embeddings over time |
| "What is NOBODY talking about?" | Hard to detect absence | Semantic gap — concepts present in your messaging with no vector neighbours among competitors |
| Cross-competitor aggregation | Requires manual SQL queries | "What do all competitors say about pricing?" — one semantic query |

The Prospector agent specifically needs this. Its job is to find **novel connections and gaps** — vector similarity across the entire competitive corpus is exactly the discovery surface it needs. Without it, the Prospector can only find patterns in the structured fields you've already extracted, which means it can only find what you've already defined. That's the opposite of novelty.

## The Dual-Layer Architecture

Here's the key insight: **vectorization finds, typed extraction resolves. Both are needed.**

```
Competitor Website
       │
       ▼
  ┌─────────────┐
  │   SCOUT      │  Scrapes raw content
  │   Extractor  │
  └──────┬──────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌──────────┐
│LAYER 1 │ │ LAYER 2  │
│Typed   │ │ Semantic │
│Extraction│ │  Search  │
│        │ │          │
│Postgres│ │ Chroma   │
│+ TypeDB│ │          │
└────────┘ └──────────┘
    │           │
    │     ┌─────┘
    ▼     ▼
┌──────────────┐
│  PROSPECTOR   │  Uses BOTH layers
│  Generator    │  - Structured queries for known dimensions
│               │  - Semantic search for novel patterns
└──────────────┘
```

**Layer 1 — Structured (Postgres + TypeDB):** Typed knowledge objects with epistemic metadata. Pricing, features, segments, positioning claims — each extracted, typed, and carrying confidence/provenance/recency. This is what the Analyst classifies and what the Strategist prepares judgment from.

**Layer 2 — Semantic (Chroma):** Embedded competitor content enabling similarity search, theme clustering, and semantic gap detection. This is what the Prospector uses for discovery.

## What Vectorization Does NOT Solve

This is where CAWDP pushes back:

**1. Type collision still applies.** Raw website content in a vector DB is still undifferentiated prose. A competitor's homepage bundles pricing claims, feature announcements, positioning statements, testimonials, and disclaimers into one page. Vectorization helps you **find** the content, but you still need typed extraction to **work with** it. The 17+ information types (claims, evidence, assumptions, options, criteria, actions, etc.) are still encoded in prose even after embedding.

**2. Epistemic metadata doesn't disappear.** A vector similarity score of 0.93 doesn't tell you that the pricing page was scraped 6 weeks ago, or that the competitor's "enterprise" plan is aspirational pricing that nobody has actually purchased. Every vector search result still needs confidence, provenance, recency, and uncertainty attached. Without this, the Prospector generates insights from stale or misleading data — and valid-but-obvious becomes valid-but-wrong.

**3. Adversarial provenance is harder in vector space.** When you search structured data, you can see exactly which field came from which source. In vector space, the embedding blends everything together. A competitor's bold vision statement and their actual product capabilities get embedded into the same vector. You need to carry provenance metadata alongside embeddings, not inside them.

**4. Specification aging applies to vectors too.** An embedding of a competitor's pricing page from 6 weeks ago will still return high similarity scores for pricing queries. The vector doesn't self-destruct when data goes stale. You need to either re-embed on a cadence (expensive) or layer staleness metadata on top of vector results (more practical).

## How It Connects to the Existing Architecture

This maps directly to the Small Business Agentic OS data layer:

| Store | Purpose | Competitive Intel Role |
|-------|---------|----------------------|
| **Postgres** | Structured data, registries | Competitor profiles, pricing tables, feature matrices, classified segments |
| **TypeDB (PRISM)** | Knowledge graph with relations | Competitor → competes_with → Competitor, Competitor → targets → Segment, Competitor → positions_as → Position |
| **Chroma** | Semantic search | Cross-competitor theme discovery, semantic gap detection, messaging drift, similarity clustering |
| **MinIO** | Raw documents | Original scraped pages (provenance trail, re-extraction if needed) |

The Strategy domain orchestrator (from the Growth Orchestrator grouping) queries **all four stores**:

- **Postgres** for "what do we know about Competitor X's pricing?" (structured query)
- **TypeDB** for "how are Competitors A, B, and C related?" (graph traversal)
- **Chroma** for "who is talking about reliability?" (semantic search)
- **MinIO** for "show me the original page this came from" (provenance verification)

## The Prospector's Two-Layer Discovery

This is where the architecture directly serves the agent's identity:

**Structured queries (Layer 1)** answer known questions:
- "Which competitors target the enterprise segment?"
- "What is Competitor X's pricing?"
- "How many competitors offer feature Y?"

**Semantic queries (Layer 2)** discover unknown patterns:
- "What themes are emerging across all competitors?"
- "Is anyone talking about [our differentiator]?"
- "What concepts appear in our messaging that have no competitors nearby?"

**The combination (both layers)** is where novelty lives:
- A competitor semantically clusters near you on positioning (Layer 2) but their pricing is 30% lower (Layer 1) — that's a threat signal you'd miss with either layer alone
- Nobody talks about "compliance" semantically (Layer 2), and no structured field mentions it (Layer 1) — that's a gap opportunity

## The Practical Implementation Path

**Phase 1 (MVP — structured only):** Scout scrapes → Analyst extracts and classifies → Registrar stores typed knowledge objects in Postgres + TypeDB. No vector store yet. This works for "what does Competitor X offer?" but not for "what patterns am I missing?"

**Phase 2 (add semantic layer):** Scout also chunks and embeds content into Chroma alongside structured extraction. Prospector gets vector search as a discovery tool. This is where the two-axis failure space (validity × novelty) gets its discovery surface — the Prospector can now find novel connections that structured queries can't surface.

**Phase 3 (temporal analysis):** Re-embed competitor content on the CC-5 cadence (pricing 7 days, features 14 days, messaging 21 days). Compare embedding drift over time to detect semantic shifts in positioning. This is where "how is the market moving?" becomes answerable.

## Key CAWDP Principle: Vectorization Adds Discovery, Not Truth

To bring this back to the workflow's core design:

> Vectorization is the Prospector's telescope — it reveals what structured observation can't see. But a telescope doesn't make the stars more reliable. You still need the Analyst's measurements, the Strategist's confidence scores, and the O7 Confidence & Gaps Statement to tell the principal what they can and can't trust.

The architecture needs both layers. The typed extraction layer (Postgres + TypeDB) is where truth and recency live. The semantic layer (Chroma) is where discovery and novelty live. The Prospector uses both. The Strategist prepares judgment from both. The principal decides.

Want me to specify the data schemas, the Prospector's two-layer query protocol, or the Chroma collection design?

---
