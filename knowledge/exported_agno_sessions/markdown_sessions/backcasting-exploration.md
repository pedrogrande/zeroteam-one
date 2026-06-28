<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## The End State We Are Backcasting From

The session is complete when the user holds a **structured, approved design document** that a technical team can use directly as the foundational specification for agent design, agent team topology, and human-in-the-loop workflow architecture — with every element traceable to an explicit user decision, and no design choice made by default.

Everything below is derived by asking: *what must be true at the end of the previous stage for this end state to be achievable?*

***

## Stage 5: Decomposition — Definition of Done

**Backcasting logic:** The session summary is only useful if every subtask has a confirmed executor, every gate is structurally justified, and every risk and outcome is mapped. If any subtask is missing a mapping, the summary has gaps. If any gate lacks a rationale, it will be challenged or bypassed. If the executor recommendation has no scoring basis, the user has no reason to trust it.

**Definition of Done**

- Every subtask has status `approved` or `rejected` — none pending
- Every approved subtask has a confirmed `recommended_executor`, a `reversibility_class`, and a `friction_type`
- Every approved subtask that is irreversible has `requires_human_gate = true` with a non-empty `human_gate_rationale`
- Every approved subtask has at least one SubtaskOutcomeMap record and at least one SubtaskRiskMap record
- Every SubtaskRiskMap for a high-composite-score risk has a `recommended_mitigation` that is not `accept`
- `aggregate_human_score` and `aggregate_agent_score` are populated on every approved subtask
- The session summary artifact has been generated and is non-empty
- Session status is `complete`

**Required Inputs**


| Input | Source | Must be true |
| :-- | :-- | :-- |
| All approved Outcomes with input/output templates | Stage 3 | Non-empty, schema complete |
| All approved Risks with composite scores and reversibility flags | Stage 4 | Ranked, all actioned |
| Clarification answers | Stage 2 | All required questions answered |
| Session domain, stakeholder context, risk tolerance | Stage 1 | Confirmed by user |

**Required Outputs**


| Output | Consumer |
| :-- | :-- |
| Approved Subtask list with sequence, executor, gate, friction, reversibility | Session summary; future agent specification |
| SubtaskOutcomeMap records | Traceability; summary |
| SubtaskRiskMap records with mitigation recommendations | Gate design; HITL placement |
| SubtaskPropertyScore records (if used) | Executor recommendation audit trail |
| Session summary document | User; technical team; template library |

**Supporting Templates and Mechanisms**

- **Subtask review card** — displays subtask title, description, executor recommendation + rationale, reversibility class, friction type, gate flag, mapped outcomes, and mapped risks on a single card for user review. No scrolling to adjacent entities required.
- **Outcome coverage check** — system validates that every approved Outcome appears in at least one SubtaskOutcomeMap before allowing stage completion. Uncovered outcomes are surfaced as a blocker with a suggested resolution.
- **Risk coverage check** — system validates that every approved Risk with composite score above a defined threshold appears in at least one SubtaskRiskMap. High-priority risks with no subtask mapping are flagged as a gap.
- **Gate justification prompt** — for every subtask where `requires_human_gate = true`, the system requires the user to read the rationale and confirm it is correct before approving the subtask, preventing rubber-stamp gate approval.
- **Executor challenge prompt** — when the user changes an executor recommendation, the system asks them to select a reason from a defined set (`agent_capability_insufficient`, `human_judgment_required`, `policy_requirement`, `preference`, `other`) so the override is structured data, not a silent edit.
- **Session summary template** — structured document with fixed sections: task description, approved outcomes with templates, ranked risk register, subtask sequence table with executor and gate assignments, and a full traceability matrix. Generated deterministically from approved records.

***

## Stage 4: Risk Identification — Definition of Done

**Backcasting logic:** The decomposition agent needs a prioritised, categorised, reversibility-classified risk set to map against subtasks. If risks are uncategorised, the mapping lacks signal. If scoring is not rationale-backed, users will adjust scores arbitrarily, making the ranking unreliable. If irreversible risks are not flagged before decomposition, gate placement becomes a retrofit.

**Definition of Done**

- Every Risk has status `approved` or `rejected` — none pending
- At least one Risk is approved
- Every approved Risk has composite_score calculated from five raw axis scores
- Every approved Risk has a non-empty plain-language rationale for each axis score
- Every approved Risk has a `mitigation_notes` value
- Every Risk with `reversibility_score > 7` has `requires_human_gate = true`
- All approved Risks are ranked by composite_score descending
- Session status is `risks_approved`

**Required Inputs**


| Input | Source | Must be true |
| :-- | :-- | :-- |
| All approved Outcomes | Stage 3 | At least one approved, templates complete |
| Clarification answers — failure modes, stakeholders, constraints | Stage 2 | Failure mode questions answered |
| Session domain and stakeholder context | Stage 1 | Confirmed |

**Required Outputs**


| Output | Consumer |
| :-- | :-- |
| Ranked Risk register with composite scores and axis breakdowns | Decomposition Agent; user review |
| Reversibility-flagged risks with human gate markers | Gate placement in Stage 5 |
| Mitigation notes per risk | SubtaskRiskMap recommended_mitigation in Stage 5 |
| User modification record (source field) | Pattern improvement loop |

**Supporting Templates and Mechanisms**

- **Risk scoring card** — presents each axis score with a plain-language label and a one-sentence rationale. User can adjust the score with a slider, and the rationale updates to reflect the adjustment. Composite score recalculates in real time.
- **Axis explainer tooltips** — for each of the five axes, a persistent tooltip defines what a score of 1, 5, and 10 means in plain language so the user has a calibration reference when agreeing or disagreeing with the agent's score.
- **Reversibility warning banner** — when a risk has `reversibility_score > 7`, a banner appears on the card reading: *"This risk involves actions that cannot be undone. A human approval gate will be required at any subtask that carries it."* User must acknowledge before approving.
- **Risk addition template** — when a user adds a risk, a structured form collects: title, description, category (dropdown), and an optional prompt that asks *"What would have to go wrong for this risk to materialise?"* to produce a useful description rather than a vague label.
- **Minimum risk coverage prompt** — if the user rejects all agent-generated risks in a category (e.g. rejects all `stakeholder_harm` risks), the system surfaces a confirmation: *"You have no approved risks in [category]. Is that correct for this task?"* preventing inadvertent gaps.

***

## Stage 3: Ideal Outcomes — Definition of Done

**Backcasting logic:** The Risk Agent needs concrete success criteria to generate meaningful, task-specific risks. Generic outcomes produce generic risks. The Decomposition Agent needs input/output templates to map subtasks to deliverables. Without schema contracts at this stage, the session summary has no I/O specification. If the user has not genuinely engaged with outcomes, every downstream decision rests on an unexamined foundation.

**Definition of Done**

- Every Outcome has status `approved` or `rejected` — none pending
- At least one primary Outcome is approved
- Every approved Outcome has a non-empty `input_template` with at least one defined field
- Every approved Outcome has a non-empty `output_template` with at least one defined field and a defined format
- Every approved Outcome has a confirmed `outcome_type` (`primary`, `secondary`, or `constraint`)
- Outcomes are ranked by sequence
- Session status is `outcomes_approved`

**Required Inputs**


| Input | Source | Must be true |
| :-- | :-- | :-- |
| Refined task description | Stage 1 | User-confirmed |
| All ClarificationAnswers — success criteria, context, stakeholders | Stage 2 | All required questions answered |
| Inferred domain and stakeholder context | Stage 1 | Confirmed |

**Required Outputs**


| Output | Consumer |
| :-- | :-- |
| Approved Outcome list with types and sequence | Risk Agent; Decomposition Agent |
| Input templates per outcome | Decomposition Agent; session summary |
| Output templates per outcome | Decomposition Agent; session summary; future agent primitive contracts |
| User modification record | Pattern improvement loop |

**Supporting Templates and Mechanisms**

- **Outcome review card** — presents outcome title, description, type label, and a collapsible section for input/output templates. User can approve, edit, or reject inline without leaving the card.
- **Template field builder** — for each input/output template, a simple field-by-field form: field name, type (text / number / array / boolean / date / file), required or optional, and an optional description. Produces structured JSON without requiring the user to write JSON.
- **Type explanation prompt** — when the user sees `primary`, `secondary`, and `constraint` labels for the first time, a brief inline explanation appears: *"Primary: the main goal. Secondary: a valuable but non-essential result. Constraint: a boundary the task must operate within."*
- **Gap identification prompt** — after the agent presents its proposed outcomes, the system asks: *"Is there anything this task needs to achieve that isn't listed here?"* before the user can proceed to approval. This is a structured invitation to add missing outcomes, not an optional text field.
- **Outcome-to-description traceability** — for each proposed outcome, the card shows which clarification answers it was derived from, so the user can verify the inference and identify mismatches.

***

## Stage 2: Clarification — Definition of Done

**Backcasting logic:** The Outcomes Agent needs reliable signal on what success looks like, what constraints apply, who the stakeholders are, and what failure would mean. If required questions are skipped or answered superficially, the outcomes will be generic. If question order creates confusion or cognitive overload, answers will be low quality. The quality of every downstream stage depends on the quality of answers collected here.

**Definition of Done**

- All required ClarificationQuestion records have a corresponding ClarificationAnswer with a non-empty value
- At least one answer exists in each of: `context`, `success_criteria`, `failure_modes`, and `stakeholders` categories
- The Clarification Agent has signalled sufficient coverage
- Session status is `outcomes_draft`

**Required Inputs**


| Input | Source | Must be true |
| :-- | :-- | :-- |
| Confirmed refined task description | Stage 1 | User-confirmed, non-empty |
| Inferred domain, stakeholder context, risk tolerance | Stage 1 | Present on TaskSession |

**Required Outputs**


| Output | Consumer |
| :-- | :-- |
| ClarificationAnswer records covering all required categories | Outcomes Agent; Risk Agent |
| Updated session fields if clarification reveals corrections to domain/stakeholder context | TaskSession |
| Completion signal from Clarification Agent | System state machine |

**Supporting Templates and Mechanisms**

- **Question card with why-this-matters note** — each question card includes a one-sentence explanation of why the question is being asked and how the answer will be used. This reduces superficial or random answers by giving the user a stake in answering well.
- **Adaptive branching logic** — the Clarification Agent generates a base question set, but the system suppresses questions made redundant by earlier answers. If the user selects *"internal only"* as stakeholder context, external communication risk questions are skipped automatically.
- **Option + free-text hybrid input** — every `single_select` and `multi_select` question includes an *"Other — describe"* option that opens an inline text field, so users are never forced to choose an imprecise option.
- **Progress bar with category labels** — the progress indicator shows not just percentage complete but which categories have been covered and which remain, so the user can see the shape of what they're building.
- **Answer review screen** — before the stage completes, the user sees all their answers summarised on a single screen with the option to edit any one before proceeding. This is the last chance to correct before the Outcomes Agent runs.

***

## Stage 1: Task Entry — Definition of Done

**Backcasting logic:** Everything downstream depends on the system having an accurate, unambiguous understanding of what the user wants to achieve. If the raw description is misinterpreted and the user doesn't catch it in the refinement step, the error propagates through all five stages. If the domain or stakeholder context is wrong, every agent in the pipeline is working from a false premise.

**Definition of Done**

- `raw_description` is non-empty and meets minimum length (defined threshold)
- `refined_description` is non-empty and has been explicitly confirmed by the user
- `domain`, `stakeholder_context`, and `risk_tolerance` are set on TaskSession
- User has confirmed or corrected all inferred fields
- Session status is `clarifying`

**Required Inputs**


| Input | Source | Must be true |
| :-- | :-- | :-- |
| Raw task description | User | Non-empty, above minimum length |

**Required Outputs**


| Output | Consumer |
| :-- | :-- |
| Confirmed refined description | Clarification Agent |
| Confirmed domain | All downstream agents |
| Confirmed stakeholder context | Risk Agent; Decomposition Agent |
| Confirmed risk tolerance | Risk Agent |
| TaskSession record with status `clarifying` | System state machine |

**Supporting Templates and Mechanisms**

- **Description input with progressive guidance** — the text input field includes placeholder text that prompts for the three elements most useful for downstream processing: *"Describe the task, who it involves, and what a good outcome looks like."* This is not a requirement — it is a scaffold that improves raw input quality without blocking submission.
- **Refinement confirmation card** — presents the agent's refined description alongside the raw input so the user can see what changed and why. Requires an explicit *"Yes, this is correct"* or *"Edit this"* action — no passive timeout or default acceptance.
- **Inferred field confirmation** — domain, stakeholder context, and risk tolerance are presented as labelled tags with brief definitions. Each has an *"Edit"* button that opens a dropdown of alternatives. User must confirm all three before proceeding — not just the description.
- **Minimum length guard** — if the description is below a defined character threshold, the submit button remains disabled and an inline message explains what additional context would help: *"Tell us a bit more about who is involved and what success looks like."*

***

## Cross-Cutting Definition of Done

Regardless of stage, these conditions must hold throughout the entire session:

- Every entity write has a corresponding immutable audit event
- No stage transition has occurred without its preceding stage's completion condition being fully met
- Every `source` field accurately reflects whether the record was agent-generated, user-added, or user-modified
- Every user approval is recorded as a timestamped event with the approving actor
- The session is recoverable to its last confirmed state after any failure
- No agent has been invoked with incomplete upstream inputs

