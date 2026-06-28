# Article 1: "The AI Team That Keeps Dropping the Ball"

### *Why multi-agent systems are failing in production — and what the real problem is*

**Narrative arc:** Start with genuine excitement about agentic AI → show why it keeps breaking in practice → reveal that the root cause isn't the AI, it's the architecture. End on a cliffhanger: "there's a structural answer to this, and it comes from how we learned to build reliable software."

***

## Part 1 — The Promise Is Real

**Section 1.1: What agentic AI actually means**
> *Opens with: IMDA Model AI Governance Framework for Agentic AI (May 2026)*  — describes the shift from "AI that answers" to "AI that acts", using tools, making plans, and executing tasks autonomously.[^1]

- An agent isn't just a chatbot — it takes actions, uses tools, makes decisions, and hands work to other agents
- The appeal: imagine a pipeline where one agent researches, another analyses, another drafts, another reviews — all while you focus on the parts only you can do
- This is already happening in enterprises today; the technology works in controlled settings

**Section 1.2: Why businesses are moving fast**
> *Opens with: EWSolutions Agentic AI Governance (2026)*  — documents the rapid shift from generative AI to agentic AI as the fastest-growing enterprise technology trend of 2026.[^2]

- Speed, consistency, and scale are the draws — things that normally require coordination across teams of humans
- The pilot results look impressive: individual tasks run faster, outputs are consistent, costs fall
- The problem emerges later, at scale, when agents have to work *together*

***

## Part 2 — The Reality: Four Ways Agentic Systems Break

**Section 2.1: Bad briefs produce bad work**
> *Opens with: Cribl "More Agents, More Problems" (2025)*  — identifies vague task specifications and poor decomposition as the most common source of multi-agent production failures, with failure rates exceeding 50%.[^3]

- Just like a new hire given a vague assignment with no success criteria, an agent without a precise definition of "done" produces confidently structured nonsense
- Most multi-agent systems are built around conversations, not contracts — there's no typed definition of what the task is or what a correct output looks like
- When every participant interprets the brief differently, the pipeline compounds the error, not corrects it

**Section 2.2: The broken telephone problem**
> *Opens with: Galileo "9 Key Challenges in Monitoring Multi-Agent Systems at Scale" (2025)*  — describes context loss, misaligned state, and misinterpreted handoffs between agents as among the hardest operational problems at scale.[^4]

- When agents pass work to each other, they're not sharing understanding — they're sharing text
- Context dropped at one handoff becomes confusion at the next; small misinterpretations amplify across a pipeline
- Unlike human teams, agents don't ask clarifying questions or flag when something "feels off"

**Section 2.3: Checking the wrong thing**
> *Opens with: rmax.ai "Agent Execution Contracts" (2025)*  — distinguishes between "did the agent run?" and "was the goal achieved?", arguing that current monitoring practices conflate execution with success.[^5]

- Most systems check whether the task completed, not whether the objective was met
- A flight that departs on time but lands in the wrong city still "ran successfully" by most agent monitoring standards
- The gap between execution and outcome is where silent failure lives — and silent failure at scale is the most dangerous kind

**Section 2.4: The Accountability Gap**
> *Opens with: LinkedIn / Victor Omoboye "Challenges of Deploying Multi-Agent Systems in Enterprises" (2026)*  — names the "Accountability Gap" directly: when something goes wrong in a multi-agent pipeline, it is often impossible to trace which agent made the decision that caused the failure.[^6]

- Multi-agent pipelines distribute responsibility across participants — which means when something goes wrong, no one and nothing is clearly accountable
- Debugging is exponentially harder: you're tracing a sequence of decisions made by autonomous components, not a linear stack trace
- This isn't a logging problem — it's an architectural one

***

## Part 3 — The Root Cause: It's a Design Problem, Not an AI Problem

**Section 3.1: The instinct is wrong — more agents and bigger models make it worse**
> *Opens with: Cribl (2025)*  — explicitly warns that the common response to multi-agent failures (adding more agents, switching to larger models) typically increases complexity and failure surface rather than improving reliability.[^3]

- The failure pattern is predictable: a pilot works, it gets expanded, agents multiply, and the failure rate climbs faster than the capability
- Organisations are debugging models when they should be redesigning workflows
- The problem isn't what the agents can do — it's how the system is structured around them

**Section 3.2: Multi-agent systems are built like conversations, not like systems**
> *Opens with: Pravitech "Why Agents Succeed and Systems Fail" (2026)*  — argues that the core architectural failure of most agentic deployments is treating agent interactions as prompt-level conversations rather than governed, contract-bound systems with enforced handoffs.[^7]

- Reliable software doesn't trust that code will behave — it enforces behaviour with types, schemas, tests, and contracts
- Agentic workflows built as "chat between agents" have none of these guardrails
- The result is a system that works beautifully in demos and fails unpredictably in production

**Section 3.3: Governance must be architected in, not bolted on**
> *Opens with: "Governance by Design: Architecting Agentic AI for Accountability" (ESSEC/Accenture, 2026)*  — shows through case study analysis that organisations successfully scaling multi-agent systems embedded governance, boundary enforcement, and human oversight structurally — organisations that didn't, couldn't scale.[^8]

- The organisations that successfully scale aren't using better models — they're using better design disciplines
- The question isn't "how do we make the agents smarter?" — it's "how do we build the system so that failure is visible, recoverable, and bounded?"
- In the next article, we'll look at what that design discipline looks like in practice

> **Closing hook:** *"We solved this problem in software engineering decades ago. The answer was contracts, schemas, and enforced boundaries. Agentic systems need the same treatment — and a new methodology is emerging to do exactly that."*

***
***

# Article 2: "Building AI Systems Worthy of Trust"

### *A design discipline for agentic workflows that actually work in production*

**Narrative arc:** Picks up the "design, not capability" thread from Article 1 → introduces CAWDP as a structured response to the specific failures named → shows what this looks like concretely → closes on the larger idea that this is ultimately about trust infrastructure for organisations.

***

## Part 1 — From Conversations to Contracts

**Section 1.1: What makes software reliable — and why agents need the same**
> *Opens with: rmax.ai "Agent Execution Contracts" (2025)*  — argues that as AI agents become autonomous system actors, the separation between specification, testing, and execution becomes a liability; only machine-readable contracts that collapse these into a single governing artefact can make agents reliably safe.[^5]

- In engineering, we don't trust that code will behave correctly — we prove it with types, schemas, and enforced invariants
- The same logic applies to agentic systems: you can't fix unpredictable behaviour with better prompts — you need structure that the system enforces, not just declares
- This is the insight behind CAWDP (Complementarity-Driven Agentic Workflow Design Process) — a design methodology that treats every agent interaction as a governed, typed, auditable contract

**Section 1.2: Start with identity, not capability**
> *Opens with: "Governance by Design" (ESSEC/Accenture, 2026)*  — finds that the organisations which successfully governed multi-agent systems started by defining the *purpose and boundaries* of each agent role before defining capabilities — not the other way around.[^8]

- The instinct when building an agentic workflow is to ask "what can this agent do?" — CAWDP starts with a different question: "what is this workflow *for*, what would violate its integrity, and what does failure look like?"
- Five identity questions — answered before any capability discussion — determine 40–70% of the downstream design
- You can't enforce a boundary you haven't defined; identity comes first

**Section 1.3: Design the work before assigning it**
> *Opens with: ISB research "Modelling AI-Human Collaboration as a Multi-Agent Adaptation" (2025)*  — finds that optimal human-AI task allocation depends primarily on task structure (decomposability, modularity, reversibility) — not on model capability alone.[^9]

- CAWDP decomposes every task to a single cognitive type, a single output artefact, and a single authority owner before asking who should do it
- Allocation follows a rigorous two-pass model: first, who has the highest capability gap? Second, what factors (irreversibility, experience dependency, cold-start difficulty) override that?
- The core principle: **the agent prepares judgment; the human makes judgment** — and that boundary is structural, not optional

***

## Part 2 — Building Systems That Fail Safely

**Section 2.1: Stress-test before you build**
> *Opens with: IMDA Model AI Governance Framework for Agentic AI (May 2026)*  — recommends that agentic AI systems be subjected to adversarial scenario planning and failure mode analysis *before* deployment, not after — and that human approval mechanisms be embedded at the system level, not the prompt level.[^1]

- CAWDP's Phase 5 (Event Storming) maps every failure event and recovery path before a single line of code is written
- The happy path is not the design — the failure cases are
- Every failure mode identified in task decomposition gets a detection mechanism, a recovery action, and a prevention mechanism assigned before the system is built

**Section 2.2: Make handoffs typed contracts, not conversations**
> *Opens with: Pravitech "Why Agents Succeed and Systems Fail" (2026)*  — documents how current agentic systems fail at handoffs because outputs are untyped natural language rather than governed structured data; the solution is schema-enforced contracts at every boundary.[^7]

- CAWDP's contract layer gives every participant a typed input schema, typed output schema, authority boundaries, and an enforcement regime
- Enforcement is explicitly tiered: **Regime 1** (declared to the agent), **Regime 2** (detected after the fact), **Regime 3** (structurally prevented) — and every boundary must state which regime it targets and why
- Anything that *can't* reach Regime 3 goes into an Unenforceable Elements Register — making the gap between intent and enforcement explicit and visible

**Section 2.3: Verification independence and the audit trail**
> *Opens with: Galileo "9 Key Challenges in Monitoring Multi-Agent Systems at Scale" (2025)*  — identifies the absence of reasoning-chain-level observability (not just action logs) as the critical gap in current multi-agent monitoring, making root-cause analysis nearly impossible after failures.[^4]

- CAWDP builds in a principle borrowed from software quality assurance: the participant that produces an output is *never* the same one that verifies it
- Every output carries epistemic metadata — how confident, based on what, with what limitations — so uncertainty is visible at each handoff, not hidden
- The result: failures are visible and recoverable, not silent and compounding

***

## Part 3 — Trust as Infrastructure

**Section 3.1: The organisational dimension of agentic AI**
> *Opens with: ITECS "Agentic AI Governance Framework 2026"*  — argues that the governance of agentic AI systems is fundamentally an organisational problem, not just a technical one: it requires inventory, identity, least privilege, observability, and continuous compliance — all of which are as much about process and culture as tooling.[^10]

- Agentic systems at scale require organisational trust — stakeholders, regulators, and customers need to be confident that the system behaves as designed, and can prove it
- CAWDP's audit trail, contract primitives, and EVOLVE cycle create the raw material for this: every decision is traceable, every boundary is documented, every drift is flagged
- This isn't a governance layer on top of a workflow — it *is* the workflow

**Section 3.2: Human-agent complementarity, not replacement**
> *Opens with: "Task Orchestration in Hybrid Workflows" (fupress.org, 2025)*  — finds that the best-performing human-AI systems are those that dynamically allocate tasks based on genuine complementarity — each actor doing what they are structurally better at, with smooth handoffs rather than rigid role assignments.[^11]

- The goal was never full autonomy — it was the right human in the right place with the right information at the right moment
- CAWDP's Human Enrichment Assessment explicitly measures whether the system expands or constrains human capability: the target is "Amplifying" or "Liberating", not "Constraining"
- Automation that removes humans from judgment isn't progress — it's a liability

**Section 3.3: Trust is earned through structure, not assertion**
> *Opens with: Singapore IMDA Model AI Governance Framework (May 2026)*  — concludes that trust in agentic AI systems cannot be asserted through declarations of intent or responsible AI principles alone; it must be earned through verifiable structural controls, human oversight mechanisms, and continuous monitoring.[^1]

- Organisations that say "trust our AI" without structural evidence of how it behaves are asking for trust on credit
- CAWDP's position: trust is a consequence of observable, governed, auditable system behaviour — earned incrementally through demonstrated reliability
- The question every leader deploying agentic AI should ask: *not* "does this work?" — but "is it built in a way that's worthy of trust?"

> **Closing line:** *"The organisations that will lead in the agentic era won't be the ones who moved fastest. They'll be the ones who built systems that people — employees, customers, regulators — can actually trust."*

***

## What You Have Now

|  | Article 1 | Article 2 |
| :-- | :-- | :-- |
| **Core question** | Why do multi-agent systems keep failing? | How do you build ones that actually work? |
| **Protagonist** | The problem | The methodology |
| **Tone** | Diagnostic, slightly provocative | Constructive, authoritative |
| **Ends on** | "It's a design problem — and design has an answer" | "Trust is infrastructure — here's how to build it" |
| **External sources** | Cribl, Galileo, IMDA, EWSolutions, rmax.ai, LinkedIn/Omoboye | IMDA, rmax.ai, ESSEC/Accenture, Pravitech, Galileo, ITECS, ISB, fupress.org |
| **CAWDP presence** | Hinted at in closing hook only | Central, introduced section by section |

<div align="center">⁂</div>

[^1]: <https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf>

[^2]: <https://www.ewsolutions.com/agentic-ai-governance/>

[^3]: <https://www.reddit.com/r/AI_Agents/comments/1snw1ec/what_challenges_arise_when_deploying_multiagent/>

[^4]: <https://galileo.ai/blog/challenges-monitoring-multi-agent-systems>

[^5]: <https://rmax.ai/notes/agent-execution-contracts/>

[^6]: <https://www.linkedin.com/pulse/challenges-deploying-multi-agent-systems-enterprises-victor-omoboye-bbb8e>

[^7]: <https://pravitech.substack.com/p/agentic-ai-specs-contracts>

[^8]: <https://arxiv.org/html/2605.20210v1>

[^9]: <https://www.emergentmind.com/papers/2504.20903>

[^10]: <https://itecsonline.com/post/agentic-ai-governance-2026-guide>

[^11]: <https://fupress.org/journal/AISSII/index.php/journal/article/view/67>
