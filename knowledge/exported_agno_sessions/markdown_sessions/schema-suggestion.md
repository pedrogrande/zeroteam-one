<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I see the main user flow being a series of questions they need to respond to by clicking option buttons or entering custom answers. This way the user is engaged in the process and understands the design throughout.

Let's see the system above as the end goal.

I want to start building the first part - task evaluation and decomposition analysis.

1. User describes a task they would like to recruit agents to help with.
2. An agent asks the User questions about the task to identify success criteria and failure modes.
3. An agent determines ideal outcomes and offers them to the user for modification or gap identification. Input and output templates can be defined, then approved by user.
4. An agent identifies potential risks associated with the task and ranks them after scoring each risk against multiple axes. These are offered to the user to modify or add to.
5. An agent decomposes the task and maps and ranks the ideal outcomes and risks to subtasks to identify recommendations for the ideal subtask executor.

Let's just focus on that. I already know we can make this better, but I want to keep it simple for now.
what would be the data schema for this tool?

Here is the full data schema for the task evaluation and decomposition tool, organised by entity with the relationships and key design decisions called out.

## Entity Overview

```
TaskSession
    ├── ClarificationQuestion (1:many)
    │       └── ClarificationAnswer (1:1)
    ├── Outcome (1:many)
    ├── Risk (1:many)
    └── Subtask (1:many)
                ├── SubtaskOutcomeMap (many:many → Outcome)
                ├── SubtaskRiskMap (many:many → Risk)
                └── SubtaskPropertyScore (1:many) [optional, for detailed analysis]
```


***

## TaskSession

The root entity. Everything else belongs to a session.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `title` | string | User-provided or agent-inferred |
| `raw_description` | text | Exactly what the user typed in step 1 |
| `refined_description` | text | Agent-synthesised after clarification |
| `domain` | string | Agent-inferred (e.g. sales, legal, ops) |
| `stakeholder_context` | enum | `internal_only` `mixed` `external_facing` `regulated` |
| `risk_tolerance` | enum | `low` `medium` `high` — agent-inferred, user-confirmed |
| `status` | enum | See flow states below |
| `created_at` | timestamp |  |
| `updated_at` | timestamp |  |

**Status flow states:**
`clarifying` → `outcomes_draft` → `outcomes_approved` → `risks_draft` → `risks_approved` → `decomposition_draft` → `decomposition_approved` → `complete`

***

## ClarificationQuestion

Questions the agent generates in step 2. Stored so the session is replayable and auditable.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `session_id` | UUID | FK → TaskSession |
| `sequence` | integer | Display and logic order |
| `category` | enum | `context` `success_criteria` `failure_modes` `constraints` `stakeholders` `timeline` |
| `question_text` | text |  |
| `input_type` | enum | `single_select` `multi_select` `free_text` `scale` |
| `options` | JSON | Array of strings — only for select types |
| `is_required` | boolean |  |
| `created_at` | timestamp |  |

## ClarificationAnswer

One record per question per session.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `session_id` | UUID | FK → TaskSession |
| `question_id` | UUID | FK → ClarificationQuestion |
| `selected_options` | JSON | Array of chosen option strings |
| `free_text` | text | For free_text and scale types |
| `created_at` | timestamp |  |


***

## Outcome

Step 3. Each session has multiple outcomes — primary, secondary, and constraints.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `session_id` | UUID | FK → TaskSession |
| `title` | string |  |
| `description` | text |  |
| `outcome_type` | enum | `primary` `secondary` `constraint` |
| `source` | enum | `agent_generated` `user_added` `user_modified` |
| `status` | enum | `proposed` `approved` `rejected` |
| `sequence` | integer | Priority order |
| `input_template` | JSON | Fields, types, required/optional — what this outcome needs as input |
| `output_template` | JSON | Fields, types, format, schema — what the deliverable looks like |
| `user_notes` | text | User modifications or additions |
| `created_at` | timestamp |  |
| `updated_at` | timestamp |  |

**`input_template` and `output_template` structure:**

```json
{
  "fields": [
    { "name": "transcript", "type": "text", "required": true },
    { "name": "attendees", "type": "array", "required": false }
  ],
  "format": "structured_json",
  "schema_notes": "..."
}
```


***

## Risk

Step 4. Scored against five axes; composite score and rank are calculated.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `session_id` | UUID | FK → TaskSession |
| `title` | string |  |
| `description` | text |  |
| `category` | enum | `output_quality` `stakeholder_harm` `process_failure` `data_integrity` `compliance` `trust_erosion` `skill_decay` `other` |
| `source` | enum | `agent_generated` `user_added` `user_modified` |
| `status` | enum | `proposed` `approved` `rejected` |
| `score_severity` | integer (1–10) | How bad if it materialises |
| `score_probability` | integer (1–10) | How likely to occur |
| `score_detectability` | integer (1–10) | 10 = hardest to detect before/during/after |
| `score_reversibility` | integer (1–10) | 10 = fully irreversible |
| `score_scope` | integer (1–10) | Breadth of impact across people and processes |
| `composite_score` | float | Calculated — see formula below |
| `rank` | integer | Calculated — ordered by composite_score descending |
| `mitigation_notes` | text | Agent-suggested mitigation |
| `user_notes` | text |  |
| `created_at` | timestamp |  |
| `updated_at` | timestamp |  |

**Composite score formula:**

```
composite_score =
  (severity × 0.30) +
  (probability × 0.20) +
  (reversibility × 0.25) +
  ((11 − detectability) × 0.15) +
  (scope × 0.10)
```

Reversibility is weighted highest alongside severity because irreversible high-severity risks are the primary structural gate-placement signal. Detectability is inverted so that harder-to-detect risks score higher.

***

## Subtask

Step 5. The decomposed work units, each with an executor recommendation and property analysis.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `session_id` | UUID | FK → TaskSession |
| `title` | string |  |
| `description` | text |  |
| `sequence` | integer | Position in workflow |
| `source` | enum | `agent_generated` `user_added` `user_modified` |
| `status` | enum | `proposed` `approved` `rejected` |
| `reversibility_class` | enum | `read_only` `reversible` `irreversible` |
| `friction_type` | enum | `productive` `unproductive` `mixed` |
| `recommended_executor` | enum | `human` `agent` `collaborative` |
| `executor_rationale` | text | Agent explanation of the recommendation |
| `requires_human_gate` | boolean | Structural — not bypassable |
| `human_gate_rationale` | text | Why the gate is required |
| `aggregate_human_score` | float | Weighted average across property scores |
| `aggregate_agent_score` | float | Weighted average across property scores |
| `user_notes` | text |  |
| `created_at` | timestamp |  |
| `updated_at` | timestamp |  |


***

## SubtaskOutcomeMap

Many-to-many. Each subtask can contribute to multiple outcomes; each outcome can span multiple subtasks.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `subtask_id` | UUID | FK → Subtask |
| `outcome_id` | UUID | FK → Outcome |
| `contribution_type` | enum | `primary_contributor` `secondary_contributor` `dependency` |
| `relevance_score` | integer (1–10) | How directly this subtask drives this outcome |

## SubtaskRiskMap

Many-to-many. Each subtask can introduce, amplify, or mitigate risks.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `subtask_id` | UUID | FK → Subtask |
| `risk_id` | UUID | FK → Risk |
| `relationship_type` | enum | `introduces` `amplifies` `mitigates` |
| `relevance_score` | integer (1–10) | Strength of the relationship |
| `recommended_mitigation` | enum | `agent_handles` `human_gate` `monitoring` `accept` |


***

## SubtaskPropertyScore *(optional)*

The detailed property-level analysis that drives `aggregate_human_score` and `aggregate_agent_score` on Subtask. Keep this table out of v1 if you want to start lean — the aggregates on Subtask are sufficient to drive executor recommendations without it.


| Field | Type | Notes |
| :-- | :-- | :-- |
| `id` | UUID | PK |
| `subtask_id` | UUID | FK → Subtask |
| `property_name` | string | From the 27-property library |
| `property_category` | enum | `cognitive` `output` `behavioural` `scale` `vulnerability` |
| `human_score` | integer (1–10) |  |
| `agent_score` | integer (1–10) |  |
| `importance_weight` | integer (1–10) | How much this property matters for this specific subtask |
| `weighted_delta` | float | Calculated: `importance_weight × (human_score − agent_score)` — positive = human advantage |


***

## Key Design Decisions

**`source` on every agent-generated entity** — distinguishing `agent_generated`, `user_added`, and `user_modified` is essential for the improvement loop. Patterns where users consistently modify or reject agent proposals are the primary signal for template refinement.

**`status` on every proposable entity** — `proposed` / `approved` / `rejected` enforces the user confirmation step structurally. Nothing proceeds to the next stage unless all outcomes and risks in the current stage are either approved or rejected — no silent defaults.

**Scores stored raw, composite calculated** — storing the five raw risk scores separately rather than only the composite preserves the ability to reweight the formula later without re-running the analysis. The composite is a derived column, not a source of truth.

**`requires_human_gate` is a boolean, not a recommendation** — once an irreversible subtask is identified, the gate is structural. This field drives the downstream workflow architecture, not just the display.

**`input_template` and `output_template` as JSON on Outcome** — these become the I/O contracts for the agent primitives library as the platform matures. Storing them here at the analysis stage means the schema is already aligned with the long-term composability model without requiring a separate build now.

