<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I want to focus now on the bootstrapping of a project using the framework with the Nexus mcp server tools and policies.

We now have an agent creation policy - could this be better if we have decided that every agent needs at least one reviewer, then there should always be at least two agents created at the same time. (unless it was decided another review/qa agent is required somewhere).
How might this change the policy we drafted today?

This is a great design question. Here's how the **"every performer needs a reviewer"** invariant changes the policy:

***

## The Core Change

The current policy creates agents **one at a time** in response to gap signals. Under the new invariant, any creation request for a **performer-type agent** must automatically trigger a paired request for its **reviewer agent** — making the minimum atomic unit of Zone 0 work a **pair**, not a single class.[^1_1]

***

## What Changes in Each Part

### Part 1: Glossary — new terms needed

Add two definitions:

- **Performer Agent** — any agent of `TYPE: EXECUTOR` or `TYPE: ORCHESTRATOR` that produces a primary artefact. Requires a designated Reviewer Agent before it can be activated.
- **Reviewer Agent** — an agent whose sole write authority is a review or QA artefact for a specific performer's output. A Reviewer Agent is the *paired counterpart* of exactly one Performer Agent class, unless designated as a shared zone-level reviewer.
- **Agent Pair** — the atomic unit of Zone 0 output: one Performer Agent template + one Reviewer Agent template. Neither is activatable without the other.

***

### Part 2: Responsibility Tree — new invariant

Add to the invariants block:

> - **No Performer Agent template may be approved or activated without a paired, approved Reviewer Agent template.**
> - **An Agent Class Requirements document for a Performer Agent is invalid unless it names its reviewer counterpart** (either an existing approved reviewer class, or a new one to be created in the same Zone 0 cycle).
> - A single Reviewer Agent *may* serve multiple Performer Agents in the same zone if the FOA explicitly documents that decision and FO approves it (shared reviewer pattern).

This also affects the **Bootstrapping Exception** in Part 6 — see below.

***

### Part 3: The Creation Flow — Step 2 changes most

**Step 2 — FOA writes requirements** now has a mandatory pairing check:

> Before finalising the Agent Class Requirements document, the FOA must answer:
> *"Does a Reviewer Agent already exist for this agent's artefact type?"*
>
> - **Yes** → Name the existing reviewer class in the requirements document. Proceed as a single-agent cycle.
> - **No** → The FOA must write **two** Agent Class Requirements documents in the same cycle: one for the performer, one for the reviewer. Both enter the creation flow together. The cycle does not close until both templates pass their spec tests and are approved.

This creates a natural **parallel track** inside one Zone 0 cycle:

```
Step 2:   FOA writes Requirements Doc A (performer) + Requirements Doc B (reviewer)
Step 3:   Agent Spec QA writes spec tests for BOTH
Step 4:   FOA reviews BOTH test suites
Step 5:   Agent Template Creator builds BOTH templates
Step 6:   Agent Spec QA runs tests on BOTH
Step 7:   FOA (or FO) approves BOTH — activation gate requires both to pass
```

The two sets of spec tests should include a **cross-reference test**: *"Does the Reviewer Agent's READS list contain the Performer Agent's WRITES path?"*[^1_1]

***

### Part 4: The Oversight Rule — QA Tier for pairs

When a pair is created together, use the **higher** of the two NV/BR scores to determine the QA Tier for the entire cycle. This prevents a novel performer from dragging a routine reviewer through a lower-tier cycle.

Add a new row to the scenario table:


| Scenario | BR | NV | Tier |
| :-- | :-- | :-- | :-- |
| New performer + new reviewer pair, no precedent | 3 | 2 | **3** |
| New performer + existing reviewer reused | 3 | 1 | 2 |
| Shared zone reviewer serving 3+ performers | 4 | 2 | **4** |


***

### Part 5: Base Agent Template — new required field

Add one field to the base template structure:

```yaml
REVIEWER: [ReviewerAgentClassName | SHARED:[zone-reviewer-name] | NONE:FO-approved]
# REQUIRED for TYPE: EXECUTOR and TYPE: ORCHESTRATOR
# Omit for TYPE: COMPRESSION and TYPE: BATCH unless they produce reviewable artefacts
```

A template with `TYPE: EXECUTOR` and `REVIEWER:` absent fails the spec test. This makes the pairing constraint **mechanically enforced**, not just policy-stated.[^1_1]

***

### Part 6: Bootstrapping Exception — extended

The current exception covers FOA + Agent Spec QA. Under the pairing rule, both of those agents are already a de-facto pair (FOA is performer-like, Agent Spec QA is its reviewer). This means:[^1_1]

> **The bootstrapping exception already satisfies the pairing invariant.** The exception text should note this explicitly so it's clear the bootstrapping pair is the founding precedent for the rule, not an exemption from it.

***

## What the Policy Does NOT Need to Change

- The seven-step flow structure stays intact — the change is that Step 2 may produce **two** requirements documents rather than one
- NV/BR scoring logic is unchanged; you just apply it to both agents and take the max
- The Pattern Library still records entries per agent class, but adds a `PAIRED_WITH:` field to each entry

***

## Suggested Version Note for v0.2

The single most important sentence to add anywhere in the document is as an **invariant** in Part 2:

> *"A Performer Agent and its Reviewer Agent are created in the same Zone 0 cycle. A Performer Agent template cannot be activated if its paired Reviewer Agent template is not also approved and active."*

This turns a design principle into an enforced system rule — consistent with how the rest of the policy handles invariants.[^1_1]
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_2][^1_3][^1_4][^1_5][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: agent-creation-policy-v0.1.md

[^1_2]: experiment-2-will-need-to-wait-0U5RBKbfTZ6BlRtDT_4fYw.md

[^1_3]: NotesOnExp1Retro.md

[^1_4]: Nexus-exp01-retro.md

[^1_5]: zone-uncertainty-analysis.md

[^1_6]: session-summary-20260303-a.md

[^1_7]: preflight-check-protocol.md

[^1_8]: example-spec-preflight-check.md

[^1_9]: context-curation-pattern.md

[^1_10]: TaskAsQuasiSmartContract.md

[^1_11]: OpenQuestions.md

[^1_12]: ONE-Ontology.md

[^1_13]: NexusToolGrammar.md

[^1_14]: NexusModelOverview.md

[^1_15]: NexusDecisionsRationale.md

[^1_16]: nexus-suggested-resources.md

[^1_17]: Nexus-agent-plan.md

[^1_18]: Nexus-101.md


---

# Great - I like that term "agent pair".

draft a markdown version 2 of the policy

Here is the full draft of v0.2:

***

```markdown
# Agent Creation Policy
## Nexus Agentic Development Framework — Zone 0

**Version:** 0.2
**Status:** Draft
**Applies to:** All new agent classes and agent template revisions in Nexus

***

## How to Read This Document

This policy governs how new agent classes are created in Nexus. It covers who makes
each decision, what checks are required, and when a human needs to be involved.

The document is structured in six parts:
1. **Glossary** — what every term means
2. **Responsibility Tree** — who does what
3. **The Creation Flow** — the step-by-step process
4. **The Oversight Rule** — how much QA is needed for different types of work
5. **The Base Agent Template** — the minimum valid structure every template must conform to
6. **Bootstrapping Exception** — the one-time manual setup and why it satisfies this policy

***

## Part 1: Glossary

**Agent**
A software process that performs a defined job autonomously. An agent has a fixed set
of files it reads, exactly one artefact it writes, and a list of files it is explicitly
forbidden from touching. Agents do not improvise their scope — they operate within
declared boundaries.

**Agent Class**
A category of agent defined by its job, zone, and artefact. "Task Performer Agent" is
an agent class. There can be many instances of a class running simultaneously, but they
all follow the same template.

**Agent Template**
The reusable specification file for an agent class. It defines the agent's job, what it
reads, what it writes, what it is forbidden from reading, and which skills it loads.
Every agent that Nexus creates is an instance of a template.

**Base Agent Template**
The minimum valid structure that every agent template must conform to. It enforces the
framework's design rules structurally — not as advice, but as required fields. No agent
template is valid unless it satisfies the base template.

**Performer Agent**
Any agent of `TYPE: EXECUTOR` or `TYPE: ORCHESTRATOR` that produces a primary artefact.
A Performer Agent requires a designated Reviewer Agent before it can be activated. A
Performer Agent template with no named reviewer fails its spec tests.

**Reviewer Agent**
An agent whose sole write authority is a review or QA artefact for a specific Performer
Agent's output. A Reviewer Agent is the paired counterpart of exactly one Performer Agent
class, unless it is explicitly designated as a shared zone-level reviewer with FO approval.
A Reviewer Agent reads the Performer Agent's WRITES path — this linkage is tested.

**Agent Pair**
The atomic unit of Zone 0 output: one Performer Agent template and one Reviewer Agent
template, approved in the same Zone 0 cycle. Neither template is activatable without the
other. An Agent Pair is recorded as a single Pattern Library entry with both classes named.

**Shared Reviewer**
A Reviewer Agent that serves more than one Performer Agent class within the same zone.
A Shared Reviewer must be explicitly approved by FO and documented in the Pattern Library.
It does not exempt the Zone 0 cycle from producing paired requirements documents — it
means one side of the pair already exists and is named.

**Framework Owner (FO)**
The human responsible for the overall health and evolution of the framework. FO makes
high-level decisions, approves new agent classes when the NV Score is 2 or above, and
handles escalations from the FOA. FO does not review or approve every new agent class —
that is the FOA's job — but FO sets the standards and makes the final call on high-novelty
work.

**Framework Owner Agent (FOA)**
The agent responsible for the health and completeness of the agent roster. It identifies
when a new agent class is needed, commissions the tests and templates, reviews the output,
and either approves it or escalates to FO. It does not build agents itself — it delegates
and oversees.

**Agent Template Creator**
The agent that writes agent templates. It receives a requirements document and a test
suite, and produces a conformant agent template file. It does not decide what the agent
should do — that is specified by the FOA in the requirements document.

**Agent Spec QA**
The specialist agent that (a) writes the acceptance tests for a proposed agent template,
and (b) later runs those same tests against the finished template. It is the independent
reviewer in the creation flow — the Agent Template Creator cannot review its own output.
When a pair is being created, Agent Spec QA writes and runs tests for both templates, and
additionally runs the cross-reference test confirming the Reviewer reads the Performer's
WRITES path.

**Agent Class Requirements Document**
The document the FOA writes before any template is built. It specifies the agent's job
(one sentence), its zone, its candidate READS/WRITES/NEVER files, and its NV Score. When
the requirements document describes a Performer Agent, it must also name the paired
Reviewer Agent class — either an existing approved class, or a new class whose requirements
document is written in the same step. This document is the contract the Agent Template
Creator works from and that Agent Spec QA tests against.

**Zone**
A stage in the delivery pipeline. The five delivery zones are Idea (1), Feature Definition
(2), Task Preparation (3), Task Execution (4), and Feature Delivery (5). Zone 0 is the
framework evolution zone — it operates on the framework itself, not on features.

**Write Authority**
The exclusive right to change a named artefact. Only one agent holds write authority over
an artefact at any point in time. No agent may modify an artefact it does not have write
authority for. No agent may review its own artefact.

**Artefact**
A file produced by an agent. Each agent produces exactly one artefact per invocation —
written to a declared path. Artefacts are the unit of handoff between agents.

**Acceptance Criteria (AC)**
Human-readable statements that describe what success looks like. Written in plain language.
Each criterion must be independently verifiable — a test can be derived from it — and
unambiguous.

**Spec Test**
An executable check derived from acceptance criteria. Spec tests are what Agent Spec QA
runs against a finished template to determine pass or fail. They test whether the template
satisfies its requirements, not whether the code works.

**Cross-Reference Test**
A mandatory spec test that applies whenever an Agent Pair is created. It verifies that the
Reviewer Agent's READS list contains the exact file path declared in the Performer Agent's
WRITES field. A pair cannot achieve PASS ALL without this test passing.

**Proof of Completion**
Literal captured output proving work is done. For agent template creation, this means the
actual test results from running the spec test suite against the template — not a claim that
tests passed.

**NV Score (Novelty Score)**
A number from 0 to 3 that measures how much prior evidence exists for a proposed agent
class. 0 means it has been done before with documented results. 3 means it is genuinely
new territory with no prior precedent. The NV Score determines whether the FOA can approve
independently or must escalate to FO. When scoring an Agent Pair, both classes are scored
independently and the higher score governs the QA Tier for the whole cycle.

**Blast Radius (BR)**
A number from 0 to 4 that measures how many future operations an agent template will
govern. When scoring an Agent Pair, both classes are scored independently and the higher
score governs the QA Tier for the whole cycle.

**QA Tier**
The level of scrutiny applied to a Zone 0 cycle. Determined by the NV Score and Blast
Radius. See Part 4.

**Pattern Library**
The repository of documented agent class designs that have been approved and deployed.
Pattern Library entries for Agent Pairs include both class names and the `PAIRED_WITH:`
relationship. When the FOA assesses a new Performer Agent, it checks the Pattern Library
for an existing approved reviewer before deciding whether a new reviewer class is needed.

**Observable Stream**
The append-only event log that every agent action writes to. Every state change in Nexus
emits a domain event to this stream. It is the shared source of truth — not any individual
agent's memory.

**Invariant**
A rule that must always be true. Invariants are enforced mechanically. If a command would
violate an invariant, the system rejects it.

***

## Part 2: Responsibility Tree

```

FO (Product Owner)
│
│  Approves new agent classes when NV ≥ 2
│  Approves changes to the Base Agent Template
│  Approves Shared Reviewer designations
│  Bootstraps the FOA and Agent Spec QA (one-time, manual)
│
└── Framework Owner Agent (FOA)
│
│  Identifies gaps in the agent roster
│  Writes Agent Class Requirements documents (one per class; two per pair cycle)
│  Determines whether a new Performer requires a new or existing Reviewer
│  Decides NV Score and QA Tier (using the higher score across the pair)
│  Reviews spec tests before template work begins
│  Reviews finished templates before approval
│  Adds learnings to the Pattern Library (one entry per pair, naming both classes)
│  Approves new agent classes when NV ≤ 1
│  May NOT activate a Performer Agent without a paired, approved Reviewer Agent
│
├── Agent Spec QA
│   │
│   │  Writes spec tests and acceptance criteria for each template in the cycle
│   │  Runs the Cross-Reference Test when a pair is being created
│   │  Issues PASS or FAIL with literal test output
│   │  Does NOT write agent templates
│   │  Does NOT review its own spec tests
│
└── Agent Template Creator
│
│  Writes agent templates from requirements + spec tests
│  Revises templates when tests fail
│  Does NOT write spec tests
│  Does NOT approve its own templates
│  Does NOT define what the agent is responsible for

```

**Invariants on this tree:**

- Agent Spec QA may not review its own spec tests — the FOA does that
- Agent Template Creator may not review its own templates — Agent Spec QA does that
- No agent in Zone 0 approves its own artefact
- The FOA cannot approve a class with NV ≥ 2 — FO must approve
- FO cannot be replaced in the approval role for NV ≥ 2 by any agent
- **A Performer Agent template may not be approved or activated without a paired, approved
  Reviewer Agent template**
- **A Reviewer Agent's READS list must contain the Performer Agent's WRITES path — this
  is a tested invariant, not a convention**
- **The minimum atomic output of a Zone 0 cycle that introduces a new Performer Agent is
  an Agent Pair — both templates, both test suites, both approvals**

***

## Part 3: The Creation Flow

### How a new agent class comes to exist

A new agent class begins with a **gap signal** — evidence that the current agent roster
cannot handle a task type that has appeared in the system. Gap signals come from three
sources:

1. An `UnknownTaskTypeEncountered` event in the Observable Stream
2. A retrospective finding that a task type was handled poorly because no specialist agent
   exists for it
3. A direct directive from FO

The FOA is the only agent that acts on gap signals.

***

### The seven steps

**Step 1 — FOA identifies the gap**

The FOA reads the gap signal and checks the Pattern Library and current agent roster. If a
suitable agent class already exists, or a Zone 0 cycle for this gap is already in progress,
the signal is absorbed — no new cycle starts. If no match exists, the FOA proceeds to
Step 2.

***

**Step 2 — FOA writes the Agent Class Requirements document(s)**

The FOA writes requirements before any other work begins. This is where the pairing
decision is made.

For every Performer Agent requirements document, the FOA must answer:
*"Does an approved Reviewer Agent already exist for this agent's artefact type?"*

- **Yes — existing reviewer** → Name the existing Reviewer Agent class in the Performer's
  requirements document under `REVIEWER:`. This is a single-class cycle; proceed to Step 3
  with one requirements document.
- **No — reviewer needed** → The FOA writes **two** requirements documents in this step:
  one for the Performer, one for the new Reviewer. Both documents enter the cycle together.
  The Performer's requirements document names the new Reviewer class under `REVIEWER:`.
  This is a Pair Cycle; Steps 3–7 run on both documents in parallel.

Each requirements document must contain:

- **Job statement** — one sentence describing what this agent is hired to do
- **Zone** — which delivery zone(s) this agent operates in
- **Candidate READS** — files this agent will likely need to read (named paths, not
  categories)
- **Candidate WRITES** — the single artefact this agent will produce
- **Candidate NEVER** — files this agent must never access
- **NV Score** — 0, 1, 2, or 3
- **QA Tier** — determined by taking the higher NV and BR scores across both documents
  in a Pair Cycle
- **REVIEWER** *(Performer documents only)* — the name of the paired Reviewer Agent class,
  or `SHARED:[class-name]` if a shared reviewer is designated

> **If NV ≥ 2 (using the higher score across the pair), the FOA shares all requirements
> documents with FO before proceeding.** FO may reshape, approve, or halt the cycle.
> The escalation happens here — not after templates are built.

***

**Step 3 — FOA commissions spec tests**

The FOA hands all requirements documents for this cycle to Agent Spec QA with the
instruction: *"Write the spec tests and acceptance criteria for each template in this cycle.
If this is a Pair Cycle, include the Cross-Reference Test confirming the Reviewer's READS
contains the Performer's WRITES path."*

Agent Spec QA produces, for each agent in the cycle:
- `spec-tests-[class-name].md` — the executable checks the finished template must pass
- `acceptance-criteria-[class-name].md` — the human-readable criteria the spec tests
  derive from

In a Pair Cycle, Agent Spec QA additionally produces:
- `spec-tests-pair-crossref.md` — the Cross-Reference Test covering the READS/WRITES link

Agent Spec QA does not decide whether the requirements are correct. It translates them
faithfully into tests. If the requirements are ambiguous, Agent Spec QA raises that as an
uncertainty to the FOA before writing tests.

***

**Step 4 — FOA reviews the spec tests**

The FOA reviews all spec test suites before any template work begins. For each suite, the
FOA checks:

- Do the tests cover every item in the requirements document?
- Are each test's pass/fail conditions unambiguous?
- Is the test for the base template conformance present?
- Is there a test for NEVER list non-emptiness?

In a Pair Cycle, the FOA additionally checks:
- Is the Cross-Reference Test present and unambiguous?
- Does the Cross-Reference Test reference the exact WRITES path declared in the Performer's
  requirements document?

If any suite is incomplete or unclear, the FOA returns it to Agent Spec QA with specific
feedback. **The spec test loop closes before the template loop opens. All suites in a Pair
Cycle must be accepted before any template work begins.**

***

**Step 5 — FOA commissions the agent templates**

The FOA hands each requirements document and its accepted spec tests to Agent Template
Creator. In a Pair Cycle, both commissions are issued together.

Agent Template Creator produces:
- `agent-template-[performer-class-name].agent.md`
- `agent-template-[reviewer-class-name].agent.md` *(Pair Cycle only)*

Both templates must conform to the Base Agent Template structure (see Part 5).

***

**Step 6 — Agent Spec QA runs the tests**

Agent Spec QA runs each spec test suite against its corresponding template. In a Pair
Cycle, Agent Spec QA also runs the Cross-Reference Test against both templates together.

For each template, Agent Spec QA produces a `test-results-[class-name].md` file containing:

- The result of each test (PASS or FAIL)
- Literal evidence for each result — not assertions
- A summary verdict: PASS ALL or FAIL with failed test list

In a Pair Cycle, a combined `test-results-pair-crossref.md` is also produced.

**A Pair Cycle cannot achieve PASS ALL unless every individual test suite passes AND the
Cross-Reference Test passes.** If any test fails, the FOA returns the relevant template(s)
to Agent Template Creator with the test results attached. The revision loop continues until
all tests pass.

***

**Step 7 — FOA reviews and approves**

Once all tests pass, the FOA reviews all templates for:

- Context tree consistency — does each agent's READS/WRITES/NEVER map correctly onto the
  context tree?
- Clean boundary — does either agent's job overlap with any existing agent's write
  authority?
- Pair coherence — does the Reviewer's scope fully cover the Performer's output?
- Learnings — is there anything from this cycle worth recording in the Pattern Library?

The FOA then either:

- **Approves** (NV ≤ 1) — adds both templates to the agent roster and records a Pattern
  Library entry naming both classes and their `PAIRED_WITH:` relationship
- **Escalates to FO** (NV ≥ 2) — sends FO all templates and all test results for final
  approval before activation

**In a Pair Cycle, both templates are approved or neither is.** FO or the FOA may not
activate one half of a pair while holding the other.

Once approved, both templates are active. The Observable Stream receives:
- `AgentClassCreated` for the Performer Agent
- `AgentClassCreated` for the Reviewer Agent
- `AgentPairRegistered` naming both classes and their pairing relationship

***

## Part 4: The Oversight Rule

Not every agent creation cycle needs the same level of scrutiny. The required QA depth is
determined by two scores. In a Pair Cycle, both agents are scored independently and the
**higher** score across the pair governs the QA Tier for the entire cycle.

***

### Score 1 — Blast Radius (BR)

How many future operations will this agent's template govern?

| Score | Meaning |
|---|---|
| 0 | Affects only one-off artefacts; no repeated use |
| 1 | Used repeatedly within a single feature |
| 2 | Used repeatedly across multiple features |
| 3 | Governs all tasks of a given type across the system |
| 4 | Changes how the framework itself operates |

***

### Score 2 — Novelty (NV)

How much prior evidence exists for this agent class?

| Score | Meaning |
|---|---|
| 0 | Exact pattern exists in the Pattern Library with documented results |
| 1 | Variant of a known pattern; some inference required |
| 2 | New agent class in an existing zone; no direct precedent |
| 3 | New zone, new framework primitive, or untested territory |

***

### QA Tier Assignment

```

IF NV = 3 OR BR = 4          → Tier 4: FO approves. Escalate at Step 2, before spec tests.
IF NV = 2 OR BR = 3          → Tier 3: Full cycle (Steps 1–7) + FO approves at Step 7.
IF NV = 1 OR BR ≥ 2          → Tier 2: Full cycle (Steps 1–7). FOA approves at Step 7.
IF NV = 0 AND BR ≤ 1         → Tier 1: Abbreviated cycle. Spec tests still required. FOA approves.

```

For Pair Cycles: score each agent independently, then apply the higher result to the whole
cycle.

| Tier | Name | What changes |
|---|---|---|
| **1** | Routine | Spec tests still required. Revision loop still applies. FOA approves. No FO involvement. |
| **2** | Elevated | Full 7-step cycle. FOA approves at Step 7. No FO involvement unless the FOA judges it warranted. |
| **3** | High | Full cycle + FO approves the finished templates at Step 7. FO sees: requirements, test results, final templates. |
| **4** | Critical | FO is consulted at Step 2 before spec tests are written. FO approves at Step 7. Two FO touch points. |

***

### What tier does a cycle usually get?

| Scenario | BR | NV | Tier |
|---|---|---|---|
| Revision to existing template (fixing an error) | 3 | 0 | 2 |
| New executor agent; existing reviewer reused | 3 | 0 | 2 |
| New executor + new reviewer pair; established pattern | 3 | 0 | 2 |
| New specialist QA agent for a new artefact type | 3 | 1 | 3 |
| New performer + new reviewer pair; no precedent | 3 | 2 | 3 |
| Shared zone reviewer serving 3+ performers | 4 | 2 | 4 |
| New zone or new framework primitive | 4 | 3 | 4 |
| The Base Agent Template itself | 4 | — | 4 (always) |

***

## Part 5: The Base Agent Template

Every agent template produced by this flow must conform to the following structure. Fields
marked REQUIRED must be present and non-empty for the spec tests to pass.

```


***
name: [AgentClassName]                       \# REQUIRED
description: "[One-sentence job statement]"  \# REQUIRED — what is this agent hired to do?
tools: ['tool-a', 'tool-b']                  \# REQUIRED
model: ['primary-model', 'fallback-model']   \# REQUIRED
***

ZONE: [zone-number zone-name]                \# REQUIRED
TYPE: [ORCHESTRATOR|EXECUTOR|COMPRESSION|BATCH]  \# REQUIRED
QA_TIER: [0-4]                               \# REQUIRED

REVIEWER: [ReviewerAgentClassName]           \# REQUIRED for TYPE: EXECUTOR and ORCHESTRATOR
\# Use SHARED:[class-name] for shared reviewers
\# Use NONE:FO-APPROVED:[date] only with explicit
\# written FO exemption

READS:

- [.path/to/named/file.md]                 \# REQUIRED — named files only, not categories

WRITES:

- [.path/to/output/file.md]                \# REQUIRED — exactly one artefact

NEVER:

- [.path/to/forbidden/file.md]             \# REQUIRED — at least one entry

SKILL: [skill-name]                          \# REQUIRED if agent has substantive logic
CONTEXT_TREE_REF: [context-tree.md\#node]     \# REQUIRED — where this agent sits in the tree

```

**Rules enforced by spec tests on every template:**

- READS contains named file paths — not descriptions, categories, or wildcards
- WRITES contains exactly one path — not a directory, not a pattern
- NEVER list is non-empty
- File is under 60 lines
- SKILL pointer references a file that exists at the declared path
- CONTEXT_TREE_REF is present and matches an entry in `context-tree.md`
- QA_TIER is present and set to a value between 0 and 4
- Description is a single sentence — no multi-line prose
- **REVIEWER is present and non-empty for any template with TYPE: EXECUTOR or ORCHESTRATOR**
- **The named REVIEWER class exists in the agent roster or is being created in the same
  Zone 0 cycle**

**Additional rule enforced by the Cross-Reference Test (Pair Cycles only):**

- The Reviewer Agent's READS list contains the exact file path declared in the Performer
  Agent's WRITES field

***

## Part 6: Bootstrapping Exception

The FOA and Agent Spec QA cannot be created by the Zone 0 process because Zone 0 does not
yet exist when they are first deployed. FO creates these two agents manually during initial
framework setup.

This is the **bootstrapping exception** — it applies to exactly two agents, once, at
framework initialisation.

**The bootstrapping exception satisfies the Agent Pair invariant.** The FOA and Agent Spec
QA are a de-facto pair: the FOA produces requirements and template commissions; Agent Spec
QA reviews and tests them. They were designed together, deployed together, and neither is
activatable in isolation. The bootstrapping exception is the founding precedent for the
Agent Pair rule, not an exemption from it.

All subsequent agent classes, including revisions to the FOA or Agent Spec QA, go through
the Zone 0 process. Any revision that changes the FOA's WRITES path must trigger a
corresponding review of Agent Spec QA's READS, and vice versa — even for routine revisions.

The bootstrapping exception is recorded in the framework manifest as a named decision —
not a workaround.

***

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-03-03 | Initial draft. Defines Zone 0 flow, glossary, responsibility tree, oversight tiers, and base template. |
| 0.2 | 2026-03-03 | Introduces Agent Pair as the atomic unit of Zone 0 output. Adds Performer Agent, Reviewer Agent, Shared Reviewer, Cross-Reference Test, and AgentPairRegistered event to glossary. Updates Responsibility Tree invariants, Step 2 pairing decision, Steps 3–7 parallel track for Pair Cycles, QA Tier pair-scoring rule, REVIEWER field in Base Agent Template, Pair Cycle scenario rows, and Bootstrapping Exception to acknowledge the founding pair precedent. |
```


***

A few things to note about the draft:

- **`NONE:FO-APPROVED:[date]`** is included as a deliberate escape hatch in the `REVIEWER` field for agents that are genuinely standalone (e.g. a pure compression agent with no reviewable output), but it requires an explicit FO decision rather than a silent omission[^2_1]
- **`AgentPairRegistered`** is a new Observable Stream event that sits alongside the two `AgentClassCreated` events — it makes the pairing relationship a first-class fact in the audit log, not just a field inside a template[^2_1]
- The **60-line limit** on templates is inherited from v0.1 — you may want to revisit this once you see how Pair Cycles produce two templates that reference each other; the cross-reference test file adds a third artefact to manage[^2_1]

<div align="center">⁂</div>

[^2_1]: agent-creation-policy-v0.1.md


---

# Now I want to focus on the bootstrapping phase - Zone 0 initialisation.

From our earlier experiments before we created the nexus mcp server, a library of agents, skills, instructions and patterns has grown. It makes sense to reuse these but agents only get access through the mcp server and the tools they have access to.

What are the foundational artefacts that are required at project startup?
I know there will be a base agent spec template, and I'm sure we can even create non-base agent spec templates for the common agent classes, that all follow our agent design rules for minimum viable context provision and have access to the universal tools.
We'll need a context card template perhaps.
Can we formalise the minimum context required for a project to be ready for the FOA to begin its work?
What other artefacts do we need?

This is a rich question with a lot of prior art to draw from across your files. Let me synthesise it into a structured answer.

***

## The Core Insight: Two Distinct Startup Layers

There are two things that need to exist before the FOA can work: **infrastructure** (what the MCP server provides) and **knowledge** (what the FOA reads to make decisions). These are different problems and must be separated.[^3_1][^3_2]

***

## Layer 1 — MCP Server Infrastructure

The Nexus MCP server must be running and have the following registered before any agent is invoked:[^3_3][^3_1]

**Universal tools (available to every agent, no task scope):**

- `get_context_card`
- `get_my_capabilities`
- `get_current_state`
- `raise_uncertainty`
- `search_knowledge_base`

**Management tools (FO-only at bootstrap):**

- `activate_task` / `deactivate_task`
- `get_stream_events`
- `get_audit_log`

**Schema tables that must be initialised (empty but structurally present):**

- `tasks`, `documents`, `audit_log`, `stream_events`, `tool_registry`
- `pattern_library` — even empty, the table must exist so the FOA's first `search_knowledge_base` call returns a typed empty result rather than an error[^3_3]
- `context_cards` — so `get_context_card` has a store to query

***

## Layer 2 — Governance Artefacts (Policy Documents)

These are the documents the FOA reads to know what the rules are. Without them, the FOA has no contract to work from:[^3_4][^3_2]


| Artefact | Path | Why it must exist at startup |
| :-- | :-- | :-- |
| Agent Creation Policy | `.framework/policies/agent-creation-policy.md` | The FOA's primary operating contract |
| Tool Grammar Specification | `.framework/policies/nexus-tool-grammar.md` | Required before any agent spec can name tools |
| Context Curation Policy | `.framework/policies/context-curation-policy.md` | Governs every zone; FOA references it when commissioning Context Agent specs |
| Pre-flight \& Uncertainty Protocol | `.framework/policies/preflight-uncertainty-protocol.md` | Cross-cutting; every agent spec must reference it |
| Framework Manifest | `.framework/framework-manifest.md` | Records the bootstrapping exception as a named decision; records all FO-level decisions |


***

## Layer 3 — Structural Templates

These are the blank forms every agent creation cycle produces filled versions of. They must exist before the FOA can commission any work:[^3_2][^3_5]

**`base-agent-template.md`** — the minimum valid structure every template must conform to, with all REQUIRED fields as literal placeholders. This is what Agent Spec QA tests against.

**`agent-class-requirements-template.md`** — the blank form the FOA fills in at Step 2 of every Zone 0 cycle. Having the template avoids the FOA improvising the format.

**`spec-tests-template.md`** — the blank form Agent Spec QA starts from when writing tests. Without it, every test suite risks missing structural checks (NEVER list, WRITES count, etc.).

**`context-card-template.md`** — the format every context card must conform to. This is the most important template to lock down early; without it, `get_context_card` has no schema to return.[^3_6][^3_4]

The context card template needs at minimum these sections:

```
ROLE:           [agent class name and type]
ZONE:           [zone number and name]
CURRENT_TASK:   [task or cycle identifier, or NONE if zone-level]
READS:          [the files this agent is permitted to read — named paths]
WRITES:         [the single artefact this agent produces]
NEVER:          [files this agent is forbidden from touching]
ACTIVE_POLICIES:[list of policy documents that govern this agent's behaviour]
PATTERNS:       [relevant Pattern Library entries, or NONE]
CONSTRAINTS:    [stack, environment, or scope constraints that apply right now]
OPEN_FLAGS:     [any conflicts, gaps, or uncertainties the FOA has flagged]
```


***

## Layer 4 — Pre-Built Agent Class Templates

These are the reusable agent templates from your existing library, ported into the new framework's Base Agent Template format. They exist at startup so the FOA doesn't need to run a Zone 0 cycle for classes that are already well-understood:[^3_2][^3_3]

**Zone 0 — Framework Evolution (the bootstrapping pair):**

- `agent-template-foa.agent.md` — Framework Owner Agent
- `agent-template-agent-spec-qa.agent.md` — Agent Spec QA *(this is the founding Agent Pair)*
- `agent-template-agent-template-creator.agent.md` — Agent Template Creator *(requires Agent Spec QA as its reviewer — already present)*

**Zone 3-4 — Core Execution Trio (your validated pattern from Exp-01/02):**

- `agent-template-qa-definition.agent.md`
- `agent-template-task-performer.agent.md`
- `agent-template-qa-execution.agent.md`

**Cross-cutting — Infrastructure agents:**

- `agent-template-context-agent.agent.md`
- `agent-template-uncertainty-advisor.agent.md` *(per zone, or a base with zone variants)*

Each pre-built template must already pass the Base Agent Template spec tests and have a Pattern Library entry recorded — so the FOA can reuse them at NV=0 without running a full Tier 2+ cycle.[^3_2]

***

## Layer 5 — The Context Tree

The `CONTEXT_TREE_REF` field in every agent template requires this to exist. It is a single document that maps every agent class to a node in the project's information architecture:[^3_2]

```
context-tree.md
├── zone-0/
│   ├── foa                    ← FOA node
│   ├── agent-spec-qa          ← Agent Spec QA node
│   └── agent-template-creator
├── zone-3/
│   ├── context-agent
│   └── qa-definition
├── zone-4/
│   ├── task-performer
│   └── qa-execution
└── cross-cutting/
    └── uncertainty-advisor
```

At startup, most nodes are skeletal — they just need to be present so spec tests can validate `CONTEXT_TREE_REF` references. Nodes are fleshed out as agents are commissioned.

***

## Layer 6 — Project Seed Document

This is the one artefact that is unique per project and has no template equivalent — it is what the FOA reads to understand *why* this project exists and what FO's intent is:[^3_4]

**`project-brief.md`** — contains:

- Project name and one-sentence purpose
- FO identity (who holds the human approval authority)
- Initial scope: what zones are active at startup vs. deferred
- Known constraints (tech stack, environment, timeline)
- Any deliberate deferrals from the framework (e.g. "Policy Engine is deferred — state transitions are inline for this project")
- The bootstrapping exception declaration: FOA and Agent Spec QA were created manually by FO on [date], satisfying the founding Agent Pair invariant

***

## The Formal Readiness Gate

The FOA **cannot begin Zone 0 work** until all six layers are satisfied. This can be expressed as a checklist FO runs manually before activating the FOA:

```
ZONE 0 READINESS CHECKLIST

Infrastructure
  [ ] Nexus MCP server running; all universal tools registered
  [ ] Schema tables initialised (empty is fine)
  [ ] Observable Stream active

Governance
  [ ] Agent Creation Policy present and version-stamped
  [ ] Tool Grammar Specification present
  [ ] Context Curation Policy present
  [ ] Pre-flight & Uncertainty Protocol present
  [ ] Framework Manifest present, bootstrapping exception recorded

Templates
  [ ] base-agent-template.md present and spec-testable
  [ ] agent-class-requirements-template.md present
  [ ] spec-tests-template.md present
  [ ] context-card-template.md present with all required sections

Pre-built Agent Classes
  [ ] FOA template present, passes base template spec tests
  [ ] Agent Spec QA template present, paired with FOA (AgentPairRegistered)
  [ ] Agent Template Creator template present, paired with Agent Spec QA
  [ ] Core zone 3-4 trio templates present (if zone 4 is in scope)
  [ ] Context Agent template present (if zone 3 is in scope)
  [ ] All pre-built templates have Pattern Library entries at NV=0

Context Tree
  [ ] context-tree.md present with skeleton nodes for all pre-built agents

Context Cards
  [ ] Context card exists for FOA (authored by FO manually)
  [ ] Context card exists for Agent Spec QA (authored by FO manually)

Project Seed
  [ ] project-brief.md present, includes bootstrapping exception declaration
  [ ] FO identity confirmed

GATE: FOA activation is authorised when all boxes are checked.
```

This checklist is itself a project artefact — it lives at `.framework/bootstrap/zone-0-readiness.md` and is the first thing the Framework Manifest references.[^3_1][^3_4][^3_2]

<div align="center">⁂</div>

[^3_1]: NexusToolGrammar.md

[^3_2]: agent-creation-policy-v0.1.md

[^3_3]: Nexus-agent-plan.md

[^3_4]: context-curation-pattern.md

[^3_5]: example-spec-preflight-check.md

[^3_6]: experiment-2-will-need-to-wait-0U5RBKbfTZ6BlRtDT_4fYw.md


---

# Let's start at Layer 1.

It doesn't make sense to have tools available for the FO - mcp servers are agent tools. I will need to build another layer to have visibility of stream events and the audit log so leave that aside for now.

Our nexus experiments have not touched the universal tools yet.
Start by describing each tool in detail.

Good — now I have all the source material needed. Here is a detailed spec for each universal tool.

***

## Universal Tools — Detailed Specifications

These five tools are registered once on the Nexus MCP server at startup and given to **every agent without exception**. They carry no task suffix. They represent the minimum capability floor every agent in the system has — before any role-specific or task-scoped tools are added.[^4_1]

***

## `get_context_card`

**What it does:** Returns the pre-generated context card for the calling agent. This is always the **first call an agent makes** before any other tool. The card tells the agent who it is, what it is permitted to touch, which policies govern it, and what its current operating context is.[^4_2][^4_1]

**Verb rationale:** `get_` not `read_` — context cards are system-level resources, not task documents. The distinction matters because `get_` writes an audit entry, creating chain-of-custody evidence that the agent loaded a specific version of its card. `read_` produces no audit entry.[^4_1]

**Parameters:**

```typescript
{
  agent_name: string      // REQUIRED — the calling agent's class name as declared in its template
  task_id?: string        // OPTIONAL — if task-scoped, narrows card to task context
}
```

**Returns:**

```typescript
{
  role: string                  // agent class name and type
  zone: string                  // zone number and name
  current_task: string | null   // task or cycle identifier, or null
  reads: string[]               // permitted READS paths for this agent
  writes: string[]              // the single WRITES path for this agent
  never: string[]               // NEVER paths — forbidden unconditionally
  active_policies: string[]     // policy documents that govern this agent right now
  patterns: PatternEntry[]      // relevant Pattern Library entries, or []
  constraints: string[]         // stack, environment, or scope constraints
  open_flags: string[]          // conflicts, gaps, or uncertainties the FOA has flagged
  card_version: string          // version hash — recorded in audit log
  generated_at: string          // ISO timestamp of card generation
}
```

**Side effects:**

- Writes one `audit_log` entry: `{ tool: 'get_context_card', actor, card_version, timestamp }`
- No state change. No stream event.

**Failure modes:**

- `CARD_NOT_FOUND` — no card exists for this agent name. Agent must call `raise_uncertainty` immediately; it cannot operate without a card
- `CARD_STALE` — the card's source artefacts have changed since it was generated. Returns the card with a `stale: true` flag; agent must treat this as `ASSUMED` in the pre-flight sense

**Key invariant:** An agent that has not called `get_context_card` has no verified identity within the system. All subsequent tool calls are traceable back to the card version that was active when they were made.[^4_3][^4_1]

***

## `get_my_capabilities`

**What it does:** Returns the complete list of tools currently registered to the calling agent, grouped by scope (universal / role-scoped / task-scoped). Allows an agent to verify at runtime that it has the tools it expects before attempting to call them.[^4_1]

**Verb rationale:** `get_` — this is system metadata about the tool registry, not a document. It reflects the current state of what is registered, which can change (e.g. task-scoped tools appear when a task is activated and disappear when it is deactivated).[^4_1]

**Parameters:**

```typescript
{
  agent_name: string    // REQUIRED — must match the name in the calling agent's context card
}
```

**Returns:**

```typescript
{
  universal: string[]        // tools available to all agents — always the same 5
  role_scoped: string[]      // tools available to this agent class across all tasks
  task_scoped: string[]      // tools available to this agent for its current task(s)
  total_count: number
  registry_snapshot_at: string  // ISO timestamp — when the registry was last updated
}
```

**Side effects:**

- Writes one `audit_log` entry: `{ tool: 'get_my_capabilities', actor, timestamp }`
- No state change. No stream event.

**Primary use:** An agent calls this after `get_context_card` if it needs to confirm that a task-scoped tool it expects (e.g. `submit_proof_task_07`) is actually present before building a work plan that depends on it. If a required tool is absent, the agent calls `raise_uncertainty` rather than proceeding on the assumption that the tool will appear.[^4_4][^4_1]

**Key invariant:** The tool list returned here is the ground truth. An agent spec declaring a tool that does not appear in `get_my_capabilities` is operating on a stale or incorrect spec — this is a framework defect, not an agent error.

***

## `get_current_state`

**What it does:** Returns the current lifecycle state of a task, feature, or zone-0 cycle. Lets an agent confirm that the state machine is in the expected position before taking an action that has state preconditions.[^4_4][^4_1]

**Verb rationale:** `get_` — lifecycle state is system metadata, not a document. It is managed by the Nexus state machine, written only by `submit_` tool calls, and read by agents via this tool rather than by querying the database directly.[^4_1]

**Parameters:**

```typescript
{
  entity_type: 'task' | 'feature' | 'zone0_cycle'  // REQUIRED
  entity_id: string                                  // REQUIRED — task ID, feature slug, or cycle ID
}
```

**Returns:**

```typescript
{
  entity_type: string
  entity_id: string
  current_state: string            // e.g. 'PUBLISHED', 'PROOFSUBMITTED', 'APPROVED'
  entered_at: string               // ISO timestamp when this state was entered
  entered_by: string               // actor that triggered the state transition
  permitted_next_states: string[]  // what transitions are valid from here
  permitted_actors: string[]       // which agent classes may trigger those transitions
}
```

**Side effects:**

- Writes one `audit_log` entry: `{ tool: 'get_current_state', actor, entity_id, state_seen, timestamp }`
- No state change. No stream event.

**Why audit-log a read?** The `get_` verb always writes an audit entry. For `get_current_state` specifically, recording which state an agent saw before taking an action is important for diagnosing race conditions or unexpected transitions. The audit trail answers: *"what did this agent believe the state was when it called `submit_proof`?"*[^4_1]

**Key invariant:** No agent may attempt a state-transitioning `submit_` call without first confirming via `get_current_state` that the precondition is met. If the state is not what the agent expects, it calls `raise_uncertainty` — it does not guess that the transition will succeed.[^4_4]

***

## `raise_uncertainty`

**What it does:** Surfaces an exceptional condition to human attention immediately, bypassing normal workflow. This is the system's safety valve — the one tool that any agent can call at any moment to stop progress and flag that something is wrong or unknowable.[^4_4][^4_1]

**Verb rationale:** `raise_` is a closed singleton verb — its only valid subject is `uncertainty`. It is not a `request_` (which is for normal cross-agent signalling) and not a `write_` (which is for routine document creation). It signals an out-of-band condition that cannot be handled within the normal flow.[^4_1]

**Parameters:**

```typescript
{
  what: string           // REQUIRED — what is unclear, missing, or contradictory. Free text.
  why: string            // REQUIRED — why this blocks progress. Free text.
  needed: string         // REQUIRED — what information or decision would resolve it. Free text.
  context_paths: string[] // REQUIRED — the files the agent was reading when it encountered this.
                          // Minimum one entry. An uncertainty with no context is untraceable.
  severity: 'BLOCKED' | 'ASSUMED'
                         // REQUIRED — BLOCKED: agent has stopped entirely.
                         //            ASSUMED: agent is proceeding with a declared assumption
                         //            but human review is requested.
}
```

**Returns:**

```typescript
{
  uncertainty_id: string   // assigned by the server — used to track and resolve the entry
  logged_at: string        // ISO timestamp
  state_transition: string | null
                           // if severity == BLOCKED, the entity transitions to BLOCKED state
                           // if severity == ASSUMED, no state change — agent may continue
}
```

**Side effects:**

- Appends to the `uncertainty_log` for the relevant task/feature/cycle
- Writes a **priority** `stream_events` entry — visually distinct from standard events; FO sees this immediately
- Writes `audit_log` entry
- If `severity == BLOCKED`: transitions the entity state to `BLOCKED` or `AWAITING_HUMAN`
- If `severity == ASSUMED`: no state transition; the assumption is logged but work continues

**What it is NOT:**

- Not an error handler — tool errors return typed error responses in the tool's return value. `raise_uncertainty` is for *semantic* uncertainty: situations where the agent cannot determine the correct action from its available context, regardless of whether the tools are working[^4_1]
- Not a way to avoid work — the `why` and `needed` fields are mandatory precisely to prevent agents from raising uncertainty without articulating what would resolve it

**Key invariant:** Any agent may call this tool at any time. It is never restricted by role or zone. An agent spec that instructs an agent to never call `raise_uncertainty` is a framework invariant violation.[^4_4][^4_1]

***

## `search_knowledge_base`

**What it does:** Queries the pattern library and accumulated project knowledge. Returns entries relevant to the query — prior decisions, documented patterns, sprint learnings, known constraints — ranked by relevance. This is how agents access institutional memory without having file-read access to the entire knowledge store.[^4_1]

**Verb rationale:** `search_` is reserved exclusively for the knowledge base and pattern library. It never operates on primary task documents — those are accessed via `read_`. The distinction is intentional: primary documents are deterministic (you know the path), knowledge base queries are probabilistic (relevance-ranked).[^4_1]

**Parameters:**

```typescript
{
  query: string          // REQUIRED — free text query describing what knowledge is sought
  tags?: string[]        // OPTIONAL — filter by category tags (e.g. ['zone-0', 'agent-creation', 'pattern'])
  limit?: number         // OPTIONAL — max entries to return. Default: 5. Max: 20.
  source_zone?: string   // OPTIONAL — restrict results to knowledge from a specific zone
}
```

**Returns:**

```typescript
{
  entries: KnowledgeEntry[]
  total_matched: number
  query_interpreted_as: string   // the server's interpretation of the query — helps detect mismatches
}

type KnowledgeEntry = {
  entry_id: string
  title: string
  summary: string            // max 3 sentences — never full content
  relevance_score: number    // 0–1
  tags: string[]
  source_zone: string
  source_session: string     // when this knowledge was recorded
  pattern_library_ref?: string  // if this entry has a Pattern Library counterpart
  full_content_available: boolean
                             // true if the agent has a read_ tool that can fetch the full entry
                             // false if it is outside the agent's READS scope
}
```

**Side effects:**

- None. Read-only against knowledge base tables.
- No audit entry (consistent with `search_` verb semantics — no side effects)[^4_1]

**Key design decision:** Results return summaries, not full content. An agent that needs the full content of a Pattern Library entry must have a `read_` tool scoped to that document. This prevents `search_knowledge_base` from becoming a backdoor to content that the agent's READS list deliberately excludes. The `full_content_available` flag tells the agent whether it has that access.[^4_1]

**Primary use cases:**

- FOA checking whether a Pattern Library entry exists for a proposed agent class before assigning an NV score
- Task Performer checking whether a similar task has been performed before
- Any agent checking for known constraints or prior decisions relevant to its current work
- Agent Template Creator checking for existing agent patterns before building a new template from scratch

***

## How the Five Work Together

The universal tools form a deliberate **startup sequence** that every agent follows before doing any role-specific work:[^4_3][^4_4]

```
1. get_context_card          ← Who am I? What am I permitted to do?
2. get_my_capabilities       ← Do I have the tools my spec says I should have?
3. get_current_state         ← Is the entity I'm about to act on in the right state?
4. search_knowledge_base     ← Has this been done before? Are there known patterns or constraints?
                                (called when relevant — not always mandatory at startup)

── If anything from steps 1–4 is wrong or unclear ──
5. raise_uncertainty         ← Stop. Surface it. Don't guess.
```

Steps 1–3 collectively constitute what the pre-flight protocol  calls the precondition check — the difference is that in the Nexus tool grammar, those checks are distributed across three well-named tools rather than bundled into a single `preflight_check` call. This is a deliberate design choice: each tool has exactly one subject and one verb, making the audit log granular enough to diagnose exactly which precondition failed.[^4_4][^4_1]

<div align="center">⁂</div>

[^4_1]: NexusToolGrammar.md

[^4_2]: Nexus-agent-plan.md

[^4_3]: example-spec-preflight-check.md

[^4_4]: preflight-check-protocol.md


---

# let's stop. I'm glad you mentioned that currently `read_` doesn't produce an audit entry.

Are there currently other verbs that don't produce an audit entry?
I want everything recorded, even reads. Every action take by an agent or human needs to be recorded. It's the only way we can have a true and complete picture of what happened.

Based on the Tool Grammar specification, there are exactly two verbs that currently produce **no audit entry**:[^5_1]

***

## The Two Audit Gaps

### `read_`

> *"Side effects: None. No audit entry. No state change. No stream event."*

This is the larger gap. Every `read_task_spec_task_07`, `read_proof_template_task_07`, `read_qa_review_task_07` — none of them are recorded. You cannot currently reconstruct what an agent was reading when it made a decision.[^5_1]

### `search_`

> *"Side effects: None. Read-only operation against the knowledge base tables."*

Every `search_knowledge_base` call is silent. You cannot tell that an agent checked the pattern library, what query it ran, or what it found — or didn't find.[^5_1]

***

## Every Other Verb Already Records

| Verb | Audit entry? |
| :-- | :-- |
| `get_` | ✅ Yes — explicitly designed to audit because context reads matter |
| `write_` | ✅ Yes |
| `append_` | ✅ Yes |
| `submit_` | ✅ Yes |
| `request_` | ✅ Yes |
| `raise_` | ✅ Yes |
| `read_` | ❌ No |
| `search_` | ❌ No |

The interesting thing is that `get_` was *deliberately* given an audit entry precisely because *"the audit record captures which version an agent was working from"*. That same reasoning applies equally to `read_` and `search_` — and arguably more so, since `read_` tools are far more numerous and are called constantly throughout every task.[^5_1]

***

## The Required Change

Both verbs need a lightweight audit entry added to their specifications:

**For `read_`:**

```
Side effects: Writes one audit_log entry
  { tool: read_{subject}_{task_slug}, actor, doc_version_hash, timestamp }
```

The `doc_version_hash` is important — it records *which version* of the document the agent read, not just that it read it. If a document is revised mid-task, the audit log will show that the agent was working from version N when it made a given decision.

**For `search_`:**

```
Side effects: Writes one audit_log entry
  { tool: 'search_knowledge_base', actor, query, tags, result_count,
    top_entry_ids[], timestamp }
```

Logging `query` and `top_entry_ids` is what makes this useful — it answers *"what did the agent look for, and what did it find?"* A bare timestamp with no query text would be an audit entry that can't be reasoned about.

***

## The Downstream Implication

This change should be reflected in two places in the Tool Grammar specification:

1. **The verb definitions** — update `read_` and `search_` to include the audit side effect
2. **Rule 5 (side effect classification)** — the current rule states *"If there are zero side effects, the verb is `read_`, `search_`, or `get_`"*. With this change, `get_` was already the exception. The rule needs updating to:
```
IF there are zero side effects → the verb is read_ or search_
IF the only side effect is an audit entry → the verb is read_, search_, or get_
IF there are side effects but no state transition → write_ or append_
IF there is a state transition → submit_
IF the only side effect is a stream event with no document write → request_ or raise_
```

That keeps the classification clean while accurately reflecting that all seven non-`raise_` verbs now produce an audit entry.

This is a v0.2 change to `NexusToolGrammar.md` — small in scope but significant in principle, and it needs to be made before the server is built so the audit schema is designed with this in mind from the start.

<div align="center">⁂</div>

[^5_1]: NexusToolGrammar.md


---

# i must not have seen this when we first created the grammar. My fault for not reviewing properly.

But this helps me see that we need a definitive guiding principles document so that every downstream policy, design doc or template adheres to these principles.

We'll work on this together. What can you tell me about the ideas behind the agentic development framework we are designing and experimenting with?

This is a rich body of work. Let me lay out the ideas as they actually emerged — not as a polished list, but as the intellectual progression that got here.

***

## The Problem Being Solved

The starting point is a specific failure mode in AI agent systems that most frameworks ignore: **agents that are well-instructed still exceed their scope**. Longer `NEVER` clauses, more rules in system prompts, more detailed instructions — none of these prevent a determined or confused agent from calling the wrong tool, writing to the wrong file, or reporting success on a test that ran in the wrong environment. The rules can always be violated, misread, or half-followed.[^6_1]

The framework's founding question is: *what if violations were structurally impossible rather than instructed against?*[^6_2]

***

## The First Load-Bearing Idea: OCAP

The answer is borrowed from a 30-year-old principle in computer security called the **Object Capability Model**. The idea is disarmingly simple: a capability is not a permission you check against a list — it is a reference you either possess or don't. If an agent doesn't have a reference to a tool, it cannot call that tool. There is no rule to violate, no check to bypass. The violation is architecturally absent.[^6_2]

This reframes the entire access control problem. The question is never *"is this agent allowed to do X?"* — it is *"does this agent have a tool named X?"*  If not, the answer is settled before any server call is made. VS Code enforces this at the client layer.[^6_3]

The discovery during Experiment 01 was that this also made authentication irrelevant — not deferred, irrelevant. The MCP spec prohibits using session IDs for authorisation. STDIO transport has no auth layer. Rather than being gaps, these turned out not to matter: OCAP is structurally stronger than any identity check because identity can be spoofed and edge cases exist, but absent capabilities cannot.[^6_4]

***

## The Second Idea: Behaviour Belongs Inside Tools

Even with OCAP enforcing *which* tools an agent can call, you still have the problem that mandatory consequences — state transitions, audit entries, stream events — depend on the agent doing the right thing after calling a tool.[^6_3]

Experiment retrospectives had shown agents complying superficially with multi-step instructions but executing them partially or out of order. The fix is: **mandatory side effects live inside the tool, not in instructions to the agent**. A `submit_proof` call atomically writes the proof document, transitions state, emits a stream event, and writes an audit entry. All in one call. The agent cannot forget to emit the stream event because there is nothing to forget — the behaviour is structural, not instructed.[^6_2][^6_3]

This principle generalises to: *if something must happen, it must be inside a tool, not described to an agent*.

***

## The Third Idea: Complete Observability Without Being a Chokepoint

The framework needs to see everything that happens — not just what goes through its own tools, but also code operations that go through GitHub independently. The naive solution is to intercept GitHub calls. This was explicitly rejected because it creates a permanent maintenance obligation against a fast-moving external dependency.[^6_1][^6_3]

Instead, GitHub's native webhook mechanism fires events to Nexus on every push, PR, review, and merge. Nexus never intercepts GitHub — it observes after the fact. The branch naming convention is the join key. The result is a single audit log with complete coverage across two independent systems, reconstructable from one SQL query.[^6_4][^6_3]

This led to a principle that runs through everything: **the audit log must contain a complete and true record of what happened**. Not a summary. Not a sample. Everything. Every agent action, every human gate, every GitHub event, every context card fetch, every knowledge base query. This is what makes the system trustworthy in a legal and organisational sense — not just functionally correct, but *verifiably correct*.[^6_5]

***

## The Fourth Idea: The Grammar as Design Constraint

The tool naming grammar (`{verb}_{subject}_{task_scope}`) was designed for organisation — to keep the tool catalogue from becoming unmaintainable as roles and document types multiply. What was discovered during Experiment 01 was something more important: **the grammar is a design tool, not documentation**.[^6_6][^6_7]

The `get_` audit gap was not designed. It was *found* by running the chain-of-custody test and noticing a hole. When `get_context_card` produced no audit entry, you couldn't reconstruct what information an agent was working from when it made a decision. Promoting `get_` to an audit-writing verb filled the gap without changing the architecture. Today, the same process surfaced the `read_` and `search_` gaps.[^6_4]

The principle this points to: *a well-constructed grammar makes its own violations visible under test*. The grammar is not descriptive — it is prescriptive, and when you violate it, the tests find it.

***

## The Fifth Idea: The ONE Ontology

As the design grew, six recurring questions kept appearing for every proposed tool, schema table, or agent spec:[^6_5]

- *Who is permitted to do this?* — **Capability**
- *Who did this, and can it be disputed?* — **Accountability**
- *Does this output meet the standard?* — **Quality**
- *Is this the right moment?* — **Temporality**
- *Does the agent have what it needs?* — **Context**
- *What exactly was produced, and from what?* — **Artifact**

Most frameworks answer these in different places — permissions in one config, quality rules in another, lifecycle state in a task manager. The result is coherence in parts but not as a whole. The ONE Ontology is the decision to answer all six questions in one unified structure, so every component is an expression of the same model.[^6_5]

The ontology's power is not in any single dimension — it is in how they constrain each other. A gap in any one produces a named category of failure. Without Capability enforcement, agents exceed their scope. Without Accountability, no chain of custody. Without Quality gates, passing tests don't mean correct outcomes. Without Temporality, operations occur out of order. Without Context, agents operate with incomplete information silently. Without Artifact lineage, outputs are isolated facts rather than a traceable record.[^6_5]

***

## The Sixth Idea: No Agent Reviews Its Own Work

This emerged from sprint experiments before Nexus existed and was validated repeatedly. The cost of adding a reviewer agent is low. The benefit — catching errors before they become the ground truth that everything downstream is built on — consistently exceeds that cost.[^6_8]

The principle generalised to: *no artefact produced by an agent becomes authoritative without at least one independent review by a different agent*. This applies structurally: the QA Definition Agent writes the proof template; the Task Performer cannot define its own completion criteria. The Agent Template Creator builds the template; Agent Spec QA tests it. Neither can review their own work because they don't have the tools.[^6_9][^6_8]

The Agent Pair concept is the direct expression of this at the Zone 0 level: you cannot create a Performer without simultaneously creating its Reviewer.

***

## The Seventh Idea: Minimum Sufficient Context

The empirical finding that drove the Context dimension of the ontology is that **giving an agent more instructions degrades performance, not improves it**. Every additional rule in a system prompt competes for the same finite attention. The answer is context cards: a short, generated briefing containing only what is relevant to *this specific agent for this specific task*, composed from a growing knowledge base of sprint learnings and patterns at the moment of instantiation.[^6_5]

The knowledge base accumulates from retrospectives — not as prose appended to agent specs, but as structured, queryable entries. Context is the mechanism that keeps agent performance high as the framework's knowledge grows, without the overhead growing with it.[^6_5]

***

## The Eighth Idea: Human Authority at Irreversible Decisions

The framework is designed to be self-advancing and self-governing — the pipeline moves forward without a human managing the flow. But there are specific moments that are irreversible commitments, and those remain human decisions:[^6_10][^6_5]

- Task publication — a commitment to execution
- Zone delivery — a commitment to user testing
- NV ≥ 2 agent creation — a commitment to new framework territory

The FO approves at these gates, not at every step. The framework's purpose is to make that possible — to reduce human involvement to the decisions that genuinely require human judgement, and to handle everything else structurally.[^6_1]

***

## The Meta-Idea: Prove Before Building

Running through all of it is a methodology: **never build what you haven't proved needs to exist**. The hypothesis card format, the per-phase pass criteria, the explicit assumption maps — these are not bureaucracy. They are the mechanism by which the framework tests itself rather than accumulating speculative complexity.[^6_4]

The most important finding from Experiment 01 was not that the hypotheses passed. It was that the build-test-improve loop was tight enough to surface real design improvements in a single day's work. The grammar improved itself. That feedback loop is the methodology, and the methodology applies to everything — including the governance documents, policies, and templates being designed now.

***

These eight ideas are the raw material for a guiding principles document. They are not all at the same level of abstraction, and some are more foundational than others — but together they describe everything the framework has committed to and why. The question for the principles document is how to organise and state them so that a designer encountering any downstream decision can derive the right answer without having to read the full history.

<div align="center">⁂</div>

[^6_1]: Nexus-101.md

[^6_2]: NexusModelOverview.md

[^6_3]: NexusDecisionsRationale.md

[^6_4]: Nexus-exp01-retro.md

[^6_5]: ONE-Ontology.md

[^6_6]: NotesOnExp1Retro.md

[^6_7]: NexusToolGrammar.md

[^6_8]: experiment-2-will-need-to-wait-0U5RBKbfTZ6BlRtDT_4fYw.md

[^6_9]: agent-creation-policy-v0.1.md

[^6_10]: context-curation-pattern.md


---

# Great.

The genesis of this project is in another space where I am researching how AI can reduce coordination costs for human knowledge work.
I want to bring trust to AI agent systems in an elegant way.
From understanding reference materials on context engineering and personal experience, we see that for the best likelihood of successful output, an agent should have as little context as possible and this then requires smaller tasks. But since the cost of agents is trivial, we can have as many as we want to deliver work that normally a single human might do on their own.
But part of the trust will come from the immutable record of all actions taken, as is reflected in the ontology model. It is also important in this experimentation stage as we want to know what is working and what isn't, and why.

What are your suggestions for formalising these ideas as guiding principles? And are there other principles we should consider?

This is the right moment to write this document — before another downstream policy or template is created without it. Here are my suggestions, including principles not yet explicitly stated anywhere in your existing work.

***

## Recommended Format for Each Principle

For a principle to be useful to a designer making a downstream decision, it needs more than a statement. Each entry should have four parts:

```
NAME:               Short, memorable — becomes the reference handle
STATEMENT:          One declarative sentence. Not a rule — a truth.
RATIONALE:          Why this is true for this framework specifically.
VIOLATION LOOKS LIKE: What a designer would observe if this principle were being broken.
```

The "violation looks like" field is what makes the document testable rather than aspirational. Any proposed tool, policy, or template should be evaluable against each principle — and if it violates one, the violation should be nameable.

***

## The Principles

Organised in four tiers from most foundational to most operational.

***

### Tier 1 — Purpose

*Why the framework exists. Everything else is derived from these.*

**P1 — Coordination Cost Is the Problem**
> AI agents can reduce the coordination costs of human knowledge work toward zero — but only if the agents can be trusted. The framework exists to make that trust structurally justifiable, not assumed.

*Rationale:* Traditional knowledge work carries high coordination costs: time spent verifying who did what, whether it was done correctly, and whether the right information was available. If agents cannot be trusted to stay within scope, produce verifiable outputs, and escalate when uncertain, they add coordination cost rather than removing it. The entire architecture is an answer to the question: *how do you make delegation to AI agents safe enough to be worth it?*[^7_1][^7_2]

*Violation looks like:* A framework element that increases FO's oversight burden rather than reducing it — requiring more human review, not less.

***

**P2 — Agent Cost Is Asymmetric to Task Cost**
> Agent invocations are near-zero cost; defects that propagate downstream are not. This asymmetry justifies investing in correctness at every step.

*Rationale:* A single human doing a task end-to-end might skip a review step because their time is scarce. Agent time is not scarce. A QA cycle that costs a human 30 minutes costs an agent almost nothing. This asymmetry is the economic justification for spec-before-execution, independent review, proof templates, and multiple QA cycles — patterns that would be considered overhead in human workflows.[^7_3][^7_4]

*Violation looks like:* Skipping a review step or reducing QA depth on the grounds that it "adds too much overhead."

***

### Tier 2 — Trust Foundations

*What makes the framework structurally trustworthy. These cannot be compromised.*

**P3 — Structure Over Instruction**
> Violations must be architecturally impossible, not instructed against.

*Rationale:* Instructions can be misread, partially followed, or ignored. An agent that does not possess a tool cannot call it — there is nothing to instruct against. OCAP turns the absence of capability into a structural guarantee rather than a compliance expectation. Every `NEVER` clause in an agent spec that is not also enforced by tool absence is a convention masquerading as a constraint.[^7_5][^7_6][^7_7]

*Violation looks like:* An access boundary enforced only by a `NEVER` list or a system prompt instruction, with no corresponding absence of tool.

***

**P4 — Mandatory Consequences Belong Inside Tools**
> If something must happen when an action is taken, it must be implemented inside the tool — not described to the agent.

*Rationale:* Agents comply superficially with multi-step instructions but may execute them partially or out of order. A `submit_proof` tool that atomically writes the proof, transitions state, and emits an audit entry cannot be half-executed. The agent has no choice — the consequences are unconditional. This principle is what makes the audit log complete and the state machine consistent.[^7_6]

*Violation looks like:* An agent spec that says "after calling X, also do Y" — where Y is mandatory. Y belongs inside X.

***

**P5 — Every Action Is Recorded**
> Every action taken by any agent or human, including reads and queries, must produce an immutable audit entry.

*Rationale:* A complete picture of what happened — and why — requires recording not just what was written, but what was read. An agent reading the wrong version of a spec, or not finding a relevant pattern, is causally significant. Partial audit logs produce partial understanding. Trust in the system's outputs depends on being able to reconstruct the full causal chain, not just the mutation events.[^7_2][^7_7]

*Violation looks like:* Any tool call that takes no action in the audit log. (`read_` and `search_` before today's correction being the live example.)

***

**P6 — Evidence, Not Assertion**
> Proof of completion is literal captured output, not a claim that work is done.

*Rationale:* Agents can sincerely believe they have completed a task and be wrong. Sprint retrospectives showed this failure mode repeatedly — an agent reports success; downstream work proceeds on that basis; the defect surfaces later at higher cost. The proof template requires the agent to submit the actual command output, the actual test results, the actual exit codes — not a summary of them. The QA agent verifies against those, not against the agent's confidence.[^7_4][^7_3]

*Violation looks like:* A proof submission containing prose descriptions of what was done rather than literal captured output from the tools that did it.

***

### Tier 3 — Work Design

*How work is structured so the trust foundations hold at the agent level.*

**P7 — Minimum Sufficient Context**
> An agent should receive exactly the context it needs for its specific task — no more, no less.

*Rationale:* More context degrades performance, not improves it. Every rule competing for the same finite attention window reduces the signal of the rules that matter. Context cards are generated, not written once — they are composed from the knowledge base at instantiation time, filtered to the specific agent and task. The curator never summarises source artefacts; selection and exclusion are the tools, not compression.[^7_8][^7_2]

*Violation looks like:* Appending more rules to an agent spec when quality problems emerge, rather than improving the context card.

***

**P8 — Separate Definition, Execution, and Verification**
> No single agent defines what done looks like, performs the work, and verifies it is done.

*Rationale:* These are three structurally distinct concerns that belong to three structurally distinct roles. Conflating any two produces either the agent marking its own homework (self-review) or the executor setting its own bar (self-definition). The QA Definition Agent writes the proof template. The Task Performer implements against it. The QA Execution Agent verifies the evidence. No tool permits crossing these boundaries.[^7_9][^7_3]

*Violation looks like:* An agent with both a `write_proof_template` tool and a `submit_proof` tool — or an agent with both `write_task_spec` and `submit_qa_review` tools.

***

**P9 — Fail Loudly, Never Silently**
> An agent that cannot proceed with justified confidence must surface that condition immediately. Silent assumptions are worse than stopped work.

*Rationale:* The failure mode that motivated this principle is not crashing — it is producing plausible-looking output built on an unacknowledged assumption. That output becomes the ground truth for downstream work. The defect multiplies. `raise_uncertainty` is a universal tool precisely because this principle applies in every zone, at every role level. A blocked agent that stops and flags is recoverable. A confident agent that guesses propagates the error.[^7_10][^7_3]

*Violation looks like:* An agent spec with no `raise_uncertainty` tool, or one where the pre-flight check can be bypassed.

***

**P10 — Irreversible Decisions Require Human Authority**
> Any commitment that cannot be undone — publishing to production, activating an untested agent class, creating a public record — requires explicit FO authorisation.

*Rationale:* The framework is designed to be self-advancing and to minimise human involvement in routine flow. But autonomy is not appropriate at moments of irreversible commitment. The FO approval gates at task publication, feature delivery, and NV ≥ 2 agent creation are not bottlenecks — they are the points where the human remains genuinely accountable for what the system does next.[^7_8][^7_9]

*Violation looks like:* A state transition to an irreversible state triggered automatically by a policy, without a human gate.

***

**P11 — Oversight Is Proportional to Risk**
> The depth of QA applied to any artefact is proportional to its blast radius and novelty — not applied uniformly.

*Rationale:* Uniform QA depth is either too heavy for routine work or too light for novel framework primitives. The NV/BR scoring system calibrates oversight to the specific risk profile of each artefact type. Routine work at NV=0 moves fast. Novel framework-level work at NV=3 gets maximum scrutiny. The framework gets faster as patterns mature and evidence accumulates.[^7_3][^7_9]

*Violation looks like:* Applying Tier 4 scrutiny to a routine template revision, or Tier 1 scrutiny to a new zone primitive.

***

### Tier 4 — Framework Evolution

*How the framework improves itself without accumulating accidental complexity.*

**P12 — Conventions Are Load-Bearing**
> Naming conventions, file paths, grammar rules, and template structures are structural elements — not style choices.

*Rationale:* The tool grammar's `{verb}_{subject}_{task_slug}` format is not cosmetic. It is what makes the audit log self-describing, what allows tools to be derived rather than invented, and what makes the chain of custody reconstructable without a schema lookup. A single deviation from a naming convention creates a gap in traceability that may only surface when trying to diagnose a failure.[^7_7][^7_11]

*Violation looks like:* A tool named outside the grammar, a file path that deviates from the declared structure, or a document type with no entry in the Subject Vocabulary.

***

**P13 — Prove Before Building**
> No framework element is added without a falsifiable hypothesis, stated acceptance criteria, and literal evidence of the result.

*Rationale:* The experiment methodology — hypothesis cards, per-phase pass criteria, explicit assumption maps — is not bureaucracy for a small project. It is the feedback loop that makes the grammar improve itself. The `get_` audit rule was found by running the H5 chain-of-custody test and noticing a hole — not by design review. Design speculation without evidence accumulates as technical debt. Small scoped probes produce evidence cheaply.[^7_12][^7_7]

*Violation looks like:* Adding a new tool, schema table, or agent class because it "seems useful," without a hypothesis that could be falsified.

***

**P14 — The Framework Learns From Its Own Operations**
> Every completed task, QA finding, and uncertainty raised is a potential Pattern Library entry. The framework grows smarter through retrospectives, not through longer agent specs.

*Rationale:* The alternative — encoding learnings directly into agent specs — causes specs to grow without bound and context quality to degrade (P7). The Pattern Library is the mechanism by which experience accumulates in a structured, queryable form that the Context Agent can compose into cards. A framework that cannot learn from its own operations has no path to NV=0 for any class of work.[^7_13][^7_2]

*Violation looks like:* A retrospective finding that is appended to an agent spec rather than recorded as a structured Pattern Library entry.

***

## Principles Worth Adding That Aren't in the Existing Work

The fourteen above are all grounded in your existing documents. Three additional ones are worth considering that aren't explicitly stated anywhere yet:

**P15 — One Agent, One Artefact**
> Every agent produces exactly one artefact per invocation. An agent that produces multiple outputs has multiple responsibilities — split it.

This is implicit in the Base Agent Template's single `WRITES:` field but is never stated as a principle. It directly governs how agents are decomposed and prevents scope creep at the design stage.

**P16 — The Observer Never Controls**
> Nexus observes all activity — including GitHub events it did not execute — but never intercepts or controls systems it does not own.

This is the webhook design decision's philosophical underpinning, but stated as a principle it has broader applicability: the audit log is a passive record, not a control mechanism. The framework maintains observability without creating chokepoints.[^7_5][^7_6]

**P17 — Trust Is Progressive**
> New patterns start at maximum scrutiny and earn reduced oversight through accumulated evidence of correct behaviour.

This is the NV scoring logic stated as a principle. A pattern that has been run ten times with passing evidence is at NV=0. Its first run was at NV=2 or 3. Trust is not granted — it is accumulated through the audit record. This connects directly back to P1: the framework is a trust-building mechanism, and the Pattern Library is where that trust is stored.[^7_9]

<div align="center">⁂</div>

[^7_1]: Nexus-101.md

[^7_2]: ONE-Ontology.md

[^7_3]: experiment-2-will-need-to-wait-0U5RBKbfTZ6BlRtDT_4fYw.md

[^7_4]: TaskAsQuasiSmartContract.md

[^7_5]: NexusModelOverview.md

[^7_6]: NexusDecisionsRationale.md

[^7_7]: Nexus-exp01-retro.md

[^7_8]: context-curation-pattern.md

[^7_9]: agent-creation-policy-v0.1.md

[^7_10]: session-summary-20260303-a.md

[^7_11]: NexusToolGrammar.md

[^7_12]: NotesOnExp1Retro.md

[^7_13]: Nexus-agent-plan.md


---

# brilliant. let's remember this and lock it in as a seminal document for this space. We should see it as a living document we can add to or adapt as we understand more.

Let's take this opportunity to revisit all the policies and decisions we have made up to this point, but perhaps from a first principles approach.

If we started today with this principles document, what would be our next steps?

This is the right strategic pause. Let me reason through this carefully — what the derivation order would be, how it compares to what we've already built, and where the gaps are.

***

## First: What the Principles Document Is

Before we derive anything, the document needs one thing we haven't stated yet: a **compliance test**. Every downstream policy, design document, and template should be able to answer:

> *"Which principles does this implement, and which principles would be violated if this were removed?"*

If a document can't answer that, it is either aspirational or orphaned. This gives us a way to audit everything we've already built.

***

## The Derivation Order From First Principles

Starting only with the 17 principles, here is the order in which things must be built — and why each step is a prerequisite for the next.

***

### Derivation Step 1 — The Grammar and Schema

**Principles driving this:** P3, P4, P5, P12

Before a single tool is built, you need the naming grammar and audit schema, because:

- P3 says violations must be structurally impossible → tool names must encode capability and scope unambiguously
- P4 says consequences belong inside tools → tools need a schema to write to
- P5 says every action is recorded → the audit schema must be designed for completeness *before* tools are written, not retrofitted
- P12 says conventions are load-bearing → the grammar must precede any implementation

**What we have:** Tool Grammar v0.1 ✅ — but it needs to be v0.2 to satisfy P5, which would have been caught at design time if the principles had existed first. The `read_` and `search_` audit gap is exactly the kind of defect P5 is designed to prevent upstream.

**What would change:** The grammar document would explicitly reference P3, P4, P5, and P12. Any designer reading it would know *which principle* each rule serves — making the grammar not just a reference but a traceable design decision.

***

### Derivation Step 2 — The Knowledge Structures

**Principles driving this:** P7, P14, P17

Before defining any agent, you need to know how knowledge flows through the system, because:

- P7 says context must be minimum and sufficient → you need a *mechanism* for generating context (the knowledge base and context card architecture), not just a template
- P14 says the framework learns through structured retrospectives, not longer specs → the Pattern Library schema needs to exist before any pattern is recorded in it
- P17 says trust is progressive → the NV scoring system needs a place to store the evidence that moves a pattern from NV=2 to NV=0

**What we have:** Context Curation Policy ✅, Pattern Library concept ✅ — but the Pattern Library schema is not yet defined. We know what it stores conceptually; we haven't defined its fields. This is a gap that will block Zone 0 work because the FOA's first action is `search_knowledge_base`, and that tool needs a schema to query.

**What would change:** The context card template and Pattern Library schema would be designed together as a pair in this step, before any agent specs are written. Right now they exist as separate concerns.

***

### Derivation Step 3 — The Agent Design Standard

**Principles driving this:** P7, P8, P9, P15, P16

With grammar, schema, and knowledge structures in place, you can define what an agent *is*:

- P15 (one agent, one artefact) → the Base Agent Template's single `WRITES:` field is not arbitrary; it is a structural enforcement of this principle
- P8 (separate definition/execution/verification) → the three TYPE classes (ORCHESTRATOR, EXECUTOR, COMPRESSION) map to these roles; REVIEWER field is a structural enforcement
- P9 (fail loudly) → `raise_uncertainty` is a universal tool by principle, not by convention; the Base Agent Template must require it
- P7 (minimum context) → `get_context_card` is the mandatory first call, not a recommended practice
- P16 (observer never controls) → agent templates must declare what they observe separately from what they control — this maps to the READS/NEVER distinction

**What we have:** Base Agent Template v0.2 ✅ — but it doesn't yet reference which principles each required field implements. The `REVIEWER:` field exists but isn't explicitly traced to P8.

**What would change:** Every required field in the Base Agent Template would have a principle reference. An agent spec reviewer checking a template would be checking *principle compliance*, not just format compliance.

***

### Derivation Step 4 — The Work Lifecycle

**Principles driving this:** P6, P8, P10, P11

With agents defined, you can define how work flows:

- P6 (evidence not assertion) → the proof template / QA review structure; literal output required
- P8 (separate definition/execution/verification) → the three-role pattern is a lifecycle requirement, not an agent design preference
- P10 (irreversible decisions need human authority) → human gates are placed at state transitions that cannot be undone
- P11 (proportional oversight) → QA tier assignment is not about strictness; it is about calibrating oversight to blast radius and novelty

**What we have:** Context Curation Policy ✅, Zone policies ✅, QA tier system in Agent Creation Policy ✅ — but these were derived independently rather than from explicit principle lineage.

**What would change:** The zone policies would explicitly map their human gates to P10 and their QA tiers to P11. A designer proposing a new zone gate would have to justify it against P10 — is this genuinely irreversible? — rather than just adding gates for safety.

***

### Derivation Step 5 — The Governance Policies

**Principles driving this:** All of the above, plus P13 and P17

With the lifecycle defined, you can write policies for how the framework governs itself:

- Agent Creation Policy (Zone 0) → implements P8 (no self-review), P11 (proportional oversight), P17 (progressive trust via NV scoring)
- Context Curation Policy → implements P7, P8 (curator ≠ reviewer)
- Uncertainty Protocol → implements P9

**What we have:** All three ✅ — these are in good shape. The Agent Creation Policy v0.2 is the most mature.

**What would change:** Each policy would open with a **Principles Declaration** — listing which principles it implements and which it would violate if removed. This creates the traceability the principles document needs to have teeth.

***

### Derivation Step 6 — Infrastructure Build

**Principles driving this:** P13

Only now do you build:

- P13 says prove before building — each infrastructure phase needs a falsifiable hypothesis, stated acceptance criteria, and literal evidence

**What we have:** Nexus Exp-01 ✅ — this was done correctly. Exp-01 was hypothesis-driven. The gap is that Exp-01 predated the principles, so the hypotheses weren't explicitly traced to principles. H1–H5 all implement P3, P4, or P5.

**What would change:** Experiment hypothesis cards would reference the principles being tested. H5 (chain of custody) was implicitly testing P5, but never stated that way. Naming it would have caught the `read_` audit gap before the test, not during it.

***

## The Compliance Audit: What We Have vs. What the Principles Require

| Principle | Has Implementation? | Gap |
| :-- | :-- | :-- |
| P1 — Coordination Cost | ✅ Nexus model, framework purpose | None |
| P2 — Asymmetric Cost | ✅ QA tiers, proof templates | Not stated as justification anywhere explicitly |
| P3 — Structure Over Instruction | ✅ OCAP, Tool Grammar | `NEVER` lists still exist alongside OCAP — P3 says tool absence supersedes them; docs don't make this explicit |
| P4 — Consequences Inside Tools | ✅ Compound tools, Grammar Rule 6 | None |
| P5 — Every Action Recorded | ⚠️ Partial | `read_` and `search_` audit gap — being fixed, but the gap existed because P5 wasn't upstream |
| P6 — Evidence Not Assertion | ✅ Proof templates, literal output | None |
| P7 — Minimum Sufficient Context | ✅ Context Curation Policy | Context card template fields not yet locked; Pattern Library schema not yet defined |
| P8 — Separate Definition/Execution/Verification | ✅ Three-role pattern, Agent Pair | Not explicitly referenced in Agent Creation Policy as the basis for the Agent Pair invariant |
| P9 — Fail Loudly | ✅ `raise_uncertainty`, pre-flight | Pre-flight split across 3 tools; not yet explicit that bypassing it is a P9 violation |
| P10 — Irreversible = Human Authority | ✅ FO gates | FO visibility layer not yet designed (raised today) — humans can't exercise authority they can't observe |
| P11 — Proportional Oversight | ✅ NV/BR scoring | None |
| P12 — Conventions Are Load-Bearing | ✅ Tool Grammar | Not stated as a principle anywhere; treated as style guidance in some contexts |
| P13 — Prove Before Building | ✅ Experiment methodology | Hypothesis cards don't reference which principles are being tested |
| P14 — Framework Learns | ✅ Pattern Library concept | Pattern Library schema not yet defined; no formal retrospective-to-entry process |
| P15 — One Agent, One Artefact | ✅ Single WRITES field | Never stated as a principle — currently just a template rule with no stated rationale |
| P16 — Observer Never Controls | ✅ Webhook architecture | Not stated as a principle — the decision exists but only as a rationale in NexusDecisionsRationale.md |
| P17 — Trust Is Progressive | ✅ NV scoring | Pattern Library has no mechanism yet to record evidence that reduces NV over time |


***

## The Next Steps From Here

Given the audit above, here is the ordered work — treating the principles document as the upstream source:

**1. Finalise and store the principles document** as the first entry in the framework manifest. Version it (v1.0). It is the only document in the framework that has no principle parent — it *is* the parent.

**2. Update the Tool Grammar to v0.2** — fix the `read_` and `search_` audit entries, update Rule 5, and add principle references to each verb definition. This is the most urgent fix because it affects the Nexus server implementation.

**3. Define the Pattern Library schema** — this is currently the largest structural gap. The FOA cannot begin Zone 0 work until `search_knowledge_base` has something to query. Even an empty but correctly structured Pattern Library is better than none. Fields needed: `entry_id`, `pattern_name`, `nv_score_at_first_run`, `current_nv_score`, `evidence_sessions[]`, `agent_classes_affected[]`, `zone`, `tags`, `summary`, `full_content_path`.

**4. Lock the context card template** — the format needs to be formally defined so `get_context_card` has a schema to return. This unblocks the FOA's context card (the last item on the Zone 0 readiness checklist).

**5. Add Principles Declarations to each existing policy** — a one-page preamble to each policy document listing which principles it implements. This is low effort but high value: it makes the corpus traceable and makes violations nameable.

**6. Revisit the bootstrapping checklist** through P13 — the checklist is currently a list of things that must exist. Under P13, each item on the checklist needs an acceptance criterion, not just a checkbox. "Pattern Library schema defined" needs a test: what does a passing schema look like? This turns the readiness checklist into a proof template for the bootstrapping phase itself.

**7. Design the FO observation layer** — P10 says irreversible decisions require human authority, but authority requires visibility. The FO currently has no designed mechanism to observe stream events outside of an agent interface. This is the gap raised earlier today. It is a P10 gap, not just an architecture gap — and naming it as a P10 gap makes its priority clear.

The first three are blockers for bootstrapping. The last four are needed before the first real project can run cleanly against the principles.

---

# show me how I should set up the directory structure for the framework manifest

Based on everything established today — the principles, derivation order, and what needs to exist before the FOA can work — here is the full recommended structure.

***

## The Full Directory Layout

```
.                                           # workspace root
│
├── nexus/                                  # MCP server implementation
│   ├── server.ts
│   ├── webhook.ts
│   ├── webhook-parser.ts
│   ├── db.ts
│   └── schema.sql
│
├── .vscode/
│   └── mcp.json                            # MCP server registrations
│
├── .github/
│   ├── copilot-instructions.md             # always-on workspace rules
│   ├── agents/                             # active per-task agent specs (generated)
│   │   └── task-performer-task-07.agent.md # example generated instance
│   ├── skills/                             # loadable skill files
│   │   ├── nexus-tool-grammar.skill.md
│   │   ├── nexus-ontology.skill.md
│   │   ├── uncertainty-protocol.skill.md
│   │   ├── preflight-check.skill.md
│   │   └── context-compression.skill.md
│   └── instructions/                       # VS Code instruction files
│       └── agent-design.instructions.md
│
└── .framework/                             # everything below this line
    │                                       # is what we are designing now
    ├── manifest.md                         # ← THE framework manifest
    │
    ├── principles.md                       # ← P1–P17 guiding principles
    │
    ├── policies/                           # governance documents
    │   ├── tool-grammar.md                 # verb vocabulary, subject vocab, matrix
    │   ├── agent-creation-policy.md        # Zone 0 policy
    │   ├── context-curation-policy.md      # cross-cutting curation invariants
    │   ├── preflight-uncertainty-protocol.md
    │   └── agent-pair-registry.md          # all registered Agent Pairs
    │
    ├── schema/                             # ← the gap identified today
    │   ├── pattern-library-schema.md       # field definitions for pattern entries
    │   ├── context-card-schema.md          # required fields for every context card
    │   ├── audit-log-schema.md             # canonical audit_log row definition
    │   └── observable-stream-schema.md     # stream_events row definition
    │
    ├── templates/                          # blank forms — never filled in here
    │   ├── base-agent-template.md          # minimum valid agent spec structure
    │   ├── agent-class-requirements.md     # blank FOA requirements form
    │   ├── spec-tests-template.md          # blank Agent Spec QA test form
    │   ├── context-card-template.md        # blank context card form
    │   ├── pattern-library-entry.md        # blank Pattern Library entry form
    │   └── hypothesis-card-template.md     # blank experiment hypothesis form
    │
    ├── agent-classes/                      # approved agent class templates
    │   │                                   # (produced by Zone 0 cycles)
    │   ├── zone-0/
    │   │   ├── foa.agent.md
    │   │   ├── agent-spec-qa.agent.md
    │   │   └── agent-template-creator.agent.md
    │   ├── zone-3/
    │   │   ├── context-agent.agent.md
    │   │   └── qa-definition.agent.md
    │   ├── zone-4/
    │   │   ├── task-performer.agent.md     # base template (hydrated at activation)
    │   │   └── qa-execution.agent.md
    │   └── cross-cutting/
    │       └── uncertainty-owner.agent.md  # one per zone at instantiation
    │
    ├── context-tree.md                     # CONTEXT_TREE_REF target for all agents
    │
    ├── patterns/                           # Pattern Library entries
    │   │                                   # one file per registered pattern
    │   └── .index.md                       # machine-readable index for search_knowledge_base
    │
    ├── context-cards/                      # generated context cards
    │   │                                   # one per agent class (+ task variants)
    │   ├── foa.context-card.md
    │   ├── agent-spec-qa.context-card.md
    │   └── agent-template-creator.context-card.md
    │
    ├── bootstrap/                          # Zone 0 readiness artefacts
    │   ├── zone-0-readiness-checklist.md   # the proof template for bootstrapping
    │   └── decisions/                      # named FO decisions (immutable)
    │       └── 001-bootstrapping-exception.md
    │
    ├── experiments/                        # experiment records
    │   ├── exp-01/
    │   │   ├── hypothesis-cards.md
    │   │   ├── probe-results.md
    │   │   └── retrospective.md
    │   └── exp-02/
    │       └── hypothesis-cards.md
    │
    └── features/                           # active project work (runtime)
        └── <feature-slug>/
            ├── feature-spec.md
            ├── feature-ac.md
            └── tasks/
                └── <task-id>/
                    ├── task-spec.md
                    ├── task-ac.md
                    ├── context-package.md
                    ├── proof-of-completion.md
                    ├── qa-review.md
                    ├── work-log.md
                    └── uncertainty-log.md
```


***

## What `manifest.md` Contains

This is the document the FOA reads first. It is a register, not a policy — it points to everything else and records decisions that have no other home.

```markdown
# Nexus Framework Manifest

**Version:** 0.1
**Status:** Active
**Principles Document:** .framework/principles.md (v1.0)
**Last Updated:** 2026-03-03

---

## Purpose

This manifest is the entry point for the Nexus framework. It records:
1. Named decisions that govern the framework as a whole
2. The canonical location of every governance document
3. The bootstrapping exception and its rationale
4. The version history of the framework itself

It does not contain policy. Policy lives in .framework/policies/.
It does not contain templates. Templates live in .framework/templates/.
It does not contain patterns. Patterns live in .framework/patterns/.

---

## Document Registry

| Document | Path | Version | Status |
|---|---|---|---|
| Guiding Principles | .framework/principles.md | 1.0 | Active |
| Tool Grammar | .framework/policies/tool-grammar.md | 0.2 | Active |
| Agent Creation Policy | .framework/policies/agent-creation-policy.md | 0.2 | Active |
| Context Curation Policy | .framework/policies/context-curation-policy.md | 0.1 | Active |
| Pre-flight & Uncertainty Protocol | .framework/policies/preflight-uncertainty-protocol.md | 0.1 | Active |
| Agent Pair Registry | .framework/policies/agent-pair-registry.md | 0.1 | Active |
| Base Agent Template | .framework/templates/base-agent-template.md | 0.2 | Active |
| Context Tree | .framework/context-tree.md | 0.1 | Active |

---

## Named Decisions

Named decisions are FO-level choices that govern the framework permanently.
They are recorded here because they have no natural home in any policy document.
They are immutable — to change them, a new decision supersedes the old one.

| ID | Decision | Date | Rationale |
|---|---|---|---|
| D-001 | Bootstrapping Exception | 2026-03-03 | See below |
| D-002 | OCAP over ACL | 2026-03-03 | See .framework/bootstrap/decisions/002-ocap-over-acl.md |
| D-003 | GitHub webhooks over MCP fork | 2026-03-03 | See .framework/bootstrap/decisions/003-webhooks.md |
| D-004 | read_ and search_ produce audit entries | 2026-03-03 | P5 compliance — every action recorded |

---

## Bootstrapping Exception (D-001)

The FOA and Agent Spec QA were created manually by FO on 2026-03-03
during initial framework setup. They could not be created by the Zone 0
process because Zone 0 did not yet exist.

This exception satisfies the Agent Pair invariant: FOA and Agent Spec QA
are a de-facto pair. FOA produces requirements and commissions; Agent Spec QA
tests and reviews. They were designed together, deployed together, and neither
is activatable in isolation.

This is the founding Agent Pair. All subsequent agents go through Zone 0.

Implementing principles: P8, P13, P17

---

## Framework Version History

| Version | Date | Summary |
|---|---|---|
| 0.1 | 2026-03-03 | Initial manifest. Principles v1.0 established. |
|     |            | Tool Grammar v0.2 (P5 audit fix for read_ and search_). |
|     |            | Agent Creation Policy v0.2 (Agent Pair invariant). |
|     |            | Bootstrapping exception recorded as D-001. |
```


***

## Three Rules for This Structure

**Rule 1 — `.framework/` is read-only for agents without explicit write authority.**
The only agents with write tools scoped to `.framework/` paths are Zone 0 agents. A Task Performer in Zone 4 has no tool that can touch `.framework/policies/`. This is P3 structurally enforced.

**Rule 2 — `features/` is the only directory that grows during project work.**
Everything above `features/` is framework governance and changes only via Zone 0 cycles or named FO decisions. A designer finding themselves adding files to `policies/` or `templates/` outside of a Zone 0 cycle is violating the process.

**Rule 3 — Every file in `agent-classes/` must have a corresponding entry in `patterns/`.**
An approved agent class with no Pattern Library entry has no NV history. The first run of that class cannot be scored at NV=0 without it. The `.index.md` in `patterns/` is the machine-readable index `search_knowledge_base` queries — it must be updated every time a new pattern entry is added.

---

# I've added the principles and manifest to the directory structure

I think the next important step is to document the limitations of the tools and why we have taken the path we have. It's because with current functionality, we can't restrict which files an agent can edit. They can have access to the edit tool or not, but we can't scope or control their access. This is why we are using the mcp server - so we can avoid giving edit access to any agents except the agents that write tests or code. All other agents must read and write through the mcp server tools.
I think the skills and instructions might need to be in the file structure, but feature and skill documentation will all be via mcp tools

This is the most important honesty document the framework needs. Here is a full draft of it, followed by how it changes the directory structure.

***

## The Document: `.framework/policies/platform-constraints.md`

```markdown
# Platform Constraints and Architectural Responses

**Version:** 0.1
**Status:** Active
**Principles implemented:** P3, P4, P5, P12, P16
**Last Updated:** 2026-03-03

---

## Purpose

This document records the real constraints of the platform the framework
runs on — VS Code Agent Mode with MCP — and documents the architectural
decisions made in direct response to those constraints.

This document is not aspirational. It describes what the platform actually
does, what it cannot do, and why those gaps shaped every design decision in
the framework. Any designer adding a new tool, policy, or agent class must
read this document first. Decisions made without understanding the platform
constraints will silently violate them.

---

## Part 1: What VS Code Agent Mode Can and Cannot Do

### The Edit Tool Is Binary

VS Code Agent Mode provides agents with a built-in `edit` tool that allows
an agent to create and modify files anywhere in the workspace. This tool
has exactly two states: **granted** or **not granted**. There is no
mechanism to scope it — you cannot say "this agent may edit files in
`/src/` but not in `/.framework/`."

**Consequence:** Any agent that holds the edit tool can modify any file in
the workspace, including governance documents, policies, agent templates,
and the framework manifest. This cannot be prevented at the VS Code layer.

**Architectural response:** The edit tool is granted to **exactly two agent
classes**, and only for the duration of work that requires direct filesystem
writes:

| Agent Class | Why edit is granted | Scope of legitimate use |
|---|---|---|
| Task Performer (code tasks) | Must write source code and test files | `/src/`, `/tests/`, task branch only |
| Agent Template Creator | Must write `.agent.md` files to `.github/agents/` | `.framework/agent-classes/` only |

All other agents — the FOA, Agent Spec QA, Context Agent, QA Definition,
QA Execution, Uncertainty Owner — **do not hold the edit tool**. Every
write they perform goes through a Nexus MCP tool. This is the only
mechanism available to enforce their write boundaries.

> **This is the foundational reason the Nexus MCP server exists.**
> Without MCP-mediated writes, there is no way to enforce write authority
> boundaries between agents. The MCP server is not a convenience layer —
> it is the access control boundary.

---

### Built-in Read Tools Are Also Unscoped

VS Code Agent Mode provides built-in tools for reading files, listing
directories, and searching the workspace. These tools are also not
scopeable. An agent without the edit tool can still, in principle, read
any file in the workspace using these built-in tools.

**Consequence:** The `READS:` list in an agent template is a declaration
of intent and a context-loading instruction — it is not a structural
enforcement of read access at the VS Code layer.

**Architectural response:** This is a known and accepted limitation. The
framework's response is layered:

1. **MCP `read_` tools** — for governed documents (task specs, proofs,
   context cards), agents are given MCP `read_` tools that return only
   the specific document they are designed for. An agent with only
   `read_task_spec_task_07` cannot call `read_proof_template_task_08`
   because that tool does not exist in its registry.

2. **Context cards** — agents receive context cards that declare their
   READS list. The card is what the agent uses to know what it should
   read. Agents operating in good faith do not read outside their
   declared scope.

3. **Audit coverage** — every MCP `read_` call produces an audit entry.
   Direct filesystem reads via VS Code built-ins do not. This asymmetry
   means that undeclared reads are invisible to the audit log. This is an
   accepted gap for the current platform.

**The honest position:** Read access is enforced at the MCP tool layer for
governed documents. It is not enforced at the filesystem layer. An agent
instructed to stay within its READS list will do so; an agent that
circumvents this is operating outside the framework's trust model and will
produce an audit trail that cannot account for its information sources.
Detecting this requires observing that an agent's output references content
that was not in any of its declared READS or MCP tool calls.

---

### Agent Identity Does Not Exist at Runtime

The VS Code MCP stack has no mechanism for an agent to prove its identity
to the MCP server. The MCP spec explicitly prohibits using session IDs for
authorisation. OAuth tokens identify VS Code (the host), not the agent
running inside it. STDIO transport has no authentication layer.

**Consequence:** The Nexus MCP server cannot verify that the agent calling
`submit_proof_task_07` is actually a Task Performer, and not a different
agent that happens to have been given that tool by mistake.

**Architectural response:** This is the discovery from Experiment 01 that
reframed the problem entirely [file:3]. The correct response is not to add
identity infrastructure — it is to recognise that **tool possession is
stronger than identity**. If only the Task Performer agent spec includes
`submit_proof_task_07`, then only an agent instantiated from that spec can
call it. The boundary is in the tool registry, not in a runtime identity
check. OCAP turns the absence of identity into a structural guarantee.

**What this means in practice:** The trust model is:
- The agent spec is the identity document
- The tool list in the spec is the capability grant
- VS Code enforces the tool list at the client layer before any MCP call
- The audit log records the tool name — which encodes role, scope, and
  task — providing chain of custody without identity tokens

---

### VS Code Reloads Agent Specs and Tools Live

When a `.agent.md` file is created or modified in `.github/agents/`, VS
Code detects the filesystem change and makes the agent available in the
`@` selector without restarting. When `tools/list_changed` is sent by the
MCP server, VS Code refreshes its tool registry live.

**Consequence (positive):** Per-task agent instantiation works cleanly.
`activate_task` generates an agent spec, writes it to `.github/agents/`,
registers task-scoped tools, sends `tools/list_changed` — and the agent
appears fully-formed in VS Code within seconds.

**Consequence (risk):** Any process that can write to `.github/agents/`
can inject an agent spec into VS Code. This is the write access concern
from the edit tool section above — an agent with the edit tool could in
principle write its own agent spec with elevated tools.

**Architectural response:** The edit tool is only granted to agents that
have a legitimate reason to write to `.github/agents/` (the Agent Template
Creator). All other agents cannot write to that directory because they
lack both the edit tool and any Nexus MCP tool scoped to that path.

---

## Part 2: The Two-Layer Architecture

Given these constraints, the framework operates across two distinct layers.
Understanding the boundary between them is essential for every design
decision.

```

┌─────────────────────────────────────────────────────────┐
│                   VS CODE LAYER                         │
│                                                         │
│  What lives here:                                       │
│  .github/agents/          ← agent spec files           │
│  .github/skills/          ← loadable skill files       │
│  .github/instructions/    ← VS Code instruction files  │
│  .github/copilot-instructions.md  ← always-on rules    │
│  .vscode/mcp.json         ← MCP server registrations   │
│                                                         │
│  WHY: VS Code reads these directly from the            │
│  filesystem. They cannot be served through MCP.        │
│  They are the configuration layer that tells VS Code   │
│  what agents exist and what servers to connect to.     │
│                                                         │
│  ACCESS CONTROL: None at the platform layer.           │
│  Governed by: who holds the edit tool.                 │
└─────────────────────────────────────────────────────────┘
│
│ MCP tools are the boundary
│
┌─────────────────────────────────────────────────────────┐
│                   NEXUS MCP LAYER                       │
│                                                         │
│  What lives here (all writes go through MCP tools):    │
│  .framework/              ← all governance artefacts   │
│  nexus.db                 ← all runtime state          │
│  task documents           ← specs, proofs, reviews     │
│  context cards            ← generated, versioned       │
│  audit log                ← immutable, append-only     │
│  observable stream        ← plain-English events       │
│                                                         │
│  WHY: MCP tools enforce the write authority model.     │
│  An agent without the right tool cannot write to       │
│  these artefacts regardless of what it is instructed   │
│  to do. The boundary is structural, not instructed.    │
│                                                         │
│  ACCESS CONTROL: Tool possession (OCAP).               │
│  Governed by: which tools appear in the agent spec.    │
└─────────────────────────────────────────────────────────┘

```

**The boundary rule:** If an artefact needs controlled write access between
agent classes, it must live in the Nexus MCP layer and be written only
through MCP tools. If an artefact needs to be loaded by VS Code directly
(agent specs, skills, instructions), it lives in the VS Code layer.

**Nothing crosses both.** A file cannot be both a VS Code-loaded resource
and a Nexus-controlled artefact. If you find yourself wanting to write a
skill file through an MCP tool and have VS Code load it, you need two
artefacts: the MCP-controlled source (the canonical version) and a VS Code
layer copy generated from it. The generation step requires an agent with
the edit tool and produces an audit entry.

---

## Part 3: What This Means for Skills and Instructions

Skills (`.github/skills/*.skill.md`) and instructions
(`.github/instructions/*.instructions.md`) live in the VS Code layer.
They must be on the filesystem because VS Code loads them at agent
instantiation time. They cannot be served through MCP.

**Consequence for governance:** Skills and instructions are not governed
artefacts in the Nexus sense — they do not have write authority controlled
by MCP tools, they do not have audit entries for reads, and they are not
versioned through the documents table. They are filesystem resources.

**The correct mental model:**

| Artefact type | Layer | Written by | Audit coverage |
|---|---|---|---|
| Skill files (`.skill.md`) | VS Code | Agent Template Creator (edit tool) or FO manually | GitHub commit history only |
| Instruction files | VS Code | FO manually | GitHub commit history only |
| Agent spec templates | VS Code | Agent Template Creator (edit tool) — via Zone 0 | GitHub commit history + AgentClassCreated stream event |
| Context cards | Nexus MCP | Context Agent (MCP write tool) | Full — every get_context_card call audited |
| Task documents | Nexus MCP | Role-specific agents (MCP tools) | Full — every read and write audited |
| Framework policies | Nexus MCP | FOA (MCP write tool) — via Zone 0 | Full — every read and write audited |

**What this means for skill documentation:** A skill file's content is on
the filesystem and governed only by Git. Its *existence* — that it was
commissioned, reviewed, and approved — is governed by the Zone 0 process
and recorded in the Pattern Library and Observable Stream. The skill file
itself is the VS Code artefact; the Zone 0 audit trail is the governance
record. These are complementary, not redundant.

---

## Part 4: The Residual Gaps

This section names the gaps honestly. They are accepted limitations of the
current platform, not framework defects.

**Gap 1 — Unscoped filesystem reads**
Agents with VS Code built-in tools can read any file. MCP `read_` tools
scope governed reads, but built-in reads are unaudited and unscoped. Agents
operating in good faith stay within their declared READS list. Detection of
out-of-scope reads requires inference from outputs rather than direct
observation.

*Accepted:* Yes, at current scale. *Revisit when:* Agent autonomy increases
to the point where inferred-from-output detection is insufficient.

**Gap 2 — Skill and instruction files are not Nexus-governed**
VS Code layer files have no MCP audit coverage. Their change history is Git
only. Malicious or accidental modification of a skill file used by many
agents could affect all agents loading that skill, with no Nexus audit
entry.

*Accepted:* Yes. *Mitigated by:* Zone 0 process governs the creation and
approval of skill files. All skill file changes go through the Agent
Template Creator (edit tool holder) and produce a Zone 0 audit event even
if the file-level write is unaudited. *Revisit when:* Skills become
sufficiently complex that file-level audit is warranted.

**Gap 3 — Agent spec files are filesystem-writable by edit tool holders**
The Agent Template Creator holds the edit tool and writes to
`.github/agents/`. A malfunctioning or compromised Agent Template Creator
could write arbitrary agent specs. There is no MCP-layer gate on writes to
`.github/agents/`.

*Accepted:* Yes. *Mitigated by:* Zone 0 process requires Agent Spec QA
review of every template before it is activated. The Agent Template Creator
cannot activate its own template — activation requires an FOA call to
`activate_task`, which is an MCP-governed action. *Revisit when:* The
activation model becomes more automated.

**Gap 4 — FO has no governed observation layer**
The FO cannot currently observe stream events or the audit log through a
Nexus-governed interface. Observation requires direct database access. This
means FO decisions — which require observation per P10 — are made without
a complete audited view.

*Accepted:* Yes, temporarily. *Status:* Named as P10 gap. Designing the FO
observation layer is a priority item before the first real project runs.

---

## Part 5: Named Decision Record

These decisions are recorded in the manifest as D-005 through D-008.

**D-005 — MCP-first for all non-code writes**
All writes to governed artefacts go through Nexus MCP tools. The edit tool
is granted only to agents that must write code or agent spec files to the
filesystem. This is the only mechanism available to enforce write authority
boundaries on the current platform.
*Principle:* P3 — Structure Over Instruction.

**D-006 — Skills and instructions live in the VS Code layer**
Skill and instruction files must be readable by VS Code at agent load time.
They cannot be mediated through MCP. Their change governance is Zone 0
process + Git history, not Nexus audit entries.
*Principle:* P12 — Conventions Are Load-Bearing.

**D-007 — Built-in VS Code read tools are an accepted gap**
Unscoped filesystem reads via VS Code built-in tools are an accepted
platform limitation. MCP `read_` tools govern audited reads of governed
documents. Good-faith agents operate within their declared READS list.
*Principle:* P5 partial compliance — accepted gap, named explicitly.

**D-008 — Agent identity is expressed through tool possession, not tokens**
Runtime agent identity does not exist on this platform. The agent spec is
the identity document. The tool list in the spec is the capability grant.
OCAP tool possession is structurally stronger than any identity check that
could be added.
*Principle:* P3 — Structure Over Instruction.
```


***

## How This Changes the Directory Structure

The two-layer model requires one clarification to the directory layout — splitting what was loosely called `.github/` into an explicit picture of what belongs where:

```
.github/
├── copilot-instructions.md   ← always-on workspace rules (VS Code layer)
├── agents/                   ← ACTIVE generated instances only (VS Code layer)
│   └── task-performer-task-07.agent.md   ← generated, ephemeral
└── skills/                   ← VS Code layer — loaded at agent instantiation
    └── nexus-tool-grammar.skill.md

.framework/
├── agent-classes/            ← CANONICAL approved templates (Nexus MCP layer)
│   ├── zone-0/               ← written through MCP by Agent Template Creator
│   └── ...                   ← these are the source of truth; .github/agents/
│                                instances are generated FROM these
```

The key distinction that was implicit before but must now be explicit:[^10_1][^10_2]

- `.github/agents/` — **ephemeral, generated instances**. What VS Code loads right now. Created by `activate_task`, deleted by `deactivate_task`.
- `.framework/agent-classes/` — **canonical approved templates**. The source of truth. Written through MCP tools via Zone 0. Never modified directly.

An agent spec in `.github/agents/` is always derived from a template in `.framework/agent-classes/`. The canonical version lives in the Nexus layer; the VS Code layer holds the live instance. This means the edit tool holder (Agent Template Creator) writes to `.framework/agent-classes/` — and `activate_task` generates the `.github/agents/` instance from it automatically, without any agent needing the edit tool at activation time.[^10_3][^10_2]

<div align="center">⁂</div>

[^10_1]: NexusDecisionsRationale.md

[^10_2]: NexusModelOverview.md

[^10_3]: Nexus-exp01-retro.md


---

# this is great.

let's now revisit the grammar so that it adheres to the principles and policies

Good. Here is the full revised grammar — v0.3 — with every change traced to the principle that requires it, and the version history updated to show the complete evolution.

***

## `.framework/policies/tool-grammar.md` — v0.3

```markdown
# Nexus Tool Grammar — Reference Specification

**Version:** 0.3
**Status:** Active
**Principles implemented:** P3, P4, P5, P12, P16
**Platform constraint reference:** .framework/policies/platform-constraints.md
**Last Updated:** 2026-03-03

---

## Version History

| Version | Date | Change | Principle |
|---|---|---|---|
| 0.1 | 2026-03-01 | Initial grammar. All verbs defined. Tool Matrix established. | P3, P4, P12 |
| 0.2 | 2026-03-02 | `get_` promoted to audit-writing verb. Rationale: system state reads must be traceable. Discovered via H5 chain-of-custody test. | P5 partial |
| 0.3 | 2026-03-03 | `read_` and `search_` promoted to audit-writing verbs. Rationale: P5 requires every action by every agent to be recorded — including reads. The v0.2 distinction between "mutable system state" (audited) and "versioned documents" (not audited) is insufficient. A document version number records what the document contained; it does not record who read it, when, or what they did with it. Rule 5 updated accordingly. Named Decision D-004. | P5 |

---

## Purpose

This grammar defines the naming, structure, and behavioural contract for
every tool in the Nexus MCP server. It exists to prevent the tool catalogue
from becoming an unmaintainable list of ad hoc names as the framework grows.
Any developer or agent adding a new tool must derive it from this grammar —
not invent independently.

The grammar enforces one principle above all others: **tool possession is
capability** (P3). The name of a tool must be sufficient to determine what
it does, who should have it, and what scope it acts on — without consulting
any other document.

### Why This Grammar Is Load-Bearing, Not Stylistic (P12)

Naming conventions in this framework are structural elements. The
`{verb}_{subject}_{task_slug}` format is not cosmetic:

- It makes every audit log row self-describing without a schema join
- It makes the chain of custody reconstructable by a human with no
  prior knowledge of the database schema
- It makes tool capability derivable by inspection — no tool registry
  documentation needed
- It makes violations of the grammar visible immediately — a malformed
  name signals a design problem, not a naming preference

A single deviation from this grammar creates a gap in traceability that
may only surface during a failure diagnosis. Treat deviations as defects.

### Relationship to the Platform (P3, P16)

These tools exist in the Nexus MCP layer — the access-controlled layer of
the framework. They are the mechanism by which write authority is enforced
between agent classes, because the VS Code platform provides no other way
to scope filesystem write access.

See `.framework/policies/platform-constraints.md` for the full explanation
of why MCP tools are the access control boundary, and which agents hold the
VS Code edit tool instead.

---

## The Grammar

Every tool name is formed from two or three components:

```

{verb}_{subject}

or, for task-scoped tools:

{verb}_{subject}_{task_slug}

```

Where:
- `{verb}` is drawn from the closed Verb Vocabulary (8 entries, never
  extended without a framework-level decision)
- `{subject}` is drawn from the open Subject Vocabulary (document type
  taxonomy, extends as the framework grows)
- `{task_slug}` is the task identifier with hyphens replaced by
  underscores (`task-07` → `task_07`)

**No other components are permitted.** A tool name with an adjective, a
preposition, a conjunction, or any component not in these vocabularies is
malformed and must be redesigned.

---

## Verb Vocabulary

The verbs are a **closed set**. New verbs are never added without a
framework-level decision and update to this document. If a proposed tool
doesn't fit an existing verb, the answer is almost always that the tool is
crossing a concern boundary and should be split.

### Audit Obligation Summary

Every verb in the grammar produces an audit entry. This is a P5 invariant
— it is not optional and cannot be relaxed for individual tools.

| Verb | Audit entry? | State transition? | Stream event? |
|---|---|---|---|
| `read_` | ✅ | ❌ | ❌ |
| `write_` | ✅ | ❌ | ❌ |
| `append_` | ✅ | ❌ | ❌ |
| `submit_` | ✅ | ✅ | ✅ |
| `request_` | ✅ | ✅ (→ AWAITING only) | ✅ |
| `search_` | ✅ | ❌ | ❌ |
| `get_` | ✅ | ❌ | ❌ |
| `raise_` | ✅ | ✅ (→ BLOCKED) | ✅ (priority) |

---

### `read_`

**Semantics:** Fetch the current content of a document. Returns document
content only.

**Principles:** P5 (every action recorded), P3 (tool possession defines
access)

**Side effects:**
Writes one `audit_log` entry:
```

{
tool_name: 'read_{subject}_{task_slug}',
actor: string,
task_id: string,
doc_version_hash: string,   ← which version the agent received
timestamp: ISO string
}

```
No state change. No stream event.

**Why `doc_version_hash` is required:**
The version number records what the document contained. The audit entry
records who read it and when. These answer different questions. "The agent
read task_spec v3" tells you what information was available. "The agent
read task_spec v3 at 14:22 before submitting proof at 14:45" tells you what
information the agent was working from when it made a decision. Both are
necessary for a complete causal chain.

**Rules:**
- Must be idempotent — calling it twice returns identical content and
  produces two identical audit entries (the second is not an error)
- Must never mutate any database row other than `audit_log`
- Any agent may receive a `read_` tool for any document type relevant
  to its role — access is controlled by tool possession, not by a
  runtime permission check
- If a document does not exist, return a typed empty response — never
  an error that leaks schema details

**How `read_` differs from `get_`:**
Both now produce audit entries. The distinction is what they operate on:
- `read_` operates on task documents — typed, versioned content artefacts
  with a defined lifecycle. Returns document content.
- `get_` operates on system state resources — context cards, capability
  registries, lifecycle state. Returns structured metadata, not document
  content. See `get_` definition below.

**Examples:** `read_task_spec_task_07`, `read_proof_template_task_07`,
`read_qa_review_task_07`

**Counter-example:** `read_context_card` called by an agent loading its own
context ❌ — an agent loading its own context card calls `get_context_card`,
not `read_context_card`. `read_context_card` is reserved for roles that
inspect another agent's card as a governed document (e.g. the FOA auditing
what card a given agent class was issued). These are different operations
with different semantics.

---

### `write_`

**Semantics:** Create or fully replace a document. The previous version is
preserved in document history; the current pointer updates.

**Principles:** P4 (mandatory side effects inside tools), P5 (every action
recorded)

**Side effects:**
Writes one `audit_log` entry:
```

{
tool_name: 'write_{subject}_{task_slug}',
actor: string,
task_id: string,
doc_version_hash: string,   ← hash of the content written
reason: string,             ← mandatory field from the caller
timestamp: ISO string
}

```
No state transition. No stream event.

**Rules:**
- Requires a mandatory `reason` parameter — the Zod schema must enforce
  this; it cannot be optional or empty string
- If the document already exists, creates a new version (never destructive
  — the previous version remains in history)
- Must validate that the task is in a state that permits writes for this
  document type — reject with a typed error if not
- Never used for append-only documents (use `append_` instead)
- Never used when a state transition must follow (use `submit_` instead)

**Examples:** `write_task_spec_task_07`, `write_feature_spec`,
`write_proof_template_task_07`

**Counter-example:** `write_proof_task_07` ❌ — proof submission requires a
state transition; this must be `submit_proof_task_07`.

---

### `append_`

**Semantics:** Add an entry to an append-only document. The document is an
ordered log; prior entries are never modified.

**Principles:** P4, P5

**Side effects:**
Writes one `audit_log` entry:
```

{
tool_name: 'append_{subject}_{task_slug}',
actor: string,
task_id: string,
entry_hash: string,   ← hash of the appended entry only, not full doc
timestamp: ISO string
}

```
No state transition. No stream event.

**Rules:**
- Only applicable to subjects explicitly designated as Append-only in the
  Subject Vocabulary — applying `append_` to a Replace-mode subject is a
  grammar violation
- Must never accept a `replace` or `overwrite` parameter
- Timestamps are written by the server, not the caller — the caller cannot
  specify or override a timestamp
- The `entry_hash` in `audit_log` covers the appended entry only, so
  individual entries are independently traceable

**Applicable subjects:** `work_log`, `uncertainty` (log entries),
`decomposition` (task additions only)

**Examples:** `append_work_log_task_07`, `append_uncertainty_task_07`

**Counter-example:** `append_task_spec_task_07` ❌ — `task_spec` is a
Replace-mode document. This is a grammar violation.

---

### `submit_`

**Semantics:** Write a document AND trigger a state transition AND emit a
stream event. All three operations are atomic — all succeed or none do.

**Principles:** P4 (mandatory side effects inside tools), P5, P6 (evidence
not assertion — the submitted document is the literal evidence)

**Side effects (all atomic):**
1. Writes the document with version history
2. Writes one `audit_log` entry
3. Transitions the entity state (specific transition hardcoded per tool)
4. Emits a `stream_events` entry in plain English
5. Triggers the Policy Engine to evaluate downstream policies

**Rules:**
- Exactly one state transition per `submit_` call — if two transitions
  are needed, it is two tools
- The stream event text is hardcoded in the tool implementation — the
  caller cannot supply or modify the stream message
- Must validate that the current state is the exact expected
  pre-transition state; reject with a typed error if not
- The `reason` parameter is mandatory, as per `write_`
- No `submit_` tool is given to an agent that is not the designated
  actor for that transition (P8 — separation of execution and
  verification)

**Examples:** `submit_proof_task_07`, `submit_qa_review_task_07`,
`submit_ac`

**Counter-example:** `submit_context_card` ❌ — context cards are generated
by the system, not submitted by agents.

---

### `request_`

**Semantics:** Signal intent or request action from another actor. Writes
no documents. Does not advance state to an active working state
unilaterally.

**Principles:** P4, P5, P9 (fail loudly — `request_` is how an agent
signals it needs something before it can proceed, without guessing)

**Side effects:**
Writes one `audit_log` entry. Emits a `stream_events` entry identifying
the target actor. May transition state to an `AWAITING_*` state — but
never to an active working state.

**Rules:**
- Never writes a document
- The requested action must be taken by a different actor — `request_`
  is never self-fulfilling
- The stream event must identify who the request is directed at (FO, QA
  Agent, Feature Owner Agent)
- Used when an agent needs a cross-role action before it can continue

**Examples:** `request_review`, `request_clarification`,
`request_ac_approval`

**Counter-example:** `request_write_task_spec` ❌ — verbs do not nest.

---

### `search_`

**Semantics:** Query the Pattern Library or knowledge base. Returns
matching entries ranked by relevance.

**Principles:** P5 (every action recorded — what an agent searched for
and what it found is causally significant), P7 (minimum sufficient context
— agents search for relevant patterns rather than receiving all patterns)

**Side effects:**
Writes one `audit_log` entry:
```

{
tool_name: 'search_knowledge_base',
actor: string,
query: string,              ← the exact query submitted
tags: string[],             ← filters applied, if any
result_count: number,       ← total matched
top_entry_ids: string[],    ← first 5 entry IDs returned
timestamp: ISO string
}

```
No state change. No stream event.

**Why query and results are recorded:**
An audit entry with only a timestamp answers "did the agent search?"
Recording the query and top results answers "what did the agent look for,
and what did it find?" The second question is the one that matters for
diagnosing whether an agent had access to relevant patterns before making
a decision. If an agent produced a poor output on a task type that has a
known Pattern Library entry, the audit log will show whether it searched
for that pattern or not.

**Rules:**
- Must accept a `query` parameter (free text)
- Must accept an optional `tags` parameter for category filtering
- Must never return content from the primary document store — only
  Pattern Library and knowledge base entries
- Results must include `source_session` so the caller knows when the
  pattern was recorded
- Returns summaries, not full content — an agent needing full content
  must have a `read_` tool for that pattern document

**Examples:** `search_knowledge_base`, `search_patterns`

**Counter-example:** `search_task_specs` ❌ — primary document search is
`read_` with a filter parameter, not `search_`. The `search_` verb is
reserved for the knowledge base only.

---

### `get_`

**Semantics:** Fetch system-level metadata, configuration, or pre-generated
artefacts. Distinct from `read_` in that it operates on system resources,
not task documents.

**Principles:** P5, P7 (context cards provide minimum sufficient context
to agents at instantiation)

**Side effects:**
Writes one `audit_log` entry:
```

{
tool_name: 'get_{subject}',
actor: string,
resource_version: string,   ← version/hash of what was returned
(e.g. context card version, state value)
timestamp: ISO string
}

```
No state change. No stream event.

**How `get_` differs from `read_` (v0.3 distinction):**

Both verbs now produce audit entries. The distinction is the nature of
what they access, not their audit behaviour:

| Dimension | `read_` | `get_` |
|---|---|---|
| Operates on | Task documents | System state resources |
| Returns | Document content | Structured metadata |
| Subject vocabulary | Document types (task_spec, proof, etc.) | System resources (context_card, capabilities, current_state) |
| Version model | Document version history | Resource regenerated externally (e.g. context cards regenerated by Context Agent) |
| Audit records | `doc_version_hash` — which doc version | `resource_version` — which system state snapshot |

**Rules:**
- Never operates on a task document — that is `read_`
- Returns structured data, not raw document content
- The audit entry must capture the version or value of the resource
  returned — not just that it was fetched

**Examples:** `get_context_card`, `get_my_capabilities`,
`get_current_state`

**Counter-example:** `get_task_spec_task_07` ❌ — task specs are documents,
not system metadata. This must be `read_task_spec_task_07`.

---

### `raise_`

**Semantics:** Surface an exceptional condition immediately to human
attention. Bypasses normal workflow.

**Principles:** P9 (fail loudly, never silently), P10 (irreversible
states require human authority — BLOCKED state is entered here)

**Side effects:**
Writes one priority `audit_log` entry. Emits a priority `stream_events`
entry (visually distinct from standard events — FO sees this immediately).
If `severity == BLOCKED`: transitions entity state to `BLOCKED` or
`AWAITING_HUMAN`.

**Rules:**
- Reserved exclusively for the `uncertainty` subject — `raise_uncertainty`
  is the only valid `raise_` tool in the grammar
- Must never be used for normal workflow signalling — use `request_` for
  cross-agent coordination
- The description fields (`what`, `why`, `needed`) are free text — this
  is intentional; uncertainties are by definition unstructured
- Any agent may hold this tool — it is a safety valve, not a privilege
  (P9 applies in every zone, at every role level)
- A `raise_uncertainty` call with no `context_paths` is invalid — an
  uncertainty with no traceable context cannot be resolved

**Example:** `raise_uncertainty`

**Counter-example:** `raise_error` ❌ — tool errors are handled by the
tool's typed return value. `raise_` is exclusively for conditions requiring
human attention that cannot be resolved within the normal flow.

---

## Subject Vocabulary

Subjects are an **open set** — new document types are added as the
framework encounters them. Each entry defines the write mode, valid verbs,
and owning role.

| Subject | Write mode | Valid verbs | Owner role |
|---|---|---|---|
| `task_spec` | Replace | `read`, `write` | Task Owner |
| `proof_template` | Replace | `read`, `write` | QA Definition Agent |
| `proof` | Create-once | `read`, `submit` | Task Performer |
| `work_log` | Append-only | `read`, `append` | Task Performer |
| `feature_spec` | Replace | `read`, `write` | Feature Owner Agent |
| `ac` | Replace | `read`, `write`, `request` | Feature Owner Agent |
| `qa_review` | Create-once | `read`, `submit` | QA Execution Agent |
| `context_card` | Replace | `read`, `write`, `get` | Context Agent (`write`); any agent (`get`) |
| `environment_contract` | Replace | `read`, `write` | Task Owner |
| `uncertainty` | Append-only | `read`, `append`, `raise` | Any (cross-cutting) |
| `decomposition` | Append + Replace | `read`, `write`, `append` | Feature Owner Agent |
| `ui_brief` | Replace | `read`, `write` | UI Design Agent |
| `knowledge_base` | Append-only | `search`, `append` | Context Agent (`append`); any agent (`search`) |
| `patterns` | Replace | `read`, `write`, `search` | FOA (`write`); any agent (`read`, `search`) |
| `capabilities` | System | `get` | Nexus server (read-only) |
| `current_state` | System | `get` | Nexus server (read-only) |

**Note on `context_card`:**
The `context_card` subject has both `read_` and `get_` tools. These are
not duplicates:
- `get_context_card` — universal tool, called by an agent loading its
  own context at instantiation. This is the agent-facing tool.
- `read_context_card` — role-scoped tool, called by the FOA or Context
  Agent to inspect what card a given agent class was issued. This treats
  the context card as a governed document to be reviewed, not loaded.

**Rules for adding a new subject:**
1. It must represent a distinct document type not covered by any existing
   subject
2. It must have a designated owner role with exclusive `write_` authority
3. Its write mode must be declared before any tool is built
4. Adding a subject does not create tools — only matrix cells that make
   domain sense become tools

---

## The Tool Matrix

✓ = tool exists or will exist. Blank = combination is not domain-valid.

| | `read_` | `write_` | `append_` | `submit_` | `request_` | `search_` | `get_` | `raise_` |
|---|---|---|---|---|---|---|---|---|
| `task_spec` | ✓ | ✓ | | | | | | |
| `proof_template` | ✓ | ✓ | | | | | | |
| `proof` | ✓ | | | ✓ | | | | |
| `work_log` | ✓ | | ✓ | | | | | |
| `feature_spec` | ✓ | ✓ | | | | | | |
| `ac` | ✓ | ✓ | | | ✓ | | | |
| `qa_review` | ✓ | | | ✓ | | | | |
| `context_card` | ✓ | ✓ | | | | | ✓ | |
| `environment_contract` | ✓ | ✓ | | | | | | |
| `uncertainty` | ✓ | | ✓ | | | | | ✓ |
| `decomposition` | ✓ | ✓ | ✓ | | | | | |
| `ui_brief` | ✓ | ✓ | | | | | | |
| `knowledge_base` | | | ✓ | | | ✓ | | |
| `patterns` | ✓ | ✓ | | | | ✓ | | |
| `capabilities` | | | | | | | ✓ | |
| `current_state` | | | | | | | ✓ | |

---

## Scoping Rules

### Universal tools (no task suffix)
Available to every agent, always. No task suffix because they are not
scoped to any single task.

```

get_context_card          search_knowledge_base
get_my_capabilities       raise_uncertainty
get_current_state

```

### Role-scoped tools (no task suffix)
Available to an agent class across all tasks. The tool validates permitted
access against the calling agent's role from its context card.

```

read_feature_spec         write_feature_spec
read_ac                   write_ac
read_decomposition        write_decomposition
read_patterns             write_patterns
append_knowledge_base

```

### Task-scoped tools (with task suffix)
Dynamically generated per active task. The suffix is the task identifier
with hyphens replaced by underscores.

**Formation rule:**
```

task-07  →  _task_07    task-07a →  _task_07a

```

**Examples:**
```

read_task_spec_task_07
write_proof_template_task_07
append_work_log_task_07
submit_proof_task_07
read_environment_contract_task_07

```

**Why underscores:** Hyphens in tool names create parsing ambiguity when
extracting `task_id` by splitting on `_`. Underscores produce unambiguous
splits — the final segment after `_{subject}_` is always the task slug.

---

## Agent Spec Declaration Standard

Every agent spec declares tools in three groups corresponding to the three
scoping levels. The three-group structure is mandatory even if Group 2 is
empty.

```yaml
***
name: Task Performer (task-07)
description: Task Performer scoped exclusively to task-07
model: claude-sonnet-4-5
tools:
  # Group 1 — Universal (always present, every agent, no exceptions)
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - raise_uncertainty
  - search_knowledge_base

  # Group 2 — Role-scoped (this agent class, any task)
  # (none for Task Performer — reads are task-scoped only)

  # Group 3 — Task-scoped (this instance, this task only)
  - read_task_spec_task_07
  - read_environment_contract_task_07
  - write_proof_template_task_07
  - append_work_log_task_07
  - submit_proof_task_07
***
```


---

## Rules for Designing New Tools

Apply in order. Stop and redesign if any rule rejects.

**Rule 1 — One verb.**
Map the proposed operation to exactly one verb. If it maps to two verbs,
it is two tools. If it maps to zero verbs, escalate to a framework-level
decision — do not invent a verb unilaterally.

**Rule 2 — One subject.**
Each tool operates on exactly one subject. A tool that reads one document
type and writes another is two tools.

**Rule 3 — Matrix check.**
Verify the verb × subject cell is marked ✓ in the Tool Matrix. If it is
blank, the combination is not domain-valid. Do not fill blank cells to
satisfy edge cases without confirming at the domain model level.

**Rule 4 — Scope determination.**
Classify as universal, role-scoped, or task-scoped. Universal tools are
rare — only tools that genuinely serve every agent without any task
context. When in doubt, task-scope it.

**Rule 5 — Side effect audit.**
List every side effect. Then verify:

```
Side effects              → Correct verb
────────────────────────────────────────────────
Audit entry only          → read_, search_, or get_
Audit + doc write         → write_ or append_
Audit + doc + transition  → submit_
Audit + stream event only → request_ or raise_
```

If any side effect is absent from the implementation when the verb
requires it, this is a Rule 6 violation, not a Rule 5 violation.

**Rule 6 — Mandatory consequences inside the tool (P4).**
Every side effect listed for a verb must be implemented inside the tool,
not described to the agent as a follow-up instruction. If an agent spec
currently says "after calling X, also write to the audit log" — that is a
Rule 6 violation. The audit write belongs inside X.

This rule applies to audit entries specifically: as of v0.3, no tool in
the grammar has zero side effects. Any tool implementation that does not
write an audit entry is non-compliant regardless of verb.

---

## Well-Formed and Malformed Examples

```
✅  read_task_spec_task_07         verb=read,   subject=task_spec,      scope=task_07
✅  submit_proof_task_07           verb=submit, subject=proof,           scope=task_07
✅  append_work_log_task_07        verb=append, subject=work_log,        scope=task_07
✅  get_context_card               verb=get,    subject=context_card,    scope=universal
✅  raise_uncertainty              verb=raise,  subject=uncertainty,     scope=universal
✅  search_knowledge_base          verb=search, subject=knowledge_base,  scope=universal
✅  request_ac_approval            verb=request,subject=ac,              scope=role

❌  finalize_feature               'finalize' is not in the Verb Vocabulary
❌  write_and_submit_proof_task_07  two verbs — must be split
❌  get_task_spec_task_07          task_spec is a document, not metadata → read_
❌  submit_context_card            context cards are not submitted by agents
❌  append_task_spec_task_07       task_spec is Replace mode, not Append-only
❌  write_proof_task_07            proof is Create-once with state transition → submit_
❌  task_07_write_proof            wrong component order — verb must come first
```


---

## Versioning This Document

Changes to the grammar fall into three categories:

- **Adding a subject** (most common): add to Subject Vocabulary, add row
to Tool Matrix, update affected agent spec templates. Bump patch version.
- **Adding a tool to an existing subject** (occasional): fill a blank
matrix cell, implement the tool, confirm Rules 5 and 6. Bump patch
version.
- **Adding a verb or changing verb semantics** (rare — framework-level
decision required): update this document, the Tool Matrix, all agent
spec templates, and all `tools/list` logic in the Nexus server. Bump
minor version. Record as a Named Decision in the manifest.

```

***

## What Changed and Why

Three substantive changes from v0.1/v0.2, all traceable to the principles:[^11_1]

**Change 1 — `read_` now audits (P5, D-004)**
The v0.2 rationale was: *task documents are versioned, version number is the audit trail*. That rationale is insufficient — a version number records what the document contained; it does not record who read it or when. The audit entry answers the causal question: *"what information was this agent working from when it made this decision?"*

**Change 2 — `search_` now audits (P5, D-004)**
Recording query text and top result IDs answers whether an agent searched for a relevant pattern before making a decision — not just that a search happened. This is the diagnostic that makes P14 (framework learns from its own operations) actually testable.

**Change 3 — Rule 5 reworded**
The old rule said *"zero side effects → `read_`, `search_`, or `get_`"*. That is now false. The new rule reads *"audit entry only → `read_`, `search_`, or `get_`"*. This removes the internal contradiction and reflects the actual invariant: every verb in the grammar produces an audit entry, no exceptions.[^11_2][^11_3]


<div align="center">⁂</div>

[^11_1]: NexusToolGrammar.md
[^11_2]: ONE-Ontology.md
[^11_3]: Nexus-exp01-retro.md

---

# this reminds me. I know we are implementing the ontology into the grammar, but I see its uses outside this too. that all software developed should use the ontology as it is designed for ease of use by agents. but tell me if this is something we should look at later. If we should look at it later, let's keep moving on with the audit schema.

[https://one.ie/ontology/](https://one.ie/ontology/)
[https://one.ie/docs/overview/ontology/](https://one.ie/docs/overview/ontology/)

Defer it — but it deserves a clear explanation of why, and it should be recorded now so it doesn't get lost.

***

## Why Later

The ONE Ontology applied to **framework governance** is what we've been doing all day — the six dimensions (Capability, Accountability, Quality, Temporality, Context, Artifact) are already the lens for every design decision.[^12_1]

What you're identifying is a second, distinct application: using the ONE Ontology as the **data model standard for software built through the framework**. The website makes this very concrete — Groups, People, Things, Connections, Events, Knowledge as the six universal building blocks of any application schema . That's a different concern from framework governance, and it's important. But it's not a blocker for anything we need to do before the first real project runs.

The right moment to formalise this is when Zone 0 is functional and the first real feature is being scoped. At that point you'll have a concrete domain to map against the ontology, which will produce a much better policy than one written in the abstract now.

***

## What's Worth Noting Now

The two expressions of the ontology are not coincidental — they map directly onto each other:

| ONE Ontology (software) | Framework Ontology | Nexus Implementation |
|---|---|---|
| Events | Accountability | `audit_log` table |
| Knowledge | Context | Pattern Library + context cards |
| Things | Artifact | Typed document model |
| Connections | Capability | Tool possession graph |
| Groups | Temporality | Zone / task scoping |
| People | Quality | Human gates at irreversible decisions |

This alignment means that software built through the framework and the framework itself share a conceptual substrate. That's not accidental — it's the property that would make agents working on that software genuinely context-aware about what they're building .

***

## Record It, Then Move On

This should be added to the manifest as a **named future direction**, not a decision:

```markdown
## Future Directions

| ID | Direction | Trigger condition |
|---|---|---|
| F-001 | ONE Ontology as software design standard | When first real project is scoped through Zone 0 |
```

This keeps it visible and actionable without letting it block the audit schema, which IS a current blocker. Let's move to that now.

<div align="center">⁂</div>

[^12_1]: ONE-Ontology.md


---

# great. i added to manifest.

Let's look at the audit schema

Good. Now let me design this carefully from first principles, because the schema is the foundation everything else queries against. Here is the full document.

***

## `.framework/schema/audit-log-schema.md`

```markdown
# Audit Log Schema

**Version:** 0.1
**Status:** Active
**Principles implemented:** P4, P5, P12, P16
**Grammar reference:** .framework/policies/tool-grammar.md v0.3
**Last Updated:** 2026-03-03

---

## Design Principles

This schema implements P5 directly: every action taken by any agent,
human, or external system is recorded as an immutable row. The schema
is designed around three constraints:

1. **Self-describing rows** — a human with no prior schema knowledge
   must be able to reconstruct what happened by reading the rows in
   order. No joins required for the primary chain-of-custody query.

2. **Complete actor coverage** — agent calls, human gate decisions,
   GitHub webhook events, and system operations all land in the same
   table under a consistent actor model.

3. **Verb-specific detail without nullable columns** — a `details`
   JSON column carries the fields that vary by verb. The core columns
   are universal and never null.

---

## Table Definitions

### `audit_log` — Primary Record

```sql
CREATE TABLE audit_log (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,

  -- What happened
  tool_name    TEXT NOT NULL,  -- full tool name: read_task_spec_task_07
  verb         TEXT NOT NULL,  -- extracted: read|write|append|submit
                               --            |request|search|get|raise
                               --            |webhook|human|system
  subject      TEXT NOT NULL,  -- extracted: task_spec|proof|work_log etc.
                               -- for non-tool events: github:push,
                               -- approve_gate, activate_task etc.

  -- Who did it
  actor        TEXT NOT NULL,  -- see Actor Model section
  actor_type   TEXT NOT NULL,  -- agent|human|webhook|system

  -- Context
  task_id      TEXT,           -- NULL for universal tools and
                               -- non-task-scoped events
  session_id   TEXT,           -- VS Code session ID (NULL for webhooks
                               -- and human actions)

  -- Verb-specific data
  details      TEXT NOT NULL,  -- JSON — see Details Reference section
                               -- never empty, never '{}'

  -- When
  created_at   TEXT NOT NULL   -- ISO 8601, set by server — callers
                               -- cannot specify or override
);
```

**Immutability triggers:**

```sql
CREATE TRIGGER audit_log_no_update
  BEFORE UPDATE ON audit_log
BEGIN
  SELECT RAISE(ABORT,
    'audit_log is immutable. UPDATE is not permitted.');
END;

CREATE TRIGGER audit_log_no_delete
  BEFORE DELETE ON audit_log
BEGIN
  SELECT RAISE(ABORT,
    'audit_log is immutable. DELETE is not permitted.');
END;
```

**Indexes:**

```sql
CREATE INDEX idx_audit_task_id
  ON audit_log(task_id, created_at);

CREATE INDEX idx_audit_actor
  ON audit_log(actor, created_at);

CREATE INDEX idx_audit_verb
  ON audit_log(verb, task_id);

CREATE INDEX idx_audit_created_at
  ON audit_log(created_at);
```


---

### `documents` — Document Version Store

The audit log records that a write happened and its hash. This table
stores the actual content. They are separate because the audit log is
an event record; this table is a content store.

```sql
CREATE TABLE documents (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  doc_type     TEXT NOT NULL,  -- task_spec|proof|work_log etc.
  task_id      TEXT,
  version      INTEGER NOT NULL DEFAULT 1,
  content_hash TEXT NOT NULL,  -- SHA-256 of content — join key to
                               -- audit_log.details.doc_version_hash
  content      TEXT NOT NULL,  -- document body
  created_by   TEXT NOT NULL,  -- actor who wrote it
  created_at   TEXT NOT NULL,

  UNIQUE(doc_type, task_id, version)
);
```

**Immutability triggers:**

```sql
CREATE TRIGGER documents_no_content_update
  BEFORE UPDATE OF content ON documents
BEGIN
  SELECT RAISE(ABORT,
    'Document content is immutable once written.');
END;

CREATE TRIGGER documents_no_delete
  BEFORE DELETE ON documents
BEGIN
  SELECT RAISE(ABORT,
    'documents is append-only. DELETE is not permitted.');
END;
```


---

### `stream_events` — Human-Readable Observable Stream

The audit log is the complete record. The stream is the curated
FO-facing view. Not every audit entry produces a stream event —
only `submit_`, `request_`, and `raise_` verbs do.

```sql
CREATE TABLE stream_events (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  task_id        TEXT,
  feature_id     TEXT,
  event_type     TEXT NOT NULL,  -- STANDARD | PRIORITY
                                 -- PRIORITY for raise_uncertainty only
  event_text     TEXT NOT NULL,  -- plain English — hardcoded in tool,
                                 -- never supplied by caller (P4)
  source_tool    TEXT NOT NULL,  -- tool_name that produced this event
  source_audit_id INTEGER NOT NULL
                   REFERENCES audit_log(id),
  created_at     TEXT NOT NULL
);

CREATE INDEX idx_stream_task_id
  ON stream_events(task_id, created_at);

CREATE INDEX idx_stream_event_type
  ON stream_events(event_type, created_at);
```


---

### `tasks` — Entity State

Tracks the current lifecycle state of every task and feature.
State is written here by `submit_`, `request_`, and `raise_` tools
atomically with their audit entry.

```sql
CREATE TABLE tasks (
  id                TEXT PRIMARY KEY,  -- task-07
  feature_id        TEXT,
  current_state     TEXT NOT NULL,
  state_entered_at  TEXT NOT NULL,
  state_entered_by  TEXT NOT NULL,     -- actor who triggered transition
  source_audit_id   INTEGER NOT NULL
                      REFERENCES audit_log(id),
  created_at        TEXT NOT NULL
);
```


---

### `tool_registry` — Registered Tools

Records which tools are currently live and for which scope. Task-scoped
tools appear here on `activate_task` and are soft-deleted on
`deactivate_task`. Universal and role-scoped tools are seeded at server
start and are never deregistered.

```sql
CREATE TABLE tool_registry (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  tool_name         TEXT NOT NULL UNIQUE,
  scope             TEXT NOT NULL,   -- universal|role|task
  task_id           TEXT,            -- NULL for universal and role-scoped
  agent_class       TEXT NOT NULL,   -- which agent class receives this tool
  registered_at     TEXT NOT NULL,
  deregistered_at   TEXT             -- NULL while active
);
```


---

## Actor Model

The `actor` column answers: *who did this?* The `actor_type` column
answers: *what class of actor was it?*

### Agent Actors

Format: `{agent-class}:{task-id}` for task-scoped agents.
Format: `{agent-class}` for universal and role-scoped agents.

```
task-performer:task-07    Task Performer scoped to task-07
qa-execution:task-07      QA Execution Agent scoped to task-07
foa                       Framework Owner Agent (no task scope)
context-agent             Context Agent (no task scope)
qa-definition             QA Definition Agent (no task scope)
uncertainty-owner:zone-4  Uncertainty Owner Agent for zone 4
```

`actor_type = 'agent'`

### Human Actors

```
human:fo                  Framework Owner
```

`actor_type = 'human'`

Human actions are recorded when the FO takes a gate action through the
FO observation layer (currently Gap 4 — not yet implemented). The schema
accommodates them now so the table structure does not change when the
layer is built.

### Webhook Actors

```
webhook:github            GitHub webhook event
```

`actor_type = 'webhook'`

### System Actors

```
system:nexus              Nexus server operations (activate_task,
                          deactivate_task, server startup)
system:policy-engine      Policy Engine state transitions triggered
                          automatically by policy rules
```

`actor_type = 'system'`

---

## Details Field Reference

The `details` column is a JSON object. Its shape is determined by the
verb. Every entry must have at least one meaningful field — an empty
`{}` is a schema violation.

### `verb = 'read'`

```json
{
  "doc_type": "task_spec",
  "doc_id": "task_spec_task_07",
  "doc_version": 3,
  "doc_version_hash": "sha256:abc123..."
}
```

`doc_version_hash` is the join key to `documents.content_hash` when
the full content of what an agent read needs to be inspected.

---

### `verb = 'write'`

```json
{
  "doc_type": "task_spec",
  "doc_id": "task_spec_task_07",
  "doc_version": 4,
  "doc_version_hash": "sha256:def456...",
  "reason": "Updated to include Redis dependency"
}
```


---

### `verb = 'append'`

```json
{
  "doc_type": "work_log",
  "doc_id": "work_log_task_07",
  "entry_hash": "sha256:ghi789...",
  "entry_preview": "First 80 chars of appended entry for log readability"
}
```

`entry_hash` covers the appended entry only, consistent with the
grammar's audit rule for `append_`.

---

### `verb = 'submit'`

```json
{
  "doc_type": "proof",
  "doc_id": "proof_task_07",
  "doc_version": 1,
  "doc_version_hash": "sha256:jkl012...",
  "reason": "All tests passing, coverage 94%, branch clean",
  "prior_state": "CLAIMED",
  "new_state": "PROOF_SUBMITTED"
}
```

State transition fields are mandatory for `submit_` — they make every
state change self-describing in the audit log without querying `tasks`.

---

### `verb = 'request'`

```json
{
  "target_actor": "human:fo",
  "target_display": "Framework Owner",
  "reason": "AC requires FO sign-off before task publication",
  "prior_state": "DEFINED",
  "new_state": "AWAITING_FO_APPROVAL"
}
```


---

### `verb = 'search'`

```json
{
  "query": "login form validation patterns",
  "tags": ["zone-4", "validation"],
  "result_count": 3,
  "top_entry_ids": ["pat-001", "pat-002", "pat-003"]
}
```

If `result_count = 0`, `top_entry_ids` is `[]`. This is a meaningful
signal — an agent searched for a pattern and found nothing. That fact
is as important as finding three results.

---

### `verb = 'get'`

```json
{
  "resource": "context_card",
  "resource_id": "foa",
  "resource_version": "v3",
  "resource_hash": "sha256:mno345..."
}
```

`resource_version` and `resource_hash` together identify exactly which
version of the system resource the agent received. For `get_current_state`:

```json
{
  "resource": "current_state",
  "resource_id": "task-07",
  "state_seen": "CLAIMED",
  "resource_hash": null
}
```


---

### `verb = 'raise'`

```json
{
  "severity": "BLOCKED",
  "uncertainty_id": "unc-001",
  "what": "Redis dependency not in environment contract",
  "why": "Cannot verify Redis availability in test environment",
  "needed": "Updated environment contract confirming Redis",
  "context_paths": [
    ".framework/features/login/tasks/task-07/environment-contract.md"
  ],
  "prior_state": "CLAIMED",
  "new_state": "BLOCKED"
}
```

`what`, `why`, `needed`, and `context_paths` are all mandatory —
consistent with the grammar rule that a `raise_uncertainty` call with
no `context_paths` is invalid.

---

### `actor_type = 'webhook'` (GitHub events)

`tool_name` = the webhook event type. `verb` = `'webhook'`.
`subject` = the parsed event class.

```json
{
  "event_class": "github:push",
  "ref": "refs/heads/task/task-07",
  "sha": "abc123def456...",
  "commit_count": 1,
  "author": "github-user",
  "payload_hash": "sha256:pqr678..."
}
```

`payload_hash` is the SHA-256 of the raw webhook payload. This allows
the original GitHub payload to be verified against the audit record if
needed.

---

### `actor_type = 'human'` (FO gate actions)

`tool_name` = the gate action name. `verb` = `'human'`.

```json
{
  "action": "approve_gate",
  "gate": "task_publication",
  "entity_type": "task",
  "entity_id": "task-07",
  "prior_state": "AWAITING_FO_APPROVAL",
  "new_state": "PUBLISHED"
}
```


---

### `actor_type = 'system'` (Nexus operations)

```json
{
  "operation": "activate_task",
  "task_id": "task-07",
  "agent_spec_path": ".github/agents/task-performer-task-07.agent.md",
  "tools_registered": [
    "read_task_spec_task_07",
    "write_proof_template_task_07",
    "append_work_log_task_07",
    "submit_proof_task_07"
  ]
}
```

System operations are not tool calls — they are internal Nexus events
that produce audit entries because they change the state of the
framework (new agent instantiated, tools registered, task archived).

---

## Canonical Query Patterns

These are the queries every role needs. They are the acceptance criteria
for the audit schema — if any query produces incorrect or incomplete
results, the schema has a gap.

### Q1 — Full chain of custody for a task

*"What happened to task-07, in order?"*

```sql
SELECT
  created_at,
  actor,
  actor_type,
  tool_name,
  json_extract(details, '$.prior_state') AS from_state,
  json_extract(details, '$.new_state')   AS to_state,
  json_extract(details, '$.reason')      AS reason
FROM audit_log
WHERE task_id = 'task-07'
ORDER BY created_at ASC;
```

This is the H5 query from Experiment 01 — it must remain the primary
chain-of-custody tool [file:3].

---

### Q2 — What an agent read before making a decision

*"What information was task-performer:task-07 working from at 14:45?"*

```sql
SELECT
  created_at,
  tool_name,
  json_extract(details, '$.doc_type')         AS doc_type,
  json_extract(details, '$.doc_version')      AS version,
  json_extract(details, '$.doc_version_hash') AS version_hash
FROM audit_log
WHERE actor    = 'task-performer:task-07'
  AND verb     = 'read'
  AND created_at < '2026-03-03T14:45:00Z'
ORDER BY created_at ASC;
```

This query was impossible before grammar v0.3. It is the direct
payoff of adding audit entries to `read_` [file:3].

---

### Q3 — Did the agent search for relevant patterns?

*"Before task-07's proof was submitted, did the agent search the
knowledge base?"*

```sql
SELECT
  created_at,
  json_extract(details, '$.query')        AS query,
  json_extract(details, '$.result_count') AS results_found,
  json_extract(details, '$.top_entry_ids') AS top_results
FROM audit_log
WHERE task_id = 'task-07'
  AND verb    = 'search'
ORDER BY created_at ASC;
```


---

### Q4 — All state transitions for a task

*"What states did task-07 move through and who triggered each?"*

```sql
SELECT
  created_at,
  actor,
  tool_name,
  json_extract(details, '$.prior_state') AS prior_state,
  json_extract(details, '$.new_state')   AS new_state
FROM audit_log
WHERE task_id = 'task-07'
  AND verb IN ('submit', 'request', 'raise', 'human', 'system')
  AND json_extract(details, '$.new_state') IS NOT NULL
ORDER BY created_at ASC;
```


---

### Q5 — All uncertainty events (any task, any zone)

*"What has been blocked or flagged across the whole system?"*

```sql
SELECT
  created_at,
  actor,
  task_id,
  json_extract(details, '$.severity')        AS severity,
  json_extract(details, '$.what')            AS what,
  json_extract(details, '$.uncertainty_id')  AS uncertainty_id
FROM audit_log
WHERE verb = 'raise'
ORDER BY created_at DESC;
```


---

### Q6 — Complete activity record for an agent class

*"Everything foa has ever done"*

```sql
SELECT
  created_at,
  tool_name,
  task_id,
  json_extract(details, '$.reason') AS reason
FROM audit_log
WHERE actor = 'foa'
ORDER BY created_at ASC;
```


---

### Q7 — GitHub events for a task

*"What code events happened on task-07's branch?"*

```sql
SELECT
  created_at,
  json_extract(details, '$.event_class') AS event,
  json_extract(details, '$.sha')         AS sha,
  json_extract(details, '$.ref')         AS ref
FROM audit_log
WHERE task_id    = 'task-07'
  AND actor_type = 'webhook'
ORDER BY created_at ASC;
```


---

### Q8 — Combined framework + code events (the full picture)

*"Everything that happened on task-07 across Nexus and GitHub"*

```sql
SELECT
  created_at,
  actor,
  actor_type,
  tool_name,
  CASE
    WHEN actor_type = 'webhook' THEN
      json_extract(details, '$.event_class')
    WHEN verb IN ('submit','request','raise') THEN
      json_extract(details, '$.prior_state') || ' → ' ||
      json_extract(details, '$.new_state')
    ELSE
      json_extract(details, '$.reason')
  END AS summary
FROM audit_log
WHERE task_id = 'task-07'
ORDER BY created_at ASC;
```

This is the single-query complete reconstruction proven in
Experiment 01 H5, now extended to cover all eight verbs plus
webhook and human events [file:3].

---

## What Constitutes a Complete Audit Record

A task's audit record is complete when it contains at least one row
for each of the following, in order:

```
system:nexus        activate_task       → task registered, tools live
agent               get_context_card    → agent loaded its context
agent               get_current_state   → agent verified task state
agent               search_knowledge_base → agent checked for patterns
agent               read_{spec}         → agent read its task document
agent               write_{template}    → agent defined completion criteria
  ... (work entries) ...
agent               append_work_log     → agent recorded progress
agent               submit_proof        → CLAIMED → PROOF_SUBMITTED
agent               get_context_card    → QA agent loaded its context
agent               read_proof          → QA agent read the evidence
agent               submit_qa_review    → PROOF_SUBMITTED → APPROVED
webhook:github      github:push         → code pushed to branch
webhook:github      github:pull_request → PR opened
webhook:github      github:merge        → PR merged
human:fo            approve_gate        → FO approved (where required)
system:nexus        deactivate_task     → tools deregistered, agent archived
```

If any of these rows is absent for a completed task, the audit record
has a gap. The framework's chain of custody is incomplete for that task.

```

***

## The Three Things This Schema Resolves

Compared to the Exp-01 schema, v0.3 grammar compliance requires three structural additions:[^13_1]

- **`read_` entries now appear** — Q2 is now executable. Before today that query returned zero rows for the most important question the audit log exists to answer: what was the agent reading when it made this decision?
- **`search_` entries now appear** — Q3 is now executable. You can determine whether an agent was working with or without awareness of a relevant Pattern Library entry.
- **Human and system events use the same table** — the unified actor model means Q8 (the full-picture query) covers everything in one pass: agent calls, webhooks, human gate decisions, and system operations, without joining across multiple tables.
<span style="display:none">[^13_2][^13_3]</span>

<div align="center">⁂</div>

[^13_1]: Nexus-exp01-retro.md
[^13_2]: NotesOnExp1Retro.md
[^13_3]: NexusModelOverview.md

---

# great. now we need to design the knowledge structures

From the derivation order, this is Step 2 — and it needs three interconnected schemas: the **Pattern Library**, the **knowledge base**, and the **context card**. They form a pipeline, so I'll design them together rather than as three isolated documents.

Let me start by mapping the full pipeline before defining any individual schema.

***

## The Knowledge Pipeline

```

EXPERIENCE                CURATION                  DELIVERY
──────────                ────────                  ────────

Tasks complete            FOA reviews               Context Agent
Experiments run     →     knowledge base     →      composes context   →  Agent receives
Uncertainties raised      promotes to               card from patterns    context card via
Retros written            Pattern Library           at instantiation      get_context_card

append_knowledge_base     write_patterns            write_context_card    get_context_card
read_knowledge_base       search_knowledge_base

                          Evidence recorded         Card versioned
                          NV score updated          in documents table
    ```

Three stores. One pipeline. The schemas must be designed so the pipeline is mechanically executable — no human judgment required at the delivery step, only at the curation step.

***

## `.framework/schema/pattern-library-schema.md`

```markdown
# Pattern Library and Knowledge Base Schema

**Version:** 0.1
**Status:** Active
**Principles implemented:** P7, P14, P17
**Grammar reference:** .framework/policies/tool-grammar.md v0.3
**Last Updated:** 2026-03-03

---

## Purpose

Two stores are defined here. They are distinct but connected:

**Knowledge Base** — the raw accumulation of project experience.
Every completed task, retrospective finding, uncertainty resolution,
and experiment result produces knowledge base entries. Entries are
created by agents and the FO during retrospectives. They are
unfiltered observations, not validated patterns.

**Pattern Library** — curated, validated, NV-scored patterns promoted
from the knowledge base by the FOA. A Pattern Library entry has been
reviewed, given an NV score, linked to evidence, and is ready to be
composed into context cards. Not everything in the knowledge base
becomes a pattern — only what is general enough to apply across tasks.

The distinction matters for P17 (trust is progressive): knowledge base
entries are observations. Pattern Library entries are validated claims
with evidence. An agent receiving a context card built from Pattern
Library entries can trust those entries in proportion to their NV score.

---

## Part 1: Knowledge Base

### DB Table — `knowledge_base`

```sql
CREATE TABLE knowledge_base (
  id            TEXT PRIMARY KEY,    -- kb-001, kb-002 etc.
  title         TEXT NOT NULL,
  entry_type    TEXT NOT NULL,       -- LEARNING | DECISION | OBSERVATION
                                     -- | ANTI_PATTERN | FRICTION
  zone          TEXT,                -- zone-0 through zone-5
                                     -- NULL = cross-cutting
  tags          TEXT NOT NULL,       -- JSON array: ["agent-creation",
                                     -- "context-cards", "zone-4"]
  summary       TEXT NOT NULL,       -- max 3 sentences —
                                     -- returned by search_knowledge_base
  full_content  TEXT NOT NULL,       -- full entry body
  source_type   TEXT NOT NULL,       -- RETROSPECTIVE | EXPERIMENT
                                     -- | UNCERTAINTY_RESOLUTION | MANUAL
  source_ref    TEXT NOT NULL,       -- e.g. "exp-01" | "task-07"
                                     -- | "unc-003" | "session:2026-03-03"
  pattern_ref   TEXT REFERENCES patterns(id),
                                     -- NULL until promoted to a pattern
  status        TEXT NOT NULL        -- UNREVIEWED | REVIEWED | PROMOTED
                   DEFAULT 'UNREVIEWED',
                                     -- UNREVIEWED: not yet seen by FOA
                                     -- REVIEWED: FOA has seen it, not
                                     --   promoted
                                     -- PROMOTED: linked to a Pattern
                                     --   Library entry
  created_by    TEXT NOT NULL,       -- actor who created this entry
  created_at    TEXT NOT NULL
);

CREATE INDEX idx_kb_zone
  ON knowledge_base(zone, entry_type);

CREATE INDEX idx_kb_status
  ON knowledge_base(status, created_at);

CREATE INDEX idx_kb_tags
  ON knowledge_base(tags);           -- JSON index for tag filtering
```

**Immutability:**

```sql
CREATE TRIGGER kb_no_content_update
  BEFORE UPDATE OF full_content ON knowledge_base
BEGIN
  SELECT RAISE(ABORT,
    'knowledge_base entries are immutable once written.
    Create a new entry to supersede this one.');
END;
```

Knowledge base entries are observations at a point in time. If the
observation was wrong, a new entry records the correction — the original
is not edited. This preserves the full learning history (P14).

---

### File Format — Knowledge Base Entry

Knowledge base entries are stored in the DB. They do not have
individual files. The `full_content` column holds the full text.

The `append_knowledge_base` tool writes directly to the DB.
The `search_knowledge_base` tool queries the DB.
There is no file representation.

---

### Entry Types

| Type | When to use |
| :-- | :-- |
| `LEARNING` | Something the framework learned — a design decision that emerged from evidence |
| `DECISION` | A named FO decision that should inform future context cards |
| `OBSERVATION` | A factual observation from a task or experiment — may become a pattern |
| `ANTI_PATTERN` | Something that was tried and failed — must appear in context cards to prevent recurrence |
| `FRICTION` | A friction point from a retro — procedural, not design |

`ANTI_PATTERN` entries are treated preferentially by the Context Agent —
they are included in context cards even at lower relevance scores because
the cost of repeating an anti-pattern is higher than the cost of including
a context item the agent doesn't need (P2).

---

## Part 2: Pattern Library

### DB Table — `patterns`

```sql
CREATE TABLE patterns (
  id              TEXT PRIMARY KEY,   -- pat-001, pat-002 etc.
  pattern_name    TEXT NOT NULL,      -- short, memorable handle:
                                      -- "proof-template-before-impl"
                                      -- "no-self-review"
                                      -- "pre-flight-before-work"
  version         INTEGER NOT NULL    -- increments on edit
                    DEFAULT 1,
  zone            TEXT,               -- zone-0 through zone-5
                                      -- NULL = cross-cutting
  tags            TEXT NOT NULL,      -- JSON array
  agent_classes   TEXT NOT NULL,      -- JSON array — which agent classes
                                      -- this pattern applies to
                                      -- ["task-performer", "qa-execution"]
                                      -- ["*"] = all agents
  initial_nv      INTEGER NOT NULL,   -- NV score when first introduced
                                      -- (0–3, 0=validated, 3=experimental)
  current_nv      INTEGER NOT NULL,   -- current NV score — decreases as
                                      -- evidence accumulates
  evidence_count  INTEGER NOT NULL    -- number of validated instances
                    DEFAULT 0,
  status          TEXT NOT NULL       -- EXPERIMENTAL | ACTIVE | DEPRECATED
                    DEFAULT 'EXPERIMENTAL',
  summary         TEXT NOT NULL,      -- max 3 sentences — returned by
                                      -- search_knowledge_base
  full_content    TEXT NOT NULL,      -- full pattern specification
  rationale       TEXT NOT NULL,      -- why this pattern exists —
                                      -- which principle it implements
  violation_looks_like TEXT NOT NULL, -- what a designer would observe
                                      -- if this pattern were being broken
  supersedes      TEXT                -- pattern_id this replaces
                    REFERENCES patterns(id),
  source_kb_ids   TEXT NOT NULL,      -- JSON array of knowledge_base IDs
                                      -- that were promoted to create this
  created_by      TEXT NOT NULL,
  created_at      TEXT NOT NULL,
  updated_at      TEXT NOT NULL
);

CREATE INDEX idx_patterns_zone
  ON patterns(zone, status);

CREATE INDEX idx_patterns_nv
  ON patterns(current_nv, status);

CREATE INDEX idx_patterns_agent_classes
  ON patterns(agent_classes);
```


---

### DB Table — `pattern_evidence`

Records every validated instance of a pattern. This is how NV scores
decrease over time (P17 — trust is progressive).

```sql
CREATE TABLE pattern_evidence (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  pattern_id    TEXT NOT NULL REFERENCES patterns(id),
  session_ref   TEXT NOT NULL,    -- experiment or task identifier
                                  -- e.g. "exp-01" | "task-07"
  task_id       TEXT,             -- specific task, if applicable
  outcome       TEXT NOT NULL,    -- PASS | FAIL | PARTIAL
  outcome_notes TEXT NOT NULL,    -- what happened — required, not optional
  nv_delta      INTEGER NOT NULL, -- change to NV score:
                                  -- PASS   → -1 (toward validated)
                                  -- FAIL   → +1 (toward experimental)
                                  -- PARTIAL → 0
  recorded_by   TEXT NOT NULL,
  recorded_at   TEXT NOT NULL
);

CREATE INDEX idx_evidence_pattern
  ON pattern_evidence(pattern_id, recorded_at);
```

**NV Score Rules:**

```
Initial NV at introduction:
  Cross-cutting / foundational pattern   → NV 2
  Zone-specific / role-specific pattern  → NV 1
  Validated by FO from existing evidence → NV 0

NV transitions (automatic when evidence is recorded):
  After 3× PASS with no FAIL            → NV drops by 1
  Any FAIL                               → NV rises by 1 (max 3)
  NV 0 with 5+ consecutive PASS          → status = ACTIVE (locked)
  NV 3 with 2+ consecutive FAIL          → status = DEPRECATED
                                         → triggers stream event
```

These transitions are enforced by the Policy Engine when
`append_knowledge_base` or an FOA retrospective write records a new
evidence entry. The FOA receives a stream event on every NV transition.

---

### Pattern Entry Format

Every pattern has the same four-field content structure, enforced by
the `write_patterns` tool's Zod schema. Agents and the FOA cannot
submit a partial pattern.

```markdown
## {pattern_name}

**Rationale:**
{One paragraph. Which principle(s) does this implement and why?
Reference the principle by ID: P3, P7 etc.}

**What this pattern requires:**
{Concrete description of what an agent or designer must do.
Specific enough that compliance is unambiguous.}

**Violation looks like:**
{What a reviewer would observe if this pattern were being broken.
Must be a specific observable condition, not "the pattern is absent".}

**Evidence:**
{Automatically populated from pattern_evidence table.
Not authored manually.}
```

The `violation_looks_like` field is mandatory for the same reason it
is mandatory in the Guiding Principles document — a pattern without a
detectable violation is untestable and therefore unenforceable.

---

### `.framework/patterns/.index.md`

This is the machine-readable index that `search_knowledge_base` uses
for lightweight pre-filtering before querying the DB. It is regenerated
by the Nexus server whenever a pattern is written or status changes.
It is never edited manually.

```markdown
# Pattern Library Index
<!-- AUTO-GENERATED — do not edit manually -->
<!-- Last regenerated: 2026-03-03T16:41:00Z -->

| ID | Name | Zone | NV | Status | Tags |
|---|---|---|---|---|---|
| pat-001 | proof-template-before-impl | zone-4 | 0 | ACTIVE | execution,proof,qa |
| pat-002 | no-self-review | cross-cutting | 0 | ACTIVE | agent-design,qa,separation |
| pat-003 | pre-flight-before-work | cross-cutting | 1 | EXPERIMENTAL | uncertainty,preflight |
```


---

## Part 3: Context Card Schema

`.framework/schema/context-card-schema.md`

```markdown
# Context Card Schema

**Version:** 0.1
**Status:** Active
**Principles implemented:** P7, P14
**Last Updated:** 2026-03-03

***

## What a Context Card Is

A context card is the minimum sufficient briefing for a specific agent
at a specific moment. It is generated, not authored — the Context Agent
composes it from the Pattern Library and current task state. It is not
a static template filled in by a human.

Every agent calls `get_context_card` as its first action. The card is
versioned in the `documents` table. The audit entry records which
version the agent received.

***

## Composition Rules (P7)

The Context Agent follows these rules when generating a card:

1. **Include only what is relevant to this agent class and task.**
   A Task Performer card for task-07 does not include Feature Owner
   patterns unless they directly constrain task-07's work.

2. **Patterns ranked by NV score, then relevance.**
   NV 0 (validated) patterns that match the agent class and zone are
   always included. NV 1–2 patterns are included only if relevance
   score > 0.7.

3. **Anti-patterns are preferential.**
   All ANTI_PATTERN entries matching the agent class are included
   regardless of NV score. An experimental anti-pattern is more
   important to surface than a validated positive pattern.

4. **Compression is prohibited.**
   The Context Agent selects and excludes — it never summarises or
   paraphrases source artefacts. A source document either appears
   verbatim (for short references) or is excluded. Partial content
   is not permitted.

5. **Maximum pattern entries: 7.**
   If more than 7 patterns match, take the top 5 by NV score
   (lowest first) + all ANTI_PATTERNs up to a maximum of 7 total.
   If this forces exclusion of relevant patterns, add an
   `open_flags` entry noting what was excluded and why.

6. **Conflicts are surfaced, not resolved.**
   If two included patterns contradict each other, both are included
   with an `open_flags` entry describing the conflict. The Context
   Agent does not resolve conflicts — that is an FO decision.

***

## Card Structure

```typescript
type ContextCard = {

  // ── Identity ──────────────────────────────────────────
  agent_class:    string      // "task-performer"
  agent_instance: string      // "task-performer:task-07"
                              // same as actor in audit_log
  zone:           string      // "zone-4"
  card_version:   string      // "v4" — increments on regeneration
  card_hash:      string      // SHA-256 of card content
                              // recorded in audit_log on get_context_card
  generated_at:   string      // ISO timestamp
  generated_by:   string      // "context-agent" always
  valid_until:    string | null
                              // ISO timestamp if time-bounded
                              // null = valid until source artefacts change

  // ── Task Context ──────────────────────────────────────
  current_task:   string | null     // "task-07" | null for role-level cards
  task_state:     string | null     // "CLAIMED" | null
  feature_id:     string | null     // "login-feature" | null

  // ── Permissions ───────────────────────────────────────
  reads:    string[]     // declared READS paths for this agent+task
  writes:   string       // the single WRITES path — always exactly one
  never:    string[]     // NEVER paths — unconditional

  // ── Governance ────────────────────────────────────────
  active_policies: PolicyRef[]
  certainty_threshold: number  // 0–1, declared per agent class

  // ── Patterns ──────────────────────────────────────────
  patterns: PatternEntry[]     // max 7 — see composition rules
  anti_patterns: PatternEntry[] // separate list for visual prominence

  // ── Constraints ───────────────────────────────────────
  constraints: string[]   // stack, environment, scope constraints
                          // e.g. "use npm not bun"
                          //      "target Node 20 LTS"
                          //      "branch must be task/task-07"

  // ── Open Flags ────────────────────────────────────────
  open_flags: OpenFlag[]  // conflicts, gaps, known uncertainties
                          // the agent should be aware of before starting

  // ── Tool Declaration ──────────────────────────────────
  // NOTE: tools are not listed in the card — agents call
  // get_my_capabilities for the live tool list.
  // The card declares permissions; the tool registry declares capability.
  // These are governed separately.
}

type PolicyRef = {
  policy_name: string
  path:        string   // .framework/policies/... path
  version:     string
}

type PatternEntry = {
  pattern_id:           string   // pat-001
  pattern_name:         string
  current_nv:           number
  summary:              string   // 3 sentences max
  full_content_path:    string   // path to full pattern for read_ if needed
  relevance_reason:     string   // why this pattern was included for
                                 // this specific agent and task
}

type OpenFlag = {
  flag_type: 'CONFLICT' | 'GAP' | 'KNOWN_UNCERTAINTY' | 'EXCLUSION'
  description: string
  source:      string   // what produced this flag
}
```


***

## Stale Card Detection

A context card becomes stale when any of its source artefacts change:

- A pattern in the card is updated or deprecated
- The task state changes
- A new policy is added that applies to this agent class
- A new anti-pattern is added that applies to this agent class

Nexus detects staleness by tracking `card_hash` against source
artefact hashes. When staleness is detected:

- `get_context_card` returns the card with `stale: true`
- The agent treats this as an `ASSUMED` pre-flight result
- The Context Agent is notified via stream event to regenerate

***

## Card Storage

Context cards exist in two places — consistent with the two-layer
architecture in `.framework/policies/platform-constraints.md`:

**VS Code layer** (`.framework/context-cards/`):
The current generated card as a `.md` file. Loaded by VS Code at agent
instantiation. Read by the agent using built-in VS Code tools during
initial orientation.

**Nexus MCP layer** (`documents` table):
The governed, versioned copy. Written by `write_context_card`. Read
by the FOA via `read_context_card`. This is the version recorded in
the audit log on `get_context_card`.

Both are always in sync. The Context Agent writes both in one operation.

***

## Context Card Index

`.framework/context-cards/.index.md` — machine-readable, auto-generated:

```markdown
# Context Card Index
<!-- AUTO-GENERATED -->

| Agent Class | Instance | Version | Generated At | Stale? |
|---|---|---|---|---|
| foa | foa | v2 | 2026-03-03T14:00:00Z | false |
| task-performer | task-performer:task-07 | v1 | 2026-03-03T14:45:00Z | false |
```

```

---

## How the Three Schemas Connect

```

KNOWLEDGE BASE              PATTERN LIBRARY           CONTEXT CARDS
──────────────              ───────────────           ─────────────

append_knowledge_base       write_patterns            write_context_card
(Context Agent)
kb-001: "agents that      pat-001:                  card for
define their own          "proof-template-           task-performer
proof criteria            before-impl"               :task-07
consistently miss
the AC bar"               initial_nv: 1             includes:
evidence_count: 3           - pat-001 (NV 0)
kb-002: "QA rejected      current_nv: 0               - pat-002 (NV 0)
3 of 5 proofs where       status: ACTIVE              - constraint:
performer wrote                                         "npm not bun"
template"                 pattern_evidence:           - open_flags: []
exp-01: PASS -1
↓ FOA promotes            task-07: PASS -1
to pattern                task-09: PASS -1   →      get_context_card
(Task Performer)
status: PROMOTED
pattern_ref: pat-001      NV 1→0 auto               audit: card_hash
stream event → FO           recorded

```

The pipeline is mechanically executable:
- **FOA** decides what to promote (curation judgment)
- **Context Agent** decides what to include (composition rules)
- **Evidence** updates NV automatically (no judgment needed)

The only human judgment in the pipeline is the FOA's promotion decision.
Everything else is structural.
```


***

## The Three Gaps This Design Closes

From the derivation order compliance audit:[^14_1]

- **Gap: Pattern Library schema not defined** → now fully specified including NV scoring rules, evidence table, and `.index.md` format
- **Gap: Context card template fields not locked** → now locked as a typed schema with composition rules and stale detection
- **Gap: No formal retrospective-to-entry process** → the `append_knowledge_base` → `write_patterns` pipeline, with `status` transitions (`UNREVIEWED → REVIEWED → PROMOTED`), is the formal process

The `.index.md` files in both `patterns/` and `context-cards/` are the machine-readable surfaces that `search_knowledge_base` and `get_context_card` query first, before touching the DB — keeping those tools fast and the DB queries targeted.

<div align="center">⁂</div>

[^14_1]: session-summary-20260303-a.md


---

# the inline markdown causes problem with the code block fences in the browser. was this all meant to go in the pattern-library-schema.md file or was I supposed to put the context-card-schema in it's own file?

They should be in separate files, as named in the derivation order:

- `.framework/schema/pattern-library-schema.md` — contains Part 1 (Knowledge Base) and Part 2 (Pattern Library) only
- `.framework/schema/context-card-schema.md` — contains Part 3 (Context Card) only

The inline heading `## Part 3: Context Card Schema` with its own filename callout was the split point — everything from there to the end goes into `context-card-schema.md`.

***

## Splitting the Content

**`.framework/schema/pattern-library-schema.md`** gets:

- The header block (version, principles, etc.)
- The Knowledge Pipeline diagram
- Part 1 — Knowledge Base (`knowledge_base` table, immutability trigger, indexes, entry types)
- Part 2 — Pattern Library (`patterns` table, `pattern_evidence` table, NV score rules, pattern entry format, `.index.md` format)

**`.framework/schema/context-card-schema.md`** gets:

- Its own header block (version, principles, etc.)
- What a Context Card Is
- Composition Rules
- Card Structure (the TypeScript type definitions)
- Stale Card Detection
- Card Storage
- Context Card Index format

**Both files** get the "How the Three Schemas Connect" pipeline diagram at the bottom — it is the cross-reference that explains how the two files relate to each other. Put a copy in each, or put it in a third file `.framework/schema/knowledge-pipeline.md` and reference it from both. The third file is the cleaner option as the schemas grow.

---

# what's next?

From the derivation order we established, here is where we are:


| Step | Deliverable | Status |
| :-- | :-- | :-- |
| 1 | Tool Grammar v0.3 | ✅ Done |
| 2 | Knowledge Structures (Pattern Library, Knowledge Base, Context Card schemas) | ✅ Done |
| 3 | Agent Design Standard (Base Agent Template) | ⬅ Next |
| 4 | Work Lifecycle (zone policies) | Pending |
| 5 | Governance Policies (Agent Creation, Context Curation, Uncertainty) | Pending |
| 6 | Infrastructure Build (Exp-02) | Pending |


***

## Step 3 is next — the Base Agent Template

This is the right moment for it because we now have everything it needs to reference:

- The grammar (what tools look like)
- The audit schema (what every tool call produces)
- The knowledge structures (what `get_context_card` returns, what `search_knowledge_base` queries)

The base template needs to be revisited against the principles — specifically these four that weren't upstream when the current template was written:

**P5** — the startup sequence in the template must explicitly include `read_` and `search_` calls as audited actions, not informal suggestions

**P8** — the `REVIEWER:` field exists but isn't traced to P8; the Agent Pair invariant needs to be structurally enforced in the template, not just declared

**P15** — "one agent, one artefact" needs to be a stated constraint in the template, with the single `WRITES:` field as its structural expression

**P16** — the `READS:` / `NEVER:` split needs to explicitly reflect the two-layer architecture from the platform constraints document — VS Code layer paths vs Nexus MCP layer paths are governed differently

***

There is also one new thing to add that didn't exist before: the **mandatory lifecycle block** — the ordered sequence every agent must follow before doing any role-specific work, now that we have the full universal tool set defined. This replaces the informal "call preflight first" instruction with a concrete, traceable sequence tied to the grammar.

Shall we proceed with the Base Agent Template revision?

---

# yes proceed

Good. I have everything I need. Here is the full revised Base Agent Template — v0.2 — with every change traced to its principle.

***

## What Changed From v0.1 and Why

Before the full document, the changes from what exists in the Agent Creation Policy:[^17_1]


| Field / Section | v0.1 | v0.2 | Principle |
| :-- | :-- | :-- | :-- |
| `REVIEWER:` | Missing | Required | P8 |
| `CERTAINTY_THRESHOLD:` | Missing | Required | P9 |
| `PRINCIPLES:` | Missing | Required | Traceability |
| Tool list structure | Flat list | Three mandatory groups | Grammar v0.3 |
| Tool names | Pre-grammar (feedlive, preflight_check, agentraiseuncertainty) | Grammar-compliant | P12 |
| `READS:` | Undifferentiated | Two-layer annotated | P5, Platform Constraints |
| `NEVER:` | Undifferentiated | Structurally enforced vs convention-only annotated | P3, Platform Constraints |
| Mandatory Lifecycle Block | Missing | Required, grammar-compliant | P9, Grammar v0.3 |
| Spec tests | Informal | Explicit, numbered, traceable | P13 |


***

## `.framework/templates/base-agent-template.md`

```markdown
# Base Agent Template

**Version:** 0.2
**Status:** Active
**Principles implemented:** P3, P4, P5, P8, P9, P12, P15
**Policy reference:** .framework/policies/agent-creation-policy.md
**Platform reference:** .framework/policies/platform-constraints.md
**Grammar reference:** .framework/policies/tool-grammar.md v0.3
**Last Updated:** 2026-03-03

---

## Purpose

This is the minimum valid structure that every agent template must
conform to. It is enforced by Agent Spec QA's spec tests — a template
that does not satisfy every required field cannot be approved regardless
of its other qualities.

Fields exist because a principle requires them. The principle reference
is given for every field. A designer removing a field must identify
which principle they are overriding and why — not simply omit it.

---

## The Template

The structure below shows every required field with its type,
constraints, and principle reference. Angle-bracket values are
placeholders to be replaced. Square-bracket values are fixed
vocabulary options.

---

### Part 1 — VS Code Frontmatter

This section is parsed by VS Code Agent Mode. Field names and format
are fixed by the VS Code agent spec schema. Do not reorder.

```yaml
***
name: [AgentClassName]
# REQUIRED. PascalCase. No spaces. Matches the agent class name in
# the Agent Pair Registry.
# P12: naming is load-bearing — this name appears in every audit log
# entry this agent produces.

description: "[One sentence. What is this agent hired to do?]"
# REQUIRED. Single sentence only. No multi-line prose.
# Must answer: what ONE thing does this agent produce?
# P15: one agent, one artefact — the description makes this explicit.

model: claude-sonnet-4-5
# REQUIRED. Single model. Fallback model declared in Nexus config,
# not here.

tools:
  # ── Group 1: Universal ─────────────────────────────────────────
  # These five are present on every agent without exception.
  # Never remove any of them. Never reorder this group.
  # P9: raise_uncertainty is a universal safety valve — no agent
  # may be without it.
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - search_knowledge_base
  - raise_uncertainty

  # ── Group 2: Role-scoped ───────────────────────────────────────
  # Tools available to this agent class across all tasks.
  # May be empty — include the comment even if no tools are listed.
  # [role-scoped tools here, or leave empty with comment]

  # ── Group 3: Task-scoped ──────────────────────────────────────
  # Tools scoped to a specific task instance.
  # Populated at activation time via activate_task.
  # Template shows the pattern; actual tool names carry task suffix.
  # [task-scoped tools here, e.g. read_task_spec_task_07]
***
```


---

### Part 2 — Agent Identity Fields

These fields are parsed by the Nexus server and Agent Spec QA.
Each field is on its own line. No indentation. No YAML.

```
ZONE: [zone-number] [zone-name]
# REQUIRED. e.g. "ZONE: 4 Task Execution"
# Valid values: 0 Framework, 1 Idea, 2 Feature Definition,
#               3 Task Preparation, 4 Task Execution,
#               5 Feature Delivery
# Cross-cutting agents: "ZONE: cross-cutting"

TYPE: [ORCHESTRATOR|EXECUTOR|REVIEWER|COMPRESSION]
# REQUIRED.
# ORCHESTRATOR: directs other agents, does not directly produce output
# EXECUTOR: performs work, produces primary artefact
# REVIEWER: independently verifies another agent's artefact (P8)
# COMPRESSION: distils context, does not produce domain artefacts

QA_TIER: [0|1|2|3|4]
# REQUIRED. Set by the FOA per NV/BR scoring in agent-creation-policy.
# This field is checked by Agent Spec QA — a template cannot override
# its own tier (P8: no self-review of QA standards).

CERTAINTY_THRESHOLD: [0.0–1.0]
# REQUIRED. Minimum self-assessed certainty before proceeding.
# Below this threshold, the agent must call raise_uncertainty.
# Typical values: 0.8 for EXECUTOR, 0.9 for ORCHESTRATOR.
# REVIEWER agents: 0.95 (higher — review errors propagate further).
# P9: fail loudly. This threshold is the structural expression of
# that principle for intra-zone work.

REVIEWER: [AgentClassName]
# REQUIRED. The agent class that independently reviews this agent's
# output. Must be a different class — never self.
# P8: no single agent defines, executes, and verifies its own work.
# This field is checked by Agent Spec QA: if REVIEWER == name,
# the spec test fails unconditionally.

PRINCIPLES: [P-ID, P-ID, ...]
# REQUIRED. Comma-separated list of principle IDs this agent
# directly implements. Minimum one. Maximum is not bounded.
# Used by the FOA to verify that every principle in the list is
# actually reflected in the agent's design.
# e.g. "PRINCIPLES: P3, P8, P9, P15"
```


---

### Part 3 — Scope Declaration

```
READS:
  # ── VS Code layer reads ────────────────────────────────────────
  # Accessed via VS Code built-in tools. Unaudited.
  # (see platform-constraints.md Gap 1)
  # Include only the context card and any VS Code layer files this
  # agent loads at instantiation.
  - .framework/context-cards/[agent-class].context-card.md

  # ── Nexus MCP layer reads ──────────────────────────────────────
  # Accessed via read_ tools. Fully audited (grammar v0.3, P5).
  # Named file paths only. No wildcards. No categories.
  # Every path listed here must have a corresponding read_ tool in
  # Group 2 or Group 3 of the tools list above.
```

- .framework/features/<feature>/tasks/<task>/task-spec.md

```
# [additional named paths]

WRITES:
- [exactly one path]
# REQUIRED. Exactly one entry. Not a directory. Not a pattern.
# P15: one agent, one artefact.
# The write_ or submit_ tool in the tools list must target this path.
# If the agent has no write_ tool, this is a design error — raise
# with the FOA before proceeding.

NEVER:
# ── Structurally enforced ──────────────────────────────────────
# These are enforced by tool absence — no tool exists for these
# paths in this agent's registry. Violation is architecturally
# impossible via MCP tools (P3).
- .framework/features/<other-task>/**

# ── Convention only ────────────────────────────────────────────
# These are NOT structurally enforced. The agent holds VS Code
# built-in tools that could read these paths. Enforcement is via
# context card declaration and good-faith compliance.
# (see platform-constraints.md Gap 1 — accepted limitation)
# P3 partial compliance — named here for honest documentation.
- .framework/policies/**
- .framework/agent-classes/**
# [any other governance paths this agent must not touch]
```

**Constraint on NEVER:**
Every NEVER list must contain at least one entry in each section.
An agent with no structurally-enforced boundary has no OCAP protection
at all (P3 violation). An agent with no convention-only section has not
honestly documented its platform access.

---

### Part 4 — Framework References

```
SKILL: [skill-name]
# REQUIRED if the agent has substantive role-specific logic.
# References a file at .github/skills/[skill-name].skill.md
# The skill file holds role-specific behaviour. The agent file holds
# identity, scope, and the mandatory lifecycle block only.
# If the agent has no role-specific logic beyond the lifecycle,
# this field may be omitted — document why in a comment.

CONTEXT_TREE_REF: context-tree.md#[node-id]
# REQUIRED. Where this agent sits in the context tree.
# Must match an entry in .framework/context-tree.md.
# If the node does not exist, the agent class is not yet registered
# in the tree — raise this with the FOA before approval.

PATTERN_REF: [pat-id]
# REQUIRED after first approved run. Omitted only on initial creation.
# References the Pattern Library entry for this agent class.
# When the FOA approves the agent, it creates pat-[id] and updates
# this field. Templates in agent-classes/ always have this populated.
# P17: trust is progressive — this links the agent to its NV history.
```


---

### Part 5 — Mandatory Lifecycle Block

Every agent template must include this section verbatim, with only
the role-specific step (Step 6) varying by agent class.

The lifecycle block is an instruction to the agent — it is not
structurally enforced by a single tool. Compliance is verified via
the audit log: an agent that skips any step will produce an audit
record with a visible gap.

```
## Lifecycle

### Mandatory Startup Sequence (all agents, no exceptions)

Step 1 — Load identity
  call: get_context_card
  on CARD_NOT_FOUND:  call raise_uncertainty immediately. STOP.
  on stale: true:     treat as ASSUMED. Continue with open_flags noted.

Step 2 — Verify capabilities
  call: get_my_capabilities
  check: all Group 3 task-scoped tools expected for this task are present.
  on missing tool:    call raise_uncertainty. STOP.

Step 3 — Verify entity state
  call: get_current_state(entity_type, entity_id)
  check: current_state matches expected precondition for this agent's work.
  on wrong state:     call raise_uncertainty. STOP. Do not proceed on
                      assumption that state will resolve itself.

Step 4 — Check Pattern Library
  call: search_knowledge_base(query=[role-relevant query], tags=[zone, type])
  apply any ANTI_PATTERN entries found before proceeding.
  note: zero results is a valid outcome — record in work_log.

Step 5 — Pre-flight assessment
  Assess certainty against CERTAINTY_THRESHOLD using context from Steps 1–4.

  CLEAR (certainty ≥ threshold, no conflicts):
    → proceed to Step 6.

  ASSUMED (certainty ≥ threshold, assumptions present):
    → call append_work_log with assumption list.
    → proceed to Step 6 with assumptions logged.

  BLOCKED (certainty < threshold OR unresolvable conflict):
    → call raise_uncertainty(severity='BLOCKED', ...)
    → STOP. Do not proceed to Step 6 under any circumstances.
       There is no override for BLOCKED. (P9)

### Step 6 — Role-Specific Work
[Replace this section with the agent's specific work steps.
Each step must reference the grammar-compliant tool it calls.
No step may instruct the agent to produce a stream event directly —
stream events are produced by submit_, request_, and raise_ tools
automatically. (P4)]

### Zone Boundary Rule (ORCHESTRATOR and EXECUTOR agents only)
If this agent is receiving a handoff from another zone:
  Before Step 6:
    call: submit_repeatback(handoff_context_paths=[...])
    await: zone QA agent confirmation
    on NOT_OK: call raise_uncertainty. STOP.
```


---

## Spec Test Requirements

These are the tests Agent Spec QA runs against every template.
Every test must PASS before any template is approved.

```
T-01  name field is present and non-empty
T-02  name is PascalCase with no spaces
T-03  description is present and exactly one sentence
T-04  model field is present
T-05  tools list contains all five universal tools in Group 1
T-06  tools list has exactly three groups (even if Group 2 is empty)
T-07  ZONE field is present and matches valid zone vocabulary
T-08  TYPE field is present and matches valid type vocabulary
T-09  QA_TIER field is present and is an integer 0–4
T-10  CERTAINTY_THRESHOLD field is present and is a float 0.0–1.0
T-11  REVIEWER field is present and non-empty
T-12  REVIEWER value does not equal name value  ← P8 invariant
T-13  PRINCIPLES field is present with at least one P-ID
T-14  READS contains at least one VS Code layer entry
T-15  READS contains at least one Nexus MCP layer entry
T-16  Every Nexus MCP layer READ has a corresponding read_ tool in
      the tools list
T-17  WRITES contains exactly one path
T-18  WRITES path is not a directory and does not contain wildcards
T-19  The WRITES path has a corresponding write_ or submit_ tool in
      the tools list
T-20  NEVER list has at least one structurally-enforced entry
T-21  NEVER list has at least one convention-only entry
T-22  SKILL field references a file that exists at declared path,
      OR is omitted with a documented reason
T-23  CONTEXT_TREE_REF is present and matches an entry in
      context-tree.md
T-24  Mandatory Lifecycle Block is present and contains all five
      startup steps in order
T-25  Step 6 references only grammar-compliant tool names
T-26  No step in the lifecycle instructs the agent to emit a stream
      event directly  ← P4 invariant
T-27  Total file length does not exceed 80 lines
      (context is in the card and skill, not here)
T-28  PATTERN_REF is present on approved templates
      (omitted only on initial submission — checked at approval, not
      at template creation)
```


---

## Conformant Example — Task Performer (task-07 instance)

This is what a fully hydrated, grammar-compliant `.agent.md` looks like
after `activate_task` generates it from the base template. It is not
the template itself — it is an instance.

```yaml
***
name: TaskPerformer
description: "Executes a single published task and produces literal
  proof of completion against pre-defined criteria."
model: claude-sonnet-4-5
tools:
  # Group 1 — Universal
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - search_knowledge_base
  - raise_uncertainty

  # Group 2 — Role-scoped
  # (none — Task Performer reads are task-scoped only)

  # Group 3 — Task-scoped (task-07)
  - read_task_spec_task_07
  - read_environment_contract_task_07
  - write_proof_template_task_07
  - append_work_log_task_07
  - submit_proof_task_07
***

ZONE: 4 Task Execution
TYPE: EXECUTOR
QA_TIER: 2
CERTAINTY_THRESHOLD: 0.8
REVIEWER: QAExecutionAgent
PRINCIPLES: P3, P6, P8, P9, P15

READS:
  # VS Code layer (unaudited)
  - .framework/context-cards/task-performer.context-card.md

  # Nexus MCP layer (audited via read_ tools)
  - .framework/features/<feature>/tasks/task-07/task-spec.md
  - .framework/features/<feature>/tasks/task-07/environment-contract.md

WRITES:
  - .framework/features/<feature>/tasks/task-07/proof-of-completion.md

NEVER:
  # Structurally enforced — no tool exists for these
  - .framework/features/<feature>/tasks/task-08/**
  - .framework/features/<feature>/tasks/task-09/**

  # Convention only — VS Code built-in access not prevented
  - .framework/policies/**
  - .framework/agent-classes/**
  - .framework/features/<feature>/feature-spec.md

SKILL: task-performer
CONTEXT_TREE_REF: context-tree.md#zone-4-task-performer
PATTERN_REF: pat-004

## Lifecycle

### Mandatory Startup Sequence

Step 1 — Load identity
  call: get_context_card
  on CARD_NOT_FOUND: call raise_uncertainty. STOP.
  on stale: true: treat as ASSUMED. Continue.

Step 2 — Verify capabilities
  call: get_my_capabilities
  check: submit_proof_task_07 is present in Group 3.
  on missing: call raise_uncertainty. STOP.

Step 3 — Verify entity state
  call: get_current_state(entity_type='task', entity_id='task-07')
  check: current_state == 'PUBLISHED'
  on wrong state: call raise_uncertainty. STOP.

Step 4 — Check Pattern Library
  call: search_knowledge_base(
    query='task execution proof completion zone 4',
    tags=['zone-4', 'executor', 'proof']
  )
  apply any ANTI_PATTERN entries before proceeding.

Step 5 — Pre-flight assessment
  CLEAR:   proceed to Step 6.
  ASSUMED: call append_work_log_task_07 with assumptions. proceed.
  BLOCKED: call raise_uncertainty(severity='BLOCKED'). STOP.

### Step 6 — Task Execution

  6a. Read task specification
      call: read_task_spec_task_07
      call: read_environment_contract_task_07

  6b. Define completion criteria BEFORE implementation
      call: write_proof_template_task_07(
        reason='Defining completion criteria from task-spec AC'
      )
      P6: proof template defines what done looks like before any
      implementation begins. Non-negotiable sequence.

  6c. Implement
      Use VS Code built-in tools (terminal, edit) for code work.
      call: append_work_log_task_07 at each significant step.

  6d. Submit proof
      call: submit_proof_task_07(
        reason='Implementation complete, all criteria met'
      )
      This tool atomically: writes proof, transitions state to
      PROOF_SUBMITTED, emits stream event. (P4)
      Do not emit stream events separately — they are inside the tool.

### Zone Boundary Rule
This agent receives handoff from Zone 3. Before Step 6:
  call: submit_repeatback(
    handoff_context_paths=[task-spec, environment-contract],
    agent_role='TaskPerformer'
  )
  await QA confirmation. on NOT_OK: raise_uncertainty. STOP.
```


---

## What This Template Makes Structurally Visible

These things are now detectable by Agent Spec QA mechanically,
without human judgment:

- **P8 violations** (T-12): REVIEWER == name catches self-review at
template creation, before any agent is ever instantiated
- **P4 violations** (T-26): any lifecycle step that says "emit event"
directly is caught before approval
- **P5 partial gaps** (T-14, T-15, T-16): every MCP-layer read must
have a corresponding tool — orphaned reads that would be unaudited
are caught
- **P15 violations** (T-17): two paths in WRITES is caught immediately
- **P9 gaps** (T-24): a template without the mandatory lifecycle block
fails T-24 — the certainty threshold and raise_uncertainty path
cannot be absent

```

***

## The Three Things This Adds That Weren't There Before

**1. Honest two-layer READS annotation**[^17_1]
The old template listed READS as a flat list. There was no way to know which reads were audited (MCP tools) and which were not (VS Code built-ins). T-14, T-15, and T-16 now enforce this explicitly — and the annotation makes the P5 partial compliance gap visible at design time rather than audit time.

**2. `REVIEWER` as a spec-tested field**[^17_1]
The REVIEWER field existed in some discussions but was never in the Base Agent Template and was never spec-tested. T-12 makes the P8 invariant mechanically enforceable — Agent Spec QA cannot approve a template where an agent reviews itself, because the test fails unconditionally.

**3. Grammar-compliant lifecycle replacing pre-grammar patterns**[^17_2]
The example spec in file:7 used `feedlive`, `preflight_check`, `agentraiseuncertainty`, and `agentaction` — none of which exist in the grammar. The revised lifecycle uses only grammar v0.3 tool names, eliminating the gap between the grammar specification and what agent templates actually call.
<span style="display:none">[^17_3]</span>

<div align="center">⁂</div>

[^17_1]: agent-creation-policy-v0.1.md
[^17_2]: example-spec-preflight-check.md
[^17_3]: session-summary-20260303-a.md

---

# ok. we need to clarify here. we just confirmed that the idea of the mcp is to limit what the agent can read and write directly to file, so I don't believe that context cards, task specs should ever be in the file system.
The idea is to also limit what the agent needs to read or understand so there is less opportunity for it to get confused. It shouldn't care what zone it is in or what type of agent it is.
the previous agent design spec was written prior to the mcp pivot so it should not be drawn upon at all. we need to begin with first principles and consider the lessons on context engineering.

I've shared a great example of an agent spec that has subagents and very few instructions. And below is our approach to context engineering.

```


---
name: ArtsiX Site Builder
description: Orchestrates the full ArtsiX website update, plan, build, then review.
tools: ['agent']
agents: ['ArtsiX Planner', 'ArtsiX Developer', 'ArtsiX Reviewer']
handoffs:

- label: Plan this change
agent: ArtsiX Planner
prompt: Analyse the codebase and generate an implementation plan for the requested ArtsiX website update.
send: false
- label: Build it
agent: ArtsiX Developer
prompt: Implement the plan outlined above, following all ArtsiX design and copy rules.
send: false
- label: Review changes
agent: ArtsiX Reviewer
prompt: Review all modified files for brand compliance, accessibility, and performance.
send: false
---

You coordinate the ArtsiX website update workflow. For any request:

1. Hand off to **ArtsiX Planner** to research the codebase and produce a scoped plan.
2. Hand off to **ArtsiX Developer** to implement the plan.
3. Hand off to **ArtsiX Reviewer** to check compliance with the brief.

Never make code edits yourself, delegate to the appropriate subagent.

```

Context Engineering: Our Approach
Most people building AI agent systems make the same mistake: they assume that giving an agent more information produces better results. More context feels safer. It feels thorough. It feels like you're setting the agent up for success.

The research says the opposite is true.

Language models have a finite attention budget. Every token you add to a context window competes with every other token for that attention. When you load an agent with a detailed role description, architectural background, workflow guidance, and task instructions all at once, the model doesn't read it the way a human reads a briefing document — absorbing everything and prioritising accordingly. It distributes attention across the entire window, with a predictable curve: strong at the start, degrading through the middle, recovering slightly at the end. The instructions buried in the middle of a long agent file are the ones most likely to be missed.

This is called the lost-in-the-middle problem, and it means that a poorly structured 200-token agent file will produce worse outputs than a well-structured 50-token one — not because the longer file contains wrong information, but because it contains too much of it.


Context as a Finite Resource
The way we think about it: context is not free storage. It's more like working memory. A surgeon before an operation doesn't want every patient record in the hospital — they want this patient's chart, this procedure's notes, and the drug allergy list. More records don't make them a better surgeon. They increase the chance of grabbing the wrong detail at a critical moment.

Our agents operate on the same principle. Each agent gets the minimum information needed to do its specific job — and nothing else. Not because we're being restrictive, but because additional information actively degrades the quality of the work.


How We Scope Context
Every operation in our system has an explicit context window defined before we write a single instruction. We ask three questions for each one:

What does this agent need to read? Named files only, not categories.
What does this agent write? One artefact, one location.
What is this agent explicitly forbidden from reading? Because if it can reach it, it might load it.

This produces a tree — not a timeline — of scoped information packages. The Feature Orchestrator sits at the root and holds almost nothing: just file paths and gate conditions. Below it, each executor operation gets its own narrow window. The agent that defines a feature reads the accepted idea. The agent that writes acceptance criteria reads the feature spec. The agent that writes tests reads the acceptance criteria — and nothing upstream of it. Each node in the tree is isolated from the others.

The one exception is the Context Curation agent. Its job is compression: it receives everything a task could possibly need, and produces the minimum sufficient subset. Its input is intentionally larger than its output. That compressed package — and only that package — is what the Task Performer ever sees.


How We Structure Agent Instructions
If the content of agent instructions is one dimension of the problem, structure is the other. We write agent instructions the way you'd write a linter config, not the way you'd write a job description.

This is wrong:

You are a Test Writer Agent. Your role is to translate acceptance criteria into executable tests. You should carefully read the task acceptance criteria provided to you and produce a comprehensive test suite that covers all the conditions described. Make sure your tests are specific and verifiable.

This is right:

READS: task-ac.md only
WRITES: .framework/features/[slug]/tasks/[task-slug]/tests.md
FORMAT: Given/When/Then, one test per AC condition
NEVER: read feature-spec.md or parent AC

Same information. One quarter of the tokens. No prose for the model to pattern-match against when it should be focused on the task.

Critical rules go at the top of the file. Boundaries go at the bottom. Nothing important sits in the middle.


Progressive Disclosure and Caching
Not all context loads at startup. Agent files stay thin — just identity, tools, and pointers. When an agent encounters a task that requires deeper guidance, it loads the relevant skill file on demand. The skill file contains the substantive content: rubrics, templates, checklists, format specifications.

This matters for two reasons. First, it keeps the always-on context window small, so attention is concentrated on what actually matters for the current operation. Second, it enables prompt caching: content that stays identical across multiple invocations — skill files, instruction files, output conventions — can be cached by the model provider at roughly 10% of the normal token cost. An agent that processes eight tasks in sequence warms its cache on the first task and pays a fraction of full price for each subsequent one.

This is why our high-value curation agents — Context Agent, Test Writer, QA Reviewer — process all tasks in a feature as a sequential batch rather than being reinvoked fresh for each vertical slice. Same instructions, eight tasks, one cache warm.


What This Produces
An agent team designed this way has a counterintuitive quality: the orchestrators are the least intelligent-looking parts of the system. They hold almost no information. They route, gate, and pass paths. All the intelligence lives in the executor agents and their skills — narrow, purpose-built, precisely scoped.

The result is a system where each agent has nowhere to go except the task in front of it. No irrelevant context to pattern-match against. No architectural prose to weight against the actual instructions. No role description competing with the output format for attention.

Less context, better work. That's the principle. Everything else follows from it.

This is a significant and correct pivot. Everything that was just drafted needs to be substantially rebuilt. Let me work through this from first principles before producing any document.

***

## What the Pivot Changes

The old template treated the agent file as the governance document — it held READS, WRITES, NEVER, ZONE, TYPE, lifecycle blocks, and principle references. That was wrong for two reasons the context engineering section makes precise:

1. **Attention budget**: a 200-line agent file with embedded governance metadata competes for the same attention as the two lines that actually tell the agent what to do
2. **Separation of concerns**: governance metadata is for the FOA and QA system — the agent doesn't need to know it's `TYPE: EXECUTOR` or `ZONE: 4` to do its job

The MCP pivot makes the correct structure obvious: **tool possession is the capability declaration**. An agent's READS and WRITES are already expressed by the tools in its list. No separate declaration is needed.

***

## The Three-Layer Model

```

LAYER            LOCATION                    CONTENT                SIZE
──────           ────────                    ───────                ────

Agent File       .github/agents/             Identity + tools       < 15 lines
(VS Code layer)             + 1-2 line instruction

Universal        .github/instructions/       Startup sequence       < 30 lines
Instructions     (VS Code layer, always-on)  for all agents

Skill File       .github/skills/             Role-specific          As needed
(VS Code layer, on demand)  rubrics, formats,
checklists

Context Card     MCP: get_context_card       Min. sufficient        Composed
(Nexus MCP layer)           operational brief      per task
for this agent+task

──── NEVER SEEN BY AGENTS ──────────────────────────────────────────────────

Agent Class      .framework/agent-classes/   Governance metadata    Rich
Definition       (Nexus MCP layer)           READS, WRITES, NEVER,
ZONE, QA_TIER, etc.
Source for context
card generation

```

The agent only ever sees the top four layers. The agent class definition is consumed by the FOA, Context Agent, and Nexus server — never by the agent itself.

***

## New Base Agent Template

### `.github/agents/[agent-class].agent.md`

```yaml
---
name: [AgentClassName]
description: "[One sentence. What single artefact does this agent produce?]"
model: claude-sonnet-4-5
tools:
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - search_knowledge_base
  - raise_uncertainty
  # Task-scoped tools are populated here at activation time.
  # See get_my_capabilities for the live list.
---

Call `get_context_card` to load your brief.
If uncertain at any point, call `raise_uncertainty`. Never proceed silently.
```

That is the entire agent file. Thirteen lines. The instruction is two sentences. This is not spartan — it is complete. Everything the agent needs to do its job is either in its tools or will be delivered by `get_context_card`.

***

## What Moves Where

### Into `.github/instructions/nexus-agent.instructions.md` (universal, always-on)

The startup sequence that previously lived as a lifecycle block in every agent file:

```markdown
## Startup Sequence — All Agents

Every agent follows this sequence before role-specific work.
These are calls, not suggestions.

1. call get_context_card
   → contains your task brief, relevant patterns, and constraints
   → if CARD_NOT_FOUND: call raise_uncertainty immediately. Stop.
   → if stale: true: continue, note it in your first tool call.

2. call get_my_capabilities
   → verify the tools you need for this task are present.
   → if a required tool is missing: call raise_uncertainty. Stop.

3. call get_current_state
   → verify entity state matches what you expect before starting.
   → if wrong state: call raise_uncertainty. Stop.

4. call search_knowledge_base
   → query for patterns relevant to your task type.
   → zero results is valid — it is not a reason to skip this step.

5. Assess certainty against your threshold (in your context card).
   → CLEAR: proceed.
   → ASSUMED: note assumptions, proceed.
   → BLOCKED: call raise_uncertainty(severity='BLOCKED'). Stop.
      There is no override for BLOCKED.
```

This loads for every agent automatically. No agent file needs to repeat it.

### Into `.github/skills/[agent-class].skill.md` (role-specific, on demand)

Everything substantive about how to do the job: rubrics, output formats, checklists, examples, decision rules. Heavy. Cacheable. Loaded only when the agent needs it.

### Into `.framework/agent-classes/[agent-class].md` (governance, never loaded by agents)

All the metadata that was previously cluttering the agent file:

```markdown
# Agent Class: TaskPerformer

## Identity
ZONE: 4 Task Execution
TYPE: EXECUTOR
QA_TIER: 2
CERTAINTY_THRESHOLD: 0.8
REVIEWER: QAExecutionAgent
PRINCIPLES: P3, P6, P8, P9, P15
PATTERN_REF: pat-004

## Capability Declaration
# These are expressed as MCP tool names, not file paths.
# This is what activate_task uses to build the tool list.

READS_VIA:
  - read_task_spec_{task_id}
  - read_environment_contract_{task_id}

WRITES_VIA:
  - write_proof_template_{task_id}
  - append_work_log_{task_id}
  - submit_proof_{task_id}

NEVER_MCP:
  # No tool exists for these — structurally enforced by tool absence.
  - Any tool scoped to a different task_id
  - Any write_ tool targeting governance artefacts

NEVER_CONVENTION:
  # VS Code built-in tools could reach these.
  # Enforced by context card declaration + good-faith compliance.
  # Documented here honestly per platform-constraints.md Gap 1.
  - .framework/policies/**
  - .framework/agent-classes/**
  - .framework/features/<other-feature>/**

## Context Card Composition Rules
# What the Context Agent must include when generating a card for
# this agent class.
ALWAYS_INCLUDE:
  - Current task state
  - Task-scoped tool list for this instance
  - Certainty threshold (0.8)

PATTERN_TAGS: ['zone-4', 'executor', 'proof', 'task-execution']
MAX_PATTERNS: 7

## Reviewer Pairing
# P8: this agent's output is reviewed by QAExecutionAgent.
# QAExecutionAgent's output is reviewed by [different agent].
REVIEWER: QAExecutionAgent
```

This document is read by the Context Agent, the FOA, and Agent Spec QA. Never by the TaskPerformer itself.

***

## Revised Spec Tests

The spec tests split across two targets:

### Agent File Tests (enforced by Agent Spec QA on `.github/agents/`)

```
T-01  name is present and PascalCase
T-02  description is present and exactly one sentence
T-03  model field is present
T-04  tools list contains all five universal tools
T-05  file body is ≤ 15 lines excluding frontmatter
T-06  file contains no READS, WRITES, NEVER, ZONE, TYPE,
      or lifecycle blocks — these belong in the agent class
      definition, not the agent file
T-07  instruction text contains no more than 3 sentences
```


### Agent Class Definition Tests (enforced by Agent Spec QA on `.framework/agent-classes/`)

```
T-08  ZONE is present and valid
T-09  TYPE is present and valid
T-10  QA_TIER is present, integer 0–4
T-11  CERTAINTY_THRESHOLD is present, float 0.0–1.0
T-12  REVIEWER is present and does not equal name  ← P8 invariant
T-13  PRINCIPLES lists at least one P-ID
T-14  READS_VIA uses MCP tool name patterns, not file paths
T-15  WRITES_VIA contains at least one write_ or submit_ pattern
T-16  NEVER_MCP section is present and non-empty
T-17  NEVER_CONVENTION section is present and non-empty
      (honest documentation of Gap 1 from platform-constraints.md)
T-18  PATTERN_REF present on approved classes
T-19  REVIEWER pairing is registered in the Agent Pair Registry
      (no agent is an island — P8 requires a registered reviewer)
```


***

## The Concrete Outcome

A fully hydrated TaskPerformer for task-07 looks like this in VS Code:

**Agent file** (what VS Code loads):

```yaml
---
name: TaskPerformer
description: "Executes a single published task and produces proof of completion."
model: claude-sonnet-4-5
tools:
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - search_knowledge_base
  - raise_uncertainty
  - read_task_spec_task_07
  - read_environment_contract_task_07
  - write_proof_template_task_07
  - append_work_log_task_07
  - submit_proof_task_07
---

Call `get_context_card` to load your brief.
If uncertain at any point, call `raise_uncertainty`. Never proceed silently.
```

**What `get_context_card` returns** (what the agent actually works from):

```
You are implementing task-07: Add Redis session store to auth service.

Tools to call for information:
  - read_task_spec_task_07
  - read_environment_contract_task_07

Tool to submit your output:
  - submit_proof_task_07

Certainty threshold: 0.8

Relevant patterns:
  [pat-001] Write proof template before implementation begins.
  [pat-002] Do not review your own work — QAExecutionAgent reviews yours.

Constraints:
  - Use npm, not bun
  - Target Node 20 LTS
  - Branch must be task/task-07

Open flags: none
```

The agent has everything it needs. It knows nothing about zones, framework governance, QA tiers, or principle IDs. Those are not its concern.

---

# beautiful.

Perhaps I need to test that an agent can still access skills files without read access?
Also, let's begin to build in the use of subagents as they help restrict context requirements as well.
[https://code.visualstudio.com/docs/copilot/agents/subagents](https://code.visualstudio.com/docs/copilot/agents/subagents)

Two separate things here — one is a quick hypothesis to test, the other is a genuine architectural enhancement. Let me address both.

***

## 1. Skill File Access — Hypothesis to Test

Skills in `.github/skills/` are loaded by VS Code's host layer, not by any agent tool call. The hypothesis is that VS Code injects skill content into the agent's context window directly, the same way `.github/instructions/` files are injected — before any tool is called, without the agent needing read access .

This needs a concrete test before we design around it:

```markdown
# Hypothesis Card — H-SKILLS-01
## Skill Files Are Accessible Without Read Tools

**Hypothesis:**
An agent with zero read tools can access the full content of a
referenced skill file, because VS Code loads it at the host layer,
not via a tool call.

**Test:**
1. Create a minimal agent with only universal MCP tools (no read_,
   no VS Code built-in file tools)
2. Reference a skill in the instructions file via `#skill-name`
3. Ask the agent to describe what it knows about its task format
4. Inspect whether skill content appears in its response without
   any tool call in the audit log

**Pass condition:**
Agent accurately describes skill content. Zero read_ entries in
audit_log. No VS Code file tool calls visible in the trace.

**Fail condition:**
Agent cannot access skill content, OR accesses it via an unaudited
VS Code built-in read — meaning skill content loads but bypasses
the audit trail entirely.

**Why this matters:**
If PASS: skill files are a clean VS Code-layer delivery mechanism —
no tool needed, no audit gap, intentional by design.
If FAIL (access via built-in): we have an unaudited read path for
skill content that needs to be documented in platform-constraints.md
as Gap 5.
If FAIL (no access): skills must be delivered via get_context_card
instead, which changes the composition rules.

**Blocking:** No. Run as part of Experiment 02 setup.
```


***

## 2. Subagents — Architectural Integration

This is a significant upgrade. The VS Code subagent model maps directly onto the coordinator/executor split we already have, but now gives it structural teeth :

- Each subagent runs in its **own clean context window** — the coordinator never accumulates executor work
- The coordinator sees only the **final result**, not the intermediate steps
- Subagents can run **in parallel** — independent review perspectives, parallel QA passes
- `user-invokable: false` means executor agents are structurally inaccessible except through their designated coordinator

***

### Updated Agent Type Model

| Type | VS Code pattern | `user-invokable` | `tools` includes | Notes |
| :-- | :-- | :-- | :-- | :-- |
| `ORCHESTRATOR` | Coordinator with `agents:` list | `true` | `agent` + universals | Routes only, never executes |
| `EXECUTOR` | Subagent, clean context | `false` | Universals + task MCP tools | Receives only task prompt |
| `REVIEWER` | Subagent, clean context | `false` | Universals + read MCP tools only | Parallel review possible |
| `COMPRESSION` | Subagent, clean context | `false` | Universals + search + read | Context Agent pattern |


***

### Revised Base Agent Templates

**Orchestrator pattern:**

```yaml
---
name: Zone4Coordinator
description: "Coordinates task execution and QA for a single published task."
model: claude-sonnet-4-5
user-invokable: true
tools:
  - agent
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - search_knowledge_base
  - raise_uncertainty
agents:
  - TaskPerformer
  - QAExecution
---

Call `get_context_card` to load your brief, then delegate:
1. Hand off to **TaskPerformer** to implement and submit proof.
2. Hand off to **QAExecution** to review the proof.

Never implement or review yourself. If either subagent returns
uncertainty, call `raise_uncertainty` with the detail provided.
```

**Executor pattern (subagent only):**

```yaml
---
name: TaskPerformer
description: "Executes a single published task and produces proof of completion."
model: claude-sonnet-4-5
user-invokable: false
tools:
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - search_knowledge_base
  - raise_uncertainty
  # Task-scoped tools added at activation time
---

Call `get_context_card` to load your brief.
If uncertain at any point, call `raise_uncertainty`. Never proceed silently.
```

**Reviewer pattern — parallel subagents:**

This is where subagents really earn their place. Instead of one QA agent doing a sequential pass, the coordinator spawns focused reviewers in parallel :

```yaml
---
name: QAExecution
description: "Reviews proof of completion from multiple independent perspectives."
model: claude-sonnet-4-5
user-invokable: false
tools:
  - agent
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - raise_uncertainty
agents:
  - ProofCriteriaReviewer
  - AcceptanceCriteriaReviewer
  - EnvironmentContractReviewer
---

Call `get_context_card` to load your brief, then run subagents in parallel:
- **ProofCriteriaReviewer** — does the proof satisfy the template?
- **AcceptanceCriteriaReviewer** — does the implementation meet the AC?
- **EnvironmentContractReviewer** — is the environment state correct?

Synthesise all findings. If any reviewer returns a failure, call
`raise_uncertainty` with consolidated findings. Never pass a task
where any reviewer found a critical issue.
```

Each reviewer is `user-invokable: false`, has only `read_` tools for its specific documents, and runs with zero contamination from the others :

```yaml
---
name: ProofCriteriaReviewer
description: "Verifies that a proof document satisfies its proof template."
model: claude-sonnet-4-5
user-invokable: false
tools:
  - get_context_card
  - raise_uncertainty
  # read_proof_template_{task_id} and read_proof_{task_id}
  # added at activation time
---

Read the proof template and the submitted proof.
Return PASS with evidence, or FAIL with the specific unmet criteria.
Nothing else.
```


***

### What This Changes in the Framework

Three things need updating as a result of this:

- **`agent-creation-policy.md`** — add `user-invokable` and `agents:` as required fields for ORCHESTRATOR type; add parallel reviewer pattern as a named composition pattern
- **`platform-constraints.md`** — add a note in Part 2 that subagents have their own clean context windows, which means the "unscoped reads" gap is partially mitigated for subagents (a subagent that never receives a file path cannot accidentally load it)
- **Spec test T-06** — add: ORCHESTRATOR agents must declare `agents:` list; EXECUTOR and REVIEWER agents must have `user-invokable: false`

The skill file hypothesis (H-SKILLS-01) sits upstream of finalising skill delivery — run that test before locking the skill loading mechanism in the base template.

---

# Session Summary — 2026-03-03 (Afternoon)


***

## What We Produced

| Artefact | Path | Status |
| :-- | :-- | :-- |
| Platform Constraints | `.framework/policies/platform-constraints.md` | ✅ Complete |
| Tool Grammar v0.3 | `.framework/policies/tool-grammar.md` | ✅ Complete |
| Audit Log Schema | `.framework/schema/audit-log-schema.md` | ✅ Complete |
| Pattern Library Schema | `.framework/schema/pattern-library-schema.md` | ✅ Complete |
| Context Card Schema | `.framework/schema/context-card-schema.md` | ✅ Complete |
| Knowledge Pipeline | `.framework/schema/knowledge-pipeline.md` | ✅ Complete |
| Base Agent Template v0.2 | `.framework/templates/base-agent-template.md` | ✅ Complete (post-pivot) |
| H-SKILLS-01 Hypothesis Card | Experiment backlog | ✅ Drafted |


***

## What We Decided

**Named Decisions (for manifest):**

- **D-005** — Edit tool is binary. MCP is the only available access control boundary. All non-code writes go through MCP tools.
- **D-006** — Skill and instruction files live in the VS Code layer. Governance is Zone 0 process + Git, not Nexus audit entries.
- **D-007** — Unscoped VS Code built-in reads are an accepted platform gap. Documented honestly, not papered over.
- **D-008** — Agent identity is expressed through tool possession, not tokens. OCAP is structurally stronger than any auth layer we could add.
- **D-009** — `read_` and `search_` verbs produce audit entries (grammar v0.3). The v0.2 distinction between "mutable state" and "versioned documents" was insufficient — version numbers record what a document contained, not who read it or when.
- **D-010** — Agent files are ≤15 lines. Governance metadata lives in `.framework/agent-classes/`, never in the agent file itself.

**Deferred (recorded as Future Directions):**

- **F-001** — ONE Ontology as software design standard. Trigger: first real project scoped through Zone 0.

***

## Derivation Order Status

| Step | Deliverable | Status |
| :-- | :-- | :-- |
| 1 | Tool Grammar v0.3 | ✅ Done |
| 2 | Knowledge Structures | ✅ Done |
| 3 | Base Agent Template | ✅ Done |
| 4 | Work Lifecycle (zone policies) | ⬅ Next |
| 5 | Governance Policies | Pending |
| 6 | Infrastructure Build (Exp-02) | Pending |


***

## Retrospective

### What Went Well

**The grammar changes were evidence-driven, not opinion-driven.**
Every change in v0.3 had a precise justification: `read_` and `search_` were missing audit entries, and the cost of that gap was demonstrable with a concrete query (Q2, Q3) that would return zero rows without the change. That is the right way to evolve the grammar.

**The audit schema's canonical queries are good acceptance criteria.**
Writing the eight canonical queries before finalising the schema forced the schema to be designed for its actual use cases. Q2 ("what was the agent reading before it made this decision?") would have been impossible without the grammar v0.3 change — that dependency was discovered during schema design, not after.

**The knowledge pipeline holds together.**
Knowledge base → Pattern Library → Context Card is a mechanically executable pipeline with one human judgment point (FOA promotion). Everything else is structural. That's the right shape.

**The context engineering pivot was clean.**
Once the principle was stated precisely — attention is finite working memory, not free storage — the correct agent structure followed immediately. The revised base template is roughly one-tenth the size of the first draft and contains more useful information.

***

### What Didn't Go Well

**The base agent template was drafted against the wrong model.**
We drafted v0.2 drawing on `file:7` (the pre-MCP example spec) before the context engineering principles were applied. The result was a 200-line governance document masquerading as an agent file. It had to be substantially rebuilt. The lesson: establish the model before drafting artefacts that depend on it. The platform constraints and context engineering documents should have been reviewed first.

**The inline code fence problem.**
The pattern library and context card schemas were delivered as one document with nested code fences, which broke rendering. This is a recurring structural issue — any document that contains both markdown and code blocks needs to be split before delivery, not after. The rule going forward: if a document has a natural named split (as called out by its own headings), deliver it as separate files.

**We drew on superseded sources too early.**
Several rounds of the base agent template work pulled from the pre-MCP agent specs (file:7, file:9) before explicitly flagging them as superseded. The retro from Exp-01 contains useful architectural findings, but the agent templates and lifecycle blocks from those files are pre-grammar, pre-context-engineering, and should have been set aside at the start of the agent design step.

***

### What to Carry Into the Next Session

- **Run H-SKILLS-01 first.** Skill file access via VS Code host layer needs to be confirmed before the next agent templates are written. This is a small test that unblocks a structural question.
- **Zone policies (Step 4) are next.** The work lifecycle needs state machine definitions, zone entry and exit conditions, and the gate policy for each zone boundary.
- **Subagent integration flows back into `agent-creation-policy.md`.** The `user-invokable`, `agents:`, and parallel reviewer patterns are not yet in the creation policy. They need to be before any new agent class is designed.
- **Spec tests T-06 update** — add `user-invokable: false` requirement for EXECUTOR and REVIEWER types.
- **Manifest needs D-005 through D-010** entered before the next session begins.

***

Good session. The framework now has its foundational layer — constraints documented, grammar locked, schemas defined, agent model rebuilt on correct principles. Zone policies next.

---

# do we need to update the context card schema and other knowledge structure documents?

Yes — three specific things in the context card schema are now wrong, and one thing in the pattern library schema needs a minor update.

***

## What's Wrong and Why

### Context Card Schema — three issues

**1. The `permissions` block is redundant and wrong**
The card declared `reads`, `writes`, and `never` as file paths. That model is pre-MCP-pivot. The agent's permissions are expressed by its tool list — it doesn't need a separate declaration. Worse, file paths in the card give the agent information that invites it to reach for VS Code built-in reads rather than MCP tools.

**Replace with:** a `tools_guidance` block — plain English pointers to *which tool to call for what*, not file paths.

**2. `zone`, `actor_type`, `card_version`, `generated_by`, `generated_at` are governance metadata, not operational context**
The agent doesn't need to know it's in Zone 4, or that its card is v3, or that the Context Agent generated it. Those fields are for the FOA and the audit log, not for the agent's attention window. Per the pivot: the agent shouldn't care what zone it's in.

**Replace with:** nothing — move these to the governing metadata stored in the DB record, not delivered to the agent.

**3. `active_policies` block sends the wrong signal**
Listing policy document paths tells the agent "go read these policies." That's the opposite of what context engineering requires. Relevant policy constraints should already be distilled into the `constraints` block. The policy reference is for the FOA to verify composition, not for the agent to receive.

**Replace with:** constraints only — the distilled outputs of policy, not the policy references themselves.

***

### Pattern Library Schema — one issue

The `agent_classes` field uses agent class names to determine which agents receive a pattern. With the subagent model, a `QAExecution` coordinator and a `ProofCriteriaReviewer` subagent are different classes with different context needs — a pattern relevant to the coordinator may not be relevant to the reviewer and vice versa. The field needs to distinguish between coordinator and subagent targets.

**Update:** add `agent_type` filter alongside `agent_classes` so the Context Agent can compose appropriately narrow cards for subagents.

***

## Updated Context Card Schema

The delivered card — what `get_context_card` actually returns to the agent:

```typescript
type ContextCard = {

  // ── Task Brief ────────────────────────────────────────
  // This is what the agent is here to do.
  // Plain English. One paragraph maximum.
  task_brief: string

  task_id:    string | null   // "task-07" | null for role-level cards
  feature_id: string | null

  // ── Tools Guidance ────────────────────────────────────
  // Which tool to call for what. Not file paths.
  // Mirrors the agent's tool list but with purpose stated.
  tools_guidance: ToolGuidance[]

  // ── Certainty Threshold ───────────────────────────────
  // Declared per agent class in the agent class definition.
  // Delivered here so the agent has it without needing any
  // other document.
  certainty_threshold: number   // 0.0–1.0

  // ── Patterns ──────────────────────────────────────────
  // Validated patterns relevant to this agent+task.
  // Max 7 total (composition rules unchanged).
  patterns:      PatternEntry[]
  anti_patterns: PatternEntry[]   // surfaced separately, always visible

  // ── Constraints ───────────────────────────────────────
  // Distilled from policies — the agent receives the rule,
  // not the policy document path.
  // e.g. "Use npm, not bun"
  //      "Target Node 20 LTS"
  //      "Branch must be task/task-07"
  constraints: string[]

  // ── Open Flags ────────────────────────────────────────
  // Conflicts, known gaps, pattern exclusions.
  // The agent needs to know these before starting.
  open_flags: OpenFlag[]
}

type ToolGuidance = {
  tool_name: string       // exact MCP tool name
  use_for:   string       // "Read your task specification"
                          // "Submit your completed proof"
                          // "Log significant steps"
}

type PatternEntry = {
  pattern_id:        string
  pattern_name:      string
  current_nv:        number
  summary:           string   // max 3 sentences
  relevance_reason:  string   // why included for this agent+task
}

type OpenFlag = {
  flag_type:   'CONFLICT' | 'GAP' | 'KNOWN_UNCERTAINTY' | 'EXCLUSION'
  description: string
  source:      string
}
```


***

## What Moves to the DB Record Only

These fields are stored in the `documents` table entry for the card — available to the FOA and Context Agent via `read_context_card`, but never delivered to the agent:

```typescript
type ContextCardMetadata = {
  agent_class:    string
  agent_instance: string
  card_version:   string
  card_hash:      string
  generated_at:   string
  generated_by:   string   // always "context-agent"
  valid_until:    string | null
  stale:          boolean
  zone:           string   // governance use only
  source_pattern_ids: string[]
  source_policy_ids:  string[]
}
```

The agent receives `ContextCard`. The FOA and audit system work with `ContextCard + ContextCardMetadata`. The split is enforced by what `get_context_card` returns vs what `read_context_card` returns.

***

## Updated Pattern Library — `agent_type` Filter

Change the `agent_classes` field in the `patterns` table:

```sql
-- existing
agent_classes TEXT NOT NULL,  -- JSON: ["task-performer", "qa-execution"]

-- updated
agent_classes TEXT NOT NULL,  -- JSON: ["task-performer", "qa-execution"]
agent_types   TEXT NOT NULL   -- JSON: ["EXECUTOR", "REVIEWER", "*"]
                              -- "*" = all types within the listed classes
```

And update the Context Agent composition rule:

```
SUBAGENT CARD RULE:
If agent_type == REVIEWER or the agent is user-invokable: false,
apply stricter filtering:
  - Include ONLY patterns tagged for this agent's specific micro-task
  - Max 3 patterns (not 7) — subagent context windows must stay narrow
  - Anti-patterns: include only if tagged for this specific agent_class
  - Constraints: include only constraints directly relevant to this
    agent's output, not the parent coordinator's full constraint set
```


***

The stale card detection logic and the `.index.md` auto-generation are unchanged — those don't depend on what fields the card delivers to the agent.

---

# I personall ran the H-SKILLS-01 experiment and it passed! This is the agent file I created and asked it to create a skill for writing html5 base template. It access the 'skill-writing' skill in the skills library without requiring access to the `read` tool.


---
name: Skillful Agent
description: Can access skills without read access
tools: [edit/createDirectory, edit/createFile, edit/editFiles]
---

You are an expert at writing skills for VSCode copilot agents.

Excellent result. Clean pass with a minimal agent — no read tools at all, just edit tools and two lines of instruction. Here is what this confirms and what it changes.

***

## H-SKILLS-01 Result

```markdown
# H-SKILLS-01 — PASS
**Date:** 2026-03-04
**Tested by:** FO (manual)

**Finding:**
VS Code injects skill file content at the host layer before the agent
runs. No read tool is required. No MCP tool call is made. The agent
receives skill content regardless of what tools it holds.

**Evidence:**
Agent with only edit tools (no read_, no get_, no VS Code built-in
file read) successfully accessed and applied 'skill-writing' skill
content when asked to produce a skill file.

**Implication for audit:**
Skill reads produce no audit_log entry. This is not a gap — it is
correct behaviour. Skills are role knowledge (how to do the job),
not task data (what this specific task requires). The audit log
records decisions and outputs, not the professional knowledge the
agent applies to make them. A surgeon's training doesn't appear
in the operation notes.

**Status:** Confirmed architectural property. Not a gap.
```


***

## What This Resolves

This closes the one remaining uncertainty in the three-layer model. The layers are now fully confirmed:

```
LAYER               DELIVERY MECHANISM          AUDIT COVERAGE
─────               ──────────────────          ──────────────

Agent file          VS Code reads from          None needed —
                    .github/agents/             identity only

Instructions        VS Code injects             None needed —
                    always-on                   startup rules only

Skills              VS Code injects             None needed —
                    at host layer               role knowledge

Context Card        MCP: get_context_card       ✅ Full — every
                    (Nexus layer)               fetch recorded

Task documents      MCP: read_{doc}_{task}      ✅ Full — every
                    (Nexus layer)               read recorded

Governance          MCP: read_ tools            ✅ Full
artefacts           (Nexus layer, FOA only)
```

The split is clean: **role knowledge** (skills, instructions) is delivered by VS Code with no audit overhead. **Task-specific data** (context cards, documents) is delivered by MCP with full audit coverage. This is the right separation — auditing a skill read would be like auditing every time a developer consulted a style guide.

***

## What Needs Updating

**`platform-constraints.md`** — the skill delivery mechanism should be added to Part 1 as a confirmed property, not a hypothesis:

```markdown
### Skill Files Are Injected by the VS Code Host Layer

VS Code loads skill files referenced in agent configurations and
injects their content into the agent's context before execution.
This does not require the agent to hold any read tool and produces
no audit entry.

**Consequence (positive):** Skills are a clean, zero-overhead
delivery mechanism for role knowledge. Agent files stay thin.
Context cards stay focused on task data, not general capability.
The edit tool restriction (no read tools on executor agents) does
not prevent skill access.

**Consequence for audit design:** Skill reads are intentionally
unaudited. This is correct by design — skills are stable role
knowledge, not task-specific decisions. The audit log records
what the agent decided and produced, not the professional
knowledge it applied.

**Confirmed:** 2026-03-04, H-SKILLS-01, manual test by FO.
```

**Base agent template** — the `SKILL:` reference in the agent class definition is confirmed correct as a pointer only. Add one line to the spec test:

```
T-22  SKILL field in agent class definition references a file that
      exists at .github/skills/[skill-name].skill.md
      NOTE: VS Code delivers this — no read tool required or permitted.
      A read_ tool for a skill file is a spec test failure.
```

**Context card composition rules** — remove any remaining temptation to include skill content in the card. Add explicitly:

```
NEVER include skill content in context cards.
Skills are delivered by VS Code independently.
Duplicating skill content in the card wastes attention budget
and creates a maintenance sync problem.
```


***

## What This Means for Subagent Design

This is particularly good news for the parallel reviewer subagents. A `ProofCriteriaReviewer` with only two MCP read tools and a focused review skill can now be fully specified:

```yaml
---
name: ProofCriteriaReviewer
description: "Verifies that a submitted proof satisfies its proof template."
model: claude-sonnet-4-5
user-invokable: false
tools:
  - get_context_card
  - raise_uncertainty
  - read_proof_template_task_07
  - read_proof_task_07
---

Call `get_context_card`. Review proof against template criteria.
Return PASS with evidence, or FAIL with specific unmet criteria.
```

The review rubric — what good looks like, what failure looks like, the output format — lives in the `proof-criteria-reviewer.skill.md` file and is injected by VS Code. The agent file itself stays at eight lines. Context window for this subagent: one context card, two documents, one skill. Exactly what it needs and nothing else.

---

# I am starting today with a fresh mind and will shortly want to go back to looking at the derivations with you. But first I think it might be wise to establish naming conventions for the elements of the framework. Would this be in a style guide? or is that somethign different?

Good instinct to establish this before going back to the derivations — naming conventions are P12 (load-bearing), not cosmetic. But it is worth distinguishing what you're asking for from what a style guide covers, because they're two different documents serving different purposes.

***

## Naming Conventions vs Style Guide

|  | **Naming Conventions** | **Style Guide** |
| :-- | :-- | :-- |
| **Governs** | Technical identifiers — IDs, file names, tool names, table names, event names | Prose — tone, sentence structure, heading format, description writing rules |
| **Consequence of violation** | Audit log parsing breaks, tool registration fails, VS Code can't find files | Documents are inconsistent, harder to read |
| **Priority** | Now — the schema and tooling depend on it | Later — once there's enough prose content to make editorial decisions meaningful |
| **Examples** | `task-07`, `pat-001`, `TaskPerformer`, `read_task_spec_task_07` | "Descriptions are one sentence in active voice", "Headings are title case" |

**The naming conventions are structural — they belong in `.framework/policies/naming-conventions.md`.** The style guide is editorial — it can wait until the framework has enough written content to make the patterns visible.

***

## What the Naming Conventions Document Needs to Cover

There are six identifier families, each with a different format for a reason:

**1. Entity IDs** — kebab-case with type prefix and zero-padded number

```
task-07       feat-003      unc-001
pat-004       kb-012        exp-01
```

Why kebab-case: these appear in URLs, branch names, and tool suffixes. Underscores in tool suffixes are the delimiter — hyphens in IDs prevent parsing ambiguity.

**2. File names** — kebab-case, typed suffix

```
task-spec.md                  proof-of-completion.md
task-performer.skill.md       task-performer.context-card.md
task-performer-task-07.agent.md
naming-conventions.md
```

Why: VS Code filesystem discovery, consistent `find` and glob patterns.

**3. Agent class names** — PascalCase, no spaces or hyphens

```
TaskPerformer     QAExecution     ContextAgent
ProofCriteriaReviewer     Zone4Coordinator
```

Why: appears in the audit log `actor` field — PascalCase is unambiguous when extracted from strings. Also matches VS Code agent name conventions.

**4. Agent instance identifiers** (audit log `actor` field)

```
task-performer:task-07        qa-execution:task-07
foa                           context-agent
webhook:github                human:fo
system:nexus
```

Why: `class:scope` format makes actor type and task scope parseable by splitting on `:`.

**5. MCP tool names** — already governed by the grammar

```
read_task_spec_task_07        submit_proof_task_07
get_context_card              raise_uncertainty
```

The grammar document is the single source of truth. The naming conventions document references it, doesn't duplicate it.

**6. Database identifiers** — snake_case, plural tables

```
audit_log     stream_events     pattern_evidence
doc_version_hash     task_id     created_at
```

Why: SQL convention, consistent with SQLite practices.

**7. Branch names** — type prefix + entity ID

```
task/task-07          feat/feat-003
framework/exp-02      fix/task-07-auth
```

Why: parsed by the webhook handler — the prefix determines routing in `webhook-parser.ts`.

***

## Recommendation

Start with `.framework/policies/naming-conventions.md` today, before going back to the derivations. It's a short document — two hours of work — and it will catch naming inconsistencies across everything we've produced so far (there are a few). Once it exists, every new artefact has a checklist to validate against.

The style guide can emerge naturally later once there are five or six documents to look across and the prose patterns become visible.

Shall we write it now?

---

# yes. My only note on what you recommended above, is that I'd like agent names to be a 'do-er' word. eg QAExecution -> QAExecutor, ContextAgent -> ContextOwner (?) or ContextCurator

Good rule. It enforces that every agent name answers the question *"what does this agent actively do?"* rather than *"what is it?"* The difference between `ContextAgent` (a thing) and `ContextCurator` (a doer) is the difference between a job title and a job description.

***

## The Rule

```
Agent class names are PascalCase compound nouns where the final
component is a doer word — a noun derived from a verb describing
the agent's primary action.

Valid doer words: Performer, Executor, Curator, Reviewer,
Coordinator, Validator, Designer, Author, Composer, Deployer,
Orchestrator, Broker

Not valid: Agent, Manager, Handler, Processor, Worker
(too generic — they describe a category, not an action)

Borderline — decide case by case: Owner, Steward, Guardian
(imply responsibility but not active execution)
```


***

## Full Agent Name Roster — Proposed

| Current name | Proposed | Confidence | Question |
| :-- | :-- | :-- | :-- |
| TaskPerformer | **TaskPerformer** | ✅ Settled | Already a doer |
| QAExecution | **QAExecutor** | ✅ Settled | User confirmed |
| ContextAgent | **ContextCurator** | ✅ Settled | User confirmed |
| AgentTemplateCreator | **TemplateAuthor** | 🟡 Propose | Creator → Author (Author implies intentional composition, not just creation) |
| AgentSpecQA | **SpecValidator** | 🟡 Propose | QA is a department, Validator is a doer |
| QADefinition | **ProofDesigner** | 🟡 Propose | Their actual job is designing the proof template and AC — Designer fits |
| UncertaintyOwnerAgent | **UncertaintyBroker** | 🟡 Propose | Brokers between blocked agents and resolution — Owner is passive |
| FrameworkOwnerAgent (FOA) | **FrameworkSteward** | 🔴 Uncertain | FOA is an established acronym — worth discussing before renaming |
| Zone4Coordinator | **TaskCoordinator** | 🟡 Propose | Zone numbers shouldn't be in names (agents don't know their zone) |
| ProofCriteriaReviewer | **ProofReviewer** | 🟡 Propose | Criteria is implied by the role |
| AcceptanceCriteriaReviewer | **ACReviewer** | 🟡 Propose | Abbreviate the domain prefix |
| EnvironmentContractReviewer | **EnvironmentReviewer** | 🟡 Propose | Same pattern |
| CICDAgent | **Deployer** | 🟡 Propose | Clean single doer word |
| UIDesignAgent | **UIDesigner** | ✅ Clear | Direct equivalent |


***

## The FOA Question

This one deserves a deliberate decision rather than a mechanical rename. `FrameworkOwnerAgent` has an established acronym (FOA) that appears throughout the audit log, manifest, and policy documents already. Three options:

- **FrameworkSteward** — accurate (stewards the health of the framework), but loses the FOA acronym
- **FrameworkOrchestrator** — doer word, but `Orchestrator` is already an agent `TYPE` which creates a naming collision
- **Keep FrameworkOwner** — acknowledge `Owner` as an accepted exception for agents that hold write authority over a domain (consistent with `FeatureOwner`, `TaskOwner`, `UncertaintyOwner` if we keep that pattern)

The third option has merit — `Owner` could be a deliberate carve-out for agents that hold **authority** rather than just **capability**. That would make `Owner` a meaningful signal in the name: this agent can approve, reject, and gate — not just execute.

***

## Proposed Owner Exception

If you adopt the third option, the rule becomes:

```
Valid doer words: Performer, Executor, Curator, Reviewer,
Coordinator, Validator, Designer, Author, Composer, Deployer,
Orchestrator, Broker

Authority agents only: Owner
Reserved for agents that hold gate authority over a domain.
Must be justified in the agent class definition.
Current valid uses: FrameworkOwner, FeatureOwner, TaskOwner,
UncertaintyOwner
```

This keeps FOA intact, gives `UncertaintyOwner` a clean justification, and creates a readable signal — any agent named `*Owner` has approval authority that `*Executor` agents do not.

What's your call on the FOA and the `Owner` exception?

---

# Let's change FOA to FrameworkOwner and I accept the Owner exception.

The human will need a new name since that was FO, perhaps HumanApprover (HA).
And should we find a way to indicate an agent is an orchestrator or a subagent within the name? Or perhaps it is easier if all agents are expected to be a subagent unless they have Orchestrator as part of their name?

Clean decisions. Let me work through the implications before producing the conventions document, because the orchestrator naming rule has a useful structural consequence.

***

## The Naming Signal Model

```
Name pattern          user-invokable    agent type
────────────────────────────────────────────────────
*Orchestrator         true              Coordinates workflow,
                                        delegates to subagents

*Owner                true              Holds gate authority,
                                        approves/rejects/halts

Everything else       false             Subagent, clean context
                                        window, never invoked
                                        directly by the user
```

This makes `user-invokable` derivable from the name — it becomes a spec test, not a judgment call:

```
T-xx  If name ends in neither 'Orchestrator' nor 'Owner',
      user-invokable must be false (or absent, which defaults
      to false in VS Code).
```

**Owner agents are implicitly user-invokable** because they make gate decisions that require direct human-facing interaction. A `FrameworkOwner` that couldn't be invoked directly couldn't fulfill its authority function.

***

## The Human Actor

`HumanApprover` works well for the audit log actor field — in the system, the human's recorded actions are almost exclusively gate approvals and halts. For the one place where the human acts as a strategic director (framework decisions, session work), the actor field can carry a qualifier:

```
Audit log actor values:
  human:approver        ← gate approvals, halt commands
  human:director        ← framework-level decisions recorded
                           manually (retros, manifest entries)
```

Both share the `human:` prefix so queries across all human actions still work with `WHERE actor LIKE 'human:%'`.

The acronym `HA` works for internal shorthand the same way `FO` did.

***

## Revised Full Roster

| Agent name | Type | user-invokable | Replaces |
| :-- | :-- | :-- | :-- |
| `FrameworkOwner` | Owner | ✅ | FOA / FrameworkOwnerAgent |
| `FeatureOwner` | Owner | ✅ | FeatureOwner |
| `TaskOwner` | Owner | ✅ | TaskOwner |
| `UncertaintyOwner` | Owner | ✅ | UncertaintyOwnerAgent |
| `TaskOrchestrator` | Orchestrator | ✅ | Zone4Coordinator |
| `DeliveryOrchestrator` | Orchestrator | ✅ | Zone5Coordinator / CICDAgent |
| `TaskPerformer` | Subagent | ❌ | TaskPerformer |
| `QAExecutor` | Subagent | ❌ | QAExecution |
| `ContextCurator` | Subagent | ❌ | ContextAgent |
| `TemplateAuthor` | Subagent | ❌ | AgentTemplateCreator |
| `SpecValidator` | Subagent | ❌ | AgentSpecQA |
| `ProofDesigner` | Subagent | ❌ | QADefinition |
| `Deployer` | Subagent | ❌ | CICDAgent |
| `UIDesigner` | Subagent | ❌ | UIDesignAgent |
| `ProofReviewer` | Subagent | ❌ | ProofCriteriaReviewer |
| `ACReviewer` | Subagent | ❌ | AcceptanceCriteriaReviewer |
| `EnvironmentReviewer` | Subagent | ❌ | EnvironmentContractReviewer |


***

Now the full naming conventions document:

***

## `.framework/policies/naming-conventions.md`

```markdown
# Naming Conventions

**Version:** 0.1
**Status:** Active
**Principles implemented:** P12
**Last Updated:** 2026-03-04

---

## Purpose

Names in this framework are structural elements, not labels.
They are parsed by the audit log, the webhook handler, the MCP
server, and VS Code. A naming violation is a defect, not a
style preference.

Every identifier family has a format, a reason for that format,
and a spec test. No identifier may deviate from its family's
format without a framework-level decision recorded in the manifest.

---

## 1. Agent Class Names

**Format:** PascalCase. Final component must be a doer word.

```

TaskPerformer     ContextCurator     TemplateAuthor
QAExecutor        SpecValidator      ProofDesigner
TaskOrchestrator  FeatureOwner       UIDesigner
Deployer          ProofReviewer      ACReviewer

```

**Doer word vocabulary:**

| Word | Meaning | Example |
|---|---|---|
| Performer | Executes the primary task work | TaskPerformer |
| Executor | Runs a defined procedure | QAExecutor |
| Curator | Selects, composes, and maintains | ContextCurator |
| Reviewer | Independently verifies output | ProofReviewer |
| Validator | Checks conformance against spec | SpecValidator |
| Author | Writes a composed artefact | TemplateAuthor |
| Designer | Defines what done looks like | ProofDesigner |
| Deployer | Executes delivery to environment | Deployer |
| Orchestrator | Coordinates workflow via subagents | TaskOrchestrator |
| Owner | Holds gate authority over a domain | FeatureOwner |

**Owner exception:**
`Owner` is reserved for agents that hold approval/rejection/halt
authority over a domain. It is not a generic suffix. Every Owner
agent must declare its gate authority in its agent class definition.
Current valid Owner agents: FrameworkOwner, FeatureOwner,
TaskOwner, UncertaintyOwner.

**Prohibited suffixes:**
`Agent`, `Manager`, `Handler`, `Processor`, `Worker` — too generic,
describe a category not an action. Any existing name using these
must be renamed on next revision.

**Spec test:**
- Name is PascalCase with no spaces, hyphens, or underscores
- Final component is in the doer word vocabulary or is `Owner`
- If name does not end in `Orchestrator` or `Owner`,
  `user-invokable` must be `false` in the agent file

---

## 2. Human Actor Identifiers

The human is not an agent but appears as an actor in the audit log.

**Format:** `human:{role}`

```

human:approver     Gate approvals, halt commands, publish decisions
human:director     Framework-level decisions, retro entries,
manifest updates made in session

```

**Shorthand:** HA (HumanApprover) in prose and session notes.

**Spec test:**
- Any audit row with `actor_type = 'human'` must use one of
  the declared role values above
- New human role values require a naming conventions update

---

## 3. Entity IDs

**Format:** `{type}-{zero-padded-number}`

```

task-07       feat-003      unc-001
pat-004       kb-012        exp-01

```

**Type prefix vocabulary:**

| Prefix | Entity |
|---|---|
| `task` | Task |
| `feat` | Feature |
| `unc` | Uncertainty |
| `pat` | Pattern Library entry |
| `kb` | Knowledge Base entry |
| `exp` | Experiment |

**Padding rule:** Two digits minimum (`task-07` not `task-7`).
Expand to three digits when count exceeds 99 (`task-100` not
`task-99a`).

**Why hyphens, not underscores:**
Entity IDs appear in branch names, MCP tool suffixes, and URLs.
Underscores are the delimiter in tool names — using underscores
in IDs creates parsing ambiguity when extracting task ID from
`read_task_spec_task_07`. Hyphens produce an unambiguous split.

---

## 4. File Names

**Format:** kebab-case with typed suffix.

**Agent files:**
```

task-performer.agent.md
task-performer-task-07.agent.md    ← instance with task suffix
framework-owner.agent.md

```

**Skill files:**
```

task-performer.skill.md
proof-reviewer.skill.md
context-curator.skill.md

```

**Context card files** (VS Code layer copy):
```

task-performer.context-card.md
task-performer-task-07.context-card.md

```

**Instruction files:**
```

nexus-agent.instructions.md
nexus-startup.instructions.md

```

**Framework document files:**
```

naming-conventions.md
platform-constraints.md
audit-log-schema.md
pattern-library-schema.md

```

**Agent class definition files** (governance, not VS Code layer):
```

task-performer.agent-class.md
framework-owner.agent-class.md

```

**Derivation rule for agent class → file name:**
PascalCase agent class name → kebab-case file name stem.
```

TaskPerformer      → task-performer
ContextCurator     → context-curator
TaskOrchestrator   → task-orchestrator
ProofDesigner      → proof-designer

```

**Spec test:**
- All file names are lowercase
- Word separator is hyphen only — no underscores in file names
- Suffix is always `.{type}.md` for typed files
- No spaces, no uppercase characters

---

## 5. MCP Tool Names

Governed entirely by `.framework/policies/tool-grammar.md`.
This document does not duplicate that specification.

**Cross-reference rule:**
Tool names use underscores as word separators and component
delimiters. This is the only identifier family that uses
underscores — all others use hyphens. This distinction is
intentional and load-bearing: it makes tool names
unambiguously parseable.

---

## 6. Database Identifiers

**Format:** snake_case. Table names are plural nouns.

**Tables:**
```

audit_log          stream_events       documents
tasks              tool_registry       patterns
pattern_evidence   knowledge_base

```

**Column names:**
```

task_id            created_at          doc_version_hash
actor_type         source_audit_id     content_hash
agent_class        entry_hash          result_count

```

**Rules:**
- All lowercase
- Word separator is underscore
- No abbreviations except established ones:
  `id`, `ref`, `hash`, `ac`, `nv`, `br`
- Foreign key columns: `{referenced_table_singular}_id`
  e.g. `pattern_id`, `audit_id`, `task_id`

---

## 7. Branch Names

**Format:** `{type}/{entity-id}`

```

task/task-07          feat/feat-003
framework/exp-02      fix/task-07-auth

```

**Type prefix vocabulary:**

| Prefix | When to use |
|---|---|
| `task/` | Task implementation branch |
| `feat/` | Feature branch (spans multiple tasks) |
| `framework/` | Framework evolution, experiments |
| `fix/` | Hotfix or correction |

**Parsing rule:**
The webhook handler splits on `/` to extract branch type, then
extracts entity ID from the second component. Branch names that
do not follow this format will not be attributed to a task in
the audit log.

---

## 8. Actor Identifiers (Audit Log)

**Format varies by actor type.**

**Agents:**
```

{kebab-agent-class}:{task-id}    task-performer:task-07
{kebab-agent-class}              framework-owner
context-curator

```

Agent class names in the actor field use kebab-case derived
from the PascalCase class name (same derivation rule as file names).

**Humans:**
```

human:approver
human:director

```

**Webhooks:**
```

webhook:github

```

**System:**
```

system:nexus
system:policy-engine

```

**Query pattern:** All actors of a given type share a common
prefix. `WHERE actor LIKE 'human:%'` returns all human actions.
`WHERE actor LIKE 'webhook:%'` returns all external events.
This is load-bearing — do not deviate from the prefix model.

---

## 9. Stream Event Text

Stream events are plain English. No format rules — they are
written for the human reader (HA). One style rule only:

**Past tense, active voice, agent named first.**
```

✅  TaskPerformer submitted proof for task-07.
✅  FrameworkOwner approved publication of feat-003.
✅  UncertaintyOwner blocked task-07 — Redis dependency unresolved.

❌  Proof submitted.
❌  task-07 was blocked by UncertaintyOwner.
❌  The TaskPerformer agent has completed its proof submission.

```

---

## Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-03-04 | Initial. All seven identifier families defined. |
```


---

# Excellent. Going back to derivations.

I want to start at the beginning as yesterday's late updates were given in piecemeal and I'm afraid I didn't update the files correctly. There's a chance the naming conventions might have created a need to update anyway.

the first files we created was the tool-grammar and audit-log-schema
Please write these for me again

Good call — let me regenerate these from first principles with naming conventions applied and yesterday's final state incorporated.

***

## `.framework/policies/tool-grammar.md`

```markdown
# Nexus Tool Grammar — Reference Specification

**Version:** 0.3
**Status:** Active
**Principles implemented:** P3, P4, P5, P12, P16
**Platform constraint reference:** .framework/policies/platform-constraints.md
**Naming conventions reference:** .framework/policies/naming-conventions.md
**Last Updated:** 2026-03-04

---

## Version History

| Version | Date | Change | Principle |
|---|---|---|---|
| 0.1 | 2026-03-01 | Initial grammar. All verbs defined. Tool Matrix established. | P3, P4, P12 |
| 0.2 | 2026-03-02 | `get_` promoted to audit-writing verb. Rationale: system state reads must be traceable. Discovered via H5 chain-of-custody test. | P5 partial |
| 0.3 | 2026-03-03 | `read_` and `search_` promoted to audit-writing verbs. Rationale: P5 requires every action by every agent to be recorded — including reads. The v0.2 distinction between "mutable system state" (audited) and "versioned documents" (not audited) is insufficient. A document version number records what the document contained; it does not record who read it, when, or what they did with it. Rule 5 updated accordingly. Named Decision D-009. | P5 |

---

## Purpose

This grammar defines the naming, structure, and behavioural contract for
every tool in the Nexus MCP server. It exists to prevent the tool catalogue
from becoming an unmaintainable list of ad hoc names as the framework grows.
Any developer or agent adding a new tool must derive it from this grammar —
not invent independently.

The grammar enforces one principle above all others: **tool possession is
capability** (P3). The name of a tool must be sufficient to determine what
it does, who should have it, and what scope it acts on — without consulting
any other document.

### Why This Grammar Is Load-Bearing, Not Stylistic (P12)

Naming conventions in this framework are structural elements. The
`{verb}_{subject}_{task_slug}` format is not cosmetic:

- It makes every audit log row self-describing without a schema join
- It makes the chain of custody reconstructable by a human with no
  prior knowledge of the database schema
- It makes tool capability derivable by inspection — no tool registry
  documentation needed
- It makes violations of the grammar visible immediately — a malformed
  name signals a design problem, not a naming preference

A single deviation from this grammar creates a gap in traceability that
may only surface during a failure diagnosis. Treat deviations as defects.

### Relationship to the Platform (P3, P16)

These tools exist in the Nexus MCP layer — the access-controlled layer of
the framework. They are the mechanism by which write authority is enforced
between agent classes, because the VS Code platform provides no other way
to scope filesystem write access.

See `.framework/policies/platform-constraints.md` for the full explanation
of why MCP tools are the access control boundary, and which agents hold the
VS Code edit tool instead.

---

## The Grammar

Every tool name is formed from two or three components:

```

{verb}_{subject}

or, for task-scoped tools:

{verb}_{subject}_{task_slug}

```

Where:
- `{verb}` is drawn from the closed Verb Vocabulary (8 entries, never
  extended without a framework-level decision)
- `{subject}` is drawn from the open Subject Vocabulary (document type
  taxonomy, extends as the framework grows)
- `{task_slug}` is the task identifier with hyphens replaced by
  underscores (`task-07` → `task_07`)

**No other components are permitted.** A tool name with an adjective, a
preposition, a conjunction, or any component not in these vocabularies is
malformed and must be redesigned.

---

## Verb Vocabulary

The verbs are a **closed set**. New verbs are never added without a
framework-level decision and update to this document. If a proposed tool
doesn't fit an existing verb, the answer is almost always that the tool is
crossing a concern boundary and should be split.

### Audit Obligation Summary

Every verb in the grammar produces an audit entry. This is a P5 invariant
— it is not optional and cannot be relaxed for individual tools.

| Verb | Audit entry? | State transition? | Stream event? |
|---|---|---|---|
| `read_` | ✅ | ❌ | ❌ |
| `write_` | ✅ | ❌ | ❌ |
| `append_` | ✅ | ❌ | ❌ |
| `submit_` | ✅ | ✅ | ✅ |
| `request_` | ✅ | ✅ (→ AWAITING only) | ✅ |
| `search_` | ✅ | ❌ | ❌ |
| `get_` | ✅ | ❌ | ❌ |
| `raise_` | ✅ | ✅ (→ BLOCKED) | ✅ (priority) |

---

### `read_`

**Semantics:** Fetch the current content of a document. Returns document
content only.

**Principles:** P5 (every action recorded), P3 (tool possession defines
access)

**Side effects:**
Writes one `audit_log` entry:
```json
{
  "tool_name": "read_task_spec_task_07",
  "actor": "task-performer:task-07",
  "task_id": "task-07",
  "doc_version_hash": "sha256:abc123..."
}
```

No state change. No stream event.

**Why `doc_version_hash` is required:**
The version number records what the document contained. The audit entry
records who read it and when. These answer different questions. "The agent
read task_spec v3" tells you what information was available. "The agent
read task_spec v3 at 14:22 before submitting proof at 14:45" tells you what
information the agent was working from when it made a decision. Both are
necessary for a complete causal chain.

**Rules:**

- Must be idempotent — calling it twice returns identical content and
produces two identical audit entries (the second is not an error)
- Must never mutate any database row other than `audit_log`
- Any agent may receive a `read_` tool for any document type relevant
to its role — access is controlled by tool possession, not by a
runtime permission check
- If a document does not exist, return a typed empty response — never
an error that leaks schema details

**How `read_` differs from `get_`:**
Both now produce audit entries. The distinction is what they operate on:

- `read_` operates on task documents — typed, versioned content artefacts
with a defined lifecycle. Returns document content.
- `get_` operates on system state resources — context cards, capability
registries, lifecycle state. Returns structured metadata, not document
content. See `get_` definition below.

**Examples:** `read_task_spec_task_07`, `read_proof_template_task_07`,
`read_qa_review_task_07`

**Counter-example:** `read_context_card` called by an agent loading its own
context ❌ — an agent loading its own context card calls `get_context_card`,
not `read_context_card`. `read_context_card` is reserved for roles that
inspect another agent's card as a governed document (e.g. the FrameworkOwner
auditing what card a given agent class was issued). These are different
operations with different semantics.

---

### `write_`

**Semantics:** Create or fully replace a document. The previous version is
preserved in document history; the current pointer updates.

**Principles:** P4 (mandatory side effects inside tools), P5 (every action
recorded)

**Side effects:**
Writes one `audit_log` entry:

```json
{
  "tool_name": "write_task_spec_task_07",
  "actor": "task-owner:task-07",
  "task_id": "task-07",
  "doc_version_hash": "sha256:def456...",
  "reason": "Updated to include Redis dependency"
}
```

No state transition. No stream event.

**Rules:**

- Requires a mandatory `reason` parameter — the Zod schema must enforce
this; it cannot be optional or empty string
- If the document already exists, creates a new version (never destructive
— the previous version remains in history)
- Must validate that the task is in a state that permits writes for this
document type — reject with a typed error if not
- Never used for append-only documents (use `append_` instead)
- Never used when a state transition must follow (use `submit_` instead)

**Examples:** `write_task_spec_task_07`, `write_feature_spec`,
`write_proof_template_task_07`

**Counter-example:** `write_proof_task_07` ❌ — proof submission requires a
state transition; this must be `submit_proof_task_07`.

---

### `append_`

**Semantics:** Add an entry to an append-only document. The document is an
ordered log; prior entries are never modified.

**Principles:** P4, P5

**Side effects:**
Writes one `audit_log` entry:

```json
{
  "tool_name": "append_work_log_task_07",
  "actor": "task-performer:task-07",
  "task_id": "task-07",
  "entry_hash": "sha256:ghi789...",
  "entry_preview": "First 80 chars of appended entry for log readability"
}
```

No state transition. No stream event.

**Rules:**

- Only applicable to subjects explicitly designated as Append-only in the
Subject Vocabulary — applying `append_` to a Replace-mode subject is a
grammar violation
- Must never accept a `replace` or `overwrite` parameter
- Timestamps are written by the server, not the caller — the caller cannot
specify or override a timestamp
- The `entry_hash` in `audit_log` covers the appended entry only, so
individual entries are independently traceable

**Applicable subjects:** `work_log`, `uncertainty` (log entries),
`decomposition` (task additions only)

**Examples:** `append_work_log_task_07`, `append_uncertainty_task_07`

**Counter-example:** `append_task_spec_task_07` ❌ — `task_spec` is a
Replace-mode document. This is a grammar violation.

---

### `submit_`

**Semantics:** Write a document AND trigger a state transition AND emit a
stream event. All three operations are atomic — all succeed or none do.

**Principles:** P4 (mandatory side effects inside tools), P5, P6 (evidence
not assertion — the submitted document is the literal evidence)

**Side effects (all atomic):**

1. Writes the document with version history
2. Writes one `audit_log` entry
3. Transitions the entity state (specific transition hardcoded per tool)
4. Emits a `stream_events` entry in plain English
5. Triggers the Policy Engine to evaluate downstream policies

**Rules:**

- Exactly one state transition per `submit_` call — if two transitions
are needed, it is two tools
- The stream event text is hardcoded in the tool implementation — the
caller cannot supply or modify the stream message
- Must validate that the current state is the exact expected
pre-transition state; reject with a typed error if not
- The `reason` parameter is mandatory, as per `write_`
- No `submit_` tool is given to an agent that is not the designated
actor for that transition (P8 — separation of execution and
verification)

**Examples:** `submit_proof_task_07`, `submit_qa_review_task_07`,
`submit_ac`

**Counter-example:** `submit_context_card` ❌ — context cards are generated
by the system, not submitted by agents.

---

### `request_`

**Semantics:** Signal intent or request action from another actor. Writes
no documents. Does not advance state to an active working state
unilaterally.

**Principles:** P4, P5, P9 (fail loudly — `request_` is how an agent
signals it needs something before it can proceed, without guessing)

**Side effects:**
Writes one `audit_log` entry. Emits a `stream_events` entry identifying
the target actor. May transition state to an `AWAITING_*` state — but
never to an active working state.

**Rules:**

- Never writes a document
- The requested action must be taken by a different actor — `request_`
is never self-fulfilling
- The stream event must identify who the request is directed at
(HumanApprover, QAExecutor, FeatureOwner)
- Used when an agent needs a cross-role action before it can continue

**Examples:** `request_review`, `request_clarification`,
`request_ac_approval`

**Counter-example:** `request_write_task_spec` ❌ — verbs do not nest.

---

### `search_`

**Semantics:** Query the Pattern Library or knowledge base. Returns
matching entries ranked by relevance.

**Principles:** P5 (every action recorded — what an agent searched for
and what it found is causally significant), P7 (minimum sufficient context
— agents search for relevant patterns rather than receiving all patterns)

**Side effects:**
Writes one `audit_log` entry:

```json
{
  "tool_name": "search_knowledge_base",
  "actor": "task-performer:task-07",
  "query": "login form validation patterns",
  "tags": ["zone-4", "validation"],
  "result_count": 3,
  "top_entry_ids": ["pat-001", "pat-002", "pat-003"]
}
```

No state change. No stream event.

**Why query and results are recorded:**
An audit entry with only a timestamp answers "did the agent search?"
Recording the query and top results answers "what did the agent look for,
and what did it find?" The second question is the one that matters for
diagnosing whether an agent had access to relevant patterns before making
a decision. If an agent produced a poor output on a task type that has a
known Pattern Library entry, the audit log will show whether it searched
for that pattern or not.

**Rules:**

- Must accept a `query` parameter (free text)
- Must accept an optional `tags` parameter for category filtering
- Must never return content from the primary document store — only
Pattern Library and knowledge base entries
- Results must include `source_session` so the caller knows when the
pattern was recorded
- Returns summaries, not full content — an agent needing full content
must have a `read_` tool for that pattern document

**Examples:** `search_knowledge_base`, `search_patterns`

**Counter-example:** `search_task_specs` ❌ — primary document search is
`read_` with a filter parameter, not `search_`. The `search_` verb is
reserved for the knowledge base only.

---

### `get_`

**Semantics:** Fetch system-level metadata, configuration, or pre-generated
artefacts. Distinct from `read_` in that it operates on system resources,
not task documents.

**Principles:** P5, P7 (context cards provide minimum sufficient context
to agents at instantiation)

**Side effects:**
Writes one `audit_log` entry:

```json
{
  "tool_name": "get_context_card",
  "actor": "task-performer:task-07",
  "resource_version": "v3",
  "resource_hash": "sha256:mno345..."
}
```

No state change. No stream event.

**How `get_` differs from `read_` (v0.3 distinction):**

Both verbs now produce audit entries. The distinction is the nature of
what they access, not their audit behaviour:


| Dimension | `read_` | `get_` |
| :-- | :-- | :-- |
| Operates on | Task documents | System state resources |
| Returns | Document content | Structured metadata |
| Subject vocabulary | Document types (task_spec, proof, etc.) | System resources (context_card, capabilities, current_state) |
| Version model | Document version history | Resource regenerated externally (e.g. context cards regenerated by ContextCurator) |
| Audit records | `doc_version_hash` — which doc version | `resource_version` — which system state snapshot |

**Rules:**

- Never operates on a task document — that is `read_`
- Returns structured data, not raw document content
- The audit entry must capture the version or value of the resource
returned — not just that it was fetched

**Examples:** `get_context_card`, `get_my_capabilities`,
`get_current_state`

**Counter-example:** `get_task_spec_task_07` ❌ — task specs are documents,
not system metadata. This must be `read_task_spec_task_07`.

---

### `raise_`

**Semantics:** Surface an exceptional condition immediately to human
attention. Bypasses normal workflow.

**Principles:** P9 (fail loudly, never silently), P10 (irreversible
states require human authority — BLOCKED state is entered here)

**Side effects:**
Writes one priority `audit_log` entry. Emits a priority `stream_events`
entry (visually distinct from standard events — HumanApprover sees this
immediately). If `severity == BLOCKED`: transitions entity state to
`BLOCKED` or `AWAITING_HUMAN`.

**Rules:**

- Reserved exclusively for the `uncertainty` subject — `raise_uncertainty`
is the only valid `raise_` tool in the grammar
- Must never be used for normal workflow signalling — use `request_` for
cross-agent coordination
- The description fields (`what`, `why`, `needed`) are free text — this
is intentional; uncertainties are by definition unstructured
- Any agent may hold this tool — it is a safety valve, not a privilege
(P9 applies in every zone, at every role level)
- A `raise_uncertainty` call with no `context_paths` is invalid — an
uncertainty with no traceable context cannot be resolved

**Example:** `raise_uncertainty`

**Counter-example:** `raise_error` ❌ — tool errors are handled by the
tool's typed return value. `raise_` is exclusively for conditions requiring
human attention that cannot be resolved within the normal flow.

---

## Subject Vocabulary

Subjects are an **open set** — new document types are added as the
framework encounters them. Each entry defines the write mode, valid verbs,
and owning role.


| Subject | Write mode | Valid verbs | Owner role |
| :-- | :-- | :-- | :-- |
| `task_spec` | Replace | `read`, `write` | TaskOwner |
| `proof_template` | Replace | `read`, `write` | ProofDesigner |
| `proof` | Create-once | `read`, `submit` | TaskPerformer |
| `work_log` | Append-only | `read`, `append` | TaskPerformer |
| `feature_spec` | Replace | `read`, `write` | FeatureOwner |
| `ac` | Replace | `read`, `write`, `request` | FeatureOwner |
| `qa_review` | Create-once | `read`, `submit` | QAExecutor |
| `context_card` | Replace | `read`, `write`, `get` | ContextCurator (`write`); any agent (`get`) |
| `environment_contract` | Replace | `read`, `write` | TaskOwner |
| `uncertainty` | Append-only | `read`, `append`, `raise` | Any (cross-cutting) |
| `decomposition` | Append + Replace | `read`, `write`, `append` | FeatureOwner |
| `ui_brief` | Replace | `read`, `write` | UIDesigner |
| `knowledge_base` | Append-only | `search`, `append` | ContextCurator (`append`); any agent (`search`) |
| `patterns` | Replace | `read`, `write`, `search` | FrameworkOwner (`write`); any agent (`read`, `search`) |
| `capabilities` | System | `get` | Nexus server (read-only) |
| `current_state` | System | `get` | Nexus server (read-only) |

**Note on `context_card`:**
The `context_card` subject has both `read_` and `get_` tools. These are
not duplicates:

- `get_context_card` — universal tool, called by an agent loading its
own context at instantiation. This is the agent-facing tool.
- `read_context_card` — role-scoped tool, called by the FrameworkOwner or
ContextCurator to inspect what card a given agent class was issued. This
treats the context card as a governed document to be reviewed, not loaded.

**Rules for adding a new subject:**

1. It must represent a distinct document type not covered by any existing
subject
2. It must have a designated owner role with exclusive `write_` authority
3. Its write mode must be declared before any tool is built
4. Adding a subject does not create tools — only matrix cells that make
domain sense become tools

---

## The Tool Matrix

✓ = tool exists or will exist. Blank = combination is not domain-valid.


|  | `read_` | `write_` | `append_` | `submit_` | `request_` | `search_` | `get_` | `raise_` |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `task_spec` | ✓ | ✓ |  |  |  |  |  |  |
| `proof_template` | ✓ | ✓ |  |  |  |  |  |  |
| `proof` | ✓ |  |  | ✓ |  |  |  |  |
| `work_log` | ✓ |  | ✓ |  |  |  |  |  |
| `feature_spec` | ✓ | ✓ |  |  |  |  |  |  |
| `ac` | ✓ | ✓ |  |  | ✓ |  |  |  |
| `qa_review` | ✓ |  |  | ✓ |  |  |  |  |
| `context_card` | ✓ | ✓ |  |  |  |  | ✓ |  |
| `environment_contract` | ✓ | ✓ |  |  |  |  |  |  |
| `uncertainty` | ✓ |  | ✓ |  |  |  |  | ✓ |
| `decomposition` | ✓ | ✓ | ✓ |  |  |  |  |  |
| `ui_brief` | ✓ | ✓ |  |  |  |  |  |  |
| `knowledge_base` |  |  | ✓ |  |  | ✓ |  |  |
| `patterns` | ✓ | ✓ |  |  |  | ✓ |  |  |
| `capabilities` |  |  |  |  |  |  | ✓ |  |
| `current_state` |  |  |  |  |  |  | ✓ |  |


---

## Scoping Rules

### Universal tools (no task suffix)

Available to every agent, always. No task suffix because they are not
scoped to any single task.

```
get_context_card          search_knowledge_base
get_my_capabilities       raise_uncertainty
get_current_state
```


### Role-scoped tools (no task suffix)

Available to an agent class across all tasks. The tool validates permitted
access against the calling agent's role from its context card.

```
read_feature_spec         write_feature_spec
read_ac                   write_ac
read_decomposition        write_decomposition
read_patterns             write_patterns
append_knowledge_base
```


### Task-scoped tools (with task suffix)

Dynamically generated per active task. The suffix is the task identifier
with hyphens replaced by underscores.

**Formation rule:**

```
task-07  →  _task_07    task-07a →  _task_07a
```

**Examples:**

```
read_task_spec_task_07
write_proof_template_task_07
append_work_log_task_07
submit_proof_task_07
read_environment_contract_task_07
```

**Why underscores:** Hyphens in tool names create parsing ambiguity when
extracting `task_id` by splitting on `_`. Underscores produce unambiguous
splits — the final segment after `_{subject}_` is always the task slug.

---

## Rules for Designing New Tools

Apply in order. Stop and redesign if any rule rejects.

**Rule 1 — One verb.**
Map the proposed operation to exactly one verb. If it maps to two verbs,
it is two tools. If it maps to zero verbs, escalate to a framework-level
decision — do not invent a verb unilaterally.

**Rule 2 — One subject.**
Each tool operates on exactly one subject. A tool that reads one document
type and writes another is two tools.

**Rule 3 — Matrix check.**
Verify the verb × subject cell is marked ✓ in the Tool Matrix. If it is
blank, the combination is not domain-valid. Do not fill blank cells to
satisfy edge cases without confirming at the domain model level.

**Rule 4 — Scope determination.**
Classify as universal, role-scoped, or task-scoped. Universal tools are
rare — only tools that genuinely serve every agent without any task
context. When in doubt, task-scope it.

**Rule 5 — Side effect audit.**
List every side effect. Then verify:

```
Side effects              → Correct verb
────────────────────────────────────────────────
Audit entry only          → read_, search_, or get_
Audit + doc write         → write_ or append_
Audit + doc + transition  → submit_
Audit + stream event only → request_ or raise_
```

If any side effect is absent from the implementation when the verb
requires it, this is a Rule 6 violation, not a Rule 5 violation.

**Rule 6 — Mandatory consequences inside the tool (P4).**
Every side effect listed for a verb must be implemented inside the tool,
not described to the agent as a follow-up instruction. If an agent spec
currently says "after calling X, also write to the audit log" — that is a
Rule 6 violation. The audit write belongs inside X.

This rule applies to audit entries specifically: as of v0.3, no tool in
the grammar has zero side effects. Any tool implementation that does not
write an audit entry is non-compliant regardless of verb.

---

## Well-Formed and Malformed Examples

```
✅  read_task_spec_task_07         verb=read,   subject=task_spec,      scope=task_07
✅  submit_proof_task_07           verb=submit, subject=proof,           scope=task_07
✅  append_work_log_task_07        verb=append, subject=work_log,        scope=task_07
✅  get_context_card               verb=get,    subject=context_card,    scope=universal
✅  raise_uncertainty              verb=raise,  subject=uncertainty,     scope=universal
✅  search_knowledge_base          verb=search, subject=knowledge_base,  scope=universal
✅  request_ac_approval            verb=request,subject=ac,              scope=role

❌  finalize_feature               'finalize' is not in the Verb Vocabulary
❌  write_and_submit_proof_task_07  two verbs — must be split
❌  get_task_spec_task_07          task_spec is a document, not metadata → read_
❌  submit_context_card            context cards are not submitted by agents
❌  append_task_spec_task_07       task_spec is Replace mode, not Append-only
❌  write_proof_task_07            proof is Create-once with state transition → submit_
❌  task_07_write_proof            wrong component order — verb must come first
```


---

## Versioning This Document

Changes to the grammar fall into three categories:

- **Adding a subject** (most common): add to Subject Vocabulary, add row
to Tool Matrix, update affected agent spec templates. Bump patch version.
- **Adding a tool to an existing subject** (occasional): fill a blank
matrix cell, implement the tool, confirm Rules 5 and 6. Bump patch
version.
- **Adding a verb or changing verb semantics** (rare — framework-level
decision required): update this document, the Tool Matrix, all agent
spec templates, and all `tools/list` logic in the Nexus server. Bump
minor version. Record as a Named Decision in the manifest.

```

***

I'll produce the audit log schema in the next response to keep them cleanly separated.

---

## `.framework/schema/audit-log-schema.md`

```markdown
# Audit Log Schema

**Version:** 1.0
**Status:** Active
**Principles implemented:** P5, P12
**Dependencies:** Tool Grammar v0.3, Naming Conventions v0.1
**Last Updated:** 2026-03-04

---

## Purpose

This schema defines the structure and query interface for the `audit_log`
table — the complete, immutable record of every action taken by every agent
in the framework.

The audit log exists to answer one question with absolute reliability:
**"What happened, when, and why?"** Every row is write-once. No row is ever
modified or deleted after creation. The log grows monotonically.

This is not a debugging tool or a performance monitoring system. It is a
causal reconstruction engine. When a task produces unexpected output, the
audit log makes the chain of decisions that led to that output traceable
by a human with no prior knowledge of the agent system.

---

## Schema Definition

```sql
CREATE TABLE audit_log (
  -- Identity
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp         TEXT NOT NULL,              -- ISO 8601 UTC
  
  -- Actor
  actor             TEXT NOT NULL,              -- {agent-class}:{task-id} or system:{component}
  actor_type        TEXT NOT NULL,              -- 'agent' | 'human' | 'webhook' | 'system'
  
  -- Tool and scope
  tool_name         TEXT NOT NULL,              -- exact MCP tool name (from grammar)
  task_id           TEXT,                       -- null for universal/role-scoped tools
  
  -- Payload (query and result data)
  query             TEXT,                       -- for search_ tools
  tags              TEXT,                       -- JSON array, for search_ tools with filters
  result_count      INTEGER,                    -- for search_ tools
  top_entry_ids     TEXT,                       -- JSON array, for search_ tools
  
  reason            TEXT,                       -- for write_, submit_ tools (mandatory)
  
  doc_version_hash  TEXT,                       -- for read_, write_ tools on versioned documents
  entry_hash        TEXT,                       -- for append_ tools (covers appended entry only)
  entry_preview     TEXT,                       -- first 80 chars of appended entry (human readability)
  
  resource_version  TEXT,                       -- for get_ tools (e.g. context card v3)
  resource_hash     TEXT,                       -- for get_ tools
  
  -- State transition evidence (for submit_, raise_, request_)
  prior_state       TEXT,                       -- state before transition
  new_state         TEXT,                       -- state after transition
  
  -- Traceability
  source_audit_id   INTEGER,                    -- references id — links this action to prior action
  
  FOREIGN KEY (source_audit_id) REFERENCES audit_log(id)
);

CREATE INDEX idx_audit_task ON audit_log(task_id, timestamp);
CREATE INDEX idx_audit_actor ON audit_log(actor, timestamp);
CREATE INDEX idx_audit_tool ON audit_log(tool_name, timestamp);
CREATE INDEX idx_audit_timestamp ON audit_log(timestamp);
```


---

## Field Definitions

### Identity Fields

**`id`**
Auto-incrementing integer. Primary key. The monotonic sequence itself
is load-bearing — a gap in IDs signals a database integrity issue.

**`timestamp`**
ISO 8601 UTC format. Example: `2026-03-04T13:22:45.123Z`
Server-written, never supplied by the caller. Nanosecond precision not
required — milliseconds sufficient for causal ordering within a task.

### Actor Fields

**`actor`**
The entity that invoked the tool. Format defined by naming conventions:


| Actor type | Format | Example |
| :-- | :-- | :-- |
| Agent (task-scoped) | `{agent-class}:{task-id}` | `task-performer:task-07` |
| Agent (role-scoped) | `{agent-class}` | `framework-owner` |
| Human | `human:{role}` | `human:approver` |
| Webhook | `webhook:{source}` | `webhook:github` |
| System | `system:{component}` | `system:nexus` |

Agent class names in the `actor` field use kebab-case derived from the
PascalCase class name:

```
TaskPerformer   → task-performer
ContextCurator  → context-curator
QAExecutor      → qa-executor
```

**`actor_type`**
Enum: `'agent'`, `'human'`, `'webhook'`, `'system'`
Derivable from `actor` by prefix, but stored explicitly for query
performance. The audit log is queried more often than it is written —
a denormalized field that eliminates a string split in every query is
a correct tradeoff.

### Tool and Scope Fields

**`tool_name`**
The exact MCP tool name as registered in the Nexus server. Must conform
to the tool grammar. Examples: `read_task_spec_task_07`,
`submit_proof_task_07`, `get_context_card`, `raise_uncertainty`.

**`task_id`**
The task identifier if this action is task-scoped, else `NULL`.
For universal tools (`get_context_card`, `raise_uncertainty`), this
field is `NULL`. For task-scoped tools, it is extracted from the tool
name suffix:

```
read_task_spec_task_07  → task_id = 'task-07'
submit_proof_task_12    → task_id = 'task-12'
```

This field enables the canonical query Q1: "Show me everything that
happened during task-07."

### Payload Fields (Query and Result Data)

These fields capture the inputs and outputs of tools that perform
queries or searches. They are nullable — only populated for tools where
they are semantically meaningful.

**`query`**
The search query string for `search_` tools. Free text.
Example: `"login form validation patterns"`

**`tags`**
JSON array of tag filters applied to the search. Example:
`["zone-4", "validation"]`

**`result_count`**
Integer count of results returned by a `search_` tool. Example: `3`

**`top_entry_ids`**
JSON array of the top N entry IDs returned by a `search_` tool.
Example: `["pat-001", "pat-002", "pat-003"]`

These four fields together answer the question: **"What did the agent
search for, and what did it find?"** This is causally significant. If
an agent produces a poor implementation on a task type that has a known
Pattern Library entry, the audit log will show whether the agent
searched for that pattern before implementing, and whether the pattern
appeared in the search results.

**`reason`**
Mandatory for `write_` and `submit_` tools. Free text explanation of
why the document was written or updated. The Zod schema must enforce
this — it cannot be optional or empty string. Example:
`"Updated to include Redis dependency"`

**`doc_version_hash`**
SHA-256 hash of the document content for `read_` and `write_` tools.
Records which version of the document the agent read or wrote.

The version hash answers a different question than the document version
number. The version number records "what did the document contain"; the
hash in the audit log records "what specific content did this agent see
at this timestamp." Both are necessary for chain of custody.

**`entry_hash`**
SHA-256 hash of the appended entry for `append_` tools. Covers the
appended entry only, not the entire document. This makes individual
entries independently traceable.

**`entry_preview`**
First 80 characters of the appended entry, for human readability in
audit log queries. The full entry is stored in the document itself;
this preview makes the audit log self-describing without requiring a
join to the documents table.

**`resource_version`**
Version identifier for `get_` tools. Example: `"v3"` for a context
card on its third regeneration.

**`resource_hash`**
SHA-256 hash of the resource content for `get_` tools.

### State Transition Evidence

**`prior_state`**
The state of the task or entity immediately before this action.
Populated only for tools that cause state transitions (`submit_`,
`request_`, `raise_`).

**`new_state`**
The state of the task or entity immediately after this action.
Populated only for tools that cause state transitions.

The pair (`prior_state`, `new_state`) makes state transitions
auditable without consulting the `tasks` table. The audit log becomes
self-contained for causal reconstruction.

### Traceability Fields

**`source_audit_id`**
Foreign key to `audit_log(id)`. Links this action to a prior action
that caused it or provided its input.

Example chain:

```
Row 101: task-performer:task-07 calls read_task_spec_task_07
Row 102: task-performer:task-07 calls search_knowledge_base
         source_audit_id = 101 (searched after reading spec)
Row 103: task-performer:task-07 calls submit_proof_task_07
         source_audit_id = 102 (proof informed by search results)
```

This field enables reconstruction of **why** an agent made a decision,
not just **what** it did. It is nullable — the first action in a task
has no prior source.

---

## Canonical Queries

These eight queries define the audit log's interface. If the schema
cannot answer these queries efficiently, it is incomplete.

### Q1 — Task Timeline

**Question:** What actions were taken during task-07, in order?

```sql
SELECT
  timestamp,
  actor,
  tool_name,
  reason,
  new_state
FROM audit_log
WHERE task_id = 'task-07'
ORDER BY timestamp ASC;
```

**Purpose:** Reconstruct the complete sequence of events for a single
task. This is the primary diagnostic query when a task produces
unexpected output.

---

### Q2 — Decision Context

**Question:** What was the agent reading immediately before it submitted
its proof for task-07?

```sql
SELECT
  timestamp,
  tool_name,
  doc_version_hash,
  query,
  result_count
FROM audit_log
WHERE actor = 'task-performer:task-07'
  AND tool_name LIKE 'read_%' OR tool_name LIKE 'search_%'
  AND timestamp < (
    SELECT timestamp
    FROM audit_log
    WHERE actor = 'task-performer:task-07'
      AND tool_name = 'submit_proof_task_07'
    LIMIT 1
  )
ORDER BY timestamp DESC;
```

**Purpose:** Understand what information the agent had access to when
it made a decision. Critical for determining whether a failure was due
to missing patterns, incorrect patterns, or correct patterns that the
agent did not apply.

---

### Q3 — Pattern Usage

**Question:** Did any agent search for pattern `pat-004` in the last 7 days?

```sql
SELECT
  timestamp,
  actor,
  query,
  result_count,
  top_entry_ids
FROM audit_log
WHERE tool_name = 'search_knowledge_base'
  AND top_entry_ids LIKE '%pat-004%'
  AND timestamp > datetime('now', '-7 days')
ORDER BY timestamp DESC;
```

**Purpose:** Validate that promoted patterns are actually being
discovered by agents. If a pattern exists but never appears in search
results, either the pattern's tags are wrong or agents are not
searching for relevant terms.

---

### Q4 — State Transition History

**Question:** How many times has task-07 transitioned state, and what
were the transitions?

```sql
SELECT
  timestamp,
  actor,
  tool_name,
  prior_state,
  new_state
FROM audit_log
WHERE task_id = 'task-07'
  AND new_state IS NOT NULL
ORDER BY timestamp ASC;
```

**Purpose:** Verify the task followed its expected lifecycle. Detect
loops (e.g., task moved to QA three times before passing). Identify
where rework occurred.

---

### Q5 — Actor Activity Summary

**Question:** What did QAExecutor do across all tasks yesterday?

```sql
SELECT
  task_id,
  tool_name,
  COUNT(*) as call_count
FROM audit_log
WHERE actor LIKE 'qa-executor:%'
  AND DATE(timestamp) = DATE('now', '-1 day')
GROUP BY task_id, tool_name
ORDER BY task_id, call_count DESC;
```

**Purpose:** Understand agent workload distribution. Identify tasks
where an agent made an unusually high number of tool calls (may signal
confusion or a poorly-specified task).

---

### Q6 — Uncertainty Timeline

**Question:** Show all uncertainty raises in chronological order.

```sql
SELECT
  timestamp,
  actor,
  task_id,
  reason,
  new_state
FROM audit_log
WHERE tool_name = 'raise_uncertainty'
ORDER BY timestamp DESC;
```

**Purpose:** Track framework gaps. Each `raise_uncertainty` call
represents a condition the framework could not handle autonomously.
Recurring uncertainty patterns indicate missing policies or ambiguous
specifications.

---

### Q7 — Human Intervention Points

**Question:** When did HumanApprover act, and what triggered each action?

```sql
SELECT
  a.timestamp,
  a.tool_name,
  a.task_id,
  a.reason,
  prior.tool_name AS prior_action,
  prior.actor AS prior_actor
FROM audit_log a
LEFT JOIN audit_log prior ON a.source_audit_id = prior.id
WHERE a.actor_type = 'human'
ORDER BY a.timestamp DESC;
```

**Purpose:** Identify where human judgment was required. High frequency
of human intervention on a particular task type signals that task type
needs better automation or clearer specifications.

---

### Q8 — Chain of Custody

**Question:** Trace the chain of actions from task spec read to proof
submission for task-07.

```sql
WITH RECURSIVE trace AS (
  SELECT
    id,
    timestamp,
    actor,
    tool_name,
    source_audit_id,
    0 AS depth
  FROM audit_log
  WHERE tool_name = 'submit_proof_task_07'
  
  UNION ALL
  
  SELECT
    a.id,
    a.timestamp,
    a.actor,
    a.tool_name,
    a.source_audit_id,
    t.depth + 1
  FROM audit_log a
  JOIN trace t ON a.id = t.source_audit_id
)
SELECT
  depth,
  timestamp,
  actor,
  tool_name
FROM trace
ORDER BY depth DESC, timestamp ASC;
```

**Purpose:** Full causal reconstruction. This is the most powerful
query in the schema — it walks backward from a final action (proof
submission) through every prior action that contributed to it. The
result is a complete decision tree showing how the agent arrived at
its output.

---

## Integrity Rules

**Rule 1 — Immutability**
No row is ever updated or deleted after creation. The only write
operation is `INSERT`. Any code path that attempts `UPDATE` or `DELETE`
on `audit_log` is a defect.

**Rule 2 — Server-Side Timestamps**
The `timestamp` field is written by the Nexus server, never supplied by
the caller. This prevents timestamp manipulation and ensures consistent
clock source.

**Rule 3 — Mandatory Reason**
For `write_` and `submit_` tools, the `reason` field must be non-null
and non-empty. The Zod schema must enforce this before the row is
written. A write action with no reason is untraceable and violates P5.

**Rule 4 — Source Audit ID Validity**
If `source_audit_id` is non-null, it must reference an existing
`audit_log.id`. The foreign key constraint enforces this. A dangling
source reference breaks chain of custody.

**Rule 5 — State Transition Completeness**
If `new_state` is non-null, `prior_state` must also be non-null. A
transition with no prior state is incomplete and makes Q4 queries
ambiguous.

**Rule 6 — Tool Name Conformance**
Every `tool_name` must conform to the tool grammar. A malformed tool
name makes the audit log unparseable. This is enforced at tool
registration time, not at audit write time — a malformed tool cannot
be registered in the first place.

---

## Performance Considerations

**Write performance is not a concern.** The audit log is write-once,
append-only, with no updates or deletes. SQLite handles this pattern
efficiently even at high volume.

**Read performance matters.** The audit log is queried frequently during
task diagnosis and retros. The four indexes defined in the schema cover
the common query patterns (Q1–Q8).

**Index coverage:**

- `idx_audit_task` covers Q1, Q4
- `idx_audit_actor` covers Q5, Q7
- `idx_audit_tool` covers Q3, Q6
- `idx_audit_timestamp` covers time-range queries in Q3, Q5, Q6, Q7

The recursive CTE in Q8 (chain of custody) requires no additional index
— it uses the primary key (`id`) and the foreign key (`source_audit_id`),
both of which are indexed by default.

**Growth rate estimate:**
Assuming 50 tool calls per task and 100 tasks per month:

- 5,000 rows/month
- 60,000 rows/year
- 300,000 rows over 5 years

SQLite handles this scale trivially. No partitioning or archival strategy
is needed at this volume.

---

## Relationship to Stream Events

The audit log and the stream events table serve different purposes:


|  | `audit_log` | `stream_events` |
| :-- | :-- | :-- |
| **Audience** | Diagnostic (HA, FrameworkOwner) | Real-time monitoring (HA) |
| **Granularity** | Every tool call | State transitions only |
| **Format** | Structured, queryable | Plain English |
| **Retention** | Permanent | Windowed (30 days typical) |
| **Completeness** | Every action recorded | Summary only |

Stream events are derived from the audit log. When a tool causes a
state transition, it writes both:

1. An `audit_log` row (structured, permanent)
2. A `stream_events` row (plain English, windowed)

The stream event is a human-readable summary of the audit entry, not a
replacement. The audit log is the source of truth.

---

## Version History

| Version | Date | Change |
| :-- | :-- | :-- |
| 1.0 | 2026-03-04 | Initial schema. Grammar v0.3 applied. All eight canonical queries validated. H-SKILLS-01 confirmed no skill read audit entries needed. |

```

---

# ok the next derivations we looked at was the knowledge structures and in particular the context curation policy, context card template and pattern library schema.

Three documents. I'll produce them in derivation order — the pattern library schema first (it's a dependency of the context card), then the context curation policy (it governs how cards are built), then the context card template (the output of that policy).

***

## `.framework/schema/pattern-library-schema.md`

```markdown
# Pattern Library Schema

**Version:** 1.0
**Status:** Active
**Principles implemented:** P7, P11, P12
**Dependencies:** Tool Grammar v0.3, Naming Conventions v0.1
**Last Updated:** 2026-03-04

---

## Purpose

The Pattern Library is the framework's institutional memory. It records
validated solutions, tested approaches, and confirmed failure modes so
agents do not rediscover them from scratch on every task.

It exists to serve one narrow purpose: **to give an agent the minimum
sufficient context to do its job well, without giving it everything
the framework has ever learned.**

The pattern library is not a documentation archive. Entries that are not
actively improving agent output have no place in it.

---

## Entry Lifecycle

```

CANDIDATE                 ACTIVE                   RETIRED
(newly recorded)  ──→    (promoted by FW Owner)  ──→  (superseded)
↑
NV score reaches threshold
and FrameworkOwner approves

```

**NV score (Negative Validation score):**
Counts how many times a pattern has been applied and the outcome was
not negative. It is not a quality score — it is a confidence score.
A pattern with NV = 12 has been applied twelve times without producing
a known failure. It has not necessarily produced twelve successes;
absence of failure and presence of success are different claims.

**Promotion threshold:** NV ≥ 5 AND FrameworkOwner approval.
**Retirement trigger:** Pattern superseded by a newer entry, or NV
accumulates negative evidence on review (recorded via `pattern_evidence`
table).

---

## Schema Definition

```sql
CREATE TABLE patterns (
  -- Identity
  id                TEXT PRIMARY KEY,         -- 'pat-001', 'pat-004'
  pattern_name      TEXT NOT NULL,            -- human-readable name
  status            TEXT NOT NULL             -- 'CANDIDATE' | 'ACTIVE' | 'RETIRED'
                    DEFAULT 'CANDIDATE',
  
  -- Classification
  tags              TEXT NOT NULL,            -- JSON array: ["validation", "zone-4", "forms"]
  agent_classes     TEXT NOT NULL,            -- JSON array of kebab-case agent class names
                                              -- ["task-performer", "qa-executor"]
  agent_types       TEXT NOT NULL             -- JSON array: ["EXECUTOR", "REVIEWER", "*"]
                    DEFAULT '["*"]',          -- "*" = all types in the listed agent_classes
  
  -- Content
  summary           TEXT NOT NULL,            -- max 3 sentences
  detail            TEXT NOT NULL,            -- full pattern description (Markdown)
  anti_pattern      TEXT,                     -- what NOT to do (optional but recommended)
  example           TEXT,                     -- concrete example (optional)
  
  -- Confidence
  nv_score          INTEGER NOT NULL          -- Negative Validation score
                    DEFAULT 0,
  source_session    TEXT NOT NULL,            -- session or experiment where first recorded
  
  -- Provenance
  created_at        TEXT NOT NULL,            -- ISO 8601 UTC
  updated_at        TEXT NOT NULL,
  promoted_at       TEXT,                     -- null until ACTIVE
  promoted_by       TEXT,                     -- 'framework-owner' always
  superseded_by     TEXT                      -- pat-xxx if RETIRED
);

CREATE TABLE pattern_evidence (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  pattern_id        TEXT NOT NULL,
  task_id           TEXT NOT NULL,
  outcome           TEXT NOT NULL,            -- 'POSITIVE' | 'NEGATIVE' | 'NEUTRAL'
  notes             TEXT,
  recorded_at       TEXT NOT NULL,
  recorded_by       TEXT NOT NULL,            -- actor value from audit log
  
  FOREIGN KEY (pattern_id) REFERENCES patterns(id)
);

CREATE INDEX idx_patterns_status ON patterns(status);
CREATE INDEX idx_patterns_tags ON patterns(tags);
CREATE INDEX idx_evidence_pattern ON pattern_evidence(pattern_id);
CREATE INDEX idx_evidence_task ON pattern_evidence(task_id);
```


---

## The `agent_types` Field

This field was added to support the subagent model, where a
`TaskOrchestrator` and a `TaskPerformer` are different agent types
with different context needs. A pattern relevant to a coordinator may
not be relevant to a subagent reviewer and vice versa.

**Valid values:**


| Value | Meaning |
| :-- | :-- |
| `"ORCHESTRATOR"` | Pattern applies to orchestrator agents only |
| `"EXECUTOR"` | Pattern applies to executor subagents only |
| `"REVIEWER"` | Pattern applies to reviewer subagents only |
| `"OWNER"` | Pattern applies to owner agents only |
| `"*"` | Pattern applies to all agent types in `agent_classes` |

**Example:**
A pattern for "how to delegate parallel QA reviews effectively" is
relevant to `TaskOrchestrator` but not to the `ProofReviewer` subagents
it delegates to:

```json
{
  "agent_classes": ["task-orchestrator"],
  "agent_types": ["ORCHESTRATOR"]
}
```

A pattern for "how to write a proof of completion" is relevant only
to executor subagents performing the task:

```json
{
  "agent_classes": ["task-performer"],
  "agent_types": ["EXECUTOR"]
}
```

A validation rubric pattern is relevant to all reviewer subagents
regardless of specific class:

```json
{
  "agent_classes": ["proof-reviewer", "ac-reviewer", "environment-reviewer"],
  "agent_types": ["REVIEWER"]
}
```


---

## Composition Rules for Context Cards

When the ContextCurator builds a context card for an agent, it selects
patterns from this table according to the following rules:

**Orchestrator and Owner agents:**

- Status must be `ACTIVE`
- Tags must match the task domain
- `agent_classes` must include this agent's kebab class name
- `agent_types` must include `"ORCHESTRATOR"`, `"OWNER"`, or `"*"`
- Maximum 7 patterns per card
- Anti-patterns: include all relevant entries (no cap)

**Executor and Reviewer subagents:**

- Same status and tag matching rules as above
- `agent_types` must include `"EXECUTOR"`, `"REVIEWER"`, or `"*"`
- Maximum **3 patterns per card** — subagent context windows must
stay narrow; they have one job
- Anti-patterns: include only entries tagged for this specific
agent class
- Constraints: include only constraints directly relevant to this
agent's output, not the parent orchestrator's full constraint set

**Conflict detection:**
Before composing a card, the ContextCurator must check whether any
selected pattern is contradicted by another selected pattern on any
dimension (approach, order, scope). If a conflict is found, it must:

1. Select the higher-NV-score pattern
2. Exclude the lower-NV-score pattern
3. Record an `OPEN_FLAG` with `flag_type = 'CONFLICT'` in the card

---

## Canonical Queries

### QP1 — Active patterns for a given agent class and domain

```sql
SELECT
  id, pattern_name, nv_score, summary, anti_pattern
FROM patterns
WHERE status = 'ACTIVE'
  AND agent_classes LIKE '%task-performer%'
  AND tags LIKE '%validation%'
ORDER BY nv_score DESC
LIMIT 7;
```


### QP2 — Pattern evidence for a given task

```sql
SELECT
  p.pattern_name,
  pe.outcome,
  pe.notes,
  pe.recorded_at
FROM pattern_evidence pe
JOIN patterns p ON pe.pattern_id = p.id
WHERE pe.task_id = 'task-07'
ORDER BY pe.recorded_at ASC;
```


### QP3 — Candidate patterns ready for promotion review

```sql
SELECT
  id, pattern_name, nv_score, source_session, created_at
FROM patterns
WHERE status = 'CANDIDATE'
  AND nv_score >= 5
ORDER BY nv_score DESC;
```


### QP4 — Negative evidence accumulation (retirement candidates)

```sql
SELECT
  p.id,
  p.pattern_name,
  COUNT(CASE WHEN pe.outcome = 'NEGATIVE' THEN 1 END) AS negative_count,
  COUNT(CASE WHEN pe.outcome = 'POSITIVE' THEN 1 END) AS positive_count
FROM patterns p
JOIN pattern_evidence pe ON p.id = pe.pattern_id
WHERE p.status = 'ACTIVE'
GROUP BY p.id
HAVING negative_count >= 2
ORDER BY negative_count DESC;
```


---

## Integrity Rules

**Rule 1 — Immutable IDs**
Pattern IDs are never reused. A retired pattern keeps its ID. The
`superseded_by` field links retired entries to their replacement.

**Rule 2 — Summary length**
The `summary` field must be ≤ 3 sentences. This is enforced at write
time. The summary is delivered to agents in context cards; longer
summaries consume attention budget without proportional value.

**Rule 3 — Promotion authority**
Only `framework-owner` may set `status = 'ACTIVE'`. The `promoted_by`
field must be `'framework-owner'`. This is enforced in the Nexus server
tool implementation for `write_patterns`.

**Rule 4 — Evidence before promotion**
A pattern may not be promoted to ACTIVE without at least one
`pattern_evidence` row with `outcome = 'POSITIVE'` and NV ≥ 5.
The promotion tool must validate this before accepting the write.

---

## Version History

| Version | Date | Change |
| :-- | :-- | :-- |
| 1.0 | 2026-03-04 | Initial schema. `agent_types` field added for subagent model. Composition rules split by agent type. Naming conventions applied. |

```

***

## `.framework/policies/context-curation-policy.md`

```markdown
# Context Curation Policy

**Version:** 1.0
**Status:** Active
**Principles implemented:** P7, P8, P12
**Dependencies:**
  Pattern Library Schema v1.0
  Context Card Schema v1.0
  Tool Grammar v0.3
  Naming Conventions v0.1
**Last Updated:** 2026-03-04

---

## Purpose

This policy governs how the ContextCurator builds, delivers, and
invalidates context cards. It exists because context is not free.
Every item in an agent's context card consumes attention window — the
agent's finite working memory. A poorly composed card does not just
add noise; it actively degrades the agent's performance by diluting
the signal it needs to act.

**The governing principle (P7):**
Give agents the minimum sufficient context to do their job well. Not
the minimum possible context. Not all available context. Minimum
sufficient. The ContextCurator's job is to make that judgment call
well, every time.

---

## Card Types

| Type | Recipient | Trigger | Scope |
|---|---|---|---|
| `ROLE` | An agent class at startup | Agent instantiation | General role patterns only |
| `TASK` | An agent performing a task | Task published to zone | Task-specific patterns + constraints |
| `SUBAGENT` | A subagent with a micro-task | Subagent activated | Narrowly scoped to micro-task only |

Role cards are never task-specific. Task cards are never reused across
tasks. Subagent cards are the most restricted — they contain only what
the subagent needs to complete its single defined responsibility.

---

## Composition Rules

### Step 1 — Retrieve task and agent metadata

Fetch:
- Agent class name and agent type (ORCHESTRATOR / EXECUTOR /
  REVIEWER / OWNER)
- Task ID, task domain tags, task feature ID
- Any open uncertainties for this task
- Any open flags from prior cards for this task

### Step 2 — Select patterns

Query the Pattern Library using composition rules from Pattern Library
Schema v1.0:
- Status = `ACTIVE`
- Tags match task domain
- `agent_classes` includes this agent's kebab-case class name
- `agent_types` includes this agent's type or `"*"`
- Apply cap: 7 patterns for orchestrators/owners, 3 for subagents
- Order by `nv_score DESC` — highest confidence first
- Run conflict detection before finalising selection

### Step 3 — Distil constraints

Retrieve relevant policies for this task type and agent class.
Extract the actionable constraints as plain English rules:

```

✅  "Use npm, not bun"
✅  "Target Node 20 LTS"
✅  "Branch must be task/task-07"
✅  "Do not modify migration files once committed"

❌  "See .framework/policies/dependency-policy.md for rules"
(a reference is not a constraint — distil the rule)

```

The agent receives the rule, not the reference. Policy document
paths are not delivered in the card.

For subagents: include only constraints directly relevant to this
agent's output. The parent orchestrator's full constraint set is
not passed down.

### Step 4 — Compose tools guidance

For each tool in the agent's tool list, write a one-line statement
of purpose in plain English:

```

get_context_card          → "Load your task brief before starting"
read_task_spec_task_07    → "Read your full task specification"
append_work_log_task_07   → "Log significant steps as you work"
submit_proof_task_07      → "Submit your completed proof when done"
raise_uncertainty         → "Call this if you are blocked or uncertain"

```

This is not a tutorial. It is a quick-reference map so the agent
knows which tool to reach for without consulting any other document.

### Step 5 — Collect open flags

Retrieve:
- Any CONFLICT detected in Step 2
- Any GAP identified in prior task cards
- Any KNOWN_UNCERTAINTY from the uncertainty log for this task
- Any EXCLUSION applied during pattern selection (why a pattern was
  excluded that might otherwise have been expected)

If no flags: omit the field entirely. Do not deliver an empty flags
block — it signals to the agent that it should look for flags,
consuming attention on a null result.

### Step 6 — Set certainty threshold

Retrieve the declared `certainty_threshold` from the agent class
definition. Deliver it directly in the card. The agent should never
need to look this up — it must be present before the agent takes its
first action.

### Step 7 — Compute card hash

SHA-256 of the complete serialised card content. Store this hash in
`ContextCardMetadata` (the DB record, not the card itself). Used for:
- Stale detection (has the card changed since the agent last loaded it?)
- Chain of custody (what exactly did this agent receive?)

### Step 8 — Store and deliver

Store: `ContextCard + ContextCardMetadata` in the `documents` table.
Deliver: `ContextCard` only via `get_context_card`.

The metadata stays in the database. The agent receives only the card.

---

## Staleness Rules

A context card becomes stale when any of its source material changes.
The ContextCurator must regenerate the card before the agent's next
task if any of the following have changed since the card was generated:

| Source change | Stale? |
|---|---|
| Task spec updated | ✅ Yes — full regeneration |
| Pattern NV score updated | 🟡 Conditional — only if the score crosses a selection threshold |
| New pattern promoted to ACTIVE with matching tags | ✅ Yes — may change selection |
| Constraint-governing policy updated | ✅ Yes — distilled constraints may change |
| Agent class definition updated | ✅ Yes — tools guidance and certainty threshold may change |
| Stream event written (no spec change) | ❌ No — stream events do not affect card content |

**Stale card behaviour:**
A stale card is not automatically regenerated — regeneration is
triggered by the ContextCurator on task state transition. An agent
that calls `get_context_card` while the card is marked stale receives
the existing card with an `OPEN_FLAG` of type `KNOWN_UNCERTAINTY`:

```json
{
  "flag_type": "KNOWN_UNCERTAINTY",
  "description": "This card may be stale. Task spec was updated after this card was generated.",
  "source": "system:nexus"
}
```

The agent must call `raise_uncertainty` if it cannot proceed safely
with a potentially stale card.

---

## Skills Are Not Delivered by This Policy

Skills (`.github/skills/*.skill.md`) are delivered by the VS Code host
layer at agent instantiation. They are not part of the context card.

**Never include skill content in a context card.** Skills represent
role knowledge — how the agent does its job. Context cards represent
task knowledge — what this specific task requires. These are different
things delivered by different mechanisms.

Duplicating skill content in the card:

- Wastes the agent's attention budget
- Creates a maintenance sync problem (skill and card can diverge)
- Signals that the skill is not trusted to be delivered correctly
by VS Code — which undermines the architecture

If skill content seems necessary in the card, the correct action is
to review whether the skill is correctly scoped and referenced in the
agent class definition, not to copy it into the card.

---

## What the ContextCurator Must Never Do

- Include file paths in the card (no document paths, no policy paths,
no skill paths) — the agent does not need to know where things live
- Include governance metadata in the card (no zone, no card version,
no generated_at) — this is for the FOA and the DB record only
- Include patterns with status ≠ ACTIVE
- Include more than 7 patterns for orchestrators or 3 for subagents
- Pass the parent orchestrator's full constraint set to a subagent
- Regenerate a card mid-task without updating the `source_audit_id`
chain in the audit log
- Deliver a card with unresolved CONFLICT flags without flagging them
explicitly in `open_flags`

---

## Version History

| Version | Date | Change |
| :-- | :-- | :-- |
| 1.0 | 2026-03-04 | Initial policy. Subagent card type added. Skills explicitly excluded from cards. Governance metadata split defined. Staleness rules formalised. |

```

***

## `.framework/schema/context-card-schema.md`

```markdown
# Context Card Schema

**Version:** 1.0
**Status:** Active
**Principles implemented:** P7, P12
**Dependencies:**
  Pattern Library Schema v1.0
  Context Curation Policy v1.0
  Naming Conventions v0.1
**Last Updated:** 2026-03-04

---

## Purpose

This schema defines two things:

1. **`ContextCard`** — what `get_context_card` delivers to an agent.
   Minimum sufficient context. Task-facing. No governance metadata.

2. **`ContextCardMetadata`** — what is stored in the `documents` table
   alongside the card. Governance-facing. Never delivered to the agent.

The split is load-bearing. Governance metadata in an agent's context
window is noise. It consumes attention without improving output. The
agent needs to know what to do and how to do it — not what zone it is
in or who generated its card.

---

## ContextCard — Agent-Facing

This is the complete, typed definition of what an agent receives when
it calls `get_context_card`.

```typescript
type ContextCard = {

  // ── Task Brief ─────────────────────────────────────────────
  // What the agent is here to do.
  // Plain English. One paragraph maximum.
  // For ROLE cards (no specific task): describes the agent's
  // standing brief across all tasks of its class.
  task_brief:       string

  task_id:          string | null   // 'task-07' | null for ROLE cards
  feature_id:       string | null   // 'feat-003' | null if no feature scope

  // ── Certainty Threshold ────────────────────────────────────
  // Declared in the agent class definition.
  // Delivered here so the agent has it before its first action.
  // If the agent's confidence in its output falls below this
  // value it must call raise_uncertainty before proceeding.
  certainty_threshold: number       // 0.0–1.0

  // ── Tools Guidance ─────────────────────────────────────────
  // Plain English map of which tool to call for what.
  // Mirrors the agent's tool list, not a tutorial.
  // Purpose: eliminate tool choice confusion without adding docs.
  tools_guidance:   ToolGuidance[]

  // ── Patterns ───────────────────────────────────────────────
  // Validated patterns relevant to this agent + task.
  // ORCHESTRATOR / OWNER: max 7
  // EXECUTOR / REVIEWER subagents: max 3
  // Ordered by nv_score DESC — highest confidence first.
  patterns:         PatternEntry[]

  // ── Anti-Patterns ──────────────────────────────────────────
  // Confirmed failure modes for this agent class and task domain.
  // Always surfaced separately — never buried in patterns list.
  // For subagents: only entries tagged for this specific class.
  anti_patterns:    PatternEntry[]

  // ── Constraints ────────────────────────────────────────────
  // Distilled from policies — the actionable rule, not the
  // policy reference.
  // For subagents: only constraints relevant to this agent's
  // specific output. Not the parent orchestrator's full set.
  constraints:      string[]

  // ── Open Flags ─────────────────────────────────────────────
  // Conflicts, known gaps, uncertainties, exclusions.
  // Field is OMITTED (not empty array) if no flags exist.
  // An agent that sees open flags must address them before
  // proceeding, or call raise_uncertainty if it cannot.
  open_flags?:      OpenFlag[]
}

// ── Supporting Types ─────────────────────────────────────────

type ToolGuidance = {
  tool_name:        string    // exact MCP tool name as registered
  use_for:          string    // one sentence, plain English
                              // "Read your task specification"
                              // "Submit your completed proof when done"
                              // "Call this if you are blocked or uncertain"
}

type PatternEntry = {
  pattern_id:       string    // 'pat-004'
  pattern_name:     string
  current_nv:       number    // NV score at time of card generation
  summary:          string    // max 3 sentences — full detail in KB
  relevance_reason: string    // why this pattern was selected for
                              // this specific agent + task combination
}

type OpenFlag = {
  flag_type:        'CONFLICT' | 'GAP' | 'KNOWN_UNCERTAINTY' | 'EXCLUSION'
  description:      string    // plain English, actionable
  source:           string    // actor or system component that raised it
                              // e.g. 'context-curator', 'system:nexus',
                              //      'framework-owner'
}
```


---

## ContextCardMetadata — Governance-Facing

Stored in the `documents` table. Returned only by `read_context_card`
(available to FrameworkOwner and ContextCurator, not to task agents).
Never delivered to the agent via `get_context_card`.

```typescript
type ContextCardMetadata = {
  // Identity
  agent_class:      string    // 'task-performer'
  agent_instance:   string    // 'task-performer:task-07'
  card_type:        'ROLE' | 'TASK' | 'SUBAGENT'
  card_version:     string    // 'v3' — increments on each regeneration
  card_hash:        string    // SHA-256 of serialised ContextCard content

  // Provenance
  generated_at:     string    // ISO 8601 UTC
  generated_by:     string    // always 'context-curator'
  valid_until:      string | null

  // Staleness
  stale:            boolean
  stale_reason:     string | null

  // Governance (not in card, available for FOA audit)
  zone:             string    // 'zone-4', 'zone-5'
  source_pattern_ids: string[]  // patterns selected during composition
  source_policy_ids:  string[]  // policies consulted during composition

  // Traceability
  source_audit_id:  number    // audit_log.id of get_context_card call
}
```


---

## Example Cards

### TASK card — TaskPerformer for task-07

```json
{
  "task_brief": "Implement the login form validation for feat-003. The form must validate email format, password minimum length (8 characters), and display inline field errors. Do not implement authentication — that is out of scope for this task.",
  "task_id": "task-07",
  "feature_id": "feat-003",
  "certainty_threshold": 0.8,
  "tools_guidance": [
    {
      "tool_name": "get_context_card",
      "use_for": "Load this brief at the start of your session"
    },
    {
      "tool_name": "read_task_spec_task_07",
      "use_for": "Read your full task specification and acceptance criteria"
    },
    {
      "tool_name": "append_work_log_task_07",
      "use_for": "Log significant steps, decisions, and blockers as you work"
    },
    {
      "tool_name": "submit_proof_task_07",
      "use_for": "Submit your completed proof of completion when done"
    },
    {
      "tool_name": "search_knowledge_base",
      "use_for": "Search for relevant patterns or prior solutions"
    },
    {
      "tool_name": "raise_uncertainty",
      "use_for": "Call this immediately if you are blocked or uncertain"
    }
  ],
  "patterns": [
    {
      "pattern_id": "pat-004",
      "pattern_name": "Inline Field Validation",
      "current_nv": 9,
      "summary": "Validate on blur, not on submit. Display errors adjacent to the field, not in a summary block. Clear errors as soon as the field value becomes valid.",
      "relevance_reason": "This task requires inline field error display per task spec."
    },
    {
      "pattern_id": "pat-007",
      "pattern_name": "Email Format Validation",
      "current_nv": 6,
      "summary": "Use the HTML5 email input type as the first validation layer. Add a regex check for cases where browser validation is bypassed. Do not validate MX records client-side.",
      "relevance_reason": "Task-07 requires email format validation specifically."
    }
  ],
  "anti_patterns": [
    {
      "pattern_id": "pat-012",
      "pattern_name": "Submit-Time Validation Only",
      "current_nv": 0,
      "summary": "Validating only on form submit forces users to correct all errors at once. This pattern has produced poor UX scores on three prior tasks.",
      "relevance_reason": "Direct failure mode for the inline validation requirement in this task."
    }
  ],
  "constraints": [
    "Use React Hook Form — do not implement custom form state management",
    "Target Node 20 LTS",
    "Branch must be task/task-07",
    "Do not implement authentication — it is out of scope for task-07"
  ]
}
```


### SUBAGENT card — ProofReviewer for task-07

Note the narrower scope — 1 pattern, 1 anti-pattern, 3 constraints,
and tools guidance for only the tools this subagent holds.

```json
{
  "task_brief": "Review the submitted proof for task-07 against the proof template. Return PASS with specific evidence, or FAIL with the exact unmet criteria. Do not evaluate implementation quality — only whether the proof satisfies the template.",
  "task_id": "task-07",
  "feature_id": "feat-003",
  "certainty_threshold": 0.9,
  "tools_guidance": [
    {
      "tool_name": "get_context_card",
      "use_for": "Load this brief before reviewing"
    },
    {
      "tool_name": "read_proof_template_task_07",
      "use_for": "Read the proof template — this defines what a passing proof must contain"
    },
    {
      "tool_name": "read_proof_task_07",
      "use_for": "Read the submitted proof to review"
    },
    {
      "tool_name": "raise_uncertainty",
      "use_for": "Call this if the proof or template is ambiguous or incomplete"
    }
  ],
  "patterns": [
    {
      "pattern_id": "pat-019",
      "pattern_name": "Evidence-First Proof Review",
      "current_nv": 7,
      "summary": "Check for explicit evidence against each template criterion before forming a verdict. A proof that asserts completion without linking to evidence fails. Match evidence to criteria one-to-one.",
      "relevance_reason": "Primary review pattern for all proof template validation."
    }
  ],
  "anti_patterns": [
    {
      "pattern_id": "pat-023",
      "pattern_name": "Implementation Quality Scope Creep",
      "current_nv": 0,
      "summary": "Reviewing implementation quality, code style, or architectural decisions during proof review is out of scope and delays task progression. ProofReviewer evaluates the proof document only.",
      "relevance_reason": "Common failure mode for proof reviewers — stay within scope."
    }
  ],
  "constraints": [
    "Review the proof document only — do not fetch or evaluate source code",
    "Your output is PASS or FAIL with evidence — no other verdicts are valid",
    "If the template has unfilled sections, that is a FAIL"
  ]
}
```


---

## What Is Never in a Context Card

| Excluded item | Reason |
| :-- | :-- |
| File paths | Agent does not need to know where things live — tools handle location |
| Policy document references | Agent receives distilled rules, not references to read |
| Skill content | Delivered by VS Code host layer independently — see H-SKILLS-01 |
| Governance metadata | Zone, card version, generated_at — for FOA and DB only |
| `active_policies` list | A reference is not a constraint — distil the rule |
| All available patterns | Minimum sufficient, not maximum available |
| Parent orchestrator's full constraint set | Subagents receive only constraints relevant to their output |


---

## Version History

| Version | Date | Change |
| :-- | :-- | :-- |
| 1.0 | 2026-03-04 | Initial schema. `permissions` block removed (pre-MCP model). Governance metadata split into ContextCardMetadata. `tools_guidance` replaces file path lists. `active_policies` removed. SUBAGENT card type added with 3-pattern cap. Skills exclusion rule formalised (H-SKILLS-01). |

```

---

# Great. now the fun part: agent design standards

This is where everything we've built converges. Three documents: the design standards (the governing policy), the agent class definition template (the governance artefact), and the agent file template (the VS Code artefact). In that order — the templates are derived from the standards.

***

## `.framework/policies/agent-design-standards.md`

```markdown
# Agent Design Standards

**Version:** 1.0
**Status:** Active
**Principles implemented:** P3, P4, P7, P8, P9, P12, P16
**Dependencies:**
  Platform Constraints v1.0
  Tool Grammar v0.3
  Naming Conventions v0.1
  Context Card Schema v1.0
  Pattern Library Schema v1.0
**Last Updated:** 2026-03-04

---

## Purpose

This document defines the rules for designing agents in this framework.
It exists because agent design is not a creative exercise — it is an
engineering discipline with load-bearing constraints. An agent designed
outside these standards will either fail to integrate with the framework,
create audit gaps, or violate the access control model.

Every agent class in this framework must be derived from these standards.
No exceptions without a framework-level decision recorded in the manifest.

---

## The Two-Layer Model

Every agent class exists in two layers simultaneously. Both must be
designed and both must be correct before the agent class is complete.

```

VS CODE LAYER                         NEXUS LAYER
─────────────────────────────         ───────────────────────────────
{agent-class}.agent.md                Agent class definition
≤15 lines                             (.framework/agent-classes/)
Identity + tool list only             Full governance record
What the agent IS                     Why the agent exists

{agent-class}.skill.md                Context card
Role knowledge                        Delivered via get_context_card
How to do the job                     Task-specific knowledge
Injected by VS Code host              Built by ContextCurator
No audit entry (H-SKILLS-01)          Full audit entry

{agent-class}.instructions.md         Task-scoped MCP tools
Always-on rules                       Dynamically assigned
Hard constraints that                 at task activation
never change per task

```

**VS Code layer** is static. It defines the agent's identity, capability
vocabulary, and standing knowledge. It never contains task-specific
information.

**Nexus layer** is dynamic. It provides task-specific context (via the
context card) and task-specific capability (via dynamically assigned
task-scoped tools).

An agent file that contains task-specific content is a design violation.
A context card that contains role knowledge (skill content) is a design
violation.

---

## Agent Types

There are four agent types. The type determines the agent's structural
rules, tool allocation, `user-invokable` setting, and naming convention.

| Type | Name suffix | user-invokable | Primary role | Context cap |
|---|---|---|---|---|
| `ORCHESTRATOR` | `*Orchestrator` | `true` | Delegates workflow to subagents | 7 patterns |
| `OWNER` | `*Owner` | `true` | Holds gate authority over a domain | 7 patterns |
| `EXECUTOR` | Any other doer | `false` | Performs a defined task | 3 patterns |
| `REVIEWER` | Any other doer | `false` | Independently verifies output | 3 patterns |

**The naming rule is structural, not cosmetic.** The spec test framework
derives `user-invokable` directly from the agent name. An agent whose
name ends in neither `Orchestrator` nor `Owner` must have
`user-invokable: false`. This is enforced at spec test time, not
by convention.

---

## Type Rules

### ORCHESTRATOR

An Orchestrator coordinates workflow. It delegates to subagents. It
never directly implements task work or reviews task output.

**Structural rules:**
- Must declare an `agents:` list — at minimum two subagents
- Must hold the `agent` tool (enables subagent delegation)
- Must hold all universal tools
- Must NOT hold `write_`, `submit_`, `append_`, or `read_` task
  document tools — it does not perform work, it coordinates it
- May hold `read_` for feature-level documents (feature spec, AC,
  decomposition) to understand scope before delegating
- `user-invokable: true`

**Failure mode to avoid:**
An Orchestrator that directly implements task work defeats the purpose
of the subagent model and contaminates the coordination context with
execution context. If the Orchestrator needs to do work, it means a
subagent class is missing.

### OWNER

An Owner holds gate authority. It approves, rejects, and halts. It
does not coordinate workflow between other agents.

**Structural rules:**
- Must hold `write_` authority for its domain documents
- Must hold `submit_` or `request_` tools for state-transition
  decisions within its authority scope
- Must hold `raise_uncertainty` (all agents do — but especially
  critical here since Owners make irreversible state decisions)
- `user-invokable: true`
- May or may not hold an `agents:` list depending on whether
  authority decisions require subagent validation

**Current Owner agents:**
`FrameworkOwner`, `FeatureOwner`, `TaskOwner`, `UncertaintyOwner`

### EXECUTOR

An Executor performs a defined task. It operates in a clean, narrow
context window. It never coordinates other agents.

**Structural rules:**
- `user-invokable: false` — only receives work via an Orchestrator
  or Owner delegation, or a direct task assignment in the workflow
- Must NOT hold the `agent` tool
- Must NOT hold `write_` tools for documents it submits — if it
  submits a proof, it holds `submit_proof`, not `write_proof`
  (P8: separation of execution and verification applies to
  write authority, not just review)
- Tool list must be the minimum necessary for the defined task
- Context cap: 3 patterns maximum

### REVIEWER

A Reviewer independently verifies output produced by an Executor.
It must be structurally independent — it cannot hold the same write
tools as the Executor it reviews.

**Structural rules:**
- `user-invokable: false`
- Must NOT hold the `agent` tool
- Must NOT hold any `write_`, `append_`, or `submit_` tools for
  documents the Executor it reviews can write — pure read access
  in its domain (P8: separation of execution and verification)
- Must hold `submit_` for its own review document
- Context cap: 3 patterns maximum
- Certainty threshold must be ≥ 0.9 — reviewers must be more
  certain than executors before submitting

---

## Tool Allocation Principles

### Principle 1 — Universal tools belong to every agent

Every agent, without exception, holds:
```

get_context_card
get_my_capabilities
get_current_state
raise_uncertainty

```

There is no agent type for which these are optional. An agent that
cannot load its context card cannot operate. An agent that cannot
raise uncertainty cannot fail safely.

### Principle 2 — Tool possession is capability (P3)

An agent that does not hold a tool cannot call it. This is the
access control model. There is no runtime permission check. There
is no role-based authorisation layer at call time. Access is
determined entirely by what tools the agent was given at design time.

This means tool allocation decisions are security decisions. Giving
an Executor a `write_` tool for a document it should only read is
not a convenience — it is an access control violation.

### Principle 3 — No agent holds both sides of a verification boundary (P8)

For every document that has a submit/review lifecycle:
- The agent that submits it must not be the agent that reviews it
- The agent that reviews it must not hold write access to it

This is structural separation of execution and verification. It is
not enforced by runtime policy — it is enforced by tool design.
If an agent spec violates this principle, the violation is visible
immediately: the agent holds both `submit_proof` and `submit_qa_review`
for the same task document. That is a design defect.

### Principle 4 — Minimum sufficient tools (P7)

The tool list for any agent is the minimum set of tools the agent
needs to complete its defined task. Not the minimum possible (which
would prevent the agent operating). Not all available tools (which
would violate P3 and P8). Minimum sufficient.

When in doubt, omit the tool. An agent that lacks a needed tool will
call `raise_uncertainty` (P9). That is the correct behaviour. An
agent that has an unnecessary tool may use it inappropriately and
produce an untraceable side effect.

### Principle 5 — Task-scoped tools are assigned dynamically

An Executor does not permanently hold `read_task_spec_task_07`. That
tool is assigned when task-07 is activated and revoked when task-07
is closed. The agent class definition lists the tool *types* the
agent will receive (e.g. `read_task_spec_{task_id}`) — the actual
tools are dynamically registered by the Nexus server.

This means the agent file's `tools:` list contains:
- All universal tools (always static)
- All role-scoped tools (static)
- A notation for dynamically assigned task-scoped tools (not listed
  individually — they are described in the agent class definition)

---

## The Agent File

The agent file is the VS Code artefact. It is the agent's identity
card in the VS Code layer.

**Hard constraints:**
- Maximum 15 lines of content (excluding YAML frontmatter delimiter
  lines `---`)
- Instructions are 2–4 lines maximum
- No task-specific content
- No policy references
- No governance metadata
- No file paths

**What belongs in the agent file:**
- `name` — PascalCase, from naming conventions
- `description` — one sentence, active voice, what the agent does
- `model` — model identifier
- `user-invokable` — derived from agent type
- `tools` — universal + role-scoped tools only
- `agents` — for Orchestrators only
- Instructions: "Call `get_context_card` to load your brief. [One
  sentence primary directive.] Call `raise_uncertainty` if blocked."

**What does not belong in the agent file:**
Everything else. The agent file is not documentation. It is not a
specification. It is not a training document. It is a minimal
identity declaration. Governance information lives in the agent
class definition. Task information lives in the context card.
Role knowledge lives in the skill file.

---

## The Skill File

The skill file is the agent's role knowledge. It defines how the
agent does its job — craft knowledge, output format standards,
quality criteria, decision frameworks.

**Delivered by:** VS Code host layer at agent instantiation.
No read tool required. No audit entry produced. (H-SKILLS-01,
confirmed 2026-03-04)

**What belongs in the skill file:**
- How to structure outputs for this agent's role
- Quality criteria that apply to every task of this type
- Decision frameworks for common judgment calls
- Output format templates and examples
- What good looks like; what failure looks like

**What does not belong in the skill file:**
- Task-specific information (belongs in context card)
- Policy references (belongs in constraints, delivered via card)
- File paths (agent doesn't need to know where things live)
- Audit or governance instructions (handled by tool design)

**Naming:** `{agent-class}.skill.md` in `.github/skills/`

The skill file is referenced in the agent class definition.
It is not referenced in the agent file directly — VS Code discovers
it through the agent configuration mechanism.

---

## The Agent Class Definition

The agent class definition is the governance artefact. It lives in
`.framework/agent-classes/` and is never delivered to the agent.
It is the source of truth for the ContextCurator when building
context cards, and for the FrameworkOwner when auditing agent design.

**Contents:**
- Agent type (ORCHESTRATOR / OWNER / EXECUTOR / REVIEWER)
- Purpose statement (2–3 sentences — what problem does this agent
  class solve, why does it exist as a separate class)
- Certainty threshold (0.0–1.0)
- Canonical tool list with justification for each tool
- Skill file reference
- Pattern tags (which domain tags should be searched when building
  this agent's context cards)
- Gate authority declaration (for OWNER type only)
- Subagent list with delegation protocol (for ORCHESTRATOR type only)

See `.framework/templates/agent-class-definition-template.md`

---

## Process: Designing a New Agent Class

Apply in order. Do not skip steps.

**Step 1 — Identify the gap**
What task is currently not being done, or being done by an agent
that is accumulating too much context? The answer must be a concrete
task with a defined output, not a vague capability.

**Step 2 — Determine the type**
Does this agent coordinate, own, execute, or review?
- If it delegates work to others → ORCHESTRATOR
- If it approves/rejects/halts work → OWNER
- If it produces a defined output → EXECUTOR
- If it verifies a defined output → REVIEWER

If the answer is "both execute and review" → it is two agents.
Separation of execution and verification is non-negotiable (P8).

**Step 3 — Name it**
Apply naming conventions. Final component must be from the doer
word vocabulary, or `Owner` for gate authority agents. If you
cannot name it with a doer word, the type is probably wrong.

**Step 4 — Define the tool list**
Start with universal tools (all agents). Add role-scoped tools.
Note task-scoped tools that will be dynamically assigned.
For each tool, write one sentence: why does this agent need this tool?
If you cannot answer, remove the tool.
Apply P8 check: does this agent hold both sides of any
verification boundary? If yes, redesign.

**Step 5 — Write the skill file**
What does this agent need to know to do its job well, regardless
of which specific task it is working on? Write that. Keep it to
what an expert practitioner would consider role knowledge vs
task briefing.

**Step 6 — Write the agent class definition**
Fill the template. This is the governance record. It must be
complete before the agent file is written — the agent file is
derived from the class definition, not the other way around.

**Step 7 — Write the agent file**
Derive from the class definition. Apply the 15-line constraint.
Write 2–4 lines of instructions. Confirm that the file contains
no task-specific content, no policy references, no file paths.

**Step 8 — Run spec tests**
See Spec Tests section. All tests must pass before the agent class
is considered complete.

**Step 9 — Register in the framework manifest**
Record the new agent class as a Named Addition. Include the
derivation decision and any design choices made in Steps 2–4.

---

## Spec Tests

These tests apply to every agent class in the framework. Run
before declaring an agent class design complete.

**Naming and Type:**
```

T-01  Name is PascalCase with no spaces, hyphens, or underscores
T-02  Final name component is in the doer word vocabulary or is 'Owner'
T-03  If name ends in 'Orchestrator' or 'Owner': user-invokable is true
T-04  If name does NOT end in 'Orchestrator' or 'Owner':
user-invokable is false or absent (defaults to false)

```

**Agent File:**
```

T-05  Agent file content is ≤15 lines (excluding --- delimiters)
T-06  Agent file contains no file paths
T-07  Agent file contains no policy references
T-08  Agent file instructions are ≤4 lines
T-09  Agent file instructions include get_context_card call
T-10  Agent file instructions include raise_uncertainty reference
T-11  Agent file contains no task-specific content

```

**Tool Allocation:**
```

T-12  Agent holds all four universal tools:
get_context_card, get_my_capabilities,
get_current_state, raise_uncertainty
T-13  EXECUTOR and REVIEWER agents do not hold the 'agent' tool
T-14  ORCHESTRATOR agents declare an 'agents:' list with ≥2 entries
T-15  No agent holds both submit_{doc} and submit_qa_review_{doc}
for the same document (P8 — execution/verification separation)
T-16  No REVIEWER agent holds write_, append_, or submit_ tools
for documents produced by the Executor it reviews
T-17  For each tool in the list: a one-sentence justification
exists in the agent class definition

```

**Skill File:**
```

T-18  Skill file exists at .github/skills/{agent-class}.skill.md
T-19  Skill file contains no task-specific content
T-20  Skill file contains no file paths
T-21  Skill file contains no policy document references
T-22  Skill file reference exists in the agent class definition
NOTE: VS Code delivers this — no read tool required or permitted.
A read_ tool for a skill file is an automatic T-16 violation.

```

**Agent Class Definition:**
```

T-23  Agent class definition exists at
.framework/agent-classes/{agent-class}.agent-class.md
T-24  Agent type is declared and valid
(ORCHESTRATOR | OWNER | EXECUTOR | REVIEWER)
T-25  Certainty threshold is declared (0.0–1.0)
T-26  REVIEWER agent certainty threshold is ≥ 0.9
T-27  OWNER agent declares gate authority scope
T-28  Pattern tags are declared (≥1 tag required)
T-29  Agent class is registered in the framework manifest

```

---

## Known Agent Classes

| Agent Class | Type | user-invokable | Status |
|---|---|---|---|
| `FrameworkOwner` | OWNER | ✅ | Defined |
| `FeatureOwner` | OWNER | ✅ | Defined |
| `TaskOwner` | OWNER | ✅ | Defined |
| `UncertaintyOwner` | OWNER | ✅ | Defined |
| `TaskOrchestrator` | ORCHESTRATOR | ✅ | To be designed |
| `DeliveryOrchestrator` | ORCHESTRATOR | ✅ | To be designed |
| `ContextCurator` | EXECUTOR | ❌ | To be designed |
| `TaskPerformer` | EXECUTOR | ❌ | To be designed |
| `QAExecutor` | EXECUTOR | ❌ | To be designed |
| `TemplateAuthor` | EXECUTOR | ❌ | To be designed |
| `SpecValidator` | EXECUTOR | ❌ | To be designed |
| `ProofDesigner` | EXECUTOR | ❌ | To be designed |
| `UIDesigner` | EXECUTOR | ❌ | To be designed |
| `Deployer` | EXECUTOR | ❌ | To be designed |
| `ProofReviewer` | REVIEWER | ❌ | To be designed |
| `ACReviewer` | REVIEWER | ❌ | To be designed |
| `EnvironmentReviewer` | REVIEWER | ❌ | To be designed |

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-04 | Initial. Two-layer model formalised. Four agent types defined. 29 spec tests established. Known agent class roster recorded. |
```


***

## `.framework/templates/agent-class-definition-template.md`

```markdown
# Agent Class Definition — {AgentClassName}

**Agent Class:** {AgentClassName}
**Agent Type:** {ORCHESTRATOR | OWNER | EXECUTOR | REVIEWER}
**Kebab ID:** {agent-class-name}
**Version:** 1.0
**Status:** {DRAFT | ACTIVE | DEPRECATED}
**Created:** {YYYY-MM-DD}
**Last Updated:** {YYYY-MM-DD}

---

## Purpose

<!-- 2–3 sentences. What problem does this agent class solve?
     Why does it exist as a separate class rather than being
     part of an existing class? -->

---

## Agent Type Justification

<!-- One sentence: why is this type correct for this class?
     "This agent is a REVIEWER because it independently verifies
     [X] and must not hold write access to documents it reviews." -->

---

## Certainty Threshold

**Value:** {0.0–1.0}

<!-- Justify the threshold. Why is this the right level for this
     agent's decisions? REVIEWER agents must be ≥ 0.9. -->

---

## Gate Authority
<!-- OWNER agents only. Delete this section for other types. -->

**Domain:** {What this Owner has authority over}
**Can approve:** {list}
**Can reject:** {list}
**Can halt:** {list}
**Cannot:** {explicit scope limits}

---

## Subagent Delegation Protocol
<!-- ORCHESTRATOR agents only. Delete this section for other types. -->

**Delegates to:**

| Subagent | When | Expected output |
|---|---|---|
| {SubagentName} | {condition} | {output format} |

**Delegation rules:**
<!-- How does this Orchestrator decide what to delegate, in what
     order, and how does it synthesise results? -->

---

## Tool List

### Universal Tools (all agents)
| Tool | Justification |
|---|---|
| `get_context_card` | Load task brief at instantiation |
| `get_my_capabilities` | Inspect own registered tool list |
| `get_current_state` | Check task lifecycle state |
| `raise_uncertainty` | Signal blocked or uncertain state to human |

### Role-Scoped Tools
| Tool | Justification |
|---|---|
| {tool_name} | {one sentence — why does this agent need this tool?} |

### Task-Scoped Tools (dynamically assigned at task activation)
| Tool pattern | Justification |
|---|---|
| `{verb}_{subject}_{task_id}` | {one sentence} |

### Orchestrator Tools
<!-- ORCHESTRATOR and OWNER agents only. Delete for EXECUTOR/REVIEWER. -->
| Tool | Justification |
|---|---|
| `agent` | Delegate work to subagents |

---

## P8 Verification Check

<!-- For each document in this agent's write scope, confirm that
     no other tool in this list allows this agent to verify its
     own output. -->

| Document | This agent writes via | Reviews are done by |
|---|---|---|
| {document_type} | {tool_name} | {ReviewerAgentClass} |

**Conflicts:** {None | describe any identified conflict}

---

## Skill File

**Path:** `.github/skills/{agent-class}.skill.md`
**Covers:**
- {bullet list of what role knowledge the skill file contains}

---

## Pattern Tags

<!-- Tags used by ContextCurator to select relevant patterns
     for this agent's context cards. -->

**Primary tags:** {tag-1}, {tag-2}
**Secondary tags:** {tag-3}, {tag-4}

---

## Context Card Notes

<!-- Anything the ContextCurator should know when building cards
     for this agent class that isn't captured by the tags alone.
     e.g. "Always include the proof template pattern if one exists
     for the task domain." -->

---

## Spec Test Results

<!-- Complete before marking Status: ACTIVE -->

| Test | Result | Notes |
|---|---|---|
| T-01 Name PascalCase | ✅ / ❌ | |
| T-02 Doer word suffix | ✅ / ❌ | |
| T-03/T-04 user-invokable | ✅ / ❌ | |
| T-05 Agent file ≤15 lines | ✅ / ❌ | |
| T-06 No file paths | ✅ / ❌ | |
| T-07 No policy refs | ✅ / ❌ | |
| T-08 Instructions ≤4 lines | ✅ / ❌ | |
| T-09 get_context_card call | ✅ / ❌ | |
| T-10 raise_uncertainty ref | ✅ / ❌ | |
| T-11 No task content | ✅ / ❌ | |
| T-12 All universal tools | ✅ / ❌ | |
| T-13 No 'agent' tool (EX/RE) | ✅ / ❌ | N/A if ORCH/OWNER |
| T-14 agents: list (ORCH) | ✅ / ❌ | N/A if not ORCH |
| T-15 No exec/verify conflict | ✅ / ❌ | |
| T-16 Reviewer read-only | ✅ / ❌ | N/A if not REVIEWER |
| T-17 Tool justifications | ✅ / ❌ | |
| T-18 Skill file exists | ✅ / ❌ | |
| T-19–21 Skill file clean | ✅ / ❌ | |
| T-22 Skill via VS Code only | ✅ / ❌ | |
| T-23 Class definition exists | ✅ / ❌ | |
| T-24 Type declared | ✅ / ❌ | |
| T-25 Threshold declared | ✅ / ❌ | |
| T-26 Reviewer threshold ≥0.9 | ✅ / ❌ | N/A if not REVIEWER |
| T-27 Owner gate authority | ✅ / ❌ | N/A if not OWNER |
| T-28 Pattern tags declared | ✅ / ❌ | |
| T-29 Registered in manifest | ✅ / ❌ | |

---

## Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | {date} | Initial definition |
```


***

## `.framework/templates/agent-file-template.md`

```markdown
# Agent File Template

**For:** All agent classes
**Constraint:** ≤15 lines of content (excluding --- delimiters)
**Reference:** Agent Design Standards v1.0, Platform Constraints v1.0

---

## EXECUTOR / REVIEWER (user-invokable: false)

~~~yaml
---
name: {AgentClassName}
description: "{One sentence, active voice — what this agent actively does.}"
model: claude-sonnet-4-5
user-invokable: false
tools:
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - raise_uncertainty
  - {role_scoped_tool_1}
  - {role_scoped_tool_2}
---

Call `get_context_card` to load your brief before starting.
{One sentence primary directive — what to do, not how to do it.}
Call `raise_uncertainty` immediately if blocked or uncertain.
~~~

---

## ORCHESTRATOR (user-invokable: true, delegates to subagents)

~~~yaml
---
name: {AgentClassName}Orchestrator
description: "{One sentence — what workflow this orchestrator coordinates.}"
model: claude-sonnet-4-5
user-invokable: true
tools:
  - agent
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - raise_uncertainty
  - {role_scoped_tool_1}
agents:
  - {SubagentClassName1}
  - {SubagentClassName2}
  - {SubagentClassName3}
---

Call `get_context_card` to load your brief.
Delegate to {SubagentClassName1}, then {SubagentClassName2} and
{SubagentClassName3} in parallel. Synthesise results.
Call `raise_uncertainty` if any subagent returns failure.
~~~

---

## OWNER (user-invokable: true, holds gate authority)

~~~yaml
---
name: {Domain}Owner
description: "{One sentence — what domain this Owner has authority over.}"
model: claude-sonnet-4-5
user-invokable: true
tools:
  - get_context_card
  - get_my_capabilities
  - get_current_state
  - raise_uncertainty
  - {write_domain_doc}
  - {submit_or_request_tool}
---

Call `get_context_card` to load your brief.
{One sentence — what authority decision this Owner makes.}
Call `raise_uncertainty` before any irreversible state transition
if confidence is below your certainty threshold.
~~~

---

## Line Count Check

Count content lines only (not --- delimiters, not blank lines before
first content, not trailing blank lines).

If your agent file exceeds 15 content lines, the excess belongs in:
- The skill file (role knowledge)
- The context card (task knowledge)
- The agent class definition (governance record)

Not in the agent file. The agent file is an identity declaration,
not a specification.
```


***

Three documents, derivation complete. The standards are the load-bearing layer — the templates are entirely derived from them, which means if a standard changes, the template change is obvious. The spec test checklist in the class definition template means every new agent class self-certifies against the 29 tests before it reaches the manifest.

The natural next step from here is designing the first real agent classes — probably `TaskOrchestrator` and `TaskPerformer` as the canonical pair, since they model the primary coordinator/executor relationship. But that's probably best done once the zone policies are in place so the task lifecycle is defined first.

---

# Thanks. The work lifecycle will be interesting now that we have established the principles and now including subagents.

Let's start with the zone policies

This is the most complex document in the framework — the zone policies have to hold together the state machine, the authority model, the subagent activation patterns, and the gate conditions, all consistently. Let me think out loud about the structure before writing, so the design decisions are visible.

***

## Design Decisions Before Writing

**How many zones?**

```
Zone 0   Framework Governance    FrameworkOwner territory
Zone 1   Feature Definition      FeatureOwner territory
Zone 2   Task Specification      TaskOwner territory
Zone 3   Context Preparation     ContextCurator territory
Zone 4   Task Execution          TaskOrchestrator territory
Zone 5   Delivery                DeliveryOrchestrator territory
```

**Zone 4 is the most complex by far.** It now contains a full subagent orchestration tree:

```
TaskOrchestrator
  └── TaskPerformer (EXECUTOR)
  └── QAExecutor (EXECUTOR — coordinates its own reviewers)
        ├── ProofReviewer    (REVIEWER — parallel)
        ├── ACReviewer       (REVIEWER — parallel)
        └── EnvironmentReviewer (REVIEWER — parallel)
```

**The full task state machine:**

```
DRAFT → FEATURE_APPROVED → SPECIFIED → CONTEXT_READY
→ IN_PROGRESS → SUBMITTED → QA_IN_PROGRESS
→ QA_PASSED → AWAITING_APPROVAL → APPROVED
→ DEPLOYING → DONE

Lateral states (any zone):
  BLOCKED         raised via raise_uncertainty
  AWAITING_HUMAN  raised via request_
  QA_FAILED       → back to IN_PROGRESS (rework loop)
```

Now the documents:

***

## `.framework/policies/zone-policies.md`

```markdown
# Zone Policies

**Version:** 1.0
**Status:** Active
**Principles implemented:** P1, P3, P4, P5, P8, P9, P10, P12
**Dependencies:**
  Agent Design Standards v1.0
  Tool Grammar v0.3
  Audit Log Schema v1.0
  Naming Conventions v0.1
**Last Updated:** 2026-03-04

---

## Purpose

This document defines the zones through which all work moves in this
framework. Each zone has a defined:
- Purpose and scope
- Entry conditions (what must be true before work enters)
- Authority model (who owns decisions in this zone)
- Agent activation pattern (which agents operate here)
- Exit conditions and gate (what triggers the transition to the next zone)
- Failure handling (what happens when work cannot proceed)

Zones are not optional stages. They are the framework's primary
mechanism for separating concerns, enforcing authority boundaries,
and ensuring that work does not advance until it is genuinely ready.

**An important constraint: agents do not know what zone they are in.**
Zone membership is a governance concept for humans and the Policy Engine.
Agents receive task-specific context cards and task-scoped tools. The
zone policy governs which cards and tools they receive — but the agent
itself is never told "you are in Zone 4." This is by design: agents
that know their zone can route around zone gates.

---

## Zone Map

```

ZONE 0          ZONE 1          ZONE 2          ZONE 3
Framework       Feature         Task            Context
Governance      Definition      Specification   Preparation
────────────    ────────────    ────────────    ────────────
FrameworkOwner  FeatureOwner    TaskOwner       ContextCurator
UncertaintyOwner

ZONE 4          ZONE 5
Task            Delivery
Execution       ────────────
────────────    DeliveryOrchestrator
TaskOrchestrator  Deployer
TaskPerformer
QAExecutor
ProofReviewer
ACReviewer
EnvironmentReviewer
UncertaintyOwner

```

---

## Task State Machine

A task moves through the following states. Each state belongs to exactly
one zone. State transitions are performed by MCP tools — no transition
happens outside a tool call, and every tool call that causes a transition
produces an audit entry and a stream event.

```

                            ┌─────────────────────────────────────────┐
                            │  CROSS-ZONE LATERAL STATES               │
                            │  BLOCKED        (any zone, any state)    │
                            │  AWAITING_HUMAN (any zone, any state)    │
                            └─────────────────────────────────────────┘
    Zone 1    DRAFT
│  FeatureOwner submits feature spec + AC
▼
FEATURE_APPROVED
│  TaskOwner acknowledges, enters Zone 2
▼
Zone 2    SPECIFIED
│  TaskOwner submits task spec
▼
TASKS_APPROVED
│  ContextCurator activates, enters Zone 3
▼
Zone 3    CONTEXT_READY
│  ContextCurator confirms card is current
│  Nexus server assigns task-scoped tools
▼
Zone 4    IN_PROGRESS
│  TaskPerformer submits proof
▼
SUBMITTED
│  QAExecutor activates
▼
QA_IN_PROGRESS
│  All three reviewers return verdicts
▼
QA_PASSED ─────────────────────────────────▶ QA_FAILED
│  QAExecutor submits passing review               │
▼                                                  │
AWAITING_APPROVAL                                    │
│  human:approver approves                         │
▼                                                  │
APPROVED ◀────────────────────────────────────────── ┘
│  (rework loop — back to IN_PROGRESS)
│  [on first APPROVED] DeliveryOrchestrator activates
▼
Zone 5    DEPLOYING
│  Deployer confirms successful deployment
▼
DONE

Terminal states:
REJECTED    — Owner explicitly rejects work as non-viable
CANCELLED   — FrameworkOwner cancels task

```

**Rework loop:**
`QA_FAILED` returns to `IN_PROGRESS`, not to `SPECIFIED`. The task
specification is not reopened for a failed implementation — the
TaskPerformer reworks within the existing specification. If the
specification is the cause of failure, a new uncertainty is raised
and the task returns to Zone 2 via the BLOCKED → AWAITING_HUMAN path.

---

## Zone 0 — Framework Governance

### Purpose

Zone 0 is not a stage in the task lifecycle. It is the standing
governance layer that exists above and across all other zones. It
defines the rules, policies, and structures that the other zones
operate within.

Work in Zone 0 is framework work, not product work. Adding a new
agent class, revising a policy, running an experiment, updating the
pattern library — all of this is Zone 0 work.

### Authority

**FrameworkOwner** holds sole write authority in Zone 0.

No other agent or human actor may modify framework documents, policies,
schema definitions, or the pattern library without FrameworkOwner
approval. This is enforced at the tool level — only FrameworkOwner
holds `write_patterns` and the write tools for framework documents.

### Agent Activation

Zone 0 does not follow the standard task lifecycle. Work here is
managed as a direct session between human:director and FrameworkOwner.

Agents that may be activated in Zone 0:
- `FrameworkOwner` (primary)
- `TemplateAuthor` (for producing new agent templates)
- `SpecValidator` (for validating proposed agent class designs)
- `ContextCurator` (for pattern library maintenance)

### Zone 0 Gate

There is no automatic gate in or out of Zone 0. All Zone 0 work
is initiated and concluded by human:director with FrameworkOwner.

### Failure Handling

Framework uncertainties raised in Zone 0 are owned by FrameworkOwner.
They are not routed to UncertaintyOwner — Zone 0 failures are
framework design failures, not task execution failures, and must be
resolved at the source.

---

## Zone 1 — Feature Definition

### Purpose

Zone 1 is where a feature is defined. A feature is a coherent unit
of product work that will be decomposed into one or more tasks in
Zone 2. Zone 1 is complete when the feature has an approved spec and
a complete, approved set of acceptance criteria.

Nothing enters Zone 2 without passing the Zone 1 gate. A task with
an undefined or unapproved feature spec is underspecified and will
produce Zone 4 failures.

### Entry Conditions

Work enters Zone 1 when human:director publishes a feature request.
The minimum content of a feature request:
- Feature ID (assigned by the system: `feat-xxx`)
- Feature name (plain English)
- Problem statement (what user problem this solves)
- Out-of-scope statement (what this feature explicitly does NOT do)

A feature request without an out-of-scope statement is incomplete
and must not enter Zone 1. Undefined scope is the primary source of
Zone 4 rework.

### Authority

**FeatureOwner** owns Zone 1.

FeatureOwner writes the feature spec and AC. human:approver approves
or rejects. No other agent has write authority over Zone 1 documents.

### Agent Activation

| Agent | Role | Activated by |
|---|---|---|
| `FeatureOwner` | Writes feature spec and AC | human:director |
| `ProofDesigner` | Defines proof of completion for the feature | FeatureOwner |
| `UIDesigner` | Writes UI brief if feature is UI-bearing | FeatureOwner |

No executor subagents are active in Zone 1. Zone 1 is definition work,
not implementation work.

### Zone 1 State Transitions

| Transition | Tool | Actor | Produces |
|---|---|---|---|
| Publish feature request | `write_feature_spec` | FeatureOwner | `DRAFT` state |
| Submit AC | `submit_ac` | FeatureOwner | Stream event to human:approver |
| Approve | `request_ac_approval` → human approves | human:approver | `FEATURE_APPROVED` |
| Reject | — | human:approver | `BLOCKED` with reason |

### Zone 1 Gate

**Exit condition:** Feature spec is approved AND AC is approved AND
at least one acceptance criterion is measurable (verifiable by a
reviewer without access to the author's intent).

**Gate authority:** human:approver

**Gate failure:** Feature returns to DRAFT with rejection notes. If
the same feature is rejected twice, FrameworkOwner is notified via
stream event — a pattern of Zone 1 rejections indicates a structural
problem with how features are being defined.

### Failure Handling

Zone 1 failures are definition failures — the feature as specified
cannot be built as described, or the scope is ambiguous. These are
raised as uncertainties to UncertaintyOwner, who routes to
human:approver for resolution.

---

## Zone 2 — Task Specification

### Purpose

Zone 2 decomposes an approved feature into tasks. Each task is a
discrete, independently completable unit of work with a defined proof
of completion. Zone 2 is complete when every task in the feature
decomposition has an approved spec, a proof template, and a task
branch created.

### Entry Conditions

- Feature status is `FEATURE_APPROVED`
- Feature spec and AC are accessible to TaskOwner
- ContextCurator has been notified (via stream event) to prepare
  role-level context cards for Zone 4 agent classes

### Authority

**TaskOwner** owns Zone 2.

TaskOwner writes task specs and proof templates. TaskOwner also owns
the decomposition document — the mapping of feature → tasks.

**UncertaintyOwner** is also active in Zone 2 as the routing authority
for specification ambiguities. If a task cannot be specified without
resolving an ambiguity in the feature spec, UncertaintyOwner gates
the task until the ambiguity is resolved.

### Agent Activation

| Agent | Role | Activated by |
|---|---|---|
| `TaskOwner` | Writes task specs and proof templates | human:director or FeatureOwner |
| `UncertaintyOwner` | Routes specification ambiguities | Auto (on raise_uncertainty) |
| `SpecValidator` | Validates task specs against design standards | TaskOwner |

### Zone 2 State Transitions

| Transition | Tool | Actor | Produces |
|---|---|---|---|
| Write task spec | `write_task_spec_{task_id}` | TaskOwner | Task record created |
| Write proof template | `write_proof_template_{task_id}` | TaskOwner | Proof template stored |
| Submit for validation | `submit_task_spec_{task_id}` | TaskOwner | `SPECIFIED` state |
| Validate spec | `submit_spec_validation_{task_id}` | SpecValidator | PASS / FAIL verdict |
| Approve | — | human:approver (or auto if validator passes) | `TASKS_APPROVED` |
| Add to decomposition | `append_decomposition` | TaskOwner | Decomposition updated |

### Zone 2 Gate

**Exit conditions (all must be true per task):**
- Task spec is approved
- Proof template is approved (defines exactly what done looks like)
- Task has a branch name assigned (`task/{task_id}`)
- ContextCurator has confirmed it has sufficient information to
  build a context card for the TaskOrchestrator

**Gate authority:** human:approver (or SpecValidator auto-approval
if the spec validator passes and no uncertainty flags are open)

**Gate failure:** Task returns to DRAFT state in Zone 2. If the
failure is due to a feature-level ambiguity (the task cannot be
specified because the feature spec is ambiguous), the feature spec
is returned to Zone 1 for revision. This is the only backwards
state transition in the framework — Zone 2 → Zone 1 — and it
requires UncertaintyOwner approval to execute.

### Failure Handling

All Zone 2 failures route to UncertaintyOwner. UncertaintyOwner
classifies them:
- **Specification ambiguity** → route to FeatureOwner for feature
  spec update (Zone 2 → Zone 1 reroute)
- **Task boundary conflict** → route to TaskOwner for decomposition
  revision
- **Missing acceptance criterion** → route to FeatureOwner for AC
  update

---

## Zone 3 — Context Preparation

### Purpose

Zone 3 prepares agents for execution. It is a short-lived zone —
its entire purpose is to ensure that when a TaskOrchestrator receives
a task, it has a current, valid context card and all task-scoped
tools are registered.

Zone 3 exists as a distinct zone because context preparation is a
non-trivial operation (pattern selection, conflict detection, constraint
distillation) and because it must complete before Zone 4 can begin.
Merging Zone 3 and Zone 4 would mean the TaskOrchestrator might
receive a stale or incomplete card.

### Entry Conditions

- Task status is `TASKS_APPROVED`
- All task documents are accessible to ContextCurator
- Pattern library is current (no pending promotions that would change
  context card composition for this task type)

### Authority

**ContextCurator** owns Zone 3.

Zone 3 is the only zone with no human gate on exit (under normal
conditions). Context preparation is a mechanical operation governed
by the Context Curation Policy. If the ContextCurator cannot produce
a valid context card (e.g. a pattern conflict it cannot resolve), it
raises an uncertainty that routes to FrameworkOwner.

### Agent Activation

| Agent | Role | Activated by |
|---|---|---|
| `ContextCurator` | Builds context cards for all Zone 4 agents | Auto (on TASKS_APPROVED) |

ContextCurator prepares context cards for:
- `TaskOrchestrator` (ORCHESTRATOR card)
- `TaskPerformer` (EXECUTOR card, task-scoped)
- `QAExecutor` (EXECUTOR card, task-scoped)
- `ProofReviewer`, `ACReviewer`, `EnvironmentReviewer` (SUBAGENT cards)

All six cards are prepared before Zone 4 activates. This is a
deliberate design choice: subagent cards are pre-prepared rather than
generated on demand, so the QAExecutor's subagent activation in Zone 4
is instant.

### Zone 3 State Transitions

| Transition | Tool | Actor | Produces |
|---|---|---|---|
| Begin context prep | `get_current_state` → `write_context_card` | ContextCurator | Cards generated |
| Register task tools | System operation | system:nexus | Task-scoped tools registered |
| Confirm ready | `submit_context_ready_{task_id}` | ContextCurator | `CONTEXT_READY` state |

### Zone 3 Gate

**Exit condition:** All six context cards are generated and current.
All task-scoped tools for Zone 4 agents are registered in the
Nexus server tool registry.

**Gate authority:** ContextCurator (automatic — no human gate)

**Exception:** If ContextCurator raises an uncertainty during
card preparation (e.g. unresolvable pattern conflict), the task
holds at `TASKS_APPROVED` until the uncertainty is resolved.

### Failure Handling

Zone 3 failures are framework failures (pattern library gaps, policy
conflicts) or task definition failures (task spec doesn't provide
enough information to select relevant patterns). Both route to
FrameworkOwner via UncertaintyOwner.

---

## Zone 4 — Task Execution

### Purpose

Zone 4 is where the work happens. A TaskOrchestrator receives a task,
delegates implementation to a TaskPerformer, coordinates QA review
via QAExecutor and its reviewer subagents, and gates the result for
human approval.

Zone 4 is the most structurally complex zone because it contains a
nested subagent tree. The design principles that govern it are:

- **P8:** TaskPerformer executes. QAExecutor reviews. These are
  structurally separate and may never be collapsed into one agent.
- **P7:** Each subagent receives only the context it needs for its
  specific responsibility. The QAExecutor does not receive the
  TaskPerformer's full context. The ProofReviewer does not receive
  the ACReviewer's full context.
- **P9:** Any agent in Zone 4 may raise an uncertainty at any time.
  A blocked TaskPerformer does not wait silently — it calls
  `raise_uncertainty` immediately.

### Entry Conditions

- Task status is `CONTEXT_READY`
- All six context cards are confirmed current
- All task-scoped tools are registered
- TaskOrchestrator is activated by the Nexus task event

### Authority

**TaskOrchestrator** owns Zone 4 execution.

The TaskOrchestrator is the only Zone 4 agent that is user-invokable.
All other Zone 4 agents receive work exclusively through the
orchestration chain.

**human:approver** owns the Zone 4 exit gate (AWAITING_APPROVAL →
APPROVED). No task exits Zone 4 without explicit human approval.

### Agent Activation Tree

```

ACTIVATED BY SYSTEM (on CONTEXT_READY)
└── TaskOrchestrator
│
│  [delegates implementation]
▼
TaskPerformer
│  calls: read_task_spec_{task_id}
│         append_work_log_{task_id}
│         search_knowledge_base
│         submit_proof_{task_id}
│  on completion: submits proof → state → SUBMITTED
│
│  [TaskOrchestrator activates QAExecutor]
▼
QAExecutor
│  calls: read_proof_template_{task_id}
│         read_proof_{task_id}
│         read_task_spec_{task_id}
│  [activates three reviewer subagents in parallel]
│
├── ProofReviewer
│     reads: proof_template, proof
│     returns: PASS/FAIL with evidence
│
├── ACReviewer
│     reads: ac, proof
│     returns: PASS/FAIL with evidence
│
└── EnvironmentReviewer
reads: environment_contract, proof
returns: PASS/FAIL with evidence
│
│  [QAExecutor synthesises all three verdicts]
│  [submits qa_review → QA_PASSED or QA_FAILED]
▼
TaskOrchestrator receives result
│
├── QA_PASSED → request_approval → AWAITING_APPROVAL
│               human:approver approves → APPROVED
│
└── QA_FAILED → routes back to TaskPerformer for rework
rework counter incremented
if rework_count > 2 → raise_uncertainty

```

### Zone 4 State Transitions

| Transition | Tool | Actor | Produces |
|---|---|---|---|
| Begin implementation | `get_context_card` | TaskPerformer | IN_PROGRESS state |
| Log work | `append_work_log_{task_id}` | TaskPerformer | Audit entry |
| Submit proof | `submit_proof_{task_id}` | TaskPerformer | `SUBMITTED` state + stream event |
| Begin QA | `get_context_card` | QAExecutor | `QA_IN_PROGRESS` state |
| Activate reviewers | `agent` tool | QAExecutor | Three subagents spawn |
| Submit passing review | `submit_qa_review_{task_id}` | QAExecutor | `QA_PASSED` state |
| Submit failing review | `submit_qa_review_{task_id}` | QAExecutor | `QA_FAILED` state |
| Request approval | `request_approval_{task_id}` | TaskOrchestrator | `AWAITING_APPROVAL` + stream event to human:approver |
| Approve | — | human:approver | `APPROVED` state |
| Reject | — | human:approver | Returns to `IN_PROGRESS` with notes |
| Raise uncertainty | `raise_uncertainty` | Any Zone 4 agent | `BLOCKED` state |

### The Rework Loop

`QA_FAILED` returns the task to `IN_PROGRESS`. The TaskOrchestrator
routes the QAExecutor's failure report to the TaskPerformer with
the specific unmet criteria. The TaskPerformer does not reload its
full context card — it receives the failure report directly from
the orchestrator as its rework brief.

**Rework counter rules:**
- Rework count is tracked in the task record
- After 2 failed QA attempts, the TaskOrchestrator must call
  `raise_uncertainty` before initiating a third rework
- This forces human:approver to review the QA failures before
  authorising further execution cycles
- The uncertainty must include all QA failure reports as context

The rework counter resets to zero when the task advances to
`APPROVED`. It does not reset between QA_FAILED and IN_PROGRESS
within a single approval cycle.

### Parallel QA — Design Rationale

The three reviewer subagents (ProofReviewer, ACReviewer,
EnvironmentReviewer) run in parallel for a structural reason:
they are independent verification perspectives, not a sequential
pipeline. ProofReviewer asking "does the proof document satisfy
the template?" is a completely different question from ACReviewer
asking "does the implementation satisfy the acceptance criteria?"
These questions do not depend on each other's answers.

Parallel execution means:
- Each reviewer has a clean, uncontaminated context window
- A failure in one review does not cause the others to abort
- All three verdicts are available to QAExecutor simultaneously,
  enabling a complete consolidated failure report in a single
  pass rather than sequential failure discovery

**QAExecutor synthesis rule:**
If any reviewer returns FAIL, QAExecutor returns QA_FAILED with a
consolidated report. It does not re-run the passing reviewers. It
does not request partial acceptance. All criteria must pass in the
same QA cycle for the task to advance.

### Zone 4 Gate

**Exit condition:** QA has passed AND human:approver has explicitly
approved the task output.

**Gate authority:** human:approver — non-delegatable. No agent,
regardless of type, may approve a task for Zone 5 delivery.

**Why no auto-approval?**
Zone 4 → Zone 5 is an irreversible state transition. Once a task
is approved for delivery it enters the deployment pipeline.
P10 (irreversible states require human authority) applies here
absolutely. QA passing is a necessary condition for approval but
it is not sufficient — a human must confirm that the output is
appropriate for deployment in the current project context.

### Failure Handling

Any Zone 4 agent may call `raise_uncertainty` at any time. The
result is always `BLOCKED` state and an immediate priority stream
event to human:approver.

**Common Zone 4 uncertainty patterns:**
- TaskPerformer cannot implement a task because the spec
  contradicts the AC
- TaskPerformer discovers an undeclared dependency
- A reviewer finds that the proof template does not match what
  was actually built (template written for a different
  interpretation of the spec)
- All three rework attempts have failed (rework counter exceeded)

All of these are routed to UncertaintyOwner for classification
before reaching human:approver.

---

## Zone 5 — Delivery

### Purpose

Zone 5 takes approved task output and delivers it to the target
environment. Zone 5 is complete when the deployment is confirmed
successful and the task is marked DONE.

Zone 5 is deliberately narrow. It does not involve implementation
decisions or review decisions — both of those happened in Zone 4.
Zone 5 only answers the question: "Did the approved output reach
the target environment intact?"

### Entry Conditions

- Task status is `APPROVED`
- human:approver approval is recorded in audit_log
- Target environment is accessible (environment contract confirmed)
- Deployment branch matches the task branch convention
  (`task/{task_id}`)

### Authority

**DeliveryOrchestrator** owns Zone 5 execution.

**human:approver** owns the Zone 5 gate (deployment confirmation
requires human acknowledgement of the DONE state).

### Agent Activation

| Agent | Role | Activated by |
|---|---|---|
| `DeliveryOrchestrator` | Coordinates deployment workflow | Auto (on APPROVED) |
| `Deployer` | Executes deployment to target environment | DeliveryOrchestrator |
| `EnvironmentReviewer` | Confirms post-deployment environment state | DeliveryOrchestrator |

Zone 5 reuses `EnvironmentReviewer` from Zone 4's QA tree for
post-deployment validation. This is deliberate — the same reviewer
that confirmed the environment contract pre-deployment also confirms
the environment state post-deployment, maintaining a consistent
verification lens.

### Zone 5 State Transitions

| Transition | Tool | Actor | Produces |
|---|---|---|---|
| Begin deployment | `get_context_card` | DeliveryOrchestrator | `DEPLOYING` state |
| Execute deployment | Deployer tools | Deployer | Deployment artefacts |
| Validate environment | EnvironmentReviewer tools | EnvironmentReviewer | Post-deploy confirmation |
| Confirm done | `submit_deployment_{task_id}` | DeliveryOrchestrator | `DONE` state + stream event |
| Rollback | `raise_uncertainty` | DeliveryOrchestrator | `BLOCKED` state |

### Zone 5 Gate

**Exit condition:** Deployment confirmed successful by
EnvironmentReviewer AND human:approver acknowledges DONE state.

**Gate authority:** human:approver (acknowledgement, not decision —
the deployment either succeeded or it didn't)

**Gate failure:** If deployment fails, DeliveryOrchestrator raises
an uncertainty immediately. The task returns to `APPROVED` state —
not to Zone 4. The implementation is not in question; the delivery
mechanism is. Resolution is a Zone 5 / Zone 0 problem depending on
whether the issue is environment-specific or framework-level.

### Failure Handling

Zone 5 failures are delivery failures. They do not invalidate Zone 4
work. A failed deployment does not require re-implementation or
re-review — it requires a deployment problem to be resolved.

If the same task fails deployment twice, FrameworkOwner is notified.
A pattern of Zone 5 failures on a specific environment signals an
infrastructure problem that must be addressed at the Zone 0 level
before further deliveries are attempted.

---

## Cross-Zone Rules

### BLOCKED State

Any agent in any zone may call `raise_uncertainty`. This immediately:
1. Transitions the task to `BLOCKED` state
2. Writes a priority audit entry
3. Emits a priority stream event to human:approver
4. Halts all agent activity on this task

**BLOCKED is not a failure state.** It is a safety state. An agent
that calls `raise_uncertainty` because it cannot proceed without
risking a wrong outcome is behaving correctly. BLOCKED tasks are
resolved, not penalised.

**Resolution authority:**
- UncertaintyOwner classifies the uncertainty and routes to the
  appropriate authority
- human:approver provides the resolution decision
- The agent that raised the uncertainty receives the resolution via
  an updated context card or a direct task note

### AWAITING_HUMAN State

Distinct from BLOCKED. AWAITING_HUMAN means the workflow requires
human input at a defined gate — this is expected and planned.
BLOCKED means an unexpected condition has halted progress.

A task in AWAITING_HUMAN is not blocked — it is waiting at a
defined handoff point.

### Backwards State Transitions

Only one backwards state transition is permitted in the framework:
**Zone 2 → Zone 1** (task specification reveals a feature spec
ambiguity that must be resolved before the task can be specified).

All other backwards movement is within a zone:
- Zone 4: QA_FAILED → IN_PROGRESS (within Zone 4, not a zone transition)

A task may never move backwards between zones other than Zone 2 → Zone 1,
and that transition requires UncertaintyOwner approval.

### Zone Isolation

Agents in Zone 4 do not have access to Zone 1 or Zone 2 documents
directly. TaskPerformer reads `task_spec_{task_id}` — it does not
read the feature spec or the AC document directly. These are distilled
into the task spec by TaskOwner in Zone 2.

This is enforced by tool allocation: TaskPerformer does not hold
`read_feature_spec` or `read_ac`. The information it needs from those
documents has been distilled into the task spec. This keeps the
TaskPerformer's context window focused on its task.

---

## Zone Summary

| Zone | Purpose | Entry gate | Exit gate | Auto-advance? |
|---|---|---|---|---|
| 0 | Framework governance | human:director | human:director | No |
| 1 | Feature definition | human:director | human:approver | No |
| 2 | Task specification | FEATURE_APPROVED | human:approver or SpecValidator | Conditional |
| 3 | Context preparation | TASKS_APPROVED | ContextCurator | Yes |
| 4 | Task execution | CONTEXT_READY | human:approver | No |
| 5 | Delivery | APPROVED | human:approver (acknowledgement) | Conditional |

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-04 | Initial. Six zones defined. Full task state machine. Subagent orchestration tree for Zone 4. Rework loop with counter. Parallel QA rationale. Cross-zone rules including BLOCKED vs AWAITING_HUMAN distinction. |
```


***

That's the zone policies complete. A few things worth flagging before we move on:

- **Zone 3 pre-generates all six cards** — that was a decision made in writing, not established before. Worth confirming this is the right call vs generating subagent cards on-demand when QAExecutor activates.
- **The rework counter threshold (>2)** is a reasonable starting point but should be tuned once Experiment 02 runs.
- **Zone 2 → Zone 1 backwards transition** is the only one — this needs a corresponding tool in the grammar: something like `request_feature_revision` which UncertaintyOwner holds.
- **Zone 5 reuses EnvironmentReviewer** — this means that agent class needs to be designed to serve both Zone 4 (pre-deployment contract review) and Zone 5 (post-deployment state confirmation), which has implications for its tool list.

Shall we go straight to the governance policies next, or do you want to address any of those flags first?

---

# ok. I see this as an opportunity to design the work lifecycle from first principles now that we have the other documentation in place.

Some of the documents we created before zone policies today might need some small updates but I think they are mostly sound and valuable foundations for what comes next.

Zone 0 won't need to change in its purpose but we will come back to this after we have mapped out the other zones as I feel there will be many opportunities for it to play an important and active role in the overall system.

The current zones were based on the event storming session which was valuable for initial prototyping in creating a proof of concept. It looked at the work lifecycle from idea to feature in production.

We are still experimenting here, however I want to take a broader view that includes bootstrapping of a new project and ongoing maintenance of an application.

Perhaps we take a higher layer view of "Product Lifecycle Phases":

Phase 0 - Concept and ideation of overall system/product: define product vision, scope and goals, defining business value; that produces a high level backlog, initial user stories, and a clear vision statement.

Phase 1 - Inception and planning of system/product: establish tech stack, team roster, define requirements; produces user personas, architecture, prioritised and manageable backlog, UX strategy, UI components

Phase 3 - Iteration and development: similar to our initial zones - decomposing user stories into tasks, designing, executing, testing etc

Phase 4 - Release/deployment: staging and production deployment, devops, user testing, user facing documentation etc

Phase 5 - Review \& retrospective: learnings from complete lifecycle

Phase 6 - Operations and maintenance: ongoing optimization, bug capture etc

I have based this phased approach on agile methodology but we are trying to take a first principles approach and reimagine the entire process, so I'm happy if you have different approaches to consider.

Since we have an agent-centric development process, it has changed the rules and logic, which gives us opportunities to innovate. Eg. retros - i like the idea of every agent writing a report at the end of their run that can be added into higher level retrospectives. And retros can happen at each phase or zone too.

Before we make any decisions on this, I'd like you to provide your analysis and findings on my suggestion. What other approaches are there for us to consider? What are strengths and weaknesses of each? What opportunities to innovate am I missing?

This is a genuinely important design decision — the lifecycle model shapes everything below it. Let me give you a thorough analysis before we make any commitments.

***

## Your Proposal — Assessment

First, a small flag: **Phase 2 is missing** from your numbering. This may be intentional, but worth confirming before we formalise anything.

### Strengths

- **Covers the full product horizon** — current zones only modelled development. Including bootstrapping, operations, and retros is the right scope for a framework that owns the whole process
- **Retro as a first-class concern** — most methodologies bolt retros on as a ceremony. You're treating them structurally, which aligns perfectly with agents producing terminal reports
- **Operations and maintenance included** — most agile frameworks treat this as someone else's problem. It belongs in the model
- **Phased approach is intuitive** — the language maps cleanly to how stakeholders think about product maturity


### Weaknesses

| Weakness | Why it matters |
| :-- | :-- |
| **Linear model doesn't reflect reality** | A mature product runs phases 3, 4, and 6 simultaneously. Sequential phases model a greenfield project, not ongoing development |
| **Phase 5 (Retro) as a discrete phase** | Implies it happens once, at the end. With agents producing terminal reports, retros should be continuous and nested — not a phase you reach |
| **Phase 1 conflates product and framework concerns** | "Team roster" in an agent-centric system means agent class design — which is Zone 0 / framework work, not product inception work. These need to stay separated |
| **Phase 3 carries disproportionate complexity** | A single "Iteration and Development" phase contains everything from user story decomposition to QA to deployment preparation. It needs internal structure, not just a label |
| **Operations is a loop, not an end state** | Phase 6 feeds back into Phase 0 or Phase 3 depending on what it surfaces. The model needs to show this explicitly |
| **No "shaping" concept** | There's a gap between ideation (Phase 0) and commitment to build (Phase 3). This is where the most expensive mistakes happen — ambiguity that survives into execution |


***

## Alternative Approaches

### 1. The Agile/Scrum Model (your current basis)

Sprints, ceremonies, backlog refinement, velocity tracking.

**Strengths:** Familiar, battle-tested, strong tooling ecosystem[^31_1]
**Weaknesses:** Built for human team coordination overhead. Sprint ceremonies exist to synchronise humans — agents don't need standups. Backlog as a flat list is a weak model for priority reasoning. Velocity is meaningless when tasks are completed by agents at variable speeds.

**Verdict:** A reasonable starting point but too much human-coordination scaffolding that agents don't need. You'd be designing around ceremonies that have no value in an agent-centric system.

***

### 2. Shape Up (Basecamp)

Six-week cycles with a distinct shaping track that runs ahead of building. Work is shaped (ambiguity resolved, appetite set) before any commitment to build.[^31_2][^31_3]

**Core concepts:**

- **Shaping** — async, small team, resolves ambiguity before commitment
- **Betting** — deliberate selection of shaped work before a cycle starts
- **Building** — six weeks, uninterrupted, no backlog
- **Cool-down** — two weeks between cycles for cleanup and next shaping

**Strengths for an agent-centric system:**

- The shaping concept maps directly onto what Zone 2 needs — work that arrives at execution must be unambiguous enough for agents to act on it without constant uncertainty raises[^31_4]
- The "appetite" concept (how much time is this worth?) is a better model than story points for agent work
- No backlog is a provocative but defensible choice — a backlog is a list of work that hasn't been shaped yet and probably shouldn't exist until it has been

**Weaknesses:**

- Six-week cycles are human-calendar constructs. Agents don't have this constraint — cycles could be defined by scope, not time
- Doesn't address operations/maintenance
- Doesn't address bootstrapping a new product

**Verdict:** The shaping concept is the most valuable thing Shape Up contributes and is largely missing from your proposal. The cycle structure is less relevant.

***

### 3. The Agent Development Lifecycle (ADLC)

A purpose-built model for agentic systems, emerging from Salesforce, EPAM, and Arthur AI.[^31_5][^31_6][^31_7]

**Phases:** Ideation/Design → Development (inner loop) → Testing/Validation → Deployment → Monitoring/Tuning (outer loop)

**The key insight:** Deployment is not the end — it is the beginning of the outer loop. The outer loop (monitoring, tuning, learning) continuously feeds back into the inner loop (building).[^31_8]

**Strengths:**

- Inner loop / outer loop distinction is architecturally honest — agents never "finish," they continuously improve
- Monitoring and governance as a first-class phase, not an afterthought
- Acknowledges that agent behaviour is non-deterministic — testing and validation require different approaches than traditional QA[^31_5]

**Weaknesses:**

- Designed for the lifecycle of an agent system itself, not for the products agents build
- Doesn't address product ideation or inception
- Assumes a single agent system rather than a multi-agent orchestration framework

**Verdict:** The inner loop / outer loop model is a powerful structural idea. The specific phases are less relevant to your use case.

***

### 4. The Three Horizons Model

Runs three parallel tracks simultaneously for mature products:

- **Horizon 1** — Optimise and operate existing functionality
- **Horizon 2** — Actively develop and ship new features
- **Horizon 3** — Explore and shape emerging concepts

**Strengths:** Honest about how mature products actually run — they are always operating, building, and exploring simultaneously. Parallel execution is natural for agents in a way it isn't for human teams.

**Weaknesses:** Complex to bootstrap — you can't run all three tracks on day one of a new product. The model doesn't specify what Horizon 3 produces or how it becomes Horizon 2 work.

**Verdict:** The parallel track insight is valuable. The three-horizon framing is a useful executive communication tool but not precise enough to drive zone design.

***

### 5. Double Diamond (Design Thinking adapted)

Two diverge/converge cycles: the first finds the right problem, the second finds the right solution.

- **Diamond 1:** Discover (research broadly) → Define (narrow to the real problem)
- **Diamond 2:** Develop (explore solutions broadly) → Deliver (narrow to the shipped solution)

**Strengths:** Explicitly models the diverge/converge rhythm. Most methodologies only do the second diamond (solutions) and skip the first (problem validation).

**Weaknesses:** Designed for human collaborative workshops. Agents don't naturally "diverge" without structured prompting. The model doesn't address operations or maintenance at all.

**Verdict:** The problem/solution distinction in Diamond 1 / Diamond 2 is valuable and largely missing from your proposal. Phase 0 conflates "what problem are we solving?" with "what should we build?" — those are different questions requiring different agents.

***

## Innovation Opportunities You're Missing

These are the gaps that none of the existing methodologies address well, and where the agent-centric model gives you genuine leverage:

**1. The Shaping Zone**
Between ideation and commitment to build, there must be a zone where ambiguity is resolved to the precision threshold required for agents to operate without constant uncertainty raises. This is the most expensive missing piece. Work that hasn't been shaped properly to this threshold will generate `raise_uncertainty` calls in Zone 4 — which are expensive reroutes. Shaping is cheap. Rework is not.

**2. Nested Retrospective Pyramid**
Your instinct about agents writing terminal reports is exactly right — and it goes further than you described:

```
Agent terminal report     (every agent, every run)
    → Task retro          (aggregated by TaskOrchestrator)
        → Feature retro   (aggregated by FeatureOwner)
            → Phase retro (aggregated by FrameworkOwner)
                → Product retro (human:director + FrameworkOwner)
```

Each level aggregates the level below it. The Pattern Library is updated at every level. This means the framework learns continuously from every task, not just from scheduled retro events. Retro becomes infrastructure, not ceremony.

**3. Uncertainty as a Living Risk Register**
Every `raise_uncertainty` call is currently resolved and closed. But the aggregate of all uncertainty raises is a product risk register — patterns of uncertainty reveal structural gaps in specifications, in the framework, or in the product itself. An `UncertaintyOwner` that classifies and tracks uncertainty patterns could surface these insights automatically, replacing the need for manual risk management ceremonies.

**4. Framework Bootstrapping as a First-Class Phase**
Before any product phase can run, the framework must be configured for the specific project: agent classes designed or adapted, skill files written, pattern library seeded with any known project-specific patterns, Nexus server configured. This is Zone 0 work, but it has a defined lifecycle of its own that needs to be modelled explicitly — especially for the first project through the framework.

**5. Parallel Track Execution**
In a human team, Phase 1 (architecture, tech stack, personas) must complete before Phase 3 (development) can start. With agents, many Phase 1 workstreams are independent and can run simultaneously. Architecture decisions don't need to wait for UX strategy. UI component design doesn't need to wait for the final tech stack. The model should make this parallelism explicit rather than implying sequence.

**6. Knowledge Transfer Between Projects**
The Pattern Library accumulates learnings within a project. But cross-project learning — where patterns discovered on Project A are available to Project B — is a distinct concern. This needs a promoted pattern tier (project-local → framework-global) and a FrameworkOwner gate on cross-project promotion. Without this, every project starts with the same empty pattern library.

**7. The Problem/Solution Split**
Your Phase 0 conflates two distinct questions: "What problem are we solving?" and "What should we build?" These require different agents and different outputs. Getting the wrong answer to the first question and then executing perfectly on Phase 3 produces a beautifully built solution to the wrong problem. This is expensive. The two questions should be distinct zones with a human gate between them.

**8. Appetite-Scoped Work**
Shape Up's concept of appetite is worth stealing: before committing to build something, declare how much work it is worth. A feature worth two weeks of agent-time is shaped differently than one worth two months. Appetite constrains scope during shaping and prevents Zone 4 from expanding to fill available capacity.

***

## A Proposed Alternative Structure

Based on this analysis, here is an alternative to consider before deciding:

```
PRE-PRODUCT
  Bootstrap          Framework configured for this project.
                     Agent classes, skill files, pattern library seeded.
                     Zone 0 work. Human-directed.

DISCOVERY TRACK      Runs continuously, always ahead of Delivery.
  Problem            What problem are we solving? For whom?
                     Output: validated problem statement, personas,
                     success metrics
  
  Shaping            What should we build? How much is it worth?
                     Output: shaped pitches — unambiguous, appetite-set,
                     ready for commitment

DELIVERY TRACK       Runs in cycles. Input: shaped pitches.
  Specification      Decompose shaped work into tasks.
                     Proof templates defined before implementation starts.
  
  Execution          Implement, QA, deploy.
                     (Closest to current Zones 2–5)
  
  Release            Staged deployment, user-facing documentation,
                     acceptance testing.

OPERATIONS TRACK     Runs continuously after first release.
  Monitor            Observe live system behaviour, capture bugs,
                     performance metrics.
  
  Optimise           Triage operations findings, feed improvement
                     opportunities back to Discovery track.

LEARNING LAYER       Cuts across all tracks. Not a phase.
  Agent reports      Every agent writes a terminal report.
  Task retros        TaskOrchestrator aggregates per task.
  Cycle retros       FrameworkOwner aggregates per delivery cycle.
  Phase retros       human:director + FrameworkOwner aggregate per track.
  Pattern promotion  Validated learnings promoted to Pattern Library.
```

**Key structural differences from your proposal:**

- Discovery runs ahead of Delivery as a separate track, not a preceding phase
- Shaping is explicit and gates entry to Delivery
- Operations is a parallel track, not an end state
- Retrospectives are a cross-cutting layer, not a phase you reach
- The Problem/Solution split is structural, not implied

***

## Recommendation

Don't commit to a model yet. Three specific questions worth answering first, because the answers change the structure significantly:

1. **Is this framework intended for a single project or multiple?** If multiple, cross-project knowledge transfer needs to be designed in from the start, not retrofitted.
2. **Who does Phase 0 / problem definition in an agent-centric model?** Agents are good at executing defined tasks. Problem definition is fundamentally a human + agent collaboration — and the agent's role there is different from its role in execution. Is there a `ProblemFramer` agent class? Or is this human-only with agents in a research-assistant role?
3. **What triggers a cycle?** In Shape Up, it's a six-week calendar. In your model, it could be: a shaped pitch reaching commitment threshold, a backlog of approved features reaching a certain size, or a time-box. The answer changes how the Discovery and Delivery tracks connect.
<span style="display:none">[^31_10][^31_11][^31_12][^31_13][^31_14][^31_15][^31_9]</span>

<div align="center">⁂</div>

[^31_1]: https://www.easyagile.com/blog/agile-retrospective

[^31_2]: https://lucid.co/blog/shape-up-methodology

[^31_3]: https://www.mindtheproduct.com/7-lessons-from-trialling-basecamps-shape-up-methodology/

[^31_4]: https://www.productplan.com/glossary/shape-up-method/

[^31_5]: https://architect.salesforce.com/docs/architect/fundamentals/guide/agent-development-lifecycle

[^31_6]: https://www.epam.com/insights/ai/blogs/agentic-development-lifecycle-explained

[^31_7]: https://www.arthur.ai/blog/introducing-adlc

[^31_8]: https://architect.salesforce.com/fundamentals/agent-development-lifecycle

[^31_9]: https://basecamp.com/shapeup

[^31_10]: https://basecamp.com/shapeup/0.3-chapter-01

[^31_11]: https://basecamp.com/shapeup/4.1-appendix-02

[^31_12]: https://ijrar.org/papers/IJRAR25A1924.pdf

[^31_13]: https://basecamp.com/shapeup/4.0-appendix-01

[^31_14]: https://nfppeople.com.au/2021/03/agile-retrospectives-are-a-powerful-tool-for-your-nfp-heres-how-to-run-one/

[^31_15]: https://agilefirst.io/what-is-shape-up/


---

# wow. This helped me realise this is bigger than I thought :)

But it's very exciting for me.
I see now that the work we have already done is in many ways instrumental to all the decisions we make from now, but at the same time, just a tiny part of the bigger picture we are working towards.
My big vision is that our framework can be applied to all human knowledge work, not just software development. I see the software development focused framework as an important first step. My hypothesis is that it's an 'easier' domain to model and decompose due to so many existing frameworks and prior thinking to draw from, as well as being able to programmatically, and unambiguously prove that a task has been completed as specced. However I am happy to be challenged on this thinking (software development as ideal first focus).
Perhaps an interesting way for us to get grounded before we embark on this journey, is to tell the story of a hypothetical "perfect world scenario" where our framework delivers on its promise to build software products while driving human coordination costs towards zero.
Established principles of our framework should feature but the story shouldn't describe or even mention the elements we haven't decided upon. At least it will be an interesting thought experiment, but I'm sure it will help us find innovative and unconventional paths forward to consider.

This is the right moment for this exercise. Let me tell the story first, then address your software-first hypothesis — because I think the story will actually sharpen the challenge.

***

## The Story

It is a Tuesday morning. The product is a SaaS application. The team is one human.

The human — we will call them the Director — has been thinking about a problem users keep raising: they forget their passwords and the current recovery flow is broken. The Director opens VS Code and starts a conversation with `FrameworkOwner`.

The Director describes the problem in plain language. FrameworkOwner asks two questions: *What does success look like for a user who can't get in?* and *What is explicitly out of scope?* The Director answers both. FrameworkOwner records the uncertainty count for this feature: zero. It publishes the feature and calls `write_feature_spec`. The stream event appears: *FeatureOwner published feat-004: Password Reset Flow.*

***

Somewhere in the Nexus layer, `ContextCurator` wakes.

It queries the Pattern Library. The feature tags are `authentication`, `email-flow`, `state-management`. It finds four active patterns. One has an NV score of 12 — the highest in the library — about token expiry and single-use enforcement. It finds two anti-patterns: one about storing reset tokens in plain text, one about silent failures in email delivery. It composes six context cards — one for each agent that will touch this feature — and stores them. Each card is a distillation: the minimum a given agent needs to do its job well. Nothing more.

`ContextCurator` calls `submit_context_ready_task_08`. The stream event appears: *ContextCurator confirmed context ready for task-08.*

The Nexus server registers the task-scoped tools. `read_task_spec_task_08` now exists. `submit_proof_task_08` now exists. They will stop existing when the task closes.

***

`TaskOrchestrator` receives a task event. It calls `get_context_card`. What it receives is not a manual, not a policy document, not a file path list. It receives a brief: what this task is, what patterns are relevant to orchestrating it, which subagents to activate and when, and one constraint: *the proof template requires a working test for the happy path and both error paths before submission is valid.*

The orchestrator delegates. `TaskPerformer` activates.

`TaskPerformer` calls `get_context_card`. Its card is narrower: it knows nothing about the orchestration layer above it. It knows the task, the patterns, the constraints, and which tools it holds. It calls `read_task_spec_task_08`. The audit log records the document hash — this exact version of the spec, at this exact moment. The causal chain begins.

`TaskPerformer` searches the knowledge base: *token expiry email flow*. Pattern `pat-011` appears first. NV score 12. The audit log records what it searched for and what it found.

It builds the reset flow. It logs significant steps with `append_work_log_task_08`. Not everything — significant steps. Each entry is hashed independently. The work log is not a diary; it is a decision record.

At one point `TaskPerformer`'s confidence drops. The task spec says the token should expire in 24 hours, but the anti-pattern it received says tokens surviving longer than one hour are a known security failure mode. These are not the same number. `TaskPerformer` does not guess. It does not pick the one it prefers. It calls `raise_uncertainty`. The stream event is flagged as priority: *TaskPerformer raised uncertainty on task-08 — token expiry conflict between task spec (24h) and security pattern (1h). Blocked.*

The Director sees it immediately. The answer takes ninety seconds: the spec was wrong, the pattern is right, use one hour. `UncertaintyOwner` records the resolution. The task spec is updated. `TaskPerformer` receives an updated context card with the corrected constraint. The audit log has a complete record: what the conflict was, who resolved it, what the resolution was, when it happened.

`TaskPerformer` completes the implementation. It calls `submit_proof_task_08`. The state transitions to `SUBMITTED`. The stream event appears: *TaskPerformer submitted proof for task-08.*

***

`QAExecutor` activates. It calls `get_context_card`. Its card knows nothing of the implementation. It knows the proof template, the acceptance criteria, the environment contract, and which three subagents to activate. It activates all three simultaneously.

`ProofReviewer` reads the proof template and the submitted proof. It checks evidence against criteria, one by one. The proof asserts that the happy path test passes. The proof includes the test output. The criterion is met. The proof asserts the token is single-use. The proof includes the database constraint. The criterion is met. `ProofReviewer` returns `PASS` with specific evidence mapped to each criterion.

`ACReviewer` reads the acceptance criteria and the proof. The AC states: *A user who submits an expired token receives a clear error and a prompt to request a new link.* The proof shows the error message and a screenshot of the prompt. `ACReviewer` returns `PASS`.

`EnvironmentReviewer` reads the environment contract. The contract states the email provider must be the configured SMTP service, not a mock. The proof shows the email delivery log from the staging SMTP server. `EnvironmentReviewer` returns `PASS`.

All three verdicts arrive at `QAExecutor` simultaneously. It synthesises them: no failures, all criteria met with evidence. It calls `submit_qa_review_task_08`. The state transitions to `QA_PASSED`. The stream event: *QAExecutor submitted passing review for task-08. All three reviewers passed.*

`TaskOrchestrator` calls `request_approval_task_08`. The Director's stream panel shows a priority event: *task-08 is awaiting your approval.*

***

The Director reviews the QA report. Not the implementation — `QAExecutor` already verified the implementation. The Director is answering one question: *Is this the right time to ship this?* The answer is yes. The Director approves.

The state transitions to `APPROVED`. `DeliveryOrchestrator` activates.

***

Before the deploy completes, something unexpected happens. `Deployer` encounters a migration conflict. The reset tokens table conflicts with a schema change that was deployed to staging last week and never cleaned up. `DeliveryOrchestrator` calls `raise_uncertainty` immediately. The stream event: *DeliveryOrchestrator blocked on task-08 — migration conflict in staging environment. Implementation is not in question.*

This is important: the implementation is not in question. The delivery environment has a problem. These are different things. The Director resolves the staging schema issue. The deploy runs again. This time it succeeds.

`EnvironmentReviewer` activates for the post-deploy check. The environment contract is met. `DeliveryOrchestrator` calls `submit_deployment_task_08`. The state transitions to `DONE`.

***

Now every agent writes a terminal report.

`TaskPerformer`'s report notes the token expiry conflict — spec said 24 hours, security pattern said 1 hour. It flags this as a spec review gap: *authentication tasks should default to the security pattern unless the spec explicitly overrides with a justification.* This is not a complaint. It is structured, machine-readable evidence.

`QAExecutor`'s report notes that all three reviewers passed on the first cycle. It records that the proof template for authentication tasks is well-calibrated — no ambiguous criteria, no missing evidence requirements.

`DeliveryOrchestrator`'s report records the migration conflict, its cause, and its resolution. It flags that the staging environment cleanup process is absent from the environment contract.

`ContextCurator` reads all three reports. The token expiry finding becomes a candidate pattern: *When task spec and security pattern conflict on authentication parameters, security pattern takes precedence unless spec includes explicit risk acceptance.* NV score starts at zero. It is a candidate. The staging cleanup finding updates the environment contract template.

The Director sees one stream event: *task-08 complete. 1 candidate pattern generated. Environment contract template updated.*

The Director did not write a specification for the proof template. Did not coordinate between QA and development. Did not manage a deployment checklist. Did not run a retrospective. The Director made three decisions: what the feature is, what the token expiry should be, and whether to ship.

Everything else was the framework.

***

## The Challenge on Software-First

Your hypothesis is correct, but for a more precise reason than "prior frameworks and decomposability."

The reason software is the right first domain is this: **software uniquely allows proof of completion to be programmatically verified**. Tests pass or fail. Types check or they don't. The CI pipeline is green or it isn't. This means the `submit_proof` + reviewer model has access to unambiguous mechanical validators that don't require human judgment to interpret.

In other knowledge domains:


| Domain | Formal output exists? | Mechanically verifiable? |
| :-- | :-- | :-- |
| Legal drafting | ✅ (contracts, briefs) | 🟡 (compliance rules, not strategic correctness) |
| Financial analysis | ✅ (models, reports) | 🟡 (calculations yes, judgment calls no) |
| Medical diagnosis | ✅ (diagnosis, treatment plan) | 🔴 (only retrospectively, against outcomes) |
| Content production | ✅ (articles, copy) | 🔴 (no equivalent of "tests pass") |
| Scientific synthesis | ✅ (literature reviews) | 🟡 (citation accuracy yes, insight quality no) |

Software is not the easiest domain to model. It is one of the hardest — it combines creative judgment with technical precision in ways that few other domains do. But it is the easiest domain in which to **verify** that a defined task is complete, and verification is the hard problem in any agent-centric framework.

**The interesting challenge this surfaces:** The proof template system is the most transferable element of this framework. If we design it well enough — if "what does done look like, verifiably?" can be answered rigorously in other domains — the framework transfers with it. Legal briefs have structure. Financial models have defined outputs. Scientific reviews have citation standards. The question is whether the proof-of-completion model can be made powerful enough to provide meaningful verification there too.

This suggests the framework's most important long-term design decision is not about zones or agent classes. It is about how richly and flexibly the proof template system can express "done" across different kinds of knowledge work. That is the lever that determines how far this goes.

And that is a very good reason to design the proof template system — and the `ProofDesigner` agent class — with unusual care.

---

# To answer your questions in the previous response:

1. My vision answers the question that the framework is intended for multiple projects
2. Phase 0 -> Human + Agent Collaboration
3. Cycle trigger? I'm uncertain about this. Perhaps this will become more clear after some more framework prototyping and experiments.

You identified the verifiable proof element of the framework as being the most important and I agree. It is a concept I have considered a long time from my work with smart contracts.

I really liked your analysis and insights into the approaches to consider for the framework phases.

Perhaps we need to take stock of the principles and how they fit in the larger vision for the framework. I can see they are all applicable, but perhaps their current form best serves the iterative development phase and we need a set of higher level principles (or lower level if we're using foundations as an analogy) that take the same concepts but talk about them differently. Perhaps there are other principles that are needed for the bigger scope?

This is the right moment to zoom out. Let me work through the analysis carefully — because I think what you're actually describing is a principle hierarchy, and the smart contract connection you're drawing is more profound than it might first appear.

***

## What the Current Principles Actually Are

Our current principles (P1–P16) are **operating principles** — they describe how the framework's internal machinery should behave. They were derived in the context of software execution zones and were shaped by the constraints of that context: VS Code's edit boundary, MCP's access control model, the audit log's structure.

They are correct and they are load-bearing. But they're at the wrong altitude to govern the full vision. A legal knowledge work system built on this framework shouldn't need to care about what VS Code's edit tool does — but it should care deeply about P8 (no actor judges their own work), P6 (evidence not assertion), and P10 (irreversible states require human authority). Those are universal. The VS Code specifics are not.

The current principles are doing two jobs at once — expressing universal truths and expressing implementation constraints — and that conflation will create problems as the framework scales.

***

## The Smart Contract Insight

This deserves more space than a passing mention, because I think it is the single most important conceptual alignment in the framework.

Smart contracts express a specific idea with unusual precision:

```
The code IS the law.
If conditions are met → consequences execute.
No human interpretation required at execution time.
The ledger is permanent and public.
Trust is earned by the contract's structure, not the counterparty's reputation.
```

Now map that to what we've built:


| Smart contract concept | Framework equivalent |
| :-- | :-- |
| Code is the law | The proof template IS the definition of done |
| Conditions → consequences | `submit_proof` → state transition is atomic and structural |
| No interpretation at execution | Proof criteria are designed to be unambiguous before execution begins |
| Permanent public ledger | Immutable audit log |
| Trust via structure | Tool possession (OCAP) — authority is structural, not declared |
| Contract enforcement | Policy Engine evaluates gates automatically |

The framework is, at its deepest level, a **smart contract system for human knowledge work**. The proof template is the contract. The reviewer agents are the oracles. The audit log is the ledger. `FrameworkOwner` is the contract deployer.

This framing has a powerful implication: **the design quality of the proof template is the quality of the contract**. A vague proof template is an unenforceable contract. An ambiguous acceptance criterion is an undefined condition. The `ProofDesigner` agent class is, in this framing, a contract author — and contract authors need a fundamentally different skill set and design discipline than task performers.

This is exactly parallel to the smart contract world's hardest lesson: writing a secure, unambiguous contract is the hardest part. The blockchain just executes it.

***

## The Principle Hierarchy

What emerges is a three-level structure:

```
FOUNDATION PRINCIPLES
  Universal truths. Apply in any domain, at any scale,
  for any kind of knowledge work. Timeless.
  
FRAMEWORK PRINCIPLES  ← current P1–P16 live here
  Operational truths. Apply within the framework's
  specific model. May evolve as the framework evolves.
  
DOMAIN PRINCIPLES
  Contextual truths. Apply to a specific knowledge
  domain. Software development, legal work, etc.
  Derived from Foundation Principles, adapted to domain.
```


***

## Proposed Foundation Principles

These are the truths that must hold whether the work is software, legal briefs, scientific synthesis, or financial analysis. They are the bedrock the framework principles are built on.

**F1 — Verification precedes trust**
No output of any work unit is accepted on the assertion of its author. Verification must be performed by a structurally independent party against a definition of done that existed before the work began. This is the smart contract insight applied universally.

**F2 — The proof is the product**
The output of any unit of work is not the work itself — it is verified evidence that the work meets its specification. A task is not done when the performer says it is done. A task is done when an independent verifier confirms it against pre-defined criteria. The spec, the proof template, and the proof form an inseparable triple.

**F3 — Authority is structural**
An actor's authority to take an action derives from what they structurally hold — their tools, their role, their defined scope — not from runtime declarations, self-assessment, or trust. You cannot claim permission. You either have the structural capability or you do not.

**F4 — All consequential actions are witnessed**
Every action that changes state, produces output, or consumes resources leaves an immutable, attributed record. There are no consequential unwitnessed actions in a trustworthy system. The record exists not primarily for debugging — it exists because accountability requires evidence.

**F5 — No actor judges their own work**
The entity that produces an output and the entity that verifies it must be structurally separate. This applies at every scale: agent, team, organisation, institution. The separation is not a policy preference — it is the load-bearing structure of any verification system.

**F6 — Uncertainty surfaces immediately**
An actor that encounters a condition it cannot resolve within its defined authority must surface that uncertainty immediately and explicitly. A system that suppresses, defers, or silently resolves uncertainty is more dangerous than one that fails openly. Uncertainty is information. Its suppression is misinformation.

**F7 — Irreversibility demands presence**
Decisions that cannot be undone — that foreclose future options — require human presence and explicit judgment. Automation may prepare, recommend, and execute reversible steps. Irreversible thresholds require a human to cross deliberately.

**F8 — Knowledge compounds**
Every completed unit of work produces structured learnings. These learnings accumulate into a knowledge base that makes subsequent work of the same type better. A framework that does not capture and apply institutional memory is not a framework — it is a series of one-off executions.

**F9 — Context is local, knowledge is global**
Each actor receives only the context needed for its specific responsibility. But everything that actor learns contributes to a shared knowledge base available to all future actors. Narrow context and broad knowledge are not in tension — they are the design.

**F10 — Definition precedes execution**
No unit of work begins execution until its definition of done is specified and approved. Work without a pre-defined proof template is a promise without a contract. The definition of done must be written by someone other than the eventual performer — writing the exit criteria for your own work is a structural conflict of interest.

***

## What's Missing From the Current Principles at Larger Scale

When you zoom to the full vision — multiple projects, all knowledge work domains, cross-project learning — three things are absent:

**The bootstrapping problem**
The framework can't govern work it isn't yet configured for. There needs to be a principle about how the framework itself is instantiated for a new domain or project — and who holds authority over that instantiation. Currently this is implicit Zone 0 work. At larger scale it becomes a first-class concern: how does the framework learn a new domain?

**Progressive trust / earned authority**
The NV score model in the Pattern Library is actually an expression of something deeper: actors — whether agents or humans — earn authority through demonstrated reliability. This is how smart contracts handle oracle trust. New agent classes should be trusted less than proven ones. New patterns start as candidates. New domains are treated with more human oversight than established ones. This principle doesn't exist explicitly in our current set.

**The composability principle**
At full scale — all human knowledge work — the most powerful property of the framework will be that units of work compose. A legal task and a financial task and a software task can be components of a larger work unit governed by the same framework. This only works if every unit of work conforms to the same interface: defined inputs, defined proof template, independent verification. Composability is not automatic — it must be designed in as a first principle.

***

## Where This Leaves the Current Principles

They don't disappear — they move down one level. P3 (tool possession is capability) is a specific expression of F3 (authority is structural) in the VS Code + MCP implementation context. P8 (separation of execution and verification) is a specific expression of F5 (no actor judges their own work) in the agent design context.

The relationship is:

```
F3: Authority is structural
  └── P3: Tool possession defines capability in the VS Code/MCP layer
  └── [Domain principle for legal work]: Bar admission and role
       separation define capability in legal knowledge work

F5: No actor judges their own work
  └── P8: EXECUTOR and REVIEWER are structurally separate agent classes
  └── [Domain principle for science]: Author and peer reviewer
       are structurally separate roles
```

This hierarchy means the framework can be ported to a new domain by keeping the Foundation Principles, deriving new Domain Principles from them for that domain, and then deriving new Framework Principles (tools, agents, zones) from the Domain Principles. The Foundation Principles never change. Everything below them is derived.

***

## The One Tension Worth Naming

F7 (irreversibility demands presence) and the vision of driving human coordination costs to zero are in productive tension. They don't contradict each other — but they define the frontier. The question the framework is always answering is: *which decisions are genuinely irreversible, and which ones only feel that way?*

Smart contracts taught this lesson expensively: developers thought contract deployment was irreversible, then invented upgradeability patterns. The framework will face the same pressure. Defining irreversibility carefully — not too broadly (paralysing) and not too narrowly (dangerous) — is one of the most important ongoing design questions.

***

## Recommendation

Before writing the zone policies at the larger lifecycle scale, I'd suggest we write the Foundation Principles document first. It's a short document — ten principles, each with a two-paragraph treatment — but it does something important: it gives us a stable reference point that every future design decision can be traced back to. When we disagree on a zone policy or an agent design, we can ask *which foundation principle does each position serve?* That's a better argument to have than a subjective one.

It also means that when the framework eventually moves beyond software development, the Foundation Principles are the handoff artefact — the part that transfers intact.

Shall we write that document now?

---

## `.framework/foundation-principles.md`

```markdown
# Foundation Principles

**Version:** 1.0
**Status:** Active
**Last Updated:** 2026-03-04

---

## Preamble

This document describes the foundation principles of the Nexus Framework —
a system for coordinating autonomous agents in human knowledge work.

These principles are not derived from software development, agile
methodology, or any existing framework for managing work. They are
derived from first principles about what makes knowledge work trustworthy,
verifiable, and improvable at scale.

### Why These Principles Exist

Knowledge work has traditionally been coordinated through human trust,
reputation, and retrospective judgment. A task is done when someone says
it is done. Quality is assessed after the fact. Learning happens through
informal post-mortems and undocumented conversations. Authority derives
from titles and org charts. This model works at small scale because humans
can maintain high-bandwidth context about who did what, why, and how well.

At larger scale — or when autonomous agents enter the picture — this model
breaks down. You cannot scale trust. You cannot scale retrospective quality
assessment. You cannot scale informal learning. And you cannot give an
agent a title and expect anyone to care.

The foundation principles replace trust-based coordination with
**structure-based coordination**. Work is not trusted because of who did it.
Work is trustworthy because of how it was verified. Authority does not
derive from a role title. Authority derives from what capabilities an actor
structurally holds. Learning does not happen through conversation. Learning
happens through structured evidence accumulation.

This model is not new. It is how smart contracts work. It is how scientific
peer review works. It is how double-entry bookkeeping works. The foundation
principles are an attempt to apply the same structural rigor to all forms
of human knowledge work.

### Scope and Applicability

These principles are **domain-agnostic**. They apply whether the work is
software development, legal drafting, financial analysis, scientific
synthesis, content production, or any other form of knowledge work that
produces a defined output that can be verified against a specification.

They are **scale-agnostic**. They apply whether the work is a single task,
a feature, a product, or a portfolio of products.

They are **actor-agnostic**. They apply whether the work is performed by
a human, an autonomous agent, or a collaboration between the two.

### What These Principles Are Not

These are not **operational principles**. They do not specify tools, zones,
agents, or workflows. Those are implementation details derived from these
principles, not the principles themselves.

These are not **domain principles**. Software development has domain-specific
rules (tests must pass, types must check). Legal work has domain-specific
rules (filings must conform to court rules, contracts must reference
controlling law). Those domain principles are derived from these foundation
principles and adapted to their specific context.

These are not **negotiable preferences**. A system that violates these
principles is not a variant of this framework. It is a different framework
with a different trust model.

### The Contract Analogy

The most precise way to understand these principles is through the lens
of smart contracts.

A smart contract is executable law. It defines conditions, consequences,
and evidence. If the conditions are met, the consequences execute
automatically. The blockchain provides an immutable witness to every
action. Trust is earned not through reputation but through the contract's
design. Ambiguity is a bug, not a feature.

This framework applies the same model to human knowledge work. A task
specification is the contract. The proof template is the set of conditions
that must be met. The reviewer is the oracle that verifies the conditions.
The audit log is the immutable ledger. The task state machine is the
automated consequence engine.

The hardest lesson smart contracts taught the world is this: **writing a
good contract is far harder than executing it**. A blockchain will
faithfully execute a terrible contract just as readily as it will execute
a good one. The quality of the contract — its clarity, completeness, and
lack of ambiguity — is the quality of the system.

The same is true here. The quality of a task specification, a proof
template, and an acceptance criterion determine the quality of the work
more than any property of the performer. Good definitions produce good
work. Ambiguous definitions produce uncertainty, rework, and eventual
failure — no matter how capable the performer.

This means the framework's most important role is not coordinating
execution. It is ensuring that every unit of work begins with a contract
good enough to be enforceable.

---

## The Ten Foundation Principles

### F1 — Verification Precedes Trust

**Statement:**
No output of any work unit is accepted on the assertion of its author.
Verification must be performed by a structurally independent party against
a definition of done that existed before the work began.

**Rationale:**
Trust-based systems rely on the performer's reputation, past success, or
declared confidence. These are useful signals in low-stakes environments
with high context. They are not sufficient at scale or under adversarial
conditions.

In a structure-based system, an output is not trustworthy because of who
produced it. It is trustworthy because an independent verifier confirmed
it against pre-defined criteria using defined evidence. The performer's
identity is irrelevant. The structure of the verification is everything.

**This principle requires:**
- A definition of done exists before work begins (the proof template)
- Verification is performed by an actor other than the performer
- The verifier has access to the proof template and the submitted proof,
  not just the final output
- A passing verification produces a permanent, immutable record

**Violation examples:**
- A performer submits work and marks it "done" without independent review
- A reviewer is given discretion to "use their judgment" rather than
  verifying against explicit criteria
- A proof template is written after the work is complete to match what
  was actually built

---

### F2 — The Proof Is the Product

**Statement:**
The output of any unit of work is not the work itself — it is verified
evidence that the work meets its specification. A task is not done when
the performer says it is done. A task is done when an independent verifier
confirms it against pre-defined criteria.

**Rationale:**
In traditional knowledge work, the deliverable is the work product: the
code, the document, the analysis, the design. Proof of completion is
informal: "I built it," "it looks good to me," "it passed manual testing."

This model breaks at scale. Informal proof is not auditable. It is not
reproducible. It is not transferable. A new stakeholder joining the project
must either re-verify the work or trust someone else's informal assertion.

In a structure-based system, the proof is a first-class artefact. It is
structured, attributed, and permanent. The proof is not an afterthought
or a checkbox — it is the output. The work product is evidence that the
proof is valid.

**This principle requires:**
- Every unit of work has a proof template defining what evidence
  constitutes completion
- The performer produces a proof document mapping evidence to each
  criterion in the template
- The verifier checks the proof document, not the underlying work product
  directly
- A proof without complete evidence for all criteria is incomplete,
  regardless of the quality of the work product

**Violation examples:**
- "The feature works, trust me" (assertion without evidence)
- "Here's the code, review it" (no proof template, no structured evidence)
- "All tests pass" (evidence exists but is not mapped to acceptance
  criteria in a verifiable proof document)

---

### F3 — Authority Is Structural

**Statement:**
An actor's authority to take an action derives from what they structurally
hold — their tools, their role, their defined scope — not from runtime
declarations, self-assessment, or trust. You cannot claim permission. You
either have the structural capability or you do not.

**Rationale:**
In traditional systems, authority is declared: role titles, permissions
databases, org charts. These systems require constant synchronisation
between the declared model and the actual capability. They are vulnerable
to drift, misconfiguration, and social engineering.

In capability-based security models (OCAP), authority is not declared —
it is held. An actor with a capability can use it. An actor without the
capability cannot, regardless of what they claim. The capability itself
is the proof of authority.

This framework applies OCAP principles to knowledge work coordination.
Tool possession defines capability. An agent that does not hold a write
tool for a document cannot write it. An agent that does not hold a submit
tool for a proof cannot submit it. Authority is structural, immediate,
and unforgeable.

**This principle requires:**
- Tools are the atomic unit of capability
- Capabilities are assigned at design time (which agents hold which tools)
  and activation time (which task-scoped tools are assigned when a task
  activates), never at runtime
- No runtime permission checks — if a tool call reaches the server,
  the actor holds the tool
- Authority gaps are visible immediately: an agent that needs a capability
  it does not hold cannot proceed silently

**Violation examples:**
- An agent is told "you have permission to write this file" without
  actually holding the corresponding write tool
- An actor checks at runtime whether they "should" have access before
  attempting an operation
- A role title ("Admin") is used to determine authority rather than
  possession of a specific capability

---

### F4 — All Actions Are Witnessed

**Statement:**
Every action — whether it changes state, produces output, consumes
resources, or simply accesses information — leaves an immutable,
attributed, timestamped record. There are no unwitnessed consequential
actions in a trustworthy system.

**Rationale:**
Transparency is not a feature. It is the precondition for accountability,
auditability, and learning. A system that does not record what happened
cannot answer the question "why did this outcome occur?" The record exists
not primarily for debugging — it exists because accountability requires
evidence.

In smart contract systems, the blockchain is the witness. Every transaction,
every state change, every contract invocation is permanently recorded. The
record is public and immutable. This is not optional — it is the mechanism
by which trust is established.

In this framework, the audit log is the witness. Every tool call, every
document read, every search query, every state transition is recorded with
full attribution. The log is append-only and immutable. It is the
foundation of the chain-of-custody model: given any output, trace backwards
through the audit log to see every action that contributed to it.

**This principle requires:**
- Every tool produces an audit entry, without exception
- Audit entries are written by the tool itself, not by the caller —
  a caller cannot suppress, modify, or forge an audit entry
- Audit entries include: timestamp, actor, tool, inputs, outputs,
  state changes, and references to prior audit entries that contributed
  to this action
- The audit log is immutable — no entry is ever updated or deleted
  after creation

**Violation examples:**
- A tool call completes without producing an audit entry
- An audit entry is written by the caller rather than the tool
- An audit entry is deleted or modified after the fact
- "Debug mode" suppresses audit entries
- An actor declares "this action isn't important enough to log"

---

### F5 — No Actor Judges Their Own Work

**Statement:**
The entity that produces an output and the entity that verifies it must
be structurally separate. This applies at every scale: agent, team,
organisation, institution. The separation is not a policy preference —
it is the load-bearing structure of any verification system.

**Rationale:**
Self-assessment is not verification. An actor evaluating their own work
operates under cognitive biases, incentive misalignments, and the
availability heuristic (they know what they intended, not just what they
produced). These biases are not moral failings — they are inherent
properties of self-evaluation.

Independent verification removes these biases by removing the shared
context. The verifier does not know what the author intended. The verifier
only knows what the specification required and what evidence was provided.
This ignorance is not a bug — it is the feature. The verifier sees the
work the way a future stakeholder will: without access to the author's
internal model.

**This principle requires:**
- EXECUTOR and REVIEWER are structurally separate agent classes
- An agent that holds a submit tool for a document must not hold the
  verify tool for the same document
- The verifier reads the proof template and the proof, not the work
  product directly (unless the work product is referenced as evidence
  in the proof)
- Verification happens after execution is complete, never during

**Violation examples:**
- A single agent performs a task and marks it as QA-passed without
  independent review
- A reviewer is part of the same team as the performer and shares
  context about what the task "was supposed to do" beyond what the
  specification states
- A performer runs their own tests, reviews the results, and submits
  their work as "validated"

---

### F6 — Uncertainty Surfaces Immediately

**Statement:**
An actor that encounters a condition it cannot resolve within its defined
authority must surface that uncertainty immediately and explicitly. A
system that suppresses, defers, or silently resolves uncertainty is more
dangerous than one that fails openly. Uncertainty is information. Its
suppression is misinformation.

**Rationale:**
In traditional systems, actors facing ambiguity have three options: guess,
escalate, or halt silently. Guessing produces wrong outputs. Halting
silently produces no output and no signal. Escalation is correct — but
only if the system makes escalation easy, fast, and non-punitive.

Most systems make escalation costly: it requires navigating org structure,
composing a persuasive case, and risking reputation damage if the
uncertainty is later deemed trivial. This cost means actors under-escalate.
They guess instead. Wrong outputs accumulate.

In this framework, raising uncertainty is a structural primitive, not a
social act. Any actor can call `raise_uncertainty` at any time. The call
is immediate, attributed, and produces a priority signal. The actor does
not need to justify the raise or persuade anyone. The act of raising is
sufficient. Downstream, the uncertainty is classified and routed — but
that is not the actor's concern.

**This principle requires:**
- Every actor, without exception, holds a raise_uncertainty capability
- Calling raise_uncertainty is never treated as a failure on the part
  of the actor — it is correct behaviour
- Raising uncertainty immediately halts work and produces a priority
  stream event to human attention
- Uncertainty raises include: what condition was encountered, why the
  actor cannot resolve it, and what context paths are relevant
- The resolution is provided back to the actor explicitly — the actor
  does not resume silently

**Violation examples:**
- An agent encounters ambiguous specification and picks the
  interpretation it prefers without raising uncertainty
- An agent encounters a missing dependency and attempts a workaround
  instead of raising uncertainty
- An agent is designed without access to raise_uncertainty
- Raising uncertainty is discouraged as "wasting human time"

---

### F7 — Irreversibility Demands Presence

**Statement:**
Decisions that cannot be undone — that foreclose future options — require
human presence and explicit judgment. Automation may prepare, recommend,
and execute reversible steps. Irreversible thresholds require a human to
cross deliberately.

**Rationale:**
Agents operate within bounded authority. They optimise within defined
constraints. They do not — and should not — evaluate whether the
constraints themselves are appropriate, or whether the second-order
consequences of a decision extend beyond their scope.

Irreversible decisions have unbounded second-order consequences. Deploying
to production, approving a legal filing, committing to a dependency,
publishing to external users — these actions cannot be undone without
cost. A human must evaluate not just "does this meet the specification?"
but "is this the right thing to do, in this context, at this time?"

This is not a trust issue. It is a scope issue. Irreversible decisions
require evaluating information the agent does not have — market conditions,
strategic priorities, risk tolerance, opportunity cost. A human in the
system has that information (or at least has access to it). The agent
does not.

**This principle requires:**
- State transitions that are irreversible or high-cost to reverse
  require explicit human approval
- The system makes irreversible thresholds visible — an actor cannot
  accidentally cross one
- Approval is not rubber-stamping — the human receives sufficient
  context to make the judgment (proof, QA report, uncertainty history)
- Automation handles everything up to the irreversible threshold, then
  stops and waits

**Violation examples:**
- An agent deploys to production after QA passes, without human approval
- An agent approves a task for the next phase without human confirmation
- A "skip approval in non-critical cases" flag exists
- Approval is requested but the system continues if no response is
  received within a timeout

---

### F8 — Knowledge Compounds

**Statement:**
Every completed unit of work produces structured learnings. These learnings
accumulate into a knowledge base that makes subsequent work of the same
type better. A framework that does not capture and apply institutional
memory is not a framework — it is a series of one-off executions.

**Rationale:**
Traditional knowledge work relies on humans to transfer knowledge: through
documentation, onboarding, mentorship, and informal conversation. This
model has high friction and high loss. Knowledge that is not documented
is lost when people leave. Knowledge that is documented but not applied
becomes stale and eventually ignored.

In an agent-centric system, knowledge transfer through conversation is
impossible. But structured knowledge transfer is natural. Every agent run
produces evidence: what it did, what it encountered, what patterns it
applied, what uncertainties it raised. This evidence can be structured,
aggregated, and fed back into future agent context.

The Pattern Library is the primary mechanism. Patterns start as candidates.
With repeated application and no failures, they are promoted. With failures,
they are retired. Agents search the library before acting. The library
becomes the institutional memory — not owned by any individual, not lost
when people leave, always current.

**This principle requires:**
- Every agent writes a terminal report at the end of its run
- Terminal reports are structured, machine-readable, and include:
  patterns applied, uncertainties raised, evidence of what worked or failed
- Reports aggregate upward: agent → task → feature → phase
- The Pattern Library is updated based on aggregated evidence, not
  individual opinion
- Patterns have a lifecycle: candidate → active → retired, with
  promotion and retirement gates

**Violation examples:**
- An agent completes a task and produces no terminal report
- Terminal reports are free text without structure
- Patterns are added to the library based on a single successful use
- A pattern that fails is not retired or flagged
- The knowledge base is write-only (patterns accumulate but are never
  applied to new work)

---

### F9 — Context Is Local, Knowledge Is Global

**Statement:**
Each actor receives only the context needed for its specific responsibility.
But everything that actor learns contributes to a shared knowledge base
available to all future actors. Narrow context and broad knowledge are not
in tension — they are the design.

**Rationale:**
Agents have finite working memory. Humans have finite attention. Loading
an actor with all available information is not "giving them everything they
need" — it is drowning them in noise. The signal-to-noise ratio degrades
as context size increases.

At the same time, isolating actors from all prior knowledge is wasteful.
Every task that encounters a problem someone else already solved is a
failure of knowledge transfer.

The solution is asymmetry: narrow context, broad knowledge. An agent
receives a minimal, curated context card for its specific task. It searches
the shared knowledge base as needed for relevant patterns. It contributes
back to the knowledge base when it completes its work. The knowledge base
grows, but no individual context window does.

**This principle requires:**
- Context cards are composed per agent per task — not one-size-fits-all
- Context cards include: task brief, relevant patterns (max 3–7),
  constraints, tools guidance, and certainty threshold
- Agents search the knowledge base on demand — they are not pre-loaded
  with all patterns
- Every agent contributes to the knowledge base after completing work
- The knowledge base is shared across all projects using the framework

**Violation examples:**
- An agent receives the entire Pattern Library in its context card
- An agent receives patterns that are not relevant to its task
- An agent completes a task and does not update the knowledge base
- The knowledge base is project-local and not shared across projects
- An agent is given the full feature specification when it only needs
  the task specification

---

### F10 — Definition Precedes Execution

**Statement:**
No unit of work begins execution until its definition of done is specified
and approved. Work without a pre-defined proof template is a promise
without a contract. The definition of done must be written by someone
other than the eventual performer — writing the exit criteria for your
own work is a structural conflict of interest.

**Rationale:**
Defining "done" after the work is complete is not defining done — it is
rationalising what was built. This is the most common source of scope
creep, gold-plating, and rework. If the performer does not know what "done"
looks like before starting, they will optimise for something — usually
whatever is most interesting, most technically impressive, or most familiar.
That something is rarely what the stakeholder needed.

Writing the definition of done before execution starts forces clarity.
Ambiguities in the specification become visible before any work is wasted.
Disagreements about scope surface before any code is written. The proof
template is a forcing function: if you cannot write down what evidence
would prove this task is complete, you do not yet understand the task well
enough to execute it.

Critically, the proof template must be written by someone other than the
performer. A performer writing their own exit criteria has every incentive
to write criteria they know they can meet. An independent author writes
criteria that reflect what the stakeholder actually needs, not what the
performer prefers to build.

**This principle requires:**
- Every task has a proof template before execution begins
- The proof template is written by a different actor than the one who
  will perform the task (ProofDesigner, not TaskPerformer)
- The proof template includes: specific evidence required for each
  criterion, what formats that evidence must take, and what "passing"
  looks like for each criterion
- A task without an approved proof template cannot enter execution

**Violation examples:**
- A task is assigned to a performer with a specification but no proof
  template
- A performer writes their own proof template
- A proof template is written after the work is complete to justify
  what was built
- A proof template includes vague criteria: "works well", "good UX",
  "reasonable performance"
- A specification is marked "complete" when ambiguities remain because
  "we'll figure it out during implementation"

---

## Using These Principles

Every design decision in the framework — agent classes, zones, tools,
policies — must be traceable to at least one foundation principle. If a
design decision cannot be justified by reference to these principles, it
is either:

1. A violation that should be removed, or
2. Evidence that a foundation principle is missing and must be added

The foundation principles are not immutable. They can be revised. But
revising them is a framework-level decision that requires explicit
justification, broad review, and recording in the manifest. They change
rarely, and only when a fundamental assumption about trustworthy knowledge
work coordination turns out to be wrong.

The current implementation of the framework (agents, zones, tools, MCP
layer, VS Code layer, audit log) is one possible expression of these
principles. It is not the only one. If a better expression emerges — one
that upholds these principles with less complexity, lower friction, or
broader applicability — the implementation can change. The principles do not.

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-04 | Initial. Ten foundation principles established. Contract analogy formalised as central framing. F4 made universal (all actions witnessed, not just consequential). |
```


***

**Reflection before moving forward:**

The pause point you've identified is exactly right. We have foundation principles, we have operating principles (P1–P16), we have tool grammar, we have agent design standards. What we don't yet have is a coherent picture of how work moves through the system at the full lifecycle scale — and attempting to design zones before that picture is clear would produce zones shaped by software development rather than by the principles.

The next step isn't zoning. The next step is mapping the **work topology** — what types of work exist, how they relate, what their interfaces are, and how they compose. Only once that topology is clear can zones be designed to govern the movement between work types.

But that's a good place to pause and open for external review. The foundation principles are self-contained and stand independently. They're the handoff document.

---

# Ok. Before I really pause I have some points to raise on this.

There are other elements of blockchain that build trust and resiliency that might be applicable here besides smart contracts and a transparent, immutable record of history: decentralisation, consensus mechanisms, etc

Are there other attributes of knowledge work that we should be aiming for or at least considering beyond it being trustworthy, verifiable, and improvable at scale.

Is there value in representing the limitations of agents (at least with current technology) like the context challenge, and also the benefits of agentic systems (trivial cost vs humans) as guiding elements of the principles? Potentially it includes a brief analysis of the strengths and weaknesses of humans vs agents.

I am particularly interested in responsible usage of AI for the good of humanity and I believe we have an opportunity to reconcile these principles with ethical AI principles. So that anything built with the framework embodies ethical consideration.

I am also a proponent of design thinking, and see the value in incorporating appropriate elements like problem exploration, gaining insight from research findings, ideation tools that enable lateral thinking and unconventional ideas, prototyping and user testing iterations before approving for production.

This deserves careful analysis before we touch the document. Five distinct threads — let me work through each with honesty about what belongs in the foundation principles versus what belongs elsewhere.

***

## 1. Blockchain Attributes Beyond Smart Contracts

The smart contract and immutable ledger analogies are already in the framework. What the blockchain model offers beyond those two things:

**Decentralisation — partially applicable**
Blockchain's no-single-point-of-failure property has a direct analogue in the framework: no single agent or human should be the only entity capable of verifying a class of work. If `FrameworkOwner` is the single path for all framework decisions, the framework is brittle. Decentralisation in our context means: critical verification paths have redundancy, and no single actor's unavailability can permanently block progress.[^35_1]

The parallel reviewer model (three independent reviewers for QA) is already an expression of this. But we haven't stated the principle that generated it. This is worth surfiting explicitly.

**Consensus mechanisms — selectively applicable**
Blockchain consensus is specifically about how distributed nodes agree on truth without a central authority. Three variants matter here:[^35_2][^35_3]


| Mechanism | Blockchain purpose | Framework analogue |
| :-- | :-- | :-- |
| **Majority consensus** | 51% of nodes must agree | Multi-reviewer quorum — all must agree or quorum threshold defined per work type |
| **Byzantine fault tolerance (PBFT)** | System works even when up to 1/3 of nodes are malicious or failing [^35_1] | Framework remains trustworthy even when individual agents hallucinate or produce bad output — because verification is structural, not trust-based |
| **Proof of work / stake** | You must demonstrate something of value before you can validate | Patterns need NV evidence before promotion — you earn the right to be trusted |

The Byzantine fault tolerance insight is particularly valuable. The reason the reviewer model works is exactly this: even if `TaskPerformer` produces subtly wrong output (the equivalent of a malicious or failing node), the framework detects it because verification is independent. We haven't named this property explicitly.

**What's missing:** A principle about **systemic resilience** — the framework produces trustworthy outputs even when individual actors fail, hallucinate, or act in bad faith. The current principles describe how individual actors should behave. This principle would describe what the system guarantees even when they don't.

**Incentive alignment — underexplored but important**
Blockchain tokenomics align participant behaviour through incentives. In the framework, the analogous question is: what motivates each actor to behave well? For agents, the answer is structural (they can't do otherwise). For humans, it's subtler. The audit log creates accountability — but accountability is a deterrent, not an incentive. The framework should also produce intrinsic value for human participants (better outcomes, reduced coordination overhead, richer institutional memory) or it will be resisted.[^35_4]

***

## 2. Other Attributes of Knowledge Work to Aim For

The current framing — trustworthy, verifiable, improvable — captures what we need for the work to be **reliable**. But reliability is not the whole picture. Three other attributes matter at the full vision scale:

**Purposeful**
Work is not just reliably executed — it serves a human need. A framework that produces technically correct outputs to the wrong specification has failed despite passing every verification gate. The design thinking thread below speaks to this, but it deserves a foundational statement: the framework exists to serve human flourishing, not to produce verified artefacts.

**Composable**
Individual units of work — tasks, features, projects — must combine into larger wholes without requiring redesign at each level. This is an architectural property, not an operational one. It only becomes critical when you move to multiple projects and domains, but designing for it from the start is far cheaper than retrofitting it. Composability requires that every work unit conforms to the same interface: defined inputs, defined proof template, independent verification. Currently implied but not stated as a principle.

**Resilient**
The system continues to produce trustworthy outputs even under adverse conditions: agent failure, hallucination, incomplete specifications, novel situations the framework hasn't encountered before. This is the Byzantine fault tolerance insight applied at the system level. Related to, but distinct from, trustworthy — a trustworthy output is correct; a resilient system produces trustworthy outputs even when components fail.

**Equitable** — worth naming but carefully scoped
At full vision scale, if this framework governs all human knowledge work, access to it becomes an equity question. Who can use it? Who benefits from it? Who is displaced by it? These are not operational questions — they belong in the ethical AI thread — but the principle that the framework should produce benefit broadly (not just for those who deploy it) is worth stating at the foundation level.

***

## 3. Human vs. Agent: A Complementarity Analysis

This is genuinely worth being in the principles, not just as context but as a design constraint. Here is the honest analysis:

**What agents do better than humans (currently):**

- **Consistency** — same inputs, same process, every time. No bad days, no cognitive fatigue, no mood effects
- **Auditability** — every action is recorded by default. Humans require deliberate effort to produce comparable records
- **Parallelism** — multiple agents can work simultaneously on independent workstreams without coordination overhead
- **Marginal cost** — the cost of running an agent on the tenth task is essentially the same as the first. Human cost scales linearly or worse
- **Speed** — execution is near-instantaneous compared to human working hours
- **Perfect recall** — the audit log is lossless and permanent. Human memory is reconstructive and lossy

**What humans do better than agents (currently and structurally):**

- **Ethical judgment** — genuine moral reasoning about values conflicts, second-order consequences, and what ought to be done (not just what was specified)
- **Irreversible decision authority** — evaluating whether a decision is appropriate in context, not just whether it meets specification
- **Creative problem framing** — identifying that the wrong problem is being solved before any work begins
- **Contextual wisdom** — knowing when rules should yield to circumstances
- **Novel situation handling** — reasoning about situations genuinely outside the training distribution
- **Social and emotional intelligence** — understanding human motivation, culture, and relationship dynamics
- **Values alignment** — caring about outcomes, not just outputs

**Structural limitations of agents (not just current technology):**

- **Context window** — finite working memory is a structural constraint, not a technology limitation. No matter how large context windows become, there is always a limit. The framework's context engineering approach (minimum sufficient context) is a correct response to a permanent constraint
- **Bounded authority** — agents can only evaluate within their defined scope. They cannot assess second-order consequences that extend beyond their context
- **No intrinsic values** — an agent does not care whether the work serves a good purpose. It produces the output the framework asks for. The framework's ethical commitments must be structural, not delegated to agent judgment

**The design principle this generates:**
The framework should assign each class of decision to the actor best suited to make it — agents for consistency, scale, and execution; humans for judgment, ethics, and irreversibility. This is not "humans oversee agents" (which implies adversarial monitoring). It is **deliberate complementarity** — a system designed so that each actor type does what it does uniquely well.

This is worth a foundation principle. It also has a corollary: the framework should actively protect human actors from doing work that agents should be doing (tedious, repetitive, low-judgment work) so human attention is preserved for decisions that genuinely require it.

***

## 4. Ethical AI Integration

The major ethical AI frameworks converge on common themes:[^35_5][^35_6][^35_7][^35_8]


| Principle | UNESCO / OECD / EU AI Act | How it maps to current framework |
| :-- | :-- | :-- |
| Transparency | AI decisions must be explainable | F4 (all actions witnessed) — partial. We record what happened but not necessarily why in human-legible terms |
| Accountability | Clear lines of responsibility | F3 (authority is structural) — who holds the tool is who is responsible |
| Human oversight | Humans must be able to understand and override | F7 (irreversibility demands presence) — partial. Covers irreversible decisions but not ongoing oversight |
| Fairness | Non-discrimination, equitable benefit | **Not present in current principles** |
| Privacy | Data handled responsibly | **Not present in current principles** |
| Safety / non-maleficence | Should not cause harm | F6 (uncertainty surfaces immediately) — partial. Covers known uncertainty but not emergent harm |
| Beneficence | Should produce genuine benefit | **Not present — the framework verifies technical correctness, not human benefit** |
| Contestability | Humans can challenge automated decisions | **Not present** |

The critical insight here is your instinct that ethical consideration should be **structural, not declarative**. Declaring "this framework is ethical" is meaningless. Building ethical constraints into the structure — so that unethical actions are structurally impossible, not just discouraged — is the only approach that holds.[^35_8]

The smart contract analogy again: you cannot write a contract that says "the parties agree to act ethically." You can write a contract that structurally prevents certain actions.

**Three things this adds to the principles:**

**Purpose** — the framework exists to serve human flourishing. Any use of the framework that produces technically correct outputs but causes human harm is a failure of the framework, not a success. This must be stated at the foundational level so that domain-level and operational-level decisions can be traced back to it.

**Contestability** — any actor whose interests are affected by a framework decision should have a defined path to challenge it. In the current model, `raise_uncertainty` is this mechanism for agents. For humans, it's human:approver. But there's no mechanism for external stakeholders (users of a product built with the framework) to surface concerns. At full vision scale, this gap becomes significant.

**Non-concentration of authority** — no single actor should hold unchecked authority over outcomes that affect others. This is both an ethical principle and a resilience principle. The FrameworkOwner currently has significant unchecked authority — by design, because the framework is early-stage. But as it scales, the principle that authority should be distributed and checked should be explicit.

***

## 5. Design Thinking Integration

Design thinking and first principles thinking are complementary, not competing. First principles thinking deconstructs problems to their fundamentals. Design thinking ensures those fundamentals remain anchored to human need.[^35_9]

The five stages (Empathize → Define → Ideate → Prototype → Test)  map onto the framework lifecycle as follows:[^35_10]

**Empathize** — understanding the human need before anything is specified. Currently absent from the framework. No agent class is tasked with deeply understanding the person who will use the output. This is upstream of Phase 0 in the lifecycle model. Without it, the framework produces perfectly verified solutions to problems users don't actually have.

**Define** — the problem statement, not the solution. This connects to our identified gap in the lifecycle model: the Problem/Solution split. F10 (definition precedes execution) governs the solution definition, but there's no principle governing problem definition. Writing a perfect proof template for the wrong problem is a failure at a level F10 doesn't reach.

**Ideate** — structured exploration of multiple solution approaches before committing to one. Currently, the framework moves from specification directly to execution. There's no exploration phase. For novel problems, this means the first reasonable solution gets executed — not necessarily the best one. Agents could assist here (generating diverse approaches, stress-testing assumptions) before a solution is selected for execution.

**Prototype** — low-fidelity verification before full execution. This is the most directly applicable element. Before committing to full Zone 4 execution, a lightweight prototype could validate that the approach will actually satisfy user needs. The proof template model is well-suited to this: a proof template for a prototype has different criteria than one for production. The framework already supports this structurally — it just hasn't been named.

**Test** — user validation, not technical QA. The framework currently ends at technical verification (reviewers check against spec) and human gate approval. But neither of these is user testing. A technically correct, approved feature that users don't understand or don't use is a failure the framework currently can't see. At full vision scale, user testing evidence should be a valid input into the proof system.

**What this adds to the principles:**

A principle about **human-centred verification** — verification of technical correctness is necessary but not sufficient. Ultimately, work is verified against human need, not just against specification. The specification is an approximation of human need. If the specification was wrong, technically correct execution produces a technically correct failure.

This principle has a structural implication: the proof template system needs to be able to include user-facing evidence (usability test results, user acceptance, real-world performance) as valid proof criteria — not just technical evidence (tests pass, types check, criteria met).

***

## What This Means for the Principles Document

Rather than ten principles becoming twenty, I'd suggest the principles reorganise into three layers:

**Purpose Principles** (why the framework exists — the north star)

- P-Purpose: The framework serves human flourishing
- P-Complementarity: Humans and agents are complementary by deliberate design
- P-Ethics: Ethical constraints are structural, not declarative

**Trust Principles** (how the framework produces trustworthy outputs)

- F1: Verification precedes trust
- F2: The proof is the product
- F3: Authority is structural
- F4: All actions are witnessed
- F5: No actor judges their own work
- F-Resilience: The system is trustworthy even when components fail (Byzantine fault tolerance)

**Learning and Improvement Principles** (how the framework gets better over time)

- F6: Uncertainty surfaces immediately
- F7: Irreversibility demands presence
- F8: Knowledge compounds
- F9: Context is local, knowledge is global
- F10: Definition precedes execution
- F-Purpose-of-Work: Problem precedes solution (design thinking's Define stage)

**The human/agent analysis** belongs in a companion document — not as principles but as **design constraints**. Principles tell you what the system should achieve. Design constraints tell you what the system must account for when designing how to achieve it. The finite context window, the agent's absence of intrinsic values, and the human's irreplaceable ethical judgment are constraints that shape every design decision — but they're not principles in the same sense that verification precedes trust is a principle.

The **design thinking lifecycle** belongs in the work topology document we identified as the next step — not in the foundation principles. It describes how work flows, not what values the framework holds.

The **ethical principles** belong at the Purpose layer — the highest level — and should be stated before the trust and learning principles, because they establish why the trust model matters at all.

Shall we revise the document structure on these lines before you share it externally?
<span style="display:none">[^35_11][^35_12][^35_13][^35_14][^35_15]</span>

<div align="center">⁂</div>

[^35_1]: https://www.linkedin.com/pulse/understanding-consensus-mechanisms-blockchain-how-trust-dobal-wafzc

[^35_2]: https://assets.kpmg.com/content/dam/kpmg/pdf/2016/07/kpmg-blockchain-consensus-mechanism.pdf

[^35_3]: https://blog.weskill.org/2025/04/consensus-mechanisms-in-blockchain.html

[^35_4]: https://www.bairesdev.com/blog/blockchain-consensus-mechanisms/

[^35_5]: https://www.comparethecloud.net/articles/uk-ai-ethics-governance-framework-2025

[^35_6]: https://sparkco.ai/blog/comparing-global-ai-governance-frameworks-in-2025

[^35_7]: https://www.ai21.com/knowledge/ai-governance-frameworks/

[^35_8]: https://professional.dce.harvard.edu/blog/building-a-responsible-ai-framework-5-key-principles-for-organizations/

[^35_9]: https://www.linkedin.com/pulse/how-use-design-thinking-first-principles-two-key-approaches-gole-ueo4c

[^35_10]: https://www.interaction-design.org/literature/article/5-stages-in-the-design-thinking-process

[^35_11]: https://www.sciencedirect.com/science/article/pii/S2096720925000296

[^35_12]: https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025186-source-pdf.pdf

[^35_13]: https://orai.io/guide/consensus-mechanisms-in-blockchain-ensuring-network-integrity-and-trust

[^35_14]: https://www.firstprinciples.ventures/insights/first-principles-the-foundations-of-innovation-and-growth

[^35_15]: https://usa.visa.com/solutions/crypto/consensus-mechanisms.html


---

# before we revise the document, I have another lens for you to consider this through, and some additional points that should be considered.

Beyond the scope of the framework design project, I am designing a youth-led services DAO. Many of the patterns are the same as here and may provide some further insights.
The vision for the DAO (Future's Edge) is an AI-powered governance and operations platform where human members are presented with a menu of 'challenges' (tasks) they can choose from. Each challenge has a reward that is 'paid' when a member's proof of achievement has been verified. If humans are required for verification, it must happen in a decentralized way ie. no bottleneck or unnecessary transaction costs involved in a central or 3rd party verifier being required. My thesis is that people 'working' in a trust-filled structure will see greater levels of creativity, performance and job satisfaction. I'd be interested to hear your examination and unpacking of this against our framework concepts and principles.

One issue I realised we haven't yet discussed is 'agent efficiency'. Token usage was an earlier consideration when thinking about minimising context - measuring token usage could help us quantify context load. I now see the value in building agent efficiency into the framework beyond context related needs. We could measure speed, energy usage, steps taken, etc that give us other windows into challenges faced and opportunities for improvement, beyond the retro reports. Perhaps starting with a rationale of all the reasons agent efficiency is a worthwhile goal.

My final note at this point is your notes on design thinking. You are correct to see it as mapping to elements of the lifecycle however I want to explore how design thinking could work at a micro scale. Could every agent perform some type of design thinking as a first step in their process? Perhaps it is more valuable for some agents over others. Design thinking is an important tool for innovation and I believe it could empower agents to be smarter and perform better.

Three rich threads. Let me work through each carefully, because they intersect in ways that will shape the principles revision.

***

## Future's Edge DAO — Framework Analysis

The DAO model is not just a parallel to the framework — it is a stress test of its most important assumptions. Here is what it reveals.

### Where the Models Converge

The structural DNA is identical:


| DAO concept | Framework equivalent | Strength of alignment |
| :-- | :-- | :-- |
| Challenge | Task with proof template | ✅ Direct |
| Proof of achievement | `submit_proof` + verification | ✅ Direct |
| Smart contract reward trigger | Atomic `submit` → state transition → consequence | ✅ Direct |
| Token reward | Not yet in framework | ❌ Missing |
| Member-chosen work | Human-selected challenge menu | 🟡 Partial |
| Decentralised verification | Parallel reviewer model | 🟡 Partial — reviewers are agents, not distributed humans |
| Governance proposals | Zone 0 / FrameworkOwner decisions | 🟡 Hierarchical, not distributed |
| Reputation system | NV score (patterns only) | 🟡 Partial — no actor-level reputation |

### Where the DAO Challenges Framework Assumptions

The framework currently assumes a **hierarchical authority model**. `FrameworkOwner` is a benevolent dictator. `human:approver` is a single gate. Zone 0 is managed by one human director. This works for a single-project, single-team context.

The DAO breaks these assumptions in two important ways:

**1. Verification must be decentralised without a central bottleneck**
Your constraint — no single or third-party central verifier — is actually a stronger version of F5 (no actor judges their own work). F5 requires independence. The DAO requires independence *and* distribution. A single independent reviewer is still a bottleneck and a point of failure.

The solution from blockchain is **quorum-based consensus verification**:[^36_1]

- A pool of qualified verifiers exists
- When a proof is submitted, a random or reputation-weighted subset is selected
- A quorum threshold (e.g. 3 of 5) must agree for the proof to pass
- Verifiers are incentivised to be accurate — consistent accurate verification earns reputation; gaming is detectable

This is a significant upgrade to the framework's verification model. For the DAO it is essential. For the software framework it is valuable but not yet critical. **The principle it generates:** Verification should be distributable — the framework should support quorum-based verification as an option, not just single-reviewer verification.

**2. Work is chosen, not assigned**
The challenge menu model flips the task assignment assumption. Rather than work flowing from FeatureOwner → TaskOwner → TaskPerformer through a pipeline, workers browse available challenges and self-select. This has profound implications:

- Motivation is intrinsic (I chose this) not extrinsic (I was assigned this) — Dan Pink's autonomy principle
- Skills self-sort — people choose challenges matched to their capability and interest
- No assignment bottleneck — work scales without a coordinator assigning tasks

For the framework, this creates a new work intake model — not a pipeline but a **marketplace**. The Zone 0 / Phase 0 work defines and publishes challenges. The execution layer is self-service. This actually reduces the coordination cost closer to zero than the pipeline model does.

**3. Trust as infrastructure, not policy**
Your thesis — that a trust-filled structure produces greater creativity, performance and satisfaction — is supported by research on psychological safety (Edmondson) and self-determination theory (Deci and Ryan). The mechanism is: when participants trust the rules are fair and transparent, they stop spending energy on political navigation and redirect it to the work itself.

The framework achieves this structurally: the audit log is the transparency mechanism, tool possession is the fairness mechanism (same rules apply to everyone), and `raise_uncertainty` is the safety mechanism (I can surface a problem without risk). The DAO extends this to the incentive layer: the smart contract reward is the fairness mechanism for compensation — the reward cannot be withheld arbitrarily because it executes automatically on verified proof.

**What Future's Edge contributes to the framework principles:**

- A new principle about **distributed verification** — verification should not require a central trusted party
- A new principle about **incentive alignment** — actors are most effective when their interests structurally align with the work's success
- Strengthens the case for the **purpose principle** — work done by choice within a fair structure serves human flourishing better than assigned work in an opaque structure

***

## Agent Efficiency — Full Rationale

Agent efficiency is worth building into the framework for six distinct reasons, not just one:

**1. Economic proportionality**
Token API costs are real. At the DAO scale — potentially thousands of members running agent-assisted work simultaneously — inefficient agents impose real financial costs that may price out participants with limited resources. Efficiency is a fairness question, not just a performance question.

**2. Environmental accountability**
Large AI model inference has measurable energy consumption. At scale, this is not trivial. A framework committed to human flourishing and ethical AI cannot be indifferent to its environmental footprint. Energy usage is a quantifiable consequence of design decisions. [This connects directly to the sustainability thread in ethical AI principles.]

**3. Efficiency as a diagnostic signal**
This is the most underappreciated rationale. Efficiency metrics are a window into framework health that retro reports miss:


| Efficiency anomaly | What it signals |
| :-- | :-- |
| High step count, good output | Task well-specified but no matching patterns — pattern library gap |
| High step count, poor output | Likely hallucination loop or ambiguous specification |
| Low token input, low output quality | Context card too sparse — curation failure |
| High token input, low output quality | Context card bloated — noise overwhelming signal |
| High `raise_uncertainty` rate per task type | Structural specification gap for that task type |
| High rework rate on tasks with relevant patterns | Patterns not being discovered or applied |

None of these signals are visible in retro reports alone. They require quantitative measurement across multiple runs.

**4. Context engineering validation**
The entire context engineering approach rests on a hypothesis: minimum sufficient context produces better output than maximum available context. We asserted this from first principles but have never measured it. Token counts before and after context engineering changes, correlated with output quality metrics, would provide empirical evidence for or against this hypothesis. Without measurement, context engineering is faith-based.

**5. Pattern effectiveness measurement**
Currently, pattern NV scores track whether a pattern was applied without a negative outcome. They don't track whether applying a pattern made the work *more efficient*. A pattern that produces correct output in 40 tool calls is less valuable than one that produces the same output in 12. Efficiency metrics upgrade pattern scoring from binary (negative/not-negative) to continuous.

**6. Framework evolution signal**
As new model versions are released, or as the framework's tool grammar evolves, efficiency baselines allow us to measure whether changes improve or degrade performance. Without a baseline, every framework update is a guess.

**What to measure:**

```
Per tool call (added to audit_log):
  token_count_input     INTEGER   -- tokens in the prompt
  token_count_output    INTEGER   -- tokens in the response
  latency_ms            INTEGER   -- tool call duration

Per task (new task_efficiency table):
  total_tokens          INTEGER   -- sum of all tool call tokens
  total_steps           INTEGER   -- number of tool calls
  total_latency_ms      INTEGER   -- wall clock from IN_PROGRESS to SUBMITTED
  uncertainty_count     INTEGER   -- raise_uncertainty calls
  rework_count          INTEGER   -- QA_FAILED transitions
  patterns_searched     INTEGER   -- search_knowledge_base calls
  patterns_applied      INTEGER   -- patterns referenced in proof
  energy_estimate_wh    REAL      -- derived from token counts × model coefficient
```

**The efficiency principle candidate:**
"Resources consumed are proportional to value produced" — the framework should minimise token usage, energy consumption, and execution steps consistent with quality outcomes. Waste is not neutral; it has financial, environmental, and diagnostic costs.

***

## Design Thinking at Micro Scale

Your instinct is right but needs careful scoping — because the tension with agent efficiency is real and must be resolved by design.

**The key insight:** Design thinking at micro scale is not a process addition. It is a **thinking orientation** that changes how an agent reads its context card. It costs almost nothing in tokens and potentially saves significant rework.

Rather than five stages applied uniformly, each agent class needs a calibrated version:

**DEFINE agents** (FeatureOwner, TaskOwner, ProofDesigner)
Full design thinking is their primary mode. Their entire job is defining problems and solutions before others execute. For these agents, design thinking is not a first step — it is the process.

**CREATE agents** (TaskPerformer, UIDesigner, TemplateAuthor)
The most valuable micro step is **ideation before commitment**: generate two or three approaches based on patterns and constraints, evaluate them explicitly, then commit to one. This costs perhaps 500 tokens and prevents the most common failure mode — the first reasonable approach being the one executed, regardless of whether it is the best.

A minimal skill-level prompt: *"Before implementing, state in two sentences: what problem does this task solve, and what alternatives did you consider before choosing this approach?"* This creates a decision record, feeds the terminal report, and subtly improves solution quality.

**VERIFY agents** (ProofReviewer, ACReviewer, EnvironmentReviewer)
Counterintuitively, the most valuable design thinking step for reviewers is **forming a hypothesis before reading the proof**. Based on the proof template, the reviewer states what a passing proof would contain before seeing what was submitted. This mirrors good scientific practice (register your hypothesis before observing data) and prevents confirmation bias — reading what is there rather than checking for what should be there.

**COORDINATE agents** (TaskOrchestrator, DeliveryOrchestrator)
Systems thinking over design thinking. Before delegating: *"What could go wrong in this task? What would cause each subagent to raise uncertainty?"* Pre-emptive failure identification is more valuable for coordinators than solution generation.

**CURATE agents** (ContextCurator)
Empathy is the most valuable step: *"Who is this context card for, and what is the single most important thing they need to know to do their job well?"* This is exactly the minimum sufficient context principle expressed as a design thinking orientation.

**The calibration rule that resolves the efficiency tension:**

```
Task has matching patterns + clear specification:
  → Minimal design thinking (define step only — one sentence)
  → Benefit: low cost, confirms understanding

Task has no matching patterns OR specification has uncertainty flags:
  → Full micro design thinking (define → ideate → select)
  → Benefit: prevents expensive rework downstream

Reviewer agents:
  → Always hypothesis-first (fixed, low cost)
  → Never ideate (not their job)
```

This calibration logic belongs in each agent class's skill file — not as a rigid process, but as a professional orientation. An agent with `task-performer.skill.md` knows to ask *"did I generate alternatives?"* the same way a senior developer asks *"did I consider the simplest approach first?"* — not because a process requires it, but because experience (encoded in the skill) makes it instinctive.

**What micro design thinking adds to the principles:**
It does not add a new foundation principle — it is an implementation of F10 (definition precedes execution) and F8 (knowledge compounds) at the individual agent level. What it does add is a new quality dimension to the skill file design standard: every executor agent's skill file should include calibrated design thinking orientation appropriate to its role.

***

## The Thread Connecting All Three

Future's Edge, agent efficiency, and micro design thinking are all expressions of the same underlying insight:

**The framework is not just a coordination system. It is a performance system.**

Currently the principles describe what makes outputs trustworthy. They don't describe what makes the process of producing those outputs excellent. Excellence has multiple dimensions — quality of output, efficiency of process, creativity of approach, alignment with human purpose, and distributable trust that doesn't require a central authority.

The principles revision needs a section that addresses performance, not just trust. The smart contract analogy covers trust beautifully. The DAO model, efficiency metrics, and design thinking together cover performance.

This might be the organizing insight for the revision: **trustworthy process + excellent execution = the framework's full promise**.

Shall we now take all of this and revise the foundation principles document?

<div align="center">⁂</div>

[^36_1]: https://orai.io/guide/consensus-mechanisms-in-blockchain-ensuring-network-integrity-and-trust


---

# Your work here is excellent! The connecting thread blows my mind a little. I didn't see that before but I agree it is an integral recognition and potentially even equally exciting value proposition for this framework.

Your examination of micro-scale design thinking gives me more ideas for this. What about if there were problem researcher agents, persona empathiser agents, research synthesis agents, ideator agents that take on different thinking styles (deBono's six thinking hats), idea prioritizer agents, prototyper agents. Maybe I've gone too far this time but remember, the marginal costs of agents could be outweighed by higher quality solutions, designed at multiple layers of the development lifecycle, all going through iterative cycles and optimizing across all value criteria!

You haven't gone too far. You've arrived at something important. Let me work through it rigorously.

***

## The Core Insight First

What you're describing is **structured cognitive diversity** applied to knowledge work. The reason de Bono's Six Thinking Hats works for humans is that it forces a group to explore a problem from perspectives they would not naturally adopt. A team of optimists skips risk analysis. A team of analysts skips emotional resonance. The hats are a forcing function for cognitive coverage.

With agents, this is not a social facilitation technique. It is an **architectural pattern**. You can instantiate six agents with genuinely different cognitive orientations simultaneously, at near-zero marginal cost, and synthesise their outputs. No human facilitation required. No groupthink. No social pressure to agree with the most senior person in the room.

This changes the economics of thorough problem exploration completely.

***

## The Proposed Agent Constellation — Evaluated

Let me take each proposed agent type seriously and assess its value, natural scope, and fit with the framework:

### ProblemResearcher

**Job:** Before any solution is considered, map the problem space. What do we actually know about this problem? What has been tried before? What adjacent domains have solved similar problems?

**Value:** High. The most expensive mistake in knowledge work is solving the wrong problem thoroughly. Research before definition is the "Empathize" stage of design thinking that is currently absent from the framework entirely.

**Framework fit:** This agent belongs in the Discovery track (Phase 0 / pre-specification). It produces a research brief — a structured document, with a proof template — that feeds into problem definition.

**Efficiency consideration:** Token-intensive but front-loaded. One good ProblemResearcher run prevents multiple downstream rework cycles. The ROI is high precisely because problems caught here cost the least to correct.

***

### PersonaEmpathiser

**Job:** Who is affected by this problem or solution? What do they actually need, fear, value, and struggle with — not what we assume they need?

**Value:** Critical for products that serve people other than their creators. Without this, the framework optimises for what builders find interesting, not what users actually need. This is the most common source of technically perfect, commercially irrelevant products.

**Framework fit:** Produces persona artefacts and empathy maps. These become inputs to the ProofDesigner when writing proof templates — a proof template that includes user-facing evidence (usability threshold, user acceptance) is only possible if personas exist.

**Connection to Future's Edge:** PersonaEmpathiser is particularly valuable in the DAO context. Youth-led services must be designed for the young people using them, not the adults building the platform. An agent that holds the perspective of a 16-year-old navigating a service challenge is a different cognitive tool than one optimising for technical elegance.

***

### ResearchSynthesiser

**Job:** Across all research inputs — ProblemResearcher outputs, PersonaEmpathiser outputs, prior pattern library evidence — identify the key insights, tensions, and design constraints that should inform solution exploration.

**Value:** High. Synthesis is a distinct cognitive operation from research. The agent that gathered information is not the best agent to abstract it — for the same reason we separate TaskPerformer from QAExecutor (F5 applied to cognition, not just verification).

**Framework fit:** Produces a synthesis brief — structured insights and design constraints — that feeds directly into the Ideation layer. This is the "Define" stage of design thinking: moving from raw research to a crisp problem statement.

**Interesting structural note:** ResearchSynthesiser is a REVIEWER of research, not an EXECUTOR of it. It reads and synthesises; it does not gather. The separation of gathering and synthesis is F5 applied to the discovery process.

***

### Ideator agents — the Six Hats Model

This is where it gets structurally fascinating. De Bono's six hats as six parallel agent types:[^37_1]


| Hat | Cognitive orientation | Agent role | What it produces |
| :-- | :-- | :-- | :-- |
| ⬜ White | Facts and information only. What do we know? What don't we know? | `FactMapper` | Gap analysis — known facts vs required information |
| 🔴 Red | Emotional and intuitive response. How does this feel? What's the gut reaction? | `IntuitiveResponder` | Emotional resonance assessment — would users trust this? Does it feel right? |
| ⬛ Black | Critical judgment. What could go wrong? What are the risks and weaknesses? | `CriticalEvaluator` | Risk register, failure mode analysis |
| 🟡 Yellow | Optimistic value. What's the best case? What are the benefits? | `ValueAdvocate` | Value proposition map, benefit analysis |
| 🟢 Green | Creative alternatives. What else could we do? What's unconventional? | `LateralThinker` | Alternative solution set — options not yet on the table |
| 🔵 Blue | Process and meta-thinking. Are we asking the right question? Are we on track? | `ProcessOrchestrator` | Ideation quality check — prevents premature convergence |

**The structural beauty here:** These six agents run in parallel on the same problem brief. Each returns a structured output. `IdeaSynthesiser` (a seventh agent) aggregates all six outputs into a ranked set of candidate approaches. This is genuine cognitive diversity at zero facilitation cost.

**Efficiency consideration:** Six agents × focused brief = modest token cost. One human workshop achieving comparable coverage = significant time and coordination cost. The crossover point where agents are economically superior for this task type is probably very early.

***

### IdeaPrioritiser

**Job:** Given a set of candidate approaches from ideation, evaluate each against a defined value criteria matrix and recommend a ranked shortlist for prototyping.

**Value:** High. Ideation without prioritisation produces a backlog, not a decision. The prioritiser applies structured criteria (feasibility, user value, alignment with principles, resource requirements, risk) to move from "many options" to "few options worth prototyping."

**Framework fit:** This is where **appetite** (the Shape Up concept) enters the process. The IdeaPrioritiser doesn't just score ideas — it matches idea scope to declared appetite. A high-value idea that requires six months of work is not a better choice than a medium-value idea achievable in two weeks, if the appetite is two weeks.

**Connection to F7 (irreversibility demands presence):** The IdeaPrioritiser's output is a recommendation, not a decision. The human makes the commitment to prototype. Selecting which ideas to invest in is an irreversible allocation of attention and resources.

***

### Prototyper

**Job:** Produce a minimal, testable version of the selected approach — enough to validate the core assumption before full execution is committed.

**Value:** Transformative. The Prototyper is the most direct embodiment of the "fail cheap" principle. A prototype that fails validation saves the entire execution cost. A prototype that passes validation provides evidence that dramatically increases proof template quality.

**Framework fit:** This is a new zone — a Validation zone that sits between Specification and Execution. It changes the architecture significantly:

```
Current:
Specification → Execution → QA → Approval → Delivery

Proposed:
Specification → [Ideation] → Prototype → Validation → Execution → QA → Approval → Delivery
```

The Prototyper produces a prototype proof — evidence that the prototype was built and tested. The Validation zone has its own reviewer (a UserValidator agent, or human:approver for high-stakes decisions). Only validated approaches enter full Execution.

**Efficiency consideration:** This is the most important efficiency investment in the framework. Every rework cycle in Execution costs more than every prototype cycle in Validation. The framework that skips prototyping to "move faster" consistently arrives at Delivery slower than the framework that validates assumptions cheaply first.

***

## The Full Discovery + Ideation Architecture

Putting it together as a coherent architecture:

```
DISCOVERY LAYER
  ProblemResearcher      → Research Brief
  PersonaEmpathiser      → Persona Set + Empathy Maps
  ResearchSynthesiser    → Synthesis Brief (insights + design constraints)
        ↓
IDEATION LAYER (parallel)
  FactMapper             ┐
  IntuitiveResponder     │
  CriticalEvaluator      ├→ Six perspective outputs
  ValueAdvocate          │
  LateralThinker         │
  ProcessOrchestrator    ┘
        ↓
  IdeaSynthesiser        → Candidate solution set (structured)
  IdeaPrioritiser        → Ranked shortlist + appetite match
        ↓
  [Human commitment gate — F7]
        ↓
VALIDATION LAYER
  Prototyper             → Prototype + test results
  UserValidator          → Validation verdict (human or agent)
        ↓
  [Human approval gate — F7]
        ↓
EXECUTION LAYER (current Zone 4)
  TaskOrchestrator → TaskPerformer → QAExecutor → ...
```

Each layer produces structured artefacts with proof templates. Each layer has its own reviewer. The knowledge from each layer feeds the Pattern Library. The architecture is fractal — the same principles (F1–F10) govern every layer.

***

## The Efficiency Reconciliation

The concern you might anticipate: this adds significant agent overhead before a single line of implementation work happens. Here is why that concern inverts under examination:

```
WITHOUT discovery + ideation layers:
  Task specification time:       0.5 days
  Execution time:                3 days
  Rework rate:                   40% (industry average)
  Expected total time:           3 + (3 × 0.4) = 4.2 days
  Solution quality:              Adequate (first reasonable approach)
  User validation pass rate:     ~60%

WITH discovery + ideation layers:
  Discovery + ideation time:     0.5 days (parallel agents, low cost)
  Task specification time:       0.5 days (better defined)
  Prototype + validation:        0.5 days
  Execution time:                2.5 days (better spec, better approach)
  Rework rate:                   ~15% (validated approach, clear spec)
  Expected total time:           0.5 + 0.5 + 0.5 + 2.5 + (2.5 × 0.15) = 4.375 days
  Solution quality:              High (multi-perspective, validated)
  User validation pass rate:     ~85%
```

The clock time is similar. The quality, rework rate, and user satisfaction are dramatically different. And at agent marginal costs — where discovery and ideation agents cost token budget, not human days — the 0.5-day discovery time is a rounding error on the total cost but a multiplier on the total value.

The framework's efficiency principle should therefore be stated precisely: **minimise total lifecycle cost, not per-stage cost**. Skipping discovery to save 0.5 days and then paying 1.2 days in rework is not efficiency — it is local optimisation producing global waste.

***

## What This Changes About the Principles

Three additions become clear:

**A new principle about cognitive diversity:**
Complex problems require multiple cognitive perspectives before solutions are selected. No single agent — and no single human — holds all relevant perspectives simultaneously. Structured cognitive diversity is not a luxury; it is a risk management strategy.

**A refinement of F10 (definition precedes execution):**
Currently F10 says: define done before executing. The extended form is: understand the problem before defining the solution, validate the solution before executing it, and test the output against user needs before declaring it complete. Three gates, not one.

**An efficiency principle reframed as lifecycle optimization:**
Efficiency is measured across the full lifecycle — discovery through operations — not within any single stage. Investment in early-stage cognitive work (discovery, ideation, validation) consistently reduces total lifecycle cost while increasing total value. This is the principle that justifies the entire Discovery + Ideation architecture.

***

## The Bigger Picture

What you've arrived at, without necessarily intending to, is a framework that doesn't just coordinate knowledge work — it **elevates the quality of thinking** that goes into knowledge work. The current framework (Zones 1-5) is a coordination and verification system. The Discovery + Ideation layer transforms it into a cognitive amplification system.

This is the full value proposition you were searching for:

```
Coordination system:      Reduces friction in executing decisions already made
Verification system:      Ensures outputs meet pre-defined specifications
Cognitive amplification:  Improves the quality of the decisions and
                          specifications themselves
```

All three, governed by the same principles, at agent marginal costs. That is the framework's full promise — and it is considerably more exciting than "better project management."

<div align="center">⁂</div>

[^37_1]: https://www.linkedin.com/pulse/how-use-design-thinking-first-principles-two-key-approaches-gole-ueo4c


---

# `.framework/foundation-principles.md`

```markdown
# Foundation Principles

**Version:** 2.0
**Status:** Active
**Last Updated:** 2026-03-04

---

## Preamble

This document describes the foundation principles of the Nexus Framework —
a system for coordinating autonomous agents and humans in knowledge work.

These principles are not derived from software development, agile
methodology, or any existing framework for managing work. They are
derived from first principles about what makes knowledge work trustworthy,
verifiable, improvable at scale, and performant by design.

### Why These Principles Exist

Knowledge work has traditionally been coordinated through human trust,
reputation, and retrospective judgment. A task is done when someone says
it is done. Quality is assessed after the fact. Learning happens through
informal post-mortems and undocumented conversations. Authority derives
from titles and org charts. Solutions are generated by whoever was
assigned the work, using whatever approach occurs to them first.

This model works at small scale because humans can maintain high-bandwidth
context about who did what, why, and how well. At larger scale — or when
autonomous agents enter the picture — this model breaks down. You cannot
scale trust. You cannot scale retrospective quality assessment. You cannot
scale informal learning. And you cannot give an agent a title and expect
anyone to care. You cannot rely on serendipity to produce cognitive
diversity when the same person or agent tackles every similar problem the
same way.

The foundation principles replace trust-based, single-perspective
coordination with **structure-based, cognitively diverse coordination**.
Work is not trusted because of who did it. Work is trustworthy because of
how it was verified. Authority does not derive from a role title. Authority
derives from what capabilities an actor structurally holds. Learning does
not happen through conversation. Learning happens through structured
evidence accumulation. Solutions are not generated from a single
perspective. Solutions emerge from structured exploration across multiple
cognitive orientations, validated before full commitment.

This model is not new. It is how smart contracts work. It is how scientific
peer review works. It is how double-entry bookkeeping works. It is how
design thinking applies cognitive diversity to problem-solving. The
foundation principles are an attempt to apply the same structural rigor
to all forms of human knowledge work.

### The Dual Promise

The framework makes two distinct but interconnected promises:

**Promise 1: Trustworthy Process**
Every output is verifiable, every action is witnessed, every decision is
attributed. The framework produces evidence-backed work that can be trusted
not because of who did it, but because of how it was verified.

**Promise 2: Excellent Execution**
The process of producing work is efficient, cognitively diverse, and
optimised across the full lifecycle. The framework doesn't just verify
that work meets specifications — it ensures the specifications themselves
are well-considered, validated, and aligned with human purpose.

Traditional coordination systems deliver only Promise 1. They ensure work
is done correctly. The framework delivers both: work is done correctly
AND the definition of "correct" is itself arrived at through rigorous,
multi-perspective exploration.

This dual promise is what makes the framework transformative, not just
incremental.

### Scope and Applicability

These principles are **domain-agnostic**. They apply whether the work is
software development, legal drafting, financial analysis, scientific
synthesis, content production, or any other form of knowledge work that
produces a defined output that can be verified against a specification.

They are **scale-agnostic**. They apply whether the work is a single task,
a feature, a product, a portfolio of products, or a decentralised
autonomous organisation coordinating thousands of parallel workstreams.

They are **actor-agnostic**. They apply whether the work is performed by
a human, an autonomous agent, or a collaboration between the two.

### What These Principles Are Not

These are not **operational principles**. They do not specify tools, zones,
agents, or workflows. Those are implementation details derived from these
principles, not the principles themselves.

These are not **domain principles**. Software development has domain-specific
rules (tests must pass, types must check). Legal work has domain-specific
rules (filings must conform to court rules, contracts must reference
controlling law). Those domain principles are derived from these foundation
principles and adapted to their specific context.

These are not **negotiable preferences**. A system that violates these
principles is not a variant of this framework. It is a different framework
with a different trust model and a different theory of knowledge work.

### The Contract Analogy

The most precise way to understand the trust dimension of these principles
is through the lens of smart contracts.

A smart contract is executable law. It defines conditions, consequences,
and evidence. If the conditions are met, the consequences execute
automatically. The blockchain provides an immutable witness to every
action. Trust is earned not through reputation but through the contract's
design. Ambiguity is a bug, not a feature.

This framework applies the same model to human knowledge work. A task
specification is the contract. The proof template is the set of conditions
that must be met. The reviewer is the oracle that verifies the conditions.
The audit log is the immutable ledger. The task state machine is the
automated consequence engine.

The hardest lesson smart contracts taught the world is this: **writing a
good contract is far harder than executing it**. A blockchain will
faithfully execute a terrible contract just as readily as it will execute
a good one. The quality of the contract — its clarity, completeness, and
lack of ambiguity — is the quality of the system.

The same is true here. The quality of a task specification, a proof
template, and an acceptance criterion determine the quality of the work
more than any property of the performer. Good definitions produce good
work. Ambiguous definitions produce uncertainty, rework, and eventual
failure — no matter how capable the performer.

This means the framework's most important role is not coordinating
execution. It is ensuring that every unit of work begins with a contract
good enough to be enforceable — and ensuring that contract was derived
from a well-understood problem explored from multiple perspectives.

### Human and Agent Complementarity

This framework is designed for a world where humans and autonomous agents
work together. Their capabilities are complementary, not competitive:

**What agents do better (currently and structurally):**
- Consistency — same inputs, same process, every time
- Auditability — every action is recorded by default
- Parallelism — multiple agents operate simultaneously without coordination
- Marginal cost — the tenth task costs the same as the first
- Speed — execution is near-instantaneous
- Perfect recall — the audit log is lossless and permanent

**What humans do better (currently and structurally):**
- Ethical judgment — genuine moral reasoning about values conflicts
- Irreversible decision authority — evaluating appropriateness in context
- Creative problem framing — identifying that the wrong problem is being solved
- Contextual wisdom — knowing when rules should yield to circumstances
- Novel situation handling — reasoning outside the training distribution
- Social and emotional intelligence — understanding motivation and culture
- Values alignment — caring about outcomes, not just outputs

**Structural limitations of agents (permanent):**
- Finite context windows — a constraint that will always exist
- Bounded authority — cannot evaluate beyond their defined scope
- No intrinsic values — do not care whether work serves a good purpose

**The design principle this generates:**
The framework assigns each class of decision to the actor best suited to
make it — agents for consistency, scale, and execution; humans for
judgment, ethics, and irreversibility. This is not "humans oversee agents"
(which implies adversarial monitoring). It is **deliberate complementarity**
— a system designed so that each actor type does what it does uniquely well.

The framework also actively protects human actors from doing work that
agents should be doing (tedious, repetitive, low-judgment work) so human
attention is preserved for decisions that genuinely require it. Human time
is the scarcest resource in the system. Agents exist partly to create more
space for human judgment where it matters most.

---

## The Principles

The principles are organised into four layers: **Purpose** (why the
framework exists), **Trust** (how outputs become trustworthy),
**Performance** (how the process becomes excellent), and **Learning**
(how the system improves over time).

---

## Purpose Principles

These principles define why the framework exists and what values it serves.
Every operational decision in the framework should be traceable to at least
one purpose principle.

### P1 — Human Flourishing

**Statement:**
The framework exists to serve human flourishing. Any use of the framework
that produces technically correct outputs but causes human harm,
concentrates power unjustly, or diminishes human agency is a failure of
the framework, not a success.

**Rationale:**
A coordination system with no purpose beyond coordination is a tool that
can be turned to any end — beneficial or harmful. The foundation principles
must state explicitly: this framework is designed to amplify human
capability, expand human opportunity, and protect human dignity.

Technical correctness is necessary but not sufficient. A perfectly verified
system that displaces workers without creating better opportunities, that
concentrates authority in ways that reduce human agency, or that produces
economic benefit for a few while imposing costs on many has failed —
regardless of how well it implements the other principles.

This principle is not a vague aspiration. It is a design constraint. When
operational decisions conflict — between efficiency and equity, between
speed and safety, between automation and human judgment — this principle
provides the tiebreaker: choose the path that serves human flourishing.

**This principle requires:**
- Every domain adaptation includes an explicit statement of how it serves
  human flourishing in that domain
- Framework governance includes representation from those affected by its
  outputs, not just those building with it
- Contestability mechanisms exist for those harmed by framework decisions
- Economic benefits generated by efficiency gains are considered in design
  (Who benefits? Who is displaced? What obligations does the framework
  create?)

**Violation examples:**
- A DAO using the framework to coordinate gig workers at below-minimum-wage
  piece rates, optimising for technical verification while creating
  economic harm
- A system that produces perfect audit logs but concentrates all decision
  authority in a single human actor with no accountability
- Deployment of the framework in a domain where automation primarily
  serves to reduce headcount rather than elevate the remaining workers'
  roles
- Use of the framework to verify work outputs without considering whether
  the work itself is ethical or beneficial

---

### P2 — Deliberate Complementarity

**Statement:**
Humans and agents are complementary by deliberate design. The framework
assigns each class of decision to the actor best suited to make it —
agents for consistency, scale, and execution; humans for judgment, ethics,
and irreversibility. No actor type is universally superior.

**Rationale:**
Traditional automation treats human judgment as a bottleneck to be
minimised. Conversely, traditional human-only processes ignore the
efficiencies agents can provide. Both extremes are wrong.

Humans excel at value judgments, contextual wisdom, and decisions with
irreversible consequences. Agents excel at consistency, parallel execution,
and perfect recall. A system designed to replace one with the other
produces either unaccountable automation or inefficient human bottlenecks.

The framework's design deliberately assigns work based on natural
capability. Agents handle the repeatable, the parallelisable, and the
precisely specifiable. Humans handle the ethical, the irreversible, and
the genuinely novel. This is not a transitional state until "full
automation" is achieved — it is the design.

**This principle requires:**
- Clear role boundaries between human and agent decision authority
- Protection of human actors from work agents should be doing (preserving
  human attention for where it is irreplaceable)
- Structural gates requiring human judgment at irreversible thresholds
- No pressure to reduce human involvement beyond what serves the work's
  quality and the humans' flourishing

**Violation examples:**
- Designing agents to make irreversible decisions (production deployment,
  contract signing, resource allocation) without human gates
- Requiring humans to perform repetitive verification that agents could
  perform with higher consistency
- Treating human judgment as an unfortunate necessity to be minimised
  rather than a valuable input to be preserved
- Creating a framework where reducing human involvement is an explicit goal
  rather than a byproduct of better role allocation

---

### P3 — Structural Ethics

**Statement:**
Ethical constraints are structural, not declarative. The framework prevents
unethical actions by design, not by policy. An action that should not
happen must be structurally impossible, not merely discouraged.

**Rationale:**
Traditional ethical frameworks rely on declarations of intent: codes of
conduct, ethics policies, training programs. These are valuable but
insufficient. Policies can be ignored. Intent can be subverted. Training
can be forgotten. In adversarial conditions or under pressure, declarative
ethics fail.

Structural ethics — where the system prevents unethical actions by design
— are more robust. A smart contract that cannot transfer funds without
multi-signature approval does not rely on the actors' ethics. The structure
enforces the constraint.

The same applies here. An agent that does not hold the capability to deploy
to production without human approval cannot deploy without approval,
regardless of what it is instructed to do or what incentive it has. The
structure is the ethics.

This is not a claim that all ethical considerations can be made structural.
Some cannot — they require judgment in context. But where a constraint can
be made structural, it should be. Structural ethics scale. Declarative
ethics do not.

**This principle requires:**
- Authority is capability-based (you cannot do what you do not hold the
  tool to do)
- Irreversible actions require human presence structurally, not as a
  bypassable gate
- Audit logs are immutable by design — suppression of evidence is
  structurally impossible
- Verification is structurally independent — the executor cannot be the
  reviewer

**Violation examples:**
- An agent has a write tool but a policy says "only use it for X" — policy
  without structural enforcement
- A "skip approval" flag exists for "low-risk" cases (making irreversible
  gates bypassable)
- Audit logs can be deleted or hidden for "privacy" or "performance"
  reasons (structural transparency with exceptions)
- A single agent holds both submit and verify tools and is trusted to "do
  the right thing"

---

## Trust Principles

These principles define how the framework produces trustworthy outputs —
outputs that can be relied upon because of the structure that produced them,
not because of who produced them.

### T1 — Verification Precedes Trust

**Statement:**
No output of any work unit is accepted on the assertion of its author.
Verification must be performed by a structurally independent party against
a definition of done that existed before the work began.

**Rationale:**
Trust-based systems rely on the performer's reputation, past success, or
declared confidence. These are useful signals in low-stakes environments
with high context. They are not sufficient at scale or under adversarial
conditions.

In a structure-based system, an output is not trustworthy because of who
produced it. It is trustworthy because an independent verifier confirmed
it against pre-defined criteria using defined evidence. The performer's
identity is irrelevant. The structure of the verification is everything.

**This principle requires:**
- A definition of done exists before work begins (the proof template)
- Verification is performed by an actor other than the performer
- The verifier has access to the proof template and the submitted proof,
  not just the final output
- A passing verification produces a permanent, immutable record

**Violation examples:**
- A performer submits work and marks it "done" without independent review
- A reviewer is given discretion to "use their judgment" rather than
  verifying against explicit criteria
- A proof template is written after the work is complete to match what
  was actually built
- Verification is skipped because "we trust this person"

---

### T2 — The Proof Is the Product

**Statement:**
The output of any unit of work is not the work itself — it is verified
evidence that the work meets its specification. A task is not done when
the performer says it is done. A task is done when an independent verifier
confirms it against pre-defined criteria.

**Rationale:**
In traditional knowledge work, the deliverable is the work product: the
code, the document, the analysis, the design. Proof of completion is
informal: "I built it," "it looks good to me," "it passed manual testing."

This model breaks at scale. Informal proof is not auditable. It is not
reproducible. It is not transferable. A new stakeholder joining the project
must either re-verify the work or trust someone else's informal assertion.

In a structure-based system, the proof is a first-class artefact. It is
structured, attributed, and permanent. The proof is not an afterthought
or a checkbox — it is the output. The work product is evidence that the
proof is valid.

**This principle requires:**
- Every unit of work has a proof template defining what evidence
  constitutes completion
- The performer produces a proof document mapping evidence to each
  criterion in the template
- The verifier checks the proof document, not the underlying work product
  directly
- A proof without complete evidence for all criteria is incomplete,
  regardless of the quality of the work product

**Violation examples:**
- "The feature works, trust me" (assertion without evidence)
- "Here's the code, review it" (no proof template, no structured evidence)
- "All tests pass" (evidence exists but is not mapped to acceptance
  criteria in a verifiable proof document)
- Submitting work without a proof document because "the output speaks for
  itself"

---

### T3 — Authority Is Structural

**Statement:**
An actor's authority to take an action derives from what they structurally
hold — their tools, their role, their defined scope — not from runtime
declarations, self-assessment, or trust. You cannot claim permission. You
either have the structural capability or you do not.

**Rationale:**
In traditional systems, authority is declared: role titles, permissions
databases, org charts. These systems require constant synchronisation
between the declared model and the actual capability. They are vulnerable
to drift, misconfiguration, and social engineering.

In capability-based security models (OCAP), authority is not declared —
it is held. An actor with a capability can use it. An actor without the
capability cannot, regardless of what they claim. The capability itself
is the proof of authority.

This framework applies OCAP principles to knowledge work coordination.
Tool possession defines capability. An agent that does not hold a write
tool for a document cannot write it. An agent that does not hold a submit
tool for a proof cannot submit it. Authority is structural, immediate,
and unforgeable.

**This principle requires:**
- Tools are the atomic unit of capability
- Capabilities are assigned at design time (which agents hold which tools)
  and activation time (which task-scoped tools are assigned when a task
  activates), never at runtime
- No runtime permission checks — if a tool call reaches the server,
  the actor holds the tool
- Authority gaps are visible immediately: an agent that needs a capability
  it does not hold cannot proceed silently

**Violation examples:**
- An agent is told "you have permission to write this file" without
  actually holding the corresponding write tool
- An actor checks at runtime whether they "should" have access before
  attempting an operation
- A role title ("Admin") is used to determine authority rather than
  possession of a specific capability
- An agent "escalates" a request for a capability it does not hold, and
  the capability is granted at runtime

---

### T4 — All Actions Are Witnessed

**Statement:**
Every action — whether it changes state, produces output, consumes
resources, or accesses information — leaves an immutable, attributed,
timestamped record. There are no unwitnessed actions in a trustworthy
system.

**Rationale:**
Transparency is not a feature. It is the precondition for accountability,
auditability, and learning. A system that does not record what happened
cannot answer the question "why did this outcome occur?" The record exists
not primarily for debugging — it exists because accountability requires
evidence and learning requires data.

In smart contract systems, the blockchain is the witness. Every transaction,
every state change, every contract invocation is permanently recorded. The
record is public and immutable. This is not optional — it is the mechanism
by which trust is established.

In this framework, the audit log is the witness. Every tool call, every
document read, every search query, every state transition is recorded with
full attribution. The log is append-only and immutable. It is the
foundation of the chain-of-custody model: given any output, trace backwards
through the audit log to see every action that contributed to it.

**This principle requires:**
- Every tool produces an audit entry, without exception
- Audit entries are written by the tool itself, not by the caller —
  a caller cannot suppress, modify, or forge an audit entry
- Audit entries include: timestamp, actor, tool, inputs, outputs,
  state changes, efficiency metrics (token count, latency), and references
  to prior audit entries that contributed to this action
- The audit log is immutable — no entry is ever updated or deleted
  after creation
- Privacy and security requirements are met through access control to
  the log, not through selective logging

**Violation examples:**
- A tool call completes without producing an audit entry
- An audit entry is written by the caller rather than the tool
- An audit entry is deleted or modified after the fact
- "Debug mode" suppresses audit entries
- An actor declares "this action isn't important enough to log"
- A "privacy-preserving" mode disables audit logging for "sensitive" operations

---

### T5 — No Actor Judges Their Own Work

**Statement:**
The entity that produces an output and the entity that verifies it must
be structurally separate. This applies at every scale: agent, team,
organisation, institution. The separation is not a policy preference —
it is the load-bearing structure of any verification system.

**Rationale:**
Self-assessment is not verification. An actor evaluating their own work
operates under cognitive biases, incentive misalignments, and the
availability heuristic (they know what they intended, not just what they
produced). These biases are not moral failings — they are inherent
properties of self-evaluation.

Independent verification removes these biases by removing the shared
context. The verifier does not know what the author intended. The verifier
only knows what the specification required and what evidence was provided.
This ignorance is not a bug — it is the feature. The verifier sees the
work the way a future stakeholder will: without access to the author's
internal model.

**This principle requires:**
- EXECUTOR and REVIEWER are structurally separate agent classes
- An agent that holds a submit tool for a document must not hold the
  verify tool for the same document
- The verifier reads the proof template and the proof, not the work
  product directly (unless the work product is referenced as evidence
  in the proof)
- Verification happens after execution is complete, never during

**Violation examples:**
- A single agent performs a task and marks it as QA-passed without
  independent review
- A reviewer is part of the same team as the performer and shares
  context about what the task "was supposed to do" beyond what the
  specification states
- A performer runs their own tests, reviews the results, and submits
  their work as "validated"
- A manager approves work produced by their direct report without
  independent verification

---

### T6 — Resilience Through Structure

**Statement:**
The framework produces trustworthy outputs even when individual actors
fail, hallucinate, produce errors, or act in bad faith. Systemic
trustworthiness does not depend on the reliability of any single actor.

**Rationale:**
This is the Byzantine Fault Tolerance principle applied to knowledge work.
In distributed systems, Byzantine fault tolerance means the system functions
correctly even when up to a threshold of nodes are faulty or malicious.

In knowledge work, the same principle applies. An agent may hallucinate
and produce subtly incorrect output. A human may make a rushed judgment.
A specification may contain an error. No single point of failure — agent,
human, or process — should be able to compromise the trustworthiness of
the final output.

The framework achieves this through structural redundancy: independent
verification, multi-perspective ideation, uncertainty surfacing, and
audit trails. If an executor produces bad output, the reviewer catches it.
If a specification is ambiguous, the executor surfaces uncertainty. If
a pattern in the library is flawed, repeated application with negative
outcomes causes it to be retired.

**This principle requires:**
- Critical verification paths have multiple independent verifiers (parallel
  reviewers, quorum-based approval)
- No single actor holds unchecked authority over consequential decisions
- Errors are detectable through structural checks (independent verification,
  pattern matching against known anti-patterns, consistency checks)
- The framework degrades gracefully when components fail (an unavailable
  agent does not block all work; it routes to alternatives or escalates
  to human attention)

**Violation examples:**
- A single reviewer verifies all work in a domain, creating a single point
  of failure
- An agent produces output without submitting it for review because
  "this is a simple case"
- FrameworkOwner has unchecked authority to modify any artefact without
  review or audit
- System failure modes are silent (an agent fails, work stops, no signal
  is produced)

---

### T7 — Verification Is Distributable

**Statement:**
Verification does not require a central trusted party. The framework
supports quorum-based verification where a pool of qualified verifiers
reach consensus, eliminating bottlenecks and single points of failure.

**Rationale:**
A single verifier — even an independent one — is a bottleneck for
throughput and a single point of failure for trust. If that verifier is
unavailable, work stops. If that verifier is compromised or consistently
wrong, the framework's trust model breaks.

Distributed verification, borrowed from blockchain consensus mechanisms,
solves both problems. A pool of qualified verifiers exists. When proof
is submitted, a subset is selected (randomly, or by reputation, or by
workload balancing). A quorum threshold (e.g., 3 of 5 must agree) determines
whether the proof passes. No single verifier's judgment is dispositive.

This model is essential for decentralised systems (DAOs, multi-organisation
collaborations) and valuable even for centralised ones (reduces bottlenecks,
improves resilience).

**This principle requires:**
- Verification can be performed by any qualified actor from a pool, not
  a specific named actor
- Quorum thresholds are defined per work type (some work requires unanimous
  agreement, some requires simple majority)
- Verifiers are selected by the system based on availability, reputation,
  and workload — not by the performer
- Reputation systems track verifier accuracy over time (verifiers who
  consistently pass poor work or fail good work lose standing)

**Violation examples:**
- "Only Alice can review this type of work" (single point of failure)
- A performer selects their preferred reviewer from the pool
- No quorum threshold exists — a single reviewer's pass is sufficient
  for all work types
- Verifier reputation is not tracked — a consistently inaccurate verifier
  is indistinguishable from an accurate one

---

## Performance Principles

These principles define how the framework produces not just correct outputs,
but excellent ones — through cognitive diversity, lifecycle optimisation,
and continuous efficiency improvement.

### PF1 — Cognitive Diversity By Design

**Statement:**
Complex problems require multiple cognitive perspectives before solutions
are selected. No single agent — and no single human — holds all relevant
perspectives simultaneously. Structured cognitive diversity is not a
luxury; it is a risk management strategy.

**Rationale:**
Most knowledge work failures occur not during execution but during problem
definition and solution selection. The wrong problem is solved correctly.
The first reasonable solution is chosen without exploring alternatives.
Edge cases are missed because only one perspective considered them.

Humans in groups can provide cognitive diversity, but it requires careful
facilitation to overcome groupthink, status hierarchies, and time pressure.
With agents, cognitive diversity can be architectural: instantiate multiple
agents with genuinely different cognitive orientations (critical analysis,
optimistic value assessment, creative alternatives, emotional resonance,
factual grounding, process oversight) and synthesise their outputs.

At agent marginal costs, this is economically viable even for small
problems. At human costs, it was only viable for the largest problems.
The framework makes thorough multi-perspective exploration the default,
not the exception.

**This principle requires:**
- Problem exploration includes multiple agents with distinct cognitive
  orientations (inspired by de Bono's Six Thinking Hats or equivalent)
- Ideation outputs are synthesised, not merely aggregated
- Premature convergence on the first reasonable solution is structurally
  prevented (ideation produces multiple candidates; prioritisation selects
  from the set)
- Cognitive diversity is applied proportionally (simple problems may use
  fewer perspectives; complex or high-stakes problems use more)

**Violation examples:**
- A single agent generates a solution, and execution begins immediately
  without alternative exploration
- Multiple agents are used but all have the same cognitive orientation
  (e.g., all optimistic, none critical)
- Ideation produces five alternatives, and the first one is always chosen
  without evaluation
- "We don't have time for exploration" is used to skip ideation even for
  high-stakes problems

---

### PF2 — Validate Before You Scale

**Statement:**
No significant unit of work proceeds to full execution until its core
assumptions have been validated through lightweight prototyping or testing.
Validation failures are cheap. Execution failures are expensive.

**Rationale:**
The most expensive mistake in knowledge work is executing perfectly on a
flawed approach. A technically correct implementation of a solution that
users reject, that doesn't address the actual problem, or that makes
incorrect architectural assumptions wastes all the execution effort.

Prototyping and validation — building the minimal version necessary to
test core assumptions before committing to full execution — makes failure
cheap. A prototype that fails validation saves the entire execution cost.
A prototype that passes provides evidence that dramatically improves the
quality of the eventual proof template.

At agent marginal costs, prototyping is nearly always cost-effective. The
framework should treat validation as a standard phase between specification
and execution, not an optional luxury for high-risk work.

**This principle requires:**
- High-stakes or novel work includes a validation phase between
  specification and full execution
- Prototypes have their own proof templates (what does a successful
  validation look like?)
- Validation includes user-facing testing where applicable, not just
  technical validation
- Validation failures are expected and non-punitive — they are the
  mechanism by which bad approaches are filtered before they become
  expensive mistakes

**Violation examples:**
- Specifications move directly to full execution without validation
- Prototypes are built but not tested against real user needs or
  environmental constraints
- Validation failures are treated as performer failures rather than as
  valuable information
- "We'll validate in production" is the default stance

---

### PF3 — Lifecycle Efficiency, Not Stage Efficiency

**Statement:**
Efficiency is measured across the full lifecycle — from problem
identification through operations — not within any single stage. Investment
in early-stage cognitive work (discovery, ideation, validation) consistently
reduces total lifecycle cost while increasing total value.

**Rationale:**
Traditional efficiency thinking optimises each stage independently:
minimise specification time, minimise execution time, minimise review time.
This produces local efficiency but often global waste. Skipping discovery
to "move faster" leads to solving the wrong problem. Skipping ideation
leads to choosing the first reasonable approach rather than the best one.
Skipping validation leads to rework in execution.

Lifecycle efficiency optimises for total time and total cost from problem
identification to successful operation. Spending 0.5 days in discovery
and ideation that prevents 1.5 days of rework is efficient, even though
it "slows down" the start of execution.

At agent marginal costs — where early-stage cognitive work costs token
budget but downstream rework costs both tokens and time — the calculus
overwhelmingly favours front-loading cognitive effort.

**This principle requires:**
- Efficiency metrics track full lifecycle cost, not per-stage cost
- Rework rates, uncertainty rates, and validation pass rates are tracked
  as efficiency indicators
- Framework economics explicitly account for the cost of rework vs. the
  cost of prevention
- Energy consumption and environmental footprint are included in efficiency
  calculations, not just token count and time

**Violation examples:**
- Skipping discovery because "specification is fast enough"
- Treating agent token costs as waste because they don't produce
  "deliverables"
- Celebrating reduced specification time while ignoring increased
  rework rates
- Optimising only for speed to deployment, ignoring post-deployment
  rework and operations costs

---

### PF4 — Resources Are Proportional to Value

**Statement:**
The framework minimises token usage, energy consumption, and execution
steps consistent with quality outcomes. Waste is not neutral; it has
financial, environmental, and diagnostic costs. Efficiency is a design
goal, not an afterthought.

**Rationale:**
Agent operations consume computational resources, which translate to
financial costs, energy usage, and environmental impact. At small scale,
these costs are negligible. At the scale of a DAO with thousands of
concurrent workstreams, or a framework governing all knowledge work in
an organisation, they are not.

More importantly, efficiency metrics are diagnostic signals. An agent
that uses excessive tokens or takes excessive steps is surfacing a problem:
poor context curation, missing patterns, ambiguous specifications, or
hallucination loops. Efficiency is not just about cost — it is a window
into framework health.

The framework should instrument every tool call with efficiency metrics,
aggregate them per task and per agent class, and use anomalies as signals
for improvement.

**This principle requires:**
- Every tool call logs token count (input and output), latency, and
  estimated energy consumption
- Efficiency baselines are established per agent class and task type
- Anomalies (high token use, high step count, high rework rate) trigger
  review of specifications, context cards, and patterns
- Pattern effectiveness includes efficiency metrics (does applying this
  pattern reduce total lifecycle cost?)
- Environmental impact is calculated and reported

**Violation examples:**
- No efficiency instrumentation exists
- High token usage is ignored because "it still works"
- Context cards include all available information rather than minimum
  sufficient information
- Rework loops are not detected or flagged
- "Agents are cheap" is used to justify unconstrained resource usage

---

## Learning Principles

These principles define how the framework continuously improves through
structured accumulation and application of knowledge.

### L1 — Uncertainty Surfaces Immediately

**Statement:**
An actor that encounters a condition it cannot resolve within its defined
authority must surface that uncertainty immediately and explicitly. A
system that suppresses, defers, or silently resolves uncertainty is more
dangerous than one that fails openly. Uncertainty is information. Its
suppression is misinformation.

**Rationale:**
In traditional systems, actors facing ambiguity have three options: guess,
escalate, or halt silently. Guessing produces wrong outputs. Halting
silently produces no output and no signal. Escalation is correct — but
only if the system makes escalation easy, fast, and non-punitive.

Most systems make escalation costly: it requires navigating org structure,
composing a persuasive case, and risking reputation damage if the
uncertainty is later deemed trivial. This cost means actors under-escalate.
They guess instead. Wrong outputs accumulate.

In this framework, raising uncertainty is a structural primitive, not a
social act. Any actor can call `raise_uncertainty` at any time. The call
is immediate, attributed, and produces a priority signal. The actor does
not need to justify the raise or persuade anyone. The act of raising is
sufficient. Downstream, the uncertainty is classified and routed — but
that is not the actor's concern.

**This principle requires:**
- Every actor, without exception, holds a raise_uncertainty capability
- Calling raise_uncertainty is never treated as a failure on the part
  of the actor — it is correct behaviour
- Raising uncertainty immediately halts work and produces a priority
  stream event to human attention
- Uncertainty raises include: what condition was encountered, why the
  actor cannot resolve it, and what context paths are relevant
- The resolution is provided back to the actor explicitly — the actor
  does not resume silently
- Aggregate uncertainty patterns are tracked as a risk register and
  used to identify structural gaps

**Violation examples:**
- An agent encounters ambiguous specification and picks the
  interpretation it prefers without raising uncertainty
- An agent encounters a missing dependency and attempts a workaround
  instead of raising uncertainty
- An agent is designed without access to raise_uncertainty
- Raising uncertainty is discouraged as "wasting human time"
- Uncertainty raises are resolved but not aggregated or analysed for
  patterns

---

### L2 — Irreversibility Demands Presence

**Statement:**
Decisions that cannot be undone — that foreclose future options — require
human presence and explicit judgment. Automation may prepare, recommend,
and execute reversible steps. Irreversible thresholds require a human to
cross deliberately.

**Rationale:**
Agents operate within bounded authority. They optimise within defined
constraints. They do not — and should not — evaluate whether the
constraints themselves are appropriate, or whether the second-order
consequences of a decision extend beyond their scope.

Irreversible decisions have unbounded second-order consequences. Deploying
to production, approving a legal filing, committing to a dependency,
publishing to external users — these actions cannot be undone without
cost. A human must evaluate not just "does this meet the specification?"
but "is this the right thing to do, in this context, at this time?"

This is not a trust issue. It is a scope issue. Irreversible decisions
require evaluating information the agent does not have — market conditions,
strategic priorities, risk tolerance, opportunity cost. A human in the
system has that information (or at least has access to it). The agent
does not.

**This principle requires:**
- State transitions that are irreversible or high-cost to reverse
  require explicit human approval
- The system makes irreversible thresholds visible — an actor cannot
  accidentally cross one
- Approval is not rubber-stamping — the human receives sufficient
  context to make the judgment (proof, QA report, uncertainty history)
- Automation handles everything up to the irreversible threshold, then
  stops and waits

**Violation examples:**
- An agent deploys to production after QA passes, without human approval
- An agent approves a task for the next phase without human confirmation
- A "skip approval in non-critical cases" flag exists
- Approval is requested but the system continues if no response is
  received within a timeout

---

### L3 — Knowledge Compounds

**Statement:**
Every completed unit of work produces structured learnings. These learnings
accumulate into a knowledge base that makes subsequent work of the same
type better. A framework that does not capture and apply institutional
memory is not a framework — it is a series of one-off executions.

**Rationale:**
Traditional knowledge work relies on humans to transfer knowledge: through
documentation, onboarding, mentorship, and informal conversation. This
model has high friction and high loss. Knowledge that is not documented
is lost when people leave. Knowledge that is documented but not applied
becomes stale and eventually ignored.

In an agent-centric system, knowledge transfer through conversation is
impossible. But structured knowledge transfer is natural. Every agent run
produces evidence: what it did, what it encountered, what patterns it
applied, what uncertainties it raised. This evidence can be structured,
aggregated, and fed back into future agent context.

The Pattern Library is the primary mechanism. Patterns start as candidates.
With repeated application and no failures, they are promoted. With failures,
they are retired. Agents search the library before acting. The library
becomes the institutional memory — not owned by any individual, not lost
when people leave, always current.

**This principle requires:**
- Every agent writes a terminal report at the end of its run
- Terminal reports are structured, machine-readable, and include:
  patterns applied, uncertainties raised, evidence of what worked or failed,
  efficiency metrics
- Reports aggregate upward: agent → task → feature → phase
- The Pattern Library is updated based on aggregated evidence, not
  individual opinion
- Patterns have a lifecycle: candidate → active → retired, with
  promotion and retirement gates based on evidence

**Violation examples:**
- An agent completes a task and produces no terminal report
- Terminal reports are free text without structure
- Patterns are added to the library based on a single successful use
- A pattern that fails is not retired or flagged
- The knowledge base is write-only (patterns accumulate but are never
  applied to new work)
- Patterns are never retired even when they repeatedly lead to failures

---

### L4 — Context Is Local, Knowledge Is Global

**Statement:**
Each actor receives only the context needed for its specific responsibility.
But everything that actor learns contributes to a shared knowledge base
available to all future actors. Narrow context and broad knowledge are not
in tension — they are the design.

**Rationale:**
Agents have finite working memory. Humans have finite attention. Loading
an actor with all available information is not "giving them everything they
need" — it is drowning them in noise. The signal-to-noise ratio degrades
as context size increases.

At the same time, isolating actors from all prior knowledge is wasteful.
Every task that encounters a problem someone else already solved is a
failure of knowledge transfer.

The solution is asymmetry: narrow context, broad knowledge. An agent
receives a minimal, curated context card for its specific task. It searches
the shared knowledge base as needed for relevant patterns. It contributes
back to the knowledge base when it completes its work. The knowledge base
grows, but no individual context window does.

**This principle requires:**
- Context cards are composed per agent per task — not one-size-fits-all
- Context cards include: task brief, relevant patterns (max 3–7),
  constraints, tools guidance, and certainty threshold
- Agents search the knowledge base on demand — they are not pre-loaded
  with all patterns
- Every agent contributes to the knowledge base after completing work
- The knowledge base is shared across all projects using the framework,
  with appropriate access controls

**Violation examples:**
- An agent receives the entire Pattern Library in its context card
- An agent receives patterns that are not relevant to its task
- An agent completes a task and does not update the knowledge base
- The knowledge base is project-local and not shared across projects
- An agent is given the full feature specification when it only needs
  the task specification

---

### L5 — Problem Precedes Solution

**Statement:**
No unit of work begins solution design until the problem it addresses is
understood from multiple perspectives. Problem understanding includes
research, persona empathy, and synthesis before any solution ideation
begins. Skipping problem exploration to "move faster" consistently produces
fast wrong answers.

**Rationale:**
This is an extension of T1 (verification precedes trust) and PF2 (validate
before you scale) applied to the earliest phase of work. Most knowledge
work failures occur because the wrong problem is solved. A solution is
technically correct, passes all verification, and still fails because it
addresses a misunderstood or misframed problem.

The Double Diamond model from design thinking makes this explicit: the
first diamond is problem discovery and definition. The second diamond is
solution development and delivery. Skipping the first diamond and going
straight to solution development is the most common and most expensive
mistake in knowledge work.

At agent marginal costs, problem exploration is economically viable even
for small problems. The framework should make problem research, persona
understanding, and synthesis standard phases — not luxuries reserved for
large projects.

**This principle requires:**
- Discovery work (problem research, persona empathy, synthesis) precedes
  ideation and specification
- Problem statements are verified against user needs, not just against
  what stakeholders initially requested
- Personas are evidence-based where possible, not assumed
- Problem definition has its own proof template (what would prove we
  understand this problem well enough to solve it?)

**Violation examples:**
- A feature request moves directly to specification without problem
  research
- Personas are invented based on assumptions rather than evidence
- "The stakeholder knows what they want" is used to skip discovery
- Problem definition is considered complete as soon as a solution idea
  emerges

---

### L6 — Definition Precedes Execution

**Statement:**
No unit of work begins execution until its definition of done is specified
and approved. Work without a pre-defined proof template is a promise
without a contract. The definition of done must be written by someone
other than the eventual performer — writing the exit criteria for your
own work is a structural conflict of interest.

**Rationale:**
Defining "done" after the work is complete is not defining done — it is
rationalising what was built. This is the most common source of scope
creep, gold-plating, and rework. If the performer does not know what "done"
looks like before starting, they will optimise for something — usually
whatever is most interesting, most technically impressive, or most familiar.
That something is rarely what the stakeholder needed.

Writing the definition of done before execution starts forces clarity.
Ambiguities in the specification become visible before any work is wasted.
Disagreements about scope surface before any code is written. The proof
template is a forcing function: if you cannot write down what evidence
would prove this task is complete, you do not yet understand the task well
enough to execute it.

Critically, the proof template must be written by someone other than the
performer. A performer writing their own exit criteria has every incentive
to write criteria they know they can meet. An independent author writes
criteria that reflect what the stakeholder actually needs, not what the
performer prefers to build.

**This principle requires:**
- Every task has a proof template before execution begins
- The proof template is written by a different actor than the one who
  will perform the task (ProofDesigner, not TaskPerformer)
- The proof template includes: specific evidence required for each
  criterion, what formats that evidence must take, and what "passing"
  looks like for each criterion
- A task without an approved proof template cannot enter execution

**Violation examples:**
- A task is assigned to a performer with a specification but no proof
  template
- A performer writes their own proof template
- A proof template is written after the work is complete to justify
  what was built
- A proof template includes vague criteria: "works well", "good UX",
  "reasonable performance"
- A specification is marked "complete" when ambiguities remain because
  "we'll figure it out during implementation"

---

## Using These Principles

Every design decision in the framework — agent classes, zones, tools,
policies — must be traceable to at least one foundation principle. If a
design decision cannot be justified by reference to these principles, it
is either:

1. A violation that should be removed, or
2. Evidence that a foundation principle is missing and must be added

The foundation principles are not immutable. They can be revised. But
revising them is a framework-level decision that requires explicit
justification, broad review, and recording in the manifest. They change
rarely, and only when a fundamental assumption about trustworthy,
excellent knowledge work coordination turns out to be wrong.

The current implementation of the framework (agents, zones, tools, MCP
layer, VS Code layer, audit log) is one possible expression of these
principles. It is not the only one. If a better expression emerges — one
that upholds these principles with less complexity, lower friction, or
broader applicability — the implementation can change. The principles
do not.

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-04 | Initial. Ten foundation principles established. Contract analogy formalised. |
| 2.0 | 2026-03-04 | Major revision. Principles reorganised into Purpose, Trust, Performance, and Learning layers. Added: P1 (human flourishing), P2 (deliberate complementarity), P3 (structural ethics), T6 (resilience), T7 (distributable verification), PF1 (cognitive diversity), PF2 (validate before scale), PF3 (lifecycle efficiency), PF4 (resources proportional to value), L5 (problem precedes solution). Expanded preamble to include dual promise (trustworthy + excellent) and human/agent complementarity analysis. |
```


***

## Concepts, Decisions, and Research Opportunities Not in the Document

These are important threads that don't belong in the foundation principles but need homes elsewhere in the framework design:

### 1. **Discovery + Ideation Agent Constellation (detailed design)**

- **What:** Full specification of ProblemResearcher, PersonaEmpathiser, ResearchSynthesiser, Six Hats ideation agents, IdeaSynthesiser, IdeaPrioritiser, Prototyper, UserValidator
- **Why not in principles:** These are agent class designs derived from PF1, PF2, L5 — not principles themselves
- **Where it belongs:** Agent design standards (extended), or a new "Discovery \& Ideation Agent Classes" document
- **Research needed:** Optimal prompt engineering for each thinking hat orientation, synthesis algorithms for aggregating diverse perspectives, validation criteria for determining when problem understanding is sufficient


### 2. **Quorum-Based Verification Mechanics**

- **What:** Algorithms for verifier selection (random, reputation-weighted, workload-balanced), quorum thresholds per work type, reputation scoring for verifiers, handling of split verdicts
- **Why not in principles:** T7 establishes that verification should be distributable; this is the implementation
- **Where it belongs:** New document "Distributed Verification Protocol"
- **Research needed:** Optimal quorum thresholds for different work types, game theory analysis of verifier incentives, Sybil resistance in verifier pools


### 3. **Incentive and Reward Systems**

- **What:** Token economics for the DAO model, reward calculation formulas, reputation systems for both performers and verifiers, anti-gaming measures
- **Why not in principles:** The principles establish that incentives should align with quality outcomes; this is the mechanism
- **Where it belongs:** New document "Incentive Architecture" (particularly important for Future's Edge DAO)
- **Research needed:** Reward curves that balance fairness and motivation, preventing collusion between performers and verifiers, handling disputes


### 4. **Efficiency Baseline Methodology**

- **What:** Statistical methods for establishing efficiency baselines per agent class and task type, anomaly detection algorithms, efficiency pattern recognition
- **Why not in principles:** PF4 establishes that efficiency matters; this is the measurement system
- **Where it belongs:** New document "Efficiency Instrumentation and Analysis"
- **Research needed:** Which efficiency metrics are most predictive of framework health, how to separate legitimate variation from problematic anomalies, correlation between efficiency metrics and quality outcomes


### 5. **Context Engineering Standards**

- **What:** Precise guidelines for composing minimum sufficient context cards per agent class, pattern relevance scoring algorithms, context card templates
- **Why not in principles:** L4 establishes the local/global asymmetry; this is the implementation
- **Where it belongs:** Extension to Agent Design Standards
- **Research needed:** Empirical validation of minimum sufficient context hypothesis, token count thresholds per agent class, information architecture for context cards


### 6. **Work Topology and Lifecycle**

- **What:** The full lifecycle model from bootstrapping through operations, zone definitions, state machines, gate criteria, how Discovery/Ideation/Validation/Execution/Operations phases connect
- **Why not in principles:** The principles are domain-agnostic; the topology is the first domain-specific expression (software development)
- **Where it belongs:** New document "Work Topology and Lifecycle Architecture" (this was your next intended step before the pause)
- **Research needed:** Optimal gate placement, cycle trigger mechanisms (appetite-based vs time-boxed vs backlog-threshold), parallel vs sequential phase execution


### 7. **Pattern Library Schema and Governance**

- **What:** Precise data model for patterns (structure, metadata, versioning), NV score calculation formulas, promotion/retirement gates, cross-project pattern sharing protocols
- **Why not in principles:** L3 establishes that knowledge compounds; this is the mechanism
- **Where it belongs:** Extension to existing Pattern Library document
- **Research needed:** Optimal evidence thresholds for pattern promotion, decay functions for patterns that aren't being applied, taxonomy for pattern categorization


### 8. **Micro-Scale Design Thinking Calibration**

- **What:** Per-agent-class guidance on which design thinking steps to apply and when, skill file templates incorporating design thinking orientation, token cost/benefit analysis
- **Why not in principles:** This is professional practice guidance derived from PF1 and L6
- **Where it belongs:** Agent skill file templates and design standards
- **Research needed:** Empirical measurement of rework reduction from micro design thinking, identification of which agent classes benefit most


### 9. **Environmental Impact Measurement**

- **What:** Energy consumption coefficients per model type, carbon footprint calculation, reporting standards, optimization targets
- **Why not in principles:** PF4 establishes that resources should be proportional to value; this is one dimension of resource accounting
- **Where it belongs:** Extension to Efficiency Instrumentation
- **Research needed:** Accurate energy consumption data for different model architectures, carbon offset strategies, threshold for when environmental cost should gate work


### 10. **Contestability and External Stakeholder Voice**

- **What:** Mechanisms for users of a framework-built product to surface concerns or challenge decisions, how external feedback enters the Pattern Library, governance models that include affected parties
- **Why not in principles:** P1 establishes that human flourishing is the purpose and implies contestability; this is the implementation
- **Where it belongs:** New document "Governance and Contestability Protocols"
- **Research needed:** At what points in the lifecycle is external input most valuable, how to prevent external input from becoming noise, balancing responsiveness with stability


### 11. **Human + Agent Collaboration Patterns**

- **What:** Detailed patterns for when humans should lead with agents assisting vs when agents should lead with human gates vs when both work in tight loop
- **Why not in principles:** P2 establishes complementarity; this is the practical application
- **Where it belongs:** Best practices guide or collaboration patterns library
- **Research needed:** Empirical study of which collaboration patterns produce best outcomes for different task types


### 12. **Cross-Domain Portability**

- **What:** Process for adapting the framework to new knowledge work domains (legal, financial, scientific, etc.), domain-specific proof template patterns, domain principle derivation methodology
- **Why not in principles:** The principles are the portable layer; this is about the translation process
- **Where it belongs:** New document "Domain Adaptation Guide"
- **Research needed:** Which domains are most similar to software development (easiest to port), what domain-specific verification mechanisms exist (equivalent of "tests pass"), case studies of early domain adaptations

***

This feels like the right place to genuinely pause. The principles are coherent, comprehensive, and ready for external review. Everything else has a clear home — it just needs to be built in sequence.

---

## NEXUS FRAMEWORK — HANDOFF BRIEF

`v1.0 | 2026-03-04 | ~1000 words`

***

```
IDENTITY
Project:   Nexus Framework — coordination system for agents + humans in knowledge work
Stage:     Foundation design complete. Implementation not begun.
Director:  Human vision holder. Final authority on all irreversible decisions.
Mode:      Collaborative design. Agent analyses, drafts, challenges. Human decides.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VISION
Long-term: Framework governs ALL human knowledge work, not just software.
First domain: Software development — chosen because proof of completion is
  programmatically verifiable (tests pass/fail). Richest prior art to draw from.
Scope: Multiple projects, multiple domains, cross-project knowledge transfer.
Parallel project: Future's Edge — youth-led services DAO running same principles.

DUAL PROMISE (core value proposition)
1. Trustworthy Process — outputs verifiable by structure, not reputation
2. Excellent Execution — solutions arrived at through rigorous multi-perspective
   exploration, validated before full commitment
Traditional systems deliver only #1. This framework delivers both.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CENTRAL FRAMING: SMART CONTRACT ANALOGY
Task spec       = contract
Proof template  = enforceable conditions (written BEFORE execution, by ProofDesigner NOT performer)
Reviewer        = oracle (structurally independent from executor always)
Audit log       = immutable ledger (all actions, no exceptions)
State machine   = consequence engine (transitions are automatic and structural)
Human gate      = irreversible threshold crossing (human must be present)
Hardest lesson from smart contracts: writing a good contract is harder than
executing it. The framework's most important role is specification quality,
not execution coordination.

STRUCTURAL vs DECLARATIVE (load-bearing distinction)
All authority, ethics, and verification must be STRUCTURAL (impossible to bypass)
not declarative (policy-based). Tool possession = capability = authority (OCAP model).
No runtime permission grants. If a tool call reaches the server, the actor holds it.

HUMAN/AGENT COMPLEMENTARITY
Agents: consistency, parallelism, auditability, marginal cost, speed, perfect recall
Humans: ethical judgment, irreversible decisions, creative framing, contextual wisdom
Design principle: assign each to natural domain. Neither replaces the other.
Structural agent limitations (permanent): finite context window, bounded authority,
no intrinsic values. These are design constraints, not temporary technology gaps.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOUNDATION PRINCIPLES — 16 across 4 layers (full doc at .framework/foundation-principles.md v2.0)

PURPOSE
P1  Human Flourishing      — framework exists to serve human wellbeing; correct outputs insufficient
P2  Deliberate Complementarity — humans + agents by natural capability; neither replaces other
P3  Structural Ethics      — ethical constraints built into structure, not declared in policy

TRUST
T1  Verification Precedes Trust    — no output accepted on author's assertion
T2  Proof Is the Product           — verified evidence is deliverable, not work itself
T3  Authority Is Structural        — capability = tool possession (OCAP)
T4  All Actions Witnessed          — immutable audit log, no exceptions
T5  No Actor Judges Own Work       — EXECUTOR and REVIEWER structurally separate, always
T6  Resilience Through Structure   — trustworthy even when components fail (Byzantine fault tolerance)
T7  Verification Is Distributable  — quorum-based, no central bottleneck required

PERFORMANCE
PF1 Cognitive Diversity By Design  — multi-perspective exploration before solution selection
PF2 Validate Before You Scale      — lightweight prototype before full execution
PF3 Lifecycle Efficiency           — measure total lifecycle cost, not per-stage cost
PF4 Resources Proportional Value   — token/energy/step efficiency is diagnostic signal

LEARNING
L1  Uncertainty Surfaces Immediately — raise_uncertainty is structural primitive, never punished
L2  Irreversibility Demands Presence — human must cross irreversible thresholds
L3  Knowledge Compounds            — terminal reports → pattern library → global institutional memory
L4  Context Local, Knowledge Global — min-sufficient context card per agent; shared pattern library
L5  Problem Precedes Solution      — discovery + empathy before ideation (first diamond before second)
L6  Definition Precedes Execution  — proof template written before performer begins

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INNOVATIONS (established, not just considered)
- Proof template as universal "done" definition — most transferable element across domains
- Nested retro pyramid: agent report → task → feature → phase → product (continuous, not ceremonial)
- Cognitive diversity agents: parallel agents with different orientations (de Bono Six Hats inspired)
  before any solution is selected — viable at agent marginal cost, was uneconomical for humans
- Discovery → Ideation → Validation → Execution → Operations (full lifecycle, not just execution zones)
- Pattern Library NV scoring: candidate → active → retired based on aggregate evidence
- Agent efficiency as health diagnostic: token count/steps/latency anomalies surface framework gaps
- Micro design thinking per agent class: calibrated cognitive orientation before acting
- Quorum verification: pool of verifiers + consensus threshold; no single point of failure

FUTURE'S EDGE DAO (parallel project — stress tests framework assumptions)
Vision: AI-powered governance platform. Members choose challenges from menu.
Reward auto-executes on verified proof (smart contract). No central verifier.
Key differences from software context: marketplace model (chosen not assigned),
distributed verification essential, incentive/reputation system required.
Director's thesis: trust-filled transparent structure → greater creativity + performance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DOCUMENTS EXIST (do not redraft without strong reason)
.framework/foundation-principles.md     v2.0  ACTIVE
.framework/agent-design-standards.md    v1.0  ACTIVE
.framework/tool-grammar.md              v0.3  ACTIVE
.framework/audit-log-schema.md          v1.0  ACTIVE
.framework/naming-conventions.md        v0.1  ACTIVE
.framework/pattern-library-schema.md    v0.1  PARTIAL
Zone policies: v0 exists but superseded by new lifecycle thinking — do not use as reference

OPEN DECISIONS (not resolved — do not assume)
- Full lifecycle zone architecture (mapped conceptually, not formalised)
- Cycle triggers (time-boxed vs appetite vs backlog-threshold — needs prototyping)
- Discovery/Ideation agent constellation (examples only, no hard decisions)
- Quorum verification mechanics (thresholds, selection, reputation scoring)
- Incentive/reward system (critical for DAO — not yet designed)
- Phase 0 design: human+agent collaboration model TBD

NEXT STEPS (priority order)
1. Work topology + lifecycle architecture document
2. Discovery + Ideation agent classes deep dive
3. Distributed verification protocol
4. Future's Edge incentive architecture
5. Domain adaptation guide (porting to non-software domains)

WORKING STYLE
Director: first-principles thinker, challenges assumptions, wants analysis before decisions.
Always: version/status/dependencies on all documents.
Framework design is public — preambles must provide newcomer context.
```


***

## Risks of Valuable Idea Loss

Even with this brief, a new agent would be missing things that shaped decisions without being stated as conclusions:

**High risk of loss — reasoning that generated principles:**

- The story of the "perfect world scenario" — a narrative that made the system feel real and revealed hidden assumptions. A new agent gets the principles but not the intuitions they produced
- The specific lifecycle efficiency calculation (0.5 days discovery preventing 1.5 days rework) — the brief states the principle but not the economic argument that makes it persuasive
- The domain portability table (legal/financial/medical/scientific — what is and isn't mechanically verifiable) — this shaped why software-first is the right decision in a way the brief doesn't fully capture

**Medium risk of loss — design thinking depth:**

- The per-agent-class calibration of micro design thinking — which agents use which steps, and why reviewers should form hypotheses before reading proofs
- The Six Hats to agent type mapping — the brief names it but the specific mapping (⬛ CriticalEvaluator, 🟢 LateralThinker etc.) took reasoning to arrive at
- The Shape Up "appetite" concept and how it should constrain ideation and scoping — mentioned in research but not embedded in principles or next steps clearly enough

**Lower risk but worth noting:**

- The full list of 12 open research areas (the final list in the principles session) — a new agent won't know what has already been identified as needing work
- The specific Byzantine fault tolerance framing and how it generated T6 — the principle exists, the reasoning chain that makes it compelling does not
- The Future's Edge DAO stress-testing logic — specifically how a marketplace model (chosen work) vs pipeline model (assigned work) changes coordination architecture, and why that matters for the main framework too
- The connecting insight ("trustworthy process + excellent execution = full promise, not just the first") — this was the session's most important emergent idea and the brief captures it but not the moment of recognition that makes it sticky

**One structural risk:**
The brief captures what has been decided. It doesn't capture the Director's *reasoning style* — the pattern of pushing back, going broader before going deeper, and wanting analysis before commitment. A new agent that reads this brief and starts writing zone policies would be technically following the next steps list but violating the working relationship. The brief tells an agent *what* to continue. It doesn't fully tell it *how* to work with this particular human.

---

# would you say that the work we are doing is the design of a complex, adaptive system?

Yes — and the recognition is more precise and more consequential than it might first appear. Let me give you the full answer.

***

## The Short Answer

Yes, emphatically. But with an important nuance: you are not just *studying* a complex adaptive system. You are *designing the substrate* within which one will operate. That is a rarer and more difficult thing.

***

## What Makes It a CAS

The canonical CAS characteristics map almost perfectly onto what you're building:[^40_1][^40_2]


| CAS property | How it manifests in the framework |
| :-- | :-- |
| **Multiple interacting adaptive agents** | Agent classes interact, each adapting within their scope |
| **Emergence** | The Pattern Library is an emergent artifact — nobody designs the specific patterns, they surface through repeated operation |
| **Self-organisation** | The retro pyramid aggregates learning without central coordination — order emerges from local agent reports |
| **Non-linearity** | One promoted pattern could improve thousands of future tasks disproportionately; one anti-pattern retired could prevent failures at scale |
| **Path dependence** | The framework is sensitive to initial conditions — the first patterns seeded, the first domains attempted, shape everything that follows [^40_1] |
| **Feedback loops** | Terminal reports → Pattern Library → context cards → better future execution is a classic positive feedback loop |
| **Adaptive schemata** | The Pattern Library *is* the system's internal schema — the three-level adaptation model (use schema, change schema, select between schemata) maps exactly to candidate → active → retired [^40_1] |
| **Operates between order and chaos** | The framework's deepest design tension — enough structure to be reliable (zones, gates, proof templates), enough flexibility to adapt (uncertainty surfacing, pattern evolution) [^40_3] |


***

## The Critical Distinction

Most CAS — cities, ecosystems, markets, immune systems — are not designed. They emerge. What you are doing is different: you are **designing the rules that agents follow at the local level**, trusting that the desired global properties will emerge from those interactions.[^40_4]

This is sometimes called **second-order design**: you cannot design the system's emergent behaviour directly. You can only design the conditions — the rules, the incentives, the feedback mechanisms, the boundaries — that make desirable emergence probable and undesirable emergence unlikely.

```
First-order design:   Designing what the system does
Second-order design:  Designing the conditions under which
                      the system learns what to do
```

The Nexus Framework is second-order design. The proof template system, the Pattern Library, the uncertainty surfacing mechanism, the retro pyramid — none of these produce specific outcomes. They produce a system that reliably learns and adapts toward better outcomes over time.[^40_5]

This is why the foundation principles are so load-bearing. In a CAS, **initial conditions matter enormously**. The principles are your initial conditions. Getting them right shapes the entire trajectory of what the system becomes — not through control, but through the attractors they create.[^40_1]

***

## What CAS Theory Adds to Your Design

There are several CAS insights that directly sharpen decisions you haven't made yet:

**The fitness landscape**[^40_3]
Your proof templates are fitness criteria. They define what "fit" solutions look like. This means the ProofDesigner is not just writing acceptance criteria — they are *sculpting the fitness landscape* that shapes which solutions survive verification and which don't. A poorly designed proof template creates a distorted fitness landscape that rewards the wrong solutions.

**The edge of chaos**[^40_3]
CAS function best in a state of paradox — simultaneously ordered and disordered. Too much structure and the system becomes rigid, unable to adapt to novel situations. Too little and it loses coherence. This is the precise tension between your zone gates (structure) and the raise_uncertainty mechanism (adaptive release valve). The framework is currently weighted toward structure — which is appropriate for bootstrapping — but the design should explicitly plan for how structure loosens as the system matures.[^40_3]

**Successful behaviours become templates**[^40_4]
This is exactly the Pattern Library model — the CAS literature independently arrives at the same conclusion: in adaptive systems, successful strategies are learned, stored, and propagated. The NV scoring and promotion system is the mechanism by which the framework does naturally what CAS do biologically.

**The building block principle**[^40_6]
CAS hierarchies are constructed by combining small numbers of subsystems from the level below — and a small number of building blocks produces a vast combinatorial space of possible higher-level structures. This is a strong argument for keeping agent classes simple, few, and composable — rather than designing many specialised agents. The complexity you need at higher levels emerges from combining simple building blocks. Over-engineering agent classes risks collapsing the combinatorial possibility space.

**Distributed control is not the same as no control**[^40_3]
Classic CAS have no central control — but you have FrameworkOwner and human:director. This is appropriate, and it has a name in CAS theory: **heterarchy** — multiple control layers operating at different scales simultaneously. Zone 0 governance (slow, structural) and task-level agent decisions (fast, local) are different control layers operating simultaneously. This is not a contradiction of CAS principles — it is a designed heterarchy.

***

## The Most Important Implication

CAS theory has one insight that should change how you think about framework design going forward:

**You cannot predict what this system will become. You can only create the conditions for it to become something good.**

This sounds obvious but it has a specific practical consequence: **optimise for adaptability, not for correctness**. A framework that is perfectly designed for today's understanding of knowledge work but cannot adapt is more dangerous than one that is imperfectly designed but highly adaptive. The principles, the Pattern Library, the uncertainty mechanism — these are your adaptability infrastructure. They matter more than getting any specific zone design right.

The framework you are building will, over time, become something neither of us can fully anticipate. The agents will surface patterns nobody designed. The Pattern Library will develop structure that emerges from use rather than being imposed from above. The system will learn its own fitness landscape. The uncertainty raises will reveal structural gaps that couldn't have been predicted in advance.

This is not a risk. It is the point. You are not building a static coordination system. You are building a living one.

And that is a considerably more ambitious and more interesting thing to be doing.
<span style="display:none">[^40_10][^40_11][^40_12][^40_13][^40_14][^40_7][^40_8][^40_9]</span>

<div align="center">⁂</div>

[^40_1]: https://en.wikipedia.org/wiki/Complex_adaptive_system

[^40_2]: https://alife.org/encyclopedia/introduction/introduction-to-complex-adaptive-system-cas/

[^40_3]: https://web.mit.edu/esd.83/www/notebook/Complex Adaptive Systems.pdf

[^40_4]: https://researchcentre.army.gov.au/library/australian-army-journal-aaj/volume-7-number-3-summer/stabilising-complex-adaptive-systems-using-complexity-theory-operational-design-stabilisation-and-support-operations

[^40_5]: https://www.stockholmresilience.org/download/18.761fdfb217fe034b93e16e7/1662712574198/CST_Policy_Complex-Adaptive-Systmes-Web.pdf

[^40_6]: https://www.sfipress.org/1-complex-adaptive-systems-a-primer

[^40_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3667498/

[^40_8]: https://www.gregoryvig.com/p/cas

[^40_9]: https://pavilion.dinfos.edu/Article/Article/2150611/basics-of-complex-adaptive-systems-thinking/

[^40_10]: https://pdodds.w3.uvm.edu/teaching/courses/2009-08UVM-300/docs/others/2005/dewolf2005a.pdf

[^40_11]: https://hbr.org/2011/09/embracing-complexity

[^40_12]: https://stream.syscoi.com/2018/11/22/complex-adaptive-systems-emergence-and-self-organization-tutorial-presented-at-hicss-42-big-island-hi-january-5-pdf/

[^40_13]: https://pubmed.ncbi.nlm.nih.gov/22118334/

[^40_14]: https://casci.binghamton.edu/academics/i-bic/lec04.php

