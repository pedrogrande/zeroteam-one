# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `a8486e9c...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-23T03:53:18 |
| **Runs** | 3 completed / 3 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-23T03:53:18* · `glm-5.1:cloud` · `19800be7...`

### Prompt

Review this plan and advise on any issues or improvement opportunities:

***
# CAWDP Orchestrator — Implementation Plan

**Purpose:** Build an Agno workflow/team that produces all 152 CAWDP artefacts through coordinated subworkflows, implementing the Pattern Library compression strategy.

**Key Insight:** The 152 outputs are not 152 answers — they are 143 small-to-medium workflows and 10 larger workflows. The fractal nature requires orchestration at multiple levels.

---

## Architecture Decision: Team + Master Workflow

**Recommendation:** Use **Agno Team** with **WorkflowFactory** for dynamic subworkflow generation.

**Rationale:**
- **Team** handles the 11 phases as specialist agents with shared decision register
- **WorkflowFactory** generates depth-adaptive subworkflows (Shallow/Medium/Deep)
- **Master Workflow** orchestrates phase progression with HITL gates between phases
- **Pattern Library** compression implemented through context providers and session_state

### Why Not Pure Workflow?

A single workflow with 152 steps would be:
- Unmanageable (too complex to reason about)
- Inflexible (can't adapt depth per output dynamically)
- Inefficient (can't parallelize independent outputs within a phase)

### Why Not Pure Team?

A team without orchestration would:
- Miss phase dependencies (P1 needs P0, P2 needs P1)
- Lack HITL gates at natural checkpoints (end of phase)
- Have no mechanism for pattern compression (team members don't share learned patterns automatically)

---

## High-Level Architecture

```
CAWDP Orchestrator Team
├── Phase Specialist Agents (11 agents, one per phase)
│   ├── P0 Agent (Purpose & Vision)
│   ├── P1 Agent (Output Specification)
│   ├── P2 Agent (Backcasting)
│   ├── P3 Agent (Task Decomposition)
│   ├── P4 Agent (Capability Allocation)
│   ├── P5 Agent (Event Storming)
│   ├── P6 Agent (System Architecture)
│   ├── P7 Agent (Agent Design)
│   ├── P8 Agent (Contract Formalization)
│   ├── P9 Agent (Human Experience)
│   └── P10 Agent (Validation & Iteration)
├── Subworkflow Factories (3 factories, one per depth)
│   ├── ShallowWorkflowFactory → extraction/computation workflows
│   ├── MediumWorkflowFactory → writer→reviewer with pattern pre-fill
│   └── DeepWorkflowFactory → Compiler→Analyst→Deriver architecture
├── Master Orchestration Workflow
│   ├── For each phase (P0→P10):
│   │   ├── Load outputs for phase from catalogue
│   │   ├── Router: route to depth-appropriate factory
│   │   ├── Run subworkflows (parallel where possible)
│   │   ├── HITL gate: review phase completion
│   │   └── Persist outputs + decisions to session_state
│   └── Final step: Generate complete CAWDP specification document
└── Shared State
    ├── decision_register (grows as phases complete)
    ├── pattern_library (learns from human decisions)
    ├── output_store (accumulated outputs by ID)
    └── phase_progress (tracking completion state)
```

---

## Three-Tier Workflow Architecture

### Tier 1: Shallow Workflows (Extraction/Computation)

**Pattern:** Single-step executor → automated review → no HITL

**Example:** P0-06 Pattern Match Result, P0-08 Orientation Declaration, P1-03 Principal Declaration

```python
def create_shallow_workflow(output_id: str, output_spec: dict) -> Workflow:
    """Generate a shallow workflow for extraction/computation outputs."""
    
    def extractor_executor(step_input: StepInput, run_context: RunContext) -> StepOutput:
        # Load dependencies from session_state
        dependencies = _load_dependencies(output_spec["dependencies"], run_context)
        
        # Apply extraction/computation logic
        result = _extract_or_compute(
            output_id=output_id,
            method=output_spec["production_method"],
            dependencies=dependencies,
        )
        
        # Store in session_state
        run_context.session_state["outputs"][output_id] = result
        
        return StepOutput(content=result)
    
    return Workflow(
        name=f"shallow-{output_id}",
        steps=[
            Step(name="Extract/Compute", executor=extractor_executor),
            Step(name="Validate", executor=_validate_against_quality_criteria),
        ],
        session_state={},
        db=get_pipeline_db(table_name=f"shallow_{output_id}"),
    )
```

**No HITL needed** — validation is programmatic (schema check, range check, dependency satisfaction).

---

### Tier 2: Medium Workflows (Writer→Reviewer with Pattern Pre-fill)

**Pattern:** Pattern pre-fill → writer agent → reviewer agent → conditional HITL

**Example:** P0-01 Five Identity Questions, P1-06 Authority Guard Schema, P7-02 Boundaries Section

```python
def create_medium_workflow(output_id: str, output_spec: dict) -> Workflow:
    """Generate a medium workflow with pattern pre-fill and conditional HITL."""
    
    # 1. Pattern pre-fill executor (40-70% filled from library)
    def pattern_prefill_executor(step_input: StepInput, run_context: RunContext) -> StepOutput:
        # Load pattern from library based on agent class/context
        pattern = pattern_library.get_pattern_for(
            output_id=output_id,
            agent_class=run_context.session_state.get("agent_class"),
            context=run_context.session_state.get("p0_answers"),
        )
        
        # Pre-fill with pattern defaults
        prefilled = pattern.fill_defaults()
        
        # Mark fields that need human judgment (not in pattern)
        gaps = pattern.identify_gaps()
        
        return StepOutput(content={
            "prefilled": prefilled,
            "gaps": gaps,
            "pattern_coverage": f"{pattern.coverage_pct}%",
        })
    
    # 2. Writer agent fills gaps
    writer = Agent(
        id=f"writer-{output_id}",
        model=default_model(),
        instructions=f"""
        You are producing: {output_spec['name']}
        
        **Pattern Pre-fill** (already completed):
        {{{{prefilled}}}}
        
        **Your Task** (fill the gaps):
        {{{{gaps}}}}
        
        **Quality Criteria:**
        {chr(10).join(f"- {c}" for c in output_spec['quality_criteria'])}
        
        Use the record_decision tool for any judgment calls.
        """,
        tools=[DecisionToolkit()],
        db=get_pipeline_db(table_name=f"writer_{output_id}"),
    )
    
    # 3. Reviewer agent checks fidelity/enrichment/cross-cutting
    reviewer = Agent(
        id=f"reviewer-{output_id}",
        model=Ollama(id="glm-5.1:cloud", host="https://ollama.com"),
        instructions=MEDIUM_REVIEWER_INSTRUCTIONS,
        db=get_pipeline_db(table_name=f"reviewer_{output_id}"),
    )
    
    return Workflow(
        name=f"medium-{output_id}",
        steps=[
            Step(name="Pattern Pre-fill", executor=pattern_prefill_executor),
            Loop(
                name="Write→Review Loop",
                steps=[
                    Step(name="Fill Gaps", agent=writer),
                    Step(name="Review", agent=reviewer),
                ],
                end_condition=_review_passes,
                requires_iteration_review=True,  # HITL only if review fails
                on_reject=OnReject.retry,
                forward_iteration_output=True,
                max_iterations=3,
            ),
            Step(name="Persist", executor=_persist_output_and_decisions),
        ],
        session_state={
            "decisions": [],
            "outputs": {},
        },
        db=get_pipeline_db(table_name=f"medium_{output_id}"),
    )
```

**Pattern compression reduces 309-618 Medium tasks to ~100-250 human decisions** (60-70% pre-filled).

---

### Tier 3: Deep Workflows (Compiler→Analyst→Deriver Architecture)

**Pattern:** Multi-wave synthesis with 3 specialist agents

**Example:** P10-01 Methodology Reflection, P10-06 Cost & Resource Baseline, P1-28 Agent Operations Manual

```python
def create_deep_workflow(output_id: str, output_spec: dict) -> Workflow:
    """Generate a deep workflow with Compiler→Analyst→Deriver architecture."""
    
    # 1. Compiler: Aggregate data from all dependencies
    compiler = Agent(
        id=f"compiler-{output_id}",
        model=default_model(),
        instructions=f"""
        You are the Compiler for: {output_spec['name']}
        
        **Your Task:**
        1. Load all dependencies: {output_spec['dependencies']}
        2. Organize data by dimension/category
        3. Identify patterns, clusters, and outliers
        4. Produce structured summary (not analysis yet)
        
        Output a structured JSON with organized data ready for analysis.
        """,
        output_schema=CompilerOutput,  # Pydantic model
        db=get_pipeline_db(table_name=f"compiler_{output_id}"),
    )
    
    # 2. Analyst: Find patterns, connections, implications
    analyst = Agent(
        id=f"analyst-{output_id}",
        model=default_model(),
        instructions=f"""
        You are the Analyst for: {output_spec['name']}
        
        **Compiler Summary:**
        {{{{previous_step_content}}}}
        
        **Your Task:**
        1. Identify patterns across dimensions
        2. Find connections between elements
        3. Assess criticality and risk
        4. Flag gaps and inconsistencies
        
        Output analysis with specific findings (not recommendations yet).
        """,
        output_schema=AnalystOutput,
        db=get_pipeline_db(table_name=f"analyst_{output_id}"),
    )
    
    # 3. Deriver: Synthesize implications and recommendations
    deriver = Agent(
        id=f"deriver-{output_id}",
        model=default_model(),
        instructions=f"""
        You are the Deriver for: {output_spec['name']}
        
        **Analyst Findings:**
        {{{{previous_step_content}}}}
        
        **Your Task:**
        1. Derive implications from patterns
        2. Generate recommendations
        3. Assess confidence per recommendation
        4. Identify evolution triggers
        
        Output {output_spec['name']} with all required sections.
        """,
        output_schema=DeriverOutput,
        db=get_pipeline_db(table_name=f"deriver_{output_id}"),
    )
    
    # 4. Reviewer: Quality gate for Deep outputs
    reviewer = Agent(
        id=f"deep-reviewer-{output_id}",
        model=Ollama(id="glm-5.1:cloud", host="https://ollama.com"),
        instructions=DEEP_REVIEWER_INSTRUCTIONS,
        db=get_pipeline_db(table_name=f"deep_reviewer_{output_id}"),
    )
    
    return Workflow(
        name=f"deep-{output_id}",
        steps=[
            Loop(
                name="Compiler→Analyst→Deriver Loop",
                steps=[
                    Step(name="Compile", agent=compiler),
                    Step(name="Analyze", agent=analyst),
                    Step(name="Derive", agent=deriver),
                    Step(name="Review", agent=reviewer),
                ],
                end_condition=_review_passes,
                requires_iteration_review=True,  # HITL for Deep outputs
                on_reject=OnReject.retry,
                forward_iteration_output=True,
                max_iterations=5,
            ),
            Step(name="Persist", executor=_persist_output_and_decisions),
        ],
        session_state={
            "decisions": [],
            "outputs": {},
        },
        db=get_pipeline_db(table_name=f"deep_{output_id}"),
    )
```

**Deep workflows require full HITL review** — 10 outputs, human reviews each.

---

## Master Orchestration Workflow

The master workflow orchestrates all 11 phases sequentially, with HITL gates between phases.

```python
from agno.workflow import Router

def create_cawdp_orchestrator() -> Workflow:
    """Master workflow that orchestrates all 152 outputs across 11 phases."""
    
    # Load catalogue
    catalogue = load_catalogue()  # 152 outputs
    
    # Group by phase
    phases = group_by_phase(catalogue)  # P0: [9 outputs], P1: [31 outputs], ...
    
    # Create phase steps
    phase_steps = []
    
    for phase_num, outputs in phases.items():
        # Create a step for each phase
        def phase_executor(step_input: StepInput, run_context: RunContext) -> StepOutput:
            phase_outputs = phases[phase_num]
            results = []
            
            # For each output in phase, route to appropriate depth workflow
            for output_spec in phase_outputs:
                # Router: choose factory based on depth
                if output_spec["depth"] == "shallow":
                    workflow = ShallowWorkflowFactory.create(output_spec)
                elif output_spec["depth"] == "medium":
                    workflow = MediumWorkflowFactory.create(output_spec)
                else:  # deep
                    workflow = DeepWorkflowFactory.create(output_spec)
                
                # Run subworkflow
                result = workflow.run(
                    message=f"Produce {output_spec['name']}",
                    session_state=run_context.session_state,  # Share state
                )
                
                results.append({
                    "output_id": output_spec["id"],
                    "status": "complete" if result.success else "failed",
                    "content": result.content,
                })
            
            return StepOutput(content={
                "phase": phase_num,
                "outputs": results,
                "decisions": run_context.session_state["decisions"],
            })
        
        phase_steps.append(
            Step(
                name=f"Phase {phase_num}",
                executor=phase_executor,
                description=f"Produce {len(outputs)} outputs for Phase {phase_num}",
            )
        )
    
    # Master workflow
    return Workflow(
        name="cawdp-orchestrator",
        description="Produce complete CAWDP specification (152 outputs across 11 phases)",
        steps=[
            Step(name="Initialize", executor=_initialize_session_state),
            *phase_steps,  # P0→P10 sequential
            Step(name="Generate Final Spec", executor=_generate_complete_spec_document),
            Step(name="Persist Decisions", executor=_persist_all_decisions),
        ],
        session_state={
            "decisions": [],
            "outputs": {},
            "pattern_library": PatternLibrary.load(),
            "agent_class": None,  # Set by user at start
            "p0_answers": {},  # Populated in P0, used by later phases
        },
        db=get_pipeline_db(table_name="cawdp_orchestrator"),
    )
```

---

## Phase Dependencies & Parallelization

Some outputs within a phase can run in parallel, others have dependencies.

### Within-Phase Parallelization Strategy

| Phase | Parallelizable Outputs | Sequential Outputs | Rationale |
|-------|------------------------|-------------------|-----------|
| P0 | A/S/H/E dimensions (4 groups) | Q1-Q5 (sequential) | Dimensions are independent; questions build on each other |
| P1 | Most outputs (28) | O1→O2→O3 (identity cascade), O30→O31 (graph requires outputs) | Identity cascade must be sequential |
| P2 | Analysis per P1 output (parallel) | P2-06 Gap Analysis (needs all others) | Each P1 output traced independently |
| P3 | Task decomposition per P1 output | P3-07 Groupings (needs all tasks) | Tasks per output are independent |
| P4 | Scoring per task (parallel) | P4-08 Confidence × Reversibility (needs P4-03 + P4-04) | Each task scored independently |
| P5 | Event identification per task | P5-07 Missing Event Analysis (needs catalog) | Events per task are independent |
| P6 | Pipeline design (sequential) | All P6 outputs depend on P5 | Architecture decisions cascade |
| P7 | Specs per agent (parallel) | None (agents are independent once roster is set) | Each agent spec is independent |
| P8 | Primitives per agent (parallel) | P8-11 10×10 Matrix (needs all primitives) | Primitives per agent are independent |
| P9 | Surface design (parallel) | P9-10 Human-to-Human (needs all surfaces) | Each surface is independent |
| P10 | Deep outputs (7 parallel) | All P10 outputs depend on P0-P9 completion | P10 is synthesis across all phases |

**Implementation:** Use `Parallel` step for parallelizable outputs within a phase:

```python
# Example: P1 parallel outputs
parallel_p1_outputs = Parallel(
    name="P1 Parallel Outputs",
    steps=[
        Step(name="O4 Scope Boundary", executor=...),
        Step(name="O5 Task Contract", executor=...),
        Step(name="O6 Authority Guard", executor=...),
        # ... 25 more independent outputs
    ],
)
```

**Estimated speedup:** 30-40% reduction in wall-clock time for phases with high parallelization (P1, P7, P8).

---

## Pattern Library Implementation

The Pattern Library is the compression mechanism. It must:
1. **Store** patterns indexed by agent class + context
2. **Fill** output templates with pattern defaults
3. **Learn** from human decisions (update patterns when human overrides)
4. **Propagate** decisions across dependent outputs

### Pattern Library Schema

```python
from pydantic import BaseModel
from typing import Dict, List, Optional

class Pattern(BaseModel):
    """A reusable pattern for a specific output type."""
    output_id: str
    agent_class: str  # Extractor, Assessor, Generator, etc.
    context_keys: List[str]  # ["p0_q1_answer", "harm_assessment"]
    defaults: Dict[str, Any]  # Pre-filled values
    coverage_pct: int  # How much of output this pattern fills (40-70%)
    confidence: float  # 0.0-1.0, based on how many times pattern was used
    
class PatternLibrary(BaseModel):
    patterns: Dict[str, Pattern]  # Indexed by output_id + agent_class
    
    def get_pattern_for(self, output_id: str, agent_class: str, context: dict) -> Optional[Pattern]:
        """Retrieve pattern matching output + class + context."""
        key = f"{output_id}:{agent_class}"
        pattern = self.patterns.get(key)
        
        if pattern and self._context_matches(pattern.context_keys, context):
            return pattern
        
        return None  # No pattern, agent must fill from scratch
    
    def learn_from_decision(self, output_id: str, agent_class: str, field: str, value: Any):
        """Update pattern based on human decision."""
        key = f"{output_id}:{agent_class}"
        
        if key not in self.patterns:
            self.patterns[key] = Pattern(
                output_id=output_id,
                agent_class=agent_class,
                context_keys=[],
                defaults={},
                coverage_pct=0,
                confidence=0.0,
            )
        
        # Update pattern defaults
        self.patterns[key].defaults[field] = value
        self.patterns[key].coverage_pct = self._calculate_coverage(key)
        self.patterns[key].confidence = min(1.0, self.patterns[key].confidence + 0.1)
    
    def propagate_decision(self, decision: Decision) -> List[str]:
        """Propagate a decision to all dependent outputs."""
        affected_output_ids = []
        
        # Find all outputs that depend on the decision's output_refs
        for output_ref in decision.output_refs:
            dependents = self._find_dependents(output_ref)
            affected_output_ids.extend(dependents)
        
        # Update patterns for all dependents
        for output_id in affected_output_ids:
            self._apply_decision_to_pattern(output_id, decision)
        
        return affected_output_ids
```

### Pattern Pre-fill Example

For P7-02 Boundaries Section:

```python
# Pattern for Assessor class agents
assessor_boundaries_pattern = Pattern(
    output_id="P07-002",
    agent_class="Assessor",
    context_keys=["p0_q3_answer"],
    defaults={
        "never_rules": [
            "Never narrow possibility without explicit human consent",
            "Never produce output without epistemic metadata",
            "Never proceed when confidence < threshold",
        ],
        "enforcement_regime": {
            "narrow_without_consent": "Regime 3 (Structural)",
            "missing_metadata": "Regime 2 (Detection + human review)",
            "low_confidence": "Regime 2 (Detection + escalation)",
        },
    },
    coverage_pct=60,  # 60% pre-filled from pattern
    confidence=0.9,  # High confidence (used 9 times)
)
```

When producing P7-02 for a new Assessor agent, the writer sees:

```
**Pattern Pre-fill (60% complete):**
- Never narrow possibility without explicit human consent → Regime 3
- Never produce output without epistemic metadata → Regime 2
- Never proceed when confidence < threshold → Regime 2

**Your Task (fill the gaps):**
- Add agent-specific never-rules from Q3 answer
- Confirm enforcement regimes are appropriate for this agent
- Add hardest boundary moment stress test from Q5
```

Human fills 40%, not 100%. **Compression achieved.**

---

## Implementation Phases

### Phase 1: Foundation (Week 1)

**Deliverables:**
- [ ] `cawdp_pipeline/factories/shallow_factory.py` — ShallowWorkflowFactory
- [ ] `cawdp_pipeline/factories/medium_factory.py` — MediumWorkflowFactory
- [ ] `cawdp_pipeline/factories/deep_factory.py` — DeepWorkflowFactory
- [ ] `cawdp_pipeline/models/pattern.py` — Pattern, PatternLibrary models
- [ ] `cawdp_pipeline/tools/pattern_tools.py` — PatternLibrary CRUD operations

**Validation:**
- Run 3 test outputs (1 per depth) through factories
- Verify workflow structure matches spec
- Verify session_state sharing works

---

### Phase 2: Phase Specialists (Week 2)

**Deliverables:**
- [ ] `cawdp_pipeline/agents/p0_specialist.py` through `p10_specialist.py` (11 agents)
- [ ] Agent instructions per phase (loaded from `agents/instructions/p{N}_instructions.md`)
- [ ] Phase-specific quality gates

**Validation:**
- Run each agent independently on sample output
- Verify output schema compliance
- Verify decision recording works

---

### Phase 3: Master Orchestrator (Week 3)

**Deliverables:**
- [ ] `cawdp_pipeline/workflows/cawdp_orchestrator.py` — master workflow
- [ ] Phase parallelization logic (Parallel steps where appropriate)
- [ ] HITL gates between phases
- [ ] Final spec document generator

**Validation:**
- Run full P0 (9 outputs)
- Verify P0 outputs feed into P1 correctly
- Verify HITL gate pauses between phases

---

### Phase 4: Pattern Library Integration (Week 4)

**Deliverables:**
- [ ] Pattern pre-fill executors for Medium workflows
- [ ] Pattern learning from human decisions
- [ ] Decision propagation across dependent outputs
- [ ] Pattern library persistence (file or DB)

**Validation:**
- Run P1 twice, verify second run has higher pattern coverage
- Verify propagation updates dependent outputs automatically
- Measure compression: track human decisions vs total tasks

---

### Phase 5: Production Hardening (Week 5)

**Deliverables:**
- [ ] Error handling for all executors
- [ ] Resumability (workflow can be paused and resumed)
- [ ] Progress tracking UI (which outputs complete, which in progress)
- [ ] Cost monitoring (token usage per output)
- [ ] Quality metrics (review pass rate per phase)

**Validation:**
- Run full P0-P3 end-to-end
- Pause at P2 HITL gate, resume successfully
- Verify all outputs persisted correctly
- Verify decision register complete

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Coverage** | 152/152 outputs produced | Count outputs in `session_state["outputs"]` |
| **Compression** | 100-250 human decisions (not 483-643 tasks) | Count HITL approvals + human-filled gaps |
| **Pattern Efficiency** | 60-70% pre-fill for Medium outputs | Measure `coverage_pct` from patterns |
| **Quality** | ≥ 90% automated review pass rate | Count end_condition passes vs HITL pauses |
| **Cost** | ≤ $50 per full CAWDP spec (152 outputs) | Track token usage across all workflows |
| **Time** | ≤ 8 hours wall-clock for full spec | Measure start to P10 completion |
| **Resumability** | 100% of paused workflows resume successfully | Test pause/resume at every HITL gate |

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Pattern Library doesn't compress** | Medium | High | Start with manual pattern authoring (not learned); validate compression on P0-P1 before full implementation |
| **Deep workflows too expensive** | Medium | Medium | Use Ollama for reviewer, GPT-4o-mini for non-synthesis steps; budget $5-10 per Deep output |
| **Phase dependencies block parallelization** | Low | Medium | Catalogue already documents dependencies; validate DAG before implementation |
| **HITL fatigue (too many gates)** | High | High | Implement conditional HITL (only when review fails); batch approve outputs within phase |
| **Session state grows too large** | Medium | Low | Persist outputs after each phase; only keep current phase in session_state |
| **Router complexity** | Low | Medium | Router logic is simple (depth-based); complexity is in factories, not router |

---

## Next Steps

1. **Validate architecture decision** — Review this plan with stakeholders
2. **Prototype one tier** — Build MediumWorkflowFactory + test on P1-06 (Authority Guard Schema)
3. **Measure compression** — Run P0 twice, measure pattern learning effectiveness
4. **Build master orchestrator** — Wire P0→P1 with HITL gate
5. **Scale to all phases** — Once P0-P1 validated, replicate pattern for P2-P10

---

## Appendix: Alternative Architectures Considered

### Alternative 1: Pure Sequential Workflow (152 steps)

**Rejected because:**
- No parallelization within phases
- No dynamic depth adaptation
- Unmanageable complexity (152 steps in one workflow)

### Alternative 2: 152 Independent Workflows (No Orchestration)

**Rejected because:**
- No phase dependency management (P2 needs P1)
- No pattern learning (each workflow isolated)
- No shared decision register

### Alternative 3: Hierarchical Teams (Phase Teams → Output Teams)

**Rejected because:**
- Agno teams don't support hierarchical nesting well
- Overly complex (11 phase teams, each with N output teams)
- Pattern propagation harder to implement across teams

### Recommended: Team + Master Workflow + WorkflowFactory

**Chosen because:**
- Team handles phase specialization (11 agents)
- Master Workflow handles phase orchestration (P0→P10 sequential)
- WorkflowFactory handles depth adaptation (Shallow/Medium/Deep)
- Pattern Library integrates naturally through session_state
- Parallelization possible within phases (Parallel steps)
- HITL gates natural at phase boundaries
- Scales to 152 outputs without unmanageable complexity

***

### Response

# CAWDP Orchestrator Plan Review

Good work getting this to a concrete implementation plan. There are some genuine structural issues that need resolving before you build, plus several CAWDP requirements that are absent. I'll go layer by layer.

---

## 🔴 Architecture Issues (fix before building)

### 1. Team layer adds nothing — drop it

The plan says "Team + Master Workflow + WorkflowFactory." But reading the actual architecture, the phase specialists aren't collaborating as a team. They're being **invoked sequentially by the master workflow**. There's no shared conversation, no leader routing, no real-time collaboration between them.

What you actually have is:

```
Master Workflow (orchestrator)
  → WorkflowFactory (depth-adaptive subworkflows)
    → Agents within subworkflows (writer, reviewer, compiler, etc.)
```

This is a **pure Workflow** architecture. The Team layer adds complexity without value. Every piece of state sharing you need (decision_register, pattern_library, output_store) is already handled by the workflow's session_state or by SurrealDB persistence.

**Fix:** Remove the Team layer. Rename "Phase Specialist Agents" to "Phase Agents" and note they're invoked by the master workflow, not organized as a team.

### 2. Subworkflow session_state sharing is underspecified

The plan assumes subworkflows share session_state with the parent workflow:

```python
result = workflow.run(
    session_state=run_context.session_state,  # Share state
)
```

In Agno, subworkflows have **their own** session state backed by their own DB table. The parent doesn't automatically get the subworkflow's state changes. You need an explicit read-back:

```python
# After subworkflow runs, read its outputs back
result = workflow.run(message=f"Produce {output_spec['name']}")
# Explicitly propagate to parent state
run_context.session_state["outputs"][output_id] = result.content
run_context.session_state["decisions"].extend(
    result.session_state.get("decisions", [])
)
```

Or better: skip session_state for shared data and use **SurrealDB directly** via the CAWDP-aware writer module. The writer module already exists as a design artifact — use it. Every output and decision gets persisted to SurrealDB, and every subworkflow reads from SurrealDB. This avoids state synchronization problems entirely.

**Fix:** Use SurrealDB as the shared state store, not session_state. The writer module enforces valid writes. Subworkflows read dependencies from DB and write outputs to DB. The master workflow reads progress from DB. Session_state is for workflow control metadata (which phase, which step), not for content.

### 3. Parallel writes to shared state will race

The parallelization strategy is sound conceptually, but the implementation runs into race conditions. If 28 P1 outputs run in parallel, and they all write to `session_state["decisions"]` or even to the same SurrealDB tables concurrently, you get lost writes or inconsistent state.

**Fix:** Each parallel subworkflow writes to its **own** SurrealDB record (e.g., `design_artefacts:{workflow_id}_{output_id}`). After the parallel block completes, a merge step reads all individual records and persists any cross-output inferences (pattern propagation, decision propagation). This is exactly the Aggregator pattern — individual writes, then consolidation.

### 4. Executor vs Agent confusion in factory code

The code samples mix executor functions and agent steps in ways that won't work cleanly in Agno. A Step has either an `executor` (function) or an `agent`, not both. The Medium workflow code shows:

```python
Step(name="Pattern Pre-fill", executor=pattern_prefill_executor),  # function ✓
Step(name="Fill Gaps", agent=writer),  # agent ✓
```

This is correct at the step level, but the Loop structure wrapping them needs clean step definitions. The Shallow workflow is fine (all executors). The Deep workflow needs agent steps for Compiler/Analyst/Deriver and executor steps for persistence.

**Fix:** Be explicit about which steps are executor functions (no LLM, deterministic) and which are agent steps (LLM-powered, judgment required). Mark them clearly in the factory code.

---

## 🟡 Missing CAWDP Requirements (add before Phase 5)

### 5. artefact_tags — the cascading P10 dependency

Every output **must** include an `artefact_tags` field (set of: surprise, gap, pattern, assessment_fragment). Without this, P10 has nothing to query. This was identified as a **critical structural requirement** that flows backward from P10 to all previous phases.

**Fix:** Add to the base output schema:

```python
class CAWDPArtefact(BaseModel):
    output_id: str
    content: Any
    epistemic_metadata: EpistemicMetadata  # CC-3
    artefact_tags: set[str] = set()  # For P10 assembly
    produced_at: datetime
    produced_by: str  # agent_id or "human"
    specification_aging: AgingMetadata  # CC-5
```

### 6. Epistemic metadata on every output

CC-3 requires 6-field epistemic metadata (confidence, provenance, assumptions, limitations, recency, uncertainty) on **every** output. The plan's persist step just stores `content` and `status`. The 10-dimension Information Quality framework with traffic light model is also absent.

**Fix:** The base output schema (above) includes it. Every subworkflow's persist step must populate it. For Shallow outputs, most fields are deterministic (confidence=1.0 for computations, provenance=algorithmic). For Medium/Deep outputs, the writer/deriver agent produces it as part of their output schema.

### 7. Enforcement regime per authority boundary

P7 and P8 require every authority boundary to specify its enforcement regime (Declare/Detect/Prevent). The Pattern Library defaults mention regimes but the output schema doesn't enforce the field.

**Fix:** When the Pattern Library fills boundary defaults, it must include `enforcement_regime` and `enforcement_justification` fields. The quality gate for P7/P8 outputs must verify these are present.

### 8. Feasibility contamination check for P0-P2

CC-9 Possibility Orientation requires P0-P2 outputs to be possibility-oriented (ideals, not mechanisms). The plan has no contamination checker. The earlier design review identified a concrete keyword list as necessary: "Agno," "PostgreSQL," "JSON," "REST API," "deploy," "implement," etc.

**Fix:** Add a contamination check executor step after each P0-P2 output:

```python
CONTAMINATION_KEYWORDS = [
    "agno", "postgresql", "surrealdb", "chroma", "json", "yaml",
    "rest api", "graphql", "deploy", "implement", "docker",
    "fastapi", "cloudflare", "ollama", "pydantic", "schema",
]

def check_contamination(output_content: str, phase: int) -> ContaminationReport:
    if phase > 2:
        return ContaminationReport(clean=True)  # P3+ allows mechanisms
    found = [kw for kw in CONTAMINATION_KEYWORDS if kw.lower() in output_content.lower()]
    return ContaminationReport(clean=len(found) == 0, contamination=found)
```

### 9. Null-state output as universal hard constraint

CAWDP v2.1 requires class-specific null states for all agents. If a subworkflow produces no result, it must produce its null state (not silence): "No results found" / "Insufficient data" / "Unable to assess" / "Cannot generate" / "Nothing to assemble" — each with epistemic metadata.

**Fix:** Add null-state handling to every factory:

```python
NULL_STATES = {
    "Extractor": "No results found",
    "Measurer": "Insufficient data for measurement",
    "Assessor": "Unable to assess — insufficient basis",
    "Generator": "Cannot generate — missing required inputs",
    "Aggregator": "Nothing to assemble — no dependent outputs complete",
}
```

### 10. Specification aging metadata on outputs

CC-5 requires every output to track its own staleness. Once produced, an output needs `produced_at`, `last_reviewed_at`, `review_cadence`, and `staleness_score`.

**Fix:** Include `AgingMetadata` in the base output schema (already in #5 above). For Shallow outputs, cadence is long (6 months). For Medium, depends on agent class. For Deep, depends on harm assessment.

---

## 🟢 Implementation Concerns (fix as you build)

### 11. The phase executor runs subworkflows synchronously

The code shows:
```python
for output_spec in phase_outputs:
    result = workflow.run(...)
```

This is a synchronous loop, not parallel execution. For phases with high parallelization (P1: 28 parallel outputs), you need to actually use Agno's `Parallel` step or asyncio.

**Fix:** The phase executor should create a `Parallel` step containing all independent output subworkflows, then a sequential step for dependent outputs. Don't loop — use the workflow engine's parallelism.

### 12. Pattern Library learning is too simplistic

`confidence = min(1.0, confidence + 0.1)` per use doesn't capture:
- Domain variation (a pattern that works for Extractors may fail for Generators)
- Context shifts (same agent class, different domain)
- Aging (a pattern from 6 months ago may be stale)
- Override frequency (if humans override 60% of the pattern, confidence should go DOWN, not up)

**Fix:** Pattern confidence should be calculated from:
```python
confidence = (uses_without_override / total_uses) * recency_factor
recency_factor = max(0.5, 1.0 - (days_since_last_validation / 180))
```

Also add a `last_validated_at` field and include specification aging for patterns themselves.

### 13. HITL gate placement is one-per-phase, but CAWDP needs more

The plan puts one HITL gate at the end of each phase. But CAWDP's human gates are more granular in some cases. For instance, the Agent Design Workflow has 7 human gates across 7 stages.

For the current 152-output application, one gate per phase is probably the right granularity for Phase 1. But the architecture should support sub-phase gates for future use cases.

**Fix:** The master workflow should support an optional `sub_gates` configuration per phase. For now, all phases get one gate. Later, phases can define internal gates (e.g., P7 might gate after agent roster is defined, then again after all specifications are complete).

### 14. DecisionToolkit is referenced but undefined

The Medium workflow code references `DecisionToolkit()` — this should be the Decision Presentation Pattern implementation (2-4 structured options with benefits/risks, custom option always available).

**Fix:** Define `DecisionToolkit` explicitly with:
```python
class DecisionToolkit:
    """Tool for recording human decisions with the Decision Presentation Pattern."""
    @tool
    def record_decision(self, decision: str, reasoning: Optional[str], 
                       output_refs: List[str]) -> str: ...
    
    @tool  
    def present_options(self, options: List[DecisionOption]) -> str: ...
```

### 15. The cost target ($50 per full spec) needs LLM-specific validation

With Ollama glm-5.1:cloud as primary model, cost depends on their pricing. The $50 target may be realistic or not depending on token consumption. The Deep outputs (Compiler→Analyst→Deriver per output, 5 iterations max, 10 Deep outputs) could be expensive.

**Fix:** Add a cost cap per subworkflow. If a Deep output exceeds its budget, halt and escalate to human. Track actual costs from Day 1, not just in Phase 5.

---

## 💡 Improvement Opportunities

### 16. Judgment propagation is the real compression engine

The plan mentions pattern pre-fill (40-70% compression) but under-develops **judgment propagation** — when a human makes a decision (e.g., "this boundary is Regime 3"), that decision automatically fills into all dependent outputs. The fractal analysis estimated this compresses 309-618 Medium tasks to ~130-250 human actions.

This is the biggest efficiency gain and it's barely described.

**Enhancement:** Add a `DecisionPropagator` that:
1. Records a human decision with its `output_refs` (which outputs it affects)
2. Queries the dependency DAG for all downstream outputs
3. Pre-fills the decision into those outputs' pattern entries
4. Flags affected outputs for "review, not re-fill" (the human should confirm, not re-decide)

Example: When a human sets "enforcement_regime: Regime 3" for a boundary in P7-02, the propagator auto-fills this into P8 contract primitives, P9 override protocol, and P10 aging schedule — 3 outputs filled from 1 decision.

### 17. Build the Pattern Library with seed data, not from scratch

The plan has the Pattern Library starting empty and learning from decisions. But you already have 5 validated patterns (Signal Detector, Multi-Lens Analyst, Discovery Explorer, Learning Scaffold, Review Partner) with known defaults. And the fractal analysis identified class-specific defaults for all Medium outputs.

**Enhancement:** Seed the Pattern Library with:
- 5 core patterns (from the Pattern System)
- Class-specific defaults per output (Extractor, Measurer, Assessor, Generator, Aggregator)
- Orientation-specific adjustments (possibility vs bridge vs constraint)

This means the Pattern Library starts at 40-60% coverage on first use, not 0%.

### 18. Progressive autonomy for the orchestrator itself

The plan doesn't track progressive autonomy for the workflow. But as patterns learn and humans approve outputs, specific output types should be able to graduate from Shadow→Advisory→Supervised→Autonomous.

**Enhancement:** Add an autonomy tracker per output type:

```python
class OutputAutonomyTracker:
    """Track progressive autonomy per output type."""
    autonomy: dict[str, AutonomyLevel]  # output_id → Shadow/Advisory/Supervised/Autonomous
    override_history: dict[str, int]  # output_id → override_count
    approval_history: dict[str, int]  # output_id → approval_count_without_changes
```

After 3 consecutive approvals without changes for a specific output type, promote from Shadow→Advisory. After 5, promote to Supervised. This is CAWDP applying to itself.

### 19. The 5-week timeline is optimistic for one developer

Week 2 includes 11 phase specialist agents with proper instructions. The P10 implementation spec identified agent instructions as the **hardest, most critical work** — encoding authority boundaries, never-rules, domain expertise, and hardest moments is a design decision that can't be delegated to agents. This alone could take 2-3 weeks.

**Enhancement:** Restructure timeline:
- Phase 1 (Week 1): Foundation + **Pattern Library seed data** (not learning, just static patterns)
- Phase 2 (Weeks 2-3): Agent instructions for P0-P5 (highest volume of outputs)
- Phase 3 (Week 4): Master orchestrator + P0→P5 integration
- Phase 4 (Weeks 5-6): P6-P10 agents + full integration
- Phase 5 (Week 7): Production hardening

Or better: **build incrementally by phase, not by layer.** Get P0 working end-to-end (Shallow+Medium+Deep, pattern pre-fill, HITL gate, persistence) before building P1. This is the "15-minute specification" MVP approach — validate the architecture on the smallest meaningful slice first.

---

## Summary

| Category | Count | Action |
|----------|-------|--------|
| 🔴 Architecture issues | 4 | Fix before building |
| 🟡 Missing CAWDP requirements | 6 | Add to output schema and quality gates |
| 🟢 Implementation concerns | 5 | Fix as you build |
| 💡 Improvements | 4 | Implement when practical |

**The single most important fix:** Drop the Team layer. It's unnecessary complexity. The master workflow + WorkflowFactory + SurrealDB-as-shared-state is the right architecture.

**The single most important addition:** The `artefact_tags` field on every output. Without it, the entire P10 pipeline (Methodology Reflection, Confidence Map, EVOLVE Playbook, Aging Schedule) has nothing to work with. This cascading dependency is invisible until you need P10 and discover everything is missing.

**The single most valuable improvement:** Judgment propagation. Pattern pre-fill is good, but one-decision-fills-many-outputs is the real compression engine. A human decides "Regime 3" once, and 3-5 downstream outputs get pre-filled automatically. That's where the 309-618 → 130-250 compression actually happens.Memory updated. The key takeaway from this review: the architecture is mostly right but the Team layer is dead weight, and six CAWDP requirements that are structurally necessary (artefact_tags, epistemic metadata, enforcement regimes, contamination checks, null states, aging metadata) need to be in the base output schema from Day 1 — retrofitting them later means revisiting every output.

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-23T04:12:44* · `glm-5.1:cloud` · `cb66bed9...`

### Prompt

Thanks for your notes. The plan is being updated.

Let's put aside the previous implementation plans we have considered and ideate on alternative methods to produce an agentic workflow design specification based on CAWDP framework and principles. 

For instance, we could focus on just Phase 0, implement it so that we can see it producing the required outputs. Then we work on Phase 1 etc.

Another option could be an output specification / template that agents need to be complete before they can say their tasks are completed.

Comment on the viability/feasibility of these ideas. Add other potential implemntation methods.

### Response

# Implementation Methods for CAWDP Design Specifications

Let me evaluate the two ideas you proposed, then add five more approaches.

---

## Idea 1: Phase-by-Phase (Start with P0)

**Viability: High** — This is the approach I recommended in the review. P0 alone produces 9 outputs, all useful independently (5 identity questions, scope boundaries, target characteristics, orientation declaration, pattern match). You get value from Day 1.

**Feasibility: High** — P0 is the smallest meaningful unit. It's the "15-minute specification" entry point. Most P0 outputs are Shallow or Medium depth. With pattern pre-fill, a human makes ~15 decisions for P0.

**Strengths:**
- Validates architecture on the smallest slice
- Each phase validates infrastructure before the next builds on it
- Natural quality gate between phases
- Progressive value — P0 alone is useful
- P0 outputs feed directly into P1, P2, etc. (Direction→Destination→Path→Work)

**Weaknesses:**
- P1 jumps from 9 to 31 outputs — a big step up in complexity
- Phase boundaries aren't always clean — P2 backcasting depends heavily on P1 output quality
- Doesn't address the enforcement question — how do you know a phase is "complete"?

**My assessment:** This is the right *build order*, but it doesn't answer *how* outputs get produced. It answers *when* you build each piece, not *what mechanism* produces outputs.

---

## Idea 2: Output Specification / Template Completion

**Viability: High** — This is essentially the output catalogue made enforceable. Each of the 152 outputs has a schema with required and optional fields. An output isn't "done" until all required fields are completed.

**Feasibility: Medium-High** — The schemas already exist (from the output catalogue and fractal analysis). The enforcement mechanism is schema validation, which is Regime 3 (prevent by design). Pydantic makes this natural.

**Strengths:**
- Natural quality gate — incomplete template = incomplete output
- Schema validation is structural enforcement (CC-4 at the output layer)
- Template completion percentage is a natural progress metric
- Pattern Library pre-fills template fields (40-70%)
- The "done" condition is unambiguous

**Weaknesses:**
- Templates define the *what*, not the *how* — agents still need instructions on producing each field's content
- Risk of template-filling without genuine judgment (the worst failure mode from the meta-application)
- Some fields require human judgment, some can be agent-produced, some are "agent prepares, human decides" — templates don't distinguish these
- Who enforces completion? Need a validation layer beyond just schema checks

**My assessment:** This is the right *enforcement mechanism*, but it doesn't answer *who* fills the templates or *in what order*.

---

## Five Additional Approaches

### Idea 3: Conversational Single-Agent (Agent Designer)

One agent walks through CAWDP conversationally, producing outputs one at a time using the Decision Presentation Pattern.

**Viability: Medium** — We already designed this (Agent Designer Agent). It's the simplest architecture: one conversation, one agent, progressive disclosure through interaction.

**Feasibility: Medium-High** — Single agent is easier to build than a multi-agent workflow. But the agent needs extensive instructions covering all 152 outputs. Context window management becomes critical by P6+.

**Strengths:**
- Simplest possible architecture
- Natural progressive disclosure
- User controls pacing
- Decision Presentation Pattern built in (2-4 options, never open questions)
- Feels like working with a knowledgeable guide

**Weaknesses:**
- Single agent handles all depth levels (Shallow to Deep)
- No parallelization — everything is sequential
- Context window limits by P7+ (lots of accumulated context)
- Single point of failure — one confused turn derails everything
- Doesn't leverage the depth classification (Shallow outputs don't need an LLM)

**When to use:** MVP for validating the concept. If you want to prove CAWDP produces value with real users, a single conversational agent producing P0 outputs is the fastest path.

---

### Idea 4: Template-Driven with Human-Required Fields

Each output template has three field types: **agent-filled** (automatic from patterns, dependencies, or computation), **human-required** (judgment calls that must come from the human), and **agent-prepared** (agent drafts, human confirms).

**Viability: High** — This directly implements CAWDP's complementarity analysis at the field level. Some fields are pure extraction (agent-filled), some are pure judgment (human-required), some are collaborative (agent-prepared, human-confirms).

**Feasibility: High** — The field-level allocation is already implied by the output catalogue. Each field has a natural complementarity: P0 Q1-Q5 are human-required, P0 target characteristics are agent-prepared from Q1-Q5 answers, P1 output schemas are agent-filled from P0 outputs, etc.

**Strengths:**
- Crystal clear about what needs human judgment
- Complementarity analysis at the field level (H/A/S per field)
- Natural quality gate — incomplete human fields = incomplete output
- Pattern Library fills agent-prepared fields
- Aligns perfectly with "agent prepares judgment, human makes judgment"

**Weaknesses:**
- Requires field-level complementarity analysis for all 152 outputs (significant upfront work)
- The "agent-prepared, human-confirms" category creates a lot of review overhead if not carefully scoped
- Some fields shift between categories depending on context (e.g., P7 boundaries are human-required for novel agents but agent-prepared for pattern-matched agents)

**When to use:** This is the right *enforcement model* for the output templates. It doesn't replace the build order or the production mechanism — it specifies who fills each field.

---

### Idea 5: Milestone-First (Commercial Architecture)

Start with Milestone 1 (Boundary Map) as the first deliverable. Build only what's needed to produce a 30-minute Boundary Map. Then Milestone 2 (Allocation Map), etc.

**Viability: High** — This is the commercial architecture already designed. Milestone 1 spans P0-P4 (identity, boundaries, allocation). It produces the first independently valuable artifact.

**Feasibility: Medium** — Milestone 1 spans 5 phases. You need P0 through P4 working to produce a Boundary Map. That's more infrastructure than P0 alone, but it produces something a real user (Sarah Chen) would pay for.

**Strengths:**
- Commercial value from first milestone
- Each milestone is independently valuable
- Natural progressive disclosure — user sees value at each milestone
- Validates with real users early
- The 4 milestones map to 4 revenue streams

**Weaknesses:**
- Milestones don't map 1:1 to phases (Milestone 1 spans P0-P4)
- Building 5 phases before any value delivery
- May produce incomplete specifications (Milestone 1 doesn't include P5-P10)
- Misses the full CAWDP depth for early milestones

**When to use:** When commercial validation is the priority. If you need to prove value to Sarah Chen before building the full system, start with Milestone 1.

---

### Idea 6: Output-First / Backcasting Implementation

Define the final output specification first (what does a complete CAWDP specification look like?), then work backwards to figure out what each phase needs to produce.

**Viability: Medium-High** — This is literally CAWDP Phase 2 (Backcasting) applied to the implementation. You define the destination (complete specification), then trace the dependency chain backwards.

**Feasibility: Medium** — The output catalogue already defines 152 outputs with dependencies. The dependency DAG already exists. The backcasting is done. But defining what "complete" means for each output at the field level requires detailed schema work.

**Strengths:**
- Knows exactly where it's going
- Each phase produces what the next phase needs
- Natural dependency tracking
- Aligns with CAWDP's own methodology (practice what you preach)

**Weaknesses:**
- May over-specify early phases before understanding what's actually needed
- The dependency chain is complex (152 outputs with cross-references)
- Risk of analysis paralysis — spending too much time on the spec and not building

**When to use:** When you want the implementation to match CAWDP's own methodology. This is the most "meta" approach — CAWDP implemented using CAWDP.

---

### Idea 7: Progressive Depth (Shallow → Medium → Deep)

Build all 11 phases at Shallow depth first. Then add Medium depth. Then add Deep depth. Instead of building phases vertically (complete P0, then complete P1), build depth horizontally (all phases shallow, then all phases medium).

**Viability: Medium** — Interesting intellectually, but Shallow outputs alone don't form a complete specification. You'd have extracted/computed values but no judgment or synthesis.

**Feasibility: Low-Medium** — Shallow depth is easiest to implement (extraction/computation, no LLM needed). But producing only Shallow outputs for all 11 phases gives you a skeleton without flesh — the specification would be incomplete.

**Strengths:**
- Fastest path to "all 152 outputs exist" (even if Shallow)
- Validates the dependency chain across all phases early
- Natural progressive disclosure by depth
- Shallow outputs can be automated (no LLM, just computation)

**Weaknesses:**
- Shallow-only specification is useless without Medium/Deep — you have facts but no judgment
- The value is in Medium and Deep outputs, not Shallow
- Phase dependencies mean P2 can't be Shallow if P1 is Deep (backcasting needs P1 depth)
- Building all 11 phases at once, even shallow, is a lot of orchestration to get right

**When to use:** Never as the primary approach. But useful as a validation layer — run Shallow outputs first to validate dependency chains, then add Medium/Deep depth.

---

## Recommendation: Combine Approaches

The two ideas you proposed aren't alternatives — they answer different questions:

| Question | Answer | Approach |
|----------|--------|----------|
| **When** do you build each piece? | Phase-by-phase, starting with P0 | Idea 1 |
| **How** do you know something is done? | Template completion with field-level enforcement | Idea 2 + Idea 4 |
| **Who** fills each field? | Complementarity allocation per field (H/A/S) | Idea 4 |
| **What** does the final product look like? | Complete specification with all 152 outputs | Idea 6 |
| **Where** do you start commercially? | Milestone 1 (Boundary Map) | Idea 5 |

The right answer combines all five:

### Recommended: Phase-by-Phase, Template-Driven, Field-Allocated, Milestone-Validated

**Build order:** P0 first (9 outputs, ~15 human decisions), then P1 (31 outputs, more automated), then P2-P4 to reach Milestone 1 (Boundary Map = commercial value).

**Enforcement:** Every output has a Pydantic schema. Required fields are validated at write time. Schema validation is Regime 3 enforcement. An output isn't "complete" until all required fields pass validation.

**Field allocation:** Each field in each template is tagged as:
- **Auto** (agent-filled, extracted or computed from dependencies)
- **Human** (requires human judgment, agent cannot fill)
- **Prepared** (agent drafts from patterns/dependencies, human confirms)

**Pattern Library:** Seeds templates with 40-70% pre-filled content. Human fills the gaps (the 30-60% that requires judgment).

**Milestone validation:** After P4, you have enough for Milestone 1 (Boundary Map). Stop and validate with a real user before continuing.

**Progressive depth:** P0 is mostly Medium depth (identity questions are judgment-heavy). Shallow outputs (extraction/computation) are automated. Deep outputs (P10 methodology reflection) come later.

---

## The Minimum Viable P0

If you're going to start with P0, here's what it looks like as a template-driven, field-allocated system:

**P0 outputs (9):**

| Output | Depth | Fields | Auto | Prepared | Human | Pattern Pre-fill |
|--------|-------|--------|------|----------|-------|-------------------|
| P0-01 Identity Card | Medium | 5 | 1 | 2 | 2 | 50-60% |
| P0-02 Purpose Statement | Medium | 3 | 0 | 2 | 1 | 40-50% |
| P0-03 Principal Declaration | Medium | 4 | 1 | 1 | 2 | 30-40% |
| P0-04 Scope Boundary Map | Medium | 6 | 2 | 2 | 2 | 60-70% |
| P0-05 Target Characteristics | Deep | 25 | 5 | 10 | 10 | 30-40% |
| P0-06 Pattern Match Result | Shallow | 3 | 3 | 0 | 0 | 100% |
| P0-07 Possibility Orientation | Shallow | 2 | 1 | 0 | 1 | 80-90% |
| P0-08 Hardest Boundary Moment | Medium | 4 | 0 | 1 | 3 | 20-30% |
| P0-09 CAWDP Characteristics | Deep | 12 | 3 | 4 | 5 | 40-50% |

**Total P0 decisions:** ~15-20 human judgments (not 483-643 tasks).

**Implementation:** 3 Shallow outputs (fully automated), 4 Medium outputs (pattern pre-fill + human gaps), 2 Deep outputs (Compiler→Analyst→Deriver).

**Template enforcement:** Each output has a Pydantic schema. The P0 workflow doesn't advance until all required fields pass validation.

**Judgment propagation:** When the human answers Q1-Q5 (P0-01), those answers propagate to P0-02 through P0-09. One human judgment fills multiple template fields.

**Next step after P0:** Build P1 (31 outputs). P1 outputs depend on P0 outputs (dependency chain). Most P1 outputs are Shallow or Medium (extraction/computation from P0 results).

---

## Summary

| Approach | Viability | Feasibility | Time to Value | Fidelity |
|----------|-----------|-------------|---------------|----------|
| 1. Phase-by-Phase | High | High | Fast (P0 = 1-2 weeks) | High |
| 2. Template Completion | High | Med-High | Medium | High |
| 3. Conversational Agent | Medium | Med-High | Fast (3-5 days) | Medium |
| 4. Field-Allocated Templates | High | High | Medium | High |
| 5. Milestone-First | High | Medium | Slower (5 phases) | Medium |
| 6. Backcasting | Med-High | Medium | Medium | High |
| 7. Progressive Depth | Medium | Low-Med | Fast (shallow) | Low |

**My recommendation:** Combine 1 + 2 + 4 + 5.

Build **P0 first** with **template-driven, field-allocated** enforcement. Validate at **Milestone 1** (after P0-P4). Use **judgment propagation** as the compression engine. Start with **conversational agent** for P0 (fastest to build), then evolve to **workflow-based** for P1+ when parallelization matters.

The conversational agent for P0 is a 3-5 day build. The workflow-based approach for P1+ is a 2-3 week build. And Milestone 1 validation with a real user happens after P0-P4 are working — approximately 4-6 weeks from now.Memory updated with the combined implementation strategy. The key insight: start simple (conversational agent for P0, 3-5 day build), validate with real users at Milestone 1, then evolve to workflow-based architecture for P1+ where parallelization matters. The four enforcement mechanisms (template schemas, field allocation, judgment propagation, milestone validation) operationalize CAWDP principles at the implementation layer.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-05-23T04:24:48* · `glm-5.1:cloud` · `11dbe300...`

### Prompt

Perhaps I jumped to the workflow conclusion when a task based approach could be a better way to see this:
What about if every field of the CAWDP output schema had associated tasks defined in a dependency graph. Each of these tasks defined which knowledge, skills, context, database tables etc was required to complete successfully. Then agents could be created to complete the tasks.

### Response

# Task-Based Architecture: Field-Level Dependency Graph

You're onto something. This is fundamentally different from the workflow approach — and it's better aligned with how CAWDP itself works.

Let me work through this properly.

---

## Why This Is Better Than the Workflow Approach

The workflow approach **predefines the sequence**. The task approach **defines the dependencies** and lets the execution emerge from the graph. This is exactly what CAWDP Phase 2 (Backcasting) does — trace dependencies backward from outputs to inputs. The implementation should mirror the methodology.

**Workflow = sequence is the architecture.**
**Task graph = dependencies are the architecture, sequence emerges.**

| Concern | Workflow | Task Graph |
|---------|----------|------------|
| Parallelization | Explicit Parallel blocks | Automatic — any task whose deps are met runs |
| New output added | Redesign workflow | Add task + dependencies, done |
| Failure recovery | Restart workflow or phase | Retry single task |
| Progress tracking | "Phase 3 of 11" | "127 of 283 fields complete" |
| Testing | Test workflow end-to-end | Test each task independently |
| Granularity | Phase-level | Field-level |
| Resumability | Restart from phase | Resume from incomplete task |

The task graph is more flexible, more testable, more resumable, and more aligned with CAWDP's own backcasting methodology.

---

## The Architecture

### Three Layers

```
Layer 1: TASK DEFINITION (the dependency graph)
   - Every field in the output schema = a task
   - Tasks declare dependencies, requirements, quality criteria
   - The graph IS the implementation of Phase 2 (Backcasting)

Layer 2: TASK ROUTING (which agent handles which task)
   - Agent types matched to task characteristics
   - Auto tasks → Extractor (computation, no LLM)
   - Prepared tasks → Writer (LLM drafts, human confirms)
   - Human tasks → Judge (presents options, human decides)
   - Deep tasks → Compiler/Analyst/Deriver team

Layer 3: TASK EXECUTION (the engine that runs the graph)
   - Task scheduler: find ready tasks, route to agents, collect results
   - State manager: track completion, handle failures, persist results
   - Human-in-the-loop: pause for human tasks, resume when completed
```

### Task Definition Schema

```python
from pydantic import BaseModel
from typing import Any, Literal
from enum import Enum

class Depth(str, Enum):
    SHALLOW = "shallow"   # Computation/extraction, no LLM
    MEDIUM = "medium"     # LLM + pattern pre-fill
    DEEP = "deep"         # Multi-agent synthesis

class Complementarity(str, Enum):
    AUTO = "auto"           # System fills (computation, extraction, propagation)
    PREPARED = "prepared"   # Agent drafts, human confirms
    HUMAN = "human"         # Human judgment required

class RequirementType(str, Enum):
    KNOWLEDGE = "knowledge"       # CAWDP methodology knowledge
    CONTEXT = "context"           # Previous output fields
    DATABASE = "database"        # SurrealDB tables/queries
    PATTERN = "pattern"           # Pattern Library entries
    HUMAN_INPUT = "human_input"   # Human judgment needed
    COMPUTATION = "computation"   # Algorithmic processing

class TaskRequirement(BaseModel):
    type: RequirementType
    description: str
    source: str  # e.g., "P0-01.identity_questions", "design_agent_specifications"
    optional: bool = False

class QualityCriterion(BaseModel):
    criterion: str
    check_type: Literal["schema", "range", "presence", "custom"]
    check_definition: str  # e.g., "value in ['Extractor', 'Measurer', ...]"

class CAWDPTask(BaseModel):
    task_id: str                    # e.g., "P0-01-Q1-identity"
    phase: int                      # 0-10
    output_id: str                  # e.g., "P0-01"
    field_path: str                 # e.g., "identity_questions.q1_answer"
    field_description: str          # What this field contains
    depth: Depth                     # Shallow/Medium/Deep
    complementarity: Complementarity # Auto/Prepared/Human
    dependencies: list[str]          # task_ids that must complete first
    requirements: list[TaskRequirement]
    quality_criteria: list[QualityCriterion]
    agent_type: str                  # Extractor/Writer/Judge/Compiler/Analyst/Deriver
    pattern_fill: float             # 0.0-1.0, how much pattern pre-fills
    epistemic_type: Literal["deterministic", "probabilistic", "elicited"]
    null_state: str                  # Class-specific null state
    artefact_tags: set[str] = set() # For P10 assembly
```

### Example Tasks

**Shallow + Auto task (extraction):**
```python
CAWDPTask(
    task_id="P0-06-pattern-match",
    phase=0,
    output_id="P0-06",
    field_path="pattern_match_result",
    field_description="The agent class pattern matched from identity answers",
    depth="shallow",
    complementarity="auto",
    dependencies=["P0-01-Q1-identity", "P0-01-Q2-orientation"],
    requirements=[
        TaskRequirement(type="context", source="P0-01.identity_questions", optional=False),
        TaskRequirement(type="pattern", source="pattern_library.core_patterns", optional=False),
        TaskRequirement(type="database", source="design_core_patterns", optional=False),
    ],
    quality_criteria=[
        QualityCriterion(criterion="Result is valid pattern name", 
                         check_type="custom", 
                         check_definition="value in ['Signal Detector', 'Multi-Lens Analyst', 'Discovery Explorer', 'Learning Scaffold', 'Review Partner']"),
    ],
    agent_type="Extractor",
    pattern_fill=1.0,  # Fully computed from pattern library
    epistemic_type="deterministic",
    null_state="No pattern matched — manual classification required",
)
```

**Medium + Prepared task (agent drafts, human confirms):**
```python
CAWDPTask(
    task_id="P0-04-scope-boundary-map",
    phase=0,
    output_id="P0-04",
    field_path="scope_boundary_map",
    field_description="Three-column boundary map (You/AI/System) with tasks and authority labels",
    depth="medium",
    complementarity="prepared",
    dependencies=["P0-01-Q1-identity", "P0-01-Q3-violates", "P0-06-pattern-match"],
    requirements=[
        TaskRequirement(type="context", source="P0-01", optional=False),
        TaskRequirement(type="context", source="P0-03-principal-declaration", optional=False),
        TaskRequirement(type="pattern", source="pattern_library.scope_templates", optional=False),
        TaskRequirement(type="knowledge", source="cawdp_5_class_taxonomy", optional=False),
    ],
    quality_criteria=[
        QualityCriterion(criterion="All three columns populated", check_type="custom", check_definition="len(scope_in) > 0 and len(scope_out) > 0"),
        QualityCriterion(criterion="Every task has authority label", check_type="custom", check_definition="all(task.authority for task in all_tasks)"),
    ],
    agent_type="Writer",
    pattern_fill=0.6,  # 60% from pattern + context
    epistemic_type="elicited",
    null_state="Nothing to assemble — scope boundaries not yet defined",
)
```

**Human task (judgment required):**
```python
CAWDPTask(
    task_id="P0-01-Q1-identity",
    phase=0,
    output_id="P0-01",
    field_path="identity_questions.q1_answer",
    field_description="What IS this agent? (essence, not behavior)",
    depth="medium",
    complementarity="human",
    dependencies=[],  # No dependencies — this is a starting point
    requirements=[
        TaskRequirement(type="human_input", source="user", optional=False),
        TaskRequirement(type="pattern", source="pattern_library.identity_examples", optional=True),
    ],
    quality_criteria=[
        QualityCriterion(criterion="Answer describes essence, not behavior", 
                         check_type="custom",
                         check_definition="not starts_with_action_verb()"),
    ],
    agent_type="Judge",  # Presents options, human decides
    pattern_fill=0.3,  # 30% — pattern provides examples, not the answer
    epistemic_type="elicited",
    null_state="Unable to assess — identity not declared",
)
```

**Deep task (multi-agent synthesis):**
```python
CAWDPTask(
    task_id="P0-05-target-characteristics",
    phase=0,
    output_id="P0-05",
    field_path="target_characteristics",
    field_description="12 target state characteristics across 4 dimensions",
    depth="deep",
    complementarity="prepared",
    dependencies=["P0-01-Q1-identity", "P0-01-Q2-orientation", "P0-01-Q3-violates", 
                   "P0-01-Q4-wrong", "P0-01-Q5-hardest-moment", "P0-06-pattern-match"],
    requirements=[
        TaskRequirement(type="context", source="P0-01.identity_questions", optional=False),
        TaskRequirement(type="context", source="P0-03.principal_declaration", optional=False),
        TaskRequirement(type="context", source="P0-04.scope_boundary_map", optional=False),
        TaskRequirement(type="knowledge", source="cawdp_target_state_dimensions", optional=False),
        TaskRequirement(type="database", source="design_workflows", optional=True),
    ],
    quality_criteria=[
        QualityCriterion(criterion="All 4 dimensions present", check_type="custom", check_definition="len(dimensions) == 4"),
        QualityCriterion(criterion="At least 2 characteristics per dimension", check_type="custom", check_definition="all(len(d.chars) >= 2 for d in dimensions)"),
        QualityCriterion(criterion="No feasibility contamination in P0", check_type="custom", check_definition="no_mechanism_keywords(text)"),
    ],
    agent_type="Compiler→Analyst→Deriver",  # Deep workflow
    pattern_fill=0.4,  # 40% — pattern provides dimension structure
    epistemic_type="probabilistic",
    null_state="Insufficient basis — identity questions must be answered first",
)
```

---

## How the Task Graph Runs

### Task Scheduler (simple topological sort)

```python
class TaskScheduler:
    def __init__(self, tasks: list[CAWDPTask], pattern_library: PatternLibrary):
        self.tasks = {t.task_id: t for t in tasks}
        self.completed: dict[str, Any] = {}  # task_id → result
        self.pattern_library = pattern_library
    
    def get_ready_tasks(self) -> list[CAWDPTask]:
        """Find tasks whose dependencies are all complete."""
        ready = []
        for task in self.tasks.values():
            if task.task_id in self.completed:
                continue
            if all(dep in self.completed for dep in task.dependencies):
                ready.append(task)
        return ready
    
    def complete_task(self, task_id: str, result: Any):
        """Mark a task as complete and propagate decisions."""
        self.completed[task_id] = result
        # Judgment propagation: when a human decision completes,
        # update all dependent tasks that can now pre-fill from this
        self.propagate_decisions(task_id, result)
    
    def propagate_decisions(self, source_task_id: str, result: Any):
        """Propagate a completed task's result to dependent tasks."""
        for task in self.tasks.values():
            if source_task_id in task.dependencies:
                # Pre-fill any fields that can be derived from this result
                self.pattern_library.learn_from_decision(
                    task_id=task.task_id,
                    field=task.field_path,
                    value=result,
                    source=source_task_id,
                )
    
    def get_progress(self) -> dict:
        """Return completion statistics."""
        total = len(self.tasks)
        done = len(self.completed)
        return {
            "total": total,
            "completed": done,
            "remaining": total - done,
            "percentage": done / total * 100,
            "by_phase": self._group_by_phase(),
            "by_depth": self._group_by_depth(),
            "by_complementarity": self._group_by_complementarity(),
        }
```

### Task Router (assigns tasks to agents)

```python
class TaskRouter:
    def route(self, task: CAWDPTask) -> Agent:
        """Route a task to the appropriate agent type."""
        if task.depth == "shallow" and task.complementarity == "auto":
            return self.extractor_agent  # No LLM needed
        elif task.depth == "medium" and task.complementarity == "prepared":
            return self.writer_agent  # LLM drafts, human confirms
        elif task.depth == "medium" and task.complementarity == "human":
            return self.judge_agent  # Decision Presentation Pattern
        elif task.depth == "deep":
            return self.deep_team  # Compiler→Analyst→Deriver
        else:
            raise ValueError(f"Unknown task type: {task.depth}/{task.complementarity}")
```

### Main Execution Loop

```python
async def run_cawdp_graph(
    tasks: list[CAWDPTask],
    pattern_library: PatternLibrary,
    writer: WriterAgent,
    judge: JudgeAgent,
    deep_team: DeepTeam,
) -> dict[str, Any]:
    """Execute the full CAWDP task graph."""
    
    scheduler = TaskScheduler(tasks, pattern_library)
    
    while not scheduler.is_complete():
        # Get tasks whose dependencies are met
        ready = scheduler.get_ready_tasks()
        
        if not ready:
            # Deadlock — some dependency is missing
            raise DeadlockError(scheduler.get_blocked_tasks())
        
        # Route and execute each ready task
        for task in ready:
            agent = router.route(task)
            
            # Load context from completed dependencies
            context = {dep: scheduler.completed[dep] for dep in task.dependencies}
            
            # Execute
            if task.complementarity == "human":
                # Pause for human judgment (Decision Presentation Pattern)
                result = await agent.present_options(task, context)
            else:
                # Execute with LLM or computation
                result = await agent.execute(task, context)
            
            # Validate against quality criteria
            for criterion in task.quality_criteria:
                if not validate(result, criterion):
                    result = await agent.retry(task, context, criterion)
            
            # Mark complete and propagate
            scheduler.complete_task(task.task_id, result)
    
    return scheduler.completed
```

---

## How Many Tasks?

Not 3800. Not 760. Realistic task counts by grouping related fields:

| Depth | Task Count | Description |
|-------|-----------|-------------|
| Shallow | ~30 | Single-field extractions/computations |
| Medium | ~180 | Multi-field outputs with judgment |
| Deep | ~10 | Multi-agent synthesis workflows |
| **Total** | **~220** | **Manageable task graph** |

How we get to ~220 (not 760+):
- P0-01 Identity Card: 1 task (5 questions grouped), not 5 separate tasks
- P0-04 Scope Boundary Map: 1 task (map as a unit), not 20 field-level tasks
- P0-05 Target Characteristics: 4 tasks (one per dimension), not 25 field-level tasks
- P1 output schemas: 1 task each (schema is a unit), not per-field tasks
- Shallow outputs: 1 task each (computation is atomic)

**Principle: Group fields into task units that share the same agent type, complementarity, and dependencies. A task is the smallest unit that makes sense to route to a single agent.**

---

## Comparison: Task Graph vs Workflow

| Aspect | Workflow (previous) | Task Graph (this) |
|--------|-------------------|-------------------|
| Sequence | Predefined in workflow code | Emerges from dependency graph |
| Parallelization | Explicit Parallel blocks | Automatic — any ready task runs |
| New output | Redesign workflow | Add task + dependencies |
| Progress tracking | "Phase 3 of 11" | "127 of 220 tasks complete" |
| Testing | End-to-end workflow test | Individual task test |
| Failure recovery | Restart phase | Retry single task |
| Granularity | Phase-level | Field-level (grouped) |
| CAWDP alignment | Phases map to workflow steps | Dependency graph IS Phase 2 |
| Complementarity | Not explicit | Built into task definition |
| Judgment propagation | Manual | Automatic via task completion |
| Pattern Library | Separate system | Built into task requirements |

---

## Key Advantages

### 1. The dependency graph IS the backcasting

CAWDP Phase 2 (Backcasting) says: "work backward from outputs to identify required inputs." The task dependency graph is literally this — every task declares what it needs. When P0-05 (Target Characteristics) depends on P0-01 (Identity Questions), that's the backcasting made executable.

### 2. Complementarity at the field level

Every task declares Auto/Prepared/Human. This is CAWDP Phase 4 (Capability Allocation) at the most granular level. The task graph doesn't just know what needs doing — it knows WHO should do it.

### 3. Pattern Library integrates naturally

Every task declares what pattern coverage it expects (0.0-1.0). When a task completes, its result propagates to dependent tasks. When a human makes a judgment, it fills multiple dependent tasks. The Pattern Library learns from every completion.

### 4. Progressive disclosure is natural

Start with P0 tasks (9 outputs, ~15-20 human decisions). The user sees progress at the field level. When P0 is complete, P1 tasks become ready. The graph enforces CAWDP's phase sequence without hardcoding it.

### 5. Resumability is trivial

If a task fails, retry that task. If the user stops after P3, resume from P4. The completed tasks are persisted. The graph knows what's ready.

### 6. Testing is task-level

Each task has clear inputs, outputs, and quality criteria. You can test any task independently by providing mock dependencies. No need for end-to-end workflow tests.

---

## Key Challenges

### 1. Task definition overhead

~220 tasks need to be defined. This is significant upfront work, but it's also the implementation of Phase 2 (Backcasting) — you're doing CAWDP on CAWDP.

**Mitigation:** Start with P0 tasks only (~30 tasks). Add P1 tasks after P0 is validated. The task definitions can be generated partially from the output catalogue.

### 2. Agent granularity

Do you need 220 agents? No. You need 5-6 agent types:
- **Extractor** (Shallow + Auto) — computation, extraction, propagation
- **Writer** (Medium + Prepared) — LLM drafts with pattern pre-fill
- **Judge** (Medium + Human) — Decision Presentation Pattern
- **Compiler** (Deep) — assemble, organize, de-duplicate
- **Analyst** (Deep) — calculate, correlate, surface anomalies
- **Deriver** (Deep) — derive recommendations from evidence

These 6 agent types handle all 220 tasks by routing based on depth and complementarity.

### 3. Human-in-the-loop coordination

Human tasks need to pause execution and wait for input. The task scheduler needs to:
- Identify which tasks need human input
- Present options (Decision Presentation Pattern)
- Pause until human responds
- Resume with the human's decision

**Mitigation:** The Judge agent handles this. It presents 2-4 options with benefits/risks, waits for the human, and returns the decision.

### 4. Context management

Agents need context from completed tasks. A Deep task (P0-05) needs results from 6 dependency tasks. That's a lot of context to load.

**Mitigation:** Don't pass full results as context. Pass **summaries** (structured extracts). P0-05 doesn't need the full text of P0-01 — it needs the pattern classification, orientation, never-rules, and wrong-ness criteria. Context compression is essential.

### 5. Error propagation

If a dependency task fails, all tasks depending on it are blocked. The scheduler needs deadlock detection.

**Mitigation:** The scheduler already has `get_blocked_tasks()`. If no tasks are ready and the graph isn't complete, it's a deadlock. Report which tasks are blocked and why.

---

## Recommended Implementation: Start with P0 Tasks

Define only P0 tasks first (~30 tasks). Build the scheduler, router, and 3 agent types (Extractor, Writer, Judge). Get P0 working end-to-end before adding P1.

```python
# P0 task count estimate:
# P0-01 Identity Card: 1 task (5 questions grouped)
# P0-02 Purpose Statement: 1 task
# P0-03 Principal Declaration: 1 task
# P0-04 Scope Boundary Map: 1 task
# P0-05 Target Characteristics: 4 tasks (one per dimension)
# P0-06 Pattern Match: 1 task (Shallow, auto)
# P0-07 Orientation Declaration: 1 task (Shallow, auto)
# P0-08 Hardest Boundary Moment: 1 task
# P0-09 CAWDP Characteristics: 4 tasks (one per dimension)
# Total: ~15 tasks for P0
```

Wait — that's only 15 tasks for P0, not 30. Because P0 is small (9 outputs) and many fields group naturally. That's even better — 15 tasks is very manageable for a first implementation.

**Build order:**
1. Define P0 task graph (15 tasks with dependencies)
2. Build Extractor agent (Shallow tasks)
3. Build Writer agent (Medium + Prepared tasks)
4. Build Judge agent (Medium + Human tasks)
5. Run P0 end-to-end
6. Add P1 tasks (~40 tasks)
7. Add Deep agents (Compiler/Analyst/Deriver)
8. Continue through P2-P10

---

## Summary

The task-based approach is **better** than the workflow approach because:

1. **It mirrors CAWDP methodology** — the dependency graph IS Phase 2 (Backcasting) made executable
2. **It's more flexible** — tasks run when dependencies are met, not in a hardcoded sequence
3. **It's more testable** — each task has clear inputs, outputs, and quality criteria
4. **It's more resumable** — retry single tasks, not entire phases
5. **It's more extensible** — add new outputs by adding tasks
6. **Complementarity is built in** — every task declares who fills it
7. **Judgment propagation is automatic** — completing a task propagates to dependents
8. **It requires fewer agents** — 6 types handle 220 tasks

The key challenge is task definition overhead (~220 tasks), but:
- Start with P0 (15 tasks)
- Tasks are generated from the output catalogue (mechanical work)
- The task definitions ARE the implementation of CAWDP's Phase 2Both memories updated. The architectural evolution is clear: each iteration has pushed CAWDP's principles deeper into the implementation — from a workflow that *uses* CAWDP to a task graph that *is* CAWDP. The dependency graph IS Phase 2, the task declarations ARE Phase 4 (complementarity at field level), and the pattern Library IS the compression mechanism that makes it practical.

---
