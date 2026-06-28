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