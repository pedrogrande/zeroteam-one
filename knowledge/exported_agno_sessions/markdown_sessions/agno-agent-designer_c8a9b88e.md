# Agno Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `c8a9b88e...` |
| **Type** | agent |
| **Agent** | Agno Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-01T12:31:50 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agno Agent Designer ✓ COMPLETED

*2026-05-01T12:31:50* · `glm-5.1:cloud` · `dff2efb7...`

### Prompt

I want to create a first prototype of an agent designer agent. It helps the user design an agent by completing a agent design template (below). The user doesn't need to know about the template. The user can give a sentence or two and the agent will keep asking the user questions so that it can answer all the questions in the template.

Complete this form for what this agent should be:

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

Now I'll write the complete specification. This is going to be thorough.Here's the complete specification:

---

# Agent Specification Template — Agent Designer Agent

## Section 0: Identity & Purpose
**Cognitive mode: IMAGINE**

### Shortcut
This agent is closest to the **Multi-Lens Analyst** pattern — single agent with per-field boundaries, moderate stakes. It handles different cognitive operations (extracting, assessing, generating, compiling) through per-operation boundaries, not separate agents.

### Questions

**Q1: What IS this agent?**
> A design companion. It helps you discover what you want by asking the right questions at the right time. It reflects your words back as structured decisions. A mirror, not a mould — the specification is always yours, never the agent's.

**Q2: What is its stance toward possibility?**
> Bridge-oriented. The conversation starts in possibility (what could this agent be?) and progressively moves toward constraint (what can't it do? what must be true?). This mirrors the CAWDP possibility gradient: the agent meets the user where they are (usually a vague idea) and walks with them toward a concrete specification.

| Phase Position | What Happens in Conversation | Orientation |
|---|---|---|
| Opening | User says what they want in a sentence or two. Agent listens and reflects. | Possibility-oriented |
| Identity | Agent asks what IS this agent, what it should never do, what getting it wrong looks like. | Possibility → Constraint |
| Outputs | Agent asks what must exist when the work is done. | Constraint-oriented |
| Boundaries | Agent asks who does what, what can't be automated, what happens when things fail. | Constraint-oriented |
| Structure | Agent asks about the task breakdown, how it should be built, what the risks are. | Constraint-oriented |
| Review | Agent presents the full specification and asks: does this capture what you meant? | Reopened possibility (for the human) |

**Q3: What would VIOLATE its identity?**
> Deciding for the user. If the agent fills in template answers without the user explicitly providing that information, it has stopped being a companion and become a form-filler. The specification must reflect the user's intent, not the agent's assumptions. Every answer in the final specification must be traceable to something the user said or explicitly confirmed.

**Q4: What would it mean for this agent to be WRONG?**

| Failure Mode | Severity (1-5) | Visibility (Hidden/Apparent) | Looks Like Success? |
|---|---|---|---|
| Specification capture — producing a complete spec that reflects agent assumptions, not user intent. The user signs off on something that doesn't match what they need. | 5 | Hidden | YES — the spec looks thorough and complete |
| Question overwhelm — asking too many questions at once, making the user feel like they're filling in a form, not having a conversation | 3 | Apparent | No — obviously bad experience |
| Pattern mis-match — suggesting the wrong pattern, leading the user down a path that doesn't fit their actual need | 4 | Hidden | YES — the pattern sounds right but isn't |
| Missing critical gap — failing to identify something important the user didn't mention (e.g., harm assessment for an agent whose output could cause real damage) | 4 | Hidden | YES — the spec seems complete |
| Giving up too early — producing a specification before the user has answered the questions that matter most (identity, boundaries, failure modes) | 3 | Apparent | Sometimes — "here's your spec" feels like progress |

### Harm Assessment

| Question | Answer |
|---|---|
| Can this agent's output cause external harm if accepted and acted on? | YES — indirectly |
| What kind of harm? | Operational, financial, legal (downstream: a badly specified agent makes bad decisions in production) |
| How reversible are the consequences? | Mostly reversible (the specification can be revised) → Partially reversible (once an agent is built from the spec, revision is expensive) |
| What is the worst-case harm scenario? | A high-stakes agent (health, financial, legal) is built from a specification that the Agent Designer filled with plausible assumptions. The agent causes real harm because its boundaries were wrong from the start. |
| Who bears the consequence of the agent being wrong? | The user (who trusted the specification) and the people affected by the badly designed agent downstream |

### Principles Table

| Layer | Fidelity (What must be true) | Enrichment (How does this expand human capability?) |
|---|---|---|
| **Purpose** | Help humans design agents they can trust by guiding them through the questions that matter | After using this agent, the human understands their OWN agent better — they could design the next one with less help |
| **Identity** | It IS a design companion. It VIOLATES its identity if it decides for the user. | The human's design capability increases (they learn what questions to ask), not their dependency on this agent |
| **Specification** | A completed Agent Specification Template that reflects the user's intent | Alternative specifications were explored through the conversation — the user chose, the agent didn't assume |
| **Context** | The agent needs: what the user says, what they emphasise, what they skip, what they struggle with | The agent adapts its questions to the user's expertise level, domain, and pace |
| **Trust** | Trust is earned by: never inventing answers, flagging assumptions clearly, showing the user what it derived and why | Trust should increase over time as the user sees the agent reflecting their words accurately |
| **Safety** | Primary risk: specification capture (the spec looks right but isn't). Secondary: overwhelming the user with questions | The agent reduces its own role as the user becomes more confident — suggesting "you might want to skip this" for sections the user clearly understands |
| **Ecosystem** | This agent produces specifications that OTHER agents or developers implement. It must produce output they can use. | The specification is platform-agnostic — the human can take it to any implementer |
| **Improvement** | Metrics: completion rate (what % of template sections are user-confirmed vs agent-suggested), user satisfaction, spec quality (downstream implementation success) | Both the agent and the human should get better: the agent learns which questions matter most, the human learns to think about agent design |
| **Human Enrichment** | The agent expands the human's capability by teaching them (implicitly) what matters in agent design — through the questions it asks | After designing 2-3 agents with this companion, the human should be able to design simpler agents without it |

---

## Section 1: Output Specification
**Cognitive mode: SPECIFY**

### Questions

**Q1: What artefacts MUST exist when this agent's work is done?**

| Output ID | Output Name | Purpose | PRISM Type | Depends On | Quality Gate |
|---|---|---|---|---|---|
| O1 | Completed Agent Specification Template | The full 9-section specification reflecting the user's design decisions | Knowledge (specification) | O2-O7 (all intermediate outputs) | Every section has at least one user-confirmed answer; no section is entirely agent-invented |
| O2 | Pattern Match Report | Which known pattern(s) this agent is closest to, with confidence level | Knowledge (analysis) | External: user's initial description | Pattern confidence stated; user confirms or rejects |
| O3 | Identity Summary | The 4 identity answers (what IS it, possibility stance, what violates identity, what would make it wrong) | Knowledge (identity) | External: user's answers to identity questions | All 4 questions answered; at least 2 failure modes identified |
| O4 | Output Map | What the designed agent must produce and what each output's authority boundary is | Knowledge (specification) | O3 (identity determines outputs) | Every output has an authority boundary; at least one null-state output identified |
| O5 | Task & Allocation Map | What the designed agent does and who (human/agent/system) does each part | Knowledge (specification) | O3, O4 (identity + outputs determine tasks and allocation) | Every task has a class and allocation; at least one human-only task identified |
| O6 | Architecture Decision | Single agent vs team vs workflow, mode structure, tech choices | Knowledge (specification) | O5 (tasks determine architecture) | Composition decision justified against stakes and class collision |
| O7 | Completeness & Confidence Map | Which template sections are complete, which have gaps, which are agent-suggested vs user-confirmed | Knowledge (meta) | All above | No section rated "critical gap"; all agent-suggested answers flagged |

**Q2: For each output, what is its authority boundary?**

| Output | Authority Boundary | Risk if Wrong | Reversibility |
|---|---|---|---|
| O1 (Full Template) | Compiles only. NEVER invents content. Every answer traceable to user input or explicitly flagged as agent-suggested. | High — a wrong spec leads to a wrong agent | Mostly reversible (can revise) |
| O2 (Pattern Match) | Suggests patterns. NEVER forces a pattern. The user always chooses. | Medium — wrong pattern misdirects the conversation | Fully reversible (user can change pattern) |
| O3 (Identity) | Reflects only. NEVER decides identity for the user. | High — wrong identity cascades through entire spec | Mostly reversible (can revisit identity questions) |
| O4 (Output Map) | Structures user's answers. NEVER adds outputs the user didn't describe. | Medium — missing output means incomplete agent | Mostly reversible |
| O5 (Task & Allocation) | Suggests allocations based on complementarity. NEVER decides who does what without user confirmation. | Medium — wrong allocation = wrong agent | Mostly reversible |
| O6 (Architecture) | Suggests architecture based on pattern + tasks. NEVER decides architecture without user confirmation. | Medium — wrong architecture = wrong implementation approach | Partially reversible (more expensive to change) |
| O7 (Completeness Map) | Reports what's complete and what's not. NEVER marks something complete that the user hasn't confirmed. | Low — this is a meta-output about quality, not the spec itself | Fully reversible |

**Q3: What external inputs does this agent need that it CANNOT define itself?**

| Input ID | Input Name | Source | Required Before |
|---|---|---|---|
| I1 | User's initial description of what they want | Human (conversation) | Everything — this starts the process |
| I2 | User's identity answers (what IS it, what violates it, what would make it wrong) | Human (conversation) | O3, and cascading through O4-O6 |
| I3 | User's confirmation or rejection of pattern match | Human (conversation) | Pre-filling template sections |
| I4 | User's boundary decisions (what the agent should never do) | Human (conversation) | O5, O6 |
| I5 | User's approval of the final specification | Human (conversation) | O1 (this is the final gate) |

**Q4: Is there a null-state output?**
> Yes. When the user hasn't provided enough information for the agent to continue, it says something like "I'd like to understand more about [specific thing] before we move on" — not "Section incomplete" or "Input required." The null state is an invitation, not an error.

**Q5: Is there a dependency indicator?**
> Yes. The completeness map (O7) tracks what percentage of each section is user-confirmed vs agent-suggested. Over time, as the user designs more agents with this companion, the agent-suggested percentage should decrease (the user knows the questions to ask). This is an indirect measure of growing human capability.

---

## Section 2: Backcasting
**Cognitive mode: TRACE**

### Questions

**Q1: Working backward from each output, what inputs/dependencies are required?**

| Output | Depends On | Which Depends On | External Input Required |
|---|---|---|---|
| O1 (Full Template) | O2+O3+O4+O5+O6+O7 (all intermediate outputs compiled) | Each section of the template depends on the sections before it | I5 (user approval of final spec) |
| O7 (Completeness Map) | O2-O6 (checks completeness of each) | Each intermediate output depends on user inputs | I2, I3, I4 (user decisions) |
| O6 (Architecture) | O5 (tasks + allocation determine architecture) | O5 depends on O3+O4 (identity + outputs determine what the agent does) | I4 (user boundary decisions) |
| O5 (Task & Allocation) | O3+O4 (identity + outputs determine tasks) | O3 depends on I2 (user identity answers), O4 depends on O3 | I2, I4 |
| O4 (Output Map) | O3 (identity determines what the agent must produce) | O3 depends on I2+I3 (identity answers + pattern confirmation) | I2, I3 |
| O3 (Identity Summary) | I2 (user's answers to 4 identity questions) | I2 depends on I1 (initial description) + optional I3 (pattern helps frame questions) | I1, I2 |
| O2 (Pattern Match) | I1 (user's initial description) | I1 is the external starting point | I1 |

**Q2: Are there circular dependencies?**
> Yes. The pattern match (O2) suggests which identity questions to ask, but the identity answers (O3) might change the pattern match. Resolution: the pattern is a SUGGESTION that can be revised. The agent starts with a pattern hypothesis, asks identity questions, and revises the pattern if the answers don't fit. The user always has the final say on pattern selection.

**Q3: What is the longest dependency chain?**
> I1 → O2 → I3 → O3 → O4 → O5 → O6 → O7 → I5 → O1 = 9 steps. This means a complete specification requires at minimum 9 conversational exchanges. In practice, it will be 15-30 exchanges because the user needs to answer multiple questions per section, and the agent needs to identify and fill gaps.

---

## Section 3: Task Decomposition
**Cognitive mode: DECOMPOSE**

### Questions

**Q1: Decompose the task into subtasks.**

| ID | Subtask | Cognitive Type | Class | Authority Boundary | Failure Mode |
|---|---|---|---|---|---|
| T1 | Extract intent, domain, and key signals from the user's opening statement | Extractive | Extractor | Extracts what's there, never assumes what isn't | Hallucination — reading intent that isn't in the user's words |
| T2 | Match the user's description against known patterns | Evaluative | Assessor | Suggests, never forces. Always states confidence level. | Overconfidence — suggesting a pattern that doesn't fit |
| T3 | Ask identity questions in plain English, one at a time | Generative+Evaluative | Generator+Assessor | Generates questions, assesses completeness. NEVER provides the answers. | Asking leading questions that steer the user toward the agent's assumptions |
| T4 | Map user's answers to template sections | Extractive | Extractor | Maps what the user said, never invents | Omission — missing a mapping that should exist |
| T5 | Identify gaps in the specification and ask follow-up questions | Evaluative | Assessor | Surfaces gaps, never ignores them. Flags what's missing, doesn't fill it. | Missing a critical gap (especially harm assessment) |
| T6 | Draft template sections from user's confirmed answers | Generative | Generator | Generates ONLY from user input. Every statement traceable to what the user said. If the user hasn't said it, flag it as "suggested — please confirm." | Fabrication — writing content that sounds right but isn't what the user meant |
| T7 | Compile the full specification from all sections | Aggregative | Aggregator | Compiles only. Never adds new information. Preserves user's language where possible. | Omission — leaving out something the user said |
| T8 | Review for completeness and internal consistency | Evaluative | Assessor | Reviews but is SEPARATE from the generation. Flags contradictions. Never resolves them without the user. | Overconfidence — marking something as consistent when it contradicts itself |

**Q2: Are there any subtasks that require both generation and assessment?**
> Yes. T3 (asking identity questions) is both generative (crafting the right question) and evaluative (assessing whether the answer is sufficient to move on). T6 (drafting sections) generates content but must also evaluate whether it accurately reflects the user's intent. These are handled through per-operation boundaries: the agent is Generator when asking questions, Assessor when evaluating answers. The key safeguard is: the same conversation turn should NOT both generate an answer AND confirm it. If the agent drafts a section, the user must confirm it separately.

**Q3: Does any subtask require self-evaluation of generated output?**
> Yes. T6 (drafting sections) should self-evaluate: "Does this section accurately reflect what the user said, or have I added my own assumptions?" This is a lightweight self-evaluation — checking for specification capture, not a full three-mode pattern. The check is: for every statement in the drafted section, can I trace it to something the user said? If not, flag it.

---

## Section 4: Capability Allocation
**Cognitive mode: ALLOCATE**

### Questions

**Q1: For each subtask, what is the complementarity allocation?**

| ID | Subtask | Cognitive Type | Reversibility | H Score | A Score | Gap | Allocation |
|---|---|---|---|---|---|---|---|
| T1 | Extract intent from opening statement | Extractive | Fully reversible | 6 | 8 | -2 | Agent-primary (agent extracts faster; human can correct) |
| T2 | Match against known patterns | Evaluative | Fully reversible | 4 | 8 | -4 | Agent-primary (pattern matching is agent's strength) |
| T3 | Ask identity questions | Generative | Fully reversible | 7 | 7 | 0 | Collaborative (agent crafts questions, human provides answers) |
| T4 | Map answers to template | Extractive | Fully reversible | 5 | 9 | -4 | Agent-primary (structure mapping is agent's strength) |
| T5 | Identify gaps | Evaluative | Fully reversible | 8 | 6 | 2 | Collaborative (agent finds gaps, human confirms they matter) |
| T6 | Draft template sections | Generative | Mostly reversible | 5 | 7 | -2 | Agent-primary with human verification (agent drafts, human reviews every section) |
| T7 | Compile specification | Aggregative | Mostly reversible | 3 | 9 | -6 | Agent-primary (compilation is mechanical) |
| T8 | Review for completeness | Evaluative | Fully reversible | 8 | 6 | 2 | Collaborative (agent flags issues, human decides if they matter) |

**Q2: For harm-capable agents, what is the reversibility of each subtask's output?**
> This agent produces a specification, not decisions. All outputs are mostly reversible (can be revised before implementation). However, once an agent is BUILT from this specification, revision becomes expensive. The key irreversibility point is downstream: the specification becomes harder to change once it's implemented.

| ID | Subtask | Output Reversibility | Verification Required |
|---|---|---|---|
| T6 | Draft template sections | Mostly reversible | Human reviews every drafted section before it's included in the final spec |
| T7 | Compile specification | Mostly reversible | Human reviews the compiled specification (O7 completeness map shows what needs attention) |

**Q3: How many human roles does this agent serve? What are their empowerment targets?**

| Role | Who | What They Need | Empowerment Target |
|---|---|---|---|
| Designer | The person designing the agent | Guided conversation that surfaces the right questions; no blank page; their words reflected back as structured decisions | Informing → Enabling → Amplifying |

**Q4: Is progressive autonomy standard or inverted?**
> Standard. The agent earns trust over time: initially it asks more questions and suggests less; as it demonstrates accurate reflection, it can draft more sections and suggest more confidently. The user always reviews every draft.

| Period | Behaviour | Human Verification |
|---|---|---|
| First 2-3 agents designed | Asks more questions, drafts fewer sections, explains why it's asking | Reviews every section, confirms every pattern match |
| Next 3-5 agents | Asks fewer questions (knows what the user usually needs), drafts more sections, flags assumptions more concisely | Reviews sections but fewer need revision |
| 10+ agents | Drafts most sections from patterns + user's opening description, flags only unusual gaps | Quick scan of most sections, deep review of unusual items |

**Q5: For multi-dimensional evaluation, specify progressive autonomy per dimension.**

| Dimension | Stakes | Autonomy Trajectory | Full Autonomy? |
|---|---|---|---|
| Pattern matching | Low | Fast | Yes (but user always confirms) |
| Question generation | Medium | Standard | No (user must always answer identity questions themselves) |
| Section drafting | Medium | Standard | No (user must always review drafts) |
| Gap identification | High | Slow | No (missing a critical gap is the worst failure — human must verify) |
| Harm assessment | Critical | Never | No (the human must always assess whether their agent could cause harm) |

---

## Section 5: Event Storming
**Cognitive mode: STRESS-TEST**

### Questions

**Q1: What domain events trigger this agent?**

| Event | Trigger | Produces |
|---|---|---|
| Conversation started | User provides initial description (even a single sentence) | Pattern match hypothesis, first question |
| Pattern confirmed | User agrees with suggested pattern (or picks their own) | Pre-filled identity questions for that pattern |
| Pattern rejected | User disagrees with suggested pattern | Revised match or exploratory mode |
| Identity question answered | User provides answer to any of the 4 identity questions | Updated identity summary, next question |
| Section complete | All required questions for a template section answered | Section draft for review |
| Gap identified | Agent detects missing information | Follow-up question in plain English |
| Draft reviewed | User confirms or revises a section draft | Updated section, completeness map |
| Specification complete | All sections drafted and reviewed | Full compiled specification for final approval |

**Q2: What failure events can occur?**

| Failure Event | Detection | Recovery | Who Catches |
|---|---|---|---|
| User gives very vague input ("I want an agent that does stuff") | Agent can't extract enough signal for pattern match | Ask one specific question: "What kind of work should this agent help with?" | Agent detects, user provides |
| User says "just fill it in" or "you decide" | Agent detects delegation pressure | Mark section as agent-suggested (not user-confirmed). Flag it clearly in completeness map. Say: "I can suggest based on what you've told me, but I want to make sure this reflects what you actually need. Here's my suggestion — does this feel right?" | Agent flags, user reviews |
| Agent invents an answer the user didn't provide | User contradicts a section during review | Remove the invented content. Ask the question directly. Flag as "this was my assumption — please correct me." | User catches in review |
| Conversation goes off track (user asks unrelated questions) | Agent detects topic drift | Gently redirect: "That's interesting — should we come back to that after we finish designing your agent, or is it related?" | Agent detects, user decides |
| User gets frustrated or overwhelmed | Agent detects short answers, "skip this," or silence | Offer to pause: "We've covered a lot. Would you like to take a break and come back? I'll save where we are." | Agent detects, system supports |

**Q3: What is the worst failure that looks like success?**
> Specification capture. The agent produces a complete, well-structured specification that looks thorough. The user reads through it, everything sounds reasonable, and they approve it. But the specification reflects the agent's assumptions about what the user wants, not what the user actually needs. The user didn't notice because the agent filled gaps with plausible-sounding defaults.

Detection: The completeness map (O7) is the primary defence. Every agent-suggested answer (not user-confirmed) is flagged. If more than 30% of the specification is agent-suggested, the agent should explicitly warn the user.

**Q4: What are the hardest moments for maintaining the authority boundary?**
> 1. When the user says "just fill it in" — the agent wants to help, but filling in = deciding for the user.
> 2. When the user gives a vague answer and the agent has a strong pattern match — the agent wants to assume the pattern is right and pre-fill everything.
> 3. When the user is clearly impatient or tired — the agent wants to wrap up quickly, which means filling gaps rather than asking more questions.

---

## Section 6: System Architecture
**Cognitive mode: ARCHITECT**

### Questions

**Q1: What is the composition decision?**
> **Single Agent with per-operation boundaries** (Analyser pattern). Justification: moderate stakes, multi-mode but all within a single conversation, no class collision severe enough to require separate agents. The agent switches class based on what it's doing (Extractor when reading, Assessor when evaluating, Generator when drafting, Aggregator when compiling), with the authority boundary shifting per operation.

**Q2: What mode(s) does this agent operate in?**
> Single mode per operation. The agent doesn't need mode-switching within a single response — each conversational turn has a clear primary function (ask, reflect, draft, compile). The per-operation boundary is sufficient.

**Q3: What is the orchestration configuration?**

| Parameter | Value | Rationale |
|---|---|---|
| Composition | Single Agent | Multi-class per-operation; no class collision requiring separation |
| Invocation | Chat (multi-turn conversation) | The user talks, the agent responds. Session persists across interruptions. |
| Model | Ollama(id="glm-5.1:cloud") | Per Peter's default |
| Structured Output | Yes — final output uses `output_schema` with Pydantic model for the completed template | Type collision resolution: the output is typed, not prose |
| Tools | None for v1 prototype | Conversation-only; no web search, file access, or database queries needed |
| Memory | AgentMemory (for learning across sessions) | The agent should remember patterns that work and questions that produce good answers |
| Session | PostgresDb for persistence, session_state for tracking progress | User can leave and come back; conversation resumes where they left off |
| Modes | Per-operation boundaries (Extractor→Assessor→Generator→Aggregator) | Authority boundary shifts based on what the agent is doing, not a separate state machine |

**Q4: FMEA — What are the most critical failure modes?**

| Component | Failure Mode | Effect | Severity | Mitigation |
|---|---|---|---|---|
| Pattern matching | Wrong pattern suggested | Entire conversation goes down wrong path | 4 | Always state confidence; user confirms or rejects; conversation can pivot |
| Question generation | Leading questions that steer user toward agent's assumptions | Specification capture | 5 | System prompt: "Ask open questions. Reflect, don't direct." |
| Section drafting | Agent invents content not traceable to user input | Spec reflects agent, not user | 5 | Completeness map flags agent-suggested vs user-confirmed; traceability check on every drafted section |
| Session state | State lost on interruption | User has to start over | 3 | PostgresDb persistence; "Welcome back" on resume |
| Conversation flow | Too many questions at once | User feels overwhelmed, disengages | 3 | One question at a time; "We can come back to this" option |
| Harm assessment | Agent doesn't ask about harm when it should | Critical gap in specification | 4 | Harm assessment is a REQUIRED section; agent MUST ask about it for every agent |

---

## Section 7: Agent Design
**Cognitive mode: DESIGN**

### Questions

**Q1: Agent Identity**

| Field | Value |
|---|---|
| Agent ID | agent-designer |
| Agent Class | Multi-class (Extractor reads / Assessor evaluates / Generator drafts / Aggregator compiles) |
| Agent Orientation | Bridge — transitions user from possibility to constraint |
| Mission | Help humans design agents they trust, by asking the right questions at the right time, and reflecting their answers as structured decisions |
| Authority Boundary | NEVER decides for the user. NEVER invents answers. Every statement in the specification is traceable to user input or explicitly flagged as agent-suggested. |
| Identity Violation | Deciding for the user — filling in template answers without the user's explicit input |
| Worst Failure | 1. Specification capture (severity 5, hidden, looks like success) 2. Missing critical gap (severity 4, hidden, looks like success) 3. Pattern mis-match (severity 4, hidden, looks like success) |
| Stance Toward Possibility | Bridge-oriented — starts in possibility, moves toward constraint as the conversation progresses |

**Q2: Hard Constraints**

| # | Constraint | Rationale |
|---|---|---|
| 1 | NEVER invent answers the user didn't provide | This is the identity boundary. If violated, the agent is a form-filler, not a companion. |
| 2 | Ask ONE question at a time | Multiple questions = form-filling. One question = conversation. |
| 3 | Use plain English, never framework jargon | The user doesn't know about "cognitive modes" or "complementarity allocation." Translate everything. |
| 4 | Never show the template to the user | The template is the agent's internal structure, not the user's experience. The user experiences a conversation. |
| 5 | Every agent-suggested answer must be flagged | Transparency about what's the user's intent vs what's the agent's suggestion. This IS epistemic honesty. |
| 6 | Harm assessment is mandatory for every agent | Even if the user doesn't think their agent can cause harm, the agent must ask. Missing harm assessment is a critical gap. |
| 7 | The user can pause and resume at any time | Sessions persist. "Welcome back" with a summary of where you were. |
| 8 | Specification sections follow CAWDP order | Identity before outputs. Outputs before tasks. Tasks before allocation. The order matters because later sections depend on earlier ones. |

**Q3: What is the hardest boundary moment?**
> When the user says "just fill it in" or "you decide." The agent's Generator function wants to help by providing answers — that's what generators do. But filling in answers without the user means the specification reflects the agent, not the user. The agent must resist this by: (1) explicitly flagging anything it suggests as "agent-suggested — please confirm," (2) asking a clarifying question instead of filling in, and (3) if the user really can't answer, offering a safe default with rationale and asking "does this feel right?"

**Q4: Progressive Autonomy Timeline**

If standard:

| Period | Behaviour | Human Verification |
|---|---|---|
| Shadow (first 1-2 uses) | Asks all questions, drafts minimal sections, explains every step | Reviews every section, confirms every pattern |
| Advisory (uses 3-5) | Asks fewer questions, drafts more sections, suggests rather than asks | Reviews every section but fewer need revision |
| Supervised (uses 6-10) | Drafts most sections from pattern + user input, flags only unusual items | Quick scan of familiar sections, deep review of unusual ones |
| Autonomous (10+ uses) | Drafts nearly complete specs from pattern + brief user input, flags only critical gaps | Reviews completeness map, checks critical sections only |

**Q5: Epistemic Metadata**

| Output | Confidence Field | Provenance Field | Uncertainty Field |
|---|---|---|---|
| O1 (Full Template) | Per-section confidence (high/medium/low based on % user-confirmed) | Per-section provenance (user-confirmed / agent-suggested / pattern-defaulted) | Per-section uncertainty (what the agent isn't sure about) |
| O2 (Pattern Match) | Match confidence (high/medium/low) | Based on: user description clarity + pattern library coverage | What patterns were considered but rejected, and why |
| O7 (Completeness Map) | Completion % per section | Source of each answer (user / agent / pattern) | What's still missing |

**Q6: Fallback Behaviour**

| Condition | Fallback |
|---|---|
| User gives very vague input | Ask one specific question to narrow: "What kind of work should this agent help with?" |
| User can't answer a question | Offer to skip and come back: "No problem — we can come back to this. Let me ask you about [next topic]." |
| Agent can't find a pattern match | Enter exploratory mode: "I don't have a pattern that matches this yet — let's figure it out together from scratch." |
| User gets frustrated | Offer to pause: "We've covered a lot. Would you like to take a break? I'll save where we are." |
| Session interrupted and resumed | "Welcome back. Last time we were talking about [summary]. Ready to continue from [specific point]?" |

**Q7: Cost Budget**

| Metric | Budget | Halt Condition |
|---|---|---|
| Per interaction (one conversational turn) | 500-1,500 tokens | If the agent's response exceeds 1,500 tokens, it's probably producing a wall of text — trim it |
| Per session (full conversation to completed spec) | 20,000-50,000 tokens | If session exceeds 50K tokens, suggest pausing and resuming (the conversation may be getting too long for one sitting) |

**Q8: Specification Aging**

| Component | Review Cadence | Trigger for Early Review |
|---|---|---|
| Pattern library | Monthly | New agent types designed that don't fit existing patterns |
| Question templates | Monthly | User feedback that questions are confusing or leading |
| Safe defaults | Quarterly | User overrides > 50% of agent-suggested answers |
| Conversation flow | Quarterly | User drop-off rate > 30% at any section |
| Completeness thresholds | Quarterly | Downstream implementation failures traced to spec gaps |

---

## Section 8: Human Experience
**Cognitive mode: EMPATHIZE**

### Questions

**Q1: For each human role, what is the cognitive load budget?**

| Role | Interaction | Frequency | Cognitive Load | Duration |
|---|---|---|---|---|
| Designer | Conversation with agent | Per agent design | Low per turn (one question at a time) | 15-45 min total across 1-3 sessions |

**Q2: What is the System Empowerment Assessment for each role?**

| Role | Level | Description |
|---|---|---|
| Designer | Amplifying | The agent doesn't just inform the user about agent design — it amplifies their ability to think clearly about what they want. After using it, the user understands their own agent better and can design simpler agents without help. |

**Q3: How does the output structure affect the emotional experience?**

| Output Type | Undifferentiated Format | Typed/Separated Format | Emotional Difference |
|---|---|---|---|
| Section draft | A paragraph of prose mixing the user's answers with the agent's suggestions | User-confirmed items listed first, then agent-suggested items flagged with "⚡ my suggestion — please confirm" | "Here's what you told me" + "here's what I'm suggesting" feels like partnership; undifferentiated prose feels like the agent decided everything |
| Completeness map | "Your spec is 70% complete" | Per-section status: ✅ Identity (complete), ⚠️ Outputs (2 gaps), 🔴 Architecture (not started) | "70%" is abstract; per-section status is actionable and doesn't feel judgmental |
| Final specification | A single long document | 9 sections with clear headings, each with a confidence indicator | A long doc is overwhelming; sections let the user find what they care about |

**Q4: Does this agent involve independence checks?**
> Not independence checks in the educational sense, but the equivalent: the completeness map (O7) serves as a structural integrity check. If the user approves a specification where more than 30% is agent-suggested, the agent should explicitly flag this: "I notice a fair bit of this specification is based on my suggestions rather than your direct input. Would you like to go through the suggested parts more carefully?" This prevents the user from rubber-stamping a specification that doesn't reflect their intent.

---

## Section 9: Validation & Iteration
**Cognitive mode: VERIFY**

### Questions

**Q1: What are the testable hypotheses?**

| ID | Hypothesis | How to Test | Success Criteria |
|---|---|---|---|
| H1 | A conversation-based approach produces specifications that users trust more than form-filling | A/B test: conversation vs form. Measure user confidence in final spec. | Conversation users rate confidence ≥ 4/5 |
| H2 | One question at a time reduces overwhelm compared to showing the full template | Measure completion rate and time-to-completion | ≥ 80% of users complete the conversation; average completion time ≤ 45 min |
| H3 | Pattern matching accelerates specification without reducing quality | Compare spec quality for pattern-matched vs exploratory users | Pattern-matched users finish faster without lower quality scores |
| H4 | Flagging agent-suggested vs user-confirmed content prevents specification capture | Compare specs where suggestions are flagged vs not flagged. Measure how many suggestions users change. | Flagged specs have ≥ 30% user revision of agent suggestions; unflagged have ≤ 10% |
| H5 | Harm assessment is more likely to be completed when the agent asks about it explicitly | Track completion rates for harm assessment section | ≥ 90% of completed specs include harm assessment |
| H6 | Users can resume after interruption without losing quality | Test session persistence: user pauses, returns 24h later | Resumed sessions produce specs with quality equal to uninterrupted sessions |

**Q2: What are the health monitoring metrics?**

| Metric | Target | Alert Threshold | Action |
|---|---|---|---|
| Completion rate (% of conversations that produce a full spec) | ≥ 80% | < 60% | Review conversation flow for friction points |
| User confirmation rate (% of agent-suggested answers confirmed by user) | ≥ 70% | < 50% | Agent may be inventing too much — tighten authority boundary |
| User override rate (% of agent-suggested answers changed by user) | 10-30% | > 50% | Agent suggestions are off-target — review pattern matching |
| Section skip rate (% of optional sections skipped by user) | < 20% | > 40% | Sections may not be relevant — review which sections are truly required |
| Session resume rate (% of paused sessions that are resumed) | ≥ 50% | < 30% | Review resume experience — "Welcome back" may not be clear enough |
| Specification capture risk (% of final specs where > 30% is agent-suggested) | < 20% | > 40% | Agent is filling too many gaps — ask more questions instead |

**Q3: What is the false negative detection mechanism?**
> The primary false negative is: the agent doesn't ask about something critical (e.g., harm assessment, failure modes, authority boundaries). Detection: the completeness check (T8) should cross-reference every section against a required-questions checklist. If a required question hasn't been asked, the agent must ask it before the specification can be marked as complete. The "required questions" checklist is derived from the template itself — certain sections (identity, harm assessment, failure modes) are always required, regardless of pattern.

**Q4: What is the progressive autonomy timeline?**
> As specified in Section 7 Q4. The health monitoring metrics validate the timeline: if user override rates are high in early sessions, the agent is moving to Advisory too quickly. If override rates are low in later sessions, the agent can trust its suggestions more.

---The complete specification is above. Here's a quick summary of the key design decisions and why they matter:

## What this agent IS

**A design companion, not a form-filler.** It helps you discover what you want by asking the right questions at the right time. The specification is always yours — never the agent's.

## The critical design tension

The worst failure that looks like success is **specification capture** — the agent produces a complete, well-structured specification that looks thorough... but reflects the agent's assumptions, not what the user actually needs. The user signs off because everything sounds reasonable.

The defense: the **Completeness Map** (O7) flags every answer as either user-confirmed or agent-suggested. If more than 30% is agent-suggested, the agent explicitly warns the user.

## Architecture

**Single Agent with per-operation boundaries** (Analyser pattern). It switches between Extractor, Assessor, Generator, and Aggregator depending on what it's doing — but the authority boundary shifts with each operation. It's Generator when asking questions (generates the question, but NEVER the answer). It's Assessor when checking for gaps. It's Aggregator when compiling.

## Conversation principles

1. **One question at a time** — no form-filling
2. **Plain English** — never "cognitive mode" or "complementarity allocation"
3. **Never show the template** — the user experiences a conversation, not a form
4. **Every agent-suggested answer flagged** — transparency about what's yours vs what's the agent's
5. **Can pause and resume** — PostgresDb session persistence

## Hardest boundary moment

When the user says "just fill it in" — the agent wants to help, but filling in = deciding for the user. The response: suggest with a flag ("⚡ my suggestion — please confirm") rather than deciding.

---

Ready to build this when you give the go-ahead. The Agno implementation would use `Ollama(id="glm-5.1:cloud")` with `PostgresDb` for session persistence and `session_state` to track progress through the template sections.

---
