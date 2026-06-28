<!-- @format -->

# Design Thinking: Problem-to-Primitives Playbook

**Version**: 1.0  
**Date**: February 2026  
**Author**: Pete Argent  
**Canonical example**: `Framework-ideation.md` — the session that produced this playbook  
**When to use**: When complexity is rising, it's unclear which problems to solve first,
or a solution is already being built before the problem is fully understood  
**Estimated duration**: 3–5 hours (full session); 1–2 hours (mini sprint variant)  
**Participants**: Domain owner + AI facilitator (or two humans, one holding the
facilitator role)

---

## Changelog

| Version | Date     | Notes                                                             |
| ------- | -------- | ----------------------------------------------------------------- |
| 1.0     | Feb 2026 | First version, derived from Agentic Development Framework session |

---

## Conditions for Success

These are not tips. They are prerequisites. The process will produce polished
thinking rather than genuine insight if these conditions are absent.

### 1. Have a goal

Write a single sentence before you start:

> _"What do I want to understand at the end of this session that I don't understand now?"_

Not a deliverable. Not a solution. A question. The goal orients the session without
constraining it. Without it, the conversation drifts toward what's interesting rather
than what's useful.

### 2. Arrive with a beginner's mind

You may come in with strong prior work — a spec, a prototype, a vision, a model you've
invested in. Name your strongest prior belief about the solution explicitly. Then
consciously set it aside as a _hypothesis to test_, not a constraint to design within.

> _"I believe the solution looks like X. I am going to treat that belief as one input,
> not a conclusion."_

The process only works if it can challenge the existing model. If the existing model
is protected, the session will confirm it rather than improve it.

**If AI-facilitated**: The AI facilitator should ask at the start: _"What's the
solution you already have in mind? Let's put it on the shelf for now and come back
to it at the end."_

### 3. Reflect in action, not just at the end

Interrupt the process whenever something lands differently than expected. Say it out
loud. These interruptions are the most valuable moments in the session — they are
where tacit knowledge surfaces and where the most important reframings happen.

You don't need to be coherent. Say:

- _"That doesn't feel right, but I can't say why yet"_
- _"That just reminded me of something completely different"_
- _"Wait — I think I've been thinking about this wrong"_

Don't save it for the retrospective. Say it when it happens.

### 4. Share thoughts freehand

Do not compose before you speak or type. The temptation — especially when working
with an AI — is to give a well-structured, coherent prompt because that feels like
how you get a good response. In this process, the opposite is true.

Messy, associative, half-formed input produces richer outputs than any structured
brief. Incoherence and loose connections are signal, not noise. The process will find
the structure. Your job is to surface what you actually think, not perform what you
think you should think.

---

## Prerequisites

Before starting, assemble the following:

**Bring in:**

- Real artefacts: retros, logs, working notes, existing specs, error reports — anything
  grounded in observed experience
- Raw motivation: why does this matter to you? What's the vision pulling you forward?
- Known friction points: where has the work felt wrong, stuck, or overly complex?

**Do not bring in:**

- Finished solutions presented as starting points
- A fully-formed proposal you want validated
- An agenda for what the session should conclude

The canonical example of the right inputs: sprint retrospectives with 5-Why analyses
and documented root causes. These transformed the session from philosophical exploration
into evidence-based design. Imagined problems produce abstract solutions. Documented
failures produce load-bearing primitives.

---

## The Five Phases

### Phase 1 — Gather

**Purpose**: Surface the real inputs. Separate observed problems from assumed solutions.  
**Duration**: 30–45 minutes

**Activities**:

- Share all artefacts without curating them — let the facilitator read across them
- Describe first-hand experience in your own words: what you actually saw, not what
  you concluded
- Identify where the existing work came from: vision-first? Experience-first?
  Metaphor-first?

**Key questions**:

- _"What do the artefacts show is actually happening?"_
- _"Which of these problems did you observe, and which did you hypothesise?"_
- _"Where does the existing solution come from — the problem, or the vision?"_

**Output**: A curated set of raw inputs, with observed and assumed problems distinguished

**If AI-facilitated**: Prompt — _"Review these artefacts and identify: (1) what problems
are actually being solved, (2) where the design surface area came from, and (3) any
signals that complexity is growing faster than understanding."_

---

### Phase 2 — Define

**Purpose**: Name the real problems precisely. Find their roots. Collapse false complexity.  
**Duration**: 45–60 minutes

**Activities**:

**Problem inventory**: List every distinct problem the existing work is trying to solve.
Name them explicitly. Count them. If you have more than five, ask whether some share a
root cause.

**Problem laddering**: For each problem, ask "why is this a problem?" three times.
Follow the chain. Two problems that look different often share the same root, which
dramatically simplifies the solution space.

> _Example: "Coordination is a problem" → "because agents don't share state" →
> "because there's no single source of truth" → "because there's no agreed protocol
> for state transitions." The root is a protocol problem, not a marketplace problem._

**Design tension mapping**: Identify the key tensions — places where the design is
trying to serve two incompatible goals simultaneously. Name them as pairs.

> _Example: "Vision completeness vs. buildability today" or "Lean agent specs vs.
> comprehensive guidance"_

**Key questions**:

- _"Which of these problems, if solved, makes the others easier?"_
- _"Is the complexity essential — required by the problem — or accidental — introduced
  by our design choices?"_
- _"What would we stop building if we only had to solve the single most important problem?"_

**Output**: A named problem inventory; root causes per problem; 3–5 design tensions

**If AI-facilitated**: Prompt — _"For each problem identified, run a 3-level 'why'
ladder. Then identify which problems share a root cause. Finally, apply the Essential
vs. Accidental Complexity lens: does the problem require this complexity, or did the
design introduce it?"_

---

### Phase 3 — How Might We

**Purpose**: Convert problems into open design questions that invite solutions without
prescribing them.  
**Duration**: 30–45 minutes

**Activities**:

For each problem or root cause identified in Phase 2, write a HMW question using
this structure:

> _"How might we [achieve a positive outcome] without [the constraint that makes it hard]?"_

**Rules for good HMW questions**:

- Not too narrow (avoids the real design challenge)
- Not too broad (could mean almost anything)
- Preserves the constraint — the second half of the sentence is as important as the first
- Does not contain a solution

**Refinement moves**:

- If a HMW is too broad, split it into two more specific questions
- If two HMWs look similar, check whether they're really the same problem at different
  levels of abstraction
- Challenge each question: _"Does this frame the problem at the right level, or are
  we solving a symptom?"_

**Output**: 6–10 refined HMW questions that become the evaluation framework for all
subsequent ideation — any proposed solution should be checkable against them

**If AI-facilitated**: Prompt — _"Convert the problem inventory into HMW questions.
For each, flag if it's too narrow, too broad, or contains an embedded solution. Then
suggest one reframe for any question that doesn't yet feel right."_

---

### Phase 4 — Ideate

**Purpose**: Generate diverse approaches before converging on any one. Separate
divergence from evaluation.  
**Duration**: 60–90 minutes

Run in two rounds. Do not evaluate during either round — defer all judgment until
Phase 5.

**Round 1 — Within the domain** (~30 min)
Generate 4–6 approaches using familiar frames from the domain. Each approach should
answer: _what is the core idea, and how does it address the HMW questions?_

Name each approach after its conceptual origin (e.g., "The Evidence-First Architecture",
"The Minimal Context Card"). Naming matters — it gives the approach an identity that
can be discussed, combined, or discarded clearly.

**Round 2 — Outside the domain** (~45 min)
Study how analogous problems are solved in completely different fields. The goal is not
to copy solutions but to borrow primitives — the underlying mechanisms that make a
solution work — and ask whether those mechanisms apply here.

Useful domains to explore depending on your problem type:

| Problem Type                      | Look At                                                             |
| --------------------------------- | ------------------------------------------------------------------- |
| Coordination & handoffs           | Aviation CRM, surgical checklists, relay racing                     |
| Quality without central authority | Wikipedia editorial process, DNA proofreading, peer review          |
| Context delivery                  | Stage management, mise en place preparation, progressive disclosure |
| Silent failure detection          | Manufacturing andon cords, circuit breakers, canary deployments     |
| Knowledge accumulation            | Immune system memory, pattern languages, double-entry bookkeeping   |
| Trust building                    | Chain of custody in forensics, financial escrow, countersigning     |

For each analogous system, ask:

1. What is the core mechanism that makes it work?
2. What does it assume about the environment?
3. What would it look like if we applied it here?

**Output**: 8–12 named approaches (4–6 from each round); each with a core idea, a
connection to the HMW questions, and a named tension or open question

**If AI-facilitated**: Prompt — _"Ideate 5 distinct approaches within the domain, each
from a different conceptual angle. Then ideate 5 approaches inspired by analogous
systems in fields outside [domain]. For each, name the core mechanism being borrowed
and identify the tension it introduces."_

---

### Phase 5 — Synthesise

**Purpose**: Converge on the load-bearing primitives. Separate what the problem requires
from what the vision inspired.  
**Duration**: 45–60 minutes

**Activities**:

**Cross-approach pattern finding**: Look across all approaches from Phase 4. What
mechanisms appear in multiple approaches? Repeated mechanisms are candidates for
primitives — they're solving the same thing from different angles.

**Essential vs. Accidental audit**: For each component in the current design, ask:
_"Does the problem require this, or did our design introduce it?"_

- **Essential**: The problem genuinely requires it. Keep it.
- **Accidental**: The design or metaphor introduced it. Candidate for removal.

**Vision shelf**: Explicitly name everything that is valid as a future direction but
not required for the minimum valuable version. Write it down. This preserves the
vision without letting it contaminate the immediate design work.

**Design principles**: Derive 3–6 principles from the synthesis. These should be
specific enough to make a design decision, not just values statements.

> _Example: "Context is delivered on demand, not preloaded" is a principle.
> "Keep things simple" is not._

**Probe design**: For each primitive, design the minimum experiment that would validate
or invalidate it. A probe has: a hypothesis, a specific action, a measurement, and a
pass/fail threshold.

**Output**: 3–5 named primitives; a vision shelf document; 3–6 design principles;
2–3 probes with hypotheses and measurements; an ordered action plan

**If AI-facilitated**: Prompt — _"Identify mechanisms that appear across multiple
approaches — these are primitive candidates. Apply the Essential vs. Accidental lens to
the existing design. Produce: named primitives, design principles specific enough to
make a decision, and a probe for each primitive."_

---

## Retrospective Protocol

Run this at the end of every session using the **4Ls format**.

### The Process Map

Before the 4Ls, capture the actual sequence of the session — what happened, in order.
This becomes the reusable process record.

> _Example from the canonical session:_
>
> 1. Brought existing artefacts (framework spec, naming conventions, PRD)
> 2. Analysed the problem space — what problems are actually being solved?
> 3. Grounded in reality — sprint retros provided observed, documented failures
> 4. Clarified real motivation — first-hand experience described, actual use case emerged
> 5. Generated HMW questions from problems, not solutions
> 6. Ideated within the domain — 5 approaches using familiar frames
> 7. Ideated outside the domain — 5 approaches from completely different fields
> 8. Broadened the inspiration base — cross-domain systems, simplification tools
> 9. Synthesised — findings, primitives, principles, action plan

### 4Ls

**Liked** — What worked well? What produced the most valuable output?

**Learned** — What shifted in your understanding? What was the most important
conceptual change?

**Lacked** — What would have made the session more productive? What was missing?

**Longed For** — What should exist for the next session that doesn't exist yet?

### Process Health Assessment

After the 4Ls, score the session on these dimensions (Strong / Partial / Missing):

| Dimension                                                      | Score | Notes |
| -------------------------------------------------------------- | ----- | ----- |
| Problem grounding (real evidence vs. hypothesised)             |       |       |
| Inspiration breadth (within vs. outside domain)                |       |       |
| HMW quality (not too narrow, not too broad)                    |       |       |
| Ideation divergence (genuinely different approaches)           |       |       |
| Synthesis quality (primitives feel load-bearing)               |       |       |
| Explicit scope cutting (accidental complexity removed)         |       |       |
| Actionability of output (specific probes, not just principles) |       |       |

---

## Recommended Cadence

| Trigger                             | Activity                                               | Duration  |
| ----------------------------------- | ------------------------------------------------------ | --------- |
| Before each new build phase         | Full session (all 5 phases)                            | 3–5 hours |
| When complexity starts feeling high | Mini sprint: Phase 2 + Phase 3 only                    | 1–2 hours |
| When a probe completes              | Learning capture → knowledge base entry                | 30 min    |
| After every 3 sprints               | Full retrospective in this format                      | 2 hours   |
| When the vision needs refreshing    | Pull from the vision shelf; check what's now buildable | 1 hour    |

---

## Adaptation Variants

### Mini Design Thinking Sprint (1–2 hours)

Run Phases 2 and 3 only. Use when the problem space is already partially understood
and you need to sharpen a specific HMW question or challenge a specific design
decision. Skip the cross-domain ideation; focus on problem laddering and HMW refinement.

### Solo with AI Facilitator

The AI facilitator holds the process structure. The human domain owner provides all
the raw inputs and makes all the judgments. The AI's role is to reflect back, probe,
and generate options — not to decide. Explicitly give the AI permission to challenge
the existing model, or it will tend to confirm it.

### Two-Human Session

One person is the domain owner; the other holds the facilitator role. The facilitator's
job is to slow down convergence, ask the next-level-down question, and name when the
group is protecting an assumption rather than examining it.

### Async Session

Each phase can be run as a separate async exchange (document → response → document).
Add an explicit synthesis step at the start of each new exchange: _"Here is what
we've established so far, and what this phase needs to produce."_ Async sessions tend
to lose the reflection-in-action dynamic — compensate by explicitly inviting
interruptions at the start of each phase.

---

## Appendix: Reusable Prompts

### Phase 1 Opening Prompt

Review the attached artefacts. Identify:

1. What distinct problems are being solved (name each separately)
2. Where the design surface area came from (problem, vision, or metaphor)
3. Signals that complexity is growing faster than understanding
4. The most important gaps between what's documented and what's been observed

### Phase 2 Problem Laddering Prompt

For each problem identified, run a 3-level "why" ladder.
Then: which problems share a root cause?
Apply the Essential vs. Accidental Complexity lens: does the problem require this
complexity, or did the design introduce it?

### Phase 3 HMW Generation Prompt

Convert the problem inventory into How Might We questions.
Structure: "How might we [positive outcome] without [the constraint that makes it hard]?"
Flag any question that: is too narrow, is too broad, or contains an embedded solution.
Suggest one reframe for each flagged question.

### Phase 4 Cross-Domain Ideation Prompt

Generate 5 approaches to [problem] inspired by analogous systems in fields outside
[domain]. For each:

- Name the source system and the core mechanism being borrowed
- Describe what the approach looks like applied to our problem
- Identify the tension or open question it introduces

### Phase 5 Synthesis Prompt

Identify mechanisms that appear across multiple approaches — these are primitive
candidates. For each primitive:

- Name it
- State what problem it solves
- Apply the Essential vs. Accidental lens: does the problem require this?
- Design a minimum probe to validate it: hypothesis, action, measurement, pass/fail threshold

---

This gives you a complete, self-contained document. A few notes on decisions made: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/d99b6417-09d8-43d9-a15e-ed0ddf8ec440/Framework-ideation.md)

- **The Conditions for Success section leads** — it's placed before any phase instructions because the session showed that the process only works when those conditions are present; they're not optional context
- **The canonical session is cited as a reference throughout** rather than reprinted, keeping the playbook lean while giving future readers a rich worked example to learn from
- **The dual-audience design is embedded** in the "If AI-facilitated" callouts in each phase, rather than as a separate section — this keeps the instructions unified and avoids duplication
- **The vision shelf** is formalised as a Phase 5 output, which was one of the Longed For items in the session retro [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/42141261/d99b6417-09d8-43d9-a15e-ed0ddf8ec440/Framework-ideation.md)
