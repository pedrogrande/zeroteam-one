<!-- @format -->

# Event Storming Session Retrospective

**Session Date:** 2026-02-21
**Duration:** ~2.5 hours
**Format:** Text-based collaborative Event Storming (Big Picture + Process Modelling)
**Facilitator:** Perplexity AI
**Participant:** Pete Argent

---

## What We Set Out To Do

Run a full Event Storming session on the Agentic Development Framework workflow — from _human has an idea_ to _working feature in production_ — using a physical whiteboard with coloured sticky notes, conducted step by step over text.

---

## What Went Well

**The storm was genuinely generative.** The first orange sticky pass produced 40+ events unprompted, covering the full lifecycle with real depth. Most Event Storming sessions with experienced practitioners don't get that far on a first pass.

**Spontaneous discoveries were the best moments.** Three of the most valuable insights weren't prompted — they emerged from you looking at the board:

- UI Design needs curated context _in_ and produces context _out_
- Zone 5 belongs to Feature Delivery, not Task Delivery — a foundational architectural decision
- Task-level tests were missing entirely from Zone 3

These are exactly the insights Event Storming is designed to surface. They would have become sprint failures.

**The "owner" framing resolved a hard problem elegantly.** When you named Feature Owner Agent and Task Owner Agent, it instantly resolved the boundary question, the context load question, and the spawning question simultaneously. That kind of naming doing multiple jobs at once is a sign of a good domain model.

**All 13 hotspots were resolved.** None were left open or deferred without a decision. That's a clean session.

**The acceptance criteria / test distinction is load-bearing.** Making this explicit — AC lives in the problem space, tests live in the solution space — gave the Test Writer Agent a precise job description and created a new quality gate: ambiguous AC is detected by the agent that tries to translate it, not discovered in production.

**The step-by-step format worked.** Doing one colour at a time, one zone at a time, prevented overwhelm and kept each step purposeful.

---

## What Didn't Go Well

**The linearity of text hid spatial relationships.** On a real board, you'd see at a glance that the uncertainty sub-flow touches four zones, that context curation is a pattern not a step, and that Zone 3 has more handoffs than all other zones combined. In text, these patterns required explicit pointing out rather than being self-evident.

**The happy path dominated too long.** Sad path events only appeared in the second pass after prompting. In a physical session with multiple participants, someone would have put up _Task Rejected_ or _Integration Tests Failed_ in the first five minutes. The solo format created a natural bias toward the flow working.

**Zone 5 was under-explored relative to Zones 3 and 4.** The Feature Delivery zone — integration tests, staging, user testing, production promotion — received less rigour than the Task Preparation and Execution zones. The policies and read models for Zone 5 are thinner than they should be.

**The Uncertainty sub-flow never got its own dedicated pass.** It was handled as part of Zone 4 rather than as the complete mini-system it turned out to be. It deserves its own Big Picture storm.

**Context curation emerged as a system-wide pattern mid-session rather than being identified upfront.** By the end, context curation appears in Zones 2, 3, and 4 with different actors each time. If we'd identified this pattern earlier, we might have designed it as a first-class primitive from the start rather than discovering it incrementally.

---

## Root Cause Analysis — Top Two Problems

### RCA 1: Sad Path Events Appeared Too Late

**Problem:** Happy path bias meant failure events only appeared after prompting, not spontaneously.

- Why? The first instruction was "list every domain event" without explicitly prompting for failure states.
- Why? The instruction assumed a balanced storm but the constraint "what happens" naturally surfaces what's intended to happen.
- Why? There was no explicit framing of "what goes wrong" as equally valid and equally important as "what goes right."

**Root cause:** The opening prompt didn't give equal weight to failure events. A future session should open with two explicit constraints: _"For every successful event, there is at least one failure event. Both belong on the board from the start."_

---

### RCA 2: Zone 5 Was Under-Specified

**Problem:** Feature Delivery policies, read models, and commands are thinner than Zones 3–4.

- Why? Zone 5 was the last zone reached and session energy was lower by then.
- Why? The major architectural decision — Zone 5 belongs to Feature, not Task — was made mid-session, which reset Zone 5 and required rebuilding it quickly.
- Why? The session had no explicit time allocation per zone, so early zones absorbed disproportionate attention.

**Root cause:** No timebox per zone. A future session should allocate roughly equal time to each zone and explicitly revisit under-specified zones before moving to blue stickies.

---

## Improvement Proposals

**IP-01: Add a dedicated sad-path pass immediately after the first orange storm.** Before organising the timeline, explicitly ask: "For every zone, what are the three most likely failure events?" Make failure events first-class from the start, not a second pass.

**IP-02: Timebox each zone before moving to the next colour.** Assign a rough time budget per zone at the start of the session. When blue stickies begin, every zone should have comparable coverage — not just the ones that received the most discussion.

**IP-03: Run a dedicated Uncertainty Sub-flow session.** This sub-system is complex enough to warrant its own separate Event Storming pass — with its own orange storm, its own actors, its own policies, and its own aggregate spec. Treat it as a domain in its own right.

**IP-04: Identify recurring patterns before adding blue and purple stickies.** Context curation appeared three times before we named it as a pattern. In future sessions, after the orange pass and before the blue pass, do an explicit pattern scan: "Are there any event clusters that appear more than once with the same shape?" Those clusters are your design primitives.

**IP-05: Zone 5 needs a dedicated follow-up session.** Before implementing anything in the Feature Delivery zone, run a focused 1-hour storm of Zone 5 alone — with explicit attention to integration test failure paths, the CI/CD boundary (H13), and the Feature aggregate's definition of done.

---

## Decisions Made This Session

For the record — these are the consequential domain decisions locked in today:

| Decision                                                        | Implication                                                                                  |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Zone 5 is Feature Delivery, not Task Delivery                   | Tasks complete at end of Zone 4; features own integration, staging, and production           |
| Feature Owner Agent spawns Task Owner Agents                    | System is hierarchical at creation boundary, not market-based                                |
| Two specialist QA Agents                                        | QA Agent (Definition) for Zones 2–3; QA Agent (Execution) for Zone 4                         |
| Task returned to queue requires human review                    | Product Owner has three outcomes: re-publish, modify and re-publish, or close                |
| AC lives in problem space; tests live in solution space         | Test Writer Agent is the ambiguity detector — unclear AC becomes an uncertainty, not a guess |
| "Iced" means actively deprioritised, not rejected               | A distinct terminal-ish state that can be revisited                                          |
| Task Blocked = unexpected problem mid-execution                 | Distinct from Task Rejected and Task Returned to Queue                                       |
| Context Agent curates, QA Agent reviews, Product Owner approves | No agent reviews its own artefact                                                            |

---

## Deliverables Produced

- ✅ Full domain event map — 40+ events across 5 zones
- ✅ 9 actors with defined authority and zone scope
- ✅ 30+ commands connecting actors to events
- ✅ 30+ policies making reactive logic explicit
- ✅ 13 Read Models per actor per decision point
- ✅ 7 external system boundaries identified
- ✅ 4 aggregates with ownership defined
- ✅ 13 hotspots — all resolved
- ✅ Task Aggregate Specification v0.2 (./TaskAggregateSpec-v0.2.md)

---

## Next Actions

| Action                                                                  | Owner     | When                         |
| ----------------------------------------------------------------------- | --------- | ---------------------------- |
| Photograph and digitise the board                                       | Pete      | Today                        |
| Update Task Aggregate Spec with retro findings                          | Pete      | This week                    |
| Resolve H13 — CI/CD domain boundary                                     | Pete      | Before Zone 5 work begins    |
| Run dedicated Uncertainty Sub-flow session                              | Pete + AI | Next session                 |
| Run dedicated Zone 5 storm                                              | Pete + AI | Before Feature Delivery spec |
| Run minimum viable coordination probe — one story, one task, end to end | Pete      | This week                    |

---

_This retrospective was produced immediately following the session while findings are fresh. It should be stored alongside the Task Aggregate Spec v0.2 as the provenance document for decisions made._
