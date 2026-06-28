# Agentic AI Starter Program — Design Thinking Document
### Captured from a design session with Pete Argent | June 23, 2026

---

## 1. The Vision

> *"I believe the world will solve more problems faster if more people know how to design and build technology."*

Pete Argent is developing the **Agentic AI Starter Program** — a 6-week, hands-on cohort course built on Agno AgentOS and VS Code Copilot. The program targets savvy AI users, young professionals, and anyone motivated to build a career in the emerging agentic AI economy.

The program is not designed to produce experts. It is designed to produce **confident, self-directed learners who keep going** — people who have crossed the early hurdles, found their footing, and have a community to support their continuing journey.

Pete sees himself as a **facilitator of learning through play**.

---

## 2. Origin Story & Design Motivation

Pete spent 12 months experimenting with multi-agent frameworks — playing, failing, rebuilding. The early months were hard: conceptual fog, false starts, and a sense of intimidation. What pushed him through was a real, motivating goal (automating assignment marking) and a "looming dread" that turned into curiosity and eventually momentum.

This lived experience is the course's most important design input. Pete now knows the shape of the learning curve and can compress it for others. The course is designed around the moments where people typically stall — not just the content they need to absorb.

**Key design principle derived from this:** A real, personal goal is what pulls learners through the hard early phase. Engineering that goal-attachment early is as important as the curriculum itself.

---

## 3. Core Philosophy

### The "Play to Learn" Frame
- Play lowers stakes — experiments are allowed to fail
- Play invites curiosity — you move toward something interesting, not away from something scary
- The tools (Agno, VS Code Copilot, frameworks) are toys before they are professional instruments
- Play is intrinsically rewarding in a way that "completing a module" is not

### Pete's LX Truths (applied to this program)
- **Student confidence is key** — the first build matters more than the first concept
- **Learning should be fun** — every session should have an element of enjoyment by design
- **You learn more when you teach** — peer-to-peer learning is central, not supplementary
- **Ask, don't tell** — facilitation over instruction; questions open possibility
- **Don't fear technology — embrace it** — name the dread early and reframe it as energy

---

## 4. The Real Success Metric

Most courses measure completion or assessment scores. This program measures something harder and more meaningful:

> **Do learners leave with the confidence and habit to keep building on their own?**

Secondary indicators:
- Learners can name a project they want to build
- Learners feel they belong to a community
- Learners have a method (play → experiment → reflect → iterate) they trust
- Learners are not waiting for permission to start the next thing

---

## 5. The Emotional Arc of the Course

The course must be designed to hold this emotional journey — not just the content journey:

| Stage         | Feeling Learners Have        | Course's Job                                      |
|---------------|------------------------------|---------------------------------------------------|
| Arrival       | Curious but uncertain        | Validate the feeling; lower the barrier           |
| Early concepts| Foggy, slightly intimidated  | Short wins; real examples; normalise confusion    |
| First build   | Fragile confidence           | Celebrate loudly; keep it simple                  |
| First failure | Doubt                        | Frame failure as data, not verdict                |
| Goal clarity  | Motivated                    | Lock in their personal project idea               |
| Competence    | Energy and momentum          | Get out of the way; let them build                |

---

## 6. Module 1: Agents 101 — Design Decisions

### Why Module 1 is the Highest-Risk Moment
This is the beginning — before any wins, before anything has clicked. The most important job of Agents 101 is not to teach content. It is to:
- Eliminate the dread (name it directly)
- Create an early win (something that works, before concepts are fully understood)
- Attach a real goal (even a vague one) as early as possible

### Learner Outcomes for Agents 101

**What they should know:**
- The definition of an AI agent and how it differs from a chatbot or plain LLM call
- Core components: model, instructions, tools, memory, context
- The perception–reason–act loop
- 3–5 real-world agent examples in domains they recognise
- Main agentic frameworks and where Agno sits in that landscape
- Honest strengths and limitations of agentic systems

**What they should feel:**
- Curious and energised — agents feel like a genuinely new capability
- Capable — this is learnable and buildable
- Grounded — not over-hyped; realistic about what agents can and can't do today
- Personally connected — they can already see an application relevant to them

**What they should think:**
- "This is a meaningful step-change from prompting a chatbot"
- "I can see why this needs a framework"
- "The limitations are real, but workable"
- "Agno seems like a sensible place to start"

**How they should think:**
- With a systems lens — an agent is interacting components, not a black box
- With appropriate scepticism — "what could go wrong here?" as a reflex
- With possibility thinking — "what could I build with this?"
- With framework awareness — tools are choices with trade-offs, not defaults

**What they can explain:**
- What makes something an agent vs. a plain LLM call — in plain language
- Why agents need tools, and what happens without them
- The difference between agent memory and conversation history
- Why frameworks exist and what problem they solve
- What Agno is and why the course uses it

**What they can do:**
- Recognise an agentic system when they encounter one
- Identify a plausible agent use case in their own domain
- Hold an informed conversation with a peer, manager, or client
- Approach Module 1's hands-on build with conceptual scaffolding in place

### Glossary: Agents 101 Key Terms
- **Agent** — A system that perceives, reasons, and acts autonomously across multiple steps
- **Model** — The LLM powering the agent's reasoning; the "brain"
- **Tool** — A function the agent calls to interact with the world
- **Memory** — Short-term (session) or long-term (persistent) information storage
- **Context** — All information available to the agent at a given moment
- **Instructions** — The system prompt defining role, behaviour, and constraints
- **Perception–Reason–Act loop** — The fundamental operating cycle of an agent
- **Agentic framework** — Scaffolding that handles orchestration, tool integration, and memory
- **Agno / AgentOS** — The framework used in this course; lightweight and production-ready
- **Multi-agent system** — Multiple agents working together with defined roles
- **Hallucination** — Confident but incorrect LLM output; a key agentic risk
- **Tool failure** — When a called tool returns unexpected or no results
- **Human-in-the-Loop (HITL)** — Human review/approval built into a workflow
- **Orchestration** — Coordination of agents, tools, and steps toward a complex goal

---

## 7. AI-Assisted Learning Design

### The Core Mechanic (Prototype Phase)
For a savvy AI user cohort, the prompt activity works as a **conversation starter with their own LLM** — not an exercise with right/wrong answers. Three steps per topic:

1. **Starter prompt** — pre-written, copy-ready, with one `[personalise this]` placeholder
2. **Run it** — learner pastes into their LLM of choice and reads the response
3. **One-line capture** — open text field: *"What's the most useful thing you just learned, or the question it raised for you?"*

### Example Prompts: Agents 101

**Topic 1 — Defining an Agent:**
> "I work as a [your role] in [your industry]. Explain what an AI agent is, using examples and language that would make sense to someone in my field. Keep it practical and jargon-light."

**Topic 2 — Examples of Useful Agents:**
> "I work in [your industry/role]. Give me five examples of AI agents that are either already being used or could realistically be built for my field. For each one, describe what the agent does, what tools it uses, and what problem it solves."

**Topic 3 — Strengths and Limitations:**
> "I'm learning to build AI agents. Give me an honest, balanced assessment of what agentic AI systems are genuinely good at versus where they commonly fail. Include at least two real-world failure modes I should be aware of as someone who will be deploying these systems."

**Topic 4 — Agentic Frameworks:**
> "Give me a brief overview of the main agentic AI frameworks available right now. For each one, describe its main use case, its strengths, and the type of developer it suits best. I am [a beginner / somewhat technical / a developer] — adjust the depth accordingly."

**Topic 5 — Agno Framework:**
> "What do you know about the Agno AgentOS framework for building AI agents? Describe its architecture, its key features, and how it compares to other frameworks. Be honest if your knowledge is limited or potentially out of date."
> ⚠️ *Note: Agno is newer — your LLM may have gaps. That's the lesson.*

### Why This Approach Works
- Savvy AI users are comfortable prompting — this meets them where they are
- Personalised responses accelerate comprehension and relevance
- The one-line capture is the prototype data payload for the future learner agent
- No right/wrong pressure; the goal is insight and curiosity, not correctness

### Future Vision: The Learner Agent
The prompt-driven mechanic is a manual prototype of a future conversational agent that:
- Learns the learner's role, goals, prior knowledge, and domain
- Adapts explanations, examples, and depth in real time
- Tracks patterns across the cohort to surface what the course design needs to improve
- Eventually replaces the static prompt with a genuine learning conversation

**Learner data the agent needs:**
- Role, industry, technical background, AI experience level
- Why they enrolled; what they want to build; their definition of success
- Preferred explanation style and depth
- One-line captures from each prompt activity (the seed data)
- Confidence signals, engagement patterns, and frustration indicators

---

## 8. Agentic AI Specialisations

Learners leave the Starter Program at the entry point to one of six specialisation paths:

| Specialisation | Best Suited To | Core Competency |
|---|---|---|
| **Systems Engineer** | Developers, ML engineers | Building and deploying agents in production |
| **Multi-Agent Designer** | Architects, senior engineers | Coordinating agent teams with defined roles |
| **Workflow Architect** | BAs, operations leads, process engineers | Structured, auditable, HITL-safe workflows |
| **AI Product Manager** | PMs, UX designers, consultants | Product strategy and UX for agentic applications |
| **Safety & Governance** | Risk, compliance, policy professionals | Guardrails, audits, and responsible deployment |
| **Domain Specialist** | Deep domain experts + AI practitioners | Expert-level agents in specific fields |

Knowing a learner's likely path at enrolment allows the learning agent to personalise examples, project ideas, and module emphasis throughout the 6 weeks.

---

## 9. The Cohort Model as the Product

The Telegram group, weekly webinars, and peer-to-peer dynamics are not supplementary to the course — they ARE the course's most important retention and motivation mechanism.

- **Social accountability** — showing up because others are there
- **Normalised struggle** — peers hitting the same walls reduces shame
- **Serendipitous learning** — domain diversity in the cohort generates insights no single instructor could provide
- **Community outlasts the course** — the network is the long-term value proposition

Pete's webinar role: orchestrate peer insight, model play, celebrate experiments that didn't work, and ask more than tell.

---

## 10. The Program Ecosystem (Future State)

| Stage       | Program                     | Goal                                            |
|-------------|-----------------------------|-------------------------------------------------|
| Start       | Agentic AI Starter (now)    | Confident, self-directed, community member      |
| Deepen      | Agentic AI Builder          | Production-ready agents and workflows           |
| Specialise  | Track-based courses         | Credible specialisation (6 paths above)         |
| Lead        | Facilitator/Mentor program  | Peer teachers in future cohorts                 |

**The flywheel:** Best graduates become community leaders and peer mentors who make the next cohort richer for everyone. The first few cohorts are deliberately a refinement exercise — their patterns, struggles, and project ideas write the follow-on curriculum.

---

## 11. Key Insights from This Design Session

1. **The real product is confidence and momentum, not knowledge** — expertise is time plus practice; what the course installs is the will to continue

2. **Pete's personal learning journey is the course's best design blueprint** — the emotional arc he experienced is the arc to engineer for learners

3. **Goal-attachment is the retention mechanism** — learners who can name what they want to build by end of Module 1 are far more likely to complete the course

4. **The one-line capture is the most important design element in the AI-assisted prototype** — it's low friction, builds reflection habit, and seeds the future learner agent

5. **"Play to learn" is a pedagogical position, not just a tone choice** — it has direct consequences for how Pete facilitates, how failure is framed, and how wins are celebrated

6. **The Telegram cohort is a product feature, not an afterthought** — it should be designed as deliberately as the content

7. **The first few cohorts are a research exercise** — patterns of struggle, acceleration, and project choice across cohorts write the follow-on curriculum automatically

8. **Naming the dread early is a trust-building act** — Pete's origin story belongs in the course introduction, not on the marketing page

9. **Agentic AI specialisations give learners a horizon** — knowing where this can lead sustains motivation through the hard early weeks

10. **The learner agent prototype starts with manual prompts and one-line captures** — this is the right minimum viable version; build the data collection before building the intelligence

---

*Document prepared: June 23, 2026*
*Program: Agentic AI Starter Program — Zero Team Space*
*Author context: Pete Argent, Technology Educator & Learning Experience Designer*
