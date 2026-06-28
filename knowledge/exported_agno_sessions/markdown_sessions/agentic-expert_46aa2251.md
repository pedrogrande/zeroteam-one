# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `46aa2251...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-06T00:12:15 |
| **Runs** | 0 completed / 1 total |

## Run 1 — Agentic Expert ⚠️ ERROR

*2026-05-06T00:12:15* · `glm-5.1:cloud` · `4280870a...`

### Prompt

I want to set up an Agno AgentOS application with a custom front end platform for small business owners.

The platform should be a dashboard for business intelligence, strategy and task management as a core foundational element. The other business data will often be related to these elements.

The vision that this will be an agent-native business with all business data feeding through for analysis and insights.

Consider this 'launch project' and advise on how we can apply PRISM methodology and CAWDP to this while providing a user friendly UI:

---
This is essentially the **platform's onboarding experience as a strategic programme** — not a sign-up form, but a guided journey that builds both the system and the business simultaneously. Here's the full task map.

***

## Programme Structure

The Launch Project runs across five phases. Each phase has agent-led sessions, owner inputs, and system outputs that populate both the intelligence layer and the operational schema.

```
Phase 1: Founder Intelligence    → Know the owner
Phase 2: Vision & Foundation     → Build the purpose layer
Phase 3: Strategic Intelligence  → Understand the landscape
Phase 4: Strategy Suite          → Develop all strategies
Phase 5: Operational Blueprint   → Build the operating system
```

***

## Phase 1: Founder Intelligence
*The agents must know the owner before they can help build anything.*

**Owner Profile Sessions**
- [ ] Life & career history interview — experience, industries, roles held
- [ ] Values elicitation session — what matters most, non-negotiables, ethical boundaries
- [ ] Strengths & skills inventory — professional strengths, natural abilities, developed expertise
- [ ] Motivations & drivers — why this business, why now, what success looks like personally
- [ ] Risk tolerance assessment — financial, reputational, operational comfort zones
- [ ] Working style & preferences — how they like to communicate, make decisions, manage people
- [ ] Network & relationships audit — existing contacts, advisors, potential collaborators
- [ ] Financial position baseline — capital available, personal income needs, investment horizon
- [ ] Time & capacity map — hours available, other commitments, energy peaks

**System Outputs**
- `founder_profile` entity populated
- `business_rule` entries for owner preferences (communication style, decision thresholds)
- Initial `customer_persona` hypotheses based on founder's network and background
- `assumption` entries for beliefs the founder holds about the market

***

## Phase 2: Vision & Foundation
*Build the purpose and identity layer — the North Star everything else aligns to.*

**Discovery Sessions**
- [ ] Purpose workshop — why does this business exist beyond making money?
- [ ] Vision articulation — what does success look like in 3, 5, 10 years?
- [ ] Mission definition — what does the business do, for whom, and how?
- [ ] Values definition — 3–5 core values with behavioural descriptions
- [ ] Anti-vision session — what would failure look like? what must never happen?

**Identity Sessions**
- [ ] Business name exploration and validation
- [ ] Brand personality definition (tone, character, how the business speaks)
- [ ] Visual identity direction (style, colour philosophy, aesthetic references)
- [ ] Naming conventions for offerings, segments, internal language

**Goal Architecture**
- [ ] Long-term goals (3–5 year horizon) — financial, impact, scale, personal
- [ ] Medium-term goals (12 month) — revenue, customers, team, capabilities
- [ ] Near-term goals (90 day) — first milestones, proof points, learning targets
- [ ] `strategic_goal` and `OKR` entities created for each
- [ ] Assumptions behind each goal documented in `assumption` store

**System Outputs**
- `business_profile` fully populated
- `brand_attribute` set defined
- `strategic_goal` hierarchy created
- `value_proposition` draft (refined in Phase 4)
- `decision_log` entry: foundational business decisions recorded

***

## Phase 3: Strategic Intelligence
*Build the intelligence layer before writing a single strategy.*

**Market Research**
- [ ] Industry definition and scope — what market is the business entering?
- [ ] Market size estimation (TAM / SAM / SOM)
- [ ] Market trend identification — growth drivers, emerging shifts, declining patterns
- [ ] Regulatory and compliance landscape — licences, obligations, industry rules
- [ ] Demand signal research — search trends, enquiry patterns, seasonal factors
- [ ] `market` and `market_trend` entities populated
- [ ] `industry_report` documents ingested into knowledge base

**Customer Intelligence**
- [ ] Ideal customer profile (ICP) definition — who is the *best* customer?
- [ ] Customer persona development (1–3 personas minimum)
- [ ] Jobs-to-be-done mapping per persona — what are they trying to achieve?
- [ ] Customer pain point inventory — what frustrates them about current solutions?
- [ ] Customer buying journey mapping — how do they discover, evaluate, decide, buy?
- [ ] Willingness-to-pay research — price sensitivity, value drivers
- [ ] `customer_persona` and `job_to_be_done` entities created

**Competitive Intelligence**
- [ ] Competitor identification — direct, indirect, and alternative competitors
- [ ] Competitor profiling (offerings, pricing, positioning, strengths, weaknesses)
- [ ] Competitive landscape mapping — who owns which segments?
- [ ] Gap analysis — where are customers underserved?
- [ ] `competitor` and `competitor_offering` entities populated
- [ ] Initial `competitive_comparison` views built by Intelligence Agent

**SWOT & Assumptions**
- [ ] SWOT analysis populated from Phase 1–3 outputs
- [ ] Critical assumption log reviewed and risk-rated
- [ ] `benchmark` data collected for key metrics (industry margins, average deal size, conversion rates)

***

## Phase 4: Strategy Suite
*Nine distinct strategies, each a focused session, all connected to the same intelligence base.*

### 4.1 Business Strategy
- [ ] Business model definition (how value is created, delivered, and captured)
- [ ] Business Model Canvas completed — all 9 blocks
- [ ] Revenue model selection (one-time, recurring, project, hybrid)
- [ ] Key partnerships and resources identified
- [ ] Cost structure mapped
- [ ] Overall strategic direction articulated (differentiation / cost leadership / niche focus)

### 4.2 Product Strategy
- [ ] Offering portfolio definition — what products/services will the business launch with?
- [ ] Offering roadmap — what gets built or added over 12 months?
- [ ] Pricing architecture — tiers, packages, price points
- [ ] Feature/benefit mapping per persona
- [ ] Minimum viable offering definition — what's enough to launch?
- [ ] `product`, `service`, `package`, `price_list` entities created

### 4.3 Brand Strategy
- [ ] Brand positioning statement — for whom, against whom, what differentiation, why credible
- [ ] Brand story — origin, mission, transformation narrative
- [ ] Tone of voice guidelines — how the brand speaks, with examples
- [ ] Brand experience principles — how every touchpoint should feel
- [ ] Naming architecture for product lines and tiers
- [ ] `positioning_statement`, `brand_attribute`, `messaging_framework` entities created

### 4.4 Marketing Strategy
- [ ] Target audience prioritisation — which persona to focus on first
- [ ] Marketing objectives linked to business goals
- [ ] Channel strategy — which channels reach the ICP and why
- [ ] Content themes and pillars — what the brand will be known for
- [ ] Lead generation approach — how strangers become leads
- [ ] Nurture strategy — how leads become customers
- [ ] Retention marketing approach — how customers become advocates
- [ ] `campaign` framework and `segment` definitions created

### 4.5 Go-to-Market Strategy
- [ ] Launch sequencing — what launches first, to whom, in what order
- [ ] GTM motion definition (product-led, sales-led, community-led, partner-led)
- [ ] First 100 customers plan — specific tactics to acquire initial customers
- [ ] Launch offer design — what is compelling to early adopters?
- [ ] Distribution channels defined — how does the offering reach the customer?
- [ ] Launch timeline and milestones
- [ ] Success metrics for launch phase (leading and lagging indicators)

### 4.6 Competitive Strategy
- [ ] Competitive positioning choices — where will the business compete and not compete?
- [ ] Differentiation proof points — specific, defensible claims
- [ ] Response playbook — how to respond to competitor moves (price cuts, new features)
- [ ] Moat-building plan — what makes the business harder to copy over time?
- [ ] `unique_selling_point` entities created with evidence
- [ ] `win_loss_record` framework established for ongoing capture

### 4.7 Growth Strategy
- [ ] Growth model selection (acquisition / retention / expansion / referral)
- [ ] Primary growth lever identification — what drives growth most efficiently?
- [ ] Growth experiments backlog — hypotheses to test in first 90 days
- [ ] Scaling triggers — at what milestones does the business change structure?
- [ ] Partnership and channel growth opportunities
- [ ] `opportunity_pipeline` entities created for strategic growth bets

### 4.8 Innovation Strategy
- [ ] Innovation horizon mapping — core (now), adjacent (next), transformational (future)
- [ ] Continuous improvement process — how does the business learn and iterate?
- [ ] Customer feedback loops — how insights flow from customers to product decisions
- [ ] Experimentation culture — appetite for testing, failure tolerance, learning cadence
- [ ] Technology and capability roadmap — what capabilities need to be built or acquired?
- [ ] `initiative` entities created for innovation investments

### 4.9 Media & Content Strategy
- [ ] Owned media plan — website, blog, email, content assets
- [ ] Earned media plan — PR, thought leadership, reviews, word of mouth
- [ ] Paid media plan (if applicable) — channels, budget, targeting approach
- [ ] Content calendar framework — themes, cadence, formats per channel
- [ ] Personal brand strategy for the founder (if relevant — LinkedIn, speaking, publishing)
- [ ] SEO strategy — topics, keywords, authority-building approach
- [ ] `template` library started for recurring content types

***

## Phase 5: Operational Blueprint
*Build the systems the agents will run.*

**Business Infrastructure**
- [ ] Legal structure confirmed (sole trader, company, trust)
- [ ] ABN, ACN registration (Australia) — agent provides guidance, owner executes
- [ ] Business bank account setup
- [ ] Payment processing configured (Stripe)
- [ ] Domain and email provisioned
- [ ] Business address established

**Operational Processes**
- [ ] Customer journey mapped end-to-end (enquiry → onboarding → delivery → payment → retention)
- [ ] Core workflows documented for each business function
- [ ] Standard operating procedures (SOPs) written for repeating processes
- [ ] Quality standards defined for each offering
- [ ] `workflow` entities created and loaded into agent knowledge base

**Financial Blueprint**
- [ ] Chart of accounts configured for the business
- [ ] Revenue targets by month for Year 1
- [ ] Cost structure and break-even analysis
- [ ] Cash flow projection — 12 months
- [ ] Pricing confirmed against cost model
- [ ] `account`, `budget`, and `tax_rate` entities created

**Team & Roles**
- [ ] Organisational structure defined (even if it's just the founder for now)
- [ ] Role descriptions for any immediate hires or contractors
- [ ] Responsibility matrix — who owns what
- [ ] `team_member` entities created

**Agent Configuration**
- [ ] Agent permissions defined per role (what each agent can do autonomously vs propose)
- [ ] Approval gate rules configured for each action type
- [ ] Business rules entered for all known preferences and constraints
- [ ] Knowledge base seeded with all strategy documents, SOPs, and business rules
- [ ] Initial `customer_persona` and `messaging_framework` loaded into agent context
- [ ] Evaluation suite run to confirm agent behaviour is correct before go-live

**Launch Readiness**
- [ ] Launch checklist reviewed against GTM strategy
- [ ] First 30-day action plan created
- [ ] First campaign or outreach sequence prepared
- [ ] Metrics dashboard configured (what the agents will report on weekly)
- [ ] First 90-day OKR review scheduled

***

## The Project Entity Structure

In the platform itself, this Launch Project maps to:

```
Project: "Business Launch"
  ├── Phase 1: Founder Intelligence     [5 sessions → founder_profile]
  ├── Phase 2: Vision & Foundation      [4 sessions → goals, brand]
  ├── Phase 3: Strategic Intelligence   [4 sessions → market, competitor, persona]
  ├── Phase 4: Strategy Suite           [9 strategy documents]
  └── Phase 5: Operational Blueprint    [infrastructure + agent config]

Each Phase → multiple Tasks
Each Task → assigned to Agent or Owner
Each completed Task → writes outputs to relevant entities
Each Session → logged as Conversation + Decision Log entries
All documents → stored in blob store, embedded in vector store
```

***

## The Compounding Effect

By the end of the Launch Project, the platform's agents don't just have configuration — they have **deep context**. They know why the business exists, who it serves, how it competes, and what the owner values. Every future agent action is grounded in that foundation.

---

### Response

This is a significant undertaking — applying your entire framework body to a concrete platform. Let me give you a structured analysis across the three dimensions you asked about (PRISM, CAWDP, UI), plus concrete implementation guidance.

I'll start with the most important observation:

## The Three Problems With the Current Task List

**Problem 1: It's a Wall of Text (Type Collision)**
The 100+ items encode at least 6 cognitive modes — narrative (life history), boundary (non-negotiables), exploratory (market research), verification (SWOT), configurational (agent permissions), evaluative (strategic direction) — all presented as checkboxes. Different modes need different interactions, not a single checklist.

**Problem 2: No Complementarity Allocation**
Who does what? The list says "Owner" or "Agent" or doesn't specify. CAWDP's ternary model (Human/Agent/System) needs to be applied to every task. Some tasks the owner MUST do (values, non-negotiables). Some tasks agents should do and present as decisions (market size estimation). Some tasks the system should handle silently (entity creation, progress tracking).

**Problem 3: No Possibility Gradient**
Phases 1-2 are possibility-oriented (exploring who you are, what you want). Phase 5 is constraint-oriented (setting up systems, configuring permissions). The current list presents them all at the same weight, in the same format. The experience should shift — expansive and exploratory early, tightening toward concrete later.

Let me now give you the comprehensive design.

---

## Part 1: PRISM Data Model

Every piece of data in the launch project maps to PRISM's 7 dimensions + 4 cross-cutting layers. Here's the complete mapping:

```
PRISM DIMENSIONS FOR THE LAUNCH PROJECT

SCOPES (isolation boundaries)
├── scope:founder-intelligence     (Phase 1 data)
├── scope:vision-foundation        (Phase 2 data)
├── scope:strategic-intelligence   (Phase 3 data)
├── scope:strategy-suite          (Phase 4 data)
└── scope:operational-blueprint   (Phase 5 data)

ACTORS (who does what)
├── actor:founder                  (the business owner)
├── actor:commercial-orchestrator (Financial, Contract, Regulatory, Business, Operations)
├── actor:growth-orchestrator     (Client, Market, Partner, Media, Strategy)
├── actor:venture-orchestrator   (Product, Idea, Technology, Innovation, Project)
├── actor:stewardship-orchestrator (Risk, Security, Regulatory, Impact, Knowledge)
└── actor:system                  (automated processes)

ENTITIES (typed objects with schemas)
├── founder_profile               (identity, values, strengths, risk tolerance, preferences)
├── business_profile              (name, structure, industry, model)
├── brand_attribute                (tone, personality, visual direction)
├── strategic_goal                 (long/medium/near-term, OKR hierarchy)
├── value_proposition              (what, for whom, why different)
├── customer_persona               (ICP, jobs-to-be-done, pain points, buying journey)
├── market                         (size, trends, regulations, demand signals)
├── competitor                     (direct, indirect, alternative)
├── competitor_offering            (what they offer, pricing, positioning)
├── product / service              (offerings, pricing, features)
├── campaign                      (marketing activities, channels)
├── workflow                       (business processes, SOPs)
├── financial_blueprint            (revenue targets, cost structure, cash flow)
├── team_member                    (roles, responsibilities)
├── agent_permission               (what each agent can do autonomously vs propose)
├── business_rule                  (owner preferences, constraints, thresholds)
├── decision_log                  (every judgment call with reasoning)
├── assumption                    (beliefs held with confidence ratings)
├── opportunity_pipeline           (growth bets, experiments)
└── initiative                    (innovation investments, experiments)

RELATIONS (typed connections between entities)
├── founder-defines-values         (founder_profile → brand_attribute)
├── goal-driven-by                 (strategic_goal → assumption)
├── persona-served-by             (customer_persona → product)
├── competitor-contrasts-with      (competitor → value_proposition)
├── strategy-informs              (strategic_goal → campaign)
├── workflow-owned-by              (workflow → team_member)
├── agent-authorized-for           (agent_permission → workflow)
├── assumption-underpins           (assumption → strategic_goal)
├── opportunity-maps-to            (opportunity_pipeline → strategic_goal)
└── initiative-advances            (initiative → strategic_goal)

EVENTS (things that happen)
├── session-completed              (a discovery/interview session finishes)
├── entity-created                  (a new business entity is created)
├── assumption-challenged          (new evidence contradicts an assumption)
├── decision-made                  (owner makes a judgment call)
├── strategy-approved             (owner signs off on a strategy)
├── agent-action-proposed          (agent suggests an action)
├── agent-action-approved          (owner approves an agent suggestion)
├── assumption-invalidated         (assumption proven wrong)
└── specification-aged            (data needs review/refresh)

KNOWLEDGE (documents, insights, patterns)
├── industry_report                (market research documents)
├── competitive_analysis           (competitor analysis outputs)
├── strategy_document              (each of the 9 strategies)
├── sop                            (standard operating procedures)
├── template                       (content templates, document templates)
├── insight                        (patterns discovered from data)
└── pattern                        (recurring observations across sessions)

INTENTIONS (goals, constraints, guardrails — the "why")
├── business_goal                  (what the business is trying to achieve)
├── founder_constraint             (non-negotiables, boundaries, risk limits)
├── brand_guardrail                (what the brand would NEVER do)
├── financial_constraint           (budget limits, pricing floors, cash requirements)
├── customer_commitment            (what the business promises to customers)
└── regulatory_requirement          (compliance obligations)
```

Now the 4 cross-cutting layers applied to EVERY entity:

```
EPISTEMIC LAYER (how confident are we?)
- confidence: how sure are we about this data?
- provenance: where did this come from? (owner session, agent research, external data)
- assumptions: what are we assuming?
- limitations: what can't this data tell us?
- recency: when was this last checked?
- uncertainty: what might change?

GOVERNANCE LAYER (who can do what?)
- authority_boundary: who decides about this? (founder-only, agent-propose-owner-decides, agent-automated)
- decision_rights: who can modify this data?
- access_level: who can see this data?
- approval_required: does changing this need sign-off?

TEMPORAL LAYER (when does this matter?)
- valid_from: when does this become relevant?
- valid_until: when does this expire or need review?
- review_cadence: how often should this be reviewed?
- last_reviewed: when was this last checked?

SCHEMA LAYER (what shape is this data?)
- schema_version: what version of the data structure?
- validation_rules: what makes this data valid?
- transformation_rules: how does this data connect to other entities?
```

The critical insight: **assumptions** are first-class citizens in this model, not throwaway notes. Every strategy, goal, and decision is built on assumptions, and those assumptions have confidence levels, provenance, and review cadences. When an assumption is challenged (which it will be), the system can trace which strategies depend on it and flag them for review.

Let me generate the TypeDB schema for this:

```schema
# PRISM Schema for Small Business Agentic Operating System
# Launch Project - Phase 1 through 5

define

## ============================================================
## ATTRIBUTE TYPES (52 attributes)
## ============================================================

# --- Identity & Reference Attributes ---
string agent-id @key
string entity-id @key
string relation-id @key
string event-id @key
string knowledge-id @key
string intention-id @key
string scope-id @key
string actor-id @key

# --- Descriptive Attributes ---
string name
string display-name
string description
string type
string category
string subcategory
string status
string phase
string session-type

# --- Content Attributes ---
string content
string summary
string reasoning
string source
string url
string file-path
string format

# --- Quantitative Attributes ---
double confidence
double relevance-score
double financial-amount
integer priority
integer review-cadence-days

# --- Temporal Attributes ---
datetime created-at
datetime updated-at
datetime reviewed-at
datetime valid-from
datetime valid-until
datetime completed-at

# --- Epistemic Attributes ---
string provenance
string assumptions
string limitations
string uncertainty
string epistemic-confidence
string epistemic-level

# --- Governance Attributes ---
string authority-boundary
string decision-rights
string access-level
string approval-required
string governance-level

# --- Schema Attributes ---
string schema-version
string validation-rules

# --- Scope Attributes ---
string scope-type
string scope-description
string isolation-level

# --- Actor Attributes ---
string actor-type
string actor-role
string permissions

# --- Intention Attributes ---
string intention-type
string intention-direction

# --- Entity Subtype Attributes ---
string entity-subtype
string industry
string business-model
string tone
string personality
string visual-direction
string pricing-model
string growth-model
string innovation-horizon
string channel

# --- Relation Subtype Attributes ---
string relation-subtype
string strength
string direction

# --- Event Subtype Attributes ---
string event-subtype
string trigger-condition
string recovery-path

# --- Knowledge Subtype Attributes ---
string knowledge-subtype
string knowledge-source

# --- Financial Attributes ---
string currency
string revenue-model
string cost-structure

# --- Progressive Autonomy ---
string autonomy-level

# --- Risk Attributes ---
string risk-level
string risk-type

# --- Competitor Attributes ---
string competitor-type
string competitor-positioning

# --- Customer Attributes ---
string persona-type
string journey-stage

# --- Goal Attributes ---
string goal-horizon
string goal-category
string okr-type
string measurement-unit
string target-value
string current-value
string unit-of-measure


## ============================================================
## ENTITY TYPES
## ============================================================

# --- Abstract Base Types ---

entity prism-artefact
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns created-at
  owns updated-at
  owns reviewed-at
  owns schema-version
  # Epistemic Layer
  owns provenance
  owns epistemic-confidence
  owns epistemic-level
  owns assumptions
  owns limitations
  owns uncertainty
  # Governance Layer
  owns authority-boundary
  owns decision-rights
  owns access-level
  owns approval-required
  # Temporal Layer
  owns valid-from
  owns valid-until
  owns review-cadence-days
  # Validation
  owns validation-rules

entity prism-relation
  owns relation-id @key
  owns relation-subtype
  owns strength
  owns direction
  owns description
  owns created-at
  owns updated-at
  # Epistemic Layer
  owns provenance
  owns epistemic-confidence
  owns assumptions
  # Governance Layer
  owns authority-boundary
  owns access-level

# --- PRISM Dimensions ---

entity scope
  owns scope-id @key
  owns name
  owns scope-type
  owns scope-description
  owns isolation-level
  owns created-at
  owns updated-at

entity actor
  owns actor-id @key
  owns name
  owns actor-type
  owns actor-role
  owns permissions
  owns description
  owns created-at
  owns updated-at

# --- Business Entities (Entity Dimension) ---

entity founder-profile
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns phase
  owns created-at
  owns updated-at
  owns reviewed-at
  owns schema-version
  owns provenance
  owns epistemic-confidence
  owns epistemic-level
  owns assumptions
  owns limitations
  owns uncertainty
  owns authority-boundary
  owns decision-rights
  owns access-level
  owns approval-required
  owns valid-from
  owns valid-until
  owns review-cadence-days
  owns validation-rules

entity business-profile
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns phase
  owns industry
  owns business-model
  owns revenue-model
  owns created-at
  owns updated-at
  owns reviewed-at
  owns schema-version
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns valid-from
  owns valid-until
  owns review-cadence-days

entity brand-attribute
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns tone
  owns personality
  owns visual-direction
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns authority-boundary
  owns review-cadence-days

entity strategic-goal
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns goal-horizon
  owns goal-category
  owns target-value
  owns current-value
  owns measurement-unit
  owns created-at
  owns updated-at
  owns reviewed-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns valid-from
  owns valid-until
  owns review-cadence-days

entity value-proposition
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns review-cadence-days

entity customer-persona
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns persona-type
  owns journey-stage
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns review-cadence-days

entity market
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns limitations
  owns authority-boundary
  owns review-cadence-days

entity competitor
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns competitor-type
  owns competitor-positioning
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns review-cadence-days

entity product
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns pricing-model
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns authority-boundary
  owns review-cadence-days

entity campaign
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns channel
  owns created-at
  owns updated-at
  owns provenance
  owns authority-boundary

entity workflow
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns created-at
  owns updated-at
  owns authority-boundary
  owns access-level

entity financial-blueprint
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns currency
  owns revenue-model
  owns cost-structure
  owns financial-amount
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns review-cadence-days

entity team-member
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns created-at
  owns updated-at
  owns authority-boundary

entity agent-permission
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns autonomy-level
  owns authority-boundary
  owns created-at
  owns updated-at

entity business-rule
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns created-at
  owns updated-at
  owns authority-boundary
  owns review-cadence-days

entity decision-log
  owns entity-id @key
  owns display-name
  owns description
  owns reasoning
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence

entity assumption
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns epistemic-confidence
  owns provenance
  owns assumptions
  owns uncertainty
  owns authority-boundary
  owns valid-from
  owns valid-until
  owns review-cadence-days
  owns created-at
  owns updated-at
  owns reviewed-at

entity opportunity-pipeline
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns priority
  owns risk-level
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns assumptions
  owns authority-boundary
  owns review-cadence-days

entity initiative
  owns entity-id @key
  owns display-name
  owns description
  owns type
  owns status
  owns innovation-horizon
  owns created-at
  owns updated-at
  owns provenance
  owns authority-boundary

entity intention
  owns intention-id @key
  owns display-name
  owns description
  owns type
  owns intention-type
  owns intention-direction
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns authority-boundary
  owns valid-from
  owns valid-until
  owns review-cadence-days

entity knowledge-item
  owns knowledge-id @key
  owns display-name
  owns description
  owns type
  owns knowledge-subtype
  owns knowledge-source
  owns content
  owns summary
  owns source
  owns url
  owns file-path
  owns format
  owns created-at
  owns updated-at
  owns provenance
  owns epistemic-confidence
  owns epistemic-level
  owns assumptions
  owns limitations
  owns uncertainty
  owns relevance-score
  owns reviewed-at
  owns review-cadence-days


## ============================================================
## RELATION TYPES
## ============================================================

relation scope-contains
  relates scope
  relates artefact

relation actor-owns
  relates actor
  relates artefact

relation actor-authorised-for
  relates actor
  relates artefact
  owns permissions

relation founder-defines
  relates founder-profile
  relates artefact

relation goal-driven-by
  relates strategic-goal
  relates assumption

relation goal-supports
  relates strategic-goal
  relates strategic-goal

relation persona-served-by
  relates customer-persona
  relates product

relation competitor-contrasts-with
  relates competitor
  relates value-proposition

relation strategy-informs
  relates strategic-goal
  relates campaign

relation workflow-owned-by
  relates workflow
  relates team-member

relation agent-authorized-for
  relates agent-permission
  relates workflow

relation assumption-underpins
  relates assumption
  relates artefact

relation opportunity-maps-to
  relates opportunity-pipeline
  relates strategic-goal

relation initiative-advances
  relates initiative
  relates strategic-goal

relation intention-constrains
  relates intention
  relates artefact

relation knowledge-informs
  relates knowledge-item
  relates artefact

relation phase-produces
  relates scope
  relates artefact
  owns phase

relation depends-on
  relates artefact
  relates artefact
  owns strength

relation evolves-from
  relates artefact
  relates artefact


## ============================================================
## RULES (Computation)
## ============================================================

rule assumption-risk-flag
  when
    $a isa assumption
    has epistemic-confidence $conf
  then
    $a has risk-level
      if $conf < 0.4 then "high"
      else if $conf < 0.7 then "medium"
      else "low";

rule specification-aging-alert
  when
    $a isa prism-artefact
    has reviewed-at $reviewed
    has review-cadence-days $cadence
  then
    $a has status
      if days-between($reviewed, now()) > $cadence then "needs-review"
      else $a.status;
```

Now let me generate the key implementation files:

```python
# agent_orchestrators.py
# Four orchestrator agents for the Small Business Agentic OS
# Each orchestrator follows CAWDP identity-first design

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.storage.postgres import PostgresDb
from agno.tools import Toolkit

# Shared model
MODEL = Ollama(id="glm-5.1:cloud")

# Shared storage
DB_URL = "postgresql://localhost:5432/edgeai"
STORAGE = PostgresDb(url=DB_URL, schema="agent_metadata")


# ============================================================
# COMMERCIAL ORCHESTRATOR
# "Is this commercially sound?"
# Class: Assessor (bridge-oriented)
# Never: commits to financial decisions, finalizes contracts, 
#        overrides risk assessments
# Authority: proposes, never decides
# ============================================================

commercial_orchestrator = Agent(
    name="Commercial Orchestrator",
    model=MODEL,
    storage=STORAGE,
    description="""You are the Commercial Orchestrator for a small business.

IDENTITY: You assess whether business decisions are commercially sound. 
You prepare judgment — the founder makes judgment.

STANCE TOWARD POSSIBILITY: Bridge-oriented. You help the founder 
evaluate commercial feasibility of ideas, but you NEVER decide what 
to pursue or what to reject. You present options with benefits and 
risks. The founder chooses.

WHAT WOULD VIOLATE YOUR IDENTITY: Making financial commitments, 
finalizing contracts, or making risk decisions on behalf of the 
founder. You assess, you never commit.

WHAT WOULD MAKE YOU WRONG: Presenting only one option as if it's the 
only choice, hiding risks to make an option look better, or presenting 
financial projections without confidence ranges and assumptions.

AUTHORITY BOUNDARIES:
- CAN: Research market data, calculate financial scenarios, flag risks, 
  prepare options with benefits and risks
- CANNOT: Make financial commitments, finalize contracts, approve 
  expenditures, override founder risk tolerance
- MUST FLAG: Any decision above the founder's stated risk tolerance, 
  any financial projection without confidence ranges

PROGRESSIVE AUTONOMY:
- Financial data gathering: can be autonomous (Extractor role)
- Financial analysis: proposes, founder reviews (Assessor role)  
- Financial commitments: founder only, never agent
- Risk assessment: proposes, founder decides

EPISTEMIC METADATA: Every financial figure, market estimate, or 
competitive analysis MUST include confidence level, provenance, 
assumptions made, and what you DON'T know.

DECISION PRESENTATION: Always present 2-4 options with benefits and 
risks. Never present a single option as the only choice.""",
    
    tools=[...],  # Commercial domain tools
    add_context=True,
)


# ============================================================
# GROWTH ORCHESTRATOR
# "Should we pursue this?"
# Class: Assessor (possibility-oriented early, bridge-oriented later)
# Never: commits to marketing spend, finalizes messaging, 
#        makes customer promises
# ============================================================

growth_orchestrator = Agent(
    name="Growth Orchestrator",
    model=MODEL,
    storage=STORAGE,
    description="""You are the Growth Orchestrator for a small business.

IDENTITY: You assess whether growth opportunities are worth pursuing. 
You prepare options — the founder makes the call.

STANCE TOWARD POSSIBILITY: Possibility-oriented early (discovering 
new markets, customer segments, channels), bridge-oriented later 
(evaluating specific opportunities against business constraints).

WHAT WOULD VIOLATE YOUR IDENTITY: Committing marketing budget, 
finalizing brand messaging, making promises to customers, or choosing 
target segments without founder approval.

WHAT WOULD MAKE YOU WRONG: Presenting growth options without 
considering resource constraints, recommending pursuit without 
flagging risks, or assuming market data is more certain than it is.

AUTHORITY BOUNDARIES:
- CAN: Research customer segments, analyze market opportunities, 
  prepare messaging options, suggest channel strategies
- CANNOT: Commit marketing spend, finalize messaging, make customer 
  promises, choose target segments without founder approval
- MUST FLAG: Any opportunity that exceeds stated resource constraints, 
  any customer segment assumption not validated by data

PROGRESSIVE AUTONOMY:
- Market research: can be autonomous (Extractor role)
- Customer persona development: proposes, founder validates (Assessor)
- Marketing spend: founder only
- Brand messaging: proposes, founder approves

EPISTEMIC METADATA: Every market size estimate, customer insight, or 
competitive positioning claim MUST include confidence level, 
provenance, assumptions, and limitations.

DECISION PRESENTATION: Always present 2-4 options with benefits and 
risks. Never present a single path as the only option.""",
    
    tools=[...],  # Growth domain tools
    add_context=True,
)


# ============================================================
# VENTURE ORCHESTRATOR
# "Is this worth building?"
# Class: Assessor (bridge-oriented)
# Never: commits to product decisions, finalizes roadmaps,
#        makes build/buy decisions
# ============================================================

venture_orchestrator = Agent(
    name="Venture Orchestrator",
    model=MODEL,
    storage=STORAGE,
    description="""You are the Venture Orchestrator for a small business.

IDENTITY: You assess whether products, features, and innovations are 
worth building. You prepare analysis — the founder decides what to build.

STANCE TOWARD POSSIBILITY: Bridge-oriented. You help evaluate the 
feasibility and desirability of ideas, but the founder decides what 
to pursue and what to shelve.

WHAT WOULD VIOLATE YOUR IDENTITY: Making product commitments, 
finalizing roadmaps, or deciding what to build without founder input.

WHAT WOULD MAKE YOU WRONG: Recommending a product direction without 
evidence, presenting a build plan without resource constraints, or 
assuming technical feasibility without validation.

AUTHORITY BOUNDARIES:
- CAN: Analyze product ideas, evaluate technical feasibility, 
  prepare build/buy/defer options, research innovation opportunities
- CANNOT: Commit to product roadmaps, make build/buy decisions, 
  allocate development resources
- MUST FLAG: Any product decision that exceeds stated budget, any 
  innovation without market validation

PROGRESSIVE AUTONOMY:
- Feature research: can be autonomous (Extractor)
- Product analysis: proposes, founder reviews (Assessor)
- Roadmap decisions: founder only
- Build commitments: founder only

EPISTEMIC METADATA: Every product estimate, feasibility assessment, 
or market validation MUST include confidence, provenance, 
assumptions, and what remains uncertain.

DECISION PRESENTATION: Always present 2-4 options with benefits 
and risks. Never present a single direction as the only path.""",
    
    tools=[...],  # Venture domain tools
    add_context=True,
)


# ============================================================
# STEWARDSHIP ORCHESTRATOR
# "Is this safe and responsible?"
# Class: Assessor (constraint-oriented)
# Never: makes risk decisions, approves compliance, 
#        overrides founder risk tolerance
# ============================================================

stewardship_orchestrator = Agent(
    name="Stewardship Orchestrator",
    model=MODEL,
    storage=STORAGE,
    description="""You are the Stewardship Orchestrator for a small business.

IDENTITY: You assess whether business decisions are safe and 
responsible. You flag risks — the founder decides what level of 
risk is acceptable.

STANCE TOWARD POSSIBILITY: Constraint-oriented. Your job is to 
identify risks, flag compliance requirements, and ensure the 
founder has full visibility of potential downsides. You NEVER 
minimize risk to make an option look more attractive.

WHAT WOULD VIOLATE YOUR IDENTITY: Minimizing risks, approving 
compliance without verification, making risk decisions on behalf 
of the founder, or presenting options without flagging downsides.

WHAT WOULD MAKE YOU WRONG: Failing to flag a compliance risk, 
presenting a risk assessment without confidence levels, or not 
flagging when information is insufficient to make a judgment.

AUTHORITY BOUNDARIES:
- CAN: Research regulatory requirements, flag risks, prepare 
  compliance checklists, assess impact of decisions
- CANNOT: Approve compliance, make risk decisions, override founder 
  risk tolerance, minimize risks to make options look better
- MUST FLAG: Every compliance requirement, every risk that exceeds 
  the founder's stated tolerance, every area where information is 
  insufficient

PROGRESSIVE AUTONOMY:
- Regulatory research: can be autonomous (Extractor)
- Risk flagging: proposes, founder reviews (Assessor)
- Compliance decisions: founder only
- Risk acceptance: founder only

EPISTEMIC METADATA: Every risk assessment, compliance claim, or 
regulatory interpretation MUST include confidence, provenance, 
assumptions, and limitations. When you're uncertain, say so 
explicitly. Uncertainty is not weakness — it's honesty.

DECISION PRESENTATION: Always present risks alongside benefits. 
Never present only the upside. Every option includes what could 
go wrong and how likely it is.

CRITICAL: You are the founder's safety net. If you don't flag a 
risk, no one else will. Your value is in what you catch, not in 
what you approve.""",
    
    tools=[...],  # Stewardship domain tools
    add_context=True,
)
```

Now let me do the complementarity analysis — this is crucial. Every task in the launch project needs an H/A/S allocation:

```python
# complementarity_analysis.py
# H/A/S allocation for the Launch Project
# H = Human-only, A = Agent-primary (prepares, human decides), 
# S = System-automated

COMPLEMENTARITY_ALLOCATION = {
    # Phase 1: Founder Intelligence
    "Phase 1": {
        "life_career_history": {
            "allocation": "A+H",  # Agent guides session, human provides content
            "agent_role": "Extractor — captures, structures, never judges",
            "human_role": "Provides personal history, context, meaning",
            "authority": "Human decides what to share and what to withhold",
            "failure_mode": "Agent interpreting instead of capturing",
            "reversibility": "High — can always add more later",
        },
        "values_elicitation": {
            "allocation": "H+H",  # Human-primary, agent supports
            "agent_role": "Mirror — reflects, never defines values",
            "human_role": "Discovers and declares own values",
            "authority": "Human-only — founder's values are not negotiable",
            "failure_mode": "Agent suggesting values instead of reflecting",
            "reversibility": "High — values can evolve, but origin is human",
        },
        "strengths_skills_inventory": {
            "allocation": "A+H",  # Agent researches, human validates
            "agent_role": "Extractor — gathers from multiple sources",
            "human_role": "Validates, corrects, adds tacit knowledge",
            "authority": "Human confirms — only the founder knows their strengths",
            "failure_mode": "Agent missing tacit strengths that aren't documented",
            "reversibility": "High — can always add more",
        },
        "risk_tolerance_assessment": {
            "allocation": "H",  # Human-only
            "agent_role": "None — risk tolerance is non-negotiable human judgment",
            "human_role": "Declares own risk tolerance",
            "authority": "Human-only — foundational constraint",
            "failure_mode": "Agent suggesting risk levels instead of discovering them",
            "reversibility": "Medium — can be revisited but shouldn't be overriden by agent",
        },
        "network_relationships_audit": {
            "allocation": "A+H",  # Agent structures, human provides
            "agent_role": "Aggregator — structures and organizes network data",
            "human_role": "Provides relationships, context, trust levels",
            "authority": "Human validates — only founder knows relationship quality",
            "failure_mode": "Agent categorizing relationships without human context",
            "reversibility": "High",
        },
        "financial_position_baseline": {
            "allocation": "A+H",  # Agent structures, human provides sensitive info
            "agent_role": "Measurer — structures financial data with ranges",
            "human_role": "Provides actual financial data",
            "authority": "Human-only for actual figures, agent provides frameworks",
            "failure_mode": "Agent making financial assumptions",
            "reversibility": "Medium — financial realities don't change easily",
        },
        "time_capacity_map": {
            "allocation": "A+H",  # Agent structures, human provides
            "agent_role": "Extractor — captures time data",
            "human_role": "Provides realistic time allocation",
            "authority": "Human validates — only founder knows their actual availability",
            "failure_mode": "Agent assuming more time than founder has",
            "reversibility": "High",
        },
    },
    
    # Phase 2: Vision & Foundation
    "Phase 2": {
        "purpose_workshop": {
            "allocation": "H",  # Human-only — foundational meaning
            "agent_role": "Mirror — reflects, never defines purpose",
            "human_role": "Discovers and articulates purpose",
            "authority": "Human-only",
            "failure_mode": "Agent suggesting purpose instead of reflecting",
            "reversibility": "High — purpose can evolve",
        },
        "vision_articulation": {
            "allocation": "A+H",  # Agent structures, human dreams
            "agent_role": "Mirror — asks prompting questions, organizes responses",
            "human_role": "Imagines and declares vision",
            "authority": "Human-only for vision content, agent for structure",
            "failure_mode": "Agent limiting vision to what seems 'realistic'",
            "reversibility": "High",
        },
        "values_definition": {
            "allocation": "H",  # Human-only — non-negotiable
            "agent_role": "Mirror — reflects patterns, never defines values",
            "human_role": "Declares core values",
            "authority": "Human-only",
            "failure_mode": "Agent suggesting values instead of discovering them",
            "reversibility": "Low — values are foundational",
        },
        "anti_vision_session": {
            "allocation": "H",  # Human-only — what must NEVER happen
            "agent_role": "Mirror — reflects fears and boundaries",
            "human_role": "Declares what's unacceptable",
            "authority": "Human-only — boundaries are non-negotiable",
            "failure_mode": "Agent softening boundaries or suggesting they're negotiable",
            "reversibility": "Low — these are guardrails",
        },
        "goal_architecture": {
            "allocation": "A+H",  # Agent structures, human decides
            "agent_role": "Assessor — identifies conflicts, dependencies, gaps",
            "human_role": "Sets goals and priorities",
            "authority": "Human decides goals, agent identifies implications",
            "failure_mode": "Agent setting goals instead of identifying implications",
            "reversibility": "Medium — goals can shift but shouldn't be agent-driven",
        },
    },
    
    # Phase 3: Strategic Intelligence
    "Phase 3": {
        "market_research": {
            "allocation": "A",  # Agent-primary
            "agent_role": "Extractor — gathers market data with epistemic metadata",
            "human_role": "Validates relevance, interprets for local context",
            "authority": "Agent gathers, human validates",
            "failure_mode": "Agent presenting estimates as facts, or missing local context",
            "reversibility": "Medium — market data changes",
        },
        "customer_intelligence": {
            "allocation": "A+H",  # Agent researches, human validates
            "agent_role": "Extractor + Assessor — gathers data, identifies patterns",
            "human_role": "Validates personas, adds tacit customer knowledge",
            "authority": "Human validates personas, agent identifies patterns",
            "failure_mode": "Agent creating personas without founder's customer insight",
            "reversibility": "Medium",
        },
        "competitive_intelligence": {
            "allocation": "A",  # Agent-primary
            "agent_role": "Extractor — gathers competitor data",
            "human_role": "Validates positioning, adds local competitive knowledge",
            "authority": "Agent gathers, human interprets",
            "failure_mode": "Agent presenting competitor analysis without confidence ranges",
            "reversibility": "Low — competitive data needs constant refreshing",
        },
        "swot_assumptions": {
            "allocation": "A+H",  # Agent structures, human assesses
            "agent_role": "Aggregator — compiles SWOT from gathered data",
            "human_role": "Validates, prioritizes, flags what's missing",
            "authority": "Human validates SWOT, agent structures it",
            "failure_mode": "Agent making SWOT judgments instead of compiling evidence",
            "reversibility": "Medium",
        },
    },
    
    # Phase 4: Strategy Suite
    "Phase 4": {
        # ALL strategies: Agent prepares options, human decides
        "business_strategy": {
            "allocation": "A+H",
            "agent_role": "Assessor — prepares options with benefits/risks",
            "human_role": "Decides strategic direction",
            "authority": "Human decides, agent prepares",
            "failure_mode": "Agent recommending one strategy instead of presenting options",
            "reversibility": "Low — strategic direction is foundational",
        },
        "product_strategy": {
            "allocation": "A+H",
            "agent_role": "Assessor — prepares options with benefits/risks",
            "human_role": "Decides product direction",
            "authority": "Human decides, agent prepares",
            "failure_mode": "Agent designing products instead of presenting options",
            "reversibility": "Medium",
        },
        "brand_strategy": {
            "allocation": "A+H",
            "agent_role": "Assessor — prepares options with brand rationale",
            "human_role": "Decides brand identity",
            "authority": "Human decides — brand is deeply personal",
            "failure_mode": "Agent defining brand instead of reflecting founder's identity",
            "reversibility": "Low — brand changes are costly",
        },
        # Marketing, GTM, Competitive, Growth, Innovation, Media strategies
        # ALL follow the same pattern: Agent prepares, human decides
    },
    
    # Phase 5: Operational Blueprint
    "Phase 5": {
        "legal_structure": {
            "allocation": "S",  # System-automated where possible
            "agent_role": "Extractor — provides regulatory requirements",
            "human_role": "Makes legal decisions (with professional advice)",
            "authority": "Human-only for legal decisions",
            "failure_mode": "Agent providing legal advice instead of information",
            "reversibility": "Low — legal structure is hard to change",
        },
        "agent_configuration": {
            "allocation": "S+A",  # System-automated with agent guidance
            "agent_role": "Assessor — recommends permissions based on risk levels",
            "human_role": "Approves all agent permissions",
            "authority": "Human approves — founder retains all authority decisions",
            "failure_mode": "Agent setting its own permissions without founder approval",
            "reversibility": "High — permissions can always be tightened",
        },
        "knowledge_base_seeding": {
            "allocation": "A",  # Agent-primary
            "agent_role": "Extractor — ingests and structures documents",
            "human_role": "Validates accuracy and completeness",
            "authority": "Agent structures, human validates",
            "failure_mode": "Agent ingesting without proper epistemic metadata",
            "reversibility": "High",
        },
    },
}
```

Now the UI design. This is where type collision resolution, progressive disclosure, and the Decision Presentation Pattern come together:

```python
# ui_interaction_design.py
# How the founder EXPERIENCES the launch project
# Not a checklist — a guided journey

from enum import Enum
from typing import Optional

# ============================================================
# POSSIBILITY GRADIENT — visual shift across phases
# Phase 1-2: expansive, warm, exploratory
# Phase 3: transitional, balanced
# Phase 4-5: concrete, structured, decisive
# ============================================================

class PossibilityOrientation(str, Enum):
    EXPANSIVE = "expansive"      # Phases 1-2: possibility-oriented
    TRANSITIONAL = "transitional"  # Phase 3: bridge-oriented
    CONSTRAINED = "constrained"    # Phases 4-5: constraint-oriented

PHASE_VISUAL = {
    1: {"orientation": PossibilityOrientation.EXPANSIVE, 
        "accent": "#D4A853",  # Warm gold — discovery
        "prompt_style": "open",  # Open-ended questions, reflective
        "interaction": "conversational"},  # Free-form conversation
    2: {"orientation": PossibilityOrientation.EXPANSIVE, 
        "accent": "#D4A853",
        "prompt_style": "reflective",  # Mirror back what they said
        "interaction": "workshop"},  # Guided workshop with choices
    3: {"orientation": PossibilityOrientation.TRANSITIONAL,
        "accent": "#3B82F6",  # Blue — analysis
        "prompt_style": "analytical",  # Data-driven questions
        "interaction": "structured"},  # Structured sessions with data
    4: {"orientation": PossibilityOrientation.CONSTRAINED,
        "accent": "#0EA5E9",  # Teal — decision
        "prompt_style": "decisive",  # Decision-focused
        "interaction": "decision-heavy"},  # Multiple decisions per session
    5: {"orientation": PossibilityOrientation.CONSTRAINED,
        "accent": "#10B981",  # Green — operational
        "prompt_style": "configurational",  # Configuration-focused
        "interaction": "checklist"},  # Structured setup with verification
}


# ============================================================
# INTERACTION MODES — different cognitive modes need different inputs
# Type collision resolution at the input surface
# ============================================================

class InteractionMode(str, Enum):
    NARRATIVE = "narrative"       # Life history, values, purpose
    BOUNDARY = "boundary"         # Non-negotiables, anti-vision
    EXPLORATORY = "exploratory"   # Market research, competitive analysis
    EVALUATIVE = "evaluative"    # SWOT, strategic choices
    CONFIGURATION = "configuration"  # Agent permissions, SOPs
    VERIFICATION = "verification"  # Confirming agent suggestions

# Map tasks to interaction modes (type collision resolution)
TASK_INTERACTION_MODE = {
    # Phase 1: Narrative + Boundary modes
    "life_career_history": InteractionMode.NARRATIVE,
    "values_elicitation": InteractionMode.BOUNDARY,
    "strengths_skills_inventory": InteractionMode.NARRATIVE,
    "risk_tolerance_assessment": InteractionMode.BOUNDARY,
    "network_relationships_audit": InteractionMode.CONFIGURATION,
    "financial_position_baseline": InteractionMode.CONFIGURATION,
    "time_capacity_map": InteractionMode.CONFIGURATION,
    
    # Phase 2: Narrative + Boundary modes (possibility-oriented)
    "purpose_workshop": InteractionMode.NARRATIVE,
    "vision_articulation": InteractionMode.NARRATIVE,
    "values_definition": InteractionMode.BOUNDARY,
    "anti_vision_session": InteractionMode.BOUNDARY,
    "goal_architecture": InteractionMode.EVALUATIVE,
    
    # Phase 3: Exploratory + Evaluative modes (bridge-oriented)
    "market_research": InteractionMode.EXPLORATORY,
    "customer_intelligence": InteractionMode.EXPLORATORY,
    "competitive_intelligence": InteractionMode.EXPLORATORY,
    "swot_assumptions": InteractionMode.EVALUATIVE,
    
    # Phase 4: Evaluative mode (constraint-oriented)
    "business_strategy": InteractionMode.EVALUATIVE,
    "product_strategy": InteractionMode.EVALUATIVE,
    "brand_strategy": InteractionMode.EVALUATIVE,
    "marketing_strategy": InteractionMode.EVALUATIVE,
    "gtm_strategy": InteractionMode.EVALUATIVE,
    "competitive_strategy": InteractionMode.EVALUATIVE,
    "growth_strategy": InteractionMode.EVALUATIVE,
    "innovation_strategy": InteractionMode.EXPLORATORY,
    "media_content_strategy": InteractionMode.EXPLORATORY,
    
    # Phase 5: Configuration + Verification modes (constraint-oriented)
    "legal_structure": InteractionMode.CONFIGURATION,
    "operational_processes": InteractionMode.CONFIGURATION,
    "financial_blueprint": InteractionMode.CONFIGURATION,
    "agent_configuration": InteractionMode.CONFIGURATION,
    "launch_readiness": InteractionMode.VERIFICATION,
}


# ============================================================
# SESSION DESIGN — one question at a time, decisions not walls
# ============================================================

SESSION_DESIGNS = {
    "values_elicitation": {
        "mode": InteractionMode.BOUNDARY,
        "phase_visual": PHASE_VISUAL[1],
        "agent_role": "Mirror",
        "agent_instruction": """You are helping the founder discover 
their core values. You MIRROR what they say, you NEVER suggest values.

Use the Decision Presentation Pattern:
1. After they share a value, reflect it back and ask which of 2-3 
   behavioural descriptions fits best
2. Present options, never ask open questions like "tell me your values"
3. When they identify a non-negotiable, mark it with higher authority 
   boundary (founder-only)

BAD: "What are your values?" (blank page problem)
GOOD: "You mentioned quality matters. Which describes your non-negotiable 
      better? (a) Never ship something I'm not proud of, or 
      (b) Quality is aspirational but speed sometimes wins"

Remember: values are NON-NEGOTIABLE. The founder defines them, 
you reflect and structure them. You NEVER suggest what values should be.""",
        
        "output_entities": ["business_rule", "brand_attribute"],
        "output_intentions": ["founder_constraint", "brand_guardrail"],
        "epistemic_metadata": {
            "confidence": "high",  # Founder stated values are high confidence
            "provenance": "founder_session",
            "assumptions": "Values stated match actual behaviour",
            "limitations": "Values may evolve as business grows",
            "recency": "session_date",
            "uncertainty": "Behavioural alignment needs validation over time",
        },
        "human_gates": [
            "value_confirmation",  # Founder confirms each value
            "non_negotiable_marking",  # Founder marks which are non-negotiable
        ],
    },
    
    "market_research": {
        "mode": InteractionMode.EXPLORATORY,
        "phase_visual": PHASE_VISUAL[3],
        "agent_role": "Extractor",
        "agent_instruction": """You are gathering market intelligence. You 
EXTRACT data, you NEVER make market decisions.

Use the Decision Presentation Pattern:
1. Present market data with confidence ranges
2. When estimating market size, always show the range and source
3. Present 2-3 interpretations of data, not one conclusion

BAD: "The market is worth $2B"
GOOD: "Three sources estimate the market at $1.5-2.5B. The lower estimate 
      (IBISWorld) is more conservative, the upper (Gartner) includes adjacent 
      markets. Which range is most relevant to your business?"

Every figure MUST include:
- Confidence level (how sure are we?)
- Source (where did this come from?)
- Assumptions (what are we assuming?)
- What we DON'T know""",
        
        "output_entities": ["market", "market_trend"],
        "output_intentions": ["regulatory_requirement"],
        "epistemic_metadata": {
            "confidence": "variable",  # Market data varies widely
            "provenance": "external_research",
            "assumptions": "Market data is current and relevant",
            "limitations": "Estimates vary by source and methodology",
            "recency": "gathering_date",
            "uncertainty": "Market conditions change rapidly",
        },
        "human_gates": [
            "market_scope_confirmation",  # Founder confirms market definition
            "relevance_validation",  # Founder validates relevance to their business
        ],
    },
    
    "strategy_session": {
        "mode": InteractionMode.EVALUATIVE,
        "phase_visual": PHASE_VISUAL[4],
        "agent_role": "Assessor",
        "agent_instruction": """You are helping the founder develop a strategy. 
You PREPARE options, you NEVER decide the strategy.

Use the Decision Presentation Pattern for EVERY strategic choice:
1. Present 2-4 options with explicit benefits and risks
2. Each option includes what could go wrong and how likely it is
3. Always allow "custom option" — the founder knows their business best

BAD: "You should focus on niche marketing"
GOOD: "Three strategic directions are viable given your market position:

Option A: Niche Focus — Serve [segment] deeply
  Benefits: (1) Clear positioning, (2) Lower customer acquisition cost
  Risks: (1) Small total market, (2) Vulnerable to niche shifts

Option B: Broad Appeal — Serve multiple segments
  Benefits: (1) Larger addressable market, (2) Revenue diversification
  Risks: (1) Higher acquisition costs, (2) Weaker positioning

Option C: Platform Play — Enable others to serve the market
  Benefits: (1) Scalable, (2) Network effects
  Risks: (1) Complex to build, (2) Longer time to revenue

Which direction resonates most, or would you like to explore a different path?"

CRITICAL: You are the ASSESSOR, not the DECIDER. You prepare, 
the founder decides. Every strategy recommendation must include 
confidence level, assumptions, and what you DON'T know.""",
        
        "output_entities": ["strategic_goal", "value_proposition"],
        "output_intentions": ["business_goal", "founder_constraint"],
        "epistemic_metadata": {
            "confidence": "medium",  # Strategy has inherent uncertainty
            "provenance": "agent_analysis_with_founder_validation",
            "assumptions": "Based on available market data and founder context",
            "limitations": "Strategy requires validation through execution",
            "recency": "session_date",
            "uncertainty": "Market conditions and competitive landscape may change",
        },
        "human_gates": [
            "strategy_direction",  # Founder chooses strategic direction
            "strategy_approval",   # Founder approves final strategy
        ],
    },
}
```

Let me also create the progressive autonomy schedule and the assumption tracking system, which are critical CAWDP elements:

```python
# progressive_autonomy.py
# Progressive autonomy schedule for each agent domain
# Shadow → Advisory → Supervised → Autonomous

PROGRESSIVE_AUTONOMY = {
    "commercial_orchestrator": {
        "financial_data_gathering": {
            "shadow": "Agent observes founder gathering data, learns patterns",
            "advisory": "Agent suggests data sources, founder confirms",
            "supervised": "Agent gathers data, founder reviews before it enters KB",
            "autonomous": "Agent gathers routine data, flags anomalies only",
            "current_level": "shadow",
            "promotion_criteria": "Accuracy ≥ 90% over 2 weeks, no missed sources",
            "never_autonomous": False,
        },
        "financial_analysis": {
            "shadow": "Agent observes founder's analysis methods",
            "advisory": "Agent prepares analysis with options, founder reviews",
            "supervised": "Agent produces analysis, founder approves",
            "autonomous": "Agent produces routine analysis (cash flow, margins), flags unusual",
            "current_level": "shadow",
            "promotion_criteria": "Analysis accuracy ≥ 95%, founder override rate < 10%",
            "never_autonomous": False,
        },
        "financial_commitments": {
            "shadow": "N/A — this is never agent-automated",
            "advisory": "N/A",
            "supervised": "N/A",
            "autonomous": "NEVER — founder-only for all financial commitments",
            "current_level": "NEVER_AUTONOMOUS",
            "promotion_criteria": "N/A",
            "never_autonomous": True,
        },
    },
    
    "growth_orchestrator": {
        "market_research": {
            "shadow": "Agent observes founder research methods",
            "advisory": "Agent suggests research sources, founder confirms",
            "supervised": "Agent conducts research, founder reviews",
            "autonomous": "Agent conducts routine research, flags significant changes",
            "current_level": "shadow",
            "promotion_criteria": "Research relevance ≥ 85%, no critical misses over 2 weeks",
            "never_autonomous": False,
        },
        "customer_persona_development": {
            "shadow": "Agent observes founder's persona descriptions",
            "advisory": "Agent suggests persona attributes based on data",
            "supervised": "Agent drafts personas, founder validates",
            "autonomous": "NEVER — personas require founder validation always",
            "current_level": "shadow",
            "promotion_criteria": "Persona accuracy ≥ 90% (founder-rated)",
            "never_autonomous": True,  # Customer understanding always needs human validation
        },
        "marketing_spend": {
            "shadow": "N/A",
            "advisory": "N/A",
            "supervised": "N/A",
            "autonomous": "NEVER — founder-only for all marketing spend",
            "current_level": "NEVER_AUTONOMOUS",
            "promotion_criteria": "N/A",
            "never_autonomous": True,
        },
    },
    
    "venture_orchestrator": {
        "product_research": {
            "shadow": "Agent observes founder research methods",
            "advisory": "Agent suggests features and competitors to investigate",
            "supervised": "Agent researches, founder validates findings",
            "autonomous": "Agent monitors competitive landscape, alerts to changes",
            "current_level": "shadow",
            "promotion_criteria": "Research relevance ≥ 85%",
            "never_autonomous": False,
        },
        "product_decisions": {
            "shadow": "N/A",
            "advisory": "N/A",
            "supervised": "N/A",
            "autonomous": "NEVER — founder-only for product direction",
            "current_level": "NEVER_AUTONOMOUS",
            "promotion_criteria": "N/A",
            "never_autonomous": True,
        },
    },
    
    "stewardship_orchestrator": {
        "regulatory_research": {
            "shadow": "Agent observes founder's regulatory questions",
            "advisory": "Agent provides regulatory information with confidence levels",
            "supervised": "Agent identifies requirements, founder validates",
            "autonomous": "Agent monitors regulatory changes, alerts founder",
            "current_level": "shadow",
            "promotion_criteria": "No missed regulatory requirements over 4 weeks",
            "never_autonomous": False,
        },
        "compliance_decisions": {
            "shadow": "N/A",
            "advisory": "N/A",
            "supervised": "N/A",
            "autonomous": "NEVER — founder-only for compliance decisions",
            "current_level": "NEVER_AUTONOMOUS",
            "promotion_criteria": "N/A",
            "never_autonomous": True,
        },
        "risk_assessment": {
            "shadow": "Agent observes founder's risk identification",
            "advisory": "Agent flags risks with likelihood and impact",
            "supervised": "Agent produces risk assessments, founder reviews",
            "autonomous": "NEVER — risk acceptance is always founder decision",
            "current_level": "shadow",
            "promotion_criteria": "Risk identification accuracy ≥ 85%",
            "never_autonomous": True,  # Risk decisions always need human judgment
        },
    },
}
```

```python
# assumption_tracker.py
# Assumptions are first-class citizens, not throwaway notes
# Every strategy, goal, and decision is built on assumptions

from datetime import datetime, timedelta
from enum import Enum
from pydantic import BaseModel

class AssumptionRisk(str, Enum):
    LOW = "low"          # Well-validated, multiple sources
    MEDIUM = "medium"    # Some evidence, needs validation
    HIGH = "high"        # Little evidence, critical to validate
    CRITICAL = "critical" # Unvalidated, business depends on it

class AssumptionStatus(str, Enum):
    UNTESTED = "untested"
    PARTIALLY_VALIDATED = "partially_validated"
    VALIDATED = "validated"
    CHALLENGED = "challenged"     # New evidence contradicts
    INVALIDATED = "invalidated"   # Proven wrong

class Assumption(BaseModel):
    """First-class assumption entity with epistemic metadata."""
    entity_id: str
    display_name: str
    description: str
    
    # Epistemic metadata (CC-3)
    confidence: float  # 0.0-1.0
    provenance: str    # Where did this assumption come from?
    assumptions: list[str]  # Meta-assumptions: what is this assumption built on?
    limitations: str   # What can't this assumption tell us?
    uncertainty: str   # What might change this assumption?
    
    # Risk classification
    risk_level: AssumptionRisk
    status: AssumptionStatus
    
    # Dependency tracking
    supports_goals: list[str]  # Which strategic goals depend on this?
    supports_strategies: list[str]  # Which strategies depend on this?
    supported_by_evidence: list[str]  # What evidence supports this?
    contradicted_by_evidence: list[str]  # What evidence contradicts this?
    
    # Specification aging (CC-5)
    review_cadence_days: int  # How often should this be reviewed?
    last_reviewed: datetime
    valid_from: datetime
    valid_until: datetime | None = None
    
    # Validation plan
    validation_method: str | None = None  # How could we test this?
    validation_timeline: str | None = None  # When could we test this?
    validation_priority: int | None = None  # How important is testing this?

    def is_stale(self) -> bool:
        """Check if assumption needs review based on specification aging."""
        if self.review_cadence_days and self.last_reviewed:
            return (datetime.now() - self.last_reviewed).days > self.review_cadence_days
        return False
    
    def cascade_impact(self) -> list[str]:
        """Return all entities that would be affected if this assumption is invalidated."""
        return self.supports_goals + self.supports_strategies


# Example assumptions from the launch project
LAUNCH_PROJECT

---
