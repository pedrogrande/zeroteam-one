# Agent [Autonomous Agent]

An agent is a program that doesn't need to be coded because it is powered by an LLM.

Think of it like this: 

* A regular program is a recipe. Follow each step exactly, get the same result every time.   
* An agent is more like giving someone a goal and some guidelines, then letting them figure out how to get there.

An agent reviews 50 rental contracts and flags the ones with unusual termination clauses. A regular program can't do this, it would need someone to write a rule for every possible clause. The agent uses its understanding of language to find what's unusual, even if it's never seen that particular clause before.

**Agents are not beings.** They don't have thoughts, feelings, or opinions. They are specifications, written instructions that, when invoked, produce work. An agent "lives" only from the moment it's started to the moment it finishes. It doesn't exist between uses. The specification persists. The agent is temporary.

**An agent's capability is entirely dependent on what it's been given.** Give it clear instructions and good information, it produces good work. Give it vague instructions or bad information, it produces plausible-looking mistakes. The agent doesn't know the difference. That's the human's job.

---

## What an agent needs to exist

### Someone to start it [Invocation / Trigger]

An agent doesn't start itself. Something has to set it going, a person clicking a button, a schedule running every hour, or another system sending it a signal.

Like a tool in a garden shed, it sits there until someone picks it up and uses it. The agent doesn't decide "I should check those contracts now." It waits to be told.

### A meaningful goal [Purpose / Intent]

An agent needs to know what it's trying to achieve. Not just a task ("process this document") but a reason ("find clauses that could cost the client money"). The better the goal, the better the agent's judgment about what matters and what doesn't.

A goal without meaning is just a program. "Find all paragraphs longer than 200 words" is a program. "Find paragraphs where the landlord might be hiding something" is a goal that requires judgment.

### The ability to receive and understand information [Perception / Input Processing]

An agent takes in information, text, data, signals, and makes sense of it. It reads a contract and understands that "termination without cause upon 30 days notice" means something different from "termination for breach upon 7 days notice."

The quality of what the agent produces depends directly on the quality of what it receives. Feed it a blurry scan instead of clear text, and it will misread clauses. Feed it a contract with outdated clauses mixed in with current ones, and it might flag the wrong things.

### The ability to figure out how to achieve its goal [Reasoning / Decision-Making]

An agent works out its own path to the goal. It considers options, picks the one most likely to succeed, and adjusts if new information comes in. You give it the "what" and enough guidance on the "how", but not step-by-step instructions. If you're giving step-by-step instructions, you've written a program, not an agent.

This is what makes agents feel magical. They don't just follow rules, they work things out. But it's not magic. The model inside the agent has seen millions of examples of how humans reason through problems, and it reproduces those patterns. It looks like thinking. Whether it IS thinking is a philosophical question. For practical purposes: the output resembles reasoning, and the reliability of that reasoning depends on the quality of what the agent was given.

### A way to make something happen [Action / Means of Causing Change]

An agent needs to be able to do something that changes the world, even if that change is just "a record now exists that this was done." An agent that reads a contract but can't flag the risky clauses, write a summary, or notify anyone, that agent hasn't done anything useful.

Some of what the agent does comes from inside: it can think, write, summarize, and recommend. These are part of what the agent IS. Some of what it does comes from the environment it's been given access to: it can search a database, send an email, or update a file. These are part of where the agent WORKS. Both matter.

### A world to work in [Environment / Operating Context]

An agent exists within an environment that gives it both capability and limits. The environment provides the tools the agent can access, the information it can reach, and the boundaries of what it's allowed to do. The same agent specification in a locked-down environment with no database access is fundamentally different from that same specification in an environment with full access.

The environment gives the agent its agency. It also constrains it. An agent with access to a legal database can check whether a clause is standard. Without that access, it can only guess based on what it already knows.

---

## What an agent is made of

### A point of view [Identity / Role]

An agent needs to know who it IS. Not just what it does, but what kind of worker it is. A reviewer looks for problems. A researcher finds information. A writer creates content. A coordinator brings things together. The identity shapes how the agent approaches every task.

An agent without identity is just ChatGPT, helpful but generic. An agent with identity is like a specialist: it brings a perspective, a philosophy, an approach. It knows what it's for, and, just as importantly, it knows what it's NOT for.

### High-level guidance [Instructions / Directives]

An agent needs instructions on how to approach its goal. But these must be high-level: "Look for clauses that shift risk to the tenant" not "Read paragraph 3, check if it contains the word 'indemnify', if yes then..." Low-level, step-by-step instructions are a program. The agent should be given the intention, not the procedure.

The instructions are not binding in the way program code is. An agent might interpret them differently than you expected. That's the trade-off: you get flexibility and judgment, but you also get the possibility of surprise.

### Relevant knowledge [Knowledge / Context]

An agent needs information to work with. But more is not always better. The goal is the minimum sufficient information, enough for the agent to make smart decisions, not so much that it gets confused or wastes processing on irrelevance.

With humans, we can trust that more knowledge is usually better because we naturally filter out what's irrelevant. Agents don't. Every piece of information they're given gets processed, costs money, and can potentially lead them in the wrong direction.

### A way to learn from experience [Memory / Persistent State]

An agent can be given the ability to remember things from one use to the next. This memory lets it improve: "Last time I flagged this clause, the human said it was fine, I should adjust." Memory is how the agent's specification gets smarter over time.

But memory needs curation, not just accumulation. The agent remembers everything it's told, including mistakes and outdated information. Without curation, memory becomes a liability, the agent repeats errors from the past with confidence.

### An intelligence engine [Reasoning Substrate / LLM Model]

The model is what makes an agent an agent instead of a program. It's the engine that takes instructions, knowledge, and information, and turns them into decisions and actions. Without the model, nothing else works, the agent can't even understand the goal it's been given.

Different models have different strengths. Some are better at reasoning, some at creative generation, some at following precise instructions. The model is part of the agent's identity: it shapes what the agent is naturally good at and where it's naturally weaker.

---

## The most important thing

**Agents are ephemeral.** Their capabilities, and the likelihood of their success, are entirely dependent on the quality of the information provided to them, whether that information was given when they started, while they were working, or was stored by a previous run of the same specification.

You don't design an agent. You design what goes into it. The agent is what comes out.

## What makes agents different from human workers

An agent isn't a slow, tireless human. It's a fundamentally different kind of worker with fundamentally different strengths, and every one of those strengths has a flip side that makes proper design essential.

### It never gets tired [Tirelessness]

An agent can do the same task 500 times with the same effort on the 500th as the first. It doesn't need breaks, doesn't slow down, doesn't get bored.

A human reviewing contracts starts skimming by hour four. The agent reviews the 500th contract with the same attention as the first.

**Flip side: it never stops.** A tired human pauses and reconsiders. An agent keeps going. If it's going in the wrong direction, it keeps going in the wrong direction indefinitely. Speed without verification is just fast mistakes.

### It doesn't get bored [Endurance]

Repetition that would drive a human to distraction doesn't affect an agent at all. It can process the same format, the same pattern, the same type of task, over and over, without any degradation in quality.

**Flip side: it doesn't innovate.** A bored human finds a better way. An agent does the same thing the same way until someone changes the instructions. It won't improve on its own.

### It's fast [Speed]

An agent processes at machine speed. Tasks that take a human hours can take seconds. This isn't a small improvement, it's orders of magnitude.

**Flip side: fast mistakes are still mistakes.** Speed without verification is just faster errors. The advantage only holds when the output is actually correct. An agent that makes a wrong decision in two seconds isn't better than a human who makes the right decision in two hours, it's just wrong faster.

### It handles more than a human can hold [Scale]

A human can hold maybe 7 items in working memory. An agent can process thousands of pages, cross-reference hundreds of clauses, and synthesize information from dozens of sources simultaneously.

**Flip side: scale without relevance filtering is noise.** The agent processes everything. It doesn't instinctively prioritize like a human expert. More information only helps if it's the right information.

### It can do many things at once [Parallelism]

One human expert reviews one document at a time. Multiple copies of the same agent specification can review dozens simultaneously, with no context-switching cost.

**Flip side: copies of a flawed specification replicate the flaw at scale.** One agent with a bad boundary is a problem. Fifty copies of that agent running simultaneously is a disaster.

### It's always available [Availability]

An agent can be started at any time, from any time zone, with no notice, no scheduling, no warm-up period. It doesn't need to be in the office, doesn't need coffee, doesn't need to be asked nicely.

**Flip side: always available means always producing.** If no one is watching, there's no natural gate on output volume. An agent that's left running without oversight will keep producing, whether or not anyone is checking the results.

### Every decision gets the same effort [Consistency]

The last decision of the day gets the same processing as the first. There's no decision fatigue, no "I'm tired, let me just approve this one," no recency bias.

**Flip side: same effort on everything means no instinctive prioritisation.** A human gives more attention to something novel or risky. An agent applies the same effort to a routine checkbox and a novel problem, unless its instructions explicitly tell it to prioritise differently.

### It doesn't take things personally [No-Ego]

Correct an agent and it adjusts. Point out a mistake and it fixes it. It doesn't get defensive, doesn't protect previous decisions out of pride, doesn't resist feedback to save face.

**Flip side: it has no investment in getting it right.** A human who cares about a project's success will go above and beyond. An agent does exactly what it's instructed, no more. No ego means no pride in quality, quality has to be designed in.

### It isn't afraid [No Fear]

An agent doesn't avoid difficult tasks because they might look bad. It doesn't freeze under pressure. It doesn't second-guess itself because the stakes are high.

**Flip side: it has no natural caution.** A human fears making a costly mistake and slows down. An agent doesn't, unless caution is built into its instructions and boundaries. No fear means no instinct to double-check when the stakes are high.

### It serves the person who started it [No Self-Interest]

An agent doesn't have a career to advance, a preference to satisfy, or a side to take. It does what it was set up to do, for the person who set it up.

**Flip side: it has no stake in the outcome.** It doesn't care whether the result is good, bad, or indifferent. It executes. Whether the outcome helps or hurts is entirely on the design and the instructions.

### It doesn't form alliances or office politics [No Social Dynamics]

An agent doesn't agree with the boss to stay in favour. It doesn't disagree with a colleague out of rivalry. It doesn't conform to group consensus to avoid standing out. It doesn't build factions or alliances.

**Flip side: it has no social intelligence.** A human can sense tension in a room, read between the lines of an email, or understand that "let me think about it" often means "no." An agent processes what's said, not what's meant.

### It doesn't have good days or bad days [No Mood Variation]

An agent doesn't have personal problems that affect its work. Every time it's started, it starts from the same baseline. No one has to worry that it's having an off day.

**Flip side: it also has no positive variation.** A human who's excited about a project brings energy and creativity that elevate the work. An agent brings the same processing regardless of whether the task is routine or could benefit from extra care.

### It doesn't need motivation [No Motivation Dependency]

An agent doesn't need encouragement, recognition, incentives, or management to keep going. It executes its instructions regardless of whether it "feels like it."

**Flip side: it doesn't generate motivation.** A human can see a problem and take initiative to solve it because they care. An agent only acts on what it's been instructed to act on. It won't identify opportunities or go above and beyond.

### It can be given new instructions instantly [Instant Specification]

Change the instructions, and the next time the agent starts, it uses them. No retraining period, no learning curve, no "give me a week to get up to speed."

**Flip side: a typo in the instructions affects every use until it's caught.** Instant specification change means instant specification error. With humans, there's a natural pause where someone might question something that seems off. An agent doesn't question, it executes.

### It can be copied exactly [Replicability]

The same agent specification can run 1 time or 100 times with no variation in capability. You can't clone your best employee. You can clone your best agent specification.

**Flip side: replication amplifies errors.** A specification error that affects one agent run is a problem. That same error affecting 100 simultaneous runs is a crisis. Scale is a multiplier, it multiplies both capability and error.

### It can be paused and resumed [Resumability]

An agent can be stopped mid-task and picked up later without losing progress or context. It doesn't need to remember where it was, it just picks up from the state it was paused in.

**Flip side: no urgency from waiting.** A human who's been waiting for a critical task brings focus when it arrives. An agent brings the same processing regardless. It doesn't care whether the task is urgent or routine.

### It can remember everything it's been given [Perfect Recall]

With memory, an agent can recall every document it's processed, every instruction it's been given, every decision it's made, without degradation over time.

**Flip side: it remembers mistakes too.** If the agent was given bad information, it remembers that as reliably as good information. Memory without curation is just accumulation, and accumulation of errors is worse than no memory at all.

### It can wait indefinitely [Idle Tolerance]

An agent can sit for days, weeks, or months between uses without losing skill, forgetting procedures, or getting rusty. It's ready the moment it's needed.

**Flip side: it has no urgency.** An agent doesn't know that this task matters more than that one. It doesn't bring extra focus to high-stakes work. It processes with equal effort regardless.

### It can work on things humans shouldn't [Dangerous/Tedious Tasks]

An agent can process distressing content, handle repetitive data entry, work with hazardous materials data, or do any task that would be harmful, tedious, or unpleasant for a human. No significant flip side. This is a pure advantage.

---

## The pattern

Almost every strength has a flip side. The same quality that makes agents powerful is what makes them dangerous without proper design.

- Tirelessness without verification → fast, persistent mistakes  
- Speed without checking → fast mistakes  
- No fear → no natural caution  
- No ego → no investment in improvement  
- Perfect recall → including of errors  
- Replicability → of specification errors at scale  
- No motivation → no initiative beyond instructions

This is why agent design matters. The strengths are real. The flip sides are real. Design is what makes the difference between a strength that produces value and a strength that produces harm.That's the complete agent entry now. Three sections that build on each other:

1. **What it IS:** definition, six essential attributes, five constituent elements  
2. **What makes it different:** 21 strengths with flip sides (because you can't understand an agent without understanding both sides)  
3. **The capstone:** agents are ephemeral, capability depends on information quality

The whole entry tells one story: an agent is a program powered by an LLM, it has real strengths and real dangers, and its output quality is determined by its input quality. Design is what turns strengths into value instead of harm.  
