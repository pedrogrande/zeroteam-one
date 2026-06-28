# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `573d8937...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-26T16:17:47 |
| **Runs** | 4 completed / 4 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-26T16:17:47* · `glm-5.1:cloud` · `fdda9874...`

### Prompt

what can you tell me about the ideology around Ruby on Rails?

### Response

# The Ideology of Ruby on Rails

Ruby on Rails has one of the most distinctive and deliberately articulated ideologies in software framework history. It's worth understanding because DHH (David Heinemeier Hansson) deliberately designed it as **opinionated software** — the ideology IS the product, not just a byproduct.

## The Core Ideological Pillars

### 1. Convention over Configuration (CoC)
The single most important principle. The framework has **opinions about how things should be done**, and you only need to specify what's *unconventional*. A new Rails app with zero configuration "just works" — the framework assumes sensible defaults for naming, structure, routing, and database mapping.

**The ideological claim:** Most decisions don't need to be made. The cost of choosing is higher than the cost of accepting a good default. Freedom from trivial decisions frees you for the decisions that matter.

### 2. Don't Repeat Yourself (DRY)
Every piece of knowledge should have a single, authoritative, unambiguous representation. Not just "write less code" — a deeper claim that **duplication is the root of maintainability problems**. If you define a database column once, it should propagate everywhere (validation, forms, display) without re-stating.

**The ideological claim:** Repetition isn't just inefficiency — it's a maintenance hazard. When the same truth lives in three places, they will inevitably diverge.

### 3. Programmer Happiness
Rails inherits Ruby's founding philosophy from Matz: **the programmer is the primary concern**, not the machine. Code should read like English, be joyful to write, and prioritise human cognitive ergonomics over runtime performance.

**The ideological claim:** Developer experience is a first-class design constraint. If it feels good to write, it will be written well.

### 4. Omakase (Chef's Choice)
DHH's Japanese restaurant metaphor: the core team **curates the best combination** of technologies rather than offering an à la carte menu. You don't pick your ORM, your test framework, your JS bundler — Rails chooses them for you.

**The ideological claim:** Expert curation beats individual assembly. The whole is greater than the sum of its parts when they're designed to work together.

### 5. The Majestic Monolith
Rails pushed back hard against the microservices trend. Most applications don't need distributed architecture, and the **complexity cost of distribution** is orders of magnitude higher than the complexity cost of a well-structured monolith.

**The ideological claim:** Architect for the scale you actually have, not the scale you imagine. Distribution is a last resort, not a default.

### 6. Opinionated Software
Rails has strong opinions and **isn't afraid to impose them**. If you disagree, Rails would rather you leave than bend the framework. This is the opposite of "unopinionated" or "pluggable" frameworks.

**The ideological claim:** A framework that tries to please everyone pleases no one. Strong opinions produce coherent systems; weak opinions produce incoherent ones.

### 7. Small Teams, Big Impact
37signals (now 37z) built Basecamp with a team of ~15 for over a decade. Rails was extracted FROM that product, not designed in a vacuum. The ideology says: **a small, tight team with sharp tools can outperform large, bureaucratic teams.**

**The ideological claim:** Team size is not capability. Constraints breed creativity. The best software comes from people who use what they build.

### 8. Integrated Stack / "Batteries Included"
Everything you need comes out of the box: ORM, routing, testing, mailers, background jobs, WebSockets, asset pipeline. No assembling 47 micro-libraries.

**The ideological claim:** Integration is a feature, not a limitation. The seams between independently-chosen components are where bugs and complexity live.

## The Cultural Layer

Beyond technical principles, Rails has a deliberately provocative culture:

- **"TMTOWTDI is a bug, not a feature"** — The opposite of Perl's philosophy. One preferred way.
- **"Rails is not your therapist"** — It won't accommodate every working style. Adapt to it.
- **"Build, don't debate"** — Ship real things, stop over-architecting.
- **Commercial open source** — DHH has been explicit that Rails serves commercial purposes. It's not charity; it's a commercially sustainable ecosystem (Basecamp/HEY built on it).
- **Counter-cultural swagger** — Rails deliberately positioned itself against Java enterprise culture, against XML configuration, against design-by-committee, against "architecture astronaut" thinking.

## The Tensions

- **Convention vs. flexibility:** CoC speeds you up when you follow the path, but fights you when you don't. "Rails makes easy things easy and hard things impossible."
- **Opinionated vs. inclusive:** Strong opinions attract passionate adherents AND passionate detractors.
- **Happiness vs. performance:** Ruby is slow. Rails is heavy. The trade-off is explicit: programmer time > machine time. But at scale, this breaks down.
- **Monolith vs. ecosystem:** As JavaScript ate the frontend, Rails' integrated stack became a constraint. The "great JavaScript schism" was arguably Rails' biggest ideological challenge.

---

## Why This Matters for Your Work

The Rails ideology is directly relevant to several things you're working on:

| Rails Ideology | Your Parallel |
|---|---|
| Convention over Configuration | **CAWDP's Pattern System** — pre-validated knowledge that fills 40-70% of a specification so users don't start from scratch |
| Opinionated Software | **"The methodology makes decisions so you don't have to"** — CAWDP is deliberately opinionated about where agents vs humans belong |
| Omakase / Integrated Stack | **CAWDP as integrated methodology** — not à la carte principles, but a curated, coherent process |
| Small Teams, Big Impact | **Born-Agent-Native orgs** — 1 human + agents replacing teams of 20 |
| Programmer Happiness | **Human Enrichment** — system expands creative freedom, not constrains it |
| The Majestic Monolith | **"Start with what you need, not what you imagine"** — progressive autonomy, not premature distribution |
| Progressive Disclosure | **Directly in your ADHD design principles** — reveal complexity as capability grows |
| Commercial Open Source | **Red Hat model** — open methodology, commercial ecosystem |

The most important parallel: **Rails proved that opinionated software with a strong ideology can create and dominate a category.** Before Rails, "web framework" wasn't a category people argued about. Rails made it one. You're trying to do the same thing with "Agent Production" — create a category through strong opinions and a coherent methodology.

DHH didn't write a framework and then discover opinions. He had opinions first, and the framework was the embodiment. That's exactly your position with CAWDP.

Want me to dig deeper into any specific aspect of the Rails ideology, or explore how these parallels might inform your positioning and product decisions?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-04-26T16:34:06* · `glm-5.1:cloud` · `b9a90397...`

### Prompt

I acknowledge the imperfections of the idealogical stance and opinionated nature, however I see many benefits that are often overlooked or at least under-represented. 

The most important benefit was the learnability. It was huge in bringing people to web application development because its abstractions meant beginners don't need to understand all the complexities from day one. They can see great outcomes from the first experience which gives them confidence and excitement to continue learning.

Another element that is important to beginners is the "Rails way". A beginner gets confused if given too many options so having the recommend way, reduces overwhelm and anxiety.

What other benefits have I not mentioned?

### Response

You've identified the two most visible benefits — learnability and overwhelm reduction. But the Rails ideology generates a cascade of less obvious benefits that compound over time. Let me lay them out.

## Benefits You Haven't Mentioned

### Communication Benefits

**Shared Language.** When everyone does things the same way, you can have conversations about *what* you're building, not *how*. "The callback order" means the same thing to every Rails developer. This drastically reduces communication overhead — no translating between architectural dialects, no "in our previous project we did it this way" friction.

**Implicit Documentation.** The codebase IS the documentation. You don't need a 50-page architecture doc because the architecture IS the convention. A new developer opens the app and knows where controllers live, how routes map, what the database schema looks like. The structure is self-documenting.

**Mentorship Scalability.** Senior developers can teach ONE way, not debate three alternatives before the junior can start. "This is how Rails does it" is more efficient than "well, you could use this ORM or that one, and here are the tradeoffs..." The mentorship bandwidth expands because the decision space collapses.

### Skill and Career Benefits

**Transferability.** Know "The Rails Way" and you can walk into any Rails project and be productive on day one. The conventions mean project-specific onboarding is minimal. This is massive for hiring, team formation, and individual career mobility — and it's the same force that makes the community large and healthy.

**Community Knowledge Compounding.** Every blog post, Stack Overflow answer, tutorial, and conference talk works for YOUR app because YOUR app follows the same conventions. The community's knowledge doesn't fragment across architectural choices — it compounds. One Rails tutorial reaches the entire community. One "how we set up our microservices" tutorial reaches... that team.

**Skill Depth Over Breadth.** Instead of learning five ways to do routing and becoming shallow in all of them, you learn one way deeply. The cognitive budget that would go to comparing alternatives goes to mastering the chosen path. Depth produces better outcomes than breadth, and conventions produce depth.

### Decision and Focus Benefits

**Decision Fatigue Elimination — For Seniors Too.** You mentioned beginners, but this benefit scales. Every decision a senior developer doesn't have to make is attention that goes to the problem domain. The framework has decided the unimportant things. Energy flows to what matters.

**Reduced Bikeshedding.** When the framework has decided, the team can't argue about it. No "which ORM should we use?" debates that consume sprint planning. The energy that goes to bikeshedding in unopinionated stacks goes to product decisions in opinionated ones.

**Technical Debt From Indecision.** Unopinionated frameworks generate a different kind of debt: the debt of choices never made, or made inconsistently across the team. Convention eliminates the debt before it forms.

### Safety and Trust Benefits

**Safe Defaults as Security.** The conventions are designed by experts who've seen what goes wrong. Follow them and you get SQL injection protection, CSRF tokens, parameter sanitization — security best practices by default. Not because you chose them, but because the framework chose them for you. Convention as trust infrastructure.

**Psychological Safety.** Knowing there's a "right way" reduces the fear of doing it wrong. This isn't just for beginners — it's for anyone who's ever worried whether their architectural choice will come back to bite them. The framework has your back. This connects directly to your ADHD design principle: **Shame-Free Failure States** — the "Rails Way" makes failure less likely AND less shameful when it happens, because you followed the path.

**Implicit Best Practices.** You get the benefit of accumulated expertise without earning it yourself. It's structural mentorship — the framework embeds 20 years of web development wisdom into its defaults. You don't need to know WHY the convention exists to benefit from it. The wisdom is in the structure, not the documentation.

### Architecture and Evolution Benefits

**Implicit Architecture.** The framework IS the architecture. MVC isn't a choice you agonise over — it's what you get. The folder structure, the request lifecycle, the testing approach — solved. You focus energy on the domain, not the scaffolding.

**Evolution Path.** When there's a recommended path, the framework can evolve that path. Rails upgrades, while sometimes painful, are possible because the framework controls the upgrade surface. Compare this to microservice architectures where each team made different choices and upgrading any dependency is a coordination nightmare.

**Ecosystem Alignment.** Gems, libraries, and tools built for Rails work together because they follow the same conventions. The ecosystem has coherence rather than fragmentation. A Rails engine can assume how your app is structured. A testing framework can assume how your models are organised.

### The Compounding Benefit

All of these compound. Transferability feeds community size. Community size feeds knowledge compounding. Knowledge compounding feeds ecosystem quality. Ecosystem quality feeds the safe defaults. Safe defaults feed learnability. Learnability feeds community size.

**The flywheel spins because the opinion is coherent.** Not because it's perfect — because it's consistent. A perfect but inconsistent framework would produce none of these benefits. An imperfect but coherent framework produces all of them.

---

## The Connection to Your Work

This is not abstract. You're building something that aspires to the same kind of ideological coherence — CAWDP as "the Rails of agent production." The benefits above are the exact benefits CAWDP should deliver to the 77% stuck at pilot:

| Rails Benefit | CAWDP Equivalent |
|---|---|
| Shared language | **Plain English Taxonomy** — "boundary," "complementarity gap," "authority boundary" mean the same thing to every CAWDP practitioner |
| Implicit documentation | **Pattern System** — the specification documents itself through pre-validated patterns |
| Safe defaults as security | **Progressive autonomy** — shadow → advisory → supervised → autonomous, safe by default |
| Psychological safety | **"The methodology makes decisions so you don't have to"** — shame-free specification |
| Implicit best practices | **Cross-cutting concerns** — CC-1 through CC-8 built into the process, not bolted on |
| Reduced bikeshedding | **The CAWDP Way** — "extractors never judge" isn't a debate, it's a principle |
| Evolution path | **Specification aging** — the methodology has a built-in upgrade mechanism |
| Community knowledge compounding | **Open framework** — every practitioner's experience enriches everyone |
| Decision fatigue elimination | **One Clear Next Step Always** — Phase 0 → Phase 1 → Phase 2, not 47 architectural choices |
| Transferability | **Certification** — a CAWDP-certified practitioner can walk into any agent project and be productive |

The deepest parallel: **Rails proved that opinionated methodology can create a category.** Before Rails, "web framework" wasn't a contested space. Rails made it one through ideological coherence — not technical superiority (Django, Laravel, and others have matched or exceeded Rails technically) but through a coherent, learnable, transferable, compounding set of opinions that built a community.

The overlooked benefits are the ones that compound. Learnability is the entry point. The flywheel is what makes it durable.The Rails-CAWDP parallel is a strong framing — "the methodology makes decisions so you don't have to" as the agent production equivalent of "convention over configuration." This also maps directly to several existing concepts: the Possibility Orientation Principle (constraining possibility progressively rather than leaving all doors open), progressive disclosure (Rails' defaults ARE progressive disclosure at the framework level), and the Daniel Kovacs UX principle "show me what's already done" (opinionated defaults do exactly this).

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-26T17:09:50* · `glm-5.1:cloud` · `2eb5db04...`

### Prompt

Rails is an opinionated software framework. I see that I am building an opinionated design framework.

I want to build abstractions that remove complexity from beginners to enable fast learning and adoptability.
I want my frameworks to have conventions over configuration.
I believe we can achieve a stronger foundation for our framework by developing a modular but curated stack to bring all the benefits while minimising the downsides that Rails brings.

How could my agentic system design framework (which includes CAWDP, PRISM ontology, and the agent design principles amongst others) be recast in this light?

How can we deliver a beginner-friendly and sophisticated framework that can reduce time to launch and deliver value from day one?

### Response

# CAWDP as an Opinionated Design Framework

This is the right framing. You're not building a methodology — you're building **the Rails of agent production**. The distinction matters. A methodology tells you what to do. An opinionated framework **makes decisions so you don't have to** and delivers value from minute one.

Let me recast everything through this lens.

---

## 1. The Ideology — Core Beliefs

Rails has "convention over configuration" and "programmer happiness." CAWDP needs equally clear, equally provocative core beliefs:

| Rails Belief | CAWDP Belief |
|---|---|
| Convention over Configuration | **The methodology makes decisions so you don't have to** |
| Don't Repeat Yourself | **Every agent strength has a flip side — design for both** |
| Programmer Happiness | **Human enrichment, not human replacement** |
| Omakase (Chef's Choice) | **The curated stack — modular but coherent** |
| The Rails Way | **The Boundary Way — agents prepare judgment, humans make judgment** |
| Build, don't debate | **Start with what you're FOR, stress-test what you're AGAINST** |
| Small teams, big impact | **One human + agents can outproduce twenty** |

These aren't just slogans. They're **design constraints that structure every decision**. "Extractors never judge" isn't a suggestion — it's the convention. You can override it, but you need to justify why. That's convention over configuration applied to agent design.

---

## 2. The Abstractions — What Beginners Interact With

Rails gives beginners three commands that deliver working software: `rails new`, `rails generate scaffold`, `rails server`. They don't need to understand MVC, ActiveRecord, or routing. The framework handles the complexity.

CAWDP needs the same thing. Here are the equivalent abstractions:

### Abstraction 1: The Pattern (equivalent to `rails generate scaffold`)

You don't start with a blank page. You pick a pattern and 40-70% of the specification is pre-filled.

| You Say | Framework Fills In |
|---|---|
| "I'm building a **Signal Detector**" (Extractor, possibility-oriented) | Authority boundary: "never judge." Progressive autonomy: shadow → advisory. Verification: structural checks only. Failure mode: silence = absence. Cost budget template: low. |
| "I'm building a **Review Partner**" (Assessor, constraint-oriented) | Authority boundary: "never finalise." Per-dimension progressive autonomy (style: fast autonomous; security: NEVER autonomous). Harm-capable protocols. DO_NOT_SUGGEST mechanism. Failure mode: plausible error without human review. |
| "I'm building a **Discovery Explorer**" (Generator, possibility-oriented) | Authority boundary: "never be vague." Two-mode cycle. Novelty assessment: never fully autonomous. Diversity enforcement. Failure mode: valid-but-obvious. |

The pattern is the entry point. It fills in the conventions so the beginner starts with something that works, not something that's empty.

### Abstraction 2: The 4 Identity Questions (equivalent to `rails new`)

Before you pick a pattern, you answer 4 questions:

1. **What IS this agent?** (essence)
2. **What's its stance toward possibility?** (orientation — determined by which CAWDP phase you're in)
3. **What would VIOLATE its identity?** (identity-level "never")
4. **What would it mean for this agent to be WRONG?** (failure mode = authority boundary)

These 4 questions DERIVE everything else. The class, the authority boundary, the progressive autonomy path, the verification protocol, the cost budget — all derivable from identity. The beginner doesn't need to know what "epistemic metadata" means. They answer 4 questions and the framework fills in the rest.

### Abstraction 3: Safe Defaults (equivalent to Rails' built-in security)

Following the framework gives you progressive autonomy, verification independence, epistemic metadata, authority boundaries, specification aging, and cost budgets **by default**. Not because you chose them — because the framework chose them for you.

This is Rails' "Strong Parameters" applied to agent design. You get security best practices by default. You don't need to know WHY the convention exists to benefit from it. The wisdom is in the structure, not the documentation.

---

## 3. Convention Over Configuration at Every Level

This is the core mechanism. At every level of the framework, there's a convention (safe default) and a configuration (explicit override). The beginner uses all conventions. The expert overrides what they need. **The framework always provides a safe default.**

| Level | Convention (Default) | Configuration (Override) |
|---|---|---|
| Agent Identity | 4 identity questions → derive everything | Custom identity specification |
| Agent Class | 5×3 taxonomy (15 archetypes) | Custom class + orientation |
| Authority Boundaries | "failure mode = authority boundary" | Custom boundary specification |
| Progressive Autonomy | shadow → advisory → supervised → autonomous | Custom autonomy stages and timelines |
| Verification | 3-level (structural / semantic / authority) | Custom verification protocol |
| Epistemic Metadata | 6-field contract (confidence, provenance, assumptions, limitations, recency, uncertainty) | Custom metadata fields |
| Knowledge Model | PRISM (7 dimensions + 4 cross-cutting layers) | Custom ontology |
| Design Process | CAWDP 10 phases with quality gates | Custom phase selection and depth |
| Task Governance | 8 contract primitives | Custom contract primitives |
| Specification Aging | assessedAt + refresh cadence | Custom aging schedule and triggers |

**The beginner never sees the Configuration column.** They use the Convention column and get a working, safe, compliant specification. The Configuration column exists for experts who need to deviate — and when they do, they must justify it.

This is "the methodology makes decisions so you don't have to" in action. Every row in the Convention column is a decision the framework has already made based on evidence from 10+ agent designs, the assignment marking workflow, and the 5-class taxonomy. The beginner inherits that evidence without needing to know it exists.

---

## 4. The Curated Stack — Modular but Coherent

Rails' curated stack (ActiveRecord, ActionDispatch, ActionView, etc.) gives you everything you need out of the box. Each component is replaceable, but the default combination is curated for coherence.

Here's CAWDP's equivalent:

```
┌─────────────────────────────────────────────────────┐
│                   THE BOUNDARY WAY                    │
│            "Agents prepare judgment.                  │
│             Humans make judgment."                    │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐ │
│  │   PROCESS    │  │   TAXONOMY   │  │  CONTRACTS   │ │
│  │   (CAWDP)    │  │  (5×3 Class  │  │  (8 Primi-  │ │
│  │  10 phases   │  │  × Orienta-  │  │  tives)      │ │
│  │  5 gates     │  │  tion)       │  │              │ │
│  │  8 CCs       │  │              │  │              │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬──────┘ │
│         │                  │                  │        │
│  ┌──────┴──────────────────┴──────────────────┴─────┐│
│  │              PRISM (Data Model)                     ││
│  │         7 Dimensions + 4 Cross-Cutting Layers      ││
│  ├────────────────────────────────────────────────────┤│
│  │    Epistemic │ Governance │ Temporal │ Schema       ││
│  │    Metadata  │  Layer     │  Layer   │ Registry     ││
│  ├──────────────┴────────────┴──────────┴──────────────┤│
│  │        SAFE DEFAULTS (Convention Layer)             ││
│  │  Authority Boundaries │ Progressive Autonomy       ││
│  │  Verification 3-Level │ 6-Field Epistemic          ││
│  │  Cost Budgets          │ Specification Aging        ││
│  │  Trust Ledger          │ Quality Gates              ││
│  ├────────────────────────────────────────────────────┤│
│  │        PATTERNS (Scaffolding Layer)                 ││
│  │  Signal Detector │ Multi-Lens Analyst │ Review     ││
│  │  Partner │ Discovery Explorer │ Learning Scaffold   ││
│  ├──────────────────────────────────────────────────── ┤│
│  │        IDENTITY QUESTIONS (Entry Layer)            ││
│  │  What IS it? │ Stance? │ What violates it? │ Wrong?││
│  └────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

**Each module is self-contained and replaceable.** You can use PRISM without CAWDP. You can use the taxonomy without PRISM. You can use contracts without the process. But the **curated default** is all of them working together, because they were designed to work together.

This is how you get the Rails benefit (coherent, integrated, "just works") without the Rails downside (monolithic, hard to swap components). Each module has a clear interface. Each module can be understood independently. But the default is the curated combination.

**The module interfaces:**

| Module | Input | Output | Can Be Used Without |
|---|---|---|---|
| Identity Questions | 4 plain English answers | Agent identity + class + orientation + failure mode + authority boundary | Any other module |
| Patterns | Agent class + orientation | 40-70% of specification pre-filled | The process (you can use patterns standalone) |
| Taxonomy | Agent purpose | Class assignment + authority boundaries + failure modes + progressive autonomy defaults | PRISM or contracts |
| Process (CAWDP) | Agent purpose + context | Complete specification through 10 phases | The taxonomy (you can use the process with custom classes) |
| PRISM | Knowledge requirements | Typed, connected, metadata-rich knowledge model | CAWDP (you can use PRISM for knowledge management) |
| Contracts | Agent specification | 8-primitive governance membrane | CAWDP (you can use contracts for task governance) |
| Safe Defaults | Agent class | Authority boundaries, progressive autonomy, verification, epistemic metadata, cost budgets, aging schedules | Any specification (you can apply defaults to custom specs) |

---

## 5. Value from Day One — The 15-Minute Agent Specification

Rails gives you a working app in 15 minutes. CAWDP should give you a working agent specification in 15 minutes.

### Minute 0-1: Pick a Pattern
"I'm building a Review Partner." The framework fills in 40-70% of the specification.

### Minute 1-3: Answer 4 Identity Questions
- **What IS it?** "A partner that reviews documents and surfaces what needs human attention."
- **What's its stance?** Constraint-oriented (operates within defined boundaries).
- **What would VIOLATE its identity?** "Making final decisions on ambiguous content."
- **What would it mean for it to be WRONG?** "Plausible error accepted without review."

From these 4 answers, the framework DERIVES:
- Agent class: Assessor (constraint-oriented)
- Authority boundary: "Never finalise"
- Failure mode: plausible error without human review
- Progressive autonomy: per-dimension (style fast, security NEVER autonomous)
- Verification: authority-level checks on all high-stakes outputs
- Epistemic metadata: confidence scores on every assessment
- Cost budget: moderate
- Specification aging: quarterly review

### Minute 3-5: Review Safe Defaults
The framework presents the derived specification. The user reviews and adjusts what matters to them. They don't need to understand progressive autonomy or epistemic metadata — they see "how this agent earns trust over time" and "what confidence scores mean for your review process" in plain English.

### Minute 5-10: Customise What Matters
The user focuses on the domain-specific parts — the parts that require THEIR expertise:
- What specific documents does it review?
- What are the domain-specific failure modes?
- What does the human override look like?
- What's the cost tolerance?

### Minute 10-15: Generate Specification
The framework produces a complete agent specification with:
- Identity card
- Authority boundaries
- Progressive autonomy path
- Verification protocol
- Epistemic metadata requirements
- Cost budget
- Specification aging schedule
- Implementation guidance (Agno configuration)

**This is the "rails generate scaffold" of agent design.** It takes a few simple inputs and produces a complete, safe, compliant output.

The key: **the beginner never needs to know what's under the hood.** They don't need to understand epistemic metadata to get it. They don't need to understand progressive autonomy to get it. They don't need to understand the 5×3 taxonomy to get it. The framework handles the complexity. The beginner answers 4 questions and gets a working specification.

---

## 6. How Modularity Addresses Rails' Downsides

| Rails Downside | How CAWDP Addresses It |
|---|---|
| **Monolithic** — hard to swap components | **Modular** — each module has a clear interface. Use PRISM without CAWDP. Use the taxonomy without PRISM. Use contracts without the process. |
| **Magic** — too much happening behind the scenes | **Transparent** — every convention has a clear WHY. "Extractors never judge" isn't magic, it's because the failure mode (qualifying instead of extracting) defines the boundary. The WHY is always one question away. |
| **Constrained** — "the Rails Way" becomes a cage | **Escapable** — progressive disclosure means you start with conventions and EXPAND into configuration. You're never trapped — you're scaffolded. The escape hatches are built in. |
| **Legacy** — hard to evolve without breaking conventions | **Evolvable** — specification aging is built into the framework. Patterns are versioned. Contracts have proxy patterns. The framework expects to change, not calcify. |
| **Generic** — convention over configuration means suboptimal for specific use cases | **Domain-appropriate** — conventions are derived from practice (10+ agent designs, real workflows), not imposed from theory. They're safe defaults because they're proven defaults. |

The deepest difference: **Rails conventions are about architecture. CAWDP conventions are about trust and safety.** Rails says "put your controllers in app/controllers." CAWDP says "extractors never judge." The first is a file path. The second is a boundary that prevents failure. The stakes are different, and the conventions reflect that.

---

## 7. Progressive Disclosure — Beginner to Expert

This is where Rails' learnability benefit is most directly applicable. The framework should have clear levels, each building on the previous:

### Level 1: The Quick Start (Beginner)
**Interacts with:** Patterns, 4 Identity Questions, Safe Defaults
**Produces:** Working agent specification in 15 minutes
**Understands:** "I picked a pattern, answered 4 questions, and got a specification that works"
**Rails equivalent:** `rails new` + `rails generate scaffold` + `rails server`

### Level 2: The Practitioner (Intermediate)
**Interacts with:** Taxonomy, Authority Boundaries, Progressive Autonomy, Verification Protocols
**Produces:** Customised specifications with adjusted boundaries and autonomy paths
**Understands:** "Extractors never judge, Assessors never finalise, Generators never be vague" — the WHY behind the conventions
**Rails equivalent:** Understanding MVC, writing custom controllers, model validations

### Level 3: The Architect (Advanced)
**Interacts with:** Full CAWDP process, PRISM ontology, Cross-Cutting Concerns, Quality Gates
**Produces:** Multi-agent workflows, complex compositions, custom authority boundaries
**Understands:** The full 10-phase process, why each quality gate exists, how cross-cutting concerns interact
**Rails equivalent:** Engines, Concerns, custom middleware, background jobs, multi-service architecture

### Level 4: The Contributor (Expert)
**Interacts with:** Pattern creation, taxonomy extension, process adaptation, methodology evolution
**Produces:** New patterns, extended taxonomy, adapted process phases, methodology contributions
**Understands:** How to extend the framework itself, when conventions should change, how to contribute patterns
**Rails equivalent:** Contributing to Rails core, writing gems, proposing RFCs

**Critical design principle:** Each level must deliver value independently. A Level 1 user gets a working specification. They don't need Level 2 to be productive. They grow into Level 2 when they need to customise. They grow into Level 3 when they need to compose. They grow into Level 4 when they need to extend.

This is progressive disclosure applied to the entire framework, not just the UI.

---

## 8. The Flywheel

Rails' flywheel:
**Convention → Community → Gems → Knowledge → Convention**

More conventions → more people use Rails → more gems are built → more knowledge compounds → more conventions are proven → more people use Rails.

CAWDP's flywheel:
**Convention → Practitioners → Patterns → Knowledge → Convention**

More conventions → more people use CAWDP → more patterns are validated → more knowledge compounds (trust ledgers, override rates, specification aging data) → more conventions are proven → more people use CAWDP.

**The trust ledger is the compounding mechanism.** Every agent designed through CAWDP produces trust data. Every progressive autonomy promotion produces evidence. Every override produces a data point. This data validates the conventions, improves the patterns, and builds the knowledge moat.

This is the same force that made Rails' gem ecosystem self-reinforcing, but applied to trust data instead of code reuse. The more people use the framework, the more trust data validates the conventions, the better the patterns become, the more value the framework delivers.

---

## 9. The Naming — "The Boundary Way"

Rails has "The Rails Way." You need an equivalent.

I'd argue it should be **"The Boundary Way"** — because the boundary IS the product. Every convention, every pattern, every safe default draws a line between what agents should do and what humans should keep. The methodology doesn't just design agents — it designs the boundary. And the boundary is what the 77% are looking for.

The four identity questions, the patterns, the safe defaults, the curated stack — they're all in service of one thing: **drawing the boundary clearly and maintaining it safely.**

"The Boundary Way" is memorable, distinctive, and directly connects to Sarah Chen's need ("someone finally helped me draw the line") and the market gap (vendors sell capability, we sell the boundary).

---

## Summary: The Opinionated Design Framework

| Dimension | Rails | The Boundary Way |
|---|---|---|
| Core belief | Convention over Configuration | The methodology makes decisions so you don't have to |
| Entry point | `rails new` + scaffold | Pattern + 4 Identity Questions |
| 15-minute outcome | Working app in browser | Working agent specification |
| Safe defaults | Strong Parameters, CSRF tokens | Authority boundaries, progressive autonomy, verification, epistemic metadata |
| Curated stack | ActiveRecord, ActionDispatch, etc. | CAWDP Process, PRISM, Taxonomy, Contracts, Safe Defaults |
| Override mechanism | Configuration | Configuration column (explicit justification required) |
| Learnability | Progressive from scaffold to custom | Progressive from pattern to full CAWDP |
| Community | Gems, Stack Overflow, conferences | Patterns, trust ledgers, certified practitioners |
| Flywheel | More conventions → more users → more gems → more conventions | More conventions → more practitioners → more patterns → more trust data → more conventions |
| Ideological stance | Programmer happiness | Human enrichment — the system expands creative freedom |
| The "Way" | The Rails Way | The Boundary Way |

The deepest parallel: **Rails proved that opinionated methodology can create and dominate a category.** Before Rails, "web framework" wasn't a contested space. Rails made it one through ideological coherence — not technical superiority, but through a coherent, learnable, transferable, compounding set of opinions that built a community.

You're doing the same thing. The 77% pilot-stuck problem isn't a tools gap. It's a **methodology gap**. And an opinionated design framework — with conventions, safe defaults, progressive disclosure, and a curated stack — is exactly what fills it.

The methodology is free. Getting it right is what we sell.

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-04-27T01:52:09* · `glm-5.1:cloud` · `e0aae0a7...`

### Prompt

How do different stakeholders and practitioners in the agentic system design process interact with the design framework?

### Response

# How Stakeholders Interact with the Design Framework

This is a foundational architecture question. The framework isn't one product — it's **six interfaces serving six stakeholder groups**, all backed by the same curated stack. Each group sees a different surface of the same building.

Let me map this out completely.

---

## The Six Stakeholder Groups

```
┌────────────────────────────────────────────────────────────────┐
│                     THE BOUNDARY WAY                            │
│                                                                │
│   DECISION        DESIGN         IMPLEMENT      OPERATE        │
│   MAKERS          PARTICIPANTS  PARTICIPANTS   PARTICIPANTS   │
│   ┌─────┐        ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│   │Owner│        │Practition│  │Engineer  │  │End User  │   │
│   │     │        │Orchestr. │  │          │  │Trust Lead│   │
│   │Board│        │Domain Exp│  │          │  │          │   │
│   └──┬──┘        └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│      │                │             │             │           │
│      └────────────────┴─────────────┴─────────────┘           │
│                         │                                      │
│                    ┌────┴────┐                                 │
│                    │ GOVERN  │  ← PI Insurers, Regulators,     │
│                    │         │    Auditors, Certifiers          │
│                    └────┬────┘                                 │
│                         │                                      │
│                    ┌────┴────┐                                 │
│                    │ EXTEND  │  ← Contributors, Community,      │
│                    │         │    Researchers                   │
│                    └─────────┘                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## Group 1: Decision Makers

**Who:** Business owners (Sarah Chen), managing partners, principals, executives, board members

**What they need:** Confidence that the approach is safe, trustworthy, and delivers ROI. They bear the risk. They don't have time to learn methodology. They need **artefacts they can hold, share, and trust** — not concepts to understand.

**What they DON'T need:** The 10-phase process, epistemic metadata schemas, PRISM entity types, or anything that sounds like "framework" in the bad sense.

**How they interact:**

| Interaction | What They See | What the Framework Does Behind the Scenes |
|---|---|---|
| The 77% Challenge (30 min) | A one-page boundary map in their language | CAWDP Phase 0 + Phase 4 (quick classification) + Safe Defaults applied automatically |
| The Boundary Map artefact | Three columns: You / AI / System. Named tasks. Where their value lives. | Full complementarity analysis, 5-class taxonomy, authority boundaries — all hidden |
| The Trust Ledger (quarterly) | Traffic lights, one-page executive summary, "promote Agent X" | Full override analysis, progressive autonomy tracking, specification aging monitoring |
| The Operations Manual | 12-page document their insurer accepts | Full CC-1 through CC-8 compliance, contract primitives, governance architecture |
| ROI conversation | "15 hours saved per week. Here's the data." | Cost budget tracking, time savings measurement, override rate analysis |

**Disclosure level:** Level 0 — they never touch the framework directly. They receive **derived views** (artefacts produced by others using the framework). The boundary map, the trust ledger, the operations manual — these ARE the framework's output for decision makers, even though they never see the process that produced them.

**Convention over configuration benefit:** The framework gives them **safe decisions without requiring them to make decisions**. Sarah Chen doesn't choose the authority boundary for a Review Partner — the pattern fills it in. She validates it. That's convention (safe default) over configuration (building from scratch).

**Key insight:** Decision makers are CONSUMERS of framework outputs, not USERS of the framework. The framework succeeds for them when the artefacts they receive give them confidence and clarity — not when they understand how the artefacts were produced.

---

## Group 2: Design Participants

**Who:** Domain practitioners (Daniel Kovacs), certified practitioners, agent orchestrators

**What they need:** A guided process that produces safe, compliant specifications without requiring them to know everything upfront. They need **progressive disclosure** — start simple, go deeper when needed.

**What they DON'T need:** Raw PRISM schemas, TypeQL queries, or the full depth of all 8 cross-cutting concerns on day one.

**How they interact:**

| Role | Interaction | Disclosure Level | Framework Modules |
|---|---|---|---|
| **Domain Practitioner** (Daniel) | Pattern + 4 Identity Questions → 15-min specification → customise | Level 1 (Quick Start) | Patterns, Identity Questions, Safe Defaults |
| **Certified Practitioner** | Full CAWDP process with quality gates, customised per domain | Level 2 (Practitioner) | Taxonomy, Authority Boundaries, Progressive Autonomy, Verification |
| **Agent Orchestrator** | Multi-agent workflow design, coalition formation, full CAWDP | Level 3 (Architect) | Full Process, PRISM, Contracts, Cross-Cutting Concerns |

**The Domain Practitioner's journey (Level 1):**

1. Pick a pattern ("I'm building a Review Partner")
2. Answer 4 identity questions
3. Framework fills in 40-70% of the specification
4. Customise domain-specific parts (what documents? what failure modes? what override?)
5. Walk away with a working specification they can hand to an engineer

They never see "CC-3 Epistemic Metadata Contracts." They see "every assessment comes with a confidence score" — the same thing in plain English. The framework translates.

**The Certified Practitioner's journey (Level 2):**

1. Start with a pattern (if applicable) or from scratch
2. Walk through CAWDP phases with quality gates
3. Understand WHY conventions exist ("extractors never judge BECAUSE the failure mode is qualifying instead of extracting")
4. Customise authority boundaries, progressive autonomy paths, verification protocols
5. Produce specifications that justify deviations from convention

They see the reasoning behind the conventions. They can override when the domain demands it. But the default is always the convention — deviation requires justification.

**The Agent Orchestrator's journey (Level 3):**

1. Design multi-agent workflows with coalition formation
2. Apply complementarity analysis across the full workflow
3. Design handoffs, contracts, and information boundaries
4. Create the human experience (cognitive load budgets, interface specs)
5. Define progressive autonomy across the coalition
6. Produce complete workflow specifications with all cross-cutting concerns

They live in the framework. It's their professional tool. They know the full depth and can navigate all modules.

**Convention over configuration benefit:** The practitioner inherits **decades of design wisdom through patterns and safe defaults**. Daniel Kovacs doesn't need to invent "never finalise" for a Review Partner — the pattern gives it to him. He customises the parts that require his domain expertise (what counts as a "plausible error" in commercial lease review?), not the parts that are universal (authority boundaries, verification levels, progressive autonomy).

**Key insight:** Design participants are the PRIMARY users of the framework. The progressive disclosure levels are designed for them. Each level delivers value independently — you can be productive at Level 1 without ever advancing to Level 2.

---

## Group 3: Implementation Participants

**Who:** Agent engineers, developers, DevOps

**What they need:** Clear, implementable specifications that translate directly to code. Typed schemas, not prose descriptions. Agno configurations, not design documents.

**What they DON'T need:** The full CAWDP design rationale, the business context, or the governance philosophy. They need the **what and how**, not the why.

**How they interact:**

| What They Receive | What It Looks Like | How It's Produced |
|---|---|---|
| Agent configuration | `Agent(name="lease-reviewer", model=Ollama("glm-5.1:cloud"), tools=[...], instructions=..., response_model=LeaseReviewSchema)` | Design Studio transformer: Actor→Agent |
| Team/Workflow configuration | Agno `Team` or `Workflow` with step choices, session config | Design Studio transformer: Coalition→Team, Events+Relations→Workflow |
| Pydantic schemas | Typed output models with validation, epistemic metadata fields | Design Studio transformer: Schema→Pydantic |
| Verification protocol | Test specifications, assertion queries, quality gate definitions | Design Studio transformer: Governance→Verification Protocol |
| Handoff contracts | Input/output schemas per handoff, authority guards, cost budgets | Design Studio transformer: Full Graph→Implementation |

**The Design-to-Implementation Bridge** (from the CAWDP Design Studio design) is the key mechanism. Six transformers read the PRISM design artefact graph and produce Agno implementation code. The engineer receives code-ready specifications, not design documents they need to interpret.

**Convention over configuration benefit:** Engineers inherit **typed, validated specifications** rather than interpreting prose. The boundary between "what the designer meant" and "what the engineer builds" is eliminated — the specification IS the implementation schema. This is convention at the handoff layer.

**Key insight:** Implementation participants are CONSUMERS of design outputs, translated to their interface. The framework serves them through the transformers, not through direct interaction with CAWDP.

---

## Group 4: Operation Participants

**Who:** End users of deployed agents, trust/compliance leads, team members whose work changes

**What they need:** Confidence in the agents they work with. Understanding of what the agent does and doesn't do. Override mechanisms. Visibility into trust data.

**What they DON'T need:** The design process, PRISM ontology, or CAWDP phases. They need the **experience of working with trustworthy agents**, not the theory of how those agents were designed.

**How they interact:**

| Role | What They See | What the Framework Provides |
|---|---|---|
| **End User** (e.g., associate at Chen Legal) | Agent outputs with confidence scores, clear authority labels, one-click override | Phase 5 Human Experience Design: cognitive load budget, interface specification, override protocol |
| **Trust Lead** (e.g., Diya at Chen Legal) | Trust Ledger dashboard, override patterns, progressive autonomy recommendations, specification aging alerts | Phase 6 monitoring: IDS, UPR, cost variance, progressive autonomy tracking, specification aging |
| **Team Member** | Clear role boundaries ("the agent handles this, you handle that"), progressive autonomy explanation | Phase 5: boundary map as team communication tool, override protocol as safety net |

**Convention over configuration benefit:** The end user inherits **designed trust** — they don't need to verify from scratch because the verification is built into the agent's output structure. Confidence scores, authority labels, typed outputs, clear "I can't safely suggest this" signals — these are conventions that produce trust by default.

**Key insight:** Operation participants experience the framework through its OUTPUTS, not its interface. A well-designed agent IS the framework's user experience for end users. The framework is invisible to them — and that's the goal.

---

## Group 5: Governance Participants

**Who:** PI insurers, regulators (EU AI Act compliance), auditors, professional associations, certification bodies

**What they need:** Evidence of governance, compliance mapping, audit trails, trust scores. They need **proof that the methodology was followed**, not the methodology itself.

**What they DON'T need:** To learn CAWDP. They need the **artefacts that demonstrate trust infrastructure**.

**How they interact:**

| Stakeholder | What They Need | What the Framework Produces |
|---|---|---|
| **PI Insurer** | Governance documentation that answers "what happens when the AI gets it wrong?" | Agent Operations Manual (Milestone 3), Trust Ledger (Milestone 4) |
| **EU AI Act Compliance** | Articles 9/12/13/14 mapping | Compliance mapping document, assured audit trail, specification aging records |
| **Auditor** | Evidence of verification independence, authority boundary enforcement, progressive autonomy decisions | Audit trail (3-level: logged/assured/verified), override records, quality gate records |
| **Professional Association** | Recommended methodology for members | Working paper, case studies, certification standards |
| **Certification Body** | Practitioner competence evidence | Portfolio-based assessment, exam content, progressive autonomy records |

**Convention over configuration benefit:** The framework produces **governance by default**. Following The Boundary Way means your audit trail, progressive autonomy records, and verification protocols are automatically generated — not bolted on after the fact. This is Rails' "Strong Parameters by default" applied to trust governance. You get compliance because the framework makes compliance the path of least resistance.

**Key insight:** Governance participants are CONSUMERS of trust evidence. The framework's greatest value for them is that trust infrastructure is **structural, not optional** — it's produced as a byproduct of following the methodology, not as a separate compliance exercise.

---

## Group 6: Extension Participants

**Who:** Community contributors, methodology researchers, pattern creators, certified practitioners who advance the framework

**What they need:** Clear interfaces for extending the framework. Pattern creation tools. Taxonomy extension protocols. Contribution standards.

**What they DON'T need:** Permission. The framework is open.

**How they interact:**

| Role | What They Do | What the Framework Provides |
|---|---|---|
| **Pattern Creator** | Creates new validated patterns from real agent designs | Pattern specification template, validation criteria, submission process |
| **Taxonomy Extender** | Proposes new agent classes or orientations | Extension protocol, evidence requirements, quality gate for acceptance |
| **Process Adapter** | Adapts CAWDP phases for new domains | Phase interface specification, quality gate definitions, cross-cutting concern mapping |
| **Researcher** | Tests framework hypotheses, publishes evidence | Hypothesis catalog, measurement protocols, data sharing agreements |
| **Certified Practitioner** | Contributes patterns from practice, reports edge cases | Trust ledger data, specification aging reports, override pattern analysis |

**Convention over configuration benefit:** Extension participants get **clear conventions for contribution** — not a free-for-all. "A pattern must be validated from 3+ real agent designs." "A taxonomy extension must include failure mode analysis." "A process adaptation must pass all quality gates." The framework has opinions about how it evolves, not just how agents evolve.

**Key insight:** Extension participants are BUILDERS of the framework. The conventions they follow ensure the framework improves without fragmenting. This is Rails' gem ecosystem discipline applied to methodology evolution.

---

## The Temporal Map — Who Participates When

Not every stakeholder is in the room at every phase. Here's who engages at each CAWDP phase:

| Phase | Cognitive Mode | Primary Stakeholder | Supporting Stakeholders | Artefact Produced |
|---|---|---|---|---|
| **P0** Purpose & Vision | IMAGINE | Decision Maker (owner) | Domain Practitioner | Target State Vision, 4 Identity Answers |
| **P1** Output Specification | SPECIFY | Agent Orchestrator | Domain Practitioner | 28 Design Outputs |
| **P2** Backcasting | TRACE | Agent Orchestrator | — | Dependency Chains, Input Requirements |
| **P3** Task Decomposition | DECOMPOSE | Agent Orchestrator | Domain Expert | Subtask Tree, Failure Modes |
| **P4** Capability Allocation | ALLOCATE | Agent Orchestrator | Decision Maker (validates human-only tasks) | Complementarity Matrix |
| **P5** Event Storming | STRESS-TEST | Agent Orchestrator | Engineer (technical feasibility) | Domain Events, Failure Events, Recovery Paths |
| **P6** System Architecture | ARCHITECT | Agent Orchestrator | Engineer | Pipeline Architecture, Templates |
| **P7** Agent Design | DESIGN | Agent Orchestrator / Practitioner | Domain Expert (boundary validation) | Agent Specifications, Job Descriptions |
| **P8** Human Experience | EMPATHIZE | Agent Orchestrator | End Users (cognitive load, override design) | Interface Specs, Cognitive Load Budget |
| **P9** Validation & Iteration | VERIFY | Agent Orchestrator | All stakeholders (progressive autonomy decisions) | Test Results, Trust Ledger, Progressive Autonomy Status |

**The Decision Maker drops in at P0 and P4.** They don't need to see the middle phases. The framework produces artefacts for them at those touchpoints.

**The Domain Practitioner is most active at P0 and P7.** They contribute domain knowledge at the beginning and validate boundaries at the design stage.

**The Orchestrator is in the room the whole time.** They're the conductor.

**The Engineer drops in at P5 and P6.** They validate technical feasibility and receive the architecture.

**End Users are consulted at P8.** Their experience is designed FOR them, not BY them.

**Governance participants receive outputs after P9.** They don't participate in the design — they receive the trust evidence.

---

## The Handoff Architecture

Every stakeholder interaction produces an artefact that becomes another stakeholder's input. The framework structures these handoffs:

```
DECISION MAKER                DESIGN PARTICIPANTS              IMPLEMENTATION
                               ┌─────────────┐
  "This is what               │  P0-P9: Full  │               ┌─────────────┐
   I'm FOR" ────────────────► │  CAWDP Process│ ────────────► │ 6 Transformers
                               │              │               │ → Agno Code │
  ◄──────── P4 validation  │              │               │              │
   "Yes, that's               │  PRISM Graph │               └──────┬──────┘
   human-only"                │  (source of  │                      │
                               │   truth)     │                      ▼
                               └──────┬──────┘               ┌─────────────┐
                                      │                      │ Running     │
                                      │                      │ Agents      │
                                      ▼                      └──────┬──────┘
                               ┌─────────────┐                      │
                               │  DERIVED     │ ◄────────────────────┘
                               │  VIEWS       │    (runtime data feeds back)
                               │              │
                               │ Boundary Map │ ──────► Decision Makers
                               │ Alloc. Map   │ ──────► Team Members
                               │ Ops Manual   │ ──────► PI Insurers
                               │ Trust Ledger │ ──────► Governance
                               │ Agno Config  │ ──────► Engineers
                               └─────────────┘
```

**Critical insight:** The PRISM design artefact graph is the single source of truth. Every stakeholder receives a **derived view** from the graph — not a separate document. The boundary map is a view. The operations manual is a view. The Agno configuration is a view. The trust ledger is a view.

This means:
- When the design changes, ALL derived views update
- When runtime data flows back (overrides, trust scores), the graph updates
- Every stakeholder always sees the current state
- There is never a version mismatch between what the owner sees and what the engineer builds

This is "artefact graph, not document" (S6 from the target state vision) operationalised at the stakeholder level.

---

## How the Opinionated Framework Serves Each Group

| Stakeholder | The Problem They Have | What the Convention Gives Them | What They Override |
|---|---|---|---|
| **Decision Maker** | "I don't know where the boundary is" | The boundary map — the framework draws it for them | Nothing (they validate, not configure) |
| **Domain Practitioner** | "I don't know how to design an agent safely" | The pattern fills in 40-70% of the spec | Domain-specific failure modes, override protocol |
| **Certified Practitioner** | "I need to customise for my client's domain" | Safe defaults for everything | Authority boundaries, progressive autonomy timeline, verification depth |
| **Agent Orchestrator** | "I need to design a multi-agent workflow" | Full process with quality gates | Pipeline architecture, coalition formation, handoff design |
| **Engineer** | "I need implementable specs, not prose" | Typed schemas, Agno configs, Pydantic models | Model selection, tool configuration, deployment architecture |
| **End User** | "I need to trust what the agent produces" | Confidence scores, authority labels, override button | Nothing (they experience, not configure) |
| **Trust Lead** | "I need evidence of trustworthiness" | Trust Ledger with real data | Monitoring thresholds, review cadences |
| **PI Insurer** | "What happens when it goes wrong?" | Operations Manual with recovery paths | Nothing (they receive, not configure) |
| **Contributor** | "I want to extend the framework" | Contribution conventions, validation criteria | Everything (they're extending, not using) |

---

## The Key Architectural Principle

**Different stakeholders need different surfaces of the same building.**

The decision maker sees the front door and the certificate on the wall. The practitioner sees the workshop floor. The engineer sees the blueprint. The inspector sees the compliance records. The end user sees the finished rooms.

They're all in the same building. They're all served by the same structure. But each one interacts with the surface that serves their need.

The opinionated framework makes this possible because **the conventions produce consistent outputs**. If every practitioner designed agents differently, there would be no consistent boundary map, no consistent operations manual, no consistent trust ledger. The conventions ensure that every derived view — no matter who produces the underlying design — is readable by every stakeholder.

**This is the deepest parallel to Rails:** The Rails convention means any Rails developer can walk into any Rails project and be productive. The Boundary Way convention means any stakeholder can read any CAWDP-produced artefact and understand it. The transferability benefit scales from individual developers to entire stakeholder ecosystems.Memories updated with the full framework recasting and the stakeholder surface architecture.

---
