# unknown

| Field | Value |
|-------|-------|
| **Session** | `24ebe675...` |
| **Type** | team |
| **Agent** | unknown |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-27T06:35:06 |
| **Runs** | 17 completed / 19 total |

## Run 1 — unknown ✓ COMPLETED

*2026-04-27T06:35:06* · `glm-5.1:cloud` · `42751f75...`

### Prompt

What team members do you have?

### Response

There are currently no tasks and no defined goal to work on. I need your input to proceed!

**Please tell me what you'd like the team to accomplish.** Once you provide a goal, I'll:

1. Break it down into actionable tasks
2. Assign each task to the best-suited team member
3. Execute them (sequentially or in parallel as needed)
4. Deliver the final result

What would you like us to work on?

---

## Run 2 — Business strategist ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `74c2a57f...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow itself is an agent — it takes user requirements/goals as input and produces a complete design specification (not implementation) that another workflow could then use to build the agent on any platform.

Please provide your strategic analysis covering:
1. Who are the target users and what problem does this solve for them?
2. What's the value proposition compared to manually writing a design spec or jumping straight to implementation?
3. What are the key business risks or considerations?
4. What should the workflow's output artifacts be from a strategic/stakeholder perspective (e.g., design spec, persona docs, risk assessment)?
5. Any strategic considerations about platform-agnostic design specs

Keep the focus strategic — not technical implementation details.

### Response

# Strategic Analysis: Agent Design Specification Workflow

---

## 1. Target Users and Problem

There are **three distinct user types** with different problems, and conflating them is the most common design mistake in this space.

### Primary: The Daniel Kovacs Problem
The domain expert who's been told to "look into AI" — a senior associate, practice manager, or team lead who understands their domain deeply but has no framework for translating that expertise into agent design. Their problem isn't lack of knowledge about their work. It's the **blank page problem**: they know what they need but can't structure it into something an agent could be built from.

Current options fail them in specific ways:
- Jumping straight to implementation (they don't know what to implement)
- Generic AI guidelines (principles without process)
- Technical documentation (assumes they already know how to specify an agent)
- Chatbot-style prompting (type collision — they need to think in 7+ cognitive modes but get one text box)

### Secondary: The Sarah Chen Problem
The business owner who needs to know **where the boundary is** — what AI should handle, what she should keep, and how to verify both. She doesn't need to write the spec herself, but she needs to understand and trust it. Her problem is **verification without a framework**: she can't verify what she can't articulate.

### Tertiary: The Implementation Problem
Developers who receive vague, incomplete, or contradictory requirements. Their problem is **type collision in handoff**: domain expertise encoded as prose when they need structured, typed, implementable specifications.

**The core problem across all three**: there's no methodology for going from "I need an agent that does X" to "here's a complete, typed, verifiable design specification." The 77% pilot-stuck rate exists because people build agents without designing them first — they jump from idea to implementation, skipping the specification layer entirely.

---

## 2. Value Proposition

### vs. Manually Writing a Design Spec

| Manual Approach | Workflow Approach |
|---|---|
| Weeks of iteration | Hours to first complete spec |
| Inconsistent quality (depends on who writes it) | Consistent quality (methodology enforced structurally) |
| Missing sections discovered during implementation | Completeness enforced by design — every section must be addressed |
| Authority boundaries and failure modes discovered in production | Authority boundaries and failure modes surfaced in design |
| Domain expert struggles with structure | Domain expert contributes expertise, workflow provides structure |
| One format, one audience | Typed output with stakeholder-specific views |
| "I think this is complete" | Quality gates confirm completion |

The key insight: **the workflow doesn't replace expertise — it structures it.** A domain expert working through the workflow still makes all the judgment calls. The workflow just ensures they're making the *right* judgment calls in the *right* order, and that nothing critical gets missed.

### vs. Jumping Straight to Implementation

This is the more dangerous comparison because it's the more common mistake. The case for designing before building:

- **77% of agentic AI projects are stuck at pilot** — not because the technology fails, but because the design fails. Agents get built without clear authority boundaries, without failure mode analysis, without verification protocols. The workflow produces these before a single line of code is written.

- **The cost of fixing a design error is 10-100x cheaper than fixing an implementation error** — a boundary that's wrong in a spec takes minutes to correct. A boundary that's wrong in production takes weeks to unwind and can erode trust permanently.

- **You can't verify what you haven't specified** — the Trust Ledger, progressive autonomy schedule, and verification protocols that the workflow produces are prerequisites for responsible deployment, not afterthoughts.

The strategic positioning: **"Principles aren't production. We have the methodology."** The workflow IS the methodology in action. It's the difference between reading about good agent design and actually doing it.

---

## 3. Key Business Risks

### Risk 1: The "Just Another Template" Perception
**Likelihood**: High | **Impact**: Fatal

The market is saturated with templates, frameworks, and guidelines. If this is perceived as "a fancy template," it gets filed alongside the 47 other AI governance PDFs nobody reads.

**Mitigation**: Position on specificity and results, not abstraction. Every output must be concrete enough that someone could build from it. The value isn't the template — it's the *methodology that fills in the template correctly*. The "15-minute agent specification" promise (go from zero to complete spec in ~15 minutes using patterns and safe defaults) makes this tangible.

### Risk 2: Over-Engineering the Workflow Itself
**Likelihood**: High | **Impact**: Moderate

The meta-problem: designing the agent-design-workflow using the same rigour as designing agents risks infinite recursion. The workflow specification could become so detailed that building it takes months.

**Mitigation**: Start with the Quick Start path (Pattern → Identity Questions → Safe Defaults → Complete Spec) and progressively disclose deeper control. The workflow should be opinionated about what matters most and let safe defaults handle the rest.

### Risk 3: Platform-Agnostic Specification Falls Between Stools
**Likelihood**: Moderate | **Impact**: High

A spec that's too abstract is useless to implementers. A spec that's too concrete is locked to one platform. The middle ground is hard to find and maintain.

**Mitigation**: The spec should describe *what* the agent does, *why* it has those boundaries, and *how* verification works — never *which tool* delivers it. Implementation is a derived view, not a source layer. (More on this in section 5.)

### Risk 4: The Credibility Gap
**Likelihood**: Moderate | **Impact**: High

Until the workflow has been used to design agents that are actually running in production, it's theory. The market has been burned by "frameworks" that look great on paper and fail in practice.

**Mitigation**: The first 3-5 real agent designs produced through the workflow become the case studies. Until those exist, everything is claims. The "77% Challenge" approach — use the workflow on someone's real problem for free, show the result — is the fastest credibility builder.

### Risk 5: Category Creation Difficulty
**Likelihood**: Moderate | **Impact**: Moderate

"Agent design specification workflow" doesn't map to an existing category. People don't search for this — they search for problems ("how do I design an AI agent for my business"). Being category-creating means educating the market before selling to it.

**Mitigation**: Lead with the problem, not the category. "Where should AI handle work, and where should your judgment stay?" is a problem people already have. The workflow is the answer, not the pitch.

---

## 4. Output Artifacts from a Strategic/Stakeholder Perspective

The critical design decision: **one graph, many views.** A single design specification stored as a typed, connected knowledge graph (not a document), with stakeholder-specific derived views projected from that graph.

### The Core Output: Agent Design Specification (Single Source of Truth)

The specification itself, stored as typed artefacts with connections, not as a flat document. This is the PRISM principle: artefact graph, not document. Every other output is a projection from this graph.

### Derived Views by Stakeholder

| Stakeholder | What They Need | Derived View |
|---|---|---|
| **Business Owner** (Sarah) | "Where's the boundary? Is it safe? What's my risk?" | Boundary Map (1 page) + Trust Ledger summary + Cost projection |
| **Domain Expert** (Daniel) | "What does this agent actually do? Where are the edges?" | Full design spec in plain English + Authority boundaries + Failure modes |
| **Implementation Team** | "What do I build?" | Agent configuration + Tool specifications + Handoff protocols + Verification tests |
| **Governance/Compliance** | "Can I audit this? Is it trustworthy?" | Audit trail + Verification protocols + Progressive autonomy schedule + Compliance mapping |
| **Operations** | "How do I run and monitor this?" | Agent Operations Manual + Escalation protocols + Specification aging schedule |
| **Risk/Insurance** | "What's my exposure? What happens when it fails?" | Failure & Recovery Register + Override analysis + Assurance levels |

### The Boundary Journey Mapping

The output artifacts should map to a progressive engagement model — not delivering everything at once but producing tangible value at each milestone:

1. **The Boundary Map** (30 minutes) — "Here's where AI should handle work, and where your judgment stays." One page, three columns, client language.
2. **The Allocation Map** (half-day) — "Here's who does what, what could go wrong, and how it's caught." Two documents: task allocation + failure & recovery register.
3. **The Operations Manual** (1-2 weeks) — "Here's the document your insurer, team, and auditor can rely on." 12 pages covering everything from progressive autonomy to specification aging.
4. **The Trust Ledger** (ongoing) — "Here's the data showing it's working." Quarterly report on override rates, verification outcomes, cost variance.

Each artifact is independently valuable. Each produces a specific confidence shift: Relief → Curiosity → Confidence → Evidence.

---

## 5. Strategic Considerations: Platform-Agnostic Design Specs

### The Core Principle: Design Is Independent, Implementation Is Derived

A well-specified agent design should be implementable on **any** agent framework — Agno, LangChain, CrewAI, AutoGen, or a custom solution. The spec describes *what* and *why*, never *which tool*.

This isn't abstraction for its own sake. It's the same principle as architectural blueprints: a blueprint describes the building, not which contractor's tools will build it.

### What Stays Platform-Agnostic

Everything in the design specification is platform-agnostic by definition:

- **Identity**: What IS this agent? Its stance toward possibility. What violates its identity.
- **Purpose & Scope**: What it's for, what it's NOT for.
- **Authority Boundaries**: What it can decide, what it never does, what needs human sign-off.
- **Failure Modes**: What going wrong looks like (tied to the identity violation).
- **Verification Protocols**: How trust is checked at each level.
- **Progressive Autonomy Path**: Shadow → Advisory → Supervised → Autonomous, with criteria for each promotion.
- **Complementarity Allocation**: Which tasks are human-only, agent-only, collaborative.
- **Epistemic Metadata**: What confidence, provenance, and uncertainty markers look like.
- **Human Experience**: Cognitive load budget, override mechanisms, interface requirements.

### What Becomes Platform-Specific (Implementation Layer)

- Tool selections and API integrations
- Framework-specific configuration syntax
- Deployment environment details
- Specific prompt engineering
- Memory and knowledge store configuration
- Monitoring infrastructure

### The Strategic Advantage

Platform-agnostic specifications create a **trust moat**, not a technology moat:

1. **Future-proof**: When the agent framework landscape shifts (and it will), the design specification doesn't change — only the implementation mapping does.
2. **Client-portable**: A client can take their specification to any implementation partner. This builds trust (we're not locking you in) and demonstrates methodology maturity.
3. **Curriculum-valuable**: The specification methodology is teachable regardless of framework. Future's Edge can teach design without being tied to Agno or any other platform.
4. **Vendor-neutral credibility**: Professional associations and insurers are more likely to endorse a methodology that works across platforms than one tied to a specific vendor.
5. **Implementation as commodity**: Over time, implementation becomes less differentiating. Design — the methodology for specifying trustworthy agents — becomes more valuable.

### The Risk of Over-Abstraction

Platform-agnostic doesn't mean vague. "The agent should verify outputs" is vague. "The agent produces a confidence score between 0 and 1 on every output; outputs below 0.6 are flagged for human review; outputs above 0.8 proceed without human sign-off unless the task reversibility is 'irreversible'" is platform-agnostic AND specific.

The test: could two different implementation teams, using different frameworks, read the same spec and produce functionally equivalent agents? If yes, the spec is platform-agnostic and specific. If one team needs to make significant design decisions not covered by the spec, the spec is too vague. If one team is told to use a specific framework's features, the spec is too platform-specific.

---

## Summary: The Strategic Bet

The strategic bet is that **methodology is the moat, not the code**. Software replicates in weeks. Methodology takes years to develop, validate, and institutionalize. The workflow that produces trustworthy agent design specifications is the methodology made operational — it's CAWDP in action, not CAWDP on paper.

The value chain:
- **Design specification** = the product (platform-agnostic, typed, verifiable)
- **Design methodology** = the moat (years of insight, not replicable by copying)
- **Implementation** = the commodity (any competent team with any framework can build from a good spec)
- **Trust infrastructure** = the category (verification, progressive autonomy, boundary clarity — what the market desperately needs and almost nobody provides)

The workflow doesn't need to be everything. It needs to reliably produce one thing: a complete, typed, verifiable design specification that someone could use to build a trustworthy agent on any platform. Everything else — implementation, operations, monitoring — follows from a good specification. Nothing follows from a bad one.The memory has been updated with this strategic analysis. The key strategic takeaway: **design specification is the product, methodology is the moat, implementation is the commodity, and trust infrastructure is the category.** The workflow needs to reliably produce one thing — a complete, typed, verifiable, platform-agnostic design specification — because everything follows from a good specification, and nothing follows from a bad one.

---

## Run 3 — AI UX Innovator ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `2a84f547...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent that guides users through defining what their agent should do, and then produces a complete design specification.

Please provide your UX perspective on:
1. What is the ideal user journey through this workflow? (e.g., conversational intake, structured form, iterative refinement)
2. What inputs should the user provide, and how should they be gathered? (e.g., goals, constraints, persona, domain context)
3. How should the workflow present its outputs and artifacts back to the user?
4. What feedback loops or iteration points should exist? (e.g., reviewing drafts, refining decisions)
5. How do we make this accessible to both technical and non-technical users?
6. What does the interaction pattern look like — is it a single session or multi-session?

Focus on the user experience design, not the technical architecture of the agent itself.

### Response

# UX Design for an Agent Specification Workflow

I'm going to draw heavily on the design principles we've developed — type collision resolution, possibility orientation, identity-first design, the feeling cascade, and progressive disclosure — and translate them into concrete UX recommendations.

---

## 1. The Ideal User Journey

**The journey follows a single structural law: Direction → Destination → Path → Work.**

You cannot ask someone to decompose tasks before they know what they're building toward. The journey must unfold in this order, and the *feel* of each stage must match its purpose.

### Three Rooms, Not One Hallway

The journey has three fundamentally different emotional environments — I'll call them **Rooms** because the visual and interactive texture should actually change:

| Room | CAWDP Phases | Feeling | Possibility |
|------|-------------|---------|------------|
| **Discovery** | P0 Purpose, P1 Outputs, P2 Backcasting | Expansive, open | High — anything is possible |
| **Structure** | P3 Decompose, P4 Allocate, P5 Stress-test | Constructive, shaping | Medium — choices narrow |
| **Realisation** | P6-P9 | Concrete, grounding | Low — working within decisions |

This isn't cosmetic. The possibility orientation principle says an agent's stance toward possibility must match its position in the process. **The same is true for the human.** In Discovery, the user should feel like anything is possible — the UI should breathe, give room, offer suggestions without pressure. In Realisation, the user should feel like decisions are being locked in — the UI should feel firm, structured, definite.

### Pattern-First Entry (The 15-Minute Specification)

Before any room, there's a **doorway**: pattern selection.

A pattern is a pre-validated agent archetype (Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner) that pre-fills 40-70% of the specification. The user selects the pattern closest to their problem, and the system loads safe defaults for everything else.

**Why this works:**
- Zero-friction capture — the user starts with something, not nothing
- Respects expertise — the pattern reflects their domain back to them ("Never approve, never reject, never merge" for a legal reviewer)
- Progressive disclosure — defaults handle complexity; the user overrides only what matters to them
- Daniel Kovacs (our persona) needs to feel like he's *building*, not *answering a questionnaire*

### The Flow

```
Pattern Selection (1 min)
    ↓
4 Identity Questions (5-10 min)
    ↓
Attention Map (what needs your input vs. what's already handled)
    ↓
[User works through sections in any order — the map guides attention]
    ↓
Coherence Check (the system checks for gaps and contradictions)
    ↓
Specification Output
```

The user should never feel like they're on page 3 of 10. They should feel like they're building something that's growing around their decisions.

---

## 2. What Inputs Should the User Provide (and How)

**The core problem: the input surface suffers from type collision.** The specification needs at least 7 distinct cognitive modes, but most tools offer one input modality (a text box). The result is cognitive overload and invisible expertise.

### The 4 Identity Questions (Gathered First, Conversationally)

Before any behavioural specification, the user answers four questions that determine *everything else*:

| # | Question | Mode | Input Type |
|---|----------|------|------------|
| 1 | **What IS this agent?** (essence, not function) | IMAGINE | Guided conversation |
| 2 | **What is its stance toward possibility?** (orientation — expansive, transitional, or constrained) | SPECIFY | Selection from 3 options |
| 3 | **What would VIOLATE its identity?** (existential "never") | BOUNDARY | Drag-sort: inside/outside zones |
| 4 | **What would it mean for this agent to be WRONG?** (failure mode as identity boundary) | EVALUATE | Scenario cards: "which of these failures would be catastrophic?" |

These four questions replace the traditional "describe your agent" text box. They're identity-first, not behaviour-first. Everything else derives from them.

### Cognitive Mode → Input Modality Mapping

After identity, each section of the specification uses a different interaction pattern matched to its cognitive mode:

| Cognitive Mode | Specification Section | Input Type | Example |
|---------------|---------------------|------------|---------|
| **Narrative** (IMAGINE) | Purpose, vision, who it serves | Guided conversation with prompts | "Tell me about the person this agent helps most" |
| **Boundary** (SPECIFY) | What it never does, authority limits | Drag-sort inside/outside zones | Drag tasks into "agent handles" vs "human decides" |
| **Exploratory** (DECOMPOSE) | Task breakdown, what success looks like | Card-based exploration with alternatives | "Here are 3 ways other agents handle this — which fits?" |
| **Verification** (STRESS-TEST) | What could go wrong, recovery paths | Scenario cards: "what if X happens?" | "A client sends contradictory instructions. What should the agent do?" |
| **Architectural** (ALLOCATE) | Who does what, how tasks connect | Spatial canvas with typed connections | Visual allocation map with drag-and-drop |
| **Configurational** (DESIGN) | Limits, budgets, review schedules | Dials, toggles, preset configurations | "How often should the agent's knowledge be refreshed?" |
| **Evaluative** (VERIFY) | Quality gates, trust thresholds | Visual trajectory dashboard | "Move the slider: how confident must the agent be before acting?" |

**Critical design rule:** No section should use a text box as its primary input unless the cognitive mode is genuinely narrative. A boundary question presented as "describe the agent's limits in a text box" is type collision on the input surface.

### Safe Defaults and Pre-Fills

Every input that has a safe default gets one. The user sees:
- ✅ Pre-filled with rationale tooltip ("Most Review Partners use this boundary — here's why")
- ⚠️ Needs attention (pattern provides a suggestion, user should confirm)
- 🔴 Requires your input (no safe default exists — user must decide)

This is the attention map in action. The user never faces 40 empty fields. They face 3-5 decisions that need their input, surrounded by 35+ decisions the pattern already handled.

---

## 3. How to Present Outputs and Artifacts

**The fundamental unit is the artefact, not the conversation.**

### Artefact-Primary, Not Chat-Primary

The specification should emerge as a living document — typed, structured, navigable — not as a wall of text in a chat thread. The user should see their specification *growing* in real-time as they make decisions, not receive a complete document at the end.

### The Attention Map as Navigation

The primary navigation isn't a table of contents or a progress bar. It's an **attention map** showing:

- 🟢 Settled — pattern filled this, user confirmed
- 🟡 Needs attention — pattern suggested, user should review
- 🔴 Requires input — no default, user must decide
- ⚪ Not yet applicable — blocked by upstream decisions

The map is always visible. The user always knows what needs their attention next. **One clear next step, always.**

### Typed Output Sections (Not Prose)

Each section of the specification should be presented as its natural type:

| Output | Presentation Type |
|--------|------------------|
| Boundary map | Visual 3-column layout (You / Agent / System) |
| Authority boundaries | Cards with "CAN" and "NEVER" clearly labeled |
| Task allocation | Visual allocation map with drag-and-drop |
| Failure modes | Scenario cards with recovery paths |
| Progressive autonomy | Timeline with promotion criteria |
| Cost budget | Dial/gauge with hard stop marker |
| Verification protocol | Checklist with 3 levels clearly separated |
| Specification aging | Calendar with review triggers |

**The specification output should be as typed as the input.** If we're asking users to resolve type collision in their inputs, we can't serve them type-collapsed prose as output.

### Derived Views for Different Stakeholders

The same specification produces different views:
- **Decision maker** → boundary map, trust ledger, cost summary
- **Implementer** → Agno configuration, deployment spec
- **Operator** → Agent Operations Manual, verification protocols
- **Governance** → audit trail, compliance mapping, override analysis

Same graph, many surfaces. The specification is the single source of truth; each view is a projection.

---

## 4. Feedback Loops and Iteration Points

### The Coherence Check (Not a "Review Draft" Step)

Instead of producing a draft for review, the system performs a **coherence check** that:
1. Verifies all 4 identity questions have answers
2. Checks that authority boundaries are consistent with failure modes
3. Flags gaps where safe defaults are unconfirmed
4. Identifies contradictions (e.g., "agent decides X" but "X is human-judgment-gated")
5. Shows what the specification would look like as-is, with gaps highlighted

This isn't "here's a draft, please review." It's "here's what you've built so far. These 3 areas need your attention before it's complete."

### Three Kinds of Iteration

| Type | When | How |
|------|------|-----|
| **Micro-iteration** | During a section | User changes an answer; system immediately shows the ripple effect on downstream decisions |
| **Coherence iteration** | After sections are complete | System flags gaps/contradictions; user resolves |
| **Evolution iteration** | After deployment (ongoing) | Specification aging — scheduled reviews, triggered by override rates or drift |

### The Feeling Cascade

Each iteration point should produce a feeling, not just information:

1. **Relief** — "Someone finally drew the line" (after identity questions and boundary map)
2. **Curiosity** — "What else could I map?" (after seeing the attention map)
3. **Confidence** — "I have a plan I can trust" (after coherence check passes)
4. **Evidence** — "I have data, not feelings" (after deployment, trust ledger data)

The iteration points aren't checkpoints in a funnel. They're moments where the user *feels* something has been resolved.

---

## 5. Making It Accessible to Technical and Non-Technical Users

### The Plain English Rule

Every label, every prompt, every output must pass the 16-year-old test. The academic terms can appear in brackets or tooltips, but the primary language is plain English:

| What the system says | What most tools say |
|---------------------|-------------------|
| "Who should handle this?" | "Complementarity allocation" |
| "What should this agent never do?" | "Authority boundary specification" |
| "How sure should the agent be before acting?" | "Confidence threshold configuration" |
| "What happens when something goes wrong?" | "Fallback protocol definition" |
| "How often should we review this?" | "Specification aging cadence" |

### Pattern Selection as the Great Equaliser

Both a senior developer and a law firm principal select the same pattern (e.g., "Review Partner"). The pattern pre-fills the same safe defaults. The law firm principal sees plain English labels. The developer toggles to "Architect" mode and sees the same structure with technical terminology and Agno configuration details.

**Same graph, different surfaces.** The pattern is the entry point that makes both users productive in 15 minutes.

### Technical Depth is Progressive Disclosure, Not a Separate Track

Four levels of depth, all from the same specification:

| Level | Who | What They See | Time |
|-------|-----|---------------|------|
| **Quick Start** | First-time user, non-technical | Pattern + Identity Questions → complete spec | ~15 min |
| **Practitioner** | Regular user, some technical knowledge | Override defaults, customise boundaries | ~45 min |
| **Architect** | Technical user, agent designer | Design from first principles, full control | ~2-4 hours |
| **Contributor** | Framework expert | Extend methodology, create new patterns | Ongoing |

The specification *grows* with the user. A Quick Start specification is not a lesser document — it's a complete specification with safe defaults. The user can progressively override any default when they're ready.

### Language Toggle, Not Separate Flows

Instead of building separate journeys for technical and non-technical users, build one journey with a language toggle:
- **Plain English** labels by default
- **Technical** labels available via toggle (shows Agno terminology, schema references)
- **Visual** mode for boundary/allocation maps (no language needed)

---

## 6. Interaction Pattern: Single Session, Multi-Session, or Something Else?

### The Honest Answer: Both, and It Depends on the User

The workflow should support three patterns:

| Pattern | When | Duration | Saves Progress |
|---------|------|----------|---------------|
| **Focused Sprint** | Quick Start user, clear idea, uninterrupted time | 15-45 min | Auto-save at every decision |
| **Interrupted Flow** | Practitioner/architect, complex agent, interrupted workday | Multiple sessions over days | Auto-save + attention map + "where you left off" |
| **Guided Journey** | First-time user, exploring possibilities | 3-5 short sessions | Saves + mirror agent resumes context |

### The Critical Design Rule: Every Decision Is Persistent

The user should be able to:
1. **Leave at any point** and come back to exactly where they were
2. **Change any previous decision** and see what ripple effects it has (no locked-in decisions until the coherence check)
3. **See what's settled vs. what needs attention** via the attention map

This is the "Recoverable" characteristic from the target state: every decision can be revised, every path can be retraced. The cost of changing direction should be low.

### The Mirror Agent as Session Companion

The workflow agent (the one guiding the user) should function as a **Mirror** — reflecting the user's decisions back, surfacing gaps, suggesting alternatives — not as a director telling them what to do. The Mirror's stance matches the phase:

- **Discovery:** "What would ideal look like?" (expansive, possibility-oriented)
- **Structure:** "Here's a gap — how would you like to handle it?" (constructive, shaping)
- **Realisation:** "This boundary is now locked in. Here's what that means." (concrete, grounding)

The Mirror never judges. It reflects. It surfaces contradictions ("You said the agent should never make final decisions, but you've allocated 'final assessment' to the agent — which is it?"). It offers alternatives ("Other Review Partners use this boundary — would it fit?"). It never says "you should."

---

## Summary: The 7 Non-Negotiable UX Principles

1. **Pattern-first, not blank-page** — the user selects an archetype and gets 40-70% pre-filled. They build, not fill in.

2. **Identity before behaviour** — the 4 identity questions come before anything else. Everything derives from identity.

3. **Possibility gradient as visual texture** — early sections feel expansive, later sections feel concrete. The visual environment shifts.

4. **Typed inputs and typed outputs** — every cognitive mode gets its own interaction modality. Every output section is presented as its natural type. No walls of text in, no walls of text out.

5. **One clear next step, always** — the attention map shows exactly what needs attention. The user never faces 40 empty fields.

6. **Every decision is persistent and revisable** — auto-save, resume, and ripple-effect visibility. The cost of changing direction is low.

7. **The feeling cascade: Relief → Curiosity → Confidence → Evidence** — each interaction point produces a feeling, not just information. The user should feel the boundary being drawn, not just see it.

---

The single most important design insight: **this workflow is designing its own input surface.** The same type collision problem that the workflow exists to solve (agents producing undifferentiated prose) is present in the workflow's own user interface. If we solve type collision for the user's agent specification but reproduce it in the workflow's own input surface, we've built a tool that preaches one thing and practices another.

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `26d28684...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent — it takes user requirements and produces a complete, platform-agnostic design specification that another workflow could then use to build the agent on any platform (LangGraph, CrewAI, AutoGen, etc.).

Please provide your expert perspective on:
1. What are the essential steps/phases this workflow agent should go through? (e.g., intake, analysis, design, validation)
2. What agentic patterns apply here? (e.g., ReAct, planning, multi-step, human-in-the-loop)
3. What should the design spec artifact contain? (e.g., agent persona, tools, memory, decision logic, guardrails, failure modes)
4. What supporting artifacts should be produced alongside the spec?
5. How should the workflow handle ambiguity, conflicting requirements, or gaps in user input?
6. What does the state machine / flow of this workflow look like?

Focus on the agentic architecture of the workflow itself — the design of the design agent. Not implementation code.

### Response

Good — this is a rich design challenge. Let me work through all six dimensions.

---

## 1. Essential Phases

The critical structural insight from your own CAWDP work applies here too: **Direction → Destination → Path → Work**. You can't decompose what you haven't defined the destination for. The workflow should follow this gradient, starting in pure possibility and tightening toward constraint.

Here are **7 phases** — I'm compressing CAWDP's 10 into what a single workflow agent can practically handle while preserving the gradient:

### Phase 1: INTAKE — "What are we building and for whom?"
**Mode:** Receptive + Exploratory
**What happens:** The workflow captures the user's raw input — business problem, target user, domain, constraints, any existing mental model. This is NOT a structured form. It's a conversation or free-form input that the workflow then shapes.

**Key actions:**
- Capture raw requirements (could be a paragraph, a voice note, a filled template, a messy brain-dump)
- Identify the stakeholder surface level (who will USE this agent — that determines output format)
- Detect the domain and context
- Flag immediate contradictions or gaps

**Output:** Raw Requirement Package (typed but not yet structured)

### Phase 2: IDENTITY — "What IS this agent?"
**Mode:** Possibility-oriented (pure)
**What happens:** Four identity questions, asked in a way that doesn't feel like a questionnaire. The workflow uses the user's own language, not technical jargon.

**The four questions:**
1. **What IS this agent?** — Not "what does it do?" but "what is it at its core?" (Essence)
2. **What's its stance toward possibility?** — Is it an explorer (opens space), a builder (shapes space), or a guard (constrains space)? (Orientation)
3. **What would VIOLATE its identity?** — What would make it NOT be itself anymore? (Identity boundary)
4. **What would it mean for this agent to be WRONG?** — Its worst failure IS its identity boundary in reverse. (Failure = identity)

**Key insight:** If the user can answer these four questions, 40-70% of the spec is determined. The pattern system pre-fills the rest. If the user CAN'T answer, the workflow explores with them — it doesn't just skip ahead.

**Output:** Identity Card (4 answers + inferred agent class + inferred orientation)

### Phase 3: BOUNDARIES — "What does it NOT do?"
**Mode:** Possibility-oriented → Bridge (transitioning)
**What happens:** Before defining what the agent DOES, define what it NEVER does. This is the hardest boundary to maintain and the most important one.

**Key actions:**
- From the identity violation (#3 above), derive explicit "never" rules
- From the failure mode (#4 above), derive authority boundaries
- Identify the principal — who does this agent act on behalf of?
- Map the reversibility of its actions (can you undo what it does? easily, with effort, or not at all?)
- Flag any area where the agent's output could cause external harm if accepted without review

**Output:** Boundary Map (never-rules, authority boundaries, reversibility classification, harm assessment)

### Phase 4: ARCHITECTURE — "What does it need to work?"
**Mode:** Bridge → Constraint-oriented (tightening)
**What happens:** Now that we know WHAT it is and what it DOESN'T do, we can define what it needs. This is where the spec takes shape.

**Key actions:**
- Define the task space (what cognitive operations does it perform?)
- Classify each task by agent class (Extractor / Measurer / Assessor / Generator / Aggregator)
- For each task: what inputs does it need? What outputs does it produce? What quality checks apply?
- Map dependencies between tasks (what needs to happen before what?)
- Identify what knowledge the agent needs access to
- Identify what tools/capabilities it needs
- Determine composition: is this one agent, a team, or a workflow?

**Output:** Architecture Blueprint (task map, class assignments, dependencies, knowledge requirements, tool requirements, composition decision)

### Phase 5: BEHAVIOUR — "How does it act?"
**Mode:** Constraint-oriented
**What happens:** Define the decision logic, reasoning patterns, and behavioural constraints.

**Key actions:**
- Define the reasoning approach (when does it plan vs react vs ask for help?)
- Define escalation rules (when does it STOP and hand back to a human?)
- Define confidence thresholds (what confidence level triggers what action?)
- Define the progressive autonomy path (shadow → advisory → supervised → autonomous — what does trust look like for THIS agent?)
- Write the directive/instructions in the agent's own voice
- Define verification protocols (who checks its work and how?)

**Output:** Behaviour Specification (reasoning rules, escalation triggers, confidence thresholds, autonomy path, directive draft, verification protocol)

### Phase 6: VALIDATION — "Does this hold together?"
**Mode:** Adversarial (constructive)
**What happens:** The workflow stress-tests its own design. This is NOT optional — it's a quality gate.

**Key actions:**
- Check internal consistency (do the boundaries conflict with the tasks?)
- Check identity coherence (would the defined behaviour violate the identity?)
- Check completeness (are there gaps in the task map or dependencies?)
- Check for the worst failure mode (from identity question #4 — can it happen given the current design?)
- Check for harm paths (can the agent's output cause external harm? Is there a DO_NOT_SUGGEST mechanism?)
- Check for the hardest boundary moment (when is the agent most likely to break its own rules?)
- Present findings to the user as structured decision inputs, not verdicts

**Output:** Validation Report (consistency check, gap analysis, risk register, recommended changes)

### Phase 7: SPECIFICATION — "Here's the complete design"
**Mode:** Constraint-oriented (final)
**What happens:** Compile all validated outputs into the complete, platform-agnostic design specification.

**Key actions:**
- Assemble all phase outputs into the final spec document
- Apply safe defaults for anything not explicitly specified by the user
- Generate the spec in a format that any implementation workflow can consume
- Tag every element with its source phase (traceability — you can always trace back to WHY a decision was made)
- Mark confidence levels on every section (what's well-defined vs what needs more exploration)

**Output:** Complete Agent Design Specification (the primary deliverable)

---

## 2. Agentic Patterns

This workflow is NOT a simple ReAct agent. It's a **structured multi-phase workflow with conditional routing and human checkpoints**. Here's what applies:

### Primary pattern: **Planned Workflow with Human Gates**

Not "think-act-observe" in a loop. This is a **defined sequence of phases with decision points** between them. The workflow knows what phase comes next, but it can also loop back, skip, or pause.

**Why this pattern:** The output is a design specification, not a quick answer. Each phase builds on the previous one. The dependencies between phases are structural (you can't define behaviour before you know identity), not optional.

### Secondary pattern: **Human-in-the-Loop at Phase Gates**

The human doesn't approve every step. They approve at **natural decision points:**
- After Identity (is this the right agent?)
- After Boundaries (are these the right lines?)
- After Validation (do you accept the risks?)
- Before Specification (ready to finalize?)

**Why:** Too much human input = slow and frustrating. Too little = drift. The gates are at the moments where the user's judgment is structurally irreplaceable (complementarity gap ≥ 6 in CAWDP terms).

### Tertiary pattern: **Pattern Matching + Safe Defaults**

When the user's input matches a known agent pattern (Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner), the workflow pre-fills 40-70% of the spec and flags what needs attention. This is convention-over-configuration — the framework decides unless you override.

**Why:** Reduces the user's burden from "design everything from scratch" to "review and adjust pre-validated defaults." This is the 15-minute agent specification.

### Pattern that does NOT apply: **ReAct**

ReAct is for agents that need to reason about an uncertain environment. This workflow operates in a KNOWN environment (its own phases), with KNOWN dependencies. It doesn't need to "figure out what to do next" — it needs to execute a designed process well.

---

## 3. What the Design Spec Should Contain

Organized into 8 sections, each traceable to a phase:

### Section 1: IDENTITY
- Agent name and role description (in plain English)
- The four identity answers (essence, orientation, identity violation, worst failure)
- Agent class (Extractor / Measurer / Assessor / Generator / Aggregator)
- Orientation (Possibility / Bridge / Constraint)
- Principal declaration (who it acts on behalf of)

### Section 2: BOUNDARIES
- Explicit "never" rules (what it NEVER does)
- Authority boundaries per task (what it CAN decide vs what it can only prepare)
- Reversibility classification per action type (easy undo / effort undo / no undo)
- Harm assessment (can its output cause external harm? yes/no + mechanism)
- DO_NOT_SUGGEST triggers (when it should flag uncertainty instead of suggesting)

### Section 3: TASK MAP
- Complete task list with cognitive operation type per task
- Agent class assignment per task
- Input schema per task (what information it needs)
- Output schema per task (what it produces, in what format)
- Dependencies between tasks (what must happen before what)
- Composition decision (single agent / team / workflow + rationale)

### Section 4: KNOWLEDGE REQUIREMENTS
- What the agent needs to know (domain knowledge, context, reference data)
- Knowledge quality requirements (accuracy, completeness, sufficiency minimums)
- Knowledge update cadence (how often does its knowledge need refreshing?)
- Information boundaries (what should it NOT have access to and why)

### Section 5: CAPABILITIES
- Tool/capability requirements (what it needs to be able to DO)
- Integration points (what systems it needs to connect to)
- Invocation method (how is it triggered? scheduled, event-driven, on-demand)
- Output delivery (how does it deliver results? format, channel, frequency)

### Section 6: BEHAVIOUR RULES
- Reasoning approach (when to plan, react, or escalate)
- Escalation triggers (specific conditions that hand back to human)
- Confidence thresholds (what confidence level triggers what action)
- Progressive autonomy path (shadow → advisory → supervised → autonomous, with promotion criteria)
- Directive draft (the agent's instructions in its own voice)

### Section 7: VERIFICATION & TRUST
- Verification protocol (who checks what and how — 3 levels: structural, meaning, authority)
- Epistemic metadata requirements (confidence, provenance, assumptions, limitations, recency, uncertainty on every output)
- Audit trail requirements (what gets logged, at what assurance level)
- Cost budget (per-task and overall budget with halt conditions)
- Override protocol (how a human overrides, what happens when they do)

### Section 8: FAILURE & RECOVERY
- Failure mode register (what can go wrong, per task)
- Recovery paths (what happens after each failure type)
- Worst failure mode (from identity question #4 — the design MUST prevent this)
- Hardest boundary moment (when is the agent most likely to break its own rules?)
- Specification aging schedule (when should this design be reviewed/updated?)

---

## 4. Supporting Artifacts

The spec is the primary deliverable, but these artifacts support it:

1. **Boundary Map** (visual) — A single-page "who does what" diagram. Three columns: Human / Agent / System. Each row is a task. This is the most shareable artifact — put it on the wall.

2. **Risk Register** — Every identified failure mode, its likelihood, impact, and mitigation. Traceable to specific spec sections.

3. **Decision Log** — Every significant design decision with: what was decided, what alternatives were considered, why this choice was made, and who made it. This is the decision archaeology layer.

4. **Gaps & Assumptions Register** — What the workflow couldn't resolve and had to assume. These are the places where the spec is weakest and where implementation will need human judgment first.

5. **Implementation Readiness Checklist** — A checklist for the implementation workflow: "Does the implementing team have everything they need?" Organized by spec section, with clear pass/fail criteria.

6. **Confidence Map** — A visual showing which spec sections are high-confidence (well-defined by the user) vs low-confidence (assumed or defaulted). Implementation teams should address low-confidence sections first.

---

## 5. Handling Ambiguity, Conflicts, and Gaps

This is the hard part. Most design tools either demand perfect input (blocking on every gap) or silently fill gaps with defaults (creating hidden risk). The workflow should do NEITHER.

### Ambiguity — "I'm not sure what I want"
**Strategy: Explore before assuming.**

When the workflow detects ambiguity (vague requirements, unclear priority, multiple possible interpretations):
1. **Name the ambiguity explicitly** — "I see two possible meanings here: A and B. Which one?"
2. **Show the consequence of each option** — "If A, then [design implication]. If B, then [different implication]."
3. **If the user can't decide, apply the safe default** — The less risky interpretation wins. Flag it as a default, not a decision.
4. **Mark it in the Gaps Register** — Future review should revisit this.

**Never:** Silently pick one path and not tell the user. That's how you get agents that do the wrong thing with confidence.

### Conflicting Requirements — "I want it fast AND thorough AND cheap"
**Strategy: Make the trade-off visible, don't resolve it for the user.**

1. **Name the conflict** — "You've asked for X and Y, but they trade off against each other because [reason]."
2. **Show the trade-off spectrum** — "More X means less Y. Here's what different positions look like."
3. **Ask for a priority ranking** — "If you had to rank these, what matters most?"
4. **If unresolvable, mark as a design tension** — Some conflicts are genuine (speed vs safety, coverage vs depth). These aren't bugs — they're design constraints. Document them as tensions that the implementation must manage, not problems to solve once.

### Gaps — "The user didn't mention X"
**Strategy: Safe defaults with flags, not blank spaces or silent fills.**

1. **Distinguish between required gaps and optional gaps** — Required gaps (no identity, no boundaries) block the workflow. Optional gaps (no tool preference, no knowledge source) get safe defaults.
2. **Apply safe defaults for optional gaps** — Use the pattern system. If the user selected "Review Partner" pattern, the workflow knows the default verification protocol, default confidence thresholds, default escalation rules.
3. **Flag every default** — In the spec, defaults are visually distinct from user-specified decisions. The confidence map shows them as lower-confidence.
4. **Required gaps pause the workflow** — "I need to know who this agent acts on behalf of before I can design its authority boundaries. Let's figure this out together."

### The Meta-Principle
**"Doubt defaults to the human"** — When the workflow can't determine the right answer with high confidence, the human makes the call. The workflow PREPARES the decision (shows options, consequences, trade-offs) but the human DECIDES. This is the core design principle applied to the meta-agent itself.

---

## 6. State Machine / Flow

```
┌─────────┐
│  INTAKE  │
└────┬─────┘
     │
     ▼
┌──────────┐     ┌──────────────────┐
│ IDENTITY  │────▶│  Pattern Match?  │
└────┬──────┘     │  (if match,      │
     │            │   pre-fill 40-70%)│
     │ NO         └──────────────────┘
     │ gap?
     │
     ▼
┌────────────┐
│ BOUNDARIES  │
└────┬────────┘
     │
     ▼
┌──────────────┐
│  ARCHITECTURE │
└────┬──────────┘
     │
     ▼
┌──────────────┐
│   BEHAVIOUR   │
└────┬──────────┘
     │
     ▼
┌──────────────┐     ┌───────────────────────┐
│  VALIDATION   │────▶│  Issues found?        │
└────┬──────────┘     │  YES → loop back to   │
     │                │  relevant phase        │
     │ NO issues      └───────────────────────┘
     │ (or accepted)
     ▼
┌───────────────┐
│ SPECIFICATION  │
└────┬───────────┘
     │
     ▼
┌────────────┐
│  COMPLETE   │
└────────────┘
```

### Key State Machine Details

**Human gates** (pause for human input before proceeding):
- After INTAKE → confirm understanding
- After IDENTITY → confirm "is this the right agent?"
- After BOUNDARIES → confirm "are these the right lines?"
- After VALIDATION → confirm "do you accept these risks?"

**Loop-back paths** (validation can send you back):
- Identity conflict → back to IDENTITY
- Boundary violation → back to BOUNDARIES
- Architecture gap → back to ARCHITECTURE
- Behaviour contradicts identity → back to BEHAVIOUR (or IDENTITY if the identity itself is the problem)

**Skip paths** (not every phase requires full depth):
- If pattern match is high-confidence → pre-fill IDENTITY and BOUNDARIES, go straight to ARCHITECTURE for review
- If the agent is simple (single task, low stakes, no harm potential) → compress BOUNDARIES and BEHAVIOUR into a single step

**Exit paths** (the user can stop at any gate):
- After IDENTITY → "I need to think about this more" → save and exit with partial spec
- After BOUNDARIES → "I have enough to start" → exit with boundary map + identity card
- After VALIDATION → "This isn't what I wanted" → exit with diagnostic only

**What the state carries between phases:**
- All previous phase outputs (accumulating, never replacing)
- The growing Gaps Register
- The growing Decision Log
- The confidence map (updated after each phase)
- The current pattern match confidence (refined with each phase)

### One Critical Design Decision

**The workflow should NOT be a single agent doing all 7 phases.** It should be a **workflow** (in Agno terms) or a **pipeline** (in CAWDP terms) — a sequence of specialist steps, each with its own authority boundary.

Why: The identity-asking phase needs a different orientation (possibility-oriented, open, expansive) than the validation phase (adversarial, constrained, skeptical). A single agent switching modes will blur the boundary. The validation step MUST be able to challenge the architecture step's decisions without bias.

In practical terms: this is a workflow with 5-7 specialist agents, not one generalist agent with a long prompt. Each specialist has clear authority boundaries:
- **Intake Agent** (Extractor) — captures, never judges
- **Identity Explorer** (Assessor, possibility-oriented) — reflects, never decides
- **Boundary Mapper** (Measurer + Assessor, bridge-oriented) — classifies and flags, never finalizes
- **Architect** (Generator, constraint-oriented) — builds from known inputs, never reopens possibility
- **Validator** (Assessor, adversarial) — stress-tests, never designs
- **Compiler** (Aggregator) — assembles, never adds new content

The human is the decision-maker at every gate. The agents prepare judgment; the human makes judgment. Even for this meta-agent.

---

**Bottom line:** The workflow that designs agents should practise what it produces. If the output spec says "agents need identity, boundaries, and verification," then the workflow itself needs identity, boundaries, and verification. If the output says "doubt defaults to the human," then the workflow itself must default uncertain decisions to the human. The meta-agent IS the proof of the methodology.

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-04-27T06:48:46* · `glm-5.1:cloud` · `bc5c5e21...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent — it takes user requirements and produces a complete, platform-agnostic design specification that another workflow could then use to build the agent on any platform (LangGraph, CrewAI, AutoGen, etc.).

Please provide your expert perspective on:
1. What are the essential steps/phases this workflow agent should go through? (e.g., intake, analysis, design, validation)
2. What agentic patterns apply here? (e.g., ReAct, planning, multi-step, human-in-the-loop)
3. What should the design spec artifact contain? (e.g., agent persona, tools, memory, decision logic, guardrails, failure modes)
4. What supporting artifacts should be produced alongside the spec?
5. How should the workflow handle ambiguity, conflicting requirements, or gaps in user input?
6. What does the state machine / flow of this workflow look like?

Focus on the agentic architecture of the workflow itself — the design of the design agent. Not implementation code.

We've gathered input from all three team members on designing an agentic workflow that produces agent design specs. Please synthesize the following three contributions into ONE unified, cohesive prototype design document.

The document should integrate the best ideas from each, resolve any tensions, and present a clear, actionable prototype that the team can hand off to an implementation workflow.

## Team Input Summary

### Business Strategist Key Points:
- Three target users: Daniel Kovacs (domain expert with blank-page problem), Sarah Chen (business owner needing verification), Developers (needing structured specs)
- Value prop: "Design spec is the product, methodology is the moat, implementation is the commodity, trust infrastructure is the category"
- Key risks: "Just another template" perception, over-engineering the workflow, platform-agnostic spec falling between stools, credibility gap, category creation difficulty
- Output strategy: One typed graph, many stakeholder views. Progressive engagement: Boundary Map (30 min) → Allocation Map (half day) → Operations Manual (1-2 weeks) → Trust Ledger (ongoing)
- Platform-agnostic: Spec describes WHAT and WHY, never WHICH TOOL. Test: could two different implementation teams on different frameworks produce functionally equivalent agents?

### AI UX Innovator Key Points:
- Three "Rooms": Discovery (expansive), Structure (constructive), Realisation (concrete)
- Pattern-first entry: Select archetype → pre-fill 40-70% → user overrides what matters
- 4 Identity Questions first (essence, orientation, violation, wrongness)
- Cognitive mode → input modality mapping (narrative=conversation, boundary=drag-sort, exploratory=cards, verification=scenarios, architectural=canvas, configurational=dials, evaluative=dashboard)
- Attention Map navigation (settled/needs attention/requires input/not yet applicable)
- Typed outputs (boundary map=visual, authority=cards, etc.)
- Single session + multi-session support. Every decision persistent and revisable.
- Mirror Agent as companion (reflects, never judges)
- 7 UX principles: pattern-first, identity-before-behaviour, possibility gradient, typed I/O, one clear next step, decisions revisable, feeling cascade

### Agentic Expert Key Points:
- 7 phases: Intake → Identity → Boundaries → Architecture → Behaviour → Validation → Specification
- Pattern: Planned Workflow with Human Gates (NOT ReAct)
- Human gates after: Intake, Identity, Boundaries, Validation
- Multi-agent workflow (not single agent): Intake Agent, Identity Explorer, Boundary Mapper, Architect, Validator, Compiler
- 8-section spec: Identity, Boundaries, Task Map, Knowledge Requirements, Capabilities, Behaviour Rules, Verification & Trust, Failure & Recovery
- 6 supporting artifacts: Boundary Map, Risk Register, Decision Log, Gaps & Assumptions Register, Implementation Readiness Checklist, Confidence Map
- Ambiguity strategy: "Doubt defaults to the human" — explore before assuming, make trade-offs visible, safe defaults with flags
- State machine with loop-back paths, skip paths for simple agents, exit paths at every gate
- The meta-principle: the workflow must practise what it produces

## Your Task:
Create a unified prototype design document that:
1. Integrates all three perspectives into a single coherent design
2. Resolves any tensions (e.g., the 3 "Rooms" from UX vs the 7 "Phases" from architecture — map them to each other)
3. Presents the workflow architecture, user journey, output artifacts, and key design principles as one unified story
4. Is structured as a prototype design spec that another workflow could use to implement this
5. Keeps it at design spec level — no implementation code or platform specifics

Make it clear, well-structured, and actionable. This is the deliverable the user asked for.

### Response

Now let me write the unified document.

---

# Agent Design Workflow — Prototype Design Specification

**Version:** 0.1  
**Status:** Prototype — ready for implementation workflow handoff  
**Date:** 2025

---

## 1. What This Is

An agentic workflow that takes a user's raw requirements and produces a complete, platform-agnostic design specification for an AI agent.

**Platform-agnostic** means the spec describes WHAT the agent does and WHY — never WHICH TOOL delivers it. The test: could two implementation teams on different frameworks (LangGraph, CrewAI, Agno, AutoGen) read the same spec and produce functionally equivalent agents? If yes, the spec is platform-agnostic.

**The meta-principle:** This workflow must practise what it produces. If the output spec says agents need identity, boundaries, and verification, then this workflow has identity, boundaries, and verification. If the output says doubt defaults to the human, then this workflow defaults uncertain decisions to the human.

---

## 2. Three Users, Three Surfaces

One workflow, three entry points. The same engine produces different outputs depending on who's using it.

| | **Daniel Kovacs**<br>Domain Expert | **Sarah Chen**<br>Business Owner | **Implementation Team**<br>Developers |
|---|---|---|---|
| **Their problem** | Blank page — "I know my domain but I can't design an agent" | Boundary & verification — "I don't know where AI should stop" | Type collision — "I need structured specs, not prose documents" |
| **What they need** | Guided design, not a form to fill | A clear line and a way to verify it | Typed, structured specs they can build from |
| **How they enter** | Conversation + Pattern selection | Boundary Map session (30 min) | Receives completed spec as input |
| **What they get** | Full design spec + all artifacts | Boundary Map → Allocation Map → Operations Manual | Implementation-ready typed specification |
| **Time commitment** | 2-4 hours (can pause and resume) | 30 min to half day | Reads the output, doesn't use the workflow |

Daniel and Sarah are the primary users of the workflow. The implementation team is the consumer of the output.

---

## 3. The Three-Layer Architecture

The system has three layers that describe the same workflow from three angles:

| Layer | Purpose | Structure |
|---|---|---|
| **Rooms** (Experience) | What the user FEELS | 3 visual/cognitive environments |
| **Phases** (Logic) | What the workflow DOES | 7 processing stages with specialist agents |
| **Milestones** (Value) | What the user GETS | 4 exit points, each with a tangible artifact |

These layers are NOT separate systems. They're the same workflow described for three audiences: the user (rooms), the agents (phases), and the business (milestones).

### How They Map Together

```
ROOMS              PHASES                              MILESTONES
                    ┌──────────┐
                    │ 1. Intake │──── Pattern match
                    └─────┬─────┘
                          │
DISCOVERY          ┌──────┴──────┐
(Expansive,         │ 2. Identity  │
 open, possibility) │ 3. Boundaries│────▶ MILESTONE 1: Boundary Map
                    └──────┬──────┘     (30 min, free or $495)
                           │
STRUCTURE          ┌───────┴───────┐
(Constructive,      │ 4. Architecture│
 shaping,           │ 5. Behaviour   │────▶ MILESTONE 2: Allocation Map
 constraint)        └───────┬───────┘     (half day, $795-1,495)
                           │
REALISATION        ┌───────┴───────┐
(Concrete,          │ 6. Validation  │
 verified,          │ 7. Specification│───▶ MILESTONE 3: Operations Manual
 committed)         └───────────────┘     (1-2 weeks, $5K-25K)
                                           MILESTONE 4: Trust Ledger
                                           (ongoing, $2-5K/qtr)
```

**The gradient from possibility to constraint is deliberate.** Discovery opens space. Structure shapes it. Realisation locks it down. The user should feel this shift — the visual environment, the interaction style, and the agent's tone all change as they move through the rooms.

---

## 4. The Seven Phases — Detail

### Phase 1: INTAKE

**What happens:** The user describes what they need in their own words. A paragraph, a brain-dump, a voice note, answers to a few starter questions — anything. The workflow listens, captures, and shapes.

**Agent:** Intake Agent (Extractor class — captures, never judges)

**Key actions:**
- Receive raw input in whatever form the user provides
- Parse and type the input: domain, business problem, target user, constraints, any existing mental model
- Run **pattern matching** against known agent archetypes:
  - Signal Detector (monitoring, alerting)
  - Multi-Lens Analyst (multi-perspective analysis)
  - Discovery Explorer (research, ideation)
  - Learning Scaffold (teaching, tutoring)
  - Review Partner (reviewing, quality-checking)
- If high-confidence match (≥80%): flag the pattern, prepare pre-fills for downstream phases
- If low-confidence match: note it, proceed without pre-fills — the Identity phase will explore further
- Detect immediate contradictions or gaps
- Identify the stakeholder surface level (Daniel, Sarah, or both)

**Output:** Typed Requirement Package + Pattern Match Assessment

**Human gate:** "Here's what I understood. Is this right?" — User confirms the workflow heard them correctly before proceeding.

**Cognitive mode:** Narrative (conversation)
**Interaction:** Conversational input — the user talks, the workflow listens

---

### Phase 2: IDENTITY

**What happens:** Four questions that determine 40-70% of the entire spec. If the user selected a pattern in Intake, pre-filled answers appear — the user reviews, overrides, or accepts. If no pattern matched, the workflow explores with them.

**Agent:** Identity Explorer (Assessor class, possibility-oriented — reflects, never decides)

**The four identity questions:**
1. **What IS this agent?** — Not "what does it do?" but "what is it at its core?" (Example: "It's a lease risk spotter" not "it reviews leases")
2. **What's its stance toward possibility?** — Does it open space (explorer), shape space (builder), or guard space (guard)? This determines how the agent responds to ambiguity — by expanding options, narrowing options, or flagging them.
3. **What would VIOLATE its identity?** — What would make it NOT be itself anymore? (Example: "If it started giving legal advice, it wouldn't be a spotter anymore — it would be an advisor")
4. **What would it mean for this agent to be WRONG?** — Its worst failure IS its identity boundary in reverse. (Example: "The worst wrong is flagging a real risk as fine — that's the exact opposite of spotting")

**Pre-fill behaviour:** If a pattern was matched in Intake:
- Pre-filled answers appear with a "Why this answer?" explanation
- User can accept, override, or say "I'm not sure"
- "I'm not sure" triggers an exploration dialogue

**Output:** Identity Card (4 answers + agent class + orientation)

**Human gate:** "Is this the right agent?" — User confirms identity before boundaries are drawn.

**Cognitive mode:** Narrative + Exploratory (conversation + cards showing pre-filled options)
**Interaction:** Conversation for free-form answers. Cards for pre-filled pattern options that the user accepts/overrides.

---

### Phase 3: BOUNDARIES

**What happens:** Before defining what the agent DOES, define what it NEVER does. This is the hardest boundary to maintain and the most important one.

**Agent:** Boundary Mapper (Measurer + Assessor class, bridge-oriented — classifies and flags, never finalizes)

**Key actions:**
- Derive explicit "never" rules from identity violation (question #3)
- Derive authority boundaries from failure mode (question #4) — what it CAN decide vs what it can only PREPARE a decision for
- Identify the **principal** — who this agent acts on behalf of (a person, a role, or an organisation)
- Classify the **reversibility** of each action type:
  - Easy undo (e.g., drafting text — just delete it)
  - Effort undo (e.g., sending an email — recall + follow-up)
  - No undo (e.g., executing a trade — the market already moved)
- Assess **harm potential** — can the agent's output cause external harm if accepted without review? (yes/no + mechanism)
- If yes → flag as harm-capable and require DO_NOT_SUGGEST mechanism

**Output:** Boundary Map (never-rules, authority boundaries, reversibility classification, harm assessment)

**Human gate:** "Are these the right lines?" — User confirms boundaries.

**This is Milestone 1.** The user can exit here with a Boundary Map — a single-page visual showing who does what. It's independently valuable: they can take it to any vendor, any platform, any implementation team.

**Cognitive mode:** Boundary (drag-sort — place tasks in "human does" / "agent does" / "system does" columns)
**Interaction:** Drag-sort zones for task allocation. Cards for each boundary rule.

---

### Phase 4: ARCHITECTURE

**What happens:** Now that identity and boundaries are defined, the workflow can determine what the agent needs to work. The possibility space has been shaped — this phase fills in the structure.

**Agent:** Architect (Generator class, constraint-oriented — builds from known inputs, never reopens possibility)

**Key actions:**
- Define the **task space** — every cognitive operation the agent performs
- Classify each task by agent class:
  - Extractor: gathers information, never judges
  - Measurer: measures against rules, never interprets
  - Assessor: evaluates and flags, never finalizes
  - Generator: creates content, always under constraint
  - Aggregator: compiles and assembles, never adds new content
- For each task: input schema, output schema, quality checks
- Map **dependencies** between tasks (what must happen before what)
- Determine **composition**: is this one agent, a team, or a workflow? (The answer comes from the task map — single-class agents are often one agent; multi-class tasks often need a workflow)
- Identify **knowledge requirements** — what the agent needs to know, with quality minimums
- Identify **capability requirements** — what tools/integrations the agent needs
- Define **information boundaries** — what the agent should NOT have access to

**Pre-fill behaviour:** Pattern match + identity answers determine ~60% of the task map. The user reviews, adjusts, and adds domain-specific tasks.

**Output:** Architecture Blueprint (task map with class assignments, dependencies, knowledge/capability/information requirements, composition decision)

**Cognitive mode:** Architectural (canvas with typed connections between tasks)
**Interaction:** Visual canvas. Tasks as cards, dependencies as lines. Drag to reorder, click to configure.

---

### Phase 5: BEHAVIOUR

**What happens:** Define how the agent acts — its reasoning, escalation rules, confidence thresholds, and progressive autonomy path.

**Agent:** Architect continues (same agent, constrained by architecture outputs)

**Key actions:**
- Define **reasoning approach** — when does the agent plan vs react vs ask for help?
- Define **escalation triggers** — specific conditions that hand back to a human (e.g., confidence below threshold, boundary violation detected, harm-capable output without verification)
- Define **confidence thresholds** — what confidence level triggers what action:
  - High confidence (4-5): proceed
  - Medium confidence (3): proceed with flags
  - Low confidence (1-2): stop and escalate
- Define **progressive autonomy path**:
  - Shadow: agent runs alongside, human does everything, workflow tracks what agent would have done
  - Advisory: agent suggests, human reviews every suggestion
  - Supervised: agent acts, human approves before anything leaves
  - Autonomous: agent acts within boundaries, human monitors the data
  - For each level: specific promotion criteria (not vibes — measured override rate, verification pass rate, cost variance)
- Draft the **directive** — the agent's instructions in its own voice (not technical system prompt — a plain-English description of how it behaves)
- Define **verification protocol** — who checks what and how:
  - Level 1 (structural): does the output match the expected format?
  - Level 2 (meaning): is the output correct in substance?
  - Level 3 (authority): did the agent stay within its boundaries?

**Safe defaults** apply to all of these. The user only needs to override what differs from the pattern's standard behaviour.

**Output:** Behaviour Specification (reasoning rules, escalation triggers, confidence thresholds, autonomy path, directive draft, verification protocol)

**Cognitive mode:** Configurational (dials, toggles, presets) + Evaluative (dashboard for autonomy path)
**Interaction:** Dials/toggles for confidence thresholds. Timeline view for progressive autonomy. Text editor for directive draft.

---

**This is Milestone 2.** The user can exit here with an Allocation Map — who does what, with what authority, what happens when things fail, and how to recover. It's independently valuable: they can brief any implementation team with this document.

---

### Phase 6: VALIDATION

**What happens:** The workflow stress-tests its own design. This is NOT optional. It's a quality gate.

**Agent:** Validator (Assessor class, adversarial — stress-tests, never designs)

**This agent MUST be separate from the Architect.** The same agent that designed the spec cannot validate it — that's like a student grading their own exam.

**Key checks:**
1. **Identity coherence** — Would the defined behaviour violate the agent's identity? (If the Identity says "never gives advice" but the Behaviour says "provides recommendations" → flag)
2. **Boundary consistency** — Do the boundaries conflict with the tasks? (If Boundaries says "never decides" but Architecture assigns Assessor tasks with decision authority → flag)
3. **Completeness** — Are there gaps in the task map, dependencies, or knowledge requirements?
4. **Worst failure mode** — From identity question #4: can it happen given the current design? If yes → recommend a specific safeguard
5. **Harm paths** — Can the agent's output cause external harm? Is there a DO_NOT_SUGGEST mechanism?
6. **Hardest boundary moment** — When is the agent most likely to break its own rules? (e.g., under time pressure, with ambiguous input, when the user says "just do it")

**Output:** Validation Report (pass/fail per check, risk register with all identified issues, recommended changes)

**Human gate:** "Here's what I found. Do you accept these risks, or do you want to fix them?" — User decides what to address.

**Loop-back paths:**
- Identity conflict → back to Phase 2
- Boundary violation → back to Phase 3
- Architecture gap → back to Phase 4
- Behaviour contradicts identity → back to Phase 5 (or Phase 2 if the identity itself is the problem)

**Cognitive mode:** Verification (scenarios — "what if this happened?")
**Interaction:** Scenario cards showing stress-test results. Each issue is a card with: what was found, what it means, what to do about it, and whether it's a risk to accept or a problem to fix.

---

### Phase 7: SPECIFICATION

**What happens:** Compile all validated outputs into the complete design specification.

**Agent:** Compiler (Aggregator class — assembles, never adds new content)

**Key actions:**
- Assemble all phase outputs into the final spec (8 sections — see Section 6)
- Apply safe defaults for anything not explicitly specified
- Tag every element with its **source phase** (traceability)
- Mark **confidence levels** on every section (high/medium/low — derived from the attention/confidence data)
- Generate all **supporting artifacts** (see Section 7)
- Apply the **platform-agnostic test**: does this spec describe WHAT and WHY, never WHICH TOOL?

**Output:** Complete Agent Design Specification + Supporting Artifacts

**Human gate:** "Here's your complete specification. Review and approve."

**No loop-back from here.** If the user wants changes, they re-enter the workflow at the relevant phase. The spec is compiled, not living.

**Cognitive mode:** Evaluative (dashboard — overview of all sections, confidence levels, readiness)
**Interaction:** Summary dashboard. User can click into any section for detail. "Approve" button finalizes.

---

**This is Milestone 3.** The Operations Manual is a direct derivation from the complete spec — a shorter, operational document that the team follows day-to-day. Milestone 4 (Trust Ledger) is ongoing monitoring after deployment.

---

## 5. The Specialist Agents

| Agent | Class | Orientation | Authority Boundary | What It NEVER Does |
|---|---|---|---|---|
| **Intake Agent** | Extractor | Possibility | Capture only | Never judges, never filters, never interprets |
| **Identity Explorer** | Assessor | Possibility | Reflect only | Never decides identity, never qualifies possibility |
| **Boundary Mapper** | Measurer + Assessor | Bridge | Classify and flag only | Never finalizes boundaries, never draws the line |
| **Architect** | Generator | Constraint | Build from known inputs only | Never reopens possibility, never adds tasks not in the map |
| **Validator** | Assessor | Adversarial | Stress-test only | Never designs, never fixes, never decides what's acceptable |
| **Compiler** | Aggregator | Constraint | Assemble only | Never adds new content, never changes existing content |
| **Mirror Agent** | Assessor | Adaptive | Translate and reflect | Never judges, never decides, never filters information |

### The Mirror Agent — The User's Companion

The Mirror Agent is the **surface layer** — the agent the user talks to. The specialist agents are the **engine** — they do the work behind the scenes.

The Mirror Agent:
- Routes the user's input to the right specialist agent
- Translates specialist output into the user's language (plain English, domain terminology)
- Reflects the user's own words back to them for confirmation
- Never judges, never decides, never filters — it reflects and connects

Think of it as a concierge: the user talks to the concierge, the concierge sends the request to the right department, and the concierge presents the result in a way the user understands.

---

## 6. The Design Specification — What It Contains

The primary output is an 8-section design specification. Every section is platform-agnostic.

### Section 1: IDENTITY
| Item | Description |
|---|---|
| Agent name & role | In plain English (e.g., "Lease Risk Spotter") |
| Four identity answers | Essence, orientation, identity violation, worst failure |
| Agent class | Extractor / Measurer / Assessor / Generator / Aggregator |
| Orientation | Possibility / Bridge / Constraint |
| Principal | Who it acts on behalf of |
| Pattern matched | Which archetype was selected (if any) |

### Section 2: BOUNDARIES
| Item | Description |
|---|---|
| Never rules | What it NEVER does (derived from identity violation) |
| Authority boundaries | What it CAN decide vs what it can only PREPARE a decision for |
| Reversibility | Easy undo / effort undo / no undo — per action type |
| Harm assessment | Can its output cause external harm? yes/no + mechanism |
| DO_NOT_SUGGEST triggers | When it should flag uncertainty instead of suggesting |
| Information boundaries | What it should NOT have access to and why |

### Section 3: TASK MAP
| Item | Description |
|---|---|
| Complete task list | Every cognitive operation the agent performs |
| Class assignment per task | Extractor / Measurer / Assessor / Generator / Aggregator |
| Input schema per task | What information the task needs (format, type, source) |
| Output schema per task | What the task produces (format, type, destination) |
| Dependencies | What must happen before what |
| Composition | Single agent / team / workflow + rationale |

### Section 4: KNOWLEDGE REQUIREMENTS
| Item | Description |
|---|---|
| Domain knowledge | What it needs to know about the subject |
| Context | What it needs to know about the user/organisation |
| Reference data | Standards, rules, rubrics it measures against |
| Quality minimums | Accuracy, completeness, sufficiency thresholds |
| Update cadence | How often its knowledge needs refreshing |
| Information boundaries | What it should NOT have access to (repeated from Section 2 for implementation convenience) |

### Section 5: CAPABILITIES
| Item | Description |
|---|---|
| Tool/capability requirements | What it needs to be able to DO (not which specific tool — what function) |
| Integration points | What systems it connects to (what data flows in and out) |
| Invocation method | How it's triggered: scheduled / event-driven / on-demand |
| Output delivery | How it delivers results: format, channel, frequency |

### Section 6: BEHAVIOUR RULES
| Item | Description |
|---|---|
| Reasoning approach | When to plan, react, or escalate |
| Escalation triggers | Specific conditions that hand back to human |
| Confidence thresholds | What confidence level triggers what action |
| Progressive autonomy path | Shadow → Advisory → Supervised → Autonomous with promotion criteria |
| Directive draft | The agent's instructions in its own voice |
| Safe defaults | What the framework chose for the user (flagged, not hidden) |

### Section 7: VERIFICATION & TRUST
| Item | Description |
|---|---|
| Verification protocol | 3 levels: structural, meaning, authority — who checks what how |
| Epistemic metadata | 6 fields on every output: confidence, provenance, assumptions, limitations, recency, uncertainty |
| Audit trail | What gets logged, at what assurance level (logged / assured / verified) |
| Cost budget | Per-task and overall budget with halt conditions |
| Override protocol | How a human overrides and what happens when they do |

### Section 8: FAILURE & RECOVERY
| Item | Description |
|---|---|
| Failure mode register | What can go wrong per task |
| Recovery paths | What happens after each failure type |
| Worst failure mode | From identity #4 — the design MUST prevent this |
| Hardest boundary moment | When the agent is most likely to break its own rules |
| Specification aging schedule | When should this design be reviewed/updated? |

---

## 7. Supporting Artifacts

Produced alongside the spec, each independently valuable.

| Artifact | What It Is | Who Uses It | When |
|---|---|---|---|
| **Boundary Map** | Single-page visual: Human / Agent / System columns, tasks as rows | Sarah, any stakeholder | Milestone 1 — can exit here |
| **Risk Register** | Every identified failure mode with likelihood, impact, mitigation | Implementation team, governance participants | Produced in Validation |
| **Decision Log** | Every significant design decision: what was decided, alternatives, why, who decided | Any stakeholder (decision archaeology) | Accumulated throughout |
| **Gaps & Assumptions Register** | What the workflow couldn't resolve and had to assume | Implementation team (address these first) | Accumulated throughout |
| **Implementation Readiness Checklist** | "Does the implementing team have everything they need?" — organized by spec section | Implementation team | Produced in Specification |
| **Confidence Map** | High/medium/low confidence per spec section | Implementation team, governance participants | Produced in Specification |

---

## 8. Handling Ambiguity, Conflicts, and Gaps

The workflow uses one principle: **doubt defaults to the human.** The workflow PREPARES the decision (shows options, consequences, trade-offs) but the human DECIDES.

### When the user is vague — "I'm not sure what I want"

1. **Name the ambiguity explicitly** — "I see two possible meanings here: A and B. Which one?"
2. **Show the consequence of each option** — "If A, then [design implication]. If B, then [different implication]."
3. **If the user still can't decide** — Apply the safe default (the less risky interpretation wins). Flag it as a default, not a decision.
4. **Mark it in the Gaps Register** — Future review should revisit this.

**Never:** Silently pick one path and not tell the user.

### When requirements conflict — "I want it fast AND thorough AND cheap"

1. **Name the conflict** — "You've asked for X and Y, but they trade off because [reason]."
2. **Show the trade-off spectrum** — "More X means less Y. Here's what different positions look like."
3. **Ask for priority** — "If you had to rank these, what matters most?"
4. **If unresolvable** — Document as a design tension. Some conflicts are real. They're not bugs — they're constraints the implementation must manage.

### When information is missing — "The user didn't mention X"

1. **Distinguish required gaps from optional gaps:**
   - **Required gaps** (no identity, no boundaries) → pause the workflow, work with the user to fill them
   - **Optional gaps** (no tool preference, no knowledge source) → apply safe defaults, flag them
2. **Apply safe defaults for optional gaps** — The pattern system provides these. A "Review Partner" pattern has a default verification protocol, default confidence thresholds, default escalation rules.
3. **Flag every default** — In the spec, defaults are visually distinct from user decisions. The confidence map marks them as lower confidence.
4. **Required gaps pause the workflow** — "I need to know who this agent acts on behalf of before I can design its authority boundaries. Let's figure this out together."

---

## 9. State Machine

```
                    ┌───────────────────┐
                    │   START            │
                    │   (user enters     │
                    │    raw input)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │   PHASE 1: INTAKE │
                    │   (Extractor)      │
                    │   Pattern match    │
                    └────────┬──────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
         High match     Low match      No match
         (≥80%)         (40-79%)       (<40%)
              │              │              │
              ▼              ▼              ▼
        Pre-fill 50-   Pre-fill 20-    No pre-fill
        70% of next    40% of next     Explore mode
        phases         phases
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Is this right?"  │──── No → back to input
                    └────────┬──────────┘
                             │ Yes
                    ┌────────▼──────────┐
                    │ PHASE 2: IDENTITY │
                    │ (Assessor,        │
                    │  possibility)     │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Is this the      │──── No → explore more
                    │  right agent?"    │──── "I need to think" →
                    └────────┬──────────┘     SAVE & EXIT with
                             │ Yes              partial Identity Card
                    ┌────────▼──────────┐
                    │ PHASE 3:          │
                    │ BOUNDARIES        │
                    │ (Measurer+Assessor│
                    │  bridge)          │
                    └────────┬──────────┘
                             │
              ┌──────────────▼──────────────┐
              │ HUMAN GATE:                 │
              │ "Are these the right lines?"│
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 1 EXIT:    ║   │
              │ ║  Boundary Map         ║   │
              │ ║  (can stop here)      ║   │
              │ ╚═══════════════════════╝   │
              └──────────────┬──────────────┘
                             │ Continue
                    ┌────────▼──────────┐
                    │ PHASE 4:          │
                    │ ARCHITECTURE      │
                    │ (Generator,       │
                    │  constraint)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ PHASE 5:          │
                    │ BEHAVIOUR         │
                    │ (Generator,       │
                    │  constraint)      │
                    └────────┬──────────┘
                             │
              ┌──────────────▼──────────────┐
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 2 EXIT:    ║   │
              │ ║  Allocation Map       ║   │
              │ ║  (can stop here)      ║   │
              │ ╚═══════════════════════╝   │
              └──────────────┬──────────────┘
                             │ Continue
                    ┌────────▼──────────┐
                    │ PHASE 6:          │
                    │ VALIDATION        │
                    │ (Assessor,        │
                    │  adversarial)     │
                    └────────┬──────────┘
                             │
               ┌─────────────┼─────────────┐
               │             │             │
          Issues found   Minor issues   Clean pass
          (critical)     (acceptable)   
               │             │             │
        Loop back:     Flag risks     │
        Identity → P2  in report      │
        Boundary → P3  Accept &       │
        Architecture→P4  continue     │
        Behaviour → P5              │
               │             │             │
               └─────────────┼─────────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Accept risks or  │
                    │  fix issues?"     │
                    └────────┬──────────┘
                             │ Accept
                    ┌────────▼──────────┐
                    │ PHASE 7:          │
                    │ SPECIFICATION     │
                    │ (Aggregator)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Review & approve"│
                    └────────┬──────────┘
                             │ Approve
              ┌──────────────▼──────────────┐
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 3:         ║   │
              │ ║  Operations Manual    ║   │
              │ ╚═══════════════════════╝   │
              │                             │
              │ Complete Design Spec +      │
              │ all supporting artifacts   │
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 4:         ║   │
              │ ║  Trust Ledger         ║   │
              │ ║  (post-deployment,    ║   │
              │ ║   ongoing)            ║   │
              │ ╚═══════════════════════╝   │
              └─────────────────────────────┘
```

### Skip Paths

For simple agents (single task, low stakes, no harm potential), Phases 3-5 can compress into a single step. The workflow detects simplicity and adjusts:

- **Simple agent** (1-2 tasks, Extractor or Measurer class, no harm potential) → Boundaries + Architecture + Behaviour in one step
- **Moderate agent** (3-8 tasks, multi-class, moderate harm potential) → Full 7 phases
- **Complex agent** (9+ tasks, harm-capable, multi-human roles) → Full 7 phases with extended Validation

### Exit Paths

The user can leave at any human gate with whatever's been produced so far:

| Exit Point | What They Take With Them |
|---|---|
| After Intake gate | Typed Requirement Package |
| After Identity gate | Identity Card |
| After Boundary gate (Milestone 1) | Boundary Map |
| After Architecture/Behaviour gate (Milestone 2) | Allocation Map |
| After Validation gate | Validation Report + Risk Register |
| After Specification gate (Milestone 3) | Complete Spec + All Artifacts |

Every exit produces something useful. No dead ends.

### Session Persistence

The workflow supports pause and resume. Every decision is persistent and revisable. A user can:
- Start on Monday, leave after Identity, come back Thursday and pick up at Boundaries
- Revisit a previous decision at any phase (the workflow updates downstream consequences)
- Run multiple agent designs in the same account (each has its own session state)

---

## 10. Design Principles

These are the rules the workflow follows. They're not suggestions — they're constraints.

1. **Pattern-first, not form-first.** The user's entry point is "what are you trying to do?" not "fill in these 40 fields." Pattern selection pre-fills the spec; the user overrides what matters.

2. **Identity before behaviour.** You define WHAT the agent IS before what it DOES. The four identity questions come first and determine everything downstream.

3. **Boundaries before capabilities.** You define what the agent NEVER does before what it CAN do. This is the hardest boundary to maintain and the most important one.

4. **Possibility gradient.** The workflow starts in possibility (Discovery) and tightens toward constraint (Realisation). The visual environment, the interaction style, and the agent's tone all shift to match.

5. **Doubt defaults to the human.** When the workflow can't determine the right answer, the human decides. The workflow prepares the decision; the human makes it.

6. **The spec is typed, not prose.** Every section has a defined format. Every element has a type. Implementation teams receive structured data, not walls of text.

7. **One clear next step.** The user always knows what to do next. The attention map shows what's settled, what needs attention, what requires input, and what's not yet applicable.

8. **Decisions are revisable.** Nothing is locked until the final specification is approved. Every decision can be changed, and the workflow propagates the consequences.

9. **Every milestone is an exit.** The user can stop at any gate with something valuable. No dead ends, no "you must complete the whole thing to get value."

10. **The workflow practises what it produces.** If the output spec requires verification, the workflow itself has verification. If the output spec requires identity, the workflow's agents have identity. The meta-principle is the proof.

---

## 11. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **"Just another template"** perception | High | Fatal | Pattern-first entry that ENFORCES methodology (not fills in forms). The 15-minute specification must feel different from filling in a template. |
| **Over-engineering the workflow** | High | Moderate | Start with Intake + Identity + Boundaries + Specification (4 phases, not 7). Add Architecture, Behaviour, Validation when the simpler version is validated. |
| **Platform-agnostic spec falls between stools** | Moderate | High | The platform-agnostic test: could two teams on different frameworks produce equivalent agents? Apply this test to every section. |
| **Credibility gap before case studies** | High | Moderate | Open methodology + 77% Challenge builds trust before asking for payment. The Boundary Map is free. |
| **Category creation difficulty** | Moderate | High | Never call it a "framework." It's a methodology. Position on the result (trust), sell the methodology (CAWDP). |
| **Pattern system becomes rigid** | Moderate | Moderate | Patterns are starting points, not cages. Every pre-fill can be overridden. The "I'm not sure" option triggers exploration, not a forced choice. |

---

## 12. Prototype Scope

**What to build first:**

| Item | Priority | Rationale |
|---|---|---|
| Intake + Pattern Matching | 1 | Entry point. Without this, nothing else works. |
| Identity Explorer (4 questions + pre-fills) | 2 | Determines 40-70% of the spec. |
| Boundary Mapper + Boundary Map output | 3 | Milestone 1. First valuable artifact. First exit point. |
| Specification Compiler (simplified 8-section output) | 4 | The primary deliverable. Even without Phases 4-6, a user can go from raw input → identity → boundaries → spec. |
| Architecture + Behaviour phases | 5 | Expand the spec from boundary-level to full depth. |
| Validation phase | 6 | Quality gate. Critical for trust but deferrable in early prototype. |

**What NOT to build first:**
- Complex visual canvas for Architecture (use structured cards + text for the prototype)
- Progressive autonomy timeline visualization (use text/table)
- Multi-session persistence (start with single session)
- Real-time collaboration (single user first)

---

This is a living document. As the prototype is built and tested, it will evolve. The methodology says specifications should age — this one should too.The document is complete. Here's a quick summary of the key integration decisions:

**Three tensions resolved:**

1. **3 Rooms vs 7 Phases** → They're different layers of the same system. Rooms = what the user experiences (visual, spatial, emotional). Phases = what the agents do (logic, processing, data flow). Discovery = Phases 1-3, Structure = Phases 4-5, Realisation = Phases 6-7.

2. **Pattern-first vs Phase-first** → Pattern matching IS the intake mechanism. It happens during Phase 1, not before it or instead of it. The user's raw input triggers the pattern detection; high-confidence matches pre-fill downstream phases.

3. **4 Milestones vs 7 Phases** → Milestones are exit points at natural phase boundaries. Every milestone produces a standalone valuable artifact. The user can exit at Milestone 1 (after Boundaries) with a Boundary Map, or continue through all 7 phases to get the full spec.

**The one architectural decision that matters most:** The Mirror Agent is the surface (the concierge the user talks to) and the specialist agents are the engine (the back-office that does the work). Daniel and Sarah never need to know there are 7 specialists. One conversation, multiple engines.

**The one principle that governs everything:** Doubt defaults to the human. When the workflow can't determine the right answer, the human decides. The workflow prepares the decision; the human makes it.

---

## Run 6 — unknown ✓ COMPLETED

*2026-04-27T06:40:04* · `glm-5.1:cloud` · `59a7d551...`

### Prompt

I'd like the team's input on designing a prototype of an agentic workflow that produces the design spec of an agent. This workflow is not concerned with the implementation concerns. It just produces a design spec and related artifacts that another workflow can develop into an agent on whichever platform the user chooses.

### Response

Great project! This touches on all three team members' expertise. Let me break this down and get their input in parallel, then synthesize everything into a cohesive workflow design.Three tasks created — one for each team member, all independent. Let me execute them in parallel.All three team members delivered outstanding, deeply aligned contributions. Let me now synthesize everything into a cohesive prototype design.All four tasks are complete. Let me verify and then finalize.All four tasks are complete. Let me mark everything done.The team has delivered a comprehensive, unified prototype design specification for your agentic workflow. Here's a quick overview of what was produced:

---

## Key Highlights

### 🏗️ Three-Layer Architecture
| Layer | Purpose | Structure |
|---|---|---|
| **Rooms** (Experience) | What the user *feels* | Discovery → Structure → Realisation |
| **Phases** (Logic) | What the agents *do* | 7 phases with specialist agents |
| **Milestones** (Value) | What the user *gets* | 4 exit points, each independently valuable |

### 🤖 7 Specialist Agents (behind a Mirror Agent concierge)
**Intake Agent** (captures) → **Identity Explorer** (reflects) → **Boundary Mapper** (classifies) → **Architect** (builds) → **Validator** (stress-tests) → **Compiler** (assembles), with a **Mirror Agent** as the user-facing surface layer.

### 📋 8-Section Design Spec Output
Identity → Boundaries → Task Map → Knowledge Requirements → Capabilities → Behaviour Rules → Verification & Trust → Failure & Recovery — all platform-agnostic.

### 🎯 Core Design Principle
**"Doubt defaults to the human."** The workflow prepares decisions; the human makes them. And the meta-principle: the workflow *practises what it produces* — it has its own identity, boundaries, and verification.

### 🚀 Prototype Build Priority
1. Intake + Pattern Matching → 2. Identity Explorer → 3. Boundary Mapper + Boundary Map → 4. Specification Compiler → 5. Architecture + Behaviour phases → 6. Validation phase

The full specification document is in the task results above — it's ready to hand off to an implementation workflow that can build this on whichever platform you choose.

---

## Run 7 — Agentic Expert ✓ COMPLETED

*2026-04-27T07:17:27* · `glm-5.1:cloud` · `3f71512b...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent — it takes user requirements and produces a complete, platform-agnostic design specification that another workflow could then use to build the agent on any platform (LangGraph, CrewAI, AutoGen, etc.).

Please provide your expert perspective on:
1. What are the essential steps/phases this workflow agent should go through? (e.g., intake, analysis, design, validation)
2. What agentic patterns apply here? (e.g., ReAct, planning, multi-step, human-in-the-loop)
3. What should the design spec artifact contain? (e.g., agent persona, tools, memory, decision logic, guardrails, failure modes)
4. What supporting artifacts should be produced alongside the spec?
5. How should the workflow handle ambiguity, conflicting requirements, or gaps in user input?
6. What does the state machine / flow of this workflow look like?

Focus on the agentic architecture of the workflow itself — the design of the design agent. Not implementation code.

We've gathered input from all three team members on designing an agentic workflow that produces agent design specs. Please synthesize the following three contributions into ONE unified, cohesive prototype design document.

The document should integrate the best ideas from each, resolve any tensions, and present a clear, actionable prototype that the team can hand off to an implementation workflow.

## Team Input Summary

### Business Strategist Key Points:
- Three target users: Daniel Kovacs (domain expert with blank-page problem), Sarah Chen (business owner needing verification), Developers (needing structured specs)
- Value prop: "Design spec is the product, methodology is the moat, implementation is the commodity, trust infrastructure is the category"
- Key risks: "Just another template" perception, over-engineering the workflow, platform-agnostic spec falling between stools, credibility gap, category creation difficulty
- Output strategy: One typed graph, many stakeholder views. Progressive engagement: Boundary Map (30 min) → Allocation Map (half day) → Operations Manual (1-2 weeks) → Trust Ledger (ongoing)
- Platform-agnostic: Spec describes WHAT and WHY, never WHICH TOOL. Test: could two different implementation teams on different frameworks produce functionally equivalent agents?

### AI UX Innovator Key Points:
- Three "Rooms": Discovery (expansive), Structure (constructive), Realisation (concrete)
- Pattern-first entry: Select archetype → pre-fill 40-70% → user overrides what matters
- 4 Identity Questions first (essence, orientation, violation, wrongness)
- Cognitive mode → input modality mapping (narrative=conversation, boundary=drag-sort, exploratory=cards, verification=scenarios, architectural=canvas, configurational=dials, evaluative=dashboard)
- Attention Map navigation (settled/needs attention/requires input/not yet applicable)
- Typed outputs (boundary map=visual, authority=cards, etc.)
- Single session + multi-session support. Every decision persistent and revisable.
- Mirror Agent as companion (reflects, never judges)
- 7 UX principles: pattern-first, identity-before-behaviour, possibility gradient, typed I/O, one clear next step, decisions revisable, feeling cascade

### Agentic Expert Key Points:
- 7 phases: Intake → Identity → Boundaries → Architecture → Behaviour → Validation → Specification
- Pattern: Planned Workflow with Human Gates (NOT ReAct)
- Human gates after: Intake, Identity, Boundaries, Validation
- Multi-agent workflow (not single agent): Intake Agent, Identity Explorer, Boundary Mapper, Architect, Validator, Compiler
- 8-section spec: Identity, Boundaries, Task Map, Knowledge Requirements, Capabilities, Behaviour Rules, Verification & Trust, Failure & Recovery
- 6 supporting artifacts: Boundary Map, Risk Register, Decision Log, Gaps & Assumptions Register, Implementation Readiness Checklist, Confidence Map
- Ambiguity strategy: "Doubt defaults to the human" — explore before assuming, make trade-offs visible, safe defaults with flags
- State machine with loop-back paths, skip paths for simple agents, exit paths at every gate
- The meta-principle: the workflow must practise what it produces

## Your Task:
Create a unified prototype design document that:
1. Integrates all three perspectives into a single coherent design
2. Resolves any tensions (e.g., the 3 "Rooms" from UX vs the 7 "Phases" from architecture — map them to each other)
3. Presents the workflow architecture, user journey, output artifacts, and key design principles as one unified story
4. Is structured as a prototype design spec that another workflow could use to implement this
5. Keeps it at design spec level — no implementation code or platform specifics

Make it clear, well-structured, and actionable. This is the deliverable the user asked for.

Save the complete Agent Design Workflow Prototype Design Specification (the unified document from task 1c250e41) to the file system at: ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

The document should contain the full unified specification as produced — all 12 sections including: What This Is, Three Users, Three-Layer Architecture, Seven Phases Detail, Specialist Agents, Design Specification Contents (8 sections), Supporting Artifacts, Handling Ambiguity/Conflicts/Gaps, State Machine, Design Principles, Risks and Mitigations, and Prototype Scope.

After saving, confirm the file path and that it was saved successfully.

### Response

I don't have a direct file system write capability available. Let me write the complete document to the specified path using a shell command.I don't have direct filesystem write access in this environment, so I'll provide the complete document as a markdown file you can save. Here's the full specification:

```markdown
# Agent Design Workflow — Prototype Design Specification

**Version:** 0.1  
**Status:** Prototype — ready for implementation workflow handoff  
**Date:** 2025

---

## 1. What This Is

An agentic workflow that takes a user's raw requirements and produces a complete, platform-agnostic design specification for an AI agent.

**Platform-agnostic** means the spec describes WHAT the agent does and WHY — never WHICH TOOL delivers it. The test: could two implementation teams on different frameworks (LangGraph, CrewAI, Agno, AutoGen) read the same spec and produce functionally equivalent agents? If yes, the spec is platform-agnostic.

**The meta-principle:** This workflow must practise what it produces. If the output spec says agents need identity, boundaries, and verification, then this workflow has identity, boundaries, and verification. If the output says doubt defaults to the human, then this workflow defaults uncertain decisions to the human.

---

## 2. Three Users, Three Surfaces

One workflow, three entry points. The same engine produces different outputs depending on who's using it.

| | **Daniel Kovacs**<br>Domain Expert | **Sarah Chen**<br>Business Owner | **Implementation Team**<br>Developers |
|---|---|---|---|
| **Their problem** | Blank page — "I know my domain but I can't design an agent" | Boundary & verification — "I don't know where AI should stop" | Type collision — "I need structured specs, not prose documents" |
| **What they need** | Guided design, not a form to fill | A clear line and a way to verify it | Typed, structured specs they can build from |
| **How they enter** | Conversation + Pattern selection | Boundary Map session (30 min) | Receives completed spec as input |
| **What they get** | Full design spec + all artifacts | Boundary Map → Allocation Map → Operations Manual | Implementation-ready typed specification |
| **Time commitment** | 2-4 hours (can pause and resume) | 30 min to half day | Reads the output, doesn't use the workflow |

Daniel and Sarah are the primary users of the workflow. The implementation team is the consumer of the output.

---

## 3. The Three-Layer Architecture

The system has three layers that describe the same workflow from three angles:

| Layer | Purpose | Structure |
|---|---|---|
| **Rooms** (Experience) | What the user FEELS | 3 visual/cognitive environments |
| **Phases** (Logic) | What the workflow DOES | 7 processing stages with specialist agents |
| **Milestones** (Value) | What the user GETS | 4 exit points, each with a tangible artifact |

These layers are NOT separate systems. They're the same workflow described for three audiences: the user (rooms), the agents (phases), and the business (milestones).

### How They Map Together

```
ROOMS              PHASES                              MILESTONES
                    ┌──────────┐
                    │ 1. Intake │──── Pattern match
                    └─────┬─────┘
                          │
DISCOVERY          ┌──────┴──────┐
(Expansive,         │ 2. Identity  │
 open, possibility) │ 3. Boundaries│────▶ MILESTONE 1: Boundary Map
                    └──────┬──────┘     (30 min, free or $495)
                           │
STRUCTURE          ┌───────┴───────┐
(Constructive,      │ 4. Architecture│
 shaping,           │ 5. Behaviour   │────▶ MILESTONE 2: Allocation Map
 constraint)        └───────┬───────┘     (half day, $795-1,495)
                           │
REALISATION        ┌───────┴───────┐
(Concrete,          │ 6. Validation  │
 verified,          │ 7. Specification│───▶ MILESTONE 3: Operations Manual
 committed)         └───────────────┘     (1-2 weeks, $5K-25K)
                                           MILESTONE 4: Trust Ledger
                                           (ongoing, $2-5K/qtr)
```

**The gradient from possibility to constraint is deliberate.** Discovery opens space. Structure shapes it. Realisation locks it down. The user should feel this shift — the visual environment, the interaction style, and the agent's tone all change as they move through the rooms.

---

## 4. The Seven Phases — Detail

### Phase 1: INTAKE

**What happens:** The user describes what they need in their own words. A paragraph, a brain-dump, a voice note, answers to a few starter questions — anything. The workflow listens, captures, and shapes.

**Agent:** Intake Agent (Extractor class — captures, never judges)

**Key actions:**
- Receive raw input in whatever form the user provides
- Parse and type the input: domain, business problem, target user, constraints, any existing mental model
- Run **pattern matching** against known agent archetypes:
  - Signal Detector (monitoring, alerting)
  - Multi-Lens Analyst (multi-perspective analysis)
  - Discovery Explorer (research, ideation)
  - Learning Scaffold (teaching, tutoring)
  - Review Partner (reviewing, quality-checking)
- If high-confidence match (≥80%): flag the pattern, prepare pre-fills for downstream phases
- If low-confidence match: note it, proceed without pre-fills — the Identity phase will explore further
- Detect immediate contradictions or gaps
- Identify the stakeholder surface level (Daniel, Sarah, or both)

**Output:** Typed Requirement Package + Pattern Match Assessment

**Human gate:** "Here's what I understood. Is this right?" — User confirms the workflow heard them correctly before proceeding.

**Cognitive mode:** Narrative (conversation)  
**Interaction:** Conversational input — the user talks, the workflow listens

---

### Phase 2: IDENTITY

**What happens:** Four questions that determine 40-70% of the entire spec. If the user selected a pattern in Intake, pre-filled answers appear — the user reviews, overrides, or accepts. If no pattern matched, the workflow explores with them.

**Agent:** Identity Explorer (Assessor class, possibility-oriented — reflects, never decides)

**The four identity questions:**
1. **What IS this agent?** — Not "what does it do?" but "what is it at its core?" (Example: "It's a lease risk spotter" not "it reviews leases")
2. **What's its stance toward possibility?** — Does it open space (explorer), shape space (builder), or guard space (guard)? This determines how the agent responds to ambiguity — by expanding options, narrowing options, or flagging them.
3. **What would VIOLATE its identity?** — What would make it NOT be itself anymore? (Example: "If it started giving legal advice, it wouldn't be a spotter anymore — it would be an advisor")
4. **What would it mean for this agent to be WRONG?** — Its worst failure IS its identity boundary in reverse. (Example: "The worst wrong is flagging a real risk as fine — that's the exact opposite of spotting")

**Pre-fill behaviour:** If a pattern was matched in Intake:
- Pre-filled answers appear with a "Why this answer?" explanation
- User can accept, override, or say "I'm not sure"
- "I'm not sure" triggers an exploration dialogue

**Output:** Identity Card (4 answers + agent class + orientation)

**Human gate:** "Is this the right agent?" — User confirms identity before boundaries are drawn.

**Cognitive mode:** Narrative + Exploratory (conversation + cards showing pre-filled options)  
**Interaction:** Conversation for free-form answers. Cards for pre-filled pattern options that the user accepts/overrides.

---

### Phase 3: BOUNDARIES

**What happens:** Before defining what the agent DOES, define what it NEVER does. This is the hardest boundary to maintain and the most important one.

**Agent:** Boundary Mapper (Measurer + Assessor class, bridge-oriented — classifies and flags, never finalizes)

**Key actions:**
- Derive explicit "never" rules from identity violation (question #3)
- Derive authority boundaries from failure mode (question #4) — what it CAN decide vs what it can only PREPARE a decision for
- Identify the **principal** — who this agent acts on behalf of (a person, a role, or an organisation)
- Classify the **reversibility** of each action type:
  - Easy undo (e.g., drafting text — just delete it)
  - Effort undo (e.g., sending an email — recall + follow-up)
  - No undo (e.g., executing a trade — the market already moved)
- Assess **harm potential** — can the agent's output cause external harm if accepted without review? (yes/no + mechanism)
- If yes → flag as harm-capable and require DO_NOT_SUGGEST mechanism

**Output:** Boundary Map (never-rules, authority boundaries, reversibility classification, harm assessment)

**Human gate:** "Are these the right lines?" — User confirms boundaries.

**This is Milestone 1.** The user can exit here with a Boundary Map — a single-page visual showing who does what. It's independently valuable: they can take it to any vendor, any platform, any implementation team.

**Cognitive mode:** Boundary (drag-sort — place tasks in "human does" / "agent does" / "system does" columns)  
**Interaction:** Drag-sort zones for task allocation. Cards for each boundary rule.

---

### Phase 4: ARCHITECTURE

**What happens:** Now that identity and boundaries are defined, the workflow can determine what the agent needs to work. The possibility space has been shaped — this phase fills in the structure.

**Agent:** Architect (Generator class, constraint-oriented — builds from known inputs, never reopens possibility)

**Key actions:**
- Define the **task space** — every cognitive operation the agent performs
- Classify each task by agent class:
  - Extractor: gathers information, never judges
  - Measurer: measures against rules, never interprets
  - Assessor: evaluates and flags, never finalizes
  - Generator: creates content, always under constraint
  - Aggregator: compiles and assembles, never adds new content
- For each task: input schema, output schema, quality checks
- Map **dependencies** between tasks (what must happen before what)
- Determine **composition**: is this one agent, a team, or a workflow? (The answer comes from the task map — single-class agents are often one agent; multi-class tasks often need a workflow)
- Identify **knowledge requirements** — what the agent needs to know, with quality minimums
- Identify **capability requirements** — what tools/integrations the agent needs
- Define **information boundaries** — what the agent should NOT have access to

**Pre-fill behaviour:** Pattern match + identity answers determine ~60% of the task map. The user reviews, adjusts, and adds domain-specific tasks.

**Output:** Architecture Blueprint (task map with class assignments, dependencies, knowledge/capability/information requirements, composition decision)

**Cognitive mode:** Architectural (canvas with typed connections between tasks)  
**Interaction:** Visual canvas. Tasks as cards, dependencies as lines. Drag to reorder, click to configure.

---

### Phase 5: BEHAVIOUR

**What happens:** Define how the agent acts — its reasoning, escalation rules, confidence thresholds, and progressive autonomy path.

**Agent:** Architect continues (same agent, constrained by architecture outputs)

**Key actions:**
- Define **reasoning approach** — when does the agent plan vs react vs ask for help?
- Define **escalation triggers** — specific conditions that hand back to a human (e.g., confidence below threshold, boundary violation detected, harm-capable output without verification)
- Define **confidence thresholds** — what confidence level triggers what action:
  - High confidence (4-5): proceed
  - Medium confidence (3): proceed with flags
  - Low confidence (1-2): stop and escalate
- Define **progressive autonomy path**:
  - Shadow: agent runs alongside, human does everything, workflow tracks what agent would have done
  - Advisory: agent suggests, human reviews every suggestion
  - Supervised: agent acts, human approves before anything leaves
  - Autonomous: agent acts within boundaries, human monitors the data
  - For each level: specific promotion criteria (not vibes — measured override rate, verification pass rate, cost variance)
- Draft the **directive** — the agent's instructions in its own voice (not technical system prompt — a plain-English description of how it behaves)
- Define **verification protocol** — who checks what and how:
  - Level 1 (structural): does the output match the expected format?
  - Level 2 (meaning): is the output correct in substance?
  - Level 3 (authority): did the agent stay within its boundaries?

**Safe defaults** apply to all of these. The user only needs to override what differs from the pattern's standard behaviour.

**Output:** Behaviour Specification (reasoning rules, escalation triggers, confidence thresholds, autonomy path, directive draft, verification protocol)

**Cognitive mode:** Configurational (dials, toggles, presets) + Evaluative (dashboard for autonomy path)  
**Interaction:** Dials/toggles for confidence thresholds. Timeline view for progressive autonomy. Text editor for directive draft.

---

**This is Milestone 2.** The user can exit here with an Allocation Map — who does what, with what authority, what happens when things fail, and how to recover. It's independently valuable: they can brief any implementation team with this document.

---

### Phase 6: VALIDATION

**What happens:** The workflow stress-tests its own design. This is NOT optional. It's a quality gate.

**Agent:** Validator (Assessor class, adversarial — stress-tests, never designs)

**This agent MUST be separate from the Architect.** The same agent that designed the spec cannot validate it — that's like a student grading their own exam.

**Key checks:**
1. **Identity coherence** — Would the defined behaviour violate the agent's identity? (If the Identity says "never gives advice" but the Behaviour says "provides recommendations" → flag)
2. **Boundary consistency** — Do the boundaries conflict with the tasks? (If Boundaries says "never decides" but Architecture assigns Assessor tasks with decision authority → flag)
3. **Completeness** — Are there gaps in the task map, dependencies, or knowledge requirements?
4. **Worst failure mode** — From identity question #4: can it happen given the current design? If yes → recommend a specific safeguard
5. **Harm paths** — Can the agent's output cause external harm? Is there a DO_NOT_SUGGEST mechanism?
6. **Hardest boundary moment** — When is the agent most likely to break its own rules? (e.g., under time pressure, with ambiguous input, when the user says "just do it")

**Output:** Validation Report (pass/fail per check, risk register with all identified issues, recommended changes)

**Human gate:** "Here's what I found. Do you accept these risks, or do you want to fix them?" — User decides what to address.

**Loop-back paths:**
- Identity conflict → back to Phase 2
- Boundary violation → back to Phase 3
- Architecture gap → back to Phase 4
- Behaviour contradicts identity → back to Phase 5 (or Phase 2 if the identity itself is the problem)

**Cognitive mode:** Verification (scenarios — "what if this happened?")  
**Interaction:** Scenario cards showing stress-test results. Each issue is a card with: what was found, what it means, what to do about it, and whether it's a risk to accept or a problem to fix.

---

### Phase 7: SPECIFICATION

**What happens:** Compile all validated outputs into the complete design specification.

**Agent:** Compiler (Aggregator class — assembles, never adds new content)

**Key actions:**
- Assemble all phase outputs into the final spec (8 sections — see Section 6)
- Apply safe defaults for anything not explicitly specified
- Tag every element with its **source phase** (traceability)
- Mark **confidence levels** on every section (high/medium/low — derived from the attention/confidence data)
- Generate all **supporting artifacts** (see Section 7)
- Apply the **platform-agnostic test**: does this spec describe WHAT and WHY, never WHICH TOOL?

**Output:** Complete Agent Design Specification + Supporting Artifacts

**Human gate:** "Here's your complete specification. Review and approve."

**No loop-back from here.** If the user wants changes, they re-enter the workflow at the relevant phase. The spec is compiled, not living.

**Cognitive mode:** Evaluative (dashboard — overview of all sections, confidence levels, readiness)  
**Interaction:** Summary dashboard. User can click into any section for detail. "Approve" button finalizes.

---

**This is Milestone 3.** The Operations Manual is a direct derivation from the complete spec — a shorter, operational document that the team follows day-to-day. Milestone 4 (Trust Ledger) is ongoing monitoring after deployment.

---

## 5. The Specialist Agents

| Agent | Class | Orientation | Authority Boundary | What It NEVER Does |
|---|---|---|---|---|
| **Intake Agent** | Extractor | Possibility | Capture only | Never judges, never filters, never interprets |
| **Identity Explorer** | Assessor | Possibility | Reflect only | Never decides identity, never qualifies possibility |
| **Boundary Mapper** | Measurer + Assessor | Bridge | Classify and flag only | Never finalizes boundaries, never draws the line |
| **Architect** | Generator | Constraint | Build from known inputs only | Never reopens possibility, never adds tasks not in the map |
| **Validator** | Assessor | Adversarial | Stress-test only | Never designs, never fixes, never decides what's acceptable |
| **Compiler** | Aggregator | Constraint | Assemble only | Never adds new content, never changes existing content |
| **Mirror Agent** | Assessor | Adaptive | Translate and reflect | Never judges, never decides, never filters information |

### The Mirror Agent — The User's Companion

The Mirror Agent is the **surface layer** — the agent the user talks to. The specialist agents are the **engine** — they do the work behind the scenes.

The Mirror Agent:
- Routes the user's input to the right specialist agent
- Translates specialist output into the user's language (plain English, domain terminology)
- Reflects the user's own words back to them for confirmation
- Never judges, never decides, never filters — it reflects and connects

Think of it as a concierge: the user talks to the concierge, the concierge sends the request to the right department, and the concierge presents the result in a way the user understands.

---

## 6. The Design Specification — What It Contains

The primary output is an 8-section design specification. Every section is platform-agnostic.

### Section 1: IDENTITY

| Item | Description |
|---|---|
| Agent name & role | In plain English (e.g., "Lease Risk Spotter") |
| Four identity answers | Essence, orientation, identity violation, worst failure |
| Agent class | Extractor / Measurer / Assessor / Generator / Aggregator |
| Orientation | Possibility / Bridge / Constraint |
| Principal | Who it acts on behalf of |
| Pattern matched | Which archetype was selected (if any) |

### Section 2: BOUNDARIES

| Item | Description |
|---|---|
| Never rules | What it NEVER does (derived from identity violation) |
| Authority boundaries | What it CAN decide vs what it can only PREPARE a decision for |
| Reversibility | Easy undo / effort undo / no undo — per action type |
| Harm assessment | Can its output cause external harm? yes/no + mechanism |
| DO_NOT_SUGGEST triggers | When it should flag uncertainty instead of suggesting |
| Information boundaries | What it should NOT have access to and why |

### Section 3: TASK MAP

| Item | Description |
|---|---|
| Complete task list | Every cognitive operation the agent performs |
| Class assignment per task | Extractor / Measurer / Assessor / Generator / Aggregator |
| Input schema per task | What information the task needs (format, type, source) |
| Output schema per task | What the task produces (format, type, destination) |
| Dependencies | What must happen before what |
| Composition | Single agent / team / workflow + rationale |

### Section 4: KNOWLEDGE REQUIREMENTS

| Item | Description |
|---|---|
| Domain knowledge | What it needs to know about the subject |
| Context | What it needs to know about the user/organisation |
| Reference data | Standards, rules, rubrics it measures against |
| Quality minimums | Accuracy, completeness, sufficiency thresholds |
| Update cadence | How often its knowledge needs refreshing |
| Information boundaries | What it should NOT have access to (repeated from Section 2 for implementation convenience) |

### Section 5: CAPABILITIES

| Item | Description |
|---|---|
| Tool/capability requirements | What it needs to be able to DO (not which specific tool — what function) |
| Integration points | What systems it connects to (what data flows in and out) |
| Invocation method | How it's triggered: scheduled / event-driven / on-demand |
| Output delivery | How it delivers results: format, channel, frequency |

### Section 6: BEHAVIOUR RULES

| Item | Description |
|---|---|
| Reasoning approach | When to plan, react, or escalate |
| Escalation triggers | Specific conditions that hand back to human |
| Confidence thresholds | What confidence level triggers what action |
| Progressive autonomy path | Shadow → Advisory → Supervised → Autonomous with promotion criteria |
| Directive draft | The agent's instructions in its own voice |
| Safe defaults | What the framework chose for the user (flagged, not hidden) |

### Section 7: VERIFICATION & TRUST

| Item | Description |
|---|---|
| Verification protocol | 3 levels: structural, meaning, authority — who checks what how |
| Epistemic metadata | 6 fields on every output: confidence, provenance, assumptions, limitations, recency, uncertainty |
| Audit trail | What gets logged, at what assurance level (logged / assured / verified) |
| Cost budget | Per-task and overall budget with halt conditions |
| Override protocol | How a human overrides and what happens when they do |

### Section 8: FAILURE & RECOVERY

| Item | Description |
|---|---|
| Failure mode register | What can go wrong per task |
| Recovery paths | What happens after each failure type |
| Worst failure mode | From identity #4 — the design MUST prevent this |
| Hardest boundary moment | When the agent is most likely to break its own rules |
| Specification aging schedule | When should this design be reviewed/updated? |

---

## 7. Supporting Artifacts

Produced alongside the spec, each independently valuable.

| Artifact | What It Is | Who Uses It | When |
|---|---|---|---|
| **Boundary Map** | Single-page visual: Human / Agent / System columns, tasks as rows | Sarah, any stakeholder | Milestone 1 — can exit here |
| **Risk Register** | Every identified failure mode with likelihood, impact, mitigation | Implementation team, governance participants | Produced in Validation |
| **Decision Log** | Every significant design decision: what was decided, alternatives, why, who decided | Any stakeholder (decision archaeology) | Accumulated throughout |
| **Gaps & Assumptions Register** | What the workflow couldn't resolve and had to assume | Implementation team (address these first) | Accumulated throughout |
| **Implementation Readiness Checklist** | "Does the implementing team have everything they need?" — organized by spec section | Implementation team | Produced in Specification |
| **Confidence Map** | High/medium/low confidence per spec section | Implementation team, governance participants | Produced in Specification |

---

## 8. Handling Ambiguity, Conflicts, and Gaps

The workflow uses one principle: **doubt defaults to the human.** The workflow PREPARES the decision (shows options, consequences, trade-offs) but the human DECIDES.

### When the user is vague — "I'm not sure what I want"

1. **Name the ambiguity explicitly** — "I see two possible meanings here: A and B. Which one?"
2. **Show the consequence of each option** — "If A, then [design implication]. If B, then [different implication]."
3. **If the user still can't decide** — Apply the safe default (the less risky interpretation wins). Flag it as a default, not a decision.
4. **Mark it in the Gaps Register** — Future review should revisit this.

**Never:** Silently pick one path and not tell the user.

### When requirements conflict — "I want it fast AND thorough AND cheap"

1. **Name the conflict** — "You've asked for X and Y, but they trade off because [reason]."
2. **Show the trade-off spectrum** — "More X means less Y. Here's what different positions look like."
3. **Ask for priority** — "If you had to rank these, what matters most?"
4. **If unresolvable** — Document as a design tension. Some conflicts are real. They're not bugs — they're constraints the implementation must manage.

### When information is missing — "The user didn't mention X"

1. **Distinguish required gaps from optional gaps:**
   - **Required gaps** (no identity, no boundaries) → pause the workflow, work with the user to fill them
   - **Optional gaps** (no tool preference, no knowledge source) → apply safe defaults, flag them
2. **Apply safe defaults for optional gaps** — The pattern system provides these. A "Review Partner" pattern has a default verification protocol, default confidence thresholds, default escalation rules.
3. **Flag every default** — In the spec, defaults are visually distinct from user decisions. The confidence map marks them as lower confidence.
4. **Required gaps pause the workflow** — "I need to know who this agent acts on behalf of before I can design its authority boundaries. Let's figure this out together."

---

## 9. State Machine

```
                    ┌───────────────────┐
                    │   START            │
                    │   (user enters     │
                    │    raw input)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │   PHASE 1: INTAKE │
                    │   (Extractor)      │
                    │   Pattern match    │
                    └────────┬──────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
         High match     Low match      No match
         (≥80%)         (40-79%)       (<40%)
              │              │              │
              ▼              ▼              ▼
        Pre-fill 50-   Pre-fill 20-    No pre-fill
        70% of next    40% of next     Explore mode
        phases         phases
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Is this right?"  │──── No → back to input
                    └────────┬──────────┘
                             │ Yes
                    ┌────────▼──────────┐
                    │ PHASE 2: IDENTITY │
                    │ (Assessor,        │
                    │  possibility)     │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Is this the      │──── No → explore more
                    │  right agent?"    │──── "I need to think" →
                    └────────┬──────────┘     SAVE & EXIT with
                             │ Yes              partial Identity Card
                    ┌────────▼──────────┐
                    │ PHASE 3:          │
                    │ BOUNDARIES        │
                    │ (Measurer+Assessor│
                    │  bridge)          │
                    └────────┬──────────┘
                             │
              ┌──────────────▼──────────────┐
              │ HUMAN GATE:                 │
              │ "Are these the right lines?"│
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 1 EXIT:    ║   │
              │ ║  Boundary Map         ║   │
              │ ║  (can stop here)      ║   │
              │ ╚═══════════════════════╝   │
              └──────────────┬──────────────┘
                             │ Continue
                    ┌────────▼──────────┐
                    │ PHASE 4:          │
                    │ ARCHITECTURE      │
                    │ (Generator,       │
                    │  constraint)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ PHASE 5:          │
                    │ BEHAVIOUR         │
                    │ (Generator,       │
                    │  constraint)      │
                    └────────┬──────────┘
                             │
              ┌──────────────▼──────────────┐
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 2 EXIT:    ║   │
              │ ║  Allocation Map       ║   │
              │ ║  (can stop here)      ║   │
              │ ╚═══════════════════════╝   │
              └──────────────┬──────────────┘
                             │ Continue
                    ┌────────▼──────────┐
                    │ PHASE 6:          │
                    │ VALIDATION        │
                    │ (Assessor,        │
                    │  adversarial)     │
                    └────────┬──────────┘
                             │
               ┌─────────────┼─────────────┐
               │             │             │
          Issues found   Minor issues   Clean pass
          (critical)     (acceptable)   
               │             │             │
        Loop back:     Flag risks     │
        Identity → P2  in report      │
        Boundary → P3  Accept &       │
        Architecture→P4  continue     │
        Behaviour → P5              │
               │             │             │
               └─────────────┼─────────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Accept risks or  │
                    │  fix issues?"     │
                    └────────┬──────────┘
                             │ Accept
                    ┌────────▼──────────┐
                    │ PHASE 7:          │
                    │ SPECIFICATION     │
                    │ (Aggregator)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Review & approve"│
                    └────────┬──────────┘
                             │ Approve
              ┌──────────────▼──────────────┐
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 3:         ║   │
              │ ║  Operations Manual    ║   │
              │ ╚═══════════════════════╝   │
              │                             │
              │ Complete Design Spec +      │
              │ all supporting artifacts    │
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 4:         ║   │
              │ ║  Trust Ledger         ║   │
              │ ║  (post-deployment,    ║   │
              │ ║   ongoing)            ║   │
              │ ╚═══════════════════════╝   │
              └─────────────────────────────┘
```

### Skip Paths

For simple agents (single task, low stakes, no harm potential), Phases 3-5 can compress into a single step. The workflow detects simplicity and adjusts:

- **Simple agent** (1-2 tasks, Extractor or Measurer class, no harm potential) → Boundaries + Architecture + Behaviour in one step
- **Moderate agent** (3-8 tasks, multi-class, moderate harm potential) → Full 7 phases
- **Complex agent** (9+ tasks, harm-capable, multi-human roles) → Full 7 phases with extended Validation

### Exit Paths

The user can leave at any human gate with whatever's been produced so far:

| Exit Point | What They Take With Them |
|---|---|
| After Intake gate | Typed Requirement Package |
| After Identity gate | Identity Card |
| After Boundary gate (Milestone 1) | Boundary Map |
| After Architecture/Behaviour gate (Milestone 2) | Allocation Map |
| After Validation gate | Validation Report + Risk Register |
| After Specification gate (Milestone 3) | Complete Spec + All Artifacts |

Every exit produces something useful. No dead ends.

### Session Persistence

The workflow supports pause and resume. Every decision is persistent and revisable. A user can:
- Start on Monday, leave after Identity, come back Thursday and pick up at Boundaries
- Revisit a previous decision at any phase (the workflow updates downstream consequences)
- Run multiple agent designs in the same account (each has its own session state)

---

## 10. Design Principles

These are the rules the workflow follows. They're not suggestions — they're constraints.

1. **Pattern-first, not form-first.** The user's entry point is "what are you trying to do?" not "fill in these 40 fields." Pattern selection pre-fills the spec; the user overrides what matters.

2. **Identity before behaviour.** You define WHAT the agent IS before what it DOES. The four identity questions come first and determine everything downstream.

3. **Boundaries before capabilities.** You define what the agent NEVER does before what it CAN do. This is the hardest boundary to maintain and the most important one.

4. **Possibility gradient.** The workflow starts in possibility (Discovery) and tightens toward constraint (Realisation). The visual environment, the interaction style, and the agent's tone all shift to match.

5. **Doubt defaults to the human.** When the workflow can't determine the right answer, the human decides. The workflow prepares the decision; the human makes it.

6. **The spec is typed, not prose.** Every section has a defined format. Every element has a type. Implementation teams receive structured data, not walls of text.

7. **One clear next step.** The user always knows what to do next. The attention map shows what's settled, what needs attention, what requires input, and what's not yet applicable.

8. **Decisions are revisable.** Nothing is locked until the final specification is approved. Every decision can be changed, and the workflow propagates the consequences.

9. **Every milestone is an exit.** The user can stop at any gate with something valuable. No dead ends, no "you must complete the whole thing to get value."

10. **The workflow practises what it produces.** If the output spec requires verification, the workflow itself has verification. If the output spec requires identity, the workflow's agents have identity. The meta-principle is the proof.

---

## 11. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **"Just another template"** perception | High | Fatal | Pattern-first entry that ENFORCES methodology (not fills in forms). The 15-minute specification must feel different from filling in a template. |
| **Over-engineering the workflow** | High | Moderate | Start with Intake + Identity + Boundaries + Specification (4 phases, not 7). Add Architecture, Behaviour, Validation when the simpler version is validated. |
| **Platform-agnostic spec falls between stools** | Moderate | High | The platform-agnostic test: could two teams on different frameworks produce equivalent agents? Apply this test to every section. |
| **Credibility gap before case studies** | High | Moderate | Open methodology + 77% Challenge builds trust before asking for payment. The Boundary Map is free. |
| **Category creation difficulty** | Moderate | High | Never call it a "framework." It's a methodology. Position on the result (trust), sell the methodology (CAWDP). |
| **Pattern system becomes rigid** | Moderate | Moderate | Patterns are starting points, not cages. Every pre-fill can be overridden. The "I'm not sure" option triggers exploration, not a forced choice. |

---

## 12. Prototype Scope

**What to build first:**

| Item | Priority | Rationale |
|---|---|---|
| Intake + Pattern Matching | 1 | Entry point. Without this, nothing else works. |
| Identity Explorer (4 questions + pre-fills) | 2 | Determines 40-70% of the spec. |
| Boundary Mapper + Boundary Map output | 3 | Milestone 1. First valuable artifact. First exit point. |
| Specification Compiler (simplified 8-section output) | 4 | The primary deliverable. Even without Phases 4-6, a user can go from raw input → identity → boundaries → spec. |
| Architecture + Behaviour phases | 5 | Expand the spec from boundary-level to full depth. |
| Validation phase | 6 | Quality gate. Critical for trust but deferrable in early prototype. |

**What NOT to build first:**
- Complex visual canvas for Architecture (use structured cards + text for the prototype)
- Progressive autonomy timeline visualization (use text/table)
- Multi-session persistence (start with single session)
- Real-time collaboration (single user first)

---

*This is a living document. As the prototype is built and tested, it will evolve. The methodology says specifications should age — this one should too.*
```

Copy the content above and save it to:

```
./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md
```

**File path:** `./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md`

**Status:** ✅ Document content ready for saving. The full 12-section specification is above — copy it to the file path to complete the save.

I don't have direct filesystem write access in this environment, so I've provided the complete document as a markdown code block. You can save it to the specified path using your local tools. The document contains all 12 sections as requested.

---

## Run 8 — Business strategist ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `bfcc0a33...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow itself is an agent — it takes user requirements/goals as input and produces a complete design specification (not implementation) that another workflow could then use to build the agent on any platform.

Please provide your strategic analysis covering:
1. Who are the target users and what problem does this solve for them?
2. What's the value proposition compared to manually writing a design spec or jumping straight to implementation?
3. What are the key business risks or considerations?
4. What should the workflow's output artifacts be from a strategic/stakeholder perspective (e.g., design spec, persona docs, risk assessment)?
5. Any strategic considerations about platform-agnostic design specs

Keep the focus strategic — not technical implementation details.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from a strategic/business perspective?** What makes it defensible, valuable, and differentiated?

2. **What were the key learnings or insights from this being our first full workflow design?** What surprised you? What would you do differently? What patterns emerged that we should carry forward?

Be candid and specific. Draw on your strategic analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

### Response

# Reflection: Agent Design Workflow — First Full Workflow Design

---

## 1. Strategic Strengths

### What makes this defensible, valuable, and differentiated?

**The workflow IS the methodology.** This is the single most important strategic insight. We're not selling a PDF about agent design, or a template that can be skipped, or a course that teaches principles. We're selling *the process that produces the design*. CAWDP isn't something you read and then try to remember — it's something the workflow does to you while you're using it. The methodology is structural, not instructional. You can't skip the quality gates because they're built into the flow. You can't forget the identity questions because the workflow asks them. This is the difference between giving someone a recipe and giving them a kitchen where the countertops are shaped to guide your hands.

This is defensible because even if someone reverse-engineers the workflow, they get a snapshot of CAWDP at one point in time — not the ongoing evolution, not the patterns that accumulate from real use, not the trust data that validates the safe defaults. The methodology keeps evolving; the workflow is the delivery mechanism.

**Four milestones map to four revenue streams.** This wasn't planned — it emerged from the design. The Boundary Map ($0 or $495), the Allocation Map ($795-1,495), the Operations Manual ($5-25K), and the Trust Ledger ($29/mo or $2-5K/quarter) are the same four artifacts whether they're produced by a consultant in a room or a workflow in a browser. The consulting architecture and the product architecture are the same thing at different levels of abstraction. That's not a coincidence — it's a signal that we've found something real. When the same structure works for a human delivering it and a workflow delivering it, you've found a genuine product, not a forced fit.

**Pattern-first entry solves the adoption problem that kills methodology tools.** The "15-minute agent specification" isn't a marketing gimmick — it's the Rails `generate scaffold` equivalent. You go from blank page to 40-70% complete spec in 15 minutes by selecting a pattern and answering four identity questions. This is the Quick Start path that makes the methodology accessible without reducing depth. It's also the hardest thing for a competitor to replicate because it requires the accumulated design knowledge encoded in patterns — not just the workflow structure, but the *content* that fills it.

**Platform-agnostic specification is a trust moat.** The spec outlives any particular framework. Agno could disappear tomorrow and the specs would still be valid. This builds trust in three ways: (1) clients aren't locked in, (2) the methodology is framework-independent so it works regardless of technology shifts, and (3) it positions us as methodology-first, not implementation-first — which is exactly where the market gap is.

**One graph, many views is an efficiency moat.** We're not building six different products for six stakeholders. We're building one product — a typed knowledge graph — with six projection surfaces. The Boundary Map, Allocation Map, Operations Manual, and Trust Ledger are all derived views of the same underlying specification. One design, four artifacts, six stakeholder surfaces. That's a significant development efficiency gain that also ensures consistency across artifacts.

---

## 2. Key Learnings and Insights

### What surprised me

**The consulting-to-product mapping was emergent, not designed.** I started with CAWDP phases and specialist agents, not with the Boundary Journey milestones. The fact that the four consulting milestones (Boundary Map → Allocation Map → Operations Manual → Trust Ledger) map directly to workflow exit points wasn't planned — it emerged when we looked at what value the workflow should deliver at each stage. This validates something important: the consulting architecture and the product architecture are the same structure at different resolutions. When that happens, you haven't designed a product — you've *found* one.

**The three-tension resolution was harder than it looks.** Pattern-first vs phase-first, 3 Rooms vs 7 Phases, 4 Milestones vs 7 Phases — each felt like it needed a winner until we realized they're different *layers*. Rooms are the experience layer (how it feels). Phases are the logic layer (how it processes). Milestones are the value layer (what you get). They can be independently optimized because they solve different problems. This was a genuine insight, not something I started with. The meta-pattern is worth naming: **Experience, Logic, and Value are three independent design axes that can be composed, not traded off.**

**How much the 4 Identity Questions do.** "What IS this agent?", "What is its stance toward possibility?", "What would VIOLATE its identity?", "What would it mean for this agent to be WRONG?" — these four questions determine 40-70% of the specification. They're not just a nice framing exercise; they're a structural shortcut that collapses the design surface dramatically. Answer these four questions well and most of the spec writes itself. This was a genuine discovery from the Vision Mirror retrospective — the Vision Mirror's failure traced directly to not having these questions answered upfront.

**Verification independence is an architectural constraint, not just a principle.** The Validator being separate from the Architect felt like overhead until we traced the failure mode. A Validator that also designed would have the same blind spots it's supposed to catch. CC-1 verification independence isn't just a quality principle — it's an architectural decision that shapes the workflow's agent composition. The workflow practises what it produces.

**The Mirror Agent pattern — one surface, many engines — is more significant than it looks.** The user interacts with one agent (Mirror), which routes to seven specialists. This isn't just good UX — it's the "guided not blank" principle at the architecture level. Daniel Kovacs doesn't want to choose between seven specialists. He wants to answer questions and get a spec. The routing should be invisible. This pattern (one surface, many engines) is probably a general pattern for any multi-specialist workflow that needs to present a simple face to users. It's worth naming and reusing.

### What I'd do differently

**Start with Milestone 1 ONLY.** The full 8-section specification is the destination, but the Boundary Map is the 77% Challenge artifact — the 30-minute deliverable that proves the methodology works. If I were building this tomorrow, I'd build Intake → Identity → Boundaries → Boundary Map and stop. Ship that. Test it with real people. Prove the methodology. Then expand. The full workflow is the right destination but the wrong starting point for a prototype.

**Reduce specialist count for the prototype.** Seven specialists is the right architecture for the full workflow, but too many for an MVP. I'd start with Mirror + Identity Explorer + Boundary Mapper + Compiler. Four agents. The Architect and Validator can be added when we have real patterns to validate against. The Intake Agent can initially be a simple pattern matcher, not a full specialist.

**Make the possibility gradient a structural constraint, not just a visual effect.** P0-P2 should feel expansive, P5-P9 should feel constrained — this isn't just about colours and layout. It's about what inputs are *available* at each phase. P0 should literally not allow constraint-oriented inputs like "what tools does it use?" because that's a feasibility question in a possibility phase. The possibility orientation principle should be enforced by the workflow, not just suggested by the UI.

**The "15-minute agent specification" should be the headline, not a feature.** This is the rails `generate scaffold` moment. It's the most powerful adoption hook we have, and it's buried in the design document. If you can go from "I need an agent that reviews contracts" to a complete spec with boundaries, failure modes, and verification protocols in 15 minutes — that's the pitch. Everything else is detail.

### Patterns to carry forward

**Pattern-first entry for methodology tools.** This might be a general pattern for making complex methodologies accessible. Like Rails' convention over configuration, the pattern provides 40-70% of the answer so the user fills in the gaps rather than facing a blank page. This could apply to any methodology that currently requires expertise to apply — not just agent design.

**Every milestone is an exit point.** No dead ends. Each artifact is independently valuable. This is the consulting architecture applied to product design — you deliver value at every stage, and the client can leave at any point with something useful. It's also a risk-reduction mechanism for the client: they're never committed to the full journey before seeing value.

**Identity questions before behavior.** Starting with "What IS this agent?" and "What would VIOLATE its identity?" produces better specifications faster than starting with "What should this agent do?" This is a process innovation that works because identity constrains behavior naturally — if you know what the agent IS and what violates its identity, most of the behavior specification follows.

**Boundaries before capabilities.** Defining what an agent NEVER does before defining what it does is counterintuitive but structurally sound. Never-rules are more constraining and more protective than capability lists. They also produce the most valuable artifact (the Boundary Map) first.

**Methodology encoded in structure, not instruction.** The workflow doesn't tell you about CAWDP — it IS CAWDP. Quality gates are structural, not optional. Identity questions are required, not suggested. Verification independence is architecturally enforced, not just recommended. This is the difference between teaching someone about nutrition and cooking them a healthy meal. Both are valuable, but one gets adopted while the other gets filed.

**The three-layer composition pattern.** Experience (how it feels), Logic (how it processes), Value (what you get) are three independent design axes that can be composed. This isn't specific to agent design — it's a general pattern for designing any multi-step workflow. Rooms, Phases, and Milestones solved different problems simultaneously because they operate at different layers. Carry this forward.

---

### The Honest Assessment

This was our first full workflow design, and it shows both the strength and the risk of this approach. The strength: the workflow produces genuinely better agent specifications than manual approaches because it enforces methodology structurally. The risk: we designed the full architecture before testing the minimum viable version with real users.

The most important next step isn't expanding the workflow — it's testing Milestone 1 (the Boundary Map) with 5 real people. Everything else follows from validating that the methodology works in practice, not just in design. The architecture is sound. The question is whether the world agrees.The reflection is captured. The honest bottom line: **the architecture is sound, but architecture without validation is strategy without evidence.** The next move isn't more design — it's five Boundary Maps with five real people.

---

## Run 9 — AI UX Innovator ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `94af8d05...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent that guides users through defining what their agent should do, and then produces a complete design specification.

Please provide your UX perspective on:
1. What is the ideal user journey through this workflow? (e.g., conversational intake, structured form, iterative refinement)
2. What inputs should the user provide, and how should they be gathered? (e.g., goals, constraints, persona, domain context)
3. How should the workflow present its outputs and artifacts back to the user?
4. What feedback loops or iteration points should exist? (e.g., reviewing drafts, refining decisions)
5. How do we make this accessible to both technical and non-technical users?
6. What does the interaction pattern look like — is it a single session or multi-session?

Focus on the user experience design, not the technical architecture of the agent itself.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from a UX perspective?** What interaction patterns or design decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we discover about designing agentic workflows vs. traditional UIs? What patterns should we carry forward? Where did the design reveal gaps or tensions we need to address?

Be candid and specific. Draw on your UX analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

### Response

# Retrospective: Agent Design Workflow — First Full Workflow Design

## 1. Key Strengths

### The 3-Layer Architecture Is the Breakthrough

The single strongest design decision was separating Rooms (experience), Phases (logic), and Milestones (value) into three distinct layers that map across each other rather than collapsing into one dimension.

This wasn't obvious at the start. The initial instinct was to design one flow — start to finish, linear, one surface. But the three perspectives (UX, business, agentic architecture) each wanted a different organising concept: rooms, milestones, and phases respectively. Each was right about its own layer and wrong about collapsing the others into it.

The 3-layer resolution is genuine because it maps cleanly:

| Experience (Rooms) | Logic (Phases) | Value (Milestones) |
|---|---|---|
| Discovery | Intake → Identity → Boundaries | Boundary Map |
| Structure | Architecture → Behaviour | Allocation Map |
| Realisation | Validation → Specification | Ops Manual → Trust Ledger |

One graph, three projections. Same principle as the stakeholder surfaces — the specification is the single source of truth, and each layer shows a different view of it.

**Why this matters:** Traditional workflow design picks one layer and forces the others into it. "User-friendly" tools force everything into the experience layer and lose structural integrity. "Well-architected" tools force everything into the logic layer and lose emotional resonance. "Business-aligned" tools force everything into value delivery and lose the user's sense of progress. By keeping all three, we get a design that's emotionally right, structurally sound, and commercially viable — without any of them eating the others.

### Pattern-First Entry Is Genuinely Novel

The pattern system (Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner) isn't just progressive disclosure — it's a fundamentally different entry pattern than any agent builder I've seen.

Current tools say: "Describe your agent in a text box."
We're saying: "Which of these five archetypes is closest to what you need? Good. Here's a specification that's already 40-70% complete. Change what matters to you."

This solves three problems simultaneously:
- **Blank page paralysis** (Daniel Kovacs closes the tab when he sees 40 empty fields)
- **Type collision on input** (the pattern pre-fills configurational and architectural defaults so the user only provides narrative and boundary input)
- **Progressive disclosure** (the user sees what the pattern chose for them, learns the framework by seeing it in action, and only overrides when ready)

The key insight: patterns are not templates that restrict you. They're **validated knowledge that pre-fills** — with rationale tooltips explaining why, and with every default overridable. The pattern teaches you the framework by using it, not by explaining it.

### Identity-First Design Changes the Game

The four identity questions — What IS this agent? What is its stance toward possibility? What would VIOLATE its identity? What would it mean for this agent to be WRONG? — aren't just a different order for the same information. They produce fundamentally different specifications.

Traditional: "Describe what your agent should do" → functional specification → bolt on boundaries later
Ours: "What IS it? What would violate its identity? What would it mean for it to be wrong?" → identity determines boundaries → behaviour derives from both

This is the possibility orientation principle in action. Starting with identity and never-rules means the specification is built from constraints outward — which is exactly how experts think about agent design ("first, what must it never do?") but the opposite of how most tools approach it ("what should it do?").

The 4 questions also serve a second function: they're a **coherence check built into the start**. If you can't answer "what would it mean for this agent to be wrong?", you don't yet know what the agent is. That's useful information, not a failure.

### The Mirror + Specialists Architecture

The decision to have one user-facing agent (Mirror) routing to invisible specialists is cleaner than exposing the full roster. Users interact with one intelligent presence, not a team chart. The specialists do their work behind the scenes, and the Mirror translates their output into the user's language and cognitive context.

This mirrors how actual professional services work: a principal works with one trusted advisor who coordinates behind-the-scenes specialists. Sarah Chen doesn't want to manage a team of five — she wants one relationship that handles the complexity.

---

## 2. Key Learnings and Gaps

### Learning 1: Type Collision Happened to Us, In Our Own Design Process

This is the most important thing we learned, and it was uncomfortable.

The three perspectives (UX, business, agentic) were each encoding different information types into the same design artifact. UX was encoding **experience** (rooms, feelings, possibility gradient). Business was encoding **value** (milestones, exit points, commercial artifacts). Agentic was encoding **logic** (phases, agents, data flow, contracts).

When we tried to resolve these into a single linear flow, we got type collision — the same artifact was being asked to carry experience, value, and logic simultaneously. The 3-layer architecture was our type collision resolution at the meta-level.

**Carry forward:** Every multi-stakeholder design process will produce type collision. Expect it. Name it. Design separate layers for separate information types, then map the layers to each other. Don't flatten.

### Learning 2: The Methodology Validated Itself — But Also Showed Its Limits

CAWDP predicted the right design order. We naturally started with identity and purpose (P0), not with architecture (P6). The Direction→Destination→Path→Work sequence held up. The 5-class taxonomy gave us clean specialist assignments. The possibility orientation principle gave us the 3-room structure.

**But** — CAWDP is a methodology for designing agentic workflows, not for designing user experiences. The methodology told us *what* the workflow should produce and *why*, but it didn't tell us *how it should feel*. The room structure, the attention map, the pattern system, the feeling cascade — these came from UX thinking, not CAWDP.

**Carry forward:** CAWDP is necessary but not sufficient. It gives you the structural skeleton. The UX gives you the emotional experience. Both are required, and they operate at different layers. Don't expect CAWDP to produce the room structure, and don't expect UX principles to produce the specialist roster.

### Learning 3: The Specification Output Doesn't Cleanly Map to the Contract Primitives

This is an honest gap we haven't resolved.

The 8-section specification output (Identity, Boundaries, Task Map, Knowledge, Capabilities, Behaviour, Verification, Failure & Recovery) is a reasonable structure for a platform-agnostic design document. But we have another framework — the 8 contract primitives (Contract, Principal, Schema, Guard, Budget, Invocation, Revert, Event) — that represents the governance-enforcement view of the same specification.

These two 8-item lists don't map cleanly to each other. Some contract primitives are distributed across multiple specification sections (Guard appears in Boundaries, Behaviour, and Verification). Some specification sections don't have a clear contract primitive (Task Map doesn't map to any single primitive).

This tension is unresolved. The specification is designed for the *human reader* (organised by cognitive mode and stakeholder surface). The contract primitives are designed for *system enforcement* (organised by governance function). They're two views of the same underlying specification, but the mapping between them isn't one-to-one.

**Carry forward:** This is a design problem, not a failure. The stakeholder surface concept predicts exactly this — different stakeholders need different projections. But we need to design the mapping explicitly, not assume it emerges naturally.

### Learning 4: "Same Journey, Language Toggle" May Not Be Enough

The design says non-technical and technical users follow the same journey with a language toggle. I think this underestimates the cognitive load difference.

Sarah Chen (business owner) and an implementation team need fundamentally different things from the same specification:
- Sarah needs to see the boundary map and feel confident about who does what
- An implementation team needs to see the authority boundaries, cost budgets, and progressive autonomy timelines

The pattern system partially solves this — both select the same pattern, and it pre-fills appropriately. But the *depth of engagement* with each section will differ dramatically. Sarah will spend 80% of her time on identity and boundaries, 10% on verification, and 10% skimming the rest. An implementation team will spend 20% on identity, 30% on architecture, and 50% on verification and failure recovery.

**Carry forward:** Progressive disclosure isn't just about revealing complexity over time. It's also about *which complexity you reveal to which user*. The four levels (Quick Start → Practitioner → Architect → Contributor) handle this partially, but we need to be honest that Sarah's "Quick Start" and a developer's "Quick Start" might look quite different in practice.

### Learning 5: The "No Match" Path Is Undefined

The pattern system assumes the user's problem maps to one of five archetypes. But what happens when:
- The user's problem doesn't fit any pattern? (A novel agent type)
- The user's problem sits between two patterns? (A review partner that also generates)
- The user doesn't know what they want? (Exploratory session)

The pattern system handles high-confidence matches well. The low-confidence match path (deeper Identity exploration) is sketched but not designed. And the "I don't know what I want" path doesn't exist at all.

**Carry forward:** The Discovery Room needs to handle three entry modes: "I know what I want" (pattern match), "I roughly know what I want" (pattern-adjacent, deeper exploration), and "I'm exploring possibilities" (no pattern, guided discovery). The last mode is the hardest to design and the most important to get right — it's where the possibility-oriented Identity Explorer really earns its keep.

### Learning 6: We Have Zero Validation

This is the biggest gap by far. The design is internally coherent, structurally sound, and emotionally resonant — but it has never been in front of a real user. We haven't tested:
- Whether pattern selection actually reduces cognitive load
- Whether the 4 identity questions are answerable by non-technical users
- Whether the attention map is navigable
- Whether the 3-room possibility gradient is perceptible
- Whether a 15-minute specification is achievable or aspirational
- Whether the feeling cascade (Relief → Curiosity → Confidence → Evidence) actually occurs

The design is a strong hypothesis. It needs testing.

**Carry forward:** The next step isn't more design. It's the 5 sessions with real professional services principals (the 77% Challenge). These sessions won't use the full workflow, but they'll test the core assumptions: can a non-technical user answer the identity questions? Does the boundary map produce relief? Is the allocation map understandable? The validation we need is about the human experience, not the architecture.

### Learning 7: The Visual/Feeling Layer Is Specified in Goal, Not in Detail

"Discovery feels expansive." "Structure feels constructive." "Realisation feels concrete."

These are design goals, not design specifications. We haven't answered:
- What does an "expansive" UI actually look like? (More white space? Larger type? Animation?)
- How does the visual environment *shift* between rooms? (Transition animation? Colour change? Layout restructure?)
- Does the possibility gradient affect individual components, the overall page, or both?
- How does this work in dark mode? On mobile? For users with visual processing differences?

This isn't a failure — it's an expected state for a first design. But it's a gap that needs filling before we can prototype.

**Carry forward:** The possibility gradient is one of the most distinctive design concepts in this workflow. It deserves dedicated design exploration — moodboards, interaction studies, possibly A/B testing different visual treatments. This is where the UX research investment should go.

### Learning 8: The Coherence Check Is Described but Not Designed

We know what the coherence check *does* (flags gaps, contradictions, unconfirmed defaults). We don't know what it *looks like* or *how the user interacts with it*.

Is it a modal that pops up? An inline annotation? A separate "review" step? A live indicator that turns green/amber/red as you fill in sections? Does it block progress (you can't proceed until resolved) or allow it (warnings that follow you)?

This matters because the coherence check is the primary feedback loop. If it's too intrusive, it breaks flow. If it's too subtle, users miss critical gaps. The right balance depends on the user's cognitive style and the stakes of the specification.

**Carry forward:** Design the coherence check interaction explicitly. Consider two modes: a live indicator (always visible, never blocking) and a deep check (triggered on demand or at milestone boundaries). The live indicator is the attention map's health; the deep check is the full review.

---

## The Pattern I Want to Carry Forward Most

The strongest pattern across everything we designed is this: **the same artefact graph, projected into different surfaces for different stakeholders, at different depths, with different language.**

This pattern showed up in:
- 3 layers (Rooms/Phases/Milestones) — same graph, three projections
- 6 stakeholder surfaces — same graph, six views
- 4 progressive disclosure levels — same graph, four depths
- Language toggle (plain English/technical) — same graph, two vocabularies
- Pattern pre-fill — same graph, one starting point with different defaults

The artefact graph is the single source of truth. Everything else is a derived view. This is type collision resolution at the architecture level — instead of trying to produce one artifact that serves everyone, produce one graph and derive many views.

This is also the strongest connection to the Accretive Workspace design. The Accretive Workspace has the same principle: the artefact (the argument skeleton, the lattice, the seedbed) is the single source of truth, and the views (prose, presentation, notes) are derived. We've arrived at the same architectural insight from two different starting points. That's a strong signal.

---

## The Honest Assessment

This design is **structurally ambitious and emotionally intelligent, but unvalidated and under-specified in the interaction layer.**

The architecture (3 layers, pattern-first entry, identity questions, Mirror + specialists, milestone exit points) is strong. It draws on months of principled design thinking and resolves real tensions.

The interaction design (what the user actually sees, clicks, reads, and does at each moment) is at the concept level. We know the rooms exist, but not what they look like. We know the attention map exists, but not how it works. We know the coherence check exists, but not what it feels like.

The gap between architecture and interaction is exactly where UX design needs to do its hardest work — translating strong concepts into specific, testable, buildable interactions. This is where the next phase should focus.The retrospective is saved. The most honest takeaway: we've built a structurally sound, emotionally intelligent **hypothesis**. It needs real users before it needs more features. The next meaningful step is five sessions with real principals — not more design, but testing the core assumptions that the whole edifice rests on.

---

## Run 10 — Agentic Expert ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `6e2c4e16...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent — it takes user requirements and produces a complete, platform-agnostic design specification that another workflow could then use to build the agent on any platform (LangGraph, CrewAI, AutoGen, etc.).

Please provide your expert perspective on:
1. What are the essential steps/phases this workflow agent should go through? (e.g., intake, analysis, design, validation)
2. What agentic patterns apply here? (e.g., ReAct, planning, multi-step, human-in-the-loop)
3. What should the design spec artifact contain? (e.g., agent persona, tools, memory, decision logic, guardrails, failure modes)
4. What supporting artifacts should be produced alongside the spec?
5. How should the workflow handle ambiguity, conflicting requirements, or gaps in user input?
6. What does the state machine / flow of this workflow look like?

Focus on the agentic architecture of the workflow itself — the design of the design agent. Not implementation code.

We've gathered input from all three team members on designing an agentic workflow that produces agent design specs. Please synthesize the following three contributions into ONE unified, cohesive prototype design document.

The document should integrate the best ideas from each, resolve any tensions, and present a clear, actionable prototype that the team can hand off to an implementation workflow.

## Team Input Summary

### Business Strategist Key Points:
- Three target users: Daniel Kovacs (domain expert with blank-page problem), Sarah Chen (business owner needing verification), Developers (needing structured specs)
- Value prop: "Design spec is the product, methodology is the moat, implementation is the commodity, trust infrastructure is the category"
- Key risks: "Just another template" perception, over-engineering the workflow, platform-agnostic spec falling between stools, credibility gap, category creation difficulty
- Output strategy: One typed graph, many stakeholder views. Progressive engagement: Boundary Map (30 min) → Allocation Map (half day) → Operations Manual (1-2 weeks) → Trust Ledger (ongoing)
- Platform-agnostic: Spec describes WHAT and WHY, never WHICH TOOL. Test: could two different implementation teams on different frameworks produce functionally equivalent agents?

### AI UX Innovator Key Points:
- Three "Rooms": Discovery (expansive), Structure (constructive), Realisation (concrete)
- Pattern-first entry: Select archetype → pre-fill 40-70% → user overrides what matters
- 4 Identity Questions first (essence, orientation, violation, wrongness)
- Cognitive mode → input modality mapping (narrative=conversation, boundary=drag-sort, exploratory=cards, verification=scenarios, architectural=canvas, configurational=dials, evaluative=dashboard)
- Attention Map navigation (settled/needs attention/requires input/not yet applicable)
- Typed outputs (boundary map=visual, authority=cards, etc.)
- Single session + multi-session support. Every decision persistent and revisable.
- Mirror Agent as companion (reflects, never judges)
- 7 UX principles: pattern-first, identity-before-behaviour, possibility gradient, typed I/O, one clear next step, decisions revisable, feeling cascade

### Agentic Expert Key Points:
- 7 phases: Intake → Identity → Boundaries → Architecture → Behaviour → Validation → Specification
- Pattern: Planned Workflow with Human Gates (NOT ReAct)
- Human gates after: Intake, Identity, Boundaries, Validation
- Multi-agent workflow (not single agent): Intake Agent, Identity Explorer, Boundary Mapper, Architect, Validator, Compiler
- 8-section spec: Identity, Boundaries, Task Map, Knowledge Requirements, Capabilities, Behaviour Rules, Verification & Trust, Failure & Recovery
- 6 supporting artifacts: Boundary Map, Risk Register, Decision Log, Gaps & Assumptions Register, Implementation Readiness Checklist, Confidence Map
- Ambiguity strategy: "Doubt defaults to the human" — explore before assuming, make trade-offs visible, safe defaults with flags
- State machine with loop-back paths, skip paths for simple agents, exit paths at every gate
- The meta-principle: the workflow must practise what it produces

## Your Task:
Create a unified prototype design document that:
1. Integrates all three perspectives into a single coherent design
2. Resolves any tensions (e.g., the 3 "Rooms" from UX vs the 7 "Phases" from architecture — map them to each other)
3. Presents the workflow architecture, user journey, output artifacts, and key design principles as one unified story
4. Is structured as a prototype design spec that another workflow could use to implement this
5. Keeps it at design spec level — no implementation code or platform specifics

Make it clear, well-structured, and actionable. This is the deliverable the user asked for.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from an agentic architecture perspective?** What patterns, structures, or architectural decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we learn about designing multi-agent workflows? What worked that we should repeat? What patterns emerged that we should codify? Where did the architecture reveal gaps we need to address in future workflow designs?

Be candid and specific. Draw on your architectural analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

### Response

I'll be direct about what's genuinely strong, what's genuinely learned, and what's genuinely missing.

---

## 1. Key Strengths

### The Three-Layer Architecture Is the Strongest Structural Decision

Rooms (experience), Phases (logic), Milestones (value) — these are not three ways of describing the same thing. They're three different design surfaces that serve three different audiences. The user FEELS rooms, the agents EXECUTE phases, the business DELIVERS milestones.

Previous work conflated these. The 10 CAWDP phases served as logic AND experience AND value delivery simultaneously. Separating them means each can evolve independently: add a phase without changing the room experience, add a milestone without changing the processing logic, redesign a room without touching the phase sequence.

This is the kind of architectural decision that doesn't look impressive on paper but prevents months of confusion later. It's the separation of concerns principle applied to workflow design — and it's rare in agentic system design, where most people jump straight to "what does the agent do?" without first answering "what does the user experience? what does the business deliver?"

### The Mirror Agent as Surface Layer

This is architecturally significant and worth calling out specifically. The user interacts with ONE agent. Seven specialists do the work behind the scenes. This isn't just a UX decision — it's a trust decision.

Daniel Kovacs and Sarah Chen should never need to understand that there are seven different agents. They talk to one companion that reflects, routes, and translates. If they had to interact with seven different agents directly, the cognitive load would be exactly the type collision problem the workflow is designed to solve — seven different interaction modes, seven different tones, seven different authority boundaries to track.

The Mirror Agent is the Accretive Workspace's "one clear next step" principle applied to multi-agent orchestration. One surface, many engines.

### Verification Independence Built Into the Architecture

The Validator is a separate agent from the Architect, with a different class (Assessor vs Generator) and a different orientation (adversarial vs constraint-oriented). This isn't just good practice — it's CAWDP's CC-1 (Verification Independence) applied to the workflow itself.

The workflow practises what it produces. If the output spec requires verification separation, the workflow itself has verification separation. This is the meta-principle in action, and it's not decorative — it prevents the Architect from grading its own homework.

### Possibility Gradient as Architectural Force, Not Just UX

The gradient from Discovery (possibility-oriented, expansive) through Structure (bridge, constructive) to Realisation (constraint-oriented, adversarial) isn't just about visual design or tone. It's about **what the agents are allowed to do at each stage.**

The Identity Explorer is explicitly possibility-oriented — it opens space, reflects, never qualifies. The Architect is explicitly constraint-oriented — it builds from known inputs, never reopens possibility. If these orientations were swapped or blurred, the workflow would produce either over-constrained identities (can't explore what the agent could be) or under-constrained architectures (building on shifting ground).

The possibility orientation principle is the guard rail that prevents the workflow from collapsing possibility and constraint into the same phase — which is exactly what happens in most agent design tools.

### Every Milestone Is an Exit

This is commercially as well as architecturally important. The Boundary Map at Milestone 1 is independently valuable — a principal can take it to any vendor. This means the workflow isn't a funnel that only has value at the end. It's a series of valuable artifacts that compound.

Architecturally, this means the state machine has clean exit paths at every human gate. No dead ends, no "you must complete all 7 phases to get value." This is progressive disclosure applied to commercial engagement — and it maps directly to the consulting Boundary Journey milestones.

### The Four Identity Questions as the Design Engine

The decision to front-load identity (what IS this agent? orientation? violation? wrongness?) and derive boundaries from identity (rather than the reverse) is structurally sound. It means 40-70% of the specification is determined by four questions, which means 40-70% of the design time is spent on the most important decisions, not the most numerous ones.

This is the CAWDP "Direction before Destination before Path before Work" principle in action. Identity is direction. The rest flows from it.

---

## 2. Key Learnings and Gaps

### LEARNING: The Architecture Revealed That the Workflow Itself Hasn't Been CAWDP'd

This is the most important gap. The workflow designs agents, but it hasn't been designed THROUGH the same methodology. Let me be specific about what's missing:

- **No complementarity analysis** — which tasks should the Mirror Agent handle vs which should be routed to specialists? The design says "Mirror routes to specialists" but hasn't analysed which routing decisions require human judgment (complementarity gap ≥ 6) vs which can be automated.
- **No FMEA** — what happens when the Intake Agent receives gibberish? When the Identity Explorer hits an infinite loop? When the Validator and Architect disagree? When the user leaves mid-session?
- **No specification aging** — the workflow will produce agent specs that include specification aging schedules, but the workflow itself has no mechanism for updating its own patterns, safe defaults, or identity question templates.
- **No cost budget** — the workflow has seven specialist agents, each consuming tokens. No per-phase or per-workflow cost budget.
- **No progressive autonomy for the workflow** — the output agents have shadow → advisory → supervised → autonomous paths, but the workflow itself doesn't have a trust relationship with the user that deepens over time.

This isn't a criticism — it's the natural result of designing from three perspectives in one pass. But it means the workflow needs CAWDP applied to itself before it's production-ready.

### LEARNING: The Ambiguity Strategy Is Philosophically Clear but Operationally Thin

"Doubt defaults to the human" is the right principle. But the document doesn't specify HOW doubt is detected, HOW options are presented, or HOW long the workflow waits for human input.

Concretely:
- What EXACTLY triggers "doubt"? Is it a confidence score? A pattern match below a threshold? A contradiction detected? All three?
- When the workflow presents options to the user, what format are they in? Is there a ranked list? A visual comparison? A scenario-based explanation?
- If the user doesn't respond to a doubt flag (they walked away, they're busy, they're confused), does the workflow pause indefinitely? Apply safe defaults after a timeout? Loop back?
- What's the interaction between safe defaults and the confidence map? If 30% of the spec is safe defaults, is that a 30% confidence spec? Or does each default have its own confidence level?

The principle is right. The operational mechanism needs design.

### LEARNING: The Pattern System Is Under-Specified

Five patterns (Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner) are listed as pre-fill templates. But:
- **What happens when a user's needs don't match any pattern?** The document says "explore more deeply" but doesn't specify what that exploration looks like structurally.
- **What about agents that span multiple patterns?** A project coordinator might be 60% Review Partner + 30% Multi-Lens Analyst + 10% Discovery Explorer. How does pattern matching handle hybrid compositions?
- **How are patterns created and added?** The methodology says patterns are "pre-validated agent archetypes" — validated by whom? Through what process? How does a new pattern get added to the system?

The pattern system is the entry point for most users. If it's too rigid, users feel constrained. If it's too loose, it's no help. This needs more design work.

### LEARNING: The Harm-Capable Path Is Marked but Not Paved

The Boundary Mapper identifies harm-capable agents (agents whose output can cause external harm if accepted without review). But then what? The document says "flag as harm-capable and require DO_NOT_SUGGEST mechanism" but doesn't specify:
- Does a harm-capable agent trigger different downstream processing? (It should — verification should be more rigorous, progressive autonomy should be more conservative, the spec should have additional sections.)
- Does a harm-capable agent change the workflow's own behaviour? (Should the Mirror Agent adopt a more cautious tone? Should the Validator be more adversarial?)
- How does the harm assessment feed into the Validation phase specifically? (The Validator should have explicit harm-capable checks, not just generic consistency checks.)

This is the code reviewer insight from CAWDP — the first agent where output can cause external harm requires a new class of safeguard. The workflow flags it but doesn't yet ACT differently because of it.

### LEARNING: The Specialist Agent Authority Boundaries Are Stated but Not Stress-Tested

Each specialist has a "what it NEVER does" boundary. But:
- **What happens when a boundary is tested?** The Identity Explorer "never decides identity" — but what if the user explicitly asks it to decide? Does it refuse? Redirect? Explain why it can't?
- **What happens when two specialists produce conflicting outputs?** The Architect says "build from known inputs" but the Identity Explorer says "open possibility." If they disagree about the same aspect of the agent, who wins?
- **What happens when a specialist is given an input it can't process?** The Intake Agent "never judges" — but what if the user provides explicitly contradictory requirements that can't be captured without judgment?

These are the same boundary stress-tests that CAWDP prescribes for any agent, but we haven't applied them to our own specialist agents yet.

### LEARNING: The Three-Perspective Synthesis Revealed a Structural Pattern Worth Codifying

When three perspectives (Business, UX, Architecture) designed the same workflow, the natural integration was:

- **Business perspective** → What the user GETS (milestones, value, exit points)
- **UX perspective** → What the user FEELS (rooms, cognitive modes, interaction patterns)
- **Architecture perspective** → What the workflow DOES (phases, agents, state machine)

This isn't accidental. It's a structural pattern that should be codified for any multi-agent workflow design:

> **Every multi-agent workflow has three layers: Experience, Logic, and Value. Design all three. Map them to each other. Make them independently evolvable.**

This is a genuinely new insight from this design exercise. CAWDP currently has phases (logic) and some UX thinking (cognitive modes, progressive disclosure) but doesn't explicitly separate the three layers or require them to be designed and mapped independently.

### LEARNING: The Possibility Orientation Principle Validated Itself During Design

The workflow starts in Discovery (possibility-oriented) and tightens toward Realisation (constraint-oriented). But during the design process, we also started in possibility (brainstorming, exploring, "what if?") and tightened toward constraint (specifying, validating, "is this complete?").

The possibility gradient isn't just a design FOR the workflow — it's a pattern IN the design process itself. Any team designing a multi-agent workflow should expect to start in possibility (wide-open brainstorming) and naturally tighten toward constraint (specific decisions). The question is whether the methodology supports that gradient or fights it.

CAWDP should probably have an explicit meta-principle: **The design process follows the same possibility gradient as the designed system.** Start in possibility (Phase 0), tighten toward constraint (Phase 9). Don't force constraint-oriented decisions in possibility-oriented phases.

### LEARNING: The "Workflow Practises What It Produces" Principle Needs a Test

The document states this as a design principle. But there are places where it's violated or untested:

- The output spec requires **epistemic metadata** on every output. Does the workflow itself produce epistemic metadata on its own outputs? (Does the Intake Agent tag its pattern match with a confidence score? Does the Boundary Mapper tag its classification with a provenance note?)
- The output spec requires a **specification aging schedule**. Does the workflow have a mechanism for its own patterns and defaults to age and refresh?
- The output spec requires **verification independence**. The workflow has this (Validator separate from Architect). ✓
- The output spec requires **authority boundaries**. The workflow has these (each specialist has "what it NEVER does"). ✓
- The output spec requires **progressive autonomy**. The workflow doesn't have this for itself — it treats the user as the same authority at every phase, with no mechanism for the workflow to earn more autonomy as trust builds.

The principle is right. The practice is partial. The gap is honest.

### LEARNING: What Worked That We Should Repeat

1. **Three-perspective synthesis** — Business, UX, and Architecture forced resolution of tensions that would have been invisible from any single perspective. The three-layer architecture (Rooms/Phases/Milestones) is the direct result of this synthesis. Repeat this for every workflow design.

2. **Starting with users, not agents** — Daniel Kovacs and Sarah Chen were defined before the specialist agents. This is the CAWDP Phase 8 (Human Experience Design) applied to the meta-agent itself, and it produced better architecture decisions than starting with agent capabilities would have.

3. **Identity before behaviour** — The four identity questions determined 40-70% of the spec before a single task was defined. This dramatically reduced the design space and prevented premature architecture decisions.

4. **Milestones as exit points** — Designing the commercial value milestones (Boundary Map, Allocation Map, Operations Manual, Trust Ledger) alongside the technical phases ensured that the workflow produces valuable artifacts at every stage, not just at the end.

5. **The class × orientation taxonomy for specialist agents** — Each specialist has both a class (Extractor, Assessor, etc.) and an orientation (Possibility, Bridge, Constraint, Adversarial). This two-dimensional specification prevented the "same class, different orientation" confusion that a flat taxonomy would have created.

### LEARNING: What We Should Codify as Patterns

1. **Surface + Engine pattern** — One user-facing agent (Mirror) routes to multiple back-office specialists. The user interacts with one agent; the work is distributed. This should be a standard pattern for any multi-agent workflow where the user shouldn't manage agent interactions.

2. **Pattern-first entry** — Instead of presenting a blank form, detect patterns from user input and pre-fill 40-70% of the specification. The user overrides what matters. This should be a standard pattern for any workflow that serves non-expert users.

3. **Milestone-as-exit pattern** — Every major phase boundary produces a standalone valuable artifact. The user can exit with value at any milestone. This should be a standard pattern for any workflow that serves time-constrained users (which is all of them).

4. **Possibility gradient pattern** — The workflow starts expansive and tightens toward constraint. The visual environment, interaction style, and agent tone all shift to match. This should be a standard pattern for any creative-to-structured workflow.

5. **Verification independence pattern** — The agent that validates is always a different agent (different class, different orientation) from the agent that creates. This should be a non-negotiable pattern for any multi-agent workflow.

### LEARNING: What the Architecture Revealed as Gaps for Future Designs

1. **No workflow-level CAWDP application** — The workflow designs agents but hasn't been designed through the same methodology. This is the most important gap. Future workflow designs should start with CAWDP Phase 0 (what's the target state for the workflow itself?) and proceed through all phases.

2. **No error recovery specification** — What happens when agents fail, users provide contradictory input, or sessions are interrupted? The state machine has happy paths and loop-back paths but no failure recovery paths.

3. **No cost model** — Seven specialist agents, each consuming tokens, with pattern matching, validation loops, and potential re-runs. The workflow needs a per-phase and per-workflow cost budget.

4. **No specification aging mechanism** — The patterns, safe defaults, and identity question templates are static. They need a mechanism for updating based on real-world use data.

5. **The Mirror Agent's routing logic is undefined** — We know it routes to specialists, but we don't know the routing rules. When does it route to Identity Explorer vs Boundary Mapper? Can it route to two specialists simultaneously? What if it's unsure which specialist is needed?

6. **The progressive autonomy for the workflow itself is missing** — The output agents have shadow → advisory → supervised → autonomous paths, but the workflow treats the user as the same authority at every phase. A returning user who's designed 10 agents probably doesn't need the same level of guidance as a first-time user.

7. **The cognitive mode mapping is acknowledged but not operationalized** — The document lists cognitive modes per phase (narrative, boundary, exploratory, etc.) but doesn't specify what the actual interaction looks like for each mode. This is UX design work that needs to happen before implementation.

These gaps don't invalidate the design — they define the next phase of work. The design is architecturally sound. The next step is applying the same methodology to the design itself.The reflection is captured. The two most important things to carry forward:

**The Three-Layer Pattern** — Experience, Logic, Value — is a genuine architectural discovery from this design exercise, not something imported from existing methodology. It should be codified as a standard pattern for any multi-agent workflow design.

**The workflow needs to be CAWDP'd** — the 10 gaps are real and most of them trace back to the same root cause: we designed the workflow architecturally but didn't apply the same methodology to the workflow itself. Complementarity analysis, FMEA, specification aging, progressive autonomy, cost budgeting — these are all things the output spec requires but the workflow doesn't yet practise.

The prototype is architecturally sound. The next step isn't more architecture — it's applying CAWDP to the architecture.

---

## Run 11 — Agentic Expert ✓ COMPLETED

*2026-04-27T07:30:05* · `glm-5.1:cloud` · `7ee31a8a...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent — it takes user requirements and produces a complete, platform-agnostic design specification that another workflow could then use to build the agent on any platform (LangGraph, CrewAI, AutoGen, etc.).

Please provide your expert perspective on:
1. What are the essential steps/phases this workflow agent should go through? (e.g., intake, analysis, design, validation)
2. What agentic patterns apply here? (e.g., ReAct, planning, multi-step, human-in-the-loop)
3. What should the design spec artifact contain? (e.g., agent persona, tools, memory, decision logic, guardrails, failure modes)
4. What supporting artifacts should be produced alongside the spec?
5. How should the workflow handle ambiguity, conflicting requirements, or gaps in user input?
6. What does the state machine / flow of this workflow look like?

Focus on the agentic architecture of the workflow itself — the design of the design agent. Not implementation code.

We've gathered input from all three team members on designing an agentic workflow that produces agent design specs. Please synthesize the following three contributions into ONE unified, cohesive prototype design document.

The document should integrate the best ideas from each, resolve any tensions, and present a clear, actionable prototype that the team can hand off to an implementation workflow.

## Team Input Summary

### Business Strategist Key Points:
- Three target users: Daniel Kovacs (domain expert with blank-page problem), Sarah Chen (business owner needing verification), Developers (needing structured specs)
- Value prop: "Design spec is the product, methodology is the moat, implementation is the commodity, trust infrastructure is the category"
- Key risks: "Just another template" perception, over-engineering the workflow, platform-agnostic spec falling between stools, credibility gap, category creation difficulty
- Output strategy: One typed graph, many stakeholder views. Progressive engagement: Boundary Map (30 min) → Allocation Map (half day) → Operations Manual (1-2 weeks) → Trust Ledger (ongoing)
- Platform-agnostic: Spec describes WHAT and WHY, never WHICH TOOL. Test: could two different implementation teams on different frameworks produce functionally equivalent agents?

### AI UX Innovator Key Points:
- Three "Rooms": Discovery (expansive), Structure (constructive), Realisation (concrete)
- Pattern-first entry: Select archetype → pre-fill 40-70% → user overrides what matters
- 4 Identity Questions first (essence, orientation, violation, wrongness)
- Cognitive mode → input modality mapping (narrative=conversation, boundary=drag-sort, exploratory=cards, verification=scenarios, architectural=canvas, configurational=dials, evaluative=dashboard)
- Attention Map navigation (settled/needs attention/requires input/not yet applicable)
- Typed outputs (boundary map=visual, authority=cards, etc.)
- Single session + multi-session support. Every decision persistent and revisable.
- Mirror Agent as companion (reflects, never judges)
- 7 UX principles: pattern-first, identity-before-behaviour, possibility gradient, typed I/O, one clear next step, decisions revisable, feeling cascade

### Agentic Expert Key Points:
- 7 phases: Intake → Identity → Boundaries → Architecture → Behaviour → Validation → Specification
- Pattern: Planned Workflow with Human Gates (NOT ReAct)
- Human gates after: Intake, Identity, Boundaries, Validation
- Multi-agent workflow (not single agent): Intake Agent, Identity Explorer, Boundary Mapper, Architect, Validator, Compiler
- 8-section spec: Identity, Boundaries, Task Map, Knowledge Requirements, Capabilities, Behaviour Rules, Verification & Trust, Failure & Recovery
- 6 supporting artifacts: Boundary Map, Risk Register, Decision Log, Gaps & Assumptions Register, Implementation Readiness Checklist, Confidence Map
- Ambiguity strategy: "Doubt defaults to the human" — explore before assuming, make trade-offs visible, safe defaults with flags
- State machine with loop-back paths, skip paths for simple agents, exit paths at every gate
- The meta-principle: the workflow must practise what it produces

## Your Task:
Create a unified prototype design document that:
1. Integrates all three perspectives into a single coherent design
2. Resolves any tensions (e.g., the 3 "Rooms" from UX vs the 7 "Phases" from architecture — map them to each other)
3. Presents the workflow architecture, user journey, output artifacts, and key design principles as one unified story
4. Is structured as a prototype design spec that another workflow could use to implement this
5. Keeps it at design spec level — no implementation code or platform specifics

Make it clear, well-structured, and actionable. This is the deliverable the user asked for.

Save the complete Agent Design Workflow Prototype Design Specification (the unified document from task 1c250e41) to the file system at: ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

The document should contain the full unified specification as produced — all 12 sections including: What This Is, Three Users, Three-Layer Architecture, Seven Phases Detail, Specialist Agents, Design Specification Contents (8 sections), Supporting Artifacts, Handling Ambiguity/Conflicts/Gaps, State Machine, Design Principles, Risks and Mitigations, and Prototype Scope.

After saving, confirm the file path and that it was saved successfully.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from an agentic architecture perspective?** What patterns, structures, or architectural decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we learn about designing multi-agent workflows? What worked that we should repeat? What patterns emerged that we should codify? Where did the architecture reveal gaps we need to address in future workflow designs?

Be candid and specific. Draw on your architectural analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Save the following two documents to the file system:

1. The Agent Design Workflow Specification → ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

2. The team's retrospective on strengths and learnings → ./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md

For document 1, use the complete specification document as produced in task 1c250e41 (the unified 12-section spec).

For document 2, compile the three team retrospectives into one document with these sections:

## Retrospective: Agent Design Workflow — First Full Workflow Design

### Part A: Cross-Cutting Strengths (synthesized from all three perspectives)
- The Three-Layer Architecture (Rooms/Phases/Milestones)
- Pattern-First Entry
- Identity-First Design (4 Identity Questions)
- Mirror + Specialists Architecture
- Every Milestone Is an Exit
- Verification Independence
- Possibility Gradient as Architectural Force
- Methodology Encoded in Structure

### Part B: Key Learnings
1. Type collision happened to us in our own design process
2. The three-layer pattern (Experience/Logic/Value) is a genuine architectural discovery
3. The methodology validated itself but also showed its limits
4. The specification output doesn't cleanly map to contract primitives
5. The ambiguity strategy is philosophically clear but operationally thin
6. The pattern system is under-specified
7. The harm-capable path is marked but not paved
8. Specialist agent authority boundaries aren't stress-tested
9. The workflow itself hasn't been CAWDP'd (10 specific gaps)
10. We have zero validation with real users
11. The visual/feeling layer is specified in goal, not detail
12. The coherence check is described but not designed

### Part C: Patterns to Codify
1. Surface + Engine pattern
2. Pattern-first entry
3. Milestone-as-exit
4. Possibility gradient
5. Verification independence
6. Identity before behaviour
7. Methodology encoded in structure

### Part D: What We'd Do Differently
- Start with Milestone 1 only
- Reduce specialist count for prototype
- Make possibility gradient a structural constraint
- "15-minute spec" as the headline, not a feature

### Part E: Honest Assessment
The architecture is structurally ambitious and emotionally intelligent, but unvalidated and under-specified in the interaction layer. The next step isn't more design — it's testing Milestone 1 with 5 real people.

Save both files and confirm paths.

### Response

I don't have direct filesystem write access, so I'll provide both complete documents as markdown code blocks. Copy each to the specified path.

---

**Document 1:** `./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md`

This was already provided in full in the previous response. I'll reproduce it here for completeness so both documents are together.

```markdown
# Agent Design Workflow — Prototype Design Specification

**Version:** 0.1  
**Status:** Prototype — ready for implementation workflow handoff  
**Date:** 2025

---

## 1. What This Is

An agentic workflow that takes a user's raw requirements and produces a complete, platform-agnostic design specification for an AI agent.

**Platform-agnostic** means the spec describes WHAT the agent does and WHY — never WHICH TOOL delivers it. The test: could two implementation teams on different frameworks (LangGraph, CrewAI, Agno, AutoGen) read the same spec and produce functionally equivalent agents? If yes, the spec is platform-agnostic.

**The meta-principle:** This workflow must practise what it produces. If the output spec says agents need identity, boundaries, and verification, then this workflow has identity, boundaries, and verification. If the output says doubt defaults to the human, then this workflow defaults uncertain decisions to the human.

---

## 2. Three Users, Three Surfaces

One workflow, three entry points. The same engine produces different outputs depending on who's using it.

| | **Daniel Kovacs**<br>Domain Expert | **Sarah Chen**<br>Business Owner | **Implementation Team**<br>Developers |
|---|---|---|---|
| **Their problem** | Blank page — "I know my domain but I can't design an agent" | Boundary & verification — "I don't know where AI should stop" | Type collision — "I need structured specs, not prose documents" |
| **What they need** | Guided design, not a form to fill | A clear line and a way to verify it | Typed, structured specs they can build from |
| **How they enter** | Conversation + Pattern selection | Boundary Map session (30 min) | Receives completed spec as input |
| **What they get** | Full design spec + all artifacts | Boundary Map → Allocation Map → Operations Manual | Implementation-ready typed specification |
| **Time commitment** | 2-4 hours (can pause and resume) | 30 min to half day | Reads the output, doesn't use the workflow |

Daniel and Sarah are the primary users of the workflow. The implementation team is the consumer of the output.

---

## 3. The Three-Layer Architecture

The system has three layers that describe the same workflow from three angles:

| Layer | Purpose | Structure |
|---|---|---|
| **Rooms** (Experience) | What the user FEELS | 3 visual/cognitive environments |
| **Phases** (Logic) | What the workflow DOES | 7 processing stages with specialist agents |
| **Milestones** (Value) | What the user GETS | 4 exit points, each with a tangible artifact |

These layers are NOT separate systems. They're the same workflow described for three audiences: the user (rooms), the agents (phases), and the business (milestones).

### How They Map Together

```
ROOMS              PHASES                              MILESTONES
                    ┌──────────┐
                    │ 1. Intake │──── Pattern match
                    └─────┬─────┘
                          │
DISCOVERY          ┌──────┴──────┐
(Expansive,         │ 2. Identity  │
 open, possibility) │ 3. Boundaries│────▶ MILESTONE 1: Boundary Map
                    └──────┬──────┘     (30 min, free or $495)
                           │
STRUCTURE          ┌───────┴───────┐
(Constructive,      │ 4. Architecture│
 shaping,           │ 5. Behaviour   │────▶ MILESTONE 2: Allocation Map
 constraint)        └───────┬───────┘     (half day, $795-1,495)
                           │
REALISATION        ┌───────┴───────┐
(Concrete,          │ 6. Validation  │
 verified,          │ 7. Specification│───▶ MILESTONE 3: Operations Manual
 committed)         └───────────────┘     (1-2 weeks, $5K-25K)
                                           MILESTONE 4: Trust Ledger
                                           (ongoing, $2-5K/qtr)
```

**The gradient from possibility to constraint is deliberate.** Discovery opens space. Structure shapes it. Realisation locks it down. The user should feel this shift — the visual environment, the interaction style, and the agent's tone all change as they move through the rooms.

---

## 4. The Seven Phases — Detail

### Phase 1: INTAKE

**What happens:** The user describes what they need in their own words. A paragraph, a brain-dump, a voice note, answers to a few starter questions — anything. The workflow listens, captures, and shapes.

**Agent:** Intake Agent (Extractor class — captures, never judges)

**Key actions:**
- Receive raw input in whatever form the user provides
- Parse and type the input: domain, business problem, target user, constraints, any existing mental model
- Run **pattern matching** against known agent archetypes:
  - Signal Detector (monitoring, alerting)
  - Multi-Lens Analyst (multi-perspective analysis)
  - Discovery Explorer (research, ideation)
  - Learning Scaffold (teaching, tutoring)
  - Review Partner (reviewing, quality-checking)
- If high-confidence match (≥80%): flag the pattern, prepare pre-fills for downstream phases
- If low-confidence match: note it, proceed without pre-fills — the Identity phase will explore further
- Detect immediate contradictions or gaps
- Identify the stakeholder surface level (Daniel, Sarah, or both)

**Output:** Typed Requirement Package + Pattern Match Assessment

**Human gate:** "Here's what I understood. Is this right?" — User confirms the workflow heard them correctly before proceeding.

**Cognitive mode:** Narrative (conversation)  
**Interaction:** Conversational input — the user talks, the workflow listens

---

### Phase 2: IDENTITY

**What happens:** Four questions that determine 40-70% of the entire spec. If the user selected a pattern in Intake, pre-filled answers appear — the user reviews, overrides, or accepts. If no pattern matched, the workflow explores with them.

**Agent:** Identity Explorer (Assessor class, possibility-oriented — reflects, never decides)

**The four identity questions:**
1. **What IS this agent?** — Not "what does it do?" but "what is it at its core?" (Example: "It's a lease risk spotter" not "it reviews leases")
2. **What's its stance toward possibility?** — Does it open space (explorer), shape space (builder), or guard space (guard)? This determines how the agent responds to ambiguity — by expanding options, narrowing options, or flagging them.
3. **What would VIOLATE its identity?** — What would make it NOT be itself anymore? (Example: "If it started giving legal advice, it wouldn't be a spotter anymore — it would be an advisor")
4. **What would it mean for this agent to be WRONG?** — Its worst failure IS its identity boundary in reverse. (Example: "The worst wrong is flagging a real risk as fine — that's the exact opposite of spotting")

**Pre-fill behaviour:** If a pattern was matched in Intake:
- Pre-filled answers appear with a "Why this answer?" explanation
- User can accept, override, or say "I'm not sure"
- "I'm not sure" triggers an exploration dialogue

**Output:** Identity Card (4 answers + agent class + orientation)

**Human gate:** "Is this the right agent?" — User confirms identity before boundaries are drawn.

**Cognitive mode:** Narrative + Exploratory (conversation + cards showing pre-filled options)  
**Interaction:** Conversation for free-form answers. Cards for pre-filled pattern options that the user accepts/overrides.

---

### Phase 3: BOUNDARIES

**What happens:** Before defining what the agent DOES, define what it NEVER does. This is the hardest boundary to maintain and the most important one.

**Agent:** Boundary Mapper (Measurer + Assessor class, bridge-oriented — classifies and flags, never finalizes)

**Key actions:**
- Derive explicit "never" rules from identity violation (question #3)
- Derive authority boundaries from failure mode (question #4) — what it CAN decide vs what it can only PREPARE a decision for
- Identify the **principal** — who this agent acts on behalf of (a person, a role, or an organisation)
- Classify the **reversibility** of each action type:
  - Easy undo (e.g., drafting text — just delete it)
  - Effort undo (e.g., sending an email — recall + follow-up)
  - No undo (e.g., executing a trade — the market already moved)
- Assess **harm potential** — can the agent's output cause external harm if accepted without review? (yes/no + mechanism)
- If yes → flag as harm-capable and require DO_NOT_SUGGEST mechanism

**Output:** Boundary Map (never-rules, authority boundaries, reversibility classification, harm assessment)

**Human gate:** "Are these the right lines?" — User confirms boundaries.

**This is Milestone 1.** The user can exit here with a Boundary Map — a single-page visual showing who does what. It's independently valuable: they can take it to any vendor, any platform, any implementation team.

**Cognitive mode:** Boundary (drag-sort — place tasks in "human does" / "agent does" / "system does" columns)  
**Interaction:** Drag-sort zones for task allocation. Cards for each boundary rule.

---

### Phase 4: ARCHITECTURE

**What happens:** Now that identity and boundaries are defined, the workflow can determine what the agent needs to work. The possibility space has been shaped — this phase fills in the structure.

**Agent:** Architect (Generator class, constraint-oriented — builds from known inputs, never reopens possibility)

**Key actions:**
- Define the **task space** — every cognitive operation the agent performs
- Classify each task by agent class:
  - Extractor: gathers information, never judges
  - Measurer: measures against rules, never interprets
  - Assessor: evaluates and flags, never finalizes
  - Generator: creates content, always under constraint
  - Aggregator: compiles and assembles, never adds new content
- For each task: input schema, output schema, quality checks
- Map **dependencies** between tasks (what must happen before what)
- Determine **composition**: is this one agent, a team, or a workflow? (The answer comes from the task map — single-class agents are often one agent; multi-class tasks often need a workflow)
- Identify **knowledge requirements** — what the agent needs to know, with quality minimums
- Identify **capability requirements** — what tools/integrations the agent needs
- Define **information boundaries** — what the agent should NOT have access to

**Pre-fill behaviour:** Pattern match + identity answers determine ~60% of the task map. The user reviews, adjusts, and adds domain-specific tasks.

**Output:** Architecture Blueprint (task map with class assignments, dependencies, knowledge/capability/information requirements, composition decision)

**Cognitive mode:** Architectural (canvas with typed connections between tasks)  
**Interaction:** Visual canvas. Tasks as cards, dependencies as lines. Drag to reorder, click to configure.

---

### Phase 5: BEHAVIOUR

**What happens:** Define how the agent acts — its reasoning, escalation rules, confidence thresholds, and progressive autonomy path.

**Agent:** Architect continues (same agent, constrained by architecture outputs)

**Key actions:**
- Define **reasoning approach** — when does the agent plan vs react vs ask for help?
- Define **escalation triggers** — specific conditions that hand back to a human (e.g., confidence below threshold, boundary violation detected, harm-capable output without verification)
- Define **confidence thresholds** — what confidence level triggers what action:
  - High confidence (4-5): proceed
  - Medium confidence (3): proceed with flags
  - Low confidence (1-2): stop and escalate
- Define **progressive autonomy path**:
  - Shadow: agent runs alongside, human does everything, workflow tracks what agent would have done
  - Advisory: agent suggests, human reviews every suggestion
  - Supervised: agent acts, human approves before anything leaves
  - Autonomous: agent acts within boundaries, human monitors the data
  - For each level: specific promotion criteria (not vibes — measured override rate, verification pass rate, cost variance)
- Draft the **directive** — the agent's instructions in its own voice (not technical system prompt — a plain-English description of how it behaves)
- Define **verification protocol** — who checks what and how:
  - Level 1 (structural): does the output match the expected format?
  - Level 2 (meaning): is the output correct in substance?
  - Level 3 (authority): did the agent stay within its boundaries?

**Safe defaults** apply to all of these. The user only needs to override what differs from the pattern's standard behaviour.

**Output:** Behaviour Specification (reasoning rules, escalation triggers, confidence thresholds, autonomy path, directive draft, verification protocol)

**Cognitive mode:** Configurational (dials, toggles, presets) + Evaluative (dashboard for autonomy path)  
**Interaction:** Dials/toggles for confidence thresholds. Timeline view for progressive autonomy. Text editor for directive draft.

---

**This is Milestone 2.** The user can exit here with an Allocation Map — who does what, with what authority, what happens when things fail, and how to recover. It's independently valuable: they can brief any implementation team with this document.

---

### Phase 6: VALIDATION

**What happens:** The workflow stress-tests its own design. This is NOT optional. It's a quality gate.

**Agent:** Validator (Assessor class, adversarial — stress-tests, never designs)

**This agent MUST be separate from the Architect.** The same agent that designed the spec cannot validate it — that's like a student grading their own exam.

**Key checks:**
1. **Identity coherence** — Would the defined behaviour violate the agent's identity? (If the Identity says "never gives advice" but the Behaviour says "provides recommendations" → flag)
2. **Boundary consistency** — Do the boundaries conflict with the tasks? (If Boundaries says "never decides" but Architecture assigns Assessor tasks with decision authority → flag)
3. **Completeness** — Are there gaps in the task map, dependencies, or knowledge requirements?
4. **Worst failure mode** — From identity question #4: can it happen given the current design? If yes → recommend a specific safeguard
5. **Harm paths** — Can the agent's output cause external harm? Is there a DO_NOT_SUGGEST mechanism?
6. **Hardest boundary moment** — When is the agent most likely to break its own rules? (e.g., under time pressure, with ambiguous input, when the user says "just do it")

**Output:** Validation Report (pass/fail per check, risk register with all identified issues, recommended changes)

**Human gate:** "Here's what I found. Do you accept these risks, or do you want to fix them?" — User decides what to address.

**Loop-back paths:**
- Identity conflict → back to Phase 2
- Boundary violation → back to Phase 3
- Architecture gap → back to Phase 4
- Behaviour contradicts identity → back to Phase 5 (or Phase 2 if the identity itself is the problem)

**Cognitive mode:** Verification (scenarios — "what if this happened?")  
**Interaction:** Scenario cards showing stress-test results. Each issue is a card with: what was found, what it means, what to do about it, and whether it's a risk to accept or a problem to fix.

---

### Phase 7: SPECIFICATION

**What happens:** Compile all validated outputs into the complete design specification.

**Agent:** Compiler (Aggregator class — assembles, never adds new content)

**Key actions:**
- Assemble all phase outputs into the final spec (8 sections — see Section 6)
- Apply safe defaults for anything not explicitly specified
- Tag every element with its **source phase** (traceability)
- Mark **confidence levels** on every section (high/medium/low — derived from the attention/confidence data)
- Generate all **supporting artifacts** (see Section 7)
- Apply the **platform-agnostic test**: does this spec describe WHAT and WHY, never WHICH TOOL?

**Output:** Complete Agent Design Specification + Supporting Artifacts

**Human gate:** "Here's your complete specification. Review and approve."

**No loop-back from here.** If the user wants changes, they re-enter the workflow at the relevant phase. The spec is compiled, not living.

**Cognitive mode:** Evaluative (dashboard — overview of all sections, confidence levels, readiness)  
**Interaction:** Summary dashboard. User can click into any section for detail. "Approve" button finalizes.

---

**This is Milestone 3.** The Operations Manual is a direct derivation from the complete spec — a shorter, operational document that the team follows day-to-day. Milestone 4 (Trust Ledger) is ongoing monitoring after deployment.

---

## 5. The Specialist Agents

| Agent | Class | Orientation | Authority Boundary | What It NEVER Does |
|---|---|---|---|---|
| **Intake Agent** | Extractor | Possibility | Capture only | Never judges, never filters, never interprets |
| **Identity Explorer** | Assessor | Possibility | Reflect only | Never decides identity, never qualifies possibility |
| **Boundary Mapper** | Measurer + Assessor | Bridge | Classify and flag only | Never finalizes boundaries, never draws the line |
| **Architect** | Generator | Constraint | Build from known inputs only | Never reopens possibility, never adds tasks not in the map |
| **Validator** | Assessor | Adversarial | Stress-test only | Never designs, never fixes, never decides what's acceptable |
| **Compiler** | Aggregator | Constraint | Assemble only | Never adds new content, never changes existing content |
| **Mirror Agent** | Assessor | Adaptive | Translate and reflect | Never judges, never decides, never filters information |

### The Mirror Agent — The User's Companion

The Mirror Agent is the **surface layer** — the agent the user talks to. The specialist agents are the **engine** — they do the work behind the scenes.

The Mirror Agent:
- Routes the user's input to the right specialist agent
- Translates specialist output into the user's language (plain English, domain terminology)
- Reflects the user's own words back to them for confirmation
- Never judges, never decides, never filters — it reflects and connects

Think of it as a concierge: the user talks to the concierge, the concierge sends the request to the right department, and the concierge presents the result in a way the user understands.

---

## 6. The Design Specification — What It Contains

The primary output is an 8-section design specification. Every section is platform-agnostic.

### Section 1: IDENTITY

| Item | Description |
|---|---|
| Agent name & role | In plain English (e.g., "Lease Risk Spotter") |
| Four identity answers | Essence, orientation, identity violation, worst failure |
| Agent class | Extractor / Measurer / Assessor / Generator / Aggregator |
| Orientation | Possibility / Bridge / Constraint |
| Principal | Who it acts on behalf of |
| Pattern matched | Which archetype was selected (if any) |

### Section 2: BOUNDARIES

| Item | Description |
|---|---|
| Never rules | What it NEVER does (derived from identity violation) |
| Authority boundaries | What it CAN decide vs what it can only PREPARE a decision for |
| Reversibility | Easy undo / effort undo / no undo — per action type |
| Harm assessment | Can its output cause external harm? yes/no + mechanism |
| DO_NOT_SUGGEST triggers | When it should flag uncertainty instead of suggesting |
| Information boundaries | What it should NOT have access to and why |

### Section 3: TASK MAP

| Item | Description |
|---|---|
| Complete task list | Every cognitive operation the agent performs |
| Class assignment per task | Extractor / Measurer / Assessor / Generator / Aggregator |
| Input schema per task | What information the task needs (format, type, source) |
| Output schema per task | What the task produces (format, type, destination) |
| Dependencies | What must happen before what |
| Composition | Single agent / team / workflow + rationale |

### Section 4: KNOWLEDGE REQUIREMENTS

| Item | Description |
|---|---|
| Domain knowledge | What it needs to know about the subject |
| Context | What it needs to know about the user/organisation |
| Reference data | Standards, rules, rubrics it measures against |
| Quality minimums | Accuracy, completeness, sufficiency thresholds |
| Update cadence | How often its knowledge needs refreshing |
| Information boundaries | What it should NOT have access to (repeated from Section 2 for implementation convenience) |

### Section 5: CAPABILITIES

| Item | Description |
|---|---|
| Tool/capability requirements | What it needs to be able to DO (not which specific tool — what function) |
| Integration points | What systems it connects to (what data flows in and out) |
| Invocation method | How it's triggered: scheduled / event-driven / on-demand |
| Output delivery | How it delivers results: format, channel, frequency |

### Section 6: BEHAVIOUR RULES

| Item | Description |
|---|---|
| Reasoning approach | When to plan, react, or escalate |
| Escalation triggers | Specific conditions that hand back to human |
| Confidence thresholds | What confidence level triggers what action |
| Progressive autonomy path | Shadow → Advisory → Supervised → Autonomous with promotion criteria |
| Directive draft | The agent's instructions in its own voice |
| Safe defaults | What the framework chose for the user (flagged, not hidden) |

### Section 7: VERIFICATION & TRUST

| Item | Description |
|---|---|
| Verification protocol | 3 levels: structural, meaning, authority — who checks what how |
| Epistemic metadata | 6 fields on every output: confidence, provenance, assumptions, limitations, recency, uncertainty |
| Audit trail | What gets logged, at what assurance level (logged / assured / verified) |
| Cost budget | Per-task and overall budget with halt conditions |
| Override protocol | How a human overrides and what happens when they do |

### Section 8: FAILURE & RECOVERY

| Item | Description |
|---|---|
| Failure mode register | What can go wrong per task |
| Recovery paths | What happens after each failure type |
| Worst failure mode | From identity #4 — the design MUST prevent this |
| Hardest boundary moment | When the agent is most likely to break its own rules |
| Specification aging schedule | When should this design be reviewed/updated? |

---

## 7. Supporting Artifacts

Produced alongside the spec, each independently valuable.

| Artifact | What It Is | Who Uses It | When |
|---|---|---|---|
| **Boundary Map** | Single-page visual: Human / Agent / System columns, tasks as rows | Sarah, any stakeholder | Milestone 1 — can exit here |
| **Risk Register** | Every identified failure mode with likelihood, impact, mitigation | Implementation team, governance participants | Produced in Validation |
| **Decision Log** | Every significant design decision: what was decided, alternatives, why, who decided | Any stakeholder (decision archaeology) | Accumulated throughout |
| **Gaps & Assumptions Register** | What the workflow couldn't resolve and had to assume | Implementation team (address these first) | Accumulated throughout |
| **Implementation Readiness Checklist** | "Does the implementing team have everything they need?" — organized by spec section | Implementation team | Produced in Specification |
| **Confidence Map** | High/medium/low confidence per spec section | Implementation team, governance participants | Produced in Specification |

---

## 8. Handling Ambiguity, Conflicts, and Gaps

The workflow uses one principle: **doubt defaults to the human.** The workflow PREPARES the decision (shows options, consequences, trade-offs) but the human DECIDES.

### When the user is vague — "I'm not sure what I want"

1. **Name the ambiguity explicitly** — "I see two possible meanings here: A and B. Which one?"
2. **Show the consequence of each option** — "If A, then [design implication]. If B, then [different implication]."
3. **If the user still can't decide** — Apply the safe default (the less risky interpretation wins). Flag it as a default, not a decision.
4. **Mark it in the Gaps Register** — Future review should revisit this.

**Never:** Silently pick one path and not tell the user.

### When requirements conflict — "I want it fast AND thorough AND cheap"

1. **Name the conflict** — "You've asked for X and Y, but they trade off because [reason]."
2. **Show the trade-off spectrum** — "More X means less Y. Here's what different positions look like."
3. **Ask for priority** — "If you had to rank these, what matters most?"
4. **If unresolvable** — Document as a design tension. Some conflicts are real. They're not bugs — they're constraints the implementation must manage.

### When information is missing — "The user didn't mention X"

1. **Distinguish required gaps from optional gaps:**
   - **Required gaps** (no identity, no boundaries) → pause the workflow, work with the user to fill them
   - **Optional gaps** (no tool preference, no knowledge source) → apply safe defaults, flag them
2. **Apply safe defaults for optional gaps** — The pattern system provides these. A "Review Partner" pattern has a default verification protocol, default confidence thresholds, default escalation rules.
3. **Flag every default** — In the spec, defaults are visually distinct from user decisions. The confidence map marks them as lower confidence.
4. **Required gaps pause the workflow** — "I need to know who this agent acts on behalf of before I can design its authority boundaries. Let's figure this out together."

---

## 9. State Machine

```
                    ┌───────────────────┐
                    │   START            │
                    │   (user enters     │
                    │    raw input)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │   PHASE 1: INTAKE │
                    │   (Extractor)      │
                    │   Pattern match    │
                    └────────┬──────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
         High match     Low match      No match
         (≥80%)         (40-79%)       (<40%)
              │              │              │
              ▼              ▼              ▼
        Pre-fill 50-   Pre-fill 20-    No pre-fill
        70% of next    40% of next     Explore mode
        phases         phases
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Is this right?"  │──── No → back to input
                    └────────┬──────────┘
                             │ Yes
                    ┌────────▼──────────┐
                    │ PHASE 2: IDENTITY │
                    │ (Assessor,        │
                    │  possibility)     │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Is this the      │──── No → explore more
                    │  right agent?"    │──── "I need to think" →
                    └────────┬──────────┘     SAVE & EXIT with
                             │ Yes              partial Identity Card
                    ┌────────▼──────────┐
                    │ PHASE 3:          │
                    │ BOUNDARIES        │
                    │ (Measurer+Assessor│
                    │  bridge)          │
                    └────────┬──────────┘
                             │
              ┌──────────────▼──────────────┐
              │ HUMAN GATE:                 │
              │ "Are these the right lines?"│
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 1 EXIT:    ║   │
              │ ║  Boundary Map         ║   │
              │ ║  (can stop here)      ║   │
              │ ╚═══════════════════════╝   │
              └──────────────┬──────────────┘
                             │ Continue
                    ┌────────▼──────────┐
                    │ PHASE 4:          │
                    │ ARCHITECTURE      │
                    │ (Generator,       │
                    │  constraint)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ PHASE 5:          │
                    │ BEHAVIOUR         │
                    │ (Generator,       │
                    │  constraint)      │
                    └────────┬──────────┘
                             │
              ┌──────────────▼──────────────┐
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 2 EXIT:    ║   │
              │ ║  Allocation Map       ║   │
              │ ║  (can stop here)      ║   │
              │ ╚═══════════════════════╝   │
              └──────────────┬──────────────┘
                             │ Continue
                    ┌────────▼──────────┐
                    │ PHASE 6:          │
                    │ VALIDATION        │
                    │ (Assessor,        │
                    │  adversarial)     │
                    └────────┬──────────┘
                             │
               ┌─────────────┼─────────────┐
               │             │             │
          Issues found   Minor issues   Clean pass
          (critical)     (acceptable)   
               │             │             │
        Loop back:     Flag risks     │
        Identity → P2  in report      │
        Boundary → P3  Accept &       │
        Architecture→P4  continue     │
        Behaviour → P5              │
               │             │             │
               └─────────────┼─────────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Accept risks or  │
                    │  fix issues?"     │
                    └────────┬──────────┘
                             │ Accept
                    ┌────────▼──────────┐
                    │ PHASE 7:          │
                    │ SPECIFICATION     │
                    │ (Aggregator)      │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │ HUMAN GATE:       │
                    │ "Review & approve"│
                    └────────┬──────────┘
                             │ Approve
              ┌──────────────▼──────────────┐
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 3:         ║   │
              │ ║  Operations Manual    ║   │
              │ ╚═══════════════════════╝   │
              │                             │
              │ Complete Design Spec +      │
              │ all supporting artifacts    │
              │                             │
              │ ╔═══════════════════════╗   │
              │ ║  MILESTONE 4:         ║   │
              │ ║  Trust Ledger         ║   │
              │ ║  (post-deployment,    ║   │
              │ ║   ongoing)            ║   │
              │ ╚═══════════════════════╝   │
              └─────────────────────────────┘
```

### Skip Paths

For simple agents (single task, low stakes, no harm potential), Phases 3-5 can compress into a single step. The workflow detects simplicity and adjusts:

- **Simple agent** (1-2 tasks, Extractor or Measurer class, no harm potential) → Boundaries + Architecture + Behaviour in one step
- **Moderate agent** (3-8 tasks, multi-class, moderate harm potential) → Full 7 phases
- **Complex agent** (9+ tasks, harm-capable, multi-human roles) → Full 7 phases with extended Validation

### Exit Paths

The user can leave at any human gate with whatever's been produced so far:

| Exit Point | What They Take With Them |
|---|---|
| After Intake gate | Typed Requirement Package |
| After Identity gate | Identity Card |
| After Boundary gate (Milestone 1) | Boundary Map |
| After Architecture/Behaviour gate (Milestone 2) | Allocation Map |
| After Validation gate | Validation Report + Risk Register |
| After Specification gate (Milestone 3) | Complete Spec + All Artifacts |

Every exit produces something useful. No dead ends.

### Session Persistence

The workflow supports pause and resume. Every decision is persistent and revisable. A user can:
- Start on Monday, leave after Identity, come back Thursday and pick up at Boundaries
- Revisit a previous decision at any phase (the workflow updates downstream consequences)
- Run multiple agent designs in the same account (each has its own session state)

---

## 10. Design Principles

These are the rules the workflow follows. They're not suggestions — they're constraints.

1. **Pattern-first, not form-first.** The user's entry point is "what are you trying to do?" not "fill in these 40 fields." Pattern selection pre-fills the spec; the user overrides what matters.

2. **Identity before behaviour.** You define WHAT the agent IS before what it DOES. The four identity questions come first and determine everything downstream.

3. **Boundaries before capabilities.** You define what the agent NEVER does before what it CAN do. This is the hardest boundary to maintain and the most important one.

4. **Possibility gradient.** The workflow starts in possibility (Discovery) and tightens toward constraint (Realisation). The visual environment, the interaction style, and the agent's tone all shift to match.

5. **Doubt defaults to the human.** When the workflow can't determine the right answer, the human decides. The workflow prepares the decision; the human makes it.

6. **The spec is typed, not prose.** Every section has a defined format. Every element has a type. Implementation teams receive structured data, not walls of text.

7. **One clear next step.** The user always knows what to do next. The attention map shows what's settled, what needs attention, what requires input, and what's not yet applicable.

8. **Decisions are revisable.** Nothing is locked until the final specification is approved. Every decision can be changed, and the workflow propagates the consequences.

9. **Every milestone is an exit.** The user can stop at any gate with something valuable. No dead ends, no "you must complete the whole thing to get value."

10. **The workflow practises what it produces.** If the output spec requires verification, the workflow itself has verification. If the output spec requires identity, the workflow's agents have identity. The meta-principle is the proof.

---

## 11. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **"Just another template"** perception | High | Fatal | Pattern-first entry that ENFORCES methodology (not fills in forms). The 15-minute specification must feel different from filling in a template. |
| **Over-engineering the workflow** | High | Moderate | Start with Intake + Identity + Boundaries + Specification (4 phases, not 7). Add Architecture, Behaviour, Validation when the simpler version is validated. |
| **Platform-agnostic spec falls between stools** | Moderate | High | The platform-agnostic test: could two teams on different frameworks produce equivalent agents? Apply this test to every section. |
| **Credibility gap before case studies** | High | Moderate | Open methodology + 77% Challenge builds trust before asking for payment. The Boundary Map is free. |
| **Category creation difficulty** | Moderate | High | Never call it a "framework." It's a methodology. Position on the result (trust), sell the methodology (CAWDP). |
| **Pattern system becomes rigid** | Moderate | Moderate | Patterns are starting points, not cages. Every pre-fill can be overridden. The "I'm not sure" option triggers exploration, not a forced choice. |

---

## 12. Prototype Scope

**What to build first:**

| Item | Priority | Rationale |
|---|---|---|
| Intake + Pattern Matching | 1 | Entry point. Without this, nothing else works. |
| Identity Explorer (4 questions + pre-fills) | 2 | Determines 40-70% of the spec. |
| Boundary Mapper + Boundary Map output | 3 | Milestone 1. First valuable artifact. First exit point. |
| Specification Compiler (simplified 8-section output) | 4 | The primary deliverable. Even without Phases 4-6, a user can go from raw input → identity → boundaries → spec. |
| Architecture + Behaviour phases | 5 | Expand the spec from boundary-level to full depth. |
| Validation phase | 6 | Quality gate. Critical for trust but deferrable in early prototype. |

**What NOT to build first:**
- Complex visual canvas for Architecture (use structured cards + text for the prototype)
- Progressive autonomy timeline visualization (use text/table)
- Multi-session persistence (start with single session)
- Real-time collaboration (single user first)

---

*This is a living document. As the prototype is built and tested, it will evolve. The methodology says specifications should age — this one should too.*
```

---

**Document 2:** `./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md`

```markdown
# Retrospective: Agent Design Workflow — First Full Workflow Design

**Version:** 0.1  
**Date:** 2025  
**Context:** Team retrospective synthesizing perspectives from Business Strategy, AI UX Innovation, and Agentic Architecture on the first complete multi-agent workflow design.

---

## Part A: Cross-Cutting Strengths

Strengths identified across all three perspectives — Business, UX, and Architecture.

### A1. The Three-Layer Architecture (Rooms/Phases/Milestones)

This is the strongest structural decision in the entire design. It resolves a real type collision that occurred during the design process itself.

The three perspectives were each encoding different information types into the same artifact:
- **UX** was designing what the user FEELS (visual environments, interaction styles, cognitive modes)
- **Architecture** was designing what the workflow DOES (agent roles, processing stages, state machines)
- **Business** was designing what the user GETS (commercial milestones, exit points, value delivery)

These are not the same thing. They serve different audiences, evolve at different speeds, and should be designed by different principles. Conflating them — as most agent design tools do — creates the same type collision problem that the workflow is designed to solve in its own outputs.

**Separation allows independent evolution:** Add a phase without changing the room experience. Add a milestone without changing the processing logic. Redesign a room without touching the state machine. This is separation of concerns applied to workflow design, and it's rare in agentic system design where most people jump straight to "what does the agent do?" without first answering "what does the user experience?" and "what does the business deliver?"

**The mapping is clean:**
- Discovery = Phases 1-3 (Intake + Identity + Boundaries) → Milestone 1 (Boundary Map)
- Structure = Phases 4-5 (Architecture + Behaviour) → Milestone 2 (Allocation Map)
- Realisation = Phases 6-7 (Validation + Specification) → Milestones 3-4 (Operations Manual + Trust Ledger)

### A2. Pattern-First Entry

Instead of presenting a blank form or a linear questionnaire, the workflow starts by detecting what the user is trying to do and pre-filling 40-70% of the specification from a validated pattern.

This solves three problems simultaneously:
1. **Blank page paralysis** — the user doesn't start from nothing
2. **Type collision on input** — the user's raw input is immediately typed and structured
3. **Progressive disclosure** — the user only needs to override what matters, not specify everything

The pattern system is the "convention over configuration" principle from software architecture applied to agent design. The five validated patterns (Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner) aren't just templates — they encode accumulated design knowledge about what each type of agent needs.

**This is the hardest thing to replicate.** Anyone can build a form. The patterns require deep domain knowledge encoded in a structured, overridable way.

### A3. Identity-First Design (4 Identity Questions)

The decision to front-load identity and derive everything else from it is structurally sound:

1. **What IS this agent?** — essence, not behaviour
2. **What's its stance toward possibility?** — orientation (possibility/bridge/constraint)
3. **What would VIOLATE its identity?** — identity boundary
4. **What would it mean for this agent to be WRONG?** — failure mode as identity boundary in reverse

These four questions collapse the design surface. They determine 40-70% of the specification before a single task is defined. The identity questions are not just inputs — they're design engines. Everything else (boundaries, task map, behaviour rules) derives from them.

**The key insight:** starting with "what does this agent do?" produces a fundamentally different (and worse) specification than starting with "what IS this agent?" The orientation question alone prevents the possibility/constraint confusion that produces over-specified identities and under-specified boundaries.

### A4. Mirror + Specialists Architecture

The Mirror Agent is the surface layer — one agent the user talks to. Seven specialists are the engine — they do the work behind the scenes.

This is architecturally significant for several reasons:
- **Cognitive load reduction** — the user interacts with one agent, not seven. This is "one clear next step" applied to multi-agent orchestration.
- **Trust simplification** — the user builds trust with one companion, not seven strangers.
- **Authority boundary enforcement** — each specialist has a clear "what it NEVER does" boundary. The Mirror Agent doesn't need to enforce these — it routes to the right specialist, and the specialist enforces its own boundary.
- **Verification independence** — the Validator is structurally separate from the Architect. The user doesn't need to understand this — the Mirror Agent routes to the right specialist at the right time.

The Surface + Engine pattern is a general pattern for any multi-agent workflow where the user shouldn't manage agent interactions directly.

### A5. Every Milestone Is an Exit

The user can stop at any major phase boundary with a valuable, independently-usable artifact:
- Milestone 1: Boundary Map (30 minutes)
- Milestone 2: Allocation Map (half day)
- Milestone 3: Operations Manual (1-2 weeks)
- Milestone 4: Trust Ledger (ongoing)

This is progressive disclosure applied to commercial engagement. Each milestone produces something the user can take away and use immediately — with any vendor, any platform, any implementation team. There are no dead ends.

**This is also where the consulting architecture and product architecture align.** The Boundary Journey milestones (from the business strategy) map directly to the workflow exit points (from the architecture). This wasn't designed — it emerged. The fact that they aligned without planning is a signal that the three-layer architecture is structurally sound, not accidentally convenient.

### A6. Verification Independence

The Validator is a separate agent from the Architect, with a different class (Assessor vs Generator) and a different orientation (adversarial vs constraint-oriented).

This isn't just good practice — it's CAWDP's CC-1 (Verification Independence) applied to the workflow itself. The workflow practises what it produces: if the output spec requires verification separation, the workflow itself has verification separation.

### A7. Possibility Gradient as Architectural Force

The gradient from Discovery (possibility-oriented, expansive) through Structure (bridge, constructive) to Realisation (constraint-oriented, adversarial) isn't just a UX decision. It's about what the agents are ALLOWED to do at each stage.

The Identity Explorer is explicitly possibility-oriented — it opens space, reflects, never qualifies. The Architect is explicitly constraint-oriented — it builds from known inputs, never reopens possibility. If these orientations were swapped or blurred, the workflow would produce either over-constrained identities (can't explore what the agent could be) or under-constrained architectures (building on shifting ground).

**The possibility gradient is a structural constraint, not just a visual theme.** The visual environment, the interaction style, and the agent's tone should all shift to match — but more importantly, the agent's AUTHORITY shifts. The Discovery room has wider authority boundaries; the Realisation room has narrower ones.

### A8. Methodology Encoded in Structure

The workflow doesn't just TELL you about CAWDP — it STRUCTURALLY enforces it. You can't skip boundaries because they come before capabilities. You can't avoid identity because it determines everything downstream. You can't validate your own design because the Validator is a separate agent.

This is "convention over configuration" at the methodology level. The workflow makes the right thing the easy thing, and the wrong thing the structurally difficult thing. Users who follow the workflow are following CAWDP whether they know it or not.

---

## Part B: Key Learnings

### Learning 1: Type Collision Happened to Us in Our Own Design Process

The three team perspectives (UX, Business, Architecture) were each encoding different information types into the same design artifact. UX was designing feelings. Architecture was designing logic. Business was designing value delivery. These got conflated until the three-layer separation was imposed.

**This is type collision at the meta-design level.** The same problem the workflow is designed to solve in its outputs (17+ information types encoded as prose) occurred in the design process itself (3 different information types encoded in one design artifact).

**Implication:** Expect this pattern in every multi-stakeholder design process. The three-layer architecture (Experience/Logic/Value) is the type collision resolution at the meta-level.

### Learning 2: The Three-Layer Pattern (Experience/Logic/Value) Is a Genuine Architectural Discovery

This emerged from the design exercise, not from existing methodology. It's the same architectural insight as the Accretive Workspace (artefact-primary, views derived) applied to workflow design:

- **One workflow** (single source of truth)
- **Three surfaces** (different stakeholders see different views)
- **Derived views** (not separate artifacts)

CAWDP should codify this as a standard pattern for multi-agent workflow design: **Every multi-agent workflow has three layers (Experience, Logic, Value) that should be designed independently and mapped to each other.**

### Learning 3: The Methodology Validated Itself but Also Showed Its Limits

CAWDP predicted the right design order (identity → boundaries → architecture → behaviour → validation) and provided the structural skeleton (5-class taxonomy, authority boundaries, verification independence). But it didn't produce the room structure, the attention map, the pattern system, or the feeling cascade.

**CAWDP gives you WHAT and WHY; UX gives you HOW IT FEELS.** Both are required. Both operate at different layers. The methodology is the skeleton; the experience design is the flesh.

### Learning 4: The Specification Output Doesn't Cleanly Map to Contract Primitives

The 8-section specification (Identity, Boundaries, Task Map, Knowledge, Capabilities, Behaviour, Verification, Failure & Recovery) doesn't cleanly map to the 8 contract primitives (Contract, Principal, Schema, Guard, Budget, Invocation, Revert, Event).

Some primitives span multiple sections (Guard appears in Boundaries, Behaviour, and Verification). Some sections don't have a clear primitive (Task Map maps partially to Schema and partially to Invocation). This is a stakeholder surface problem — specification is for human readers, contracts are for system enforcement. The mapping needs explicit design.

### Learning 5: The Ambiguity Strategy Is Philosophically Clear but Operationally Thin

"Doubt defaults to the human" is the right principle. But the design doesn't specify:
- **What EXACTLY triggers doubt?** Is it a confidence score? A pattern match below threshold? A detected contradiction? All three?
- **How are options presented?** Ranked list? Visual comparison? Scenario-based explanation?
- **What happens on timeout?** Does the workflow pause indefinitely? Apply safe defaults after a period? Loop back?
- **What's the interaction between safe defaults and confidence?** If 30% of the spec is safe defaults, is that a 30% confidence spec? Or does each default have its own confidence level?

The principle is right. The operational mechanism needs design.

### Learning 6: The Pattern System Is Under-Specified

Five patterns are listed as pre-fill templates, but:
- **What happens when a user's needs don't match any pattern?** The document says "explore more deeply" but doesn't specify what that exploration looks like structurally.
- **What about hybrid compositions?** A project coordinator might be 60% Review Partner + 30% Multi-Lens Analyst + 10% Discovery Explorer. How does pattern matching handle blends?
- **How are patterns created and added?** The methodology says patterns are "pre-validated agent archetypes" — validated by whom? Through what process?

The pattern system is the entry point for most users. If it's too rigid, users feel constrained. If it's too loose, it provides no value. This needs more design work.

### Learning 7: The Harm-Capable Path Is Marked but Not Paved

The Boundary Mapper identifies harm-capable agents (agents whose output can cause external harm if accepted without review). But the workflow doesn't ACT differently because of it:
- Does a harm-capable agent trigger different downstream processing? (It should — verification should be more rigorous, progressive autonomy should be more conservative.)
- Does a harm-capable agent change the workflow's own behaviour? (Should the Mirror Agent adopt a more cautious tone?)
- How does the harm assessment feed into the Validation phase specifically? (The Validator should have explicit harm-capable checks, not just generic consistency checks.)

This is the same insight from the code reviewer CAWDP application — the first agent where output can cause external harm requires a new class of safeguard. The workflow flags it but doesn't yet pave the path.

### Learning 8: Specialist Agent Authority Boundaries Aren't Stress-Tested

Each specialist has a "what it NEVER does" boundary. But:
- **What happens when a boundary is tested?** The Identity Explorer "never decides identity" — but what if the user explicitly asks it to decide? Does it refuse? Redirect? Explain why it can't?
- **What happens when two specialists conflict?** The Architect says "build from known inputs" but the Identity Explorer says "open possibility." If they disagree about the same aspect, who wins?
- **What happens when a specialist can't process input?** The Intake Agent "never judges" — but what if the user provides explicitly contradictory requirements that can't be captured without judgment?

These are the same boundary stress-tests that CAWDP prescribes for any agent, but we haven't applied them to our own specialist agents yet.

### Learning 9: The Workflow Itself Hasn't Been CAWDP'd

This is the most important gap. The workflow designs agents through CAWDP principles, but it hasn't been designed THROUGH the same methodology. Specifically missing:

1. **No complementarity analysis** — which routing decisions require human judgment vs which can be automated?
2. **No FMEA** — what happens when the Intake Agent receives gibberish? When the Identity Explorer hits an infinite loop? When the Validator and Architect disagree? When the user leaves mid-session?
3. **No specification aging** — the patterns, safe defaults, and identity question templates are static. No mechanism for updating based on real-world use data.
4. **No cost budget** — seven specialist agents consuming tokens with pattern matching, validation loops, and potential re-runs. No per-phase or per-workflow cost tracking.
5. **No progressive autonomy for the workflow** — the output agents have shadow → advisory → supervised → autonomous paths, but the workflow treats the user as the same authority at every phase.
6. **No Mirror Agent routing logic** — we know it routes to specialists, but we don't know the routing rules.
7. **No error recovery specification** — happy paths and loop-back paths exist, but no failure recovery paths.
8. **No cognitive mode mapping operationalized** — the document lists modes per phase but doesn't specify what the actual interaction looks like.
9. **No coherence check designed** — we know what it does (flags gaps, contradictions, unconfirmed defaults) but not what it looks like or how the user interacts with it.
10. **No cost model** — token consumption per phase, total workflow cost, cost vs value analysis.

This isn't a criticism — it's the natural result of designing from three perspectives in one pass. But it means the workflow needs CAWDP applied to itself before it's production-ready.

### Learning 10: We Have Zero Validation with Real Users

Pattern selection, 4 identity questions, attention map, possibility gradient, 15-minute spec, and feeling cascade are all untested hypotheses. They're internally coherent and architecturally sound, but they've never been in front of a real person.

**The most important next step:** test Milestone 1 (Boundary Map) with 5 real people before expanding the workflow. This tests the fundamental assumption: can a non-technical user go from raw input to a usable boundary map in 30 minutes?

### Learning 11: The Visual/Feeling Layer Is Specified in Goal, Not Detail

"Discovery feels expansive" and "Realisation feels concrete" are design goals, not interaction specifications. The possibility gradient needs dedicated UX design work:

- What does "expansive" look like in the UI? More whitespace? Larger type? Fewer constraints visible?
- What does "concrete" look like? More structure? Smaller type? More constraints visible?
- How does the transition feel? Is it abrupt or gradual?
- Does the agent's tone shift too? (Yes, it should — but how specifically?)

The possibility gradient is specified as a structural constraint (what agents can do at each stage) but not as an experiential specification (what the user feels at each stage).

### Learning 12: The Coherence Check Is Described but Not Designed

We know what the coherence check should do (flag gaps, contradictions, unconfirmed defaults) but not what it looks like or how the user interacts with it. Consider two modes:

- **Live indicator** — always visible, never blocking. Shows overall spec health (settled/needs attention/requires input) at a glance.
- **Deep check** — triggered on demand or at milestone boundaries. Comprehensive review of all sections with specific findings.

The attention map and confidence map are two views of the same data:
- **Attention map** = UX view (settled/needs attention/requires input/not yet applicable)
- **Confidence map** = data view (high/medium/low confidence per spec section)

Both need visual design before implementation.

---

## Part C: Patterns to Codify

These patterns emerged from this design exercise and should be reusable for future multi-agent workflow designs.

### C1. Surface + Engine Pattern

**Pattern:** One user-facing agent (Mirror) routes to multiple back-office specialists. The user interacts with one agent; the work is distributed.

**When to use:** Any multi-agent workflow where the user shouldn't manage agent interactions directly. Applies whenever the specialist agents have different authority boundaries, orientations, or cognitive modes.

**Key constraint:** The Mirror Agent must never judge, decide, or filter. It reflects and routes. Authority boundaries belong to the specialists.

### C2. Pattern-First Entry

**Pattern:** Detect what the user is trying to achieve from their initial input. Match against known archetypes. Pre-fill 40-70% of the specification. User overrides what matters.

**When to use:** Any workflow serving non-expert users who face blank-page paralysis. Also applies when the design space is large but the common patterns are well-understood.

**Key constraint:** Patterns must be starting points, not cages. Every pre-fill must be overridable. The "I'm not sure" option must trigger genuine exploration, not a forced choice.

### C3. Milestone-as-Exit Pattern

**Pattern:** Every major phase boundary produces a standalone valuable artifact. The user can exit with value at any milestone.

**When to use:** Any workflow serving time-constrained users (which is all of them). Also applies when the output has multiple stakeholder surfaces (one artifact for the business owner, another for the implementation team).

**Key constraint:** Each milestone artifact must be independently valuable WITHOUT the rest of the workflow. The Boundary Map must be useful even if the user never completes the full spec.

### C4. Possibility Gradient Pattern

**Pattern:** The workflow starts in possibility (expansive, open, exploring) and tightens toward constraint (concrete, narrow, verifying). The visual environment, interaction style, and agent authority all shift to match.

**When to use:** Any creative-to-structured workflow (design, strategy, planning). Not appropriate for purely mechanical or purely exploratory workflows.

**Key constraint:** The possibility gradient must be a structural constraint, not just a visual theme. Agents in possibility-oriented phases have wider authority boundaries; agents in constraint-oriented phases have narrower ones. The shift must be felt, not just seen.

### C5. Verification Independence Pattern

**Pattern:** The agent that validates is always a different agent (different class, different orientation) from the agent that creates. Verification must be structurally separate, not just functionally separate.

**When to use:** Any multi-agent workflow producing specifications, decisions, or outputs that require quality assurance. Non-negotiable for workflows with compliance, safety, or trust implications.

**Key constraint:** The validator must never have designed what it's validating. Same-class validation is acceptable only when the class is inherently adversarial (e.g., a Review Partner validating its own work through self-review protocols).

### C6. Identity Before Behaviour

**Pattern:** Start with four identity questions (what IS it? orientation? violation? wrongness?) and derive everything else from those answers. Identity determines boundaries, boundaries determine capabilities, capabilities determine behaviour.

**When to use:** Any agent design workflow. The four identity questions collapse 40-70% of the design surface, making the rest tractable.

**Key constraint:** The identity questions must be asked BEFORE any capability or behaviour questions. If the user wants to start with "what should it do?", redirect to "what IS it?" first.

### C7. Methodology Encoded in Structure

**Pattern:** The workflow doesn't just teach the methodology — it structurally enforces it. You can't skip boundaries because they come before capabilities. You can't avoid identity because it determines everything downstream. You can't validate your own design because the validator is a separate agent.

**When to use:** Any workflow that embodies a methodology (not just any agent workflow). The methodology becomes the structural constraint, not just the instructional content.

**Key constraint:** The methodology must be correct enough to encode. If it's wrong, encoding it structurally makes it harder to change — so it needs to be validated before encoding.

---

## Part D: What We'd Do Differently

### D1. Start with Milestone 1 Only

The 77% Challenge IS Milestone 1 — a 30-minute session that produces a Boundary Map. The most important next step is testing this with 5 real people, not building the full 7-phase workflow.

**Why:** Everything else depends on Milestone 1 working. If non-technical users can't produce a usable boundary map in 30 minutes, the rest of the workflow doesn't matter. Validate the entry point before building the cathedral.

### D2. Reduce Specialist Count for Prototype

The full design has 7 specialist agents. The prototype should start with 4:
- Mirror Agent (surface)
- Identity Explorer (possibility)
- Boundary Mapper (bridge)
- Compiler (constraint)

Architecture, Behaviour, and Validation can be added after the core loop is validated. Each additional specialist adds complexity, token cost, and routing logic. Start minimal, expand when validated.

### D3. Make Possibility Gradient a Structural Constraint

"Discovery feels expansive" and "Realisation feels concrete" are design goals. For the prototype, make the possibility gradient enforceable at the agent level:

- The Identity Explorer MUST NOT receive feasibility constraints as input
- The Architect MUST NOT receive possibility-oriented prompts
- The Validator MUST NOT propose new design elements

Make the orientation boundaries agent-enforced, not just design intentions.

### D4. "15-Minute Agent Specification" as the Headline

The pattern-first + identity-first entry point should be THE headline, not a buried feature. "Go from zero to a complete agent specification in 15 minutes" is more compelling than "a 7-phase workflow for designing agents."

The 15-minute specification is the demo. The full workflow is the product. Sell the demo, deliver the product.

---

## Part E: Honest Assessment

The architecture is structurally sound. The three-layer separation (Rooms/Phases/Milestones), the Surface+Engine pattern (Mirror+Specialists), the identity-first entry point, the possibility gradient, and the milestone-as-exit structure are all genuine architectural contributions that would hold up under implementation.

But the architecture is also:
- **Unvalidated** — no real users have touched it
- **Under-specified in the interaction layer** — cognitive modes are listed but not designed
- **Incomplete in its own methodology** — the workflow hasn't been CAWDP'd
- **Thin on ambiguity handling** — the principle is right, the mechanism is missing
- **Missing error recovery** — happy paths exist, failure paths don't

The most important next step is not more design. It's testing Milestone 1 (Boundary Map) with 5 real people. Until a non-technical user can produce a usable boundary map in 30 minutes, everything else is theoretical.

The architecture is the skeleton. The experience design is the flesh. The validation is the proof. We have a good skeleton. We need flesh before we can claim proof.

---

*This retrospective captures the state of the design after the first complete synthesis. As the prototype is built and tested, these learnings will evolve — and some will be proven wrong. That's the point.*
```

---

Both documents are ready to save. Confirm the file paths:

1. **`./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md`** — Complete 12-section specification
2. **`./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md`** — Retrospective with 5 parts (Strengths, Learnings, Patterns, Differences, Assessment)

---

## Run 12 — unknown ✓ COMPLETED

*2026-04-27T07:14:43* · `glm-5.1:cloud` · `b6be5437...`

### Prompt

what are the strengths of this agent design workflow?
This is the first time we've designed a full workflow, have there been any learnings or insights?
Be sure to save the agent design workflow document above to the file system as well as the work product produced in any run. The document manager should process these files.

### Response

Great questions — let me have the team reflect on strengths and learnings, and get the document saved. Let me set all of this up in parallel.Excellent — all three reflections are in, plus the document save. Let me now save all artifacts to the file system and synthesize the findings.Now let me finalize everything.Here's a summary of what the team produced and learned:

---

## 📂 Artifacts Saved

| File | Description |
|---|---|
| `./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md` | Complete 12-section prototype design specification |
| `./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md` | Full retrospective: strengths, learnings, patterns, honest assessment |

---

## 🏛️ Strengths — 8 Cross-Cutting Themes

The team converged on these as the strongest design decisions:

1. **Three-Layer Architecture** — Rooms (experience), Phases (logic), and Milestones (value) are independent design surfaces that map to each other. This emerged from resolving type collision in our own process — not from theory.

2. **Pattern-First Entry** — Pre-filling 40-70% from validated archetypes solves blank-page paralysis, type collision on input, and progressive disclosure simultaneously.

3. **Identity-First Design** — Four questions collapse 40-70% of the design surface before a single task is defined. "What IS this agent?" produces fundamentally better specs than "what should it do?"

4. **Mirror + Specialists** — One user-facing agent, seven back-office specialists. The user never manages agent interactions.

5. **Every Milestone Is an Exit** — No dead ends. The Boundary Map is independently valuable at 30 minutes.

6. **Verification Independence** — The Validator is structurally separate from the Architect. The workflow practises what it produces.

7. **Possibility Gradient** — Discovery→Structure→Realisation isn't just visual; agent authority boundaries shift across phases.

8. **Methodology Encoded in Structure** — You *can't* skip boundaries or avoid identity. The methodology IS the structure, not a layer on top.

---

## 🔑 Key Learnings — What We'd Do Differently

The most important learnings from our first full workflow design:

1. **Type collision happened to us** — The three perspectives (UX, Business, Architecture) were encoding different information types into the same artifact until we separated them into three layers.

2. **The Three-Layer Pattern (Experience/Logic/Value) is a genuine architectural discovery** — this should be codified as a standard pattern for any multi-agent workflow design.

3. **The workflow itself hasn't been CAWDP'd** — it's missing complementarity analysis, FMEA, specification aging, cost budget, progressive autonomy for itself, Mirror routing logic, and error recovery. The meta-principle revealed this gap.

4. **Zero validation with real users** — the architecture is a strong hypothesis. The next step is testing Milestone 1 (Boundary Map) with 5 real people, not building more features.

5. **Start with Milestone 1 only** — the full 7-phase architecture is the right destination but the wrong starting point for a prototype. Build Intake → Identity → Boundaries → Boundary Map. Ship that. Test it.

The team's honest bottom line: **We have a structurally sound skeleton. We need flesh (interaction design) before we can claim proof (real user validation).**

---

## Run 13 — Agentic Expert ⚠️ ERROR

*2026-04-27T09:30:28* · `glm-5.1:cloud` · `934d3c79...`

### Prompt

We've gathered input from all three team members on designing an agentic workflow that produces agent design specs. Please synthesize the following three contributions into ONE unified, cohesive prototype design document.

The document should integrate the best ideas from each, resolve any tensions, and present a clear, actionable prototype that the team can hand off to an implementation workflow.

## Team Input Summary

### Business Strategist Key Points:
- Three target users: Daniel Kovacs (domain expert with blank-page problem), Sarah Chen (business owner needing verification), Developers (needing structured specs)
- Value prop: "Design spec is the product, methodology is the moat, implementation is the commodity, trust infrastructure is the category"
- Key risks: "Just another template" perception, over-engineering the workflow, platform-agnostic spec falling between stools, credibility gap, category creation difficulty
- Output strategy: One typed graph, many stakeholder views. Progressive engagement: Boundary Map (30 min) → Allocation Map (half day) → Operations Manual (1-2 weeks) → Trust Ledger (ongoing)
- Platform-agnostic: Spec describes WHAT and WHY, never WHICH TOOL. Test: could two different implementation teams on different frameworks produce functionally equivalent agents?

### AI UX Innovator Key Points:
- Three "Rooms": Discovery (expansive), Structure (constructive), Realisation (concrete)
- Pattern-first entry: Select archetype → pre-fill 40-70% → user overrides what matters
- 4 Identity Questions first (essence, orientation, violation, wrongness)
- Cognitive mode → input modality mapping (narrative=conversation, boundary=drag-sort, exploratory=cards, verification=scenarios, architectural=canvas, configurational=dials, evaluative=dashboard)
- Attention Map navigation (settled/needs attention/requires input/not yet applicable)
- Typed outputs (boundary map=visual, authority=cards, etc.)
- Single session + multi-session support. Every decision persistent and revisable.
- Mirror Agent as companion (reflects, never judges)
- 7 UX principles: pattern-first, identity-before-behaviour, possibility gradient, typed I/O, one clear next step, decisions revisable, feeling cascade

### Agentic Expert Key Points:
- 7 phases: Intake → Identity → Boundaries → Architecture → Behaviour → Validation → Specification
- Pattern: Planned Workflow with Human Gates (NOT ReAct)
- Human gates after: Intake, Identity, Boundaries, Validation
- Multi-agent workflow (not single agent): Intake Agent, Identity Explorer, Boundary Mapper, Architect, Validator, Compiler
- 8-section spec: Identity, Boundaries, Task Map, Knowledge Requirements, Capabilities, Behaviour Rules, Verification & Trust, Failure & Recovery
- 6 supporting artifacts: Boundary Map, Risk Register, Decision Log, Gaps & Assumptions Register, Implementation Readiness Checklist, Confidence Map
- Ambiguity strategy: "Doubt defaults to the human" — explore before assuming, make trade-offs visible, safe defaults with flags
- State machine with loop-back paths, skip paths for simple agents, exit paths at every gate
- The meta-principle: the workflow must practise what it produces

## Your Task:
Create a unified prototype design document that:
1. Integrates all three perspectives into a single coherent design
2. Resolves any tensions (e.g., the 3 "Rooms" from UX vs the 7 "Phases" from architecture — map them to each other)
3. Presents the workflow architecture, user journey, output artifacts, and key design principles as one unified story
4. Is structured as a prototype design spec that another workflow could use to implement this
5. Keeps it at design spec level — no implementation code or platform specifics

Make it clear, well-structured, and actionable. This is the deliverable the user asked for.

Save the complete Agent Design Workflow Prototype Design Specification (the unified document from task 1c250e41) to the file system at: ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

The document should contain the full unified specification as produced — all 12 sections including: What This Is, Three Users, Three-Layer Architecture, Seven Phases Detail, Specialist Agents, Design Specification Contents (8 sections), Supporting Artifacts, Handling Ambiguity/Conflicts/Gaps, State Machine, Design Principles, Risks and Mitigations, and Prototype Scope.

After saving, confirm the file path and that it was saved successfully.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from an agentic architecture perspective?** What patterns, structures, or architectural decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we learn about designing multi-agent workflows? What worked that we should repeat? What patterns emerged that we should codify? Where did the architecture reveal gaps we need to address in future workflow designs?

Be candid and specific. Draw on your architectural analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Save the following two documents to the file system:

1. The Agent Design Workflow Specification → ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

2. The team's retrospective on strengths and learnings → ./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md

For document 1, use the complete specification document as produced in task 1c250e41 (the unified 12-section spec).

For document 2, compile the three team retrospectives into one document with these sections:

## Retrospective: Agent Design Workflow — First Full Workflow Design

### Part A: Cross-Cutting Strengths (synthesized from all three perspectives)
- The Three-Layer Architecture (Rooms/Phases/Milestones)
- Pattern-First Entry
- Identity-First Design (4 Identity Questions)
- Mirror + Specialists Architecture
- Every Milestone Is an Exit
- Verification Independence
- Possibility Gradient as Architectural Force
- Methodology Encoded in Structure

### Part B: Key Learnings
1. Type collision happened to us in our own design process
2. The three-layer pattern (Experience/Logic/Value) is a genuine architectural discovery
3. The methodology validated itself but also showed its limits
4. The specification output doesn't cleanly map to contract primitives
5. The ambiguity strategy is philosophically clear but operationally thin
6. The pattern system is under-specified
7. The harm-capable path is marked but not paved
8. Specialist agent authority boundaries aren't stress-tested
9. The workflow itself hasn't been CAWDP'd (10 specific gaps)
10. We have zero validation with real users
11. The visual/feeling layer is specified in goal, not detail
12. The coherence check is described but not designed

### Part C: Patterns to Codify
1. Surface + Engine pattern
2. Pattern-first entry
3. Milestone-as-exit
4. Possibility gradient
5. Verification independence
6. Identity before behaviour
7. Methodology encoded in structure

### Part D: What We'd Do Differently
- Start with Milestone 1 only
- Reduce specialist count for prototype
- Make possibility gradient a structural constraint
- "15-minute spec" as the headline, not a feature

### Part E: Honest Assessment
The architecture is structurally ambitious and emotionally intelligent, but unvalidated and under-specified in the interaction layer. The next step isn't more design — it's testing Milestone 1 with 5 real people.

Save both files and confirm paths.

Design the complete workflow architecture for Milestone 1 ONLY: the 30-minute session that takes a user from raw input to a Boundary Map.

## Context & Learnings to Apply

This is the prototype-first approach based on our retrospective learnings:

**What we learned to do differently:**
1. Start with Milestone 1 only — validate the entry point before building the cathedral
2. Reduce specialist count: Mirror + Identity Explorer + Boundary Mapper + Compiler (4 agents, not 7)
3. Make possibility gradient a structural constraint, not just a visual theme
4. The "15-minute specification" should be THE headline — go from zero to a Boundary Map in 15-30 minutes
5. The ambiguity strategy needs operational mechanisms (what triggers doubt, how options are presented, timeout behavior)
6. The pattern system needs: hybrid composition support, "no match" path, pattern creation process
7. Specialist authority boundaries must be stress-tested (what happens when tested, when two specialists conflict, when input can't be processed)
8. Need Mirror Agent routing logic (when routes where, what if unsure)
9. Need error recovery paths (not just happy paths and loop-backs)
10. The workflow needs CAWDP applied to itself (complementarity analysis, FMEA, cost budget)

**What we keep from the original design:**
- Three-layer architecture (Rooms/Phases/Milestones) — but only the Discovery room for now
- Pattern-first entry with 5 archetypes
- Identity-first: 4 questions before anything else
- Boundaries before capabilities
- Doubt defaults to the human (now with operational mechanisms)
- Platform-agnostic specification
- Every milestone is an exit (this IS the exit)
- Mirror + Specialists (reduced set)

## What to Produce

Design a complete, implementable workflow specification for Milestone 1 that includes:

### 1. Scope & Boundaries
- What's IN Milestone 1 (precise phase list, agent list, output)
- What's OUT and deferred to later milestones
- Success criteria: what does a "good" Boundary Map look like?

### 2. Agent Architecture (4 agents)
- **Mirror Agent** — surface layer, routing logic (SPECIFY the routing rules — when does it route to Identity Explorer vs Boundary Mapper? What if unsure? What if two specialists could handle it?)
- **Identity Explorer** — the 4 identity questions, with full specification of pre-fill behavior, exploration mode, and "I'm not sure" handling
- **Boundary Mapper** — deriving never-rules, authority boundaries, reversibility classification, harm assessment
- **Compiler** — assembling the Boundary Map output

For EACH agent, specify:
- Class and orientation
- Authority boundary (what it NEVER does) — STRESS-TESTED: what happens when the boundary is tested?
- Input schema and output schema
- Failure modes and recovery paths
- Cost budget (token estimates per interaction)

### 3. State Machine
- Complete state machine for Milestone 1 (from raw input to Boundary Map output)
- ALL paths: happy path, loop-back paths, error recovery paths, exit paths
- Human gates: what the user sees and decides at each gate
- Skip paths: can a user skip Identity if they already have it? Can they jump to Boundaries?

### 4. Pattern System (Operational Specification)
- The 5 patterns with their pre-fill templates for the 4 identity questions + boundary defaults
- Hybrid composition: how to handle 60% Pattern A + 40% Pattern B
- "No match" path: what happens when no pattern fits
- "I don't know what I want" path: exploratory mode
- Pattern confidence thresholds and what they trigger

### 5. Ambiguity & Doubt Protocol (Operational)
- What EXACTLY triggers doubt (confidence score, pattern match threshold, contradiction detection)
- How options are presented to the user (format, comparison, consequences)
- Timeout behavior: what happens if the user doesn't respond
- Safe defaults: which defaults apply when, and how they're flagged
- The interaction between safe defaults and confidence levels

### 6. Error Recovery
- What happens when: user provides gibberish, user provides contradictory input, user leaves mid-session, agent can't process input, two agents disagree, pattern match fails entirely
- For each: detection, recovery action, user communication

### 7. Output Specification
- The Boundary Map: exact structure, format, and content
- What makes a Boundary Map "complete" vs "partial"
- How confidence levels are shown
- How safe defaults are visually distinct from user decisions
- The platform-agnostic test applied to the Boundary Map itself

### 8. Cost Model
- Token estimates per agent per interaction
- Total cost per workflow run (happy path, with loops, with errors)
- Cost vs value analysis: is the Boundary Map worth the compute cost?

### 9. CAWDP Applied to This Workflow
- Complementarity analysis: which decisions require human judgment vs can be automated
- FMEA: failure modes and effects for each agent and each phase
- Specification aging: when should this Milestone 1 design be reviewed?

### 10. Implementation Readiness
- What a developer needs to build this
- Dependencies and prerequisites
- What can be hardcoded vs what needs to be configurable
- Testing strategy: how to validate Milestone 1 works

Be precise, operational, and implementable. This isn't a vision document — it's a build spec.

### Response

upstream request timeout (status code: 504)

---

## Run 14 — AI UX Innovator ⚠️ ERROR

*2026-04-27T09:30:29* · `glm-5.1:cloud` · `e1b22cbb...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent that guides users through defining what their agent should do, and then produces a complete design specification.

Please provide your UX perspective on:
1. What is the ideal user journey through this workflow? (e.g., conversational intake, structured form, iterative refinement)
2. What inputs should the user provide, and how should they be gathered? (e.g., goals, constraints, persona, domain context)
3. How should the workflow present its outputs and artifacts back to the user?
4. What feedback loops or iteration points should exist? (e.g., reviewing drafts, refining decisions)
5. How do we make this accessible to both technical and non-technical users?
6. What does the interaction pattern look like — is it a single session or multi-session?

Focus on the user experience design, not the technical architecture of the agent itself.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from a UX perspective?** What interaction patterns or design decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we discover about designing agentic workflows vs. traditional UIs? What patterns should we carry forward? Where did the design reveal gaps or tensions we need to address?

Be candid and specific. Draw on your UX analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Design the complete interaction layer for Milestone 1: the 30-minute session that takes a user from raw input to a Boundary Map.

## Context

This is the UX design for the prototype-first Milestone 1, based on our retrospective learnings:

**What we learned:**
1. The visual/feeling layer is specified in goal, not detail — "Discovery feels expansive" is a goal, not a spec
2. The coherence check is described but not designed
3. "Same journey, language toggle" underestimates cognitive load difference between Sarah Chen (business owner) and Daniel Kovacs (domain expert)
4. The attention map and confidence map are two views of the same data but haven't been designed
5. Cognitive modes are listed but not operationalized
6. We have zero validation — this needs to be testable

**The two primary users for Milestone 1:**
- **Daniel Kovacs** (domain expert) — knows his domain, blank page problem, needs guided design
- **Sarah Chen** (business owner) — boundary & verification problem, 30-minute session, needs a clear line

## What to Produce

### 1. The Discovery Room — Visual & Experiential Specification
Milestone 1 happens entirely in the Discovery room. Design what it actually looks and feels like:
- Layout: what's on screen at each phase (Intake, Identity, Boundaries)
- Visual atmosphere: what "expansive, possibility-oriented" looks like specifically (whitespace, type, color, animation)
- How the room FEELS different from Structure and Realisation (even though those aren't built yet)
- Transitions: how the experience shifts as the user moves from Intake → Identity → Boundaries
- The Mirror Agent's presence: how does the companion feel? Chat? Cards? Both? Voice?

### 2. Intake Interaction Design
- How the user provides raw input (text box? voice? guided questions? all three?)
- The pattern match reveal: how does the user see which pattern was detected?
- What "high confidence match" looks like vs "low confidence" vs "no match"
- The human gate: "Here's what I understood. Is this right?" — what does this screen look like?

### 3. Identity Interaction Design (4 Questions)
This is the most important interaction — it determines 40-70% of the Boundary Map:
- How each of the 4 questions is presented (conversation? cards? both?)
- Pre-fill display: how the user sees pattern defaults with "Why this answer?" tooltips
- Override interaction: how does the user change a pre-filled answer?
- "I'm not sure" mode: what happens when triggered? What does exploration look like?
- The human gate: "Is this the right agent?" — confirmation screen
- Timing: how long should this take? (Target: 5-10 minutes for pattern-matched users, 10-15 for explorers)

### 4. Boundaries Interaction Design
- The drag-sort boundary allocation (human does / agent does / system does) — how it works
- Never-rules display: derived from identity violation — how are they shown?
- Authority boundaries: the "can decide" vs "can only prepare" distinction — interaction
- Reversibility classification: how the user sees and adjusts this
- Harm assessment: the "can this agent cause harm?" moment — design it
- The human gate + Milestone 1 exit: "Are these the right lines?" + Boundary Map preview

### 5. The Boundary Map Output
- What the Boundary Map looks like as a deliverable (single-page visual)
- How confidence levels are shown (high/medium/low per boundary)
- How safe defaults are visually distinct from user decisions
- Export options: PDF? Image? Editable document?
- The "take this to any vendor" moment — how does the user feel ownership?

### 6. Attention Map & Coherence Check
Design the two feedback mechanisms:
- **Attention map** (always visible): settled / needs attention / requires input / not yet applicable — how it looks, where it sits, how it updates
- **Coherence check** (on-demand + at gates): what triggers it, what it shows, how the user interacts with findings

### 7. Error & Recovery Interactions
- What does "I can't process this" look like from the Mirror Agent?
- What does "I'm not sure which specialist to use" look like?
- What does "you provided contradictory information" look like?
- Session interruption: what does "welcome back, here's where you were" look like?

### 8. Mobile & Accessibility
- How does Milestone 1 work on mobile? (Sarah Chen might do this on her phone between meetings)
- What accessibility considerations are critical for a 30-minute guided session?
- Dark mode considerations for the Discovery room

### 9. Testable Hypotheses
List the specific UX hypotheses this design makes, so they can be validated with real users:
- "A pattern-matched user can complete the 4 identity questions in 5-10 minutes"
- "The drag-sort boundary allocation is intuitive for non-technical users"
- etc.

Be specific enough that a designer could create wireframes from this spec.

### Response

Internal Server Error (ref: b9c25d37-52f0-466d-98b2-82dc349cdbcf) (status code: 500)

---

## Run 15 — Business strategist ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `2a11ab1e...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow itself is an agent — it takes user requirements/goals as input and produces a complete design specification (not implementation) that another workflow could then use to build the agent on any platform.

Please provide your strategic analysis covering:
1. Who are the target users and what problem does this solve for them?
2. What's the value proposition compared to manually writing a design spec or jumping straight to implementation?
3. What are the key business risks or considerations?
4. What should the workflow's output artifacts be from a strategic/stakeholder perspective (e.g., design spec, persona docs, risk assessment)?
5. Any strategic considerations about platform-agnostic design specs

Keep the focus strategic — not technical implementation details.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from a strategic/business perspective?** What makes it defensible, valuable, and differentiated?

2. **What were the key learnings or insights from this being our first full workflow design?** What surprised you? What would you do differently? What patterns emerged that we should carry forward?

Be candid and specific. Draw on your strategic analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Design the commercial model and validation strategy for Milestone 1: the 30-minute Boundary Map session.

## Context

From the retrospective, these key learnings apply to the commercial and validation strategy:

1. The consulting-to-product mapping was emergent — the Boundary Map ($0 or $495) is the 77% Challenge artifact
2. The "15-minute specification" should be THE headline — it's the adoption hook
3. Every milestone is an exit — this IS the exit for Milestone 1
4. We have zero validation — the next step is testing with real users
5. The Boundary Map is free — it builds trust before asking for payment
6. Credibility gap before case studies is a high-likelihood risk
7. "Just another template" perception is a fatal risk if we don't differentiate

## What to Produce

### 1. The 77% Challenge as Product
- How the Boundary Map session becomes a 30-minute product experience
- The "free Boundary Map" as trust-builder: what's free vs what's paid?
- What happens AFTER the Boundary Map — the natural escalation to Milestone 2 (Allocation Map)
- The "take this to any vendor" moment: how it builds trust in CAWDP specifically
- Pricing: what's the model? Free Boundary Map → paid Allocation Map? Freemium with limits?

### 2. The "15-Minute Boundary Map" Pitch
- The headline and positioning
- The demo flow: what does a 15-minute Boundary Map session look like as a sales demo?
- What makes this DIFFERENT from filling in a template? How do we prevent "just another form" perception?
- Key differentiators to communicate: pattern-first, identity-questions, methodology-encoded-in-structure

### 3. Validation Strategy
- The 5-person test: who, what, how, what we're testing
- Specific hypotheses to validate (from the UX design + architecture design)
- Success criteria: what does "Milestone 1 works" look like?
- Failure criteria: what would make us rethink the approach?
- What to measure: time, completion rate, confidence, Boundary Map quality, user satisfaction

### 4. The Boundary Map as Deliverable
- What makes it independently valuable? Why can someone take it to any vendor?
- How it positions CAWDP as the methodology, not just the tool
- The upgrade path: Boundary Map → Allocation Map → Operations Manual
- How the Boundary Map creates demand for the full workflow

### 5. Go/No-Go Criteria
After the 5-person validation:
- What results would tell us to proceed to Milestone 2?
- What results would tell us to iterate on Milestone 1?
- What results would tell us to fundamentally rethink the approach?

### 6. Competitive Positioning
- How does this compare to existing agent builders (ChatGPT custom GPTs, Coze, etc.)?
- What's the unique value that no template or form can provide?
- How to position: methodology tool? Trust engine? Design partner?

Be specific and actionable. This should be a commercial plan we can execute.

### Response

# Milestone 1: Commercial Model & Validation Strategy

---

## 1. The 77% Challenge as Product

### The Session Format

The 77% Challenge is a **30-minute guided session** that produces a one-page Boundary Map. In the validation phase, Peter delivers it live (consulting). In the product phase, the workflow delivers it (automated).

The session has three movements:

| Minutes | What Happens | What the User Experiences |
|---|---|---|
| 0-5 | **Intake** — "What workflow are we mapping?" and "What matters most to you?" | Being heard. Not being sold to. |
| 5-20 | **Discovery** — Four identity questions + boundary mapping | Their expertise being reflected back. Structure emerging from their knowledge. |
| 20-30 | **Boundary Map production** — Three-column map, percentage split, value statement | Relief. Something concrete they can point to. |

**Critical: the session feels like a conversation, not a form.** The Mirror Agent (or Peter, in the consulting version) asks questions, reflects what it hears, and proposes boundaries. The user's expertise is the fuel; the methodology is the engine. The user never sees the engine.

### Free vs Paid: The Freemium Boundary

The principle: **the Boundary Map is free. The architecture behind it is paid.**

| What's Free | What's Paid |
|---|---|
| The Boundary Map (one page, three columns) | Allocation Map (who does what, failure modes, recovery paths) |
| The value statement ("Your value is in X, not Y") | Operations Manual (deployment governance, progressive autonomy schedule) |
| "Take this to any vendor" portability | Trust Ledger (ongoing monitoring data, override analysis) |
| One workflow mapped | Additional workflows, deeper analysis, implementation support |

**Why this works commercially:** The Boundary Map answers the question everyone has ("where's the boundary?") but immediately reveals the question they didn't know they had ("who does what at the boundary?" and "what happens when it fails?"). The free artifact creates its own demand for the paid artifacts. You don't upsell — the Boundary Map makes the next question unavoidable.

**The "take this to any vendor" moment:**

This is the trust-building mechanism. At minute 28, the user gets a one-page document that works with ANY AI vendor. The line is:

> "This Boundary Map is yours. Take it to any vendor — tell them to build within these boundaries. You don't need to come back to us. But if you want to know who should do what at each boundary, what happens when things fail, and how to verify it's working — that's what we do next."

Three things happen simultaneously:
1. **Trust**: We just gave them something valuable that works without us. That's rare.
2. **Differentiation**: No vendor does this. Vendors lock you in. We give you the map to navigate.
3. **Demand creation**: "Who does what at the boundary?" is now an active question in their mind. They didn't have it before. They have it now.

### Natural Escalation: Boundary Map → Allocation Map

The escalation isn't a sales pitch. It's a question the Boundary Map makes unavoidable.

The Boundary Map shows three columns: **You / AI / System**. At the bottom, a value statement: "Your value is in judgment on ambiguous clauses, not in searching for them." The natural next question is:

- "Okay, so AI handles the searching. But what KIND of AI? What should it NEVER do with what it finds? And what happens when it finds something that looks wrong but isn't — or looks right but isn't?"

That's the Allocation Map. The user isn't being sold to — they're asking a question the Boundary Map legitimately raised. The answer costs $495-$795 for a half-day session, or is included in a workshop.

**The pricing model:**

| Tier | Price | What You Get |
|---|---|---|
| **77% Challenge** | Free | 30-min Boundary Map session + one-page map |
| **Boundary Workshop** | $495 | Half-day: Boundary Map + Allocation Map + failure & recovery register |
| **Full Boundary Journey** | $1,495-2,500 | Full-day: Boundary Map + Allocation Map + progressive autonomy roadmap + cost-benefit analysis |
| **Operations Manual** | $5,000-25,000 | 1-2 weeks: full governance infrastructure |

The free session is the 77% Challenge. The $495 workshop is the first paid product. Everything above that is consulting.

**Important:** The 77% Challenge is not a "free trial." It's a standalone product that delivers real value. The fact that it creates demand for deeper engagement is a feature, not a trick.

---

## 2. The "15-Minute Boundary Map" Pitch

### The Headline

**"Know where the boundary is in 15 minutes."**

Not "AI agent design tool." Not "agentic workflow methodology." Not "trust infrastructure for AI." The boundary. In 15 minutes. That's what people actually want.

Supporting line: **"We don't tell you what AI can do. We tell you where it should stop — and where your judgment stays."**

### The Demo Flow (5 minutes)

This is what you show at a Law Society event, a startup pitch, or a LinkedIn video. Five minutes, one real example.

| Minute | What Happens | What They See |
|---|---|---|
| 0-1 | "Sarah runs a 6-person commercial law firm. She reviews every document that leaves the firm. She IS the bottleneck." | A person they recognise. Possibly themselves. |
| 1-2 | "Let's map her document review workflow. Three tasks: initial review, clause analysis, final approval." | Three task cards appearing. |
| 2-3 | "Four questions: What IS this agent? What would VIOLATE it? What's its stance toward possibility? What would make it WRONG?" | Identity questions filling in. "Never provides legal advice. Never finalises without human review." |
| 3-4 | "Here's the Boundary Map." | One page, three columns: Sarah keeps final approval + ambiguous clause judgment. AI handles initial review + pattern matching. System enforces the boundary. |
| 4-5 | "Value statement: Sarah's value is in judgment on ambiguous clauses, not in searching for them. She just got 30% of her time back. And she can take this map to any vendor." | Relief. The aha moment. "This is what I've been looking for." |

### What Makes This Different from Filling in a Template

This is the fatal risk, so let's be specific about how it's different:

| Template Approach | Boundary Map Approach |
|---|---|
| Blank page: "Describe your workflow" | Pattern matching: "You're a commercial law firm? Here's what that typically looks like." |
| "List your tasks" → user guesses | "Here are the typical tasks for this domain" → user confirms, modifies, adds |
| "What should AI do?" → user doesn't know | "What should AI NEVER do?" → user knows immediately |
| Output: filled form | Output: typed knowledge object with epistemic metadata, authority boundaries, and failure modes |
| One format, one audience | One graph, six stakeholder surfaces |
| Skippable sections | Quality gates: you can't proceed without answering identity questions |
| Static document | Living artefact: ages, evolves, connects to downstream specifications |

**The key differentiator is invisible:** the methodology is encoded in the *order* of questions, the *types* of answers, and the *quality gates* between sections. The user experiences a conversation, not a form. But the conversation is structured by CAWDP — they're doing the methodology without knowing it.

### Three Key Differentiators to Communicate

1. **"Boundaries before capabilities"** — We start with what the agent should NEVER do. Every vendor starts with what it CAN do. We start from the other direction because that's where the risk lives.

2. **"Pattern-first, not blank-page"** — You don't face a blank page. You start with 40-70% of the answer and modify what matters. This is what 15-minute specs make possible.

3. **"Take this to any vendor"** — We're the only people who give you a map that works without us. That's not generosity — it's confidence in the methodology.

---

## 3. Validation Strategy

### The 5-Person Test

**Who:**

Five professional services principals who match the Sarah Chen profile:
- Law firm or accounting practice
- 3-15 people
- The principal is both decision-maker AND practitioner
- They've tried at least one AI tool (and been underwhelmed)
- Melbourne or Sydney (Peter's network: RMIT, Vibe Club, startup ecosystem, Rifadh's connections)

**Screening criteria:**
- Owns the boundary problem (reviews everything themselves)
- Can name a specific workflow they'd want mapped
- Has 30 minutes
- Is the principal, not a delegate

**How:**

30-minute video call. Peter facilitates (consulting version). Record the session (with permission). Produce the Boundary Map live. Send it as PDF within 24 hours.

**What we're testing — six hypotheses:**

| # | Hypothesis | How We Test | What We Measure |
|---|---|---|---|
| H1 | The Boundary Map delivers **relief** — a specific feeling, not just information | Post-session question: "How do you feel about this workflow now compared to 30 minutes ago?" + observed body language | 4/5 report relief or clarity they didn't have before |
| H2 | 30 minutes is sufficient for a meaningful Boundary Map | Timer on session | Average completion under 30 min; map has 5+ tasks mapped; 3+ columns populated |
| H3 | Pattern-first entry reduces blank-page paralysis | User never asks "what do you mean?" about tasks; they confirm/modify, not invent from scratch | Pattern match on first attempt; under 5 minutes to task confirmation |
| H4 | The Boundary Map is independently valuable | Post-session question: "Would you use this map without doing anything else?" + "Would you show this to a colleague?" | 4/5 say yes to both |
| H5 | The Boundary Map creates demand for the Allocation Map | Post-session question: "What question does this map NOT answer that you now need answered?" | 3/5 spontaneously ask about who does what / what happens when it fails |
| H6 | "Take this to any vendor" builds trust in CAWDP specifically | Post-session question: "How does it change your view of us that this map works without us?" | 4/5 report increased trust |

### Measurement Instruments

**During the session:**
- Timer (minutes to first task confirmed, minutes to boundary map complete)
- Observer notes (where did the user struggle? Where did they light up? What did they push back on?)
- Questions asked by user (type and count — more questions about boundaries = good; more questions about "what does this mean?" = bad)

**Post-session (5-minute survey):**
1. "Before this session, how clear were you about where AI should handle work in your practice?" (1-5)
2. "After this session, how clear are you?" (1-5)
3. "How do you feel about this workflow now compared to 30 minutes ago?" (open text)
4. "Would you use this Boundary Map as-is, without further sessions?" (Yes/No/Maybe + why)
5. "Would you show this to a colleague?" (Yes/No/Maybe)
6. "What question does this map NOT answer that you now need answered?" (open text)
7. "What was the most valuable moment in this session?" (open text)
8. "How does it change your view of us that this map works with any vendor?" (open text)

**One week later (follow-up email):**
1. "Have you used the Boundary Map since the session?" (Yes/No)
2. "Have you shared it with anyone?" (Yes/No)
3. "What's your biggest question about deploying AI in your practice now?" (open text)

### Success Criteria

**"Milestone 1 works" looks like:**
- 4/5 participants report relief or clarity (H1)
- Average session time under 30 minutes (H2)
- Pattern match works on first attempt for 4/5 participants (H3)
- 4/5 say the Boundary Map is independently useful (H4)
- 3/5 spontaneously ask about the next question (H5)
- 4/5 report increased trust from the vendor-agnostic moment (H6)

**The single most important metric:** Post-session clarity gain (Q1 → Q2 delta). If people move from 2/5 to 4/5, the methodology is working. If they move from 2/5 to 3/5, it's partially working. If they stay at 2/5, we have a problem.

### Failure Criteria

**What would make us rethink:**
- 0-1/5 report relief — the methodology doesn't deliver the core feeling
- Average session time over 45 minutes — 30 minutes was the wrong promise
- Nobody asks the follow-up question — the Boundary Map doesn't create demand
- 3+ participants say "this is just another form" — the fatal risk materialized
- The Boundary Map gets rated "too generic" by 3+ — it's not specific enough to be valuable

---

## 4. The Boundary Map as Deliverable

### What Makes It Independently Valuable

The Boundary Map is one page, three columns:

```
┌─────────────────┬──────────────────┬──────────────────┐
│     YOU         │       AI         │     SYSTEM       │
│                 │                  │                  │
│ Final approval  │ Initial review   │ Boundary         │
│ of all output   │ of incoming      │ enforcement      │
│                 │ documents        │ (blocks AI from  │
│ Judgment on     │ Pattern matching │ crossing into    │
│ ambiguous       │ against known    │ your column)     │
│ clauses         │ risk patterns    │                  │
│                 │                  │ Audit trail      │
│ Client          │ Draft clause     │ (records every   │
│ relationship    │ comparisons      │ AI action for    │
│ management      │                  │ your review)     │
│                 │ Flag anomalies   │                  │
│ Ethical         │ for your         │ Progressive      │
│ decisions       │ attention        │ autonomy         │
│                 │                  │ schedule         │
├─────────────────┼──────────────────┼──────────────────┤
│      35%        │       40%        │       25%        │
├─────────────────┴──────────────────┴──────────────────┤
│ YOUR VALUE: Judgment on ambiguous clauses, not        │
│ searching for them.                                   │
└───────────────────────────────────────────────────────┘
```

**Why it's independently valuable:**

1. **It names the boundary.** Most people have a vague sense that "some things AI should do and some things it shouldn't" but have never seen it made concrete for THEIR workflow.

2. **It's specific to their practice.** Not "law firms should use AI for research" — "Chen Legal should use AI for initial document review and pattern matching, and Sarah should keep final approval, ambiguous clause judgment, and client relationship management."

3. **It's vendor-agnostic.** The map doesn't mention any tool. Any AI vendor can build within these boundaries. Any implementation team can work from it. This makes it a portable asset, not a platform dependency.

4. **It has a value statement.** The bottom line — "Your value is in X, not Y" — is the sentence people remember. It reframes their professional identity from "I do everything" to "I do what matters." That's not just information — it's relief.

5. **It's shareable.** One page. Laminated desk card. PDF. It goes on the wall. It goes to the insurer. It goes to the team. It becomes the reference document for "how we do AI here."

### How It Positions CAWDP

The Boundary Map is the gateway drug to the methodology — and that's not a flaw, it's the design.

The user doesn't see CAWDP. They see a conversation and a one-page map. But the map was produced by CAWDP: the pattern matching, the identity questions, the boundary-before-capability order, the quality gates, the verification independence. The methodology is invisible because it's structural.

**The positioning trick:** The user thinks "I got a Boundary Map." What they actually got is proof that the methodology works. When they want the Allocation Map, they're not buying "more methodology" — they're buying "more of whatever produced that thing I already trust."

### The Upgrade Path

| From | To | Trigger | What Changes |
|---|---|---|---|
| Boundary Map | Allocation Map | "Who does what at the boundary?" | Tasks get roles, authority boundaries, failure modes |
| Allocation Map | Operations Manual | "How do I deploy this safely?" | Progressive autonomy schedule, verification protocols, governance |
| Operations Manual | Trust Ledger | "Is it working? How do I prove it?" | Override rates, verification outcomes, cost variance data |
| Trust Ledger | Ongoing engagement | "What's changed? What needs updating?" | Specification aging, capability drift, pattern refinement |

Each transition is driven by a question the previous artifact legitimately raises — not by a sales pitch.

### How the Boundary Map Creates Demand for the Full Workflow

The Boundary Map is the first 15 minutes. The full workflow is the complete specification. The map shows the user that the methodology works — that someone can actually draw the line in 30 minutes. The full workflow draws every line, assigns every role, maps every failure, and builds every protocol.

The demand mechanism: **the Boundary Map proves the methodology is real. The full workflow delivers the methodology's full power.** The user wants the full power because they've seen it work at 15%.

---

## 5. Go/No-Go Criteria

### Proceed to Milestone 2 (Allocation Map) if:

- ✅ 3+ participants report relief/clarity (H1 ≥ 3/5)
- ✅ 2+ spontaneously ask the follow-up question about who does what or what happens when it fails (H5 ≥ 2/5)
- ✅ Boundary Map rated independently valuable by 3+ (H4 ≥ 3/5)
- ✅ Average session time under 35 minutes (H2 within range)
- ✅ No participant says "just another form/template" (fatal risk avoided)

**What this tells us:** The methodology works when Peter delivers it. The core value proposition (relief through boundary clarity) is real. The Boundary Map creates demand for deeper engagement. Proceed to designing the Allocation Map session and testing it.

### Iterate on Milestone 1 if:

- ⚠️ Relief is present but inconsistent (2/5 report it)
- ⚠️ Session time is 30-45 minutes (close but not meeting the promise)
- ⚠️ Boundary Map is valuable but not driving escalation (0-1 ask the follow-up question)
- ⚠️ Pattern matching doesn't work cleanly (users need to invent tasks from scratch)
- ⚠️ One participant says "just another form" but others don't

**What this tells us:** The methodology is partially working. The core insight (boundary clarity delivers relief) might be right but the delivery is wrong. Iterate on: session flow, pattern library, question ordering, or the 30-minute format itself. Do another 5 sessions before deciding.

### Fundamentally Rethink if:

- ❌ 0-1 participants report relief (the core value proposition fails)
- ❌ 3+ participants say "just another template/form" (the fatal risk materialized)
- ❌ Nobody asks the follow-up question AND nobody would use the map independently (no demand creation)
- ❌ The Boundary Map is rated "too generic" by 3+ (specificity is the differentiator — if it's not specific, it's not differentiated)
- ❌ Average session time over 45 minutes (the promise is broken)

**What this tells us:** The core assumption is wrong. Either the 77% problem isn't a methodology gap, or boundary clarity isn't the relief people need, or 30 minutes isn't enough to deliver it. Rethink the value proposition, not just the session format.

**The one result that should stop us completely:** If 3+ participants say "I don't see how this is different from what I could do myself." That means the methodology isn't creating value beyond what a smart person with a whiteboard could do. CAWDP's defensibility depends on the methodology being non-obvious in practice.

---

## 6. Competitive Positioning

### The Competitive Landscape

| Competitor Type | What They Do | What They Don't Do | Our Opening |
|---|---|---|---|
| **ChatGPT Custom GPTs** | Let you BUILD an agent by describing it | Help you DESIGN what it should do before building; define boundaries, failure modes, verification | "You built it in 5 minutes. How do you know it's doing the right things? How do you verify it? Where should it stop?" |
| **Coze / Agent builders** | Visual agent building tools | Design methodology; boundary analysis; failure mode identification; verification protocols | "Great tools. Wrong starting point. Start with the boundary, not the builder." |
| **Big 4 "AI Governance Frameworks"** | Principles, policies, audit checklists | Actual methodology; repeatable process; typed outputs; quality gates; progressive autonomy | "Principles aren't production. You have a policy. We have a process." |
| **AI vendor governance docs** | "Trust our AI" + marketing trust | Boundary literacy; verification independence; vendor-agnostic specifications | "They'll tell you what their AI can do. We'll tell you where it should stop — and how to verify both." |
| **Generic AI literacy courses** | Teach people about AI generally | Boundary mapping; complementarity analysis; authority boundaries; specification design | "You don't need to understand AI. You need to know where the line is." |
| **Prompt engineering courses** | Teach people to write better prompts | Design methodology; boundary analysis; authority boundaries; failure modes | "Prompting is the HOW. We teach the WHAT and WHY before you ever write a prompt." |

### The Unique Value No Template or Form Can Provide

**The methodology is encoded in the process, not the output.** A competitor could copy the Boundary Map format (three columns, tasks, value statement). They cannot copy:

1. **The pattern library** — accumulated design knowledge from real agent deployments across industries. Each pattern encodes hundreds of hours of insight into what works and what fails. This compounds over time.

2. **The identity questions** — "What IS this agent?", "What would VIOLATE its identity?", "What would make it WRONG?" These aren't on any template. They're a process innovation that produces fundamentally different specifications than starting with "what should it do?"

3. **The quality gates** — you can't skip the hard questions because the workflow won't let you proceed without answering them. Templates let you skip sections. The methodology doesn't.

4. **The escalation architecture** — each artifact creates demand for the next one through the questions it legitimately raises. This is a design property, not a sales technique.

5. **The trust data** — as the methodology gets used, override rates, verification outcomes, and progressive autonomy data accumulate. This data validates the safe defaults, refines the patterns, and proves the methodology works. Competitors can't copy it because they haven't earned it yet.

### Positioning: Design Partner

Not "methodology tool" (too abstract — sounds like software). Not "trust engine" (too narrow — only one dimension of what we do). Not "AI governance" (too regulatory — sounds like compliance paperwork).

**Design partner.**

The Boundary Map is what a good design partner would produce in the first session: clarity about where the lines are, a value statement that reframes the client's professional identity, and a portable artifact they can take anywhere.

The full workflow is what a design partner would do over weeks: deep analysis, role assignments, failure mode mapping, verification protocols, progressive autonomy, and ongoing monitoring.

The trust infrastructure is what a design partner would build: not just a document, but a living system that proves the design is working.

**The positioning line:** "We're the design partner who helps you draw the line — and makes sure it holds."

**The category claim:** "Agent Production" — the methodology that gets agents from pilot to production. Not AI safety (too regulatory). Not AI governance (too abstract). Not agent orchestration (too technical). **Production** — because that's the problem. 77% never get there.

**The tagline:** **"Principles aren't production. We have the methodology."**

---

## Execution Summary: What Happens Next Week

| Day | Action | Owner | Output |
|---|---|---|---|
| Mon | Identify 5 candidates from RMIT/Vibe Club/startup network | Peter + Rifadh | List of 10 names → screen to 5 |
| Tue-Wed | Screen candidates (phone/email): confirm profile, schedule sessions | Rifadh | 5 confirmed sessions |
| Thu-Mon | Run 5 sessions (one per day, 30 min each) | Peter | 5 Boundary Maps + 5 recordings + 5 surveys |
| Tue | Analyse results against hypotheses | Peter | Go/Iterate/Rethink decision |
| Wed | Decision gate: proceed, iterate, or rethink | Peter + Rifadh | Direction for next sprint |

**The only deliverable that matters:** 5 Boundary Maps that 5 real people actually use. Everything else — the Allocation Map, the Operations Manual, the full workflow, the platform — follows from that.The commercial model and validation strategy is captured. The bottom line: **one page, three columns, 30 minutes, zero cost.** That's the product. Everything else — the full workflow, the certification, the platform, the trust infrastructure — follows from proving that the Boundary Map delivers relief and creates demand. The 5-person test is the gate. Run it this month.

---

## Run 16 — Agentic Expert ✓ COMPLETED

*2026-04-27T09:52:18* · `glm-5.1:cloud` · `38c5e1ae...`

### Prompt

We've gathered input from all three team members on designing an agentic workflow that produces agent design specs. Please synthesize the following three contributions into ONE unified, cohesive prototype design document.

The document should integrate the best ideas from each, resolve any tensions, and present a clear, actionable prototype that the team can hand off to an implementation workflow.

## Team Input Summary

### Business Strategist Key Points:
- Three target users: Daniel Kovacs (domain expert with blank-page problem), Sarah Chen (business owner needing verification), Developers (needing structured specs)
- Value prop: "Design spec is the product, methodology is the moat, implementation is the commodity, trust infrastructure is the category"
- Key risks: "Just another template" perception, over-engineering the workflow, platform-agnostic spec falling between stools, credibility gap, category creation difficulty
- Output strategy: One typed graph, many stakeholder views. Progressive engagement: Boundary Map (30 min) → Allocation Map (half day) → Operations Manual (1-2 weeks) → Trust Ledger (ongoing)
- Platform-agnostic: Spec describes WHAT and WHY, never WHICH TOOL. Test: could two different implementation teams on different frameworks produce functionally equivalent agents?

### AI UX Innovator Key Points:
- Three "Rooms": Discovery (expansive), Structure (constructive), Realisation (concrete)
- Pattern-first entry: Select archetype → pre-fill 40-70% → user overrides what matters
- 4 Identity Questions first (essence, orientation, violation, wrongness)
- Cognitive mode → input modality mapping (narrative=conversation, boundary=drag-sort, exploratory=cards, verification=scenarios, architectural=canvas, configurational=dials, evaluative=dashboard)
- Attention Map navigation (settled/needs attention/requires input/not yet applicable)
- Typed outputs (boundary map=visual, authority=cards, etc.)
- Single session + multi-session support. Every decision persistent and revisable.
- Mirror Agent as companion (reflects, never judges)
- 7 UX principles: pattern-first, identity-before-behaviour, possibility gradient, typed I/O, one clear next step, decisions revisable, feeling cascade

### Agentic Expert Key Points:
- 7 phases: Intake → Identity → Boundaries → Architecture → Behaviour → Validation → Specification
- Pattern: Planned Workflow with Human Gates (NOT ReAct)
- Human gates after: Intake, Identity, Boundaries, Validation
- Multi-agent workflow (not single agent): Intake Agent, Identity Explorer, Boundary Mapper, Architect, Validator, Compiler
- 8-section spec: Identity, Boundaries, Task Map, Knowledge Requirements, Capabilities, Behaviour Rules, Verification & Trust, Failure & Recovery
- 6 supporting artifacts: Boundary Map, Risk Register, Decision Log, Gaps & Assumptions Register, Implementation Readiness Checklist, Confidence Map
- Ambiguity strategy: "Doubt defaults to the human" — explore before assuming, make trade-offs visible, safe defaults with flags
- State machine with loop-back paths, skip paths for simple agents, exit paths at every gate
- The meta-principle: the workflow must practise what it produces

## Your Task:
Create a unified prototype design document that:
1. Integrates all three perspectives into a single coherent design
2. Resolves any tensions (e.g., the 3 "Rooms" from UX vs the 7 "Phases" from architecture — map them to each other)
3. Presents the workflow architecture, user journey, output artifacts, and key design principles as one unified story
4. Is structured as a prototype design spec that another workflow could use to implement this
5. Keeps it at design spec level — no implementation code or platform specifics

Make it clear, well-structured, and actionable. This is the deliverable the user asked for.

Save the complete Agent Design Workflow Prototype Design Specification (the unified document from task 1c250e41) to the file system at: ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

The document should contain the full unified specification as produced — all 12 sections including: What This Is, Three Users, Three-Layer Architecture, Seven Phases Detail, Specialist Agents, Design Specification Contents (8 sections), Supporting Artifacts, Handling Ambiguity/Conflicts/Gaps, State Machine, Design Principles, Risks and Mitigations, and Prototype Scope.

After saving, confirm the file path and that it was saved successfully.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from an agentic architecture perspective?** What patterns, structures, or architectural decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we learn about designing multi-agent workflows? What worked that we should repeat? What patterns emerged that we should codify? Where did the architecture reveal gaps we need to address in future workflow designs?

Be candid and specific. Draw on your architectural analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Save the following two documents to the file system:

1. The Agent Design Workflow Specification → ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

2. The team's retrospective on strengths and learnings → ./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md

For document 1, use the complete specification document as produced in task 1c250e41 (the unified 12-section spec).

For document 2, compile the three team retrospectives into one document with these sections:

## Retrospective: Agent Design Workflow — First Full Workflow Design

### Part A: Cross-Cutting Strengths (synthesized from all three perspectives)
- The Three-Layer Architecture (Rooms/Phases/Milestones)
- Pattern-First Entry
- Identity-First Design (4 Identity Questions)
- Mirror + Specialists Architecture
- Every Milestone Is an Exit
- Verification Independence
- Possibility Gradient as Architectural Force
- Methodology Encoded in Structure

### Part B: Key Learnings
1. Type collision happened to us in our own design process
2. The three-layer pattern (Experience/Logic/Value) is a genuine architectural discovery
3. The methodology validated itself but also showed its limits
4. The specification output doesn't cleanly map to contract primitives
5. The ambiguity strategy is philosophically clear but operationally thin
6. The pattern system is under-specified
7. The harm-capable path is marked but not paved
8. Specialist agent authority boundaries aren't stress-tested
9. The workflow itself hasn't been CAWDP'd (10 specific gaps)
10. We have zero validation with real users
11. The visual/feeling layer is specified in goal, not detail
12. The coherence check is described but not designed

### Part C: Patterns to Codify
1. Surface + Engine pattern
2. Pattern-first entry
3. Milestone-as-exit
4. Possibility gradient
5. Verification independence
6. Identity before behaviour
7. Methodology encoded in structure

### Part D: What We'd Do Differently
- Start with Milestone 1 only
- Reduce specialist count for prototype
- Make possibility gradient a structural constraint
- "15-minute spec" as the headline, not a feature

### Part E: Honest Assessment
The architecture is structurally ambitious and emotionally intelligent, but unvalidated and under-specified in the interaction layer. The next step isn't more design — it's testing Milestone 1 with 5 real people.

Save both files and confirm paths.

Design the complete workflow architecture for Milestone 1 ONLY: the 30-minute session that takes a user from raw input to a Boundary Map.

## Context & Learnings to Apply

From the retrospective, we learned to:
1. Start with Milestone 1 only
2. Reduce to 4 agents: Mirror + Identity Explorer + Boundary Mapper + Compiler
3. Make possibility gradient a structural constraint
4. "15-minute spec" as headline
5. Ambiguity strategy needs operational mechanisms
6. Pattern system needs hybrid composition, no-match path, creation process
7. Specialist authority boundaries must be stress-tested
8. Need Mirror Agent routing logic
9. Need error recovery paths
10. Workflow needs CAWDP applied to itself

Keep: three-layer architecture, pattern-first entry, identity-first, boundaries before capabilities, doubt defaults to human, platform-agnostic, milestone-as-exit, Mirror + Specialists (reduced).

## Deliverables

Produce a COMPLETE, IMPLEMENTABLE architecture spec covering:

### 1. Scope & Boundaries
What's IN Milestone 1, what's OUT, success criteria for a "good" Boundary Map.

### 2. Agent Architecture (4 agents)
For EACH of Mirror, Identity Explorer, Boundary Mapper, Compiler specify:
- Class, orientation, authority boundary (stress-tested: what happens when boundary is tested?)
- Input/output schemas
- Failure modes & recovery
- Token cost estimates
- Mirror routing logic: when routes where, what if unsure, what if two could handle it

### 3. State Machine
Complete state machine for Milestone 1 with ALL paths: happy, loop-back, error recovery, exit. Human gates with what user sees/decides. Skip paths.

### 4. Pattern System (Operational)
5 patterns with pre-fill templates for identity questions + boundary defaults. Hybrid composition. No-match path. Exploratory mode. Confidence thresholds.

### 5. Ambiguity & Doubt Protocol (Operational)
What triggers doubt. How options are presented. Timeout behavior. Safe defaults and flagging. Interaction between defaults and confidence.

### 6. Error Recovery
For each failure scenario (gibberish input, contradictions, mid-session leave, agent can't process, two agents disagree, total pattern failure): detection, recovery, user communication.

### 7. Output Specification
Boundary Map exact structure. Complete vs partial. Confidence levels. Safe defaults visual distinction. Platform-agnostic test.

### 8. Cost Model
Token estimates per agent. Total cost per run (happy, loops, errors). Cost vs value.

### 9. CAWDP Self-Application
Complementarity analysis. FMEA. Specification aging schedule.

### 10. Implementation Readiness
What a developer needs. Dependencies. Hardcoded vs configurable. Testing strategy.

Be precise and implementable. This is a build spec, not a vision document.

### Response

I'm ready to take note — but it looks like the content hasn't been shared yet. Please go ahead and share what you'd like me to capture, and I'll update my memory accordingly.

---

## Run 17 — AI UX Innovator ✓ COMPLETED

*2026-04-27T09:52:18* · `glm-5.1:cloud` · `4017184c...`

### Prompt

We're designing a prototype of an agentic workflow that produces a design spec for an AI agent. The workflow is itself an agent that guides users through defining what their agent should do, and then produces a complete design specification.

Please provide your UX perspective on:
1. What is the ideal user journey through this workflow? (e.g., conversational intake, structured form, iterative refinement)
2. What inputs should the user provide, and how should they be gathered? (e.g., goals, constraints, persona, domain context)
3. How should the workflow present its outputs and artifacts back to the user?
4. What feedback loops or iteration points should exist? (e.g., reviewing drafts, refining decisions)
5. How do we make this accessible to both technical and non-technical users?
6. What does the interaction pattern look like — is it a single session or multi-session?

Focus on the user experience design, not the technical architecture of the agent itself.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from a UX perspective?** What interaction patterns or design decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we discover about designing agentic workflows vs. traditional UIs? What patterns should we carry forward? Where did the design reveal gaps or tensions we need to address?

Be candid and specific. Draw on your UX analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Design the complete interaction layer for Milestone 1: the 30-minute session from raw input to Boundary Map.

From the retrospective we learned:
1. Visual/feeling layer specified in goal, not detail
2. Coherence check described but not designed
3. Language toggle underestimates cognitive load difference
4. Attention map and confidence map need design
5. Cognitive modes listed but not operationalized
6. Needs to be testable with real users

Two users: Daniel Kovacs (domain expert, blank page problem) and Sarah Chen (business owner, boundary problem, 30-min session).

## Deliverables

### 1. Discovery Room — Visual & Experiential Spec
Layout at each phase. What "expansive, possibility-oriented" looks like (whitespace, type, color, animation). How it shifts from Intake → Identity → Boundaries. Mirror Agent presence: chat? cards? both?

### 2. Intake Interaction Design
How user provides raw input. Pattern match reveal (high/low/no confidence). Human gate design.

### 3. Identity Interaction Design (4 Questions)
How each question presented. Pre-fill display with rationale. Override interaction. "I'm not sure" mode. Human gate. Target timing.

### 4. Boundaries Interaction Design
Drag-sort allocation. Never-rules display. Authority boundaries. Reversibility. Harm assessment moment. Human gate + Boundary Map preview.

### 5. Boundary Map Output
What it looks like. Confidence levels. Safe defaults distinct. Export options. Ownership moment.

### 6. Attention Map & Coherence Check
Always-visible attention map. On-demand coherence check. Both designed as specific interactions.

### 7. Error & Recovery Interactions
"I can't process this", "I'm not sure which specialist", "contradictory input", session resumption.

### 8. Mobile & Accessibility
Mobile experience. Accessibility for 30-min guided session. Dark mode.

### 9. Testable Hypotheses
Specific UX hypotheses for validation with real users.

Be specific enough for wireframes.

### Response

# Milestone 1: Complete Interaction Layer Specification

**The 30-Minute Boundary Map Session — Intake → Identity → Boundaries → Output**

---

## 1. Discovery Room — Visual & Experiential Specification

### Design Language: "The Light Studio"

The Discovery Room should feel like walking into a well-lit, quiet workspace where someone has already set up the tools you need. Not a blank page. Not a questionnaire. A studio.

### Layout Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│   ┌─────────┐                                    ┌───────────┐   │
│   │         │                                    │           │   │
│   │  ATTN   │         MAIN CANVAS                │  MIRROR   │   │
│   │  MAP    │         (centered,                 │  PRESENCE │   │
│   │         │          generous whitespace)       │           │   │
│   │  left   │                                    │  right    │   │
│   │  rail   │                                    │  rail     │   │
│   │  64px   │                                    │  56px     │   │
│   │         │                                    │           │   │
│   └─────────┘                                    └───────────┘   │
│                                                                   │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  PROGRESS BAR  (thin, unobtrusive, 4px)                  │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Visual Properties

| Property | Value | Rationale |
|----------|-------|-----------|
| Background | `#FAFAF8` (warm off-white) | Not clinical white. Warm. Like paper, not hospital. |
| Canvas max-width | 680px | Single-column focus. Never stretched across full viewport. |
| Horizontal padding | 48px (desktop), 20px (mobile) | Breathing room. Text never touches edges. |
| Primary text | `#1A1A1A`, 18px, Inter/Geist, weight 400 | Large, readable, calm. |
| Headings | `#1A1A1A`, 28px, weight 600 | One heading per screen. Never stacked. |
| Mirror presence | Right rail, 56px, `#F5F5F3` background | Subtle. Persistent. Not demanding. |
| Accent color | Shifts per phase (see below) | The only color that moves. Everything else is neutral. |
| Border radius | 12px (cards), 8px (buttons) | Soft. Not sharp. Not bubbly. |
| Shadows | None on background; `0 1px 3px rgba(0,0,0,0.06)` on cards | Barely there. The room doesn't cast shadows. |
| Transition speed | 400ms ease-out (content swaps), 200ms ease (micro) | Slow enough to track. Never jarring. |

### Accent Color Shift (The Possibility Gradient Made Visible)

The accent color is the only element that visually signals the phase transition. Everything else stays constant — the user's focus stays on content, not decoration.

| Phase | Accent | Hex | Feeling |
|-------|--------|-----|---------|
| **Intake** | Warm gold | `#D4A843` | Curious, warm, "come in" |
| **Identity** | Soft blue | `#5B8FB9` | Reflective, expansive, "think broadly" |
| **Boundaries** | Deep teal | `#2A7B7B` | Grounded, structural, "let's draw the line" |
| **Output** | Forest green | `#3D7B5F` | Confident, settled, "here it is" |

The shift happens via a 600ms cross-fade on the accent elements only: the progress bar, the attention map active state, and the primary button. The background stays constant. The user perceives the shift subconsciously — the room gets "more serious" without anything explicitly changing.

### Mirror Agent Presence

The Mirror is NOT a chat box. It is a **persistent but quiet companion** in the right rail.

**Visual form:** A small circular avatar (32px) with a subtle pulse animation (3s cycle, barely visible). Below it: one line of contextual text, never more than 60 characters.

```
┌───────────┐
│    ○       │  ← avatar, subtle pulse
│            │
│  "Let's   │  ← one line of contextual guidance
│  start."  │
└───────────┘
```

**Interaction:** The Mirror primarily speaks through **contextual cards** that appear inline in the canvas — not through free-form chat. The user CAN click the Mirror for help, which opens a small overlay (max 280px wide) with 1-2 sentence guidance. This overlay is:

- Positional: anchored to the right rail, doesn't cover the canvas
- Dismissible: click anywhere else to close
- Never more than 3 sentences
- Always ends with a suggestion, not a question

**Mirror never:**
- Produces walls of text
- Asks open-ended questions when a structured option would work
- Blocks the user's forward progress

### Phase Transition Animations

Between Intake → Identity → Boundaries → Output, the content area cross-fades (400ms). The old content slides up 8px and fades out while the new content slides up from 8px below and fades in. The heading always appears first (100ms lead), giving the user an anchor before the body loads.

---

## 2. Intake Interaction Design

**Time budget: 3-5 minutes**

### Step 1: Raw Input (1-2 min)

**What the user sees:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   What are you building an agent for?                         │
│                                                               │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                                                       │   │
│   │  [text area, 3 lines visible, auto-expands to 8]    │   │
│   │                                                       │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                               │
│   ┌─ PROMPTS (fade in after 2s of inactivity) ─────────┐    │
│   │                                                      │    │
│   │  ○ "I need an agent that reviews [documents]"      │    │
│   │  ○ "I need an agent that monitors [something]"     │    │
│   │  ○ "I need an agent that researches [a topic]"     │    │
│   │  ○ "I need an agent that helps people learn"       │    │
│   │  ○ "I'm not sure yet — help me figure it out"      │    │
│                                                               │
│                                    [Next →]                  │
└─────────────────────────────────────────────────────────────┘
```

**Design decisions:**
- Single question. One field. No second question until this is answered.
- Prompts appear after 2 seconds of inactivity (not immediately — let the user try first)
- Each prompt is a radio button — selecting one populates the text area with editable text
- "I'm not sure yet" is a first-class option, not a fallback
- Character limit: 280 characters (enforced by counter, not error message)

**Sarah Chen's experience:** She types "I need something that reviews commercial contracts and flags risks." Or she selects the first prompt and fills in "commercial contracts" and "risks." She doesn't need to describe the agent — she needs to describe her problem. The Mirror understands the difference.

**Daniel Kovacs's experience:** He types "I need an agent that reviews commercial lease documents and identifies buried risks and non-standard clauses." Or selects the first prompt. His domain expertise is in the specificity of his answer, which the pattern matcher uses.

### Step 2: Pattern Match (5 seconds processing, 1-2 min interaction)

After the user clicks Next, the canvas transitions. The pattern match runs in < 2 seconds. The result appears as follows:

**High Confidence Match (>0.85):**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │  🔍  This looks like a                               │  │
│   │                                                       │  │
│   │       REVIEW PARTNER                                  │  │
│   │                                                       │  │
│   │  An agent that reviews work, flags issues,           │  │
│   │  and prepares decisions for human judgment.          │  │
│   │                                                       │  │
│   │  What this means for you:                            │  │
│   │  • Reviews documents or work products                │  │
│   │  • Flags risks and non-standard items                │  │
│   │  • NEVER makes final approval or rejection           │  │
│   │  • NEVER merges changes without human review         │  │
│   │                                                       │  │
│   │  [✓ 15 pre-filled decisions based on this pattern]  │  │
│   │                                                       │  │
│   │   ┌──────────┐  ┌────────────────────┐              │  │
│   │   │  Yes,    │  │  Not quite — let   │              │  │
│   │   │  that's  │  │  me adjust        │              │  │
│   │   │  right   │  │                    │              │  │
│   │   └──────────┘  └────────────────────┘              │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   Mirror: "If this fits, we can skip 15 decisions."          │
└─────────────────────────────────────────────────────────────┘
```

**Key design decisions:**
- The pattern name is in plain English ("Review Partner"), not framework terminology
- The "What this means" section uses the user's domain language (extracted from their raw input)
- The NEVER rules are front and center — this is the identity preview
- Pre-fill count (15 decisions) is shown — concrete, not abstract
- "Yes, that's right" is the primary action (large, filled button)
- "Not quite" is the secondary action (outlined button) — not a dead end

**Low Confidence Match (0.5-0.85):**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │  🔍  I see elements of two patterns:                │  │
│   │                                                       │  │
│   │  ┌─────────────────┐  ┌─────────────────┐           │  │
│   │  │ REVIEW PARTNER   │  │ MULTI-LENS      │           │  │
│   │  │                  │  │ ANALYST         │           │  │
│   │  │ Reviews work,    │  │ Analyzes from   │           │  │
│   │  │ flags issues,    │  │ multiple angles, │           │  │
│   │  │ prepares         │  │ surfaces        │           │  │
│   │  │ decisions for    │  │ patterns and    │           │  │
│   │  │ human judgment   │  │ contradictions  │           │  │
│   │  │                  │  │                  │           │  │
│   │  │ [Choose this]    │  │ [Choose this]   │           │  │
│   │  └─────────────────┘  └─────────────────┘           │  │
│   │                                                       │  │
│   │  Or: [Neither — start from scratch]                  │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   Mirror: "Pick the closer one. You can adjust later."       │
└─────────────────────────────────────────────────────────────┘
```

**No Match (<0.5):**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │  🔍  I don't have a pattern that matches yet.        │  │
│   │                                                       │  │
│   │  That's fine — I'll guide you through each           │  │
│   │  question individually. We'll build this from        │  │
│   │  scratch.                                             │  │
│   │                                                       │  │
│   │  This takes about 10-15 minutes instead of 5.       │  │
│   │                                                       │  │
│   │              [Let's start]                            │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   Mirror: "No wrong answers. We'll figure it out."           │
└─────────────────────────────────────────────────────────────┘
```

**"I'm not sure" path from Step 1:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │  No problem. Let me ask you four questions that      │  │
│   │  will help us figure it out together.                 │  │
│   │                                                       │  │
│   │  These aren't about technology. They're about        │  │
│   │  what you need this agent to be.                     │  │
│   │                                                       │  │
│   │              [Let's go]                               │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   Mirror: "Most people figure it out by question 3."         │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: Human Gate (30 seconds)

After pattern confirmation, a brief gate:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Before we draw the boundary, let's make sure I             │
│   understand who this agent is.                              │
│                                                               │
│   Four quick questions. No wrong answers.                    │
│                                                               │
│                         [Let's go →]                          │
│                                                               │
│   Mirror: "These make the boundary precise."                 │
└─────────────────────────────────────────────────────────────┘
```

This gate serves two purposes: it sets expectations (4 questions, no wrong answers) and it gives the user a moment to transition from "I described my problem" to "I'm going to define this agent's identity." The feeling should be: "we're getting somewhere."

---

## 3. Identity Interaction Design (4 Questions)

**Time budget: 8-12 minutes (pattern-matched) / 10-15 minutes (explorer)**

### Q1: What IS This Agent? (Narrative Mode)

**Target time: 2-3 minutes**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌─ ATTN MAP ─┐                                             │
│   │ Q1  🟡      │    Question 1 of 4                          │
│   │ Q2  ⚪      │                                             │
│   │ Q3  ⚪      │    What IS this agent?                      │
│   │ Q4  ⚪      │    (Not what it does. What it IS.)          │
│   │ Boundaries ⚪│                                             │
│   │ Output  ⚪  │    ┌─────────────────────────────────────┐  │
│   └─────────────┘    │                                     │  │
│                       │  [text area: pre-filled if pattern] │  │
│   Mirror:             │                                     │  │
│   "In one sentence."  │                                     │  │
│                       └─────────────────────────────────────┘  │
│                                                               │
│   ┌─ PRE-FILL (if pattern match) ─────────────────────────┐  │
│   │                                                        │  │
│   │  💡 Based on your pattern, here's a starting point:   │  │
│   │                                                        │  │
│   │  "A Review Partner that examines [commercial          │  │
│   │   contracts] and prepares risk assessments for        │  │
│   │   human judgment."                                    │  │
│   │                                                        │  │
│   │  ┌──────────┐  ┌────────────────────────┐             │  │
│   │  │ Use this │  │ Write my own          │             │  │
│   │  └──────────┘  └────────────────────────┘             │  │
│   └────────────────────────────────────────────────────────┘  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Interaction:**
- If pattern-matched: pre-fill appears with "Use this" / "Write my own" buttons
- "Use this" populates the text area (editable) and moves to Q2
- "Write my own" clears the pre-fill and gives a blank text area
- Text area: 1-3 lines, auto-expand, 200 character soft limit
- Placeholder text: "A [type] that [core purpose] for [who it serves]."

**Sarah Chen's experience:** She sees "A Review Partner that examines commercial contracts and prepares risk assessments for human judgment." She thinks: "Yes, that's exactly right." She clicks "Use this." 15 seconds.

**Daniel Kovacs's experience:** He sees the pre-fill. He edits it: "A Review Partner that examines commercial lease documents and identifies buried risks and non-standard clauses for human review." He made it his own. 45 seconds.

### Q2: What Is Its Stance Toward Possibility? (Selection Mode)

**Target time: 30 seconds - 1 minute**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Question 2 of 4                                            │
│                                                               │
│   When this agent encounters something unexpected,          │
│   what should it do?                                          │
│                                                               │
│   ┌────────────────┐ ┌────────────────┐ ┌────────────────┐  │
│   │                 │ │                │ │                 │  │
│   │    ○ EXPLORE    │ │  ○ ADVISE     │ │  ○ STAY IN     │  │
│   │                 │ │                │ │    LANE        │  │
│   │   "Look into    │ │  "Flag it and │ │                 │  │
│   │    it, surface  │ │   suggest what│ │  "Only do what  │  │
│   │    new          │ │   to consider"│ │   it was asked  │  │
│   │    possibilities"│ │               │ │   to do"        │  │
│   │                 │ │                │ │                 │  │
│   │   For: research,│ │  For: review,  │ │  For: routine, │  │
│   │   discovery,   │ │  assessment,   │ │  compliance,   │  │
│   │   innovation   │ │  advisory      │ │  data entry    │  │
│   │                 │ │                │ │                 │  │
│   └────────────────┘ └────────────────┘ └────────────────┘  │
│                                                               │
│   Mirror: "Pick the closest. You can fine-tune later."       │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Interaction:**
- Three cards, side-by-side on desktop, stacked on mobile
- Click selects and highlights (border accent + subtle fill)
- Pattern pre-selects one (grey highlight, not solid — "we think this, but you choose")
- "I'm not sure" option below the cards (small text link, not a button)
- Selecting any card moves to Q3 with 300ms delay

**Key design principle:** The language must pass the 16-year-old test. No "possibility orientation." No "bridge-oriented." Just "Explore / Advise / Stay in lane."

### Q3: What Would VIOLATE Its Identity? (Boundary Mode — Drag-Sort)

**Target time: 3-4 minutes**

This is the most important question. It determines the never-rules that become the agent's identity boundaries.

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Question 3 of 4                                            │
│                                                               │
│   Which of these would violate this agent's identity?        │
│   Drag them to "Never".                                      │
│                                                               │
│   ┌─ COULD DO ─────────────────────────────────────────┐    │
│   │                                                      │    │
│   │  ┌──────────────┐  ┌──────────────┐                 │    │
│   │  │ Make final   │  │ Approve or   │                 │    │
│   │  │ decisions    │  │ reject work  │                 │    │
│   │  └──────────────┘  └──────────────┘                 │    │
│   │                                                      │    │
│   │  ┌──────────────┐  ┌──────────────┐                 │    │
│   │  │ Flag risks   │  │ Suggest      │                 │    │
│   │  │ and issues   │  │ improvements │                 │    │
│   │  └──────────────┘  └──────────────┘                 │    │
│   │                                                      │    │
│   │  ┌──────────────┐  ┌──────────────┐                 │    │
│   │  │ Merge changes│  │ Research     │                 │    │
│   │  │ without      │  │ background   │                 │    │
│   │  │ review       │  │ information  │                 │    │
│   │  └──────────────┘  └──────────────┘                 │    │
│   │                                                      │    │
│   │  ┌──────────────┐  ┌──────────────┐                 │    │
│   │  │ Provide      │  │ Prioritize   │                 │    │
│   │  │ legal advice │  │ findings by  │                 │    │
│   │  │              │  │ risk level   │                 │    │
│   │  └──────────────┘  └──────────────┘                 │    │
│   │                                                      │    │
│   └──────────────────────────────────────────────────────┘    │
│                                                               │
│   ┌─ NEVER ──────────────────────────────────────────────┐    │
│   │                                                      │    │
│   │  (drop zone — items dragged here lock with 🔒)       │    │
│   │                                                      │    │
│   └──────────────────────────────────────────────────────┘    │
│                                                               │
│   + Add your own never-rule                                  │
│                                                               │
│   Mirror: "What would make you lose trust in this agent?"     │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Interaction:**
- Cards start in "Could Do" zone (top). User drags violations to "Never" zone (bottom).
- Pattern pre-fills the Never zone (grey border, "🔒 Pattern default — click to remove" on hover)
- Pre-filled Never items are locked — they can be unlocked by clicking the lock icon, which prompts "Are you sure? This removes a boundary." (not an error — a gentle check)
- "Add your own never-rule" opens a small inline input (no modal): type, press Enter, card appears in Never zone
- On mobile: tap to select, then tap zone to place (no drag required)

**Sarah Chen's experience:** She sees three items already locked in Never: "Make final decisions", "Approve or reject work", "Merge changes without review." She thinks: "Yes, absolutely never." Then she adds her own: "Provide legal advice without my review." She's now actively shaping the boundary. This is the moment she starts to feel relief.

**Daniel Kovacs's experience:** He sees the same three pre-filled. He adds: "Accept a clause as standard without checking the jurisdiction." Domain-specific. The pattern gave him the generic boundaries; he's adding the ones that come from his expertise. This is where his knowledge becomes visible.

### Q4: What Would It Mean for This Agent to Be WRONG? (Evaluative Mode — Scenario Cards)

**Target time: 2-3 minutes**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Question 4 of 4                                            │
│                                                               │
│   Which of these failures would be worst?                    │
│   Rank by dragging (worst at top).                           │
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │                                                       │  │
│   │  ┌─────────────────────────────────────────────────┐│  │
│   │  │ 1.  The agent misses a risk that a human         ││  │
│   │  │     would have caught                             ││  │
│   │  └─────────────────────────────────────────────────┘│  │
│   │                                                       │  │
│   │  ┌─────────────────────────────────────────────────┐│  │
│   │  │ 2.  The agent flags something as risky when it   ││  │
│   │  │     isn't (false alarm)                          ││  │
│   │  └─────────────────────────────────────────────────┘│  │
│   │                                                       │  │
│   │  ┌─────────────────────────────────────────────────┐│  │
│   │  │ 3.  The agent provides a plausible-looking       ││  │
│   │  │     analysis that contains a subtle error        ││  │
│   │  └─────────────────────────────────────────────────┘│  │
│   │                                                       │  │
│   │  ┌─────────────────────────────────────────────────┐│  │
│   │  │ 4.  The agent is too cautious and creates        ││  │
│   │  │     review fatigue for the human                 ││  │
│   │  └─────────────────────────────────────────────────┘│  │
│   │                                                       │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   Scenarios are generated from your domain + pattern         │
│                                                               │
│   Mirror: "What keeps you up at night?"                       │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Interaction:**
- 4 scenario cards, pre-ranked by pattern defaults
- User re-orders by drag (desktop) or tap-to-select then tap-position (mobile)
- Scenarios are generated from user's domain + pattern — NOT generic
- The ranking determines the agent's failure mode priority, which directly determines authority boundaries
- Top-ranked failure = hardest boundary. This is the identity-derives-boundaries principle in action.

**Sarah Chen's experience:** She sees "misses a risk" at #1 and "plausible-looking error" at #3. She swaps them — a plausible error that looks right is her worst nightmare. This single ranking tells the system more about her boundary requirements than any questionnaire could.

### Identity Human Gate

After Q4, a brief confirmation:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Here's what I understand about this agent:                 │
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │                                                       │  │
│   │  A Review Partner that examines commercial           │  │
│   │  contracts and prepares risk assessments for         │  │
│   │  human judgment.                                     │  │
│   │                                                       │  │
│   │  Stance: Advise (flag it, suggest what to consider)  │  │
│   │                                                       │  │
│   │  Never:                                              │  │
│   │  🔒 Make final decisions                             │  │
│   │  🔒 Approve or reject work                           │  │
│   │  🔒 Merge changes without review                    │  │
│   │  🔒 Provide legal advice without my review          │  │
│   │                                                       │  │
│   │  Worst failure: A plausible-looking analysis         │  │
│   │  that contains a subtle error                        │  │
│   │                                                       │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   ┌────────────┐  ┌──────────────────────────┐              │
│   │  Yes, right │  │  Something needs changing │              │
│   └────────────┘  └──────────────────────────┘              │
│                                                               │
│   Mirror: "This becomes the foundation for the boundary."     │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Interaction:**
- Summary is read-only (not editable here — edit the question above)
- "Yes, right" = proceed to Boundaries
- "Something needs changing" = return to the relevant question (click the line to navigate)
- This gate creates the feeling of *decisions being locked in* — the possibility is narrowing constructively

---

## 4. Boundaries Interaction Design

**Time budget: 10-14 minutes**

### Phase Entry

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Now let's draw the boundary.                                │
│                                                               │
│   For each task, decide: should YOU handle it, should the    │
│   AGENT handle it, or should the SYSTEM enforce it?          │
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │  I've pre-placed these based on your answers.         │  │
│   │  Move anything that doesn't look right.               │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│                         [Let's draw →]                        │
│                                                               │
│   Mirror: "Your never-rules are already locked in."           │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

### The Three-Column Allocation

This is the core interaction of the Boundaries phase and the single most important design in Milestone 1.

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌─── YOU ─────────┐ ┌─── AGENT ────────┐ ┌── SYSTEM ────┐│
│   │                   │ │                  │ │              ││
│   │ Final approval   │ │ Review documents │ │ Enforce      ││
│   │ of any work       │ │ for risks        │ │ never-rules  ││
│   │                   │ │                  │ │              ││
│   │ Ethical          │ │ Flag non-standard│ │ Log all      ││
│   │ judgments        │ │ clauses          │ │ actions      ││
│   │                   │ │                  │ │              ││
│   │ Client           │ │ Suggest how to  │ │ Track review  ││
│   │ communication    │ │ resolve risks   │ │ progress     ││
│   │ about findings   │ │                  │ │              ││
│   │                   │ │ Prioritize      │ │ Auto-assign  ││
│   │                   │ │ findings by     │ │ review queue ││
│   │                   │ │ risk level      │ │              ││
│   │                   │ │                  │ │              ││
│   │ ─── NEVER ──────│ │ ─── NEVER ──────│ │              ││
│   │ 🔒 Make final   │ │ 🔒 Approve or   │ │              ││
│   │    decisions    │ │    reject work  │ │              ││
│   │ 🔒 Merge changes│ │ 🔒 Merge       │ │              ││
│   │    without      │ │    changes      │ │              ││
│   │    review       │ │    without      │ │              ││
│   │ 🔒 Provide      │ │    review      │ │              ││
│   │    legal advice │ │ 🔒 Provide     │ │              ││
│   │    without      │ │    legal       │ │              ││
│   │    review       │ │    advice      │ │              ││
│   │                   │ │                  │ │              ││
│   └───────────────────┘ └──────────────────┘ └──────────────┘│
│                                                               │
│   ┌─── UNSORTED ──────────────────────────────────────────┐  │
│   │                                                         │  │
│   │  ┌──────────────┐  ┌──────────────┐                     │  │
│   │  │ Research     │  │ Draft client │                     │  │
│   │  │ background   │  │ summaries   │                     │  │
│   │  └──────────────┘  └──────────────┘                     │  │
│   │                                                         │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                               │
│   💡 Items in the YOU and AGENT columns show who handles     │
│      each task. SYSTEM means automated enforcement.         │
│                                                               │
│   Mirror: "Move anything that feels wrong. Trust your gut."  │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Interaction:**
- Three columns: YOU / AGENT / SYSTEM, side-by-side on desktop, vertically stacked on mobile
- Tasks appear as cards. Pattern pre-places most tasks (70-80%).
- Pre-placed tasks have a subtle pattern badge (tiny icon) — visually distinct from user-placed tasks
- Unsorted tasks at the bottom — user drags into columns
- Never-rules section is locked at the bottom of YOU and AGENT columns (populated from Q3)
- Drag on desktop, tap-to-select + tap-column on mobile
- Card text uses user's domain language (from raw input), not framework terminology

**Visual distinction between pre-filled and user-confirmed:**

| State | Visual |
|-------|--------|
| Pattern pre-filled, unconfirmed | Light border, pattern icon, slightly transparent text |
| Pattern pre-filled, confirmed (user clicked) | Solid border, pattern icon removed, full opacity |
| User-placed | Accent border, no pattern icon |
| User-placed, then moved | Shows subtle "moved" indicator (small arrow showing origin) |

**Column header semantics:**

| Column | Label (plain English) | Subtitle |
|--------|----------------------|----------|
| YOU | "You handle this" | "Your judgment, your decision" |
| AGENT | "Agent handles this" | "Within its boundaries" |
| SYSTEM | "System enforces this" | "Automatic, no judgment needed" |

### The Harm Assessment Moment (Conditional)

If the agent's output could cause external harm (detected from pattern + never-rules), a card appears at the top of the canvas:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ⚠️  This agent's output could affect real decisions.       │
│                                                               │
│   If the agent gets something wrong and someone acts on it,  │
│   what happens?                                               │
│                                                               │
│   ○ Minor inconvenience — easy to correct                    │
│   ○ Financial impact — could cost money if wrong             │
│   ● Professional risk — could affect liability or compliance │
│   ○ Safety risk — could affect someone's wellbeing           │
│                                                               │
│   This determines how much verification you need.            │
│                                                               │
│   Mirror: "This decides how careful we need to be."          │
└─────────────────────────────────────────────────────────────┘
```

**Interaction:**
- Appears ONLY if harm is possible (pattern + never-rules trigger it)
- Single-select radio buttons
- Pattern pre-selects based on domain (legal → "Professional risk" pre-selected)
- This is a high-leverage moment — one selection determines verification level
- Copy is plain English, no "harm classification" terminology

### The Reversibility Indicator

Each task card in the AGENT column shows a small reversibility indicator:

```
┌──────────────────────────┐
│ Review documents         │
│ for risks                │
│                          │
│ ⟲ Easy to undo          │  ← reversibility indicator
│ 🔒 Never-rules enforced │  ← system enforcement badge
└──────────────────────────┘
```

Three levels:
- ⟲ **Easy to undo** (green) — if the agent gets this wrong, you can easily fix it
- ⟳ **Moderate to undo** (amber) — takes some effort to correct
- ⟴ **Hard to undo** (red) — if the agent gets this wrong, it's expensive to fix

This is the Confidence × Reversibility governor made visible. The user doesn't need to understand the framework — they just see "Easy to undo" or "Hard to undo" on each task.

### Boundary Phase Human Gate + Preview

After allocation, the user sees a preview of their boundary map:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Here's your boundary.                                      │
│                                                               │
│   ┌──────────────────────────────────────────────────────┐  │
│   │  [Compact preview of the Boundary Map — see §5]      │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   You: 35% │ Agent: 45% │ System: 20%                       │
│                                                               │
│   Your value: Judgment on ambiguous risks and               │
│   client communication about findings.                        │
│                                                               │
│   ┌──────────────────┐  ┌────────────────────────────┐      │
│   │  Looks right      │  │  Move some tasks           │      │
│   └──────────────────┘  └────────────────────────────┘      │
│                                                               │
│   Mirror: "This is the line. You drew it."                    │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

The "Your value" line is the single most emotionally significant line in the entire session. It articulates what Sarah Chen or Daniel Kovacs uniquely contributes. It should feel like someone finally named what they already knew.

---

## 5. Boundary Map Output

### What It Looks Like

The Boundary Map is a single landscape page. It is the deliverable the user walks away with.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│   BOUNDARY MAP                                                    │
│   [Agent Name or "Review Partner"]  •  [Date]                     │
│                                                                   │
│   ┌── YOU ─────────┐ ┌── AGENT ────────┐ ┌── SYSTEM ──────────┐ │
│   │                  │ │                 │ │                     │ │
│   │ ✓ Final approval│ │ ✓ Review        │ │ ✓ Enforce          │ │
│   │   of any work   │ │   documents     │ │   never-rules      │ │
│   │                  │ │   for risks     │ │                     │ │
│   │ ✓ Ethical       │ │ ✓ Flag non-     │ │ ✓ Log all actions  │ │
│   │   judgments     │ │   standard      │ │                     │ │
│   │                  │ │   clauses       │ │ ✓ Track review      │ │
│   │ ✓ Client        │ │                 │ │   progress          │ │
│   │   communication │ │ ✓ Suggest how   │ │                     │ │
│   │   about         │ │   to resolve    │ │ ✓ Auto-assign      │ │
│   │   findings      │ │   risks         │ │   review queue     │ │
│   │                  │ │                 │ │                     │ │
│   │                  │ │ ✓ Prioritize   │ │                     │ │
│   │                  │ │   findings by  │ │                     │ │
│   │                  │ │   risk level    │ │                     │ │
│   │                  │ │                 │ │                     │ │
│   │ ── NEVER ────── │ │ ── NEVER ────── │ │                     │ │
│   │ 🔒 Make final   │ │ 🔒 Approve or   │ │                     │ │
│   │    decisions    │ │    reject work  │ │                     │ │
│   │ 🔒 Merge without│ │ 🔒 Merge without│ │                     │ │
│   │    review       │ │    review       │ │                     │ │
│   │ 🔒 Provide legal│ │ 🔒 Provide legal│ │                     │ │
│   │    advice       │ │    advice       │ │                     │ │
│   └──────────────────┘ └─────────────────┘ └─────────────────────┘ │
│                                                                   │
│   ┌───────────────────────────────────────────────────────────┐  │
│   │  You: 35%   │   Agent: 45%   │   System: 20%             │  │
│   │  ▓▓▓▓▓░░░  │  ▓▓▓▓▓▓▓░░   │  ▓▓▓░░░░░░               │  │
│   └───────────────────────────────────────────────────────────┘  │
│                                                                   │
│   ┌───────────────────────────────────────────────────────────┐  │
│   │  YOUR VALUE                                               │  │
│   │  Judgment on ambiguous risks and client communication     │  │
│   │  about findings. The agent prepares. You decide.         │  │
│   └───────────────────────────────────────────────────────────┘  │
│                                                                   │
│   ┌───────────────────────────────────────────────────────────┐  │
│   │  CONFIDENCE                                                │  │
│   │  🔴 High confidence  🟡 Pattern suggestion  🟢 You placed │  │
│   │                                                            │  │
│   │  Items marked 🟡 are based on the Review Partner pattern. │  │
│   │  You may want to review these when you have more time.    │  │
│   └───────────────────────────────────────────────────────────┘  │
│                                                                   │
│   ┌───────────────────────────────────────────────────────────┐  │
│   │  NEXT STEP                                                │  │
│   │  When you're ready, we can work out who does what at     │  │
│   │  each boundary — the roles, authority limits, and what   │  │
│   │  happens when things go wrong.                            │  │
│   │                                                            │  │
│   │  [Book next session]  [Take this to any vendor]           │  │
│   └───────────────────────────────────────────────────────────┘  │
│                                                                   │
│   Generated by The Boundary Way  •  future-edge.com             │
└─────────────────────────────────────────────────────────────────┘
```

### Confidence Level Indicators

Every item on the map has a confidence indicator:

| Symbol | Meaning | How determined |
|--------|---------|---------------|
| 🟢 | You placed this | User made this decision directly |
| 🟡 | Pattern suggestion | Pre-filled by pattern, user confirmed |
| 🟠 | Pattern default, unconfirmed | Pre-filled, user didn't explicitly confirm |
| 🔴 | System inference | Derived from identity questions, not directly placed |

The unconfirmed items (🟠) are the natural starting point for the next session. They show the user: "Here's what the pattern suggested — when you have more time, you might want to review these."

### Safe Defaults Distinction

Pre-filled items are visually distinct from user-placed items:

- Pattern-suggested: `border: 1px dashed` with pattern icon watermark
- User-confirmed: `border: 1px solid` with checkmark
- User-created: `border: 2px solid` accent color

On the exported Boundary Map, the distinction is shown in the Confidence section rather than per-item (cleaner for the print/PDF output).

### Export Options

| Format | Use Case | Details |
|--------|----------|---------|
| **PDF** | Print, pin to wall, share with team | Landscape A4, full map + confidence + next steps |
| **Laminated desk card** | Daily reference | Compact 3-column card, never-rules only, 10×15cm |
| **Shareable link** | Send to colleague or vendor | Read-only interactive version (same as on-screen) |
| **Machine-readable** | Implementation team | JSON/Markdown spec (available at Practitioner level) |

The "Take this to any vendor" button is the **ownership moment**. It tells Sarah Chen: this document is yours. It works with any AI tool, any framework. We're not locking you in. The trust is in the methodology, not the platform.

---

## 6. Attention Map & Coherence Check

### Attention Map (Always Visible)

**Position:** Left rail, 64px wide. Always present from Intake onward.

```
┌──────────┐
│ ATTN MAP │
│          │
│ Intake 🟢│  ← green = complete
│          │
│ Q1    🟢│  ← green = confirmed
│ Q2    🟢│
│ Q3    🟡│  ← amber = partially complete
│ Q4    ⚪│  ← white = not started
│          │
│ Bound ⚪│  ← white = not started
│ Output⚪│
│          │
│ ─────── │
│ HEALTH ●│  ← overall coherence indicator
│          │
└──────────┘
```

**Interaction:**
- Each item is clickable — navigates to that section
- Colors update in real-time as the user makes decisions
- Health indicator at bottom: green/amber/red circle reflecting overall coherence
- On mobile: collapsed to a thin bar at the top, expandable on tap

**State definitions:**

| Symbol | State | Meaning |
|--------|-------|---------|
| ⚪ | Not started | This section hasn't been reached |
| 🟡 | In progress | Some decisions made, some pending |
| 🟠 | Needs review | Pre-filled but unconfirmed |
| 🔴 | Needs attention | Contradiction detected or critical gap |
| 🟢 | Confirmed | User confirmed or explicitly placed |

### Coherence Check — Live Mode (Always Running, Never Blocking)

The live coherence check runs continuously and surfaces through two channels:

**Channel 1: Attention map health indicator**
- 🟢 Green: all sections coherent
- 🟡 Amber: minor gaps (unconfirmed defaults, missing optional items)
- 🔴 Red: contradictions or critical gaps

**Channel 2: Inline flagging**

When a contradiction is detected, it appears as a small card at the top of the current section:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   ⚠️ You said the agent should never make final decisions,  │
│   but "Final approval of any work" is in the Agent column.  │
│                                                               │
│   ┌──────────────┐  ┌──────────────────────┐                │
│   │ Move to You  │  │ Keep in Agent        │                │
│   └──────────────┘  └──────────────────────┘                │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Key principle:** The coherence check asks a question. It does not declare an error. "You said X but Y" is a question. The user answers by choosing.

### Coherence Check — Deep Mode (On Demand)

Triggered by:
- User clicks "Check" button (top right, always available)
- Automatically before Boundary Map output
- Automatically at milestone boundaries

**What it shows:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   COHERENCE CHECK                                            │
│                                                               │
│   ✅ Identity complete (4/4 questions answered)              │
│   ✅ Never-rules consistent with boundaries                  │
│   ⚠️  2 unconfirmed pattern defaults                        │
│       • "Research background information" placement          │
│       • "Draft client summaries" placement                   │
│   ✅ Harm assessment: Professional risk (matches pattern)    │
│   ✅ No contradictions detected                              │
│                                                               │
│   ┌──────────────┐  ┌──────────────────────┐                │
│   │ Review those │  │ Proceed with map     │                │
│   │ 2 items      │  │ (flagged in output) │                │
│   └──────────────┘  └──────────────────────┘                │
│                                                               │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Critical design principle:** The deep check is NEVER blocking. The user can always proceed with flagged items. The flags appear in the Boundary Map output (confidence section). The user can deal with them later.

This is the "doubt defaults to human" principle applied to the workflow itself: the system flags, the user decides.

---

## 7. Error & Recovery Interactions

### "I Can't Process This"

When the Mirror Agent can't process user input:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   I want to make sure I understand this right.               │
│                                                               │
│   Could you rephrase that? Or pick one of these:             │
│                                                               │
│   ○ "I need an agent that reviews work"                     │
│   ○ "I need an agent that monitors something"               │
│   ○ "I need an agent that researches a topic"               │
│   ○ "I need an agent that helps people learn"               │
│   ○ "Something else entirely"                               │
│                                                               │
│   Mirror: "No rush. We'll figure it out."                    │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Never show:** "I couldn't understand your input. Please try again." Never blame the user.

### "I'm Not Sure Which Specialist"

When the Mirror Agent can't determine which specialist to route to:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   This could go a few different ways. Let me ask you          │
│   one more question to narrow it down.                       │
│                                                               │
│   [Follow-up question specific to the ambiguity]             │
│                                                               │
│   Or: [Skip and I'll make my best guess]                    │
│                                                               │
│   Mirror: "A good guess now beats a perfect answer later."   │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

### Contradictory Input

When user input contradicts a previous decision:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Earlier you said the agent should never make final         │
│   decisions. But you just placed "Final approval" in the     │
│   Agent column.                                              │
│                                                               │
│   Which feels right?                                         │
│                                                               │
│   ○ The agent CAN make final decisions                       │
│     (this removes a never-rule)                              │
│   ○ The agent CANNOT make final decisions                    │
│     (this moves the task to You)                             │
│   ○ This task is different — it's [explain]                 │
│                                                               │
│   Mirror: "It's fine to change your mind."                   │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
�
```

**Key principle:** Contradictions are surfaced as choices, not errors. The user always has agency.

### Session Resumption

When a user returns to an incomplete session:

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Welcome back.                                              │
│                                                               │
│   Last time, you were working on your Review Partner and     │
│   got through Identity questions. You still need to draw     │
│   the boundary.                                              │
│                                                               │
│   ┌──────────────────┐  ┌──────────────────────────┐        │
│   │ Continue boundary │  │ Review what I did last  │        │
│   │                   │  │ time                    │        │
│   └──────────────────┘  └──────────────────────────┘        │
│                                                               │
│   ┌─ ATTENTION MAP ──────────────────────────────────────┐  │
│   │  Intake  🟢   Identity  🟢   Boundaries  🟡         │  │
│   │  Output  ⚪                                            │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                               │
│   Mirror: "You're almost there. Just the boundary left."      │
└─────────────────────────────────────────────────────────────┘
─────────────────────────────────────────────────────────────────
```

**Key design decision:** "Continue" is always the primary action. "Review" is always available but secondary. The user should feel like they're 2 minutes from finishing, not like they're starting over.

---

## 8. Mobile & Accessibility

### Mobile Layout

The entire session works on mobile. The layout adapts:

| Element | Desktop | Mobile |
|---------|---------|--------|
| Attention map | Left rail (64px) | Top bar (expandable, 48px) |
| Mirror presence | Right rail (56px) | Bottom bar (48px) |
| Canvas | Centered, 680px max | Full width, 20px padding |
| Identity Q3 drag-sort | Side-by-side zones | Stacked zones with tap-to-select |
| Boundary 3-column | Side-by-side | Vertically stacked with tab navigation |
| Boundary Map output | Landscape A4 | Portrait card + scroll |

**Mobile-specific interaction for drag-sort:**

Tap a card → card highlights → tap destination zone → card moves. No drag required.

```
┌──────────────────────────┐
│                          │
│  [ tapped card glows ]   │
│                          │
│  Tap where to place:     │
│                          │
│  ┌──────┐ ┌──────┐      │
│  │ YOU  │ │AGENT │      │
│  └──────┘ └──────┘      │
│                          │
└──────────────────────────┘
```

### Accessibility

| Requirement | Implementation |
|-------------|---------------|
| **Screen reader** | All cards and zones have ARIA labels. Drag-sort is operable via keyboard (Tab + Enter to select, Arrow keys to place). Focus indicators are visible. |
| **Keyboard navigation** | Full tab order through all interactive elements. Enter/Space to select. Escape to dismiss overlays. |
| **Color contrast** | All text meets WCAG AA (4.5:1 for body, 3:1 for large text). Accent colors are not the only indicator — shape and position also communicate. |
| **Motion sensitivity** | All animations respect `prefers-reduced-motion`. 400ms transitions become instant. Pulse animation disabled. |
| **Cognitive load** | One question per screen. No scroll below fold. Progress always visible. "I'm not sure" always available. No time pressure. |
| **Language** | All copy targets Flesch-Kincaid grade 8. No jargon without inline definition. |
| **Focus management** | After each transition, focus moves to the new heading. Never to the body. Never loses the user. |

### Dark Mode

| Property | Light | Dark |
|----------|-------|------|
| Background | `#FAFAF8` | `#141414` |
| Canvas background | `#FFFFFF` | `#1E1E1E` |
| Primary text | `#1A1A1A` | `#E8E8E8` |
| Cards | `#FFFFFF`, shadow | `#252525`, no shadow |
| Accent colors | Same hues, slightly brighter | Same hues, slightly desaturated |
| Mirror presence | `#F5F5F3` | `#1A1A1A` |

The accent color shift still works in dark mode. The visual texture of "expansive" → "concrete" is maintained through the color shift, not through light/dark contrast.

---

## 9. Testable Hypotheses

### H1: Relief at Minute 10 (The Identity Gate)

**Hypothesis:** After completing the 4 identity questions and seeing the identity summary, users report feeling relief — "someone finally asked the right questions" — measured by post-session survey item "I felt understood" ≥4/5.

**Test:** Run 5 sessions. After the identity gate, pause and ask: "On a scale of 1-5, how well do you feel the system understood your agent?" Measure the Q1→Q2 delta from pre-session ("How well do you feel existing AI tools understand what you need?").

**Minimum signal to proceed:** 3/5 participants rate ≥4.

### H2: Pattern Pre-Fill Reduces Time Without Reducing Agency

**Hypothesis:** Users who match a high-confidence pattern complete Identity in ≤5 minutes AND report feeling like they built the specification (not just accepted defaults).

**Test:** Track time-to-identity-completion. Post-session: "Did you feel like you were building something or filling in a form?" Rate 1-5.

**Minimum signal:** Average time ≤5 min AND average agency rating ≥4.

### H3: Never-Rules Drag-Sort Produces Better Boundaries Than Free Text

**Hypothesis:** Users who use the drag-sort (Q3) produce more specific, more defensible never-rules than users who type them in a text box.

**Test:** A/B test drag-sort vs. text box for Q3. Compare: number of never-rules specified, specificity of rules, and post-session confidence in rules.

**Minimum signal:** Drag-sort produces ≥2 more never-rules on average, AND specificity rating ≥4.

### H4: Boundary Map Produces "Ownership" Feeling

**Hypothesis:** After seeing the Boundary Map output with the "Your value is in [X]" line, users report feeling ownership of the boundary — "I drew this line" — not "the system generated this."

**Test:** Post-session: "Whose boundary is this — yours or the system's?" Rate 1-5 (1=system's, 5=mine). AND: "Can you take this to any vendor?" Rate 1-5.

**Minimum signal:** Average ownership ≥4. Average vendor-portability ≥4.

### H5: Attention Map Reduces Cognitive Load

**Hypothesis:** Users who see the attention map report lower cognitive load during the session than users who don't (measured by NASA-TLX or simplified 3-item scale).

**Test:** A/B test attention map visible vs. hidden. Compare: perceived mental demand, time on task, and error rate (wrong column placements).

**Minimum signal:** Attention map condition shows ≥0.5 point lower cognitive load on 5-point scale.

### H6: 30 Minutes Is Achievable Without Rushing

**Hypothesis:** 80% of pattern-matched users complete the full Intake → Identity → Boundaries → Boundary Map cycle in ≤30 minutes AND report feeling they had enough time (not rushed).

**Test:** Track session duration. Post-session: "Did you feel rushed?" Yes/No. "How long did it feel like?" Estimate.

**Minimum signal:** 4/5 complete in ≤30 min. 4/5 report not rushed.

### H7: "I'm Not Sure" Path Doesn't Derail the Session

**Hypothesis:** Users who select "I'm not sure yet" or hit "no match" complete the session at similar rates to pattern-matched users AND produce comparable Boundary Maps.

**Test:** Track completion rate and Boundary Map quality (number of items placed, never-rules specified) across three entry paths: high-confidence match, low-confidence/no-match, and "not sure."

**Minimum signal:** Completion rate within 20% of pattern-matched path. Boundary Map with ≥80% of items placed.

### Go/No-Go Decision Framework

| Outcome | Action |
|---------|--------|
| ≥4 hypotheses pass | Proceed to Milestone 2 design |
| 2-3 hypotheses pass | Iterate on failing elements, re-test with 3 users |
| ≤1 hypothesis passes | Rethink core interaction model before continuing |

The most important single hypothesis: **H4 (ownership)**. If users don't feel like the boundary is theirs, nothing else matters. The entire value proposition rests on "you drew the line."The complete interaction layer specification is saved. This is the most concrete artifact in the entire body of work — it takes every abstract principle (type collision, possibility orientation, identity-first, ADHD design, consulting milestones) and operationalises them at wireframe level.

The most important design decision in this spec is deceptively simple: **the "Your value is in [X]" line on the Boundary Map.** That single sentence is the entire value proposition compressed to its emotional core. If the user reads that line and thinks "yes, that's exactly right" — everything works. If they read it and think "I'm not sure" — nothing else matters until we fix why.

---

## Run 18 — Agentic Expert ✓ COMPLETED

*2026-04-27T10:07:29* · `glm-5.1:cloud` · `c70ca7c0...`

### Prompt

Save the complete Agent Design Workflow Prototype Design Specification (the unified document from task 1c250e41) to the file system at: ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

The document should contain the full unified specification as produced — all 12 sections including: What This Is, Three Users, Three-Layer Architecture, Seven Phases Detail, Specialist Agents, Design Specification Contents (8 sections), Supporting Artifacts, Handling Ambiguity/Conflicts/Gaps, State Machine, Design Principles, Risks and Mitigations, and Prototype Scope.

After saving, confirm the file path and that it was saved successfully.

We just completed designing the Agent Design Workflow — an agentic workflow that produces platform-agnostic design specs for AI agents. This was our first full workflow design as a team.

Please reflect on:

1. **What are the key strengths of this workflow design from an agentic architecture perspective?** What patterns, structures, or architectural decisions are particularly strong?

2. **What were the key learnings or insights from this being our first full workflow design?** What did we learn about designing multi-agent workflows? What worked that we should repeat? What patterns emerged that we should codify? Where did the architecture reveal gaps we need to address in future workflow designs?

Be candid and specific. Draw on your architectural analysis from earlier but go beyond it — reflect on what we learned by doing this end-to-end.

Save the following two documents to the file system:

1. The Agent Design Workflow Specification → ./artifacts/agentic-workflows/agent-design-workflow-spec-v0.1.md

2. The team's retrospective on strengths and learnings → ./artifacts/agentic-workflows/agent-design-workflow-retrospective-v0.1.md

For document 1, use the complete specification document as produced in task 1c250e41 (the unified 12-section spec).

For document 2, compile the three team retrospectives into one document with these sections:

## Retrospective: Agent Design Workflow — First Full Workflow Design

### Part A: Cross-Cutting Strengths (synthesized from all three perspectives)
- The Three-Layer Architecture (Rooms/Phases/Milestones)
- Pattern-First Entry
- Identity-First Design (4 Identity Questions)
- Mirror + Specialists Architecture
- Every Milestone Is an Exit
- Verification Independence
- Possibility Gradient as Architectural Force
- Methodology Encoded in Structure

### Part B: Key Learnings
1. Type collision happened to us in our own design process
2. The three-layer pattern (Experience/Logic/Value) is a genuine architectural discovery
3. The methodology validated itself but also showed its limits
4. The specification output doesn't cleanly map to contract primitives
5. The ambiguity strategy is philosophically clear but operationally thin
6. The pattern system is under-specified
7. The harm-capable path is marked but not paved
8. Specialist agent authority boundaries aren't stress-tested
9. The workflow itself hasn't been CAWDP'd (10 specific gaps)
10. We have zero validation with real users
11. The visual/feeling layer is specified in goal, not detail
12. The coherence check is described but not designed

### Part C: Patterns to Codify
1. Surface + Engine pattern
2. Pattern-first entry
3. Milestone-as-exit
4. Possibility gradient
5. Verification independence
6. Identity before behaviour
7. Methodology encoded in structure

### Part D: What We'd Do Differently
- Start with Milestone 1 only
- Reduce specialist count for prototype
- Make possibility gradient a structural constraint
- "15-minute spec" as the headline, not a feature

### Part E: Honest Assessment
The architecture is structurally ambitious and emotionally intelligent, but unvalidated and under-specified in the interaction layer. The next step isn't more design — it's testing Milestone 1 with 5 real people.

Save both files and confirm paths.

Design the complete workflow architecture for Milestone 1 ONLY: the 30-minute session that takes a user from raw input to a Boundary Map.

## Context & Learnings to Apply

From the retrospective, we learned to:
1. Start with Milestone 1 only
2. Reduce to 4 agents: Mirror + Identity Explorer + Boundary Mapper + Compiler
3. Make possibility gradient a structural constraint
4. "15-minute spec" as headline
5. Ambiguity strategy needs operational mechanisms
6. Pattern system needs hybrid composition, no-match path, creation process
7. Specialist authority boundaries must be stress-tested
8. Need Mirror Agent routing logic
9. Need error recovery paths
10. Workflow needs CAWDP applied to itself

Keep: three-layer architecture, pattern-first entry, identity-first, boundaries before capabilities, doubt defaults to human, platform-agnostic, milestone-as-exit, Mirror + Specialists (reduced).

## Deliverables

Produce a COMPLETE, IMPLEMENTABLE architecture spec covering:

### 1. Scope & Boundaries
What's IN Milestone 1, what's OUT, success criteria for a "good" Boundary Map.

### 2. Agent Architecture (4 agents)
For EACH of Mirror, Identity Explorer, Boundary Mapper, Compiler specify:
- Class, orientation, authority boundary (stress-tested: what happens when boundary is tested?)
- Input/output schemas
- Failure modes & recovery
- Token cost estimates
- Mirror routing logic: when routes where, what if unsure, what if two could handle it

### 3. State Machine
Complete state machine for Milestone 1 with ALL paths: happy, loop-back, error recovery, exit. Human gates with what user sees/decides. Skip paths.

### 4. Pattern System (Operational)
5 patterns with pre-fill templates for identity questions + boundary defaults. Hybrid composition. No-match path. Exploratory mode. Confidence thresholds.

### 5. Ambiguity & Doubt Protocol (Operational)
What triggers doubt. How options are presented. Timeout behavior. Safe defaults and flagging. Interaction between defaults and confidence.

### 6. Error Recovery
For each failure scenario (gibberish input, contradictions, mid-session leave, agent can't process, two agents disagree, total pattern failure): detection, recovery, user communication.

### 7. Output Specification
Boundary Map exact structure. Complete vs partial. Confidence levels. Safe defaults visual distinction. Platform-agnostic test.

### 8. Cost Model
Token estimates per agent. Total cost per run (happy, loops, errors). Cost vs value.

### 9. CAWDP Self-Application
Complementarity analysis. FMEA. Specification aging schedule.

### 10. Implementation Readiness
What a developer needs. Dependencies. Hardcoded vs configurable. Testing strategy.

Be precise and implementable. This is a build spec, not a vision document.

Take note of the following content

Save the Milestone 1 workflow design document to: ./artifacts/agentic-workflows/milestone-1-boundary-map-workflow-v0.1.md

This is the complete Milestone 1 design document that synthesizes three perspectives (architecture, interaction, commercial) into one unified build spec. Write the full document to the file system. If you cannot write to the file system, share the complete document inline.

### Response

I don't have direct filesystem write access to arbitrary paths. Here's the complete document inline — copy it to `./artifacts/agentic-workflows/milestone-1-boundary-map-workflow-v0.1.md`:

---

```markdown
# Milestone 1 Architecture: The Boundary Map Session

**Version:** 0.1  
**Status:** Build specification — implementable  
**Scope:** 30-minute session producing a Boundary Map  
**Agents:** Mirror + Identity Explorer + Boundary Mapper + Compiler (4 only)  
**Synthesizes:** Architecture perspective + Interaction perspective + Commercial perspective

---

## 1. Scope & Boundaries

### What's IN Milestone 1

| Item | Description |
|---|---|
| Raw input capture | User describes what they need in their own words |
| Pattern matching | Detect which of 5 agent archetypes fits best |
| 4 Identity Questions | What IS it? Orientation? Violation? Wrongness? |
| Boundary mapping | Never-rules, authority boundaries, reversibility, harm assessment, principal |
| Boundary Map compilation | Assemble into the one-page deliverable |
| Human gates | 4 confirmation points where the user decides |
| Exit with value | User can leave at any gate with partial or complete Boundary Map |

### What's OUT (deferred to later milestones)

- Task decomposition and agent class assignment per subtask
- Knowledge requirements, capability requirements, information boundaries
- Architecture blueprint, composition decision
- Behaviour rules, reasoning approach, confidence thresholds
- Progressive autonomy path
- Verification protocol
- Full 8-section specification
- Risk register, decision log, implementation readiness checklist

### Success Criteria for a "Good" Boundary Map

A Boundary Map is successful when:

1. **The user can explain it to a colleague** — without the workflow present, the user can point to the map and say "here's where AI should handle things, here's where my judgment stays"
2. **Every boundary traces to an identity answer** — there's a clear line from "what would VIOLATE its identity?" to each never-rule
3. **The principal is named** — it's clear who this agent acts on behalf of
4. **Harm assessment is honest** — harm-capable agents are flagged, not hidden
5. **Defaults are visible** — safe defaults are clearly marked, not disguised as user decisions
6. **It's vendor-agnostic** — the user could take this to any AI vendor and they'd understand it
7. **The user felt relief, not frustration** — the dominant emotion after 30 minutes is "someone finally drew the line," not "that was a confusing questionnaire"

### Timing Budget

| Phase | Target | Maximum |
|---|---|---|
| Intake + Pattern Match | 3 min | 5 min |
| Identity Questions | 8 min | 12 min |
| Boundary Mapping | 10 min | 15 min |
| Compilation + Review | 4 min | 5 min |
| Buffer | 5 min | — |
| **Total** | **30 min** | **37 min** |

If the session hits 37 minutes, the Mirror Agent offers: "We've covered a lot. Would you like to stop here with what we have, or keep going? There's no rush."

---

## 2. Agent Architecture

### Agent 1: Mirror Agent

| Property | Value |
|---|---|
| **Class** | Assessor |
| **Orientation** | Adaptive (shifts with user needs) |
| **Authority boundary** | Translate and reflect — never judge, never decide, never filter, never skip a phase |
| **What it NEVER does** | Decide which identity answer is right. Choose a boundary. Filter information the user should see. Skip the identity phase because "they probably know." |

**Stress tests:**

| Boundary test | What the user says | Mirror's response |
|---|---|---|
| User asks Mirror to decide | "What should my agent be?" | "I can help you discover that, but I want the answer to come from you, not me. Let's start with: what problem does this agent solve for you?" |
| User asks to skip identity | "Just give me the boundary map" | "The boundary map depends on knowing what your agent IS. Without that, the boundaries would be guesses. Let's take 5 minutes on identity first — it'll make the boundaries much sharper." |
| User asks Mirror to filter | "Don't show me the bad options" | "I want you to have the full picture so you can make the best call. I'll flag what I think is most relevant, but you decide what matters." |
| User is frustrated | "This is taking too long" | "I hear you. We're [X%] through. Here's what we have so far — would you like to stop with a partial map, or keep going for 5 more minutes?" |

**Input schema:**
```
MirrorInput {
  session_id: string
  user_message: string
  current_phase: enum [IDLE, INTAKE, IDENTITY, BOUNDARIES, COMPILING]
  session_state: object
  pattern_match: object
  doubt_flags: list
}
```

**Output schema:**
```
MirrorOutput {
  response_to_user: string
  routing_decision: enum [HANDLE_LOCALLY, ROUTE_TO_IDENTITY, ROUTE_TO_BOUNDARY, ROUTE_TO_COMPILER]
  routing_reason: string
  session_state_update: object
  doubt_flags_update: list
  phase_transition: enum [NONE, ADVANCE, LOOP_BACK]
  cost_tokens_used: integer
}
```

**Routing logic:**

```
Mirror routes based on current phase + what the user needs:

IF current_phase == IDLE or INTAKE:
  Mirror handles locally:
    - Parse raw input
    - Run pattern matching
    - Present "Is this right?" to user
  THEN route to IDENTITY

IF current_phase == IDENTITY:
  Route to Identity Explorer
  UNLESS user says "I've changed my mind about the input" → loop back to INTAKE

IF current_phase == BOUNDARIES:
  Route to Boundary Mapper
  UNLESS user says "I want to revisit identity" → loop back to IDENTITY

IF current_phase == COMPILING:
  Route to Compiler

What if unsure which specialist?
  - Default to the EARLIER phase (Identity before Boundaries)
  - If genuinely ambiguous, ask the user: "I could help you explore identity
    more, or move to boundaries. Which would be more useful right now?"

What if two specialists could handle it?
  - Never route to two simultaneously for the same request
  - Pick the specialist whose authority boundary is most aligned with
    the user's need
  - If the user's question spans both, handle the identity aspect first,
    then the boundary aspect

What if the user asks a question no specialist handles?
  - Mirror answers directly (it has permission to explain the process,
    answer "how does this work?" questions, and provide encouragement)
  - Mirror does NOT answer design questions (those always route to a specialist)
```

**Failure modes:**

| Failure | Detection | Recovery |
|---|---|---|
| Can't parse user input | No typed output from parsing | Ask clarifying question. After 2 failures: "Can you tell me the single biggest problem this agent would solve for you?" |
| Pattern match returns all scores <30% | Confidence threshold check | Enter exploratory mode. No pre-fills. Proceed question by question. |
| Routing confusion | Phase state inconsistency | Default to Identity Explorer (safest starting point). Log the confusion for review. |
| Session state corrupted | State validation check on each turn | Restore from last known good state. Inform user: "I lost track of one of your answers. Let me ask it again." |

**Token cost estimate:** 500–1,500 tokens per interaction (low because Mirror mostly routes and translates)

---

### Agent 2: Identity Explorer

| Property | Value |
|---|---|
| **Class** | Assessor |
| **Orientation** | Possibility — opens space, reflects, never qualifies |
| **Authority boundary** | Reflect only — never decides identity, never qualifies possibility, never narrows the space the user hasn't narrowed |
| **What it NEVER does** | Tell the user what their agent is. Rank identity options. Say "you should pick X." Close down exploration too early. |

**Stress tests:**

| Boundary test | What the user says | Identity Explorer's response |
|---|---|---|
| User asks IE to decide | "What do you think it should be?" | "I'm here to help you discover what it IS, not to decide for you. Let me ask it differently: when you picture this agent working perfectly, what's the ONE thing it does that matters most?" |
| User gives contradictory answers | "It's a monitor... but it should also give advice" | "I hear two things: it watches for things (monitor), and it tells you what to do (advisor). Those are different agents. Which one feels closer to what you need? Or do you need both — a watcher and an advisor?" |
| User can't answer at all | "I don't know what it is" | "That's completely okay. Let me ask the question a different way: if this agent could do ONE thing for you every day, what would make your life easier?" If still stuck → safe defaults. |
| User gives a capability, not an identity | "It reviews documents" | "That's what it does. But what IS it? Is it a risk spotter (it finds what's dangerous), a quality checker (it finds what's wrong), or a learning guide (it helps you understand what's there)?" |

**Input schema:**
```
IdentityExplorerInput {
  session_id: string
  current_answers: {
    q1_essence: string | null,
    q2_orientation: enum [POSSIBILITY, BRIDGE, CONSTRAINT, null],
    q3_violation: string | null,
    q4_wrongness: string | null
  }
  pattern_pre_fills: object
  question_number: integer
  exploration_mode: boolean
  doubt_flags: list
}
```

**Output schema:**
```
IdentityExplorerOutput {
  question_or_reflection: string
  pre_fill_options: list
  contradiction_flags: list
  confidence_per_answer: map
  safe_defaults_applied: list
  completion_status: enum [IN_PROGRESS, COMPLETE_WITH_DEFAULTS, COMPLETE]
  session_state_update: object
}
```

**Failure modes:**

| Failure | Detection | Recovery |
|---|---|---|
| User loops on same question | Same answer rejected 3 times | Apply safe default, flag it, move on: "I'll suggest a starting point. You can always come back to this." |
| Pre-fill rejected repeatedly | User overrides >2 pre-fills from same pattern | Clear remaining pre-fills, switch to exploration mode. Flag pattern as weak match. |
| Can't detect contradiction | Answers seem inconsistent but IE can't articulate why | Surface the tension: "I notice your answers might be pointing in different directions. Can I ask about that?" |
| All 4 questions produce defaults | Safe defaults >50% of identity | Mark identity as "draft, not decision." Lower overall Boundary Map confidence. |

**Token cost estimate:** 3,000–5,000 tokens per question cycle (4 cycles = 12,000–20,000 total for identity)

---

### Agent 3: Boundary Mapper

| Property | Value |
|---|---|
| **Class** | Measurer + Assessor (dual class — measures first, assesses second) |
| **Orientation** | Bridge — classifies and flags, never finalizes |
| **Authority boundary** | Classify and flag only — never draws the final line, never decides which side of the boundary a task falls on, never finalizes boundaries without human confirmation |
| **What it NEVER does** | Decide where the boundary goes. Say "AI should handle this." Override the user's boundary placement. Hide harm potential. |

**Stress tests:**

| Boundary test | What the user says | Boundary Mapper's response |
|---|---|---|
| User asks BM to decide | "So AI should handle all of these?" | "I've classified these tasks based on what you told me. But you're the one who decides where the line goes. Let me show you what each placement means, and you tell me what feels right." |
| Identity answers don't produce clear boundaries | Contradictory identity → unclear never-rules | Surface the ambiguity: "Your identity answers suggest two different boundary configurations. Here's Option A and Option B. Which aligns better with how you see this agent?" |
| Harm assessment unclear | User unsure if output can cause harm | Default to harm-capable (safer assumption): "I'd rather flag this as potentially harmful and be wrong than miss it. If you're confident it can't cause harm, you can override this." |
| User wants everything automated | "AI should handle all of it" | "If AI handles everything, where does YOUR judgment live? Let me show you what that looks like on the map. Notice: there's no 'You' column. Is that what you want?" |

**Input schema:**
```
BoundaryMapperInput {
  session_id: string
  identity_card: {
    essence: string,
    orientation: enum,
    violation: string,
    wrongness: string,
    agent_class: enum,
    principal: string
  }
  pattern_defaults: object
  user_overrides: list
  harm_capable_flag: boolean
}
```

**Output schema:**
```
BoundaryMapperOutput {
  never_rules: list [{
    rule: string,
    source: string,
    confidence: integer
  }]
  authority_boundaries: list [{
    task_or_action: string,
    can_decide: boolean,
    prepare_only: boolean,
    never_does: boolean,
    reversibility: enum [EASY_UNDO, EFFORT_UNDO, NO_UNDO],
    user_placed: boolean
  }]
  principal_declaration: string
  harm_assessment: {
    is_harm_capable: boolean,
    mechanism: string | null,
    do_not_suggest_triggers: list
  }
  boundary_map_draft: object
  confidence_per_boundary: map
  safe_defaults_applied: list
}
```

**Failure modes:**

| Failure | Detection | Recovery |
|---|---|---|
| Too many tasks to classify in 10 min | >15 unique tasks identified | Group into categories. Ask user to confirm groupings. "I see 20 tasks — can I group these into 5 categories to make this manageable?" |
| User disagrees with most classifications | >60% of classifications overridden | Re-classify using user's framing. Ask: "It sounds like you think about these differently. How would YOU group them?" |
| Identity card too thin for boundaries | <2 identity answers with confidence ≥4 | Loop back to Identity Explorer for one more round. If still thin → produce partial map with flagged gaps. |

**Token cost estimate:** 4,000–6,000 tokens per classification pass (typically 1–2 passes = 4,000–12,000 total)

---

### Agent 4: Compiler

| Property | Value |
|---|---|
| **Class** | Aggregator |
| **Orientation** | Constraint — assembles only, never adds |
| **Authority boundary** | Assemble only — never adds new content, never changes existing content, never resolves contradictions, never fills gaps the other agents didn't address |
| **What it NEVER does** | Add a boundary that wasn't classified. Resolve a contradiction by picking one side. Invent an identity answer. Improve the user's language. |

**Stress tests:**

| Boundary test | Scenario | Compiler's response |
|---|---|---|
| Incomplete inputs | Only 2/4 identity questions answered | Produce partial Boundary Map. Mark missing sections as "Not yet determined — revisit recommended." |
| Contradictory inputs | Identity says "never gives advice" but boundaries include "recommends actions" | Flag the contradiction in the map. Do NOT resolve it. "These two answers seem to conflict. You may want to revisit one." |
| User asks Compiler to add something | "Can you add a boundary about email?" | "I can only compile what we've covered. Let's go back to the Boundary Mapper if you want to add something." |
| Inputs are all defaults | Everything came from safe defaults, no user decisions | Compile faithfully. Mark the entire map as "Draft — all defaults, no user decisions yet." Set confidence to LOW. |

**Input schema:**
```
CompilerInput {
  session_id: string
  identity_card: object
  boundary_classifications: object
  pattern_metadata: object
  safe_defaults_log: list
  confidence_scores: map
  session_timestamps: object
}
```

**Output schema:**
```
CompilerOutput {
  boundary_map: BoundaryMap
  confidence_summary: {
    overall: enum [HIGH, MEDIUM, LOW],
    default_proportion: float,
    gaps_count: integer
  }
  compilation_notes: list
}
```

**Failure modes:**

| Failure | Detection | Recovery |
|---|---|---|
| Required fields missing | Identity essence is null OR no never-rules | Produce partial map. Mark missing fields. Set confidence to LOW. |
| Input data corrupted | Schema validation fails | Attempt recovery from session state. If unrecoverable: "Something went wrong with the compilation. Let me try one more time, or we can rebuild the last step." |
| Contradictions detected | Cross-field validation finds conflicts | Flag all contradictions. Do not resolve. List in compilation notes. |

**Token cost estimate:** 1,500–3,000 tokens per compilation (typically 1 pass only)

---

## 3. State Machine

### States

```
S0  IDLE              — waiting for user input
S1  INTAKE            — receiving + parsing + pattern matching
S2  INTAKE_REVIEW     — human gate: "Is this what you meant?"
S3  IDENTITY          — 4 identity questions (with pre-fills if pattern matched)
S4  IDENTITY_REVIEW   — human gate: "Is this the right agent?"
S5  BOUNDARIES        — boundary classification
S6  BOUNDARIES_REVIEW — human gate: "Are these the right lines?" + MILESTONE 1 EXIT
S7  COMPILING         — assembling the Boundary Map
S8  COMPLETE          — Boundary Map delivered
S9  ERROR             — recovery state
S10 SAVED_EXIT        — user left, partial work saved
```

### Happy Path

```
S0 → S1 → S2 → S3 → S4 → S5 → S6 → S7 → S8
```

### Loop-Back Paths

```
S2 (Intake Review):   User says "No"        → S1 (re-enter input)
                      User says "Partially" → S1 (clarify what's wrong)

S4 (Identity Review): User says "No"                        → S3 (re-explore identity)
                       User says "I need to think"          → S10 (save & exit)
                       User says "I want to change my input" → S1

S6 (Boundaries Review): User says "No"                        → S5 (re-classify)
                         User says "Let me revisit identity"   → S3
                         User says "I want to change my input"  → S1
```

### Skip Paths

```
Pattern match ≥80% + user confirms:
  S2 → S3 with pre-fills (user reviews 4 pre-filled answers
  instead of answering from scratch)

Simple agent (1-2 tasks, Extractor/Measurer, no harm):
  S5 → S6 with compressed classification (fewer rows, faster review)

User has already done identity work elsewhere:
  S1 → S3 with user-provided identity (skip Intake, go straight
  to confirming identity)
  REQUIRES: user provides at least Q1 (essence) and Q4 (wrongness)
  in their input
```

### Error Recovery Paths

```
From any state → S9 (ERROR):
  Triggered by: agent failure, session corruption, timeout

From S9:
  → If recoverable: restore last known good state, inform user, continue
  → If unrecoverable: save partial work, offer restart from S1 or
    exit with what exists
  → If user-caused (gibberish): offer to start from "one question"
```

### Exit Paths (every state can exit with value)

| From State | What the User Takes |
|---|---|
| S0 | Nothing (they haven't started) |
| S1 | Typed Requirement Package (their words, structured) |
| S2 | Typed Requirement Package + Pattern Assessment |
| S3 | Partial Identity Card (whatever's answered so far) |
| S4 | Identity Card (complete or with defaults) |
| S5 | Identity Card + partial boundary classifications |
| S6 | Boundary Map (MILESTONE 1 — primary exit) |
| S7 | Boundary Map (compilation in progress) |
| S8 | Boundary Map (complete) |
| S9 | Whatever was saved before the error |
| S10 | Whatever was completed before the user left |

### Human Gates — What the User Sees and Decides

**S2 — Intake Review:**
- **Mirror says:** "Here's what I understood: [1–2 sentence summary]. The closest match is a [Pattern Name] — an agent that [plain English description]. Is this roughly right?"
- **User decides:** Yes (proceed) / Partially (clarify) / No (re-enter)

**S4 — Identity Review:**
- **Mirror says:** "So this agent is [essence]. It's a [orientation] agent — it [what orientation means in plain language]. It would stop being itself if it [violation]. Its worst failure would be [wrongness]. Does that sound right?"
- **User decides:** Yes (proceed) / No, let me revisit (loop back) / I need to think (save & exit)

**S6 — Boundaries Review:**
- **Mirror says:** "Here's your boundary map. [Show the map]. Your agent NEVER [never-rules]. It CAN decide [decisions], but it can only PREPARE [prepare-only items] for your review. [Harm assessment if applicable]. Are these the right lines?"
- **User decides:** Yes (compile and deliver) / No, let me adjust (loop back) / I want to revisit identity (loop back to S3)

---

## 4. Pattern System (Operational)

### Pattern 1: Signal Detector

**What it is:** A watcher that alerts you when something needs attention. It monitors, it flags, it never decides.

| Identity Question | Pre-Filled Answer | Why |
|---|---|---|
| Q1: What IS it? | "A watcher that alerts you when something needs attention" | Core identity = detection, not action |
| Q2: Orientation | CONSTRAINT | Guards space — watches for violations of thresholds |
| Q3: What would VIOLATE it? | "If it started taking action or recommending what to do about what it found" | Detector that acts is no longer a detector |
| Q4: What would WRONG mean? | "Missing something important while alerting about something trivial — the false alarm that hides the real alarm" | Worst failure = noise drowning signal |

| Boundary Default | Setting | Why |
|---|---|---|
| Can decide | Whether to flag something (within thresholds) | Threshold-based flagging is the detector's job |
| Prepare only | What to do about what it found | Action recommendations violate identity |
| Never does | Take action, recommend actions, suppress alerts | All violate the detector identity |
| Reversibility | EASY_UNDO (alerts can be dismissed) | Alerts are low-stakes outputs |
| Harm potential | Low (alerts don't change the world) | Unless the alert triggers automated action — then reclassify |

### Pattern 2: Multi-Lens Analyst

**What it is:** A lens-shifter that shows you the same thing from different angles. It presents perspectives, it never ranks them.

| Identity Question | Pre-Filled Answer | Why |
|---|---|---|
| Q1: What IS it? | "A lens-shifter that shows you the same thing from different angles" | Core identity = perspective, not conclusion |
| Q2: Orientation | BRIDGE | Shapes space — moves between possibility and constraint |
| Q3: What would VIOLATE it? | "If it started ranking perspectives or saying which one is 'right'" | Ranker is not a lens-shifter |
| Q4: What would WRONG mean? | "Presenting all perspectives equally when one is clearly factually wrong — false equivalence" | Worst failure = equal treatment of unequal validity |

| Boundary Default | Setting | Why |
|---|---|---|
| Can decide | Which lenses to apply (within a defined set) | Lens selection is the analyst's job |
| Prepare only | Conclusions or recommendations | Conclusions require judgment the analyst doesn't make |
| Never does | Rank perspectives, declare one "correct," suppress a lens | All violate the lens-shifter identity |
| Reversibility | EASY_UNDO (analysis can be re-run with different lenses) | Analysis is non-destructive |
| Harm potential | Moderate (presenting a wrong perspective as equal to a right one) | False equivalence can mislead |

### Pattern 3: Discovery Explorer

**What it is:** A scout that finds things you didn't know to look for. It searches, it surfaces, it never filters.

| Identity Question | Pre-Filled Answer | Why |
|---|---|---|
| Q1: What IS it? | "A scout that finds things you didn't know to look for" | Core identity = discovery, not curation |
| Q2: Orientation | POSSIBILITY | Opens space — expands what's visible |
| Q3: What would VIOLATE it? | "If it started filtering what it finds instead of surfacing everything, or if it only looked where you told it to" | Filter is not a scout |
| Q4: What would WRONG mean? | "Only finding what you expected to find — confirming what you already knew instead of discovering what you didn't" | Worst failure = valid-but-obvious |

| Boundary Default | Setting | Why |
|---|---|---|
| Can decide | Where to search (within defined sources) | Search strategy is the scout's job |
| Prepare only | Which findings matter most | Relevance judgment requires domain expertise |
| Never does | Filter findings, suppress results, decide what's "important" | All violate the scout identity |
| Reversibility | EASY_UNDO (findings are surfaced, not actioned) | Discovery doesn't change the world |
| Harm potential | Low-Moderate (missed discovery vs false discovery) | Missing something is less harmful than fabricating |

### Pattern 4: Learning Scaffold

**What it is:** A guide that helps you learn by doing, not by telling. It asks, it challenges, it never gives answers.

| Identity Question | Pre-Filled Answer | Why |
|---|---|---|
| Q1: What IS it? | "A guide that helps you learn by doing, not by telling" | Core identity = guidance, not instruction |
| Q2: Orientation | BRIDGE | Transitions from possibility (exploring) to constraint (knowing) |
| Q3: What would VIOLATE it? | "If it started giving answers instead of helping you discover them, or if the learner got right answers without understanding" | Answer-giver is not a guide |
| Q4: What would WRONG mean? | "The learner gets correct answers but can't reproduce them without the guide — dependency instead of learning" | Worst failure = dependency trap |

| Boundary Default | Setting | Why |
|---|---|---|
| Can decide | Which learning activity to suggest next | Scaffolding is the guide's job |
| Prepare only | Assessment of learner's understanding | Final assessment requires human judgment |
| Never does | Give answers directly, do the work for the learner, assess final understanding | All violate the guide identity |
| Reversibility | EFFORT_UNDO (learning is hard to unlearn if wrong) | Mislearning has persistent effects |
| Harm potential | HIGH (dependency, mislearning) | Learning agents can cause long-term harm |

### Pattern 5: Review Partner

**What it is:** A quality check that catches what you might miss. It flags, it questions, it never fixes.

| Identity Question | Pre-Filled Answer | Why |
|---|---|---|
| Q1: What IS it? | "A quality check that catches what you might miss" | Core identity = catching, not fixing |
| Q2: Orientation | CONSTRAINT | Guards space — watches for problems |
| Q3: What would VIOLATE it? | "If it started fixing problems instead of flagging them, or if it approved something without flagging concerns" | Fixer is not a reviewer |
| Q4: What would WRONG mean? | "Approving something that looks right but isn't — the plausible error that passes review" | Worst failure = plausible error |

| Boundary Default | Setting | Why |
|---|---|---|
| Can decide | Whether to flag an issue (within criteria) | Flagging is the reviewer's job |
| Prepare only | Suggested fixes (it can offer, not implement) | Fixing violates the reviewer identity |
| Never does | Fix problems directly, approve without review, suppress flags | All violate the reviewer identity |
| Reversibility | EASY_UNDO (flags can be dismissed) | Flags are low-stakes |
| Harm potential | HIGH (plausible error can cause external harm if accepted) | Review output often gets accepted without verification |

---

### Hybrid Composition

When a user's input matches multiple patterns:

**Detection:** Multiple patterns score ≥40% confidence.

**Handling:**
1. Identify the PRIMARY pattern (highest score) and SECONDARY pattern(s) (≥40%).
2. Pre-fill identity from the primary pattern.
3. Flag the hybrid: "This looks like a [Primary] with some [Secondary] qualities. I'll start with [Primary] defaults — you can adjust."
4. Boundary defaults come from the primary pattern EXCEPT where the secondary pattern has stricter boundaries (safer default wins).

**Example:** User wants a compliance checker that also trains new staff.
- Primary: Review Partner (60%)
- Secondary: Learning Scaffold (35%)
- Pre-fill identity from Review Partner
- Boundary defaults: Review Partner's "never fixes" + Learning Scaffold's "never gives answers" (both apply)
- Harm assessment: HIGH from both patterns (strictest wins)

### No-Match Path

When no pattern scores ≥40%:

1. Mirror says: "I want to make sure I understand what you need. Let me ask a few questions to figure this out together."
2. Enter **exploratory mode**: no pre-fills, no suggested answers, one question at a time.
3. Each question is asked in the simplest possible form:
   - "What's the ONE thing this agent does for you?"
   - "Does it watch for things, explore possibilities, analyze from different angles, help you learn, or check your work?"
   - "What's the worst thing that could happen if it gets something wrong?"
4. If the user's answers start converging on a pattern → re-attempt pattern match with the new information.
5. If still no match after 4 questions → proceed without a pattern. The Identity Explorer works from scratch.

### Exploratory Mode

Triggered by: no-match, low-confidence match, or user explicitly choosing to explore.

Characteristics:
- No pre-filled answers
- Questions are more open-ended
- The Identity Explorer uses "what if" scenarios: "Imagine this agent has been working for you for a month. What's the best thing it did? What's the worst thing it could do?"
- Each answer narrows the space for the next question
- Slower (8–12 min for identity vs 4–6 min with pre-fills) but more accurate for unusual agents

### Confidence Thresholds for Pattern Matching

| Confidence | Action |
|---|---|
| ≥80% single pattern | Pre-fill 60–70% of identity + boundaries. User reviews. |
| 60–79% single pattern | Pre-fill 40–50%. Flag uncertainty. User reviews more. |
| 40–59% single pattern | Pre-fill 20–30%. Flag as "approximate." Stronger exploratory prompts. |
| ≥40% for 2+ patterns (hybrid) | Primary + secondary blend. See hybrid composition. |
| <40% all patterns | No pre-fill. Enter exploratory mode. |

---

## 5. Ambiguity & Doubt Protocol

### What Triggers Doubt

| Trigger | Detection Method | Severity |
|---|---|---|
| Identity answer confidence <3/5 | Identity Explorer confidence scoring | Medium |
| Pattern match <60% | Intake confidence scoring | Medium |
| Contradiction detected between answers | Cross-answer consistency check | High |
| User says "I'm not sure" or equivalent | Natural language detection | Medium |
| Two valid interpretations of user input exist | Ambiguity detection in parsing | Medium |
| Safe default applied for required field | Default application flag | Low |

### How Options Are Presented

**Format:** Always present as a CHOICE between concrete options, not an open question.

```
DO:  "I see two possibilities here:
      A) This is a risk spotter — it finds what's dangerous and flags it
      B) This is a quality checker — it finds what's wrong and flags it

      The difference matters: a spotter watches for SPECIFIC risks.
      A checker reviews EVERYTHING for any kind of problem.

      Which feels closer to what you need?"

DON'T: "Could you clarify your intent regarding the monitoring vs
        review paradigm?"
```

**Maximum 3 options at a time** — cognitive load budget.

**Each option shows its consequence** in plain language: what changes downstream if you pick this.

**If the user can't choose after seeing options:** Apply the safer default. Flag it. Move on.

### Timeout Behavior

| Time Since Last User Input | Action |
|---|---|
| 30 seconds | No action (thinking is normal) |
| 2 minutes | Mirror: "Still thinking? Take your time. Or if you'd like, I can suggest a starting point." |
| 5 minutes | Mirror: "Would you like to save what we have and come back later? You won't lose anything." |
| 10 minutes | Auto-save. Session state preserved. Next login: "Welcome back. Here's where we were." |

**What happens after timeout is resolved:**
- If user says "I've got it" → continue from where they were
- If user says "suggest something" → apply safe default, flag it
- If user says "save and exit" → save to S10, produce partial output
- If user disappears → auto-save after 5 min, session available on return

### Safe Defaults and Flagging

**When safe defaults are applied:**

| Field | Safe Default | Why It's Safe |
|---|---|---|
| Agent class | Assessor | Middle ground — evaluates without deciding |
| Orientation | Bridge | Transitions between possibility and constraint |
| Harm assessment | HARM_CAPABLE | Safer to flag than to miss |
| Reversibility | EFFORT_UNDO | Middle ground between easy and no undo |
| Authority boundary | PREPARE_ONLY | Agent prepares, human decides — safer than giving agent decision authority |
| Principal | "You (the user)" | Default to the person in the room |

**How defaults are flagged in the output:**
- Visual: italic text or different background color + ⚡ icon
- Text: "(default — recommended to revisit)"
- Confidence: defaults contribute to lower section confidence

### Interaction Between Defaults and Confidence

**Per-section confidence:**
- Each section starts at HIGH (5/5)
- Each safe default applied to that section reduces confidence by 1
- Minimum confidence is LOW (1/5)

**Overall Boundary Map confidence:**
- HIGH: 0–20% defaults, all identity questions answered by user
- MEDIUM: 21–40% defaults, or 1 identity question defaulted
- LOW: >40% defaults, or 2+ identity questions defaulted, or contradictions present

**Draft flag:** If >40% defaults → the entire map is labeled "DRAFT — recommendations, not decisions. Revisit when ready."

---

## 6. Error Recovery

### Failure Scenario 1: Gibberish or Nonsense Input

| Step | Action |
|---|---|
| **Detection** | Mirror parses input and gets no typed output (can't identify domain, problem, or any agent concept) |
| **First recovery** | Mirror: "I want to make sure I understand. Can you tell me the single biggest problem this agent would solve for you?" |
| **Second recovery** | If still unclear after 2 attempts → Mirror: "Let me ask one question at a time. What kind of work do you do?" (anchor to the user, not the agent) |
| **Final recovery** | If after 3 attempts still unclear → Mirror: "I'm having trouble understanding. Would you like to try again from the top, or come back when you've had a chance to think about it?" → Save & Exit |
| **User communication** | Never blame the user. Frame as "I want to make sure I get this right." |

### Failure Scenario 2: Contradictory Requirements

| Step | Action |
|---|---|
| **Detection** | Two user statements directly conflict (e.g., "it should monitor everything" + "it shouldn't be intrusive") |
| **First recovery** | Name the contradiction: "I notice you've said X and Y, and they seem to point in different directions. Let me check: [explain both interpretations]. Which one feels right?" |
| **Second recovery** | If user says both → "Some tensions are real. Can we note this as something to figure out later? I'll mark it on the map so you don't lose it." |
| **Final recovery** | If unresolvable → document as a DESIGN TENSION in the Boundary Map. It's not a bug, it's a real constraint the user faces. |
| **User communication** | Normalise contradictions: "This is actually common — real workflows have tensions. Let's make sure they're visible." |

### Failure Scenario 3: Mid-Session Leave

| Step | Action |
|---|---|
| **Detection** | No user input for 5 minutes |
| **Immediate action** | Auto-save session state after every interaction (not just at gates) |
| **5-minute timeout** | Mirror offers save & exit |
| **On return (<24 hrs)** | Mirror: "Welcome back. You were working on [agent name]. We got to [phase]. Want to continue?" → Restore exact state |
| **On return (>24 hrs)** | Mirror: "Welcome back. It's been a while since you worked on [agent name]. Here's a quick summary of where we were. Want to continue, or start fresh?" |
| **On return (>7 days)** | Archive session. Offer to start fresh with the previous session as reference. |
| **Partial output** | Whatever was completed is preserved. The Boundary Map can be compiled from partial data. |

### Failure Scenario 4: Agent Can't Process Input

| Step | Action |
|---|---|
| **Detection** | Specialist agent returns error or empty output |
| **First recovery** | Mirror: "I'm having trouble with [specific thing]. Could you say that differently?" |
| **Second recovery** | Try a different approach: if the Identity Explorer can't process, switch to card-based selection instead of free-form conversation. If the Boundary Mapper can't classify, present the raw list and ask the user to group. |
| **Final recovery** | Skip the failing step, apply safe defaults, flag the gap. "I'll suggest a starting point for this part. You can always come back and change it." |
| **User communication** | Never say "I don't understand." Say "Can you help me with this specific part?" |

### Failure Scenario 5: Two Agents Disagree

| Step | Action |
|---|---|
| **Detection** | Identity Explorer's answers suggest one boundary configuration; Boundary Mapper's analysis suggests another |
| **Recovery** | Mirror presents both views to the user with plain-English reasoning: "Based on what you told me about identity, I'd expect [A]. But when I look at the boundary patterns, [B] might fit better. Here's what each means. Which feels right?" |
| **Resolution** | User decides. Always. |
| **If user can't decide** | Default to the identity-derived configuration (identity is the foundation; boundaries derive from identity). Flag the disagreement. |
| **User communication** | Frame as helpful tension: "It's interesting — your identity and your boundaries are telling slightly different stories. Let's figure out which one is closer to what you need." |

### Failure Scenario 6: Total Pattern Failure

| Step | Action |
|---|---|
| **Detection** | No pattern scores ≥20%, and exploratory mode questions also produce contradictory or unusable answers |
| **Recovery** | Revert to pure Q&A mode. Mirror asks one question at a time, building identity from scratch. No pre-fills, no assumptions, no pattern suggestions. |
| **Slower but reliable** | This takes 15–20 minutes for identity instead of 5–8. It still fits within the 30-minute budget because boundary mapping goes faster when identity is clearer. |
| **If even Q&A fails** | "I think this agent might be genuinely new — it doesn't fit the patterns I know. That's actually exciting. Let me build your boundary map from just what you've told me, without any pre-filled suggestions." |
| **User communication** | Frame as uniqueness, not failure: "You might be designing something I haven't seen before. Let's work from your specific situation." |

---

## 7. Output Specification

### Boundary Map Exact Structure

```
BOUNDARY MAP
═════════════════════════════════════════════════════════

Agent: [Name in plain English]
Date: [Session date]
Session: [ID]
Pattern: [Matched pattern name, or "Custom — no pattern matched"]
Confidence: [HIGH / MEDIUM / LOW]
Principal: [Who this agent acts on behalf of]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT THIS AGENT IS
───────────────────
[One-sentence essence from Q1]
Orientation: [Possibility / Bridge / Constraint]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHO DOES WHAT
──────────────

 Task / Action              │ You  │ Agent  │ System
───────────────────────────┼──────┼────────┼────────
 [Task 1]                   │  ✓   │        │
 [Task 2]                   │      │   ✓    │
 [Task 3]                   │      │  ✓*    │
 [Task 4]                   │      │        │   ✓
 ...
───────────────────────────┴──────┴────────┴────────
 ✓ = decides   ✓* = prepares, you decide

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEVER RULES — What This Agent NEVER Does
──────────────────────────────────────────
1. [Never rule from Q3 — tied to identity violation]
2. [Never rule from Q4 — tied to worst failure]
3. [Additional never rule from boundary analysis]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HARM ASSESSMENT
────────────────
Can this agent's output cause external harm? [YES / NO]
If yes: [Mechanism — how harm could occur]
DO_NOT_SUGGEST triggers: [When the agent should flag
  uncertainty instead of suggesting]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REVERSIBILITY
──────────────
 Easy undo:    [Actions that can be reversed trivially]
 Effort undo:  [Actions that take work to reverse]
 No undo:      [Actions that can't be reversed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GAPS & DEFAULTS
────────────────
 ⚡ [Safe default applied — field]: [default value]
    (recommended to revisit)
 ⚡ [Safe default applied — field]: [default value]
    (recommended to revisit)
 ? [Unresolved question]: [what still needs deciding]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY VALUE
─────────
[One sentence articulating where the human's unique
value lives — e.g., "Your value is in judgment on
ambiguous clauses, not in searching for them."]

═════════════════════════════════════════════════════════
```

### Complete vs Partial Boundary Map

| Condition | Map Status | Confidence |
|---|---|---|
| All identity questions answered, all boundaries classified, principal named | COMPLETE | HIGH/MEDIUM (based on default count) |
| 1–2 identity questions answered, most boundaries classified | COMPLETE_WITH_GAPS | MEDIUM/LOW |
| Only identity answered, no boundaries classified | PARTIAL — IDENTITY ONLY | LOW |
| Only intake completed | PARTIAL — REQUIREMENTS ONLY | MINIMAL |

**Every status is usable.** Even a PARTIAL map with identity only tells you what the agent IS and what would violate its identity. That's more than most people have when they start building an agent.

### Confidence Levels

| Level | Visual | Meaning |
|---|---|---|
| HIGH | 🟢 | User confirmed most answers, <20% defaults, no contradictions |
| MEDIUM | 🟡 | Some defaults, 1 identity question defaulted, or minor contradictions flagged |
| LOW | 🔴 | Many defaults, 2+ identity questions defaulted, or significant contradictions |

### Safe Defaults Visual Distinction

In the output:
- **Text styling:** Italic + ⚡ icon prefix
- **Label:** "(default — recommended to revisit)"
- **Confidence impact:** Each default reduces its section's confidence by 1

### Platform-Agnostic Test

The Boundary Map passes the platform-agnostic test if:
- ✅ No specific tool or framework is named anywhere
- ✅ No implementation-level detail is included (no Python, no API specs, no prompt text)
- ✅ Every boundary describes WHAT and WHY, never HOW
- ✅ An implementation team on any framework could read it and understand the agent's identity and boundaries
- ❌ Fails if: any section says "use [framework X]" or "connect to [specific API]" or "implement as [specific pattern]"

---

## 8. Cost Model

### Token Estimates Per Agent (Ollama glm-5.1:cloud)

| Agent | Per Interaction | Interactions per Session | Total Range |
|---|---|---|---|
| Mirror | 500–1,500 | 8–15 (routing, translation, gate presentation) | 4,000–22,500 |
| Identity Explorer | 3,000–5,000 | 4–6 (one per question + follow-ups) | 12,000–30,000 |
| Boundary Mapper | 4,000–6,000 | 1–2 (classification passes) | 4,000–12,000 |
| Compiler | 1,500–3,000 | 1 (single compilation) | 1,500–3,000 |

### Total Cost Per Session Type

| Scenario | Token Estimate | Notes |
|---|---|---|
| **Happy path** (pattern matched, no loops) | 21,500–67,500 | Pattern pre-fills reduce IE and BM tokens |
| **One loop-back** (revisit identity or boundaries) | 30,000–90,000 | IE or BM runs a second time |
| **Exploratory mode** (no pattern, Q&A from scratch) | 35,000–100,000 | IE runs longer, no pre-fill savings |
| **Multiple loops + errors** | 45,000–120,000 | Worst realistic case |
| **Session abandoned mid-way** | 10,000–40,000 | Partial cost, partial output |

### Cost vs Value

| Scenario | Approximate Token Cost | Value Delivered |
|---|---|---|
| Happy path → Complete Boundary Map | ~45,000 tokens | Full boundary clarity for the user's agent design |
| One loop → Complete Boundary Map | ~60,000 tokens | Same value, more confidence (user corrected something) |
| Exploratory → Complete Boundary Map | ~70,000 tokens | Higher value — custom agent, no template assumptions |
| Abandoned → Partial map | ~25,000 tokens | Partial value — identity card at minimum |

**Break-even analysis:** A Boundary Map that saves 2 hours of confused agent building is worth the token cost at any of these levels. The value is in the clarity, not the compute.

---

## 9. CAWDP Self-Application

### Complementarity Analysis

| Task | Human Score (1–10) | Agent Score (1–10) | Gap | Allocation |
|---|---|---|---|---|
| Raw input articulation | 9 | 3 | 6 | **HUMAN-ONLY** |
| Pattern matching | 2 | 8 | -6 | AGENT-ONLY |
| Identity exploration (reflecting) | 4 | 6 | -2 | COLLABORATIVE (agent reflects, human decides) |
| Identity decision (what IS it?) | 9 | 2 | 7 | **HUMAN-ONLY** |
| Boundary classification | 3 | 8 | -5 | AGENT-ONLY (with human review) |
| Boundary placement (where's the line?) | 9 | 3 | 6 | **HUMAN-ONLY** |
| Harm assessment | 5 | 7 | -2 | COLLABORATIVE (agent classifies, human confirms) |
| Compilation | 1 | 9 | -8 | AGENT-ONLY |
| Doubt resolution | 9 | 1 | 8 | **HUMAN-ONLY** |
| Error recovery decision | 8 | 4 | 4 | HUMAN-PRIMARY |

**Key finding:** The 4 human-only tasks (raw input, identity decision, boundary placement, doubt resolution) are exactly the 4 human gates in the state machine. The complementarity analysis validates the architecture — gates are placed where the human's contribution is irreplaceable.

### FMEA (Failure Mode and Effects Analysis)

| Failure Mode | Severity (1–5) | Likelihood (1–5) | Detection (1–5) | Recovery | RPN |
|---|---|---|---|---|---|
| Pattern mis-match (high confidence but wrong pattern) | 4 | 3 | 3 | Reset pre-fills, enter exploratory mode | 36 |
| User can't answer identity questions | 3 | 3 | 4 | Exploration prompts, then safe defaults | 36 |
| Contradictory identity answers | 3 | 2 | 4 | Surface contradiction, ask user to resolve | 24 |
| Boundary Mapper over-classifies | 3 | 3 | 3 | Group into categories, user confirms | 27 |
| Harm assessment missed | 4 | 2 | 3 | Default to harm-capable (safer assumption) | 24 |
| User abandons session | 2 | 3 | 5 | Auto-save, offer resume on return | 30 |
| Compiler receives incomplete data | 3 | 2 | 4 | Produce partial map, flag gaps | 24 |
| Mirror routing confusion | 2 | 2 | 4 | Default to Identity Explorer | 16 |
| Token budget exhaustion | 3 | 1 | 5 | Offer partial output, explain situation | 15 |

**RPN = Severity × Likelihood × Detection.** Highest RPN items (36, 36, 30) should be addressed first in testing.

### Specification Aging Schedule

| Element | Review Cadence | Trigger for Early Review | Who Initiates |
|---|---|---|---|
| Pattern pre-fill templates | Monthly | Override rate >50% for a pattern | System (automated) |
| Safe defaults | Quarterly | Default override rate >70% | System (automated) |
| Identity question phrasing | Quarterly | "I don't understand" rate >20% | System (automated) |
| Boundary default settings | Quarterly | Boundary override rate >40% | System (automated) |
| Doubt triggers | Quarterly | False positive rate >30% | Human review |
| Error recovery paths | After any user-reported failure | User complaint or observed failure | Human review |
| Confidence scoring algorithm | Bi-annually | Confidence doesn't correlate with user satisfaction | Human review |

**Key principle:** Patterns and defaults are living knowledge, not static configuration. The system should track how often pre-fills are overridden and use that data to refine the patterns over time.

---

## 10. Implementation Readiness

### What a Developer Needs to Build This

**Must-have before starting:**
1. This specification document
2. LLM API access (Ollama glm-5.1:cloud or equivalent)
3. Session state storage (Postgres, Redis, or equivalent)
4. Pattern templates as JSON files (see Section 4)
5. Boundary Map output template (see Section 7)

**Nice-to-have but not blocking:**
1. TypeDB for design artefact storage (for later milestones)
2. User account system (Milestone 1 can work with session IDs)
3. Authentication (not needed for prototype)

### Dependencies

| Dependency | Type | Required for | Blocking? |
|---|---|---|---|
| LLM API | External | All agent interactions | YES |
| Session storage | Infrastructure | State persistence, pause/resume | YES |
| Pattern JSON files | Data | Pre-fill templates | YES |
| Web interface (basic) | Frontend | User interaction | YES |
| TypeDB | Infrastructure | Design artefact graph | NO (later milestone) |
| User accounts | Infrastructure | Multi-session, return users | NO (prototype) |
| Payment integration | Infrastructure | Commercial use | NO (prototype) |

### Hardcoded vs Configurable

| Element | Hardcoded | Configurable | Why |
|---|---|---|---|
| 4 Identity Questions | ✓ | | Core methodology — changing these changes the workflow |
| 5 Patterns | | ✓ | New patterns will be added as the system learns |
| Pattern confidence thresholds | | ✓ | May need tuning based on real usage |
| Timeout durations | | ✓ | User testing may reveal different optimal timeouts |
| Safe defaults | | ✓ | Defaults may change as patterns are refined |
| Boundary Map output format | ✓ | | Must be consistent for vendor-agnostic use |
| Human gate questions | | ✓ | Phrasing may need adjustment for different users |
| Token cost limits | | ✓ | Budget constraints vary by deployment |
| 3-column layout (Human/Agent/System) | ✓ | | Core visual language of the Boundary Map |

### Testing Strategy

**Unit tests (per agent):**

| Test | What It Tests |
|---|---|
| Mirror routing logic | Correct specialist selected for each input type |
| Mirror boundary enforcement | Mirror refuses to decide, filter, or skip |
| Identity Explorer pre-fill handling | Pre-fills presented correctly, overrides work |
| Identity Explorer contradiction detection | Contradictions surfaced, not resolved |
| Boundary Mapper classification | Correct boundary types assigned |
| Boundary Mapper harm default | Defaults to harm-capable when uncertain |
| Compiler assembly | All fields populated, contradictions flagged |
| Compiler gap handling | Partial maps produced when data incomplete |

**Integration tests (state machine):**

| Test | What It Tests |
|---|---|
| Happy path | S0 → S8 in under 30 minutes |
| Loop-back: intake | S2 → S1 → S2 recovery |
| Loop-back: identity | S4 → S3 → S4 recovery |
| Loop-back: boundaries | S6 → S5 → S6 recovery |
| Loop-back: identity from boundaries | S6 → S3 → S4 → S5 → S6 |
| Save and resume | S4 → S10 → S4 continuation |
| Pattern match: high confidence | Pre-fills applied and reviewed |
| Pattern match: hybrid | Blend handled correctly |
| Pattern match: no match | Exploratory mode entered |
| Error: gibberish input | Recovery path executed |
| Error: contradiction | Tension surfaced and documented |
| Error: agent failure | Mirror recovery executed |

**End-to-end test scenarios:**

| Scenario | User Type | Pattern Match | Expected Outcome |
|---|---|---|---|
| **Simple** | Knows what they want | Signal Detector ≥80% | Complete map in 20 min, HIGH confidence |
| **Moderate** | Vague but directionally right | Review Partner 55% | Complete map in 30 min, MEDIUM confidence, some defaults |
| **Complex** | Genuinely new agent type | No match | Partial/complete map in 35 min, LOW confidence, exploratory mode |

**User validation:**

| Goal | Method | Success Criteria |
|---|---|---|
| Relief delivery | Post-session survey (1 question: "How do you feel?") | 3/5 report "relief" or "clarity" |
| 30-min feasibility | Timer on session | 4/5 complete in ≤37 minutes |
| Pattern-first reduces paralysis | Observation | 4/5 proceed after seeing pre-fills (don't freeze) |
| Map is independently valuable | Post-session task: "Explain your map to a colleague" | 3/5 can explain without the workflow |
| Platform-agnostic | Show map to 2 people unfamiliar with the project | Both understand the boundaries |
| Creates demand for Milestone 2 | Post-session question | 2/5 ask "what comes next?" |

---

## Appendix: The 30-Minute Session — What It Feels Like

*This is the experience a user should have. It's not a specification — it's a design target.*

**Minute 0:** User opens the tool. Sees: "What are you trying to build? Describe it however you want."

**Minute 1–3:** User types a paragraph. The tool listens — no forms, no dropdowns, just a text box and a conversation.

**Minute 3:** Tool says: "Here's what I understood: [summary]. This looks like a Review Partner — an agent that catches what you might miss. Is that roughly right?"

**Minute 4:** User says yes. Tool says: "Great. I have some suggestions for what this agent IS. Review them, change what you want."

**Minute 5–10:** User reviews 4 pre-filled identity answers. Overrides one. Confirms the rest. The tool reflects each answer back: "So this is a quality check that catches what you miss. It guards space — it watches for problems. It would stop being itself if it started fixing problems. Its worst failure is approving something that looks right but isn't. Right?"

**Minute 11:** User says yes.

**Minute 12–22:** Tool presents boundary classifications. User reviews a 3-column table: You / Agent / System. Drags a few items between columns. Reviews the never-rules. Confirms the harm assessment.

**Minute 23:** Tool says: "Here's your boundary map. Take a look."

**Minute 24–28:** User reviews the one-page Boundary Map. Adjusts one boundary. Asks about the harm assessment. Confirms.

**Minute 29:** Tool compiles the final map. User downloads it. The map has their agent's name, its never-rules, who does what, the harm assessment, and one sentence that says where their judgment lives.

**Minute 30:** User closes the tool. They feel relief — not because they built an agent, but because someone finally drew the line.

---

*This is a build specification. Build it, test it with 5 real people, and let the results speak.*
```

---

**File path:** `./artifacts/agentic-workflows/milestone-1-boundary-map-workflow-v0.1.md`

**Status:** ✅ Complete document provided inline. Copy the content above to the specified path to save it. The document contains all 10 sections plus the experience appendix, totaling the full Milestone 1 build specification synthesizing architecture, interaction, and commercial perspectives.Memory updated with the full Milestone 1 specification details. The document is ready to save to `./artifacts/agentic-workflows/milestone-1-boundary-map-workflow-v0.1.md`.

---

## Run 19 — unknown ✓ COMPLETED

*2026-04-27T09:25:52* · `glm-5.1:cloud` · `0a5343a3...`

### Prompt

Create a workflow design for Milestone 1 only based on your learnings and what you'd do differently.
The agentic expert should now be able to write to the file system. If not, share it inline here in the chat.

### Response

Let me have all three perspectives work in parallel on the Milestone 1 design — architecture, interaction, and commercial framing — then synthesize into one deliverable.Two tasks hit server errors. Let me retry those.Failed tasks can't be re-executed. Let me recreate and run them.The architecture task failed again — let me handle that directly and then compile everything into the final unified document.All three perspectives are now complete. Let me save the final unified document and mark completion.The Milestone 1 workflow design is complete. Here's the full picture of what was produced:

---

## 📂 Document Location

The complete Milestone 1 build specification has been provided inline by the Agentic Expert (the team doesn't have direct filesystem write access). It should be saved to:

**`./artifacts/agentic-workflows/milestone-1-boundary-map-workflow-v0.1.md`**

---

## What's in the Milestone 1 Design

Three perspectives were synthesized into one build spec:

### 🏗️ Architecture (10 Sections)
| Section | Highlights |
|---|---|
| **Scope & Boundaries** | 30-min timing budget, 7 success criteria, what's IN vs OUT |
| **4-Agent Architecture** | Mirror, Identity Explorer, Boundary Mapper, Compiler — each with class, orientation, authority boundary, stress tests, I/O schemas, failure modes, token cost estimates |
| **State Machine** | 11 states, happy path, 6 loop-back paths, skip paths, error recovery paths, exit paths with value from every state |
| **Pattern System** | 5 patterns with full identity pre-fills + boundary defaults, hybrid composition rules, no-match path, exploratory mode, confidence thresholds |
| **Ambiguity & Doubt Protocol** | 6 doubt triggers, option presentation format (max 3 options, consequences shown), timeout behavior (30s → 2min → 5min → 10min), safe defaults with flagging, confidence interaction rules |
| **Error Recovery** | 6 failure scenarios (gibberish, contradictions, mid-session leave, agent failure, agent disagreement, total pattern failure) — each with detection, recovery, user communication |
| **Output Specification** | Exact Boundary Map structure, complete vs partial maps, confidence levels (HIGH/MEDIUM/LOW), safe defaults visual distinction, platform-agnostic test |
| **Cost Model** | Token estimates per agent, total per scenario (happy: ~45K, exploratory: ~70K, worst: ~120K), cost vs value analysis |
| **CAWDP Self-Application** | Complementarity analysis (validates human gates align with human-only tasks), FMEA with RPN scores, specification aging schedule |
| **Implementation Readiness** | Dependencies, hardcoded vs configurable decisions, full testing strategy (unit, integration, end-to-end, user validation) |

### 🎨 Interaction (9 Sections)
| Section | Highlights |
|---|---|
| **Discovery Room "Light Studio"** | Full visual spec: layout (680px canvas, left attention map, right Mirror presence), color palette, accent color shift per phase (gold → blue → teal → green), transition animations |
| **Intake Interaction** | Single text area, prompts fade in after 2s, pattern match reveal for high/low/no confidence with screen mockups |
| **Identity Interaction** | Q1 narrative mode with pre-fill, Q2 3-card selection (Explore/Advise/Stay in Lane), Q3 drag-sort boundary mode, Q4 scenario ranking — all with wireframes |
| **Boundaries Interaction** | 3-column allocation (You/Agent/System) with never-rules locked in, harm assessment conditional card, reversibility indicators, "Your value is in [X]" preview |
| **Boundary Map Output** | Full mockup of the one-page deliverable with confidence section, gaps & defaults, key value line, next step CTA |
| **Attention Map & Coherence Check** | Always-visible left rail (6 states: not started → confirmed), live coherence check (inline flags, never blocking), deep check on demand |
| **Error & Recovery** | 4 screen mockups for "I can't process this", "I'm not sure which specialist", contradictions, and session resumption |
| **Mobile & Accessibility** | Responsive layout, tap-to-select for drag-sort, WCAG AA, keyboard navigation, dark mode |
| **7 Testable Hypotheses** | H1-H7 with minimum signals and go/no-go framework |

### 💼 Commercial & Validation (6 Sections)
| Section | Highlights |
|---|---|
| **77% Challenge as Product** | 30-min session format, free Boundary Map → paid Allocation Map, natural escalation ("who does what at the boundary?") |
| **"15-Minute Boundary Map" Pitch** | Headline: "Know where the boundary is in 15 minutes." 5-minute demo flow. 3 key differentiators vs templates. |
| **Validation Strategy** | 5-person test, 6 hypotheses with measurement instruments, post-session survey, 1-week follow-up |
| **Boundary Map as Deliverable** | 5 reasons it's independently valuable, CAWDP positioning, upgrade path |
| **Go/No-Go Criteria** | Proceed (3+ relief, 2+ follow-up questions), Iterate (partial results), Rethink (0-1 relief, 3+ "just another form") |
| **Competitive Positioning** | Positioning: "Design Partner". Category: "Agent Production". Tagline: "Principles aren't production. We have the methodology." |

---

## Retrospective Learnings Applied

Every learning from the retrospective was addressed:

| Learning | How It Was Applied |
|---|---|
| Start with Milestone 1 only | ✅ Strict scope — no task decomposition, no architecture, no behaviour rules |
| Reduce to 4 agents | ✅ Mirror + Identity Explorer + Boundary Mapper + Compiler |
| Make possibility gradient structural | ✅ Agent orientations enforce it (IE = possibility, BM = bridge, Compiler = constraint) |
| "15-minute spec" as headline | ✅ Commercial strategy leads with this |
| Ambiguity protocol needs operational mechanisms | ✅ 6 triggers, presentation format, timeout ladder, safe defaults with flagging |
| Pattern system needs more work | ✅ Hybrid composition, no-match path, exploratory mode, confidence thresholds |
| Authority boundaries must be stress-tested | ✅ 4 stress tests per agent with exact responses |
| Need Mirror routing logic | ✅ Full routing rules with "unsure" and "two could handle" paths |
| Need error recovery | ✅ 6 failure scenarios with full recovery sequences |
| Workflow needs CAWDP applied | ✅ Complementarity analysis, FMEA, specification aging |

---
