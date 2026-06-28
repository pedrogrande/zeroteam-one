# Task Contract Data Model — Implementation Report

**Date:** 2026-06-27
**Spec:** `project-docs/tasks/task-contract-data-model-v0.1.md`
**Branch:** `main`

---

## 1. What Has Been Implemented

### Overview

The full Task Contract data model (v0.1 spec) has been implemented as a **polymorphic contract store** with a hybrid persistence strategy: scalar columns for queryable fields, JSONB for the embedded aggregate, and normalised tables for actors and audit events. A complete FastAPI CRUD + state-transition API is exposed at `/api/v1/tasks` and `/api/v1/actors`, mounted alongside the existing AgentOS app via the `base_app` pattern.

### Files created

| File | Lines | Purpose |
|------|-------|---------|
| `tasks/enums.py` | 277 | 30 `StrEnum` classes for every discriminated union in the spec |
| `tasks/domain.py` | 812 | Pydantic v2 domain models: `ContractBase` + `TaskContract` + 30 supporting entities + `CONTRACT_KIND_REGISTRY` |
| `tasks/db.py` | 63 | SQLAlchemy engine/session factory, reuses `db/url.py:get_db_url()` |
| `tasks/models.py` | 149 | ORM models: `contracts` (polymorphic), `actors`, `audit_events`, `contract_versions` |
| `tasks/state_machine.py` | 97 | `VALID_TRANSITIONS` graph, `validate_transition()`, `assert_transition()` |
| `tasks/repository.py` | 698 | `ContractRepository`, `ActorRepository`, `AuditRepository` with cross-reference validation + hash chain |
| `api/schemas.py` | 178 | API request/response Pydantic models (separate from domain) |
| `api/deps.py` | 38 | FastAPI dependencies for DB session + repositories |
| `api/tasks.py` | 332 | `/tasks` router: CRUD, versioning, transitions, claims, decomposition, audit trail |
| `api/actors.py` | 95 | `/actors` router: CRUD |
| `api/router.py` | 17 | Aggregates sub-routers under `prefix="/api/v1"` |
| `tests/tasks/conftest.py` | 117 | Postgres test fixtures: session-scoped engine, per-test table lifecycle |
| `tests/tasks/test_enums.py` | 70 | Enum value coverage |
| `tests/tasks/test_domain_models.py` | 169 | Pydantic validation, serialization, registry, duplicate-role validator |
| `tests/tasks/test_state_machine.py` | 84 | Transition validation across the full state graph |
| `tests/tasks/test_api.py` | 297 | FastAPI TestClient endpoint tests (14 tests covering all endpoints) |
| **Total** | **3,636** | |

### Files modified

| File | Change |
|------|--------|
| `app/main.py` | Switched to `base_app` pattern: custom `FastAPI()` with `/api/v1` router passed as `base_app=` to `AgentOS(on_route_conflict="preserve_base_app")`. Added `init_tables()` to lifespan. |
| `pyproject.toml` | Added `tasks*` and `api*` to `[tool.setuptools.packages.find] include` |
| `compose.yaml` | Added `zeroedge-test-db` service (Postgres+pgvector on port 5433, database `task_test`) |

### API endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/tasks` | Create a task contract (version 1.0.0, status=draft) |
| GET | `/api/v1/tasks` | List tasks with filters (contract_kind, status, actor_id, parent_id) |
| GET | `/api/v1/tasks/{task_id}` | Get latest version |
| GET | `/api/v1/tasks/{task_id}/versions` | Version history |
| GET | `/api/v1/tasks/{task_id}/versions/{version}` | Specific version |
| PATCH | `/api/v1/tasks/{task_id}` | Update (creates new semver version) |
| POST | `/api/v1/tasks/{task_id}/transition` | State transition (validated via state machine) |
| POST | `/api/v1/tasks/{task_id}/claim` | Claim as performer |
| POST | `/api/v1/tasks/{task_id}/decompose` | Create child contracts with lineage |
| GET | `/api/v1/tasks/{task_id}/audit` | Audit trail with hash chain |
| POST | `/api/v1/actors` | Create actor |
| GET | `/api/v1/actors` | List actors |
| GET | `/api/v1/actors/{actor_id}` | Get actor |
| PATCH | `/api/v1/actors/{actor_id}` | Update actor trust score |

### Domain model coverage

All 15+ entities from the v0.1 spec are implemented as Pydantic models:

- `ContractBase` (shared) → `TaskContract` (task-specific)
- `Actor`, `ActorRole`, `OriginIntent`, `Jurisdiction`
- `TaskSpec` (with `Scope`, `Effort`, `ExpectedOutputs`, `Handoff`)
- `AcceptanceCriterion`, `Artefact`, `VerificationRecord`
- `ValueDeclaration` (with `ValueToRequester`, `ValueToPerformer`, `ValueToOrganisation`, `ValueToBroaderStakeholders`, `ValueVerification`)
- `Input`, `Dependency`, `Schedule` (with `Recurrence`), `Priority` (with `Allocation`)
- `Risk`, `CompensationSpec` (with `BaseCompensation`, `Incentive`, `ReputationEffects`)
- `ExecutionState` (with `ValidTransition`, `Dispute`), `AuditEvent`, `ContractLineage`
- `LearningRecord` (with `Retrospective`, `KnowledgeOutput`, `CapabilityDevelopment`)
- `Commitment`, `Ruleset`, `NotificationRule`, `QualitySpec`, `Governance`
- `CapabilityRequirements`, `VerificationSpec`

### Key features

- **Polymorphic `contracts` table** — `contract_kind` discriminator column with CHECK constraint. Adding `WorkflowContract` later requires no table migration.
- **Immutable versioning** — each edit creates a new row with a semver bump. Old versions preserved. `contract_versions` table for fast history queries.
- **Hash-chained audit trail** — each `AuditEvent.immutable_hash = SHA256(previous_hash + event_json)`. Tamper-evidence from day one.
- **Cross-reference validation** — repository validates all `actor_id` and `contract_id` references inside the JSONB document before every write, compensating for JSONB's lack of FK enforcement.
- **Duplicate role detection** — Pydantic `@field_validator` rejects duplicate `actor_id + role_type` pairs in `actor_roles`.
- **GIN index on `document`** — supports `@>` containment queries on embedded JSONB fields.
- **State machine** — 10-state graph with terminal states (completed, cancelled, expired). Invalid transitions return 422.

### Test results

```
64 passed, 2 warnings in 2.53s
```

- 45 task contract tests (8 enum, 11 domain model, 12 state machine, 14 API)
- 19 existing project tests (all still passing)
- `ruff check` — clean
- `ruff format` — clean

---

## 2. What Worked Well

### Agno `base_app` pattern

The Agno-documented `base_app` + `on_route_conflict="preserve_base_app"` pattern worked exactly as advertised. Custom `/api/v1` routes coexist cleanly with AgentOS's built-in routes (agents, sessions, workflows, etc.). No route conflicts encountered. The pattern was confirmed via Agno docs search before implementation.

### Pydantic v2 domain models

The two-layer inheritance (`ContractBase` → `TaskContract`) with `CONTRACT_KIND_REGISTRY` proved clean and extensible. The `use_enum_values=True` config means enums serialize to strings automatically in JSONB — no manual conversion. The `extra="forbid"` config caught unexpected fields during development.

### Hybrid persistence strategy

The scalar-column + JSONB-document split delivered on its promise. Queries like "list all open tasks" hit the indexed `status` column (fast), while the full contract aggregate is always available in the `document` JSONB column. The GIN index on `document` is available for future `@>` containment queries without needing expression indexes upfront.

### Cross-reference validation

The repository-level `assert_exists()` pattern for actors and contracts successfully compensates for JSONB's inability to enforce FKs inside the document. The `test_create_task_nonexistent_actor` test verifies this returns 422.

### Hash chain

The SHA-256 hash chain on audit events works correctly. The `test_audit_trail` test verifies that the second event's `previous_hash` matches the first event's `immutable_hash`.

### State machine

The `VALID_TRANSITIONS` dict is simple, readable, and testable. The `test_full_lifecycle` test walks through draft → open → claimed → in_progress → completed without errors.

### Postgres test database

Switching from SQLite to a dedicated Postgres test container (`zeroedge-test-db` on port 5433) eliminated all the column-type patching fragility. Tests now exercise the real schema — JSONB, PGUUID, GIN indexes, CHECK constraints. Per-test table lifecycle (`create_all` before, `drop_all` after) provides isolation without per-test database creation overhead.

---

## 3. Issues Encountered

### SQLite incompatibility (resolved)

The initial test implementation used SQLite with monkey-patched column types (`JSONB` → `JSON`, `PGUUID` → `String(36)`). This caused several issues:

1. **`BigInteger` autoincrement** — SQLite requires `INTEGER PRIMARY KEY` for autoincrement; `BigInteger` doesn't work. Fixed by changing `row_id` to `Integer`.
2. **DateTime string rejection** — SQLite's `DateTime` type rejects ISO 8601 strings; it expects Python `datetime` objects. Fixed by adding `_parse_dt()` in the repository.
3. **Missing `func` import** — The `list_contracts` method used `func.max()` but `func` wasn't imported. Fixed by adding it to the import.
4. **Session commit missing** — The test fixture's `_test_get_session` didn't commit after yielding, so data wasn't visible across requests. Fixed by adding `session.commit()`.

All of these were symptoms of the fundamental problem: testing Postgres-specific schema against SQLite. Switching to a real Postgres test database eliminated the entire class of issues.

### `autouse` fixture scope (current issue)

The `conftest.py` uses `@pytest.fixture(autouse=True)` for `_isolated_tables` and `_patch_engine`, which means **every** test in `tests/tasks/` — including pure-Python tests that don't touch the database (enums, domain models, state machine) — requires a running Postgres test database. If the `zeroedge-test-db` container isn't running, all 45 tests error with connection failures, not just the 14 API tests that actually need a database.

### `HTTP_422_UNPROCESSABLE_ENTITY` deprecation warning

Two tests trigger a `DeprecationWarning` from `anyio` because FastAPI's `HTTP_422_UNPROCESSABLE_ENTITY` is deprecated in favor of `HTTP_422_UNPROCESSABLE_CONTENT`. This is a Starlette/FastAPI version issue, not a code issue.

### `contract_id` required in create request

The `TaskContract` domain model requires `contract_id` as a non-optional field. The API's `create_task` endpoint sets it if missing, but the test helper `_make_task_document()` had to include it explicitly. A cleaner approach would make `contract_id` optional in the create request and auto-generate it in the repository.

---

## 4. Improvements for Future Implementations

### Fix the `autouse` fixture scope

The `autouse=True` fixtures in `tests/tasks/conftest.py` should be scoped to only the API tests that need a database. Options:

- Move the DB fixtures to `tests/tasks/test_api.py` only, or
- Use a marker (`@pytest.mark.db`) and conditionally apply the fixture, or
- Split `conftest.py` so pure-Python tests (enums, domain, state machine) don't trigger DB connection.

This would allow the 31 pure-Python tests to run without the test database container.

### Add Alembic migrations

The current implementation uses `Base.metadata.create_all()` for table creation. This is fine for development but doesn't support schema evolution. Before any production deploy, Alembic migrations should be added so schema changes can be applied incrementally without dropping data.

### Add JWT auth to custom endpoints

The `/api/v1` router is currently unauthenticated. When `RUNTIME_ENV=prd`, the AgentOS JWT middleware protects AgentOS routes but the custom `/api/v1` routes are added before the middleware. A `Depends(get_authentication_dependency(settings))` should be added to the router, matching how Agno's own routers handle auth.

### Artefact submission and verification endpoints

The API schemas (`ArtefactSubmitRequest`, `VerificationRequest`) are defined but the artefact submission and verification endpoints are not yet implemented in `api/tasks.py`. The `ArtefactRepository` exists in the repository layer but has no API surface. These should be added:

- `POST /api/v1/tasks/{task_id}/artefacts` — submit artefact
- `POST /api/v1/tasks/{task_id}/artefacts/{artefact_id}/verify` — verify artefact
- `GET /api/v1/tasks/{task_id}/dependencies` — list dependencies

### Expression indexes for hot JSONB fields

The GIN index on `document` covers general containment queries, but if specific fields become hot filters (e.g. `document->>'priority_classification'`), targeted expression indexes should be added:

```sql
CREATE INDEX ix_contracts_priority ON contracts ((document->>'priority_classification'));
```

Defer until profiling shows the need.

### Semver bump strategy refinement

The current `version_bump` parameter accepts `"patch"`, `"minor"`, or `"major"` but defaults to `"patch"` for all updates. A smarter strategy would auto-detect the bump level based on what changed:

- Status change → patch
- Scope change (inclusions/exclusions) → minor
- Contract type or compensation change → major

### Agent integration (future phase)

The plan called for API-only in this phase. A future phase should give agents (project_manager, technical_lead) tools to create, query, and transition task contracts. This would make agents active participants in the task contract lifecycle — creating tasks from conversations, updating status as work progresses, and decomposing complex tasks into children.

### `WorkflowContract` addition (future phase)

The polymorphic `contracts` table is designed for this. Adding `WorkflowContract(ContractBase)` requires:

1. New Pydantic model in `tasks/domain.py`
2. `ContractKind.workflow` enum value in `tasks/enums.py`
3. Register in `CONTRACT_KIND_REGISTRY`
4. New `api/workflows.py` router at `/workflows`

No table migration, no new tables. The `contracts`, `actors`, and `audit_events` tables are shared.

### Transaction-based test isolation

Instead of `create_all` / `drop_all` per test, consider using a transaction-per-test pattern: begin a transaction at the start of each test, roll back at the end. This is faster (no DDL per test) and provides stronger isolation. The challenge is that FastAPI's TestClient manages its own sessions, so the test transaction would need to be nested or the session factory patched to share the test transaction.

### API response pagination

The `list_contracts` repository method accepts `limit` and `offset`, but the `TaskListResponse` returns `total` as `len(items)` rather than the actual total count. A proper `SELECT COUNT(*)` query should be added for accurate pagination metadata.

### OpenAPI documentation enrichment

The FastAPI endpoints have minimal docstrings. Adding `summary`, `description`, and `response_model` examples to each endpoint would improve the auto-generated OpenAPI docs at `/docs`.

---

## 5. Architecture Summary

```
app/main.py  (AgentOS with base_app=custom FastAPI app)
├── api/
│   ├── router.py          — APIRouter(prefix="/api/v1")
│   ├── deps.py             — DB session + repository dependencies
│   ├── tasks.py            — /tasks router (CRUD, versioning, transitions, claims, decomposition, audit)
│   ├── actors.py           — /actors router (CRUD)
│   └── schemas.py          — API request/response models
├── tasks/
│   ├── enums.py            — 30 StrEnum classes
│   ├── domain.py           — ContractBase + TaskContract + 30 entities + CONTRACT_KIND_REGISTRY
│   ├── db.py               — SQLAlchemy engine/session factory
│   ├── models.py           — ORM: contracts, actors, audit_events, contract_versions
│   ├── repository.py        — ContractRepository, ActorRepository, AuditRepository
│   └── state_machine.py    — VALID_TRANSITIONS + validate_transition()
├── tests/tasks/
│   ├── conftest.py         — Postgres test fixtures (session-scoped engine, per-test tables)
│   ├── test_enums.py       — 8 tests
│   ├── test_domain_models.py — 11 tests
│   ├── test_state_machine.py — 12 tests
│   └── test_api.py         — 14 tests
└── compose.yaml            — zeroedge-test-db service (port 5433)
```
