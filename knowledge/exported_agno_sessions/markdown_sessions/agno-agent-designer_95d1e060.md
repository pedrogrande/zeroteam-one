# Agno Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `95d1e060...` |
| **Type** | agent |
| **Agent** | Agno Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-01T08:22:34 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agno Agent Designer ✓ COMPLETED

*2026-05-01T08:22:34* · `glm-5.1:cloud` · `776198d1...`

### Prompt

Review this implementation plan. Point out any areas of improvement of gaps you see:

# Plan: Implementation Spec Pipeline — Gaps & Testing

> **Status**: Draft
> **Created**: 2026-05-01
> **Source**: Implementation Spec Pipeline implementation (Phases 1-5 of the design-spec → agent-spec bridge)

## TL;DR

Complete the 8 remaining gaps to make the design-spec → agent-spec pipeline fully functional end-to-end. The data layer (4 spec models, CRUD, indexes, agent toolkit) is done. What remains is: updating the ImplementationMap CRUD to accept spec linkage columns, giving the agent access to design specs, adding markdown rendering, building the final assembly step, handling database migrations, writing a seed script, and creating integration tests.

---

## What's Already Done

| Component | Status | File |
|-----------|--------|------|
| 4 spec models (AgentDataSpec, AgentToolsSpec, AgentBehaviourSpec, AgentVerificationSpec) | ✅ Done | `db/models.py` |
| 4 spec indexes | ✅ Done | `db/models_indexes.py` |
| 4 CRUD modules (data_specs, tools_specs, behaviour_specs, verification_specs) | ✅ Done | `db/data_specs.py`, `db/tools_specs.py`, `db/behaviour_specs.py`, `db/verification_specs.py` |
| ImplementationMap model with 8 spec linkage columns | ✅ Done | `db/models.py` |
| ImplementationMap indexes | ✅ Done | `db/models_indexes.py` |
| ImplementationMap CRUD (without spec linkage params) | ✅ Done | `db/implementation_maps.py` |
| `get_session()` helper | ✅ Done | `db/session.py` |
| Implementation spec agent with 10-tool toolkit | ✅ Done | `agents/implementation_spec_agent.py` |
| Agent registration in app/main.py | ✅ Done | `app/main.py` |
| Quick prompts in config.yaml | ✅ Done | `app/config.yaml` |
| All exports in db/__init__.py | ✅ Done | `db/__init__.py` |
| ruff check, ruff format, mypy all pass | ✅ Done | — |

---

## Phase 1: ImplementationMap CRUD Update

**Goal**: `register_implementation_map()` accepts the 8 new spec linkage columns so the map can track which spec versions it bridges.

**Steps**
1. Add 8 new parameters to `register_implementation_map()` in `db/implementation_maps.py`: `data_spec_id`, `data_spec_version`, `tools_spec_id`, `tools_spec_version`, `behaviour_spec_id`, `behaviour_spec_version`, `verification_spec_id`, `verification_spec_version` — all optional, defaulting to `None`
2. Pass these through to the `ImplementationMap()` constructor
3. Verify with mypy and ruff

**Relevant files**
- `db/implementation_maps.py` — update `register_implementation_map()` signature and constructor call
- `db/models.py` — `ImplementationMap` model already has the 8 columns (done)

**Verification**
1. `ruff check db/implementation_maps.py` passes
2. `mypy db/implementation_maps.py --ignore-missing-imports` passes
3. Manual: call `register_implementation_map()` with all 8 spec columns and confirm they persist

---

## Phase 2: Design Spec Integration for Implementation Spec Agent

**Goal**: The implementation spec agent can read the design spec for an agent to inform its spec drafting.

**Steps**
1. Add `get_design_spec_for_agent` tool to `ImplementationSpecToolkit` that calls `db.design_specs.get_design_spec(agent_id)` and returns the full design spec as JSON
2. Update the agent instructions to reference this tool: "Before drafting any spec, read the design spec to understand the agent's identity, constraints, and architecture"
3. Import `get_design_spec` from `db` in `agents/implementation_spec_agent.py`

**Relevant files**
- `agents/implementation_spec_agent.py` — add tool method and update instructions
- `db/design_specs.py` — existing `get_design_spec()` function (read-only, no changes needed)

**Verification**
1. `ruff check agents/implementation_spec_agent.py` passes
2. `mypy agents/implementation_spec_agent.py --ignore-missing-imports` passes
3. Manual: call `get_design_spec_for_agent("knowledge-agent")` and confirm it returns the design spec JSON

---

## Phase 3: Markdown Rendering for Spec Phases

**Goal**: Each spec can be rendered as human-readable markdown matching the template format, stored in `rendered_markdown`.

**Steps**
1. Create `db/spec_renderers.py` with 4 functions: `render_data_spec_markdown()`, `render_tools_spec_markdown()`, `render_behaviour_spec_markdown()`, `render_verification_spec_markdown()`
2. Each function takes the spec model instance and returns a markdown string matching the template question format (Q10-Q19, Q20-Q29, Q30-Q40, Q41-Q51)
3. Add a `render_and_save` convenience function for each spec type that renders the markdown and updates the `rendered_markdown` column
4. Import renderers in `db/__init__.py`

**Relevant files**
- `db/spec_renderers.py` — new file with 4 render functions + 4 save functions
- `db/__init__.py` — export render functions
- `docs/agent-specs/agent-design-template.md` — reference for question numbering and format

**Verification**
1. `ruff check db/spec_renderers.py` passes
2. `mypy db/spec_renderers.py --ignore-missing-imports` passes
3. Unit test: create a spec with sample data, render markdown, verify it contains expected section headers and question numbers

---

## Phase 4: Final Assembly — Spec → AgentSpec

**Goal**: When all 4 specs are approved, a function assembles them into an `AgentSpec` row and links them via `ImplementationMap`.

**Steps**
1. Create `db/spec_assembly.py` with `assemble_agent_spec(agent_id: str, assembled_by: str) -> AgentSpec` that:
   - Validates all 4 specs are approved (raises `ValueError` if not)
   - Fetches the latest approved version of each spec
   - Fetches the design spec for the agent
   - Creates an `ImplementationMap` linking design spec → 4 implementation specs → agent spec
   - Returns the created `AgentSpec`
2. The assembly function maps spec fields to AgentSpec columns:
   - `AgentDataSpec.session_memory_config` → `AgentSpec.add_history_to_context`, `num_history_runs`, `enable_agentic_memory`
   - `AgentToolsSpec.subtask_tool_map` → `AgentSpec.tools` (serialized)
   - `AgentBehaviourSpec.system_message` → `AgentSpec.system_message`
   - `AgentBehaviourSpec.model_config` → `AgentSpec.model`
   - `AgentVerificationSpec.progressive_autonomy_level` → stored in ImplementationMap
3. Add `assemble_agent_spec` to `db/__init__.py` exports
4. Add an `assemble_agent_spec` tool to `ImplementationSpecToolkit` that calls this function

**Relevant files**
- `db/spec_assembly.py` — new file with assembly logic
- `db/__init__.py` — export `assemble_agent_spec`
- `db/agent_specs.py` — existing `register_agent_spec()` for creating the AgentSpec
- `db/implementation_maps.py` — updated `register_implementation_map()` with spec linkage
- `agents/implementation_spec_agent.py` — add assembly tool

**Verification**
1. `ruff check db/spec_assembly.py` passes
2. `mypy db/spec_assembly.py --ignore-missing-imports` passes
3. Integration test: create all 4 approved specs, call `assemble_agent_spec()`, verify AgentSpec and ImplementationMap are created with correct linkages
4. Negative test: call `assemble_agent_spec()` with an unapproved spec, verify `ValueError`

---

## Phase 5: ImplementationMap Auto-Population

**Goal**: When the assembly function creates an ImplementationMap, it populates the consolidated JSONB fields from the individual specs.

**Steps**
1. In `assemble_agent_spec()`, after creating the AgentSpec, build the ImplementationMap JSONB fields:
   - `subtask_tool_map` ← from `AgentToolsSpec.subtask_tool_map`
   - `cc_implementation_map` ← from `AgentVerificationSpec.cc_implementation_map`
   - `database_schemas` ← from `AgentDataSpec.schema_sql` (wrapped in a dict)
   - `tool_registry` ← from `AgentToolsSpec.tool_authority_allowed` + `tool_authority_never`
   - `infrastructure_dependencies` ← from `AgentDataSpec.external_reads`
   - `inter_agent_interfaces` ← from `AgentToolsSpec.inter_agent_receive` + `inter_agent_send`
   - `human_interfaces` ← from `AgentBehaviourSpec.human_interface_primary` + `human_interface_secondary`
   - `progressive_autonomy_level` ← from `AgentVerificationSpec.autonomy_phases` (first phase)
2. Pass these to `register_implementation_map()` along with the 8 spec linkage columns

**Relevant files**
- `db/spec_assembly.py` — add consolidation logic
- `db/implementation_maps.py` — already updated in Phase 1

**Verification**
1. Integration test: after assembly, verify ImplementationMap has all JSONB fields populated from the corresponding specs
2. Verify spec linkage columns (`data_spec_id`, etc.) are correctly set

---

## Phase 6: Database Migration for Existing Tables

**Goal**: The running Docker database has the new tables and the ImplementationMap table has its 8 new columns.

**Steps**
1. Add a `scripts/migrate_db.py` script that:
   - Connects to the database
   - Creates the 4 new spec tables using `init_*_table()` functions
   - Adds 8 new columns to `implementation_maps` if they don't exist (using `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`)
2. Update `app/main.py` to call `init_*_table()` for all 4 new tables (already done)
3. Document the migration in the plan

**Relevant files**
- `scripts/migrate_db.py` — new migration script
- `app/main.py` — already calls `init_*_table()` for all 4 new tables

**Verification**
1. Run `docker compose down -v` to wipe the database
2. Run `docker compose up -d --build` to start fresh
3. Verify all 4 new tables exist in the `ai` schema
4. Verify `implementation_maps` has the 8 new columns
5. Verify existing tables (`agent_specs`, `agent_design_specs`, etc.) are unchanged

---

## Phase 7: Seed Script for Existing Agents

**Goal**: Backfill Phase 2–5 specs for the 3 existing agents (knowledge-agent, mcp-agent, infrastructure-agent) based on their current configurations.

**Steps**
1. Create `scripts/seed_implementation_specs.py` that:
   - For each existing agent, reads the current `AgentSpec` and `AgentDesignSpec`
   - Creates a `AgentDataSpec` with the agent's database, knowledge base, and session config
   - Creates a `AgentToolsSpec` with the agent's tools and authority boundaries
   - Creates a `AgentBehaviourSpec` with the agent's system message, model config, and response format
   - Creates a `AgentVerificationSpec` with progressive autonomy phases and health metrics
   - Sets all specs to `status="approved"` since they describe already-running agents
   - Creates an `ImplementationMap` linking everything together
2. Use the markdown renderers from Phase 3 to populate `rendered_markdown` for each spec

**Relevant files**
- `scripts/seed_implementation_specs.py` — new seed script
- `scripts/seed_infrastructure.py` — reference for seed script pattern
- `db/spec_renderers.py` — markdown rendering (from Phase 3)

**Verification**
1. Run `docker compose up -d --build` to start fresh
2. Run `python -m scripts.seed_infrastructure` to seed infrastructure
3. Run `python -m scripts.seed_implementation_specs` to seed implementation specs
4. Query each spec table and verify data exists for all 3 agents
5. Verify all specs have `status="approved"`
6. Verify ImplementationMap has correct linkages

---

## Phase 8: Integration Tests

**Goal**: End-to-end tests that verify the full pipeline from design spec → 4 implementation specs → AgentSpec assembly.

**Steps**
1. Add `pytest` and `pytest-asyncio` to `pyproject.toml` dev dependencies
2. Create `tests/` directory with `conftest.py` that sets up a test database
3. Create `tests/test_spec_pipeline.py` with these test cases:

   **Test 1: Spec CRUD operations**
   - Register each spec type, verify version=1
   - Register again, verify version=2
   - Get by version, get latest, list all

   **Test 2: Pipeline gate enforcement**
   - Attempt to create tools spec without approved data spec → verify error
   - Create data spec, submit for review, approve → verify status transitions
   - Create tools spec after data spec approved → verify success
   - Attempt to create behaviour spec without approved tools spec → verify error
   - Continue through full pipeline

   **Test 3: Markdown rendering**
   - Create a spec with sample data
   - Render markdown
   - Verify it contains expected section headers

   **Test 4: Full assembly**
   - Create and approve all 4 specs
   - Call `assemble_agent_spec()`
   - Verify AgentSpec is created
   - Verify ImplementationMap has correct linkages and populated JSONB fields

   **Test 5: Assembly rejection**
   - Create 3 approved specs and 1 draft spec
   - Call `assemble_agent_spec()` → verify ValueError

   **Test 6: ImplementationMap spec linkage**
   - Create an ImplementationMap with all 8 spec columns
   - Retrieve it and verify all columns are set correctly

4. Create `tests/test_spec_renderers.py` for unit tests of the markdown renderers

**Relevant files**
- `tests/conftest.py` — new file with test database setup
- `tests/test_spec_pipeline.py` — new file with integration tests
- `tests/test_spec_renderers.py` — new file with renderer unit tests
- `pyproject.toml` — add pytest dependencies

**Verification**
1. `pytest tests/ -v` passes all tests
2. `ruff check tests/` passes
3. `mypy tests/ --ignore-missing-imports` passes

---

## Decisions

| Decision | Rationale |
|----------|-----------|
| Application-level pipeline gates | Pipeline gates are enforced in the toolkit code, not database constraints. This allows admins to override if needed. |
| Markdown rendering stored in DB | Stored in `rendered_markdown` column on each spec, not generated on-the-fly. This allows versioning and human review without re-rendering. |
| Assembly function in db/ module | Lives in `db/spec_assembly.py`, not in the agent toolkit. The toolkit calls it. This keeps business logic testable without an agent. |
| No web UI | All interaction is CLI/agent-based, as confirmed in earlier discussion. |
| pytest with synchronous DB access | No async needed since SQLAlchemy Session is synchronous. |

## Further Considerations

1. **Should the assembly function also create the Agno Agent object?** Currently it only creates the `AgentSpec` database row. A future step could instantiate the actual Agno Agent from the spec. Recommendation: defer to a separate task — the spec row is sufficient for now.

2. **Should we add a `deprecated` status transition?** Currently specs go `draft → review → approved`. If a spec needs to be superseded, the current approach is to create a new version. A `deprecated` status could mark old versions explicitly. Recommendation: add in Phase 4 (Verification Spec) since `SpecStatusEnum` already has `deprecated`.

3. **Should the seed script also create design specs for existing agents?** The 3 existing agents have `AgentSpec` rows but may not have `AgentDesignSpec` rows. The seed script should check and create design specs if missing. Recommendation: yes, include this in the seed script.

### Response

Here's my review, organized by impact.

---

## 🔴 Critical: Will Cause Problems If Not Addressed

### 1. Phase Ordering Is Wrong — Migration Must Come First

Phase 6 (database migration) creates the columns that Phase 1 (CRUD update) writes to. If you update the CRUD code before the database has the columns, you get runtime errors when the code tries to insert data into columns that don't exist.

The model definition has the columns (Python code), but the *running database* doesn't. This is exactly the silent match failure pattern from your TypeDB work — the code says "these columns exist" but the database disagrees, and the failure happens at runtime, not at compile time.

**Fix**: Move Phase 6 before Phase 1, or more precisely: Phase 6 is a prerequisite for Phases 1, 4, 5, and 7. Everything that touches the new columns or tables needs the migration done first.

### 2. No Transaction Management in Assembly

Phase 4's `assemble_agent_spec()` creates an AgentSpec AND an ImplementationMap. If the ImplementationMap creation fails after the AgentSpec succeeds, you have an orphaned AgentSpec with no traceability. There's no rollback, no transaction wrapping, no cleanup.

**Fix**: Wrap the assembly in a database transaction. If any step fails, roll back everything. This is the "revert" primitive from your contract model — atomic success or atomic failure.

### 3. No Version Conflict Handling

The assembly function reads 4 specs and assembles them. If someone approves a new version of one spec *while the assembly is running*, you get an inconsistent AgentSpec built from a mix of old and new spec versions. No locking, no optimistic concurrency, no "read at this timestamp" isolation.

**Fix**: At minimum, the assembly function should read the exact version it validated, not "latest approved." It should lock on the version numbers, not the agent_id. If a newer version exists at assembly time, either fail with a clear message or require explicit re-validation.

### 4. Pipeline Gates Are Regime 2, Not Regime 3

You explicitly chose application-level enforcement: "Pipeline gates are enforced in the toolkit code, not database constraints." This is Regime 2 (detect and respond) — the same agent that drafts specs can bypass the gates by calling the CRUD functions directly.

You've argued repeatedly that Regime 3 (prevent by design) is the correct enforcement level. Database CHECK constraints or stored procedures would make it structurally impossible to create a tools spec without an approved data spec, regardless of how the code is called.

**Fix**: At minimum, add database-level constraints for the critical gates (can't assemble without all 4 approved). The "admin override" concern can be handled with a separate `force_assembly` function that requires explicit justification and creates an audit record — which is better than leaving the gate open for anyone who bypasses the toolkit.

---

## 🟡 CAWDP Alignment: The Methodology Isn't Applied to Itself

This is the most important category. You've built a comprehensive methodology for designing trustworthy agentic systems. This plan doesn't apply it.

### 5. No Target State Vision (Phase 0)

What does "fully functional end-to-end" actually look like? Can you describe the ideal outcome in concrete terms? Without this, you can't tell whether the pipeline is actually done or just "working."

**Fix**: Add 5-10 measurable success criteria. Example: "Given an approved design spec, the implementation spec agent produces 4 implementation specs in under 10 minutes, all pass validation, and assembly produces an AgentSpec that matches the design spec's intent on ≥80% of fields."

### 6. No Identity Specification for the Implementation Spec Agent

The agent has 10 tools but no identity. What IS it? What's its stance toward possibility? What would VIOLATE its identity? What would make it WRONG?

For a Generator-class agent drafting specs, the worst failure that looks like success is a spec that looks complete but misses critical design intent — technically correct, practically useless. This is the "valid-but-obvious" pattern from your Prospector analysis.

**Fix**: Add the 4 identity questions to the agent design before building more tools. They'll change what the agent does and how it does it.

### 7. No Verification Independence (CC-1)

The same agent that drafts specs also assembles and validates them. The test plan says "attempt to create tools spec without approved data spec → verify error" but this tests the *gate*, not the *quality*. Who checks that the drafted spec actually captures the design intent? Who verifies the assembly is correct?

**Fix**: Add a separate verification step — either a second agent (Validator class, constraint-oriented) or a structured human review checkpoint. The agent drafts; someone else verifies.

### 8. No Epistemic Metadata on Outputs (CC-3)

When the agent drafts a spec, there's no confidence level, no provenance (was this from design spec analysis, pattern matching, or user input?), no assumptions documented, no uncertainty flagged. A spec field that was inferred from a pattern looks the same as one that was explicitly stated by the user.

**Fix**: Add at minimum a `confidence` and `provenance` field to each spec section or field. This doesn't need to be per-field — a section-level confidence is a reasonable start. But "I'm 95% sure about the data schema and 40% sure about the autonomy phases" is genuinely different from "I'm 90% sure about everything."

### 9. No Information Boundaries (CC-4)

The `get_design_spec_for_agent` tool gives the agent access to the FULL design spec as JSON. No filtering, no token budget, no relevance scoring. For a small spec this might be fine, but design specs can be massive, and dumping the entire thing into context means:
- Token waste on irrelevant sections
- No prioritisation of what matters for the current spec phase
- The agent might hallucinate connections between unrelated sections

**Fix**: At minimum, add a token budget to the tool and truncate/warn if exceeded. Better: add a `sections` parameter so the agent can request only the relevant sections for the current spec phase.

### 10. No Specification Aging (CC-5)

When do these specs get reviewed? What triggers a re-review? If the design spec changes, are the implementation specs flagged as potentially stale? If the agent's actual behavior drifts from its spec, who notices?

**Fix**: Add a `last_reviewed_at` field and a `review_cadence_days` field to each spec model. When `now() - last_reviewed_at > review_cadence_days`, the spec is flagged as "due for review." Start with simple defaults: approved specs reviewed every 90 days, or whenever the linked design spec changes.

### 11. No Progressive Autonomy Plan

The implementation spec agent starts with 10 tools and full write access. There's no Shadow → Advisory → Supervised → Autonomous progression. It drafts specs from day one with no oversight.

**Fix**: Even a simple plan helps. Example: Phase 1 (Shadow) — agent drafts specs but human must approve every field. Phase 2 (Advisory) — agent drafts complete specs, human reviews before submission. Phase 3 (Supervised) — agent submits specs, human reviews before assembly. Phase 4 (Autonomous) — agent handles full pipeline, human monitors trust ledger.

---

## 🟡 Practical Improvements

### 12. Assembly Field Mapping Is Incomplete

Phase 4 lists 4 field mappings. The `AgentSpec` model likely has 15-20+ fields. What happens to the rest? Do they get default values? Are they left null? Does the assembly fail if a field can't be mapped?

**Fix**: Add a complete mapping table showing every AgentSpec field and where its value comes from (which spec field, or a default, or "requires human input").

### 13. Seed Script Creates "Approved" Specs That Might Be Wrong

Backfilling existing agents as `status="approved"` is pragmatic but risky. If the backfilled specs don't accurately describe the running agents, you've created approved-but-wrong documentation — the worst failure that looks like success.

**Fix**: Seed with `status="draft"` and require a human to review and approve each one. Or add a `backfilled` status that signals "this was generated from existing config, not from the design pipeline — verify before trusting."

### 14. No Error Recovery Architecture

What happens when the database is unavailable? When a spec is malformed? When the agent can't process the design spec? The plan has no error handling specification beyond "raises ValueError."

**Fix**: At minimum, define what happens for: (a) database connection failure, (b) spec not found, (c) spec in wrong status, (d) assembly partial failure, (e) agent can't parse design spec. For each: detection, recovery, user communication.

### 15. "Further Considerations" Are Actually Current Concerns

The `deprecated` status already exists in `SpecStatusEnum` but the pipeline doesn't handle it. Design spec creation in the seed script is recommended but not planned. These aren't future considerations — they affect the current design.

**Fix**: Either add `deprecated` handling to the pipeline now (what happens when a spec is deprecated — does it block assembly? does it trigger re-review of dependent specs?) or explicitly document it as out-of-scope with a ticket.

### 16. No Audit Trail for Approvals and Overrides (CC-8)

The spec models have `created_by` but no record of who approved, when, or why. If an admin overrides a pipeline gate, there's no trace.

**Fix**: Add an `approval_log` JSONB field or a separate audit table that records: who approved, when, what the previous status was, and any override justification.

---

## 🟢 What's Working Well

- **The "What's Already Done" table** is clear and honest about scope
- **Separating assembly logic from agent toolkit** (decisions table) is smart — business logic in `db/`, agent calls it. This makes the pipeline testable without an agent
- **Phase 8 test plan** covers the critical paths (CRUD, gates, rendering, assembly, rejection)
- **Storing rendered markdown** rather than generating on-the-fly enables versioning and human review
- **The verification sections per phase** are practical and specific (ruff, mypy, manual checks)
- **Not building a web UI** is the right call for this stage

---

## Summary: Priority Order

| Priority | Issue | Impact |
|----------|-------|--------|
| 🔴 P0 | Phase ordering — migration before CRUD | Will cause runtime failures |
| 🔴 P0 | Transaction management in assembly | Orphaned records on partial failure |
| 🔴 P0 | Version conflict handling | Inconsistent AgentSpec from mixed versions |
| 🔴 P1 | Regime 3 enforcement for critical gates | Bypassable pipeline gates undermine trust |
| 🟡 P1 | Epistemic metadata on outputs (CC-3) | Can't distinguish confident from uncertain specs |
| 🟡 P1 | Verification independence (CC-1) | Agent marks its own homework |
| 🟡 P2 | Identity specification for the agent | 10 tools without identity = no boundary enforcement |
| 🟡 P2 | Specification aging (CC-5) | Specs silently drift from reality |
| 🟡 P2 | Information boundaries (CC-4) on design spec access | Token waste, no relevance filtering |
| 🟡 P2 | Progressive autonomy plan | Full autonomy from day one |
| 🟡 P3 | Assembly field mapping completeness | Unknown gaps in spec → AgentSpec mapping |
| 🟡 P3 | Seed script "approved" risk | Wrong specs marked as trusted |
| 🟢 P4 | Error recovery architecture | Better failure handling |
| 🟢 P4 | Audit trail for approvals | CC-8 compliance |
| 🟢 P4 | `deprecated` status handling | Already in enum but not in pipeline |

The pattern I see: this is a solid *engineering* plan for building the pipeline, but it's missing the *design reasoning* that your own methodology requires. The pipeline works, but you can't trust it yet because trust infrastructure (verification independence, epistemic metadata, structural enforcement, specification aging) isn't built in.

---
