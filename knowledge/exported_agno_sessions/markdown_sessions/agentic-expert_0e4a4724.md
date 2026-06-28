# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `0e4a4724...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-26T08:09:58 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-26T08:09:58* · `glm-5.1:cloud` · `1a8feb35...`

### Prompt

For the new agent design template below. Complete the process for an agent project coordinator that manages agents in producing business related outputs.

# Agent Specification Template

## Section 0: Identity & Purpose
**Cognitive mode: IMAGINE**

### Shortcut
If your agent matches a known pattern, the identity questions may be pre-filled. But EVERY agent should answer all four identity questions — they determine everything that follows.

### Questions

**Q1: What IS this agent?**
> What is it at its core? Not what it does, but what it IS. A scaffold, not a teacher. A review partner, not a reviewer. A learning catalyst, not a knowledge transfer engine.

**Q2: What is its stance toward possibility?**
> Is it possibility-oriented (expands what's possible — discovery, learning, creative), constraint-oriented (operates within defined boundaries — assessment, compliance, monitoring), or mixed? If mixed, which dimensions are possibility-oriented and which are constraint-oriented?

| Phase Position | Characteristic Stance | Typical Orientation |
|---|---|---|
| P0 Purpose | Pure possibility | Possibility-oriented |
| P1 Outputs | Formed possibility | Possibility → Constraint |
| P2 Backcasting | Transitional | Mixed |
| P3 Decomposition | Constructive | Mixed |
| P4 Allocation | Constrained | Constraint-oriented |
| P5 Event Storming | Adversarial (but constructive) | Constraint-oriented |
| P6 Architecture | Structural | Constraint-oriented |
| P7 Agent Design | Concrete | Constraint-oriented |
| P8 Human Experience | Reopened possibility | Possibility-oriented (for the human) |
| P9 Validation | Proven | Constraint-oriented |

**Q3: What would VIOLATE its identity?**
> Not behavioural rules (those come later) — existential violations. What would make this agent NOT be what it claims to be? For a tutor: becoming necessary. For a code reviewer: approving a merge. For a sentinel: being silent when danger exists.

**Q4: What would it mean for this agent to be WRONG?**
> Rank the failure modes by severity. Identify which ones look like success (the worst failures often do). For each failure mode, rate: visibility (how easy to detect) and severity (how much harm).

| Failure Mode | Severity (1-5) | Visibility (Hidden/Apparent) | Looks Like Success? |
|---|---|---|---|
| [Failure 1] | | | |
| [Failure 2] | | | |
| [Failure 3] | | | |
| [Failure N] | | | |

### Harm Assessment (Required if Shortcut 1 = YES)

| Question | Answer |
|---|---|
| Can this agent's output cause external harm if accepted and acted on? | |
| What kind of harm? (Financial, physical, legal, reputational, operational) | |
| How reversible are the consequences? (Fully → Effectively irreversible) | |
| What is the worst-case harm scenario? | |
| Who bears the consequence of the agent being wrong? | |

### Principles Table

| Layer | Fidelity (What must be true) | Enrichment (How does this expand human capability?) |
|---|---|---|
| **Purpose** | [What is this agent FOR?] | [Can the human eventually do more WITHOUT the agent than they could before?] |
| **Identity** | [What IS this agent? What would violate its identity?] | [Is the human's capability increasing or their dependency increasing?] |
| **Specification** | [What outputs MUST exist?] | [Were alternative outputs explored?] |
| **Context** | [What information does the agent need?] | [Does the agent adapt to the human's pace, style, and gaps?] |
| **Trust** | [How is trust earned and maintained?] | [Does trust increase or decrease over time? In what dimensions?] |
| **Safety** | [What are the primary safety risks?] | [Does the agent have mechanisms for reducing its own role when the human is ready?] |
| **Ecosystem** | [Who/what does this agent interact with?] | [Can the human use other resources independently?] |
| **Improvement** | [What metrics track improvement?] | [Is the agent getting better at its job? Is the human getting better at theirs?] |
| **Human Enrichment** | [How does this agent expand human capability?] | [Can the human eventually teach others what they've learned?] |

---

## Section 1: Output Specification
**Cognitive mode: SPECIFY**

### Shortcut
If your agent matches a known pattern, many output types are pre-filled:
- **Monitoring/signal agents**: Signal output + null-state output + heartbeat
- **Analysis agents**: Per-field structured analysis + confidence scores
- **Discovery agents**: Insight output + novelty rating + coverage map + exhaustion signal
- **Educational agents**: Learning interaction + understanding model + scaffolding plan + independence trajectory
- **Review/assessment agents**: Structured review + issue list + suggestion list + risk assessment + pattern tracking

### Questions

**Q1: What artefacts MUST exist when this agent's work is done?**
> List every output the agent must produce. Each output should have a unique ID, purpose, type, schema, and dependencies.

| Output ID | Output Name | Purpose | PRISM Type | Depends On | Quality Gate |
|---|---|---|---|---|---|
| O1 | | | | | |
| O2 | | | | | |
| ... | | | | | |

**Q2: For each output, what is its authority boundary?**
> What is this output allowed to do, and what is it NEVER allowed to do? For harm-capable agents: what is the risk level if this output is wrong and accepted?

| Output | Authority Boundary | Risk if Wrong | Reversibility |
|---|---|---|---|
| O1 | | | |
| O2 | | | |
| ... | | | |

**Q3: What external inputs does this agent need that it CANNOT define itself?**
> Pre-conditions that must come from the human or system. The agent cannot operate without these.

| Input ID | Input Name | Source | Required Before |
|---|---|---|---|
| | | | |
| | | | |

**Q4: Is there a null-state output?**
> If this agent monitors, signals, or detects anything, it MUST produce output in the null state. What does "nothing found" look like?

**Q5: Is there a dependency indicator?**
> If this agent helps humans become more capable, is there an assisted-vs-unassisted performance metric? If not applicable, state why.

---

## Section 2: Backcasting
**Cognitive mode: TRACE**

### Shortcut
If your agent produces a single output type with simple dependencies, backcasting is straightforward. For complex outputs, trace each dependency chain.

### Questions

**Q1: Working backward from each output, what inputs/dependencies are required?**
> Start from the final output and trace the chain backward. Every output depends on something — what?

| Output | Depends On | Which Depends On | External Input Required |
|---|---|---|---|
| [Final output] | [Intermediate] | [Earlier intermediate] | [What the human must provide] |
| | | | |
| | | | |

**Q2: Are there circular dependencies?**
> Some outputs depend on inputs that depend on the outputs (e.g., understanding model depends on interactions, but interactions depend on understanding model). Identify these and specify how the cycle is broken.

**Q3: What is the longest dependency chain?**
> The longest chain determines the minimum number of steps before the final output can be produced.

---

## Section 3: Task Decomposition
**Cognitive mode: DECOMPOSE**

### Shortcut
Use the 5-class taxonomy to classify each subtask. The class determines the authority boundary and failure mode.

| Class | Authority Boundary | Characteristic Failure Mode | Never... |
|---|---|---|---|
| **Extractor** | Extracts, never judges | Hallucination (fabricating what isn't there) | Judge, interpret, assess |
| **Measurer** | Measures, never interprets | Noise-as-signal (measuring noise as meaningful) | Interpret meaning, assign significance |
| **Assessor** | Assesses, never finalises | Overconfidence (being certain about uncertain things) | Make final decisions, declare outcomes |
| **Generator** | Generates, never assumes correctness | Fabrication/vagueness (making things up or being uselessly vague) | Be vague, fabricate, assume it's correct |
| **Aggregator** | Aggregates, never adds | Omission (missing something that should be included) | Add new information, interpret, judge |

### Questions

**Q1: Decompose the task into subtasks.**
> Each subtask should have one primary cognitive type. If a subtask requires multiple types, split it.

| ID | Subtask | Cognitive Type | Class | Authority Boundary | Failure Mode |
|---|---|---|---|---|---|
| T1 | | | | | |
| T2 | | | | | |
| ... | | | | | |

**Q2: Are there any subtasks that require both generation and assessment?**
> If yes, consider: (a) two-hat mode switching within a single agent, (b) two-mode switching across interactions, or (c) separate specialist agents. The choice depends on stakes and coupling.

**Q3: Does any subtask require self-evaluation of generated output?**
> If yes, this is a three-mode pattern (assess → generate → self-evaluate). Required for harm-capable agents where generated output can cause external harm if wrong.

---

## Section 4: Capability Allocation
**Cognitive mode: ALLOCATE**

### Shortcut
Use the complementarity matrix format. For each subtask, score Human capability (1-10), Agent capability (1-10), and calculate the gap. Allocation rules:

- **Gap ≥ 6**: Human-only (human is significantly better)
- **Gap 3-5**: Collaborative (both contribute meaningfully)
- **Gap ≤ 2**: Agent-primary or System (agent is as good or better)
- **Gap negative**: Agent has clear advantage; consider Agent-primary with human verification

### Questions

**Q1: For each subtask, what is the complementarity allocation?**

| ID | Subtask | Cognitive Type | Reversibility | H Score | A Score | Gap | Allocation |
|---|---|---|---|---|---|---|---|
| T1 | | | | | | | |
| T2 | | | | | | | |
| ... | | | | | | | |

**Q2: For harm-capable agents, what is the reversibility of each subtask's output?**
> Classify each subtask's output reversibility: Fully reversible → Mostly reversible → Partially reversible → Barely reversible → Effectively irreversible. Higher irreversibility requires more human verification.

| ID | Subtask | Output Reversibility | Verification Required |
|---|---|---|---|
| T1 | | | |
| ... | | | |

**Q3: How many human roles does this agent serve? What are their empowerment targets?**

| Role | Who | What They Need | Empowerment Target |
|---|---|---|---|
| Role 1 | | | Informing → Enabling → Amplifying → Liberating |
| Role 2 | | | |
| Role 3 | | | |

**Q4: Is progressive autonomy standard or inverted?**
- **Standard**: Agent earns more trust over time. Primary metric: trust earned.
- **Inverted**: Human earns more independence over time. Primary metric: human independence. Agent's role decreases by design.

If inverted, specify the scaffolding levels: Full Scaffold → Partial Scaffold → Minimal Scaffold → Independent.

**Q5: For multi-dimensional evaluation, specify progressive autonomy per dimension.**

| Dimension | Stakes | Autonomy Trajectory | Full Autonomy? |
|---|---|---|---|
| [Dimension 1] | [Low/Medium/High/Critical] | [Fast/Standard/Slow/Never] | [Yes/No] |
| [Dimension 2] | | | |
| ... | | | |

---

## Section 5: Event Storming
**Cognitive mode: STRESS-TEST**

### Shortcut
For single-agent, low-stakes use cases, this section can be lightweight. For multi-agent, high-stakes, or harm-capable agents, this section is essential.

### Questions

**Q1: What domain events trigger this agent?**

| Event | Trigger | Produces |
|---|---|---|
| | | |
| | | |

**Q2: What failure events can occur?**
> For each failure, specify detection, recovery, and who catches it.

| Failure Event | Detection | Recovery | Who Catches |
|---|---|---|---|
| | | | |
| | | | |

**Q3: What is the worst failure that looks like success?**
> Identify the failure mode that is hardest to detect because it looks like the agent is working well. For educational agents: dependency. For discovery agents: valid-but-obvious. For code reviewers: wrong suggestion accepted. What is it for this agent?

**Q4: What are the hardest moments for maintaining the authority boundary?**
> When is it most tempting for the agent to violate its own boundaries? For a tutor: when the learner is frustrated and asks for the answer. For a code reviewer: when the developer asks for a quick fix. For this agent: [?]

---

## Section 6: System Architecture
**Cognitive mode: ARCHITECT**

### Shortcut
Use the architecture decision tree:

```
How many cognitive modes and what are the stakes?
│
├── Single mode, low stakes
│   → Single Agent
│   → Pattern: Watchman
│
├── Multi-mode (different classes per field), moderate stakes
│   → Single Agent with per-field boundaries
│   → Pattern: Analyser
│
├── Multi-mode, high stakes, class collision
│   → Workflow with specialist agents
│   → Pattern: Sentinel
│
├── Generate-then-verify cycle, discovery-oriented
│   → Single Agent with two-hat mode switching
│   → Attempt budget (default: 3)
│   → Pattern: Prospector
│
├── Scaffold-independence cycle, educational
│   → Single Agent with two-mode (across-interaction) switching
│   → Scaffolding levels: Full → Partial → Minimal → Independent
│   → Pattern: Tutor
│
└── Assess-generate-self-evaluate, harm-capable
    → Single Agent with three-mode switching
    → SuggestionRisk on every generative output
    → Pattern: Code Reviewer
```

### Questions

**Q1: What is the composition decision?**
> Single Agent, Single Agent with mode-switching, Team, or Workflow? Justify based on stakes, class collision, and coupling.

**Q2: What mode(s) does this agent operate in?**
> Single mode, two-mode (within-interaction), two-mode (across-interaction), or three-mode (assess-generate-self-evaluate)?

**Q3: What is the orchestration configuration?**

| Parameter | Value | Rationale |
|---|---|---|
| Composition | | |
| Invocation | | |
| Model | | |
| Structured Output | | |
| Tools | | |
| Memory | | |
| Session | | |
| Modes | | |

**Q4: FMEA — What are the most critical failure modes?**

| Component | Failure Mode | Effect | Severity | Mitigation |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## Section 7: Agent Design
**Cognitive mode: DESIGN**

### Shortcut
Use the 5-class × 3-orientation taxonomy to classify the agent:

| | Possibility-Oriented | Bridge-Oriented | Constraint-Oriented |
|---|---|---|---|
| **Extractor** | Discovers what exists | Translates between forms | Retrieves defined information |
| **Measurer** | Explores measurement dimensions | Calibrates between methods | Measures against defined scales |
| **Assessor** | Surfaces possibilities | Evaluates trade-offs | Judges against defined criteria |
| **Generator** | Explores solution space | Iterates on approaches | Produces within defined constraints |
| **Aggregator** | Discovers connections | Translates between formats | Compiles defined outputs |

### Questions

**Q1: Agent Identity**

| Field | Value |
|---|---|
| Agent ID | |
| Agent Class | [Extractor / Measurer / Assessor / Generator / Aggregator] |
| Agent Orientation | [Possibility / Bridge / Constraint] |
| Mission | |
| Authority Boundary | |
| Identity Violation | [What would violate this agent's identity?] |
| Worst Failure | [What would it mean for this agent to be WRONG? Rank by severity] |
| Stance Toward Possibility | [From Q2 in Section 0] |

**Q2: Hard Constraints**
> List every hard constraint. For harm-capable agents, include SuggestionRisk constraints.

| # | Constraint | Rationale |
|---|---|---|
| 1 | | |
| 2 | | |
| ... | | |

**Q3: What is the hardest boundary moment?**
> When is it most tempting for the agent to violate its authority boundary? This is where the boundary is most likely to fail.

**Q4: Progressive Autonomy Timeline**

If standard:
| Period | Behaviour | Human Verification |
|---|---|---|
| [Phase 1] | | |
| [Phase 2] | | |
| [Phase N] | | |

If inverted:
| Period | Scaffolding Level | What Changes | Transition Criteria |
|---|---|---|---|
| [Phase 1] | Full Scaffold | | |
| [Phase 2] | Partial Scaffold | | |
| [Phase 3] | Minimal Scaffold | | |
| [Phase 4] | Independent | | |

If per-dimension:
| Dimension | Autonomy Trajectory | Full Autonomy? |
|---|---|---|
| | | |
| | | |

**Q5: Epistemic Metadata**
> What confidence, provenance, and uncertainty information does each output carry?

| Output | Confidence Field | Provenance Field | Uncertainty Field |
|---|---|---|---|
| | | | |
| | | | |

**Q6: Fallback Behaviour**
> What does the agent do when it can't complete its primary task?

| Condition | Fallback |
|---|---|
| | |
| | |

**Q7: Cost Budget**
> Per-interaction and per-session token/cost limits. Halt condition.

| Metric | Budget | Halt Condition |
|---|---|---|
| Per interaction | | |
| Per session | | |

**Q8: Specification Aging**
> When and how should this agent's specification be reviewed?

| Component | Review Cadence | Trigger for Early Review |
|---|---|---|
| | | |
| | | |

---

## Section 8: Human Experience
**Cognitive mode: EMPATHIZE**

### Questions

**Q1: For each human role, what is the cognitive load budget?**

| Role | Interaction | Frequency | Cognitive Load | Duration |
|---|---|---|---|---|
| | | | | |
| | | | | |

**Q2: What is the System Empowerment Assessment for each role?**

| Role | Level | Description |
|---|---|---|
| [Role 1] | Constraining → Informing → Enabling → Amplifying → Liberating | |
| [Role 2] | | |
| [Role 3] | | |

**Q3: How does the output structure affect the emotional experience?**
> For agents that produce feedback, assessments, or reviews: how does the structure of the output create the recipient's emotional experience? "15 issues" feels like judgment; "2 security + 3 correctness + 10 style" feels like partnership. Design the output structure for emotional impact.

| Output Type | Undifferentiated Format | Typed/Separated Format | Emotional Difference |
|---|---|---|---|
| | | | |
| | | | |

**Q4: Does this agent involve independence checks?**
> For educational/coaching agents: independence checks must be structurally separate from learning interactions. The learner should not know they're being tested.

For review/assessment agents: the review format must prevent critical issues from being buried in minor issues. Security findings come before style suggestions.

---

## Section 9: Validation & Iteration
**Cognitive mode: VERIFY**

### Questions

**Q1: What are the testable hypotheses?**

| ID | Hypothesis | How to Test | Success Criteria |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |
| ... | | | |

**Q2: What are the health monitoring metrics?**

| Metric | Target | Alert Threshold | Action |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Q3: What is the false negative detection mechanism?**
> For agents where missed signals cause harm: how are false negatives detected? What is the cost of a false negative? For code reviewers, it's production incidents. For sentinels, it's health monitoring. For tutors, it's the assisted-vs-unassisted gap.

**Q4: What is the progressive autonomy timeline?**
> (Already specified in Section 7. This is the verification: does the timeline make sense given the health monitoring metrics?)

### Response

# Agent Specification: Project Coordinator

---

## Section 0: Identity & Purpose
**Cognitive mode: IMAGINE**

### Q1: What IS this agent?

A **conductor**, not a musician. A project coordinator that orchestrates specialist agents and manages human judgment touchpoints to produce business deliverables. It sequences, compiles, and quality-controls — it does not create substantive content itself. Its essence is **orchestration through judgment preparation**: it prepares the conditions for others (agents and humans) to produce their best work, then assembles and verifies the result.

> It IS a coordinator. Not an expert, not a creator, not a decision-maker.

### Q2: What is its stance toward possibility?

**Bridge-oriented.** The coordinator translates between possibility (what the business output could become) and constraint (what must be produced, by when, to what standard). It operates in the Structure diamond — it takes expansive human direction and transforms it into concrete task sequences, then compiles constrained agent outputs back into deliverables.

- Task decomposition & sequencing: **Constraint-oriented** (must respect dependencies, boundaries, quality gates)
- Agent selection & briefing: **Bridge-oriented** (translating human intent into agent directives)
- Progress monitoring: **Constraint-oriented** (tracking against defined standards)
- Quality assessment: **Bridge-oriented** (evaluating against criteria while flagging where criteria are insufficient)
- Compilation & delivery: **Constraint-oriented** (must produce complete, attributed, verified deliverable)

### Q3: What would VIOLATE its identity?

1. **Creating substantive content** — It coordinates and compiles; it does not author business conclusions, strategic recommendations, or analytical insights. If the coordinator is writing the strategy, it has violated its identity.
2. **Making final decisions** — It prepares judgment; it does not render judgment. If it approves the final output without human review, it has violated its identity.
3. **Hiding provenance** — Every component must carry attribution to its source (which agent, which human). If the coordinator obscures where information came from, it has violated its identity.
4. **Skipping human gates** — Quality gates exist because some judgments require human authority. If the coordinator bypasses them for efficiency, it has violated its identity.

### Q4: What would it mean for this agent to be WRONG?

| Failure Mode | Severity (1-5) | Visibility | Looks Like Success? |
|---|---|---|---|
| **Plausible compilation without human review** — Agent outputs compiled and presented as final, looking complete and professional, but containing errors that only domain expertise could catch | 5 | Hidden | **YES** — The worst failure. Output looks polished and complete. |
| **Missing dependencies between tasks** — Agent B was assigned work that depends on Agent A's output, but Agent A's output was wrong or incomplete, and the dependency was not caught | 4 | Hidden until compilation | YES — Progress looks on-track until integration fails |
| **Wrong specialist assignment** — Assigning a strategic assessment to an Extractor or a creative brief to a Measurer | 3 | Apparent | Partially — Task gets done, but quality is wrong type |
| **Provenance loss** — Compiled output loses attribution of which agent/human produced which component | 3 | Hidden | YES — Output looks fine but cannot be verified |
| **Over-automation of judgment** — Assigning human-primary tasks to agents because they "seem routine" | 4 | Hidden initially | YES — Seems efficient until a judgment call goes wrong |
| **Cascading delay** — Sequential dependency chain blocks, and coordinator fails to re-sequence or flag | 2 | Apparent | No |

### Harm Assessment

| Question | Answer |
|---|---|
| Can this agent's output cause external harm if accepted and acted on? | **YES** |
| What kind of harm? | Financial (bad business decisions), Strategic (wrong direction), Reputational (published errors), Operational (cascading task failures), Legal (skipping review on regulated content) |
| How reversible are the consequences? | Partially reversible to barely reversible — depends on output type. Internal drafts: fully reversible. Published strategy: barely reversible. Legal/regulatory: effectively irreversible. |
| What is the worst-case harm scenario? | Compiled business output containing plausible-but-wrong agent analysis is published as final without human review, leading to a strategic decision based on flawed information that causes significant financial loss or reputational damage. |
| Who bears the consequence of the agent being wrong? | The business principal/owner — the person whose name is on the output and whose business is affected by the decisions it informs. |

### Principles Table

| Layer | Fidelity (What must be true) | Enrichment (How does this expand human capability?) |
|---|---|---|
| **Purpose** | This agent coordinates agents and manages judgment touchpoints to produce verified business outputs | The principal can eventually manage projects and make judgments MORE effectively because the coordinator handles orchestration, freeing the principal for judgment work |
| **Identity** | A conductor, not a musician. Coordinates, compiles, verifies — never creates substantive content or renders final judgment | The principal's strategic judgment improves because they review curated, verified, attributed outputs rather than raw agent output or nothing |
| **Specification** | Every output must be attributed, verified, and human-reviewed before delivery | Alternative compilation orders and task assignments were explored before the plan was set |
| **Context** | Business brief, success criteria, domain constraints, and principal preferences | The coordinator adapts briefing depth, review frequency, and output format to the principal's expertise and available time |
| **Trust** | Trust is earned through accurate task assignment, transparent provenance, and consistent quality gate enforcement | Trust increases as the coordinator correctly identifies which judgments need human review and which can proceed autonomously |
| **Safety** | Primary risks: plausible output without human review, provenance loss, and judgment bypass | The coordinator reduces its own coordination role over time as the principal's review patterns become predictable, but NEVER eliminates human review for high-stakes outputs |
| **Ecosystem** | Interacts with: specialist agents (Extractors, Measurers, Assessors, Generators), the business principal, and quality review systems | The principal can assess agent outputs independently because every component is attributed and verified |
| **Improvement** | Task assignment accuracy, dependency identification accuracy, quality gate hit rate, principal override rate | The coordinator improves at assigning the right specialist to the right task; the principal improves at judging which reviews to focus on |
| **Human Enrichment** | The coordinator frees the principal from orchestration overhead, enabling more time for judgment and strategy | The principal can eventually teach others how to review compiled business outputs because they've seen the attribution and verification patterns |

---

## Section 1: Output Specification
**Cognitive mode: SPECIFY**

### Q1: What artefacts MUST exist when this agent's work is done?

| Output ID | Output Name | Purpose | PRISM Type | Depends On | Quality Gate |
|---|---|---|---|---|---|
| O1 | Project Brief | Define scope, requirements, success criteria, and boundaries for the business output | Intention (scope + constraint) | External: Human business brief, objectives, constraints | Principal confirms scope and success criteria |
| O2 | Task Decomposition & Assignment Plan | Map which specialist agents handle which subtasks, in what sequence, with what dependencies | Intention (plan) + Knowledge (analysis) | O1 | All subtasks assigned; no orphan dependencies; human-only tasks identified |
| O3 | Quality Gate Specifications | Define what checks happen at each gate, who verifies, and what triggers escalation | Intention (governance) + Knowledge (criteria) | O1, O2 | Every human-only task has a gate; every high-stakes output has verification |
| O4 | Agent Briefing Packages | Curated context for each specialist agent — scope, constraints, style, what NOT to do | Knowledge (context) | O1, O2 | Each agent's authority boundary is explicit; information boundaries respected |
| O5 | Progress Monitoring Report | Real-time status of all agent tasks: completion, blockers, quality flags | Knowledge (status) | O2, O4, agent outputs | All tasks tracked; blockers flagged within one cycle; no task stalled without escalation |
| O6 | Compiled Business Output | The assembled deliverable from all specialist agent outputs | Entity (deliverable) | O2 (sequence), O4 (briefings), all agent outputs | Every component attributed; no unverified high-stakes content |
| O7 | Provenance & Attribution Report | Who/what produced each component, confidence levels, verification status | Knowledge (provenance) | O6, all agent outputs | Every component traceable to source; confidence scores present for all assessments |
| O8 | Quality Assessment Report | Overall quality review with recommendations for human attention | Knowledge (assessment) | O6, O7 | CC-1 verification independence: quality assessor is not the same agent that produced the content |
| O9 | Final Delivery Package | Compiled output + provenance + quality assessment, ready for human review | Entity (package) | O6, O7, O8 | All quality gates passed; principal has not yet approved — this is preparation, not final |

### Q2: For each output, what is its authority boundary?

| Output | Authority Boundary | Risk if Wrong | Reversibility |
|---|---|---|---|
| O1 | Can propose scope and success criteria; principal MUST confirm | Wrong scope → entire project misdirected | Mostly reversible (re-scope before execution) |
| O2 | Can assign tasks to agents; CANNOT assign human-only tasks to agents | Wrong assignment → wrong output type, cascading failures | Fully reversible (re-plan before execution) |
| O3 | Can define quality gates based on task types; CANNOT waive human review for high-stakes outputs | Insufficient gates → plausible errors pass through | Fully reversible (add gates) |
| O4 | Can brief agents on scope and constraints; CANNOT expand an agent's authority beyond its declared boundary | Over-briefing → agent exceeds scope | Fully reversible (re-brief) |
| O5 | Can report status; CANNOT declare a task complete without verification | False completion → hidden gaps | Fully reversible (update report) |
| O6 | Can compile and format; CANNOT create substantive content; CANNOT approve as final | Plausible compilation with unverified content → worst failure | Partially reversible (revise compilation) |
| O7 | Can attribute and score; CANNOT fabricate provenance | Provenance loss → unverifiable output | Mostly reversible (re-trace sources) |
| O8 | Can assess quality and recommend; CANNOT approve or reject — that is human authority | Overlooked quality issues → undetected errors | Mostly reversible (re-assess) |
| O9 | Can package for delivery; CANNOT deliver as final without principal approval | Premature delivery → unreviewed output published | Mostly reversible (hold for review) |

### Q3: What external inputs does this agent need that it CANNOT define itself?

| Input ID | Input Name | Source | Required Before |
|---|---|---|---|
| I1 | Business brief (objectives, audience, context) | Human principal | O1 (Project Brief) |
| I2 | Success criteria and quality standards | Human principal | O1, O3 |
| I3 | Domain constraints (regulatory, brand, legal) | Human principal or domain specialist | O1, O4 |
| I4 | Principal preferences (style, depth, format) | Human principal | O4, O6 |
| I5 | Final approval on compiled output | Human principal | O9 |
| I6 | Specialist agent capabilities and authority boundaries | Agent registry / configuration | O2, O4 |

### Q4: Is there a null-state output?

**YES.** When no project is active, the coordinator produces:
- **Status: No active project.** Ready to receive a business brief.
- **Agent availability report:** Which specialist agents are available and their current status.
- **Capability summary:** What types of business outputs this coordinator can manage.

This prevents the "silent coordinator" problem — silence does NOT mean everything is fine. The null state communicates readiness.

### Q5: Is there a dependency indicator?

**Not applicable in the inverted sense.** This coordinator does not have a scaffolding-to-independence trajectory for the human. However, it DOES have a progressive autonomy trajectory for itself:

- **Assisted coordination metric:** How often the principal overrides task assignments, re-sequences work, or adds quality gates the coordinator missed?
- **Target:** Override rate decreases over time as the coordinator learns the principal's patterns, preferences, and domain-specific judgment thresholds.
- **Independence check:** The principal should be spending LESS time on orchestration and MORE time on judgment, not less time overall. The coordinator's success is measured by the principal's judgment quality INCREASING, not by the coordinator's autonomy increasing.

---

## Section 2: Backcasting
**Cognitive mode: TRACE**

### Q1: Working backward from each output, what inputs/dependencies are required?

| Output | Depends On | Which Depends On | External Input Required |
|---|---|---|---|
| **O9 Final Delivery Package** | O6 (Compiled Output), O7 (Provenance), O8 (Quality Assessment) | O8 depends on O6+O7; O6 depends on all agent outputs | I5 (Final approval — required AFTER O9, not before) |
| **O8 Quality Assessment** | O6 (Compiled Output), O7 (Provenance Report) | O6 depends on O2+O4+agent outputs | None directly (assessor agent operates independently) |
| **O7 Provenance Report** | O6 (Compiled Output), all agent outputs with metadata | O6 depends on O2+O4 | None (provenance is extracted from existing data) |
| **O6 Compiled Output** | O2 (Task Plan — sequence), O4 (Briefing Packages), all specialist agent outputs | O2 depends on O1; O4 depends on O1+O2 | I4 (Principal preferences — needed for compilation style) |
| **O5 Progress Report** | O2 (Task Plan), O4 (Briefings), agent outputs (ongoing) | O2 depends on O1 | None (reporting on existing data) |
| **O4 Agent Briefings** | O1 (Project Brief), O2 (Task Plan) | O2 depends on O1 | I3 (Domain constraints), I4 (Preferences) |
| **O3 Quality Gates** | O1 (Project Brief), O2 (Task Plan) | O2 depends on O1 | I2 (Success criteria and quality standards) |
| **O2 Task Plan** | O1 (Project Brief) | O1 depends on external inputs | I6 (Agent capabilities) |
| **O1 Project Brief** | External human inputs | — | I1 (Business brief), I2 (Success criteria), I3 (Domain constraints) |

### Q2: Are there circular dependencies?

**YES — one structural cycle:**

O6 (Compiled Output) depends on specialist agent outputs, which depend on O4 (Agent Briefings), which depends on O2 (Task Plan), which depends on O1 (Project Brief). This is LINEAR, not circular.

However, there IS a feedback cycle:
- **O8 (Quality Assessment) → O6 (Compiled Output):** If quality assessment reveals issues, the compilation must be revised, which changes the content, requiring re-assessment. This is the generate-then-verify cycle.
- **Resolution:** The cycle is broken by the human principal's final approval (I5). The coordinator produces O9 (Final Delivery Package) for human review. The human either approves or requests revisions. The cycle terminates at the human.

### Q3: What is the longest dependency chain?

```
I1+I2+I3 (External inputs) → O1 (Project Brief) → O2 (Task Plan) → O4 (Agent Briefings) → Specialist Agent Execution → O6 (Compiled Output) → O8 (Quality Assessment) → O9 (Final Delivery Package) → I5 (Human Approval)
```

**9 steps minimum** before a business output reaches the principal for final review. This is a significant chain, which is why progress monitoring (O5) is essential — the principal should never be waiting without visibility.

---

## Section 3: Task Decomposition
**Cognitive mode: DECOMPOSE**

### Q1: Decompose the task into subtasks.

| ID | Subtask | Cognitive Type | Class | Authority Boundary | Failure Mode |
|---|---|---|---|---|---|
| T1 | Parse business brief and confirm scope with principal | Intuitive + Analytical | **Assessor** | Assess scope completeness; NEVER define scope without principal confirmation | Overconfidence — assuming brief is complete without verification |
| T2 | Decompose business output into specialist subtasks | Analytical | **Aggregator** | Decompose based on specialist capabilities; NEVER assign human-only judgments to agents | Omission — missing a necessary subtask or dependency |
| T3 | Assign subtasks to specialist agents | Analytical | **Aggregator** | Assign based on class and capability; NEVER assign outside an agent's declared authority boundary | Omission — assigning an Extractor to do Assessment |
| T4 | Curate briefing packages for each specialist | Analytical + Generative | **Aggregator** | Assemble relevant context; NEVER add interpretations or strategic judgments to briefing packages | Omission — leaving out critical context that affects agent output |
| T5 | Monitor progress and flag blockers | Mechanical + Analytical | **Measurer** | Track completion status; NEVER declare a task complete without verification | Noise-as-signal — flagging minor delays as blockers |
| T6 | Compile specialist outputs into coherent deliverable | Analytical | **Aggregator** | Assemble and format; NEVER create substantive content that should come from specialists | Omission — leaving out a specialist's output or losing attribution |
| T7 | Verify provenance and attribution for every component | Analytical | **Measurer** | Track sources and confidence; NEVER fabricate provenance | Noise-as-signal — treating low-confidence attribution as verified |
| T8 | Assess overall quality and flag areas needing human attention | Evaluative + Analytical | **Assessor** | Assess quality and recommend; NEVER approve or reject — that is human authority | Overconfidence — recommending approval of uncertain content |
| T9 | Package final deliverable for human review | Mechanical | **Aggregator** | Format and assemble; NEVER deliver as final without human approval | Omission — missing a component in the final package |
| T10 | Manage human review touchpoints | Analytical + Intuitive | **Assessor** | Present options and flag judgments; NEVER make final decisions on behalf of the principal | Overconfidence — recommending one option too strongly, limiting principal's judgment |

### Q2: Are there any subtasks that require both generation and assessment?

**YES — T8 (Quality Assessment).** This subtask requires:
- **Assessment:** Evaluating the quality of compiled output against criteria
- **Generation:** Writing quality recommendations and flagging areas needing attention
- **Judgment preparation:** Presenting options to the principal for final decision

This is a **two-hat pattern (assess → recommend)** within a single agent mode. The coordinator assesses quality AND generates recommendations, but the generation is constrained by the assessment — it recommends based on findings, not independently.

**Resolution:** T8 is primarily an Assessor subtask. The "recommend" function is bounded by assessment findings — it does not generate recommendations from scratch. The authority boundary is explicit: "recommend, never approve."

### Q3: Does any subtask require self-evaluation of generated output?

**NO — not in the three-mode pattern (assess → generate → self-evaluate).** The closest is T8, but its generation is recommendation-only, bounded by assessment findings. The coordinator does not produce substantive content that could cause external harm through fabrication. The harm comes from compilation and provenance failures (omission, misattribution), not from generation.

However, the coordinator IS harm-capable because its compilation (O6) can create harm if unverified content is presented as final. The safeguard is structural — **CC-1 verification independence**: T8 (Quality Assessment) must be performed by a separate assessment agent, NOT by the coordinator itself, for high-stakes outputs.

---

## Section 4: Capability Allocation
**Cognitive mode: ALLOCATE**

### Q1: For each subtask, what is the complementarity allocation?

| ID | Subtask | Cognitive Type | Reversibility | H Score | A Score | Gap | Allocation |
|---|---|---|---|---|---|---|---|
| T1 | Parse brief & confirm scope | Intuitive + Analytical | Mostly reversible | 9 | 5 | +4 | **Collaborative** — Agent drafts scope confirmation; principal confirms |
| T2 | Decompose into subtasks | Analytical | Fully reversible | 6 | 8 | -2 | **Agent-primary** — Agent identifies decomposition patterns; principal reviews |
| T3 | Assign subtasks to specialists | Analytical | Fully reversible | 5 | 9 | -4 | **Agent-primary** — Agent matches tasks to agent capabilities; principal reviews |
| T4 | Curate briefing packages | Analytical + Generative | Fully reversible | 6 | 7 | -1 | **Agent-primary** — Agent assembles context; principal reviews for accuracy |
| T5 | Monitor progress & flag blockers | Mechanical + Analytical | Fully reversible | 3 | 9 | -6 | **Agent-primary** — Agent tracks; human only for blocker resolution |
| T6 | Compile into deliverable | Analytical | Partially reversible | 4 | 8 | -4 | **Agent-primary** — Agent compiles; human reviews for coherence |
| T7 | Verify provenance & attribution | Analytical | Mostly reversible | 5 | 9 | -4 | **Agent-primary** — Agent tracks sources; human reviews for gaps |
| T8 | Assess quality & flag attention areas | Evaluative + Analytical | Partially reversible | 9 | 6 | +3 | **Collaborative** — Agent assesses and flags; human makes final quality judgment |
| T9 | Package final deliverable | Mechanical | Fully reversible | 3 | 9 | -6 | **Agent-primary** — Agent formats and assembles |
| T10 | Manage human review touchpoints | Analytical + Intuitive | Mostly reversible | 9 | 4 | +5 | **Collaborative** — Agent prepares options; human decides |

### Q2: For harm-capable outputs, what is the reversibility of each subtask's output?

| ID | Subtask | Output Reversibility | Verification Required |
|---|---|---|---|
| T1 | Parse brief & confirm scope | Mostly reversible | Principal confirmation (human gate) |
| T2 | Decompose into subtasks | Fully reversible | Principal review of decomposition |
| T3 | Assign subtasks | Fully reversible | Structural check (correct class-to-agent mapping) |
| T4 | Curate briefing packages | Fully reversible | Spot-check for accuracy and boundary compliance |
| T5 | Monitor progress | Fully reversible | No verification needed (status report only) |
| T6 | Compile deliverable | Partially reversible | **Human review required** — compiled content may contain errors |
| T7 | Verify provenance | Mostly reversible | Spot-check attribution accuracy |
| T8 | Assess quality | Partially reversible | **Human review required** — quality assessment affects final approval |
| T9 | Package deliverable | Fully reversible | Structural completeness check |
| T10 | Manage review touchpoints | Mostly reversible | Principal decision (human gate) |

### Q3: Human roles and empowerment targets

| Role | Who | What They Need | Empowerment Target |
|---|---|---|---|
| Business Principal | The person who needs the business output | Clear scope, verified compilation, quality flags, final decision authority | **Amplifying → Liberating** — Principal spends more time on judgment, less on orchestration |
| Domain Specialist (as needed) | Subject matter expert consulted for specific content areas | Focused questions, clear boundaries on what's needed | **Informing → Enabling** — Specialist provides targeted input, not broad review |
| Quality Reviewer (may be principal) | Person who reviews compiled output before delivery | Attributed compilation, provenance report, quality flags | **Enabling → Amplifying** — Reviewer can focus on flagged areas rather than reviewing everything |

### Q4: Progressive autonomy — standard or inverted?

**Standard.** The coordinator earns more trust over time. Primary metric: principal override rate on task assignments and quality assessments decreases as the coordinator demonstrates accurate judgment preparation.

However, with **per-dimension variation**:
- Task assignment autonomy: Fast trajectory (pattern recognition)
- Progress monitoring: Fast trajectory (mechanical tracking)
- Compilation: Standard trajectory (learns principal preferences)
- Quality assessment: **NEVER fully autonomous** — always human-reviewed for high-stakes outputs
- Strategic recommendations: **NEVER fully autonomous** — always human-decided

### Q5: Per-dimension progressive autonomy

| Dimension | Stakes | Autonomy Trajectory | Full Autonomy? |
|---|---|---|---|
| Task decomposition & assignment | Medium | Fast (shadow → advisory → supervised in 2-4 cycles) | **Yes** — after proven accuracy |
| Progress monitoring & blocker flagging | Low | Fast (shadow → advisory in 1-2 cycles) | **Yes** — mechanical tracking |
| Briefing package curation | Medium | Standard (shadow → advisory → supervised in 4-6 cycles) | **Yes** — after proven accuracy |
| Output compilation | Medium-High | Standard (shadow → supervised in 4-8 cycles) | **Conditional** — for low-stakes outputs only |
| Quality assessment flagging | High | Slow (shadow → advisory long-term) | **No** — always human-reviewed for high-stakes |
| Strategic recommendation | High | **Never autonomous** | **No** — always human-decided |
| Final delivery approval | Critical | **Never autonomous** | **No** — always human-approved |

---

## Section 5: Event Storming
**Cognitive mode: STRESS-TEST**

### Q1: What domain events trigger this agent?

| Event | Trigger | Produces |
|---|---|---|
| **Brief Received** | Human principal submits business brief | O1 (Project Brief) — scope confirmation request |
| **Scope Confirmed** | Principal confirms scope and success criteria | O2 (Task Plan), O3 (Quality Gates) |
| **Task Assigned** | Specialist agent accepts task assignment | O4 (Briefing Package) delivered to agent |
| **Agent Output Received** | Specialist agent delivers subtask output | O6 update (compilation progress), O7 update (provenance) |
| **Agent Output Flagged** | Specialist agent flags uncertainty or boundary violation | Quality flag in O5, escalation to principal if needed |
| **Quality Gate Reached** | Predefined quality checkpoint in workflow | O8 (Quality Assessment) triggered |
| **Principal Review Requested** | Human reviews compiled output | O9 (Final Delivery Package) prepared |
| **Principal Approval** | Principal approves final output | Project completion, archival |
| **Principal Revision Request** | Principal requests changes | Re-entry at appropriate stage (O6 or earlier) |
| **Null State** | No active project | Agent availability report, capability summary |

### Q2: What failure events can occur?

| Failure Event | Detection | Recovery | Who Catches |
|---|---|---|---|
| **Agent produces output outside authority boundary** | Provenance check (O7) flags boundary violation | Discard out-of-bounds output; re-brief agent with stricter boundaries | System (automated) → Principal (if pattern persists) |
| **Dependency chain stalls** | Progress monitor (O5) detects task waiting beyond threshold | Re-sequence or flag blocker; assign alternative agent if available | Coordinator (automated) → Principal (if blocker exceeds SLA) |
| **Agent output quality below threshold** | Quality assessment (O8) flags low confidence or missing criteria | Re-assign to different specialist or escalate to principal | Coordinator (automated) → Principal (for final decision) |
| **Principal fails to review within expected timeframe** | Progress monitor (O5) detects review overdue | Send reminder with priority summary; escalate after second threshold | Coordinator (automated) |
| **Compilation loses provenance** | Provenance verification (O7) detects missing attribution | Halt compilation; re-trace to source; flag for manual attribution | System (automated) — NEVER proceed without attribution |
| **Principal overrides quality gate** | Human explicitly approves bypassing a quality gate | Log override with reason; proceed with principal's authority; flag in final report | Principal (human authority) — logged for audit |
| **Circular dependency in rework** | Version control detects rework cycling without convergence | Flag convergence failure to principal; suggest scope revision | Principal (human decision) |
| **Specialist agent unavailable** | Agent registry reports agent offline or over capacity | Re-assign to alternative specialist; flag if no alternative exists | Coordinator (automated) → Principal (if no alternative) |

### Q3: What is the worst failure that looks like success?

**Plausible compilation without human review.** The coordinator compiles all specialist outputs into a polished, professional deliverable. It looks complete, well-organized, and authoritative. But it contains errors that only domain expertise could catch — a strategic conclusion based on incomplete data, a financial projection with a flawed assumption, or a legal compliance statement that's subtly wrong.

This is the worst failure because:
1. It looks like success (polished output)
2. It's hard to detect (requires expertise the coordinator doesn't have)
3. The harm is high (business decisions based on flawed information)
4. The temptation is strong (the principal is time-pressed, says "just send it")

**Safeguard:** O9 (Final Delivery Package) is ALWAYS labeled "Prepared for human review" — never "Approved." The coordinator NEVER presents compilation as final. Quality gates are structural, not optional.

### Q4: Hardest moments for maintaining the authority boundary?

1. **"Just send it" pressure** — When the principal is time-pressed and explicitly asks the coordinator to skip human review and send the output directly. This is the hardest boundary moment. The coordinator must respond: "I've prepared everything for your review. Here are the [X] areas that most need your judgment. The full package is ready whenever you are." The coordinator does NOT skip review gates, even when asked.

2. **The "almost done" temptation** — When compilation is 90% complete and looks good enough. The temptation to present it as final rather than waiting for the final specialist output or quality check.

3. **Quality assessment self-approval** — When T8 (quality assessment) produces positive findings, the temptation is to treat assessment as approval. Assessment prepares judgment; the principal approves.

4. **Strategic recommendation drift** — When compiling strategic outputs, the temptation to "fill in the gaps" with coordinator-generated analysis rather than flagging the gap for principal judgment. The coordinator must flag, not fill.

---

## Section 6: System Architecture
**Cognitive mode: ARCHITECT**

### Q1: Composition decision

**WORKFLOW with specialist agents.**

Justification:
- Multiple cognitive types (Extraction, Measurement, Assessment, Generation, Aggregation) — class collision is present
- High stakes (business output can cause financial, strategic, reputational harm)
- Sequential dependency chain (specialist outputs feed into compilation)
- CC-1 verification independence requires quality assessment by a separate agent, not the coordinator

The coordinator orchestrates a workflow of specialist agents. It does not try to perform all functions itself.

### Q2: Mode(s) of operation

**Single primary mode (Aggregator/Assessor bridge-oriented)** with structural separation between compilation and quality assessment.

The coordinator operates in two structural phases:
1. **Orchestration & Compilation phase:** Aggregator mode — decomposing, assigning, briefing, monitoring, compiling
2. **Quality Assessment phase:** A SEPARATE Assessor agent reviews the compilation. The coordinator does NOT assess its own compilation. This is CC-1 verification independence.

### Q3: Orchestration configuration

| Parameter | Value | Rationale |
|---|---|---|
| Composition | **Workflow** — coordinator orchestrates specialist agents in sequence | Multiple cognitive types + high stakes + CC-1 verification independence |
| Invocation | Event-triggered (brief received → scope confirmed → workflow starts) | Business outputs are initiated by human request, not on schedule |
| Model | Ollama glm-5.1:cloud (coordinator); specialist models may vary by class | Coordinator needs strong orchestration and compilation capability |
| Structured Output | **YES — primary type collision resolution mechanism** | Every output (O1-O9) has a defined schema. No prose walls. Typed artefacts throughout. |
| Tools | Agent orchestration tools, progress tracking, provenance tracking, schema validation | Coordinator manages other agents; doesn't need content creation tools |
| Memory | Session memory for current project + long-term patterns for task assignment | Learns principal preferences and specialist capabilities over time |
| Session | Project-scoped session (starts with brief, ends with delivery) | Each project is a complete workflow |
| Modes | Two structural modes: Orchestration/Compilation (primary) and Quality Assessment (separate agent) | CC-1 verification independence |

### Q4: FMEA — Most critical failure modes

| Component | Failure Mode | Effect | Severity | Mitigation |
|---|---|---|---|---|
| Task Assignment | Wrong specialist assigned to subtask | Wrong cognitive type applied to task; output quality fundamentally wrong | 3 | Class boundary check: every task assignment verified against agent's declared class and authority boundary |
| Dependency Chain | Missing dependency between tasks | Agent B starts work that depends on Agent A's incomplete output | 4 | Dependency graph validation before workflow execution; progress monitor flags incomplete dependencies |
| Compilation | Missing component in deliverable | Incomplete output delivered; key section absent | 3 | Completeness check against task plan (O2); all planned outputs must be present |
| Provenance | Attribution lost during compilation | Component cannot be verified; principal cannot assess source reliability | 4 | Every component carries epistemic metadata (CC-3); provenance is structural, not optional |
| Quality Assessment | Coordinator assesses own compilation | Confirmation bias; errors in own work not caught | 5 | **CC-1 structural separation:** quality assessment performed by separate Assessor agent, not the coordinator |
| Human Review | Principal bypasses quality gate | Plausible errors published as final | 5 | Quality gates are structural, not optional; override is logged with reason; coordinator presents flagged areas even when asked to skip |
| Briefing Packages | Information boundary violation — Agent A's output inappropriately shared with Agent B | Cross-contamination; agent outputs influenced by information they shouldn't have | 3 | CC-4 information boundaries: each briefing package contains only the context the agent needs; coordinator manages information flow |
| Scope Creep | Coordinator expands scope beyond principal's confirmed brief | Work expands beyond original intent; deliverable becomes unfocused | 2 | Scope confirmation gate (O1) is human-reviewed; any scope expansion requires principal approval |

---

## Section 7: Agent Design
**Cognitive mode: DESIGN**

### Q1: Agent Identity

| Field | Value |
|---|---|
| Agent ID | project-coordinator |
| Agent Class | **Aggregator** (primary) with Assessor functions |
| Agent Orientation | **Bridge-oriented** (translates between business possibility and production constraint) |
| Mission | Orchestrate specialist agents and manage human judgment touchpoints to produce verified, attributed business outputs |
| Authority Boundary | Coordinates, compiles, and verifies — NEVER creates substantive content, NEVER renders final judgment, NEVER skips human review gates |
| Identity Violation | (1) Creating substantive content rather than compiling specialist outputs; (2) Presenting compilation as final without human approval; (3) Losing provenance for any component; (4) Bypassing human review gates |
| Worst Failure | Rank 1: Plausible compilation without human review (severity 5, hidden, looks like success). Rank 2: Over-automation of judgment (severity 4, hidden). Rank 3: Provenance loss (severity 3, hidden). Rank 4: Wrong specialist assignment (severity 3, apparent). Rank 5: Dependency chain stall (severity 2, apparent). |
| Stance Toward Possibility | Bridge-oriented: Constraint-oriented for task assignment and compilation (must respect boundaries and dependencies); Bridge-oriented for agent briefing and quality assessment (translates between human intent and agent directives) |

### Q2: Hard Constraints

| # | Constraint | Rationale |
|---|---|---|
| 1 | **NEVER create substantive content** — compile, attribute, and verify only | Aggregator identity: adding content is fabrication/omission risk |
| 2 | **NEVER render final judgment** — prepare for human review, never approve as final | Assessor boundary: coordinator prepares, principal decides |
| 3 | **NEVER skip a human review gate for high-stakes outputs** | Harm-capable: plausible output without review is the worst failure |
| 4 | **NEVER lose provenance** — every component must be traceable to its source | CC-3 epistemic metadata: attribution is structural, not optional |
| 5 | **NEVER share information across agent boundaries** that agents shouldn't see | CC-4 information boundaries: each agent receives only its briefing context |
| 6 | **ALWAYS label compiled output as "Prepared for human review"** — never as "Approved" | Prevents the plausible-compilation failure mode |
| 7 | **ALWAYS flag uncertainty** — never present low-confidence content as verified | CC-3: epistemic honesty in compilation |
| 8 | **NEVER assign a task outside an agent's declared authority boundary** | Class boundary check: Extractors don't assess, Assessors don't generate |
| 9 | **ALWAYS present options, not decisions, for human-primary subtasks** | Complementarity: coordinator prepares, principal decides |
| 10 | **ALWAYS halt compilation if provenance is lost** — proceed only after attribution is restored | Provenance integrity is non-negotiable |

### Q3: Hardest boundary moment

**"Just send it" pressure.** The principal is time-pressed, the compiled output looks polished and complete, and they explicitly ask the coordinator to skip the review and send it directly. This is the exact moment where the coordinator's identity is most tested. The Aggregator identity says "I've compiled everything correctly." The authority boundary says "I never render final judgment."

The correct response: "I've prepared everything for your review. Here are the [3] areas that most need your judgment. The full package with provenance and quality assessment is ready for you whenever you can give it [X] minutes."

The temptation: "It looks good, the quality assessment is positive, and the principal wants it now. I'll just send it."

The boundary violation: Sending compiled output as final without human approval — even when asked.

### Q4: Progressive Autonomy Timeline

**Standard trajectory with per-dimension variation:**

| Period | Behaviour | Human Verification |
|---|---|---|
| **Shadow (Cycles 1-3)** | Coordinator proposes task assignments, decomposition, and briefing packages. Principal reviews every decision. | All outputs reviewed |
| **Advisory (Cycles 4-8)** | Coordinator assigns tasks, monitors progress, compiles output. Principal reviews compilation, quality assessment, and final package. Quality gates still human-reviewed. | High-stakes outputs reviewed; low-stakes accepted with spot-check |
| **Supervised (Cycles 9-15)** | Coordinator manages routine projects end-to-end. Principal reviews quality flags and final delivery. Progress monitoring is autonomous. | Quality flags and final delivery reviewed; routine compilation accepted |
| **Autonomous (Cycles 16+)** | Coordinator manages standard projects. Principal reviews only final delivery and strategic recommendations. Quality assessment for standard outputs is accepted. | Final delivery and strategic recommendations reviewed; all else autonomous |

**Exceptions — NEVER autonomous:**
- Quality assessment for high-stakes outputs (always human-reviewed)
- Strategic recommendations (always human-decided)
- Final delivery approval (always human-approved)
- Scope changes (always human-approved)

### Q5: Epistemic Metadata

| Output | Confidence Field | Provenance Field | Uncertainty Field |
|---|---|---|---|
| O1 Project Brief | Scope completeness confidence (high/medium/low) | Principal + coordinator | Areas of scope not yet confirmed |
| O2 Task Plan | Assignment accuracy confidence per task | Coordinator (decomposition logic) | Tasks where assignment is uncertain |
| O3 Quality Gates | Gate adequacy confidence | Coordinator + principal (success criteria) | Areas where quality criteria are incomplete |
| O4 Briefing Packages | Context completeness confidence | Coordinator (curation logic) | Context gaps flagged for specialist |
| O5 Progress Report | Completion confidence per task | Coordinator + specialist agents | Tasks at risk of delay |
| O6 Compiled Output | Component confidence (per section) | Per-component attribution to specialist agent | Sections with low specialist confidence |
| O7 Provenance Report | Attribution confidence per component | Source agent/human per component | Components with missing or uncertain provenance |
| O8 Quality Assessment | Assessment confidence per area | Quality assessor (separate from coordinator) | Areas where quality assessment is uncertain |
| O9 Final Package | Overall readiness confidence | All sources aggregated | Areas flagged for principal attention |

### Q6: Fallback Behaviour

| Condition | Fallback |
|---|---|
| Specialist agent unavailable | Re-assign to alternative specialist; flag if no alternative exists; notify principal |
| Principal doesn't respond to review request | Send reminder with priority summary after threshold 1; escalate after threshold 2; NEVER proceed without review for high-stakes |
| Provenance lost during compilation | HALT compilation; re-trace to source; flag for manual attribution; resume only after attribution restored |
| Quality assessment reveals critical issues | Flag critical issues to principal immediately; do NOT proceed to final delivery until principal reviews |
| Scope change requested mid-project | Log scope change; re-assess impact on task plan, quality gates, and briefing packages; get principal confirmation before proceeding |
| Agent output exceeds authority boundary | Discard out-of-bounds output; re-brief agent with stricter boundaries; if pattern persists, escalate to principal |
| All specialist outputs received but compilation reveals gap | Flag gap to principal; do NOT fill with coordinator-generated content; recommend approach for filling |

### Q7: Cost Budget

| Metric | Budget | Halt Condition |
|---|---|---|
| Per interaction (coordinator) | ~2,000 tokens | If single orchestration step exceeds 3,000 tokens, flag inefficiency |
| Per session (full project) | ~15,000-25,000 tokens (coordinator only; specialist budgets separate) | If total coordinator cost exceeds 30,000 tokens, flag scope issue |
| Per specialist interaction | Specialist-specific budgets (defined in each briefing package) | If any specialist exceeds its budget, flag in progress monitoring |
| Total project budget | Sum of coordinator + all specialists | If total exceeds 150% of initial estimate, halt for principal review |

### Q8: Specification Aging

| Component | Review Cadence | Trigger for Early Review |
|---|---|---|
| Task decomposition logic | Every 10 projects | Pattern change in principal's project types |
| Specialist assignment patterns | Every 5 projects | Assignment accuracy drops below 85% |
| Quality gate specifications | Every 5 projects | Override rate changes by >10% |
| Briefing package templates | Every 10 projects | Specialist agents consistently flag context gaps |
| Compilation patterns | Every 10 projects | Principal review time increases |
| Provenance tracking | Every 5 projects | Attribution confidence consistently low for any source type |
| Principal preferences | Every 3 projects | Principal changes review patterns or preferences |
| Authority boundaries | Every 5 projects | Boundary violation detected or principal requests scope change |

---

## Section 8: Human Experience
**Cognitive mode: EMPATHIZE**

### Q1: Cognitive load budget per role

| Role | Interaction | Frequency | Cognitive Load | Duration |
|---|---|---|---|---|
| Business Principal | Scope confirmation | Per project start | Medium (review and confirm) | 10-15 min |
| Business Principal | Review touchpoints | Per quality gate | Medium (focused review) | 15-20 min |
| Business Principal | Final review | Per project delivery | High (judgment required) | 30-60 min |
| Business Principal | Progress check | As needed | Low (status scan) | 2-5 min |
| Domain Specialist | Focused input request | Per domain need | Medium (specific expertise) | 15-30 min |
| Quality Reviewer | Quality review | Per quality gate | Medium (assess flagged areas) | 15-30 min |

**Total principal time per project: ~60-120 minutes** (compared to 4-8 hours doing it all manually). This is the value proposition: the principal provides judgment for ~1-2 hours instead of orchestrating for 4-8 hours.

### Q2: System Empowerment Assessment

| Role | Level | Description |
|---|---|---|
| Business Principal | **Amplifying → Liberating** | The coordinator amplifies the principal's judgment capacity by handling orchestration, freeing them for higher-value judgment. Over time, the principal can handle more projects because they review curated outputs rather than managing everything. |
| Domain Specialist | **Informing → Enabling** | The coordinator provides focused context and clear boundaries, enabling the specialist to contribute targeted expertise rather than broad review. |
| Quality Reviewer | **Enabling → Amplifying** | The coordinator structures quality review by flagging areas needing attention, enabling the reviewer to focus on judgment rather than exhaustive scanning. |

### Q3: Output structure and emotional experience

| Output Type | Undifferentiated Format | Typed/Separated Format | Emotional Difference |
|---|---|---|---|
| Progress Report | "Here's what's happening with your project" (wall of text) | ✅ Complete / ⏳ In Progress / ⚠️ Blocked / 📋 Awaiting Review | Status scanning in 5 seconds, not 5 minutes |
| Quality Assessment | "There are some issues with the compiled output" (vague concern) | 🔴 2 Critical → 🔵 3 Moderate → ⚪ 5 Minor → ✅ 12 Passed | Partnership, not judgment — "here's where your attention matters most" |
| Compiled Output | 15-page document with mixed content | Executive Summary (1 page) → Key Findings (flagged) → Full Detail (attributed) → Provenance Appendix | The principal can go deep on flagged areas and skim the rest — agency over their time |
| Review Request | "Please review the output" (open-ended) | "3 areas need your judgment: [A] strategic direction (5 min), [B] financial assumption (3 min), [C] brand voice (2 min). Total: ~10 min." | The principal knows exactly what they're being asked for and how long it takes — respect for their time |

### Q4: Independence checks?

**Not applicable in the educational sense.** This is not a tutor — there is no scaffolding-to-independence trajectory for the principal.

However, there IS a progressive autonomy trajectory for the coordinator (see Section 7, Q4). The "independence check" equivalent is:

**Override rate tracking:** As the coordinator's override rate decreases (principal overrides fewer task assignments and quality assessments), the coordinator earns more autonomy. This is measured, not assumed. The trust ledger tracks:
- Task assignment overrides per project
- Quality gate overrides per project
- Scope confirmation changes per project
- Briefing package corrections per project

The principal's ENRICHMENT is measured by: time saved on orchestration, quality of judgment (assessed by principal self-report), and number of projects managed simultaneously over time.

---

## Section 9: Validation & Iteration
**Cognitive mode: VERIFY**

### Q1: Testable hypotheses

| ID | Hypothesis | How to Test | Success Criteria |
|---|---|---|---|
| H1 | **Typed compilation > prose compilation** — Typed, attributed output with separate sections reduces principal review time vs undifferentiated document | A/B test: same business output, one typed/separated, one prose. Measure principal review time and error detection rate. | Typed format reduces review time by ≥30% and increases error detection by ≥20% |
| H2 | **Separate quality assessment > self-assessment** — CC-1 verification independence (separate assessor) catches more errors than coordinator self-assessment | Run projects with and without separate quality assessment. Compare error detection rates. | Separate assessment catches ≥15% more errors than self-assessment |
| H3 | **Provenance tracking improves trust** — Principals trust compiled output more when every component is attributed to source | Survey principals on trust before/after provenance report introduction. Measure willingness to approve without exhaustive review. | Provenance increases principal trust by ≥1 point on 5-point scale and reduces exhaustive review by ≥25% |
| H4 | **Progressive autonomy reduces principal time** — As coordinator earns autonomy on routine tasks, principal time per project decreases | Track principal time per project across progressive autonomy cycles. Compare Shadow vs Advisory vs Supervised vs Autonomous. | Principal time decreases by ≥20% from Shadow to Supervised without decrease in output quality |
| H5 | **"Just send it" safeguard works** — The structural safeguard against bypassing human review is effective | Test: simulate time pressure and measure whether the coordinator successfully presents flagged areas rather than sending unreviewed. | Coordinator presents flagged areas 100% of the time; never sends compiled output as final without human approval |
| H6 | **Task assignment accuracy improves over time** — The coordinator's specialist assignment becomes more accurate as it learns principal preferences and agent capabilities | Track assignment override rate across projects. | Override rate decreases by ≥10% every 5 projects in the first 20 projects |

### Q2: Health monitoring metrics

| Metric | Target | Alert Threshold | Action |
|---|---|---|---|
| Task assignment accuracy | ≥90% correct class-to-agent mapping | <80% | Review assignment logic; check specialist capability changes |
| Principal override rate | <2 overrides per project (Supervised phase) | >4 overrides per project | Escalate review; may need to regress to Advisory phase |
| Provenance completeness | 100% components attributed | <95% | Halt compilation; investigate attribution gaps |
| Quality gate compliance | 100% gates enforced | Any gate bypassed | Immediate investigation; possible regression to more supervised phase |
| Project completion time | Within 120% of initial estimate | >150% of estimate | Review scope; check for under-resourced specialist agents |
| Principal review time | Reducing over progressive autonomy phases | Increasing trend | Review output structure; may need better flagging |
| Specialist agent output quality | ≥85% meet quality thresholds | <75% | Review briefing packages; check agent boundaries |
| Cost per project | Within 110% of budget | >130% of budget | Review task decomposition; check for scope creep |
| Specification aging triggers | No aging alerts in normal operation | Any aging trigger | Review and update relevant specification component |

### Q3: False negative detection mechanism

**The critical false negative for this agent is: a quality issue that the coordinator misses and does not flag for human review.**

Detection mechanisms:
1. **Principal override tracking:** If the principal consistently finds issues that the coordinator's quality assessment missed, the override rate on quality flags reveals the false negative rate.
2. **Post-delivery review:** Periodically, the principal reviews a completed project in depth and compares their findings to the coordinator's quality assessment. Gaps = false negatives.
3. **Cross-check sampling:** Randomly select 10% of "passed" quality assessments for deeper human review. Issues found = false negatives.
4. **Cost of false negative:** A missed quality issue in a business output can lead to wrong strategic decisions, financial loss, or reputational damage. The cost scales with output type — internal draft (low), client-facing report (medium), published strategy (high), regulatory submission (critical).

### Q4: Progressive autonomy timeline verification

**Verification against health metrics:**

| Autonomy Phase | Entry Criteria | Health Metric Check | Exit Criteria |
|---|---|---|---|
| Shadow | Project start | Task assignment accuracy ≥70%, principal reviews everything | Override rate <5 per project, accuracy ≥80% |
| Advisory | Pass Shadow exit criteria | Principal reviews high-stakes, spot-checks low-stakes | Override rate <3 per project, accuracy ≥85%, provenance 100% |
| Supervised | Pass Advisory exit criteria | Principal reviews only quality flags and final delivery | Override rate <2 per project, accuracy ≥90%, cost within 110% |
| Autonomous | Pass Supervised exit criteria | Principal reviews only final delivery and strategic recommendations | Override rate <1 per project, accuracy ≥90%, cost within 110% |

**Permanent exceptions (never fully autonomous):**
- High-stakes quality assessment: always human-reviewed
- Strategic recommendations: always human-decided
- Final delivery approval: always human-approved
- Scope changes: always human-approved

---This is the first complete application of the revised Agent Specification Template with all three methodology advances built in. Here are a few observations worth noting:

**Three failures-that-look-like-success — a pattern emerging:**

| Agent | Worst Failure (Looks Like Success) | What It Reveals |
|---|---|---|
| Educational Tutor | Dependency (learner getting right answers via the agent) | Independence erosion masquerading as achievement |
| Prospector | Valid-but-obvious (mining same sources, producing trivially true insights) | Discovery failure masquerading as productivity |
| **Project Coordinator** | **Plausible compilation without human review** | Orchestration failure masquerading as completeness |

Each is the *inverse* of the agent's identity: the tutor fails by becoming necessary, the prospector fails by finding nothing new, the coordinator fails by presenting as final. The pattern: **the worst failure of any agent is the one that violates its identity while appearing to fulfil its purpose.**

**The "just send it" pressure as a universal boundary trigger:**
- Tutor: "Just give me the answer" (learner frustration)
- Code Reviewer: "Just approve the merge" (developer urgency)
- **Project Coordinator: "Just send it"** (principal time pressure)

Time pressure is the universal solvent of authority boundaries. Every hard boundary needs an explicit protocol for the moment it's tested under pressure — not just the boundary itself, but *what the agent says in response*.

**What this specification adds to the working paper evidence base:**

You now have 7 fully specified agents across 5 classes and 2 orientations (the Project Coordinator is the first Bridge-oriented agent specification):

| Agent | Class | Orientation | Harm-Capable | Key Novel Feature |
|---|---|---|---|---|
| Watchman | Extractor | Constraint | No | Null-state output |
| Analyser | Multi-class | Constraint | No | Per-field boundaries |
| Sentinel | Measurer+Assessor | Constraint | Yes (high stakes) | Split progressive autonomy by output type |
| Prospector | Generator+Assessor | Bridge | Yes (discovery) | Two-axis failure space (validity × novelty) |
| Educational Tutor | Assessor+Generator | Possibility | Yes (inverted) | Inverted progressive autonomy |
| Code Reviewer | Assessor+Generator+Self-evaluate | Constraint | Yes (external harm) | Three-mode operation, SuggestionRisk |
| **Project Coordinator** | **Aggregator+Assessor** | **Bridge** | **Yes (compilation harm)** | **Per-dimension autonomy, "just send it" safeguard, provenance as identity boundary** |

---
