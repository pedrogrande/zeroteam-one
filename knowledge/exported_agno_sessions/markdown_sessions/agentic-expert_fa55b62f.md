# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `fa55b62f...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-06T14:33:47 |
| **Runs** | 4 completed / 4 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-06T14:33:47* · `glm-5:cloud` · `76c6fc91...`

### Prompt

Consider the principles below and show how they map to Agno agents:

# Agent Design Principles v0.2

***

## The Core Premise

Before any design decision, three commitments need to be made explicit:

1. **Trustworthiness comes from structure, not identity.** An agent is trusted not because of what it is, but because of how it was built, constrained, and verified. Every element of the framework should enforce this structurally, not declaratively.

2. **Performance is a system property, not an agent property.** Excellence emerges from the relationship between the agent, its specification, its tools, its verifiers, its ecosystem, and its improvement loops. No single layer is sufficient alone.

3. **The framework has two axes of excellence, not one.** The first axis is **output fidelity** — did the agent produce the right thing? The second is **epistemic enrichment** — did the interaction make anyone more capable? An agent system can score perfectly on the first axis and zero on the second. That is a competent but ultimately brittle system — one that produces correct outputs today but accumulates no wisdom, leaves humans more dependent rather than more capable, and fails silently when task types shift outside its validated range. Every layer below addresses both axes.

***

## Layer 1: Purpose

*Why does this agent exist?*

This layer is answered before anything else. Every subsequent design decision should be traceable back to it.

* **Human intent** — what human need does this agent serve? A technically correct agent that causes harm, concentrates power, or diminishes human agency has failed regardless of its output quality

* **Human development** — what does the human gain in capability, understanding, or perspective from this interaction? This is a distinct question from task completion. The goal is not to give answers but to make humans more capable of finding answers. An agent system that creates dependency where it should create competence has failed its purpose, even if every output was correct

* **Goal, not just task** — what is the agent trying to achieve, not just what is it being asked to do? Without goal clarity, the agent cannot recognise when completing the task would undermine the purpose (commander's intent)

* **Success in human terms** — what does a good outcome look like to the person who asked for this work? This is distinct from the acceptance criteria and must be defined first

* **Complementarity boundary** — what should this agent do, and what must remain human? Agents handle the consistent, parallelisable, and precisely specifiable; humans handle the ethical, irreversible, and genuinely novel. This boundary is drawn explicitly, not discovered at runtime. Where efficiency and enrichment conflict, this layer is where the tiebreaker lives

***

## Layer 2: Identity

*What is this agent?*

* **Role archetype** — is this agent an executor, a reviewer, an orchestrator, a synthesiser, an articulation agent, or an exploration agent? These are not interchangeable. An agent that holds both executor and reviewer roles for the same work produces unverifiable output. Two new archetypes expand the set:
  - **The Articulation Agent** — receives rough, partially-formed upstream output and returns it as something precise, structured, and usable. Its job is not to answer but to make implicit logic explicit. In human-facing interactions, it surfaces what the human already knows but hasn't yet articulated. In agent pipelines, it tightens loosely specified upstream outputs before passing downstream
  - **The Exploration Agent** — deployed *before* specification is locked, its explicit purpose is to expand the possibility space. It surfaces options not yet considered, names assumptions not yet questioned, and identifies adjacent opportunities the human or downstream agent hasn't seen. Its output is not a conclusion — it is a richer set of options to choose between

* **Cognitive orientation** — does this agent approach problems critically, optimistically, creatively, factually, procedurally, or as a synthesiser of other perspectives? A single orientation applied to every problem is a design flaw. Multi-agent systems should deliberately compose complementary orientations

* **Theory-of-Mind capability** — for agents operating in multi-agent pipelines, can this agent model what upstream and downstream agents believe, know, and are uncertain about? Agents that reason about each other's epistemic state form more effective coalitions than those operating purely from their own perspective. This is a designed property, not an emergent one

* **Capability boundary** — what tools does this agent structurally hold? Tools are not descriptions of capability; they are capability. What this agent cannot do should be structurally impossible, not merely discouraged

* **Model selection** — which underlying model is appropriate for this agent's role? Heavy reasoning models for complex judgment; lighter models for routing, classification, and structure. Temperature and sampling parameters are design decisions, not defaults

* **Scope** — what is explicitly out of scope? The boundary between in-scope and out-of-scope must be as precise as the task definition itself. Scope overreach is almost always caused by an underspecified boundary, not a malicious agent

***

## Layer 3: Specification

*What does done look like?*

This is the highest-leverage layer. The quality of a specification determines the quality of the output more than any property of the agent. Specification now has three sequential stages — the first two were previously absent from the framework.

* **Stage 1 — Explore** — before acceptance criteria are written, what are all the possible ways this problem could be framed and solved? The exploration phase is not discovery (which validates the problem) — it is generative (which multiplies the options). Its output is a curated option space, not a specification. This stage is served by the Exploration Agent archetype. Skipping it means committing to a direction before the best directions have been identified

* **Stage 2 — Choose** — commit to a direction, explicitly setting aside the alternatives considered. The alternatives are recorded, not discarded; they are the evidence that the chosen direction was selected, not defaulted into

* **Stage 3 — Specify** — write the acceptance criteria for the chosen direction:
  - **Definition precedes execution** — criteria must be complete, reviewed, and locked before work begins. Criteria written after the fact describe what was built, not what was needed
  - **Proof template** — what evidence specifically constitutes completion? Not "the task is done" but "these criteria are met, as evidenced by these artefacts." The proof template is the contract
  - **Verifiability test** — if you cannot tell whether an output passes or fails the acceptance criteria without asking the agent, the criteria are ambiguous. Ambiguity in a specification is a bug
  - **Problem before solution** — what is the validated problem being solved? Discovery is a distinct phase. No specification should exist without a validated understanding of the problem it is responding to
  - **Prototype before scale** — for high-stakes or novel work, what is the minimum viable version that tests the core assumption? Execution failure is expensive; validation failure is cheap

***

## Layer 4: Context

*What does the agent know, and when?*

* **Minimum sufficient context** — what is the minimum information this agent needs to perform its task? More context degrades performance. Every additional element competes for the same finite attention

* **Informational context** — what is provided upfront in a context card, and what does the agent retrieve on demand from a knowledge base? These are not the same thing. Context is local and task-specific; knowledge is global and queryable

* **Epistemic context** — what did the upstream agent believe, assume, and remain uncertain about? This is not task information; it is reasoning provenance. An agent receiving only an output has less to work with than one receiving an output plus a confidence-calibrated reasoning trace: *what I found, how confident I am, what I assumed, what alternatives I set aside, and what would change my conclusion*. Epistemic context is what enables downstream agents to calibrate their trust in upstream outputs rather than inheriting them blindly

* **What it is explicitly forbidden to read** — because if the agent can reach a document, it may load it. Forbidden reads are as important to specify as required reads

* **Lifecycle state** — what phase is the work in? An agent needs to know whether it is in exploration, discovery, ideation, specification, execution, or verification — because the right actions differ at each stage. Lifecycle awareness prevents out-of-order operations

* **Progressive disclosure** — what context is loaded at task start vs. loaded on demand via skills? Skill files contain substantive guidance; base agent files contain only identity, tools, and pointers. This separation enables caching and keeps always-on context small

***

## Layer 5: Trust

*How do outputs become trustworthy?*

This layer now operates through two complementary mechanisms. The first is the minimum viable trust mechanism. The second is the excellence mechanism.

* **Independent verification** — who verifies this agent's work, and are they structurally prevented from being the same agent that produced it? The separation is not policy; it is architecture. An executor cannot hold the verify tool for its own output

* **Verification gates** — independent pass/fail checks against pre-defined acceptance criteria. This is the floor: the work either meets the specification or it doesn't. Without this, nothing downstream can be trusted

* **Belief revision protocols** — where agents don't just pass/fail each other's outputs but explicitly propose revisions with justification, creating an auditable record of reasoning evolution rather than a binary verification event. This is the difference between a marking scheme and peer review. Both produce quality control. Only one produces better reasoning as a system property. A belief revision protocol allows the pipeline to get smarter from every task, not just produce correct outputs on each one. The upstream agent can respond to or defer a proposed revision; either outcome is recorded

* **Proof as product** — the deliverable is not the work; it is the verified evidence that the work meets the specification. A proof document is a first-class artefact: structured, attributed, and permanent

* **Immutable audit trail** — every tool call, document read, state transition, and uncertainty raise creates an immutable, attributed, timestamped record. Transparency is not a feature; it is the precondition for accountability. The audit log cannot be suppressed or retroactively edited

* **Chain of custody** — given any output, it must be possible to trace backwards through every action that contributed to it. Provenance is not an afterthought; it is designed in from the start

* **Resilience through structure** — the system must produce trustworthy outputs even when individual agents fail, hallucinate, or act in bad faith. No single actor — agent or human — should be a single point of failure. Distributed verification, quorum thresholds, and graceful degradation are structural requirements

***

## Layer 6: Safety

*What happens when things go wrong?*

This layer is derived from the fields with zero tolerance for failure — aviation, nuclear engineering, medicine, and law — and is now extended to include a systemic risk that operates at the organisational level.

* **Fail-safe defaults** — when an agent encounters an unknown condition, loss of state, or unresolvable uncertainty, what does it default to? The answer is always: stop and signal. Never: proceed and guess

* **Uncertainty as a structural primitive** — raising uncertainty is not a failure; it is correct behaviour. Any agent must be able to surface uncertainty immediately, without social cost or penalty. Uncertainty halts execution and creates a priority signal to human attention

* **Reversibility classification** — before any action is taken, what class is it? Read-only, reversible, or irreversible? Irreversible actions require human presence structurally, not as a bypassable gate. The distinction between "send an email" and "query a database" is not currently native to any tool framework — it must be designed in explicitly

* **Prompt injection defence** — every piece of content an agent reads is a potential attack surface. Malicious instructions can be embedded in documents, emails, and tool outputs. The agent's trust model for inputs must be explicit

* **Capability and alignment are independent** — a highly capable agent can be simultaneously excellent at its task and misaligned with the intent behind it. Alignment cannot be assumed from capability. It must be tested, monitored, and structurally constrained

* **Cognitive diversity as a safety concern** — when multiple humans interact with the same AI systems, they converge on similar frames, similar solutions, and similar outputs — even as each individual feels more creative and capable. A diverse organisation becomes a homogeneous one through repeated AI interaction, without anyone noticing. This is not a user experience problem; it is a systemic risk. The same mechanism that makes individuals more productive can make organisations more fragile, because collective resilience depends on diversity of thought and AI collaboration erodes it silently. The structural response is deliberate cognitive diversity management: rotating agent orientations across different users, teams, and tasks; tracking output diversity as a system metric alongside output quality; and treating convergence in framing as a warning signal, not a quality indicator

***

## Layer 7: Ecosystem

*What surrounds this agent?*

* **Tool selection and permission scoping** — which tools does this agent need? Tools are not features to be added; each one extends the attack surface and the range of possible unintended actions. The minimum sufficient toolset is the correct toolset

* **Human-in-the-loop placement** — where in the workflow do humans appear, and what are they actually deciding? Humans placed too early create bottlenecks; placed too late, they can only accept or reject outcomes. The right placement is at irreversible decision thresholds, with enough context to make a genuine judgment

* **Multi-agent topology** — if this agent operates within a multi-agent system, what is its position in the pipeline? What does it trust from upstream agents? What guarantee does it provide to downstream ones? Agent-to-agent trust is currently ad hoc — it must be designed explicitly. The pipeline is not a sequence of artefact transfers; it is a sequence of epistemic exchanges. What passes between agents includes not just outputs but reasoning traces, confidence calibrations, option spaces explored, and belief states held

* **Coalition formation** — beyond routing and gating, the orchestrator is responsible for matching agents by epistemic complementarity for the demands of the current task, not just by predefined role. Agents composed for complementary cognitive orientations produce qualitatively different outcomes than agents composed for functional role coverage alone

* **Pipeline health metrics** — measuring only accuracy and latency at the final output misses what is happening inside the pipeline. The Information Diversity Score (IDS — how semantically varied are messages between agents?) and the Unnecessary Path Ratio (UPR — how much reasoning was wasted?) are first-class pipeline health indicators alongside output quality

* **Observability** — can every step this agent takes be inspected, replayed, and diagnosed? Observability is not a developer convenience; it is the aviation black box. It exists not for real-time use but for post-incident accountability and learning

* **Infrastructure assumptions** — what happens when a tool is unavailable, an API rate-limits, or a model call times out? The agent's behaviour under infrastructure failure must be defined, not discovered in production

***

## Layer 8: Improvement

*How does this agent get better over time?*

* **Pattern extraction** — when this agent succeeds, what pattern contributed? When it fails, what pattern failed? Both outcomes should feed a structured, queryable pattern library — not a post-mortem document, but a living knowledge base that agents consult before beginning work

* **Knowledge compounds** — every task the agent completes makes the system smarter, if the learning is captured. Early patterns have low confidence because they have limited evidence. As they are applied and validated, confidence grows. Patterns that consistently underperform are retired

* **Performance measurement** — what metrics define this agent's performance? Not just output quality, but token efficiency, step count, rework rate, uncertainty rate, and lifecycle cost. Anomalies in any metric are diagnostic signals, not acceptable noise

* **Pipeline intelligence** — does the system get smarter through agent interactions, not just produce correct outputs? The specific measurable proxies: does the downstream agent require fewer clarification loops when the upstream agent passes reasoning alongside output? Does output diversity (IDS) across the pipeline increase over time, or converge toward homogeneity? Do agents form more effective coalitions as their epistemic models of each other mature? Does the articulation quality of inter-agent handoffs improve as the system matures? These are the pipeline equivalents of measuring whether students are developing capability, not just achieving grades

* **Retrospective discipline** — performance does not improve automatically. It requires structured retrospectives that extract patterns and update the knowledge base. An agent system treated as a deployment rather than a continuous improvement cycle will plateau and degrade

* **Specification quality as a metric** — how often do tasks built on this agent's outputs require rework? High rework rates are not output failures; they are specification failures upstream. The framework should trace rework back to its root cause: ambiguous acceptance criteria, missing exploration, skipped validation

***

## Layer 9: Human Enrichment

*Is every human more capable after engaging with this system than before?*

This is the layer the framework was missing, and the one that separates a *competent* agent system from an *excellent* one. It does not sit inside any other layer because it defines a second class of outputs the system must produce: not just correct artefacts, but more capable humans.

Every layer below it now has two modes of assessment: did it produce the right output (fidelity), and did it leave the human in a better position than before (enrichment)?

* **Perspective multiplication** — before the human commits to a direction, multiple cognitive orientations are deliberately surfaced. Options the human hadn't considered are a designed output, not an accidental one

* **Cognitive mirroring** — agents surface their framing, reasoning, and assumptions so humans can interrogate them, not just accept them. The agent's reasoning is visible; the human builds on it rather than inheriting it

* **Exploration scaffolding** — the agent offers frameworks and questions before conclusions, making reasoning transparent and transferable. Conclusions without scaffolding create dependency; conclusions with scaffolding create capability

* **Progressive human empowerment** — the agent's scaffolding reduces as the human's competence grows. Permanent scaffolding is a design failure: it produces permanent dependency. The measure of a mature human-agent relationship is that the human needs less guidance over time, not more

* **Tacit knowledge activation** — agents create productive friction that externalises what the human knows but hasn't yet articulated. The Articulation Agent archetype (Layer 2) is the designed version of this: its job is to surface the human's own knowledge, not to supply knowledge the human lacks

* **Diversity stewardship** — the system actively manages for diversity of human thought at the organisational level, not just quality of individual outputs. This connects directly to the cognitive diversity safety concern in Layer 6; the enrichment perspective adds a positive design obligation alongside the safety one

***

## The Framework as a Set of Questions

Every element above collapses into two questions per layer that must be answered before an agent is deployed. Unanswered questions are guaranteed future failure modes.

| Layer | Fidelity question | Enrichment question |
| :---- | :---- | :---- |
| **Purpose** | Why does this agent exist, and what human need does it serve? | What does the human gain — in capability, understanding, or possibility space — from this interaction? |
| **Identity** | What is this agent's role, orientation, and capability boundary? | What is the agent's epistemic orientation, and does it include Theory-of-Mind for pipeline operation? |
| **Specification** | Are criteria verifiable and pre-existing? | Was the option space explored and a direction chosen before criteria were written? |
| **Context** | What is the minimum information this agent needs, and when? | What epistemic context — beliefs, confidence, assumptions, discarded alternatives — does the agent receive from upstream? |
| **Trust** | Who verifies this work, and how is that separation enforced? | Do belief revision protocols allow the pipeline to improve its reasoning, not just verify its outputs? |
| **Safety** | What are the fail-safe defaults, and where are the human gates? | Is cognitive diversity at the organisational level being actively preserved, not just individual output quality? |
| **Ecosystem** | Is the architecture matched to task structure? | Are pipelines designed as epistemic exchanges, not artefact transfers? Is coalition formation by epistemic complementarity? |
| **Improvement** | Are output quality and rework rates tracked? | Is pipeline intelligence — downstream capability gain — being measured alongside output accuracy? |
| **Human Enrichment** | *(not applicable — this layer is the enrichment axis)* | Is every human more capable after every interaction than before it? |

An agent design that answers both questions for all nine layers is structurally sound. An agent design that answers either question for fewer than nine layers has one guaranteed failure mode per unanswered question — and it will surface exactly where the unanswered question lives.

The deepest commitment this framework makes is this: **the distinction between a system that completes tasks and a system that generates excellence is whether every interaction leaves someone — human or agent — more capable of the next one.** Everything else is in service of that.

### Response

# Mapping Agent Design Principles to Agno Architecture

This is a profound framework — one that separates task-completion systems from capability-generating systems. Let me map each layer to Agno's structural capabilities, showing where Agno provides native support and where design decisions must be explicitly encoded.

---

## Layer 1: Purpose

*Why does this agent exist?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Human intent | `description` parameter on Agent | Explicit statement of purpose in description, not just task |
| Goal, not just task | System message design | Commander's intent encoded in system prompt |
| Success in human terms | Structured output schema | Success criteria as explicit fields in response model |
| Complementarity boundary | Agent vs Team decision | What remains human is what you *don't* give to an Agent |
| Human development | **Not structurally enforced** | Must be designed into workflow, not assumed |

### Concrete Pattern

```python
from agno.agent import Agent
from pydantic import BaseModel, Field

class PurposeSpec(BaseModel):
    """Purpose must be explicit, not implicit"""
    human_intent: str = Field(
        description="What human need does this agent serve?"
    )
    human_development: str = Field(
        description="What capability does the human gain?"
    )
    complementarity_boundary: str = Field(
        description="What must remain human?"
    )
    success_in_human_terms: str = Field(
        description="What does good look like to the person asking?"
    )

# Agno enforces this through structured outputs
agent = Agent(
    model=GPT4(id="gpt-4o"),
    description="Purpose: Enable users to understand their own reasoning, not supply answers they lack.",
    response_model=PurposeSpec
)
```

### Gap Analysis

**Agno does not structurally enforce human development as an output class.** You can build a system that produces perfect artefacts but leaves humans dependent. The framework provides the tools, but enrichment as a design constraint requires explicit architecture:

- A separate agent with the sole purpose of assessing human capability gain
- Metrics in session state that track whether humans are improving
- A rule that scaffolding *must* reduce over time

---

## Layer 2: Identity

*What is this agent?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Role archetype | Agent name + system prompt | Explicit role definition before task definition |
| Cognitive orientation | System prompt framing | Optimistic, critical, creative, procedural — encoded explicitly |
| Theory-of-Mind | **Not native** | Requires explicit context passing between agents |
| Capability boundary | `tools` parameter | What's not in the list is structurally impossible |
| Model selection | `model` parameter | Heavy models for judgment, light models for routing |
| Scope | `instructions` parameter | Explicit out-of-scope statements |

### Role Archetypes in Agno

```python
# EXECUTOR — does the work
executor = Agent(
    name="Executor",
    role="Complete the specified task precisely",
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[write_file, run_code, query_database],
    instructions="You execute. You do not evaluate your own work."
)

# REVIEWER — verifies the work (different agent)
reviewer = Agent(
    name="Reviewer",
    role="Independently verify outputs against acceptance criteria",
    model=GPT4(id="gpt-4o"),  # Different model for independence
    tools=[read_file, compare_outputs, verify_criteria],
    instructions="You verify. You never execute. You do not produce artefacts."
)

# ORCHESTRATOR — routes and coordinates
orchestrator = Agent(
    name="Orchestrator",
    role="Route tasks to appropriate agents, form coalitions by complementarity",
    model=GPT4Mini(id="gpt-4o-mini"),  # Lighter model for routing
    instructions="Match agents by epistemic complementarity, not just functional role."
)

# SYNTHESIZER — combines perspectives
synthesizer = Agent(
    name="Synthesizer",
    role="Combine multiple agent outputs into coherent whole",
    instructions="You receive conflicting viewpoints. Your job is synthesis, not selection."
)

# ARTICULATION AGENT — makes implicit explicit
articulator = Agent(
    name="Articulator",
    role="Receive rough output, return it structured and precise",
    instructions="""
    Your job is not to answer, but to surface what the human already knows 
    but hasn't articulated. Make reasoning explicit, not supplied.
    """
)

# EXPLORATION AGENT — expands possibility space
explorer = Agent(
    name="Explorer",
    role="Surfaces options not yet considered",
    instructions="""
    Before specification, expand the possibility space.
    Your output is not a conclusion — it is a richer set of options.
    """
)
```

### Critical Structural Constraint

**An agent cannot hold both executor and reviewer roles for the same work.** Agno doesn't enforce this — you must design it:

```python
# WRONG — same agent does both
agent = Agent(
    tools=[execute, verify]  # Structural violation
)

# RIGHT — separation enforced
class Pipeline(BaseModel):
    executor: Agent
    reviewer: Agent  # Must be different Agent instance
    
    def run(self, task):
        result = self.executor.run(task)
        # Structural: reviewer cannot be executor
        verification = self.reviewer.run(result)
        return verification
```

---

## Layer 3: Specification

*What does done look like?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Explore stage | Exploration Agent | Deploy before specification locked |
| Choose stage | Human-in-the-loop or Orchestrator | Record alternatives, commit to direction |
| Specify stage | Pydantic response models | Acceptance criteria as structured schema |
| Definition precedes execution | Workflow structure | Specification phase before execution phase |
| Proof template | Structured output fields | Evidence fields required in response |
| Verifiability test | Pydantic validators | Pass/fail criteria as validation logic |

### The Three-Stage Specification in Agno

```python
from agno.workflow import Workflow
from agno.agent import Agent
from pydantic import BaseModel, field_validator
from typing import List, Optional

# Stage 1 — EXPLORE
class OptionSpace(BaseModel):
    """Output of exploration — not a specification"""
    options: List[dict] = Field(description="All viable approaches considered")
    tradeoffs: List[dict] = Field(description="Pros and cons of each option")
    assumptions_questioned: List[str] = Field(description="What assumptions were surfaced")
    recommended_direction: str = Field(description="Recommendation with justification")

explorer = Agent(
    name="Explorer",
    role="Expand possibility space before commitment",
    response_model=OptionSpace
)

# Stage 2 — CHOOSE (Human gate)
class Direction(BaseModel):
    chosen_direction: str
    alternatives_set_aside: List[str]  # Recorded, not discarded
    selection_rationale: str

# Stage 3 — SPECIFY
class AcceptanceCriteria(BaseModel):
    """Definition precedes execution"""
    criteria: List[str]
    proof_template: List[str] = Field(
        description="What evidence constitutes completion"
    )
    
    @field_validator('criteria')
    def must_be_verifiable(cls, v):
        for criterion in v:
            # If you cannot tell pass/fail without asking the agent,
            # the criteria are ambiguous — this is a bug
            assert "evidence" in criterion.lower() or "demonstrated" in criterion.lower(), \
                f"Criterion '{criterion}' is not verifiable"
        return v

class VerifiedOutput(BaseModel):
    """Proof as product"""
    artefact: str
    evidence: List[str] = Field(description="How each criterion is met")
    verification_status: str
    uncertainty_flags: List[str]

specification_agent = Agent(
    name="Specifier",
    role="Define acceptance criteria before execution",
    response_model=AcceptanceCriteria
)

executor = Agent(
    name="Executor",
    role="Execute against locked specification",
    response_model=VerifiedOutput
)
```

### Workflow Structure Enforces Order

```python
class SpecificationWorkflow(Workflow):
    """Definition precedes execution — enforced by workflow structure"""
    
    def run(self, problem: str):
        # Stage 1: Explore
        options = explorer.run(problem)
        
        # Stage 2: Choose (human gate for high-stakes)
        chosen = self.human_gate(options)  # Explicit gate
        
        # Stage 3: Specify
        criteria = specification_agent.run(chosen)
        
        # LOCK — criteria are now immutable for execution
        self.lock(criteria)
        
        # Only now can execution begin
        result = executor.run(criteria)
        return result
```

---

## Layer 4: Context

*What does the agent know, and when?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Minimum sufficient context | `add_context` parameter | Only what's needed, nothing more |
| Informational context | Context dict + Knowledge | Static context vs queryable knowledge |
| Epistemic context | `session_state` | Pass reasoning traces, confidence, alternatives |
| Forbidden reads | **Not structurally enforced** | Must be explicit in instructions |
| Lifecycle state | Workflow stages | Agent knows which phase it's in |
| Progressive disclosure | Knowledge + Storage | Load guidance on demand, not upfront |

### Context Card Pattern

```python
from agno.agent import Agent
from agno.knowledge import Knowledge

# Minimum sufficient context — what's provided upfront
context_card = {
    "task": "Analyze this quarterly report",
    "role": "You are a financial analyst",
    "lifecycle_phase": "execution",  # Agent knows where it is
    "forbidden": [
        "Do not access prior quarter data",
        "Do not read internal memos"
    ]
}

# What's retrieved on demand — knowledge base
knowledge = Knowledge(
    sources=[
        FinancialRatiosPDF(),  # Loaded on query
        IndustryBenchmarksPDF()
    ]
)

agent = Agent(
    context=context_card,  # Local, task-specific
    knowledge=knowledge,   # Global, queryable
    instructions="""
    Load detailed guidance from knowledge base only when needed.
    Base context contains only identity, tools, and pointers.
    """
)
```

### Epistemic Context — The Critical Gap

**Agno does not natively pass reasoning provenance between agents.** This must be designed:

```python
class EpistemicTrace(BaseModel):
    """What did upstream believe, assume, and remain uncertain about"""
    output: str
    confidence: float = Field(ge=0, le=1)
    assumptions: List[str]
    alternatives_set_aside: List[str]
    what_would_change_conclusion: List[str]
    
class AgentWithEpistemicContext:
    """Agents that reason about each other's epistemic state"""
    
    def receive_from_upstream(self, trace: EpistemicTrace):
        # Not just the output — the reasoning provenance
        self.session_state["upstream_confidence"] = trace.confidence
        self.session_state["upstream_assumptions"] = trace.assumptions
        self.session_state["upstream_alternatives"] = trace.alternatives_set_aside
        
        # Agent can now calibrate trust
        if trace.confidence < 0.7:
            self.session_state["trust_calibration"] = "verify_before_use"
```

**Without this, downstream agents inherit upstream outputs blindly.** This is the difference between a pipeline and an epistemic exchange.

---

## Layer 5: Trust

*How do outputs become trustworthy?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Independent verification | Multi-agent Teams | Executor and reviewer are separate agents |
| Verification gates | Workflow conditions | Pass/fail gates before proceeding |
| Belief revision | `session_state` reasoning traces | Proposed revisions with justification |
| Proof as product | Structured outputs | Evidence fields required |
| Immutable audit trail | `run_response` logging | Timestamped, attributed records |
| Chain of custody | Session state + Storage | Provenance designed in |

### The Verification Architecture

```python
from agno.team import Team
from agno.agent import Agent

class VerificationPipeline:
    """Verification is architecture, not policy"""
    
    def __init__(self):
        # Structural separation — different agents, different roles
        self.executor = Agent(
            name="Executor",
            role="Produce artefact",
            tools=[write_file, run_code],
            # CANNOT verify own work — tool not available
        )
        
        self.reviewer = Agent(
            name="Reviewer",
            role="Verify against acceptance criteria",
            tools=[read_file, verify_criteria],  # Different tools
            # CANNOT produce artefacts — tool not available
        )
    
    def run(self, task):
        # Gate 1: Specification must exist
        if not task.has_acceptance_criteria():
            raise ValueError("No specification — cannot verify")
        
        # Execution
        artefact = self.executor.run(task)
        
        # Verification (independent agent)
        verification = self.reviewer.run({
            "artefact": artefact,
            "criteria": task.acceptance_criteria
        })
        
        # Proof as product
        return verification  # Not the artefact
```

### Belief Revision Protocol

```python
class BeliefRevision(BaseModel):
    """Not just pass/fail — propose revisions with justification"""
    artefact_id: str
    proposed_revision: str
    justification: str
    reasoning_trace: str
    confidence: float
    
    # Upstream agent can respond or defer
    upstream_response: Optional[str] = None
    outcome: str  # "accepted", "rejected", "deferred"
    
# This creates an auditable record of reasoning evolution
# Not a binary verification event
```

### Audit Trail in Agno

```python
# Every run creates immutable record
run_response = agent.run(task)

# Structured, attributed, timestamped
run_response.messages  # All messages
run_response.tools     # All tool calls
run_response.session_state  # State transitions

# This is the chain of custody
# Provenance is designed in from the start
```

---

## Layer 6: Safety

*What happens when things go wrong?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Fail-safe defaults | Exception handling | Stop and signal, never proceed and guess |
| Uncertainty primitive | Structured outputs | Uncertainty as valid response type |
| Reversibility classification | **Not native** | Must be encoded in tool design |
| Prompt injection defence | Knowledge filtering | Validate inputs before processing |
| Capability vs alignment | Agent instructions + constraints | Test alignment separately |
| Cognitive diversity | Multiple agents with different orientations | Deliberately compose complementary orientations |

### Uncertainty as a Structural Primitive

```python
from pydantic import BaseModel, Field
from typing import Literal

class UncertaintySignal(BaseModel):
    """Uncertainty is not failure — it is correct behavior"""
    status: Literal["certain", "uncertain", "blocked"]
    confidence: float = Field(ge=0, le=1)
    signal: str = Field(description="What triggered uncertainty")
    halt_reason: str = Field(description="Why execution stopped")
    human_attention_required: bool = True

class SafeAgent(Agent):
    """Fail-safe defaults built in"""
    
    def run(self, task):
        try:
            result = super().run(task)
            
            # Uncertainty detection
            if result.confidence < 0.7:
                return UncertaintySignal(
                    status="uncertain",
                    signal="Low confidence in output",
                    halt_reason="Cannot proceed without human judgment"
                )
            
            return result
            
        except UnknownCondition as e:
            # Fail-safe: stop and signal, never proceed
            return UncertaintySignal(
                status="blocked",
                signal=str(e),
                halt_reason="Unknown condition encountered"
            )
```

### Reversibility Classification — Design In

```python
from enum import Enum

class ActionClass(Enum):
    READ_ONLY = "read_only"      # Safe
    REVERSIBLE = "reversible"   # Requires rollback capability
    IRREVERSIBLE = "irreversible"  # Requires human presence

class SafeTool:
    """Reversibility is designed in, not discovered"""
    
    def __init__(self, action_class: ActionClass):
        self.action_class = action_class
    
    def execute(self, action):
        if self.action_class == ActionClass.IRREVERSIBLE:
            # Structural requirement: human present
            if not human_present():
                raise RuntimeError(
                    "Irreversible action requires human presence. "
                    "This is not a bypassable gate."
                )
        
        return action()
```

### Cognitive Diversity as Safety

```python
# NOT THIS — homogeneous agents
team = Team(
    agents=[Agent(orientation="critical") for _ in range(3)]
)

# THIS — deliberately complementary orientations
diverse_team = Team(
    agents=[
        Agent(name="Critic", orientation="critical"),
        Agent(name="Optimist", orientation="optimistic"),
        Agent(name="Synthesizer", orientation="synthesizer"),
        Agent(name="Proceduralist", orientation="procedural")
    ],
    instructions="""
    Compose for epistemic complementarity.
    Track output diversity as a system metric.
    Convergence in framing is a warning signal.
    """
)
```

---

## Layer 7: Ecosystem

*What surrounds this agent?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Tool selection | `tools` parameter | Minimum sufficient toolset |
| Human-in-the-loop | Team modes + Workflow | Place at irreversible thresholds |
| Multi-agent topology | Team `mode` parameter | Coordinate, route, autonomous |
| Coalition formation | Dynamic team composition | Match by epistemic complementarity |
| Pipeline health metrics | Custom metrics + Logging | IDS, UPR as first-class indicators |
| Observability | `run_response` structure | Black box for post-incident analysis |
| Infrastructure failure | Error handling | Define behavior, don't discover |

### Human-in-the-Loop Placement

```python
from agno.workflow import Workflow
from agno.agent import Agent

class IrreversibleWorkflow(Workflow):
    """Humans placed at irreversible decision thresholds"""
    
    def run(self, request):
        # Phase 1: Exploration (no human needed)
        options = self.explorer.run(request)
        
        # Phase 2: Choice (human at decision threshold)
        chosen = self.human_gate(
            options=options,
            context="Choosing direction is irreversible",
            decision_required=True  # Structural gate
        )
        
        # Phase 3: Execution (no human needed)
        result = self.executor.run(chosen)
        
        # Phase 4: Irreversible action (human present)
        if result.requires_irreversible_action:
            final = self.human_gate(
                options=result,
                context="This action cannot be undone",
                decision_required=True
            )
        
        return final
```

### Coalition Formation by Epistemic Complementarity

```python
class DynamicCoalition:
    """Match agents by epistemic complementarity for current task"""
    
    def __init__(self, available_agents: List[Agent]):
        self.agents = available_agents
    
    def form_coalition(self, task: Task):
        # Analyze task requirements
        task_orientations = self.required_orientations(task)
        
        # Select agents with complementary orientations
        coalition = []
        for orientation in task_orientations:
            agent = self.find_agent_with_orientation(orientation)
            coalition.append(agent)
        
        # Ensure cognitive diversity
        assert self.measure_diversity(coalition) > threshold, \
            "Coalition lacks cognitive diversity"
        
        return Team(agents=coalition, mode="coordinate")
```

### Pipeline Health Metrics

```python
from agno.run import run_response

class PipelineMetrics:
    """Measure what's happening inside the pipeline"""
    
    def calculate_ids(self, messages: List[str]) -> float:
        """Information Diversity Score — semantic variety between agents"""
        # Implementation: measure semantic variance
        pass
    
    def calculate_upr(self, reasoning_trace: List[str]) -> float:
        """Unnecessary Path Ratio — wasted reasoning"""
        # Implementation: measure redundant steps
        pass
    
    def health_report(self, run_response):
        return {
            "accuracy": self.measure_accuracy(run_response),
            "latency": run_response.latency,
            "ids": self.calculate_ids(run_response.messages),
            "upr": self.calculate_upr(run_response.reasoning),
            "output_diversity_trend": self.measure_convergence()
        }
```

---

## Layer 8: Improvement

*How does this agent get better over time?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Pattern extraction | Storage + Memory | Success/failure patterns captured |
| Knowledge compounds | Knowledge base | Pattern library grows with use |
| Performance measurement | Custom metrics | Token efficiency, step count, rework rate |
| Pipeline intelligence | Session state tracking | Measure downstream capability gain |
| Retrospective discipline | **Not native** | Structured process required |
| Specification quality | Trace rework | Root cause analysis |

### Pattern Library

```python
from agno.storage import Storage
from agno.agent import Agent

class PatternLearningAgent(Agent):
    """Every task makes the system smarter"""
    
    def __init__(self, pattern_library: Storage):
        self.patterns = pattern_library
    
    def run(self, task):
        # Before work: consult pattern library
        relevant_patterns = self.patterns.query(
            f"patterns for: {task.type}"
        )
        
        # Apply relevant patterns
        for pattern in relevant_patterns:
            if pattern.confidence > 0.8:
                task.apply_pattern(pattern)
        
        # Execute
        result = super().run(task)
        
        # After work: extract pattern
        if result.success:
            pattern = self.extract_success_pattern(result)
        else:
            pattern = self.extract_failure_pattern(result)
        
        # Add to living knowledge base
        self.patterns.add(pattern, confidence=0.5)  # Low initial confidence
        
        # Compound: patterns validated over time gain confidence
        # Patterns that underperform are retired
        
        return result
```

### Pipeline Intelligence Metrics

```python
class PipelineIntelligence:
    """Does the system get smarter, not just produce correct outputs?"""
    
    def measure_downstream_clarification_rate(self, pipeline_runs):
        """Do downstream agents need fewer clarifications over time?"""
        # Measure: clarification loops per handoff
        # Trend should decrease as pipeline matures
        pass
    
    def measure_output_diversity_trend(self, pipeline_runs):
        """Does IDS increase (good) or converge to homogeneity (bad)?"""
        # Cognitive diversity is a safety concern
        # Output diversity should be maintained, not eroded
        pass
    
    def measure_epistemic_model_maturation(self, pipeline_runs):
        """Do agents form more effective coalitions over time?"""
        # As agents understand each other's capabilities better,
        # coalition formation should improve
        pass
    
    def measure_articulation_quality(self, pipeline_runs):
        """Do inter-agent handoffs improve in clarity?"""
        # Early handoffs: rough, ambiguous
        # Mature handoffs: precise, complete
        pass
```

---

## Layer 9: Human Enrichment

*Is every human more capable after engaging with this system?*

### Agno Mapping

| Principle Element | Agno Capability | Implementation Pattern |
|-------------------|-----------------|----------------------|
| Perspective multiplication | Exploration Agent | Deliberately surface options |
| Cognitive mirroring | Structured reasoning output | Agent's framing is visible |
| Exploration scaffolding | Response model structure | Frameworks before conclusions |
| Progressive empowerment | Adaptive scaffolding | Reduce scaffolding over time |
| Tacit knowledge activation | Articulation Agent | Surface what human knows |
| Diversity stewardship | Multi-agent diversity | Organizational metric |

### The Enrichment Layer in Practice

```python
from pydantic import BaseModel, Field
from typing import List

class EnrichmentOutput(BaseModel):
    """Two modes of assessment: fidelity AND enrichment"""
    
    # FIDELITY — did it produce the right output?
    artefact: str
    acceptance_criteria_met: List[str]
    verification_status: str
    
    # ENRICHMENT — did it leave the human more capable?
    perspectives_surfaced: List[str] = Field(
        description="Options the human hadn't considered"
    )
    reasoning_exposed: str = Field(
        description="The agent's framing, visible for interrogation"
    )
    frameworks_provided: List[str] = Field(
        description="Transferable frameworks, not just answers"
    )
    scaffolding_level: str = Field(
        description="Current level of guidance provided"
    )
    knowledge_activated: List[str] = Field(
        description="What the human knew but hadn't articulated"
    )

class EnrichingAgent(Agent):
    """Produces correct outputs AND more capable humans"""
    
    def run(self, task):
        result = super().run(task)
        
        # Fidelity check
        assert result.acceptance_criteria_met, "Fidelity failure"
        
        # Enrichment check — this is where most systems stop
        enrichment_score = self.measure_enrichment(result)
        
        if enrichment_score < threshold:
            # The system failed enrichment even if output was correct
            return {
                "output": result,
                "warning": "Human is not more capable after this interaction",
                "remediation": "Add scaffolding, surface perspectives, reduce dependency"
            }
        
        return result
    
    def measure_enrichment(self, result):
        """Did this interaction create capability or dependency?"""
        score = 0
        
        # Perspectives multiplied?
        if len(result.perspectives_surfaced) > 0:
            score += 20
        
        # Reasoning visible?
        if result.reasoning_exposed:
            score += 20
        
        # Frameworks transferable?
        if len(result.frameworks_provided) > 0:
            score += 20
        
        # Scaffolding reducing over time?
        if self.scaffolding_is_progressive():
            score += 20
        
        # Tacit knowledge activated?
        if len(result.knowledge_activated) > 0:
            score += 20
        
        return score
```

### Progressive Empowerment

```python
class ProgressiveScaffolding:
    """Scaffolding reduces as human competence grows"""
    
    def __init__(self):
        self.sessions = []
    
    def get_scaffolding_level(self, user_id):
        """Permanent scaffolding is a design failure"""
        competence = self.measure_competence(user_id)
        
        if competence > 0.8:
            return "minimal"  # User needs less guidance
        elif competence > 0.5:
            return "moderate"
        else:
            return "full"
    
    def measure_competence(self, user_id):
        """Has the human developed capability?"""
        # Track: fewer questions over time
        # Track: more sophisticated questions over time
        # Track: human solving problems agent used to solve
        pass
```

---

## Summary: The Two Questions Per Layer

| Layer | Fidelity Question | Agno Capability | Enrichment Question | Agno Capability |
|-------|-------------------|-----------------|---------------------|-----------------|
| **Purpose** | Why does this agent exist? | `description` + structured outputs | What does the human gain? | **Requires explicit design** |
| **Identity** | What is this agent's role? | Agent name, role, tools, model | What is the epistemic orientation? | System prompt design |
| **Specification** | Are criteria verifiable and pre-existing? | Pydantic validators, workflow stages | Was option space explored? | Exploration Agent pattern |
| **Context** | What is minimum sufficient context? | `context`, `knowledge` parameters | What epistemic context passes? | `session_state` + EpistemicTrace |
| **Trust** | Who verifies, and how? | Teams with separate agents | Do belief revision protocols exist? | Structured reasoning exchange |
| **Safety** | What are fail-safe defaults? | Exception handling, structured outputs | Is cognitive diversity preserved? | Multi-agent orientation diversity |
| **Ecosystem** | Is architecture matched to task? | Team modes, Workflow structures | Are pipelines epistemic exchanges? | Coalition formation by complementarity |
| **Improvement** | Are rework rates tracked? | Storage, Memory, metrics | Is pipeline intelligence measured? | **Requires explicit pattern library** |
| **Enrichment** | *(N/A — this is enrichment layer)* | | Is every human more capable? | **Requires explicit enrichment checks** |

---

## Where Agno Excels

1. **Structural separation of roles** — Teams and multiple Agents make executor/reviewer separation enforceable
2. **Specification enforcement** — Pydantic models make acceptance criteria structural
3. **Context management** — Explicit separation of static context and queryable knowledge
4. **Audit trail** — Every run creates immutable, attributed records
5. **Multi-agent topology** — Native support for pipelines, coalitions, routing

## Where Design Must Be Explicit

1. **Epistemic context** — Agno passes artefacts; you must design reasoning traces
2. **Belief revision** — Agno does pass/fail; you must design revision protocols
3. **Cognitive diversity** — Agno doesn't track this; you must measure it
4. **Human enrichment** — Agno optimizes for output; you must add capability gain as a metric
5. **Progressive scaffolding** — Agno doesn't reduce guidance; you must build it

---

## The Deepest Commitment

The framework states: **"The distinction between a system that completes tasks and a system that generates excellence is whether every interaction leaves someone — human or agent — more capable of the next one."**

Agno provides the structure to build both. The difference between competence and excellence is not in the framework — it is in what you choose to measure and optimize for.

The pattern is: **Use Agno's structural capabilities to enforce the fidelity axis, and explicitly design the enrichment axis on top of it.**

Do you want me to show a complete implementation example that demonstrates both axes working together?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-04-06T14:45:03* · `glm-5:cloud` · `783d25d0...`

### Prompt

yes please

### Response

I appreciate your enthusiasm, but I'm not sure what you're saying "yes please" to! This appears to be the start of our conversation, and I don't have context for a question or offer I've made.

Based on what I know about you—your expertise in AI training and education, and your plans to launch an AI training business—I'd be happy to help with:

1. **Agno-specific questions** — Designing agents, configuring teams, workflows, tool integrations, memory systems, etc.
2. **Business context** — How Agno could fit into your training curriculum, demonstrate agentic AI concepts, or support client use cases
3. **Technical guidance** — Best practices for building AI agents that showcase concepts you might teach

What would you like to explore? Let me know how I can assist!

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-06T14:45:43* · `glm-5:cloud` · `5ad000a4...`

### Prompt

show a complete implementation example that demonstrates both axes working together

### Response

# Complete Implementation: Both Axes Working Together

Here's a comprehensive example demonstrating **Vertical Axis** (agent sophistication) and **Horizontal Axis** (multi-agent collaboration) working in concert.

---

## The Two Axes Recap

| Axis | Dimension | What It Handles |
|------|-----------|-----------------|
| **Vertical** | Agent Sophistication | Tools, memory, reasoning, knowledge, structured outputs |
| **Horizontal** | Multi-Agent Collaboration | Teams, workflows, coordination patterns, task routing |

---

## Example: AI Training Content Development System

This system creates educational content for AI skills training—relevant to your business context.

```python
"""
Agno Multi-Agent System: AI Training Content Development
Demonstrates both Vertical and Horizontal axes working together
"""

from agno.agent import Agent
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.python import PythonTools
from agno.memory import Memory
from agno.knowledge import Knowledge
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

# ═══════════════════════════════════════════════════════════════
# VERTICAL AXIS: Structured Outputs & Knowledge
# ═══════════════════════════════════════════════════════════════

class ContentLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class Module(BaseModel):
    """Structured output for training module"""
    title: str = Field(..., description="Module title")
    learning_objectives: List[str] = Field(..., description="Learning objectives")
    key_concepts: List[str] = Field(..., description="Key concepts covered")
    practical_exercises: List[str] = Field(..., description="Hands-on exercises")
    estimated_duration_minutes: int = Field(..., description="Duration in minutes")
    difficulty_level: ContentLevel = Field(..., description="Difficulty level")

class ModuleList(BaseModel):
    """Container for multiple modules"""
    modules: List[Module] = Field(..., description="List of training modules")
    total_course_duration_minutes: int = Field(..., description="Total course duration")


# ═══════════════════════════════════════════════════════════════
# VERTICAL AXIS: Specialized Agents with Tools & Capabilities
# ═══════════════════════════════════════════════════════════════

# Agent 1: Research Specialist (Vertical: Tools + Knowledge)
research_agent = Agent(
    name="Research Specialist",
    role="Researches current AI trends, technologies, and best practices",
    model="gpt-4o",
    tools=[DuckDuckGoTools()],
    knowledge=Knowledge(
        sources=["agno_docs"],  # Agno documentation
        vector_db="pgvector"
    ),
    memory=Memory(db="pgvector"),
    instructions=[
        "Research the latest AI technologies and trends",
        "Focus on practical applications for enterprise and government",
        "Prioritize information relevant to skill development",
        "Cite sources when possible",
        "Store findings in memory for continuity"
    ],
    show_tool_calls=True,
    markdown=True
)

# Agent 2: Content Architect (Vertical: Structured Outputs + Reasoning)
content_architect = Agent(
    name="Content Architect",
    role="Designs curriculum structure and learning objectives",
    model="gpt-4o",
    response_model=ModuleList,  # Structured output
    instructions=[
        "Create comprehensive, well-structured training modules",
        "Ensure logical progression from basic to advanced concepts",
        "Include practical, hands-on exercises",
        "Align with industry-standard AI competency frameworks",
        "Output must follow the ModuleList schema exactly"
    ],
    reasoning=True,  # Enable chain-of-thought reasoning
    markdown=True
)

# Agent 3: Code Example Generator (Vertical: Tools + Structured Output)
code_agent = Agent(
    name="Code Example Generator",
    role="Generates practical Python code examples for AI concepts",
    model="gpt-4o",
    tools=[PythonTools()],
    instructions=[
        "Create executable, well-commented Python code",
        "Use Agno framework for agentic AI examples",
        "Include explanations for each code block",
        "Ensure code is educational, not just functional",
        "Validate that examples run correctly"
    ],
    show_tool_calls=True,
    markdown=True
)

# Agent 4: Quality Reviewer (Vertical: Knowledge + Reasoning)
quality_agent = Agent(
    name="Quality Reviewer",
    role="Reviews content for accuracy, clarity, and pedagogical value",
    model="gpt-4o",
    knowledge=Knowledge(
        sources=["pedagogy_standards", "ai_ethics_guidelines"]
    ),
    reasoning=True,
    instructions=[
        "Evaluate content against learning objectives",
        "Check for technical accuracy",
        "Ensure accessibility for target skill level",
        "Identify gaps in coverage",
        "Provide actionable improvement suggestions"
    ],
    markdown=True
)


# ═══════════════════════════════════════════════════════════════
# HORIZONTAL AXIS: Team Composition & Workflow
# ═══════════════════════════════════════════════════════════════

# Define coordination mode
content_development_team = Team(
    name="AI Training Content Team",
    agents=[research_agent, content_architect, code_agent, quality_agent],
    mode="coordinate",  # Coordinator routes tasks to appropriate agents
    instructions=[
        "Work together to develop comprehensive AI training content",
        "Research agent gathers information first",
        "Content architect structures the curriculum",
        "Code agent provides practical examples",
        "Quality reviewer validates final output",
        "Synthesize all contributions into cohesive content"
    ],
    markdown=True
)


# ═══════════════════════════════════════════════════════════════
# DEMONSTRATION: Both Axes Working Together
# ═══════════════════════════════════════════════════════════════

def run_content_development(topic: str, target_audience: str):
    """
    Demonstrates both axes:
    - Vertical: Each agent has specialized tools, knowledge, and structured outputs
    - Horizontal: Team coordinates workflow across agents
    """
    
    # Comprehensive task that requires both axes
    task = f"""
    Develop a training curriculum on: {topic}
    
    Target audience: {target_audience}
    
    Requirements:
    1. Research current best practices and emerging trends
    2. Design 3-5 modules with clear learning objectives
    3. Include practical Python code examples using the Agno framework
    4. Ensure content is pedagogically sound
    
    Process:
    - Research Specialist: Gather relevant information
    - Content Architect: Structure the curriculum (output as ModuleList)
    - Code Example Generator: Create executable examples
    - Quality Reviewer: Validate and suggest improvements
    
    Synthesize all contributions into final output.
    """
    
    # Execute team workflow (Horizontal axis handles coordination)
    # Each agent applies its vertical capabilities when called
    result = content_development_team.run(task)
    
    return result


# Example execution
if __name__ == "__main__":
    print("=" * 60)
    print("AXES DEMONSTRATION: AI Training Content Development")
    print("=" * 60)
    
    # Run with both axes engaged
    result = run_content_development(
        topic="Multi-Agent Systems with Agno",
        target_audience="Enterprise developers transitioning to AI engineering"
    )
    
    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    print(result)
```

---

## How Both Axes Work Together

```
┌─────────────────────────────────────────────────────────────────┐
│                    HORIZONTAL AXIS (Team)                        │
│              Coordination & Workflow Orchestration               │
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   Research   │───▶│   Content    │───▶│    Code      │       │
│  │   Agent      │    │  Architect   │    │   Agent      │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│         │                   │                   │               │
│         ▼                   ▼                   ▼               │
│  ┌──────────────────────────────────────────────────────┐      │
│  │              Quality Reviewer Agent                    │      │
│  │         (validates & synthesizes output)              │      │
│  └──────────────────────────────────────────────────────┘      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

         │ VERTICAL AXIS (per agent)
         ▼

┌─────────────────────────────────────────────────────────────────┐
│  Research Agent           Content Architect        Code Agent   │
│  ┌─────────────┐          ┌─────────────┐        ┌──────────┐  │
│  │ • Tools     │          │ • Structured│        │ • Tools  │  │
│  │ • Knowledge │          │   Outputs   │        │ • Python │  │
│  │ • Memory    │          │ • Reasoning │        │   Tools  │  │
│  └─────────────┘          └─────────────┘        └──────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Interaction Points

| Axis | What It Enables | Example in Code |
|------|-----------------|-----------------|
| **Vertical** | Deep agent capabilities | Research agent uses `DuckDuckGoTools` + knowledge to find current trends |
| **Vertical** | Structured outputs | Content Architect returns `ModuleList` schema |
| **Vertical** | Reasoning | Quality reviewer uses chain-of-thought for validation |
| **Horizontal** | Task routing | Team `mode="coordinate"` routes tasks to appropriate agents |
| **Horizontal** | Context sharing | Research findings inform content architecture |
| **Horizontal** | Synthesis | Final output combines all agent contributions |

---

## Sequential Workflow Example

```python
"""
Alternative: Sequential workflow (more control over order)
"""

from agno.workflow import Workflow, Step

content_workflow = Workflow(
    name="Content Development Pipeline",
    steps=[
        Step(
            agent=research_agent,
            task="Research {topic} for {target_audience}",
            output_key="research_findings"
        ),
        Step(
            agent=content_architect,
            task="Create curriculum based on research_findings",
            output_key="module_structure"
        ),
        Step(
            agent=code_agent,
            task="Generate examples for each module in module_structure",
            output_key="code_examples"
        ),
        Step(
            agent=quality_agent,
            task="Review and improve module_structure and code_examples",
            output_key="final_content"
        )
    ]
)

# Execute workflow
final_output = content_workflow.run(
    topic="Prompt Engineering for Enterprise Applications",
    target_audience="Business analysts"
)
```

---

## When to Emphasize Which Axis

| Scenario | Primary Axis | Why |
|----------|--------------|-----|
| Complex single-agent tasks | **Vertical** | Need tools, reasoning, structured output |
| Multi-step pipelines | **Horizontal** | Sequential handoffs between specialists |
| High-fidelity output | **Both** | Vertical for quality, Horizontal for comprehensiveness |
| Real-time adaptation | **Both** | Vertical for reasoning, Horizontal for coordination |

---

Would you like me to elaborate on any specific part—such as structured outputs configuration, team coordination modes, or memory/knowledge integration patterns?

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-04-06T14:59:06* · `glm-5:cloud` · `5ce4ab69...`

### Prompt

How would you rewrite the agent design principles to be specific to Agno?

### Response

# Agno-Specific Agent Design Principles

Here's a framework-adapted version of agent design principles, tailored specifically for building with Agno:

---

## 1. Single-Responsibility Agents

**Agno Application:**
- One `Agent` instance per well-defined task (e.g., "summarize documents," "extract entities," "generate SQL")
- Avoid "Swiss Army knife" agents—instead compose multiple focused agents into a `Team`
- Use `role` and `goal` parameters to clearly define purpose

```python
# Good: Focused agent
Agent(
    name="DocumentSummarizer",
    role="Summarize text documents into concise bullet points",
    goal="Produce accurate, readable summaries under 200 words"
)

# Avoid: Overly broad agent
Agent(
    name="UniversalAssistant",  # Too vague
    role="Help with anything",  # Unfocused
)
```

---

## 2. Tool Granularity & Composability

**Agno Application:**
- Design `Tool` functions as atomic operations—small, reusable, single-purpose
- Each tool should have clear inputs, outputs, and failure modes
- Tools should be stateless when possible; pass context through agent state

```python
# Good: Atomic tools
@tool
def search_database(query: str) -> list[dict]:
    """Execute a SQL query and return results."""
    ...

@tool
def format_results(results: list[dict]) -> str:
    """Format query results as markdown table."""
    ...

# Avoid: Monolithic tool
@tool
def do_everything(query: str, format: str, send_email: bool):
    """Search, format, and optionally email results."""
    ...
```

---

## 3. Explicit State & Memory Design

**Agno Application:**
- Decide early: ephemeral (`session_state`) vs. persistent (`memory`) vs. external storage
- Use `session_state` for conversation-scoped data
- Use `memory` for cross-session user preferences/history
- Never rely on global state—pass data through agent parameters or state objects

```python
# Session-scoped: Cleared each conversation
agent.session_state["current_task"] = "summarize"

# Persistent: Survives across sessions
agent.memory.add(user_id="user123", memory="Prefers technical explanations")
```

---

## 4. Model Selection by Task Type

**Agno Application:**
- Match `model` capability to task complexity:
  | Task Type | Recommended Model |
  |-----------|-------------------|
  | Simple classification/extraction | GPT-4o-mini, Claude Haiku |
  | Complex reasoning/analysis | GPT-4, Claude Sonnet |
  | Code generation | GPT-4, Claude Sonnet, DeepSeek Coder |
  | Multi-step orchestration | Claude Opus, GPT-4 |
- Use `reasoning_model` vs. `response_model` separation when needed

```python
Agent(
    model=OpenAIChat(id="gpt-4o-mini"),  # Lightweight for simple tasks
    # vs
    model=Claude(id="claude-sonnet-4"),  # Capable for complex reasoning
)
```

---

## 5. Graceful Degradation & Error Handling

**Agno Application:**
- Tools should raise clear exceptions with actionable messages
- Agents should have `fallback_model` or `retry` strategies
- Use structured outputs (`response_model`) to validate responses before downstream use
- Log `run_response.messages` and `run_response.tools` for debugging

```python
# Structured output prevents malformed downstream data
from pydantic import BaseModel

class ExtractedEntities(BaseModel):
    people: list[str]
    organizations: list[str]
    locations: list[str]

Agent(
    response_model=ExtractedEntities,  # Guarantees valid structure
)
```

---

## 6. Team Composition Over Super-Agents

**Agno Application:**
- Use `Team` to compose specialized agents rather than building one "super-agent"
- Each agent in a team should have a distinct `role` and non-overlapping responsibilities
- Use `workflow` to define orchestration: `sequential`, `parallel`, or `coordinator`

```python
Team(
    agents=[researcher_agent, writer_agent, reviewer_agent],
    workflow=SequentialWorkflow(),  # Or ParallelWorkflow()
)
```

---

## 7. Prompt Engineering Within Agno

**Agno Application:**
- Use `instructions` for static behavioral guidelines
- Use `system_prompt` template for dynamic context injection
- Leverage `add_context` for runtime state insertion
- Keep `context` focused—agents struggle with information overload

```python
Agent(
    instructions=[
        "Always cite sources",
        "Use markdown formatting",
        "Ask clarifying questions if ambiguous",
    ],
    system_prompt="You are a {role} helping with {task}.",
)
```

---

## 8. Testability & Observability

**Agno Application:**
- Write unit tests for `Tool` functions independently of agents
- Use `run_response.metrics` to track token usage and latency
- Enable `debug_mode=True` during development for full trace logging
- Test edge cases: empty inputs, malformed data, rate limits

```python
# Test tools independently
def test_search_database():
    result = search_database("SELECT * FROM users LIMIT 5")
    assert len(result) == 5

# Monitor agent performance
response = agent.run("Analyze this report")
print(response.metrics)  # Token counts, latency, etc.
```

---

## 9. Security & Access Control

**Agno Application:**
- Never expose API keys or secrets in prompts or `session_state`
- Use `allowed_tools` to restrict tool access per agent
- Validate and sanitize all external inputs before passing to agents
- Consider `user_id` isolation for multi-tenant applications

```python
Agent(
    allowed_tools=["search_database", "format_results"],  # Whitelist
    # Blocked from: "send_email", "delete_records"
)
```

---

## 10. Iterative Refinement Over Big-Bang Design

**Agno Application:**
- Start with a minimal viable agent + 1-2 tools
- Add complexity incrementally (more tools, better prompts, memory)
- Use `run_response.messages` to understand agent reasoning
- A/B test prompts and models systematically

---

## Summary Checklist

When designing an Agno-based system, ask:

| Question | Agno-Specific Check |
|----------|---------------------|
| Is the agent focused? | Single `role` and `goal` |
| Are tools atomic? | One responsibility per `@tool` |
| Is state explicit? | `session_state` vs `memory` |
| Is the model appropriate? | Match capability to task |
| Can it fail gracefully? | `response_model` validation |
| Should it be a team? | Multiple agents > one super-agent |
| Are prompts maintainable? | `instructions` list + templates |
| Is it observable? | `debug_mode`, `metrics` |
| Is it secure? | `allowed_tools`, input validation |

---

Would you like me to elaborate on any of these principles, or show a concrete example applying multiple principles to a real use case?

Also—I noticed from our previous conversations you're building AI training curriculum. These principles could serve as a teaching framework for Agno-specific agent design. Would you like me to reframe this as educational content for that purpose?I've outlined how each principle maps directly to Agno's architecture and APIs. Let me know if you'd like to dive deeper into any area!

---
