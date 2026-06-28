<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## What System Stories Are

System stories sit below user and agent stories. They represent what the platform does autonomously — state transitions, validation guards, calculations, persistence, audit events, and recovery behaviors. They require no LLM and no user action. Most are candidates for fully deterministic implementation.

***

## Stage 1: System Stories

- As the system, I need to create a TaskSession record with status `clarifying` immediately on raw description submission so that the session exists as a durable entity before any agent processing begins.
- As the system, I need to validate that the raw description meets a minimum length and is not empty before allowing submission so that the Session Agent receives meaningful input.
- As the system, I need to persist the refined description and inferred fields (domain, stakeholder context, risk tolerance) as a draft update to TaskSession before presenting them to the user so that the session is recoverable if the user closes before confirming.
- As the system, I need to lock the refined description and transition session status to `clarifying` only after the user explicitly confirms it so that no inferred field is treated as accepted without acknowledgment.

***

## Stage 2: System Stories

- As the system, I need to persist each ClarificationAnswer record immediately on submission so that session state is never dependent on browser memory.
- As the system, I need to enforce that all required questions have answers before allowing progression to `outcomes_draft` so that the Outcomes Agent never operates on insufficient input.
- As the system, I need to allow the user to navigate back to any previous question and overwrite the existing ClarificationAnswer record so that earlier mistakes can be corrected without restarting the session.
- As the system, I need to recalculate the progress indicator after each answer so that the user sees an accurate count of remaining questions at all times.
- As the system, I need to emit a `clarification_complete` event when the Clarification Agent signals sufficient coverage so that the transition to Stage 3 is triggered without polling.

***

## Stage 3: System Stories

- As the system, I need to block the transition from `outcomes_draft` to `outcomes_approved` until every Outcome record has a status of either `approved` or `rejected` so that no outcome can be silently carried forward.
- As the system, I need to prevent progression if zero outcomes have been approved so that the decomposition stage never runs on an empty outcome set.
- As the system, I need to record a modification timestamp and set `source` to `user_modified` on any Outcome the user edits so that the difference between agent-generated and user-modified records is permanently traceable.
- As the system, I need to validate that every approved Outcome has a non-empty input_template and output_template before allowing stage transition so that the decomposition agent always has schema contracts to map against.

***

## Stage 4: System Stories

- As the system, I need to calculate the composite risk score using the defined weighted formula whenever any axis score is created or updated so that the displayed rank always reflects the current scores without requiring a manual recalculation step.
- As the system, I need to re-rank all Risk records by composite score descending after any score change so that the ranked list is always current.
- As the system, I need to automatically set a `requires_human_gate` flag on any Risk record with a reversibility score above 7 so that irreversible risks are structurally surfaced before the decomposition stage.
- As the system, I need to block the transition from `risks_draft` to `risks_approved` until every Risk record has a status of `approved` or `rejected` so that no unreviewed risk enters the decomposition analysis.
- As the system, I need to prevent progression if zero risks have been approved so that the decomposition agent always has a risk set to map against subtasks.
- As the system, I need to record a modification timestamp and set `source` to `user_modified` on any Risk record the user edits so that scoring calibration adjustments are traceable.

***

## Stage 5: System Stories

- As the system, I need to calculate the `weighted_delta` on each SubtaskPropertyScore record whenever human_score, agent_score, or importance_weight is set so that aggregate scores are always derivable from current values.
- As the system, I need to calculate `aggregate_human_score` and `aggregate_agent_score` on each Subtask as weighted averages of its SubtaskPropertyScore records so that executor recommendation logic has a numeric basis.
- As the system, I need to apply the executor recommendation threshold rule deterministically — if `aggregate_agent_score` exceeds `aggregate_human_score` by more than a defined threshold, recommend `agent`; if reversed, recommend `human`; within threshold, recommend `collaborative` — so that recommendations are consistent and auditable.
- As the system, I need to set `requires_human_gate` to true on any Subtask with `reversibility_class` of `irreversible` so that gate placement is structurally enforced, not only agent-recommended.
- As the system, I need to block the transition from `decomposition_draft` to `decomposition_approved` until every Subtask has a status of `approved` or `rejected` so that no subtask is carried forward without explicit user acknowledgment.
- As the system, I need to generate the structured session summary as a read-only artifact on transition to `complete` so that the output is permanently available without requiring a re-run.
- As the system, I need to transition session status to `complete` only when all subtasks are actioned and the user explicitly confirms the full decomposition so that completion is a deliberate act.

***

## Cross-Cutting System Stories

These apply across all stages.

**Audit trail**

- As the system, I need to write an immutable audit event for every state transition, entity creation, entity modification, and user approval so that the full session history is permanently traceable.
- As the system, I need to record the actor type (`user` or `agent`), entity type, entity ID, previous value, and new value on every audit event so that any output can be traced back to every decision that contributed to it.

**Session recovery**

- As the system, I need to persist the current stage and last completed step so that a returning user is returned to exactly where they left off without data loss.
- As the system, I need to detect incomplete sessions older than a defined threshold and surface them to the user on next login so that abandoned analyses are not silently lost.

**Stage transition guards**

- As the system, I need to enforce that each stage's completion condition is met before the next stage's agent is invoked so that no downstream agent operates on incomplete upstream data.
- As the system, I need to prevent backward navigation to a completed and locked stage without explicit user intent to re-open it so that approved decisions are not accidentally overwritten.

**Progress state**

- As the system, I need to expose the current session status and completion percentage to the UI at all times so that the user always knows where they are in the process.

**Error and failure handling**

- As the system, I need to catch any agent failure and persist the session at its last valid state so that an agent error does not corrupt or lose user work.
- As the system, I need to surface agent failures to the user with a recoverable action (retry or continue manually) so that the session is never silently blocked.

***

## Deterministic Action Opportunities

These are operations where an LLM adds no value. Each should be implemented as pure logic.


| Action | Stage | Rule |
| :-- | :-- | :-- |
| Composite risk score calculation | 4 | Fixed weighted formula — no inference needed |
| Risk re-ranking | 4 | Sort descending by composite_score |
| Irreversibility gate flag on Risk | 4 | `reversibility_score > 7 → requires_human_gate = true` |
| Irreversibility gate flag on Subtask | 5 | `reversibility_class = irreversible → requires_human_gate = true` |
| Executor recommendation | 5 | Score delta against defined threshold bands |
| Weighted delta on SubtaskPropertyScore | 5 | `importance_weight × (human_score − agent_score)` |
| Aggregate human/agent score on Subtask | 5 | Weighted average of property scores |
| Stage transition guard | All | All entities in stage must be `approved` or `rejected` |
| Zero-approval block | 3, 4, 5 | At least one entity must be `approved` to proceed |
| `source` field assignment | 3, 4, 5 | `user_modified` if any field edited after agent generation |
| Required question enforcement | 2 | `is_required = true AND answer = null → block progression` |
| Progress indicator calculation | 2 | `answered_count / total_count` |
| Audit event creation | All | On every write operation, no conditions |
| Session summary generation | 5 | Structured assembly of approved records — no generation needed |
| Session status transition | All | State machine with defined allowed transitions only |

The session status state machine in particular should be fully deterministic with no agent involvement:

```
clarifying
  → outcomes_draft       [on: clarification_complete event]
  → outcomes_approved    [on: all outcomes actioned + user confirms]
  → risks_draft          [on: outcomes_approved]
  → risks_approved       [on: all risks actioned + user confirms]
  → decomposition_draft  [on: risks_approved]
  → decomposition_approved [on: all subtasks actioned + user confirms]
  → complete             [on: decomposition_approved]
```

No transition is agent-triggered except `clarification_complete`. Every other transition is a pure system event fired by a deterministic completion condition.

