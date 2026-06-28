<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# great. if we wanted to add the intelligence layer where market research, competitive landscape and strategy inputs among others were also important. What extra data entities might this add?

This is a significant and exciting extension — moving the platform from an **operational OS** to a **strategic intelligence layer**. This is where the agent stops just executing tasks and starts actively helping the owner understand their position and make better decisions.

## The Intelligence Layer Domains

### 🌍 Market Context

The external environment the business operates within.

- **Market** — a defined addressable market or segment (name, geography, size estimate, growth rate, sources)
- **Market Trend** — a named shift or signal in the market (description, direction, confidence, date observed, source)
- **Industry Report** — an ingested research document (title, source, date, summary, linked blob)
- **Market Signal** — a lightweight observation (news item, social mention, regulatory change) tagged by relevance and impact
- **Demand Indicator** — tracked proxies for customer demand (search volume trends, enquiry rates, seasonal patterns)

***

### 🏆 Competitive Intelligence

Who else is competing for the same customers.

- **Competitor** — a named competing business (name, website, size estimate, positioning, geography)
- **Competitor Offering** — a specific product or service a competitor sells (price, features, positioning — linked to Competitor)
- **Competitive Move** — a tracked change a competitor has made (price change, new product, marketing push, date observed)
- **Competitive Comparison** — an agent-built analysis comparing the business's offerings against a competitor's on defined dimensions
- **Win/Loss Record** — outcome of competitive sales situations (which competitor, why won/lost, linked Opportunity)

***

### 🎯 Customer Intelligence

Deeper understanding of who customers are and what drives them.

- **Customer Persona** — a named archetype of a customer type (demographics, goals, pain points, buying triggers)
- **Job-to-be-Done** — a specific outcome a customer is trying to achieve (linked to Persona, informs Offering design)
- **Feedback** — structured or unstructured input from customers (source: survey/interview/review, sentiment, themes)
- **Review** — a public or private rating (platform, score, date, content, linked Customer)
- **NPS Response** — a net promoter score entry (score, comment, date, linked Customer)
- **Churn Reason** — a recorded explanation for a lost customer (category, verbatim, linked Customer)

***

### 📐 Strategy

The business's own direction, goals and thinking.

- **Strategic Goal** — a high-level outcome the business is working toward (description, timeframe, owner, status)
- **OKR** — an objective and key results set (objective, linked key results with targets and current values)
- **Initiative** — a strategic project or programme of work (linked to Goal, timeframe, resources)
- **Assumption** — a belief the strategy depends on (stated, tested/untested, evidence, risk level)
- **Decision Log** — a record of a significant business decision (what was decided, why, alternatives considered, date)
- **SWOT Entry** — a named strength, weakness, opportunity, or threat (category, description, evidence, date)
- **Business Model Canvas Element** — structured entries across the 9 BMC blocks (value prop, channels, revenue streams etc.)

***

### 💡 Positioning \& Value

How the business presents itself and creates differentiation.

- **Value Proposition** — a formal statement of the value delivered to a specific Persona (linked to Persona and Offering)
- **Brand Attribute** — a named quality the business wants to be known for (tone, visual, personality traits)
- **Positioning Statement** — a structured claim of differentiation vs a Competitor for a Persona
- **Unique Selling Point** — a specific, provable differentiator (claim, evidence, linked Offering)
- **Messaging Framework** — a structured set of messages for a Persona or Campaign (headlines, proof points, objection responses)

***

### 📡 External Intelligence Sources

Where the intelligence comes from — tracked and attributable.

- **Source** — a named information feed (website, publication, RSS feed, government data source, review platform)
- **Monitored Keyword** — a term the agent watches for in signals (competitor name, product category, industry term)
- **Intelligence Report** — an agent-generated synthesis across multiple signals on a topic (equivalent to Dash's agent-built views — written to `agent_` schema)
- **Benchmark** — a comparative metric from the market or industry (average conversion rate, typical margin, standard pricing)

***

### 🔭 Scenario Planning

Forward-looking intelligence for resilience.

- **Scenario** — a named future state (optimistic, base, pessimistic) with defined conditions
- **Risk** — a named business risk (category, likelihood, impact, mitigation, owner)
- **Opportunity Pipeline** — a tracked strategic opportunity (market entry, partnership, new offering) distinct from a sales Opportunity
- **Pivot Record** — a documented strategic shift (what changed, why, when, linked to Decision Log)

***

## How These Layer onto the Existing Model

The intelligence entities don't replace the operational ones — they contextualise them. The key relationships:

```
Market Trend ──── informs ──── Strategic Goal
                          └─── Initiative
                          └─── Value Proposition

Competitor Offering ── compared against ── Product / Service
Win/Loss Record ────── linked to ────────── Opportunity (existing)
                                       └─── Competitor

Customer Persona ── shapes ── Messaging Framework
                         └─── Offering (Product / Service)
                         └─── Campaign (existing)

Feedback / Review ── feeds ── Customer Persona
                         └─── Churn Reason
                         └─── SWOT Entry

Strategic Goal ── measured by ── OKR
              └── delivered via ── Initiative ── broken into ── Project (existing)

Decision Log ── references ── Assumption
            └── influenced by ── Market Signal / Competitive Move
```


***

## The Agent Schema Extensions (`agent_` layer)

The intelligence layer generates derived views the agents build and maintain — following the Dash Engineer pattern:

- **market_position_score** — where the business sits relative to competitors on key dimensions
- **strategic_health_dashboard** — OKR progress + market trend alignment + risk register summary
- **opportunity_whitespace** — gaps in the market not covered by current offerings or competitors
- **customer_sentiment_trend** — aggregated from Reviews, NPS, Feedback over time
- **competitive_threat_index** — a computed risk score per competitor based on recent moves

***

## Two New Agent Roles

This intelligence layer warrants two specialist agents in the team:


| Agent | Responsibility | Key Tools |
| :-- | :-- | :-- |
| **Intelligence Agent** | Monitors external sources, ingests signals, updates competitive and market entities, surfaces trends | Web search (MCP), RSS ingestion, document parsing, vector search across Industry Reports |
| **Strategy Agent** | Reasons across goals, OKRs, market position, and business performance to surface strategic insights and recommendations | Reads `agent_` intelligence views + operational summaries, writes Decision Log entries, generates Intelligence Reports |

The **Strategy Agent** is the highest-trust agent in the system — it has read access across *all* schemas (operational + intelligence) but writes only to the `agent_` layer and the Decision Log. It answers questions like:

- *"Are we priced competitively for the segment we're targeting?"*
- *"Which of our current customers look most like our ideal persona?"*
- *"What's the biggest strategic risk we're not responding to?"*
- *"How are we tracking against our goals for this quarter?"*

***

## The Compounding Intelligence Effect

This is where the platform becomes genuinely hard to replicate. Over time, the combined operational + intelligence model means the agents can connect dots no standalone tool ever could:

- A **Win/Loss Record** linked to a **Competitive Move** reveals that a price change by a competitor is costing real deals — surfaces automatically, no analyst required
- A **Market Trend** linked to a **Customer Persona's Job-to-be-Done** suggests a new offering — the Strategy Agent flags it as an opportunity
- **Churn Reasons** correlated with **NPS Responses** and **Feedback** build a richer picture of product-market fit than any single survey
- **OKR progress** mapped against **Initiative** execution and **Expense** reality gives the owner an honest gap analysis between strategy and operations

This is the insight no SaaS stack of disconnected tools can produce — because no single tool has the full picture. The SMB OS does.

