<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# List every step of the workflow we are designing as user stories and agent stories.

Here is the complete workflow as user and agent stories, stage by stage. Each story is written in the standard format and is atomic — one story, one responsibility.

***

## Stage 1: Task Entry

**User Stories**

- As a user, I want to describe my task in plain language so that the system understands what I am trying to achieve without requiring technical knowledge.
- As a user, I want to see my description reflected back to me in a refined form so that I can confirm the system has understood me correctly before proceeding.
- As a user, I want to be able to edit the refined description before it is locked so that any misinterpretation is caught at the start, not discovered later.

**Agent Stories**

- As the Session Agent, I need to receive the user's raw task description and create a TaskSession record with status `clarifying` so that all subsequent entities have a root to attach to.
- As the Session Agent, I need to infer a domain, stakeholder context, and initial risk tolerance from the raw description so that downstream agents have a calibrated starting point rather than defaulting to neutral assumptions.
- As the Session Agent, I need to produce a refined description that synthesises what was written without adding assumptions, and present it for user confirmation before proceeding.

***

## Stage 2: Clarification

**User Stories**

- As a user, I want to be asked one question at a time so that the process feels like a conversation, not a form.
- As a user, I want each question to offer selectable options alongside a free-text option so that I can answer quickly when an option fits and precisely when it doesn't.
- As a user, I want to understand why each question is being asked so that I engage with it genuinely rather than choosing the fastest answer.
- As a user, I want to be able to skip optional questions so that I am not blocked by questions I cannot answer.
- As a user, I want to see a progress indicator so that I know how many questions remain and can pace my engagement.
- As a user, I want to be able to go back and change a previous answer so that a later question doesn't lock in an earlier mistake.

**Agent Stories**

- As the Clarification Agent, I need to generate a sequenced set of questions covering context, success criteria, failure modes, constraints, stakeholders, and timeline so that the outcome and risk agents have sufficient signal to work from.
- As the Clarification Agent, I need to assign each question a category, input type, and option set before presenting it so that the user interface can render it correctly without additional logic.
- As the Clarification Agent, I need to mark which questions are required and which are optional so that the session can proceed without blocking on gaps the user cannot fill.
- As the Clarification Agent, I need to adapt subsequent questions based on previous answers so that the question set remains relevant and does not ask questions already resolved by earlier responses.
- As the Clarification Agent, I need to persist each answer as a ClarificationAnswer record immediately so that session state is never lost if the user pauses or returns later.
- As the Clarification Agent, I need to signal when sufficient answers have been collected to proceed so that the session transitions to `outcomes_draft` at the right moment, not after a fixed question count.

***

## Stage 3: Ideal Outcomes

**User Stories**

- As a user, I want to see a list of proposed ideal outcomes derived from my answers so that I can evaluate whether the system has understood what success looks like.
- As a user, I want each outcome to be labelled as primary, secondary, or constraint so that I understand its role in the task before deciding whether to approve it.
- As a user, I want to be able to edit the title or description of any proposed outcome so that it reflects my language and intent, not just the agent's inference.
- As a user, I want to be able to add outcomes the agent missed so that nothing important to me is absent from the foundation of the analysis.
- As a user, I want to be able to reject an outcome with a reason so that the system learns what it got wrong.
- As a user, I want to see the proposed input and output templates for each outcome so that I understand what the task will need and what it will produce.
- As a user, I want to be able to modify the input and output templates before approving so that the schema reflects my actual data and format requirements.
- As a user, I want to be required to explicitly approve each outcome before the analysis continues so that I cannot proceed on outcomes I haven't engaged with.

**Agent Stories**

- As the Outcomes Agent, I need to synthesise the clarification answers into a ranked set of outcomes covering primary goals, secondary goals, and constraints so that the user has a complete picture of what the task is trying to achieve.
- As the Outcomes Agent, I need to assign each outcome a type (`primary`, `secondary`, `constraint`) based on the clarification responses so that the user can evaluate the relative importance of each without having to sort them manually.
- As the Outcomes Agent, I need to generate an input template for each outcome that defines the fields, types, and required/optional status of what the outcome needs as input so that the output contract is grounded in real data requirements.
- As the Outcomes Agent, I need to generate an output template for each outcome that defines the deliverable's structure, format, and schema so that the user can approve a concrete specification, not an abstract description.
- As the Outcomes Agent, I need to record whether each outcome was `agent_generated`, `user_added`, or `user_modified` so that patterns in user corrections can inform future template improvement.
- As the Outcomes Agent, I need to confirm that all outcomes have a status of `approved` or `rejected` before allowing the session to transition to `risks_draft` so that no outcome is carried forward silently.

***

## Stage 4: Risk Identification and Scoring

**User Stories**

- As a user, I want to see a list of potential risks identified by the agent so that I can evaluate the threats to this task before any design decisions are made.
- As a user, I want each risk to be categorised so that I can scan quickly for the kinds of risk I care most about.
- As a user, I want to see how each risk has been scored across multiple dimensions so that I understand the reasoning behind its ranking, not just the rank itself.
- As a user, I want to see a plain-language explanation of what each score means so that I can agree or disagree with it intelligently.
- As a user, I want to be able to adjust any individual score if I believe the agent has miscalibrated it so that the final ranking reflects my knowledge of this context.
- As a user, I want to be able to add risks the agent hasn't identified so that domain-specific or contextual risks unique to my situation are included.
- As a user, I want to be able to reject a risk with a reason so that false positives are removed and the system learns from them.
- As a user, I want to see the risks ranked by composite score after approval so that I have a clear priority order entering the decomposition stage.
- As a user, I want to see which risks are flagged as irreversible so that I understand early which ones will require structural human gates.

**Agent Stories**

- As the Risk Agent, I need to generate a set of risks drawn from the approved outcomes, the clarification answers, the domain, and the stakeholder context so that the risk inventory is specific to this task, not generic.
- As the Risk Agent, I need to assign each risk a category from the defined enum so that the user can filter and scan by risk type.
- As the Risk Agent, I need to score each risk across five axes — severity, probability, detectability, reversibility, and scope — and store each score separately so that the composite can be recalculated if the user adjusts any axis score.
- As the Risk Agent, I need to calculate the composite score using the defined weighted formula and rank all risks in descending order so that the user sees the highest-priority risks first.
- As the Risk Agent, I need to generate a plain-language rationale for each axis score so that the user can evaluate whether the scoring reflects their context.
- As the Risk Agent, I need to generate a mitigation note for each risk that identifies the most appropriate response so that the user has a starting point for the gate and oversight decisions that follow in decomposition.
- As the Risk Agent, I need to flag any risk with a reversibility score above 7 as requiring a structural human gate so that irreversibility is surfaced explicitly before the decomposition stage.
- As the Risk Agent, I need to record whether each risk was `agent_generated`, `user_added`, or `user_modified` so that scoring calibration patterns can be tracked and improved.
- As the Risk Agent, I need to confirm that all risks have a status of `approved` or `rejected` before the session transitions to `decomposition_draft` so that no unreviewed risk enters the analysis.

***

## Stage 5: Task Decomposition and Executor Recommendation

**User Stories**

- As a user, I want to see the task broken down into discrete subtasks so that I can evaluate whether the decomposition is complete and correctly granular.
- As a user, I want each subtask to show which approved outcomes it contributes to so that I understand why it exists in the workflow.
- As a user, I want each subtask to show which approved risks it introduces, amplifies, or mitigates so that I can see the risk posture of the full workflow at a glance.
- As a user, I want to see a recommendation for whether each subtask should be executed by a human, an agent, or collaboratively so that I have a starting position to evaluate rather than a blank assignment.
- As a user, I want to see the rationale behind each executor recommendation so that I can agree, disagree, or modify it with understanding.
- As a user, I want to see whether each subtask requires a human gate flagged explicitly so that I know before approving the design where I will be required to be present.
- As a user, I want to see each subtask labelled as productive or unproductive friction so that I understand which ones carry meaning I should retain and which are overhead candidates for automation.
- As a user, I want to see each subtask labelled by reversibility class so that I can immediately identify the highest-consequence points in the workflow.
- As a user, I want to be able to modify a subtask's description, executor assignment, or gate requirement so that the final design reflects my judgment, not just the agent's.
- As a user, I want to be able to add subtasks the agent missed so that no meaningful work unit is absent from the final design.
- As a user, I want to be able to reorder subtasks so that the sequence reflects the actual workflow logic.
- As a user, I want to be required to explicitly approve the full decomposition before the session is marked complete so that I have consciously reviewed every element of the design.
- As a user, I want to see a summary of the approved design — subtasks, executor assignments, gates, and key risks — as a final output so that I have a document I can share, revisit, or hand to a technical team.

**Agent Stories**

- As the Decomposition Agent, I need to break the task into a set of discrete, sequenced subtasks that together cover the full scope of the approved outcomes so that no outcome is left without a subtask responsible for producing it.
- As the Decomposition Agent, I need to assign each subtask a reversibility class — `read_only`, `reversible`, or `irreversible` — based on the nature of its actions so that gate requirements are structurally grounded, not assumed.
- As the Decomposition Agent, I need to classify each subtask as `productive`, `unproductive`, or `mixed` friction so that the executor recommendation is informed by what humans should retain for meaning, not only what agents can do.
- As the Decomposition Agent, I need to create a SubtaskOutcomeMap record for each subtask-outcome relationship, including a contribution type and relevance score, so that the traceability between work and goals is explicit.
- As the Decomposition Agent, I need to create a SubtaskRiskMap record for each subtask-risk relationship, including the relationship type (`introduces`, `amplifies`, `mitigates`) and a recommended mitigation, so that the risk posture of each subtask is visible in context.
- As the Decomposition Agent, I need to score each subtask against the relevant human and agent properties and calculate aggregate scores so that executor recommendations are derived from analysis, not heuristic.
- As the Decomposition Agent, I need to produce an executor recommendation of `human`, `agent`, or `collaborative` for each subtask, with a rationale, so that the user has a justified starting position.
- As the Decomposition Agent, I need to set `requires_human_gate` to true for any subtask that is irreversible, has an amplified high-severity risk, or contains productive friction that must be retained, and record the rationale for each gate so that gate placement is transparent and auditable.
- As the Decomposition Agent, I need to present the full decomposition as a structured, reviewable set — not a single output — so that the user can evaluate, modify, and approve each subtask individually.
- As the Decomposition Agent, I need to confirm that all subtasks have a status of `approved` or `rejected` before the session status transitions to `complete` so that no element of the design is carried forward without the user's explicit acknowledgment.
- As the Session Agent, I need to generate a structured summary of the completed session — including approved outcomes, ranked risks, subtask sequence, executor assignments, and all human gates — so that the output is immediately usable as a foundation for agent specification.

