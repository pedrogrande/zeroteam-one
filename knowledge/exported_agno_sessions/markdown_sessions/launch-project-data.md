<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# If we see the launch of a new agent-native business as a 'Launch project', what would be all the  tasks that need to be done to establish both the system and the business strategy (including goals, business plan, operational blueprint etc)?

The agents should have knowledge of the business owners, their motivations, their experience, values, strengths etc.

The platform agents should help the owners develop a vision, mission and set of business goals that align with their values.
Strategy sessions should create a full suite of strategies including product strategy, marketing strategy, brand strategy, go to market strategy, innovation strategy, growth strategy, media strategy, competitive strategy and overall business strategy.

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

- [ ] Life \& career history interview — experience, industries, roles held
- [ ] Values elicitation session — what matters most, non-negotiables, ethical boundaries
- [ ] Strengths \& skills inventory — professional strengths, natural abilities, developed expertise
- [ ] Motivations \& drivers — why this business, why now, what success looks like personally
- [ ] Risk tolerance assessment — financial, reputational, operational comfort zones
- [ ] Working style \& preferences — how they like to communicate, make decisions, manage people
- [ ] Network \& relationships audit — existing contacts, advisors, potential collaborators
- [ ] Financial position baseline — capital available, personal income needs, investment horizon
- [ ] Time \& capacity map — hours available, other commitments, energy peaks

**System Outputs**

- `founder_profile` entity populated
- `business_rule` entries for owner preferences (communication style, decision thresholds)
- Initial `customer_persona` hypotheses based on founder's network and background
- `assumption` entries for beliefs the founder holds about the market

***

## Phase 2: Vision \& Foundation

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

**SWOT \& Assumptions**

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


### 4.9 Media \& Content Strategy

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

**Team \& Roles**

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

This is the difference between an AI tool that executes tasks and an AI partner that genuinely understands the business. The Launch Project *is* the knowledge loading script — run as a strategic conversation rather than a setup wizard.

