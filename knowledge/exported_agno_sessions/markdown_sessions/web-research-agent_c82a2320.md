# Web Research Agent

| Field | Value |
|-------|-------|
| **Session** | `c82a2320...` |
| **Type** | agent |
| **Agent** | Web Research Agent |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-19T06:53:50 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Web Research Agent ✓ COMPLETED

*2026-05-19T06:53:50* · `glm-5.1:cloud` · `dfde8098...`

### Prompt

Let's apply CAWDP to designing an agentic workflow for scraping competitor websites, saving collected data to the database, adding content to a vector database, and enabling an agent to gather insights about the competitive landscape. The ideal outcomes is that the business understands the crowded vs open spaces in the market, the types of products on offer, the market segments being targeted, the messaging being used, and other factors that help us differentiate and identify strategic moves.

### Response

# CAWDP Framework: Agentic Competitive Intelligence Workflow

## C — Context

### Problem Space
The business needs **continuous, automated competitive intelligence** to understand market positioning, identify whitespace opportunities, and inform strategic decisions. Manual analysis is slow, shallow, and quickly outdated.

### Key Questions the System Must Answer
| Category | Sample Questions |
|---|---|
| **Market Crowding** | Which segments have the most competitors? Where are the few? |
| **Product Landscape** | What product categories exist? What features are table-stakes vs differentiating? |
| **Target Segments** | Who are competitors targeting? What personas, verticals, company sizes? |
| **Messaging & Positioning** | What value propositions dominate? What claims are common? What tone/style? |
| **Pricing & Packaging** | What pricing models are used? Free tiers? Enterprise pricing signals? |
| **Strategic Moves** | Who's expanding? Who's pivoting? Who's launching new products? |

### Constraints & Risks
- **Ethical/legal scraping** — respect `robots.txt`, rate limits, and terms of service.
- **Data freshness** — competitive data decays; system must refresh regularly.
- **Hallucination risk** — insights must be traceable to source data.
- **Noise vs signal** — raw scrape data is massive; the system must distill, not just collect.

---

## A — Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                           │
│              (Workflow Manager / Agent Controller)               │
└────────┬──────────┬──────────┬──────────┬───────────────────────┘
         │          │          │          │
    ┌────▼───┐ ┌────▼───┐ ┌────▼───┐ ┌────▼────┐
    │Scraper │ │Parser  │ │Analyst │ │Reporter │
    │ Agent  │ │ Agent  │ │ Agent  │ │ Agent   │
    └────┬───┘ └────┬───┘ └────┬───┘ └────┬────┘
         │          │          │          │
    ┌────▼──────────▼──────────▼──────────▼────┐
    │           DATA LAYER                      │
    │  ┌─────────────┐  ┌───────────────────┐  │
    │  │  TypeDB      │  │  Vector DB        │  │
    │  │  (Structured │  │  (Semantic        │  │
    │  │   Knowledge  │  │   Search +        │  │
    │  │   Graph)     │  │   Embeddings)     │  │
    │  └──────┬──────┘  └────────┬──────────┘  │
    └─────────┼──────────────────┼──────────────┘
              │                  │
    ┌─────────▼──────────────────▼──────────────┐
    │           STORAGE LAYER                     │
    │  ┌────────────┐  ┌────────┐  ┌──────────┐  │
    │  │ Raw HTML   │  │ Parsed │  │ Insights │  │
    │  │ Store      │  │ Store  │  │ Archive  │  │
    │  └────────────┘  └────────┘  └──────────┘  │
    └────────────────────────────────────────────┘
```

### Agent Definitions

| Agent | Responsibility | Tools/Model |
|---|---|---|
| **Scraper Agent** | Discovers competitor URLs, manages crawl queue, respects robots.txt, retrieves pages | HTTP client, sitemap parser, robots.txt checker |
| **Parser Agent** | Extracts structured data from raw HTML — products, pricing, messaging, team info, blog posts | LLM + HTML parser (BeautifulSoup/JSSoup), schema.org extractor |
| **Analyst Agent** | Synthesizes parsed data into insights — gap analysis, positioning maps, trend detection | LLM (reasoning-optimized), TypeQL queries, vector similarity search |
| **Reporter Agent** | Formats insights into stakeholder-ready outputs — dashboards, briefs, alerts | LLM, templating engine, notification service |

---

## W — Workflow

### Phase 1: Discovery & Scrape

```yaml
phase: discovery_and_scrape
steps:
  - name: seed_competitor_list
    agent: Scraper
    input: Known competitor names + industry keywords
    action: >
      Search for competitors using web search APIs or curated lists.
      Expand seed list using "similar to" and "alternatives to" queries.
    output: competitor_registry (name, domain, category, priority)

  - name: crawl_competitor_sites
    agent: Scraper
    input: competitor_registry
    action: >
      For each competitor:
        1. Fetch robots.txt — determine allowed paths and crawl-delay.
        2. Fetch sitemap.xml — build URL inventory.
        3. Prioritize: homepage, /products, /pricing, /about, /blog, /careers.
        4. Crawl with rate limiting, store raw HTML.
    output: raw_html_corpus [{competitor_id, url, html, fetched_at}]

  - name: schedule_recrawl
    agent: Scraper
    action: >
      Set recrawl cadence based on change-detection:
        - Pricing pages: daily
        - Product pages: weekly
        - Blog pages: bi-weekly
        - About/Team: monthly
    output: recrawl_schedule
```

### Phase 2: Parse & Structure

```yaml
phase: parse_and_structure
steps:
  - name: extract_product_data
    agent: Parser
    input: raw_html_corpus
    action: >
      Use LLM-assisted extraction to pull:
        - Product/service names and descriptions
        - Feature lists and comparison tables
        - Pricing tiers, amounts, billing models
        - Integrations and platform support
        - Target audience statements (ICP language)
    output: structured_products [
      {competitor, product_name, category, features[], pricing, 
       target_segment, differentiators[]}
    ]

  - name: extract_messaging_and_positioning
    agent: Parser
    input: raw_html_corpus
    action: >
      Extract:
        - Headlines, taglines, value propositions
        - Pain points addressed (implicit and explicit)
        - Claims: "only", "first", "best", "leading"
        - Social proof: logos, testimonials, case studies
        - Tone and voice characteristics
    output: structured_messaging [
      {competitor, headline, value_props[], claims[], social_proof[], tone}
    ]

  - name: extract_market_signals
    agent: Parser
    input: raw_html_corpus
    action: >
      Extract:
        - Blog post topics and publishing cadence
        - Job openings (signals investment areas)
        - Press releases and funding announcements
        - Partner/channel references
    output: structured_signals [
      {competitor, signal_type, content, detected_at}
    ]
```

### Phase 3: Store & Index

```yaml
phase: store_and_index
steps:
  - name: write_to_typedb
    agent: Parser
    input: structured_products, structured_messaging, structured_signals
    action: >
      Insert as TypeDB entities and relations:
        - Entities: competitor, product, feature, pricing_model, 
          target_segment, claim, value_proposition
        - Relations: 
          competitor-OWNS->product
          product-HAS_FEATURE->feature
          product-TARGETS->segment
          product-HAS_PRICING->pricing_model
          competitor-CLAIMS->value_proposition
          competitor-USES_TONE->tone
          competitor-PUBLISHES->signal
    output: typedb_knowledge_graph

  - name: embed_and_index_vectors
    agent: Parser
    input: raw text excerpts + structured summaries
    action: >
      For vector DB ingestion:
        1. Chunk product descriptions, messaging copy, and blog content.
        2. Generate embeddings for each chunk.
        3. Store with metadata: {competitor, page_type, url, date}.
        4. Enable similarity search across competitor messaging.
    output: vector_index_populated

  - name: store_raw_artifacts
    agent: Parser
    input: raw_html_corpus
    action: Archive raw HTML for traceability and re-parsing.
    output: raw_html_archive
```

### Phase 4: Analyze & Insight

```yaml
phase: analyze_and_insight
steps:
  - name: market_crowding_analysis
    agent: Analyst
    action: >
      TypeQL queries to determine:
        - How many competitors target each identified segment?
        - Which product categories are most/least contested?
        - Where are competitors concentrated vs sparse?
      Output: crowding_heatmap_data

  - name: positioning_map
    agent: Analyst
    action: >
      Use vector similarity to cluster competitors by:
        - Messaging similarity (who sounds alike?)
        - Feature overlap (who competes head-to-head?)
        - Pricing approach (premium, freemium, usage-based?)
      Output: positioning_clusters, differentation_gaps

  - name: whitespace_identification
    agent: Analyst
    action: >
      Identify:
        - Underserved segments (few competitors targeting)
        - Unclaimed messaging positions (no one using this language)
        - Missing feature combinations (potential product gaps)
        - Pricing model gaps (opportunities for novel models)
      Output: whitespace_opportunities []

  - name: trend_detection
    agent: Analyst
    action: >
      Over time, track:
        - New entrants in the space
        - Feature convergence (everyone adding X)
        - Messaging shifts (from "efficiency" to "AI-powered")
        - Pricing model evolution
      Output: trend_reports []
```

### Phase 5: Report & Deliver

```yaml
phase: report_and_deliver
steps:
  - name: generate_competitive_brief
    agent: Reporter
    input: All analyst outputs
    action: >
      Produce:
        - Executive summary: top 5 competitive moves this period
        - Market map: visual landscape overview
        - Whitespace report: top 3 opportunities with rationale
        - Competitor profiles: one-pagers for each tracked competitor
        - Alert feed: significant changes detected this cycle
    output: stakeholder_brief

  - name: answer_ad_hoc_queries
    agent: Analyst
    action: >
      Enable natural-language Q&A over the knowledge graph:
        - "Which competitors target enterprise healthcare?"
        - "Who has the most similar messaging to us?"
        - "What pricing models are gaining traction?"
        - "What segments is no one targeting?"
      Use: TypeQL for structured queries + vector search for semantic queries.
    output: on_demand_insights
```

---

## D — Data

### TypeDB Schema (Conceptual)

```typeql
define

  competitor sub entity,
    owns competitor_name,
    owns competitor_domain,
    owns last_crawled,
    plays owns-product,
    plays makes-claim,
    plays targets-segment,
    plays publishes-signal;

  product sub entity,
    owns product_name,
    owns product_description,
    plays is-owned,
    plays has-feature,
    plays has-pricing,
    plays targets-via-product;

  feature sub entity,
    owns feature_name,
    owns feature_description,
    plays feature-of;

  pricing_model sub entity,
    owns model_type,         # "freemium", "usage-based", "flat-rate", "tiered"
    owns price_amount,
    owns billing_period,
    plays pricing-of;

  target_segment sub entity,
    owns segment_name,      # "Enterprise", "SMB", "Developers", "Healthcare"
    owns segment_description,
    plays segment-target,
    plays segment-target-via-product;

  value_proposition sub entity,
    owns vp_text,
    owns vp_category,       # "efficiency", "cost-savings", "innovation", etc.
    plays claim-made;

  signal sub entity,
    owns signal_type,       # "hiring", "funding", "partnership", "product-launch"
    owns signal_content,
    owns signal_date,
    plays signal-published;

  tone sub entity,
    owns tone_descriptor,   # "authoritative", "playful", "technical", "aspirational"
    plays tone-used;

  # Relations
  ownership sub relation,
    relates owns-product,
    relates is-owned;

  product-feature sub relation,
    relates has-feature,
    relates feature-of;

  product-pricing sub relation,
    relates has-pricing,
    relates pricing-of;

  competitor-segment sub relation,
    relates targets-segment,
    relates segment-target;

  product-segment sub relation,
    relates targets-via-product,
    relates segment-target-via-product;

  competitor-claim sub relation,
    relates makes-claim,
    relates claim-made;

  competitor-signal sub relation,
    relates publishes-signal,
    relates signal-published;

  competitor-tone sub relation,
    relates uses-tone,
    relates tone-used;
```

### Vector DB Schema

```json
{
  "collection": "competitor_content",
  "dimension": 1536,
  "metadata_schema": {
    "competitor_id": "string",
    "competitor_name": "string",
    "content_type": "enum[product_description, messaging, blog_post, pricing_copy, about_page]",
    "url": "string",
    "extracted_at": "datetime",
    "chunk_index": "int"
  }
}
```

### Key TypeQL Queries for Insights

```typeql
# Which segments are most crowded?
match
  $seg is target_segment;
  $seg has segment_name $name;
  competitor-segment($comp, $seg);
  get $name, $comp;
  # Count per segment → crowding metric

# Which competitors have similar features?
match
  $f is feature;
  $f has feature_name $fname;
  product-feature($p1, $f);
  product-feature($p2, $f);
  $p1 != $p2;
  get $p1, $p2, $fname;

# What pricing models exist in our segment?
match
  $pm is pricing_model;
  $pm has model_type $ptype;
  product-pricing($prod, $pm);
  get $prod, $ptype;

# Find whitespace: segments with no competitor
# (All segments minus targeted ones)
match
  $seg is target_segment;
  not { competitor-segment($comp, $seg); };
  get $seg;
```

---

## P — Process

### Operational Cadence

| Activity | Frequency | Trigger |
|---|---|---|
| Full competitor crawl | Weekly | Scheduled |
| Pricing/product page crawl | Daily | Scheduled |
| Signal detection (jobs, press) | Daily | Scheduled |
| Market analysis refresh | Bi-weekly | Post-crawl |
| Stakeholder brief generation | Monthly | Scheduled |
| Ad-hoc insight queries | On-demand | User request |
| Schema evolution | As needed | New data type detected |

### Quality Assurance Gates

```
[Scrape] ──► Parse QA: Is extraction >85% complete? ──► [Parse]
    │                                                          │
    │           ◄── NO: Flag for manual review ──◄────────────┘
    │                                                          │
    │         YES ──► [Store] ──► [Analyze] ──► [Report]
    │                           │
    │                           ▼
    │              Insight QA: Are claims grounded in data?
    │              (Every insight must link to source URL)
    │                           │
    │                YES ◄──────┴──────► NO: Regenerate with citations
    │                 │
    │                 ▼
    │            [Deliver to Stakeholders]
```

### Traceability & Governance Rules

1. **Every insight must cite its source.** The Analyst agent must include competitor name + URL for every claim.
2. **No hallucinated data.** If the Parser agent is <90% confident in extraction, flag for human review rather than inserting into the graph.
3. **Recrawl before re-analysis.** Never analyze stale data without checking freshness.
4. **Bias awareness.** The system should note when analysis is based on publicly available data only (insiders may have different views).
5. **Ethical scraping.** Respect `robots.txt`, crawl delays, and never bypass authentication.

### Escalation Protocol

| Condition | Action |
|---|---|
| Scraping blocked by competitor | Log, skip, try again next cycle; no circumvention |
| Conflicting data across pages | Flag conflict, use most recent page, note discrepancy |
| Major competitive shift detected | Immediate alert to stakeholders (new entrant, major pivot) |
| Low extraction confidence (<85%) | Queue for human review, insert with `review_required: true` |

---

## Putting It All Together

The system operates as a **continuous loop**:

```
DISCOVER → SCRAPE → PARSE → STORE → ANALYZE → REPORT → (evolve) → DISCOVER → ...
```

Each cycle enriches the knowledge graph, improves the vector index, and deepens the analytical model. Over time, the system shifts from **descriptive** ("here's what competitors are doing") to **predictive** ("based on hiring + messaging shifts, Competitor X is likely entering Segment Y").

---

Let me store this workflow design so you can retrieve and evolve it later:The database connection isn't available at the moment, but the full workflow design is documented above. Here's a quick summary of what we've designed:

### What You Now Have

| CAWDP Layer | What It Delivers |
|---|---|
| **Context** | Clear problem definition — answering market crowding, product landscape, segment targeting, messaging, and strategic move questions |
| **Architecture** | 4 specialized agents (Scraper → Parser → Analyst → Reporter) over a dual-store (TypeDB + Vector DB) with raw HTML archival |
| **Workflow** | 5-phase pipeline from discovery through reporting, with recrawl cadences from daily to monthly |
| **Data** | Full TypeDB schema for competitive entities & relations, plus vector DB config for semantic search over competitor content |
| **Process** | QA gates, traceability rules, ethical scraping protocols, and escalation paths |

The key strategic insight in this design is that **TypeDB's knowledge graph handles the structured "what and who"** (which competitors exist, what products they offer, which segments they target) while the **vector DB handles the semantic "how"** (how similar is their messaging, what positioning clusters exist, what whitespace is unclaimed). The Analyst agent bridges both — running TypeQL queries for categorical analysis and vector similarity searches for positional analysis.

Want me to dive deeper into any specific phase, elaborate on the TypeQL queries, or flesh out agent prompts?

---
