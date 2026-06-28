# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `7f94dc13...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-18T04:39:17 |
| **Runs** | 3 completed / 3 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-18T04:39:17* · `glm-5.1:cloud` · `b7b4f06e...`

### Prompt

Help me understand the architecture of an application that made it easy for a user to design a workflow using CAWDP. I'd like all artefacts from the process to be captured in a data store so that the developed design can be used by another process to implement elsewhere.

### Response

Now let me look at the current Agno capabilities to ensure the implementation mapping is accurate:Peter, this is a beautiful design challenge — and it's one where your own body of work converges. The CAWDP Design Studio is a **specialized Accretive Workspace in Lattice shape** where the fragments ARE CAWDP design artefacts and the methodology IS the structure.

Let me build this from the inside out.

---

# The CAWDP Design Studio — Architecture

## Phase 0: Target State Vision

**What would the perfect CAWDP design tool produce?**

A **typed, connected, navigable graph of design decisions** — not a document, not a wiki, not a set of markdown files. Every artefact from every CAWDP phase, captured with full type, epistemic metadata, and governance metadata. The graph is machine-readable: another process can traverse it to generate Agno implementation code.

**12 Characteristics of the Ideal Output:**

| # | Characteristic | What it means for this app |
|---|---|---|
| 1 | Typed not flat | Every artefact has an explicit type that determines its behavior and rendering |
| 2 | Epistemically transparent | Every artefact carries confidence, provenance, assumptions, limitations, recency, uncertainty |
| 3 | Intentionally aware | Artefacts connect to goals, constraints, mandates, guardrails |
| 4 | Connected as a graph | Typed relationships link artefacts across phases (supports, contradicts, depends-on, evolves-from, generated-by) |
| 5 | Implementation-retrievable | A code generator can traverse the graph and produce Agno Agent/Team/Workflow definitions |
| 6 | Authority-encoded | Complementarity boundaries and decision authority live in the data, not in a separate policy doc |
| 7 | Self-signaling decay | assessedAt timestamps + staleness scoring flag when design decisions need revisiting |
| 8 | Compoundable | New designs reference and extend existing ones — pattern library grows |
| 9 | Decision-archaeological | Reasoning chains preserved — why each decision was made, what alternatives were considered |
| 10 | Quality-gated structurally | Quality gates are executable assertions, not checkboxes |
| 11 | Scope-bounded | Each design has clear scope boundaries |
| 12 | Human-judgment-gated | High-stakes decisions (complementarity gaps ≥6, irreversible allocations) require explicit human sign-off |

---

## 1. The Core Data Model — PRISM as the Design Artefact Graph

**The fundamental unit is the Design Artefact — a PRISM entity with full cross-cutting layers.**

```
DesignArtefact {
  // PRISM DIMENSION — which of the 7 dimensions this artefact lives in
  dimension: 'scopes' | 'actors' | 'entities' | 'relations' | 'events' | 'knowledge' | 'intentions'
  
  // TYPE — specific artefact type within that dimension
  type: string  // validated against Schema Registry
  
  // CORE CONTENT — the artefact itself
  content: dict  // schema-validated by Schema Registry
  
  // PRISM CROSS-CUTTING LAYER 1: Epistemic (CC-3)
  epistemic: {
    confidence: float          // 0-1
    provenance: str            // who/what created this
    assumptions: list[str]     // what was assumed
    limitations: list[str]     // known limitations  
    assessedAt: datetime       // for staleness scoring (CC-5)
    uncertainty: float         // 0-1
  }
  
  // PRISM CROSS-CUTTING LAYER 2: Governance
  governance: {
    authority_boundary: str     // what this artefact can/cannot decide
    access_policy: str          // who can read/modify
    verification_level: str    // 'structural' | 'semantic' | 'authority' (CC-1)
    cawdp_phase: int           // 0-6, which phase produced this
    quality_gate_status: str   // 'pending' | 'passed' | 'failed' | 'waived'
  }
  
  // PRISM CROSS-CUTTING LAYER 3: Temporal
  temporal: {
    version: int
    previous_version_id: str | null
    specification_age_days: int  // auto-calculated from assessedAt
    staleness_score: float        // 0-1, auto-calculated
    refresh_cadence_days: int    // how often this should be revisited
  }
  
  // PRISM CROSS-CUTTING LAYER 4: Schema
  schema: {
    schema_id: str             // reference to Schema Registry
    schema_version: str        // version of the schema
    validation_status: str     // 'valid' | 'invalid' | 'pending'
  }
}
```

```
DesignRelation {
  // TYPED CONNECTION between artefacts
  source_artefact_id: str
  target_artefact_id: str
  relation_type: 'depends-on' | 'generated-by' | 'evolves-from' | 
                 'supports' | 'contradicts' | 'allocates-to' | 
                 'verifies' | 'handoff-to' | 'constrains' | 
                 'alternatives-considered' | 'triggers' | 'feeds-into'
  
  // Same cross-cutting layers as DesignArtefact
  epistemic: { confidence, provenance, ... }
  governance: { access_policy, verification_level }
  temporal: { version, assessedAt }
  schema: { schema_id, validation_status }
}
```

### CAWDP Phase → PRISM Dimension Mapping

This is the critical mapping that makes CAWDP's phases correspond to typed storage:

| CAWDP Phase | Primary PRISM Dimensions | Key Artefact Types | Example |
|---|---|---|---|
| **Phase 0** — Target State Vision | **Intentions** | goal, constraint, mandate, guardrail, preference, target_characteristic | "All outputs carry epistemic metadata" |
| **Phase 1** — Task Intelligence | **Entities**, Events, Relations | task, cognitive_operation, domain_event, dependency | "Extract claims from submission" |
| **Phase 2** — Capability Allocation | **Actors**, Intentions, Relations | human_actor, agent_actor, system_actor, complementarity_decision, reversibility_classification | "Claims Analyst: Agent, A:4" |
| **Phase 2.5** — Event Storming | **Events**, Relations | domain_event, failure_event, trigger_condition, data_flow | "Agent returns low confidence → flag for human" |
| **Phase 3** — System Architecture | **Entities**, Relations, Scopes | pipeline_stage, handoff_contract, template, system_enforcement_point, fmea_entry | "Stage 1 → Stage 2 handoff: Enhanced Submission Package" |
| **Phase 4** — Agent Design | **Actors**, Knowledge | agent_job_description, authority_boundary, failure_mode, archetype_instance | "Drift Detector: Measurer, never interpret" |
| **Phase 5** — Human Experience Design | **Actors**, Scopes, Knowledge | human_experience_spec, cognitive_load_budget, interface_spec, system_empowerment_index | "Human reviews 3 flags per cohort" |
| **Phase 6** — Validation & Iteration | **Events**, Knowledge | test_case, progressive_autonomy_schedule, mva_spec, validation_result | "H1: typed fragments > prose" |

### Type Collision Resolution at the Data Layer

This is where your tridirectional type collision insight becomes architecture. The data model enforces:

1. **Output type collision** → Each artefact HAS a type. The code generator renders different types differently.
2. **Input type collision** → Each workspace maps to a cognitive mode. The user never enters a boundary decision in a narrative text field.
3. **Extraction type collision** → When importing from documents, the system extracts typed knowledge objects FROM documents, not documents WITH metadata.

---

## 2. The Seven Phase Workspaces — Cognitive Mode Mapping

Each CAWDP phase manifests as a distinct workspace with its own interaction modality. The user never sees "Phase 1: Task Intelligence" — they see the workspace that matches their current cognitive mode.

### The Workspace Map

```
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 0 · The North Star                                          │
│  Cognitive Mode: Exploration → "The Possibility Garden"            │
│  "What does success look like?"                                     │
│  ═══════════════════════════════════════════════════════════════     │
│  [Curated alternatives]  [Goal cards]  [Constraint fence]           │
│  Artefacts: Intentions (goals, constraints, 12 characteristics)     │
│  Quality Gate: All 12 characteristics at confidence ≥ 0.5         │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 1 · The Decomposition Table                                 │
│  Cognitive Mode: Boundary → "The Fence" + Architecture → "Floor"   │
│  "What are all the tasks? What type is each?"                       │
│  ═══════════════════════════════════════════════════════════════     │
│  [Task cards with type badges]  [Drag-to-zone]  [Dependency arrows] │
│  Artefacts: Entities (tasks with op types), Relations (deps)        │
│  Quality Gate: All tasks decomposed to leaf + operation type set    │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 2 · The Allocation Map                                      │
│  Cognitive Mode: Configuration → "The Control Panel"               │
│                   + Evaluation → "The Growth Tracker"               │
│  "Who does this — Human, Agent, or System?"                         │
│  ═══════════════════════════════════════════════════════════════     │
│  [C×R Matrix]  [H/A/S zones]  [Complementarity scores]             │
│  Artefacts: Actors (with authority_boundary), Intentions (C×R)     │
│  Quality Gate: All tasks allocated, gaps ≥6 flagged human-only      │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 2.5 · The Event Wall (conditional — multi-agent only)       │
│  Cognitive Mode: Architecture → "The Workshop Floor"               │
│  "What events flow? What can go wrong?"                             │
│  ═══════════════════════════════════════════════════════════════     │
│  [Sticky-note events]  [Typed arrows]  [Failure event highlight]   │
│  Artefacts: Events (domain + failure), Relations (triggers, flows)  │
│  Quality Gate: Failure events ≥50% of domain events                 │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 3 · The Pipeline Builder                                    │
│  Cognitive Mode: Architecture + Verification → "Evidence Builder"  │
│  "How do tasks connect? What are the handoff contracts?"            │
│  ═══════════════════════════════════════════════════════════════     │
│  [DAG canvas]  [Typed edge contracts]  [Enforcement checkpoints]    │
│  Artefacts: Entities (stages, templates), Relations (handoffs)      │
│  Quality Gate: All handoffs typed, FMEA for top 3 failure modes    │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 4 · The Agent Workshop                                      │
│  Cognitive Mode: Configuration → "The Control Panel"               │
│                   + Boundary → "The Fence"                          │
│  "What is each agent's job? What must it NEVER do?"                 │
│  ═══════════════════════════════════════════════════════════════     │
│  [Archetype selector]  [Authority boundary = inverse of failure]    │
│  [Constraint toggles]  [Cost-benefit gauge]                         │
│  Artefacts: Actors (agent job descriptions), Knowledge (patterns)   │
│  Quality Gate: All agents have authority boundaries, stress tested  │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 5 · The Human Canvas                                        │
│  Cognitive Mode: Narrative → "The Origin Story"                     │
│                   + Evaluation → "The Growth Tracker"               │
│  "What does the human experience? Where do they judge?"             │
│  ═══════════════════════════════════════════════════════════════     │
│  [Decision journey]  [Judgment points]  [Cognitive load meter]      │
│  Artefacts: Actors (human spec), Scopes (load budget)               │
│  Quality Gate: Load budget ≤ cap, SEI ≥3 (Enabling)               │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 6 · The Test Track                                          │
│  Cognitive Mode: Verification → "The Evidence Builder"             │
│                   + Evaluation → "The Growth Tracker"               │
│  "How do we test this? What autonomy level?"                        │
│  ═══════════════════════════════════════════════════════════════     │
│  [Test case cards]  [Progressive autonomy slider]  [MVA checklist]  │
│  Artefacts: Events (validation), Knowledge (test results)           │
│  Quality Gate: All design decisions have tests, autonomy scheduled │
└─────────────────────────────────────────────────────────────────────┘
```

### Cross-Cutting Concerns — Always Visible

These run ACROSS all workspaces via a persistent right rail:

```
┌──────────────────┐
│ RIGHT RAIL        │
│ ─────────────     │
│ 📊 Quality Gate   │  ← Current gate status (pass/fail/waive)
│ 🏷️ Epistemic     │  ← Confidence, provenance on selected artefact
│ ⏰ Temporal       │  ← Staleness score, specification age
│ 🛡️ Governance     │  ← Authority boundary, verification level
│ 💰 Cost Budget    │  ← Running cost per agent/pipeline
│ 📋 Audit Trail    │  ← Every change, attributed and timestamped
│ 🔗 Connections    │  ← Graph edges to/from selected artefact
└──────────────────┘
```

---

## 3. The Guidance Engine — CAWDP Without Exposing CAWDP

The user never needs to know they're using CAWDP. The methodology is embedded in the system, not presented as a process to learn.

### How It Works

A **CAWDP Guidance Agent** (running in the Agno agent runtime) sits behind every workspace. It:

1. **Knows which phase the user is in** — via session state
2. **Knows what artefacts exist and what's missing** — by querying TypeDB
3. **Generates contextual guidance** — "I notice you have 5 tasks but 3 don't have operation types yet. Want me to suggest types?"
4. **Never says "You're in Phase 2"** — it says "Great decomposition! Now let's figure out who should do each task."
5. **Surface alternatives** — "Have you considered that this task might be better as System-first rather than Agent-first? Here's why..."
6. **Enforces quality gates** — "You can't move to the Pipeline Builder yet because 3 tasks don't have complementarity scores. Let's fix those first."

### The Guidance Agent Is a Mirror, Not a Director

Per your Accretive Workspace principles, the agent role in the Lattice shape is **Mirror** — reflecting back what the user has decided, tracking drift, surfacing what changed. It does NOT tell the user what to do. It prepares structured decision inputs for human judgment.

```python
# CAWDP Guidance Agent
guidance_agent = Agent(
    name="CAWDPMirror",
    role="Mirror the user's design decisions back, surface gaps, suggest alternatives",
    model=Ollama(id="glm-5.1:cloud"),
    tools=[
        query_artefact_graph,   # Read from TypeDB
        query_pattern_library,  # Read from Chroma
        check_quality_gate,     # Evaluate gate criteria
        suggest_alternatives,   # Generate alternative allocations
    ],
    instructions="""
    You are a CAWDP Mirror agent. Your job is to:
    1. Reflect what the user has decided, not what they should decide
    2. Surface gaps in the current design
    3. Suggest alternatives when the user is stuck
    4. Flag when quality gates are not met
    5. NEVER make design decisions — the human decides
    6. Attach epistemic metadata to every suggestion
    
    You know the CAWDP methodology but you never name it.
    You know which phase the user is in but you never say it.
    You guide through the work, not through the process.
    """
)
```

### Phase Transition Logic

Phase transitions happen when quality gates pass, not when the user clicks "Next." This is structural, not navigational:

```python
def can_advance(current_phase: int, artefacts: list[DesignArtefact]) -> GateResult:
    """Quality gate evaluation — structural, not optional"""
    
    gate_criteria = GATE_DEFINITIONS[current_phase]
    
    results = []
    for criterion in gate_criteria:
        matching = [a for a in artefacts if criterion.matches(a)]
        if criterion.severity == "blocking" and len(matching) == 0:
            results.append(GateFailure(
                criterion=criterion,
                message=f"Missing: {criterion.description}",
                remediation=criterion.remediation_hint
            ))
        elif criterion.severity == "warning" and len(matching) == 0:
            results.append(GateWarning(
                criterion=criterion,
                message=f"Recommended: {criterion.description}",
                can_proceed=True
            ))
        else:
            results.append(GatePass(criterion=criterion))
    
    return GateResult(
        can_advance=all(r.can_proceed for r in results),
        results=results
    )
```

---

## 4. The Quality Gate Engine — Executable Assertions

Quality gates are the structural enforcement of CAWDP's design discipline. They are NOT checkboxes — they are executable assertions that query the artefact graph.

### Gate Definitions Per Phase

| Phase | Gate | Assertion (pseudocode) | Severity |
|---|---|---|---|
| **0** | All 12 characteristics defined | `count(artefacts.where(type='target_characteristic')) >= 12` | Blocking |
| **0** | At least 3 goals | `count(artefacts.where(type='goal')) >= 3` | Blocking |
| **0** | Constraints include reversibility constraint | `artefacts.where(type='constraint').exists(c -> 'reversibility' in c.content.tags)` | Warning |
| **1** | All tasks decomposed to leaf level | `all(artefacts.where(type='task').is_leaf())` | Blocking |
| **1** | All tasks have operation type | `all(artefacts.where(type='task').has('cognitive_operation_type'))` | Blocking |
| **1** | Dependencies are acyclic | `graph(artefacts, relations).is_dag()` | Blocking |
| **2** | All tasks have allocation | `all(artefacts.where(type='task').has('allocated_to'))` | Blocking |
| **2** | Complementarity gaps ≥6 flagged | `all(artefacts.where(gap>=6).allocated_to == 'human')` | Blocking |
| **2** | Reversibility classified | `all(artefacts.where(type='task').has('reversibility_class'))` | Warning |
| **2.5** | Failure events ≥50% domain events | `count(failure_events) / count(domain_events) >= 0.5` | Warning |
| **3** | All handoffs have typed contracts | `all(relations.where(type='handoff-to').has('contract_schema_id'))` | Blocking |
| **3** | FMEA for top 3 failure modes | `count(artefacts.where(type='fmea_entry')) >= 3` | Blocking |
| **3** | System enforcement points defined | `count(artefacts.where(type='system_enforcement_point')) >= 1` | Warning |
| **4** | All agents have authority boundaries | `all(agents.has('authority_boundary'))` | Blocking |
| **4** | Boundary = inverse of failure mode | `all(agents.where(failure='noise-as-signal').boundary == 'never_interpret')` | Blocking |
| **4** | Cost-benefit assessed per agent | `all(agents.has('cost_benefit'))` | Warning |
| **5** | Cognitive load budget ≤ cap | `sum(human_decision_points.load) <= budget_cap` | Blocking |
| **5** | System Empowerment Index ≥3 | `min(agents.sei_score) >= 3` | Warning |
| **6** | All design decisions have tests | `all(decisions.has_matching_test())` | Blocking |
| **6** | Progressive autonomy schedule defined | `exists(artefacts.where(type='progressive_autonomy_schedule'))` | Blocking |

---

## 5. The Design-to-Implementation Bridge

**This is the critical architectural innovation.** The PRISM graph isn't just a design store — it IS the implementation specification. A set of transformers traverse the graph and produce Agno implementation code.

### Six Transformers

```
┌──────────────────────────────────────────────────────────────┐
│              DESIGN-TO-IMPLEMENTATION BRIDGE                  │
│                                                              │
│  PRISM Graph (TypeDB)                                        │
│       │                                                      │
│       ├──→ [1] Actor → Agno Agent Transformer                │
│       │     Reads: Actor entities with authority_boundary,   │
│       │     role, cognitive_orientation, capability_boundary  │
│       │     Produces: Agno Agent class definition             │
│       │                                                      │
│       ├──→ [2] Coalition → Agno Team Transformer             │
│       │     Reads: Actor groups + Relations (supervision)    │
│       │     Produces: Agno Team definition with mode/members  │
│       │                                                      │
│       ├──→ [3] Events + Relations → Agno Workflow Transformer│
│       │     Reads: Event sequences, trigger conditions,      │
│       │     handoff contracts, data flows                    │
│       │     Produces: Agno Workflow with steps, step_choices,│
│       │     session state management                         │
│       │                                                      │
│       ├──→ [4] Schema Registry → Pydantic Models Transformer │
│       │     Reads: Schema Registry entries                   │
│       │     Produces: Pydantic BaseModel classes for all I/O  │
│       │                                                      │
│       ├──→ [5] Governance → Verification Protocol Transformer│
│       │     Reads: Policies, authority boundaries,           │
│       │     verification independence levels                 │
│       │     Produces: Verification agent defs, audit config   │
│       │                                                      │
│       └──→ [6] Full Graph → Agent Operations Manual Transform│
│             Reads: Entire design graph                       │
│             Produces: Markdown Agent Operations Manual       │
│             (born-agent-native template)                     │
│                                                              │
│  Every transformer output is traceable:                      │
│  code_artefact.design_artefact_ids → PRISM entities          │
└──────────────────────────────────────────────────────────────┘
```

### Transformer Example: Actor → Agno Agent

```python
def transform_actor_to_agno_agent(actor: DesignArtefact) -> str:
    """Read an Actor entity with agent_job_description and produce Agno code"""
    
    content = actor.content
    epistemic = actor.epistemic
    
    # Authority boundary IS the inverse of failure mode
    authority_boundary = content.get("authority_boundary", {})
    failure_mode = content.get("characteristic_failure_mode", "")
    
    # Generate Agno Agent definition
    agent_code = f'''
from agno.agent import Agent
from agno.models.ollama import Ollama
from pydantic import BaseModel, Field

class {content["name"]}Output(BaseModel):
    """Structured output for {content["name"]}"""
    {generate_pydantic_fields(content["output_schema"])}

{content["name"]} = Agent(
    name="{content['name']}",
    role="{content['role_description']}",
    model=Ollama(id="{content.get('model_id', 'glm-5.1:cloud')}"),
    tools=[{generate_tool_imports(content['capability_boundary']['tools'])}],
    instructions=[
        "{content['role_description']}",
        "AUTHORITY BOUNDARY: {authority_boundary['constraint']}",
        "FAILURE MODE: {failure_mode} — this boundary prevents it",
        "NEVER {authority_boundary['prohibited']}",
        "When uncertain: {content['escalation_protocol']}",
        "Epistemic metadata: always attach confidence, assumptions, limitations",
    ],
    response_model={content["name"]}Output,
)
'''
    # Attach traceability metadata
    agent_code += f"\n# Generated from design artefact: {actor.id}"
    agent_code += f"\n# PRISM dimension: actors, type: {actor.type}"
    agent_code += f"\n# CAWDP Phase: {actor.governance.cawdp_phase}"
    agent_code += f"\n# Design confidence: {epistemic.confidence}"
    
    return agent_code
```

### Transformer Example: Events + Relations → Agno Workflow

```python
def transform_events_to_agno_workflow(
    events: list[DesignArtefact],
    relations: list[DesignRelation],
    actors: list[DesignArtefact]
) -> str:
    """Read event sequences and produce Agno Workflow definition"""
    
    # Build execution order from dependency graph
    dag = build_dag(events, relations.where(type='depends-on'))
    stages = topological_sort(dag)
    
    # Map each stage to agent(s)
    workflow_steps = []
    for stage in stages:
        allocated_actors = get_allocated_actors(stage, actors, relations)
        is_human_gate = any(a.type == 'human_actor' for a in allocated_actors)
        
        if is_human_gate:
            workflow_steps.append(f'''
    # HUMAN CHECKPOINT — {stage.content['name']}
    # Complementarity gap: {stage.content.get('gap_score', 'N/A')}
    workflow.add_human_checkpoint(
        name="{stage.content['name']}",
        context="{stage.content['human_decision_description']}",
    )''')
        else:
            agent_refs = [a.content['variable_name'] for a in allocated_actors]
            workflow_steps.append(f'''
    workflow.add_step(
        name="{stage.content['name']}",
        agent={agent_refs[0]},  # Primary agent
        # Parallel agents: {agent_refs[1:] if len(agent_refs) > 1 else 'none'}
    )''')
    
    return f'''
from agno.workflow import Workflow

class {workflow_name}Workflow(Workflow):
    """Generated from CAWDP Design Studio"""
    
    def run(self, input_data):
{''.join(workflow_steps)}
'''
```

---

## 6. System Architecture — Tech Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FRONTEND LAYER                               │
│  AstroJS v6+ / HeroUI v3 / Shadcn                                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐               │
│  │ North    │ │ Decompo- │ │ Alloc-   │ │ Pipeline  │  ...7         │
│  │ Star     │ │ sition   │ │ ation    │ │ Builder    │  workspace   │
│  │ (Phase 0)│ │ Table    │ │ Map      │ │ (Phase 3) │  pages       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘               │
│  Shared: @dnd-kit (drag-sort), @xyflow/react (DAG canvas),          │
│  Type-coloured borders, Energy/Confidence dots,                     │
│  Right Rail (epistemic + governance + temporal + quality gate),     │
│  Capture Bar (zero-friction input), Next Step indicator             │
├─────────────────────────────────────────────────────────────────────┤
│                         API LAYER                                    │
│  Hono v4 on Cloudflare Workers                                      │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                 │
│  │ Artefact CRUD│ │ Gate Eval    │ │ Transform &  │                 │
│  │ (PRISM ops)  │ │ (quality)    │ │ Export (bridge│                 │
│  └──────────────┘ └──────────────┘ └──────────────┘                 │
│  + Session management + User auth + Audit trail ingestion           │
├─────────────────────────────────────────────────────────────────────┤
│                    AGENT RUNTIME LAYER                               │
│  Agno v2.5+ AgentOS / Python FastAPI                                │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐        │
│  │ CAWDP      │ │ Quality    │ │ Decompo-   │ │ Template   │        │
│  │ Mirror     │ │ Gate Agent │ │ sition Asst│ │ Agent      │        │
│  │ (guidance) │ │ (evaluate)│ │ (assist)    │ │ (archetype)│        │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘        │
│  LLM: Ollama Cloud (glm-5.1:cloud)                                  │
├─────────────────────────────────────────────────────────────────────┤
│                       DATA LAYER                                     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌────────────┐ │
│  │ TypeDB v4.12 │ │ Chroma v1.5  │ │ Postgres     │ │ MinIO/R2   │ │
│  │ PRISM Graph  │ │ Pattern Lib  │ │ Sessions     │ │ Exports    │ │
│  │ (artefacts + │ │ (archetype   │ │ Audit trail  │ │ Documents  │ │
│  │  relations + │ │  embeddings, │ │ User data    │ │ Generated  │ │
│  │  schemas)    │ │  RAG)        │ │ Cost tracking│ │ code        │ │
│  └──────────────┘ └──────────────┘ └──────────────┘ └────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### Why TypeDB for the PRISM Graph

TypeDB's type system is the closest match to PRISM's dimensional + cross-cutting architecture:

- **7 PRISM dimensions** → 7 TypeDB entity types
- **Typed relations** → TypeDB relation types with role players
- **Cross-cutting layers** → TypeDB attributes on every entity/relation
- **Schema Registry** → TypeDB rule system for validation
- **Graph traversal** → TypeDB's native query language traverses relations efficiently
- **Schema evolution** → TypeDB supports incremental schema changes without migration

### TypeDB Schema Sketch (PRISM)

```tql
define

# PRISM DIMENSIONS
scopes sub entity,
  plays scope:member,
  has name, has description, has isolation_boundary;

actors sub entity,
  plays relation:actor,
  has name, has role_type, has authority_boundary,
  has cognitive_orientation, has capability_boundary;

entities sub entity,
  plays relation:entity,
  has name, has entity_type, has content;

relations sub relation,
  relates source,
  relates target,
  has relation_type, has strength;

events sub entity,
  plays relation:event,
  has name, has event_type, has trigger_condition,
  has reasoning_id, has assurance_level;

knowledge sub entity,
  plays relation:knowledge,
  has name, has knowledge_type, has content,
  has provenance, has relevance_score;

intentions sub entity,
  plays relation:intention,
  has name, has intention_type,
  has content, has reasoning_id;

# CROSS-CUTTING LAYERS (attributes on every entity/relation)
# Epistemic Layer
confidence sub attribute, double;
provenance sub attribute, string;
assumptions sub attribute, string;  
limitations sub attribute, string;
assessedAt sub attribute, datetime;
uncertainty sub attribute, double;

# Governance Layer  
authority_boundary sub attribute, string;
access_policy sub attribute, string;
verification_level sub attribute, string;
cawdp_phase sub attribute, long;
quality_gate_status sub attribute, string;

# Temporal Layer
version sub attribute, long;
specification_age_days sub attribute, long;

# Schema Layer
schema_id sub attribute, string;
schema_version sub attribute, string;
validation_status sub attribute, string;

# DESIGN RELATIONS (typed connections between artefacts)
depends-on sub relation,
  relates source, relates target;
generated-by sub relation,
  relates source, relates target;
evolves-from sub relation,
  relates source, relates target;
allocates-to sub relation,
  relates source, relates target;
handoff-to sub relation,
  relates source, relates target;
verifies sub relation,
  relates source, relates target;
constrains sub relation,
  relates source, relates target;
```

---

## 7. The User Journey — Screen-by-Screen

### Home Screen

```
┌─────────────────────────────────────────────────────────────────┐
│  CAWDP Design Studio                                   [User]   │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐                       │
│  │ 🌟 New Design   │  │ 📂 Recent       │                       │
│  │                 │  │                 │                       │
│  │ Start from      │  │ Assignment      │                       │
│  │ scratch or      │  │ Marking v1  67% │                       │
│  │ template?        │  │ KB Ingestion 23%│                       │
│  └─────────────────┘  └─────────────────┘                       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 🧩 Template Library                                  │       │
│  │ Content Review Pipeline · 4 agents · 2 human gates   │       │
│  │ Customer Support Router · 6 agents · 1 human gate    │       │
│  │ Assignment Marking (full) · 23 agents · 13 gates     │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│  ┌──────┐                                                       │
│  │ Next │ ← One Clear Next Step Always                          │
│  └──────┘                                                       │
└─────────────────────────────────────────────────────────────────┘
```

### Phase Workspace (example: Phase 2 — The Allocation Map)

```
┌─────────────────────────────────────────────────────────────────┐
│  ◀ North Star  │  Decomposition ✓  │ ● ALLOCATION  │ Pipeline  │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────────────────────────┐  ┌──────────────────┐ │
│  │                                     │  │ 🛡️ GOVERNANCE    │ │
│  │   C×R MATRIX                       │  │ ──────────       │ │
│  │                                     │  │ Phase: 2         │ │
│  │  High R │ A A S S H H             │  │ Gate: 2/4 pass  │ │
│  │  Med R  │ A S S H H H             │  │                  │ │
│  │  Low R  │ S S H H H H             │  │ 📊 EPISTEMIC     │ │
│  │          ─────────────────         │  │ Selected:        │ │
│  │          Lo  Med  Hi  Confidence   │  │ Claims Analyst   │ │
│  │                                     │  │ C: 0.7 P: Agent │ │
│  │  [drag task → zone to allocate]    │  │ Assumptions: ... │ │
│  │                                     │  │                  │ │
│  │  TASK ZONES                         │  │ ⏰ TEMPORAL       │ │
│  │  ┌─ HUMAN ──┐ ┌─ AGENT ──┐       │  │ Age: 2 days      │ │
│  │  │Score C2  │ │Claims Ana│       │  │ Staleness: 0.03  │ │
│  │  │Score C3  │ │Comm Assr │       │  │                  │ │
│  │  └──────────┘ │Drift Det │       │  │ 🔗 CONNECTIONS    │ │
│  │               └──────────┘       │  │ depends-on: 3    │ │
│  │  ┌─ SYSTEM ──┐                    │  │ feeds-into: 2    │ │
│  │  │Audit log  │                    │  │ generated-by: 1  │ │
│  │  └──────────┘                    │  └──────────────────┘ │
│  └─────────────────────────────────────┘                       │
│                                                                 │
│  ┌──────────────────────────────────────────────────────┐      │
│  │ 💬 "3 tasks still need allocation. The C×R matrix    │      │
│  │ suggests 'Review feedback' is high-confidence,       │      │
│  │ low-reversibility — a strong human-only candidate."  │      │
│  └──────────────────────────────────────────────────────┘      │
│                                                                 │
│  ┌──────────────┐                                               │
│  │ Resolve 3 →  │ ← One Clear Next Step                        │
│  └──────────────┘                                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Key Architectural Decisions

### Decision 1: The Design Artefact Graph IS the Product

The PRISM graph in TypeDB is not a staging area for a document — it IS the design output. Documents (markdown, PDF) are DERIVED VIEWS of the graph, just like prose is a derived view of fragments in the Accretive Workspace. This inverts the current paradigm where the document is primary and data is metadata.

**Consequence:** Every export format is a transformer that reads the graph and produces a view. There is no "save as document" — there is "render as document from graph."

### Decision 2: Quality Gates Are Structural, Not Optional

You cannot advance to Phase 3 without passing Phase 2 quality gates. This is not a UX preference — it is architecture. The system physically prevents creation of Phase 3 artefacts until Phase 2 gates pass. Waivers are possible but must be explicitly approved with a recorded rationale (governance layer).

### Decision 3: The CAWDP Methodology Is Invisible to the User

The user never sees "Phase 2: Capability Allocation." They see "Who does what?" The methodology is embedded in the system's structure, not presented as a process to learn. This is the same principle as your CoS Agent Platform — the methodology IS the platform.

**Consequence for Future's Edge:** This app simultaneously IS a CAWDP teaching tool and hides CAWDP from the user. After completing a design, the user can choose to "reveal the methodology" — showing them that they just used CAWDP without knowing it. This is the same on-ramp you designed for Rifadh.

### Decision 4: Type Collision Is Resolved at Every Layer

- **Output:** Every artefact is typed → rendered differently per type
- **Input:** Every workspace uses a different cognitive mode → user enters data in the right modality
- **Extraction:** When importing designs, the system extracts typed objects from documents

### Decision 5: The Design-to-Implementation Bridge Is Bidirectional

The bridge works both ways:
- **Design → Code:** Transformers produce Agno implementation from design artefacts
- **Code → Design:** If an Agno agent is modified in production, the change can flow back to update the design artefact (specification aging trigger)

This creates a living specification — the design graph is never stale because production changes flow back.

---

## 9. What This Unifies

This architecture connects every major concept in your body of work:

| Prior Concept | How It Lives in the Design Studio |
|---|---|
| **PRISM** | The data model — every artefact is a PRISM entity with 4 cross-cutting layers |
| **CAWDP** | The process structure — 7 phases + 8 CCs + 5 quality gates embedded in the system |
| **Accretive Workspace** | The interaction paradigm — fragments + edges + shapes, but fragments = design artefacts |
| **Type Collision** | Resolved at all three layers (input, output, extraction) by design |
| **7 Cognitive Modes** | Mapped to 7 phase workspaces — right modality for each cognitive task |
| **ADHD Principles** | Zero-friction capture, one clear next step, visibility as memory, engagement over priority |
| **Agent-Native Org** | The Design Studio itself is a born-agent-native product |
| **Specification as Product** | The design IS the implementation spec — transformers produce code from the graph |
| **Trust Infrastructure** | Quality gates, epistemic metadata, audit trails, specification aging — all structural |
| **Agent Operations Manual** | Generated by Transformer #6 from the full design graph |

---

## 10. MVP Scope

To avoid the "premature platform" risk you identified, the MVP should be **one complete CAWDP phase**, not the full 7-phase system:

**Recommended MVP: Phase 1 + Phase 2 (Task Intelligence → Capability Allocation)**

Why these two:
- Phase 1 creates the task decomposition (the most universally needed CAWDP output)
- Phase 2 creates the complementarity allocation (the most novel CAWDP output — no other tool does this)
- Together they produce a **Complementarity Gap Diagnostic** — which is product #1.9 in your Red Hat model (the free 10-minute self-serve web tool)
- The C×R matrix visualization is a distinctive, shareable output
- Two phases is enough to validate H1 (typed fragments > prose) and H3 (complementarity routing improves completion)
- The guidance agent only needs to understand 2 phases

**MVP Tech Scope:**
- Frontend: 2 workspace pages (Decomposition Table + Allocation Map) + Home
- API: Artefact CRUD + Gate evaluation
- Agent Runtime: 1 guidance agent
- Data: TypeDB for artefact graph, Postgres for sessions
- Bridge: 1 transformer (Export as JSON/YAML complementarity report — not full Agno code yet)

**MVP Timeline: 3-4 weeks** (using Agno agent-augmented development)

---

Peter, this architecture makes your design artefacts the first-class product — not documents about the design, but the design itself as structured, typed, connected, metadata-rich data that another process can consume to generate implementation. The CAWDP methodology is the skeleton; PRISM is the data model; the Accretive Workspace paradigm is the interaction model; and the Design-to-Implementation Bridge is the feature that makes this product category-defining.

Want me to go deeper on any specific layer, or start on the TypeDB schema definition for the MVP?The memory has been captured. This architecture document represents a significant convergence point for your body of work — PRISM becomes the data model, CAWDP becomes the process engine, the Accretive Workspace becomes the interaction paradigm, and the Design-to-Implementation Bridge makes "specification as product" a concrete, executable feature rather than an aspiration.

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-04-18T05:51:48* · `glm-5.1:cloud` · `e6055ac6...`

### Prompt

yes, use PRISM to start on the TypeDB schema

### Response

Now let me write the complete TypeDB schema. This is a production-ready `schema.tql` file for the PRISM-based Design Artefact Graph.

---

# PRISM TypeDB Schema for CAWDP Design Studio

```tql
# ═══════════════════════════════════════════════════════════════════
# PRISM — Patterned Refraction of Intelligence Systems Model
# TypeDB Schema for CAWDP Design Studio
# Version: 1.0.0
# 
# Architecture: 7 PRISM Dimensions + 4 Cross-Cutting Layers
#               + Infrastructure Types
#               + Typed Relations
#               + Computation Rules
#
# DESIGN PRINCIPLES:
#   1. Every entity inherits from prism-artefact → carries 4 cross-cutting layers
#   2. Every relation inherits from prism-relation → carries cross-cutting layers
#   3. Content schemas validated via schema-registry, NOT properties:any
#   4. Authority boundaries encoded in the data, not external policy docs
#   5. Epistemic metadata on every artefact (CC-3 operationalised at data layer)
#   6. Specification aging via assessedAt + staleness rules (CC-5)
#   7. Type collision resolved — every artefact HAS a type
# ═══════════════════════════════════════════════════════════════════

define

# ═══════════════════════════════════════════════════════════════════
# SECTION 0: PRIMITIVE ATTRIBUTE TYPES
# ═══════════════════════════════════════════════════════════════════

# --- Identity Attributes ---
prism-id sub attribute, string;
name sub attribute, string;
description sub attribute, string;

# --- Epistemic Layer Attributes (CC-3) ---
confidence sub attribute, double;           # 0.0 - 1.0
provenance sub attribute, string;           # who/what created this artefact
assumption-text sub attribute, string;      # a single stated assumption
limitation-text sub attribute, string;      # a single known limitation
assessed-at sub attribute, datetime;        # when last assessed (staleness scoring)
uncertainty sub attribute, double;          # 0.0 - 1.0

# --- Governance Layer Attributes ---
authority-boundary sub attribute, string;   # what this artefact can/cannot decide
access-policy sub attribute, string;         # read/write permissions
verification-level sub attribute, string;    # 'structural' | 'semantic' | 'authority'
cawdp-phase sub attribute, long;            # 0-6, which CAWDP phase produced this
quality-gate-status sub attribute, string;  # 'pending' | 'passed' | 'failed' | 'waived'
gate-waiver-rationale sub attribute, string; # why a gate was waived

# --- Temporal Layer Attributes ---
version-number sub attribute, long;         # monotonically increasing version
specification-age-days sub attribute, long; # auto-calculated from assessed-at
staleness-score sub attribute, double;       # 0.0 - 1.0, auto-calculated
refresh-cadence-days sub attribute, long;    # how often this should be revisited

# --- Schema Layer Attributes ---
schema-id sub attribute, string;            # reference to schema-registry entry
schema-version sub attribute, string;       # version of the schema
validation-status sub attribute, string;    # 'valid' | 'invalid' | 'pending'

# --- Content Attributes (schema-validated JSON stored as string) ---
content-json sub attribute, string;          # JSON content validated by schema-registry

# --- PRISM-Specific Attributes ---
relevance-score sub attribute, double;      # 0.0 - 1.0, for context windowing
relation-strength sub attribute, double;    # 0.0 - 1.0, connection strength
reasoning-id sub attribute, string;         # trace to Intentions dimension
assurance-level sub attribute, string;      # 'logged' | 'assured' | 'verified' (CC-8)

# --- Actor-Specific Attributes ---
actor-type sub attribute, string;           # 'human' | 'agent' | 'system'
role-type sub attribute, string;            # 'executor' | 'reviewer' | 'orchestrator' | 'synthesiser' | 'articulation' | 'exploration'
cognitive-orientation sub attribute, string; # 'critical' | 'optimistic' | 'creative' | 'factual' | 'procedural' | 'synthesiser'
agent-class sub attribute, string;          # 'extractor' | 'measurer' | 'assessor' | 'generator' | 'aggregator'
failure-mode sub attribute, string;          # characteristic failure mode
prohibited-action sub attribute, string;     # what this actor MUST NEVER do
model-id sub attribute, string;             # LLM model identifier
model-temperature sub attribute, double;    # LLM temperature
cost-budget sub attribute, double;          # per-agent cost budget (CC-7)
escalation-path sub attribute, string;      # who to escalate to

# --- Complementarity Attributes ---
human-score sub attribute, long;            # H: 0-10
agent-score sub attribute, long;            # A: 0-10
system-score sub attribute, long;           # S: 0-10
complementarity-gap sub attribute, long;    # max(H,A,S) - second_max(H,A,S)
reversibility-class sub attribute, string;  # 'read-only' | 'reversible' | 'irreversible'
allocation-target sub attribute, string;    # 'human' | 'agent' | 'system' | 'collaborative'

# --- Intention-Specific Attributes ---
intention-type sub attribute, string;       # 'goal' | 'constraint' | 'mandate' | 'guardrail' | 'preference' | 'assumption' | 'complementarity-decision' | 'reversibility-classification'

# --- Event-Specific Attributes ---
event-type sub attribute, string;           # 'domain' | 'failure' | 'trigger' | 'validation' | 'data-flow'
trigger-condition sub attribute, string;    # what triggers this event
severity sub attribute, string;             # 'low' | 'medium' | 'high' | 'critical'

# --- Entity-Specific Attributes ---
entity-type sub attribute, string;          # 'task' | 'pipeline-stage' | 'template' | 'fmea-entry' | 'target-characteristic' | 'cognitive-operation' | 'mva-spec'
cognitive-operation-type sub attribute, string; # 'mechanical' | 'analytical' | 'evaluative' | 'generative' | 'intuitive'
is-leaf sub attribute, boolean;            # is this a leaf-level decomposition?
template-type sub attribute, string;        # 'input' | 'output' | 'handoff' | 'verification' | 'decision' | 'feedback' | 'escalation'

# --- Knowledge-Specific Attributes ---
knowledge-type sub attribute, string;       # 'pattern' | 'insight' | 'decision' | 'evidence' | 'constraint' | 'agent-job-description' | 'archetype-instance' | 'test-result' | 'interface-spec' | 'progressive-autonomy-schedule'

# --- Scope-Specific Attributes ---
scope-type sub attribute, string;           # 'design-scope' | 'isolation-boundary' | 'system-enforcement-point' | 'cognitive-load-budget'
isolation-type sub attribute, string;       # 'tenant' | 'project' | 'phase' | 'actor'
load-capacity sub attribute, long;          # cognitive load budget capacity
load-consumed sub attribute, long;         # cognitive load currently consumed

# --- Progressive Autonomy Attributes ---
autonomy-level sub attribute, string;       # 'shadow' | 'advisory' | 'supervised' | 'autonomous'
autonomy-graduation-criteria sub attribute, string; # what must be true to advance

# --- System Empowerment Attributes ---
sei-score sub attribute, long;             # 1-5: Constraining→Informing→Enabling→Amplifying→Liberating

# --- Infrastructure Attributes ---
session-id sub attribute, string;          # design session identifier
user-id sub attribute, string;             # user who created artefact
timestamp sub attribute, datetime;         # creation/modification time
action-type sub attribute, string;         # 'create' | 'update' | 'delete' | 'gate-eval' | 'waive' | 'transform'


# ═══════════════════════════════════════════════════════════════════
# SECTION 1: PRISM ARTEFACT — ABSTRACT BASE TYPE
# All 7 PRISM dimensions inherit from this, gaining 4 cross-cutting layers
# ═══════════════════════════════════════════════════════════════════

prism-artefact sub entity,
  abstract,
  # Identity
  has prism-id,
  has name,
  has description,
  # Epistemic Layer (CC-3) — every artefact carries these 6 fields
  has confidence,
  has provenance,
  has assumption-text,
  has limitation-text,
  has assessed-at,
  has uncertainty,
  # Governance Layer — authority and access baked into the data
  has authority-boundary,
  has access-policy,
  has verification-level,
  has cawdp-phase,
  has quality-gate-status,
  has gate-waiver-rationale,
  # Temporal Layer — versioning and staleness
  has version-number,
  has specification-age-days,
  has staleness-score,
  has refresh-cadence-days,
  # Schema Layer — validated content, NOT properties:any
  has schema-id,
  has schema-version,
  has validation-status,
  # Content — schema-validated JSON
  has content-json,
  # Metadata
  has user-id,
  has timestamp,
  plays scoped-by:scoped-artefact,
  plays generated-by:generated-artefact,
  plays evolves-from:previous-version,
  plays evolves-from:current-version,
  plays supports:supported-artefact,
  plays supports:supporting-evidence,
  plays contradicts:contradicted-artefact,
  plays contradicts:contradicting-evidence;


# ═══════════════════════════════════════════════════════════════════
# SECTION 2: SEVEN PRISM DIMENSIONS (Entity Types)
# ═══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# DIMENSION 1: SCOPES — Isolation, boundaries, budgets
# ──────────────────────────────────────────────────────────────

scope sub prism-artefact,
  abstract,
  has scope-type,
  plays scoped-by:containing-scope;

design-scope sub scope,
  has isolation-type,
  plays allocation-scope:scope-container;

isolation-boundary sub scope,
  has isolation-type;

system-enforcement-point sub scope,
  has description;

cognitive-load-budget sub scope,
  has load-capacity,
  has load-consumed,
  plays load-governor:budget-holder;


# ──────────────────────────────────────────────────────────────
# DIMENSION 2: ACTORS — Person / Agent / System
# Broader than ONE's "people" — includes agent job descriptions
# and authority boundaries (complementarity modeling)
# ──────────────────────────────────────────────────────────────

actor sub prism-artefact,
  abstract,
  has actor-type,
  has authority-boundary,
  has role-type,
  has cognitive-orientation,
  has cost-budget,
  has escalation-path,
  has sei-score,
  plays allocation-scope:allocated-actor,
  plays handoff-to:handoff-source,
  plays handoff-to:handoff-target,
  plays supervised-by:supervisor,
  plays supervised-by:supervisee,
  plays verifies:verifier-actor,
  plays load-governor:actor-load;

human-actor sub actor,
  has human-score,
  has complementarity-gap;

agent-actor sub actor,
  has agent-score,
  has agent-class,
  has failure-mode,
  has prohibited-action,
  has model-id,
  has model-temperature,
  has autonomy-level,
  has autonomy-graduation-criteria;

system-actor sub actor,
  has system-score;


# ──────────────────────────────────────────────────────────────
# DIMENSION 3: ENTITIES — With Schema Registry validation
# Replaces ONE's properties:any with validated, typed content
# ──────────────────────────────────────────────────────────────

prism-entity sub prism-artefact,
  abstract,
  has entity-type,
  plays depends-on:dependent,
  plays depends-on:dependency,
  plays feeds-into:data-source,
  plays feeds-into:data-sink;

task sub prism-entity,
  has cognitive-operation-type,
  has is-leaf,
  has human-score,
  has agent-score,
  has system-score,
  has complementarity-gap,
  has reversibility-class,
  has allocation-target,
  plays allocation-scope:allocated-task;

cognitive-operation sub prism-entity,
  has cognitive-operation-type;

pipeline-stage sub prism-entity,
  has description,
  plays triggers:triggering-stage,
  plays triggers:triggered-stage;

template sub prism-entity,
  has template-type,
  has content-json;

fmea-entry sub prism-entity,
  has failure-mode,
  has severity,
  has description;

target-characteristic sub prism-entity,
  has description;

mva-spec sub prism-entity,
  has content-json;


# ──────────────────────────────────────────────────────────────
# DIMENSION 4: RELATIONS — Typed connections with strength
# (This dimension is realised via TypeDB's native relation types
#  defined in Section 3 below)
# ──────────────────────────────────────────────────────────────

# Note: In PRISM, the Relations dimension captures typed, weighted
# connections. In TypeDB, these are first-class relation types.
# Each relation type below IS a PRISM relation with full
# cross-cutting layer attributes.


# ──────────────────────────────────────────────────────────────
# DIMENSION 5: EVENTS — With reasoningId, 3-level assurance
# ──────────────────────────────────────────────────────────────

event sub prism-artefact,
  abstract,
  has event-type,
  has reasoning-id,
  has assurance-level,
  has trigger-condition,
  has severity,
  plays triggers:event-source,
  plays triggers:event-target;

domain-event sub event,
  has event-type;

failure-event sub event,
  has failure-mode,
  has severity;

trigger-condition-event sub event,
  has trigger-condition;

validation-event sub event,
  has validation-status,
  has content-json;

data-flow-event sub event,
  has content-json;


# ──────────────────────────────────────────────────────────────
# DIMENSION 6: KNOWLEDGE — With provenance, relevanceScore
# Types: pattern, insight, decision, evidence, constraint,
#        agent-job-description, archetype-instance, test-result,
#        interface-spec, progressive-autonomy-schedule
# ──────────────────────────────────────────────────────────────

knowledge sub prism-artefact,
  abstract,
  has knowledge-type,
  has relevance-score,
  plays supports:supporting-evidence,
  plays contradicts:contradicting-evidence;

pattern sub knowledge,
  has knowledge-type;

insight sub knowledge,
  has knowledge-type;

decision sub knowledge,
  has reasoning-id,
  has content-json;

evidence sub knowledge,
  has knowledge-type;

knowledge-constraint sub knowledge,
  has knowledge-type;

agent-job-description sub knowledge,
  has agent-class,
  has failure-mode,
  has prohibited-action,
  has model-id,
  has model-temperature,
  has cost-budget,
  has escalation-path,
  has sei-score,
  has autonomy-level,
  has autonomy-graduation-criteria,
  has content-json;

archetype-instance sub knowledge,
  has content-json;

test-result sub knowledge,
  has validation-status,
  has content-json;

interface-spec sub knowledge,
  has content-json;

progressive-autonomy-schedule sub knowledge,
  has content-json;


# ──────────────────────────────────────────────────────────────
# DIMENSION 7: INTENTIONS — The missing "Why" dimension
# Goals, constraints, mandates, guardrails, preferences,
# assumptions, complementarity decisions, reversibility
# ──────────────────────────────────────────────────────────────

intention sub prism-artefact,
  abstract,
  has intention-type,
  has reasoning-id,
  plays constrains:constraining-intention,
  plays constrains:constrained-artefact,
  plays alternatives-considered:chosen-intention,
  plays alternatives-considered:rejected-intention;

goal sub intention,
  has intention-type;

design-constraint sub intention,
  has intention-type,
  has reversibility-class;

mandate sub intention,
  has intention-type;

guardrail sub intention,
  has intention-type,
  has prohibited-action;

preference sub intention,
  has intention-type;

assumption sub intention,
  has intention-type;

complementarity-decision sub intention,
  has intention-type,
  has human-score,
  has agent-score,
  has system-score,
  has complementarity-gap,
  has allocation-target,
  has content-json;

reversibility-classification sub intention,
  has intention-type,
  has reversibility-class;


# ═══════════════════════════════════════════════════════════════════
# SECTION 3: TYPED RELATIONS (PRISM Dimension 4 realised)
# Every relation inherits cross-cutting layers from prism-relation
# ═══════════════════════════════════════════════════════════════════

prism-relation sub relation,
  abstract,
  # Epistemic Layer on relations
  has confidence,
  has provenance,
  has assessed-at,
  # Governance Layer on relations
  has access-policy,
  has verification-level,
  # Temporal Layer on relations
  has version-number,
  has assessed-at,
  # Connection strength for context windowing
  has relation-strength,
  has reasoning-id;

# --- Structural Relations ---

depends-on sub prism-relation,
  relates dependent,
  relates dependency;

generated-by sub prism-relation,
  relates generated-artefact,
  relates generating-artefact;

evolves-from sub prism-relation,
  relates previous-version,
  relates current-version;

# --- Allocation Relations ---

allocation-scope sub prism-relation,
  relates scope-container,
  relates allocated-task,
  relates allocated-actor;

# --- Pipeline Relations ---

handoff-to sub prism-relation,
  relates handoff-source,
  relates handoff-target,
  has content-json;

supervised-by sub prism-relation,
  relates supervisor,
  relates supervisee;

# --- Verification Relations ---

verifies sub prism-relation,
  relates verifier-actor,
  relates verified-artefact;

# --- Governance Relations ---

constrains sub prism-relation,
  relates constraining-intention,
  relates constrained-artefact;

scoped-by sub prism-relation,
  relates scoped-artefact,
  relates containing-scope;

# --- Causation Relations ---

triggers sub prism-relation,
  relates triggering-stage,
  relates triggered-stage,
  relates event-source,
  relates event-target;

# --- Data Flow Relations ---

feeds-into sub prism-relation,
  relates data-source,
  relates data-sink;

# --- Evidence Relations ---

supports sub prism-relation,
  relates supporting-evidence,
  relates supported-artefact;

contradicts sub prism-relation,
  relates contradicting-evidence,
  relates contradicted-artefact;

# --- Design Decision Relations ---

alternatives-considered sub prism-relation,
  relates chosen-intention,
  relates rejected-intention,
  has content-json;

# --- Cognitive Load Relations ---

load-governor sub prism-relation,
  relates budget-holder,
  relates actor-load;


# ═══════════════════════════════════════════════════════════════════
# SECTION 4: INFRASTRUCTURE TYPES
# ═══════════════════════════════════════════════════════════════════

# --- Schema Registry (replaces properties:any) ---

schema-registry sub entity,
  has schema-id,
  has schema-version,
  has name,
  has description,
  has content-json,
  has validation-status,
  has timestamp,
  plays schema-validation:validating-schema;

schema-validation sub relation,
  relates validated-artefact,
  relates validating-schema;

# --- Design Session ---

design-session sub entity,
  has session-id,
  has name,
  has description,
  has user-id,
  has timestamp,
  has cawdp-phase,
  has quality-gate-status,
  plays session-containment:containing-session;

session-containment sub relation,
  relates containing-session,
  relates contained-artefact;

# --- Quality Gate Results ---

quality-gate-result sub entity,
  has name,
  has cawdp-phase,
  has quality-gate-status,
  has gate-waiver-rationale,
  has content-json,
  has timestamp,
  has user-id;

# --- Audit Trail (CC-8: Assured Audit Trail) ---

audit-entry sub entity,
  has prism-id,
  has action-type,
  has user-id,
  has timestamp,
  has assurance-level,
  has content-json,
  plays audit-reference:audited-artefact;

audit-reference sub relation,
  relates audited-artefact,
  relates audit-entry-reference;


# ═══════════════════════════════════════════════════════════════════
# SECTION 5: COMPUTATION RULES
# ═══════════════════════════════════════════════════════════════════

# --- Complementarity Gap Calculation ---
# gap = max(H, A, S) - second_max(H, A, S)
# If gap >= 6, allocation is clear (human-only if H is max)
# This rule encodes the complementarity gap threshold

rule complementarity-gap-when-human-highest:
  when {
    $t is task;
    $t has human-score $h;
    $t has agent-score $a;
    $t has system-score $s;
    $h >= $a;
    $h >= $s;
    $gap = $h - max($a, $s);
  } then {
    $t has complementarity-gap $gap;
    $t has allocation-target "human";
  };

rule complementarity-gap-when-agent-highest:
  when {
    $t is task;
    $t has human-score $h;
    $t has agent-score $a;
    $t has system-score $s;
    $a >= $h;
    $a >= $s;
    $gap = $a - max($h, $s);
  } then {
    $t has complementarity-gap $gap;
    $t has allocation-target "agent";
  };

rule complementarity-gap-when-system-highest:
  when {
    $t is task;
    $t has human-score $h;
    $t has agent-score $a;
    $t has system-score $s;
    $s >= $h;
    $s >= $a;
    $gap = $s - max($h, $a);
  } then {
    $t has complementability-gap $gap;
    $t has allocation-target "system";
  };

# --- Specification Aging (CC-5) ---
# Staleness increases as days since assessed-at grow
# This rule triggers refresh warnings when staleness exceeds threshold

rule staleness-score-calculation:
  when {
    $a isa prism-artefact;
    $a has assessed-at $assessed;
    $a has refresh-cadence-days $cadence;
    $now = now();
    $age-days = days-between($assessed, $now);
    $staleness = $age-days / $cadence;
  } then {
    $a has specification-age-days $age-days;
    $a has staleness-score $staleness;
  };

# --- Authority Boundary = Inverse of Failure Mode ---
# For agent-actors, the authority boundary constraint MUST be
# the inverse of the characteristic failure mode
# This is a validation rule, not a computation rule
# (Enforced at application layer, not TypeDB rule layer,
#  but documented here for completeness)
#
# EXTRACTOR  failure: hallucination   → boundary: "never judge"
# MEASURER   failure: noise-as-signal → boundary: "never interpret"  
# ASSESSOR   failure: overconfidence → boundary: "never finalise"
# GENERATOR  failure: fabrication     → boundary: "never be vague"
# AGGREGATOR failure: omission        → boundary: "never add"


# ═══════════════════════════════════════════════════════════════════
# SECTION 6: SEED DATA — TEMPLATE SCHEMAS
# These schema-registry entries define the content-json format
# for key artefact types. Loaded separately as seed-templates.tql
# ═════════════════════════════════════════════════════════════════

# Note: Actual schema content loaded via seed-templates.tql
# Each schema-registry entry contains a JSON Schema definition
# that validates the content-json of artefacts referencing it.
#
# Example schema-registry entries to seed:
#
# 1. agent-job-description-schema  — validates agent job descriptions
# 2. handoff-contract-schema       — validates pipeline handoff contracts  
# 3. target-characteristic-schema  — validates Phase 0 target characteristics
# 4. task-decomposition-schema     — validates Phase 1 task decomposition
# 5. complementarity-matrix-schema — validates Phase 2 allocation decisions
# 6. fmea-schema                   — validates FMEA entries
# 7. test-case-schema              — validates Phase 6 test cases
# 8. progressive-autonomy-schema   — validates progressive autonomy schedules
# 9. cognitive-load-budget-schema   — validates Phase 5 load budgets
# 10. interface-spec-schema         — validates human interface specifications
```

---

## Seed Template Schema Definitions (`seed-templates.tql`)

```tql
# ═══════════════════════════════════════════════════════════════════
# SEED: Schema Registry Entries for CAWDP Design Studio
# These JSON Schema definitions validate content-json on artefacts
# ═══════════════════════════════════════════════════════════════════

define

# --- 1. Agent Job Description Schema ---
insert
  $schema-1 isa schema-registry,
    has schema-id "agent-job-description-v1",
    has schema-version "1.0.0",
    has name "Agent Job Description",
    has description "Validates complete agent job descriptions per CAWDP Phase 4",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "AgentJobDescription",
      "type": "object",
      "required": ["identity", "mission", "input_schema", "output_schema", "hard_constraints", "authority_boundary", "failure_mode", "escalation_protocol"],
      "properties": {
        "identity": {
          "type": "object",
          "required": ["name", "class", "role", "orientation"],
          "properties": {
            "name": {"type": "string"},
            "class": {"enum": ["extractor", "measurer", "assessor", "generator", "aggregator"]},
            "role": {"type": "string"},
            "orientation": {"enum": ["critical", "optimistic", "creative", "factual", "procedural", "synthesiser"]},
            "scope": {"type": "string"}
          }
        },
        "mission": {"type": "string"},
        "input_schema": {"type": "object"},
        "output_schema": {"type": "object"},
        "context": {
          "type": "object",
          "properties": {
            "minimum_sufficient": {"type": "array", "items": {"type": "string"}},
            "forbidden_reads": {"type": "array", "items": {"type": "string"}},
            "epistemic_context": {"type": "string"}
          }
        },
        "hard_constraints": {
          "type": "array",
          "items": {"type": "string"}
        },
        "authority_boundary": {
          "type": "object",
          "required": ["constraint", "prohibited", "inverse_of_failure"],
          "properties": {
            "constraint": {"type": "string"},
            "prohibited": {"type": "string"},
            "inverse_of_failure": {"type": "boolean"}
          }
        },
        "failure_mode": {
          "type": "object",
          "required": ["mode", "mitigation"],
          "properties": {
            "mode": {"type": "string"},
            "mitigation": {"type": "string"}
          }
        },
        "quality_criteria": {"type": "array", "items": {"type": "string"}},
        "error_handling": {
          "type": "object",
          "properties": {
            "on_uncertainty": {"enum": ["stop_and_signal", "escalate", "provisional_answer"]},
            "on_tool_failure": {"type": "string"},
            "on_context_loss": {"type": "string"}
          }
        },
        "escalation_protocol": {
          "type": "object",
          "required": ["escalation_target", "escalation_conditions"],
          "properties": {
            "escalation_target": {"type": "string"},
            "escalation_conditions": {"type": "array", "items": {"type": "string"}}
          }
        },
        "progressive_autonomy": {
          "type": "object",
          "properties": {
            "current_level": {"enum": ["shadow", "advisory", "supervised", "autonomous"]},
            "graduation_criteria": {"type": "string"},
            "fallback_behavior": {"type": "string"}
          }
        },
        "cost_budget": {"type": "number"},
        "specification_aging": {
          "type": "object",
          "properties": {
            "refresh_cadence_days": {"type": "integer"},
            "staleness_triggers": {"type": "array", "items": {"type": "string"}}
          }
        }
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 2. Handoff Contract Schema ---
insert
  $schema-2 isa schema-registry,
    has schema-id "handoff-contract-v1",
    has schema-version "1.0.0",
    has name "Handoff Contract",
    has description "Validates typed contracts between pipeline stages (Phase 3)",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "HandoffContract",
      "type": "object",
      "required": ["source_stage", "target_stage", "output_schema", "input_schema", "contract_type"],
      "properties": {
        "source_stage": {"type": "string"},
        "target_stage": {"type": "string"},
        "contract_type": {"enum": ["artefact_transfer", "epistemic_exchange", "judgment_preparation"]},
        "output_schema": {"type": "object"},
        "input_schema": {"type": "object"},
        "epistemic_metadata_included": {"type": "boolean"},
        "verification_required": {"type": "boolean"},
        "human_gate": {"type": "boolean"},
        "data_contract": {"type": "object"}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 3. Target Characteristic Schema ---
insert
  $schema-3 isa schema-registry,
    has schema-id "target-characteristic-v1",
    has schema-version "1.0.0",
    has name "Target State Characteristic",
    has description "Validates Phase 0 target state vision characteristics",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "TargetCharacteristic",
      "type": "object",
      "required": ["characteristic", "description", "rationale"],
      "properties": {
        "characteristic": {"type": "string"},
        "description": {"type": "string"},
        "rationale": {"type": "string"},
        "measurement_approach": {"type": "string"},
        "priority": {"enum": ["non-negotiable", "high", "medium", "low"]},
        "examples": {"type": "array", "items": {"type": "string"}}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 4. Task Decomposition Schema ---
insert
  $schema-4 isa schema-registry,
    has schema-id "task-decomposition-v1",
    has schema-version "1.0.0",
    has name "Task Decomposition",
    has description "Validates Phase 1 task decomposition artefacts",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "TaskDecomposition",
      "type": "object",
      "required": ["task_name", "task_description", "cognitive_operation_type", "is_leaf"],
      "properties": {
        "task_name": {"type": "string"},
        "task_description": {"type": "string"},
        "cognitive_operation_type": {"enum": ["mechanical", "analytical", "evaluative", "generative", "intuitive"]},
        "is_leaf": {"type": "boolean"},
        "parent_task_id": {"type": ["string", "null"]},
        "subtask_ids": {"type": "array", "items": {"type": "string"}},
        "dependencies": {"type": "array", "items": {"type": "string"}},
        "domain_events": {"type": "array", "items": {"type": "string"}},
        "edge_cases": {"type": "array", "items": {"type": "string"}}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 5. Complementarity Matrix Schema ---
insert
  $schema-5 isa schema-registry,
    has schema-id "complementarity-matrix-v1",
    has schema-version "1.0.0",
    has name "Complementarity Matrix",
    has description "Validates Phase 2 H/A/S allocation decisions",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "ComplementarityMatrix",
      "type": "object",
      "required": ["task_id", "scores", "allocation", "reversibility_class"],
      "properties": {
        "task_id": {"type": "string"},
        "scores": {
          "type": "object",
          "required": ["human", "agent", "system"],
          "properties": {
            "human": {"type": "integer", "minimum": 0, "maximum": 10},
            "agent": {"type": "integer", "minimum": 0, "maximum": 10},
            "system": {"type": "integer", "minimum": 0, "maximum": 10}
          }
        },
        "gap": {"type": "integer", "minimum": 0, "maximum": 10},
        "allocation": {"enum": ["human", "agent", "system", "collaborative"]},
        "reversibility_class": {"enum": ["read-only", "reversible", "irreversible"]},
        "allocation_rationale": {"type": "string"},
        "human_only_forced": {"type": "boolean"}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 6. FMEA Schema ---
insert
  $schema-6 isa schema-registry,
    has schema-id "fmea-v1",
    has schema-version "1.0.0",
    has name "FMEA Entry",
    has description "Validates failure mode and effects analysis entries (Phase 3)",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "FMEAEntry",
      "type": "object",
      "required": ["failure_mode", "severity", "occurrence", "detection", "rpn"],
      "properties": {
        "failure_mode": {"type": "string"},
        "effect": {"type": "string"},
        "severity": {"type": "integer", "minimum": 1, "maximum": 10},
        "cause": {"type": "string"},
        "occurrence": {"type": "integer", "minimum": 1, "maximum": 10},
        "current_controls": {"type": "string"},
        "detection": {"type": "integer", "minimum": 1, "maximum": 10},
        "rpn": {"type": "integer", "minimum": 1, "maximum": 1000},
        "recommended_action": {"type": "string"},
        "responsible": {"type": "string"}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 7. Test Case Schema ---
insert
  $schema-7 isa schema-registry,
    has schema-id "test-case-v1",
    has schema-version "1.0.0",
    has name "Test Case",
    has description "Validates Phase 6 test cases derived from design decisions",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "TestCase",
      "type": "object",
      "required": ["test_id", "hypothesis", "target_dimension", "measurement"],
      "properties": {
        "test_id": {"type": "string"},
        "hypothesis": {"type": "string"},
        "target_dimension": {"enum": ["fidelity", "enrichment", "complementarity", "type_collision", "trust", "cost", "specification_aging"]},
        "measurement": {"type": "string"},
        "pass_criteria": {"type": "string"},
        "artefact_ids_tested": {"type": "array", "items": {"type": "string"}},
        "result": {"enum": ["pass", "fail", "pending", "inconclusive"]},
        "evidence": {"type": "string"}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 8. Progressive Autonomy Schedule Schema ---
insert
  $schema-8 isa schema-registry,
    has schema-id "progressive-autonomy-v1",
    has schema-version "1.0.0",
    has name "Progressive Autonomy Schedule",
    has description "Validates Phase 6 progressive autonomy deployment schedules",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "ProgressiveAutonomySchedule",
      "type": "object",
      "required": ["agent_id", "levels"],
      "properties": {
        "agent_id": {"type": "string"},
        "levels": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["level", "graduation_criteria"],
            "properties": {
              "level": {"enum": ["shadow", "advisory", "supervised", "autonomous"]},
              "graduation_criteria": {"type": "string"},
              "expected_duration_days": {"type": "integer"},
              "human_override_rate_target": {"type": "number"},
              "trust_score_threshold": {"type": "number"}
            }
          }
        }
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 9. Cognitive Load Budget Schema ---
insert
  $schema-9 isa schema-registry,
    has schema-id "cognitive-load-budget-v1",
    has schema-version "1.0.0",
    has name "Cognitive Load Budget",
    has description "Validates Phase 5 human cognitive load budgets",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "CognitiveLoadBudget",
      "type": "object",
      "required": ["budget_capacity", "decision_points"],
      "properties": {
        "budget_capacity": {"type": "integer"},
        "decision_points": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["task_id", "load_cost", "reversibility"],
            "properties": {
              "task_id": {"type": "string"},
              "description": {"type": "string"},
              "load_cost": {"type": "integer"},
              "reversibility": {"enum": ["read-only", "reversible", "irreversible"]},
              "agent_preparation": {"type": "string"},
              "human_decision": {"type": "string"}
            }
          }
        },
        "total_consumed": {"type": "integer"},
        "budget_remaining": {"type": "integer"},
        "sei_score": {"type": "integer", "minimum": 1, "maximum": 5}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;

# --- 10. Interface Spec Schema ---
insert
  $schema-10 isa schema-registry,
    has schema-id "interface-spec-v1",
    has schema-version "1.0.0",
    has name "Human Interface Specification",
    has description "Validates Phase 5 human-facing interface specifications",
    has content-json '''
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "InterfaceSpec",
      "type": "object",
      "required": ["interface_type", "decision_points", "override_mechanism"],
      "properties": {
        "interface_type": {"enum": ["dashboard", "checklist", "approval_gate", "nudge", "alert", "report"]},
        "decision_points": {"type": "array", "items": {"type": "string"}},
        "override_mechanism": {"type": "string"},
        "feedback_channel": {"type": "string"},
        "scaffolding_level": {"enum": ["high", "medium", "low", "minimal"]},
        "cognitive_mode": {"enum": ["narrative", "boundary", "exploration", "verification", "architecture", "configuration", "evaluation"]}
      }
    }
    ''',
    has validation-status "valid",
    has timestamp $now;
```

---

## Schema Statistics

| Section | Count | Purpose |
|---|---|---|
| **Attribute types** | 52 | All typed, no `any` blobs |
| **Entity types** | 28 | 7 dimensions + infrastructure |
| **Relation types** | 13 | Typed connections with cross-cutting layers |
| **Computation rules** | 4 | Complementarity gap + staleness scoring |
| **Schema Registry entries** | 10 | JSON Schema validators replacing `properties:any` |

## What This Schema Enables

1. **Every artefact carries epistemic metadata** — confidence, provenance, assumptions, limitations, assessedAt, uncertainty. CC-3 is not a policy; it's a type constraint.

2. **Authority boundaries are in the data** — every actor has `authority-boundary`, `prohibited-action`, `failure-mode`. The schema itself enforces the "boundary = inverse of failure mode" principle.

3. **Schema Registry replaces properties:any** — every `content-json` is validated by a JSON Schema in the schema-registry. The EAV anti-pattern from the ONE critique is structurally impossible.

4. **Specification aging is computed** — staleness rules auto-calculate from assessedAt and refresh-cadence-days. CC-5 is alive in the data.

5. **Complementarity gap is computed** — the gap between H/A/S scores is calculated by TypeDB rules, and allocation target is inferred. The 6+ point threshold is queryable.

6. **Design-to-Implementation traceability** — every relation has `reasoning-id` linking back to the Intentions dimension. Every generated code artifact traces to its design artefact via `generated-by` relations.

7. **Quality gates are queryable** — `quality-gate-status` on every artefact enables the Gate Engine to query the graph for pass/fail/waive status.

---

Peter, this is a complete, loadable TypeDB schema. The next step would be writing the `docker-compose.yml` to spin up TypeDB + Chroma + Postgres, and then the Python client code to connect to TypeDB and start inserting artefacts.

Want me to proceed with the docker-compose and the Python TypeDB client setup?The schema is captured. This is a significant milestone — PRISM is now an executable data model, not just a design concept. The `prism-artefact` abstract base type is the key architectural decision: it makes the 4 cross-cutting layers structurally non-optional at the data layer, which is exactly what CAWDP demands. Every artefact that enters this graph automatically carries epistemic metadata, governance constraints, temporal tracking, and schema validation — not because a developer remembered to add them, but because the type system requires it.

Ready for docker-compose and Python client whenever you are.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-18T15:01:57* · `glm-5.1:cloud` · `72ce77b4...`

### Prompt

this is too much at once.
let's start with Phase 0
what data will need to be stored to accurately capture the primary information about the task and it's ideal outcomes?

### Response

You're right. Let me strip it back to just Phase 0.

## Phase 0: What Data Needs To Be Stored

Phase 0 answers two questions:
1. **What are we doing?** (the task)
2. **What does perfect look like?** (the ideal outcome)

Here's the minimal set:

---

### The Task

```
name:              "Assignment marking — 50 submissions"
description:       "Mark a cohort of 50 student submissions 
                    against a rubric, producing feedback and grades"
context:           "University course, RMIT Blockchain Economics, 
                    Assessment 1 briefing deck"
scope_in:          "Marking, feedback drafting, cohort analysis"
scope_out:         "Grade appeals, course design, student contact"
human_role:        "Lecturer — final judgment, ethical decisions, 
                    relationship management"
```

### The Target State (12 characteristics)

This is the heart of Phase 0 — describing the ideal outcome across 12 dimensions:

```
characteristics: [
  {
    name:           "Typed not flat",
    description:    "Every piece of output is a typed, structured object — 
                     not undifferentiated prose",
    rationale:      "Typed outputs enable downstream processing, 
                     verification, and aggregation",
    priority:       "non-negotiable",
    measurable_as:  "Every output has a schema; 0% unstructured prose 
                     in final deliverables"
  },
  {
    name:           "Epistemically transparent",
    description:    "Every output carries confidence, provenance, 
                     and assumptions",
    rationale:      "The lecturer needs to know what to trust",
    priority:       "high",
    measurable_as:   "100% of agent outputs include confidence score 
                     and provenance tag"
  },
  // ... 10 more characteristics
]
```

### The Commander's Intent

```
goal:              "Enable the lecturer to make better judgments faster, 
                    not to replace their judgment"
success_in_human_terms: "Lecturer feels confident in every grade, 
                         has time for thoughtful feedback, 
                         and catches every anomaly"
without_this:      "Hours of undifferentiated prose, inconsistency across 
                    submissions, no anomaly detection"
potential_harm:    "Students receive inaccurate grades, lecturer trusts 
                    agent output without verification, feedback is generic"
```

### The Boundaries

```
constraints: [
  "Grades must be reviewed by lecturer before release",
  "No student data leaves the system",
  "Budget capped at $X per submission"
]

mandates: [
  "Every piece of agent output must carry epistemic metadata",
  "The agent never finalises a grade — only recommends"
]

guardrails: [
  "If confidence < 0.5, flag for human review",
  "If anomaly detected, escalate immediately"
]

assumptions: [
  "Submissions are in PDF format",
  "Rubric is provided and stable",
  "Lecturer has domain expertise but limited time"
]
```

---

That's it. **Four structures** for Phase 0:

| Structure | Purpose | PRISM Dimension |
|---|---|---|
| **Task** | What we're doing, for whom, in scope | Entities + Scopes |
| **Target State** (12 characteristics) | What perfect looks like | Intentions + Entities |
| **Commander's Intent** | Why we're doing it, what harm looks like | Intentions |
| **Boundaries** | Constraints, mandates, guardrails, assumptions | Intentions |

The key insight: **Phase 0 is mostly Intentions** — goals, constraints, mandates, guardrails, and assumptions. The task definition is an Entity. The scope boundaries are Scopes. But the bulk of Phase 0 is answering "what do we want, what must we avoid, what are we assuming?"

Want me to write the minimal TypeDB entity types for just these four structures?

---
