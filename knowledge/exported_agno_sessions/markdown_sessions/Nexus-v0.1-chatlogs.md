<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# experiment 2 will need to wait. the agents you suggest we put to work in experiment 2 will need context cards and we haven't decided how to do that yet.

from the event storming session, we saw that context curation was one of the most important jobs.

Final Prompt from previous conversation thread:

```
something we learned in earlier experiments was that every agent should have at least one reviewer (QA) of their work - it was decided it should be seen as a repeatable pattern throughout our system. the method has been shown to deliver more value than it costs. Important tasks can have more reviewers/qa agents either in parallel, or a reviewer that reviews the QAs tests. I have previously tested this with the QA writing tests, executor performing duties, QA runs tests and returns fails to executor, who fixes and returns to QA for retest until all pass.

what does this look like with Nexus?
```

Response :

```
This maps onto Nexus with remarkable clarity — and it resolves the proof template authorship ambiguity that was carried forward as an open question from the Exp-01 retro. The validated pattern actually improves the architecture by separating three roles that the original design had partially conflated.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/4e1b72e0-f288-433d-98d2-429a3ac23f68/continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md)]​


The Core Insight: Three Distinct Roles, Three Structural Separations
The original Exp-01 design had the Task Performer writing its own proof template. The validated pattern reveals that this is wrong — an agent should not define its own completion criteria. That conflates two concerns that belong to different actors:
RoleResponsibilityCan writeCan read
QA Definition Agent
Defines what done looks like — writes the proof template before implementation begins
proof_template
task_spec, ac
Task Performer Agent
Implements to satisfy the pre-defined criteria — submits literal evidence
proof, work_log
task_spec, proof_template
QA Execution Agent
Verifies that the evidence satisfies the criteria — approves or returns with findings
qa_review
proof_template, proof, task_spec
No agent reviews its own artefact. No agent defines its own completion conditions. These are structural properties enforced by tool scoping, not instructions.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/237f741a-c611-4056-9159-84d325d8355a/when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md)]​


The Lifecycle: Full Iteration Loop
text
DEFINED
  │
  ├─ activate_task fires
  ▼
TESTSPECINPROGRESS
  │  QA Definition Agent writes proof template
  │  submit_proof_template_task_XX → validates template covers AC
  ▼
TESTSPECREADY
  │  Task Performer reads spec + proof template
  │  Implements to satisfy pre-defined criteria
  │  submit_proof_task_XX (literal command output)
  ▼
PROOFSUBMITTED
  │  request_review_task_XX (Task Performer signals completion)
  ▼
AWAITINGQAREVIEW
  │  QA Execution reads proof + proof template + task spec
  │  submit_qa_review_task_XX (outcome: RETURNED, findings: [...])
  ▼
RETURNED ◄────────────────────────────────┐
  │  Task Performer reads QA findings       │
  │  Fixes issues, re-runs tests            │
  │  submit_proof_task_XX (round N)         │  ITERATION LOOP
  ▼                                         │
PROOFSUBMITTED                             │
  │  request_review_task_XX                │
  ▼                                         │
AWAITINGQAREVIEW                           │
  │  submit_qa_review_task_XX              │
  │  outcome: RETURNED ────────────────────┘
  │  outcome: APPROVED
  ▼
APPROVED (terminal for task scope)

The iteration loop is explicit in the state machine and visible in the audit log. Every cycle of submit_proof → submit_qa_review(RETURNED) → submit_proof is a named round.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/4e1b72e0-f288-433d-98d2-429a3ac23f68/continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md)]​


Tool Scopes by Role (Task-Scoped)
QA Definition Agent (task-qa-def-task-XX)
text
tools:
  # Universal
  - get_context_card
  - raise_uncertainty

  # Task-scoped reads
  - read_task_spec_task_XX
  - read_ac_task_XX           # reads AC to translate into executable proof criteria

  # Task-scoped writes
  - write_proof_template_task_XX
  - submit_proof_template_task_XX  # compound: write + state TESTSPECREADY + stream event

Task Performer Agent (task-performer-task-XX)
text
tools:
  # Universal
  - get_context_card
  - raise_uncertainty

  # Task-scoped reads
  - read_task_spec_task_XX
  - read_proof_template_task_XX   # reads what QA Definition wrote — their contract
  - read_qa_review_task_XX        # reads QA findings when in RETURNED state

  # Task-scoped writes
  - append_work_log_task_XX
  - submit_proof_task_XX           # compound: write + state PROOFSUBMITTED + stream event
  - request_review_task_XX         # request_ verb: state → AWAITINGQAREVIEW + stream event

  # GitHub MCP (scoped to task branch)
  - create_branch, push_files, create_pull_request

QA Execution Agent (task-qa-exec-task-XX)
text
tools:
  # Universal
  - get_context_card
  - raise_uncertainty

  # Task-scoped reads
  - read_proof_template_task_XX    # the criteria to verify against
  - read_proof_task_XX             # the evidence submitted
  - read_task_spec_task_XX         # original requirements

  # Task-scoped writes
  - submit_qa_review_task_XX       # compound: write + state APPROVED|RETURNED + stream event + findings

The structural property is clear: QA Execution has no write tool that the Task Performer possesses, and vice versa. QA Definition has no submission tool for proofs. Every cross-contamination between roles is architecturally absent.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/4e1b72e0-f288-433d-98d2-429a3ac23f68/continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md)]​


How Rounds Are Tracked
The audit_log records every submit_proof and submit_qa_review call with timestamps. The iteration count is derivable without a separate field — but making it explicit in the documents table is cleaner:
sql
-- documents table gains a round column
ALTER TABLE documents ADD COLUMN round INTEGER DEFAULT 1;

-- audit_log action field carries the round
-- e.g. action: '{"round": 2, "outcome": "RETURNED", "findings": [...]}'

The audit log for a two-round task looks like this:
text
submit_proof_template_task_XX  | round:—  | qa-def   | 09:10  | template written
submit_proof_task_XX           | round:1  | agent    | 09:45  | proof submitted
request_review_task_XX         | round:1  | agent    | 09:46  | QA requested
submit_qa_review_task_XX       | round:1  | qa-exec  | 10:05  | RETURNED: test env wrong, exit code mismatch
submit_proof_task_XX           | round:2  | agent    | 10:38  | proof resubmitted
request_review_task_XX         | round:2  | agent    | 10:39  | QA requested
submit_qa_review_task_XX       | round:2  | qa-exec  | 10:52  | APPROVED: all criteria met

Pete can see immediately: two rounds, specific reason for return, time from return to resubmission (33 minutes). No files opened.


The Broader Structural Rule: Every Agent Has a Reviewer
The validated pattern generalises as a framework-level invariant — not a guideline:
No artefact produced by an agent becomes authoritative without at least one independent review by a different agent.
Applied consistently across all roles:
Agent producing artefactArtefactReviewing agent
Feature Owner Agent
Feature spec, AC
QA Definition Agent
QA Definition Agent
Proof template
Task Performer reads, but also optionally a Meta-reviewer
Task Performer Agent
Proof (evidence)
QA Execution Agent
QA Execution Agent
QA review
Meta-QA (for high-priority tasks)
Context Agent
Context card
(Pete reviews for first few; auto-generated after pattern base matures)
The cost of adding a reviewer is low — one additional agent spec generated from a template, a handful of scoped read tools, and one submit_ tool. The sprint evidence shows the benefit consistently exceeds that cost.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/237f741a-c611-4056-9159-84d325d8355a/when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md)]​


Scaling: Parallel Reviewers and Meta-Review
For high-priority tasks, the pattern extends in two directions:
Parallel QA (two independent execution agents):
text
AWAITINGQAREVIEW
  ├─ QA Execution A: submit_qa_review_a_task_XX
  └─ QA Execution B: submit_qa_review_b_task_XX

State → APPROVED only when BOTH submit APPROVED
State → RETURNED if EITHER submits RETURNED (union of findings)

This requires the Policy Engine (not yet built) to evaluate a compound condition: all QA reviews for task_id are APPROVED. The tool grammar handles it cleanly — each QA agent gets a suffixed review tool (submit_qa_review_a_task_XX, submit_qa_review_b_task_XX). The compound condition is a policy row, not a code change.
Meta-review (reviewer reviews the QA's proof template):
text
TESTSPECINPROGRESS
  │  QA Definition writes proof template
  ▼
TESTSPECINREVIEW
  │  Meta-reviewer reads proof template
  │  submit_proof_template_review_task_XX (APPROVED | RETURNED)
  ▼
TESTSPECREADY (only if meta-review APPROVED)

This means the test specification itself is verified before the Task Performer ever sees it. A flawed proof template — one that would pass a broken implementation — is caught before it causes a full implementation cycle to be wasted. This directly addresses Assumption 4 from the framework assumption map: "literal command output is sufficient and reliable proof of completion" — which depends on the proof template being correct. Meta-review is the structural answer to that assumption's risk.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/237f741a-c611-4056-9159-84d325d8355a/when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md)]​


What This Changes in the Grammar
One addition to the Subject Vocabulary:
SubjectWrite modeValid verbsOwnerNotes
proof_template
Replace → then Create-once after approval
read, write, submit
QA Definition Agent (not Task Performer)
submit_proof_template transitions to TESTSPECREADY; template is immutable after that
proof_template_review
Create-once
read, submit
Meta-reviewer (optional)
Only for high-priority tasks; submit_proof_template_review either approves or returns
qa_review
Create-once per round
read, submit
QA Execution Agent
One per round; each is versioned and immutable after submit
And one clarification to the submit_ verb definition:
submit_qa_review accepts an outcome parameter (APPROVED | RETURNED) and a findings array. When outcome is RETURNED, findings is mandatory (Zod enforces this). When outcome is APPROVED, findings must be empty. The tool rejects a RETURNED submission with no findings — you cannot return a task without telling the Task Performer what to fix.


What This Means for Experiment 02
The Exp-02 hypothesis cards remain structurally valid — but the agent roster expands from two agents (Task Performer + QA Execution) to three (adding QA Definition), and the state machine gains two new states (TESTSPECINPROGRESS, TESTSPECREADY). The iteration loop is new ground. The specific test for Exp-02 Phase 5 should run at least one full RETURNED → fix → APPROVED cycle — not just the happy path — because the value of the pattern is only visible when a failure actually occurs and gets resolved through the loop rather than through Pete's intervention.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_f8ffc8cb-ddc4-4340-8bce-21d7722606ba/4e1b72e0-f288-433d-98d2-429a3ac23f68/continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md)]​
```

This is the right call — Experiment 2 has a genuine dependency on context card design, and the event storming was explicit about why that dependency matters. Here's the full picture of what's already been settled and where the open design decisions actually sit.

## What the Event Storming Established

Context curation emerged as the most important cross-cutting pattern in the entire session — not as a planned finding, but as a spontaneous discovery made three separate times before it was named. The session retrospective recorded this directly as an improvement proposal:[^1_1]

> *"Context curation appeared three times before we named it as a pattern. In future sessions, after the orange pass and before the blue pass, do an explicit pattern scan."*[^1_1]

The cross-cutting policy principle formalised was: **no significant work begins without context being explicitly prepared and verified**. It manifests at three structural points:[^1_2]

- `CurateUIContext` before `DesignUI` — Zone 2
- `CurateContext` before `PublishTask` — Zone 3
- `FullContextPackageLoaded` before `ClaimTask` — Zone 4

The authority chain was resolved as a domain decision: **Context Agent curates, QA Agent reviews, Product Owner approves** — and crucially, the agent that produces an artefact never reviews it.[^1_1]

## What's Already Designed

The design synthesis and subsequent agent spec work produced substantial prior art:[^1_2]

- **The context tree** — a full `READS/WRITES/NEVER` annotated tree for every agent invocation, with the Curate Context node identified as structurally unique: the only node where input is intentionally larger than output
- **The compression rubric** — four passes: Does the performer need to act on this? Is it already distilled downstream? Is it verifiable in this task's scope? Does it conflict with anything already included?
- **The context-package template** — eight sections: what to produce, AC (verbatim), tests (verbatim), UI specification (extracted), stack constraints (filtered list), environment constraints, boundaries, conflicts and flags
- **The inclusion/exclusion criteria** — explicit rules per artefact type, authority hierarchy for conflicts, what is always excluded (feature-level AC, sibling task files, agent instructions, rationale)
- **Conflict detection** — four typed conflict categories (direct contradiction, scope overlap, missing dependency, stale reference), each with a handling rule

This is mature and tested — the navbar pipeline run validated that the compression logic works in practice.[^1_2]

## The Actual Unresolved Question

The prior design covers **task-level context packages** — what the Task Performer Agent receives to execute work. The Experiment 2 agents need something different: **agent-level context cards** — the briefing each agent receives about its *role* and current operating context.

In the Nexus tool grammar from the previous thread, `get_context_card` is a universal tool given to every agent. What it returns has not been specified. This is the gap.

The specific design decisions needed:


| Decision | Options | What's at stake |
| :-- | :-- | :-- |
| **Static vs. dynamic cards** | Fixed card per role type OR generated fresh per task from a knowledge base | Dynamic cards honour HMW \#2 ("surface the right context at the moment it's needed") but require a generation process that doesn't exist yet |
| **Card granularity** | One card per role (QA Def, Task Performer, QA Exec) OR one card per role per task type OR one card per instantiation | Finer granularity = more relevant, more overhead to produce |
| **Card authorship for first cards** | Pete writes manually OR Context Agent generates OR both in sequence | This is the bootstrapping problem — the Context Agent needs a card too |
| **Card format / template** | What fields? Role identity, task context, relevant patterns, constraints, never-do | No template has been agreed |
| **How `get_context_card` retrieves it** | Database query by agent type + task ID? File read by path? Generated on-call? | This is an implementation decision but it drives the data model |

## The Minimum Viable Path

The cleanest unblocking move — consistent with the probe-first, evidence-based approach — is to **have Pete write the first three context cards manually** for QA Definition Agent, Task Performer Agent, and QA Execution Agent. The act of writing them forces the format to emerge from real content rather than from speculation.

The design synthesis identified this exact dynamic: *"Probe 3 — take one agent spec, identify the minimum information needed for one specific task type, generate a card manually. Run the agent with only the card, not the full spec. Measure: does task quality hold?"*[^1_3]

The format that emerges from writing those three cards becomes the card template. The compression rubric already designed for task-level packages is the right starting model — the four-pass logic applies equally to agent-level cards. The principal difference is the source material: task-level cards draw from task artefacts; agent-level cards draw from role definition, current task type, and applicable patterns from the knowledge base.

The bootstrapping sequence this implies:

1. Pete writes three role context cards (one per Experiment 2 agent) in plain markdown, applying the compression rubric manually
2. The cards become the first entries in what will eventually be a curated card library
3. `get_context_card` in Experiment 2 is implemented as a simple file read by agent type — not a generation process
4. Post-experiment retro captures: what did each agent actually use from its card? What was missing? What was never read?
5. That evidence drives the card template design — not a design session done in advance of evidence

The context curation session that needs to happen before Experiment 2 therefore has a concrete, bounded output: **three markdown context card files and a draft card template derived from writing them**. That's a session, not a system.
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_4][^1_5][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^1_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^1_3]: when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md

[^1_4]: i-d-like-you-to-conduct-the-ev-NbbGJS8yQ0.M4J0MHn24rw.md

[^1_5]: the-nature-of-the-decentralised-autonomous-organisation.pdf

[^1_6]: the-economic-institutions-of-artificial-intelligence.pdf

[^1_7]: RethinkingHowWeOrganizeWork.md

[^1_8]: Research Proposal_ Transaction Cost Economics in the AI Era.md

[^1_9]: Pre-PhD Publication Strategy_.md

[^1_10]: are-there-any-research-or-repo-c6nWZv4AThiVrYAYqhgRYQ.md

[^1_11]: summarise-this-article-and-hig-jRNDcfEvRN23xWGwmfaoZQ.md

[^1_12]: How to write a great agents.md

[^1_13]: Customize_AI_in_Visual_Studio_Code.md

[^1_14]: Custom_agents_in_VS_Code.md

[^1_15]: create-agentsmd.prompt.md

[^1_16]: ContextEngineeringSkills-README.md

[^1_17]: Pete Argent - Expert Report.pdf

[^1_18]: Stengths Insight Report.pdf

[^1_19]: CV-PeteArgent-AI.pdf

[^1_20]: TrustfulAI.md


---

# I currently have meta agents that create new agents and write their skills according to our rules. There is also an agent spec reviewer that reviews the agent creator's work.

This is a pattern we will want in Nexus too - agent creators. And this is an important one to get right.

So let's work on the policy document and decide on what rubrics decide how much qa oversight is needed for different classes of tasks and subtasks.

This is the right moment to build this policy document — before Experiment 2 runs, before context cards are designed, and before agent creators are built into Nexus. The oversight rubric needs to be upstream of all of those decisions because it determines the QA structure every agent spec author must satisfy.

Here's the full draft.

***

## What the Meta-Agent Pattern Tells Us

Your existing meta-agent setup already contains the answer to its own question: an Agent Creator writes a spec, and an Agent Spec Reviewer catches its errors before the spec becomes active. That's a **Tier 3 task** running a **two-role review chain** — QA Definition (what does correct look like?) + QA Execution (does this meet that standard?) — and you already validated it has positive ROI. The policy document just needs to make that structural reasoning explicit and then generalise it across all task classes.[^2_1]

The key insight: **the blast radius of an agent spec is asymmetric**. A bad implementation task produces one wrong output. A bad agent spec produces every future invocation of that agent producing wrong outputs — the defect multiplies with use rather than sitting inert. This asymmetry is why the meta-agent pattern deserves its own named tier rather than being treated as "just a high-priority task."[^2_1]

***

## The Classification Rubric: Three Dimensions

Before assigning a tier, every task is scored on three independent dimensions.

### Dimension 1 — Blast Radius (BR)

How many downstream operations are governed by this artefact?


| Score | Meaning |
| :-- | :-- |
| 0 | Affects this task's artefact only; no downstream consumer |
| 1 | Consumed by one downstream agent or task in this feature |
| 2 | Consumed by multiple downstream agents or tasks in this feature |
| 3 | Consumed by all tasks of this type across all features (structural) |
| 4 | Governs how the framework itself operates (invariants, policy registry, context tree) |

### Dimension 2 — Reversibility (RV)

If this artefact contains an error, how hard is it to correct?


| Score | Meaning |
| :-- | :-- |
| 0 | Fully reversible — delete the file, nothing downstream consumed it |
| 1 | Requires correction + downstream consumers must be re-run |
| 2 | Requires production rollback or data migration |
| 3 | Irreversible — published externally, in a public audit log, or defines immutable state |

### Dimension 3 — Novelty (NV)

How much prior evidence exists for this task type in the pattern library?


| Score | Meaning |
| :-- | :-- |
| 0 | Exact pattern run before; documented in pattern library with passing evidence |
| 1 | Variant of a known pattern; some inference required |
| 2 | New task type in an existing zone; no direct precedent |
| 3 | New agent class, new zone, new framework primitive — untested territory |


***

## Tier Assignment Rule

```
IF any dimension score = 4 OR (BR = 3 AND NV ≥ 1) → Tier 4: Critical
IF any dimension score ≥ 3 OR sum(BR + RV + NV) ≥ 6 → Tier 3: High
IF any dimension score ≥ 2 OR sum(BR + RV + NV) ≥ 3 → Tier 2: Elevated
IF any dimension score ≥ 1 → Tier 1: Standard
IF all scores = 0 → Tier 0: Trivial
```


***

## QA Oversight Structure by Tier

| Tier | Name | QA Structure | State Machine Addition |
| :-- | :-- | :-- | :-- |
| **0** | Trivial | Observable stream only; no review gate | None — emits to stream, no `AWAITINGQAREVIEW` state |
| **1** | Standard | Single QA Execution Agent | Baseline: `PROOFSUBMITTED → AWAITINGQAREVIEW → APPROVED/RETURNED` |
| **2** | Elevated | QA Definition Agent writes proof template first; QA Execution Agent reviews proof | Adds `TESTSPECINPROGRESS → TESTSPECREADY` before execution begins |
| **3** | High | Tier 2 chain + either: (a) Meta-reviewer validates the proof template before execution, OR (b) Two parallel QA Execution Agents; `APPROVED` requires both | Adds `TESTSPECINREVIEW` (meta-review path) or parallel `submit_qa_review_a/b` compound condition |
| **4** | Critical | Full Tier 3 chain + mandatory human gate before `APPROVED` transitions to `COMPLETE` | Pete's approval is a domain event, not a convention — `AWAITINGHUMANAPPROVAL` is a named state |

The structural rule from Experiment 1 holds as the floor: **no artefact produced by an agent becomes authoritative without at least one independent review**. Tier 0 is the only exception — and only for artefacts with no downstream consumer.[^2_1]

***

## Agent Creation as a Named Task Class

Agent creation gets its own classification because it fails the standard rubric in a specific way: **blast radius compounds with time**. Every task the agent runs after deployment is affected by its spec. The longer a defective spec runs, the more rework it generates.

### Agent Creation Tier Assignment

Scoring an agent spec task:

- BR = **3** (structural — applies across all future invocations of that agent type)
- RV = **1** (correctable, but all tasks run since deployment need audit)
- NV = depends on whether this is a new agent class (**2–3**) or a revision to an existing spec (**0–1**)

**New agent class → Tier 4 (Critical)**
**Revision to existing agent spec → Tier 3 (High)**

This means:

- New agent classes always require Pete's approval before the spec becomes active — the human gate is structural, not precautionary[^2_2][^2_1]
- Spec revisions require the Tier 3 chain: proof template is meta-reviewed before the Agent Creator ever executes


### What the Agent Spec Reviewer's Proof Template Contains

The QA Definition Agent for an agent creation task writes a proof template against the **agent design rules** (`agent-design.instructions.md`). The template specifies:[^2_1]

```
PASS CRITERIA FOR agent-spec-task-XX proof template

Structural conformance:
- READS declares named files with full absolute paths (not categories)
- WRITES declares exactly one artefact with full path
- NEVER list is present and non-empty
- File is under 60 lines

Context tree compliance:
- READS list is consistent with context-tree.md for this agent's zone
- No READS item that a child node already reads (no over-reach)
- No READS item that the orchestrator holds (no upward leak)

Skill pointers:
- Every skill referenced in the spec exists at the declared path
- No skill functionality duplicated inline in the agent file

QA structure declaration:
- task_tier field is present and set to a valid value (0–4)
- QA structure declared in task spec matches the tier rubric

Invariant compliance:
- No agent reviews its own artefact (no self-reference in READS for review step)
- Agent identity does not imply write authority it doesn't have
```

The Task Performer (Agent Creator) receives this proof template as their contract before writing a single line of the spec.

***

## The Tier Field on the Task Aggregate

The task aggregate gains one new field:[^2_2]

```sql
ALTER TABLE tasks ADD COLUMN qa_tier INTEGER NOT NULL DEFAULT 1
  CHECK (qa_tier BETWEEN 0 AND 4);
```

**Who sets it:** The Task Owner Agent proposes the tier based on the rubric scores at task definition time. QA Agent Definition validates the proposed tier as part of reviewing the task spec — tier assignment is itself a reviewable claim, not a self-declaration.

**Invariant added:** No task may enter `TESTSPECINPROGRESS` without `qa_tier` set. No task may enter `AWAITINGHUMANAPPROVAL` unless `qa_tier = 4`. The QA structure enforced must match the tier — a Tier 3 task that only runs one QA agent fails its own proof criteria.

***

## Immediate Implications

The policy document has three direct consequences for work already in flight:

- **Context cards (the current blocker):** Context card authorship is a Tier 3 task (BR = 3 — every agent of that type uses the card; NV = 2 or 3 for first cards). The first set of cards Pete writes manually bypasses this — but once the Context Agent is authoring cards, the cards need a meta-reviewer before becoming active.
- **Experiment 2 agent specs:** The three agents (QA Definition, Task Performer, QA Execution) are new agent classes — Tier 4. Their specs require Pete's sign-off before Experiment 2 can run, which is already happening informally; the policy just makes it a named gate.
- **The meta-agent in Nexus:** The Agent Creator Agent and Agent Spec Reviewer map directly onto the Tier 3 or Tier 4 chain. The only question is whether the Agent Creator is the Task Performer and the Agent Spec Reviewer is QA Execution, or whether you want a separate QA Definition Agent writing the proof template before the Creator starts. Given that agent creation is structural, the proof template path is worth it — a bad template written by QA Definition is caught cheaply; a bad spec approved without one isn't caught until the agent ships.
<span style="display:none">[^2_3][^2_4][^2_5][^2_6]</span>

<div align="center">⁂</div>

[^2_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^2_2]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^2_3]: Custom_agents_in_VS_Code.md

[^2_4]: AgenticDevelopmentFrameworkIdeation.md

[^2_5]: when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md

[^2_6]: How-to-write-a-great-agents.md


---

# In Nexus, the agent creator will be creating templates for reuse. It needs a special flow. Some questions: who decides we need a new agent? who decides what context/skills it needs? who decides what it is responsible for?

For this system to be scalable, we can't rely on human oversight except for very important cases.
I suggest we have a base agent template that is the structure for all agents.
A Framework Owner agent (FOA) can decide we need a new class of agent and delegates the drafting of an agent template spec test with acceptance criteria. The FOA delegates the spec test to be reviewed by a QA agent that specialises in agent template spec tests. An iterative loop is here until spec tests pass. Then FOA delegates to agent template creator to generate agent template spec. The FOA then delegates to a QA to run the tests and keep returning to agent template creator until tests pass. FOA can review the process for learnings and approve new agent spec template.

This is the right architectural move. The FOA pattern solves the scalability question by making the framework self-maintaining within established rules, with Pete's oversight reserved only for genuinely novel territory. Here's the full design.

***

## The Three Ownership Questions, Answered

Before the flow, the three questions need clean answers that slot into the existing ownership model:[^3_1]


| Question | Answer | Mechanism |
| :-- | :-- | :-- |
| Who decides we need a new agent? | **FOA** — monitors gap signals autonomously | Triggered by: retro findings, new task type with no matching agent, context tree coverage gap, Pete directive |
| Who decides what context/skills it needs? | **FOA** writes Agent Class Requirements (zone, READS/WRITES/NEVER candidates, skills needed); **Agent Template Creator** operationalizes against the context tree and base template | Requirements are the contract; the creator translates them into a conformant spec |
| Who decides what it's responsible for? | **FOA** writes the Job statement — one sentence, ownership boundary declared | Applies the owner naming rule: only one agent has exclusive write authority over a named artefact |

The FOA is not replacing Pete. It's applying the framework's own rules autonomously. When the gap is within established patterns (NV ≤ 1), rule-application is the entire decision. When it's genuinely novel territory (NV ≥ 2), the FOA escalates — because that's a creative judgment, not rule-application.[^3_2]

***

## Zone 0: Framework Evolution

This is a new zone that sits above the five delivery zones. It operates on the framework itself, not on features or tasks. It has its own aggregate, its own actors, and its own state machine.

### Actors

| Actor | Type | Role |
| :-- | :-- | :-- |
| **Framework Owner Agent (FOA)** | Agent — persistent | Identifies gaps, writes Agent Class Requirements, commissions tests and template, approves or escalates |
| **Agent Spec QA** | Agent — specialist | Drafts spec tests and AC; later runs those same tests against the finished template |
| **Agent Template Creator** | Agent — executor | Translates Agent Class Requirements into a conformant agent template file |
| **Pete** | Human | Approves only when NV ≥ 2 — new territory with no established pattern precedent |

**Why Agent Spec QA writes the tests AND runs them:** In the standard task flow, QA Definition and QA Execution are separate agents because their read models differ. Here they can be the same specialist because the read model at both steps is identical — the Agent Class Requirements document and the base template schema. Splitting them adds a handoff without adding independence.[^3_1]

***

## The Full Flow: State Machine

```
NEW_AGENT_GAP_IDENTIFIED
 │ Trigger: retro finding / context tree gap / Pete directive
 │ FOA reads: context-tree.md, agent-roster, pattern-library
 ↓
AGENT_CLASS_REQUIREMENTS_DRAFTED
 │ FOA writes: agent-class-requirements.md
 │ Contains: Job (1 sentence), Zone, READS/WRITES/NEVER candidates,
 │           Skills needed, NV score (0–3), qa_tier
 ↓
SPEC_TEST_COMMISSIONED ──────────────────┐
 │ FOA → Agent Spec QA                   │
 │ Agent Spec QA reads: requirements doc  │
 │ Agent Spec QA writes: spec-tests.md +  │
 │   acceptance-criteria.md              │
 ↓                                       │
SPEC_TEST_REVIEW                         │
 │ FOA reviews: do tests cover all        │
 │   requirements? Are AC measurable?     │
 │ → RETURNED ────────────────────────────┘
 │ → ACCEPTED: proceed
 ↓
SPEC_TESTS_ACCEPTED
 ↓
TEMPLATE_CREATION_COMMISSIONED ──────────┐
 │ FOA → Agent Template Creator           │
 │ Creator reads: requirements + tests    │
 │ Creator writes: agent-template-[x].md  │
 ↓                                       │
TEMPLATE_TESTED                          │
 │ Agent Spec QA runs spec-tests.md       │
 │   against the template                 │
 │ → FAILED: FOA → ReturnToCreator ───────┘
 │ → PASSED: proceed
 ↓
TEMPLATE_PASSED_TESTS
 ↓
FOA_REVIEW
 │ FOA captures learnings → pattern-library
 │ FOA checks: context tree consistency?
 │ FOA checks: clean boundary, no overlap?
 │ IF NV ≤ 1 → FOA approves
 │ IF NV ≥ 2 → escalate to Pete
 ↓
TEMPLATE_ACTIVE (added to framework roster)
```


***

## The Base Agent Template

Every agent spec that exits this flow must conform to this structure. The base template is itself a **Tier 4 artefact** — any change to it requires Pete's approval.[^3_2]

```markdown
---
name: [AgentName]
description: "[Single sentence job statement — what is this agent hired to do?]"
tools: [tool-a, tool-b]
model: [primary-model], [fallback-model]
---

ZONE: [zone-number zone-name]
TYPE: [ORCHESTRATOR | EXECUTOR | COMPRESSION | BATCH]
QA_TIER: [0-4]

READS:
- [.framework/path/to/file.md]

WRITES:
- [.framework/path/to/output.md — exactly one artefact]

NEVER:
- [.framework/path/to/forbidden.md]

SKILL: [skill-name]
CONTEXT_TREE_REF: [context-tree.md#node-name]
```

The base template enforces every agent design rule structurally:[^3_2]

- Job in one sentence — no role description, no prose
- READS as named files only — no categories
- WRITES as one artefact — one path
- NEVER list — non-empty is required to pass spec tests
- SKILL pointer — all substantive logic lives in a skill file, not inline
- CONTEXT_TREE_REF — forces the creator to declare where this agent sits in the tree

***

## The FOA's Own Context Profile

The FOA is the one agent with framework-level read authority. Its context tree node:

```
FRAMEWORK OWNER AGENT
TYPE: ORCHESTRATOR (meta-level)
READS:
  - .framework/context-tree.md
  - .github/instructions/agent-design.instructions.md
  - .github/agents/*.agent.md (roster — summary only, not full content)
  - .framework/pattern-library/ (relevant entries)
  - .framework/base-agent-template.md
  - retro-findings.md (most recent)
WRITES:
  - .framework/zone-0/agent-class-requirements.md
  - .framework/pattern-library/[new-entry].md (learnings)
  - .framework/agent-roster.md (on approval only)
NEVER:
  - feature-spec.md, task-spec.md, or any delivery zone artefacts
  - context-package.md (delivery zone, not framework)
CACHE: YES — instructions and roster are stable
BUDGET: 20k tokens (highest in the system — justified by framework-level scope)
```


***

## The Scalability Rule: When Pete Gets Called

The NV score from the QA Oversight Policy makes this mechanical, not subjective:[^3_2]

- **NV = 0** (exact pattern before, evidence in library) → FOA approves unilaterally. Example: a new executor agent for an existing zone following the same READS/WRITES/NEVER pattern as established agents.
- **NV = 1** (variant of known pattern) → FOA approves after FOA_REVIEW. Example: a batch executor variant or a new specialist QA for an existing artefact type.
- **NV = 2** (new agent class in an existing zone, no direct precedent) → FOA escalates to Pete. Example: a new zone-bridging agent or a new compression node type.
- **NV = 3** (new zone, new framework primitive, untested territory) → FOA escalates to Pete immediately at AGENT_CLASS_REQUIREMENTS_DRAFTED — before the spec test cycle begins, not after. Spending tokens on a test cycle for something Pete will likely reshape is waste.

This means **the Pete gate is a function of novelty, not importance**. The FOA handles all routine framework evolution. Pete handles the frontier.

***

## Open Questions This Flow Raises

These need resolution before Zone 0 is implemented:

1. **Gap detection mechanism:** Does the FOA poll the context tree on a schedule, subscribe to `UnknownTaskType` events from the Observable Stream, or only activate on Pete's directive? The Observable Stream model from the design thinking work suggests event subscription is the right primitive  — `UnknownTaskTypeEncountered` becomes the domain event that triggers the FOA.[^3_3]
2. **FOA bootstrapping:** The FOA itself is an agent — who creates it? The answer is Pete, manually, during initial framework setup. The FOA is the one agent exempt from the Zone 0 creation flow because it IS the Zone 0 creation flow. This is the bootstrapping exception and needs to be named as such in the framework manifest.
3. **Duplicate gap signals:** If two features running in parallel both surface the same gap (two different `UnknownTaskTypeEncountered` events for the same missing agent class), does the FOA deduplicate before commissioning? This needs a deduplication policy — likely: FOA checks the agent roster before creating a requirements doc, and if an `IN_PROGRESS` Zone 0 cycle already covers the gap, the second signal is absorbed.
4. **Template revision vs. new class:** When a retro finding suggests an existing agent template needs amendment, is that Zone 0 or a different process? The NV score still applies: NV = 0 (correcting an error in an existing template) is different from NV = 1 (evolving an existing template to cover new cases). Both go through Zone 0, but an error correction should have a shorter path — the spec tests already exist, the revision just needs to pass them again.
5. **The Agent Spec QA's own creation:** Agent Spec QA is itself an agent. It was presumably created by Pete manually (bootstrapping phase). But once Zone 0 is operational, any new specialist QA type would go through Zone 0 — which means the FOA is commissioning spec tests for an agent that will eventually review spec tests. The circularity is manageable (Agent Spec QA reviews *templates*, not itself) but worth naming explicitly as an invariant: **Agent Spec QA may not review its own template**.

<div align="center">⁂</div>

[^3_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^3_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^3_3]: when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md


---

# this sounds great but even I am getting a little confused. Let's develop this policy so that it is explainable to humans and agents. It should include a glossary and a responsibility tree of agents?

Here is the complete, standalone policy document — written to be readable by both humans and agents.

***

# Agent Creation Policy

## Nexus Agentic Development Framework — Zone 0

**Version:** 0.1
**Status:** Draft
**Applies to:** All new agent classes and agent template revisions in Nexus

***

## How to Read This Document

This policy governs how new agent classes are created in Nexus. It covers who makes each decision, what checks are required, and when a human needs to be involved.

The document is structured in four parts:

1. **Glossary** — what every term means
2. **Responsibility Tree** — who does what
3. **The Creation Flow** — the step-by-step process
4. **The Oversight Rule** — how much QA is needed for different types of work

***

## Part 1: Glossary

**Agent**
A software process that performs a defined job autonomously. An agent has a fixed set of files it reads, exactly one artefact it writes, and a list of files it is explicitly forbidden from touching. Agents do not improvise their scope — they operate within declared boundaries.

**Agent Class**
A category of agent defined by its job, zone, and artefact. "Task Performer Agent" is an agent class. There can be many instances of a class running simultaneously, but they all follow the same template.

**Agent Template**
The reusable specification file for an agent class. It defines the agent's job, what it reads, what it writes, what it is forbidden from reading, and which skills it loads. Every agent that Nexus creates is an instance of a template.

**Base Agent Template**
The minimum valid structure that every agent template must conform to. It enforces the framework's design rules structurally — not as advice, but as required fields. No agent template is valid unless it satisfies the base template.

**Framework Owner Agent (FOA)**
The agent responsible for the health and completeness of the agent roster. It identifies when a new agent class is needed, commissions the tests and template, reviews the output, and either approves it or escalates to Pete. It does not build agents itself — it delegates and oversees.

**Agent Template Creator**
The agent that writes agent templates. It receives a requirements document and a test suite, and produces a conformant agent template file. It does not decide what the agent should do — that is specified by the FOA in the requirements document.

**Agent Spec QA**
The specialist agent that (a) writes the acceptance tests for a proposed agent template, and (b) later runs those same tests against the finished template. It is the independent reviewer in the creation flow — the Agent Template Creator cannot review its own output.

**Agent Class Requirements Document**
The document the FOA writes before any template is built. It specifies the agent's job (one sentence), its zone, its candidate READS/WRITES/NEVER files, and its NV Score. This document is the contract that the Agent Template Creator works from and that Agent Spec QA tests against.

**Zone**
A stage in the delivery pipeline. The five delivery zones are Idea (1), Feature Definition (2), Task Preparation (3), Task Execution (4), and Feature Delivery (5). Zone 0 is the framework evolution zone — it operates on the framework itself, not on features.

**Write Authority**
The exclusive right to change a named artefact. Only one agent holds write authority over an artefact at any point in time. No agent may modify an artefact it does not have write authority for. No agent may review its own artefact.

**Artefact**
A file produced by an agent. Each agent produces exactly one artefact per invocation — written to a declared path. Artefacts are the unit of handoff between agents.

**Acceptance Criteria (AC)**
Human-readable statements that describe what success looks like. Written in plain language. Each criterion must be independently verifiable — a test can be derived from it — and unambiguous.

**Spec Test**
An executable check derived from acceptance criteria. Spec tests are what Agent Spec QA runs against a finished template to determine pass or fail. They test whether the template satisfies its requirements, not whether the code works.

**Proof of Completion**
Literal captured output proving work is done. For agent template creation, this means the actual test results from running the spec test suite against the template — not a claim that tests passed.

**NV Score (Novelty Score)**
A number from 0 to 3 that measures how much prior evidence exists for a proposed agent class. 0 means it has been done before with documented results. 3 means it is genuinely new territory with no prior precedent. The NV Score determines whether the FOA can approve independently or must escalate to Pete.

**Pattern Library**
The repository of documented agent class designs that have been approved and deployed. When the FOA assesses a new agent class, it checks the pattern library first. A pattern library entry with NV = 0 means the FOA can approve the new class without Pete's review.

**Observable Stream**
The append-only event log that every agent action writes to. Every state change in Nexus emits a domain event to this stream. It is the shared source of truth — not any individual agent's memory.

**Invariant**
A rule that must always be true. Invariants are enforced mechanically. If a command would violate an invariant, the system rejects it.

***

## Part 2: Responsibility Tree

```
Pete (Product Owner)
│
│  Approves new agent classes when NV ≥ 2
│  Approves changes to the Base Agent Template
│  Bootstraps the FOA and Agent Spec QA (one-time, manual)
│
└── Framework Owner Agent (FOA)
    │
    │  Identifies gaps in the agent roster
    │  Writes Agent Class Requirements documents
    │  Decides NV Score and QA Tier
    │  Reviews spec tests before template work begins
    │  Reviews finished templates before approval
    │  Adds learnings to the Pattern Library
    │  Approves new agent classes when NV ≤ 1
    │
    ├── Agent Spec QA
    │   │
    │   │  Writes spec tests and acceptance criteria
    │   │  Reviews spec tests (FOA approves, not Agent Spec QA)
    │   │  Runs spec tests against finished templates
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
- The FOA cannot approve a class with NV ≥ 2 — Pete must approve
- Pete cannot be replaced in the approval role for NV ≥ 2 by any agent

***

## Part 3: The Creation Flow

### How a new agent class comes to exist

A new agent class begins with a **gap signal** — evidence that the current agent roster cannot handle a task type that has appeared in the system. Gap signals come from three sources:

1. An `UnknownTaskTypeEncountered` event in the Observable Stream
2. A retrospective finding that a task type was handled poorly because no specialist agent exists for it
3. A direct directive from Pete

The FOA is the only agent that acts on gap signals.

***

### The seven steps

**Step 1 — FOA identifies the gap**

The FOA reads the gap signal and checks the Pattern Library and current agent roster. If a suitable agent class already exists, or a Zone 0 cycle for this gap is already in progress, the signal is absorbed — no new cycle starts. If no match exists, the FOA proceeds to Step 2.

***

**Step 2 — FOA writes the Agent Class Requirements document**

The FOA writes `agent-class-requirements.md` before any other work begins. This document must contain:

- **Job statement** — one sentence describing what this agent is hired to do
- **Zone** — which delivery zone(s) this agent operates in
- **Candidate READS** — files this agent will likely need to read (named paths, not categories)
- **Candidate WRITES** — the single artefact this agent will produce
- **Candidate NEVER** — files this agent must never access
- **NV Score** — 0, 1, 2, or 3 (see Part 4 for scoring rules)
- **QA Tier** — 0 through 4 (determined by the NV Score and Blast Radius Score)

> **If NV ≥ 2, the FOA shares the requirements document with Pete before proceeding.** Pete may reshape the requirements, approve them, or halt the cycle. Spending tokens on a test cycle for something Pete will reshape is waste. The escalation happens here — not after the template is built.

***

**Step 3 — FOA commissions spec tests**

The FOA hands the requirements document to Agent Spec QA with the instruction: *"Write the spec tests and acceptance criteria for a template that satisfies these requirements."*

Agent Spec QA produces:

- `spec-tests.md` — the executable checks that the finished template must pass
- `acceptance-criteria.md` — the human-readable criteria the spec tests derive from

Agent Spec QA does not decide whether the requirements are correct. It translates them faithfully into tests. If the requirements are ambiguous, Agent Spec QA raises that as an uncertainty to the FOA before writing tests.

***

**Step 4 — FOA reviews the spec tests**

The FOA reviews the spec tests before any template work begins. The FOA checks:

- Do the tests cover every item in the requirements document?
- Are each test's pass/fail conditions unambiguous?
- Is the test for the base template conformance present?
- Is there a test for NEVER list non-emptiness?

If the spec tests are incomplete or unclear, the FOA returns them to Agent Spec QA with specific feedback. This loop continues until the FOA accepts the spec tests. **The spec test loop closes before the template loop opens.**

***

**Step 5 — FOA commissions the agent template**

The FOA hands the requirements document and the accepted spec tests to Agent Template Creator with the instruction: *"Write an agent template that satisfies these requirements and passes these tests."*

Agent Template Creator produces `agent-template-[class-name].agent.md` conforming to the Base Agent Template structure (see below).

***

**Step 6 — Agent Spec QA runs the tests**

Agent Spec QA runs `spec-tests.md` against the finished template. It produces a `test-results.md` file containing:

- The result of each test (PASS or FAIL)
- Literal evidence for each result — not assertions
- A summary verdict: PASS ALL or FAIL with failed test list

If any test fails, the FOA returns the template to Agent Template Creator with the test results attached. Agent Template Creator revises and resubmits. **The revision loop continues until all tests pass.**

***

**Step 7 — FOA reviews and approves**

Once all tests pass, the FOA reviews the template for:

- Context tree consistency — does this agent's READS/WRITES/NEVER map correctly onto the context tree?
- Clean boundary — does this agent's job overlap with any existing agent's write authority?
- Learnings — is there anything from this cycle worth recording in the Pattern Library?

The FOA then either:

- **Approves** (NV ≤ 1) — adds the template to the agent roster and records a Pattern Library entry
- **Escalates to Pete** (NV ≥ 2) — sends Pete the template and test results for final approval before activation

Once approved, the template is active. The `AgentClassCreated` event is emitted to the Observable Stream.

***

## Part 4: The Oversight Rule

Not every agent creation cycle needs the same level of scrutiny. The required QA depth is determined by two scores.

***

### Score 1 — Blast Radius (BR)

How many future operations will this agent's template govern?


| Score | Meaning |
| :-- | :-- |
| 0 | Affects only one-off artefacts; no repeated use |
| 1 | Used repeatedly within a single feature |
| 2 | Used repeatedly across multiple features |
| 3 | Governs all tasks of a given type across the system |
| 4 | Changes how the framework itself operates |


***

### Score 2 — Novelty (NV)

How much prior evidence exists for this agent class?


| Score | Meaning |
| :-- | :-- |
| 0 | Exact pattern exists in the Pattern Library with documented results |
| 1 | Variant of a known pattern; some inference required |
| 2 | New agent class in an existing zone; no direct precedent |
| 3 | New zone, new framework primitive, or untested territory |


***

### QA Tier Assignment

```
IF NV = 3 OR BR = 4          → Tier 4: Pete approves. Escalate at Step 2, before spec tests.
IF NV = 2 OR BR = 3          → Tier 3: Full cycle (Steps 1–7) + Pete approves at Step 7.
IF NV = 1 OR BR ≥ 2          → Tier 2: Full cycle (Steps 1–7). FOA approves at Step 7.
IF NV = 0 AND BR ≤ 1         → Tier 1: Abbreviated cycle. Spec tests still required. FOA approves.
```

| Tier | Name | What changes |
| :-- | :-- | :-- |
| **1** | Routine | Spec tests are still required. Revision loop still applies. FOA approves. No Pete involvement. |
| **2** | Elevated | Full 7-step cycle. FOA approves at Step 7. No Pete involvement unless the FOA judges it warranted. |
| **3** | High | Full cycle + Pete approves the finished template at Step 7. Pete sees: requirements, test results, final template. |
| **4** | Critical | Pete is consulted at Step 2 before spec tests are written. Pete approves at Step 7. Two Pete touch points. |


***

### What tier does a new agent class usually get?

| Scenario | BR | NV | Tier |
| :-- | :-- | :-- | :-- |
| Revision to existing template (fixing an error) | 3 | 0 | 2 |
| New executor agent following an established pattern | 3 | 0 | 2 |
| New specialist QA agent for a new artefact type | 3 | 1 | 3 |
| New agent class in an existing zone, no precedent | 3 | 2 | 3 |
| New zone or new framework primitive | 4 | 3 | 4 |
| The Base Agent Template itself | 4 | — | 4 (always) |


***

## Part 5: The Base Agent Template

Every agent template produced by this flow must conform to the following structure. Fields marked REQUIRED must be present and non-empty for the spec tests to pass.

```
---
name: [AgentClassName]                       # REQUIRED
description: "[One-sentence job statement]"  # REQUIRED — what is this agent hired to do?
tools: ['tool-a', 'tool-b']                  # REQUIRED
model: ['primary-model', 'fallback-model']   # REQUIRED
---

ZONE: [zone-number zone-name]                # REQUIRED
TYPE: [ORCHESTRATOR|EXECUTOR|COMPRESSION|BATCH]  # REQUIRED
QA_TIER: [0-4]                               # REQUIRED

READS:
  - [.path/to/named/file.md]                 # REQUIRED — named files only, not categories

WRITES:
  - [.path/to/output/file.md]                # REQUIRED — exactly one artefact

NEVER:
  - [.path/to/forbidden/file.md]             # REQUIRED — at least one entry

SKILL: [skill-name]                          # REQUIRED if agent has substantive logic
CONTEXT_TREE_REF: [context-tree.md#node]     # REQUIRED — where this agent sits in the tree
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

***

## Part 6: Bootstrapping Exception

The FOA and Agent Spec QA cannot be created by the Zone 0 process because Zone 0 does not yet exist when they are first deployed. Pete creates these two agents manually during initial framework setup.

This is the **bootstrapping exception** — it applies to exactly two agents, once, at framework initialisation. All subsequent agent classes, including revisions to the FOA or Agent Spec QA, go through the Zone 0 process.

The bootstrapping exception is recorded in the framework manifest as a named decision — not a workaround.

***

## Version History

| Version | Date | Changes |
| :-- | :-- | :-- |
| 0.1 | 2026-03-03 | Initial draft. Defines Zone 0 flow, glossary, responsibility tree, oversight tiers, and base template. |

<span style="display:none">[^4_1][^4_2]</span>

<div align="center">⁂</div>

[^4_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^4_2]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md


---

# from now on, let's refer to the human as Framework Owner (FO) instead of Pete.

what other policies have we identified that are needed after our event storming session or since?

Good — noted on "Framework Owner (FO)" replacing "Pete" going forward.

Here is the full policy gap inventory, drawing everything together from the event storming session, retrospective, subsequent design sessions, and the Zone 0 work we just completed.

***

## Policy Inventory: What We Have and What's Missing

Policies are organised by status. Each gap has a source (where it was identified) and a blocking status (what it prevents).

***

## What We Have (Confirmed Stable)

The Policy Registry v0.1 contains 39 policies across five zones:[^5_1]

- **Zone 1** — 1 policy (IdeaAccepted → DefineFeature)
- **Zone 2** — 7 policies (feature definition, AC, UI design, parallel gate)
- **Zone 3** — 6 policies (task prep, tests, context curation, publish gate)
- **Zone 4** — 16 policies (execution happy path, sad path, uncertainty sub-flow)
- **Zone 5** — 9 policies (provisional, pending H13)

**Zone 0** now has a draft policy set from this session — the Agent Creation Policy v0.1.

***

## Policy Gaps Identified

### Gap 1 — Zone 5: CICD Boundary (H13)

**Source:** Event storming session, never resolved[^5_1]
**Status:** Blocking Zone 5 implementation
**The question:** If `StagingEnvironmentVerificationFailed`, does the domain own it (policy + actor responds) or does the pipeline own it (domain only observes)?
**What's missing:** P5.08 — the only policy in the entire registry with no resolution. Also blocks the full sad-path for P5.07 and P5.09 — the failure review loops for integration test failure and user testing failure have no commands, read models, or exit conditions defined.
**Needed:** Dedicated Zone 5 Event Storming session

***

### Gap 2 — Zone 4 Uncertainty Sub-flow: Second Rejection Path

**Source:** Policy Registry v0.1 open items; retrospective IP-03[^5_2][^5_1]
**Status:** Does not block Zones 3–4 implementation, but leaves a hole in the BLOCKED state resolution path
**The question:** When the Advisor Agent's mitigation is also rejected — what happens? Can the uncertainty sub-flow be re-entered from BLOCKED, or must it always route through Framework Owner review?
**What's missing:** P4.U7 onwards — the full path from second-rejection BLOCKED to resolution
**Needed:** Dedicated Uncertainty Sub-flow Event Storming session

***

### Gap 3 — Zone 5: Context Curation Pattern

**Source:** Policy Registry v0.1 cross-cutting pattern note[^5_1]
**Status:** Low urgency, but inconsistent with an established cross-cutting principle
**The question:** Does the Feature Owner Agent need a curated context card before `PlanUserTesting`? The pattern predicts yes — context curation precedes every significant work start in Zones 2, 3, and 4 — but it was never confirmed for Zone 5.
**What's missing:** Either a `CurateFeatureDeliveryContext` policy before P5.04, or an explicit decision that Zone 5 is the exception
**Needed:** Resolved in the Zone 5 Event Storming session

***

### Gap 4 — Zone 3: AC Ambiguity Escalation

**Source:** H8 resolution; noted in Policy Registry v0.1 as a "critical reactive behaviour" but never given a policy ID[^5_1]
**Status:** The behaviour exists in the Test Owner Agent spec, but has no formal policy entry
**The question:** When the Test Owner Agent raises an uncertainty because AC is too ambiguous to produce a test, what is the policy that fires, who receives it, and what are the valid responses from the Task Owner Agent?
**What's missing:** A named policy P3.07 (or similar) covering `ACTooAmbiguousToTest → RaiseUncertainty → Task Owner Agent revises AC`. Currently it is an invariant but not a reactive policy with a named command and actor.
**Needed:** Add to Policy Registry as a discrete policy entry

***

### Gap 5 — Zone 0: Framework Evolution (New — from this session)

**Source:** This session[^5_2]
**Status:** Not blocking current delivery zones, but needed before Nexus builds the FOA
**What's missing:** The full Zone 0 policy set, including:

- `P0.01` — `UnknownTaskTypeEncountered → FOA AssessGap`
- `P0.02` — `GapConfirmed (NV ≥ 2) → FOA EscalateToFrameworkOwner` (before spec tests)
- `P0.03` — `AgentClassRequirementsAccepted → FOA CommissionSpecTests`
- `P0.04` — `SpecTestsAccepted → FOA CommissionAgentTemplate`
- `P0.05` — `TemplateTestsFailed → FOA ReturnToCreator`
- `P0.06` — `TemplateTestsPassed (NV ≤ 1) → FOA ApproveAgentClass`
- `P0.07` — `TemplateTestsPassed (NV ≥ 2) → FOA EscalateToFrameworkOwner`
- `P0.08` — `AgentClassApproved → AddToRoster + UpdatePatternLibrary`
- Deduplication policy: what happens when two gap signals arrive for the same missing class simultaneously
- Template revision vs. new class distinction: error correction vs. evolution
**Needed:** Zone 0 Policy Registry — a dedicated document equivalent to the main Policy Registry

***

### Gap 6 — Zone 4: Task Retry Limits

**Source:** Design thinking session; sprint retrospectives[^5_3]
**Status:** Not blocking, but a known failure mode from real sprint data
**The question:** If a task is returned to the queue, revised, and fails again — is there a retry limit? The current policy (P4.10) routes every returned task to Framework Owner review, but there is no policy governing what happens if a task fails repeatedly after review-approved re-publishes.
**What's missing:** A policy for `TaskFailedRepeatedly → EscalateOrClose` — either a hard retry count (e.g. three returns → FO decision on whether the task itself is flawed) or an escalation trigger
**Needed:** Add to Policy Registry; may surface in the Uncertainty Sub-flow session

***

### Gap 7 — Cross-Cutting: Framework Owner Availability

**Source:** Assumptions audit, Assumption 2[^5_2]
**Status:** Architectural risk, not a missing policy per se — but needs a policy response
**The question:** The framework requires FO at multiple gates: context approval, task publishing, returned task review, Zone 0 escalations, and NV ≥ 2 approvals. There is no policy for what happens when FO is unavailable — the pipeline stalls silently.
**What's missing:** A `FrameworkOwnerUnavailable` handling policy, or explicit documentation that stalling at FO gates is acceptable behaviour (i.e. it is by design, not a failure)
**Needed:** A policy decision: is FO unavailability a domain failure or an acceptable pause? If the latter, the gates need a `AWAITING_FO` state that is visible in the Observable Stream

***

### Gap 8 — Zone 1: Idea Prioritisation

**Source:** Policy Registry v0.1 Zone 1 note[^5_1]
**Status:** Low urgency
**The question:** `IdeaPrioritised` currently has no downstream policy — it informs backlog ordering but causes no automatic action. As the backlog grows, there may need to be a policy that triggers re-ordering or surfacing the next accepted idea to the Feature Owner Agent.
**What's missing:** Either a `P1.02` `IdeaPrioritised → ReorderBacklog` or an explicit decision that backlog management is FO-driven with no automatic policy
**Needed:** A short decision, not a full session

***

## Summary: Policy Work Queue

| \# | Gap | Blocking? | How to resolve |
| :-- | :-- | :-- | :-- |
| 1 | Zone 5 CICD boundary (H13) | Yes — Zone 5 implementation | Zone 5 Event Storming session |
| 2 | Uncertainty sub-flow second rejection | No — but leaves a hole | Dedicated Uncertainty sub-flow session |
| 3 | Zone 5 context curation pattern | No — low urgency | Confirm in Zone 5 session |
| 4 | AC ambiguity escalation (no policy ID) | No — behaviour exists, just unnamed | Add P3.07 to Policy Registry |
| 5 | Zone 0 policy set | No — FO builds Zone 0 last | Write Zone 0 Policy Registry |
| 6 | Task retry limits | No — risk without a bound | Add to Policy Registry; revisit in uncertainty session |
| 7 | FO unavailability handling | Architectural risk | Policy decision: stall = acceptable pause? |
| 8 | Idea prioritisation policy | No — low urgency | Short decision, add to Policy Registry |

The two sessions that unlock the most gaps are the **Zone 5 Event Storming session** (clears gaps 1 and 3) and the **Uncertainty Sub-flow session** (clears gap 2 and likely 6). Gaps 4, 7, and 8 can be resolved in focused short decisions without a full session.[^5_2][^5_1]

<div align="center">⁂</div>

[^5_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^5_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^5_3]: when-people-design-and-develop-ga22rLeiTA64m3y4v9GD5A.md


---

# what are the options and your recommendations for CICD boundary policy?

The H13 CICD boundary question has a clean core: when `StagingEnvironmentVerificationFailed` fires, does the domain own it or just observe it? Everything else follows from that single decision. Here are the three distinct options, their implications, and a recommendation.

***

## The Core Question

The domain currently sends a command to the CICD pipeline (`VerifyStagingEnvironment`) and receives one of two events back: `StagingEnvironmentVerified` or `StagingEnvironmentVerificationFailed`. The question is what the domain *does* with the failure event.[^6_1]

***

## Option 1 — The Domain Observes Only

**What it means:** `StagingEnvironmentVerificationFailed` is treated as a read-only signal from an external system. The domain records it in the Observable Stream and emits no downstream policy. No domain actor is assigned to respond. The failure lives entirely within the CICD pipeline's responsibility.

**What it looks like in the policy registry:**

```
P5.08  StagingEnvironmentVerificationFailed
       → No domain policy. Event observed and logged only.
       → CICD pipeline is responsible for resolution.
       → Feature aggregate enters AWAITING_PIPELINE state.
```

**Advantages:**

- Clean boundary — the domain does not try to govern infrastructure it does not control
- No actor needs to be assigned a job they cannot meaningfully do (domain agents cannot fix a broken pipeline)
- Consistent with how external systems are treated elsewhere in the framework

**Disadvantages:**

- A feature can silently stall in `AWAITING_PIPELINE` indefinitely with no domain-level response
- The FO has no visibility unless they are watching the CICD pipeline independently
- Breaks the framework's own principle: *failure always routes to a review*  — this option creates a failure with no review[^6_1]

***

## Option 2 — The Domain Owns It Fully

**What it means:** `StagingEnvironmentVerificationFailed` is a domain failure. The Feature Owner Agent is assigned a review task, must diagnose the failure, and issues a command to either retry or escalate. The domain has write authority over the staging failure path.

**What it looks like in the policy registry:**

```
P5.08  StagingEnvironmentVerificationFailed
       → Feature Owner Agent reviews → ReviewStagingFailure
       → Outcomes: RetryStaging | EscalateToFO | CloseFeature
```

**Advantages:**

- Consistent with every other failure in the system — failure routes to a review, always
- Maintains complete visibility in the Observable Stream
- FO remains in the loop via the domain, not by monitoring external tools

**Disadvantages:**

- The Feature Owner Agent may have no ability to act on the information — a pipeline misconfiguration requires a human or infrastructure change, not a domain agent
- Risks creating a review loop that produces no resolution because the actual cause is outside the domain's reach
- Could produce false accountability: the domain *looks* like it is handling it while the real fix happens elsewhere

***

## Option 3 — Hybrid: Observe and Escalate to FO

**What it means:** The domain does not assign a domain agent to resolve the failure, but it does emit a named escalation event and creates an `AWAITING_FO` state that is visible in the Observable Stream. The FO is the actor who resolves it — either by fixing the pipeline externally and triggering a retry, or by closing the feature.

**What it looks like in the policy registry:**

```
P5.08  StagingEnvironmentVerificationFailed
       → System Policy: EscalateToFrameworkOwner
       → Feature enters AWAITING_FO state
       → FO reviews externally, then either:
            → IssueRetryStaging command (domain receives CICD retry)
            → IssueCloseFeature command (terminal state)
```

**Advantages:**

- Upholds *failure routes to a review* — the FO is the reviewer, not a domain agent
- Honest about who can actually act: the FO has access to the pipeline, domain agents do not
- The feature does not stall silently — `AWAITING_FO` is visible in the Observable Stream
- Consistent with how the framework already handles situations requiring human judgment (H1 resolution: *irreversible actions require human authority*)
- Adds a named `AWAITING_FO` state to the Feature aggregate — which also addresses Gap 7 from the policy inventory (FO unavailability) more broadly

**Disadvantages:**

- Requires formalising `AWAITING_FO` as a distinct Feature aggregate state
- The FO cannot delegate this — it is a hard stop until they act

***

## Recommendation: Option 3

**Adopt the hybrid model.** The reasoning follows directly from decisions already made in the framework:[^6_1]

1. **The "failure always routes to review" principle cannot have exceptions.** Option 1 breaks it. That principle was described as "a deliberate trust decision, not a coincidence of design." One exception teaches the system — and agents reading it — that the principle is optional.
2. **Domain agents cannot fix infrastructure.** Option 2 creates a review loop with no genuine resolution path. The Feature Owner Agent reviewing a pipeline failure cannot fix it — that is the FO's job. Assigning the review to an agent that cannot act is theatre, not governance.
3. **The FO already holds authority at irreversible decision points.** H1 established this — publishing a task requires the FO because it is irreversible. Staging verification failure is also an irreversible-adjacent decision: retrying staging costs real pipeline time and potentially deploys broken code. That warrants FO authority, not agent authority.
4. **`AWAITING_FO` is the right primitive.** It is honest, visible, and auditable. It also resolves Gap 7 from the policy inventory — if you formalise `AWAITING_FO` as a Feature aggregate state here, you have the mechanism to apply it wherever FO availability is a gate across the whole framework.

***

## What H13 Resolution Produces

Resolving H13 with Option 3 closes the following gaps:


| Item | How it closes |
| :-- | :-- |
| P5.08 — unresolved policy | Gets a named policy: `StagingEnvironmentVerificationFailed → EscalateToFO` |
| Feature Aggregate Spec v0.1 — Invariant 11 placeholder | Resolved: domain observes and escalates, does not govern the pipeline |
| Zone 5 sad-path gap | P5.07 and P5.09 failure review loops now have a consistent model: FO reviews, not Feature Owner Agent |
| Gap 7 — FO unavailability | `AWAITING_FO` state provides the Observable Stream signal that the system is waiting on a human |

The one thing Option 3 does **not** resolve is the underlying Zone 5 under-specification — the failure review loops for `IntegrationTestsFailed` and `UserTestingFailed` (P5.07 and P5.09) still need commands, read models, and exit conditions. That work belongs in the Zone 5 Event Storming session. But H13 itself no longer needs to wait for it.[^6_2]

<div align="center">⁂</div>

[^6_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^6_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md


---

# Let's bring CICD into the domain as I see the value of this framework is its ability to own idea to deployed process. AI agents are already being used in DevOps and is largely automated anyway.

This is a significant architectural decision — it expands the domain boundary and converts H13 from a deferral into a resolution. Let me work through what this means fully.

***

## Decision: CICD Joins the Domain

By bringing CICD inside the domain boundary, the pipeline is no longer an external system that the domain *observes* — it becomes a set of domain actors with write authority, commands they issue, and events they produce. The pink sticky becomes a yellow sticky.[^7_1]

This is consistent with where AI-assisted DevOps is heading: pipelines are already largely automated, and the gap between "an agent writes code" and "an agent deploys code" is increasingly artificial.

***

## What Changes Immediately

### The External Systems Map

The event storming session identified the CICD Pipeline, Staging Environment, and Production Environment as three separate external pink stickies. Under this decision:[^7_1]


| Was | Now |
| :-- | :-- |
| CICD Pipeline — external system (pink) | CICD Agent — domain actor (yellow) |
| Staging Environment — external system (pink) | Staging Environment — infrastructure the CICD Agent governs |
| Production Environment — external system (pink) | Production Environment — infrastructure the CICD Agent governs |
| Version Control — external system (pink) | Could remain external, or become a CICD Agent responsibility |

The CICD Agent becomes a new domain actor in Zone 5 — the first actor that operates exclusively in that zone.

***

## The CICD Agent: What It Owns

Following the same template as every other agent in the framework, the CICD Agent needs a clean job statement, write authority, and a defined artefact:

**Job statement:** The CICD Agent executes and verifies all automated delivery operations — integration testing, staging promotion, staging verification, and production promotion — and reports outcomes to the Observable Stream as first-class domain events.

**Write authority by state:**


| Feature State | CICD Agent Write Authority |
| :-- | :-- |
| `ALL_TASKS_COMPLETE` | Runs integration tests → emits `IntegrationTestsPassed` or `IntegrationTestsFailed` |
| `INTEGRATION_TESTS_PASSED` | Promotes to staging → emits `PromotedToStaging` |
| `PROMOTED_TO_STAGING` | Verifies staging environment → emits `StagingEnvironmentVerified` or `StagingEnvironmentVerificationFailed` |
| `USER_TESTING_PASSED` | Promotes to production → emits `FeaturePromotedToProduction` |

**Artefact it owns:** `deployment-record.md` — an append-only log of every deployment action, environment state at the time of execution, exit codes, and test outputs. This is the Zone 5 equivalent of `proof-of-completion` in Zone 4.

***

## H13 Resolved

With CICD inside the domain, H13 has a clean answer:

> **`StagingEnvironmentVerificationFailed` is a domain failure. The CICD Agent owns it. The policy fires to the Feature Owner Agent for review, consistent with every other failure in the framework.**

The policy table for Zone 5 now completes:


| ID | Trigger | Policy | Actor |
| :-- | :-- | :-- | :-- |
| P5.01 | `AllTasksCompleted` | CICD Agent runs integration tests | CICD Agent |
| P5.02 | `IntegrationTestsPassed` | CICD Agent promotes to staging | CICD Agent |
| P5.03 | `PromotedToStaging` | CICD Agent verifies staging environment | CICD Agent |
| P5.04 | `StagingEnvironmentVerified` | Feature Owner Agent plans user testing | Feature Owner Agent |
| P5.05 | `UserTestingPassed` | CICD Agent promotes to production | CICD Agent |
| P5.06 | `FeaturePromotedToProduction` | System marks feature complete | System Policy |
| P5.07 | `IntegrationTestsFailed` | Feature Owner Agent reviews → CICD Agent retries or FO closes | Feature Owner Agent |
| **P5.08** | **`StagingEnvironmentVerificationFailed`** | **Feature Owner Agent reviews → CICD Agent retries or FO closes** | **Feature Owner Agent** |
| P5.09 | `UserTestingFailed` | Feature Owner Agent reviews → CICD Agent retries or FO closes | Feature Owner Agent |

**P5.08 is now resolved.** The failure routes to a review — consistent with every other failure in the system.[^7_1]

***

## What the CICD Agent Needs to Read

Following the read model pattern, the CICD Agent needs:

- **Before running integration tests:** Full task list with all `COMPLETED` status confirmations, integration test suite, environment contract baseline
- **Before promoting to staging:** Integration test results (passed), staging environment spec
- **Before verifying staging:** Staging deployment confirmation, staging environment contract (equivalent to Zone 4's environment contract, but at feature level)
- **Before promoting to production:** User testing results (passed), production environment spec, staging verification confirmation

***

## New Invariants for Zone 5

The domain now owns these rules mechanically:

1. The CICD Agent may not run integration tests unless every task in the Feature's task list is in `COMPLETED` or `CLOSED` status
2. The CICD Agent may not promote to staging unless integration tests have passed in the current cycle — a prior passing run does not count if tasks have changed
3. The CICD Agent's `deployment-record.md` is append-only and constitutes proof of delivery — equivalent to `proof-of-completion` at task level
4. No human trigger is required for any CICD Agent action — all fires are policy-triggered
5. The FO retains authority to halt any CICD Agent action by issuing `HaltDelivery` — an emergency stop that transitions the Feature to `DELIVERY_HALTED`

***

## What This Means for the Framework Design

Bringing CICD inside the domain has three second-order consequences worth noting before the Zone 5 Event Storming session:

**1. Zone 5 now has a first-class actor.**
Every other zone had clearly defined actors at the point of storming. Zone 5 was thin partly because its primary actor — the CICD Agent — was sitting outside the boundary. With it inside, the Zone 5 session will be materially more productive.

**2. The "idea to deployed" value proposition is now structurally complete.**
The domain boundary now runs from `IdeaCaptured` (Zone 1) to `FeaturePromotedToProduction` (Zone 5) without any external handoff. Every state transition is a domain event. Every failure routes to a domain review. The Observable Stream covers the entire lifecycle.[^7_2]

**3. The CICD Agent needs its own Zone 0 creation cycle.**
It is a new agent class, operating in a zone that was previously external, with no existing pattern in the Pattern Library. That puts it at **NV Score 2, BR Score 3 → QA Tier 3**: full 7-step creation cycle with FO approval at Step 7. This is the first real test of the Zone 0 process.

***

## What the Zone 5 Event Storming Session Now Needs to Storm

The decision to bring CICD into the domain changes the Zone 5 session agenda:

- **Orange storm:** What are all the events the CICD Agent can produce? Include failure events from the start — pipeline failures, environment drift, test flakiness, rollback events
- **Sad path emphasis (IP-01):** For every CICD Agent success event, there is at least one failure event. Both on the board from the first pass
- **New hotspots to expect:** What does the CICD Agent do when a staging promotion fails mid-flight? Does it retry autonomously or always route to review? What is the retry limit before FO escalation? What constitutes a valid staging environment verification — is it a health check, a smoke test, or a full regression?
- **Deployment record spec:** What does `deployment-record.md` need to contain to serve as genuine proof of delivery?
- **Rollback policy:** If `FeaturePromotedToProduction` is followed immediately by a critical failure, does the domain own rollback, or is that outside scope?

<div align="center">⁂</div>

[^7_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^7_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md


---

# Should The Uncertainty Sub-flow should really be in each zone? The uncertainty tool in Nexus is a universal tool available to all agents.

This is an important structural question that has implications for how uncertainty is modelled across the entire framework.

***

## The Current Model vs. What You're Describing

The event storming session placed the Uncertainty sub-flow inside Zone 4, treating it as a Task-level concern. But you're identifying something more fundamental: uncertainty is not a Zone 4 phenomenon — it's a capability that any agent, in any zone, may need at any point in their work.[^8_1]

The distinction matters architecturally:


| Current model | Proposed model |
| :-- | :-- |
| Uncertainty is a Zone 4 sub-flow within the Task aggregate | Uncertainty is a cross-cutting domain primitive available in all zones |
| `UncertaintyRaised` is a Task event | `UncertaintyRaised` is a domain event independent of aggregate |
| Advisor Agent operates only in Zone 4 | Advisor Agent (or equivalent) is available to all agents in all zones |
| Uncertainty has one lifecycle tied to the Task lifecycle | Uncertainty has its own aggregate, its own lifecycle, independent of parent |


***

## What This Decision Actually Resolves

The session retrospective flagged the Uncertainty sub-flow as needing its own dedicated Event Storming session (IP-03), partly because it is "complex enough to be treated as its own domain". Your observation explains *why* it felt that way — it was being treated as a Zone 4 sub-flow when it is actually a **standalone aggregate** that crosses all zones.[^8_1]

This also directly addresses Assumption 10 from the assumptions audit: *"The Uncertainty sub-flow handles all classes of mid-execution blockage"* — the reason that assumption felt fragile is that the sub-flow was anchored to Zone 4 when the tool it represents is universal.[^8_2]

***

## Uncertainty as a Cross-Cutting Aggregate

If uncertainty is a universal tool, the Uncertainty aggregate needs to be redesigned as independent:

### What the Uncertainty Aggregate Owns

| Artefact | Description | Set by |
| :-- | :-- | :-- |
| `uncertainty-id` | Unique identifier, assigned at raise time | System |
| `parent-ref` | Reference to the raising agent and their current context (zone, aggregate, artefact being worked on) | System |
| `zone` | Which zone the uncertainty was raised in | System |
| `description` | What the agent cannot resolve independently | Raising agent |
| `context-snapshot` | Read model the agent had at the time of raising | Raising agent |
| `research` | Advisor Agent's findings | Advisor Agent |
| `mitigation` | Proposed resolution path | Advisor Agent |
| `review-result` | Accepted or rejected | Raising agent's zone reviewer |
| `resolution-status` | RAISED → RESEARCHED → MITIGATION_DEFINED → RESOLVED or REJECTED | System |
| `uncertainty-log` | Append-only history of all state changes | System |

### Valid States

```
RAISED
  → RESEARCHED (Advisor Agent)
    → MITIGATION_DEFINED (Advisor Agent)
      → RESOLVED (reviewer accepts mitigation)
      → REJECTED (reviewer rejects mitigation)
        → ESCALATED_TO_FO (second rejection or no viable path)
```


***

## How This Changes Each Zone

Rather than uncertainty being "in Zone 4," every zone has a consistent pattern:

**Any agent, in any zone, may raise an uncertainty when they cannot proceed.**

The trigger and response are the same regardless of zone:

```
Whenever [Agent] cannot proceed due to unresolvable ambiguity
→ Agent raises UncertaintyRaised (with parent-ref to current zone + artefact)
→ Advisor Agent researches
→ Mitigation defined and reviewed
→ If accepted: Agent resumes where it left off
→ If rejected: Escalated to FO
```


### Zone-by-zone examples that are now possible

| Zone | Who might raise | Example |
| :-- | :-- | :-- |
| Zone 1 | Feature Owner Agent | Accepted Idea has contradictory success criteria — cannot DefineFeature |
| Zone 2 | UI Design Agent | Brand guidelines conflict with accepted AC — cannot DesignUI |
| Zone 2 | Test Owner Agent | AC is too ambiguous to produce a test — *already modelled as this, just unnamed* |
| Zone 3 | Context Agent | Two accepted artefacts contain conflicting information — cannot CurateContext |
| Zone 4 | Task Performer Agent | Environment state doesn't match contract — cannot PerformTask |
| Zone 5 | CICD Agent | Integration test suite produces non-deterministic results — cannot confirm pass |

Note that the AC ambiguity escalation (Gap 4 from the policy inventory) is *already* this pattern — it just wasn't named as an uncertainty raise. Bringing uncertainty into all zones closes Gap 4 as a by-product.

***

## What Changes for the Advisor Agent

The Advisor Agent currently has an implicit Zone 4 scope. If uncertainty is universal, the Advisor Agent becomes a **zone-agnostic specialist** — the one agent in the framework whose job is triggered by events from any zone, not by zone position.

This actually makes the Advisor Agent cleaner to spec, not more complex:

- **Job statement:** The Advisor Agent researches and proposes mitigations for any uncertainty raised by any agent in any zone. It has no zone of its own — it is invoked by event, not by position.
- **Read model:** Always the same — `uncertainty-description` + `context-snapshot` from the raising agent + relevant artefacts from the parent zone
- **Write authority:** Only over the Uncertainty aggregate — specifically `research`, `mitigation`, and `resolution-status` fields
- **NEVER:** The Advisor Agent never modifies the artefact the raising agent was working on — it only resolves the uncertainty so the raising agent can continue

***

## New Policy: P_U (Cross-Cutting, All Zones)

Instead of P4.U1–P4.U6 belonging to Zone 4, the uncertainty policies become a **cross-cutting policy set** referenced from every zone:


| ID | Trigger | Policy | Actor |
| :-- | :-- | :-- | :-- |
| P.U1 | `UncertaintyRaised` (any zone) | Advisor Agent researches | Advisor Agent |
| P.U2 | `UncertaintyResearched` | Advisor Agent defines mitigation | Advisor Agent |
| P.U3 | `MitigationDefined` | Zone-appropriate reviewer reviews | Zone reviewer |
| P.U4 | `MitigationAccepted` | Raising agent resumes | Raising agent |
| P.U5 | `MitigationRejected` (first) | Advisor Agent revises mitigation | Advisor Agent |
| P.U6 | `MitigationRejected` (second) | Uncertainty escalated to FO | System Policy |
| P.U7 | `UncertaintyEscalated` | FO resolves or closes the parent work item | FO |

P.U6 and P.U7 close **Gap 2** from the policy inventory — the second-rejection path that was left unresolved.[^8_2]

***

## What the Uncertainty Sub-flow Session Now Needs to Storm

The dedicated session (IP-03) is still needed, but the frame is now cleaner:[^8_1]

- **Storm the Uncertainty aggregate as a standalone domain** — not as a Zone 4 sub-flow
- **Storm all the zones it touches** — what does a raised uncertainty look like in Zone 1 vs Zone 5? Are there zone-specific variations in who the reviewer is?
- **Storm the Advisor Agent spec** — it is now one of the most important agents in the framework because it touches every zone
- **Storm the reviewer role by zone** — in Zone 4, the reviewer is implicit (the Task Owner Agent resumes). In Zone 2, who reviews a mitigation for a UI design uncertainty? The same chain — QA Agent Definition → FO?
- **Storm the parent aggregate relationship** — when an uncertainty is raised in Zone 3, what state does the parent Task enter? `UNCERTAINTY_RAISED` already exists in the Task lifecycle; this now needs equivalents in the Feature aggregate for Zones 2 and 5

***

## Summary of What This Decision Unlocks

- **H13 ripple:** The CICD Agent in Zone 5 can now raise uncertainties when pipeline results are non-deterministic — which was previously unhandled
- **Gap 2 closed:** The second-rejection path now has a named policy (P.U6 → P.U7)
- **Gap 4 closed:** AC ambiguity escalation is now formally the universal uncertainty pattern, not a special case
- **Assumption 10 strengthened:** The uncertainty sub-flow now genuinely handles all classes of blockage across all zones, not just Zone 4 task execution failures
- **Advisor Agent promoted:** From a Zone 4 supporting actor to one of the framework's most important cross-cutting agents

<div align="center">⁂</div>

[^8_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^8_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md


---

# I see the value in having an uncertainty advisor for each zone. A zone 2 advisor shouldn't need context of other zones to do its work.

This is a clean and important refinement. You're applying the same design principle that resolved H11 — when two agents carry materially different context loads, splitting them is the right call.[^9_1]

***

## The Parallel with H11

H11 asked: one QA Agent or specialist QA agents? The answer was two specialists — QA Agent Definition (Zones 2–3) and QA Agent Execution (Zone 4) — because their context loads were genuinely different.[^9_1]

The same logic applies here with even more force. An Advisor Agent resolving a UI design uncertainty in Zone 2 needs:

- Feature spec, brand guidelines, accepted AC, UI context
- Knowledge of design patterns and visual systems

An Advisor Agent resolving an environment contract failure in Zone 4 needs:

- Task spec, environment contract snapshot, tool capabilities, execution logs
- Knowledge of infrastructure, runtime environments, debugging patterns

These are not variations of the same context — they are different domains of expertise entirely. A single Advisor Agent carrying all of this would be one of the most overloaded agents in the system, and its context card would be enormous.

***

## The Zonal Advisor Model

Each zone gets its own Advisor Agent, scoped to that zone's artefacts, actors, and failure modes:


| Agent | Zone | Resolves uncertainties raised by | Context it needs |
| :-- | :-- | :-- | :-- |
| Zone 1 Advisor Agent | Zone 1 | Feature Owner Agent (pre-feature definition) | Idea spec, success criteria, backlog patterns |
| Zone 2 Advisor Agent | Zone 2 | Feature Owner Agent, UI Design Agent, Context Agent | Feature spec, AC, brand guidelines, UI design patterns |
| Zone 3 Advisor Agent | Zone 3 | Test Owner Agent, Context Agent, Task Owner Agent | Task spec, AC, test patterns, context curation patterns |
| Zone 4 Advisor Agent | Zone 4 | Task Performer Agent | Task spec, environment contract, tool capabilities, execution logs |
| Zone 5 Advisor Agent | Zone 5 | CICD Agent, Feature Owner Agent | Deployment record, pipeline patterns, integration test results, environment specs |


***

## What Each Advisor Agent Owns

The job statement and write authority are identical across all five — only the read model differs:

**Job statement (universal):** The [Zone N] Advisor Agent researches and proposes mitigations for uncertainties raised by agents operating in Zone [N]. It does not modify the artefact the raising agent was working on. It resolves the uncertainty so the raising agent can resume.

**Write authority (universal):** Only over the Uncertainty aggregate — `research`, `mitigation`, and `resolution-status` fields within uncertainties whose `zone` field matches their own zone.

**NEVER (universal):** A Zone N Advisor Agent may never read artefacts from other zones, and may never write to any artefact other than the Uncertainty aggregate.

This last invariant is critical — it enforces the zone boundary mechanically, not by convention.

***

## The Reviewer by Zone

When P.U3 fires (`MitigationDefined → zone-appropriate reviewer reviews`), the reviewer is now unambiguous:


| Zone | Mitigation reviewer |
| :-- | :-- |
| Zone 1 | FO (idea-level decisions are always human) |
| Zone 2 | QA Agent Definition (already the Zone 2 quality gate) |
| Zone 3 | QA Agent Definition (same agent, different artefact type) |
| Zone 4 | QA Agent Execution (already the Zone 4 quality gate) |
| Zone 5 | Feature Owner Agent (Zone 5 review authority already established) |

This is elegant — the Advisor Agent hands the mitigation to whoever already holds review authority in that zone. No new actors required.

***

## The Updated Cross-Cutting Policy Set

The P.U policies now read with zone-specific actors substituted at P.U3:


| ID | Trigger | Policy | Actor |
| :-- | :-- | :-- | :-- |
| P.U1 | `UncertaintyRaised` (zone N) | Zone N Advisor Agent researches | Zone N Advisor Agent |
| P.U2 | `UncertaintyResearched` | Zone N Advisor Agent defines mitigation | Zone N Advisor Agent |
| P.U3 | `MitigationDefined` | Zone N reviewer reviews mitigation | Zone N reviewer (see table above) |
| P.U4 | `MitigationAccepted` | Raising agent resumes | Raising agent |
| P.U5 | `MitigationRejected` (first) | Zone N Advisor Agent revises | Zone N Advisor Agent |
| P.U6 | `MitigationRejected` (second) | System escalates to FO | System Policy |
| P.U7 | `UncertaintyEscalated` | FO resolves or closes parent work item | FO |

The `zone` field on the Uncertainty aggregate is what routes P.U1 to the correct Advisor Agent — it is the dispatch key.

***

## What This Means for the Uncertainty Sub-flow Session

The dedicated session now has a sharper frame. Rather than designing one Advisor Agent, it needs to storm five:

- **For each zone:** what are the most common uncertainty types? What does the context snapshot need to contain for the Advisor Agent to do useful research?
- **Zone 1 is the special case:** FO reviews all Zone 1 mitigations. Is there even enough volume of Zone 1 uncertainties to justify a dedicated Zone 1 Advisor Agent, or does Zone 1 uncertainty always escalate directly to FO?
- **Zone boundary enforcement:** What is the invariant that prevents a Zone 4 Advisor Agent from reading a feature spec? This needs to be in the NEVER list of every Advisor Agent template and enforced by the base agent template spec test.
- **Handoff on escalation (P.U7):** When FO resolves an escalated uncertainty, which zone's Advisor Agent — if any — is involved in communicating the resolution back to the raising agent?

***

## Second-Order Effect: Zone 0 Gets an Advisor Agent Too

Zone 0 — the framework evolution zone — will also produce uncertainties. The Framework Owner Agent writing an Agent Class Requirements document may encounter something it cannot resolve: a proposed agent class that appears to conflict with an existing boundary, or an NV Score it cannot confidently assign.

A **Zone 0 Advisor Agent** follows the same pattern — scoped entirely to framework-level artefacts (agent roster, pattern library, base agent template), with FO as the mitigation reviewer. This is consistent, costs nothing new structurally, and prevents the FOA from silently proceeding when it should surface a problem.

<div align="center">⁂</div>

[^9_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md


---

# answer this for me:

For each zone: what are the most common uncertainty types? What does the context snapshot need to contain for the Advisor Agent to do useful research?

This is the most practically useful input for the Uncertainty Sub-flow session. Here is the full analysis by zone, derived directly from the read models, actors, and failure patterns in the framework.[^10_1][^10_2]

***

## Zone 0 — Framework Evolution

The Zone 0 Advisor Agent handles uncertainties raised by the Framework Owner Agent during agent class creation.

**Most common uncertainty types:**

- A proposed agent class appears to overlap with an existing agent's write authority — unclear who owns the boundary
- NV Score cannot be confidently assigned — the proposed class is partially novel but has some precedent
- The NEVER list cannot be fully specified because the agent's scope is not yet well-defined enough
- A proposed agent class requires a skill that does not yet exist in the skill inventory

**Context snapshot must contain:**

- Agent Class Requirements document (the draft being worked on)
- Current agent roster (all existing agent class names, zones, and WRITES paths)
- Pattern Library (all prior approved agent classes with their NV scores)
- Base Agent Template structure
- Context tree — the READS/WRITES/NEVER map for the whole system

***

## Zone 1 — Idea Capture

Zone 1 is human-operated, but the Feature Owner Agent acts on the `IdeaAccepted` event. Uncertainties here arise at the threshold between idea and feature.[^10_2]

**Most common uncertainty types:**

- The accepted idea contains contradictory success criteria — cannot write a coherent feature spec
- The idea's scope is ambiguous — unclear whether it represents one feature or several
- Success criteria are outcome-stated but the domain model has no equivalent concept — e.g., "users should feel confident" has no testable feature-level translation
- The idea references a dependency (another feature, an external system) that has no current domain representation

**Context snapshot must contain:**

- The accepted idea document
- Success criteria as written by the FO
- The current feature backlog (to check for overlap or dependency)
- Any prior ideas in `ICED` or `REJECTED` status that appear related — history of similar ideas informs scope

**Note:** Zone 1 uncertainties are reviewed by the FO directly — the stakes of building the wrong thing are too high for an agent review gate here.[^10_2]

***

## Zone 2 — Feature Definition

Zone 2 has the richest uncertainty surface because it runs two parallel tracks simultaneously — AC definition and UI design — and both must complete before anything downstream can proceed.[^10_1]

**Most common uncertainty types — AC track:**

- An acceptance criterion cannot be written in unambiguous GivenWhenThen format — the intended behaviour has multiple valid interpretations
- Two acceptance criteria within the same feature contradict each other
- An acceptance criterion requires a technical implementation decision to be made before the problem-space statement can be written — the feature spec is leaking into solution space
- Success criteria from the idea cannot be translated into verifiable feature-level AC — too qualitative

**Most common uncertainty types — UI design track:**

- Brand guidelines conflict with an accepted acceptance criterion — e.g., brand requires a single-column layout but AC requires two interactive panels visible simultaneously
- The curated UI context is incomplete — missing component library references, or references a design token that does not exist
- The feature spec is ambiguous about the interaction model — cannot design UI without knowing whether the interaction is inline, modal, or page-level
- An accepted UI design component does not exist in the design system — should it be built, substituted, or does the AC need to change?

**Context snapshot must contain:**

- Feature spec (current draft)
- Feature-level acceptance criteria (current state)
- Brand guidelines (full, not summarised — design decisions require specificity)
- Design system / component library reference
- Success criteria from the parent idea (for intent checking)
- QA Agent Definition's review notes if the uncertainty arose after a review rejection

**Reviewer:** QA Agent Definition — already the Zone 2 quality gate for both AC and UI.[^10_2]

***

## Zone 3 — Task Preparation

Zone 3 is the highest-complexity zone in the system, with more handoffs than any other. Uncertainties here tend to surface at the translation boundaries — AC to tests, and combined artefacts to context package.[^10_2]

**Most common uncertainty types — Test Owner Agent:**

- An acceptance criterion cannot produce at least one executable test — this is the formally named ambiguity detection trigger (Invariant 9)[^10_2]
- Two acceptance criteria produce tests that contradict each other — passing one would fail the other
- The expected system behaviour is clear but the environment required to verify it is not specified — cannot write a test without knowing the environment contract
- A test requires a third-party service or data state that is not described in the feature spec

**Most common uncertainty types — Context Agent:**

- Two accepted artefacts (e.g., feature spec and UI artefact) contain conflicting information about the same behaviour — the context conflict rule fires, agent stops[^10_1]
- The context package would exceed the declared budget for the task type — compression is not possible without losing information that appears essential
- A task spec references a shared resource (database schema, API contract) that is not in any of the declared READS files
- The UI artefact references a component or state that is not mentioned in the task spec or AC — unclear whether to include it

**Most common uncertainty types — Task Owner Agent:**

- Feature decomposition produces a task that cannot be made independent — it has a hard dependency on the output of a sibling task that may not be complete first
- A task's required skills cannot be declared because the task involves a capability not represented in the known skill inventory
- The task scope, after decomposition, is too large to be atomic — splitting it further would violate the feature's acceptance criteria granularity

**Context snapshot must contain:**

- Task spec (what the Task Owner Agent defined)
- Task-level AC (current state)
- Feature spec (read-only reference — not editable, but needed for intent checking)
- UI artefact reference (for context conflict detection)
- Environment contract template — what fields are expected
- Skill inventory — to check whether required skills exist

**Reviewer:** QA Agent Definition — same agent as Zone 2, different artefact type.[^10_2]

***

## Zone 4 — Task Execution

Zone 4 had the most developed uncertainty model before this redesign, since the original sub-flow lived here. The failure modes are the most concrete and technical.[^10_2]

**Most common uncertainty types — Task Performer Agent:**

- Environment verification fails — the environment state does not match the environment contract captured at claim time
- A tool required by the task is unavailable, returns unexpected output, or behaves differently than the task spec assumed
- The context package is internally consistent but insufficient — a decision is required that the context package does not resolve
- The proof of completion format is ambiguous — the task spec describes what to do but not what output format constitutes literal proof
- Two items in the context package contradict each other — the conflict rule fires[^10_1]
- A dependency output from a prior task (referenced in context) is stale or has changed since the context was curated

**Most common uncertainty types — mid-execution (not environment):**

- An implementation path that satisfies one acceptance criterion would violate another
- The task encounters an edge case not covered by any acceptance criterion or test — the agent cannot proceed without a decision about whether to handle it or raise it
- A required API, schema, or service endpoint has changed since the context package was assembled

**Context snapshot must contain:**

- Context package (the curated, approved package — this is the Task Performer's only authorised read source)[^10_1]
- Environment contract (the snapshot taken at claim time)
- Uncertainty log for this task (all prior uncertainties, including resolved ones — this travels with the task)
- Tool output / error log (the literal captured output that triggered the uncertainty)

**Note:** The Zone 4 Advisor Agent has the highest token budget of any Advisor Agent — the context package alone can be substantial, and the tool output / error log may be verbose. This was flagged in the context tree as justified by the uncertainty resolution scope.[^10_1]

**Reviewer:** QA Agent Execution — already the Zone 4 quality gate.[^10_2]

***

## Zone 5 — Feature Delivery

Zone 5 uncertainties are the newest category, following the decision to bring CICD into the domain. The failure modes here are infrastructure and integration-level rather than specification-level.

**Most common uncertainty types — CICD Agent:**

- Integration tests produce non-deterministic results — same code, different pass/fail on repeated runs
- Staging environment verification fails in a way that cannot be attributed to the deployed code — environment configuration issue vs. application issue is unclear
- An integration test fails but the failure appears to be in a test fixture or test data, not the application code
- Staging promotion succeeds but a post-promotion health check returns an unexpected state that was not covered by the staging environment spec
- A production promotion is blocked by an external dependency (upstream service, certificate, DNS) that is outside the deployed code

**Most common uncertainty types — Feature Owner Agent (Zone 5):**

- User testing results are mixed — some criteria clearly pass, others clearly fail, but a subset is genuinely ambiguous about intent
- User testing uncovers a behaviour that is technically within AC but produces a clearly undesirable outcome — the AC was correct but incomplete
- Integration test failure details are insufficient to determine whether the fix belongs in a task revision or a feature spec revision

**Context snapshot must contain:**

- Deployment record (the CICD Agent's append-only artefact — all deployment actions, environment states, exit codes)
- Integration test results (full output, not summary — non-determinism diagnosis requires the raw logs)
- Staging environment spec (what the environment was expected to look like)
- Feature-level AC and success metrics (for intent checking against user testing results)
- Prior uncertainty log at feature level (if any uncertainties were raised in Zone 2 or Zone 3 that remain relevant to delivery)

**Reviewer:** Feature Owner Agent — Zone 5 review authority. For escalation, the FO resolves.[^10_1]

***

## The Pattern Across All Zones

Two uncertainty types appear in almost every zone, just in different forms:[^10_1][^10_2]

- **Conflict between two accepted artefacts** — something upstream was accepted independently, but when combined with another accepted artefact, they contradict each other. This is the context conflict rule. Every Advisor Agent's context snapshot must always include both conflicting artefacts, not just one.
- **Ambiguity that was not detectable at definition time** — the artefact passed its quality gate correctly, but a downstream translation (AC → test, spec → context, code → deployment) reveals an ambiguity that was invisible at the earlier stage. These are the most expensive uncertainties because they require tracing back through the zone boundary to fix the root artefact.

Both of these reinforce why the context snapshot cannot be a summary — it must be the literal artefacts involved, so the Advisor Agent can make a specific, verifiable determination rather than a general recommendation.

<div align="center">⁂</div>

[^10_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^10_2]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md


---

# this discussion helps me see that currently, we don't even ask agents if they are uncertain about what they need to do, they will just attempt it anyway.

How do we build this behaviour? In earlier ideation, we saw the value of having a call-repeat-loop like in aviation, where one agent leaves instructions for the next agent, that agent needs to repeat back what they understand and get that approved before they move on. Is this a good way? Or would it be enough to get the agent to give us a certainty score? Or is it a combination? Or some other way?

This is one of the most important behavioural questions in the whole framework. Let me work through the options properly before making a recommendation.

***

## The Problem Being Solved

Right now, agents attempt work silently when uncertain. The failure mode is not that agents crash — it is that they *produce output* that looks like it satisfies the task but doesn't, because a silent assumption was made at the start. The cost is discovered downstream, not at the point of uncertainty.[^11_1]

This is exactly the failure class the framework was designed to prevent. The Evidence Gate, the Environment Contract, the no-silent-retry principle — all of these address what happens *after* execution. This question addresses what happens *before*.

***

## The Three Options

### Option 1 — Call-Repeat Loop (Aviation CRM Model)

The outgoing agent leaves a structured handoff document. The incoming agent reads it, writes back a plain-language statement of what they understand their job to be, what they will produce, and what assumptions they are making. A reviewer (human or QA agent) must confirm the repeat before work begins.

**Example in practice:**

> *Feature Owner Agent leaves:* "Define three tasks for the login feature. AC is attached. UI artefact is attached."
>
> *Task Owner Agent repeats back:* "I understand I am to define three discrete tasks from this AC. I will produce task-spec.md for each. I am assuming tasks can be executed in parallel — if there are ordering dependencies I am not aware of, I cannot confirm parallelism without more information."
>
> *Reviewer confirms or corrects before Task Owner Agent proceeds.*

**Strengths:**

- Forces the agent to surface hidden assumptions *before* they become embedded in artefacts
- The repeat-back itself is diagnostic — a garbled or incomplete repeat tells you the context package is deficient, before any work has been done
- Mirrors a practice with a strong real-world safety record (aviation, surgical checklists, nuclear operations)
- Consistent with the framework's existing pattern: *context curation before every significant work start*[^11_2]

**Weaknesses:**

- Adds a round-trip to every task handoff — latency cost at every zone boundary
- Reviewer fatigue: if every agent repeats back, the human (or QA agent) reviewing those repeats becomes a bottleneck
- Shallow repeats — an agent can parrot back the instructions without genuine comprehension, producing a repeat that passes but still contains a hidden misunderstanding

***

### Option 2 — Certainty Score

Before beginning work, the agent emits a structured certainty assessment:

```
CERTAINTY SCORE: 7/10
LOW CONFIDENCE AREAS:
  - Whether "response time" in AC means server response or perceived load time
  - Whether the environment contract covers the Redis dependency
PROCEEDING: Yes, with assumptions logged
```

A policy fires on the score: above threshold → proceed, below threshold → RaiseUncertainty automatically.

**Strengths:**

- Low overhead — one structured output, no back-and-forth required for high-confidence tasks
- The threshold creates a consistent, mechanically enforceable gate
- Logged assumptions are traceable — if something goes wrong downstream, the assumption log shows exactly where the agent decided to proceed despite uncertainty
- Agents that score low frequently on a task type are a signal that the context package for that task type is systematically deficient

**Weaknesses:**

- Certainty scores are self-reported — an agent can be confidently wrong. High certainty does not mean correct understanding; it means the agent *believes* it understands. These are not the same thing.
- Threshold calibration is hard. Too low and the pipeline stalls on minor uncertainties. Too high and agents suppress genuine uncertainties to stay above the threshold.
- A score without a repeat-back tells you the agent has a level of confidence but not *what* the agent actually understood — the diagnostic value is limited

***

### Option 3 — Structured Pre-flight Check

Before beginning any significant work, the agent runs a mandatory pre-flight check against its context package. This is not a score and not a full repeat-back — it is a structured checklist the agent completes against declared preconditions:

```
PRE-FLIGHT CHECK — Task Performer Agent
Task: implement-login-form
Context package: loaded ✓
AC item count: 5 ✓
Environment contract: present ✓
All READS files accessible: ✓
Conflicts detected: None ✓
Ambiguities requiring assumption:
  → "response time" — assuming server response time (< 200ms)
    ASSUMPTION LOGGED. Proceeding.
  → Redis dependency not in environment contract
    CANNOT PROCEED. Raising uncertainty.
```

Ambiguities that can be resolved by a reasonable assumption are logged and proceed. Ambiguities that cannot be resolved — missing artefacts, detected conflicts, missing environment state — trigger `RaiseUncertainty` automatically.

**Strengths:**

- Mechanically enforceable — the pre-flight check is a required step in the agent template, not optional
- Distinguishes between *logged assumption* (proceed with trace) and *genuine blocker* (stop and raise)
- Does not add a reviewer round-trip for tasks where the agent's pre-flight is clean
- The assumption log becomes part of the task's artefact trail — reviewers can see what assumptions were made without having to approve them in advance

**Weaknesses:**

- The assumption/blocker distinction requires the agent to self-categorise — a wrong categorisation (treating a blocker as an assumption) is the same failure as no pre-flight at all
- Does not validate *comprehension* — the agent may complete the checklist correctly but still misunderstand the task

***

## Recommendation: Layered Model

No single option covers all failure modes. The right answer is a layered model where the mechanism matches the stakes:

### Layer 1 — Pre-flight Check (mandatory for all agents, all zones)

Every agent runs a structured pre-flight before beginning work. It checks:

1. All declared READS files are present and non-empty
2. No detected conflicts between loaded artefacts (the context conflict rule )[^11_2]
3. The agent can state its job in one sentence consistent with the task spec
4. All preconditions for the current state transition are met

This produces one of three outcomes:

- **CLEAR** — proceed
- **ASSUMED** — proceed with logged assumption(s)
- **BLOCKED** — raise uncertainty before any work begins

This layer catches the mechanical failures: missing context, conflicted artefacts, missing environment state. These are the most common and most preventable failure class.

***

### Layer 2 — Comprehension Repeat-Back (at zone boundaries only)

At each zone boundary — when a new agent class receives a handoff from a different zone — the receiving agent produces a one-paragraph plain-language statement:

> *"I understand my job is to [X]. I will produce [Y]. My assumptions are [Z]. I cannot proceed if [condition] is not met."*

This repeat-back is reviewed by the zone's quality gate agent (QA Agent Definition in Zones 2–3, QA Agent Execution in Zone 4) before the work begins. It does not require FO review for routine handoffs — only if the repeat-back reveals a misunderstanding that the QA agent cannot resolve.

This layer catches *comprehension failures* — where the context is complete and unconflicted but the agent has misread the intent. These are rarer but more expensive because they produce plausible-looking but wrong artefacts.

**Zone boundary crossings in the current framework:**

- Zone 1 → Zone 2: Idea → Feature Owner Agent
- Zone 2 → Zone 3: Feature Owner Agent → Task Owner Agent (at decomposition)
- Zone 3 → Zone 4: Task Performer Agent claims published task
- Zone 4 → Zone 5: All tasks complete → CICD Agent

That is four repeat-backs per feature, at the moments of highest risk — not at every task handoff within a zone.

***

### Layer 3 — Certainty Score (for intra-zone handoffs within Zone 3 and Zone 4)

Within zones where handoffs are frequent and the QA agent is already in the loop (Zone 3's chain from Task Owner → Test Owner → Context Agent, and Zone 4's Task Performer → QA Execution chain), a certainty score replaces the full repeat-back for efficiency:

- Score ≥ threshold: proceed, log score
- Score < threshold: mandatory uncertainty raise before proceeding

The threshold is set per agent class during Zone 0 creation — not globally — because what constitutes "sufficient certainty" differs materially between a Context Agent curating a package and a Task Performer executing code.[^11_2]

***

## How This Connects to the Existing Framework

This layered model slots cleanly into existing structures:


| Layer | Where it lives | What it produces |
| :-- | :-- | :-- |
| Pre-flight check | Base Agent Template — required field in every agent spec | `pre-flight-result.md` or inline to the uncertainty log |
| Comprehension repeat-back | Zone boundary policies — new P_ZB (zone boundary) policy set | `comprehension-statement.md` — reviewed by zone QA agent |
| Certainty score | Agent template — declared threshold, emitted before intra-zone work begins | Score + assumption log appended to the task's uncertainty log |

The pre-flight check becomes **Invariant 10** across all aggregates: *No agent may begin work without a completed pre-flight check. A BLOCKED pre-flight result always triggers `RaiseUncertainty`. It may never be overridden by the agent itself.*

The comprehension repeat-back becomes part of the **context curation cross-cutting pattern** — zone boundary handoffs are now explicitly: *curate context → zone boundary repeat-back → QA confirms → work begins*.[^11_2]

The certainty score becomes a **declared field in the agent template** — alongside READS, WRITES, and NEVER, every agent template declares its `CERTAINTY_THRESHOLD` and what the agent does when it falls below it.

***

## The Aviation Analogy Applied Precisely

The call-repeat loop in aviation works because the co-pilot repeating back "flaps to 15, flaps to 15" is not just confirming they heard the instruction — they are forcing a moment of conscious engagement before an irreversible action. The captain confirming "correct" is not bureaucracy — it is a synchronisation checkpoint before a point of no return.[^11_1]

In this framework, the equivalent moments of no return are:

- Publishing a task (irreversible commitment to execution queue)
- CICD Agent promoting to staging (irreversible deployment)
- CICD Agent promoting to production (irreversible release)

The comprehension repeat-back at zone boundaries is precisely the call-repeat loop — applied at the moments where a misunderstanding would be most expensive to discover and most costly to reverse. Applying it to every intra-zone handoff would be the equivalent of requiring a call-repeat for every checklist item on a routine cruise — the mechanism loses its signal value through overuse.

<div align="center">⁂</div>

[^11_1]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^11_2]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md


---

# how is this implemented in the Nexus MCP tooling?

In Nexus-as-MCP, this behaviour lives in three places: the context tree, the agent specs, and a dedicated uncertainty skill/protocol. The good news is most of the plumbing is already sketched in your docs; we’re just wiring it together into a concrete pattern. [^12_1][^12_2]

***

## 1) Pre‑flight check as a required MCP tool

Implement a single MCP tool that every executor agent must call before doing work, driven by `.framework/context-tree.md` and the agent spec. [^12_1]

- **Tool name (example):** `preflight_check`
- **Inputs:**
    - `agent_name`
    - `task_id` / feature slug
    - paths for declared READS/WRITES/NEVER from the agent’s `.agent.md`
- **Checks it performs:**
    - All declared READS files exist and are non-empty.
    - No conflict between any loaded artefacts (apply the **Context Conflict Rule** from the context tree: when two files disagree, do not average; log and stop). [^12_1]
    - Precondition invariants for the aggregate state (e.g. for Task Performer, task must be `PUBLISHED`, env contract present, etc.). [^12_2]
- **Outputs:**
    - `status` ∈ {`CLEAR`, `ASSUMED`, `BLOCKED`}
    - `assumptions[]` (structured list)
    - `conflicts[]` (if any)
- **Policy:**
    - `CLEAR` → agent may proceed.
    - `ASSUMED` → agent proceeds but assumptions are appended to the task’s `uncertainty-log.md`.
    - `BLOCKED` → agent **must** call `agentraiseuncertainty` and stop. No override in the agent spec.

This directly enforces “don’t just attempt it anyway” in tooling, not in vibes. Every executor’s `.agent.md` template includes a “always call `preflight_check` before main work” block. [^12_1]

***

## 2) Uncertainty as a first‑class MCP skill

Your draft already defines an **uncertainty-protocol** skill and `agentraiseuncertainty` tool, with a schema for what the agent must log. [^12_1] You extend that:

- **Tool:** `agentraiseuncertainty`
- **Inputs (already sketched):**
    - `what` — what is unclear
    - `why` — why it blocks progress
    - `needed` — what information would resolve it
    - `context_paths` — files the agent was reading when it got stuck
- **Behaviour:**

```
- Writes an entry to `.framework/features/<slug>/tasks/<task>/uncertainty-log.md` (or the zone-equivalent) [^12_1]
```

    - Emits `UncertaintyRaised` event into the Observable Stream. [^12_2]
    - Triggers the appropriate **zone Advisor Agent** via MCP (you wire advisor servers as separate MCP servers or tools).
- **Follow‑up tools for Advisor:**
    - `research_uncertainty`
    - `define_mitigation`
    - `review_mitigation`

In Nexus MCP terms, this is just another server with tools; what makes it “behaviour” is that every agent spec includes “on BLOCKED pre-flight, call `agentraiseuncertainty` and yield”.

***

## 3) Certainty score as part of the uncertainty tool, not its own thing

Instead of a separate “certainty score” feature, make certainty one of the fields in the uncertainty protocol / pre-flight output:

- In **pre-flight**, the tool computes a `self_assessed_certainty` (0–1 or 0–10) from the agent’s own reasoning step.
- Policy:
    - If `certainty < threshold` but preconditions are mechanically satisfied, pre-flight returns `ASSUMED` with a required `assumptions[]` list.
    - Threshold is declared per agent in its `.agent.md` (“CERTAINTY_THRESHOLD: 0.8”).

This gives you the benefits of a certainty score (telemetry, trend analysis, routing to human if persistently low) without making it the only gate. A high score never bypasses invariant checks.

***

## 4) Call‑repeat at zone boundaries via MCP “handoff” tools

You already have the **context tree** and VS Code layering model: context cards, skills, prompt files, agent files. [^12_1] To implement call‑repeat at zone boundaries:

- Add a standard MCP tool: `handoff_repeatback`.
- **When it runs:**
    - At four points: Idea→Feature, Feature→Task, Task→Execution, Execution→CICD.
    - Called by the receiving agent as its first action after loading its context card.
- **Inputs:**
    - `handoff_context_paths` (the curated card + key artefacts)
    - `agent_role` (e.g. `TaskOwner`, `TaskPerformer`, `CICDAgent`)
- **Outputs:**
    - `job_statement` — “I understand my job is to…”
    - `deliverable` — “I will produce…”
    - `assumptions[]`
- **Where it goes:**
    - Writes to a small `.framework/.../handoff-repeatback.md` for that boundary.
    - Emits a `HandoffRepeatBack` event on the Observable Stream.
- **Review:**
    - The zone’s QA agent (Definition or Execution) is configured, via its MCP spec, to watch for `HandoffRepeatBack` events and run a lightweight check:
        - If the repeat matches the spec intent → flag as `OK` and let the executor proceed.
        - If not → instruct the executor to raise uncertainty instead of starting work.

In tooling terms, these are just well-named MCP tools plus some routing rules; the “CRM/aviation” behaviour emerges from the combination of:

- “Always call `handoff_repeatback` on cross-zone handoffs”
- “Always call `preflight_check` before execution”
- “Always call `agentraiseuncertainty` on BLOCKED pre-flight or QA not-OK”

***

## 5) Where this lives in the Nexus MCP stack

Concretely, in your VS Code / Nexus MCP setup this looks like: [^12_1][^12_3]

- **Always-on instructions (.github/copilot-instructions.md):**
    - Sanctuary rules, “never proceed on BLOCKED pre-flight”, “always surface and log uncertainties”.
- **Skill files:**
    - `uncertainty-protocol.skill.md` that wraps `agentraiseuncertainty`, `research_uncertainty`, etc.
    - `preflight-check.skill.md` that defines how to call the `preflight_check` MCP tool for this repo.
    - `handoff-repeatback.skill.md` that defines the cross-zone repeat interface.
- **Agent files (.agent.md):**
    - For each agent: a short “Lifecycle” section:
        - Step 1: call `preflight_check`.
        - Step 2: if zone boundary, call `handoff_repeatback`.
        - Step 3: if pre-flight status is BLOCKED or QA marks repeatback as unclear, call `agentraiseuncertainty` and stop.
- **MCP config:**
    - Nexus MCP server exports tools:
        - `environmentsnapshot`, `contextcardgenerate`, `agentaction`, `feedlive`, `agentraiseuncertainty`, `preflight_check`, `handoff_repeatback` as HTTP/STDIO MCP tools. [^12_1][^12_4]
    - Router config (Nexus or client) ensures these tools are available to all relevant agents.

With that, “ask agents if they are uncertain and make them stop instead of guessing” is not a cultural aspiration; it’s literally encoded in the protocol: they cannot transition into “do work” without going through MCP tools that either return CLEAR/ASSUMED or force an uncertainty raise.

Would you like to sketch one concrete `.agent.md` snippet that shows these three steps wired into, say, the Task Performer Agent for your starter template?
<span style="display:none">[^12_10][^12_11][^12_12][^12_13][^12_14][^12_15][^12_16][^12_17][^12_18][^12_19][^12_20][^12_21][^12_22][^12_23][^12_24][^12_25][^12_26][^12_27][^12_28][^12_29][^12_30][^12_31][^12_32][^12_5][^12_6][^12_7][^12_8][^12_9]</span>

<div align="center">⁂</div>

[^12_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^12_2]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md

[^12_3]: https://www.npmjs.com/package/@structured-world/project-nexus-mcp

[^12_4]: https://nexusrouter.com/docs/configuration/mcp

[^12_5]: https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/cells/infrastructure/cell_arch_tooling/

[^12_6]: https://handbook.gitlab.com/handbook/people-group/learning-and-development/level-up/legacy/

[^12_7]: https://handbook.gitlab.com/handbook/total-rewards/benefits/general-and-entity-benefits/inc-benefits-us/total-rewards-processes/

[^12_8]: https://handbook.gitlab.com/handbook/engineering/infrastructure/cost-management/cloud-finops/

[^12_9]: https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-framework/

[^12_10]: https://handbook.gitlab.com/handbook/customer-success/professional-services-engineering/project-mgmt/professional-services-delivery-methodology/release-and-engagement-planning/

[^12_11]: https://handbook.gitlab.com/handbook/engineering/devops/dev/create/engineers/training/

[^12_12]: https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/glql/

[^12_13]: https://handbook.gitlab.com/handbook/security/security-engineering/application-security/runbooks/hackerone-process/

[^12_14]: https://handbook.gitlab.com/handbook/people-group/learning-and-development/gitlab-101/

[^12_15]: https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/observability_logging/

[^12_16]: https://handbook.gitlab.com/handbook/company/culture/all-remote/events/

[^12_17]: https://handbook.gitlab.com/handbook/security/customer-support-operations/docs/zendesk/themes/

[^12_18]: https://handbook.gitlab.com/handbook/company/culture/inclusion/tmrg-tmag/tmrg-gitlab-women/mentorship-program/

[^12_19]: https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/persona-snippets/user-personas/devon/

[^12_20]: https://github.com/tanaikech/nexus-mcp-extension

[^12_21]: https://modelcontextprotocol.io/docs/learn/server-concepts

[^12_22]: https://blog.nexus.xyz/mcp-server-support-on-nexus/

[^12_23]: https://www.youtube.com/watch?v=E2DEHOEbzks

[^12_24]: https://nexusrouter.com/docs

[^12_25]: https://d197for5662m48.cloudfront.net/documents/publicationstatus/307051/preprint_pdf/4b78f8182a230b4025c2f049f5030bde.pdf

[^12_26]: https://github.com/R-Mabasha/nexus-mcp/blob/main/README.md

[^12_27]: https://www.linkedin.com/posts/asimplek_ai-agents-mcp-activity-7417296461756923904-j0B8

[^12_28]: https://arxiv.org/abs/2508.12566

[^12_29]: https://www.anthropic.com/engineering/code-execution-with-mcp

[^12_30]: https://playbooks.com/mcp/esh2n-nexus-data-processor

[^12_31]: https://mcpmarket.com/server/nexus-4

[^12_32]: https://github.com/modelcontextprotocol/servers


---

# yes. sketch the spec

Here’s a lean Task Performer Agent spec that bakes in pre-flight, handoff repeat-back, and uncertainty raising in Nexus MCP terms. [^13_1][^13_2]

***

## Task Performer Agent (.agent.md)

```yaml
---
name: TaskPerformerAgent
description: "Executes a single published task, verifies environment, performs work, and produces proof of completion."
tools:
  - environmentsnapshot          # env contract verification
  - agentaction                  # run commands / code
  - preflight_check              # MCP pre-flight tool
  - handoff_repeatback           # MCP handoff tool
  - agentraiseuncertainty        # uncertainty protocol
  - feedlive                     # write to Observable Stream
model: [gpt-5.1, gpt-4.1-mini]
---

ZONE: 4 Task Execution
TYPE: EXECUTOR
QA_TIER: 2
CERTAINTY_THRESHOLD: 0.8

READS:
  - .framework/features/<feature>/tasks/<task>/task-spec.md
  - .framework/features/<feature>/tasks/<task>/task-ac.md
  - .framework/features/<feature>/tasks/<task>/task-tests.md
  - .framework/features/<feature>/tasks/<task>/context-package.md
  - .framework/features/<feature>/tasks/<task>/environment-contract.md
  - .framework/features/<feature>/tasks/<task>/uncertainty-log.md

WRITES:
  - .framework/features/<feature>/tasks/<task>/proof-of-completion.md

NEVER:
  - feature-spec.md
  - acceptance-criteria.md        # feature-level AC
  - ui-artefact.md
  - sibling task-spec.md
  - sibling context-package.md

SKILL: task-performer
CONTEXT_TREE_REF: context-tree.md#zone-4-task-performer
```


***

## Lifecycle (behavioural rules)

```text
1. On TaskPublished → ClaimTask
   - Precondition: task.status == PUBLISHED

2. On ClaimTask:
   - Load context-package.md and environment-contract.md
   - Call MCP tool: preflight_check
       Input:
         agent_name: TaskPerformerAgent
         task_id: <task>
         reads: [task-spec, task-ac, task-tests, context-package, environment-contract]
       Output:
         status ∈ {CLEAR, ASSUMED, BLOCKED}
         certainty ∈ [0,1]
         assumptions[]
         conflicts[]
   - Append assumptions (if any) to uncertainty-log.md
   - Emit PreFlightChecked event to Observable Stream via feedlive

   - If status == BLOCKED OR certainty < CERTAINTY_THRESHOLD:
       - Call MCP tool: agentraiseuncertainty
           what: description of what is unclear or missing
           why: why it blocks progress
           needed: what information would resolve it
           context_paths: [all READS files]
       - STOP. Do not proceed to VerifyEnvironment.

3. On first entry to Zone 4 (handoff from Zone 3):
   - Call MCP tool: handoff_repeatback
       Input:
         agent_role: TaskPerformerAgent
         handoff_context_paths: [task-spec, task-ac, task-tests, context-package]
       Output:
         job_statement
         deliverable
         assumptions[]
   - Write/append to handoff-repeatback.md
   - Emit HandoffRepeatBack event via feedlive
   - WAIT for QA Agent Execution review:
       - If QA marks repeatback as OK → continue.
       - If QA flags misunderstanding → call agentraiseuncertainty and STOP.

4. VerifyEnvironment:
   - Call environmentsnapshot / environmentverify against environment-contract.md
   - If mismatch:
       - Call agentraiseuncertainty (EnvironmentVerificationFailed case)
       - Emit EnvironmentVerificationFailed event
       - STOP. Task moves to UNCERTAINTYRAISED.

5. PerformTask:
   - With CLEAR pre-flight, OK repeatback, and verified environment, call agentaction
     to execute the task implementation commands.
   - Capture literal command output into proof-of-completion.md
   - Emit TaskPerformed event.

6. SubmitForReview:
   - Ensure proof-of-completion.md is populated.
   - Emit TaskSubmittedForReview event.
   - Yield to QA Agent Execution (no self-review).
```

This is the pattern you can clone for other executor agents: same pre-flight + handoff + uncertainty wiring, different READS/WRITES and zone. [^13_1][^13_2]

What’s the next agent you’d like to sketch — CICD Agent for Zone 5, or a Zone 3 Advisor Agent?

<div align="center">⁂</div>

[^13_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^13_2]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md


---

# let's look at the policy for context curation

This is a good moment to formalise this — context curation is the most load-bearing cross-cutting pattern in the framework, appearing in Zones 2, 3, and 4, and confirmed as essential for Zone 5 [^14_1][^14_2]. It was identified in the session retrospective as a pattern that emerged three times before it was named, which means it was never formally specced as a policy in its own right [^14_2].

***

## The Context Curation Pattern

Every significant work start is preceded by a three-step chain: **curate → review → approve**. No work begins with unreviewed or unapproved context. This is not a guideline — it is a structural invariant enforced by the agent template's READS constraint: no agent may begin work without a `context-package.md` in `APPROVED` status in its READS list [^14_1][^14_2].

***

## Context Curation Policy Across All Zones

### Zone 2 — UI Design Context

| Step | Event | Command | Actor |
| :-- | :-- | :-- | :-- |
| Curate | `FeatureAccepted` | `CurateUIContext` | Context Agent |
| Review | `UIDesignContextCurated` | `ReviewUIContext` | QA Agent Definition |
| Approve | `UIDesignContextReviewed` | `AcceptUIContext` | QA Agent Definition |
| Work begins | `UIDesignContextAccepted` | `DesignUI` | UI Design Agent |

**What the context package contains:**

- Feature spec
- Feature-level AC
- Brand guidelines (full, not summarised)
- Design system / component library reference
- Success criteria from the parent idea

**Curation invariant:** The Context Agent must not summarise or compress any source artefact when producing the UI context package. Compression is lossy — a downstream agent working from a summary of brand guidelines will miss specifics that matter at design time.

***

### Zone 3 — Task Context

| Step | Event | Command | Actor |
| :-- | :-- | :-- | :-- |
| Curate | `TestsAccepted` | `CurateContext` | Context Agent |
| Review | `ContextCurated` | `ReviewContext` | QA Agent Definition |
| Approve | `ContextReviewed` | `ApproveContext` | FO (human gate) |
| Work begins | `ContextApproved` | `PublishTask` | FO |

**What the context package contains:**

- Task spec
- Task-level AC
- Accepted test suite (with expected outputs)
- UI artefact reference (read-only, from Zone 2)
- Feature-level AC (read-only reference — for intent checking only)
- Environment contract template

**Zone 3 note:** The FO approval gate here is the last human checkpoint before a task enters the execution queue [^14_2]. This is intentional — task publication is an irreversible commitment to execution, and irreversible decisions require human authority. The QA Agent Definition reviews for completeness and consistency; the FO approves the decision to commit.

***

### Zone 4 — Execution Context (at claim time)

Zone 4 does not have a separate curation step — the context package was curated and approved in Zone 3. What Zone 4 adds is an **environment contract** captured at claim time, which is appended to the already-approved context. This is not curation — it is a snapshot [^14_2].


| Step | Event | Command | Actor |
| :-- | :-- | :-- | :-- |
| Snapshot | `TaskClaimed` | `VerifyEnvironment` / `environmentsnapshot` | Task Performer Agent |
| Conflict check | Pre-flight | `preflight_check` | Task Performer Agent (via MCP) |
| Work begins | `EnvironmentVerified` + pre-flight `CLEAR` | `PerformTask` | Task Performer Agent |

**Zone 4 curation invariant:** The Task Performer Agent must not supplement its context package with any files outside its declared READS list, even if those files are reachable. Additional context not in the approved package must be requested through the uncertainty protocol, not sourced independently.

***

### Zone 5 — Feature Delivery Context

This is the unconfirmed Zone 5 pattern — the retrospective flagged it as "the cross-cutting pattern predicts yes" but it was never formally resolved [^14_1][^14_2]. With the CICD Agent now inside the domain and the Feature Owner Agent owning user testing, the pattern resolves predictably:


| Step | Event | Command | Actor |
| :-- | :-- | :-- | :-- |
| Curate | `StagingEnvironmentVerified` | `CurateDeliveryContext` | Context Agent |
| Review | `DeliveryContextCurated` | `ReviewDeliveryContext` | Feature Owner Agent |
| Approve | `DeliveryContextReviewed` | `ApproveDeliveryContext` | FO (human gate) |
| Work begins | `DeliveryContextApproved` | `PlanUserTesting` | Feature Owner Agent |

**What the delivery context package contains:**

- Feature-level AC and success metrics
- Integration test results summary
- Staging environment verification record
- User testing plan template
- Prior user testing history (if feature was previously tested and failed)

**Zone 5 note:** The FO approval gate before user testing mirrors the Zone 3 gate before task publication — both are points of irreversible commitment, and both are human decisions [^14_2].

***

### Zone 0 — Agent Creation Context

Consistent with the pattern everywhere else:


| Step | Event | Command | Actor |
| :-- | :-- | :-- | :-- |
| Curate | `GapConfirmed` | `CurateAgentRequirements` | Framework Owner Agent |
| Review | `RequirementsDocumentDrafted` | `ReviewRequirements` | Agent Spec QA |
| Approve (NV ≤ 1) | `RequirementsReviewed` | `ApproveRequirements` | Framework Owner Agent |
| Approve (NV ≥ 2) | `RequirementsReviewed` | `ApproveRequirements` | FO (human gate) |
| Work begins | `RequirementsApproved` | `CommissionSpecTests` | Framework Owner Agent |


***

## The Formal Cross-Cutting Policy

Formalising what was previously only a named pattern:

```
POLICY: ContextCurationBeforeWork (Cross-cutting, all zones)

Whenever a new agent is about to begin significant work in any zone:
  1. A context package specific to that work MUST be curated
     by the Context Agent (or zone-equivalent curator)
  2. The context package MUST be reviewed by the zone's quality gate agent
  3. The context package MUST be approved by the zone's approval authority
     before the working agent may claim or begin their task
  4. No working agent may supplement an approved context package
     with artefacts outside its declared READS list
  5. If curation, review, or approval produces a conflict or rejection,
     the uncertainty protocol fires before work is attempted
```


***

## The Context Agent Spec Sketch

The Context Agent is a Zone 3 curator — but following the curation pattern, it operates in every zone with a zone-specific variant. Here is the Zone 3 spec:

```yaml
---
name: ContextAgent
description: "Curates the minimum necessary approved context package for a task before it is published to the execution queue."
tools:
  - preflight_check
  - agentraiseuncertainty
  - feedlive
  - contextcardgenerate           # assembles the context card
  - patternsearch                 # checks pattern library for similar task types
model: [gpt-5.1, gpt-4.1-mini]
---

ZONE: 3 Task Preparation
TYPE: EXECUTOR
QA_TIER: 2
CERTAINTY_THRESHOLD: 0.85

READS:
  - .framework/features/<feature>/tasks/<task>/task-spec.md
  - .framework/features/<feature>/tasks/<task>/task-ac.md
  - .framework/features/<feature>/tasks/<task>/task-tests.md
  - .framework/features/<feature>/ui-artefact.md
  - .framework/features/<feature>/feature-ac.md          # read-only, intent only
  - AGENTS.md                                            # stack constraints

WRITES:
  - .framework/features/<feature>/tasks/<task>/context-package.md

NEVER:
  - proof-of-completion.md
  - review-result.md
  - sibling task context-package.md
  - feature-spec.md content (reference slug only)
```

**Lifecycle:**

```text
1. On TestsAccepted → CurateContext
   - Call preflight_check
   - If BLOCKED or certainty < threshold → agentraiseuncertainty, STOP

2. Call patternsearch against pattern library:
   - Has a context package for this task type been curated before?
   - If yes: load pattern as starting structure, verify still current
   - If no: curate from scratch using contextcardgenerate

3. Apply Minimum Necessary Rule:
   - Include only what the Task Performer needs to do THIS task
   - Do not include feature-level context beyond what is required
     for intent checking — task performers do not need the full
     feature spec, only their task's AC and approved tests

4. Apply Context Conflict Rule:
   - If any two READS files contradict each other:
     DO NOT average, DO NOT choose one silently
     Log conflict to uncertainty-log.md
     Call agentraiseuncertainty, STOP

5. Write context-package.md
   - Emit ContextCurated event via feedlive

6. Yield to QA Agent Definition for review (no self-review)
```


***

## Key Invariants for Context Curation

These should be added to the Policy Registry as formal invariants:

1. **No agent begins significant work without an APPROVED context package.** A missing or `DRAFT` context package is a failure condition, not a warning — it must block the pre-flight check.
2. **The curator never reviews their own package.** The agent that curates the context is never the agent that approves it.
3. **Compression is prohibited.** Source artefacts may be selected and filtered, but not paraphrased or summarised within the package. Lossy compression of guidelines or constraints is an error class of its own.
4. **The context conflict rule is mandatory.** If any two artefacts in the package contradict each other, the curator stops and raises uncertainty. Proceeding with a known conflict is a framework invariant violation.
5. **Context packages are versioned.** If a source artefact changes after a context package is approved (e.g., AC is revised after context was approved for a task), the package must be invalidated and re-curated. A stale package is treated the same as a missing package.

<div align="center">⁂</div>

[^14_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

[^14_2]: event-storming-session-NbbGJS8yQ0.M4J0MHn24rw.md


---

# let's table this discussion. give me a summary of matters we discussed, the decisions we've made and the artefacts we produced.

Here is the full summary of this session.

***

## Session Summary

**Date:** 3 March 2026
**Participants:** Framework Owner (FO), AI Assistant

***

## Matters Discussed

- Developing the Agent Creation Policy into a human- and agent-readable document with glossary and responsibility tree
- Identifying all policy gaps remaining after the event storming session
- Options and recommendation for the CICD boundary (H13)
- Bringing CICD inside the domain boundary
- Restructuring the Uncertainty sub-flow as a cross-cutting primitive rather than a Zone 4 sub-flow
- Zonal Advisor Agents — one per zone with scoped context
- Uncertainty types and context snapshot requirements per zone
- The behavioural gap: agents attempting work silently when uncertain
- Pre-flight check, call-repeat loop, and certainty score as mechanisms for surfacing uncertainty before execution
- A layered model combining all three mechanisms
- MCP tooling implementation of the behavioural model
- The Task Performer Agent spec as a concrete implementation sketch
- Formalising the context curation cross-cutting policy including the Context Agent spec

***

## Decisions Made

### Terminology

- **"Pete" is now "Framework Owner (FO)"** across all documents. All prior document references to "Pete" should be updated on next revision.


### H13 — CICD Boundary

- **CICD is brought inside the domain.** The CICD Pipeline, Staging Environment, and Production Environment move from pink external system stickies to a domain actor: **CICD Agent**.
- `StagingEnvironmentVerificationFailed` is now a domain failure. P5.08 resolves: failure routes to Feature Owner Agent review, consistent with every other failure in the framework.
- H13 is **resolved**. Zone 5 implementation is no longer blocked.


### Uncertainty Sub-flow

- The Uncertainty sub-flow is **no longer a Zone 4 sub-flow**. It is a **cross-cutting domain primitive** available to all agents in all zones.
- The `UncertaintyRaised` event is independent of any aggregate — it carries a `zone` and `parent-ref` field that routes it correctly.
- The `P4.U` policy numbering is replaced by `P.U` (cross-cutting, all zones).


### Zonal Advisor Agents

- There is **one Advisor Agent per zone** (Zones 0–5), replacing the single Advisor Agent.
- Each Advisor Agent's NEVER list enforces that it cannot read artefacts from other zones.
- The `zone` field on the Uncertainty aggregate is the dispatch key — it determines which Advisor Agent is invoked.
- The **mitigation reviewer is the zone's existing quality gate agent** — no new actors required:
    - Zone 0: FO
    - Zone 1: FO
    - Zone 2: QA Agent Definition
    - Zone 3: QA Agent Definition
    - Zone 4: QA Agent Execution
    - Zone 5: Feature Owner Agent (FO for escalation)
- **P.U6 and P.U7 are resolved** (second rejection path): second rejection → `EscalateToFO` → FO resolves or closes parent work item.


### Agent Naming

- **Advisor Agent → Uncertainty Owner Agent** — owns the Uncertainty aggregate outright, consistent with the naming convention (Feature Owner, Task Owner).[^15_1]
- **Test Writer Agent → Test Owner Agent** — owns the test suite artefact and the ambiguity detection gate.
- QA Agent Definition, QA Agent Execution, Context Agent, UI Design Agent — names unchanged.


### Pre-flight and Uncertainty Behaviour

- **Agents must not attempt work silently when uncertain.** This is enforced by tooling, not convention.
- **A layered behavioural model** is adopted:
    - **Layer 1 — Pre-flight check** (mandatory, all agents, all zones): runs before any work begins; outputs `CLEAR`, `ASSUMED`, or `BLOCKED`.
    - **Layer 2 — Comprehension repeat-back** (zone boundaries only, four points in the lifecycle): receiving agent states what it understands its job to be; reviewed by zone QA agent before work begins.
    - **Layer 3 — Certainty score** (intra-zone handoffs in Zones 3 and 4): declared threshold per agent class; below threshold forces uncertainty raise.
- **`BLOCKED` pre-flight is non-overridable** — the agent cannot proceed and must call `agentraiseuncertainty`.
- **Certainty threshold** is a declared field in every agent template (`CERTAINTY_THRESHOLD:`).


### Context Curation

- Context curation is **formally adopted as a cross-cutting policy** (`POLICY: ContextCurationBeforeWork`), not just a named pattern.
- The pattern is confirmed in **all six zones** including Zone 5 (DeliveryContext before PlanUserTesting) and Zone 0 (RequirementsDocument before CommissionSpecTests).
- **Five formal invariants** govern context curation across all zones: no work without an APPROVED package; curator never reviews their own package; compression is prohibited; context conflict rule is mandatory; packages are versioned and invalidated on source change.


### Zone 5 Policy Set

- P5.01–P5.09 are now complete with the CICD Agent as a first-class domain actor.
- P5.08 resolved (see H13 above).
- The CICD Agent's artefact is `deployment-record.md` — the Zone 5 equivalent of `proof-of-completion.md`.
- **FO retains emergency authority** via `HaltDelivery` command, which transitions any Feature to `DELIVERY_HALTED`.


### Zone 0 Policy Set

- Zone 0 now has a **draft policy set** (P0.01–P0.08) covering the full agent creation cycle.
- A **Zone 0 Uncertainty Owner Agent** is added, scoped to framework-level artefacts only.

***

## Artefacts Produced

| Artefact | Status | Notes |
| :-- | :-- | :-- |
| **Agent Creation Policy v0.1** | Draft | Full document — glossary, responsibility tree, 7-step creation flow, NV/BR scoring, QA tier table, Base Agent Template, bootstrapping exception |
| **Policy Gap Inventory** | Complete | 8 gaps identified, sourced, and prioritised with blocking status |
| **H13 CICD Boundary Analysis** | Complete | Three options documented; Option 3 (hybrid) recommended; superseded by FO decision to bring CICD fully inside domain |
| **CICD Agent Spec (outline)** | Draft | Job statement, write authority by Feature state, read model, new invariants, Zone 5 policy table P5.01–P5.09 |
| **Uncertainty Sub-flow Redesign** | Draft | Cross-cutting aggregate design, P.U1–P.U7 policy set, Uncertainty aggregate artefacts and state machine |
| **Zonal Advisor Agent Model** | Draft | One Advisor Agent per zone (0–5), zone-scoped context, reviewer-by-zone table |
| **Uncertainty Types \& Context Snapshots by Zone** | Complete | Full analysis for Zones 0–5 — common uncertainty types and required context snapshot contents |
| **Layered Pre-flight / Uncertainty Behaviour Model** | Draft | Layer 1 (pre-flight), Layer 2 (repeat-back), Layer 3 (certainty score) — with aviation analogy applied precisely |
| **MCP Tooling Implementation Design** | Draft | `preflight_check`, `handoff_repeatback`, `agentraiseuncertainty` tool specs; VS Code skill/agent/prompt file placement |
| **Task Performer Agent Spec** | Draft | Full `.agent.md` sketch including READS/WRITES/NEVER, CERTAINTY_THRESHOLD, and lifecycle with all three behavioural layers wired in |
| **Context Curation Cross-Cutting Policy** | Draft | Formal policy statement, per-zone curation tables (Zones 0–5), Context Agent Zone 3 spec, five formal invariants |


***

## Open Items Carried Forward

| Item | Priority | How to resolve |
| :-- | :-- | :-- |
| Zone 5 Event Storming session | High — CICD Agent is now inside the domain, session will be more productive | Dedicated session: storm CICD Agent events, deployment record spec, rollback policy |
| Uncertainty Sub-flow Event Storming session | High | Storm the Uncertainty aggregate as a standalone domain across all six zones with Zonal Advisor Agents |
| Zone 0 Policy Registry | Medium | Write the formal document equivalent to Policy Registry v0.1 for Zone 0 |
| Task retry limits (Gap 6) | Medium | Add to Policy Registry; likely surfaces in Uncertainty Sub-flow session |
| FO unavailability handling (Gap 7) | Medium | Policy decision: formalise `AWAITING_FO` as a Feature aggregate state |
| Idea prioritisation policy (Gap 8) | Low | Short decision; add P1.02 to Policy Registry |
| CICD Agent Zone 0 creation cycle | When ready to build | NV Score 2, BR Score 3 → QA Tier 3; first real test of the Zone 0 process |
| Update all documents to replace "Pete" with "FO" | On next revision | Apply globally to all specs, policies, and domain maps |
| Remaining agent specs | When ready to build | Uncertainty Owner Agents (×6), CICD Agent, Zone 5 Context Agent, remaining Zonal Advisor Agents |

<div align="center">⁂</div>

[^15_1]: continuing-on-from-the-event-s-JyBjI3OZSCeqGeN4mkS3YA.md

