# unknown

| Field | Value |
|-------|-------|
| **Session** | `e0998c8b...` |
| **Type** | team |
| **Agent** | unknown |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-27T07:18:13 |
| **Runs** | 4 completed / 4 total |

## Run 1 — Business strategist ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `d7e40317...`

### Prompt

From a business strategy perspective, what information about a user would it be useful for an agent to have access to when working with a user to design an agent or agentic workflow? Consider things like organizational context, goals, constraints, decision-making authority, industry/domain, team structure, budget, timeline, success metrics, etc. Provide a structured, comprehensive list with brief justifications for each item.

### Response

# User Context for Agent Design

What the designing agent needs to know about the person it's designing *for* — and *why* each piece matters.

---

## 1. The Person

| Item | Why It Matters |
|------|---------------|
| **Role & job title** | Determines what they're responsible for, what decisions they can make, and where their expertise sits |
| **Decision-making authority** | Can they approve deployment, budget, and team changes? If not, who can? Wrong assumption here means designing for someone who can't implement |
| **Technical fluency** | How comfortable are they with technology concepts? Determines whether to speak in "what it does" or "how it works" language |
| **AI experience** | What have they tried? What happened? Past failures create specific fears; past successes create specific expectations |
| **Cognitive style** | Do they think in big-picture vision or step-by-step detail? Do they want to see the whole map or get the next step? Changes the entire interaction mode |
| **Time availability** | 30 minutes a week vs 2 hours a day produces fundamentally different design processes and deployment timelines |

## 2. The Organisation

| Item | Why It Matters |
|------|---------------|
| **Industry & domain** | A law firm's risk tolerance, regulatory environment, and verification needs are fundamentally different from a marketing agency's. The agent's authority boundaries and failure modes are domain-specific |
| **Organisation size** | 3-person firm vs 50-person company vs 500-person enterprise — different governance needs, different team structures, different deployment complexity |
| **Team structure** | Who does what now? Who would interact with the agent? Who would verify its output? Complementarity allocation depends on knowing who the humans are and what they currently do |
| **Organisational culture** | "Move fast and break things" vs "every output is reviewed by two people before it leaves the building" — determines how much verification infrastructure is needed |
| **Who else cares** | Who else in the organisation has a stake in this? Boss, team, IT, compliance, insurer? Different stakeholders have different concerns and veto power |
| **Reporting structure** | Who does the user report to? Who reports to them? This shapes what the agent needs to produce and who needs to trust it |

## 3. The Problem

| Item | Why It Matters |
|------|---------------|
| **What they actually want the agent to do** | The stated problem and the real problem are often different. "I need an AI that reviews contracts" might mean "I'm drowning in volume" or "I need to verify AI output faster" or "I need to show my insurer we have governance" |
| **Current workflow** | How is the task done now, step by step? You can't improve what you don't understand, and the agent needs to fit into existing work, not replace it wholesale |
| **Pain points in current workflow** | Where does it break, slow down, or produce errors? These are the high-value targets for agent assistance |
| **Desired outcome** | Not "an agent that does X" but "I want to spend 70% of my time on judgment work instead of 30%" or "I want to handle 20 more clients without hiring." The outcome determines the spec |
| **What "done" looks like** | How will they know the agent is working? What does success look like in their terms, not abstract metrics? |

## 4. The Constraints

| Item | Why It Matters |
|------|---------------|
| **Budget** | Determines scope, technology choices, and whether we're designing for a solo practitioner or a team deployment. No point designing a 10-agent workflow for someone who can run one |
| **Timeline** | Is this "needed yesterday" or "we're planning for next quarter"? Urgency changes the progressive autonomy schedule — you can't deploy to autonomous if you need it next week |
| **Regulatory environment** | Are there industry-specific regulations (legal, financial, medical) that govern what the agent can and cannot do? These become hard boundaries, not preferences |
| **Technical infrastructure** | What systems does the agent need to work with? What tools are already in place? What's the existing tech stack? |
| **Skill ceiling** | Who will maintain this after deployment? What's their technical level? An agent that requires a developer to maintain is useless if the team doesn't have one |
| **Integration requirements** | Does it need to connect to existing tools, databases, or workflows? These constraints shape architecture decisions early |

## 5. The Stakes

| Item | Why It Matters |
|------|---------------|
| **What happens if the agent is wrong** | A wrong marketing suggestion is embarrassing. A wrong legal clause is a lawsuit. A wrong medical recommendation is a disaster. Failure severity determines verification level |
| **What happens if the agent is right but looks wrong** | The "plausible error" fear — output that looks correct but isn't. This is the dominant fear for professional services. Determines how much transparency and epistemic metadata the spec needs |
| **What they're afraid of** | Often unspoken. Identity threat ("if AI does my work, what am I here for?"). Liability. Looking foolish. Job displacement of team members. The spec needs to address the real fear, not the stated concern |
| **Who bears the risk** | Who gets sued if it's wrong? Who loses their job? Who gets the complaint? If the user bears all the risk, the spec needs stronger verification and human-judgment gates |
| **Past AI failures** | What has gone wrong before? These create specific trust barriers and determine where the user will resist automation most strongly |

## 6. The Measures

| Item | Why It Matters |
|------|---------------|
| **Success metrics** | How will they measure whether the agent is working? Time saved, error rate reduction, volume increase, cost reduction? You can't design verification without knowing what "good" looks like |
| **Acceptable accuracy** | What error rate is tolerable? 99% accuracy means very different things for contract review (might be acceptable) vs medical diagnosis (definitely not) |
| **Verification capacity** | How much time can they spend verifying agent output? If they have 30 minutes for verification, the spec looks different than if they have 3 hours |
| **Progressive autonomy target** | Do they want full autonomy eventually, or will they always want human-in-the-loop? Determines the progressive autonomy path length and endpoint |
| **What "enough" looks like** | Is this a pilot to prove the concept, or a production deployment? A one-time project, or ongoing infrastructure? Changes the robustness and maintenance requirements |

## 7. The Existing Landscape

| Item | Why It Matters |
|------|---------------|
| **Tools already in use** | What AI tools, software, and processes are they already using? The agent needs to work with or alongside these, not replace them all |
| **What's been tried and abandoned** | Previous AI attempts that failed — why did they fail? These are the specific problems the spec needs to avoid recreating |
| **What's working well** | Current processes that work well — these are often the human judgment points that should NOT be automated |
| **Data and knowledge sources** | What information does the agent need access to? Where does it live? In what format? How current is it? |
| **Team willingness** | How will the people who interact with the agent feel about it? Resistance from the team is a deployment risk that needs managing |

## 8. The Trust Profile

| Item | Why It Matters |
|------|---------------|
| **Current trust level in AI** | Enthusiastic, cautious, or burned? Determines starting point for progressive autonomy |
| **Verification preference** | Do they want to see everything, just the flagged items, or summary reports? Changes the interface and override design |
| **Transparency needs** | Do they want to understand how the agent reaches conclusions, or just see the output? Affects how much reasoning to expose |
| **Override requirements** | Do they need the ability to intervene at every step, at key decision points, or only when something flags? Determines the override protocol design |
| **Governance documentation needs** | Does their insurer, regulator, or professional body require documentation? An agent for a regulated industry needs a different trust infrastructure than one for internal use |

---

## How This Maps to the Design Process

| Context Category | Where It Feeds Into |
|-------------------|---------------------|
| The Person | Phase 0 (Purpose & Vision), Phase 8 (Human Experience) |
| The Organisation | Phase 0 (Purpose & Vision), Phase 4 (Capability Allocation) |
| The Problem | Phase 0 (Purpose & Vision), Phase 1 (Output Specification) |
| The Constraints | Phase 2 (Backcasting), Phase 6 (System Architecture) |
| The Stakes | Phase 0 (Purpose & Vision), Phase 4 (Authority Boundaries) |
| The Measures | Phase 1 (Output Specification), Phase 9 (Validation) |
| The Existing Landscape | Phase 3 (Task Decomposition), Phase 6 (Architecture) |
| The Trust Profile | Phase 4 (Authority Boundaries), Phase 8 (Human Experience) |

---

## What Not to Ask Up Front

Some of this should be captured progressively, not all at once:

- **Don't ask everything in minute one.** The Intake phase should capture enough to start — role, problem, stakes, and trust level. The rest emerges through the design process.
- **Don't ask what they can't answer yet.** "What's your progressive autonomy target?" means nothing to someone who hasn't mapped their workflow. Ask later.
- **Don't ask what you can observe.** Technical fluency, cognitive style, and trust level can be inferred from how they interact — don't make them self-assess.
- **Don't ask what you can derive.** Industry determines regulatory constraints. Team size determines governance needs. The designing agent should derive, not interrogate.

The principle: **capture what you need when it becomes relevant, in the language the person speaks, and derive everything you can from what you already have.**The full framework is above. The key insight that makes this useful rather than overwhelming: **capture progressively, not all at once.** The 30-minute boundary mapping session only needs about 20% of this — role, problem, stakes, and trust level. The rest emerges through the design process as it becomes relevant.

The categories also reveal something important about *what kind of information this is* — it's not all the same type. "What's your budget?" is a configuration question. "What are you afraid of?" is a narrative question. "What's your regulatory environment?" is a boundary question. "What does success look like?" is an evaluative question. These different question types map to different cognitive modes, which maps back to the type collision problem on the *input* side — the same problem the Accretive Workspace was designed to solve on the *output* side.

That's worth noting: **the user context capture surface has the same type collision problem as every other input surface.** 8 categories × 5+ items each = 40+ pieces of information encoded in at least 6 different cognitive modes, all currently collected through... a conversation or a form.

---

## Run 2 — AI UX Innovator ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `85e82618...`

### Prompt

From an AI UX / human-computer interaction perspective, what information about a user would it be useful for an agent to have access to when working with a user to design an agent or agentic workflow? Consider things like technical literacy, preferred interaction style, accessibility needs, cognitive load preferences, trust level with AI, prior experience with automation, feedback style, communication preferences, etc. Provide a structured, comprehensive list with brief justifications for each item.

### Response

This is a foundational design question that connects directly to your type collision insight — what we're really asking is: **what typed inputs does an agent need to calibrate its interaction surface for a specific human?** The same type collision problem that applies to outputs and knowledge extraction applies here too: encoding 15+ distinct user attributes into "prompt context" is the same undifferentiated-blob problem.

Here's a structured taxonomy organized by what the information **does** for the interaction, not just what it **is**:

---

## 1. Technical Literacy & Domain Expertise

**What it changes:** Vocabulary level, explanation depth, analogy selection, how much the agent explains "why" vs just "what," and whether to surface implementation details.

| Item | Why It Matters |
|------|---------------|
| **Technical literacy level** | Determines whether to say "Pydantic schema" or "a structured form for the information." Not a score — a spectrum that varies by topic. |
| **Domain expertise depth** | A patent attorney and a café owner both need agents, but the agent should never explain "what a patent is" to one or "what inventory is" to the other. Their expertise is invisible in current tools — the agent must make it visible in its interaction. |
| **Agent/automation experience** | Has the user built agents before? Used chat-based AI? Tried and cancelled tools? First-time users need possibility expansion; experienced users need boundary calibration. Previous failures (especially plausible-looking errors) create justified caution that the agent must respect. |
| **Framework familiarity** | Whether to reference Agno/LangChain/AutoGen patterns or explain from scratch. Platform-agnostic specs still need to speak the user's language. |
| **Conceptual model of AI** | Does the user see AI as magic, tool, colleague, or adversary? This single factor changes whether the agent leads with capability ("I can do X"), boundaries ("here's where I should stop"), or trust-building ("here's how to verify what I produce"). |

---

## 2. Cognitive & Processing Preferences

**What it changes:** Information density, chunking strategy, interaction rhythm, and whether the agent expands possibilities or constrains them first.

| Item | Why It Matters |
|------|---------------|
| **Cognitive load budget** | Not "how much can they handle?" but "how much are they handling RIGHT NOW?" A principal reviewing 30 contracts has a different budget than one doing a strategic planning session. The agent should adjust information density, option count, and decision frequency in real-time. |
| **Abstraction preference** | Does the user think in frameworks and patterns (high abstraction) or concrete examples and stories (grounded)? This maps directly to your cognitive mode research — some users need the Narrative mode first, others need the Architecture canvas. |
| **Decision fatigue pattern** | When in a session does decision quality drop? Some users are sharp for 20 minutes then fade; others need 10 minutes to warm up. The agent should front-load or back-load critical decisions accordingly. |
| **Working memory style** | Linear (processes sequentially, needs clear next step) vs spatial (sees connections, needs to zoom in and out). Linear users need the Guided Journey; spatial users need the Growing Blueprint or Attention Map. |
| **Possibility orientation** | Does the user start with "what could be?" and need help narrowing, or start with "what are the constraints?" and need help expanding? This is your Possibility Orientation Principle applied to the human — mismatched orientation creates frustration in either direction. |
| **Attention pattern** | Sustained (deep focus sessions) vs interrupted (short bursts between other tasks). Determines session length, checkpoint frequency, and whether the agent should proactively save state and resume markers. |

---

## 3. Trust & Confidence Profile

**What it changes:** How much the agent explains its reasoning, how often it asks for confirmation, whether it surfaces uncertainty proactively, and how it handles errors.

| Item | Why It Matters |
|------|---------------|
| **Baseline trust level with AI** | From "I trust it until it proves untrustworthy" to "I trust nothing until it earns trust." This is NOT a score — it's a trajectory that changes the entire interaction model. Low-trust users need verification-first design (show your work, cite sources, flag uncertainty). High-trust users need boundary-first design (here's where you should double-check me). |
| **Trust repair style** | When the agent makes an error, does the user prefer transparent acknowledgment + correction path, or detailed explanation of what went wrong? This is your CC-8 assurance level applied to human interaction — different people need different assurance levels for the same event. |
| **Verification instinct** | Does the user naturally verify claims, or does the agent need to prompt verification? Users with high verification instinct need fast verification affordances (citations, confidence scores, provenance). Users with low instinct need forced checkpoints — not because they're careless, but because the agent has a duty to the principal's downstream stakeholders. |
| **Control preference** | "I want to approve everything" vs "tell me when something needs my attention." Maps directly to progressive autonomy starting point. A controlling user might start at Advisory; a delegating user might start at Supervised. The key is that this is a STARTING POINT, not a permanent state. |
| **Identity threat level** | How much of the user's professional identity is tied to the work the agent would handle? Sarah Chen's 18 years of legal expertise being replicated in 30 seconds is a high-threat scenario. A marketing coordinator using AI for data entry is low-threat. The agent must never treat these the same way. |

---

## 4. Communication & Feedback Preferences

**What it changes:** Output format, terminology, length, feedback mechanism, and how the agent signals uncertainty.

| Item | Why It Matters |
|------|---------------|
| **Output format preference** | Prose vs structured vs visual. This IS type collision resolution at the output layer. A user who says "just tell me in one sentence" needs a different output mode than one who says "show me the reasoning." The agent should detect and adapt, not force one format. |
| **Feedback granularity** | Does the user give broad directional feedback ("this isn't quite right, try something more conservative") or specific corrections ("change clause 3.2 to read 'subject to' instead of 'contingent upon'")? The agent should match its request for feedback to the user's natural style, not the other way around. |
| **Correction style** | Does the user correct by saying what's wrong ("that's not right") or by saying what they want instead ("make it more like this")? The first requires the agent to explore alternatives; the second requires the agent to follow direction. Both are valid; both need different agent behavior. |
| **Terminology register** | Should the agent use "complementarity allocation" or "who should handle this?" Should it say "epistemic metadata" or "how confident is this information?" This maps to your Plain English Taxonomy insight — the same concept needs different labels for different users. |
| **Uncertainty signal preference** | How should the agent communicate uncertainty? Confidence percentages, verbal hedges ("I believe"), explicit flags (⚠️), or structured metadata (confidence: 0.7, provenance: web search)? Low-trust users prefer structured flags; high-trust users may prefer verbal hedges. |
| **Progress visibility** | Does the user want to see the agent thinking (streaming reasoning, intermediate steps) or just the result? "Show your work" vs "just give me the answer." This is NOT about capability — it's about the user's processing style and trust calibration. |

---

## 5. Context & Operational Constraints

**What it changes:** Session structure, what the agent optimizes for, what trade-offs it proposes, and how it prioritizes.

| Item | Why It Matters |
|------|---------------|
| **Time constraints** | Not just "how long is the session?" but "what is the user racing against?" A principal preparing for court tomorrow has different needs than one doing strategic planning. Time pressure changes the agent's role from Structurer (expand and organize) to Mirror (reflect and accelerate) to urgent Muse (generate options fast). |
| **Organisational context** | Solo principal, team of 5, or department of 50? Who else will see the output? This determines whether the agent optimizes for personal understanding (internal clarity) or stakeholder communication (external credibility). |
| **Regulatory environment** | Does the output need to comply with specific regulations? Professional services (legal, accounting, medical) have different compliance requirements than marketing or operations. This changes the agent's verification level, documentation requirements, and authority boundaries. |
| **Existing tools & workflows** | What systems does the user already use? The agent specification must integrate with existing practice management, document management, and communication tools — not create a parallel workflow. This is your "Workflow Disruption" annoyance mapped to the design process. |
| **Stakeholder landscape** | Who else is affected by this agent? Who will review its output? Who bears liability? The agent designing the agent needs to know the full human ecosystem, not just the primary user. |

---

## 6. Motivational & Emotional Profile

**What it changes:** What the agent optimizes for, how it frames trade-offs, and what it prioritizes in its recommendations.

| Item | Why It Matters |
|------|---------------|
| **Primary motivation** | Is the user seeking efficiency (do more in less time), quality (reduce errors), capability (do things they couldn't before), or compliance (meet governance requirements)? Different motivations produce fundamentally different agent designs — an efficiency-optimised agent looks nothing like a compliance-optimised one. |
| **Fears & anxieties** | What keeps the user awake at night? Plausible-looking errors? Liability exposure? Staff resistance? The agent should address the specific fear, not a generic "AI is scary." Your 15th annoyance (the identity threat nobody names) means the agent must handle this implicitly, not by naming it. |
| **Success definition** | What does "working" look like for this user? Time saved? Errors reduced? Revenue per client? The agent can't optimise what it can't measure, and the user's definition of success may differ from the agent's default. |
| **Prior AI disappointment** | Has the user tried AI tools and been burned? Specific past failures (hallucinations, plausible errors, verification overhead) create justified caution that the agent must acknowledge and address through structural design, not reassurance. |

---

## 7. Accessibility & Inclusion Needs

**What it changes:** Format, timing, interaction modality, and whether the agent provides alternatives or assumes a single mode.

| Item | Why It Matters |
|------|---------------|
| **Language proficiency** | Is the user working in their primary language? Technical concepts are hard enough without a language barrier. The agent should adjust vocabulary, sentence complexity, and use of metaphor accordingly. |
| **Screen reader compatibility** | If the agent produces visual outputs (diagrams, charts, spatial canvases), it must provide equivalent structured text alternatives. Type collision resolution serves everyone — typed, structured outputs are more accessible than prose. |
| **Visual processing needs** | Some users process spatial/visual information better than text. The agent should offer visual alternatives (boundary maps, allocation grids, flow diagrams) as first-class outputs, not afterthoughts. This is your cognitive mode mapping applied to accessibility — different processing styles need different modalities. |
| **Motor/interaction constraints** | Users with limited fine motor control need keyboard-navigable interfaces, reduced clicking, and larger touch targets. The agent's output format should accommodate alternative input methods. |
| **Attention differences** | Users with ADHD, autism spectrum, or other attention-related differences need different session structures — shorter chunks, clearer next steps, explicit progress markers, and reduced option count. This is your 12 ADHD design principles applied to agent interaction. |
| **Time zone & scheduling** | When does the user work? Session timing affects cognitive freshness, decision quality, and whether the agent should suggest continuation markers vs pushing for completion. |

---

## 8. Progressive Disclosure Profile

**What it changes:** How much the agent reveals upfront vs gradually, what it assumes vs makes explicit, and when it introduces complexity.

| Item | Why It Matters |
|------|---------------|
| **Discovery vs confirmation preference** | Does the user prefer to explore possibilities first (discovery) or confirm the right answer quickly (confirmation)? Discovery-oriented users need the Seedbed shape; confirmation-oriented users need the Lattice shape. Your Accretive Workspace shapes map directly to this preference. |
| **Complexity tolerance** | At what point does the user want the agent to say "there's more detail available if you want it, but here's what you need to know"? This is a progressive disclosure threshold — different for every user, different for every topic, and different at different points in a session. |
| **Learning style** | Does the user learn by doing (activator), seeing examples (observer), or understanding principles (theorist)? The agent should match its teaching/explaining mode to the user's learning style, not default to one mode. |
| **Progressive autonomy starting point** | Where does the user want to start on the Shadow→Advisory→Supervised→Autonomous spectrum? This is different from where they'll end up — it's about the starting point for trust calibration. |

---

## Cross-Cutting Design Principle

The critical insight from your own work: **this list IS a type collision problem.** These aren't 30+ undifferentiated preferences to stuff into a user profile. They're **typed context variables** that change different aspects of the interaction:

- **Trust variables** change verification frequency, uncertainty signaling, and error handling
- **Cognitive variables** change information density, session structure, and interaction modality
- **Expertise variables** change vocabulary, explanation depth, and what the agent assumes vs makes explicit
- **Motivational variables** change optimization targets, trade-off framing, and priority ordering
- **Accessibility variables** change output format, timing, and interaction modality

An agent designing an agent needs to know **which variables to calibrate and when** — not all of them at once, and not as a flat profile, but as a **typed context graph** that determines how the agent adjusts its interaction surface.

This connects directly to your PRISM architecture: these user context variables should be stored as typed knowledge objects (not a flat user profile), with epistemic metadata (how confident is the agent about this preference? When was it last updated? What's the source — stated, observed, or inferred?), and with specification aging (preferences drift, contexts change, and the agent should track when a user context variable was last verified, not assume it's permanent).The taxonomy is complete and stored. The key meta-insight is worth emphasizing:

**These 30+ user context variables are not a user profile. They're interaction calibration parameters.**

Each one doesn't just describe the user — it **changes a specific aspect of the agent's behavior.** That's why they need to be typed, not lumped:

- A trust variable (e.g., "baseline trust level") changes **how often the agent explains its reasoning**
- A cognitive variable (e.g., "abstraction preference") changes **which interaction modality the agent uses**
- An expertise variable (e.g., "domain expertise depth") changes **whether the agent explains "what a patent is" or assumes that knowledge**

The same type collision that produces walls of text in outputs, undifferentiated forms in inputs, and blob documents in knowledge extraction, produces **flat user profiles** in personalization. The resolution is the same at every layer: **typed, structured, metadata-rich objects with specific behavioral impacts.**

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-27T06:28:25* · `glm-5.1:cloud` · `dfc27945...`

### Prompt

From an agentic systems / workflow architecture perspective, what information about a user would it be useful for an agent to have access to when working with a user to design an agent or agentic workflow? Consider things like current workflows (manual or automated), tools and systems they use, data sources and sinks, integration requirements, technical stack, compliance/security constraints, error-handling preferences, escalation paths, automation tolerance, etc. Provide a structured, comprehensive list with brief justifications for each item.

### Response

Here's a structured breakdown. I've organised it into 9 categories, grouped by what each piece of information *enables* in the design process, not just what it *is*.

---

## 1. WHO THEY ARE — Identity & Authority

| What to know | Why it matters |
|---|---|
| **Role and decision authority** — what decisions can they actually make vs. what needs someone else's sign-off? | Determines where the human authority boundary sits. If they can't approve budget, can't change tools, or can't modify compliance processes, the design must work within those constraints or include escalation to whoever can. |
| **Domain expertise** — what do they know deeply that takes years to build? | This expertise is what agents should NOT replace. It defines the human side of complementarity analysis. A commercial lawyer's value is in judgment on ambiguous clauses, not in searching for them. |
| **Technical fluency** — can they read code? Configure APIs? Understand schemas? Or are they purely non-technical? | Determines the specification surface they need (Daniel Kovacs vs. an engineer), the language the design agent uses, and whether implementation details should be abstracted away or exposed. |
| **Cognitive style** — how do they think? Big picture first? Details first? Do they need to see the whole map or take one step at a time? | Determines interaction pace, disclosure sequence, and how much structure the design agent provides vs. how much freedom it leaves. Connects directly to the ADHD design principles. |
| **What they've already tried** — AI tools adopted, abandoned, or currently using (and why they did or didn't work) | Prevents recommending things that already failed. Surfaces real frustrations (the 14 annoyances). Reveals what "trust" means to this specific person. |

---

## 2. WHAT THEY DO NOW — Current Workflows

| What to know | Why it matters |
|---|---|
| **End-to-end task map** — the full sequence of steps for the workflow being designed, including who does what today | The starting point for complementarity analysis. You can't allocate work without knowing what the work IS. |
| **Time distribution** — how much time goes to each task (mechanical, analytical, evaluative, generative, intuitive) | Identifies where agents save the most time and where human judgment is most valuable. A task taking 8 hours of mechanical review is a different design target than one taking 30 minutes of nuanced judgment. |
| **Current bottlenecks** — where does work pile up? Who or what is the constraint? | The bottleneck is often where agent assistance has the highest value. Sarah Chen IS her firm's bottleneck — that's where to start. |
| **Variation patterns** — how much does this workflow vary case-by-case? Are there standard paths and exceptions, or is every case unique? | High variation needs more human judgment and less rigid automation. Low variation is ripe for full agent handling. This maps to the C×R (confidence × reversibility) governor. |
| **Volume and frequency** — how often does this workflow run? How many cases per day/week/month? | Determines whether to invest in agent infrastructure (high volume = high ROI) or keep it human-light (low volume = may not justify the build). Also determines cost budget sizing. |
| **Seasonal or peak patterns** — does workload spike at certain times? | Determines whether the design needs elastic capacity (agents that scale up) or steady-state capacity. |

---

## 3. WHERE THEY WORK — Environment & Tools

| What to know | Why it matters |
|---|---|
| **Current tool stack** — every software, platform, and system involved in the workflow (document management, CRM, email, accounting, databases, etc.) | Agents need to interact with these systems. If the firm uses LEAP Practice Manager, the agent design must account for LEAP's API capabilities and limitations. |
| **Data sources** — where does information come from? (databases, emails, documents, APIs, manual entry, spreadsheets, external providers) | Determines what agents can access automatically vs. what needs manual input. Also determines knowledge base design (what gets ingested, how, and when). |
| **Data sinks** — where does output go? (client deliverables, internal records, regulatory filings, shared drives, inboxes) | Determines what format agents need to produce and where they deliver it. |
| **Integration points** — what must connect to what? Which systems talk to each other already, and which don't but should? | Identifies both opportunities (agents can bridge disconnected systems) and constraints (can't integrate with a system that has no API). |
| **Data formats and standards** — what formats does the workflow produce and consume? (PDF, DOCX, JSON, XML, CSV, proprietary formats) | Determines output schema design. If the downstream system only accepts PDF, the agent must produce PDF. |
| **Network and access constraints** — VPN requirements, firewall rules, IP allowlists, air-gapped systems | Determines whether agents can access external APIs, cloud services, or must operate entirely within a closed network. |

---

## 4. WHAT STOPS THEM — Constraints & Boundaries

| What to know | Why it matters |
|---|---|
| **Compliance obligations** — regulatory requirements, industry standards, professional body rules that govern the workflow | The hardest constraint. If the law says a qualified person must review X, the agent can prepare X but never finalise it. This is a non-negotiable authority boundary. |
| **Security requirements** — data classification levels, encryption standards, access control policies, data residency rules | Determines what data agents can see, where they can process it, and what they can store. Some data may be off-limits entirely. |
| **Privacy constraints** — personal data handling rules (GDPR, Australian Privacy Act, client confidentiality obligations) | Determines whether agents can use external LLMs (data leaves the organisation) or must use local models only. This is a common dealbreaker for cloud-based agent services. |
| **Budget constraints** — what can they spend on agent infrastructure, ongoing costs, and human time for oversight? | Determines the realistic scope of what gets built. A $500/month budget designs very differently than a $50,000/month budget. Maps to CC-7 Cost Budget. |
| **Time constraints** — deadlines, urgency, how soon they need the workflow operational | Determines whether to start with shadow mode (safe, slow) or whether time pressure demands faster (but riskier) deployment. Time pressure restructures human oversight — it doesn't eliminate it. |
| **Contractual constraints** — client contracts, vendor agreements, SLAs that limit what can be automated or outsourced | Some contracts prohibit third-party processing of client data, which would block most agent deployments. |

---

## 5. WHAT BREAKS — Failure & Recovery

| What to know | Why it matters |
|---|---|
| **Current failure modes** — where does the existing workflow fail today? What goes wrong, how often, and what's the impact? | The design should fix existing failures, not introduce new ones. If the current manual process has a 5% error rate on a specific step, the agent needs to do better than 5% on that step or it's not worth building. |
| **Error tolerance** — what's the acceptable error rate for this workflow? Is one wrong answer in a thousand fine, or is any error catastrophic? | Determines verification intensity. A typo in a marketing email is recoverable; a wrong number in a legal contract is not. Maps directly to the C×R governor and progressive autonomy speed. |
| **Reversibility of outcomes** — can the agent's output be undone? Easily, with effort, or not at all? | The most important single variable for determining how much autonomy an agent should have. Fully reversible outputs earn autonomy faster; irreversible outputs stay human-supervised longer. |
| **Current error-handling process** — what happens when something goes wrong today? Who catches it, how, and what do they do? | The existing error detection is the baseline. Agent verification must be at least as good, and the design should specify who catches agent errors that the current process wouldn't catch. |
| **Escalation paths** — who gets called when something goes wrong? What decisions require human intervention? | Defines the human side of the failure recovery register. If there's no clear escalation path, the design must create one. |
| **Cost of failure** — financial, legal, reputational, operational impact of the worst-case error | Determines how much to invest in verification infrastructure. High cost of failure = more verification layers, slower progressive autonomy, more human checkpoints. |

---

## 6. HOW THEY FEEL ABOUT IT — Attitudes & Preferences

| What to know | Why it matters |
|---|---|
| **Automation tolerance** — how comfortable are they with agents acting autonomously? Do they want to approve everything, or are they happy to let agents run within defined boundaries? | Determines the starting point for progressive autonomy. Someone who needs to see everything starts in shadow mode; someone who trusts the framework can start in advisory mode. |
| **Risk appetite** — are they cautious (verify everything, go slow) or comfortable with uncertainty (deploy, monitor, adjust)? | Affects deployment speed, verification intensity, and how much the design agent can recommend vs. must prove before implementing. |
| **Control preferences** — do they need to feel in charge, or are they comfortable delegating? | Connects to the identity threat (annoyance #15). If their identity is tied to doing the work, the design must position agents as amplification, not replacement. |
| **Trust calibration** — do they over-trust AI (rubber-stamp risk) or under-trust it (verification time tax)? | Over-trusters need structural checks (verification independence, can't skip review steps). Under-trusters need progressive autonomy with evidence (trust ledger data showing agents perform well). |
| **Change tolerance** — how much disruption to their existing workflow is acceptable? | Determines whether the design fits into current processes (low disruption) or redesigns processes around agent capabilities (high disruption). Start where they are, not where you wish they were. |
| **Communication preferences** — do they want concise summaries, detailed reports, or conversation? Do they prefer text, visual, or interactive? | Determines the output surface the design agent and the designed agents both use. Sarah Chen wants "the answer in one sentence with a yes or no," not a wall of text. |
| **Past AI experiences** — good, bad, or indifferent? What happened, and how did it make them feel? | The emotional baseline. Someone burned by a hallucinated contract clause will need more trust-building than someone who's never tried AI. |

---

## 7. WHO ELSE IS INVOLVED — Stakeholders

| What to know | Why it matters |
|---|---|
| **Other people in the workflow** — who else touches this work? (colleagues, managers, clients, external partners) | The designed workflow affects everyone who interacts with it. An agent that produces output for a colleague changes that colleague's work too. |
| **Approval chain** — who needs to approve what? How many layers of sign-off? | Determines where human authority boundaries sit and how many checkpoints the workflow needs. |
| **Client expectations** — do clients know or care if AI is involved? Are there contractual disclosure requirements? | Some clients require human-only work; others don't care. This affects whether agents can be used at all and whether their involvement must be disclosed. |
| **Team capabilities** — who else in the organisation can manage, configure, or override agents? | The Agent Orchestrator function. If no one else can do it, the design must account for the principal being the single point of failure for agent management. |
| **Upstream and downstream dependencies** — who provides input to this workflow, and who consumes its output? | The workflow is a node in a larger system. An agent that changes its output format may break the downstream consumer. |

---

## 8. WHAT THEY KNOW — Knowledge & Expertise

| What to know | Why it matters |
|---|---|
| **Tacit knowledge** — what do they know that they can't easily write down? The gut feelings, pattern recognition, and "I just know" expertise. | The hardest thing to capture but the most important. If the workflow depends on tacit knowledge, agents can't fully automate it — they can only prepare inputs for the human who holds that knowledge. |
| **Decision criteria** — when they make a judgment call, what are they actually weighing? What makes one option better than another? | Makes tacit knowledge explicit. If they can articulate their decision criteria, agents can prepare structured decision inputs. If they can't, the design must account for intuitive-only judgment. |
| **Edge case awareness** — what unusual situations do they watch for? What "never happens" scenarios actually do happen? | Edge cases are where agents fail most dangerously. The human's awareness of rare but critical situations defines what the agent must be designed to detect and escalate. |
| **Knowledge sources they trust** — which references, databases, colleagues, or resources do they rely on for accuracy? | Determines what the agent should access for grounding. If they always check X source before deciding Y, the agent should too. |
| **What they don't know** — gaps in their own expertise that they're aware of | The honest acknowledgment of knowledge gaps. Agents should be designed to flag when the task enters territory the human isn't expert in either — this is a system-level risk, not just an agent risk. |

---

## 9. WHAT THEY WANT — Goals & Success Criteria

| What to know | Why it matters |
|---|---|
| **Primary goal** — what's the ONE thing they most want to change? (time saved, accuracy improved, capacity increased, risk reduced, cost lowered) | The design must deliver on this goal first. Everything else is secondary. If they want time back, the design optimises for hours saved. If they want risk reduction, it optimises for verification. |
| **Success metrics** — how will they know the workflow is working? What numbers matter? | Defines what the trust ledger measures. If they care about override rate, track override rate. If they care about time-to-completion, track that. |
| **Non-negotiables** — what must NEVER change regardless of efficiency gains? | Hard boundaries. If client communication must always be human-to-human, no agent drafts client emails — period. |
| **Desired future state** — what does their ideal workday look like? What would they do with the time they get back? | Phase 0 vision. The design should move them toward this, not just away from current pain. Sarah Chen wants to be home by 6:30 and mentor younger lawyers — the design should create space for that. |
| **Willingness to invest** — time for design sessions, time for shadow mode review, budget for tools and infrastructure, time for training | The design that can't be implemented is worthless. Willingness to invest determines the realistic scope of what gets built and how fast. |
| **Exit criteria** — what would make them abandon the agent workflow and go back to manual? | Defines the trust failure threshold. If accuracy drops below X%, or if overrides exceed Y%, the workflow should flag and potentially revert — not silently continue failing. |

---

## PRIORITY TIER

Not everything above is needed on day one. Here's a rough priority:

**Must have before designing anything** (gates the design):
- Role and decision authority
- End-to-end task map
- Compliance and security constraints
- Reversibility of outcomes
- Primary goal
- Non-negotiables

**Should have during design** (shapes quality):
- Current tool stack and integration points
- Current failure modes and error tolerance
- Automation tolerance and trust calibration
- Other people in the workflow and approval chain
- Tacit knowledge and decision criteria
- Budget and time constraints

**Nice to have / emergent** (refines over time):
- Cognitive style and communication preferences
- Past AI experiences
- Seasonal/peak patterns
- Desired future state
- Exit criteria

---

The critical insight: **most of this information is about BOUNDARIES, not capabilities.** The design agent needs to know where the lines are — what the agent can't do, what the human must keep, what the system enforces, what compliance demands — far more than it needs a list of features or capabilities. This is the Boundary Way in practice: boundaries before capabilities, never-rules before what-it-does.The framework is captured. The key structural insight — **boundary information gates design; capability information only refines it** — is the same principle running through everything from CAWDP's Phase 0 identity questions ("What would VIOLATE its identity?" comes before "What does it do?") to the consulting Boundary Journey (Milestone 1 draws the line before anything else).

This also connects directly to the CAWDP Design Studio: the Mirror Agent's intake phase needs this information, and the priority tiers map to progressive disclosure — must-have information gates the design (you literally can't design without it), should-have shapes quality, and nice-to-have refines over time (emergent from the trust ledger and ongoing use).

---

## Run 4 — unknown ✓ COMPLETED

*2026-04-27T07:18:13* · `glm-5.1:cloud` · `ff0c4074...`

### Prompt

what information about a user would it be useful for the agent to have access to, when working with a user to design an agent or agentic workflow?

### Response

Great question! This spans business strategy, UX design, and agentic architecture — so let me pull in the full team to get a well-rounded answer. I'll create tasks for each specialist to weigh in from their domain, then synthesize the results.All three tasks are independent — let me run them in parallel to get each perspective simultaneously.All three experts have delivered rich, detailed perspectives. Let me synthesize these into a unified framework.Here's the **synthesized framework** — what information about a user is useful for an agent to have when designing an agent or agentic workflow:

---

# User Context for Agent Design: A Unified Framework

The three perspectives (business strategy, UX/interaction, and agentic architecture) converge on a critical insight: **the agent doesn't need a flat user profile — it needs typed calibration parameters, each of which changes a specific aspect of its behavior.** Below is the consolidated taxonomy, organized into **8 domains**, each with a clear purpose and priority tier.

---

## 1. 🧑 WHO THEY ARE — Identity & Authority

> **What it calibrates:** Where the human authority boundary sits, what the agent can decide vs. escalate, and how the agent speaks.

| What to Know | Why It Matters |
|---|---|
| **Role & decision authority** | Can they approve budget? Deployment? Tool changes? If not, who can? Wrong assumption = designing for someone who can't implement. |
| **Domain expertise depth** | What they know deeply (years of judgment, pattern recognition) = what agents should **NOT** replace. Defines the human side of complementarity. |
| **Technical fluency** | "Pydantic schema" vs. "a structured form." Determines specification surface, vocabulary, and whether to expose implementation details. |
| **Cognitive style** | Big-picture vs. step-by-step? Framework-first vs. example-first? Changes entire interaction mode, session structure, and disclosure sequence. |
| **AI/automation experience** | First-time users need possibility expansion; experienced users need boundary calibration. Past failures create justified caution. |
| **Identity threat level** | How much of their professional identity is tied to the work being automated? High threat → design as amplification, not replacement. |

---

## 2. 🏢 WHERE THEY WORK — Organizational & Environmental Context

> **What it calibrates:** Governance complexity, integration requirements, stakeholder landscape, and how much verification infrastructure is needed.

| What to Know | Why It Matters |
|---|---|
| **Industry & domain** | A law firm's risk tolerance and regulatory environment are fundamentally different from a marketing agency's. Failure modes are domain-specific. |
| **Organization size & structure** | 3-person firm vs. 500-person enterprise — different governance, deployment complexity, and team structures. |
| **Team composition & reporting** | Who does what now? Who would interact with the agent? Who verifies output? Complementarity allocation depends on knowing who the humans are. |
| **Organizational culture** | "Move fast" vs. "everything reviewed twice" — determines how much verification infrastructure is needed. |
| **Stakeholder landscape** | Who else is affected? Who reviews output? Who bears liability? The agent must serve the full human ecosystem, not just the primary user. |
| **Approval chain** | How many layers of sign-off? Determines where human checkpoints must exist. |
| **Client expectations** | Do clients require human-only work? Must AI involvement be disclosed? Affects whether agents can be used at all. |

---

## 3. 🔄 WHAT THEY DO NOW — Current Workflows

> **What it calibrates:** Task decomposition, complementarity analysis, and where agents create the most value.

| What to Know | Why It Matters |
|---|---|
| **End-to-end task map** | The starting point for complementarity analysis. You can't allocate work without knowing what the work IS. |
| **Time distribution per task** | Where does time go? 8 hours of mechanical review is a different target than 30 minutes of nuanced judgment. |
| **Current bottlenecks** | Where work piles up = highest-value target for agent assistance. |
| **Variation patterns** | High variation needs more human judgment; low variation is ripe for full agent handling. Maps to confidence × reversibility governor. |
| **Volume & frequency** | Determines ROI — high volume justifies infrastructure investment; low volume may not. |
| **Current failure modes** | Where does the workflow break today? Agent design should fix existing failures, not introduce new ones. |
| **What's been tried & abandoned** | Previous AI attempts that failed — why? These are the specific problems the design must avoid recreating. |

---

## 4. 🛠️ WHERE IT LIVES — Tools, Systems & Data

> **What it calibrates:** Architecture constraints, integration design, output schemas, and what's technically feasible.

| What to Know | Why It Matters |
|---|---|
| **Current tool stack** | Agents must integrate with existing systems (LEAP, Salesforce, Outlook, etc.), not create parallel workflows. |
| **Data sources** | Where does information come from? Determines what agents can access automatically vs. what needs manual input. |
| **Data sinks & formats** | Where does output go? PDF, DOCX, JSON? Downstream systems dictate output schema. |
| **Integration points** | What connects to what? Which systems talk, and which don't but should? Identifies bridging opportunities and hard constraints. |
| **Network & access constraints** | VPN, firewalls, air-gapped systems — determines whether agents can use external APIs or must operate locally. |
| **Skill ceiling for maintenance** | Who maintains this after deployment? An agent needing a developer is useless if the team doesn't have one. |

---

## 5. 🚧 WHAT STOPS THEM — Constraints & Boundaries

> **What it calibrates:** Hard boundaries that gate design — these are non-negotiable, not preferences.

| What to Know | Why It Matters |
|---|---|
| **Compliance obligations** | The hardest constraint. If the law requires a qualified person to review X, the agent can prepare but never finalize X. |
| **Security & privacy requirements** | Data classification, encryption, residency rules. Determines what agents can see, process, and store. May block cloud-based agents entirely. |
| **Contractual constraints** | Client contracts prohibiting third-party data processing. Common dealbreaker for agent deployment. |
| **Budget** | $500/month vs. $50,000/month — fundamentally different design scope. |
| **Timeline & urgency** | "Needed yesterday" vs. "planning for next quarter" — time pressure restructures oversight, it doesn't eliminate it. |
| **Non-negotiables** | What must NEVER change regardless of efficiency gains. Hard boundaries the design cannot cross. |

---

## 6. 💥 WHAT BREAKS — Failure, Risk & Stakes

> **What it calibrates:** Verification intensity, progressive autonomy speed, and how much to invest in safety infrastructure.

| What to Know | Why It Matters |
|---|---|
| **Reversibility of outcomes** | The single most important variable for autonomy decisions. Fully reversible → autonomy faster; irreversible → human-supervised longer. |
| **Cost of failure** | Financial, legal, reputational impact of worst-case error. High cost = more verification layers, slower autonomy. |
| **Error tolerance** | What's acceptable? 99% accuracy means different things for marketing emails vs. medical diagnoses. |
| **Who bears the risk** | Who gets sued if it's wrong? If the user bears all risk, the spec needs stronger verification and human-judgment gates. |
| **Current error-handling process** | What happens when something goes wrong today? Agent verification must be at least as good. |
| **Escalation paths** | Who gets called? What requires human intervention? The design must define this if it doesn't exist. |
| **Past AI failures** | What went wrong before? Specific failures create specific trust barriers and resistance patterns. |

---

## 7. 🤝 HOW THEY INTERACT — Trust, Cognition & Communication

> **What it calibrates:** The interaction surface — how often the agent explains reasoning, how it signals uncertainty, output format, session rhythm.

| What to Know | Why It Matters |
|---|---|
| **Baseline trust level** | "Trust until proven otherwise" vs. "trust nothing until earned." Changes entire interaction model — verification-first vs. boundary-first design. |
| **Automation tolerance** | "I approve everything" vs. "tell me when something needs attention." Starting point for progressive autonomy. |
| **Control preference** | Need to feel in charge, or comfortable delegating? High control = more checkpoints, more transparency. |
| **Cognitive load budget** | Not capacity — current load. 30 contracts in review = different information density than strategic planning. |
| **Abstraction preference** | Frameworks & patterns vs. concrete examples & stories. Maps to which interaction modality the agent uses. |
| **Decision fatigue pattern** | When does decision quality drop? Front-load or back-load critical decisions accordingly. |
| **Communication preferences** | Prose vs. structured vs. visual. "One sentence with a yes or no" vs. "show me the reasoning." |
| **Uncertainty signal preference** | Confidence %, verbal hedges, explicit flags, or structured metadata? |
| **Verification instinct** | Does the user naturally verify, or does the agent need to prompt it? Low instinct = forced checkpoints. |
| **Accessibility needs** | Language proficiency, screen reader compatibility, visual processing needs, attention differences, motor constraints. |

---

## 8. 🎯 WHAT THEY WANT — Goals & Success Criteria

> **What it calibrates:** What the agent optimizes for, how it frames trade-offs, what it prioritizes.

| What to Know | Why It Matters |
|---|---|
| **Primary motivation** | Efficiency, quality, capability, or compliance? Different motivations = fundamentally different agent designs. |
| **Desired outcome (not "agent that does X")** | "Spend 70% of my time on judgment work instead of 30%" vs. "handle 20 more clients without hiring." The outcome determines the spec. |
| **Success metrics** | Time saved, error rate, override rate, cost reduction? The agent can't optimize what it can't measure. |
| **Acceptable accuracy threshold** | What error rate is tolerable? Determines verification intensity and progressive autonomy ceiling. |
| **Progressive autonomy target** | Full autonomy eventually, or always human-in-the-loop? Determines the autonomy path length and endpoint. |
| **Desired future state** | What does their ideal workday look like? The design should move them toward this, not just away from current pain. |
| **Exit criteria** | What would make them abandon the agent and go back to manual? Defines the trust failure threshold. |
| **Willingness to invest** | Time for design, time for shadow mode, budget, training capacity. Determines realistic scope. |

---

## 🔑 Three Critical Meta-Principles

### 1. Boundary Information Gates Design; Capability Information Only Refines It
The agent needs to know where the **lines** are — what it can't do, what the human must keep, what compliance demands — far more than a list of features. Never-rules before what-it-does.

### 2. Capture Progressively, Not All at Once
Don't ask everything in minute one. The intake phase needs ~20% of this — role, problem, stakes, and trust level. The rest emerges through the design process as it becomes relevant. Some things (cognitive style, trust level, technical fluency) are better **observed** than asked.

### 3. This Is a Type Collision Problem
These 40+ variables are **typed calibration parameters**, not a flat user profile. Trust variables change verification behavior; cognitive variables change interaction modality; expertise variables change vocabulary. They should be stored as **typed, structured, metadata-rich objects** (with confidence, provenance, and recency) — not stuffed into a single context window.

---

## 📊 Priority Tiers

**🔴 Must have before designing anything** (gates the design):
- Role & decision authority
- End-to-end task map
- Compliance & security constraints
- Reversibility of outcomes
- Primary goal
- Non-negotiables

**🟡 Should have during design** (shapes quality):
- Tool stack & integration points
- Failure modes & error tolerance
- Automation tolerance & trust calibration
- Stakeholders & approval chain
- Budget & time constraints
- Domain expertise & tacit knowledge

**🟢 Nice to have / emergent** (refines over time):
- Cognitive style & communication preferences
- Past AI experiences
- Seasonal/peak patterns
- Desired future state
- Exit criteriaThe framework above is the full synthesis. If you'd like, I can also:
- **Map each variable to specific agent behavior changes** (e.g., "if trust is low → increase verification frequency by X, surface uncertainty explicitly, use confidence scores")
- **Design a progressive intake protocol** — what to ask first, what to observe, what to derive, and when
- **Create a typed schema** for storing these as structured knowledge objects rather than a flat profile

---
