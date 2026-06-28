# AI UX Innovator

| Field | Value |
|-------|-------|
| **Session** | `a4bfe49e...` |
| **Type** | agent |
| **Agent** | AI UX Innovator |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-12T21:39:14 |
| **Runs** | 3 completed / 3 total |

## Run 1 — AI UX Innovator ✓ COMPLETED

*2026-04-12T21:39:14* · `glm-5.1:cloud` · `f6d4c07e...`

### Prompt

Currently, the most common surfaces for creating agent specifications are natural language markdown files, in code within IDEs, or web forms.

I'd like to explore alternatives that might surprise & delight non-technical users as they design agents that align with my agent design principles. 

Let's starty by understanding the problem space we are hoping to solve based on the following 'hunch'.
"I have a hunch that non-technical professionals and small business owners, feel excited but nervous about using AI tools largely due to non-intuitive and tech-heavy options."

Write a mini-persona profile and answer the questions in the problem space template below.

```
## The Principles as a Set of Questions

Every element collapses into two questions per layer that must be answered before an agent is deployed. Unanswered questions are guaranteed future failure modes.

| Layer | Fidelity question | Enrichment question |
| :---- | :---- | :---- |
| **Purpose** | Why does this agent exist, and what human need does it serve? | What does the human gain — in capability, understanding, or possibility space — from this interaction? Can they now perform unassisted at higher quality? |
| **Identity** | What is this agent's role, orientation, and capability boundary? | What epistemic metadata does this agent contract to attach to its outputs, and does its orientation contribute cognitive diversity to the pipeline? |
| **Specification** | Are criteria verifiable, pre-existing, and type-resolved? | Was the option space explored and a direction chosen before criteria were written? Do the acceptance criteria specify which information types must be decomposable? |
| **Context** | What is the minimum information this agent needs, and when? What information boundaries are structurally enforced? | What epistemic context does the agent receive from upstream? Is that context typed or raw prose? |
| **Trust** | Who verifies this work, at what independence level, and how is that level selected? | Do belief revision protocols allow the pipeline to improve its reasoning, not just verify its outputs? Is the audit trail assurance level matched to task stakes? |
| **Safety** | What are the fail-safe defaults, and where are the human gates? What recovery protocol operates when the agent halts? | Is cognitive diversity at the organisational level being actively preserved, not just individual output quality? |
| **Ecosystem** | Is the architecture matched to task structure? What is the per-invocation cost ceiling? | Are pipelines designed as epistemic exchanges? Is coalition formation by epistemic complementarity? Is diversity monitored? |
| **Improvement** | Are output quality, rework rates, and specification aging tracked? | Is pipeline intelligence — downstream capability gain — being measured alongside output accuracy? |
| **Human Enrichment** | Can the human now perform the task unassisted at higher quality than before? (Unverified enrichment is unconfirmed, not confirmed.) | Is every human more capable after every interaction than before it? Is the Scaffolding Dependency Index narrowing or widening? |
```

```
# Problem Space Statement Template

| Question | Your Response |
| :---- | :---- |
| What is the problem? |  |
| Who experiences it? |  |
| What is their goal? |  |
| What triggers the problem? |  |
| What are the root causes? |  |
| What are the impacts of the problem? |  |
| How is the customer getting around the problem? |  |

## Your Business Problem Statement

*Replace the appropriate sections with your answers from above:*

A person (user type, persona) has a goal in mind, BUT because of some kind of trigger, she encounters a problem in the way.  This problem has one or more underlying causes.  Experiencing this problem has one or more negative impacts on her. She might do a bunch of hacks and workarounds to deal with the problem, but it’s still a problem.
```

### Response

Now let me check if there's any relevant knowledge to enrich this analysis:---

# Mini-Persona Profile

## **Maria Santos — "The Expert Who Feels Like a Beginner"**

| Attribute | Detail |
|:--|:--|
| **Age / Role** | 42, Founder & Strategist, Lumina Marketing (boutique consultancy, 5 staff) |
| **Background** | 15 years in brand strategy. Built her business on instinct and client trust. Reads people and markets with exceptional accuracy. Zero coding experience. |
| **AI Exposure** | Casual ChatGPT user for draft emails and brainstorming. Read a LinkedIn article about "AI agents that run your business." Watched a demo. Thought: *"I need this."* Then thought: *"I have no idea where to start."* |
| **Decision-Making** | Makes 50+ consequential decisions weekly — client scope, pricing, team allocation, creative direction. Comfortable with ambiguity. Discomfort with *appearing incompetent.* |
| **AI Emotional State** | **Excited** because she senses agents could multiply her strategic reach — "What if I had a partner that never forgot a client insight?" **Nervous** because every specification surface she's seen (markdown files, agent YAML, configuration web forms) speaks a language she doesn't speak and signals "this was not built for you." |
| **Core Fear** | Not that AI will fail — but that *she* will fail at specifying it, and the failure will prove she doesn't belong in this space. |
| **Core Desire** | A surface that makes her feel *smarter* for engaging with it, not *dumber* — one that draws out expertise she already has rather than demanding expertise she doesn't. |
| **Quote** | *"I can tell you exactly what I need my assistant to do. I could describe it for an hour. But the moment I see a form with 'system prompt' and 'tool configuration' — I freeze. Not because I don't know what I want. Because the form is asking me to think like a programmer, not a strategist."* |

---

# Problem Space Statement Template

| Question | Your Response |
|:--|:--|
| **What is the problem?** | Non-technical professionals with deep domain expertise cannot faithfully translate their knowledge into agent specifications through current surfaces, resulting in either abandonment ("AI isn't ready") or dangerously under-specified agents that fail silently in deployment — because the surface itself, not the user, is the bottleneck. |
| **Who experiences it?** | Non-technical professionals and small business owners who make complex decisions daily using narrative, relational, and experiential thinking — but whose mental models and vocabulary are misaligned with the systems-engineering register of current agent specification surfaces (markdown files, IDEs, configuration web forms). |
| **What is their goal?** | To design AI agents that genuinely serve their business needs — agents whose purpose, identity, specification, context, trust, safety, ecosystem, improvement, and enrichment properties are faithfully encoded — so the agent is aligned, trustworthy, enriching, and robust rather than brittle, opaque, and misaligned. In other words: they need to answer all 18 framework questions well, through a surface that lets them think the way they actually think. |
| **What triggers the problem?** | The moment of moving from *"I want an AI agent"* to *"I need to specify it."* The specification surface is the trigger — it demands a mode of thinking (systems engineering, formal specification, declarative configuration) that doesn't match how these users hold and express expertise (narrative, conversational, analogical, relational). The surface asks them to *write a spec* when what they naturally do is *describe a relationship.* |
| **What are the root causes?** | **① Type Collision at the Input Surface** — The 18 framework questions require fundamentally different cognitive modes (narrative meaning, boundary definition, verification design, safety configuration, outcome measurement, enrichment verification). Current surfaces collapse them all into one input type: text in a box. Every question feels harder than it is because the affordance doesn't match the thinking required. **② Vocabulary Mismatch** — The language of agent specification ("epistemic metadata," "type resolution," "information boundaries," "verification independence") is drawn from engineering and philosophy, not from the domains where these users hold expertise. The surface makes their knowledge invisible because it doesn't speak their language. **③ Incompetence Signaling** — Markdown files, IDEs, and YAML config forms all signal "this is a technical person's domain." Before the user writes a single word, the surface has triggered imposter syndrome. The medium says "you don't belong here" before the content asks "what do you know?" **④ Absence of Progressive Disclosure** — All 18 questions arrive simultaneously. A web form presents every layer at once. A markdown template shows every section. The user faces the full complexity of agent design in a single glance — no pathway, no sequence, no sense of "answer this, and the next question will make more sense." **⑤ No Feedback Loop** — Users don't discover whether their answers are sufficient until the agent fails in deployment. There is no live validation, no "here's what your agent will do based on what you've told me so far," no Principle Validator that catches gaps before they become failure modes. The form collects answers; it doesn't create understanding. **⑥ Missing Bridge** — No current surface helps the user *discover what they think through the act of answering.* The form assumes you already know before you write. But the 18 questions are designed to produce insight — they're not just data collection, they're thinking tools. A surface that treats them as data fields misses their deepest purpose. |
| **What are the impacts of the problem?** | **Abandonment** — "AI isn't ready for my business yet" (but really: the surface isn't ready for them). **Under-specification** — Users answer the accessible questions, skip the hard ones, and deploy agents with guaranteed failure modes. Per the framework, every unanswered question is a guaranteed future failure. **Mis-specification** — Users answer in the wrong register: too vague for verifiable criteria, too specific for purpose statements, wrong abstraction level for the question type. The agent gets built, but built wrong. **Trust erosion** — The agent behaves unpredictably because foundational questions went unanswered. The user's initial nervousness converts to confirmed distrust: "I was right to be nervous." **Expertise loss** — The user's rich, tacit domain knowledge never reaches the agent. The agent is impoverished by the surface's inability to accept what the user naturally provides. **Harm** — Under-specified agents operate without proper safety boundaries, information boundaries, or verification — agents without fail-safe defaults, without human gates at irreversible thresholds, without recovery protocols. The harm is not theoretical: it follows directly from unanswered Safety and Trust questions. **Inequality** — Agent design becomes a gated capability — only those who speak "systems engineering" can design agents well. This is a design failure, not a talent constraint. |
| **How is the customer getting around the problem?** | **Proxy specification** — Using ChatGPT to "write me a prompt" — creates a specification the user doesn't understand, can't evaluate, and can't adapt. The agent becomes someone else's design, not theirs. **Template copying** — Finding agent templates online and hoping one fits — but they can't evaluate fit because they don't understand what the template assumes. Copying a template is not answering the 18 questions; it's inheriting someone else's answers. **Consultant dependency** — Hiring a technical person to configure the agent — but this removes agency (literally). The agent becomes opaque magic, not a trusted partner. The user can't modify, extend, or understand it. This violates the Human Enrichment principle directly: it creates permanent dependency instead of progressive empowerment. **Trial and error** — Tinkering until something "sort of works" — but never answering the deep questions. The agent works for common cases and fails on edge cases the user never tested. **Avoidance** — Retreating to simple chat interfaces and never attempting to design a real agent. The excitement remains, the nervousness wins, and the potential is never realised. **Over-simplification** — Choosing "easy" agent builders that hide the 18 questions entirely. The agent deploys fast but with invisible gaps. Convenience becomes brittleness. |

---

## Your Business Problem Statement

Maria, a non-technical professional and small business owner who makes complex strategic decisions daily using narrative, relational, and experiential thinking, **has a goal** to design AI agents that genuinely serve her business — agents whose purpose, identity, specification, context, trust, safety, ecosystem, improvement, and enrichment properties faithfully encode her domain expertise so the agent is aligned, trustworthy, enriching, and robust, **BUT** because the moment she moves from "I want an AI agent" to "I need to specify it," she encounters a specification surface that demands systems-engineering thinking through text boxes, markdown files, or configuration forms — a surface that commits type collision (collapsing 18 cognitively distinct questions into one input type), speaks a vocabulary foreign to her expertise, signals "you don't belong here" before asking what she knows, presents all questions simultaneously without progressive disclosure, provides no feedback on whether her answers are sufficient, and treats the 18 questions as data collection rather than the thinking tools they actually are, **this problem** has six underlying causes: input surface type collision, vocabulary mismatch, incompetence signaling, absence of progressive disclosure, no feedback loop, and the missing bridge between answering and discovering. **Experiencing this problem** causes Maria to abandon AI tools, under-specify agents (creating guaranteed failure modes), mis-specify agents in the wrong register, erode her trust when agents behave unpredictably, lose the opportunity to encode her expertise, risk harm from agents deployed without proper safety and trust boundaries, and face an inequality where agent design capability is gated by systems-engineering literacy rather than domain expertise. She currently hacks around the problem through proxy specification (AI writes her prompts), template copying (hoping someone else's answers fit), consultant dependency (surrendering agency), trial and error (tinkering without understanding), avoidance (retreating to simple chat), or over-simplification (using builders that hide the questions entirely). But it's still a problem — and the deepest one is this: **the surface is telling Maria her expertise doesn't count because it can't accept it in the form she naturally holds it.**

---

The critical insight that emerges from this analysis: **your type collision observation applies symmetrically to inputs, not just outputs.** The 18 framework questions encode at least 6 distinct cognitive modes (narrative, boundary, verifiable, architectural, configurational, evaluative) — but current surfaces offer exactly one input modality for all of them. A new surface that gives each question type its own native interaction modality would not just reduce friction — it would make the questions *easier to answer well* by matching affordance to cognition. That's the design opportunity.

Shall I move next to mapping the 18 questions to their cognitive modes and brainstorming interaction modalities for each? That would be the bridge from problem space to solution space.Done — your memory now captures this exploration with the symmetric type collision insight preserved.

---

## Run 2 — AI UX Innovator ✓ COMPLETED

*2026-04-12T21:59:26* · `glm-5.1:cloud` · `4139bded...`

### Prompt

I'd like us to first understand the problems more. Take a look through a communications theory lens like the Shannon–Weaver model.
Are there other lens that helps us better understand the problems?

### Response

---

# The Problem Through Theoretical Lenses

---

## Lens 1: Shannon–Weaver Model

Shannon's model describes communication as:

```
INFORMATION SOURCE → TRANSMITTER → CHANNEL → RECEIVER → DESTINATION
                                         ↑
                                       NOISE
```

Let me map this precisely onto the specification surface problem.

### The Mapping

| Element | In Our System | What It Carries |
|:--|:--|:--|
| **Information Source** | Maria's domain expertise | Tacit, narrative, relational, analogical, experiential knowledge |
| **Transmitter** | The specification surface (markdown / IDE / web form) | The encoding device — converts Maria's knowledge into a transmittable signal |
| **Channel** | The text field | The medium through which the encoded signal travels |
| **Receiver** | The agent runtime | Decodes the signal into operational agent configuration |
| **Destination** | The deployed agent | Must faithfully enact all 18 encoded answers |

### Five Noise Sources (Not One)

Shannon identified noise as acting on the channel. Our system has **five** distinct noise sources, each destroying a different class of information:

**① Encoding Noise — At the Transmitter**

Maria possesses knowledge in rich, multi-modal form: she can *tell you a story* about why this agent matters, *point to boundaries* of what it should never do, *show you examples* of good and bad outputs, and *enact the rhythm* of how decisions should escalate. The surface demands she encode ALL of this into one signal type: text. The encoding process itself destroys information — not because Maria lacks knowledge, but because the codec (text-only encoding) cannot represent the full bandwidth of what she knows.

*Example:* Layer 1 (Purpose) asks "Why does this agent exist?" Maria could answer this in a 2-minute story about a client she nearly lost because a follow-up slipped. That story contains goal, context, emotional stakes, success criteria, and complementarity boundary — all five sub-questions answered in one narrative act. But the text field asks her to decompose that story into separate propositional answers, each stripped of the narrative structure that held them together. The encoding is lossy by design.

**② Channel Capacity Noise — At the Channel**

Shannon's most powerful insight: **a channel has a finite capacity determined by its bandwidth, and information exceeding that capacity is lost.** The text field is a single-type channel — it carries one signal type (character strings). When you try to transmit multiple signal types through a single-type channel, the excess types don't arrive degraded; they don't arrive at all.

This is the type collision insight in Shannon's language. The 18 questions encode at least 6 distinct signal types:

| Signal Type | Questions That Use It | What the Channel Strips |
|:--|:--|:--|
| **Narrative** | Purpose (L1), Enrichment (L9) | Temporal structure, emotional arc, causal chain |
| **Boundary** | Identity (L2), Context (L4), Safety (L6) | Sharp edges, exclusion zones, hard limits |
| **Verifiable** | Specification (L3), Trust (L5) | Testability, evidence structure, pass/fail clarity |
| **Architectural** | Ecosystem (L7) | Relationships, topology, data flow, dependencies |
| **Configurational** | Safety (L6), Context (L4) | Parameter settings, toggle states, thresholds |
| **Evaluative** | Improvement (L8), Enrichment (L9) | Metrics, trajectories, comparative judgments |

A text field can carry *words about* any of these. But it cannot carry the *native form* of any of them. A boundary drawn visually has different information content than a boundary described in prose. A metric displayed as a gauge has different information content than a metric written as a sentence. The channel strips the type information and leaves only the propositional residue.

**③ Semantic Noise — Between Transmitter and Receiver**

Even when Maria successfully encodes her answer into text, the vocabulary she uses may not match the vocabulary the agent runtime expects. She writes "My agent should never make a commitment on my behalf." The runtime needs `allowed_actions: ["commit"], denied: true`. The semantic distance between human language and machine language creates noise — the receiver decodes a signal that looks valid but carries different meaning than the sender intended.

This is not a translation problem (which would be solvable). It's an **ontology mismatch** — Maria and the runtime operate with different conceptual frameworks for the same reality. She thinks in "commitments I make to clients." The runtime thinks in "action classes and permission envelopes." The mapping between these is not one-to-one.

**④ Feedback Channel Noise — The Missing Return Path**

Shannon's model includes an implicit feedback channel — the receiver signals back whether the message was received successfully. In TCP/IP, this is the ACK. In human conversation, it's "Did you mean...?"

The current specification surface has **no feedback channel.** Maria writes her answer, submits it, and never knows whether the receiver decoded it correctly until the agent fails in deployment. There is no "ACK" for specification quality. No signal returns to tell her "I understood your purpose, but your safety specification has a gap" or "Your boundary description is ambiguous at this point."

This is perhaps the deepest Shannon failure: a communication system without a feedback channel cannot detect or correct transmission errors. The system is flying blind.

**⑤ Entropy Noise — At the Information Source**

Shannon defined information as the reduction of uncertainty (entropy). Maria's knowledge about her business has high entropy — it's complex, context-dependent, and partially tacit. The 18 questions are designed to *reduce entropy* — to extract structured, low-entropy answers from a high-entropy knowledge source. But the surface doesn't help with this entropy reduction. It demands low-entropy output (clear, structured answers) without providing the entropy-reduction mechanism (scaffolding, progressive disclosure, articulation assistance). Maria must perform all entropy reduction *before* she writes, in her head, with no support from the surface.

### What Shannon Uniquely Reveals

> **The problem is not that Maria can't answer the questions. The problem is that the communication channel cannot carry the type of signals her answers naturally take.** The information exists at the source. It is destroyed in transit — by encoding loss, channel capacity limits, semantic mismatch, and the absence of feedback. Shannon gives us a precise vocabulary for this: the channel capacity of a text field is insufficient for the information bandwidth the 18 questions require.

### Failure Signal

Maria writes something for every question, deploys the agent, and it behaves in ways she didn't intend. She says: "But I told it not to do that." She did. The channel just couldn't carry the signal.

---

## Lens 2: Affordance Theory (Gibson → Norman)

**Core idea:** An affordance is what an object *allows* you to do — its action possibilities. A chair affords sitting. A door handle affords pulling. The perceived affordance must match the intended action.

### The Mapping

| Question Type | Action Required | Affordance Needed | Affordance Provided |
|:--|:--|:--|:--|
| **Narrative** (L1, L9) | Tell a story | Conversation, timeline, storytelling | Text field |
| **Boundary** (L2, L4, L6) | Draw a line | Visual boundary, toggle, exclusion zone | Text field |
| **Verifiable** (L3, L5) | Define a test | Criteria builder, checklist, evidence template | Text field |
| **Architectural** (L7) | Design a structure | Topology editor, relationship mapper, flow builder | Text field |
| **Configurational** (L4, L6) | Set parameters | Sliders, toggles, dropdowns, threshold controls | Text field |
| **Evaluative** (L8, L9) | Make a judgment | Rating, comparison, trajectory indicator | Text field |

Every single action type gets the same affordance: **a cursor blinking in a text box.** This is the affordance equivalent of making every tool in a workshop a hammer.

### What Affordance Theory Uniquely Reveals

> **The surface doesn't just fail to help — it actively misleads.** A text field *affords* typing continuous prose. When you present a boundary question next to a text field, the user writes prose *about* the boundary instead of *drawing* the boundary. The affordance steers them toward the wrong cognitive action for the question type. The surface creates mis-specification, not just under-specification.

This is distinct from the Shannon insight: Shannon says the information is lost in transit. Affordance theory says the information is *misshapen at the point of creation* because the tool shapes the thinking.

### Failure Signal

Maria writes a paragraph about what her agent should never do, when what the agent needs is a hard boundary rule. The text field afforded storytelling about boundaries, not boundary-setting itself.

---

## Lens 3: Cognitive Load Theory (Sweller)

**Core idea:** Working memory is limited. Three types of load:
- **Intrinsic load** — inherent difficulty of the material (the 18 questions themselves)
- **Extraneous load** — unnecessary cognitive work imposed by the presentation format
- **Germane load** — productive effort that builds understanding

Good design minimises extraneous load and frees working memory for germane load.

### The Mapping

The 18 questions have **intrinsic load** — they are genuinely hard questions that require deep thinking. That load is appropriate and necessary.

But the surface adds massive **extraneous load**:

| Extraneous Load Source | What It Demands | Cognitive Cost |
|:--|:--|:--|
| Type collision | Switch between 6 cognitive modes without surface support | Mode-switching tax on every question |
| Vocabulary translation | Convert domain language into engineering language | Continuous mental translation |
| Absence of progressive disclosure | Hold all 18 questions in working memory simultaneously | Overwhelm from total complexity |
| No feedback | Evaluate own answer quality without external signal | Self-monitoring tax |
| Form layout | Navigate spatial relationships between questions that are logically sequential | Spatial vs. sequential mismatch |

**Germane load** — the productive thinking that actually answers the questions — gets squeezed out. Maria spends her limited working memory on *how to answer* (extraneous) rather than *what to answer* (germane).

### What Cognitive Load Theory Uniquely Reveals

> **The surface is cognitively parasitic.** It consumes the very cognitive resources the user needs to answer the questions well. The harder the question, the less capacity remains for dealing with the surface — which means the hardest questions (Safety, Trust, Ecosystem) get the worst answers, not because they're harder to think about, but because the surface has already depleted the cognitive budget before the user reaches them.

This is distinct from Shannon (information loss in transit) and Affordance (misshapen thinking) — this explains *why Maria gives up partway through*. She hasn't run out of knowledge. She's run out of working memory.

### Failure Signal

Maria's answers deteriorate as she moves through the layers. L1-Purpose is rich and specific. L7-Ecosystem is one sentence. L9-Enrichment is left blank. The gradient of answer quality maps directly to the depletion of cognitive resources.

---

## Lens 4: Distributed Cognition (Hutchins)

**Core idea:** Cognition is not confined to individual minds. It is *distributed* across people, artefacts, and environments. A cockpit is a cognitive system — the instruments, the layout, and the pilot all participate in the thinking. The artefacts don't just *record* thought; they *participate* in it.

### The Mapping

The current specification surface functions as a **transcription device** — it records finished thoughts. It does not participate in the thinking. It offers:
- No partial state holding (you can't sketch an idea and come back)
- No externalised structure (the relationships between the 18 questions exist only in Maria's head)
- No cognitive offloading (every answer must be fully formed before the surface accepts it)
- No representational aid (no visualisations, no mappings, no diagrams that do cognitive work)

A **distributed cognition** surface would function as a **thinking partner**:
- It would hold partial answers and show what's still missing
- It would externalise the relationships between layers (showing how L1-Purpose constrains L3-Specification)
- It would allow thinking-through-doing (sketching, rearranging, connecting)
- It would provide representations that reduce cognitive load (visuals that do work prose can't)

### What Distributed Cognition Uniquely Reveals

> **The surface makes Maria do ALL the cognition herself, then merely records the output.** This is the deepest failure: the surface could be a cognitive partner that extends her thinking, but instead it's a passive form that demands her thinking be complete before it engages. A well-designed surface doesn't just accept answers — it helps you *discover* answers. The 18 questions are designed as thinking tools, but the surface treats them as data fields.

This is distinct from all previous lenses: Shannon describes information loss, Affordance describes misshapen action, Cognitive Load describes resource depletion. Distributed Cognition describes **missed opportunity for cognitive partnership** — the surface could *extend* Maria's cognition, but instead it *parasitises* it.

### Failure Signal

Maria says "I know what I want, I just can't figure out how to put it into this form." This is the signature of a surface that demands transcription of pre-formed thoughts rather than enabling thinking-in-the-surface.

---

## Lens 5: Communication Accommodation Theory (Giles)

**Core idea:** In healthy communication, speakers **converge** — they adjust their speech patterns, vocabulary, and register toward each other. This convergence builds rapport, increases comprehension, and signals respect. When only one party converges, the other experiences **divergence** — which signals dominance, creates distance, and increases misunderstanding.

### The Mapping

In the current specification surface, the accommodation is **100% one-directional**:

| What Maria Must Do | What the Surface Does |
|:--|:--|
| Translate domain language → engineering language | Nothing |
| Adapt narrative thinking → propositional format | Nothing |
| Match the surface's vocabulary | Never shifts to match hers |
| Accept the surface's cognitive rhythm | Never adjusts to her pace |
| Answer questions in the surface's sequence | Never reorders based on her mental model |

The surface never converges toward Maria. It sits at the far end of every dimension — vocabulary, register, pace, sequence, modality — and demands she cross the entire distance alone.

### What Communication Accommodation Theory Uniquely Reveals

> **The surface communicates dominance.** It says, in effect: "My language, my format, my sequence, my pace. You adapt." This is the deeper reason behind Maria's nervousness — it's not just that the surface is unfamiliar, it's that the surface *refuses to meet her*. Every interaction with the surface reinforces the message: "This space was not designed for you." The excitement she feels is about the potential of agents. The nervousness is the surface telling her she doesn't belong.

This explains something the other lenses don't: **why Maria's emotional state matters for specification quality.** A surface that demands one-way accommodation doesn't just make the task harder — it makes the user feel *unwelcome*, which produces worse answers through a different mechanism: threat-induced cognitive narrowing. Under perceived social threat, working memory narrows, creative thinking contracts, and people retreat to safe, conventional answers rather than authentic, specific ones.

### Failure Signal

Maria's answers become generic and cautious — she writes what she thinks the surface "wants to hear" rather than what she actually knows. The specification is technically complete but authentically empty.

---

## Lens 6: Self-Determination Theory (Deci & Ryan)

**Core idea:** Humans have three basic psychological needs. When fulfilled, motivation is intrinsic and performance is high. When frustrated, motivation becomes anxious and performance degrades:
- **Competence** — feeling effective and capable
- **Autonomy** — feeling volitional and self-directed
- **Relatedness** — feeling connected and understood

### The Mapping

| Need | How the Surface Frustrates It | Consequence |
|:--|:--|:--|
| **Competence** | Every blank field signals "you don't know this." The engineering vocabulary makes her domain expertise invisible. | Maria feels incompetent *despite being expert* |
| **Autonomy** | The surface dictates the vocabulary, sequence, format, and modality. Maria can choose *what* to write, not *how* to express it. | Maria feels controlled, not self-directed |
| **Relatedness** | No surface acknowledges her context, her business, her language. No sense of "this tool understands my world." | Maria feels alone in a foreign country |

### What Self-Determination Theory Uniquely Reveals

> **The surface doesn't just make the task harder — it makes the human smaller.** It takes a competent professional and places her in an environment that systematically frustrates every basic psychological need. The result is not just poor specifications — it's **learned helplessness about AI**. Maria doesn't just fail to design this agent. She concludes she *can't* design agents. She exits the market entirely. The surface has created a permanent exclusion, not a temporary difficulty.

This is the lens that connects the UX problem to the **market problem.** The nervousness in your hunch isn't just a feeling — it's a psychological need frustration that produces exit, not effort.

### Failure Signal

Maria doesn't just leave the form incomplete. She stops engaging with AI agents entirely. She tells her network: "AI tools aren't built for people like us." The surface has not just lost a user — it has created an anti-evangelist.

---

## Lens 7: Vygotsky's Zone of Proximal Development

**Core idea:** Every learner has a **Zone of Proximal Development** — the space between what they can do independently and what they can do with guidance. Tasks inside the ZPD are achievable *with scaffolding*. Tasks outside are impossible. Tasks already below the ZPD are trivial.

### The Mapping

The 18 questions sit **inside Maria's ZPD** — she CAN answer them, but only with the right scaffolding:

- **With scaffolding:** A conversation that draws out her purpose, a visual that helps her see boundaries, a template that shows what a good specification looks like, a feedback signal that confirms she's on track
- **Without scaffolding:** A blank text field and a question written in engineering language

The current surface provides **zero scaffolding.** It demands independent performance on tasks that require guided participation. It treats every question as if Maria should already know the answer in the format it requires.

Vygotsky's insight is that scaffolding is **not a convenience** — it is the mechanism by which ZPD tasks become achievable. Without it, the learner is placed in the impossible zone and predictably fails. With it, the same learner achieves the same task. The learner hasn't changed. The scaffolding has.

### What Vygotsky Uniquely Reveals

> **The 18 questions are not data fields — they are learning opportunities.** They are designed to produce insight, not just collect data. A surface that treats them as data fields (what Maria already knows, transcribed) misses their primary function: to help Maria *discover what she knows but hasn't yet articulated.* The scaffolded surface doesn't just accept answers — it creates the conditions under which good answers become possible. The current surface creates the conditions under which good answers become *impossible*.

This reframes the entire design challenge: **the surface is not a form — it is a learning environment.**

### Failure Signal

Maria says "I don't know how to answer that" about a question she *could* answer if someone asked it to her conversationally over coffee. The question isn't too hard. The scaffold is missing.

---

## Synthesis: The Diagnostic Constellation

Each lens illuminates a different layer of the same structural misalignment:

| Lens | Where the Problem Lives | What Is Lost |
|:--|:--|:--|
| **Shannon–Weaver** | The channel | Information — destroyed in transit by encoding loss, type collision, and missing feedback |
| **Affordance Theory** | The tool | Fidelity — the tool shapes the action toward the wrong cognitive mode |
| **Cognitive Load** | The mind | Capacity — extraneous load depletes the resources needed for genuine thinking |
| **Distributed Cognition** | The system | Partnership — the surface could extend cognition but instead parasitises it |
| **Communication Accommodation** | The relationship | Respect — one-way accommodation signals dominance and creates distance |
| **Self-Determination** | The person | Motivation — need frustration produces exit, not effort |
| **Vygotsky** | The learning | Discovery — scaffold-less questions make achievable answers impossible |

**The composite diagnosis:** The problem is not that Maria lacks expertise. The problem is that every layer of the communication system — channel, tool, mind, system, relationship, person, and learning environment — is misaligned with her simultaneously. The loss compounds across layers. Information destroyed at encoding (Shannon) can't be recovered by better thinking (Cognitive Load). Thinking shaped by wrong affordances (Affordance) can't be corrected by feedback that doesn't exist (Shannon). A surface that demands one-way accommodation (Accommodation) triggers need frustration (Self-Determination) that narrows cognition (Cognitive Load) in a surface that offers no scaffolding (Vygotsky) and no cognitive partnership (Distributed Cognition).

**The unified insight:** The specification surface is not a neutral medium. It is an active participant in the communication system — and currently, it is a *hostile* participant. A new surface must be an *ally* across all seven dimensions simultaneously.

---

This is what we're designing: not a better form, but a **communication ally** — a surface that carries the right signal types, affords the right cognitive actions, frees cognitive capacity for genuine thinking, extends cognition rather than parasitising it, accommodates the user as much as the user accommodates it, fulfils psychological needs rather than frustrating them, and provides the scaffolding that makes achievable answers possible.

Shall I move next to mapping the 18 questions to their cognitive modes and designing interaction modalities for each — using this seven-lens diagnostic as our quality gate?Memory updated with the full seven-lens diagnostic. The "hostile participant → communication ally" framing is now captured as the unified insight driving this work.

---

## Run 3 — AI UX Innovator ✓ COMPLETED

*2026-04-12T22:49:49* · `glm-5.1:cloud` · `ed77aed9...`

### Prompt

map the 18 questions to their cognitive models and appropriate interaction modalities

### Response

---

# 7 Cognitive Modes → 7 Interaction Modalities → 18 Question Mapping

---

## The Cognitive Mode Taxonomy

The 18 questions resolve into **7 distinct cognitive modes** — each demanding a fundamentally different kind of thinking. A single surface (text field) cannot serve all seven. Each needs its own native interaction modality.

| # | Cognitive Mode | The Cognitive Act | "Maria, what are you actually DOING?" |
|:--|:--|:--|:--|
| 1 | **Narrative** | Making meaning through story | "I'm telling you why this matters" |
| 2 | **Boundary** | Drawing lines of inclusion/exclusion | "I'm deciding what's in and what's out" |
| 3 | **Exploration** | Expanding the possibility space | "I'm discovering what else this could be" |
| 4 | **Verification** | Defining what "done right" looks like | "I'm deciding what counts as proof" |
| 5 | **Architecture** | Designing relational structure | "I'm arranging how the pieces connect" |
| 6 | **Configuration** | Setting behavioural parameters | "I'm tuning how this should behave" |
| 7 | **Evaluation** | Judging trajectory over time | "I'm checking if things are getting better" |

---

## The 7 Interaction Modalities

Each modality is designed to be the **native expression surface** for its cognitive mode — no translation, no encoding, no type collision. The surface doesn't ask Maria to write *about* the answer; it lets her *perform* the answer.

---

### 1 · NARRATIVE → **"The Origin Story"**

**What Maria does:** Talks. Tells a story. Explains in her own words.

**What the surface does:** Listens. Structures. Reflects back.

**How it works:**
- The surface opens as a **conversation** — not a form. It asks: *"So, why do you need this agent? Tell me about a moment when you wished you had one."*
- Maria responds naturally — by voice or typing. She tells her story. She doesn't write a specification; she describes a *need*.
- As she talks, the surface **extracts structured components in real-time** — surfacing them in a sidebar: *"I heard you say... this agent exists to [purpose]. The need is [need]. The gain would be [gain]."*
- Maria reviews the sidebar. She sees her own expertise **reflected back, structured.** She corrects what's wrong, confirms what's right.
- The conversation continues: *"What would it mean for you to be more capable after using this agent? Not just faster — genuinely more skilled?"*

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | Native signal preserved — narrative travels as narrative, not as prose |
| Affordance | Affords storytelling — Maria's most natural cognitive act |
| Cognitive Load | No encoding tax — Maria just talks |
| Distributed Cognition | Surface participates — structures the narrative, doesn't just record it |
| Accommodation | Surface meets Maria's language — then translates to framework |
| Self-Determination | Signals COMPETENCE — Maria sees her expertise is real and structured |
| Vygotsky | Scaffolds — the conversation draws out what Maria knows but hasn't articulated |

---

### 2 · BOUNDARY → **"The Fence"**

**What Maria does:** Sorts. Places things inside or outside. Draws lines.

**What the surface does:** Makes boundaries visible and manipulable.

**How it works:**
- The surface presents a **two-zone space** — a fence line down the middle. Left: ✅ "The Agent CAN." Right: 🚫 "The Agent CANNOT."
- A **stack of cards** sits at the top — each representing a potential action, decision, or capability. Cards are generated from what Maria said in L1: *"Make client commitments", "Draft strategy proposals", "Send emails on your behalf", "Access financial data", "Revise approved campaigns"…*
- Maria **drags each card** to one side. This is boundary-setting as a physical act.
- Some cards are ambiguous. Maria can **split them**: "Draft strategy proposals" becomes ✅ "Draft initial options" on the left, and 🚫 "Finalise strategy without my review" on the right.
- Boundary **strength** is adjustable: a toggle turns a thin dotted line into a thick wall. *"This is a nice-to-have limit"* (soft) vs. *"The agent must NEVER do this"* (hard).
- The surface shows a **live summary**: *"Your agent has 12 capabilities and 5 hard boundaries. 2 areas are still undefined."*

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | Spatial signal preserved — boundary as position, not prose |
| Affordance | Affords sorting and placing — not writing about limits |
| Cognitive Load | Concrete sorting replaces abstract description |
| Distributed Cognition | Surface generates candidate cards from prior context |
| Accommodation | Cards are in Maria's language, not engineering terms |
| Self-Determination | Signals AUTONOMY — Maria controls the fence, not the form |
| Vygotsky | Scaffolds — cards provide concrete handles for boundary thinking |

---

### 3 · EXPLORATION → **"The Possibility Garden"**

**What Maria does:** Browses. Considers. Chooses.

**What the surface does:** Generates. Curates. Records alternatives.

**How it works:**
- Instead of asking Maria to *generate* alternatives (which demands creative effort from nothing), the surface **generates a garden of possibilities** based on her prior answers.
- Each possibility appears as a **vivid card** with a name, an evocative illustration, and one paragraph: *"The Loyal Strategist — An agent that deeply understands your business and surfaces strategic options you haven't considered. It never acts without your approval."* vs. *"The Tireless Executor — An agent that handles every operational detail so you can focus on big-picture thinking. It runs your systems while you dream."*
- Maria **browses the garden** — reading, comparing, feeling which ones resonate. She **picks** one or two. She **discards** the rest.
- **Critical design decision:** The discarded alternatives are NOT deleted. Per the framework: *"The alternatives are recorded, not discarded; they are the evidence that the chosen direction was selected, not defaulted into."* The surface shows them in a *"Paths Not Taken"* section — visible, cited, but not active.
- Maria feels the joy of **discovery** — "Oh, I didn't think of THAT kind of agent!" — without the burden of generation.

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | The possibility signal is generated, not lost to encoding failure |
| Affordance | Affords browsing and choosing — not generating from nothing |
| Cognitive Load | Extraneous load of generation is offloaded to the surface |
| Distributed Cognition | Surface participates — co-generates the possibility space |
| Accommodation | Options are described in Maria's language |
| Self-Determination | Signals COMPETENCE — Maria's judgment is the valuable act |
| Vygotsky | Scaffolds — alternatives provided, not demanded |

---

### 4 · VERIFICATION → **"The Evidence Builder"**

**What Maria does:** Judges. Looks at something concrete and says "yes, that's good enough" or "no, that's not."

**What the surface does:** Generates concrete examples. Converts judgment into verification rules.

**How it works:**
- Instead of asking Maria to *write acceptance criteria* (an abstract, engineering-register task), the surface **shows her concrete examples** and asks for her judgment.
- Based on the agent's purpose (L1) and specification (L3), the surface generates **sample outputs**: *"Here's what your agent might produce for a typical task. Is this good enough?"*
- Maria reviews the sample. She can **annotate it**: highlight what's right, circle what's missing, mark what's wrong.
- The surface **converts her annotations into verification rules**: *"You highlighted the evidence section as essential — so every output must include evidence. You circled the recommendation as insufficient — so recommendations must include at least 2 options with trade-off analysis."*
- Maria can **test the rule**: the surface generates another sample and checks it against the rule. *"This output passes 4 of 5 criteria. The missing one is: trade-off analysis on recommendations."*
- Maria says **yes or no** to each rule. She doesn't write criteria. She judges concrete examples, and the surface does the translation.

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | Judgment signal preserved — not collapsed into prose criteria |
| Affordance | Affords judging concrete examples — the most natural verification act |
| Cognitive Load | Concrete judgment is cognitively lighter than abstract criterion writing |
| Distributed Cognition | Surface converts judgment → rules. Maria judges; surface structures |
| Accommodation | Maria sees samples in her domain language |
| Self-Determination | Signals COMPETENCE — her judgment IS the verification |
| Vygotsky | Scaffolds — samples provide handles for judgment thinking |

---

### 5 · ARCHITECTURE → **"The Workshop Floor"**

**What Maria does:** Arranges. Connects. Positions.

**What the surface does:** Makes structure spatial. Enforces connection logic.

**How it works:**
- The surface opens as a **2D workspace** — a workshop floor. On it are **component cards** generated from prior answers: information sources, tools, other agents, human checkpoints, escalation paths.
- Maria **drags cards into position**, creating a spatial layout that represents the agent's architecture. She places related components near each other. She separates what shouldn't interact.
- She **draws connections** between components — a line from "Client Database" to "Strategy Generator" means data flows between them.
- Connection **types** are selectable: data flow, escalation, verification, permission grant. The surface uses **colour and line style** to distinguish them.
- The surface **enforces architectural logic**: *"You've connected the Strategy Generator to the Email Sender, but there's no human checkpoint between them. Since sending email is irreversible, should a human review step sit here?"*
- The layout IS the specification. No translation to prose required.

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | Spatial structure preserved — layout IS the architecture |
| Affordance | Affords arranging and connecting — not describing structure in prose |
| Cognitive Load | Spatial arrangement uses pattern recognition, not propositional reasoning |
| Distributed Cognition | The layout externalises the architecture — surface holds the structure |
| Accommodation | Components named in Maria's language, not engineering terms |
| Self-Determination | Signals AUTONOMY — Maria designs the structure herself |
| Vygotsky | Scaffolds — components are pre-generated; Maria arranges, doesn't create from nothing |

---

### 6 · CONFIGURATION → **"The Control Panel"**

**What Maria does:** Adjusts. Sets levels. Chooses presets.

**What the surface does:** Translates dials into agent behaviour. Shows consequences.

**How it works:**
- The surface presents **physical-feeling controls**: dials, toggles, sliders, and preset buttons. No text fields.
- Each control governs a behavioural parameter: verification strictness, escalation threshold, autonomy level, cost ceiling, diversity requirement.
- **Presets** offer starting points: *"The Careful Assistant"* (low autonomy, high verification, strict escalation) vs. *"The Trusted Partner"* (moderate autonomy, standard verification, escalation at irreversible thresholds only). Maria starts from a preset and adjusts.
- When Maria moves a dial, the surface shows **consequences in real-time**: *"At this autonomy level, the agent can draft proposals independently but cannot send them without your approval. Cost per invocation: ~$0.03."*
- Every control has a **"What does this mean?"** tooltip in plain language: *"Escalation threshold: How serious does a situation need to be before the agent stops and asks you for a decision?"*
- The surface **tracks completeness**: *"7 of 9 controls set. Unset: recovery protocol, diversity minimum."*

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | Configuration signal preserved — position of dial IS the value |
| Affordance | Affords adjusting — the most natural parameter-setting act |
| Cognitive Load | Presets remove the need to set every value from scratch |
| Distributed Cognition | Surface translates dial position → agent behaviour specification |
| Accommodation | Every control explained in plain language, not engineering |
| Self-Determination | Signals AUTONOMY — Maria is in control, literally |
| Vygotsky | Scaffolds — presets are the "more capable other" that guide initial setup |

---

### 7 · EVALUATION → **"The Growth Tracker"**

**What Maria does:** Sets targets. Reads trajectories. Makes judgments about direction.

**What the surface does:** Visualises trajectories. Projects futures. Enables comparison.

**How it works:**
- The surface presents **visual trajectories** — line graphs, progress arcs, and before/after comparisons.
- Maria doesn't *describe* whether the Scaffolding Dependency Index is narrowing. She **sees it**: a line trending upward (more capable) or downward (more dependent). She can move a **target marker** to set what "better" looks like.
- The surface **projects forward**: *"Based on your current design, here's the trajectory for human capability over 30 interactions. The scaffolding dependency should narrow. Does this look right?"*
- **Before/after comparisons** show the predicted state: *"Before: You spend 2 hours on client follow-ups. After: You spend 30 minutes reviewing the agent's work and approving it. Net gain: 1.5 hours of strategic thinking time."*
- Maria can **compare alternatives** visually: *"If you chose 'The Trusted Partner' preset, here's the trajectory. If you chose 'The Careful Assistant', here's the other one."*
- The key insight: Maria doesn't need to *understand* the Scaffolding Dependency Index. She needs to *see* whether the graph goes the way she wants.

**Lens alignment:**
| Lens | How it's served |
|:--|:--|
| Shannon | Trajectory signal preserved — visual, not propositional |
| Affordance | Affords visual pattern recognition — automatic, not effortful |
| Cognitive Load | Visual evaluation is cognitively lighter than prose analysis |
| Distributed Cognition | Surface projects trajectories — extends Maria's temporal reasoning |
| Accommodation | Metrics shown in domain-relevant terms (hours, tasks, quality) |
| Self-Determination | Signals COMPETENCE — Maria judges, surface calculates |
| Vygotsky | Scaffolds — projections enable judgment that Maria couldn't make unaided |

---

## The Full 18-Question Mapping

| Layer | Question | Primary Mode | Interaction Modality | Secondary Mode |
|:--|:--|:--|:--|:--|
| **L1 Purpose** | Why does this agent exist, and what human need does it serve? | 🗣️ Narrative | **The Origin Story** | — |
| **L1 Purpose** | What does the human gain in capability, understanding, or possibility space? | 🗣️ Narrative | **The Origin Story** | 🔭 Exploration |
| **L2 Identity** | What is this agent's role, orientation, and capability boundary? | 🧱 Boundary | **The Fence** | ⚙️ Configuration |
| **L2 Identity** | What epistemic metadata does this agent contract to attach to its outputs? | ✅ Verification | **The Evidence Builder** | ⚙️ Configuration |
| **L3 Specification** | Are criteria verifiable, pre-existing, and type-resolved? Do they specify which information types must be decomposable? | ✅ Verification | **The Evidence Builder** | — |
| **L3 Specification** | Was the option space explored and a direction chosen before criteria were written? | 🔭 Exploration | **The Possibility Garden** | — |
| **L4 Context** | What is the minimum information this agent needs, and when? What information boundaries are structurally enforced? | 🏗️ Architecture | **The Workshop Floor** | 🧱 Boundary |
| **L4 Context** | What epistemic context does the agent receive from upstream? Is that context typed or raw prose? | 🏗️ Architecture | **The Workshop Floor** | ✅ Verification |
| **L5 Trust** | Who verifies this work, at what independence level, and how is that level selected? | ✅ Verification | **The Evidence Builder** | 🏗️ Architecture |
| **L5 Trust** | Do belief revision protocols allow the pipeline to improve its reasoning? Is the audit trail assurance level matched to task stakes? | 📈 Evaluation | **The Growth Tracker** | — |
| **L6 Safety** | What are the fail-safe defaults, and where are the human gates? What recovery protocol operates when the agent halts? | 🧱 Boundary | **The Fence** | ⚙️ Configuration |
| **L6 Safety** | Is cognitive diversity at the organisational level being actively preserved? | ⚙️ Configuration | **The Control Panel** | 📈 Evaluation |
| **L7 Ecosystem** | Is the architecture matched to task structure? What is the per-invocation cost ceiling? | 🏗️ Architecture | **The Workshop Floor** | ⚙️ Configuration |
| **L7 Ecosystem** | Are pipelines designed as epistemic exchanges? Is coalition formation by epistemic complementarity? Is diversity monitored? | 🏗️ Architecture | **The Workshop Floor** | 📈 Evaluation |
| **L8 Improvement** | Are output quality, rework rates, and specification aging tracked? | 📈 Evaluation | **The Growth Tracker** | — |
| **L8 Improvement** | Is pipeline intelligence — downstream capability gain — being measured alongside output accuracy? | 📈 Evaluation | **The Growth Tracker** | — |
| **L9 Enrichment** | Can the human now perform the task unassisted at higher quality than before? | ✅ Verification | **The Evidence Builder** | 📈 Evaluation |
| **L9 Enrichment** | Is every human more capable after every interaction than before it? Is the Scaffolding Dependency Index narrowing or widening? | 📈 Evaluation | **The Growth Tracker** | — |

---

## The Journey: How the 9 Layers Unfold

The layers are **sequential** — earlier answers constrain later ones. The surface must make this dependency visible. As Maria progresses, the **agent takes visual shape**. She's not filling a form — she's sculpting a partner.

```
L1 🗣️ ORIGIN STORY     ─── "Why?" ─────────────────────────────────┐
                                                                   │ constrains
L2 🧱 THE FENCE         ─── "What's in and out?" ──────────────────┤
     ✅ EVIDENCE BUILDER ─── "What epistemic commitments?" ─────────┤
                                                                   │ constrains
L3 🔭 POSSIBILITY GARDEN── "What else could this be?" ─────────────┤
     ✅ EVIDENCE BUILDER ─── "How do we know it's done right?" ────┤
                                                                   │ constrains
L4 🏗️ WORKSHOP FLOOR     ─── "How do the pieces connect?" ─────────┤
                                                                   │ constrains
L5 ✅ EVIDENCE BUILDER   ─── "Who verifies, how independently?" ───┤
     📈 GROWTH TRACKER   ─── "Does reasoning improve over time?" ──┤
                                                                   │ constrains
L6 🧱 THE FENCE          ─── "Where are the hard walls?" ───────────┤
     ⚙️ CONTROL PANEL    ─── "How should it fail safely?" ─────────┤
                                                                   │ constrains
L7 🏗️ WORKSHOP FLOOR     ─── "What surrounds this agent?" ─────────┤
                                                                   │ constrains
L8 📈 GROWTH TRACKER     ─── "Is it getting better?" ──────────────┤
                                                                   │ constrains
L9 ✅ EVIDENCE BUILDER   ─── "Can you do it alone now?" ────────────┘
     📈 GROWTH TRACKER   ─── "Is the human more capable?"
```

**The key design principle:** At each layer transition, the surface **shows the constraint flow**. When Maria finishes L1, the surface says: *"Based on your purpose, here are the roles and boundaries that would make sense."* L2 is pre-seeded from L1. L3 is pre-seeded from L2. Every layer starts with a **draft generated from prior answers** — which Maria can accept, modify, or override. She never faces a blank space.

---

## Mode Frequency Across the Journey

| Mode | Questions | Layers Where It Appears | Journey Role |
|:--|:--|:--|:--|
| 🗣️ Narrative | 2 | L1 | **The beginning** — meaning-making before anything else |
| 🧱 Boundary | 3 | L2, L6 | **The guardrails** — defining what's sacred and what's excluded |
| 🔭 Exploration | 1 | L3 | **The expansion** — ensuring the best direction was chosen |
| ✅ Verification | 4 | L2, L3, L5, L9 | **The quality engine** — the most-used mode; ensuring truth |
| 🏗️ Architecture | 4 | L4, L7 | **The structure** — how the pieces relate |
| ⚙️ Configuration | 2 | L6 | **The tuning** — setting behavioural parameters |
| 📈 Evaluation | 4 | L5, L8, L9 | **The trajectory** — judging direction over time |

Three modes dominate: **Verification (4), Architecture (4), Evaluation (4).** These are the modes where current surfaces fail most catastrophically — because they're the most abstract, the most engineering-register, and the most cognitively demanding in prose form. By giving each its own native modality, the surface attacks the hardest problems first.

---

## What This Resolves Across All Seven Lenses

| Lens | Before | After |
|:--|:--|:--|
| **Shannon** | 6 signal types collapsed into 1 channel | Each signal type has its own channel — no information loss |
| **Affordance** | Text field affords prose for all tasks | Each modality affords the right cognitive action |
| **Cognitive Load** | Extraneous load depletes germane load | Surface offloads encoding, generation, and structure |
| **Distributed Cognition** | Surface records; demands finished thought | Surface participates — co-generates, co-structures, co-projects |
| **Accommodation** | 100% one-way — Maria adapts to surface | Surface generates in Maria's language; translates to framework |
| **Self-Determination** | All three needs frustrated | Competence (her judgment drives everything), Autonomy (she controls every modality), Relatedness (the surface meets her where she is) |
| **Vygotsky** | No scaffolding — demands independent performance | Every modality scaffolds — pre-seeds, generates candidates, provides examples, projects trajectories |

---

**The composite design statement:** Maria walks through 9 layers, each one opening a different interaction modality that matches the cognitive mode of its questions. She never faces a blank text field. The surface transforms at each layer — from conversation, to fence-building, to garden-browsing, to evidence-judging, to spatial arrangement, to dial-adjusting, to trajectory-reading. At each transition, prior answers flow forward as constraints and pre-seeds. By the end, she has sculpted a complete agent specification — without ever having written one word of engineering prose.

Shall I move next to designing the **visual coherence model** — how these 7 modalities form a single unified surface experience rather than 7 disconnected screens? That's where the "surprise and delight" becomes a product, not just a set of ideas.Memory updated. The full 7-mode → 7-modality → 18-question mapping is now captured, along with the journey structure and the "communication ally" lens alignment for each modality.

---
