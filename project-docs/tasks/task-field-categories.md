# Task field categories

Finding the structural patterns across contract elements dramatically reduces the cognitive and computational cost of instantiating any individual task contract.

***

## Category 1 — Foundational Governance References

*Elements that point to org-wide or protocol-level policy documents. The task contract stores a reference and version number only. The policy lives elsewhere and is maintained independently.*

- Governing protocol and ruleset version (Preamble)
- Jurisdiction declaration
- Performer safety guidelines
- Confidentiality handling obligations and data retention requirements
- Regulatory / compliance obligations
- Dispute resolution mechanism and escalation path
- Compensation and incentive ruleset
- Reputation system reference
- Immutability protocol specification
- Knowledge building guidelines
- Retrospective format guidelines
- Notification ruleset
- Quality guidelines
- Task valuation framework

***

## Category 2 — Ruleset-Determined Values

*Elements whose value is computed or classified by applying a defined ruleset to inputs. The task contract stores the result and the ruleset version used to produce it. Rules can be updated without changing every contract.*

- Complexity rating (inputs: task type, unknowns, interdependencies)
- Cognitive load type (inputs: work nature, domain, output type)
- Time sensitivity classification (inputs: deadline proximity, value decay profile)
- Priority score (inputs: value, urgency, risk, strategic alignment, dependency count)
- Priority classification — must-have through won't-have
- Value decay profile (inputs: task type, deadline type, market conditions)
- Blast radius classification (inputs: downstream dependency count, affected actor scope)
- Reversibility classification (inputs: output type, affected systems)
- Risk tier (inputs: likelihood × severity matrix)
- Experience level requirement (inputs: complexity, domain specificity, trust requirement)
- Approval requirement tier (inputs: blast radius + reversibility)
- Flow potential rating (inputs: complexity vs performer capability match)
- Leverage score (inputs: strategic alignment, dependency centrality, effort estimate)
- Reputation impact (inputs: task tier, quality achieved, timeliness)
- Waste classification (inputs: value stream linkage, outcome contribution traceability)

***

## Category 3 — Inherited from Parent Entities

*Elements that default to the value set at a parent level (goal, project, initiative, process, contract) unless explicitly overridden at the task level. Reduces redundant specification.*

- Strategic linkage (parent goal / OKR / initiative ID)
- Value stream position
- Outcome contribution statement (inherits direction, task refines specifics)
- Confidentiality classification (inherits from parent project or engagement)
- Governing jurisdiction (inherits from organisational or DAO default)
- Compliance obligations (inherits from parent regulatory context)
- Stakeholder list (inherits from parent project, task may add specifics)
- Notification recipients (inherits from parent, task may extend)
- Compensation type and mechanism (inherits from engagement or role contract)
- Governing ruleset versions (inherits from parent, unless task-specific override)
- Dispute resolution path (inherits from parent engagement or protocol)
- Knowledge base destination (inherits from parent project or domain)
- Retrospective trigger conditions (inherits from parent process or programme)
- Audit and immutability protocol (inherits from organisational or DAO standard)
- Tag taxonomy (inherits parent's mandatory tags, task adds specifics)

***

## Category 4 — Always Unique

*Elements that are necessarily distinct for every task contract instance. Cannot be templated, inherited, or computed — they must be authored.*

- Contract identifier (generated)
- Task title
- Task description
- Originating desire statement
- Problem / gap description
- Current state description
- Desired future state description
- Scope inclusions and exclusions
- Assumptions
- Definition of done (acceptance criteria text)
- Expected outputs (specific artefact list)
- Handoff specification (recipient, format, timing)
- Input resource list (specific to this task)
- Dependency list (specific task contract IDs)
- Earliest start condition / pre-conditions checklist
- Due date and deadline type
- Requester ID and requester desire statement
- Performer ID (populated on claiming)
- Claim timestamp
- Proof of completion submissions (artefact hashes, references)
- Actual effort recorded
- Actual outcome recorded
- Outcome variance
- Retrospective notes
- Audit trail entries
- Signatures and commitment timestamps
- Final contract hash

***

## Category 5 — Always From a Constrained Value Set (Enumerations)

*Elements that must be one of a defined set of values. These are stable enough to enumerate in a schema. They require no computation — just selection.*

- Contract status
- Contract type (one-off, recurring, ad hoc)
- Creation source (human-initiated, process-triggered, agent-generated, event-triggered)
- Work nature / task type
- Functional domain
- Value stream category (value-creating, enabling, protecting, discovering, waste)
- Value type (financial, operational, strategic, relational, informational)
- Cognitive load type
- Focus mode requirement (yes/no)
- Deadline type (hard, soft)
- Recurrence type (once, scheduled, ad hoc)
- Allocation mechanism (assigned, claimable, auctioned, delegated, automated)
- Performer type (human, agent, hybrid)
- Dependency type (hard, soft, informational)
- Lifecycle status (draft through archived)
- State transition authority type
- Risk type categories
- Reversibility (reversible, partially reversible, irreversible)
- Blast radius level
- Risk tier (1–4)
- Quality levels (poor, satisfactory, great, excellent)
- Confidentiality classification
- Compensation type
- Verification independence requirement (yes/no)
- Knowledge output type
- Skill development opportunity (yes/no)
- Review type (quality, compliance, safety, domain expertise)
- Stakeholder input rights (none, advisory, approval)

***

## Category 6 — Template-Provided Defaults

*Elements that are pre-populated by a task template and accepted as-is for common task types. The human or agent reviews and confirms rather than authors. Overridable but rarely need to be.*

- Complexity rating (for well-understood recurring task types)
- Cognitive load type
- Estimated effort (statistical average from historical task instances)
- Estimated lead time
- Required skills, knowledge domains, and tools (for typed task templates)
- Standard acceptance criteria (e.g. "invoice reviewed" always requires the same three criteria)
- Standard artefact types and formats
- Verification method per artefact type
- Notification trigger defaults
- Risk register (standard risks pre-populated for task type)
- Safety obligations (standard obligations for task category)
- Quality criteria per output type
- Retrospective trigger conditions
- Knowledge output flag and type

***

## Category 7 — Computed at Runtime

*Elements that are automatically calculated from other fields at the moment of contract instantiation or state transition. No human input required.*

- Priority score (formula applied to value, urgency, risk, dependencies)
- Leverage score (computed from dependency graph centrality + strategic alignment)
- Context switch cost (computed from task type + current assignee workload state)
- Zeigarnik weight (computed from time open + visibility + assignee load)
- Bottleneck flag (computed from count of downstream tasks blocked by this one)
- Claim window open/close timestamps (computed from earliest start + due date)
- Estimated lead time (computed from effort estimate + historical queue wait data)
- Deferral count (auto-incremented on each postponement)
- Completion proof hash (generated on artefact submission)
- Final contract hash (generated on completion and signing)
- Value decay urgency signal (computed from decay profile + time elapsed)
- Reputation delta (computed from quality achieved + timeliness + task tier)

***

## Category 8 — Human Confirmation Required (AI-Proposed, Human-Approved)

*Elements where AI can generate a high-quality draft or recommendation, but a human must consciously confirm before the contract is valid. These carry accountability, ethical weight, or contextual nuance that should not be fully automated.*

- Originating desire statement
- Outcome contribution statement
- Definition of done (AI drafts from task type + context, human confirms)
- Scope exclusions (AI proposes based on template, human confirms)
- Risk register (AI pre-populates from task type, human reviews and signs off)
- Safety risk assessment (AI flags, human confirms or escalates)
- Requester commitment signature
- Performer commitment signature (on claiming)
- Value declaration (AI estimates, human confirms before publishing)
- Dispute resolution initiation
- Cancellation with downstream consequence
- Retrospective notes (AI summarises, human reviews)
- Task validated assessment (AI proposes, human confirms)

***

## The Efficiency Architecture This Creates

Mapping these categories together reveals a **tiered instantiation model**:

| Tier | What Happens | Human Effort |
|---|---|---|
| **1 — Select template** | Category 6 defaults pre-populate ~40% of contract | Near zero |
| **2 — Inherit from parent** | Category 3 values flow down automatically | Near zero |
| **3 — Confirm enumerations** | Category 5 values reviewed and selected | Seconds per field |
| **4 — Runtime computation** | Category 7 values calculated automatically | Zero |
| **5 — Author unique elements** | Category 4 fields drafted (AI-assisted) and confirmed | Minutes |
| **6 — Governance references** | Category 1 references resolved automatically from context | Zero |
| **7 — Ruleset evaluation** | Category 2 values computed and surfaced for review | Seconds to review |
| **8 — Human confirmation** | Category 8 items reviewed and signed | Focused human attention |

For a well-typed, routine task using a mature template — an invoice review, a blog post, a bug fix — the human touch points collapse to: *confirm the unique description, review the AI-drafted DoD, and sign the commitment*. Everything else is inherited, computed, or defaulted.

The complexity doesn't disappear. It is **absorbed by the system**, surfaced only when it matters, and always traceable when accountability requires it.
