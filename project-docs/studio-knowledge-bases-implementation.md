# Implementation Report: Studio Knowledge Bases via AgentOS Registry

**Date:** 2026-06-27
**Status:** Complete — all tests passing, lint clean, docs updated.
**Scope:** Register five domain knowledge bases with the AgentOS Studio Registry so they're selectable when building agents, teams, and workflows in Studio. No changes to hard-coded agents or teams.

---

## What was built

Five domain knowledge bases, each backed by PgVector (hybrid search) + OpenAI `text-embedding-3-small` embeddings + a `contents_db` (required for Studio resolution) + a pre-seeded `PDFReader` using `AgenticChunking`:

| Knowledge base | Table | Contents table | Domain |
|----------------|-------|----------------|--------|
| AI Assisted Learning | `ai_assisted_learning` | `ai_assisted_learning_contents` | Research & practice for AI-accelerated learning |
| Agent Design | `agent_design` | `agent_design_contents` | Patterns for designing agents — instructions, tools, guardrails |
| Agentic Workflow Design | `agentic_workflow_design` | `agentic_workflow_design_contents` | Multi-step pipeline patterns — loops, conditions, HITL |
| User Profile Information | `user_profile_information` | `user_profile_information_contents` | User-specific context for personalisation |
| AgentOS Lab | `agentos_lab` | `agentos_lab_contents` | Operational knowledge for the AgentOS platform |

They are registered with Studio by passing `knowledge=STUDIO_KNOWLEDGE_BASES` to `AgentOS(...)` in `app/main.py`. AgentOS auto-discovers them and mirrors them into its internal Registry — no explicit `Registry(...)` construction required.

---

## Files changed

| File | Change |
|------|--------|
| `db/session.py` | Added `create_studio_knowledge(name, table_name, description)` factory. New imports: `AgenticChunking`, `PDFReader`, `Optional`. |
| `db/__init__.py` | Exported `create_studio_knowledge` in `__all__` and the re-export line. |
| `db/knowledge_bases.py` (new) | Instantiates the five domain KBs; exposes `STUDIO_KNOWLEDGE_BASES: list[Knowledge]`. |
| `app/main.py` | Imported `STUDIO_KNOWLEDGE_BASES`; passed `knowledge=STUDIO_KNOWLEDGE_BASES` to `AgentOS(...)`. |
| `AGENTS.md` | Added "Studio Knowledge Bases" subsection + `db/knowledge_bases.py` to Key Files. |
| `tests/test_db_session.py` | Added tests for `create_studio_knowledge()` (shape + no-OpenAI-key guard). |
| `tests/test_knowledge_bases.py` (new) | Tests for the 5 KBs: unique names, expected domains, agentic PDF reader, no-key guard. |

---

## How it works

### 1. The factory — `create_studio_knowledge()`

Located in `db/session.py`. Wraps the existing `create_knowledge()` (which builds the PgVector + OpenAI embedder + `contents_db` shape) and adds two Studio-specific things:

```python
def create_studio_knowledge(name, table_name, description=None) -> Knowledge:
    knowledge = create_knowledge(name=name, table_name=table_name)
    knowledge.description = description  # surfaced in Studio's KB picker
    # Pre-seed a PDFReader with AgenticChunking under the "pdf" key
    if knowledge.readers is None:
        knowledge.readers = {}
    knowledge.readers["pdf"] = PDFReader(
        name="Agentic Chunking PDF Reader",
        chunking_strategy=AgenticChunking(),
    )
    return knowledge
```

### 2. The domain KBs — `db/knowledge_bases.py`

Five module-level `Knowledge` instances, each with a `name`, `table_name`, and `description`. Collected into `STUDIO_KNOWLEDGE_BASES`.

### 3. Registration — `app/main.py`

```python
from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES

agent_os = AgentOS(
    ...
    knowledge=STUDIO_KNOWLEDGE_BASES,
    ...
)
```

AgentOS's `_auto_discover_knowledge_instances()` collects KBs from `AgentOS.knowledge`, and `_populate_registry_knowledge()` mirrors them into `self.registry.knowledge` by unique `name`.

---

## Key decisions

### `AgentOS(knowledge=...)` over explicit `Registry(...)`

The example in `project-docs/example-knowledge-agentos.py.md` builds an explicit `Registry(knowledge=[...])` and passes `registry=...`. We chose `AgentOS(knowledge=...)` instead because:

- It's simpler — one less object to construct and keep in sync.
- AgentOS auto-creates an internal `Registry` and mirrors the KBs in via `_populate_registry_knowledge()` (verified at `agno/source/agno/os/app.py:674`).
- Functionally equivalent for the knowledge-only case.

Switch to an explicit `Registry(...)` only if you want to co-locate other registry components (tools, models, schemas, memory managers) alongside the KBs.

### `contents_db` is mandatory for Studio

Confirmed in the Agno source (`agno/source/agno/os/app.py:680`):

> *"a `contents_db` is required for a knowledge base to be resolvable from a Studio/Builder component config (vector-search-only knowledge is not registered)."*

`_auto_discover_knowledge_instances()` (app.py:1310) skips any KB without a `contents_db`. The existing `create_knowledge()` already wires one in via `get_postgres_db(contents_table=f"{table_name}_contents")`, so `create_studio_knowledge()` inherits this for free.

### Agentic chunking injection via `readers["pdf"]` (the gotcha)

This is the most important implementation detail. **`Knowledge.add_reader(reader)` does NOT store the reader under the `"pdf"` key** — it derives the key from `reader.name` (lowercased, spaces→underscores) via `_generate_reader_key`. So:

```python
# WRONG — stores under "agentic_chunking_pdf_reader", not "pdf"
knowledge.add_reader(PDFReader(name="Agentic Chunking PDF Reader", ...))
```

But `Knowledge.pdf_reader` → `_get_reader("pdf")` looks up the **literal** `"pdf"` key. If it misses, it falls back to `ReaderFactory.create_reader("pdf")`, which returns a `PDFReader` with the default `DocumentChunking` — silently undoing the agentic chunking requirement.

**Fix:** assign the dict entry directly:

```python
knowledge.readers["pdf"] = PDFReader(chunking_strategy=AgenticChunking())
```

This guarantees Studio-initiated PDF uploads hit the agentic-chunking reader.

### `AgenticChunking` model

Left as the default (`OpenAIChat` with `DEFAULT_OPENAI_MODEL_ID`) — uses OpenAI credits for breakpoint detection. `OPENAI_API_KEY` is already required for embeddings, so no new env var. Could be overridden to `default_model()` (Ollama `glm-5.2:cloud`) later if cost/latency matters.

### Scope exclusions

- No `knowledge=` added to hard-coded agents (`web_search`, `code_search`, `agno_support_agent`, `project_manager`, `technical_lead`) or `engineering_team`.
- No seed content loaded at boot — content is uploaded via Studio.

---

## Verification

### Unit tests

```bash
OPENAI_API_KEY=sk-test python -m pytest tests/test_db_session.py tests/test_knowledge_bases.py -v
```

Result: **10 passed**. The full suite (`pytest tests/`) is **70 passed**.

Tests cover:

- `create_studio_knowledge()` returns a `Knowledge` with `contents_db`, `PgVector`/`SearchType.hybrid`, and `readers["pdf"]` is a `PDFReader` with `AgenticChunking`.
- `create_studio_knowledge()` raises `RuntimeError` when `OPENAI_API_KEY` is unset.
- `STUDIO_KNOWLEDGE_BASES` has 5 instances with unique names, expected domain names, each with an agentic PDF reader, and raises without `OPENAI_API_KEY`.

### Lint & types

```bash
ruff check db/session.py db/__init__.py db/knowledge_bases.py app/main.py tests/test_db_session.py tests/test_knowledge_bases.py
# All checks passed!

mypy db/session.py db/__init__.py db/knowledge_bases.py app/main.py tests/test_db_session.py tests/test_knowledge_bases.py --config-file pyproject.toml
# No errors in the touched files. (16 pre-existing errors in tasks/repository.py, api/deps.py, api/tasks.py — untouched.)
```

### Import smoke test

```bash
OPENAI_API_KEY=sk-test python -c "from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES; print(len(STUDIO_KNOWLEDGE_BASES), [kb.name for kb in STUDIO_KNOWLEDGE_BASES])"
# 5 ['AI Assisted Learning', 'Agent Design', 'Agentic Workflow Design', 'User Profile Information', 'AgentOS Lab']
```

### Runtime verification (next step — requires Docker)

```bash
docker compose up -d --build
curl -s http://localhost:8000/registry?component_type=knowledge | jq   # expect 5 entries
```

Then open Studio (`http://localhost:8000`) → create an agent → Knowledge picker shows all five. Upload a PDF to one KB via the Knowledge UI → confirm status reaches ready → a search returns hits.

### Dependency note

`pypdf` must be installed in the host venv for `PDFReader` to import. The Docker image already includes it via `requirements.txt`; the host venv needed:

```bash
VIRTUAL_ENV="$PWD/.venv" uv pip install pypdf
```

---

## Guide: How to add a new Studio knowledge base

Follow this recipe when you need to register a new domain knowledge base for Studio-composed agents, teams, and workflows.

### Step 1 — Add the KB instance

Open `db/knowledge_bases.py` and add a new module-level instance, then append it to `STUDIO_KNOWLEDGE_BASES`:

```python
my_new_domain_kb: Knowledge = create_studio_knowledge(
    name="My New Domain",                 # shown in Studio's KB picker
    table_name="my_new_domain",           # snake_case; vectors land here
    description=(
        "What this KB covers — one or two sentences. "
        "Shown under the name in Studio."
    ),
)

STUDIO_KNOWLEDGE_BASES: list[Knowledge] = [
    ai_assisted_learning_kb,
    agent_design_kb,
    agentic_workflow_design_kb,
    user_profile_information_kb,
    agentos_lab_kb,
    my_new_domain_kb,                     # <-- add here
]
```

**Naming rules:**

- `name` must be unique across all KBs (AgentOS validates this at boot via `_validate_knowledge_instance_names` — duplicates raise `Duplicate knowledge instances detected`).
- `table_name` must be a unique snake_case slug. The contents table is auto-derived as `{table_name}_contents`.

That's it for code. No changes to `app/main.py` — it already passes `STUDIO_KNOWLEDGE_BASES`, and the list picks up the new entry automatically.

### Step 2 — Add a test

Open `tests/test_knowledge_bases.py` and update the count + expected-names assertions:

```python
def test_studio_knowledge_bases_has_five_unique_instances():
    # bump to 6
    assert len(STUDIO_KNOWLEDGE_BASES) == 6
    ...

def test_studio_knowledge_bases_expected_names():
    names = {kb.name for kb in STUDIO_KNOWLEDGE_BASES}
    assert names == {
        "AI Assisted Learning",
        "Agent Design",
        "Agentic Workflow Design",
        "User Profile Information",
        "AgentOS Lab",
        "My New Domain",                    # <-- add here
    }
```

The `test_studio_knowledge_bases_each_has_agentic_pdf_reader` test iterates over all KBs automatically, so it covers the new one with no changes.

### Step 3 — Run the tests

```bash
OPENAI_API_KEY=sk-test python -m pytest tests/test_knowledge_bases.py -v
```

### Step 4 — Restart the API

```bash
docker compose restart zeroedge-api
```

Uvicorn hot-reload is unreliable for newly-registered module-level objects, so a restart is required for the new KB to load.

### Step 5 — Verify in Studio

```bash
curl -s http://localhost:8000/registry?component_type=knowledge | jq
```

Expect the new KB in the list. Then open Studio → create an agent → the Knowledge picker should show "My New Domain".

### Step 6 — Upload content

Upload via the Studio Knowledge UI, or via the API:

```bash
curl -X POST http://localhost:8000/knowledge/My%20New%20Domain/content \
  -F "file=@path/to/document.pdf"
```

The pre-seeded `PDFReader(chunking_strategy=AgenticChunking())` chunks the PDF semantically before embedding.

---

## Guide: Customising a knowledge base

### Different chunking strategy

If a KB needs a different chunking strategy (e.g. `SemanticChunking` for code-heavy docs), either:

**Option A — per-KB override** (preferred for one-offs): don't use `create_studio_knowledge()`; build the `Knowledge` directly with a custom reader:

```python
from agno.knowledge.chunking.semantic import SemanticChunking
from db.session import create_knowledge

my_kb = create_knowledge(name="Code KB", table_name="code_kb")
my_kb.description = "Code snippets and patterns."
if my_kb.readers is None:
    my_kb.readers = {}
my_kb.readers["pdf"] = PDFReader(chunking_strategy=SemanticChunking(embedder=OpenAIEmbedder(id="text-embedding-3-small")))
```

**Option B — extend the factory** (preferred if multiple KBs share the strategy): add a `chunking_strategy` parameter to `create_studio_knowledge()`.

### Different embedder

Set `EMBEDDER_MODEL_ID` in `.env` to override the default `text-embedding-3-small` for all KBs. For a per-KB embedder, build the `Knowledge` directly and pass `embedder=` to `PgVector`.

### Different vector DB

`create_studio_knowledge()` is PgVector-specific. For a different vector store (LanceDB, Qdrant, etc.), build the `Knowledge` directly with the relevant `VectorDb` instance — but keep the `contents_db=` argument, since Studio resolution still requires it.

### Using the KB in a hard-coded agent

This setup deliberately excludes hard-coded agents. To attach a Studio KB to a code-defined agent, import it and pass `knowledge=`:

```python
from db.knowledge_bases import agent_design_kb

my_agent = Agent(
    ...
    knowledge=agent_design_kb,
    search_knowledge=True,
)
```

Note: this also makes the KB's `contents_db` count toward the agent's DB connections.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| KB doesn't appear in Studio picker | Missing `contents_db` | Use `create_studio_knowledge()` or ensure `contents_db=` is set on the `Knowledge`. |
| Boot fails with `Duplicate knowledge instances detected` | Two KBs share a `name` | Give each KB a unique `name`. |
| PDFs chunk with fixed-size, not agentic | Reader stored under wrong key | Assign `knowledge.readers["pdf"]` directly, not via `add_reader()`. |
| `ImportError: pypdf not installed` | Host venv missing `pypdf` | `VIRTUAL_ENV="$PWD/.venv" uv pip install pypdf` (Docker image already has it). |
| `RuntimeError: OPENAI_API_KEY is not set` | Embedder needs the key | Set `OPENAI_API_KEY` in `.env`. |
| New KB not visible after edit | Uvicorn didn't reload module-level objects | `docker compose restart zeroedge-api`. |

---

## Reference

- Agno Registry docs: <https://docs.agno.com/agent-os/studio/registry>
- Agno contents_db docs: <https://docs.agno.com/knowledge/concepts/contents-db>
- Agno readers overview: <https://docs.agno.com/knowledge/concepts/readers/overview>
- Agno agentic chunking: <https://docs.agno.com/knowledge/concepts/chunking/agentic-chunking>
- Agno PgVector: <https://docs.agno.com/knowledge/vector-stores/pgvector/overview>
- Source verification: `agno/source/agno/os/app.py` (`_auto_discover_knowledge_instances` at line 1302, `_populate_registry_knowledge` at line 674), `agno/source/agno/knowledge/knowledge.py` (`_get_reader` at line 938, `_generate_reader_key` at line 916).
