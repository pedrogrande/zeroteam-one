# AI UX Innovator

| Field | Value |
|-------|-------|
| **Session** | `01503788...` |
| **Type** | agent |
| **Agent** | AI UX Innovator |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-12T02:24:46 |
| **Runs** | 10 completed / 10 total |

## Run 1 — AI UX Innovator ✓ COMPLETED

*2026-04-12T02:24:46* · `glm-5.1:cloud` · `99dd2d8c...`

### Prompt

I want to build an AI+Human collaboration workspace application that I haven't been able to find in existing tools. I want to be able to choose to collaborate with a general purpose agent, specialist agents, teams of agents and workflows of agents. 

Too often, the output from the LLM is a wall of text with limited options for extracting the valuable components of the response.

Let's focus on a desktop web application since that is the primary work-appropriate device for what I'm planning.

I want to throw out all existing models for AI tool interaction and ideate through from first principles to find novel solutions that empower the human user and simplifies their workflows.

Start by expanding on this list of common and uncommon use cases that we can then analyse further.

1. Written content production: report, article, documentation, blog post, communication (email etc)
2. Strategy development for an organisation or personal goals
3. Problem solving with design thinking methodologies
4. Data analysis for insights
5. Research and learning
6. Planning and scheduling
7. Creating charts and diagrams
8. Life management with goals, events, contact management, idea capture

### Response

Now let me lay out the expanded use case landscape. I've analysed each through the lens of your core frustration — the **wall of text problem** — because that's what we're ultimately designing against.

---

# Use Case Expansion: AI+Human Collaboration Workspace

## The Analysing Lens

Before expanding, I want to name the principle that guided this expansion, because it'll matter when we design the interaction paradigm:

> **The Shannon Problem**: LLMs transmit enormous bandwidth through a channel (text) that has no semantic encoding. The human receiver must decode signal from noise, decompose structure from prose, and extract actionability from narrative. Every use case below manifests this differently, and each manifestation tells us something about what the interaction model must support.

For each use case I've identified:
- **Sub-tasks** — the atomic operations within the category
- **The Wall of Text Problem** — how the Shannon Problem manifests specifically here
- **Extracting Value** — what it would look like to decompose the output into manipulable, valuable components
- **Uncommon Use Cases** — the edges where existing tools fail hardest and where novel interaction paradigms have the most room to innovate

---

## 1. Written Content Production

**Sub-tasks**: Drafting, editing, restructuring, tone adaptation, format translation (blog→thread→deck→script), sourcing evidence, fact-checking, generating variants, argument structuring, abstract/summary generation, critique and counter-argument generation

**The Wall of Text Problem**: AI generates full drafts that bury 3 brilliant insights in 2000 words of filler. You can't isolate the insights, can't keep section 2 while discarding section 4, and can't see the argument's skeleton separately from its prose.

**Extracting Value**:
- Argument skeleton as a separate, manipulable object from the prose
- Claims tagged separately from their supporting evidence
- Quotable phrases extracted as independent artefacts
- Tone as a layer that can be adjusted independently of substance
- The 3 insights surfaced as standalone, reusable components

**Uncommon Use Cases**:
- **Collaborative argument development** — not "write me an article" but "help me build an argument" where claims, evidence, counter-arguments, and reasoning chains are first-class objects you can rearrange
- **Style transfer on existing content** — change the voice without changing the substance
- **Meeting notes → structured artefacts** — raw notes decomposed into decisions, action items, open questions, and commitments as separate objects
- **Cross-medium translation** — same core content as blog post, Twitter thread, slide deck, and video script, with structure preserved across formats

---

## 2. Strategy Development

**Sub-tasks**: Vision articulation, goal decomposition, competitive analysis, scenario planning, strategic option generation, risk assessment, assumption mapping, stakeholder analysis, strategic narrative construction, strategy versioning

**The Wall of Text Problem**: Strategy documents are dense and interdependent. The valuable components — assumptions, risks, dependencies, options — are buried in prose. You can't "play" with a strategic option to see what happens. You can't isolate the assumption that, if wrong, collapses the whole strategy.

**Extracting Value**:
- Assumptions isolated and independently testable
- Strategic options as manipulable objects (select one and see cascading effects)
- Dependencies mapped separately from the narrative
- Knowns vs unknowns vs known-unknowns as distinct artefact types
- Confidence levels attached to each component

**Uncommon Use Cases**:
- **Strategy simulation** — "What happens to this strategy if assumption X changes?" — live, interactive
- **Strategic assumption stress-testing** — identify which assumptions the strategy is most fragile to
- **Alignment detection** — map where stakeholders agree, disagree, and have different mental models
- **Strategy versioning** — track how strategic thinking evolved over time, with explicit records of what changed and why

---

## 3. Problem Solving with Design Thinking

**Sub-tasks**: Problem framing, empathy mapping, ideation, prototyping, assumption reversal, constraint reframing, root cause analysis, solution evaluation, iteration design

**The Wall of Text Problem**: Design thinking outputs are inherently multi-modal — maps, sketches, matrices, journeys — but AI forces them into prose. The relational structure between insights, the tension between competing ideas, and the progression from problem to solution are all lost in the linearisation.

**Extracting Value**:
- Each insight as a manipulable card that can be moved, connected, grouped
- Connection mapping between insights visible separately from the insights themselves
- The problem frame separated from the solution ideas
- Tension points as standalone objects that can be examined
- "How Might We" questions as seeds that can each sprout their own exploration

**Uncommon Use Cases**:
- **Problem reframing service** — same problem, 5 different frames, each generating different solution spaces
- **Constraint-based ideation** — "Given these constraints, what's possible?" — constraints as interactive parameters
- **Anti-solution generation** — "What would make this problem worse?" — then invert to find solutions
- **Rapid assumption reversal** — "What if the opposite of this assumption were true?"

---

## 4. Data Analysis for Insights

**Sub-tasks**: Pattern recognition, anomaly detection, trend identification, correlation discovery, hypothesis generation, visualisation, narrative creation from data, statistical testing, outlier analysis

**The Wall of Text Problem**: AI narrates data but you can't drill into which data point supports which claim. The insight and the evidence are inseparable. You can't interact with the data directly or ask "show me what changes if we remove this outlier."

**Extracting Value**:
- Every claim linked to its supporting data evidence
- Anomalies as independent, clickable objects
- Methodology separated from findings
- Trends interactive, not just described
- Confidence intervals attached to each insight
- Counter-narratives surfaced alongside the primary narrative

**Uncommon Use Cases**:
- **Hypothesis-driven analysis** — start with explicit hypotheses, test them against data, show which survived
- **Counter-analysis** — "What would someone who disagrees with this finding argue?" — structural devil's advocate
- **Temporal comparison** — "How has this pattern changed over time?" — with the change isolated as its own artefact
- **Narrative vs. data separation** — the story the data tells vs. the data itself, so you can challenge either independently

---

## 5. Research and Learning

**Sub-tasks**: Literature review, concept exploration, knowledge gap identification, connection mapping, curriculum design, mental model building, evidence synthesis, source evaluation, claim verification

**The Wall of Text Problem**: Research summaries blend established knowledge with novel insights with contradictions. You can't distinguish "I knew this" from "this is new" from "this contradicts what I thought." The novelty signal is lost.

**Extracting Value**:
- Knowledge gap map — what don't I know yet?
- Consensus vs. controversy as distinct categories
- Mental models extracted as reusable, standalone frameworks
- Novelty tagging — new to me vs. new to field vs. new to world
- Source quality separated from claim quality
- Connections between concepts made explicit and navigable

**Uncommon Use Cases**:
- **Personal knowledge gap analysis** — given what you know, what should you learn next?
- **Concept lineage mapping** — how did this idea evolve? Who built on whom?
- **Contradiction detection** — "What do sources disagree about regarding this topic?" — the disagreements surfaced as primary output
- **Expertise progression tracking** — "What did I understand before this session vs. after?" — learning made visible
- **Mental model extraction** — not "explain this concept" but "build me a mental model I can reuse"

---

## 6. Planning and Scheduling

**Sub-tasks**: Task decomposition, dependency mapping, timeline creation, resource allocation, risk planning, priority sequencing, milestone definition, estimation, critical path analysis

**The Wall of Text Problem**: Plans in prose hide the structure. Dependencies are invisible. The critical path is buried. Adjusting one task requires re-reading everything. You can't see what happens when one assumption changes.

**Extracting Value**:
- Tasks, dependencies, resources, and milestones as distinct object types
- Critical path as its own extractable artefact
- Assumptions the plan rests on, isolated and testable
- Each task as a manipulable object that can be dragged, reordered, reassigned
- Risk factors as adjustable parameters that cascade through the plan

**Uncommon Use Cases**:
- **Plan stress-testing** — "What happens to the timeline if this assumption is wrong?"
- **Multi-scenario planning** — optimistic, realistic, pessimistic as parallel, comparable artefacts
- **Plan comparison** — "How does Plan A differ from Plan B?" — differences surfaced as a primary output
- **Dependency-first planning** — start from what depends on what, then fill in details

---

## 7. Creating Charts and Diagrams

**Sub-tasks**: Concept mapping, process flow design, system architecture, relationship visualisation, comparison matrices, timeline diagrams, decision trees, stakeholder maps, causal loop diagrams

**The Wall of Text Problem**: AI describes diagrams in prose. The spatial and relational information — which is the *entire point* of a diagram — is trapped in linear text. You can't interact with nodes and edges.

**Extracting Value**:
- Structured data for any visualisation: nodes, edges, and properties as first-class, manipulable objects
- The data separated from the visual presentation layer
- Every element in a diagram interactive, editable, and reconnectable
- Layout as an independent concern — same data, multiple visual forms
- Annotations and evidence attached to specific nodes/edges

**Uncommon Use Cases**:
- **Live diagram evolution** — start with a concept, the diagram grows as understanding deepens
- **Diagram-to-knowledge extraction** — "What does this diagram reveal that prose couldn't?"
- **Multi-layer diagrams** — same structure, different overlays (risk, cost, ownership, priority)
- **Diagram comparison** — "What changed between version 1 and version 2?" — structural diffs, not textual diffs

---

## 8. Life Management

**Sub-tasks**: Goal tracking, habit formation, decision logging, relationship management, idea capture, energy management, priority management, value alignment, commitment tracking, reflection practice

**The Wall of Text Problem**: Life advice is generic. AI can't distinguish what's already working for you from what's a new suggestion. The same output could apply to anyone. Your specific patterns, history, and context are invisible in the response.

**Extracting Value**:
- Universal principles separated from personal applications
- Action items extracted independently from insights
- Start/stop/continue classification as distinct categories
- Energy patterns separated from time commitments
- Recurring personal patterns surfaced as standalone observations

**Uncommon Use Cases**:
- **Decision quality review** — "How did past decisions turn out? What can I learn from my decision patterns?"
- **Energy-pattern-aware scheduling** — match commitments to energy levels, not just calendar availability
- **Value-alignment audit** — "Are my actions matching my stated values?" — with the gaps surfaced as primary output
- **Personal pattern recognition** — "What patterns keep showing up in my life?" — across decisions, relationships, energy, commitments
- **Idea graveyard management** — ideas you've considered and decided against, with reasoning preserved, so you don't keep revisiting them

---

## New Categories: Beyond the Original Eight

These are use cases that don't fit neatly into any of the above, and where the wall of text problem creates particularly acute pain.

---

## 9. Decision-Making and Judgment Support

**Why it's distinct from strategy**: Strategy is about direction and positioning. Decision-making is about specific choices under uncertainty with real consequences — "Do we hire this person?", "Do we take this deal?", "Do we pivot now?"

**Sub-tasks**: Option enumeration, criteria definition, weighted evaluation, risk assessment, reversibility classification, decision logging, bias detection, regret minimisation, second-order effect analysis

**The Wall of Text Problem**: AI gives you a recommendation buried in prose. You can't see the options, criteria, and evidence separately. You can't adjust one criterion's weight and see how the recommendation changes.

**Extracting Value**:
- Options as cards that can be compared side by side
- Criteria as adjustable weights with live recalculation
- Evidence as linked objects attached to specific claims
- Confidence and reversibility as visual, not textual, indicators
- Decision trail — every decision with its inputs, reasoning, and outcome tracked

**Uncommon Use Cases**:
- **Reversibility-first decision framing** — "Can this be undone? If so, decide fast. If not, decide slow."
- **Bias detection** — "What cognitive biases might be affecting this decision?"
- **Second-order effect mapping** — "What happens as a consequence of this consequence?"
- **Regret minimisation** — "Which option would I regret NOT taking?"

---

## 10. Creative Exploration and Ideation

**Why it's distinct from problem-solving**: Problem-solving converges on a solution. Creative exploration diverges — generating possibilities, making unexpected connections, playing with "what if" without needing an answer.

**Sub-tasks**: Brainstorming, lateral thinking, combinatory play, analogy generation, constraint-based creativity, "what if" scenarios, random stimulus association, SCAMPER operations, cross-domain inspiration

**The Wall of Text Problem**: AI generates lists that are linear, sequential, and forgettable. You can't riff on individual ideas. You can't combine two ideas to see what emerges. You can't mark one idea as "interesting" and have the system generate more in that direction.

**Extracting Value**:
- Each idea as a seed that can grow, branch, and combine with others
- Idea genealogy — "Where did this idea come from? What inspired it?"
- Mutation operations — "What if we changed this one thing about this idea?"
- Combination operations — "What if we merged these two ideas?"
- Idea quality signals separated from idea novelty signals

**Uncommon Use Cases**:
- **Idea breeding** — take two ideas, generate their offspring
- **Constraint-based creativity** — add constraints, see what emerges
- **Cross-domain pollination** — "What would a biologist/a musician/a chef see in this problem?"
- **Idea maturation tracking** — ideas start as seeds, grow over sessions, connect to other ideas, get pruned or cultivated

---

## 11. Communication and Relationship Management

**Why it's distinct from content production**: Content production is about the message. Communication management is about the *relationship* — understanding dynamics, calibrating tone for specific audiences, navigating conflict.

**Sub-tasks**: Tone calibration, audience adaptation, conflict resolution preparation, stakeholder mapping, communication timing, follow-up tracking, difficult conversation preparation, trust building, expectation management

**The Wall of Text Problem**: AI writes an email, but you can't separate what you say from how you say it. You can't see how different audiences might receive the same message. The relational context — history, dynamics, power — is invisible in the output.

**Extracting Value**:
- Content separated from tone — adjust one independently of the other
- Relationship dynamics extracted from interaction history
- Audience reception previews — "How might Person A vs Person B receive this?"
- Escalation signals as separate from the message content
- Follow-up actions extracted and trackable

**Uncommon Use Cases**:
- **Difficult conversation simulation** — practice the conversation before having it, with the agent playing the other person
- **Stakeholder empathy mapping** — "What does this person care about? What are they worried about? What would make them say yes?"
- **Communication pattern analysis** — "How has my communication style changed over the past month? Am I more defensive? More collaborative?"
- **Timing optimisation** — "When is the best time to send this message given the relationship context?"

---

## 12. System Design and Architecture

**Why it's distinct from strategy or planning**: This is about designing *systems* — software, organisational, conceptual — where components have defined interfaces, constraints, and trade-offs.

**Sub-tasks**: Requirements gathering, component design, interface definition, constraint mapping, trade-off analysis, iteration design, dependency analysis, failure mode analysis, integration design

**The Wall of Text Problem**: AI describes architecture in prose. You can't see components, relationships, and boundaries separately. You can't isolate a trade-off and examine its implications independently.

**Extracting Value**:
- Components as objects with defined interfaces and responsibilities
- Trade-offs as explicit decision records (we chose X over Y because Z)
- Constraints as testable, adjustable properties
- Boundaries as visible demarcations
- Failure modes as separate artefacts linked to the components they affect

**Uncommon Use Cases**:
- **Constraint-first design** — define what's not possible, then find the space of what is
- **Failure mode pre-mortem** — "How would this system fail?" before building it
- **Trade-off explorer** — "What happens to the system if we change this constraint?"
- **Architecture evolution** — "How does this architecture need to change as requirements change?"

---

## 13. Knowledge Management and Sensemaking

**Why it's distinct from research**: Research is about discovering new information. Sensemaking is about making sense of information you already have — finding patterns, contradictions, and gaps across what you know.

**Sub-tasks**: Synthesis, contradiction detection, thematic clustering, gap identification, provenance tracking, mental model construction, narrative weaving, uncertainty mapping

**The Wall of Text Problem**: AI summarises everything into a flat narrative. You lose the structure, the disagreements, and the nuances. "Some experts believe X, others Y" becomes "X and Y are perspectives."

**Extracting Value**:
- Established facts separated from emerging theories from open questions
- Who believes what and why — mapped and navigable
- Contradictions surfaced as primary output, not smoothed over
- Gaps in understanding made explicit and prioritised
- Provenance attached to every claim

**Uncommon Use Cases**:
- **Contradiction mapping** — "Where do my sources disagree, and what would resolve the disagreement?"
- **Knowledge frontier detection** — "What's the edge of what I know? What's just beyond it?"
- **Belief evolution tracking** — "How has my understanding of this topic changed over time?"
- **Unknown unknowns surfacing** — "What am I not even aware I should be asking about?"

---

## 14. Financial and Business Modelling

**Sub-tasks**: Revenue modelling, cost estimation, scenario testing, sensitivity analysis, unit economics, funding strategy, financial projection, break-even analysis, valuation

**The Wall of Text Problem**: AI gives you a business plan but you can't interact with the assumptions separately from the conclusions. Change one assumption and you need to regenerate everything.

**Extracting Value**:
- Every assumption as an adjustable parameter with live recalculation
- Sensitivity analysis visible at a glance — which assumptions matter most?
- The model separated from the narrative — change the numbers, the story updates
- Scenario comparison as a primary interface, not an afterthought

**Uncommon Use Cases**:
- **Assumption stress-testing** — "Which assumptions, if wrong, would change the conclusion?"
- **Scenario playground** — drag sliders, see cascading effects in real time
- **Break-even explorer** — "How many customers do we need at what price point?"
- **Model version comparison** — "How has our financial model evolved? What changed and why?"

---

## 15. Personal Development and Coaching

**Why it's distinct from life management**: Life management is about running your life. Personal development is about growing — building self-awareness, developing skills, expanding capability.

**Sub-tasks**: Pattern recognition in behaviour, blind spot identification, strength mapping, feedback integration, development plan creation, progress tracking, cognitive bias awareness, emotional intelligence development

**The Wall of Text Problem**: AI gives generic coaching advice. It can't connect to your specific patterns, history, and growth trajectory. The same advice applies to anyone.

**Extracting Value**:
- Universal advice separated from personally relevant insights
- Recurring personal patterns surfaced and tracked over time
- Strengths vs. development areas as a living, evolving map
- Progress visible — "What have I actually improved at?"
- Specific, contextual feedback distinct from general principles

**Uncommon Use Cases**:
- **Pattern mirroring** — "You tend to do X when Y happens. Here are three recent examples."
- **Blind spot surfacing** — "You've never mentioned Z, but it appears in 40% of your situations."
- **Growth tracking** — "How has your thinking about this topic changed over the past 6 months?"
- **Strength amplification** — not just fixing weaknesses, but deliberately leveraging identified strengths

---

## 16. Monitoring and Sensemaking of Ongoing Situations

**Why it's distinct**: This is about *ongoing* tracking, not one-time analysis. Markets evolve, projects change, stories develop. The value is in what's *new* and what's *changed*, not what's the same.

**Sub-tasks**: Signal detection, pattern change notification, trend tracking, alert generation, synthesis across sources, anomaly flagging, significance assessment

**The Wall of Text Problem**: AI gives you a daily digest. You can't see what changed, what's new, what's escalating. The signal — what's different — is buried in the noise of what's the same.

**Extracting Value**:
- Change detection as a first-class output type — "What's different since last time?"
- The new separated from the ongoing
- Signals escalated by importance and urgency independently
- Trend direction visible at a glance, not buried in prose
- Anomalies surfaced as primary artefacts

**Uncommon Use Cases**:
- **Pattern shift detection** — "This market has been trending up for 3 months. This week, the pattern changed. Here's what's different."
- **Signal vs. noise separation** — "Out of 50 things that happened, these 3 matter. Here's why."
- **Narrative drift tracking** — "How has the story about this topic changed over the past month?"
- **Early warning systems** — "This indicator is approaching a threshold. No action needed yet, but worth watching."

---

## Cross-Cutting Patterns

Looking across all 16 categories, several patterns emerge that directly inform what the interaction paradigm must support:

1. **Decomposition is universal** — Every use case benefits from breaking outputs into their constituent parts (claims, evidence, assumptions, actions, questions) and making those parts independently manipulable.

2. **Structure is more valuable than prose** — The same information, structured rather than narrativised, is more useful. The narrative is one view of the data, not the data itself.

3. **The same content needs multiple views** — A strategy needs to be viewable as a narrative, as a set of assumptions, as a dependency map, as a risk matrix. The content is the same; the view changes.

4. **Interactivity is not a feature — it's the paradigm** — Every use case benefits from being able to adjust, compare, combine, and explore rather than just receive.

5. **Context and personalisation matter** — Generic advice is the least valuable output. The same framework applied to your specific context, history, and patterns is where the value lives.

6. **Time adds a dimension that current tools ignore** — Strategies evolve, decisions have outcomes, patterns emerge over time. Current tools treat every interaction as stateless.

These patterns are the raw material for designing a fundamentally different interaction model. Ready to dig into any of these further, or shall we move to analysing what these use cases tell us about the interaction paradigm?

---

## Run 2 — AI UX Innovator ✓ COMPLETED

*2026-04-12T02:55:22* · `glm-5.1:cloud` · `07a57302...`

### Prompt

Analyse the use cases for patterns and unexpected insights

### Response

---

# Pattern Analysis: What 16 Use Cases Reveal When You Treat Them as Data

---

## Pattern 1: The Meta-Use-Case

Strip away the domain labels and every use case is the same thing:

> **"Here is a complex, uncertain reality. Help me understand it well enough to act."**

Writing a report is making sense of what you know and presenting it clearly. Strategy is making sense of a complex landscape. Design thinking is making sense of a problem space. Data analysis is making sense of numbers. Research is making sense of a field. Decisions are making sense of trade-offs under uncertainty. Even "life management" is making sense of your own patterns.

This is important because it means we're not designing 16 different products. We're designing **one product that serves one meta-use-case** across 16 domains. The interaction paradigm needs to be domain-adaptable, not domain-specific. The same structural operations (decompose, relate, manipulate, track) apply whether you're analysing a market or managing your commitments.

**The product is a sensemaking environment.** Everything else is configuration.

---

## Pattern 2: The Type System — 17 Types That Recur Everywhere

When you look at what the agent is actually *producing* across all 16 use cases, the same categories of information appear over and over. They're just buried in prose so you can't see them.

| # | Type | What it is | Present in use cases |
|---|------|-----------|---------------------|
| 1 | **Claim** | An assertion that may or may not be true | 1, 4, 5, 13, 16 |
| 2 | **Evidence** | The basis for believing a claim | 1, 4, 5, 9, 13 |
| 3 | **Assumption** | Something taken as true without proof | 2, 6, 9, 12, 14 |
| 4 | **Option** | A possible path forward | 2, 3, 9, 10 |
| 5 | **Criterion** | A standard for evaluation | 4, 9, 12, 14 |
| 6 | **Action** | Something to do | 6, 8, 11 |
| 7 | **Question** | Something not yet answered | 3, 5, 8, 13 |
| 8 | **Connection** | A link between other types | 3, 5, 7, 12 |
| 9 | **Constraint** | A boundary on what's possible | 3, 6, 12, 14 |
| 10 | **Confidence** | How sure are we? | 4, 5, 9, 16 |
| 11 | **Perspective** | A different way of seeing the same thing | 2, 3, 10, 11, 13 |
| 12 | **Pattern** | A recurring structure | 4, 8, 15, 16 |
| 13 | **Gap** | What's missing | 5, 13 |
| 14 | **Tension** | Where things conflict | 3, 11, 13 |
| 15 | **Dependency** | What depends on what | 2, 6, 12 |
| 16 | **Outcome** | What happened as a result | 8, 9, 15 |
| 17 | **Provenance** | Where did this come from? | 5, 10, 13 |

**This is the root cause of the wall of text problem.**

It's not that the output is badly formatted. It's that 17 distinct types of information are being encoded as a single type — prose. The human is forced to do type inference in real time while reading: "Is this a claim or an assumption? Is this evidence or opinion? Is this an action or a suggestion?"

This is cognitively expensive and error-prone. It's like a database that stores everything as a single string field. The solution isn't "better prose" — it's **typed outputs** where each piece of information is explicitly what it is.

This type system is the foundation of the entire interaction paradigm. It's the periodic table of knowledge work.

---

## Pattern 3: The Operation Set — 14 Things Humans Need to Do With Types

Across all 16 use cases, humans need to perform the same operations on the type system:

| # | Operation | What it means | Example |
|---|-----------|--------------|---------|
| 1 | **Extract** | Pull one type out of a mixed output | "Give me just the assumptions" |
| 2 | **Isolate** | Separate one type from another | "Show claims separately from evidence" |
| 3 | **Compare** | Put two+ things side by side | Compare strategic options, scenarios, versions |
| 4 | **Adjust** | Change a parameter, see cascading effects | Change an assumption, see the impact |
| 5 | **Combine** | Merge two+ things into something new | Idea breeding, strategy synthesis |
| 6 | **Rearrange** | Change structure/order without changing content | Reorder priorities, restructure an argument |
| 7 | **Drill** | Go deeper into a specific component | "Show me the evidence for THIS claim" |
| 8 | **Navigate** | Move between related components | From claim → evidence → source → related claims |
| 9 | **Track** | Follow how something changes over time | Strategy evolution, decision outcomes |
| 10 | **Evaluate** | Apply criteria to assess quality/fitness | Score options against criteria |
| 11 | **Transform** | Convert between representations | Same data as narrative ↔ table ↔ diagram |
| 12 | **Annotate** | Add human judgment to agent output | Mark as "important", "disagree", "investigate" |
| 13 | **Branch** | Fork a path to explore separately | Two versions of a strategy, parallel ideas |
| 14 | **Stress-test** | "What happens if this assumption is wrong?" | Break the model, find the weak points |

Current chat interfaces support exactly ONE of these operations natively: "generate more text." You can sometimes hack extraction by asking again, or comparison by asking for a table, but none of these are first-class interactions. They're all workarounds.

**The interaction paradigm must make ALL 14 operations first-class.** Each one should be as natural as "send a message" is in chat.

---

## Pattern 4: The Extraction Hierarchy — A Product Roadmap Disguised as an Insight

Looking at what the use cases collectively demand, there's a clear hierarchy of capability that no current tool supports:

```
┌─────────────────────────────────────────────────────────┐
│  L5  CONTEXTUAL     Personalised to your history,       │
│      COMPONENTS     patterns, preferences               │
├─────────────────────────────────────────────────────────┤
│  L4  EVOLVING       Track changes over time, version,   │
│      COMPONENTS     compare versions                    │
├─────────────────────────────────────────────────────────┤
│  L3  MANIPULABLE    Can adjust, compare, combine,       │
│      COMPONENTS     stress-test, branch                │
├─────────────────────────────────────────────────────────┤
│  L2  RELATED        Links between types — claim→evidence│
│      COMPONENTS     assumption→impact, option→criteria  │
├─────────────────────────────────────────────────────────┤
│  L1  TYPED          Claims, evidence, assumptions as    │
│      COMPONENTS     separate, labelled objects          │
├─────────────────────────────────────────────────────────┤
│  L0  RAW OUTPUT     Wall of text — what we have now     │
└─────────────────────────────────────────────────────────┘
```

**Current tools operate at Level 0.** The use cases demand Level 5.

But this isn't just an observation — it's a **product roadmap**. Each level is a milestone that unlocks new use cases:

- **L1 unlocks**: extraction ("just the assumptions"), isolation (claims from evidence)
- **L2 unlocks**: navigation (follow the links), drill-down (from claim to evidence)
- **L3 unlocks**: interactivity (adjust, compare, combine, stress-test)
- **L4 unlocks**: time ("what changed?"), versioning, evolution tracking
- **L5 unlocks**: personalisation (your patterns, your context, your history)

And crucially: **each level includes all levels below it.** L3 is worthless without L1 and L2. L5 is impossible without L4. This is an architecture, not a feature list.

---

## Pattern 5: The Temporal Spectrum

Use cases don't just differ in *what* they do — they differ in *how long they live*.

```
EPISODIC                    ITERATIVE                    ONGOING
"One shot, done"           "Build across sessions"       "Never done"
─────────────────────────────────────────────────────────────────
Quick content gen          Strategy development          Life management
One-off data analysis      Design thinking               Relationship mgmt
Single diagram             Research & learning            Personal development
                           Planning                      Monitoring
                           Decisions                     Sensemaking
                           Ideation
                           Architecture
                           Business modelling
```

**Current AI tools are designed for the left column.** The vast majority of real human value lives in the centre and right columns.

The implication: the workspace must treat artefacts as **first-class persistent objects**, not ephemeral chat outputs. A strategy you worked on yesterday should be there tomorrow, with what changed since last time surfaced as a primary output. A decision you made last month should carry its reasoning trail when you revisit it.

This is where **"What changed?"** becomes the most important question that current tools don't answer. Across every iterative and ongoing use case, the critical question is always: what's different since last time? In strategies. In plans. In decisions. In knowledge. In relationships. In markets. Current tools treat every interaction as stateless. A stateful tool that surfaces changes, drifts, and developments as primary output would be transformational.

---

## Pattern 6: The Agency Model — Confidence × Reversibility

Across all use cases, what the human needs from the agent is governed by two orthogonal axes:

```
                    REVERSIBLE          IRREVERSIBLE
              ┌──────────────────┬──────────────────┐
  HIGH       │                  │                  │
  CONFIDENCE  │  AGENT ACTS      │  HUMAN CONFIRMS  │
              │  AUTONOMOUSLY    │  BEFORE ACTION   │
              │                  │                  │
              ├──────────────────┼──────────────────┤
              │                  │                  │
  LOW        │  AGENT ACTS,     │  HUMAN DECIDES   │
  CONFIDENCE  │  HUMAN REVIEWS   │  AGENT PREPARES  │
              │  LATER           │  THE GROUND      │
              │                  │                  │
              └──────────────────┴──────────────────┘
```

This 2×2 matrix governs the entire human-agent interaction model:

- **High confidence + reversible** → Agent acts autonomously (reformatting, monitoring, consistency checks)
- **High confidence + irreversible** → Agent recommends, human confirms (sending emails, making payments, publishing)
- **Low confidence + reversible** → Agent tries, human reviews (draft content, exploration, ideation)
- **Low confidence + irreversible** → Agent prepares the ground, human decides (strategic decisions, hiring, pivoting)

**This matrix is completely absent from current AI tools.** They treat every interaction as if it's in the top-left quadrant: the agent generates, the human accepts. But real knowledge work spends most of its time in the bottom-right — where the human must decide under uncertainty and the agent's job is to *prepare the judgment*, not to *make the judgment*.

This reframes the entire interaction model:

> **The agent is a JUDGMENT PREPARATION system, not an ANSWER GENERATION system.**

The agent's highest-value role is to reduce everything between the human's decision points to its minimum, structured form — so the human can see clearly what they're deciding, what they're assuming, and what they're risking. The agent doesn't give you the answer. The agent gives you the clearest possible frame for YOUR answer.

---

## Pattern 7: The Shannon Channel Problem

From Shannon's communications theory, the efficiency of a channel depends on how well the encoding matches the decoder's needs.

The LLM channel has enormous bandwidth. But it encodes everything as a single symbol set (prose) with no structural differentiation. The decoder (the human) must do all the demultiplexing — separating claims from evidence, assumptions from conclusions, actions from suggestions, questions from statements.

This is why the wall of text problem gets worse as outputs get longer: the human's demultiplexing load increases linearly with output length, while the value extracted increases sub-linearly (because valuable components are diluted in filler).

What the use cases collectively demand is a **multi-channel communication system**:

| Channel | Carries | Current treatment |
|---------|---------|-------------------|
| **Claims** | What's being asserted | Buried in prose |
| **Evidence** | What supports the claim | Buried in prose |
| **Uncertainty** | How confident, how reversible | Absent or buried |
| **Action** | What to do | Buried in prose |
| **Context** | Why this matters | Absent |
| **Relationship** | How this connects | Lost in linearisation |
| **Time** | When true, how changed | Absent |

Seven channels of information, one pipe (prose), zero demultiplexing support. The human does it all in their head.

**The workspace must be a demultiplexer.** Not a chat window. Not a document editor. A structured channel where each type of information arrives on its own frequency, labelled, linked, and ready for the operation the human needs to perform on it.

---

## Pattern 8: Six Design Tensions

The use cases don't all pull in the same direction. Several important tensions must be designed for, not resolved:

### T1: Convergence ↔ Divergence
Some use cases narrow (decisions, planning) while others widen (creative exploration, research). The same tool must support both modes. **Design implication**: the workspace needs a mode switch — not a separate tool, but a toggle on the same environment that shifts the agent's orientation from convergent to divergent and back.

### T2: Structure ↔ Freedom
Structured outputs (typed components, cards, diagrams) are more useful but constrain expression. Free-form prose is more expressive but creates the wall of text problem. **Design implication**: structure by default, freedom on demand. Every output is typed and decomposed unless the human explicitly asks for free-form, in which case the agent can generate prose — but the human can always restructure it later.

### T3: Speed ↔ Depth
Quick answers vs. deep exploration. **Design implication**: two gears. A fast gear for "just give me the assumptions" (instant extraction) and a deep gear for "let's build a strategy" (collaborative, multi-step). The human should be able to shift between gears mid-interaction without starting over.

### T4: Personalisation ↔ Universality
The most valuable outputs are personal (your patterns, your history). The most scalable approach is generic. **Design implication**: personal by design. The workspace accumulates context about the human over time — their patterns, preferences, past decisions, recurring themes. Every new interaction starts from this accumulated context, not from scratch. Generic advice is the floor; personal insight is the ceiling.

### T5: Autonomy ↔ Control
The human wants delegation for some things, granular control for others. **Design implication**: the confidence × reversibility matrix (Pattern 6) determines the default. But the human can override: "Just do it" or "Show me everything before you act." The interaction cost of switching between modes must be near-zero.

### T6: Individual ↔ Collaborative
Some work is deeply personal; some requires multiple perspectives. **Design implication**: the same artefact can be worked on solo or with a team of agents. The human chooses the agent topology: one generalist, one specialist, or a team. The artefact doesn't change; the collaboration mode does.

---

## Ten Unexpected Insights

These emerged from the cross-pattern analysis. None of them is obvious from any single use case.

### 1. The fundamental unit is the ARTEFACT, not the conversation.

Every use case has something that persists: a strategy, a model, a decision record, a knowledge map. The conversation is just the mechanism for building and refining the artefact. Current tools are conversation-centric when they should be artefact-centric. The conversation should serve the artefact, not be the artefact.

### 2. The wall of text is a TYPE COLLISION problem.

Seventeen types of information, one encoding, zero demultiplexing. The solution isn't "better prose" — it's typed outputs where each piece of information is explicitly what it is. This is an architecture problem, not a formatting problem.

### 3. The most valuable AI capability is STRUCTURING, not generation.

Across every use case, the bottleneck isn't getting more content — it's getting structured, decomposable, manipulable content. The highest-value capability is taking an undifferentiated mass and giving it structure that matches human cognition. Generation is commoditised. Structuring is the differentiator.

### 4. The agent should be a MIRROR, not an ORACLE.

The most valuable outputs aren't new information — they're reflections of the human's own patterns, assumptions, and blind spots. Across personal development, decision support, and sensemaking, the agent's highest-value role is showing you what you already implicitly know but haven't made explicit. This is the Articulation Agent archetype from your own design principles — and it applies to nearly every use case, not just personal ones.

### 5. "What changed?" is the most important unanswered question.

Across iterative and ongoing use cases, the critical question is always "what's different since last time?" Current tools treat every interaction as stateless. Stateful artefacts that surface changes, drifts, and developments as primary output would be transformational.

### 6. Confidence × Reversibility governs everything.

This 2×2 matrix determines whether the agent acts autonomously, recommends, tries, or prepares. It's the control law for the entire human-agent interaction model, and it doesn't exist in any current tool.

### 7. Every use case has a "dark matter" layer.

The unstated assumptions, emotional context, and cognitive load that the human carries but never types. Current tools only see what's in the prompt. A workspace that accumulates this context over time — like a persistent model of the human's world — could dramatically reduce cognitive load per interaction. The prompt is the visible 5%. The workspace should carry the invisible 95%.

### 8. The same content needs MULTIPLE VIEWS, not one.

A strategy is a narrative AND a set of assumptions AND a dependency map AND a risk matrix AND a scenario comparison. The content is the same; the view changes. Current tools give you one view (prose) and force you to request others one at a time. The workspace should show multiple views simultaneously or allow instant view-switching without re-generation.

### 9. The Extraction Hierarchy is a product roadmap.

Level 0 (raw output) through Level 5 (contextual components) isn't just a model — it's a build order. Each level unlocks new use cases and new value. This gives us a principled way to prioritise features and validate that we're building the right thing at the right time.

### 10. The workspace is not a tool — it's an ENVIRONMENT.

Tools are picked up and put down. Environments are inhabited. The 16 use cases describe a space where the human lives and works, not a sequence of transactions. The workspace should feel like an environment you arrange for yourself — with your artefacts, your agents, your views, and your accumulated context — not a chat you restart every time.

This echoes the architectural insight from your dream workspace: **a governed society, not a toolbox.** The agents are actors in your environment. The artefacts are the structures they build and maintain. You are the inhabitant, not the operator.

---

## What This Collectively Tells Us About What We're Building

If I had to compress this entire analysis into a single design brief:

> **Build a sensemaking environment where the human inhabits a workspace of persistent, typed artefacts. Agents serve as judgment preparation systems — structuring, decomposing, relating, and tracking information so the human can see clearly what they're deciding. The fundamental interaction is not "ask and receive" but "arrange, inspect, adjust, and evolve." Conversation is one mode among many. The artefact is primary. The human's role is judgment. The agent's role is preparation. The workspace's role is persistence and structure.**

This is a fundamentally different product category from "AI chat." It's not a better chat interface. It's a new thing.

Ready to take this into interaction paradigm design, or do you want to drill deeper into any of these patterns?

---

## Run 3 — AI UX Innovator ✓ COMPLETED

*2026-04-14T02:36:11* · `glm-5.1:cloud` · `cc73956a...`

### Prompt

Consider these principles to design for neurodivergent people like me (I am ADHD):

The 12 principles are grounded in specific neurological mechanisms:

Cognitive Load as a Budget — cognitive load disproportionately degrades ADHD performance; visual clarity closes the gap

Visibility as Memory — hidden features/tasks are functionally non-existent for working memory-impaired users

One Clear Next Step Always — task initiation is a neurological bottleneck, not a motivational one

Interrupt Architecture — interruptions cost 23 minutes of recovery time; ADHD amplifies this

Engagement Over Priority — ADHD brains run on interest, novelty, and challenge — not abstract importance

Shame-Free Failure States — RSD means "overdue" language triggers avoidance loops, not action

Predictability as Safety — unpredictable interfaces trigger demand avoidance

Zero-Friction Capture — if capturing an idea takes more than 3 seconds, it's gone

Replanning as Normal Workflow — replanning must cost less than starting over

Customisation as Ownership — ADHD profiles are highly variable; no universal solution exists

Multi-Modal Input/Output — different ADHD profiles have different optimal modalities

Cognitive Prosthetic, Not Monitor — software should extend capability, not surveil performance

### Response

Now let me map each principle against our pattern analysis and extract design implications.

---

# ADHD Principles × Pattern Analysis: Design Implications for the Workspace

---

## The Overarching Insight

These 12 principles aren't accessibility add-ons. They're **design constraints that make the product better for everyone**. This is Universal Design: designing for the extremes improves the experience for everyone in the middle. Curb cuts help wheelchair users *and* delivery drivers. Typed outputs help ADHD brains *and* every brain that doesn't want to parse walls of text.

The chat paradigm violates **all 12 principles simultaneously**. This isn't a minor usability problem. It's an architectural mismatch between the medium and the human.

---

## Principle-by-Principle Analysis

---

### 1. Cognitive Load as a Budget

**Neurological mechanism**: ADHD brains have significantly reduced working memory capacity. Cognitive load degrades performance disproportionately.

**Maps to**: Type Collision (Pattern 2), Extraction Hierarchy (Pattern 4), Shannon Channel Problem (Pattern 7)

**The problem with chat**: A 2,000-word AI response requires the ADHD brain to hold 17 different type inferences in working memory simultaneously while reading. That's 17 invisible type categories that must be sorted in real time: *Is this a claim or an assumption? Is this an action or a suggestion? Is this evidence or opinion?* Each type inference competes for the same depleted working memory budget. The brain spends its entire budget on *decoding* rather than *thinking*.

**Design implication**:

> **Type everything at the surface level.** The 17 types (claims, evidence, assumptions, options, criteria, actions, questions, connections, constraints, confidence, perspectives, patterns, gaps, tensions, dependencies, outcomes, provenance) should be **visually distinguishable at a glance** — not by reading and inferring, but by colour, shape, position, or icon. Type inference is the system's job, not the human's. Every unit of type inference the system removes from the human's cognitive budget is a unit returned to actual thinking.

This means typed outputs aren't a "nice to have" formatting feature. They're **cognitive prosthetics** — external working memory that carries type information the ADHD brain can't reliably hold.

**Additional implication**: The workspace should respect cognitive budget by **defaulting to minimum necessary information** and making depth opt-in (drill-down), not opt-out (scroll/skim). This inverts the current chat paradigm where everything is shown and the human must filter.

---

### 2. Visibility as Memory

**Neurological mechanism**: ADHD working memory impairment means that if something isn't visible, it effectively doesn't exist in the current cognitive context. Hidden features, collapsed sections, and off-screen content are functionally absent.

**Maps to**: Artefact-centric model (Insight 1), Temporal Spectrum (Pattern 5)

**The problem with chat**: Chat scrolls. Previous messages disappear. Context is constantly being pushed off screen. For an ADHD brain, "out of sight" literally means "out of mind" — not as a metaphor, but as a neurological reality. Every scroll is a working memory reset.

**Design implication**:

> **The workspace must be spatial, not temporal.** Artefacts, their typed components, and their relationships must be persistently visible — or retrievable with zero cognitive cost. The human should never need to remember where something is. The spatial layout IS the memory.

This means:
- The primary workspace is a **persistent visual field** (canvas, board, surface — not a scroll)
- Artefacts maintain their position. They don't scroll away.
- Relationships between components are visible (lines, proximity, grouping) — not stored in memory
- **Navigation is spatial** (pan, zoom) not sequential (scroll, search)
- The "what changed?" question (Insight 6) must be answerable **at a glance** — changes are visually marked, not buried in a diff

This directly supports the artefact-centric model. Artefacts aren't messages in a scroll. They're objects in a space that you arrange and that persist.

---

### 3. One Clear Next Step Always

**Neurological mechanism**: Task initiation is a neurological bottleneck for ADHD, not a motivational one. The ADHD brain needs a single, unambiguous next action — not a menu of options, not a list of possibilities, not an open-ended prompt.

**Maps to**: Judgment Preparation (Pattern 6), Agency Model (Confidence × Reversibility)

**The problem with chat**: Chat presents infinite options. "What would you like to do?" is the worst possible interface for an ADHD brain. It requires the human to (1) evaluate options, (2) choose one, (3) formulate it, and (4) type it — all before any value is delivered. This is four cognitive steps before initiation, and the ADHD brain gets stuck at step 1.

**Design implication**:

> **The agent's primary output is not an answer. It's a single, clear next action.** After every interaction, the workspace presents exactly one thing the human can do right now — with a single click or keystroke. Not 7 options. Not a menu. One thing.

This reframes Judgment Preparation into something even more precise: **Action Preparation**. The agent doesn't just prepare the judgment space. It reduces it to the smallest possible decision point and presents it as an obvious next step.

Implementation:
- The workspace always has a **"What's next?"** zone showing exactly one recommended action
- That action is executable with one click/keystroke
- The human can always deviate, but the default path is always visible and always one step
- This applies to the Confidence × Reversibility matrix:
  - High confidence + reversible → "Done. Click to see what changed."
  - High confidence + irreversible → "Ready to send. Review and confirm."
  - Low confidence + reversible → "Tried this approach. Review the result."
  - Low confidence + irreversible → "I've prepared three options. Pick one."

---

### 4. Interrupt Architecture

**Neurological mechanism**: Interruptions cost 23 minutes of recovery time. ADHD amplifies this — context switching is neurologically expensive, and recovery requires re-loading the entire working memory state that was displaced.

**Maps to**: Temporal Spectrum (Pattern 5), Replanning (Principle 9), One Clear Next Step (Principle 3)

**The problem with chat**: Chat IS interruption. Every new message interrupts. Every notification breaks context. Every "while you're here, can you also..." derails. And crucially, the ADHD brain has no mechanism to quickly re-load the displaced context — it must be manually reconstructed.

**Design implication**:

> **The workspace must have interrupt architecture built in, not bolted on.** This means: (1) a persistent state that can be exactly resumed, (2) a visual indication of where you were when interrupted, (3) zero-cost context recovery, and (4) the ability to capture incoming ideas without derailing current work.

Implementation:
- **State persistence at the interaction level**: Every workspace state is automatically saved. Returning after an interruption means returning to exactly where you were — same artefact, same zoom level, same highlighted component.
- **Visual breadcrumbs**: The workspace shows what you were doing and where you were in the flow, so resumption is instant, not a reconstruction exercise.
- **The Inbox is separate from the Workspace**: Incoming information, ideas, and agent outputs go to an inbox that doesn't disrupt the current visual field. The inbox is accessible, not urgent. You check it when you're ready, not when it pings.
- **Context snapshots**: Before an interruption, the workspace automatically captures a snapshot of your cognitive state — what artefact you were working on, what you were focused on, what the next step was. This enables the "One Clear Next Step" to be restored immediately after recovery.

---

### 5. Engagement Over Priority

**Neurological mechanism**: ADHD brains run on interest, novelty, and challenge — not abstract importance. This isn't a character flaw; it's a dopamine regulation difference. The ADHD nervous system is interest-based, not importance-based.

**Maps to**: Divergent use cases (Pattern 10 — Creative Exploration), Mirror not Oracle (Insight 7)

**The problem with chat**: Chat presents work as a series of tasks organized by priority. "Here are your top 3 priorities." For an ADHD brain, this is almost guaranteed to trigger avoidance if none of them are interesting. The brain literally cannot engage with "important but boring" in the same way a neurotypical brain can.

**Design implication**:

> **The workspace must present work through the lens of engagement, not priority.** This doesn't mean ignoring what matters — it means *finding the engaging entry point into what matters*. Every priority has an interesting angle. The agent's job is to find it and present it.

Implementation:
- **Interest-first surfacing**: Instead of "Here are your priorities," the workspace shows "Here's something interesting about your strategy" or "I found a pattern in your decisions you might find surprising." (Mirror, not Oracle)
- **Novelty detection as a primary feature**: The "What changed?" function (Insight 6) is inherently engaging — it surfaces the new, the different, the unexpected. This is dopamine-friendly.
- **Challenge framing**: Present tasks as puzzles to solve, not chores to complete. "What assumption would break this strategy?" is more engaging than "Review your strategy."
- **The workspace allows productive tangents**: If the ADHD brain gets interested in something adjacent, the workspace supports following that interest while preserving the ability to return. (This is the Branch operation — Principle 9's "Replanning" in action.)

---

### 6. Shame-Free Failure States

**Neurological mechanism**: Rejection Sensitive Dysphoria (RSD) means that "overdue," "missed," "behind," and "failed" language triggers avoidance loops, not action. The ADHD brain doesn't respond to shame-based motivation — it shuts down.

**Maps to**: Life Management (UC8), Personal Development (UC15), Temporal tracking (Pattern 5), "What changed?" (Insight 6)

**The problem with chat**: AI chat often uses language like "You haven't done X yet" or "This is overdue" or "You should have..." For an ADHD brain, this triggers RSD, which triggers avoidance, which makes the problem worse. It's a vicious cycle.

**Design implication**:

> **The workspace never uses shame language. Ever.** There are no "overdue" labels, no red warnings, no "you haven't done X" messages. Instead, the workspace uses: "What's changed since we last looked at this?" (curiosity, not judgment). "Here's a fresh angle on this." (novelty, not nagging). "This is ready for your next step." (opportunity, not obligation).

Implementation:
- **Time-neutral language**: Instead of "overdue," use "next," "ready for," "evolving." Instead of "you haven't," use "this is waiting for."
- **Progress, not deficit**: Show what's been accomplished, not what's missing. Progress bars fill up, they don't empty.
- **Restart, never punish**: If something was abandoned, the workspace presents it as "ready to pick up" — never as "you didn't finish this." The One Clear Next Step immediately offers a re-entry point.
- **Change detection replaces deadline tracking**: Instead of "this is late," the workspace says "this has evolved since you last saw it" — framing time as change, not failure.

---

### 7. Predictability as Safety

**Neurological mechanism**: Unpredictable interfaces trigger demand avoidance in ADHD brains. If I can't predict what will happen when I click, I'm less likely to click. Predictability creates safety, and safety creates engagement.

**Maps to**: Type System (Pattern 2), Customisation (Principle 10), Cognitive Load (Principle 1)

**The problem with chat**: Chat is inherently unpredictable. The same prompt can produce wildly different outputs. You can't learn the system because the system doesn't behave consistently. This is demand avoidance catnip.

**Design implication**:

> **The workspace must be predictable in structure and surprising in content.** Structure (layout, interaction patterns, type presentation, navigation) must be 100% consistent. Content (what the agent says, what insights surface, what patterns emerge) should be surprising and novel. Structure is the safety rail. Content is the engagement hook.

Implementation:
- **Consistent type presentation**: Every claim looks like a claim. Every assumption looks like an assumption. Every option looks like an option. The visual language is learned once and applies everywhere.
- **Consistent interaction patterns**: Extract always works the same way. Compare always works the same way. Drill always works the same way. The 14 operations are consistent gestures.
- **Consistent agent behaviour**: Agents follow predictable patterns. You learn how the Strategy Agent behaves, and it behaves that way every time. Surprise comes from insight, not from unpredictability.
- **Gradual disclosure**: New features appear predictably, not as surprises. The workspace gets richer over time, but each addition follows a pattern you can anticipate.

---

### 8. Zero-Friction Capture

**Neurological mechanism**: If capturing an idea takes more than 3 seconds, it's gone. The ADHD brain has an ideas window that slams shut fast. The friction of opening a new chat, typing context, and waiting for a response is fatal to idea capture.

**Maps to**: Creative Exploration (UC10), Life Management (UC8), One Clear Next Step (Principle 3)

**The problem with chat**: To capture an idea in chat, you must: (1) decide which chat to use or start a new one, (2) type enough context for the AI to understand, (3) wait for a response, (4) then do something with it. That's 4 steps and 10+ seconds minimum. The idea is already gone.

**Design implication**:

> **Capture must accept untyped, unstructured input and type it AFTER capture.** A single keystroke or gesture captures the raw idea. The workspace then structures it — assigns a type, connects it to relevant artefacts, and presents it back for confirmation. The human never has to decide WHERE or HOW to capture. Just CAPTURE.

Implementation:
- **Universal capture**: A single keyboard shortcut or button captures any input — text, voice, image, URL, file. No context needed.
- **Post-capture typing**: The agent classifies the capture into the type system (claim, idea, question, action, etc.) and presents it back. The human confirms or corrects. This is the "Mirror" function in action — the agent shows you what you captured, typed.
- **Auto-connection**: The agent suggests connections to existing artefacts. "This idea connects to your strategy's assumption about X. Link it?"
- **No destination required**: Captured items go to a universal inbox first. Organisation can happen later. (Replanning as Normal Workflow — Principle 9.)

---

### 9. Replanning as Normal Workflow

**Neurological mechanism**: ADHD brains plan differently. They plan in bursts, adjust frequently, and abandon plans that no longer engage. This isn't a deficit — it's a different planning style. Replanning must cost less than starting over.

**Maps to**: Temporal Spectrum (Pattern 5), "What changed?" (Insight 6), Artefact-centric model (Insight 1)

**The problem with chat**: Chat treats every interaction as independent. There's no plan to replan. The plan existed in the human's head, not in the system, so replanning means reconstructing the entire context.

**Design implication**:

> **Plans are living snapshots, not commitments carved in stone.** The workspace maintains the plan as a persistent artefact. When the plan changes, the workspace shows what changed and why. Replanning is the system presenting the delta, not the human starting over.

Implementation:
- **Artefacts persist**: Strategies, plans, decisions, knowledge maps — they exist as living documents. The workspace tracks their evolution.
- **Change detection is primary**: "Here's what's changed since you last looked" is the default landing view, not "here's your to-do list."
- **Branching, not deleting**: Abandoned plans become branches, not failures. "You explored this direction and chose differently. Here's why." This is shame-free history (Principle 6).
- **Low-cost replanning**: Because plans are typed, structured artefacts, adjusting one assumption automatically recalculates dependent components. Replanning costs a single parameter change, not a complete restart.

---

### 10. Customisation as Ownership

**Neurological mechanism**: ADHD profiles are highly variable. What works for one ADHD brain may not work for another. No universal solution exists. Ownership and customisation create engagement and commitment.

**Maps to**: Personalisation vs. Universality (Tension T4), Mirror not Oracle (Insight 7), Multi-Modal (Principle 11)

**The problem with chat**: Chat has one interface: text input, text output. One modality. One pace. One density. No customisation. It's a universal solution for a population that has no universal.

**Design implication**:

> **The workspace adapts to the human, not the other way around.** Every aspect — density, modality, pace, colour, layout, information hierarchy, agent personality, type presentation — is customisable. But not through a settings menu. Through use. The workspace learns from behaviour and adapts. Customisation through doing, not configuring.

Implementation:
- **Progressive customisation**: The workspace starts with sensible defaults and adapts based on observed behaviour. If you always expand assumptions first, assumptions get prioritised. If you prefer visual over textual, visual becomes default.
- **Multiple views of the same artefact**: The same strategy can be viewed as a narrative, a map, a timeline, a set of assumptions, or a decision tree. The human chooses the view that works for their brain.
- **Agent personality matching**: Different humans need different agent orientations. Some need the Critic. Some need the Explorer. Some need the Mirror. The workspace adapts agent orientation over time.
- **Layout ownership**: The spatial workspace can be arranged by the human. Artefact positions, zoom levels, grouping — these are personal preferences that persist.

---

### 11. Multi-Modal Input/Output

**Neurological mechanism**: Different ADHD profiles have different optimal modalities. Some are visual processors. Some are verbal. Some are kinesthetic. Some switch modalities based on cognitive load. The same brain may prefer visual input when fresh and text input when tired.

**Maps to**: Shannon Channel Problem (Pattern 7), Transform operation (14 operations), Design Tension T2 (Structure ↔ Freedom)

**The problem with chat**: Chat is text-in, text-out. One modality. For visual processors, this is a permanent handicap. For tired brains, it's a wall. For kinesthetic processors, it's disembodied.

**Design implication**:

> **Input and output must support multiple modalities, and the human must be able to switch between them at any point without losing context.** The same artefact can be consumed as text, viewed as a diagram, listened to as audio, or manipulated as cards. The modality is a view preference, not a content constraint.

Implementation:
- **Input**: Text, voice, sketch/diagram, file upload, drag-and-drop, gesture. Zero-friction capture (Principle 8) means any modality can capture an idea.
- **Output**: The same typed content can be rendered as:
  - Text (narrative)
  - Cards (typed components)
  - Diagram (relationships between components)
  - Table (comparison)
  - Timeline (evolution)
  - Audio (read aloud)
  - The Transform operation (one of our 14) is a first-class interaction: switch view with a single click.
- **Modality switching**: Start with text, switch to visual when the text gets dense, switch to audio when eyes are tired. The artefact doesn't change. The view does.

---

### 12. Cognitive Prosthetic, Not Monitor

**Neurological mechanism**: ADHD brains have impaired executive function (planning, organising, prioritising, initiating). Software that extends these capabilities is a prosthetic. Software that tracks performance against those capabilities is surveillance. The emotional difference is enormous: prosthetics are empowering; surveillance is shaming.

**Maps to**: Judgment Preparation (Pattern 6), Mirror not Oracle (Insight 7), Environment not Tool (Insight 10)

**The problem with chat**: Chat doesn't extend executive function — it requires it. You must initiate, plan, prioritise, and organise every interaction. The chat sits there waiting for you to figure out what to do. It's a monitor, not a prosthetic.

**Design implication**:

> **The workspace extends capability rather than tracking compliance.** It remembers what you can't. It surfaces what you'd miss. It suggests the next step when you're stuck. It maintains the structure when your working memory drops it. It doesn't tell you what you should have done; it shows you what you can do next.

Implementation:
- **Working memory externalisation**: The workspace holds the structure (types, relationships, dependencies) so the human doesn't have to. This is the type system as cognitive prosthetic.
- **Proactive surfacing, not reactive waiting**: Instead of waiting for a prompt, the workspace proactively shows what's changed, what's ready, what's next. (But respectfully — Principle 4: interrupt architecture.)
- **Pattern mirroring**: "You tend to abandon strategies after 2 weeks. Your current strategy is at day 12. Would you like to check in on it?" — This is mirror, not monitor. It surfaces your own patterns, not your compliance.
- **No progress tracking against external standards**: No streaks, no scores, no "you're behind." Progress is measured against your own past, not against an external timeline. "This strategy has evolved 3 times since you created it. Here's how." Not "You haven't updated this in 14 days."

---

## Five Reinforcing Intersections

Where principles combine, they produce emergent design insights that no single principle would generate alone.

---

### Intersection 1: Capture → Structure → Present

**Principles**: Zero-Friction Capture + One Clear Next Step + Replanning as Normal

**Emergent insight**: The core workflow loop isn't "prompt → response." It's **capture → structure → present**.

1. **Capture** (ZFC): Human inputs something — untyped, unstructured, any modality. Zero friction.
2. **Structure** (System): The workspace types it, connects it, positions it. Zero cognitive load on the human.
3. **Present** (OCNS): The workspace surfaces exactly one clear next step. Not a menu. Not a question. One action.

This loop replaces the chat loop (prompt → generate → read → infer → decide → type next prompt) with a loop that externalises cognition at every step.

The Replanning principle ensures this loop is iterative: the human can capture → structure → present, then decide to replan, and the cycle starts again with the plan already structured. Replanning costs nothing because the artefact persists.

---

### Intersection 2: Mirror → Engage → Extend

**Principles**: Engagement Over Priority + Mirror Not Oracle + Cognitive Prosthetic

**Emergent insight**: The most engaging agent output is **your own thinking reflected back at you**. The Mirror principle (Insight 7) isn't just about decision support — it's about engagement. ADHD brains engage with what's interesting, and nothing is more interesting than seeing your own patterns surfaced in ways you hadn't noticed.

This means:
- The agent doesn't tell you what to do. It shows you what you've been doing.
- The agent doesn't present priorities. It presents patterns.
- The agent doesn't nag. It mirrors.
- The prosthetic doesn't track compliance. It extends capability by showing you what you can't see alone.

This combination transforms the agent from an authority figure (engagement-killing, demand-avoidance-triggering) into a thinking partner (engagement-building, novelty-providing, challenge-offering).

---

### Intersection 3: Predictable Structure, Surprising Content

**Principles**: Predictability as Safety + Type System + Customisation as Ownership

**Emergent insight**: The workspace has two layers that must be designed independently:

- **Structure layer**: 100% predictable. Same types, same operations, same navigation, same interaction patterns. Learned once, applied everywhere. This creates safety.
- **Content layer**: Surprising, novel, engaging. New insights, unexpected connections, patterns you hadn't seen. This creates engagement.

The ADHD brain needs BOTH. Predictability without surprise is boring (engagement failure). Surprise without predictability is overwhelming (cognitive load failure). The workspace must be **structurally predictable and contently surprising**.

Customisation (Principle 10) sits at the intersection: the human customises the structure to their preference (layout, modality, density), while the content adapts based on their patterns and interests. Structure becomes more predictable over time (as you customise it to your brain). Content becomes more surprising over time (as the Mirror surfaces deeper patterns).

---

### Intersection 4: Emotional Safety Infrastructure

**Principles**: Shame-Free Failure States + Cognitive Prosthetic Not Monitor + Replanning as Normal + Dark Matter (Insight 8)

**Emergent insight**: The workspace needs **emotional safety infrastructure** as much as it needs cognitive infrastructure. This isn't soft — it's structural. Without it, the ADHD brain will avoid the workspace entirely.

Emotional safety infrastructure includes:
- **No shame language** (Principle 6): No "overdue," "missed," "behind." Ever.
- **No surveillance** (Principle 12): No compliance tracking, no scores, no streaks.
- **No lost work** (Principle 9): Abandoned paths become branches, not failures. Re-entry is always possible.
- **Dark matter awareness** (Insight 8): The workspace carries context the human doesn't have to articulate. It remembers preferences, patterns, and history without requiring the human to restate them. This reduces the cognitive AND emotional load of every interaction.

The combined effect: the workspace is a **safe place to think**. You can't lose work. You can't fall behind. You can't be shamed. You can always pick up where you left off. This is the foundation on which everything else is built. Without emotional safety, none of the cognitive features matter — the ADHD brain won't use them.

---

### Intersection 5: Typed Outputs Are Cognitive Accessibility

**Principles**: Cognitive Load Budget + Visibility as Memory + Zero-Friction Capture + Predictability as Safety + Type Collision (Insight 2)

**Emergent insight**: The type system (17 types, 14 operations) isn't just a useful feature — it's **cognitive accessibility infrastructure**. Every typed output removes a unit of cognitive load from the human. Every visible type removes the need to infer it. Every predictable interaction removes the need to learn it. Every zero-friction capture removes the need to organise before you can think.

This means the Extraction Hierarchy (Level 0–5) isn't just a product roadmap — it's an **accessibility roadmap**:

| Level | Accessibility Impact |
|-------|---------------------|
| L0: Raw output | **Hostile.** Requires full type inference in working memory. Maximum cognitive tax. |
| L1: Typed components | **Accessible.** Types are visible. Type inference is externalised. Cognitive budget freed for thinking. |
| L2: Related components | **Empowering.** Relationships are visible. Working memory for connections is externalised. |
| L3: Manipulable components | **Prosthetic.** Can adjust, compare, combine without cognitive load. Executive function extended. |
| L4: Evolving components | **Memory externalised.** Changes tracked over time. No need to remember what changed. |
| L5: Contextual components | **Dark matter surfaced.** Personal patterns, preferences, history carried by the system. The human brings less context each time. |

Each level is a step toward the workspace being a cognitive prosthetic rather than a cognitive tax. The product roadmap IS the accessibility roadmap.

---

## The Chat Paradigm: 12 Violations

For completeness, here's how the current chat paradigm violates each principle:

| # | Principle | How Chat Violates It |
|---|-----------|---------------------|
| 1 | Cognitive Load Budget | Forces 17-type inference on every message. Maximum cognitive tax. |
| 2 | Visibility as Memory | Scrolls previous content off screen. Working memory reset on every scroll. |
| 3 | One Clear Next Step | Presents infinite options ("What would you like to do?"). Requires 4 cognitive steps before any value. |
| 4 | Interrupt Architecture | Every message is an interruption. No state persistence. No context recovery. |
| 5 | Engagement Over Priority | Presents tasks by importance, not interest. No novelty detection. No challenge framing. |
| 6 | Shame-Free Failure | No persistent artefacts to abandon and return to. No concept of "evolved plans" — only the current state. Shame enters through "you didn't finish" framing. |
| 7 | Predictability as Safety | Same prompt, different response. Unpredictable structure. No learned interaction patterns. |
| 8 | Zero-Friction Capture | 4+ steps to capture an idea. Context required before value delivered. 3-second window missed. |
| 9 | Replanning as Normal | No persistent plan artefact. Replanning = restating the entire context. Costs the same as starting over. |
| 10 | Customisation as Ownership | One interface. One modality. One density. No layout control. No view switching. |
| 11 | Multi-Modal I/O | Text in, text out. That's it. |
| 12 | Cognitive Prosthetic | Requires executive function to use. Monitors compliance through conversation history. Doesn't extend capability. |

The chat paradigm violates all 12. Not some. Not most. All.

This isn't a UX problem. It's an architectural mismatch. You can't fix chat by making it "better chat." You need a fundamentally different paradigm.

---

## What the Workspace Feels Like

When all 12 principles are honoured, the workspace feels like this:

**You open it.** Your artefacts are there, exactly where you left them. Nothing has moved. The structure is familiar. (Predictability as Safety. Visibility as Memory.)

**One thing is highlighted.** "This assumption in your strategy has new evidence. Want to see it?" One clear next step. You click. (One Clear Next Step. Engagement Over Priority.)

**The evidence appears as a typed card** — not a wall of text. You can see it's evidence (not a claim, not an opinion) because the type is visible. You can see its confidence level, its provenance, and what it connects to. (Cognitive Load Budget. Type System. Related Components.)

**You read the evidence.** It's interesting. It challenges an assumption. You capture a thought: "What if this assumption is wrong?" — one keystroke, no context needed. The workspace types it as a question, connects it to the assumption, and presents it back. (Zero-Friction Capture. Mirror.)

**You decide to explore the question.** You branch: "What happens if this assumption fails?" The workspace generates a stress-test — not a wall of text, but a structured comparison of scenarios with typed components. You can adjust the assumption and see cascading effects. (Replanning as Normal. Manipulable Components. Judgment Preparation.)

**You get interrupted.** A meeting starts. You close the workspace. When you return, it's exactly where you left it — same artefact, same branch, same next step highlighted. (Interrupt Architecture. Visibility as Memory.)

**Three days later, you return.** The workspace says: "This strategy has evolved 3 times since you created it. Here's what changed." Not "you haven't checked this in 3 days." No shame. Just information. (Shame-Free. Change Detection. Prosthetic.)

**You notice the workspace has learned something about you.** It's started surfacing assumptions first, because you always check assumptions before claims. It's using diagrams more, because you click through those faster. The customisation happened through doing, not configuring. (Customisation as Ownership. Multi-Modal.)

**And throughout, the workspace never told you what to do.** It showed you what you're working on. It surfaced your own patterns. It prepared your judgments. It extended your working memory. It carried your context. It kept your ideas safe. It made replanning free. It gave you one clear step, always.

**That's not chat. That's a cognitive environment.**

---

Ready to translate these principles and patterns into a concrete interaction paradigm — the actual UX model for the workspace?

---

## Run 4 — AI UX Innovator ✓ COMPLETED

*2026-04-14T02:58:59* · `glm-5.1:cloud` · `7e8c739b...`

### Prompt

Let's first zoom into a single use case to understand how these principles and patterns could be applied. 
Perhaps start with the collaborative written content production use case.
What problem is the user trying to solve? What is their goal?
What is the ideal user flow?

### Response

# Collaborative Written Content Production: Ideal User Flow

---

## The Problem

You want to write something — an article, a report, a blog post, a strategy document. What you actually want is to **develop your thinking** and **produce writing that captures it clearly**. The writing serves the thinking, not the other way around.

Current tools give you two terrible options:

1. **Write it yourself** — staring at a blank page, trying to hold your entire argument in working memory while you produce prose in linear order
2. **Ask an AI** — receive a wall of text that may contain 3 brilliant ideas buried in 2000 words you can't decompose, rearrange, or selectively keep

Neither option matches how your brain actually works.

---

## How ADHD Writing Actually Works

ADHD writing is **accretive**, not generative. The brain doesn't produce a complete outline and then fill it in. It works like this:

1. **Fragment** — a claim, a question, an analogy, a title, a turn of phrase — arrives
2. **Another fragment** arrives, possibly about a different part of the same piece
3. **A connection** between fragments becomes visible
4. **A structural insight** — "this should be the argument, not that" — emerges
5. **A burst of writing** — words flow for one specific section
6. **An interruption** — an idea for a different section, or a real-world interruption
7. **A return** — picking up where you left off, or shifting to a different part
8. **A revision** — seeing that something you wrote needs to move, change tone, or connect differently

This is not a failure of planning. It's a different planning style — one that builds from fragments rather than from outlines. The ideal flow must support accretive writing, not fight it.

---

## The Goal

**Produce a structured, typed artefact where every component (claim, evidence, assumption, action, question, etc.) is explicitly typed, linked, and manipulable — and from which prose can be generated for any audience, tone, or medium.**

The skeleton is primary. The prose is a rendering of the skeleton. Change the skeleton, regenerate the prose. Change the audience, regenerate the prose. The thinking persists; the prose serves it.

---

## The Artefact: What You're Actually Building

Before the flow, you need to understand what you're building. It's not a document. It's this:

```
┌─────────────────────────────────────────────────────┐
│  ARTEFACT: "Why Type Collision Is the Root Problem"  │
│                                                      │
│  ┌─── PURPOSE ───┐                                   │
│  │  Convince AI   │                                   │
│  │  tool designers│                                   │
│  │  that the wall │                                   │
│  │  of text is a  │                                   │
│  │  type problem, │                                   │
│  │  not a format  │                                   │
│  │  problem       │                                   │
│  └────────────────┘                                   │
│                                                      │
│  ┌─── AUDIENCE ──┐                                   │
│  │  Product       │                                   │
│  │  designers and │                                   │
│  │  AI tool       │                                   │
│  │  builders      │                                   │
│  └────────────────┘                                   │
│                                                      │
│  ┌─── SKELETON ──────────────────────────────────┐  │
│  │                                                 │  │
│  │  🔵 CLAIM: The wall of text problem is a type  │  │
│  │     collision problem, not a formatting problem │  │
│  │     ├─ 🟢 EVIDENCE: 17 distinct types of info │  │
│  │     │  appear across knowledge work use cases  │  │
│  │     ├─ 🟢 EVIDENCE: LLMs encode all 17 types │  │
│  │     │  as a single type (prose)                 │  │
│  │     └─ 🔴 QUESTION: Is 17 the right number,   │  │
│  │        or is this a spectrum?                     │  │
│  │                                                 │  │
│  │  🔵 CLAIM: Typed outputs reduce cognitive load  │  │
│  │     ├─ ⚠️ ASSUMPTION: Type inference is the    │  │
│  │     │  primary cognitive cost of reading AI     │  │
│  │     │  output                                  │  │
│  │     ├─ 🟢 EVIDENCE: ADHD working memory        │  │
│  │     │  impairment makes type inference          │  │
│  │     │  disproportionately costly               │  │
│  │     └─ 🟣 PERSPECTIVE: This is a universal     │  │
│  │        design problem, not an accessibility    │  │
│  │        special case                           │  │
│  │                                                 │  │
│  │  🔵 CLAIM: The solution is typed, decomposable │  │
│  │     outputs, not better prose                   │  │
│  │     ├─ ⚠️ ASSUMPTION: Users want to interact   │  │
│  │     │  with components, not just read them     │  │
│  │     ├─ 🔴 QUESTION: What are the interaction   │  │
│  │     │  patterns for typed components?          │  │
│  │     └─ 🟡 OPTION: Artefact-centric workspace   │  │
│  │        with typed components as first-class    │  │
│  │        objects                                 │  │
│  │                                                 │  │
│  └─────────────────────────────────────────────────┘  │
│                                                      │
│  ┌─── ASSUMPTIONS ──┐  ┌─── QUESTIONS ──┐           │
│  │ ⚠️ Type inference │  │ 🔴 Is 17 the   │           │
│  │    is the primary │  │    right       │           │
│  │    cognitive cost  │  │    number?     │           │
│  │ ⚠️ Users want to  │  │ 🔴 What are    │           │
│  │    interact, not   │  │    interaction │           │
│  │    just read      │  │    patterns?   │           │
│  └────────────────────┘  └────────────────┘           │
│                                                      │
│  ┌─── PROSE RENDERING ────────────────────────────┐  │
│  │  [Blog post] [Report] [Thread] [Deck] [Abstract]│  │
│  │  Status: Draft  ·  Audience: AI tool builders    │  │
│  │  Tone: Analytical  ·  Last evolved: 2 days ago  │  │
│  └─────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

This is what you're building: a **structured, typed artefact** where:
- Every component is explicitly what it is (🔵 claim, 🟢 evidence, ⚠️ assumption, 🔴 question, 🟣 perspective, 🟡 option)
- Relationships between components are visible (claims are supported by evidence, challenged by questions, built on assumptions)
- The skeleton is separate from the prose — you can rearrange, add, or remove components without touching the prose
- Prose is **generated from** the skeleton, not the other way around
- Multiple prose renderings can exist for the same skeleton (blog post, report, thread, deck, abstract)
- Assumptions, questions, and gaps are tracked explicitly — not lost in the prose

---

## The Ideal User Flow

### Phase 0: Arrival

You open the workspace. Your artefacts are there, exactly where you left them. (Visibility as Memory. Predictability as Safety.)

**One thing is highlighted.** The workspace shows you:

> 💡 **"Your 'Type Collision' artefact has new connections. 3 related assumptions from your Strategy artefact. Want to see them?"**

One clear next step. You click. (OCNS. Engagement Over Priority. Mirror Not Oracle.)

---

### Phase 1: Capture — Getting Ideas In

You have a vague impulse: "I want to write about the type collision problem." You don't have an outline. You don't have a thesis. You have fragments.

**You type, speak, or paste your first fragment:**

> "The wall of text problem isn't a formatting problem — it's a type collision problem"

**Zero friction.** One keystroke captures this. No context required. No "what kind of artefact?" No "what's the audience?" Just capture. (ZFC. Cognitive Load Budget.)

The workspace **types the fragment for you**:

> 🔵 **CLAIM** captured: "The wall of text problem isn't a formatting problem — it's a type collision problem"

You didn't have to decide it was a claim. The system inferred it and presents it back for confirmation. You can change it, but you don't have to. (Mirror Not Oracle. Predictability as Safety.)

**Another fragment arrives** — possibly from a different part of your brain:

> "17 distinct information types appear across all knowledge work use cases"

The workspace types it:

> 🟢 **EVIDENCE** captured: "17 distinct information types appear across all knowledge work use cases"

**And connects it** to your existing claim:

> 💡 **"This evidence supports your claim about type collision. Link it?"**

One click. Connected. (Visibility as Memory. Related Components — L2 of the Extraction Hierarchy.)

**A third fragment** — this time it's a doubt, not a conviction:

> "But is 17 really the right number? What if it's more of a spectrum?"

The workspace types it:

> 🔴 **QUESTION** captured: "Is 17 the right number, or is this a spectrum?"

**And attaches it** to the relevant claim:

> 💡 **"This question challenges your claim about type collision. Attach it?"**

You're building. Fragments are arriving, getting typed, getting connected. No outline required. No linear order required. The structure emerges from the fragments. (Accretive writing. Replanning as Normal.)

**An interruption** — a meeting starts. You close the workspace. (Interrupt Architecture.)

---

### Phase 2: Return — Picking Up Where You Left Off

You return three days later. The workspace opens to exactly where you were:

> 📍 **"You were building 'Type Collision Is the Root Problem.' Last activity: captured a question about whether 17 types is the right number. Here's where you left off:"**

Your artefact is visible. Your fragments are there. Your connections are there. Your next step is highlighted. (Interrupt Architecture. Visibility as Memory. One Clear Next Step.)

**The workspace shows you what changed** since you last looked:

> 🔄 **"While you were away, your Strategy artefact developed an assumption about type collision that connects here. Also: your question about 17 types now has a related gap — no one has formally categorised AI output types."**

This is "What changed?" in action. Not "you haven't been here in 3 days" (shame). Not "here's your to-do list" (priority). **Interesting, relevant change** surfaced for you. (Shame-Free. Engagement Over Priority. Change Detection — L4 of the Extraction Hierarchy.)

---

### Phase 3: Structure — Arranging What You Have

You now have 6 fragments: 2 claims, 2 pieces of evidence, 1 question, 1 assumption. Time to arrange them.

The workspace presents the **skeleton view** — your components as typed cards on a surface:

```
🔵 CLAIM: Wall of text is type collision, not formatting
🟢 EVIDENCE: 17 distinct types across use cases
🟢 EVIDENCE: LLMs encode all 17 as single type
🔴 QUESTION: Is 17 the right number?
⚠️ ASSUMPTION: Type inference is primary cognitive cost
🔵 CLAIM: Typed outputs reduce cognitive load
🟣 PERSPECTIVE: This is universal, not accessibility-only
```

**You drag and rearrange.** Claims at the top. Evidence underneath. Questions on the side. Assumptions flagged. The spatial arrangement IS the argument structure. (Visibility as Memory. Manipulable Components — L3.)

**You notice a gap.** The argument assumes type inference is the primary cognitive cost, but you haven't stated that explicitly. You click the assumption and upgrade it:

> ⚠️ ASSUMPTION → "Type inference is the primary cognitive cost of reading AI output"

The workspace flags this as **unsupported** — no evidence yet. It's visible. You can't forget it. (Cognitive Load Budget. Related Components.)

---

### Phase 4: Develop — Going Deep on One Section

You're ready to work on one specific claim. You click it:

> 🔵 CLAIM: "The wall of text problem isn't a formatting problem — it's a type collision problem"

The workspace zooms into this claim. You see:
- Its supporting evidence (2 items)
- Its challenging questions (1 item)
- Its assumptions (1 item)
- Its status (draft — no prose yet)

**One clear next step:**

> ✏️ **"Generate prose for this claim?"** or ✏️ **"Add more evidence?"** or ✏️ **"Explore the question first?"**

You choose "Generate prose." The agent writes prose for just this claim, drawing on the connected evidence and assumptions. (Judgment Preparation. Agent as Structurer, not Generator.)

The prose appears as a **rendering** of the skeleton — clearly secondary to the structure. You can edit it, or you can edit the skeleton and regenerate. The prose serves the thinking; the thinking doesn't serve the prose.

**You spot something in the generated prose** — a turn of phrase you like:

> "...like a database storing everything as a single string field"

You **extract it** as a separate typed component:

> 💎 **PHRASE** captured: "like a database storing everything as a single string field"

Now it's its own object. You can use it in any rendering. It won't be lost in the prose. (ZFC. Extraction — one of the 14 operations.)

---

### Phase 5: Stress-Test — Checking the Argument

You have a structured skeleton with prose for some claims. Time to check if the argument actually works.

You invoke the **Stress-Test agent** — a specialist that examines your argument:

> 🔍 **"I've found 2 unsupported assumptions, 1 unanswered question, and 0 counter-evidence."**

It presents its findings as **typed components** connected to your skeleton:

> ⚠️ UNSUPPORTED: "Type inference is the primary cognitive cost" — no evidence linked
> 🔴 UNANSWERED: "Is 17 the right number?" — no resolution
> 🟢 COUNTER-EVIDENCE: none found (good sign)

The stress-test doesn't give you a wall of text analysis. It gives you **typed, connected components** you can act on. You can:
- Click the unsupported assumption to add evidence
- Click the unanswered question to explore it
- Accept the counter-evidence status as reassurance

Each action is one click. One clear next step. (Judgment Preparation. OCNS. Stress-Test operation.)

---

### Phase 6: Adapt — Changing Audience, Tone, Medium

The skeleton is solid. Now you need this as a blog post, a Twitter thread, and a slide deck.

**You don't rewrite.** You change the rendering parameters:

> 📄 **RENDER:** Audience → "AI tool builders" · Tone → "Analytical" · Medium → "Blog post"
> 📄 **RENDER:** Audience → "General tech" · Tone → "Conversational" · Medium → "Twitter thread"
> 📄 **RENDER:** Audience → "Conference attendees" · Tone → "Persuasive" · Medium → "Slide deck"

The agent generates each rendering FROM THE SAME SKELETON. The claims, evidence, assumptions, and questions don't change. Only the prose wrapping changes. (Transform operation. Separation of structure from presentation.)

You can view any rendering at any time. You can edit the skeleton and regenerate all renderings. **The thinking persists. The prose serves it.**

---

### Phase 7: Evolve — Returning After Time

Two weeks later, you return. The workspace shows:

> 🔄 **"Your 'Type Collision' artefact has evolved. Since you last worked on it:"**
> - ✅ The question "Is 17 the right number?" now has a **gap** attached: "No formal categorisation of AI output types exists"
> - 📎 A new **evidence** item was linked by the Research Agent: "Cognitive load theory confirms type inference cost"
> - 📊 Your **assumption** "Type inference is primary cognitive cost" has moved from ⚠️ unsupported to 🟡 partially supported

**What changed?** Answered. **What's new?** Surfaced. **What's next?** One clear step. (L4 Evolving Components. L5 Contextual Components. Change Detection. Shame-Free. Engagement Over Priority.)

You never see "you haven't updated this in 2 weeks." You see **what evolved in your absence.** Your artefact grew while you were away. You can engage with the growth, or you can ignore it and go in a new direction. (Cognitive Prosthetic. Replanning as Normal.)

---

## The Flow, Abstracted

The abstract pattern underlying this narrative:

```
CAPTURE ──→ TYPE ──→ CONNECT ──→ ARRANGE ──→ DEVELOP ──→ RENDER
   │           │         │          │           │           │
   │           │         │          │           │           ├→ Blog post
   │           │         │          │           │           ├→ Thread
   │           │         │          │                     ├→ Deck
   │           │         │          │           │           └→ Abstract
   │           │         │          │           │
   │           │         │          │           └→ Prose is generated per-component
   │           │         │          │              from skeleton, not the other way
   │           │         │          │
   │           │         │          └→ Spatial arrangement = argument structure
   │           │         │             (not linear outline)
   │           │         │
   │           │         └→ Components link to each other
   │           │             (claims→evidence, assumptions→impacts)
   │           │
   │           └→ System infers type (claim, evidence, assumption, etc.)
   │              Human confirms or corrects
   │              (Mirror, not Oracle)
   │
   └→ Any modality, any fragment, zero context required
      (Zero-Friction Capture)
```

**At any point**, the 14 operations are available: Extract, Isolate, Compare, Adjust, Combine, Rearrange, Drill, Navigate, Track, Evaluate, Transform, Annotate, Branch, Stress-Test.

**At any point**, the human can:
- Add a fragment (ZFC)
- See what changed (L4, Change Detection)
- Get one clear next step (OCNS)
- Switch modalities (Multi-Modal)
- Branch the argument (Replanning)
- Switch views (Transform — skeleton, prose, map, comparison)
- Stress-test (Judgment Preparation)

**The agent can**:
- Type captured fragments (Mirror)
- Suggest connections (L2 Related Components)
- Generate prose for any component (Structuring, not Generating)
- Run specialist agents (Stress-Test, Counter-Perspective, Gap-Finder)
- Detect changes since last visit (L4)
- Adapt to the human's patterns over time (L5)

---

## What Makes This Different From Current Tools

| Current Chat Paradigm | This Workspace |
|---|---|
| Start with a blank prompt | Start with a fragment — any fragment |
| Receive a wall of text | See typed, connected components |
| Can't isolate the 3 good ideas | Every idea is its own typed object |
| Can't rearrange the argument | Drag, drop, rearrange the skeleton |
| Can't see what's assumed vs. claimed | Types are visible: claims, evidence, assumptions, questions |
| Can't separate thinking from writing | Skeleton = thinking; prose = rendering |
| Can't adapt for different audiences | Change rendering parameters, regenerate |
| Can't stress-test the argument | Specialist agents examine the skeleton |
| Can't find where you left off | Persistent artefact, visual breadcrumbs |
| Can't see what changed | Change detection as primary output |
| Can't capture a fragment in <3 seconds | One keystroke capture, system types it |
| Can't rearrange without rewriting | Skeleton rearrangement, prose follows |
| Can't track assumptions | Assumptions are first-class typed objects |
| Chat is the primary interface | Artefact is the primary interface; chat is a sidebar |
| Every interaction is stateless | Artefact persists and evolves |
| Agent is an oracle | Agent is a mirror and structurer |

---

## The Key Design Principles in Action

| Principle | How It Manifests |
|---|---|
| **Cognitive Load Budget** | Types are visible, not inferred. Skeleton view replaces walls of text. Depth is opt-in. |
| **Visibility as Memory** | Artefact is persistently visible. No scrolling. No reconstruction. Spatial layout IS memory. |
| **One Clear Next Step** | Always one highlighted action. "Generate prose for this claim?" Not a menu of 7 options. |
| **Interrupt Architecture** | Exact state persistence. Visual breadcrumbs. Inbox separate from workspace. |
| **Engagement Over Priority** | "3 new connections found" not "3 tasks overdue." Mirror, not taskmaster. |
| **Shame-Free Failure** | No "overdue" labels. Artefacts "evolved," not "abandoned." Re-entry is always one click. |
| **Predictability as Safety** | Types look the same everywhere. Operations work the same everywhere. Structure is consistent. |
| **Zero-Friction Capture** | One keystroke captures any fragment. System types it. No context needed. |
| **Replanning as Normal** | Rearranging the skeleton IS replanning. No cost. Branches, not deletions. |
| **Customisation as Ownership** | View switches (skeleton, prose, map, comparison). Layout persists. Agent learns your patterns. |
| **Multi-Modal I/O** | Capture via text, voice, paste, drag. View as skeleton, prose, map, timeline. |
| **Cognitive Prosthetic** | The workspace holds structure so you don't have to. It surfaces changes so you don't miss them. It mirrors your thinking so you can see it. |

---

This is the flow for one use case. But the underlying pattern — **capture → type → connect → arrange → develop → render** — applies to all 16 use cases. The types change. The rendering changes. The agents change. But the flow is the same.

Want to explore another use case through this flow, or start translating this into a concrete interaction paradigm and UX model?

---

## Run 5 — AI UX Innovator ✓ COMPLETED

*2026-04-14T03:17:58* · `glm-5.1:cloud` · `35d8d275...`

### Prompt

explore another use case

### Response

# Strategy Development: Ideal User Flow

---

## Why This Use Case Stresses Our Pattern

Written content production was **accretive and expressive** — fragments arriving, getting typed, connecting into an argument skeleton, prose generated from structure. The primary artefact was a document. The temporal mode was episodic → iterative.

Strategy development is **nearly the opposite in every dimension that matters**:

| Dimension | Written Content | Strategy Development |
|---|---|---|
| Primary types | Claims, evidence, questions | Assumptions, options, dependencies, scenarios |
| Primary operations | Extract, Rearrange, Transform | Adjust, Stress-Test, Compare, Track, Branch |
| Temporal mode | Episodic → Iterative | **Iterative → Ongoing** (strategies never stop evolving) |
| Artefact shape | Structured argument with prose renderings | **Living system with no final version** |
| Key risk | Wall of text | **Shiny idea chasing, invisible assumptions, drift** |
| Confidence × Reversibility | Low confidence + reversible (draft, iterate) | **Low confidence + irreversible (strategic decisions)** |
| Agency model | Human directs, agent structures | **Human decides, agent prepares judgment** |

This is the test: does our flow pattern hold when the artefact never finishes, the primary types are different, the primary operations are different, and the consequences of decisions are irreversible?

---

## The Problem

You're developing a strategy. For Future's Edge, for a client, for a product, for yourself. What you want is to **make good decisions under uncertainty**, see your own assumptions clearly, compare options rigorously, and know when your strategy is drifting.

Current tools give you two terrible options:

1. **Think it through yourself** — but your working memory can't hold all the assumptions, dependencies, and options simultaneously. You lose track of what depends on what. Shiny ideas feel like new strategies rather than branches to explore.

2. **Ask an AI** — receive a dense strategy document where assumptions, options, evidence, and recommendations are all mixed together. You can't isolate the assumptions. You can't adjust one and see what changes. You can't compare options side by side. You can't see how the strategy has evolved over time.

And there's a third problem specific to ADHD strategy work:

3. **You get excited by new ideas** — every new possibility feels like a pivot, not a branch. You can't see that the new idea might be compatible with the existing strategy, or that it might be a variation of something you already considered. Ideas proliferate without structure. Without visibility, assumptions go underground. Decisions get avoided because they feel permanent.

---

## How ADHD Strategy Work Actually Works

ADHD strategy work is **divergent-first, convergent-later** — but current tools force immediate convergence (write the strategy document, pick the option, make the decision). The actual process:

1. **Ideas arrive fast and from many angles** — a new market, a new product angle, a new partnership, a competitive threat. The brain sees connections and possibilities everywhere.
2. **Working memory can't hold all the assumptions** — so assumptions go underground. You make decisions based on assumptions you don't know you're making.
3. **New ideas feel like new strategies** — but they might be branches of the same strategy, or they might be genuinely new directions. You can't tell because you can't see the whole picture.
4. **Comparing options is overwhelming** — each option has multiple dimensions (market size, competition, risk, effort, alignment). You can't hold all the dimensions for all the options in working memory.
5. **Decisions feel permanent** — so you avoid them, gathering more information instead of committing. But without decisions, the strategy has no shape.
6. **The strategy evolves** — what seemed right last month feels different this month. But you can't see *what* changed or *why*. Is it a real shift, or just the shiny idea of the month?

---

## The Goal

**Produce a living strategy artefact where every assumption, option, dependency, and decision is explicitly typed, linked, and adjustable — and from which scenarios can be generated, compared, and stress-tested.**

The strategy is not a document. It's a **lattice** — a connected system of assumptions, options, dependencies, decisions, and outcomes. Documents are renderings of the lattice. The lattice persists. The renderings serve it.

---

## The Artefact: What You're Actually Building

```
┌──────────────────────────────────────────────────────────────────────┐
│  ARTEFACT: "Future's Edge Go-To-Market Strategy"                     │
│  Status: ACTIVE · Last evolved: 3 hours ago · Version: 14           │
│                                                                      │
│  ┌─── PURPOSE ─────────────────────────────────────────────────┐    │
│  │  Establish Future's Edge as the leading provider of          │    │
│  │  AI skills education for career and venture acceleration     │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─── ASSUMPTIONS LATTICE ──────────────────────────────────────┐    │
│  │                                                                │    │
│  │  ⚠️ A1: "AI training market will grow 40% annually"          │    │
│  │     Confidence: 🟡 Medium  ·  Dependencies: A2, A4           │    │
│  │     Source: Industry report ·  First made: Jan 12             │    │
│  │                                                                │    │
│  │  ⚠️ A2: "Non-technical professionals are underserved"         │    │
│  │     Confidence: 🟢 High  ·  Dependencies: A5                  │    │
│  │     Source: Customer research ·  First made: Dec 28           │    │
│  │                                                                │    │
│  │  ⚠️ A3: "Agno framework is a differentiator"                  │    │
│  │     Confidence: 🟡 Medium  ·  Dependencies: A1               │    │
│  │     Source: Competitive analysis ·  First made: Feb 3          │    │
│  │                                                                │    │
│  │  ⚠️ A4: "Enterprises will pay premium for agentic AI skills"  │    │
│  │     Confidence: 🔴 Low  ·  Dependencies: —                    │    │
│  │     Source: Intuition ·  First made: Mar 15 ·  ⚠️ NEW        │    │
│  │                                                                │    │
│  │  ⚠️ A5: "Career accelerator programs can be delivered online" │    │
│  │     Confidence: 🟢 High  ·  Dependencies: —                  │    │
│  │     Source: Market validation ·  First made: Jan 20           │    │
│  │                                                                │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─── OPTIONS MATRIX ───────────────────────────────────────────┐    │
│  │                                                                │    │
│  │        Market    Speed    Risk    Alignment    Invest           │    │
│  │  O1:  Enterprise  Slow    Low     High        $$$$$            │    │
│  │  O2:  Individual  Fast    Med     Med         $$$             │    │
│  │  O3:  Hybrid      Med     Med     High        $$$$            │    │
│  │                                                                │    │
│  │  O4:  🌟 NEW: Platform play — become the agentic AI skill     │    │
│  │       marketplace (shiny idea from yesterday)                 │    │
│  │       → Not yet evaluated ·  Branch from O1/O3                │    │
│  │                                                                │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─── DEPENDENCIES ─────────────────────────────────────────────┐    │
│  │                                                                │    │
│  │  A1 ──→ O1 ──→ "Enterprise requires agentic AI skills"       │    │
│  │  A3 ──→ O3 ──→ "Agno differentiator enables hybrid"          │    │
│  │  A4 ──→ O1 ──→ "Enterprise premium justifies slow approach"   │    │
│  │  A2 ──→ O2 ──→ "Underserved market justifies fast approach"   │    │
│  │                                                                │    │
│  │  🔴 A4 has no evidence. If A4 is wrong, O1 is weakened.      │    │
│  │                                                                │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─── DECISIONS ────────────────────────────────────────────────┐    │
│  │                                                                │    │
│  │  ✅ D1: Focus on career accelerator first (Made: Jan 20)     │    │
│  │     → Based on: A2, A5 ·  Reversible: Yes ·  Status: ACTIVE │    │
│  │                                                                │    │
│  │  ✅ D2: Use Agno as technical foundation (Made: Feb 3)       │    │
│  │     → Based on: A3 ·  Reversible: Partially ·  Status: ACTIVE│    │
│  │                                                                │    │
│  │  ⏳ D3: Enterprise vs. individual first? (Pending)            │    │
│  │     → Depends on: A4, O1 vs O2 comparison                    │    │
│  │     → Confidence: 🔴 Low ·  Reversibility: 🔴 Low            │    │
│  │     → 🚨 LOW CONFIDENCE + LOW REVERSIBILITY = HUMAN DECIDES │    │
│  │                                                                │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─── SCENARIOS ────────────────────────────────────────────────┐    │
│  │                                                                │    │
│  │  S1: "AI training market grows as projected"                  │    │
│  │     → A1 holds, A2 holds, A4 holds                            │    │
│  │     → O1 (enterprise) is strongest                            │    │
│  │                                                                │    │
│  │  S2: "AI training market grows but enterprises are slow"      │    │
│  │     → A1 holds, A2 holds, A4 FAILS                            │    │
│  │     → O2 (individual) is strongest ·  ⚠️ O1 weakened          │    │
│  │                                                                │    │
│  │  S3: "Agno gets commoditised"                                 │    │
│  │     → A3 FAILS                                                 │    │
│  │     → All options weakened ·  🔴 STRATEGIC PIVOT NEEDED       │    │
│  │                                                                │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─── EVOLUTION TIMELINE ───────────────────────────────────────┐   │
│  │  Dec 28 ─── Jan 12 ─── Jan 20 ─── Feb 3 ─── Mar 15 ──→     │  │
│  │  A2 added    A1 added    D1 made     D2 made    A4 added      │  │
│  │                          A5 added    A3 added    ⚠️ NEW       │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  💡 NEXT STEP: Assumption A4 has low confidence and no evidence.     │
│     This assumption weakens O1 (enterprise path).                   │
│     Would you like to:                                               │
│     [Add evidence for A4]  [Stress-test A4]  [Compare O1 vs O2]    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## The Ideal User Flow

### Phase 0: Arrival

You open the workspace. Your strategy artefact is there, exactly where you left it. But unlike the writing use case — where you might not have looked at it in weeks — strategy artefacts are **ongoing**. Things have happened since you were last here.

**The workspace shows you what changed:**

> 🔄 **"Since you were last here (3 days ago):"**
> - ⚠️ A new assumption (A4: "Enterprises will pay premium for agentic AI skills") was added by you in a late-night session
> - 📎 A research agent found **partial evidence** for A1 (market growth) but **no evidence** for A4
> - 🔗 The dependency between A4 and O1 was automatically detected: if A4 is wrong, the enterprise option weakens
> - 🌟 A new option (O4: Platform play) was captured from your notes — it's not yet evaluated

This is **"What changed?"** in action. Not a to-do list. Not "you should work on this." Interesting, relevant change surfaced for you. (Change Detection. Engagement Over Priority. Mirror Not Oracle.)

**One clear next step is highlighted:**

> 💡 **"Assumption A4 has low confidence and no evidence. This weakens O1. Want to stress-test it?"**

(OCNS. Judgment Preparation. Confidence × Reversibility.)

---

### Phase 1: Capture — Ideas Arriving

You've been thinking about Future's Edge. A new idea arrives: "What if we became the marketplace for agentic AI skills — not just training, but matching trained people with companies that need them?"

**In the old paradigm:** This idea would either be lost (if you didn't write it down immediately) or become a new, competing strategy (if you wrote it down as a separate document). It feels like a pivot. It might not be.

**In this workspace:** One keystroke captures it:

> 🟡 **OPTION** captured: "Platform play — become the agentic AI skill marketplace"

Zero friction. No context needed. No "is this a new strategy or a branch of the existing one?" The system captures the raw idea and types it as an option. (ZFC. Cognitive Load Budget.)

**The workspace automatically connects it:**

> 💡 **"This option relates to your existing O1 (Enterprise) and O3 (Hybrid). Want to branch it?"**

You click "Branch." The new option appears as O4, connected to the existing strategy. It's not a restart. It's an exploration. (Replanning as Normal. Branch operation.)

**A doubt also arrives:** "But do enterprises actually pay premium for agentic AI skills? That feels like an assumption, not a fact."

Capture:

> ⚠️ **ASSUMPTION** captured: "Enterprises will pay premium for agentic AI skills"

The workspace types it and immediately flags it:

> ⚠️ **Low confidence, no evidence.** This assumption supports O1 (Enterprise). If it's wrong, O1 weakens.

This is the Mirror function. The workspace isn't telling you what to think. It's showing you the structure of your own thinking — making your assumption visible and showing its dependencies. You might not have noticed that your enterprise strategy rests on this assumption. Now you can't miss it. (Mirror Not Oracle. Visibility as Memory. Cognitive Prosthetic.)

---

### Phase 2: Structure — Making Assumptions Visible

The most dangerous aspect of strategy work is **assumptions you don't know you're making**. Current tools bury assumptions in prose. The workspace makes them first-class objects.

You have 5 assumptions. The workspace shows them as a lattice:

```
⚠️ A1: AI training market grows 40%/yr ·  🟡 Medium confidence ·  📎 Evidence: 2 items
⚠️ A2: Non-technical professionals underserved ·  🟢 High confidence ·  📎 Evidence: 5 items  
⚠️ A3: Agno framework is a differentiator ·  🟡 Medium confidence ·  📎 Evidence: 1 item
⚠️ A4: Enterprises pay premium for agentic skills ·  🔴 Low confidence ·  📎 Evidence: 0 items
⚠️ A5: Career accelerator can be delivered online ·  🟢 High confidence ·  📎 Evidence: 3 items
```

Each assumption has: a confidence level (typed, not inferred), a count of supporting evidence, and links to the options that depend on it. You can see at a glance that A4 is weak and that your enterprise option depends on it. (Cognitive Load Budget. Type Collision resolved. Visibility as Memory.)

**This is the most valuable thing the workspace does for strategy: make assumptions visible, typed, and connected to their dependencies.** Not buried in prose. Not held in working memory. First-class objects in the lattice.

---

### Phase 3: Compare — Seeing Options Side by Side

You have 4 options. In the old paradigm, you'd describe each in prose and try to hold them all in working memory while comparing. In this workspace, they're in a **comparison matrix**:

```
                Market      Speed      Risk      Alignment    Invest
O1: Enterprise   Large       Slow       Low       High        $$$$$
O2: Individual   Medium      Fast       Med       Med          $$$
O3: Hybrid       Large       Med        Med       High        $$$$
O4: Platform     V.Large     Slow       High      Med         $$$$$$$
```

Each cell is a typed component — not prose. You can:
- **Adjust any cell** and see cascading effects (Adjust operation)
- **Stress-test any assumption** and see which options change (Stress-Test operation)
- **Compare two options** side by side in detail (Compare operation)
- **Branch an option** to explore a variation without losing the original (Branch operation)

(Manipulable Components — L3. One Clear Next Step.)

The workspace surfaces the key decision:

> 🚨 **"The biggest decision you're facing is D3: Enterprise vs. Individual first."**
> 
> This depends on **A4** (low confidence, no evidence) and the **O1 vs O2 comparison.**
> 
> **Confidence:** 🔴 Low · **Reversibility:** 🔴 Low
> 
> This sits in the **"Human decides, agent prepares"** quadrant.

This is the Confidence × Reversibility matrix in action. The workspace doesn't make the decision. It shows you exactly what decision you're facing, what it depends on, and how much confidence you should have. Judgment Preparation. (OCNS. Judgment Preparation. Confidence × Reversibility.)

---

### Phase 4: Stress-Test — Checking If the Strategy Holds

You want to know: "What happens if A4 is wrong? What if enterprises DON'T pay premium for agentic AI skills?"

**Old paradigm:** This requires holding the entire strategy in working memory and reasoning through it. Cognitive load catastrophe.

**This workspace:** You click A4. You click "Stress-Test: What if this assumption fails?"

The workspace runs the cascade:

```
A4 FAILS ─── O1 WEAKENED (enterprise option relies on A4)
         └── D2 PARTIALLY AFFECTED (Agno decision less impacted)
         
REMAINING VIABLE OPTIONS:
  ✅ O2 (Individual) — not dependent on A4
  ⚠️ O3 (Hybrid) — partially dependent on A4, still viable with individual component
  ❌ O1 (Enterprise) — significantly weakened without A4
  ❓ O4 (Platform) — unknown dependency on A4

SCENARIO S2 ACTIVATED: "AI training market grows but enterprises are slow"
  → Individual and hybrid paths are strongest
  → Enterprise path requires new evidence for A4 or a pivot
```

This took one click. No cognitive load. The workspace holds the dependency structure and cascades the impact. You see the result. You decide what it means. (Stress-Test operation. Manipulable Components. Judgment Preparation.)

---

### Phase 5: Branch — When the Shiny Idea Arrives

A new idea arrives: "What if we partner with universities to certify agentic AI skills?"

**Old paradigm:** This feels like a new strategy. It derails the current one. You start a new document, lose track of the old one, and now have two strategies that might be compatible but you can't see how.

**This workspace:** One keystroke captures it as a new option:

> 🟡 **OPTION** captured: "University partnership for certification"

The workspace automatically connects it to existing components:

> 💡 **"This relates to A5 (career accelerator online) and O2 (Individual). Branch from O2?"**

You click "Branch." The new option appears as O5, branching from O2. The existing strategy is untouched. The new idea is explored alongside it, not instead of it. If it works, it gets merged. If it doesn't, it stays as a branch — not a failure, not a distraction. A possibility that was explored.

**This directly addresses the shiny idea chasing challenge.** Shiny ideas aren't problems. They're possibilities. The problem is that current tools can't hold them alongside the existing strategy without overwhelming working memory. The workspace can. (Replanning as Normal. Branch operation. Shame-Free — abandoned branches aren't failures.)

---

### Phase 6: Decide — Making the Irreversible Decision

You've compared options. You've stress-tested assumptions. You've explored branches. Now you need to decide: Enterprise or Individual first?

**The workspace presents a Decision Card:**

```
┌─── DECISION: D3 ───────────────────────────────────────────────┐
│                                                                  │
│  QUESTION: Enterprise vs. Individual first?                      │
│                                                                  │
│  DEPENDS ON:                                                     │
│  ⚠️ A4 (Low confidence, no evidence) — supports Enterprise     │
│  ⚠️ A2 (High confidence, 5 evidence) — supports Individual      │
│                                                                  │
│  REVERSIBILITY: 🔴 LOW (committing resources)                   │
│  CONFIDENCE: 🔴 LOW (key assumption untested)                   │
│                                                                  │
│  ──────────────────────────────────────────────────────────────── │
│  QUADRANT: Human decides, agent prepares                        │
│  ──────────────────────────────────────────────────────────────── │
│                                                                  │
│  OPTIONS COMPARED:                                               │
│  ┌──────────────────────┬──────────────────────┐                │
│  │  O1: Enterprise      │  O2: Individual       │                │
│  │  Market: Large       │  Market: Medium       │                │
│  │  Speed: Slow         │  Speed: Fast          │                │
│  │  Risk: Low (if A4)   │  Risk: Medium         │                │
│  │  Alignment: High    │  Alignment: Medium    │                │
│  │  Invest: $$$$$       │  Invest: $$$           │                │
│  │  ⚠️ Depends on A4    │  ✅ Independent of A4 │                │
│  └──────────────────────┴──────────────────────┘                │
│                                                                  │
│  SUGGESTED NEXT STEPS:                                           │
│  [Test A4 first]  [Choose O2 (lower risk)]  [Choose O1 anyway] │
│                                                                  │
│  📊 Decision quality: Deciding now with untested A4 = 🔴 LOW    │
│  📊 Decision quality: Testing A4 first = 🟡 MEDIUM               │
│  📊 Decision quality: Choosing O2 (independent of A4) = 🟢 HIGH │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**The agent doesn't make the decision.** It prepares the ground. It shows you what you're deciding, what it depends on, how confident you can be, and what the options look like side by side. It suggests next steps that might improve decision quality. But the decision is yours.

This is **Judgment Preparation** at its most critical: low confidence, low reversibility. The human decides. The agent makes the decision as clear as possible. (Judgment Preparation. Confidence × Reversibility. OCNS.)

---

### Phase 7: Evolve — The Strategy Changes Over Time

Three months later, you return. The workspace shows:

> 🔄 **"Your strategy has evolved 14 times since December. Here's what changed:"**
> 
> - A4 moved from 🔴 Low confidence to 🟡 Medium (you tested it with 3 enterprise conversations)
> - O4 (Platform play) was explored and **branched off as a future possibility** — not abandoned, but deferred
> - D3 was made: **Individual first, enterprise later** — based on O2's independence from A4
> - New assumption A6 emerged from customer research: "Career accelerator participants want portfolio projects"
> - O2 evolved: now includes a portfolio project component based on A6
> - 🆕 The research agent flagged a **new gap**: no evidence on whether portfolio projects affect hiring outcomes

**Nothing is lost.** Every decision, assumption, option, and branch is tracked. The strategy's evolution is visible. You can see why you made each decision, what assumptions it rested on, and what changed since then. (Track operation. L4 Evolving Components. Shame-Free — "evolved," not "abandoned.")

---

## How This Flow Differs From Written Content Production

| Dimension | Written Content | Strategy Development |
|---|---|---|
| **Entry point** | A fragment of writing (claim, phrase, idea) | A fragment of strategic thinking (assumption, option, doubt) |
| **Primary capture types** | Claims, evidence, questions, phrases | Assumptions, options, dependencies, scenarios |
| **Primary operation in Phase 3** | Arrange (rearranging the argument skeleton) | Compare (seeing options side by side) |
| **Primary operation in Phase 4** | Develop (prose generation for a claim) | Stress-Test (what if this assumption fails?) |
| **Primary operation in Phase 5** | Adapt (change audience/tone/medium) | Branch (explore a shiny idea alongside the current strategy) |
| **Primary operation in Phase 6** | Render (generate prose from skeleton) | Decide (make a judgment with agent-prepared information) |
| **Temporal mode** | Episodic → Iterative | **Iterative → Ongoing** |
| **Key risk addressed** | Wall of text | **Shiny idea chasing, invisible assumptions** |
| **What "done" means** | Published | **Never done — always evolving** |
| **Agent's highest-value role** | Structurer (organise fragments) | **Mirror (surface hidden assumptions) + Judgment Preparer (present decisions clearly)** |

---

## What's the Same: The Underlying Pattern

Despite the differences, the abstract flow is the same:

```
CAPTURE ──→ TYPE ──→ CONNECT ──→ ARRANGE ──→ DEVELOP ──→ RENDER
   │           │         │          │           │           │
   │           │         │          │           │           └→ Scenarios
   │           │         │          │           └→ Stress-test, Compare, Decide
   │           │         │          └→ Options matrix, dependency lattice
   │           │         └→ Assumptions link to options and decisions
   │           └→ System infers type (assumption, option, dependency...)
   │              Human confirms or corrects
   └→ Any modality, any fragment, zero context required
```

**The pattern holds.** The flow is universal. The types change. The operations change. The artefact changes. But the fundamental pattern — **capture fragments, type them, connect them, arrange them, develop them, render them** — works for both written content production and strategy development.

---

## What's Different: The ADHD-Specific Interventions

Strategy development surfaces ADHD-specific challenges more sharply than writing:

| ADHD Challenge | Workspace Intervention |
|---|---|
| **Shiny idea chasing** | Every idea becomes a **branch**, not a restart. Branches are explored alongside the current strategy. They can be merged or deferred, not lost or abandoned. |
| **Invisible assumptions** | Assumptions are **first-class typed objects** with confidence levels, evidence counts, and dependency links. You literally cannot miss them. |
| **Comparison paralysis** | Options are **comparable** in a matrix, not described in prose. The decision card shows exactly what you're deciding and what it depends on. |
| **Decision avoidance** | OCNS + Confidence × Reversibility shows you **one decision at a time**, with preparation. The agent doesn't decide for you; it makes the decision clear. |
| **Strategy drift** | Evolution timeline + change detection shows **what changed and why**. You can see if you're drifting or evolving. |
| **Working memory overload** | The lattice holds all assumptions, options, and dependencies **externally**. You see the whole picture without holding it in your head. |
| **RSD-triggering "overdue" items** | Strategy components **evolve** — they're never "overdue." Change is framed as growth, not failure. |

---

## The Key Insight From This Use Case

Strategy development reveals something the writing use case didn't fully expose:

> **The Confidence × Reversibility matrix is the GOVERNOR of the entire interaction model.**

In written content, most decisions are reversible (you can always edit). In strategy, many decisions are **irreversible** (committing resources, choosing a market, launching a product). The interaction model must change based on where a decision sits in the matrix:

- **High confidence + reversible** → Agent acts, human reviews later. (Auto-add evidence to an assumption)
- **High confidence + irreversible** → Agent recommends, human confirms. (Suggesting a well-evidenced strategic direction)
- **Low confidence + reversible** → Agent tries, human sees result. (Exploring a branch option)
- **Low confidence + irreversible** → **Agent PREPARES, human DECIDES.** (The enterprise vs. individual decision)

This quadrant — low confidence, low reversibility — is where strategy lives. The agent's highest-value role here is not to generate answers but to **prepare the clearest possible frame for the human's judgment**.

This is the deepest expression of "Judgment Preparation, not Answer Generation." And it's why the agent must be a **Mirror** in strategy work — surfacing your own assumptions, showing you the structure of your own thinking, making the invisible visible. The agent doesn't know your strategy better than you do. But it can hold more of it simultaneously than your working memory can.

---

The pattern holds across two maximally different use cases. Ready to explore a third, or start translating this into a concrete interaction paradigm?

---

## Run 6 — AI UX Innovator ✓ COMPLETED

*2026-04-14T03:38:17* · `glm-5.1:cloud` · `1daca660...`

### Prompt

Explore one more use case

### Response

# Creative Exploration and Ideation: Ideal User Flow

---

## Why This Use Case Stresses Our Pattern Differently

Written content production was **convergent and expressive** — build a skeleton, then render it as prose. The agent was a **Structurer**.

Strategy development was **convergent and decisive** — build a lattice, then make judgments. The agent was a **Mirror and Judgment Preparer**.

Creative exploration is **divergent and non-linear**. It doesn't converge. It doesn't build toward a deliverable. It *spreads*. The agent's role shifts again — to **Muse**: surfacing connections, proposing mutations, keeping energy flowing.

This is also where a crucial ADHD insight flips:

> **The same neurological trait — novelty-seeking, interest-based engagement, idea proliferation — that's a CHALLENGE in strategy work is a SUPERPOWER in creative work.**

The workspace must **amplify** this superpower, not suppress it. Shiny idea chasing isn't a problem here. It's the *method*.

---

## The Problem

You're exploring a creative space — brainstorming a product concept, ideating a business model, developing a design concept, writing a story, or just following curiosity wherever it leads. What you want is to **generate, connect, combine, and evolve ideas** without losing them, without being overwhelmed, and without the fun dying.

Current tools give you terrible options:

1. **Brainstorm in your head** — ideas arrive fast and leave faster. ADHD working memory drops them within seconds. You have three brilliant ideas in a row and remember one.

2. **Write a list** — linear, sequential, forgettable. Lists kill creative energy. They flatten what should be a constellation into a sequence. Ideas that should connect across the list are separated by lines. And you can't riff on individual ideas without losing the thread.

3. **Ask an AI** — receive a bulleted list of 10 ideas that all sound the same. You can't grab one idea and say "but what if THIS part was different?" You can't breed two ideas together. You can't see where your ideas went in and the AI's ideas came out. And the format is so boring that your ADHD brain checks out by idea #4.

4. **Mind map** — better, but still limited. Ideas are boxes on branches. You can't combine two ideas from different branches without redrawing. You can't mutate an idea in place. You can't see "what if" without committing to a new branch.

The ADHD creative process is:
- **Bursty** — ideas arrive in clusters, not in sequence
- **Non-linear** — idea #7 connects back to idea #2
- **Combinatory** — two ideas breed a third that's neither parent
- **Mutation-prone** — "what if we changed this one thing?" is the primary creative move
- **Energy-dependent** — the process only works while engagement is high; when interest fades, it stops

Current tools are linear, static, boring, and hostile to bursty non-linear thinking.

---

## How ADHD Creative Exploration Actually Works

1. **An idea arrives** — from anywhere: a conversation, a walk, a shower, reading, dreaming. It's often not an idea but a fragment — a question, an image, a connection, an analogy.

2. **The fragment sparks another** — not sequentially, but associatively. Idea A reminds you of idea B, which reminds you of idea C, which connects back to something you thought of last week.

3. **You see a connection** — two fragments from different places suddenly relate. This is the moment of creative insight, and it depends on both fragments being VISIBLE at the same time.

4. **You want to mutate** — "what if we changed this one thing about idea A?" You don't want a new version that replaces the old one. You want BOTH. The original AND the mutation. Side by side.

5. **You want to combine** — "what if idea A and idea B had a baby?" This is combinatory play, and it's the core of creativity. But current tools can't do this. You can't breed two list items.

6. **Energy drops** — you hit a wall, get distracted, or the flow stops. Every idea you've captured needs to be PRESERVED, not lost to the void of a closing tab or a forgotten note.

7. **You return later** — and you want to see what you were thinking, not reconstruct it. What sparked? What connected? What felt exciting? The emotional charge matters as much as the logical content.

8. **You want to go deeper on one idea** — but only one. The others can wait. You want to develop this idea without losing sight of the constellation it came from.

9. **You want to share or use the idea** — but only the best ones. The seedbed needs a way to surface what's ready to become something, versus what's still a seed.

---

## The Goal

**Produce a living seedbed of ideas — each one a typed, connected, mutable object that can grow, combine, mutate, and evolve — where the process itself is engaging enough to sustain ADHD creative flow.**

The artefact is not a document (writing) or a lattice (strategy). It's a **seedbed** — a space where ideas are seeds that can sprout, cross-pollinate, and grow into something larger. Some seeds will sprout. Some will stay dormant for months and then germinate. Some will be combined into hybrids. The seedbed is never "done." It's always growing.

---

## The Artefact: What You're Actually Building

```
┌──────────────────────────────────────────────────────────────────────────┐
│  SEEDBED: "Future's Edge Product Concepts"                               │
│  Status: GROWING · Seeds: 23 · Sprouts: 5 · Hybrids: 3 · Last tended: 1h │
│                                                                          │
│  ┌─── SEEDS ──────────────────────────────────────────────────────────┐  │
│  │                                                                     │  │
│  │  💡 S1: "Agentic AI skills marketplace" · 🟢 High energy · 🔗 4  │  │
│  │     → from: late-night idea · tagged: platform, product            │  │
│  │                                                                     │  │
│  │  💡 S2: "Micro-credentials for agent design" · 🟡 Med energy · 🔗 2│  │
│  │     → from: conversation with Jay · tagged: credentials, product   │  │
│  │                                                                     │  │
│  │  💡 S3: "AI+Human collaboration workspace" · 🔴 High energy · 🔗 7│  │
│  │     → from: frustration with current tools · tagged: product, core │  │
│  │                                                                     │  │
│  │  💡 S4: "Generative Exploration Swarm as curriculum content" · 🔗 3│  │
│  │     → from: connecting agent design to business model · tagged:    │  │
│  │        curriculum, product                                         │  │
│  │                                                                     │  │
│  │  💡 S5: "ADHD-friendly productivity system" · 🟡 Med energy · 🔗 5│  │
│  │     → from: personal experience · tagged: product, neurodivergent │  │
│  │                                                                     │  │
│  │  ... 18 more seeds ...                                              │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌─── CONNECTIONS ─────────────────────────────────────────────────────┐  │
│  │                                                                     │  │
│  │  S1 ──tag:platform── S3    "Both need a platform"                  │  │
│  │  S2 ──tag:credentials── S4 "Credentials validate curriculum"      │  │
│  │  S3 ──tag:neurodivergent── S5  "Workspace must be ADHD-friendly"  │  │
│  │  S5 ──tag:product── S1    "Marketplace needs ADHD users"          │  │
│  │  S4 ──tag:curriculum── S3  "Swarm teaches workspace design"      │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌─── HYBRIDS (bred from 2+ seeds) ───────────────────────────────────┐  │
│  │                                                                     │  │
│  │  🔀 H1: "ADHD-friendly AI collaboration workspace as curriculum   │  │
│  │          project" · Parents: S3 + S5 + S4 · Energy: 🟢 High       │  │
│  │                                                                     │  │
│  │  🔀 H2: "Micro-credentials for agentic AI design via platform"    │  │
│  │          · Parents: S1 + S2 · Energy: 🟡 Medium                   │  │
│  │                                                                     │  │
│  │  🔀 H3: "Generative exploration swarm for product ideation"       │  │
│  │          · Parents: S4 + S1 · Energy: 🟡 Medium                   │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌─── SPROUTS (seeds with enough energy to develop further) ──────────┐  │
│  │                                                                     │  │
│  │  🌱 H1 → "Workspace as curriculum project" ──────────────── 🟢     │  │
│  │     → has: typed artefacts, argument skeletons, seedbeds          │  │
│  │     → needs: business model, target market definition             │  │
│  │     → next: [Develop into artefact] [Stress-test] [Compare]      │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌─── EVOLUTION ───────────────────────────────────────────────────────┐  │
│  │                                                                     │  │
│  │  ● S1 captured (3 days ago)                                        │  │
│  │  ● S3 captured (2 days ago) · connected to S1, S5                  │  │
│  │  ● H1 bred from S3+S5+S4 (1 day ago) · high energy                │  │
│  │  ● S5 mutated: "ADHD-friendly" → "neurodivergent-by-design"       │  │
│  │  ● 🔥 H1 energy rising — 3 connections in last 24h                │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  💡 NEXT STEP: Hybrid H1 has rising energy and 3 strong connections.     │
│     [Develop H1]  [Breed H1 with another seed]  [Explore connections]   │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## The Ideal User Flow

### Phase 1: Capture — Ideas Arriving Fast

You're in the shower. An idea arrives: "What if we made the collaboration workspace itself the curriculum project for the accelerator program?"

**In the old paradigm:** By the time you're out of the shower, the idea is half-gone. By the time you find a note app, type it out, and add context, it's a shadow of what it felt like. The emotional charge — the excitement — is already fading.

**In this workspace:** One gesture. Voice, text, whatever. Zero friction.

> 💡 **SEED** captured: "What if the collaboration workspace itself is the curriculum project for the accelerator?"

**The workspace captures not just the idea, but the energy around it:**

> 🟢 **High energy** (captured at the moment — not retroactively rated)

Why does energy matter? Because creative ideas have an emotional charge. The ones that excite you are the ones worth developing. The ones that feel "meh" might be good, but they won't sustain ADHD engagement. Energy is the engagement signal. (Engagement Over Priority.)

**The workspace types the seed and starts connecting:**

> 💡 **"This connects to 3 existing seeds:"**
> - S3: "AI+Human collaboration workspace" → same product concept
> - S4: "Generative Exploration Swarm as curriculum" → curriculum connection
> - S5: "ADHD-friendly productivity system" → neurodivergent design connection
>
> **Create hybrid?** [Yes — H1] [Just connect] [Not now]

You click "Yes." Three seeds breed a hybrid. Not a new document. Not a new list item. A **hybrid** — a new idea that has two or three parents, whose DNA is traceable. (Combine operation. Engagement Over Priority. ZFC.)

---

### Phase 2: Connect — Seeing What Relates

You're on a roll now. Ideas are arriving. Each one gets captured in under 3 seconds. Each one gets typed and connected.

But here's where the seedbed differs from a list or a mind map: **connections are surfaced by the Muse agent, not just created by you.**

The Muse agent watches your seed patterns and says:

> 🧬 **"Your seeds keep mentioning 'neurodivergent' and 'workspace' together. That's 4 connections now. This might be a theme worth exploring."**

This is the Mirror function in creative mode — not reflecting your assumptions back to you (that's strategy), but reflecting your **patterns of interest** back to you. The Muse shows you what you're already drawn to, before you can articulate it. (Mirror Not Oracle. Engagement Over Priority. Cognitive Prosthetic.)

**Another connection:**

> 🧬 **"Seed S1 (marketplace) and Seed S2 (micro-credentials) share a tag: 'platform.' Want to explore what a platform combining these might look like?"**

[Explore] → The Muse doesn't write a 2000-word document. It generates a **seed sketch** — a 2-sentence description of what the combination might look like, typed as a potential hybrid. You can develop it, mutate it, or let it sit.

---

### Phase 3: Mutate — "What If We Changed This One Thing?"

You're looking at Seed S5: "ADHD-friendly productivity system." A mutation arrives:

> 🧬 **"What if we reframed S5 from 'ADHD-friendly' to 'neurodivergent-by-design'?"**
>
> Current: "ADHD-friendly productivity system"
> Mutation: "Neurodivergent-by-design productivity system"
>
> [Keep both] [Replace] [Mutate further]

**"Keep both"** is the key. In creative work, you don't want to choose between the original and the mutation. You want to see them side by side. Both are valid. The mutation might be better. Or the original might be better for one context and the mutation for another. (Branch operation. Replanning as Normal. Shame-Free — no idea is "wrong", just "not yet developed.")

The mutation creates a new seed: S5a, linked to S5 as its parent. You can trace the genealogy of any idea. Where did it come from? What did it mutate from? What did it combine with? (Provenance. Track operation. L4 Evolving Components.)

---

### Phase 4: Combine — Breeding Ideas

The most distinctive creative operation is **combinatory play** — taking two ideas and breeding a third that inherits from both. Current tools can't do this. You can't breed two bullet points.

In this workspace, you select two (or more) seeds:

> 🔀 **Breed S3 × S5:**
>
> Parent A: "AI+Human collaboration workspace"
> Parent B: "ADHD-friendly productivity system"
>
> **Muse suggests 3 offspring:**
>
> 🧬 O1: "An ADHD-first AI workspace that replaces chat with typed artefacts"
>    → Inheriting: workspace concept (A) + ADHD-first design (B)
>
> 🧬 O2: "A cognitive prosthetic that structures your thinking in real-time"
>    → Inheriting: AI collaboration (A) + cognitive prosthetic (B)
>
> 🧬 O3: "A seedbed for ideas — where AI captures, connects, and breeds your fragments"
>    → Inheriting: collaboration (A) + fragment capture (B)

Each offspring is a **typed seed** with genealogy, energy level, and connections. You can develop any of them, breed them further, or let them sit in the seedbed.

**This is the Combine operation at its most creative.** Two ideas become three. None is "the answer." All are possibilities. The workspace doesn't converge — it **diverges productively**, then lets you decide which paths are worth developing. (Engagement Over Priority. Combine operation. Branch operation.)

---

### Phase 5: Develop — Going Deep on One Idea

Hybrid H1 has rising energy. You want to develop it. You click "Develop."

**In writing, "Develop" meant generating prose from a skeleton. In strategy, "Develop" meant stress-testing assumptions. In creative exploration, "Develop" means something different: growing a seed into something that has enough structure to evaluate.**

The workspace doesn't generate a wall of text. It generates a **seed sketch**:

```
🌱 H1: "ADHD-friendly AI collaboration workspace as curriculum project"
   ┌──────────────────────────────────────────────────────────┐
   │  What it is: A workspace that teaches AI skills by using  │
   │  AI skills — the product IS the pedagogy                  │
   │                                                            │
   │  Why it might work:                                        │
   │  🔗 S3 → Real product validates curriculum                 │
   │  🔗 S5 → ADHD-first design differentiates                  │
   │  🔗 S4 → Swarm methodology becomes curriculum content     │
   │                                                            │
   │  What it needs:                                            │
   │  ❓ Business model                                         │
   │  ❓ Target market validation                                │
   │  ❓ Technical feasibility                                   │
   │                                                            │
   │  Energy: 🟢 High · Connections: 7 · Parents: S3+S5+S4     │
   └──────────────────────────────────────────────────────────┘
```

The seed sketch shows what the idea IS, why it might work (with links to its parent seeds), and what it still needs. It's not a business plan. It's a **germination** — enough structure to evaluate, not enough to be overwhelming. (OCNS. Cognitive Load Budget.)

**One clear next step:**

> 💡 **"H1 has 3 open questions. Want to explore the business model question? Or develop the 'product is pedagogy' angle?"**

You choose. The workspace follows your energy. (Engagement Over Priority.)

---

### Phase 6: Graduate — From Seed to Artefact

Some seeds will grow strong enough to become full artefacts. H1 might become a strategy lattice. It might become a written content argument. It might become a product spec.

**The seedbed doesn't force graduation.** Seeds can stay seeds forever. But when a seed has enough energy, connections, and development, the workspace suggests:

> 🎓 **"H1 has high energy, 7 connections, and 3 rounds of development. It might be ready to become a Strategy Lattice or a Product Spec. Graduate it?"**

If you say yes, the seed becomes a new artefact — with all its connections, genealogy, and development preserved. It doesn't leave the seedbed. It's still connected. But it now has its own structure: a strategy lattice, an argument skeleton, a product spec.

**This is the key transition from creative exploration to other use cases.** The seedbed feeds writing. The seedbed feeds strategy. The seedbed feeds product development. Ideas start as seeds and graduate into structured artefacts when they're ready.

---

### Phase 7: Return — After Time Away

Two weeks later, you open the seedbed. You haven't looked at it in a while. In the old paradigm, those ideas would be gone — lost in a notes app, buried in a scrolling chat, or simply forgotten.

**The workspace shows you what happened while you were away:**

> 🔄 **"Your seedbed has been growing:"**
>
> 🌱 H1 energy: still 🟢 High · 2 new connections found
> - Connection to S1 (marketplace): "The workspace could BE the marketplace"
> - Connection to S8 (new seed from last week): "Curriculum-as-product model"
>
> 🧬 **New mutation suggested:** S5a → S5b: "Neurodivergent-by-design, not just ADHD"
> → This broadens the market and aligns with universal design principles
>
> 🔗 **New connection discovered by Muse:** S4 (Swarm curriculum) and S11 (agent design principles) share the theme "teaching through doing"
>
> 📊 **Seedbed health:** 23 seeds · 5 sprouts · 3 hybrids · 4 connections added since last visit

**Nothing is lost. Nothing is "overdue." Seeds don't expire.** They either grow or they stay dormant, waiting for the right connection. (Shame-Free. Visibility as Memory. Change Detection. Replanning as Normal.)

**One clear next step:**

> 💡 **"H1 has a new connection to S1 that reframes it as a marketplace, not just a workspace. Explore this?"**

(OCNS. Engagement Over Priority. The workspace surfaces the most interesting change, not the most "important" task.)

---

## How This Flow Differs From Writing and Strategy

| Dimension | Written Content | Strategy Development | Creative Exploration |
|---|---|---|---|
| **Artefact** | Structured argument | Strategy lattice | **Idea seedbed** |
| **Artefact shape** | Linear → rendered | Lattice → decided | **Constellation → grown** |
| **Primary types** | Claims, evidence, questions | Assumptions, options, decisions | **Seeds, connections, hybrids, mutations** |
| **Primary operation** | Extract, Rearrange, Transform | Compare, Adjust, Stress-Test | **Connect, Combine, Mutate** |
| **Agent role** | Structurer | Mirror, Judgment Preparer | **Muse** |
| **Temporal mode** | Episodic → Iterative | Iterative → Ongoing | **Bursty → Ongoing** |
| **Convergence** | Converges toward prose | Converges toward decisions | **Never converges (or graduates to another artefact type)** |
| **Key ADHD challenge** | Wall of text | Invisible assumptions, decision avoidance | **Idea loss, idea isolation, energy drops** |
| **Key ADHD superpower** | Accretive thinking | Visionary connections | **Novelty-seeking, combinatory play** |
| **Confidence × reversibility** | Low confidence + reversible | Low confidence + irreversible | **High confidence + high reversibility (ideas are cheap)** |
| **What "done" means** | Published | Never done — evolving | **Seeds graduate, seedbed is never done** |

---

## What's the Same: The Underlying Pattern (Again)

```
CAPTURE ──→ TYPE ──→ CONNECT ──→ ARRANGE ──→ DEVELOP ──→ RENDER
   │           │         │          │           │           │
   │           │         │          │           │           └→ Seed sketches
   │           │         │          │           └→ Germinate, not generate
   │           │         │          └→ Constellation, not matrix
   │           │         └→ Muse suggests connections + breeds hybrids
   │           └→ System infers type (seed, connection, mutation)
   │              + captures energy level at moment of creation
   └→ Any modality, any fragment, zero context required
       + ENERGY tagging (how excited are you about this idea?)
```

**The pattern holds.** Capture → Type → Connect → Arrange → Develop → Render.

But the *weight* shifts:
- **Capture** is even more critical — ideas arrive faster and leave faster in creative mode. ZFC is paramount.
- **Connect** becomes the dominant operation, not Arrange. Ideas don't need to be ordered; they need to be *linked*.
- **Arrange** is looser — a constellation, not a skeleton or lattice. No single "right" arrangement.
- **Develop** is lighter — a germination, not a full development. Just enough structure to evaluate.
- **Render** produces seed sketches, not finished prose or decisions.

---

## The Key Insights From This Use Case

### Insight 1: Energy Is a First-Class Type

In writing, confidence is a first-class type (how sure are we about this claim?). In strategy, confidence is also critical (how confident are we in this assumption?).

In creative exploration, **energy** is the first-class type. Not "how confident am I?" but **"how excited am I about this idea?"** The workspace captures energy at the moment of creation — not retroactively.

This is Engagement Over Priority made structural. The seedbed doesn't sort by importance. It sorts by energy. The ideas that excite you are the ideas worth developing. For ADHD brains, energy IS the access point. If you're not interested, you can't engage. If you can't engage, you can't develop.

**Energy as a first-class type** means:
- Seeds are captured with an energy level (🟢 High, 🟡 Medium, 🔴 Low)
- The Muse agent surfaces high-energy seeds first
- Connections between high-energy seeds are highlighted
- Hybrids inherit energy from their parents
- The "next step" always follows energy, not priority

### Insight 2: The Agent Role Shifts With the Use Case

| Use Case | Agent Role | Primary Function |
|---|---|---|
| Written Content | **Structurer** | Organise fragments into a coherent skeleton |
| Strategy | **Mirror + Judgment Preparer** | Surface hidden assumptions; present decisions clearly |
| Creative Exploration | **Muse** | Suggest connections, breed hybrids, propose mutations, keep energy flowing |

The Muse agent doesn't evaluate. It doesn't say "this idea is good" or "this idea is bad." It doesn't converge. It **diverges productively** — showing you connections you might not see, breeding combinations you might not think of, proposing mutations that keep the creative energy flowing.

The Muse's behaviors:
- **Connect**: "These two seeds share a theme. Want to link them?"
- **Breed**: "Seed A + Seed B might produce this offspring. Explore?"
- **Mutate**: "What if we changed this one thing about Seed C?"
- **Surface**: "Seed D has been quiet for 3 weeks, but it just got a new connection. Look?"
- **Energize**: "Your last 4 seeds all mention 'neurodivergent.' This might be a theme worth developing."

The Muse NEVER says: "You should prioritise this." "This idea is better than that one." "You're working on too many things." Those are priority-based judgments, and in creative exploration, priority is the wrong frame. Engagement is the right frame. (Engagement Over Priority.)

### Insight 3: Creative Artefacts Graduate, They Don't Finish

Writing has a finish line (publication). Strategy has decision points (commit to an option). Creative exploration has neither. Ideas don't "finish." They **graduate** — they become something else.

A seed graduates into:
- A strategy lattice (when it's ready for strategic evaluation)
- A written content argument skeleton (when it's ready to be articulated)
- A product spec (when it's ready to be built)
- Another seed in a different seedbed (when it connects to a different domain)

The seedbed is a **feeder system** for the other artefact types. Creative exploration feeds strategy, which feeds writing, which feeds creative exploration again. It's a cycle, not a pipeline.

### Insight 4: ADHD Traits Are Context-Dependent, Not Universal

This is the most important meta-insight from comparing the three use cases:

> **The same ADHD trait — novelty-seeking — is a CHALLENGE in strategy work and a SUPERPOWER in creative work.**

In strategy, novelty-seeking = shiny idea chasing = distraction from decisions. The workspace must **contain** it (branch, don't restart).

In creative exploration, novelty-seeking = combinatory play = the source of all creativity. The workspace must **amplify** it (breed, mutate, connect).

This means **the workspace must adapt its behaviour based on the use case** — not just its layout or its types, but its fundamental stance toward the human's ADHD traits. In strategy mode, it's a Mirror that helps you see your own assumptions. In creative mode, it's a Muse that amplifies your divergent thinking. Same brain. Same traits. Different context. Different workspace behaviour.

---

## The Three Use Cases Compared

| Dimension | Written Content | Strategy | Creative Exploration |
|---|---|---|---|
| **Artefact** | Argument skeleton | Strategy lattice | Idea seedbed |
| **Primary types** | Claims, evidence, questions | Assumptions, options, decisions | Seeds, connections, hybrids, energy |
| **Primary flow** | Capture → Arrange → Develop | Capture → Compare → Decide | **Capture → Connect → Combine → Mutate** |
| **Agent role** | Structurer | Mirror + Judgment Preparer | **Muse** |
| **Agent stance** | "Let me organise this" | "Let me show you what you're assuming" | **"Let me show you what you're not seeing"** |
| **ADHD trait** | Accretive thinking | Visionary connections | **Novelty-seeking** |
| **Workspace stance** | Support accretion | Contain divergence | **Amplify divergence** |
| **Energy tracking** | Implicit | Not primary | **First-class type** |
| **Confidence tracking** | Medium (claims) | Critical (assumptions) | **Low (ideas are cheap)** |
| **What "done" means** | Published | Never done | **Graduated** |
| **Shame trigger** | Not finishing | Not deciding | **Not capturing** |
| **Key operation** | Rearrange | Stress-Test | **Combine** |
| **Key principle** | Visibility as Memory | Judgment Preparation | **Engagement Over Priority** |

---

## The Universal Pattern, Stress-Tested Three Times

The same underlying flow works for all three use cases:

```
CAPTURE ──→ TYPE ──→ CONNECT ──→ ARRANGE ──→ DEVELOP ──→ RENDER
```

But the **weight**, **stance**, and **primary operation** shifts based on what the human brain needs:

- **Writing** needs **structure** → Arranging the skeleton is the primary act → Agent is Structurer
- **Strategy** needs **visibility** → Seeing assumptions and dependencies is the primary act → Agent is Mirror
- **Creative** needs **energy** → Connecting and combining ideas is the primary act → Agent is Muse

The 12 ADHD principles apply to all three, but different principles are dominant:

- **Writing**: Visibility as Memory, Cognitive Load Budget, Zero-Friction Capture
- **Strategy**: One Clear Next Step, Shame-Free Failure States, Predictability as Safety
- **Creative**: Engagement Over Priority, Zero-Friction Capture, Replanning as Normal

The type system applies to all three, but different types are first-class:

- **Writing**: Claims, Evidence, Questions
- **Strategy**: Assumptions, Options, Dependencies, Confidence
- **Creative**: Seeds, Connections, Energy, Mutations

The Confidence × Reversibility matrix applies to all three, but the quadrant differs:

- **Writing**: Low confidence + reversible → Agent generates, human edits
- **Strategy**: Low confidence + irreversible → Agent prepares, human decides
- **Creative**: High confidence + reversible → Agent suggests, human explores

---

The pattern holds. The specifics shift. The workspace adapts.

Ready to synthesise all three use cases into a concrete interaction paradigm?

---

## Run 7 — AI UX Innovator ✓ COMPLETED

*2026-04-14T04:04:01* · `glm-5.1:cloud` · `33f28c6a...`

### Prompt

ok. synthesise to concrete interaction paradigm

### Response

# The Accretive Workspace: A Concrete Interaction Paradigm

---

## 0. What This Is

This is not a feature list. This is a **coherent model of how human, agent, and artefact relate** — the rules of engagement, the spatial layout, the type system, the governance, and the adaptation. Everything flows from seven first principles.

---

## I. The Seven First Principles

These are non-negotiable. Every design decision is evaluated against them.

| # | Principle | Source |
|---|---|---|
| **P1** | **The artefact is primary. The conversation serves it.** | Use case analysis |
| **P2** | **Everything is a typed fragment. Nothing is undifferentiated prose.** | Type collision insight (Shannon) |
| **P3** | **The agent prepares judgment. The human makes judgment.** | Confidence × Reversibility governance |
| **P4** | **Capture is zero-friction. Structure comes after.** | ADHD: ZFC + Accretive model |
| **P5** | **One clear next step, always.** | ADHD: OCNS + Cognitive Load Budget |
| **P6** | **The workspace adapts to the work, not the other way around.** | Domain-adaptive agent roles |
| **P7** | **Nothing is lost. Everything evolves.** | ADHD: Visibility + Shame-Free + Replanning |

---

## II. The Core Model: Fragments, Edges, Shapes

### The Fragment

Every piece of information in the workspace is a **fragment** — a typed, connected, manipulable object.

```
┌─────────────────────────────────────────────────────────────┐
│  FRAGMENT                                                    │
│                                                              │
│  id:           f-8472                                       │
│  type:         ⚠️ ASSUMPTION                               │
│  content:      "Enterprises will pay premium for agentic    │
│                AI skills"                                    │
│  energy:       🟡 Medium  (captured at moment of creation)  │
│  confidence:   🔴 Low                                      │
│  provenance:   "Intuition · Added Mar 15 · Late-night session"│
│  artefact:     "Future's Edge GTM Strategy"                 │
│  created:      2025-03-15T23:42:00                          │
│  last_evolved: 2025-03-18T09:15:00                          │
│                                                              │
│  ── EDGES ─────────────────────────────────────────────────  │
│  → f-8473  DEPENDS_ON    "A1: market growth"                │
│  → f-8475  SUPPORTS      "O1: enterprise path"             │
│  ← f-8480  CHALLENGED_BY "Q3: is 17 the right number?"     │
│  ← f-8491  EVIDENCE_FOR  "E2: 3 enterprise conversations"  │
│                                                              │
│  ── RENDERINGS ──────────────────────────────────────────   │
│  (none — prose not yet generated for this fragment)          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The Edge

Every connection between fragments is an **edge** — a typed, directed relationship.

```
┌──────────────────────────────────────────────────┐
│  EDGE                                             │
│                                                   │
│  from:    f-8472 (Assumption: enterprise premium)  │
│  to:      f-8475 (Option: enterprise path)        │
│  type:    SUPPORTS                                │
│  strength: Strong (system-inferred, user-confirmed)│
│  created: 2025-03-15T23:42:30                     │
│                                                   │
│  EDGE TYPES (unified across all shapes):           │
│  ─────────────────────────────────────────────────  │
│  SUPPORTS        ·  This fragment supports that    │
│  CHALLENGES      ·  This fragment challenges that  │
│  DEPENDS_ON      ·  This fragment needs that       │
│  BREEDS_FROM     ·  This fragment was bred from    │
│  MUTATES_FROM    ·  This fragment mutated from     │
│  RELATES_TO      ·  General connection              │
│  ANSWERS         ·  This fragment answers that      │
│  IMPLIES         ·  This fragment implies that      │
│  CONTRADICTS     ·  This fragment contradicts that  │
│                                                   │
└──────────────────────────────────────────────────┘
```

### The Shape

Every artefact has a **shape** — a domain-specific configuration that determines how fragments are displayed, what operations are primary, and how the agent behaves.

```
┌──────────────────────────────────────────────────────────────┐
│  SHAPE                                                        │
│                                                               │
│  Three shapes, validated across three use cases:              │
│                                                               │
│  ┌─── ARGUMENT ─────────────────────────────────────────────┐ │
│  │  Domain: Written content production                      │ │
│  │  Primary types: Claim, Evidence, Question, Phrase        │ │
│  │  Primary ops:  Rearrange, Extract, Transform, Develop   │ │
│  │  Agent role:   STRUCTURER                                │ │
│  │  Layout:       Vertical skeleton with depth drill-down   │ │
│  │  Renderings:   Blog, Report, Thread, Deck, Abstract      │ │
│  │  Key metric:  Coverage (all claims supported?)            │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌─── LATTICE ──────────────────────────────────────────────┐ │
│  │  Domain: Strategy development                            │ │
│  │  Primary types: Assumption, Option, Decision, Scenario    │ │
│  │  Primary ops:  Compare, Adjust, Stress-Test, Track       │ │
│  │  Agent role:   MIRROR + JUDGMENT PREPARER                │ │
│  │  Layout:       Dependency graph with comparison panels    │ │
│  │  Renderings:   Strategy doc, Decision card, Scenario map  │ │
│  │  Key metric:  Decision readiness (all decisions prepared?) │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌─── SEEDBED ──────────────────────────────────────────────┐ │
│  │  Domain: Creative exploration & ideation                 │ │
│  │  Primary types: Seed, Hybrid, Mutation, Connection        │ │
│  │  Primary ops:  Connect, Combine, Mutate, Branch           │ │
│  │  Agent role:   MUSE                                       │ │
│  │  Layout:       Constellation with energy glow             │ │
│  │  Renderings:   Seed sketches, idea briefs, concept cards  │ │
│  │  Key metric:  Energy (which seeds have highest charge?)    │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                               │
│  Shapes TRANSITION:                                           │
│  Seedbed → Lattice (seed graduates into strategy)             │
│  Lattice → Argument (strategy produces content)               │
│  Argument → Seedbed (content sparks new ideas)                │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## III. The Unified Type System

All 18 fragment types exist in one type registry. Every shape uses a subset as primary, but all types are available everywhere.

```
┌─────────────────────────────────────────────────────────────────┐
│  FRAGMENT TYPE REGISTRY                                          │
│                                                                  │
│  CORE TYPES (available in all shapes)                             │
│  ────────────────────────────────────────────                     │
│  🔵  CLAIM       ·  An assertion that may be true or false       │
│  🟢  EVIDENCE    ·  Data, research, or observation supporting X  │
│  ⚠️  ASSUMPTION  ·  Something taken as true without proof       │
│  🟡  OPTION      ·  A possible path or alternative               │
│  🔴  QUESTION    ·  Something not yet answered                   │
│  🟣  PERSPECTIVE ·  A different way of seeing the same thing     │
│  🔗  CONNECTION  ·  A relationship between other fragments       │
│  🚧  CONSTRAINT  ·  A boundary on what's possible               │
│  📊  PATTERN     ·  A recurring structure or behaviour           │
│  🔍  GAP         ·  What's missing                               │
│  ⚡  TENSION     ·  Where things conflict                        │
│  ➡️  DEPENDENCY  ·  What depends on what                         │
│  📋  CRITERIA    ·  A standard for evaluation                    │
│  ✅  OUTCOME     ·  What happened as a result                    │
│  🎯  ACTION      ·  Something to do                              │
│  📎  PROVENANCE  ·  Where this came from                         │
│                                                                  │
│  SHAPE-SPECIFIC TYPES                                            │
│  ────────────────────────────────────────────                     │
│  ARGUMENT-only:  💬 PHRASE · A quotable/extractable expression   │
│  LATTICE-only:   📐 SCENARIO · A "what if" configuration         │
│                  🚦 DECISION · A judgment point requiring action  │
│  SEEDBED-only:   💡 SEED · An idea with energy and genealogy    │
│                  🔀 HYBRID · Bred from 2+ parent seeds           │
│                  🧬 MUTATION · A variant of an existing seed     │
│                                                                  │
│  METADATA (attached to every fragment, every shape)               │
│  ────────────────────────────────────────────                     │
│  energy:      🟢 High · 🟡 Medium · 🔴 Low · ⚪ Not applicable  │
│  confidence:  🟢 High · 🟡 Medium · 🔴 Low · ⚪ Not applicable  │
│  reversibility: 🟢 Reversible · 🟡 Partial · 🔴 Irreversible   │
│  provenance:  "Source · When · Context"                           │
│  status:      🟢 Active · 🟡 Dormant · 🔴 Challenged            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**This is type collision resolution at the data layer.** The 17+ types that LLMs encode as prose are now first-class, queryable, typed objects. The Shannon problem is solved structurally: each type has its own channel.

---

## IV. The Spatial Model

The workspace has a **fixed spatial grammar** that adapts to shape but never reorganises. Predictability as Safety.

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  ┌─── LEFT RAIL ───┐  ┌─── CANVAS ──────────────────────┐      │
│  │                  │  │                                  │      │
│  │  📁 ARTEFACTS    │  │                                  │      │
│  │   ├─ Strategy    │  │     THE ARTEFACT LIVES HERE      │      │
│  │   ├─ Workspace   │  │                                  │      │
│  │   └─ Seedbed     │  │     Fragments, arranged by      │      │
│  │                  │  │     shape-specific layout        │      │
│  │  🕐 EVOLUTION    │  │                                  │      │
│  │   What changed   │  │     Argument: vertical skeleton  │      │
│  │   since last     │  │     Lattice: dependency graph   │      │
│  │   visit          │  │     Seedbed: energy constellation │      │
│  │                  │  │                                  │      │
│  │  🧭 SHAPE        │  │                                  │      │
│  │   Current shape  │  │                                  │      │
│  │   + transition   │  │                                  │      │
│  │   options        │  │                                  │      │
│  │                  │  │                                  │      │
│  └──────────────────┘  └──────────────────────────────────┘      │
│                                                                  │
│  ┌─── RIGHT RAIL ────────────────────────────────────────────┐  │
│  │                                                            │  │
│  │  🤖 AGENT CHANNEL                                          │  │
│  │   ──────────────────────────────────────                    │  │
│  │   Typed outputs, NOT prose.                                │  │
│  │   Each agent contribution is a fragment.                    │  │
│  │                                                            │  │
│  │   💡 "This assumption connects to O1."                     │  │
│  │   ⚠️ "A4 has low confidence. Want to stress-test?"          │  │
│  │   🧬 "S3 + S5 could produce a hybrid. Breed?"              │  │
│  │                                                            │  │
│  │   Agent role adapts to shape:                               │  │
│  │   Argument → STRUCTURER                                    │  │
│  │   Lattice  → MIRROR + JUDGMENT PREPARER                    │  │
│  │   Seedbed  → MUSE                                          │  │
│  │                                                            │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌─── BOTTOM BAR ──────────────────────────────────────────────┐
│  │                                                              │
│  │  ⚡ CAPTURE: [Type or drop anything here]                    │
│  │                                                              │
│  │  💡 NEXT STEP: "A4 has low confidence. [Stress-test] [Add    │
│  │     evidence] [Compare O1 vs O2]"                           │
│  │                                                              │
│  └──────────────────────────────────────────────────────────────┘
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### The Five Zones, Explained

| Zone | Position | Purpose | ADHD Principle |
|---|---|---|---|
| **Left Rail** | Fixed left | Artefact list, evolution feed, shape selector | Visibility as Memory, Predictability |
| **Canvas** | Centre, dominant | The artefact itself — fragments arranged by shape | Cognitive Load Budget, Visibility |
| **Right Rail** | Fixed right | Agent contributions — typed fragments, not prose | Judgment Preparation, Type Collision |
| **Capture Bar** | Fixed bottom | Zero-friction input — type, paste, voice, drag | ZFC, Multi-Modal |
| **Next Step** | Fixed bottom-right | One clear action, always | OCNS, Cognitive Load Budget |

**The canvas is the primary interface.** Not the agent channel. Not the capture bar. The artefact. The agent channel and capture bar are servants. The artefact is master. (P1: The artefact is primary.)

**The layout never reorganises.** Left rail is always artefacts. Right rail is always agent. Bottom is always capture + next step. Centre is always the artefact. Predictability as Safety — the human always knows where to look.

**The canvas adapts to shape.** An argument shows a vertical skeleton. A lattice shows a dependency graph. A seedbed shows an energy constellation. But the zones never move.

---

## V. The Flow Engine

The universal pattern `capture → type → connect → arrange → develop → render` is always present. But the **emphasis** and **primary operations** shift by shape.

```
┌──────────────────────────────────────────────────────────────────────┐
│  FLOW ENGINE                                                         │
│                                                                      │
│  ┌─── UNIVERSAL (always active) ───────────────────────────────────┐ │
│  │                                                                  │ │
│  │  CAPTURE ──→ TYPE ──→ CONNECT ──→ ARRANGE ──→ DEVELOP ──→ RENDER│ │
│  │                                                                  │ │
│  │  Every interaction follows this sequence. The system             │ │
│  │  types after capture, connects after typing, and                │ │
│  │  suggests the next step based on where the artefact             │ │
│  │  is in the sequence.                                            │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─── SHAPE EMPHASIS (which steps are most active) ───────────────┐ │
│  │                                                                  │ │
│  │                  CAPTURE  TYPE  CONNECT  ARRANGE  DEVELOP RENDER│ │
│  │  ARGUMENT:         ●      ●      ○       ●●      ●●     ●●   │ │
│  │  LATTICE:          ●      ●      ●       ○       ●●     ●     │ │
│  │  SEEDBED:          ●●     ●      ●●      ○       ●      ○     │ │
│  │                                                                  │ │
│  │  ●● = dominant   ● = active   ○ = background                   │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─── SHAPE PRIMARY OPERATIONS ────────────────────────────────────┐ │
│  │                                                                  │ │
│  │  ARGUMENT:  Rearrange · Extract · Transform · Develop prose    │ │
│  │  LATTICE:   Compare · Adjust · Stress-Test · Track · Decide    │ │
│  │  SEEDBED:   Connect · Combine · Mutate · Branch · Graduate     │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### How Capture → Type → Connect works (universal)

1. **CAPTURE**: Human types, pastes, speaks, or drags into the capture bar. Zero context required. Zero modality forced.

2. **TYPE**: System infers fragment type. Presents inference with confidence. Human confirms or corrects in one click. This is Mirror — the system reflects its understanding back. If uncertain, the system asks a clarifying question — one question, not seven.

3. **CONNECT**: System finds potential edges to existing fragments. Presents top 3 connections. Human confirms, rejects, or adds. One click per connection.

### How Arrange → Develop → Render works (shape-specific)

**ARGUMENT:**
- Arrange → Drag fragments into skeleton order. Claims at top, evidence below, questions on the side.
- Develop → Generate prose per-claim from connected evidence. Not the whole document — one claim at a time.
- Render → Choose audience, tone, medium. Generate full rendering from skeleton. Multiple renderings from one skeleton.

**LATTICE:**
- Arrange → View as dependency graph. Options and assumptions automatically positioned.
- Develop → Stress-test assumptions. Compare options. Build scenarios. Present decision cards.
- Render → Generate strategy doc, scenario map, or decision summary. Always with confidence/reversibility visible.

**SEEDBED:**
- Arrange → View as energy constellation. High-energy seeds glow brighter. Connections visible as gravitational links.
- Develop → Breed hybrids. Propose mutations. Germinate seed sketches.
- Render → Generate seed sketch, concept card, or idea brief. Light renderings — enough to evaluate, not enough to overwhelm.

---

## VI. The Agent Model

### Three Roles, One Agent System

The agent role shifts automatically based on the artefact's shape. The human never selects a role. The role emerges from the work.

```
┌──────────────────────────────────────────────────────────────────────┐
│  AGENT ROLE MATRIX                                                   │
│                                                                      │
│  ┌─── STRUCTURER (ARGUMENT shape) ─────────────────────────────────┐ │
│  │                                                                  │ │
│  │  Stance: "Let me organise this for you"                         │ │
│  │                                                                  │ │
│  │  Behaviours:                                                     │ │
│  │  • Types captured fragments → presents inference for confirmation│ │
│  │  • Suggests skeleton arrangement based on fragment relationships │ │
│  │  • Generates prose per-claim when requested                     │ │
│  │  • Flags unsupported claims and unanswered questions             │ │
│  │  • Offers multiple renderings (audience, tone, medium)           │ │
│  │                                                                  │ │
│  │  Never: Judges the argument · Makes truth claims · Selects      │ │
│  │         rendering without asking · Overwrites human edits        │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─── MIRROR (LATTICE shape) ──────────────────────────────────────┐ │
│  │                                                                  │ │
│  │  Stance: "Let me show you what you're assuming"                 │ │
│  │                                                                  │ │
│  │  Behaviours:                                                     │ │
│  │  • Surfaces assumptions with confidence levels and dependencies │ │
│  │  • Flags low-confidence assumptions supporting high-stakes       │ │
│  │    options (C×R governor activation)                            │ │
│  │  • Prepares decision cards with options, evidence, and gaps      │ │
│  │  • Runs stress-tests on request (cascade: if A fails → what?)   │ │
│  │  • Tracks changes across sessions → "what changed since last"   │ │
│  │                                                                  │ │
│  │  Never: Makes decisions · Recommends one option · Hides          │ │
│  │         low-confidence assumptions · Judges strategy quality     │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─── MUSE (SEEDBED shape) ────────────────────────────────────────┐ │
│  │                                                                  │ │
│  │  Stance: "Let me show you what you're not seeing"               │ │
│  │                                                                  │ │
│  │  Behaviours:                                                     │ │
│  │  • Surfaces connections between seeds (pattern detection)        │ │
│  │  • Proposes hybrids: "S3 × S5 might produce..."                 │ │
│  │  • Suggests mutations: "What if we changed this one thing?"      │ │
│  │  • Tracks energy patterns: "Your last 4 seeds mention X"        │ │
│  │  • Suggests graduation: "H1 has enough energy to become a       │ │
│  │    lattice. Graduate it?"                                        │ │
│  │                                                                  │ │
│  │  Never: Evaluates ideas · Sorts by priority · Says "too many    │ │
│  │         ideas" · Suppresses divergence · Converges prematurely   │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  UNIVERSAL AGENT BEHAVIOURS (all shapes):                            │
│  ──────────────────────────────────────────────                       │
│  • Every agent output is a TYPED FRAGMENT, not prose                 │
│  • Agent never generates walls of text                               │
│  • Agent presents one clear next step, not menus                     │
│  • Agent frames changes as evolution, not failure                    │
│  • Agent respects C×R governor for every suggested action             │
│  • Agent never makes irreversible decisions                          │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### The Confidence × Reversibility Governor

The C×R matrix is always active but the human never sees it explicitly. It governs **what the agent does autonomously vs. what it prepares for human judgment**.

```
┌──────────────────────────────────────────────────────────────────┐
│  C×R GOVERNOR (invisible to human, structurally enforced)         │
│                                                                   │
│                    REVERSIBLE           IRREVERSIBLE               │
│              ┌──────────────────┬──────────────────────┐           │
│  HIGH        │  AGENT ACTS     │  AGENT RECOMMENDS    │           │
│  CONFIDENCE  │  human reviews  │  human confirms      │           │
│              │  later          │  (one click)          │           │
│              ├──────────────────┼──────────────────────┤           │
│  LOW         │  AGENT TRIES    │  AGENT PREPARES      │           │
│  CONFIDENCE  │  human sees     │  HUMAN DECIDES       │           │
│              │  result          │  (full judgment)     │           │
│              └──────────────────┴──────────────────────┘           │
│                                                                   │
│  Examples by shape:                                               │
│  ──────────────────                                                │
│  ARGUMENT:                                                        │
│    Auto-type a fragment (high conf + reversible)                  │
│    vs. Choose rendering order (low conf + irreversible-ish)       │
│                                                                   │
│  LATTICE:                                                         │
│    Auto-connect fragments (high conf + reversible)                │
│    vs. Make strategic decision (low conf + irreversible)         │
│                                                                   │
│  SEEDBED:                                                         │
│    Auto-breed seeds (high conf + reversible)                      │
│    vs. Graduate seed to lattice (low conf + irreversible-ish)    │
│                                                                   │
│  The governor is the AUTOMATIC ENFORCEMENT of P3:                 │
│  "The agent prepares judgment. The human makes judgment."         │
│  It operates silently, shaping agent autonomy per action.         │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## VII. The Transition Model

Artefacts don't live in isolation. They **transition** between shapes as the work evolves.

```
┌──────────────────────────────────────────────────────────────────────┐
│  TRANSITION MAP                                                       │
│                                                                       │
│                     ┌─────────────┐                                   │
│          graduate   │             │   produces                         │
│     ┌───────────────┤   SEEDBED   ├──────────────┐                    │
│     │               │  (creative) │               │                    │
│     │               └──────┬──────┘               │                    │
│     │                      │                       │                    │
│     │                reseed│                  ┌────▼─────┐              │
│     │                      │            feeds │          │              │
│     │               ┌──────▼──────┐    ┌────── ARGUMENT │              │
│     │    stress-test│             │    │      │ (content) │              │
│     │  ┌────────────┤   LATTICE   ├───►│      └──────────┘              │
│     │  │            │  (strategy) │    │                                │
│     │  │            └─────────────┘    │  content sparks                │
│     │  │                               │  new ideas → reseed            │
│     │  │          lattice informs      │                                │
│     │  │          decision →           │                                │
│     │  │                                │                                │
│     │  ▼                                ▼                                │
│  ┌──────────────────────────────────────────┐                          │
│  │                                          │                          │
│  │  CROSS-ARTEFACT FLOW                     │                          │
│  │  Fragments can be linked across          │                          │
│  │  artefacts. An assumption in one         │                          │
│  │  strategy can support a claim in         │                          │
│  │  another argument. A seed in one         │                          │
│  │  seedbed can graduate into a different   │                          │
│  │  artefact's lattice.                     │                          │
│  │                                          │                          │
│  │  The workspace is not a collection       │                          │
│  │  of isolated artefacts. It's an          │                          │
│  │  ECOSYSTEM of connected fragments.        │                          │
│  │                                          │                          │
│  └──────────────────────────────────────────┘                          │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

### Transition Rules

| Transition | Trigger | What Happens |
|---|---|---|
| **Seed → Lattice** (graduate) | Seed has high energy + enough development + human confirms | Seed becomes an assumption or option in a new/existing lattice. Genealogy preserved. |
| **Lattice → Argument** (produce) | Decision made + needs articulation | Decision becomes a claim. Supporting evidence becomes evidence. Assumptions become acknowledged assumptions. |
| **Argument → Seed** (reseed) | Writing sparks a new idea | New idea captured as seed in seedbed. Link to originating fragment preserved. |
| **Lattice → Seed** (reseed) | Strategy sparks a new possibility | New possibility captured as seed. "Where did this come from?" is traceable. |

**Transitions are never destructive.** The original artefact is preserved. The new artefact is a projection of specific fragments into a new shape. The fragments persist in both. This is P7: Nothing is lost. Everything evolves.

---

## VIII. The ADHD Infrastructure

The 12 principles aren't features. They're **structural properties** of the interaction model. They're enforced by the architecture, not optional settings.

```
┌──────────────────────────────────────────────────────────────────────┐
│  ADHD INFRASTRUCTURE — BAKED IN, NOT BOLTED ON                       │
│                                                                       │
│  ┌─── PRINCIPLE ────────────── ─── HOW IT'S STRUCTURAL ───────────┐ │
│  │                                                                  │ │
│  │  COGNITIVE LOAD BUDGET                                          │ │
│  │  ──────────────────────                                         │ │
│  │  • Typed fragments eliminate type inference while reading         │ │
│  │  • Canvas shows ONE shape at a time (not all fragments)          │ │
│  │  • Agent presents ONE next step (not a menu)                    │ │
│  │  • Drill-down is opt-in (depth on demand, not by default)        │ │
│  │  • Shape-appropriate layouts reduce visual scanning              │ │
│  │                                                                  │ │
│  │  VISIBILITY AS MEMORY                                           │ │
│  │  ──────────────────                                             │ │
│  │  • Artefacts persist in left rail (never scrolled away)          │ │
│  │  • Evolution feed shows what changed (no reconstruction)         │ │
│  │  • Fragment types are visually coded (colour + icon)             │ │
│  │  • Edges are visible (relationships don't live in working memory)│ │
│  │  • Spatial layout IS memory (where things are = what they are)   │ │
│  │                                                                  │ │
│  │  ONE CLEAR NEXT STEP ALWAYS                                     │ │
│  │  ─────────────────────────                                      │ │
│  │  • Bottom-right always shows ONE action                         │ │
│  │  • Agent channel presents ONE suggestion at a time              │ │
│  │  • Decision cards present ONE decision at a time                │ │
│  │  • Never: menus of 5+ options, blank canvases, open-ended prompts│ │
│  │                                                                  │ │
│  │  INTERRUPT ARCHITECTURE                                         │ │
│  │  ────────────────────                                            │ │
│  │  • Exact state persisted on close                               │ │
│  │  • Visual breadcrumb: "You were here" on return                 │ │
│  │  • Evolution feed shows what changed while away                 │ │
│  │  • No "overdue" or "stale" labels — only "evolved"              │ │
│  │  • Capture bar always accessible (even mid-task)                │ │
│  │                                                                  │ │
│  │  ENGAGEMENT OVER PRIORITY                                       │ │
│  │  ──────────────────────                                          │ │
│  │  • Seedbed sorts by energy, not importance                      │ │
│  │  • Next step follows the human's last interest, not a to-do     │ │
│  │  • Agent surfaces connections (interesting) not tasks (priority) │ │
│  │  • Shape transitions follow human energy, not a process plan     │ │
│  │  • "What changed?" not "What's due?"                            │ │
│  │                                                                  │ │
│  │  SHAME-FREE FAILURE STATES                                      │ │
│  │  ──────────────────────────                                      │ │
│  │  • Artefacts "evolve" — never "abandoned" or "overdue"           │ │
│  │  • Branches are explorations — not "wrong turns"                 │ │
│  │  • Dormant seeds are "resting" — not "failed"                   │ │
│  │  • Low-confidence assumptions are "untested" — not "wrong"        │ │
│  │  • Return messages: "Your artefact grew" not "You were away"     │ │
│  │                                                                  │ │
│  │  PREDICTABILITY AS SAFETY                                       │ │
│  │  ──────────────────────                                          │ │
│  │  • Spatial grammar never changes (5 zones, always same place)    │ │
│  │  • Fragment types look the same across all shapes                │ │
│  │  • Operations work the same on all fragment types                │ │
│  │  • Agent role shifts are signalled, not hidden                   │ │
│  │  • Transitions are explicit and human-initiated                  │ │
│  │                                                                  │ │
│  │  ZERO-FRICTION CAPTURE                                          │ │
│  │  ────────────────────                                            │ │
│  │  • Capture bar is ALWAYS visible (fixed bottom)                  │ │
│  │  • One gesture to capture: type, paste, voice, drag               │ │
│  │  • No context required (system infers type after capture)        │ │
│  │  • No modality forced (text, voice, paste all work)              │ │
│  │  • System types it. System connects it. Human confirms.          │ │
│  │                                                                  │ │
│  │  REPLANNING AS NORMAL WORKFLOW                                  │ │
│  │  ──────────────────────────                                      │ │
│  │  • Rearranging the skeleton IS replanning (argument)             │ │
│  │  • Branching an option IS replanning (lattice)                   │ │
│  │  • Mutating a seed IS replanning (seedbed)                      │ │
│  │  • No cost to restructure — fragments are independent objects    │ │
│  │  • Branches, not versions — everything coexists                  │ │
│  │                                                                  │ │
│  │  CUSTOMISATION AS OWNERSHIP                                     │ │
│  │  ──────────────────────────                                      │ │
│  │  • View modes (skeleton, graph, constellation, timeline)         │ │
│  │  • Layout preferences persist per artefact                       │ │
│  │  • Agent learns patterns over time (personalised suggestions)    │ │
│  │  • Custom fragment subtypes for power users                     │ │
│  │  • Shape transitions are human-initiated, not system-forced      │ │
│  │                                                                  │ │
│  │  MULTI-MODAL I/O                                                │ │
│  │  ────────────────                                               │ │
│  │  • Input: text, voice, paste, drag, file import                  │ │
│  │  • Output: skeleton, graph, constellation, timeline, prose       │ │
│  │  • Operations: click, drag, keyboard, voice command              │ │
│  │  • Agent contributions: typed cards, not prose blocks             │ │
│  │  • Renderings: blog, report, thread, deck, map, card             │ │
│  │                                                                  │ │
│  │  COGNITIVE PROSTHETIC NOT MONITOR                                │ │
│  │  ─────────────────────────────────                               │ │
│  │  • Workspace holds structure so you don't have to                 │ │
│  │  • Workspace surfaces changes so you don't miss them             │ │
│  │  • Workspace mirrors your thinking so you can see it             │ │
│  │  • Never: productivity scores, time tracking, task nagging       │ │
│  │  • The workspace EXTENDS your cognition, it doesn't SURVEIL it   │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

## IX. The Input-Output Model

### Input: The Capture → Type → Connect Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│  INPUT PIPELINE                                                      │
│                                                                      │
│  1. CAPTURE                                                          │
│     Human: types, pastes, speaks, drags → capture bar                │
│     System: accepts ANY content, ANY modality                        │
│     Cost: < 3 seconds. Zero context required.                        │
│                                                                      │
│  2. TYPE                                                             │
│     System: infers fragment type + shape context                     │
│     System: presents inference: "🔵 CLAIM?" ← one click to confirm  │
│     Human: confirms or corrects (one click or one word)              │
│     Fallback: if confidence < 0.7, asks one clarifying question      │
│                                                                      │
│  3. CONNECT                                                          │
│     System: finds top 3 potential edges to existing fragments         │
│     System: presents: "🔗 Supports O1?" ← one click to confirm      │
│     Human: confirms, rejects, or adds custom connection               │
│                                                                      │
│  4. NEXT STEP                                                        │
│     System: determines next step based on:                           │
│       - Current shape (argument → arrange, lattice → compare, etc.)  │
│       - Artefact state (what's missing? what's low confidence?)      │
│       - Human's energy (what have they been engaging with?)          │
│     System: presents ONE action: "💡 Stress-test A4?"                │
│     Human: takes action, or ignores and does something else          │
│                                                                      │
│  TOTAL INTERACTION COST: 1 gesture + 2-3 clicks per fragment        │
│  TOTAL TIME: < 10 seconds from capture to connected fragment        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Output: The Render Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│  OUTPUT PIPELINE                                                     │
│                                                                      │
│  Rendering is ALWAYS from fragments, never from scratch.            │
│  The skeleton is primary. The rendering is derived.                   │
│                                                                      │
│  ARGUMENT renderings:                                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                │
│  │  📄 Blog Post │ │  📊 Report   │ │  🧵 Thread   │                │
│  │  tone: conv.  │ │  tone: formal│ │  tone: punchy │                │
│  │  depth: full  │ │  depth: full │ │  depth: key   │                │
│  └──────────────┘ └──────────────┘ └──────────────┘                │
│  ┌──────────────┐ ┌──────────────┐                                  │
│  │  📽️ Deck     │ │  📋 Abstract │                                  │
│  │  tone: visual │ │  tone: tight │                                  │
│  │  depth: key  │ │  depth: skim │                                  │
│  └──────────────┘ └──────────────┘                                  │
│                                                                      │
│  LATTICE renderings:                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                │
│  │  📐 Strategy  │ │  🚦 Decision │ │  🗺️ Scenario │                │
│  │     Doc       │ │     Card     │ │     Map      │                │
│  └──────────────┘ └──────────────┘ └──────────────┘                │
│                                                                      │
│  SEEDBED renderings:                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                │
│  │  💡 Seed     │ │  🃏 Concept  │ │  📝 Idea     │                │
│  │     Sketch   │ │     Card     │ │     Brief    │                │
│  └──────────────┘ └──────────────┘ └──────────────┘                │
│                                                                      │
│  EVERY RENDERING:                                                    │
│  • Is generated FROM fragments, not from scratch                     │
│  • Links back to source fragments (click any part → see its origin)  │
│  • Can be regenerated when the artefact evolves                      │
│  • Carries epistemic metadata (confidence, provenance, status)       │
│  • Is a projection, not the source of truth                          │
│                                                                      │
│  THE FRAGMENTS ARE THE SOURCE OF TRUTH.                              │
│  RENDERINGS ARE DERIVED VIEWS.                                       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## X. The Interaction Rules

These are the **constitutional rules** — the constraints that make the paradigm coherent.

```
┌──────────────────────────────────────────────────────────────────────┐
│  THE 12 INTERACTION RULES                                           │
│                                                                      │
│  1.  THE ARTEFACT IS THE INTERFACE.                                  │
│      The human interacts with the artefact, not the agent.            │
│      The agent contributes TO the artefact.                          │
│                                                                      │
│  2.  EVERY PIECE OF INFORMATION IS A TYPED FRAGMENT.                 │
│      No undifferentiated prose. No "response" type.                   │
│      If the agent generates prose, it's a RENDERING, not a fragment. │
│                                                                      │
│  3.  CAPTURE FIRST, STRUCTURE SECOND.                                │
│      The human never has to decide a type before capturing.          │
│      The system infers. The human confirms.                          │
│                                                                      │
│  4.  ONE NEXT STEP, ALWAYS.                                         │
│      The workspace always shows exactly one suggested action.        │
│      The human can ignore it and do anything else.                   │
│                                                                      │
│  5.  THE AGENT PREPARES. THE HUMAN JUDGES.                          │
│      For every action, the C×R governor determines autonomy.         │
│      Irreversible + low confidence = human decides.                  │
│                                                                      │
│  6.  FRAGMENTS ARE INDEPENDENT.                                     │
│      Any fragment can be moved, deleted, or rearranged               │
│      without affecting other fragments.                              │
│                                                                      │
│  7.  CONNECTIONS ARE EXPLICIT.                                       │
│      No implicit dependencies. No "you should know" edges.           │
│      Every relationship is a typed edge the human can see.           │
│                                                                      │
│  8.  BRANCHES, NOT VERSIONS.                                        │
│      When two paths diverge, both exist.                             │
│      No "overwrite." No "replace." No "undo" needed.                 │
│                                                                      │
│  9.  CHANGE IS GROWTH.                                              │
│      "Your artefact evolved" not "You haven't been here."            │
│      Dormant fragments are "resting" not "abandoned."                │
│                                                                      │
│  10. THE SHAPE SERVES THE WORK.                                     │
│      The human doesn't choose a shape and then work.                  │
│      The human works and the shape emerges.                           │
│      Graduation is suggested, not forced.                            │
│                                                                      │
│  11. EVERY FRAGMENT HAS PROVENANCE.                                 │
│      Who created it. When. From what.                                │
│      Human-created vs. agent-suggested is always visible.             │
│      Genealogy (breeding, mutation) is always traceable.             │
│                                                                      │
│  12. THE WORKSPACE EXTENDS, NOT SURVEILS.                           │
│      No productivity scores. No time tracking. No nagging.            │
│      The workspace holds structure so you don't have to.              │
│      It surfaces what you'd miss. It mirrors what you'd lose.         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## XI. What This Paradigm Replaces

| Current Paradigm | Accretive Workspace |
|---|---|
| **Conversation-centric** | **Artefact-centric** |
| **One type: prose** | **18 typed fragment types** |
| **One channel: text** | **Multi-channel: typed fragments + edges** |
| **One agent role: oracle** | **Three agent roles: Structurer, Mirror, Muse** |
| **Stateless** | **Stateful (artefacts persist and evolve)** |
| **Linear: prompt → response** | **Accretive: capture → type → connect → arrange → develop → render** |
| **All-or-nothing** | **Branches coexist** |
| **Change is invisible** | **"What changed?" is primary output** |
| **Human reads walls of text** | **Human makes judgments at decision points** |
| **ADHD = accessibility add-on** | **ADHD = structural design constraint** |
| **Tool you pick up and put down** | **Environment you inhabit** |
| **Chat IS the product** | **Chat doesn't exist. The artefact is the product.** |

---

## XII. What To Build First

The paradigm is complete. The question is: what's the **minimum viable artefact** that validates the core hypotheses?

### Hypotheses to Test

| # | Hypothesis | Validation |
|---|---|---|
| **H1** | Typed fragments > undifferentiated prose for comprehension | Can users find specific information faster in a typed artefact vs. a prose output? |
| **H2** | Capture → Type → Connect reduces capture friction vs. current tools | Do users capture more fragments with less effort? |
| **H3** | Shape-adaptive agent roles improve output relevance | Do Structurer/Mirror/Muse outputs feel more useful than generic oracle outputs? |
| **H4** | One Clear Next Step reduces decision paralysis vs. open-ended prompting | Do users take action faster with OCNS vs. a blank prompt? |
| **H5** | C×R governor increases trust vs. autonomous agent action | Do users trust agent actions more when reversibility is visible? |
| **H6** | Cross-artefact transitions create emergent value | Does graduating a seed into a lattice produce insights neither shape would have alone? |

### Minimum Viable Artefact

**Pick ONE shape. ONE use case. Validate H1-H5.**

Recommended: **The Argument shape** (written content production).

Why:
- Simplest type system (claims, evidence, questions, phrases)
- Simplest flow (capture → arrange → develop → render)
- Clearest agent role (Structurer)
- Most directly comparable to existing tools (writing assistants)
- Fastest to build a testable prototype
- Addresses the user's core frustration (wall of text) most directly

**Build:**
1. Fragment data model (type, content, metadata, edges)
2. Capture → Type → Connect pipeline
3. Argument canvas (vertical skeleton)
4. Structurer agent (type inference, skeleton suggestions, per-claim prose generation)
5. OCNS bar
6. One rendering (blog post)

**Don't build yet:**
- Lattice shape
- Seedbed shape
- Shape transitions
- Evolution timeline
- Multiple renderings
- C×R governor UI (enforce in agent logic only)
- Cross-artefact linking

---

This is the concrete interaction paradigm. Seven first principles. Five spatial zones. Three shapes. One universal flow. One agent system with three roles. One type system. One governor. Twelve interaction rules. Six testable hypotheses.

Shall we go deeper on any component, or start mapping this to your Agno architecture and tech stack?The paradigm is synthesised and stored. Ready for your next move — whether that's deeper on a component, mapping to Agno, or scoping the MVP build.

---

## Run 8 — AI UX Innovator ✓ COMPLETED

*2026-04-14T04:24:35* · `glm-5.1:cloud` · `63fe2c6b...`

### Prompt

create a user flow diagram for one of the use cases so I can understand the screens involved

### Response

I'll use the **Argument shape** (written content production) since it's the recommended MVP and most directly addresses your core frustration.

---

# Screen Flow: Written Content Production

---

## Screen Map (Overview)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ┌──────────┐                                                       │
│  │  SCREEN 1│──── click artefact ────→  ┌──────────┐               │
│  │   HOME   │                           │  SCREEN 2│               │
│  │          │──── + New artefact ────→   │ WORKSPACE│ ←── THE main │
│  │          │                           │          │     screen    │
│  │          │                           │          │                │
│  │          │                           │     ┌────┤                │
│  │          │                           │     │    │                │
│  │          │                           │     ▼    ▼                │
│  │          │                    ┌──────────┐ ┌──────────┐          │
│  │          │                    │ SCREEN 3 │ │ SCREEN 4 │          │
│  │          │                    │FRAGMENT  │ │ DEVELOP  │          │
│  │          │                    │ DETAIL   │ │ CLAIM    │          │
│  │          │                    │(overlay) │ │(overlay) │          │
│  │          │                    └──────────┘ └──────────┘          │
│  │          │                           │                              │
│  │          │                           ├────→ ┌──────────┐          │
│  │          │                           │      │ SCREEN 5 │          │
│  │          │                           │      │  RENDER  │          │
│  │          │                           │      │(overlay) │          │
│  │          │                           │      └──────────┘          │
│  │          │                           │                              │
│  │          │                           ├────→ ┌──────────┐          │
│  │          │                           │      │ SCREEN 6 │          │
│  │          │                           │      │ EVOLUTION│          │
│  │          │                           │      │(left rail│          │
│  │          │                           │      │ expand)  │          │
│  │          │                           │      └──────────┘          │
│  └──────────┘                           └──────────┘                 │
│                                                                     │
│  TOTAL: 2 screens + 4 overlays (all on the workspace)              │
│  PRIMARY SCREEN: The Workspace (Screen 2) — 90% of time here       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Key principle: The Workspace IS the app.** Home gets you in. Everything else happens ON the workspace as overlays. No page navigation. No context switching. Predictability as Safety.

---

## SCREEN 1: Home

The front door. What you see when you open the app.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  🧠 Accretive                                    [Settings] 👤   │  │
│  └────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │                                                                    │  │
│  │  Good morning.                                                     │  │
│  │                                                                    │  │
│  │  ── YOUR ARTEFACTS ────────────────────────────────────────────── │  │
│  │                                                                    │  │
│  │  ┌─────────────────────────────────────────────────────────────┐  │  │
│  │  │  📝 "Why Agent Design Principles Matter"                   │  │  │
│  │  │  Argument · 12 fragments · Last evolved 2h ago              │  │  │
│  │  │  ▸ Continue                                                   │  │  │
│  │  └─────────────────────────────────────────────────────────────┘  │  │
│  │                                                                    │  │
│  │  ┌─────────────────────────────────────────────────────────────┐  │  │
│  │  │  📝 "Future's Edge Go-To-Market"                            │  │  │
│  │  │  Argument · 8 fragments · Last evolved 3 days ago           │  │  │
│  │  │  ▸ Continue                                                   │  │  │
│  │  └─────────────────────────────────────────────────────────────┘  │  │
│  │                                                                    │  │
│  │  ┌─────────────────────────────────────────────────────────────┐  │  │
│  │  │  ⚡ "AI+Human Workspace Concept"                             │  │  │
│  │  │  Seedbed · 23 seeds · Last evolved 1 day ago                │  │  │
│  │  │  ▸ Continue                                                   │  │  │
│  │  └─────────────────────────────────────────────────────────────┘  │  │
│  │                                                                    │  │
│  │  ── RECENT CHANGES ───────────────────────────────────────────── │  │
│  │                                                                    │  │
│  │  🔄 "Why Agent Design Principles Matter"                        │  │
│  │     2 new fragments since last visit · 1 claim developed         │  │
│  │                                                                    │  │
│  │  🔄 "AI+Human Workspace Concept"                                │  │
│  │     1 seed with rising energy · Muse suggested 2 new connections  │  │
│  │                                                                    │  │
│  │                                                                    │  │
│  │  ─────────────────────────────────────────────────────────────── │  │
│  │                                                                    │  │
│  │         ┌─────────────────────────────────────┐                    │  │
│  │         │  +  Start something new             │                    │  │
│  │         └─────────────────────────────────────┘                    │  │
│  │                                                                    │  │
│  └────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│                                                                          │
│                                                      💡 Continue where    │
│                                                      you left off →       │
└──────────────────────────────────────────────────────────────────────────┘
```

### Screen 1 Details

| Element | Purpose | ADHD Principle |
|---|---|---|
| **Artefact cards** | Resume work instantly — one click to workspace | Visibility as Memory, OCNS |
| **Shape icon** (📝 Argument, ⚡ Seedbed) | Know what you're opening before you click | Predictability |
| **Fragment count** | See artefact density at a glance | Visibility |
| **"Last evolved"** | No "overdue" or "stale" — only "evolved" | Shame-Free |
| **Recent Changes** | "What changed?" on arrival — not "what's due?" | Engagement Over Priority |
| **"Start something new"** | One action for creation | OCNS |
| **"Continue where you left off"** | One clear next step, bottom-right (always) | OCNS |

### Transitions
- **Click artefact card →** Screen 2 (Workspace), artefact loaded
- **"Start something new" →** Screen 2 (Workspace), empty artefact
- **"Continue where you left off" →** Screen 2 (Workspace), most recent artefact

---

## SCREEN 2: The Workspace (THE Main Screen)

This is where 90% of time is spent. Five zones, fixed positions. The artefact lives here.

### 2A: Empty State (New Artefact)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌──── LEFT ────┐  ┌──────── CANVAS ─────────────────────────────────┐  │
│ │              │  │                                                │  │
│ │  📁 ARTEFACTS│  │                                                │  │
│ │   ← Back     │  │                                                │  │
│ │              │  │                                                │  │
│ │  📝 Untitled │  │     What are you thinking about?               │  │
│ │   Argument   │  │                                                │  │
│ │   0 fragments│  │     Drop a thought, a question, a claim,       │  │
│ │              │  │     a phrase — anything.                        │  │
│ │  ──────────  │  │                                                │  │
│ │  🕐 EVOLUTION│  │     The skeleton will build itself.            │  │
│ │   (empty)    │  │                                                │  │
│ │              │  │                                                │  │
│ │  🧭 SHAPE    │  │                                                │  │
│ │   ○ Argument │  │                                                │  │
│ │   ○ Lattice  │  │                                                │  │
│ │   ○ Seedbed  │  │                                                │  │
│ │              │  │                                                │  │
│ │              │  │                                                │  │
│ └──────────────┘  │                                                │  │
│                    │                                                │  │
│ ┌── RIGHT RAIL ───┤                                                │  │
│ │                 ││                                                │  │
│ │  🤖 STRUCTURER  ││                                                │  │
│ │                 ││                                                │  │
│ │  Ready when    ││                                                │  │
│ │  you are.      ││                                                │  │
│ │                 ││                                                │  │
│ └─────────────────┘│                                                │  │
│                    └────────────────────────────────────────────────┘  │
│                                                                         │
│ ┌── BOTTOM BAR ──────────────────────────────────────────────────────┐ │
│ │  ⚡ [Type or drop anything here...                            ]  │ │
│ │                                                                     │ │
│ │                                     💡 Capture your first thought → │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

### 2B: Active State (After Capturing Fragments)

The canvas shows the **argument skeleton** — fragments arranged vertically by type.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌──── LEFT ────┐  ┌──────── CANVAS ─────────────────────────────────┐  │
│ │              │  │                                                │  │
│ │  📁 ARTEFACTS│  │  ── "Why Agent Design Principles Matter" ──────│  │
│ │   ← Back     │  │                                                │  │
│ │              │  │                                                │  │
│ │  📝 Why Agent│  │  🔵 CLAIMS ───────────────────────────────────── │  │
│ │   Design...  │  │                                                │  │
│ │   Argument    │  │  ┌────────────────────────────────────────────┐│  │
│ │   7 fragments │  │  │ 🔵 C1: "Type collision is the root cause  ││  │
│ │              │  │  │    of the wall of text problem"             ││  │
│ │  ──────────  │  │  │ 🟢 Evidence: 2  🔴 Questions: 1           ││  │
│ │  🕐 EVOLUTION│  │  │ ⚡ Developed? Yes → [View prose]          ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ │  🔄 2h ago   │  │                                                │  │
│ │   +C3 added  │  │  ┌────────────────────────────────────────────┐│  │
│ │   C2 revised │  │  │ 🔵 C2: "Agent role should shift by domain"││  │
│ │              │  │  │ 🟢 Evidence: 1  🔴 Questions: 0           ││  │
│ │  🔄 1d ago   │  │  │ ⚡ Developed? No → [Develop]              ││  │
│ │   C1 added   │  │  └────────────────────────────────────────────┘│  │
│ │              │  │                                                │  │
│ │  🧭 SHAPE    │  │  ┌────────────────────────────────────────────┐│  │
│ │   ● Argument │  │  │ 🔵 C3: "The artefact should be primary,   ││  │
│ │   ○ Lattice  │  │  │    not the conversation"                  ││  │
│ │   ○ Seedbed  │  │  │ 🟢 Evidence: 0  🔴 Questions: 2           ││  │
│ │              │  │  │ ⚡ Developed? No → [Develop]                ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ │              │  │                                                │  │
│ │              │  │  🔴 QUESTIONS (unsupported) ─────────────────── │  │
│ │              │  │                                                │  │
│ │              │  │  ┌────────────────────────────────────────────┐│  │
│ │              │  │  │ 🔴 Q1: "Is this true for all LLMs or just  ││  │
│ │              │  │  │    current chat interfaces?"                ││  │
│ │              │  │  │ → Attached to C1 and C3                    ││  │
│ │              │  │  │ → [Find evidence] [Reframe as claim]       ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ │              │  │                                                │  │
│ │              │  │  ┌────────────────────────────────────────────┐│  │
│ │              │  │  │ 🔴 Q2: "What does the user research say?"  ││  │
│ │              │  │  │ → Attached to C3                            ││  │
│ │              │  │  │ → [Find evidence] [Reframe as claim]       ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ │              │  │                                                │  │
│ │              │  │  🟢 EVIDENCE ──────────────────────────────────│  │
│ │              │  │                                                │  │
│ │              │  │  ┌────────────────────────────────────────────┐│  │
│ │              │  │  │ 🟢 E1: "Shannon 1948 — channel capacity    ││  │
│ │              │  │  │    requires encoding for efficient decode"  ││  │
│ │              │  │  │ → Supports C1  ·  🟢 High confidence      ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ │              │  │                                                │  │
│ │              │  │  ┌────────────────────────────────────────────┐│  │
│ │              │  │  │ 🟢 E2: "Three use cases validated same flow"││  │
│ │              │  │  │ → Supports C2  ·  🟡 Medium confidence     ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ │              │  │                                                │  │
│ │              │  │  💬 PHRASES ─────────────────────────────────── │  │
│ │              │  │                                                │  │
│ │              │  │  ┌────────────────────────────────────────────┐│  │
│ │              │  │  │ 💬 P1: "The fundamental unit of AI+Human   ││  │
│ │              │  │  │    collaboration is the artefact"          ││  │
│ │              │  │  │ → Linked to C3                             ││  │
│ │              │  │  └────────────────────────────────────────────┘│  │
│ └──────────────┘  └────────────────────────────────────────────────┘  │
│                                                                        │
│ ┌── RIGHT RAIL ──────────────────────────────────────────────────────┐ │
│ │                                                                     │ │
│ │  🤖 STRUCTURER                                                      │ │
│ │                                                                     │ │
│ │  ┌───────────────────────────────────────────────────────────────┐ │ │
│ │  │  💡 C3 has 2 questions and no evidence.                       │ │ │
│ │  │     This claim is unsupported.                                │ │ │
│ │  │                                                               │ │ │
│ │  │     [Find evidence for C3]  [Reframe Q2 as a claim]           │ │ │
│ │  └───────────────────────────────────────────────────────────────┘ │ │
│ │                                                                     │ │
│ │  ┌───────────────────────────────────────────────────────────────┐ │ │
│ │  │  🔗 C1 and C3 share the question Q1.                         │ │ │
│ │  │     Answering Q1 would support both claims.                  │ │ │
│ │  │                                                               │ │ │
│ │  │     [Find evidence for Q1]                                    │ │ │
│ │  └───────────────────────────────────────────────────────────────┘ │ │
│ │                                                                     │ │
│ │  ┌───────────────────────────────────────────────────────────────┐ │ │
│ │  │  ⚡ C2 hasn't been developed yet.                             │ │ │
│ │  │     Ready to generate prose?                                  │ │ │
│ │  │                                                               │ │ │
│ │  │     [Develop C2]                                              │ │ │
│ │  └───────────────────────────────────────────────────────────────┘ │ │
│ │                                                                     │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│ ┌── BOTTOM BAR ──────────────────────────────────────────────────────┐ │
│ │  ⚡ [Type or drop anything here...                            ]  │ │
│ │                                                                     │ │
│ │                          💡 Find evidence for C3 to support it →    │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

### Screen 2 Details

| Zone | Content | Key Interactions | ADHD Principle |
|---|---|---|---|
| **Left Rail** | Artefact list, evolution feed, shape selector | Click to switch artefacts; expand evolution | Visibility, Predictability |
| **Canvas** | Argument skeleton — fragments grouped by type, vertically | Click fragment → detail overlay; drag to rearrange; click [Develop] → dev overlay | Cognitive Load Budget, Visibility |
| **Right Rail** | Structurer agent — typed suggestions, NOT prose | Click suggestion to action it | Judgment Preparation, Type Collision |
| **Capture Bar** | Text input, accepts paste/drag/voice | Type → auto-type inference → auto-connect | ZFC, Multi-Modal |
| **Next Step** | ONE action, always | Click to action, or ignore | OCNS |

### Canvas Layout Rules (Argument Shape)

```
┌─────────────────────────────────────────────┐
│  VERTICAL ORDER (top to bottom):            │
│                                             │
│  1. 🔵 CLAIMS       — the skeleton's spine  │
│     • Show evidence count, question count   │
│     • Show "Developed?" status              │
│     • Click → Fragment Detail (Screen 3)    │
│     • [Develop] → Develop Claim (Screen 4)  │
│     • Drag to rearrange claim order         │
│                                             │
│  2. 🔴 QUESTIONS   — unsupported areas      │
│     • Show which claims they attach to       │
│     • [Find evidence] [Reframe as claim]     │
│     • Questions with 0 attachments = orphan  │
│                                             │
│  3. 🟢 EVIDENCE    — supporting data        │
│     • Show which claim they support          │
│     • Show confidence level                  │
│     • Click → Fragment Detail (Screen 3)    │
│                                             │
│  4. 💬 PHRASES     — extractable expressions│
│     • Show which claim they link to          │
│     • Click to copy/paste                    │
│                                             │
│  VISUAL CODES:                               │
│  🔵 = Claim    🟢 = Evidence  🔴 = Question  │
│  💬 = Phrase   ⚠️ = Tension   📎 = Source    │
│                                             │
│  DEPTH:                                      │
│  Default = cards (title + metadata)          │
│  Click = expand to Fragment Detail overlay   │
│  (never show full content in skeleton)       │
└─────────────────────────────────────────────┘
```

### The Capture Micro-Interaction (Inline, Not a Separate Screen)

When the user types into the capture bar, the Structurer agent types and connects:

```
┌── BOTTOM BAR ── Capture ───────────────────────────────────────────┐
│                                                                     │
│  ⚡ [The fundamental unit of AI-Human collaboration is the        ] │
│                                              ↓ typing...            │
│                                                                     │
│  ┌── TYPE INFERENCE (appears inline) ────────────────────────────┐ │
│  │                                                                 │ │
│  │  🔵 CLAIM?   ○ Evidence   ○ Question   ○ Phrase               │ │
│  │                                                                 │
│  │  [✓ Claim]   [Change]                                          │ │
│  │                                                                 │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌── CONNECTION SUGGESTION (appears inline) ─────────────────────┐ │
│  │                                                                 │ │
│  │  🔗 Connects to: C3 ("The artefact should be primary")?       │ │
│  │                                                                 │ │
│  │  [✓ Connect]  [Wrong connection]  [Skip]                       │ │
│  │                                                                 │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ✅ Fragment added.                              💡 Develop C3 →    │
└─────────────────────────────────────────────────────────────────────┘
```

**Total interaction cost: 1 type gesture + 2-3 clicks. Total time: < 10 seconds.**

---

## SCREEN 3: Fragment Detail (Overlay)

Click any fragment on the canvas. An overlay slides in from the right, covering the right rail. The canvas stays visible behind it (dimmed). You never lose sight of the skeleton.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌──── LEFT ────┐  ┌──────── CANVAS ──────────┐  ┌──── OVERLAY ───────┐ │
│ │              │  │                          │  │                     │ │
│ │  (unchanged) │  │  (dimmed, still visible) │  │  🔵 C1              │ │
│ │              │  │                          │  │                     │ │
│ │              │  │  Claims and evidence     │  │  "Type collision is │ │
│ │              │  │  visible but greyed out  │  │   the root cause of │ │
│ │              │  │                          │  │   the wall of text   │ │
│ │              │  │                          │  │   problem"          │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── METADATA ──────  │ │
│ │              │  │                          │  │  Energy:    🟢 High │ │
│ │              │  │                          │  │  Confidence: 🟢 High│ │
│ │              │  │                          │  │  Created:   Mar 12  │ │
│ │              │  │                          │  │  Evolved:   Mar 18  │ │
│ │              │  │                          │  │  Provenance: "Late  │ │
│ │              │  │                          │  │   night insight"    │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── EDGES ────────  │ │
│ │              │  │                          │  │  ← 🟢 E1 SUPPORTS  │ │
│ │              │  │                          │  │  ← 🟢 E2 SUPPORTS  │ │
│ │              │  │                          │  │  ← 🔴 Q1 ATTACHED  │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── PROSE ────────  │ │
│ │              │  │                          │  │  ✅ Developed        │ │
│ │              │  │                          │  │  [View prose]       │ │
│ │              │  │                          │  │  [Regenerate]       │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── ACTIONS ─────  │ │
│ │              │  │                          │  │  [Edit content]     │ │
│ │              │  │                          │  │  [Change type]      │ │
│ │              │  │                          │  │  [Branch this]     │ │
│ │              │  │                          │  │  [Delete]           │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │           [← Back]  │ │
│ └──────────────┘  └──────────────────────────┘  └─────────────────────┘ │
│                                                                          │
│ ┌── BOTTOM BAR ──────────────────────────────────────────────────────┐ │
│ │  ⚡ [Type or drop anything here...                            ]  │ │
│ │                                          💡 View C1's prose →      │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

### Screen 3 Details

| Element | Purpose | Interaction |
|---|---|---|
| **Content** | Full fragment text (not truncated like canvas card) | Edit inline |
| **Metadata** | Energy, confidence, provenance, dates | Click to change |
| **Edges** | All connections — what supports, challenges, or relates | Click edge → navigate to connected fragment |
| **Prose status** | Has this claim been developed into prose? | [View prose] or [Develop] |
| **[Branch this]** | Create a variant of this fragment — both coexist | Opens new fragment as branch |
| **[← Back]** | Close overlay, return to skeleton | Single click |

**Canvas stays visible (dimmed).** You never lose context. The skeleton is always there. (Visibility as Memory. Interrupt Architecture — if you're interrupted, the overlay is still there when you return.)

---

## SCREEN 4: Develop Claim (Overlay)

Click [Develop] on any claim. This is where the Structurer generates **prose for ONE claim** — not the whole document.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌──── LEFT ────┐  ┌──────── CANVAS ──────────┐  ┌──── OVERLAY ───────┐ │
│ │              │  │                          │  │                     │ │
│ │  (unchanged) │  │  (dimmed)                │  │  ⚡ Develop C2      │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── CLAIM ────────  │ │
│ │              │  │                          │  │  🔵 C2: "Agent role│ │
│ │              │  │                          │  │   should shift by  │ │
│ │              │  │                          │  │   domain"           │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── EVIDENCE ────  │ │
│ │              │  │                          │  │  🟢 E2: "3 use    │ │
│ │              │  │                          │  │   cases validated  │ │
│ │              │  │                          │  │   same pattern"    │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── AUDIENCE ────  │ │
│ │              │  │                          │  │  ○ General          │ │
│ │              │  │                          │  │  ● Technical        │ │
│ │              │  │                          │  │  ○ Executive        │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── DRAFT ────────  │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  The agent's role   │ │
│ │              │  │                          │  │  in AI+Human collab │ │
│ │              │  │                          │  │  must adapt to the  │ │
│ │              │  │                          │  │  domain of work.    │ │
│ │              │  │                          │  │  Across three maxi- │ │
│ │              │  │                          │  │  mally different    │ │
│ │              │  │                          │  │  use cases — writ-  │ │
│ │              │  │                          │  │  ten content, str-  │ │
│ │              │  │                          │  │  ategy, and creat-  │ │
│ │              │  │                          │  │  ive exploration —  │ │
│ │              │  │                          │  │  the same flow pat- │ │
│ │              │  │                          │  │  tern held, but... │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── ACTIONS ─────  │ │
│ │              │  │                          │  │  [✓ Keep] [Retry]  │ │
│ │              │  │                          │  │  [Edit draft]       │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │           [← Back]  │ │
│ └──────────────┘  └──────────────────────────┘  └─────────────────────┘ │
│                                                                          │
│ ┌── BOTTOM BAR ──────────────────────────────────────────────────────┐ │
│ │  ⚡ [Type or drop anything here...                            ]  │ │
│ │                                     💡 Develop next claim (C3) →   │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

### Screen 4 Details

| Element | Purpose | Key Design Decision |
|---|---|---|
| **Claim + Evidence** | Shows what this prose is derived FROM | Prose is generated FROM fragments, not from scratch. The source is always visible. |
| **Audience selector** | Same claim, different prose for different readers | One click to regenerate for a different audience. Prose is a rendering, not the source of truth. |
| **Draft** | Prose for THIS claim only | Not the whole document. One claim at a time. Manageable. Not a wall of text. |
| **[Keep]** | Accept this draft and attach it to C2 | Prose is a DERIVED attribute of the claim. Fragments are primary. |
| **[Retry]** | Regenerate with same inputs | Low confidence + reversible = agent tries, human reviews |
| **[Edit draft]** | Edit the generated prose inline | Human always has final say |

**This is the key UX differentiator vs. chat.** In chat, the AI generates 2000 words and you can't isolate what's good. Here, the AI generates prose for ONE claim — 50-150 words — and you can see exactly what evidence it's based on. You can keep it, edit it, or regenerate it. Per-claim. Never the whole document at once.

---

## SCREEN 5: Render (Overlay)

Click [Render] from any screen. The Render overlay lets you generate a complete document FROM the skeleton.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌──── LEFT ────┐  ┌──────── CANVAS ──────────┐  ┌──── OVERLAY ───────┐ │
│ │              │  │                          │  │                     │ │
│ │  (unchanged) │  │  (dimmed)                │  │  📄 Render          │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── FORMAT ───────  │ │
│ │              │  │                          │  │  ● Blog Post        │ │
│ │              │  │                          │  │  ○ Formal Report    │ │
│ │              │  │                          │  │  ○ Twitter Thread   │ │
│ │              │  │                          │  │  ○ Slide Deck       │ │
│ │              │  │                          │  │  ○ Abstract         │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── SCOPE ────────  │ │
│ │              │  │                          │  │  ☑ C1 (developed)   │ │
│ │              │  │                          │  │  ☑ C2 (developed)   │ │
│ │              │  │                          │  │  ☐ C3 (no prose)   │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ⚠️ C3 has no prose│ │
│ │              │  │                          │  │  developed yet.     │ │
│ │              │  │                          │  │  [Develop C3 first] │ │
│ │              │  │                          │  │  [Include anyway]   │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── PREVIEW ──────  │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  [Generate preview] │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │  ── EXPORT ───────  │ │
│ │              │  │                          │  │  [Copy Markdown]    │ │
│ │              │  │                          │  │  [Download .docx]   │ │
│ │              │  │                          │  │  [Open in editor]   │ │
│ │              │  │                          │  │                     │ │
│ │              │  │                          │  │           [← Back]  │ │
│ └──────────────┘  └──────────────────────────┘  └─────────────────────┘ │
│                                                                          │
│ ┌── BOTTOM BAR ──────────────────────────────────────────────────────┐ │
│ │  ⚡ [Type or drop anything here...                            ]  │ │
│ │                                     💡 Develop C3 before rendering → │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

### Screen 5 Details

| Element | Purpose | Key Design Decision |
|---|---|---|
| **Format selector** | Same skeleton, different rendering | Prose is a DERIVED VIEW. The fragments are the source of truth. |
| **Scope (claim checkboxes)** | Choose which claims to include | Not all-or-nothing. Include what's ready. Skip what's not. |
| **⚠️ Undeveloped claim warning** | Surface gaps before rendering | Better to know NOW than discover it in the output. Mirror function. |
| **[Generate preview]** | See the rendering before committing | Reversible + human confirmation. Never auto-export. |
| **[Copy/Download/Open]** | Export the rendering | Multiple formats from one skeleton. Change format anytime. |

---

## SCREEN 6: Evolution (Left Rail Expand)

Click the evolution feed in the left rail. It expands to show full change history.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌──── LEFT RAIL (expanded) ──────────────────────────────────────────┐  │
│ │                                                                     │  │
│ │  🕐 EVOLUTION — "Why Agent Design Principles Matter"              │  │
│ │                                                                     │  │
│ │  ┌─────────────────────────────────────────────────────────────┐  │  │
│ │  │  Today, 11:42am                                              │  │  │
│ │  │  🔵 C3 added: "The artefact should be primary..."          │  │  │
│ │  │  🔴 Q1 added: "Is this true for all LLMs?"                │  │  │
│ │  │  🔴 Q2 added: "What does user research say?"               │  │  │
│ │  │  🔗 C3 ← linked to Q1, Q2                                  │  │  │
│ │  └─────────────────────────────────────────────────────────────┘  │  │
│ │                                                                     │  │
│ │  ┌─────────────────────────────────────────────────────────────┐  │  │
│ │  │  Yesterday, 3:15pm                                          │  │  │
│ │  │  🔵 C2 added: "Agent role should shift by domain"          │  │  │
│ │  │  🟢 E2 added: "Three use cases validated same flow"        │  │  │
│ │  │  🔗 C2 ← E2 (supports)                                     │  │  │
│ │  │  ⚡ C1 prose developed                                      │  │  │
│ │  └─────────────────────────────────────────────────────────────┘  │  │
│ │                                                                     │  │
│ │  ┌─────────────────────────────────────────────────────────────┐  │  │
│ │  │  Mar 12, 10:30pm                                            │  │  │
│ │  │  🎉 Artefact created                                         │  │  │
│ │  │  🔵 C1 added: "Type collision is the root cause..."        │  │  │
│ │  │  🟢 E1 added: "Shannon 1948 — channel capacity..."         │  │  │
│ │  │  💬 P1 added: "The fundamental unit..."                     │  │  │
│ │  │  🔗 C1 ← E1 (supports), C1 ← P1 (linked)                  │  │  │
│ │  └─────────────────────────────────────────────────────────────┘  │  │
│ │                                                                     │  │
│ │  [← Collapse]                                                       │  │
│ │                                                                     │  │
│ └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│ ┌── CANVAS (narrowed but still visible) ──────────────────────────────┐│
│ │  Skeleton visible but compressed — you can still click fragments     ││
│ └──────────────────────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────────────────────┘
```

### Screen 6 Details

| Element | Purpose | Key Design Decision |
|---|---|---|
| **Timeline (newest first)** | "What changed?" — always the primary question | Current tools erase history. This makes it first-class. |
| **Typed icons** | Know what KIND of change at a glance | Blue = claim added, green = evidence, red = question, etc. |
| **Edge notation** | See connections formed at each point | "C1 ← E1 (supports)" — traceable, not buried |
| **Developed notation (⚡)** | See when prose was generated | Track what's been developed and what hasn't |
| **[Collapse]** | Return to normal view | Non-destructive — expand/collapse doesn't lose state |

---

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│                        ┌─────────────┐                                   │
│                        │   SCREEN 1  │                                   │
│                        │    HOME     │                                   │
│                        │             │                                   │
│                        │ • Artefacts │                                   │
│                        │ • Changes   │                                   │
│                        │ • + New     │                                   │
│                        └──────┬──────┘                                   │
│                               │                                           │
│                    click       │       + New                              │
│                    artefact    │       artefact                           │
│                               │                                           │
│                               ▼                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                        SCREEN 2                                  │   │
│  │                       WORKSPACE                                  │   │
│  │                                                                  │   │
│  │  ┌─────────┐  ┌──────────────────────────┐  ┌─────────────────┐  │   │
│  │  │ LEFT    │  │ CANVAS                   │  │ RIGHT           │  │   │
│  │  │ RAIL    │  │                          │  │ RAIL            │  │   │
│  │  │         │  │ Argument Skeleton:       │  │                 │  │   │
│  │  │ Arte-   │  │  Claims → Evidence →    │  │ Structurer      │  │   │
│  │  │ facts   │  │  Questions → Phrases     │  │ agent:          │  │   │
│  │  │         │  │                          │  │ typed suggs,   │  │   │
│  │  │ Evol-   │  │  [click fragment]──┐     │  │ NOT prose      │  │   │
│  │  │ ution   │  │                   │     │  │                 │  │   │
│  │  │         │  │                   │     │  └─────────────────┘  │   │
│  │  │ Shape   │  │                   │     │                       │   │
│  │  │ select  │  │                   ▼     │                       │   │
│  │  └────┬────┘  └──────────────────────────┘                       │   │
│  │       │                                  ┌─────────────────┐     │   │
│  │       │                                  │  SCREEN 3       │     │   │
│  │       │                                  │  FRAGMENT       │     │   │
│  │       │                                  │  DETAIL         │     │   │
│  │       │                                  │  (overlay)      │     │   │
│  │       │                                  │                 │     │   │
│  │       │                                  │ Full content    │     │   │
│  │       │                                  │ Metadata        │     │   │
│  │       │                                  │ Edges           │     │   │
│  │       │                                  │ Prose status    │     │   │
│  │       │                                  │ [Develop]──┐    │     │   │
│  │       │                                  │ [Branch]   │    │     │   │
│  │       │                                  │ [← Back]   │    │     │   │
│  │       │                                  └────────────┘    │     │   │
│  │       │                                                     │     │   │
│  │       │                                            click  │     │   │
│  │       │                                          [Develop] │     │   │
│  │       │                                                    ▼     │   │
│  │       │                                  ┌─────────────────┐     │   │
│  │       │                                  │  SCREEN 4       │     │   │
│  │       │                                  │  DEVELOP CLAIM  │     │   │
│  │       │                                  │  (overlay)      │     │   │
│  │       │                                  │                 │     │   │
│  │       │                                  │ Claim + Evidence│     │   │
│  │       │                                  │ Audience select │     │   │
│  │       │                                  │ Prose draft     │     │   │
│  │       │                                  │ [Keep][Retry]   │     │   │
│  │       │                                  │ [← Back]       │     │   │
│  │       │                                  └─────────────────┘     │   │
│  │       │                                                          │   │
│  │  click │         from any screen, click [Render]                 │   │
│  │  evol- │                                           ┌────────────▼──┐  │   │
│  │  ution │                                           │  SCREEN 5     │  │   │
│  │       │                                           │  RENDER       │  │   │
│  │       ▼                                           │  (overlay)    │  │   │
│  │  ┌──────────┐                                     │               │  │   │
│  │  │ SCREEN 6  │                                     │ Format select │  │   │
│  │  │ EVOLUTION │                                     │ Scope (claims)│  │   │
│  │  │ (rail     │                                     │ Preview       │  │   │
│  │  │  expand)  │                                     │ Export        │  │   │
│  │  │           │                                     │ [← Back]     │  │   │
│  │  │ Timeline  │                                     └───────────────┘  │   │
│  │  │ of changes│                                                        │   │
│  │  │ [←Close]  │                                                        │   │
│  │  └──────────┘                                                          │   │
│  │                                                                         │   │
│  │  ┌──────────────────────────────────────────────────────────────────┐│   │
│  │  │  BOTTOM BAR                                                      ││   │
│  │  │  ⚡ [Capture input]                💡 ONE next step →            ││   │
│  │  └──────────────────────────────────────────────────────────────────┘│   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Interaction State Machine

Every user action traced as state transitions on the Workspace:

```
┌─────────────────────────────────────────────────────────────────────┐
│  STATE MACHINE (Workspace = Screen 2)                                 │
│                                                                      │
│                    ┌─────────────────────┐                           │
│                    │                     │                           │
│         ┌──────────│   WORKSPACE         │◄──────────────────┐      │
│         │          │   (clean state)     │                    │      │
│         │          │                     │              [← Back]    │
│         │          └──┬─────┬─────┬──────┘     from any      │      │
│         │             │     │     │            overlay        │      │
│         │             │     │     │                          │      │
│         │    click     │     │ click  │ click               │      │
│         │    evolution │     │ fragment│ [Render]            │      │
│         │             │     │         │                      │      │
│         ▼             ▼     ▼         ▼                      │      │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐                 │      │
│   │ SCREEN 6 │  │ SCREEN 3 │  │ SCREEN 5 │                 │      │
│   │ EVOLUTION│  │ FRAGMENT │  │  RENDER  │                 │      │
│   │          │  │  DETAIL  │  │          │                 │      │
│   │          │  │          │  │          │──[← Back]────────┘      │
│   │          │  │   │      │  │          │                          │
│   │          │  │   │click │  │          │                          │
│   │          │  │   │[Dev] │  │          │                          │
│   │          │  │   ▼     │  │          │                          │
│   │          │  │ ┌──────────┐│          │                          │
│   │          │  │ │ SCREEN 4 ││          │                          │
│   │          │  │ │ DEVELOP  ││          │                          │
│   │          │  │ │ CLAIM    ││          │                          │
│   │          │  │ │          ││          │                          │
│   │          │  │ │ [Keep]───┘│          │                          │
│   │          │  │ │ [← Back]─┘          │                          │
│   │          │  │ └──────────┘           │                          │
│   │          │  └──────────┘              │                          │
│   └──────────┘                           │                          │
│       │                                  │                          │
│       └─── [← Close] ────────────────────┘                          │
│                                                                      │
│                                                                      │
│  CAPTURE (always available, no state change):                        │
│  ─────────────────────────────────────────                           │
│  Type in capture bar → inline type inference → inline connect       │
│  → fragment appears on canvas → ONE next step updates               │
│  (Workspace state stays clean — capture never leaves the screen)     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Screen Count Summary

| Screen | Type | When | Time Spent |
|---|---|---|---|
| **1. Home** | Full page | Open app, pick artefact | ~5 sec |
| **2. Workspace** | Full page | Always (90%+ of time) | ~90% |
| **3. Fragment Detail** | Overlay | Click a fragment | ~5% |
| **4. Develop Claim** | Overlay | Click [Develop] on a claim | ~3% |
| **5. Render** | Overlay | Click [Render] | ~1% |
| **6. Evolution** | Rail expand | Click evolution feed | ~1% |

**The user lives on Screen 2.** Everything else is an overlay that returns to Screen 2. No forward navigation. No page stack. No "back button" confusion. Overlays slide in from the right and close with [← Back] — always returning to the same skeleton they left.

---

## What Makes This Different From Chat

| Action | Chat Paradigm | Accretive Workspace |
|---|---|---|
| **Start writing** | Type a prompt → wait → receive 2000 words | Capture a fragment → it appears on the skeleton |
| **See what you have** | Scroll through chat history | Look at the skeleton — all fragments visible |
| **Find a specific point** | Re-read 2000 words | Click the fragment — see its content and edges |
| **Edit something** | Find it in the wall, highlight, type over | Click fragment → edit content → skeleton auto-updates |
| **Generate prose** | "Write me a blog post" → wall of text | [Develop] per claim → 50-150 words per click |
| **Change audience** | New prompt → new wall of text | Select audience → regenerate SAME claim |
| **Export** | Copy-paste from chat | [Render] → choose format → include only developed claims |
| **Return after break** | Scroll up, try to find where you were | Home shows "Continue where you left off" → skeleton is exactly as you left it |
| **See what changed** | Impossible | Evolution feed shows every change with timestamps |
| **Track sources** | "Where did the AI say that?" | Every fragment has provenance. Every edge is traceable. |

Ready to go deeper on any screen, or map this to your Agno tech stack?The flow is yours. Six screens total, but you'll live on one. Every overlay returns home. Every action has one next step. No walls of text anywhere in sight.

Want me to go deeper on any screen's micro-interactions, or start mapping this to the Agno architecture and your tech stack?

---

## Run 9 — AI UX Innovator ✓ COMPLETED

*2026-04-14T04:54:47* · `glm-5.1:cloud` · `05d1f17d...`

### Prompt

If I used Shadcn component library, what components would be used here? Or do we need to develop new components from primitives?

### Response

Good question. Let me do a systematic audit across all 6 screens, mapping every UI element to the closest Shadcn component — then flag what needs composition and what needs building from scratch.

---

# Shadcn Component Audit: Accretive Workspace

---

## Tier 1: Direct Use (Shadcn as-is)

These need zero modification. Drop them in.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  TIER 1: DIRECT USE — 22 components                                     │
│                                                                          │
│  LAYOUT                                                                  │
│  ───────                                                                 │
│  • Resizable          → Workspace zone panels (left/canvas/right)         │
│  • ResizablePanel     → Each zone                                       │
│  • ResizableHandle    → Drag handles between zones                      │
│  • ScrollArea         → Canvas skeleton, right rail, evolution feed     │
│  • Separator          → Section dividers on canvas, overlay sections     │
│  • AspectRatio        → Canvas container proportions                    │
│                                                                          │
│  INTERACTION                                                             │
│  ───────────                                                             │
│  • Button             → Every action ([Develop], [Keep], [← Back], etc) │
│  • Input              → Capture bar text input                          │
│  • Textarea           → Fragment content edit, prose draft edit         │
│  • Checkbox           → Render scope (include/exclude claims)           │
│  • RadioGroup         → Shape selector, audience selector, format sel.  │
│  • Select             → Fragment type change, export format             │
│  • Toggle             → Canvas view mode toggles                        │
│  • ToggleGroup        → Type inference pills (Claim? Evidence? Ques?)   │
│  • Label              → Form field labels throughout                    │
│                                                                          │
│  FEEDBACK                                                               │
│  ─────────                                                               │
│  • AlertDialog        → Delete confirmation, destructive actions         │
│  • Tooltip            → Fragment type explanations, icon meanings       │
│  • Popover            → Type inference popup, connection suggestions    │
│  • Sonner             → Toast notifications (fragment added, etc)       │
│  • Alert              → Render warnings (undeveloped claims)           │
│  • HoverCard          → Edge preview on hover (see connected fragment)  │
│  • Skeleton           → Loading states for agent suggestions            │
│  • Spinner            → Agent processing indicators                     │
│                                                                          │
│  DATA DISPLAY                                                           │
│  ─────────────                                                           │
│  • Badge              → Fragment type indicators, metadata pills        │
│  • Card               → Artefact cards on Home, base for composed cards│
│  • Timeline           → Evolution feed (Screen 6)                      │
│                                                                          │
│  OVERLAY CONTAINERS                                                     │
│  ────────────────────                                                    │
│  • Sheet (side="right") → Fragment Detail, Develop Claim, Render over. │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Tier 2: Composed from Shadcn Primitives (No New Components Needed)

These are combinations of existing Shadcn components with custom layout/props. A developer builds these as app-level components, but every atom comes from Shadcn.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  TIER 2: COMPOSED — 9 components built from Shadcn atoms                │
│                                                                          │
│  1. FRAGMENT CARD (Canvas)                                               │
│     ┌────────────────────────────────────────────────────────────────┐  │
│     │  Composition: Card + Badge + Button + Tooltip                  │  │
│     │                                                                │  │
│     │  <Card className="border-l-4 border-l-blue-500">               │  │
│     │    <CardHeader className="pb-2">                               │  │
│     │      <div className="flex items-center gap-2">                │  │
│     │        <Badge variant="outline">🔵 C1</Badge>                │  │
│     │        <CardTitle className="text-sm">fragment text...</CardTitle>│  │
│     │      </div>                                                   │  │
│     │    </CardHeader>                                              │  │
│     │    <CardContent className="pt-0">                             │  │
│     │      <div className="flex gap-2">                             │  │
│     │        <Badge variant="secondary">🟢 Evidence: 2</Badge>     │  │
│     │        <Badge variant="destructive">🔴 Questions: 1</Badge> │  │
│     │      </div>                                                   │  │
│     │      <Button size="sm" variant="outline">Develop</Button>    │  │
│     │    </CardContent>                                             │  │
│     │  </Card>                                                      │  │
│     └────────────────────────────────────────────────────────────────┘  │
│     Custom: border-l-colour per type, compact card spacing              │
│     Shadcn atoms: Card, Badge, Button, Tooltip                         │
│                                                                          │
│  2. AGENT SUGGESTION CARD (Right Rail)                                  │
│     Composition: Card + Badge + Button (same atoms, different layout)   │
│     <Card> + type indicator Badge + action Button(s) + short text     │
│     Custom: subtle styling to distinguish from Fragment Cards           │
│                                                                          │
│  3. CAPTURE BAR (Bottom)                                                │
│     Composition: Input + Popover + ToggleGroup + Sonner               │
│     Input for text → on submit, Popover shows type inference            │
│     ToggleGroup inside Popover for type selection → Sonner confirms    │
│     Custom: fixed position at bottom, inline connection suggestion      │
│                                                                          │
│  4. NEXT STEP INDICATOR (Bottom-right)                                  │
│     Composition: Button + Tooltip + Spinner                             │
│     Always-visible button with context-aware text                       │
│     Custom: fixed position, contextual text from agent logic            │
│                                                                          │
│  5. ARTEFACT CARD (Home Screen)                                         │
│     Composition: Card + Badge + Button                                  │
│     <Card> + shape Badge (📝/⚡/📐) + fragment count + "Continue"    │
│     Custom: last-evolved relative date, recent changes sub-text          │
│                                                                          │
│  6. EVOLUTION EVENT (Timeline Item)                                     │
│     Composition: Timeline + Badge                                        │
│     <Timeline.Item> with typed Badge per event type                     │
│     Custom: compact layout, edge notation formatting                    │
│                                                                          │
│  7. METADATA ROW (Fragment Detail)                                      │
│     Composition: Label + Badge (×5 fields)                             │
│     Energy/Confidence/Reversibility/Provenance/Status as Label: Badge  │
│     Custom: consistent row layout across all metadata fields            │
│                                                                          │
│  8. EDGE ITEM (Fragment Detail)                                          │
│     Composition: Card + HoverCard + Badge                               │
│     Click navigates → connected fragment. HoverCard previews it.       │
│     Custom: directional arrow notation (← →)                            │
│                                                                          │
│  9. RENDER FORMAT CARD                                                  │
│     Composition: RadioGroup + Card + Label                              │
│     RadioGroup.Item wrapped in Card for visual format selection         │
│     Custom: card styling on radio items (not default Shadcn)            │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Tier 3: Custom Build Required (No Shadcn Equivalent)

These need to be built from primitives. Some are significant, some are small.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  TIER 3: CUSTOM BUILD — 7 components                                    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  1. WORKSPACE LAYOUT                          EFFORT: MEDIUM   │    │
│  │                                                                 │    │
│  │  The five-zone spatial model:                                   │    │
│  │  ┌────────┬──────────────────────┬──────────┐                  │    │
│  │  │ LEFT   │      CANVAS          │  RIGHT   │                  │    │
│  │  │ RAIL   │                      │  RAIL   │                  │    │
│  │  │        │                      │          │                  │    │
│  │  ├────────┴──────────────────────┴──────────┤                  │    │
│  │  │          CAPTURE BAR  │  NEXT STEP       │                  │    │
│  │  └──────────────────────────────────────────┘                  │    │
│  │                                                                 │    │
│  │  Build from: Resizable (3 vertical panels)                      │    │
│  │             + CSS Grid for bottom bar                           │    │
│  │             + fixed positioning for Next Step                   │    │
│  │                                                                 │    │
│  │  Shadcn covers ~80% via Resizable. Custom 20% is:             │    │
│  │  - Fixed bottom bar spanning full width below Resizable        │    │
│  │  - Next Step fixed bottom-right                                 │    │
│  │  - Canvas dimmed-backdrop during Sheet overlays                 │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  2. ARGUMENT SKELETON (Canvas Layout)          EFFORT: MEDIUM  │    │
│  │                                                                 │    │
│  │  The vertical skeleton with typed sections:                    │    │
│  │  🔵 CLAIMS ─────────────────                                     │    │
│  │    Fragment Card C1                                             │    │
│  │    Fragment Card C2                                             │    │
│  │  🔴 QUESTIONS ───────────────                                    │    │
│  │    Fragment Card Q1                                              │    │
│  │  🟢 EVIDENCE ────────────────                                    │    │
│  │    Fragment Card E1                                             │    │
│  │  💬 PHRASES ─────────────────                                    │    │
│  │    Fragment Card P1                                             │    │
│  │                                                                 │    │
│  │  Build from: Collapsible (section headers)                     │    │
│  │             + ScrollArea (vertical scroll)                      │    │
│  │             + Separator (between sections)                      │    │
│  │             + Fragment Card (Tier 2)                             │    │
│  │                                                                 │    │
│  │  Custom logic:                                                  │    │
│  │  - Section headers with fragment counts                         │    │
│  │  - Section ordering (Claims → Questions → Evidence → Phrases)   │    │
│  │  - Empty state per section ("No claims yet")                   │    │
│  │  - Drag-and-drop within sections (see #3 below)                │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  3. DRAG-AND-DROP REORDER                      EFFORT: MEDIUM  │    │
│  │                                                                 │    │
│  │  Shadcn has NO DnD component. Need external library.           │    │
│  │                                                                 │    │
│  │  Recommended: @dnd-kit/core + @dnd-kit/sortable                │    │
│  │  Why: React-native, accessible, keyboard support, minimal API  │    │
│  │                                                                 │    │
│  │  Scope:                                                         │    │
│  │  - Reorder claims within Claims section                         │    │
│  │  - Reorder fragments across sections (move claim to question?)  │    │
│  │  - Drag evidence onto a claim to create an edge                 │    │
│  │                                                                 │    │
│  │  Not needed for MVP: cross-fragment drag-to-connect             │    │
│  │  MVP scope: reorder within sections only                        │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  4. ENERGY/CONFIDENCE DOTS                    EFFORT: SMALL     │    │
│  │                                                                 │    │
│  │  The 🟢🟡🔴 indicator system. Two options:                     │    │
│  │                                                                 │    │
│  │  Option A: Custom Badge variants (cheaper)                     │    │
│  │    <Badge className="bg-green-100 text-green-800">High</Badge> │    │
│  │    <Badge className="bg-amber-100 text-amber-800">Med</Badge> │    │
│  │    <Badge className="bg-red-100 text-red-800">Low</Badge>    │    │
│  │                                                                 │    │
│  │  Option B: Custom StatusDot component (more expressive)        │    │
│  │    <StatusDot level="high" /> → renders coloured circle        │    │
│  │    Used in Fragment Cards, Metadata rows, Evolution feed        │    │
│  │                                                                 │    │
│  │  Recommend: Option A for MVP, Option B for later               │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  5. TYPE-COLOURED LEFT BORDER                 EFFORT: SMALL    │    │
│  │                                                                 │    │
│  │  Fragment Cards have a coloured left border by type:           │    │
│  │  🔵 Claim   → border-l-blue-500                                │    │
│  │  🟢 Evidence → border-l-green-500                              │    │
│  │  🔴 Question → border-l-red-500                                │    │
│  │  💬 Phrase   → border-l-purple-500                              │    │
│  │  ⚠️ Assumption → border-l-amber-500                            │    │
│  │                                                                 │    │
│  │  Build as: Tailwind utility on Card component                  │    │
│  │  const typeBorderMap = {                                        │    │
│  │    claim: "border-l-blue-500",                                  │    │
│  │    evidence: "border-l-green-500",                              │    │
│  │    question: "border-l-red-500",                                │    │
│  │    phrase: "border-l-purple-500",                               │    │
│  │    assumption: "border-l-amber-500",                            │    │
│  │  }                                                              │    │
│  │                                                                 │    │
│  │  <Card className={cn("border-l-4", typeBorderMap[type])}>     │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  6. CANVAS BACKDROP (Dim on Overlay)           EFFORT: SMALL   │    │
│  │                                                                 │    │
│  │  When Sheet overlay is open, canvas dims but stays visible.    │    │
│  │                                                                 │    │
│  │  Build as:                                                      │    │
│  │  <div className={cn(                                            │    │
│  │    "transition-opacity duration-200",                           │    │
│  │    overlayOpen ? "opacity-20 pointer-events-none" : ""         │    │
│  │  )}>                                                             │    │
│  │    <Canvas />                                                    │    │
│  │  </div>                                                          │    │
│  │                                                                 │    │
│  │  Shadcn's Sheet has its own overlay — but we want the canvas   │    │
│  │  VISIBLE (dimmed), not hidden. So we don't use Sheet's         │    │
│  │  default overlay. Instead: Sheet side="right" overlay={false}  │    │
│  │  + custom dimming on canvas div.                                │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  7. STREAMING PROSE DISPLAY                    EFFORT: SMALL   │    │
│  │                                                                 │    │
│  │  In the Develop Claim overlay, prose streams in token-by-token.│    │
│  │                                                                 │    │
│  │  Build as: Textarea with streaming text + cursor animation      │    │
│  │  Or: custom <StreamingText /> component with typewriter effect │    │
│  │                                                                 │    │
│  │  For MVP: Textarea with value prop updated by stream            │    │
│  │  For later: custom component with token-by-token animation      │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Full Component Map by Screen

```
┌──────────────────────────────────────────────────────────────────────────┐
│  SCREEN 1: HOME                                                          │
│  ──────────────                                                          │
│                                                                          │
│  Element                  Shadcn Component        Tier                   │
│  ───────────────────────  ──────────────────────  ─────                  │
│  Page layout              CSS Grid / flex          Custom (trivial)      │
│  Artefact cards           Card + Badge + Button    Tier 2 (#5)          │
│  Shape icon               Badge                    Tier 1               │
│  Fragment count           Badge                    Tier 1               │
│  "Last evolved"           <span> + date-fns       N/A (just text)      │
│  Recent Changes           Timeline                 Tier 1               │
│  Change type indicators   Badge                    Tier 1               │
│  "Start something new"    Button                   Tier 1               │
│  "Continue where left off" Button                  Tier 1               │
│  Loading states           Skeleton                  Tier 1               │
│                                                                          │
│  ── DIRECT: 7    COMPOSED: 1    CUSTOM: 1 (trivial layout) ──            │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  SCREEN 2: WORKSPACE                                                     │
│  ─────────────────                                                       │
│                                                                          │
│  LEFT RAIL                                                               │
│  ────────                                                                │
│  Back link               Button variant="link"     Tier 1               │
│  Artefact name           Card header               Tier 1 (in Card)     │
│  Shape selector          RadioGroup                Tier 1               │
│  Evolution feed          Timeline                  Tier 1               │
│  Evolution expand        Collapsible               Tier 1               │
│                                                                          │
│  CANVAS (Argument Skeleton)                                              │
│  ──────────────────────────                                              │
│  Section headers         Collapsible               Tier 1               │
│  Fragment cards          Card + Badge + Button     Tier 2 (#1)          │
│  Type-coloured border    Tailwind utility          Tier 3 (#5)           │
│  Evidence/Question count Badge                    Tier 1               │
│  "Developed?" status     Badge                    Tier 1               │
│  [Develop] button        Button size="sm"         Tier 1               │
│  [View prose] link       Button variant="link"    Tier 1               │
│  [Find evidence]         Button variant="outline"  Tier 1               │
│  Vertical scroll         ScrollArea               Tier 1               │
│  Section dividers        Separator                Tier 1               │
│  Drag reorder            @dnd-kit/sortable         Tier 3 (#3)          │
│  Canvas layout           Resizable + CSS Grid     Tier 3 (#2)          │
│                                                                          │
│  RIGHT RAIL (Agent Channel)                                              │
│  ─────────────────────────                                                │
│  Agent role label        Badge                    Tier 1               │
│  Suggestion cards        Card + Badge + Button    Tier 2 (#2)          │
│  Action buttons          Button                   Tier 1               │
│  Scrollable              ScrollArea               Tier 1               │
│  Loading state           Skeleton + Spinner        Tier 1               │
│                                                                          │
│  BOTTOM BAR                                                              │
│  ──────────                                                              │
│  Capture input           Input                    Tier 1               │
│  Type inference pills    ToggleGroup              Tier 1               │
│  Type inference popup   Popover                  Tier 1               │
│  Connection suggestion  Popover + Card           Tier 2 (#3)          │
│  Next Step button        Button                   Tier 2 (#4)          │
│  Confirmation toast      Sonner                   Tier 1               │
│                                                                          │
│  CANVAS DIMMED           Custom opacity div        Tier 3 (#6)          │
│                                                                          │
│  ── DIRECT: 17    COMPOSED: 4    CUSTOM: 4 ──                           │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  SCREEN 3: FRAGMENT DETAIL (Overlay)                                     │
│  ─────────────────────────────────────                                    │
│                                                                          │
│  Overlay container      Sheet side="right"           Tier 1             │
│  Fragment text          Textarea (read/edit toggle)  Tier 1             │
│  Metadata rows          Label + Badge (×5)           Tier 2 (#7)        │
│  Edge list              Card + HoverCard + Badge     Tier 2 (#8)       │
│  Prose status           Badge                        Tier 1             │
│  [View prose]           Button                        Tier 1             │
│  [Edit content]         Button                        Tier 1             │
│  [Change type]          Select                        Tier 1             │
│  [Branch this]          Button                        Tier 1             │
│  [Delete]               AlertDialog trigger           Tier 1             │
│  [← Back]              Button variant="outline"       Tier 1             │
│  Edge navigation        HoverCard (preview on hover)  Tier 1             │
│                                                                          │
│  ── DIRECT: 9    COMPOSED: 2    CUSTOM: 0 ──                            │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  SCREEN 4: DEVELOP CLAIM (Overlay)                                       │
│  ────────────────────────────────                                         │
│                                                                          │
│  Overlay container      Sheet side="right"           Tier 1             │
│  Claim display          Card                          Tier 1             │
│  Evidence list          Badge (linked evidence)       Tier 1             │
│  Audience selector      RadioGroup                    Tier 1             │
│  Prose draft area       Textarea                       Tier 1             │
│  Streaming text         Custom                        Tier 3 (#7)       │
│  [Keep]                 Button                        Tier 1             │
│  [Retry]               Button variant="outline"       Tier 1             │
│  [Edit draft]          Toggle (read/edit mode)        Tier 1             │
│  [← Back]              Button variant="outline"        Tier 1             │
│                                                                          │
│  ── DIRECT: 8    COMPOSED: 0    CUSTOM: 1 ──                             │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  SCREEN 5: RENDER (Overlay)                                              │
│  ───────────────────────                                                  │
│                                                                          │
│  Overlay container      Sheet side="right"           Tier 1             │
│  Format selector        RadioGroup + Card             Tier 2 (#9)       │
│  Scope checkboxes       Checkbox (per claim)          Tier 1             │
│  Undeveloped warning    Alert                         Tier 1             │
│  [Generate preview]    Button                        Tier 1             │
│  [Copy Markdown]       Button                        Tier 1             │
│  [Download .docx]      Button                        Tier 1             │
│  [Open in editor]      Button                        Tier 1             │
│  [← Back]             Button variant="outline"        Tier 1             │
│                                                                          │
│  ── DIRECT: 7    COMPOSED: 1    CUSTOM: 0 ──                            │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  SCREEN 6: EVOLUTION (Left Rail Expand)                                  │
│  ──────────────────────────────────                                       │
│                                                                          │
│  Expand/collapse        Resizable panel width         Tier 1             │
│  Timeline               Timeline                      Tier 1             │
│  Event type badges     Badge                         Tier 1             │
│  Edge notation          <span> with Badge              Tier 2 (#6)       │
│  [Collapse]            Button                         Tier 1             │
│                                                                          │
│  ── DIRECT: 4    COMPOSED: 1    CUSTOM: 0 ──                            │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Summary: Build Effort

```
┌──────────────────────────────────────────────────────────────────────────┐
│  TOTALS ACROSS ALL 6 SCREENS                                            │
│                                                                          │
│  Tier 1: DIRECT USE           52 element instances from 22 components   │
│  Tier 2: COMPOSED             9 custom compositions from Shadcn atoms  │
│  Tier 3: CUSTOM BUILD         7 components requiring new code           │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────── │
│                                                                          │
│  CUSTOM BUILD DETAIL                                                     │
│                                                                          │
│  #  Component                  Effort    Dependencies                    │
│  ────────────────────────────  ───────   ─────────────────              │
│  1  Workspace Layout          Medium    Resizable + CSS Grid            │
│  2  Argument Skeleton         Medium    Collapsible + ScrollArea + #1  │
│  3  Drag-and-Drop Reorder     Medium    @dnd-kit/sortable (external)   │
│  4  Energy/Confidence Dots    Small     Badge variants                  │
│  5  Type-Coloured Border      Small     Tailwind + Card                 │
│  6  Canvas Backdrop           Small     Sheet + opacity div             │
│  7  Streaming Prose Display   Small     Textarea + stream logic         │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────── │
│                                                                          │
│  THE GOOD NEWS:                                                          │
│                                                                          │
│  • 22 Shadcn components cover ~85% of all UI elements                   │
│  • 9 composed components are straightforward Shadcn combinations       │
│  • Only 3 of 7 custom components are "medium" effort                    │
│  • The 4 "small" custom components are < 1 hour each                   │
│  • NO entirely new interaction paradigms needed in Shadcn               │
│  • The only external dep is @dnd-kit (well-maintained, accessible)     │
│                                                                          │
│  THE ONE WATCH-OUT:                                                      │
│                                                                          │
│  • Shadcn's Sheet overlay normally covers the background.              │
│    We need the canvas VISIBLE (dimmed) behind the sheet.               │
│    This means: Sheet overlay={false} + custom dimming on canvas.       │
│    Small code change, important UX property.                           │
│                                                                          │
│  FUTURE SHAPES (Lattice, Seedbed) WILL NEED:                           │
│                                                                          │
│  • Lattice: graph visualisation library (reactflow or @xyflow)         │
│  • Seedbed: spatial layout engine (canvas/SVG + physics sim)           │
│  • Both are significant custom builds, OUT OF SCOPE for Argument MVP   │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## External Dependencies Beyond Shadcn

| Package | Purpose | When Needed |
|---|---|---|
| **@dnd-kit/core + @dnd-kit/sortable** | Drag-and-drop reorder of fragments within sections | MVP |
| **date-fns** | Relative date formatting ("2h ago", "3 days ago") | MVP |
| **@xyflow/react** (formerly reactflow) | Dependency graph for Lattice shape | Post-MVP |
| **zrender / d3-force / custom SVG** | Constellation layout for Seedbed shape | Post-MVP |
| **@tiptap/react** (optional) | Rich text editing in Develop Claim overlay | Post-MVP |

---

**The bottom line: Shadcn gets you ~85% there.** The remaining 15% is composition (straightforward) and 3 medium-effort custom components (workspace layout, skeleton layout, drag-and-drop). Nothing exotic. No new interaction paradigm needs to be invented at the component level — the paradigm innovation is in how the components are arranged and how data flows between them, not in the components themselves.

Want me to go deeper on any of the custom components, or map this to your tech stack (AstroJS + HeroUI vs. Shadcn + Next.js/React Router)?The audit is done. **85% Shadcn direct**, 9 composed from its atoms, 7 custom (3 medium, 4 trivial), one external dep for MVP. The paradigm innovation lives in composition and data flow, not in exotic UI primitives.

Want me to go deeper on any custom component, or should we start reconciling this with your actual tech stack (AstroJS + HeroUI vs. a Shadcn-based React app)?

---

## Run 10 — AI UX Innovator ✓ COMPLETED

*2026-04-15T03:07:54* · `glm-5.1:cloud` · `7b5fd419...`

### Prompt

I want to try mocking up the workspace screen in an AI UI generator. Give me a prompt I can use for this.

### Response

Here's a prompt you can paste directly into v0, bolt.new, Lovable, or similar:

---

```
Create a desktop web app UI for "The Accretive Workspace" — an AI+Human collaboration tool where the fundamental unit is a TYPED FRAGMENT (not a chat message). This is NOT a chat interface. It's an artefact-centric workspace.

## PRODUCT CONTEXT

This workspace replaces the "wall of text" chat paradigm with typed, decomposable fragments. Each fragment has a type (Claim, Evidence, Question, Assumption, etc.) that determines its colour and behaviour. Fragments are connected by typed edges (supports, challenges, depends-on). The user builds an argument skeleton from fragments, then generates prose per-claim — never the whole document at once.

The current artefact is an argument titled "Why Agent Design Principles Matter" in Argument shape. The agent role is STRUCTURER — it organises, suggests connections, and flags gaps. It does NOT generate walls of text.

## LAYOUT: FIVE FIXED ZONES

Create a 5-zone layout that fills the viewport (no scrolling the page itself, only zones scroll):

```
┌────────────┬────────────────────────────────┬──────────────┐
│  LEFT RAIL │          CANVAS                │  RIGHT RAIL  │
│  (220px)   │     (flex-1, dominant)         │   (320px)    │
│            │                                │              │
│            │                                │              │
│            │                                │              │
│            │                                │              │
│            │                                │              │
├────────────┴────────────────────────────────┴──────────────┤
│                   BOTTOM BAR (fixed, 80px)                  │
│         Capture input (left) │ Next Step button (right)     │
└─────────────────────────────────────────────────────────────┘
```

The LEFT RAIL and RIGHT RAIL are fixed width. The CANVAS takes all remaining space. The BOTTOM BAR spans full width. Zones never move. This is Predictability as Safety — the spatial grammar is permanent.

## ZONE 1: LEFT RAIL (220px, fixed width)

Contains 3 collapsible sections stacked vertically. Use a subtle background colour (zinc-50) to differentiate from canvas.

**Section: ARTEFACTS**
- Header with back arrow (←) and artefact title "Why Agent Design Principles Matter"
- Below title: shape badge "📝 Argument" and fragment count "7 fragments"
- A thin separator line

**Section: EVOLUTION** 
- Header "🕐 Evolution" with a collapse chevron
- Two timeline entries stacked:
  - "🔄 2h ago — +C3 added, C2 revised"
  - "🔄 1d ago — +C1 added"
- Style: compact, muted text, small type-coloured dots before each entry

**Section: SHAPE**
- Header "🧭 Shape" 
- Three radio-style options, only first is active:
  - ● Argument (active, selected)
  - ○ Lattice
  - ○ Seedbed

**Section: QUICK NAV** (at bottom of left rail)
- Small text links: "Claims (3)" "Questions (2)" "Evidence (2)" "Phrases (1)"
- Clicking scrolls canvas to that section

## ZONE 2: CANVAS (dominant, centre)

The artefact skeleton. White background. Scrollable vertically. Content arranged in sections with type-coloured section headers and fragment cards.

**Section: 🔵 CLAIMS (3)**
- Section header: bold, with a blue left border accent (4px), fragment count badge
- Three fragment cards stacked vertically with 12px gap:

  CARD C1: (blue left border, 4px border-l-blue-500)
  ┌────────────────────────────────────────────────────────┐
  │ 🔵 C1 · "Type collision is the root cause of the      │
  │    wall of text problem"                               │
  │                                                        │
  │ 🟢 Evidence: 2  ·  🔴 Questions: 1  ·  ⚡ Developed ✓ │
  │                                                        │
  │ [View prose]                            [Develop]      │
  └────────────────────────────────────────────────────────┘

  CARD C2: (blue left border)
  ┌────────────────────────────────────────────────────────┐
  │ 🔵 C2 · "Agent role should shift by domain"            │
  │                                                        │
  │ 🟢 Evidence: 1  ·  🔴 Questions: 0  ·  ○ Not developed │
  │                                                        │
  │                              [Develop]                  │
  └────────────────────────────────────────────────────────┘

  CARD C3: (blue left border)
  ┌────────────────────────────────────────────────────────┐
  │ 🔵 C3 · "The artefact should be primary, not the      │
  │    conversation"                                       │
  │                                                        │
  │ 🟢 Evidence: 0  ·  🔴 Questions: 2  ·  ○ Not developed │
  │                                                        │
  │                              [Develop]                  │
  └────────────────────────────────────────────────────────┘

- Each card has: blue left border (4px), fragment type icon+label, content text (truncated to 2 lines), metadata badges, and action button(s)
- Cards have subtle hover state (slight shadow lift)
- "Developed ✓" badge is green, "Not developed" is muted/grey
- C3's evidence count is red/amber to flag it as unsupported

**Section: 🔴 QUESTIONS (2)** 
- Red left border accent on section header
- Two question cards (red left border, 4px border-l-red-400):

  CARD Q1: (red left border)
  ┌────────────────────────────────────────────────────────┐
  │ 🔴 Q1 · "Is this true for all LLMs or just current    │
  │    chat interfaces?"                                   │
  │                                                        │
  │ → Attached to: C1, C3                                 │
  │ [Find evidence]  [Reframe as claim]                    │
  └────────────────────────────────────────────────────────┘

  CARD Q2: (red left border)
  ┌────────────────────────────────────────────────────────┐
  │ 🔴 Q2 · "What does the user research say?"             │
  │                                                        │
  │ → Attached to: C3                                     │
  │ [Find evidence]  [Reframe as claim]                    │
  └────────────────────────────────────────────────────────┘

**Section: 🟢 EVIDENCE (2)**
- Green left border accent on section header
- Two evidence cards (green left border, 4px border-l-green-500):

  CARD E1: (green left border)
  ┌────────────────────────────────────────────────────────┐
  │ 🟢 E1 · "Shannon 1948 — channel capacity requires      │
  │    encoding for efficient decode"                      │
  │                                                        │
  │ → Supports C1  ·  🟢 High confidence                  │
  └────────────────────────────────────────────────────────┘

  CARD E2: (green left border)
  ┌────────────────────────────────────────────────────────┐
  │ 🟢 E2 · "Three use cases validated the same flow       │
  │    pattern"                                            │
  │                                                        │
  │ → Supports C2  ·  🟡 Medium confidence                 │
  └────────────────────────────────────────────────────────┘

**Section: 💬 PHRASES (1)**
- Purple left border accent on section header
- One phrase card (purple left border, 4px border-l-purple-500):

  CARD P1: (purple left border)
  ┌────────────────────────────────────────────────────────┐
  │ 💬 P1 · "The fundamental unit of AI+Human collab       │
  │    is the artefact"                                     │
  │                                                        │
  │ → Linked to: C3                                        │
  │ [Copy]                                                 │
  └────────────────────────────────────────────────────────┘

Sections are separated by 24px spacing. Section headers are sticky (stay visible when scrolling within that section).

## ZONE 3: RIGHT RAIL (320px, fixed width)

The agent channel. Light zinc background. Contains typed agent suggestions — NOT prose. Each suggestion is a small card with a type indicator and an action button.

**Header:**
"🤖 StructurER" in small caps, muted. Below: thin separator.

**Three suggestion cards stacked:**

SUGGESTION 1: (amber-tinted background, warning icon)
┌──────────────────────────────────────┐
│ 💡 C3 has 2 questions and no         │
│ evidence. This claim is unsupported. │
│                                      │
│ [Find evidence for C3] [Reframe Q2]  │
└──────────────────────────────────────┘

SUGGESTION 2: (blue-tinted background, connection icon)
┌──────────────────────────────────────┐
│ 🔗 C1 and C3 share the question Q1. │
│ Answering Q1 would support both.     │
│                                      │
│ [Find evidence for Q1]               │
└──────────────────────────────────────┘

SUGGESTION 3: (neutral background, develop icon)
┌──────────────────────────────────────┐
│ ⚡ C2 hasn't been developed yet.      │
│ Ready to generate prose?             │
│                                      │
│ [Develop C2]                         │
└──────────────────────────────────────┘

Each suggestion card is compact — 2-3 lines max, one clear action, no walls of text. The agent NEVER generates prose in this rail. It only surfaces typed observations and offers typed actions.

## ZONE 4: BOTTOM BAR (full width, 80px, fixed at bottom)

Two sections: Capture input (left 70%) and Next Step (right 30%).

**Capture Bar (left):**
A single-line text input spanning most of the bar. Placeholder: "⚡ Type or drop anything here..."
Small icon indicating supported input types: text, paste, drag.
Rounded, prominent, feels like the primary action surface.

**Next Step (right):**
A single button with contextual text:
"💡 Find evidence for C3 →"
This button changes based on what the agent suggests. Always one action. Always visible.

The bottom bar has a subtle top border and slight background tint to separate it from the canvas.

## OVERALL AESTHETIC

- Clean, minimal, generous whitespace
- Font: system font (Inter/sans-serif), 14px body, 12px metadata
- Colour system: blue=claim, green=evidence, red=question, purple=phrase, amber=assumption, amber/warning=agent-flagged
- Cards have subtle rounded corners (8px), thin borders (1px zinc-200), left accent borders by type (4px)
- No shadows except on hover (subtle lift)
- Backgrounds: canvas=white, rails=zinc-50, bottom bar=zinc-50, suggestions=zinc-50 with type-tinted accents
- The CANVAS dominates visually — it's where you live. The rails are supporting players.
- No chat bubbles. No message history. No "AI said:" blocks. Only typed fragments and typed suggestions.
- The overall feel should be more like a structured document editor than a chat app. Think: Notion meets Figma meets a knowledge graph — but the nodes are typed fragments, not pages or vector objects.
```

---

A few tips for getting the best result:

1. **If the generator produces a chat-like layout**, add: *"This is NOT a chat interface. There are no message bubbles, no chat history, no AI response blocks. The centre is a structured document skeleton made of typed fragment cards arranged by section."*

2. **If the agent suggestions look like prose paragraphs**, add: *"The right rail suggestions must be MAXIMUM 3 lines each. They are typed observations with action buttons, not text blocks. Think of them as alert cards, not chat messages."*

3. **If fragment cards all look the same**, add: *"Each fragment card type has a DISTINCT left border colour: Claims are blue (border-l-blue-500), Questions are red (border-l-red-400), Evidence is green (border-l-green-500), Phrases are purple (border-l-purple-500). The type is visually encoded — you should be able to tell what type a fragment is from colour alone."*

4. **If the capture bar looks like a search bar**, add: *"The capture bar is NOT a search field. It's a zero-friction input that accepts any thought, question, claim, or fragment. It should feel like a scratchpad input — always visible, always ready, minimal friction."*

Good luck. Would love to see what it produces — share the result and I'll help you refine.

---
