# The Architecture of Trust: A Handbook for Designing Human-Centred Agentic Systems

**Format:** 22 chapters, approximately 320–380 pages. Each chapter opens with the central question it answers, closes with **Leader's Take** (key decisions and governance implications) and **Designer's Take** (instruments and design actions). Practitioner instruments are embedded in the relevant chapter, not exiled to appendices.

***

## Front Matter

- **How to Use This Book** — Two reading paths: the leader's path (Parts I, II, V, VI, VII) and the designer's path (all parts). Explicit about what each audience can skip without losing the argument.
- **A Note on Durable Principles** — The design decisions in this book will outlast the tools available today. Where tooling is relevant, it is named as an example, not a prescription.

***

## Part I: The Case for Getting This Right
*The economic and human argument before any design work begins*

### Chapter 1 — The Coordination Cost Problem ✅
The book's opening argument, stated plainly. AI systems that cannot be trusted do not eliminate coordination costs — they move them. Verification overhead, error recovery, accountability gaps, and governance overhead can negate and frequently exceed the value the system was meant to create.  The institutional economics lens: structural trust reduces coordination costs more efficiently than reputational trust at every scale above a small, stable, high-context team. This is not an ethical argument. It is an operational one, and it is the reason this book exists. 

*Leader's Take:* The investment question to ask before any deployment.
*Designer's Take:* The coordination cost map as a pre-design diagnostic.

### Chapter 2 — Capable Is Not the Same as Trustworthy ✅
The decisive distinction. A highly capable agent can simultaneously be excellent at its task and working against the intent behind it.  Capability and alignment are independent dimensions. Most systems address this with policies — guidelines, guardrails, terms of use. These are declarative controls. They describe what should happen; nothing in the architecture makes harmful outcomes impossible. The gap between declaration and structure is where every well-documented AI failure has lived. Robodebt as the canonical case study. 

*Leader's Take:* How to tell whether your vendor is selling declarative or structural trustworthiness.
*Designer's Take:* The five questions that distinguish structural from declarative controls in any system.

### Chapter 3 — Is Your Organisation Ready? 🔲 *[new work required]*
The readiness assessment before investment is committed. Five organisational conditions that predict successful agentic deployment: problem definition discipline, governance maturity, human capability baseline, data infrastructure readiness, and change leadership capacity.  A structured readiness instrument. The most honest chapter in the book — most organisations are not ready in all five dimensions, and knowing which dimension is weakest determines where to invest first. Also addresses the build/buy/partner decision and what each choice demands of the organisation. 

*Leader's Take:* The readiness assessment instrument.
*Designer's Take:* Which readiness gaps create design constraints you'll need to work around.

***

## Part II: Starting with the Human
*The inversion that defines trustworthy agentic system design*

### Chapter 4 — The Human as the Unit of Design ✅
The most important structural choice in this book: design starts with the human, not the agent. Before any agent is specified, the designer needs a human profile — what this person values, where they excel, where they fail, and what would make them genuinely better at their work.  Two design modes: strengths amplification (additive — agents create conditions for peak performance) and weakness compensation (corrective — agents catch failure modes before they cause harm). The chapter introduces the meta-question that validates all design decisions that follow: *what does this human gain in capability from every interaction with this system?* 

*Leader's Take:* The questions to ask when evaluating whether a proposed system serves your people or just serves throughput.
*Designer's Take:* Introduction to the Human Performance Map instrument.

### Chapter 5 — The Human Performance Map 🔲 *[new work required]*
The practical instrument that makes Chapter 4 actionable. Seven dimensions: what limits throughput, what degrades decision quality under pressure, what produces best output, what depletes the person, what capability ceiling they're hitting, what they can't currently access, and what they should be able to do in twelve months that they cannot today. Worked examples across knowledge worker, clinician, and operations manager profiles. The instrument output feeds directly into the Framing Declaration in Chapter 7.

*Leader's Take:* Using the map to set human-centred success criteria before procurement begins.
*Designer's Take:* The full instrument with completion guidance.

### Chapter 6 — The Complementarity Boundary ✅
What belongs to the agent and what must remain human — drawn explicitly as a design decision, not discovered at runtime when something goes wrong.  Task classification across four dimensions: consistency (routine vs. novel), parallelisability (independent vs. sequentially dependent), reversibility (undoable vs. permanent), and ethical weight (rule-following vs. judgment required). The skill atrophy risk: aviation's automation surprise translated to knowledge work. The complementarity boundary as the document that makes every subsequent design decision contestable and auditable. 

*Leader's Take:* The governance questions about where human judgment is genuinely required.
*Designer's Take:* The classification matrix as a design instrument.

***

## Part III: Framing the System
*The decision that shapes every other design choice*

### Chapter 7 — Choosing a Framing ✅
The highest-leverage design decision in agentic systems is also the most commonly skipped. Most systems are built inside an implicit framing that was never consciously chosen. The default — agents do work for humans — is often the least appropriate and the most quietly damaging.  Introduces the five design axes and thirteen framings, presented as a decision space rather than a taxonomy. Covers the critical tensions: doing vs. capability development; performance optimisation vs. stewardship; cognitive extension vs. teammate. 

*Leader's Take:* The framing as a governance instrument — it makes the system's purpose explicit and contestable.
*Designer's Take:* The framing as the constraint that governs principle weighting and conformance profile.

### Chapter 8 — The Framing Declaration ✅
The practical instrument. Five sequential decision gates — each resolving one axis before the next opens: Who are you designing for? What is the nature of the work? What does success look like, and when? What kind of relationship should this be? Who else is affected?  Each gate's output is named and defined. The declaration's three-part structure: primary framing, temporal commitment (present performance vs. future capability vs. both), and mandatory layers (framings that are structurally required regardless of the primary choice). The meta-question that validates the whole: *what does this human gain in capability — not just in output — from every interaction?* 

*Leader's Take:* The Framing Declaration as a governance document — the first artefact produced before any build decision.
*Designer's Take:* The worksheet with completion guidance and common failure patterns.

***

## Part IV: Designing the System
*The design framework — at the altitude a practitioner can use*

### Chapter 9 — Foundation: Purpose, Identity, and the Agent's Role ✅
The first design decisions: why the agent exists, what it fundamentally is, and what role it plays. Human intent, human development, goal vs. task, the complementarity boundary as a structural constraint.  Role archetypes — executor, reviewer, orchestrator, synthesiser, articulation agent, exploration agent — presented as non-interchangeable structural roles with concrete failure modes when confused. Cognitive orientation as a deliberate design choice. The two questions every design decision must answer: *did the agent produce the right output* (fidelity) *and does every interaction leave the human more capable* (enrichment)? 

*Leader's Take:* The role archetype as a procurement and governance instrument.
*Designer's Take:* Role-capability mapping and the cognitive orientation decision.

### Chapter 10 — Specification: The Highest-Leverage Layer ✅
The layer the industry most consistently underestimates. Output quality is determined more by specification quality than by any property of the agent.  Three sequential stages: explore the option space before committing to a direction; choose a direction explicitly, recording the alternatives set aside; specify verifiable acceptance criteria that predate execution. The proof template as a contract — the deliverable is not the work, it is the verified evidence that the work meets its specification. The verifiability test: if you cannot tell whether an output passes or fails without asking the agent, the criteria are ambiguous. Ambiguity in a specification is a bug. 

*Leader's Take:* Specification quality as a governance metric — the single most predictive indicator of deployment success.
*Designer's Take:* The proof template library with domain examples.

### Chapter 11 — Context: What the Agent Knows, and When ✅
More context actively degrades agent performance. Minimum sufficient context is a correctness condition, not an optimisation.  The difference between informational context (task-specific, provided upfront) and knowledge (global, queried on demand). Epistemic context — the upstream reasoning provenance that enables downstream agents to calibrate trust rather than inherit outputs blindly. The sterile cockpit principle applied to context design. Progressive disclosure and why it matters for performance and cost. 

*Leader's Take:* Context design as a cost and quality management decision.
*Designer's Take:* The context card template and the forbidden reads principle.

### Chapter 12 — Trust, Safety, and Structural Guarantees ✅
How trustworthy outputs are produced by construction, not by intention. Independent verification as architecture rather than policy — the executor cannot hold the verify tool for its own output.  Belief revision protocols vs. verification gates: the difference between a marking scheme and peer review. Proof as product. Immutable audit trail. Fail-safe defaults. Uncertainty as a structural primitive — raising uncertainty is correct behaviour, never penalised. Reversibility classification before action. The cognitive diversity safety concern: how organisations interacting with the same agent systems converge toward homogeneity without noticing. 

*Leader's Take:* The five structural guarantees to require from any agentic system before deployment.
*Designer's Take:* The verification architecture decision tree.

### Chapter 13 — Multi-Agent Systems: Designing the Ensemble ✅
When to use a single agent and when to compose a system. Architecture patterns — executor/reviewer separation, supervisor-worker, specialist networks, peer review pipelines — with concrete guidance on when each applies.  Coalition formation by epistemic complementarity rather than functional role coverage: agents with genuinely different cognitive orientations produce qualitatively different outcomes. The Information Diversity Score as the primary pipeline health indicator beyond output accuracy. What passes between agents — not just outputs but reasoning traces, confidence calibrations, and option spaces explored. Human-in-the-loop placement at irreversible decision thresholds, not as an approval checkbox. 

*Leader's Take:* The governance questions about accountability in multi-agent pipelines.
*Designer's Take:* Pipeline topology decision framework and handoff specification.

***

## Part V: Structural Trust
*Making untrustworthy outcomes architecturally impossible*

### Chapter 14 — From Declared to Structural: The Trust Architecture ✅
The shift that defines this book. Declarative ethics describes what should happen. Structural ethics makes harmful outcomes architecturally impossible.  The 24 principles of the Structural Trust Framework presented at a governance altitude: what each category (Purpose, Trust, Performance, Learning, Accountability) is preventing and what it is enabling. The economic argument for structural trust: it scales without proportional governance overhead. The ONE ontology presented as a concept — reality as the design substrate, principles enforced as database constraints — without the schema detail. 

*Leader's Take:* How to evaluate any vendor's "trustworthy AI" claims against structural vs. declarative criteria.
*Designer's Take:* Pointer to the full principle reference in the appendix.

### Chapter 15 — Conformance: Choosing the Right Level of Trust ✅
Four tiered conformance profiles — Core Trust, Full Lifecycle, High-Stakes/Regulated, Blockchain Trust Layer — and how the Framing Declaration determines which is appropriate.  The incremental adoption path: instrumentation first, enforcement second, optimisation third. The Proof of Value Layer: how the framework produces continuous, structured evidence of its own effectiveness. The three-part adoption question every organisation must answer: what profile does this deployment require, what profile is the organisation currently capable of implementing, and what is the gap plan? 

*Leader's Take:* The conformance profile as a procurement specification and audit criterion.
*Designer's Take:* Adoption pathway with common failure patterns and mitigations.

***

## Part VI: Governance, Compliance, and the Hard Cases
*Making the framework deployable in regulated, multi-party, and high-stakes contexts*

### Chapter 16 — Governance Architecture and Regulatory Alignment 🔲 *[new work required]*
Practical governance architecture for enterprise deployments. Explanation and contestation mechanisms — how affected parties can understand and challenge decisions.  Regulatory alignment: what conformance with the STF satisfies across ISO 42001, NIST AI RMF, EU AI Act, and Australia's AI governance requirements, and where genuine gaps remain. Risk tiering: how consequence severity, reversibility, and stakeholder exposure govern which principles are mandatory, which are advisory, and which conformance profile is the regulatory minimum. The proportionality instrument. 

*Leader's Take:* The regulatory minimum conformance map — what you must do vs. what you should do.
*Designer's Take:* The risk tiering matrix and its connection to specification depth.

### Chapter 17 — Data Governance, Supply Chain, and Third-Party Agents 🔲 *[new work required]*
Two governance challenges the existing frameworks do not yet address. Data governance in agentic pipelines: data provenance, consent surfaces, retention and access control when agents handle regulated data, and the intersection of minimum sufficient context with deletion rights.  Third-party agent governance: trust inheritance when your pipeline delegates to agents you didn't build, capability attestation, and liability allocation in multi-party deployments. The current state of agent-to-agent trust protocols (MCP, A2A) and their governance limitations. 

*Leader's Take:* The contractual and regulatory questions to ask before integrating any third-party agent.
*Designer's Take:* The provenance design pattern and the trust inheritance decision.

### Chapter 18 — Explainability Architecture 🔲 *[new work required — from provided concept]*
Explainability as a structural property, not a retrospective feature. ExplanationDocument as a first-class artefact produced alongside every consequential output.  Chain-of-thought visibility for human reviewers. Policy traceability — how a decision connects back to the specification, acceptance criteria, and framing declaration that produced it. Bias auditability. How explainability requirements differ across conformance profiles and regulatory contexts. The mechanism by which the affected party's right to understand and contest decisions is technically realised rather than procedurally claimed. 

*Leader's Take:* The three explainability questions to ask before any customer-facing or consequential deployment.
*Designer's Take:* The ExplanationDocument template and the traceability chain design.

***

## Part VII: Knowing Whether It's Working
*Evaluation, observability, and the methodology that makes proof a practice*

### Chapter 19 — Evaluation: Testing the Full Lifecycle 🔲 *[new work required]*
Testing agentic systems requires a categorically different methodology from testing software. Single-turn evaluation misses failures that only emerge across multi-step tasks.  Evaluation dimensions: planning quality, tool selection, intermediate correctness, error recovery, memory usage, and long-horizon consistency. Offline evaluation (golden datasets, adversarial testing, red-teaming), online evaluation (canary, shadow deployment), and human-in-the-loop review for high-stakes outputs. LLM-as-judge approaches and their structural limits — why they are useful and where they fail. Building an evaluation pipeline before deployment, not after the first incident. 

*Leader's Take:* The three evaluation questions that should be contractual requirements.
*Designer's Take:* The evaluation pipeline design pattern.

### Chapter 20 — Observability: Knowing What the Agent Is Doing ✅🔲 *[partially new work]*
Observability is the aviation black box — it exists not for real-time use but for post-incident accountability and for learning.  Telemetry design for agentic systems. Trace capture and structured logging as the runtime realisation of the immutable audit trail. Continuous monitoring for model drift, input distribution shift, and prompt regression after model version changes. Incident response when an agent takes a harmful action — the runbook structure. The connection between observability and the Proof of Value Layer: runtime evidence feeding the framework's own continuous improvement loop. 

*Leader's Take:* Observability as a governance requirement, not a developer nicety.
*Designer's Take:* The monitoring instrument and the incident response protocol.

***

## Part VIII: Strategy and What This Makes Possible
*For the leader thinking beyond the current deployment*

### Chapter 21 — Redesigning Work: The Human Transition 🔲 *[new work required]*
The transition that most technical books ignore entirely. As agents take on execution, human roles shift toward goal-setting, trade-off navigation, and agent orchestration.  The change management challenge — what resistance looks like and why it is rational, how to redesign roles without destroying the human value organisations depend on, what skill development looks like for people working alongside agents. The direct connection to framing: organisations that built with Framing 10 (capability developer) create people prepared for this transition; those that defaulted to Framing 1 (agents do work) find their people least prepared precisely when the transition is unavoidable. 

*Leader's Take:* The five role redesign principles and the change leadership playbook.
*Designer's Take:* The human capability compounding design pattern — building systems that make people better, not dependent.

### Chapter 22 — What This Makes Possible ✅🔲 *[partly new work]*
The closing argument at civilisational scale — earned by everything that came before. Coordination cost reduction as the measurable value proposition.  What structurally trustworthy, human-centred agentic systems make accessible to people and organisations who currently lack it — the equaliser framing at population scale. The governance institutions question: what would governance structures look like if the structural trust principles were applied not to a single organisation but to the multi-stakeholder, multi-jurisdictional contexts that high-capability agentic systems will inevitably inhabit? Honest about what is speculative. Ambitious about what is possible. The question that leaves a leader with something to think about on the drive home. 

*Leader's Take:* The strategic horizon question: what would your organisation look like if this worked at full scale?
*Designer's Take:* The research agenda — the open design questions whose answers would advance this field.

***

## Appendices

| | |
|---|---|
| **A: The Framing Declaration Worksheet** | Five gates as a one-page instrument ✅ |
| **B: The Human Performance Map** | Standalone instrument with completion guide 🔲 |
| **C: The Agent Empathy Map** | Facilitative ecosystem design instrument ✅ |
| **D: 24 Principles Quick Reference** | One page per principle with fidelity and enrichment questions ✅ |
| **E: Proof Template Library** | Domain templates — software, legal, financial, clinical ✅ |
| **F: Conformance Profile Checklist** | Pre-deployment review by profile tier ✅ |
| **G: Regulatory Alignment Reference** | Clause-level mapping across major frameworks 🔲 |
| **H: Glossary** | 40 terms, precisely defined ✅ |

***

## What This Revision Achieves

| Dimension | Integrated Concept | This Revision |
|---|---|---|
| Chapter count | 30 | 22 |
| Primary format | Framework reference | Practitioner handbook |
| Human placement | Part II (Ch 4) | Part II (Ch 4) — preserved |
| Business case | Ch 27, near end | Ch 3, Part I |
| Economics thesis | Ch 28, near end | Ch 1, frames the whole book |
| Technical depth | Full in main text | Right altitude; detail in sidebars and appendix |
| Leader's utility | Implicit | Explicit — every chapter closes with Leader's Take |
| Designer's utility | Comprehensive | Precise — every chapter closes with Designer's Take |
| Instruments | Listed as appendices | Embedded in relevant chapters |
| Civilisational scope | Ch 30, standalone | Ch 22, earned by the preceding 21 chapters |
| New work required | 9 chapters | 7 chapters — same gaps, fewer of them |

The book is now genuinely readable by both audiences without either having to skip sections to find value. The leader reads a coherent economic and governance argument. The designer uses a complete set of instruments. And both finish Chapter 22 with the same question: *if this works at scale, what does it make possible?*