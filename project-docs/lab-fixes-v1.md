# Coding Agent Guide: Fixing Architecture Risks in the Agno AgentOS Lab

## Scope & Exclusions

This guide addresses **all non-cloud, non-production risks** from the architecture review. The following risks are **excluded** per your instructions:

| Excluded | Reason |
|----------|--------|
| R-01 (default DB creds) | Cloud/production concern |
| R-08 (Slack user auth) | Production-specific |
| R-26 (`AGNO_DEBUG=True`) | Dev-only logging |
| R-28 (JWT default behavior) | Production auth |

All remaining risks are addressed below. **Every Agno API suggestion has been validated against the official Agno docs** by the Agno Support Agent.

---

## Quick Reference: Validated Agno APIs

Before starting, here are the **correct, docs-verified import paths and patterns** the guide relies on:

```python
# ✅ Correct guardrail imports (from package level, NOT submodules)
from agno.guardrails import PromptInjectionGuardrail
from agno.guardrails import PIIDetectionGuardrail    # NOT "PIIGuardrail"
from agno.guardrails import OpenAIModerationGuardrail
from agno.guardrails import BaseGuardrail            # or: from agno.guardrails.base import BaseGuardrail

# ✅ Guardrails go in pre_hooks (input validation)
agent = Agent(pre_hooks=[PromptInjectionGuardrail()], ...)

# ✅ Output validation uses plain functions in post_hooks (NOT BaseGuardrail)
# post_hook functions receive RunOutput with .content, .tools, .messages
agent = Agent(post_hooks=[my_output_validator], ...)

# ✅ tool_call_limit caps total tool calls per run
agent = Agent(tool_call_limit=10, ...)

# ✅ PostgresDb: single shared instance recommended for shared sessions
db = PostgresDb(db_url=db_url)  # pass same instance to multiple agents
```

> ⚠️ **Key correction:** `BaseGuardrail.check()` receives `RunInput` (for input validation only). It does **not** receive `RunOutput`. For output validation, use **plain functions** in `post_hooks` that receive `RunOutput`.

> ⚠️ **PII detection checks user input, not external content.** `PIIDetectionGuardrail` runs in `pre_hooks` and inspects the user's message — not tool results or fetched web pages. The rationale for `enable_pii=False` on sub-agents is that they receive **delegated input** (already filtered by the team leader), not raw user input. The team leader (user-facing entry point) should have PII detection enabled. If the team has a `LearningMachine` capturing user profiles, consider `mask_pii=True` to mask rather than block PII.

---

## Phase 1: Critical Fixes (High Severity)

### Fix 1.1 — Compose Service Name Mismatch (R-21, R-50)

**File:** `.devcontainer/compose.override.yaml`
**Risk:** The override references `zeroteam-api` and `zeroteam-db`, but `compose.yaml` defines `zeroedge-api` and `zeroedge-db`. Docker Compose treats the override entries as new empty services. The dev container will fail on startup.

**Instructions for coding agent:**

1. Open `.devcontainer/compose.override.yaml`
2. Replace all occurrences of `zeroteam-api` with `zeroedge-api`
3. Replace all occurrences of `zeroteam-db` with `zeroedge-db`
4. Verify the final file looks like this:

```yaml
services:
  devcontainer:
    build:
      context: ..
      dockerfile: Dockerfile
    command: /bin/sh -c "while sleep 1000; do :; done"
    depends_on:
      - zeroedge-api          # ← was zeroteam-api
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OLLAMA_API_KEY=${OLLAMA_API_KEY}
    volumes:
      - ..:/workspace:cached

  zeroedge-api:                # ← was zeroteam-api
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OLLAMA_API_KEY=${OLLAMA_API_KEY}

  zeroedge-db:                 # ← was zeroteam-db
    ports:
      - "5432:5432"
```

1. Validate: run `docker compose -f compose.yaml -f .devcontainer/compose.override.yaml config` and confirm the services merge correctly (no duplicate/empty services).

---

### Fix 1.2 — Enrich Existing `example.env` with Missing Variables (R-22)

**File:** `example.env` (already exists at repo root)
**Risk:** The existing `example.env` is missing `DB_DRIVER`, `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASS`, `DB_DATABASE`, and `RUNTIME_ENV` entries. New users copying it to `.env` won't have database defaults documented. (`postCreateCommand` works fine — `example.env` already exists.)

**Instructions for coding agent:**

1. Open the existing `example.env` and **merge** the following entries (do not overwrite the file — it has better JWT documentation than the template below). Add any missing keys:

```env
# ============================================================
# Agno AgentOS Lab — Environment Configuration Template
# ============================================================
# Copy this file to .env and fill in your values:
#   cp example.env .env
# ============================================================

# --- Required ---
# OpenAI API key for models + embeddings
OPENAI_API_KEY=sk-your-key-here

# --- Optional: Local model (Ollama) ---
# OLLAMA_API_KEY=your-ollama-key

# --- Optional: Parallel SDK for WebSearch ---
# PARALLEL_API_KEY=your-parallel-key

# --- Database (defaults shown — change for non-local setups) ---
DB_DRIVER=postgresql+psycopg
DB_HOST=localhost
DB_PORT=5432
DB_USER=ai
DB_PASS=ai
DB_DATABASE=ai

# --- Runtime ---
RUNTIME_ENV=dev
AGENTOS_URL=http://127.0.0.1:8000

# --- Slack (optional — both must be set to enable) ---
# SLACK_BOT_TOKEN=xoxb-your-token
# SLACK_SIGNING_SECRET=your-signing-secret

# --- Embedder (optional override) ---
# EMBEDDER_MODEL_ID=text-embedding-3-small
# AGENT_MODEL_ID=glm-5.1:cloud
```

1. Add `example.env` to `.dockerignore` (it should NOT be in the Docker image):
   - Open `.dockerignore` and add the line `example.env`

2. Do **NOT** add `example.env` to `.gitignore` — it should be committed as a template.

3. Verify: run `cp -n example.env .env && cat .env` to confirm the copy works (the `-n` flag matches the existing `postCreateCommand`).

---

### Fix 1.3 — Missing `dockerize` in Docker Image (R-13)

**File:** `scripts/entrypoint.sh` (lines 25-29) and `Dockerfile`
**Risk:** `WAIT_FOR_DB=True` (set in `compose.yaml`) triggers `dockerize`, which is not installed. The entrypoint will fail with `dockerize: command not found`.

**Instructions for coding agent:**

1. Open `scripts/entrypoint.sh` and replace the `dockerize` wait block with a pure-bash wait loop. Replace this section:

```bash
if [[ "$WAIT_FOR_DB" = true || "$WAIT_FOR_DB" = True ]]; then
    echo -e "    ${DIM}Waiting for database at ${DB_HOST}:${DB_PORT}...${NC}"
    dockerize -wait tcp://$DB_HOST:$DB_PORT -timeout 300s
    echo -e "    ${BOLD}Database ready.${NC}"
    echo ""
fi
```

With a Python-based wait loop (the base image `agnohq/python:3.12` already has Python — no new system package needed):

```bash
if [[ "$WAIT_FOR_DB" = true || "$WAIT_FOR_DB" = True ]]; then
    echo -e "    ${DIM}Waiting for database at ${DB_HOST}:${DB_PORT}...${NC}"
    python -c "
import socket, sys, time
deadline = time.time() + 300
while time.time() < deadline:
    try:
        socket.create_connection(('${DB_HOST}', ${DB_PORT}), timeout=2).close()
        break
    except OSError:
        time.sleep(1)
else:
    sys.exit('Timed out waiting for database after 300s')
"
    echo -e "    ${BOLD}Database ready.${NC}"
    echo ""
fi
```

> **Why not `nc`/`netcat-openbsd`?** Adding a system package to the Docker image increases image size and requires a Dockerfile change. Python is already available in the base image (`agnohq/python:3.12`), so a `socket.create_connection` one-liner achieves the same result with zero new dependencies.

1. **No Dockerfile changes needed.** Verify: rebuild the image and run `docker compose up` — confirm the wait-for-db loop works.

---

### Fix 1.4 — Add Guardrails to All Agents (R-19, R-03, R-14, R-15)

This is the most significant fix for a lab focused on **responsible agentic AI**. None of the three agents or the team currently have `pre_hooks` or `post_hooks` configured.

**Validated Agno APIs (confirmed by Agno Support Agent):**

- `from agno.guardrails import PromptInjectionGuardrail`
- `from agno.guardrails import PIIDetectionGuardrail`
- `from agno.guardrails import OpenAIModerationGuardrail`
- `pre_hooks=[guardrail_instance]` — runs before agent processes input
- `post_hooks=[plain_function]` — runs after output is generated; function receives `RunOutput` with `.content`, `.tools`, `.messages`

#### Fix 1.4a — Create a shared guardrails module

**Instructions for coding agent:**

1. Create a new file `app/guardrails.py`:

```python
"""
Guardrails
==========

Shared guardrail and post-hook definitions for all agents.
Supports the lab's "responsible agentic AI" mandate by enforcing
input safety (prompt injection, PII, moderation) and output
integrity (citation grounding, file-path verification).
"""

from __future__ import annotations

import re
from pathlib import Path

from agno.exceptions import InputCheckError, OutputCheckError, CheckTrigger
from agno.guardrails import PromptInjectionGuardrail, PIIDetectionGuardrail
from agno.run.agent import RunOutput


# ---------------------------------------------------------------------------
# Pre-hook guardrails (input validation)
# ---------------------------------------------------------------------------

def default_pre_hooks(*, enable_pii: bool = True) -> list:
    """Return a list of pre-hook guardrails for input validation.

    Args:
        enable_pii: If True, include PIIDetectionGuardrail.
    """
    hooks = [PromptInjectionGuardrail()]
    if enable_pii:
        hooks.append(PIIDetectionGuardrail(mask_pii=False))
    return hooks


# ---------------------------------------------------------------------------
# Post-hook validators (output validation — plain functions, NOT BaseGuardrail)
# ---------------------------------------------------------------------------

def validate_citations_from_tools(run_output: RunOutput) -> None:
    """Post-hook: ensure any URL cited in the response appeared in tool results.

    Prevents the agent from hallucinating sources that were never fetched.
    Raises OutputCheckError if cited URLs are not grounded in tool output.
    """
    response_content = str(run_output.content or "")

    # Collect all URLs from tool execution results
    tool_urls: set[str] = set()
    if run_output.tools:
        for tool_exec in run_output.tools:
            result_str = str(getattr(tool_exec, "result", "") or "")
            tool_urls.update(re.findall(r'https?://[^\s"\'<>]+', result_str))

    # Find all URLs cited in the response
    cited_urls: set[str] = set(re.findall(r'https?://[^\s"\'<>]+', response_content))

    unverified = cited_urls - tool_urls
    if unverified:
        raise OutputCheckError(
            f"Response cites URLs not found in tool results: {unverified}",
            check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
        )


def validate_file_paths_exist(run_output: RunOutput, workspace_root: Path) -> None:
    """Post-hook: ensure file paths cited in the response actually exist.

    Prevents the CodeSearch agent from fabricating file paths.
    Note: this is a factory — call it with your workspace root to get
    a closure suitable for post_hooks.
    """
    # This is used as a factory; see make_file_path_validator below.
    pass


def make_file_path_validator(workspace_root: Path):
    """Create a post-hook function bound to a specific workspace root.

    Usage:
        post_hooks=[make_file_path_validator(Path("/app"))]
    """
    def _validator(run_output: RunOutput) -> None:
        response_content = str(run_output.content or "")

        # Find all backtick-quoted paths in the response (e.g. `app/main.py`)
        cited_paths = re.findall(r'`([^`]+\.\w+)`', response_content)

        missing: list[str] = []
        for cited in cited_paths:
            # Skip URLs and non-path strings
            if cited.startswith("http") or "/" not in cited and "\\" not in cited:
                continue
            candidate = workspace_root / cited
            if not candidate.exists():
                missing.append(cited)

        if missing:
            raise OutputCheckError(
                f"Response cites file paths that do not exist in the workspace: {missing}",
                check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
            )

    return _validator
```

> **Docs note:** `OutputCheckError` and `CheckTrigger` are from `agno.exceptions`. `RunOutput` is from `agno.run.agent`. These are confirmed by the Agno docs ([/reference/hooks/post-hooks](https://docs.agno.com/reference/hooks/post-hooks), [/guardrails/overview](https://docs.agno.com/guardrails/overview)).

> ⚠️ **Validate `RunOutput.tools` structure before relying on `validate_citations_from_tools`.** The post-hook accesses `run_output.tools` and `getattr(tool_exec, "result", "")`. If the actual attribute names differ (e.g., `tool_calls` instead of `tools`, or a different result field), the validator will silently collect an empty `tool_urls` set — meaning `cited_urls - tool_urls` = all cited URLs → raises on every response containing URLs. Before production use, add a quick smoke test that prints `dir(run_output)` and the structure of a tool execution object from a real run.

1. Verify the imports work: run `python -c "from app.guardrails import default_pre_hooks, validate_citations_from_tools, make_file_path_validator"`

#### Fix 1.4b — Add guardrails to the WebSearch agent

**File:** `agents/web_search.py`

**Instructions:**

1. Add import at the top:

```python
from app.guardrails import default_pre_hooks, validate_citations_from_tools
```

1. Add `pre_hooks` and `post_hooks` to the Agent constructor:

```python
web_search = Agent(
    # ... existing parameters ...
    pre_hooks=default_pre_hooks(enable_pii=False),  # sub-agent: receives delegated input, not raw user input
    post_hooks=[validate_citations_from_tools],      # ensure cited URLs came from tools
    tool_call_limit=10,                               # see Fix 2.1 below
)
```

#### Fix 1.4c — Add guardrails to the CodeSearch agent

**File:** `agents/code_search.py`

**Instructions:**

1. Add imports:

```python
from pathlib import Path
from app.guardrails import default_pre_hooks, make_file_path_validator

REPO_ROOT = Path(__file__).resolve().parents[1]
```

1. Add `pre_hooks` and `post_hooks`:

```python
code_search = Agent(
    # ... existing parameters ...
    pre_hooks=default_pre_hooks(enable_pii=False),
    post_hooks=[make_file_path_validator(REPO_ROOT)],
    tool_call_limit=10,
)
```

#### Fix 1.4d — Add guardrails to the Agno Support agent

**File:** `agents/agno_support.py`

**Instructions:**

1. Add import:

```python
from app.guardrails import default_pre_hooks
```

1. Add `pre_hooks`:

```python
agno_support_agent = Agent(
    # ... existing parameters ...
    pre_hooks=default_pre_hooks(enable_pii=False),
    tool_call_limit=10,
)
```

#### Fix 1.4e — Add guardrails to the Engineering Team

**File:** `teams/engineering_team.py`

**Instructions:**

1. Add import:

```python
from app.guardrails import default_pre_hooks
```

1. Add `pre_hooks` to the `Team` constructor (the variable is `engineering_team`, a `Team` instance — **not** an `Agent`). The `Team` class accepts `pre_hooks` natively:

```python
engineering_team = Team(
    # ... existing parameters ...
    pre_hooks=default_pre_hooks(enable_pii=True),  # PII on for user-facing team
)
```

> ⚠️ **LearningMachine conflict:** The team has `LearningMachine(user_profile=LearningMode.ALWAYS, user_memory=LearningMode.ALWAYS)` which captures user profile info — this often includes PII (names, emails). With `PIIDetectionGuardrail(mask_pii=False)` (the default), PII in user input **raises `InputCheckError` and blocks the run**. Consider using `PIIDetectionGuardrail(mask_pii=True)` for the team so PII is masked rather than blocked, allowing the learning machine to capture sanitized profile data:
>
> ```python
> pre_hooks=default_pre_hooks(enable_pii=True),  # see note above re: mask_pii
> ```
>
> If you want masking, update `default_pre_hooks` to accept a `mask_pii` parameter or construct the guardrail inline here.

---

### Fix 1.5 — Add Basic Application Tests (R-42)

**Risk:** Zero unit tests for the application layer.

**Instructions for coding agent:**

1. Create a `tests/` directory at the repo root:

```
tests/
├── __init__.py
├── conftest.py
├── test_db_url.py
├── test_db_session.py
├── test_agents_init.py
└── test_guardrails.py
```

1. **`tests/conftest.py`** — shared fixtures:

```python
"""Shared test fixtures."""
import os
import pytest


@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    """Ensure test env vars are set before any imports."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_USER", "test")
    monkeypatch.setenv("DB_PASS", "test")
    monkeypatch.setenv("DB_DATABASE", "test")
```

1. **`tests/test_db_url.py`** — unit tests for `db/url.py`:

```python
"""Tests for db/url.py — URL construction from env vars."""
import os
from unittest.mock import patch
from urllib.parse import quote


def test_build_db_url_with_defaults():
    """Test URL construction with default values when env vars are unset."""
    from db.url import build_db_url
    with patch.dict(os.environ, {}, clear=True):
        url = build_db_url()
        assert "postgresql+psycopg" in url
        assert "ai:ai" in url
        assert "localhost" in url
        assert "5432" in url
        assert url.endswith("/ai")


def test_build_db_url_with_custom_values():
    """Test URL construction with custom env vars."""
    from db.url import build_db_url
    with patch.dict(os.environ, {
        "DB_DRIVER": "postgresql+asyncpg",
        "DB_USER": "myuser",
        "DB_PASS": "p@ss w0rd",
        "DB_HOST": "db.example.com",
        "DB_PORT": "6543",
        "DB_DATABASE": "mydb",
    }):
        url = build_db_url()
        assert url == f"postgresql+asyncpg://myuser:{quote('p@ss w0rd')}@db.example.com:6543/mydb"


def test_build_db_url_password_is_url_encoded():
    """Test that special characters in password are URL-encoded."""
    from db.url import build_db_url
    with patch.dict(os.environ, {"DB_PASS": "p@ss/w0rd"}):
        url = build_db_url()
        # The password should be percent-encoded
        assert quote("p@ss/w0rd") in url
        assert "p@ss/w0rd" not in url.split("@")[0].split(":")[-1]  # raw password not in URL
```

1. **`tests/test_db_session.py`** — unit tests for `db/session.py`:

```python
"""Tests for db/session.py — factory functions."""
import os
from unittest.mock import patch


def test_get_postgres_db_returns_postgresdb():
    """Test that get_postgres_db returns a PostgresDb instance."""
    from agno.db.postgres import PostgresDb
    from db.session import get_postgres_db
    db = get_postgres_db()
    assert isinstance(db, PostgresDb)


def test_get_postgres_db_with_contents_table():
    """Test that contents_table parameter creates a knowledge-aware PostgresDb."""
    from agno.db.postgres import PostgresDb
    from db.session import get_postgres_db
    db = get_postgres_db(contents_table="test_contents")
    assert isinstance(db, PostgresDb)


def test_create_knowledge_returns_knowledge():
    """Test that create_knowledge returns a Knowledge instance."""
    from agno.knowledge import Knowledge
    from db.session import create_knowledge
    knowledge = create_knowledge(name="test_kb", table_name="test_vectors")
    assert isinstance(knowledge, Knowledge)
```

1. **`tests/test_agents_init.py`** — smoke tests for agent construction:

```python
"""Smoke tests — verify all agents initialize without errors."""
import os
from unittest.mock import patch


def test_web_search_agent_initializes():
    """WebSearch agent should construct without errors."""
    from agents.web_search import web_search
    assert web_search is not None
    assert web_search.id == "web-search"


def test_code_search_agent_initializes():
    """CodeSearch agent should construct without errors."""
    from agents.code_search import code_search
    assert code_search is not None
    assert code_search.id == "code-search"


def test_agno_support_agent_initializes():
    """Agno Support agent should construct without errors."""
    from agents.agno_support import agno_support_agent
    assert agno_support_agent is not None
    assert agno_support_agent.id == "agno-support-agent"


def test_all_agents_have_pre_hooks():
    """All agents should have guardrails via pre_hooks.

    Depends on Fix 1.4 being applied first. If guardrails haven't been
    added yet, this test will fail — that's expected.
    """
    from agents.web_search import web_search
    from agents.code_search import code_search
    from agents.agno_support import agno_support_agent

    for agent in [web_search, code_search, agno_support_agent]:
        assert agent.pre_hooks is not None, f"{agent.id} missing pre_hooks"
        assert len(agent.pre_hooks) > 0, f"{agent.id} has empty pre_hooks"


def test_web_search_has_tool_call_limit():
    """WebSearch agent should have a bounded tool_call_limit."""
    from agents.web_search import web_search
    assert web_search.tool_call_limit is not None
    assert web_search.tool_call_limit > 0
```

1. **`tests/test_guardrails.py`** — tests for guardrail functions:

```python
"""Tests for app/guardrails.py — guardrail and post-hook logic."""
import pytest
from pathlib import Path
from unittest.mock import MagicMock


def test_default_pre_hooks_returns_list():
    """default_pre_hooks should return a non-empty list."""
    from app.guardrails import default_pre_hooks
    hooks = default_pre_hooks()
    assert isinstance(hooks, list)
    assert len(hooks) >= 1  # at least PromptInjectionGuardrail


def test_default_pre_hooks_pii_toggle():
    """enable_pii flag should control PIIDetectionGuardrail inclusion."""
    from app.guardrails import default_pre_hooks
    from agno.guardrails import PIIDetectionGuardrail

    with_pii = default_pre_hooks(enable_pii=True)
    without_pii = default_pre_hooks(enable_pii=False)

    assert any(isinstance(h, PIIDetectionGuardrail) for h in with_pii)
    assert not any(isinstance(h, PIIDetectionGuardrail) for h in without_pii)


def test_make_file_path_validator_detects_missing():
    """File path validator should flag non-existent paths."""
    from app.guardrails import make_file_path_validator
    from agno.exceptions import OutputCheckError

    validator = make_file_path_validator(Path("/tmp/nonexistent_workspace"))
    mock_output = MagicMock()
    mock_output.content = "The function is in `nonexistent/path/file.py`"

    with pytest.raises(OutputCheckError):
        validator(mock_output)
```

1. Add a test target to `pyproject.toml` — find the `[project.optional-dependencies]` section and ensure `dev` includes `pytest`:

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    # ... existing dev deps ...
]
```

1. Add a test step to `.github/workflows/validate.yml` after the mypy step:

```yaml
      - name: Run unit tests
        run: uv run pytest tests/ -v
```

---

## Phase 2: Medium-Severity Fixes

### Fix 2.1 — Add `tool_call_limit` to All Agents (R-04, R-05, R-20)

**Validated API:** `tool_call_limit: Optional[int]` on `Agent.__init__` — caps total tool calls per run (confirmed at [/tools/tool-call-limit](https://docs.agno.com/tools/tool-call-limit)).

**Instructions for coding agent:**

This is partially handled in Fix 1.4 (guardrails were added alongside `tool_call_limit`). Ensure each agent has an appropriate limit:

| Agent | File | Recommended `tool_call_limit` | Rationale |
|-------|------|-------------------------------|-----------|
| WebSearch | `agents/web_search.py` | `10` | Bounded searches + fetches |
| CodeSearch | `agents/code_search.py` | `10` | Bounded filesystem scans |
| Agno Support | `agents/agno_support.py` | `10` | Bounded doc lookups |
| Engineering Team | `teams/engineering_team.py` | `15` | Team routes to members, needs more headroom |

For the **WorkspaceContextProvider sub-agent** (R-05), do **not** modify vendored Agno source. Instead, subclass `WorkspaceContextProvider` in your own codebase and override `_build_agent()`:

**File:** `agents/code_search.py`

```python
from agno.context.workspace import WorkspaceContextProvider

class BoundedWorkspaceContextProvider(WorkspaceContextProvider):
    """WorkspaceContextProvider with a bounded tool_call_limit on the sub-agent."""

    def _build_agent(self) -> Agent:
        return Agent(
            id=self.id,
            name=self.name,
            model=self.model,
            instructions=self.instructions_text.replace("{root}", str(self.root)),
            tools=[self._build_workspace_tools()],
            markdown=True,
            tool_call_limit=10,
        )
```

Then use `BoundedWorkspaceContextProvider` instead of `WorkspaceContextProvider` when constructing `codebase_context`. This keeps vendored code untouched and survives Agno upgrades.

---

### Fix 2.2 — Fix `db_url` Module-Level Constant (R-12, R-33, R-34)

**Risk:** `db_url` is computed at import time in `db/url.py`. If env vars are set later (e.g., by the evals dotenv loader), stale values are used. Same issue affects `agents/web_search.py` (tool selection) and `evals/cases.py` (expected tool name).

**File:** `db/url.py`

**Instructions for coding agent:**

1. Keep `build_db_url()` as-is (it's the function that reads env vars).
2. Remove the module-level `db_url = build_db_url()` line and replace with a lazy getter function. **Do not use a `__getattr__` shim** — it's defeated by `from db.url import db_url` (the import triggers `__getattr__` at import time, defeating the laziness) and it's not mypy-friendly. Just export the function:

```python
# Remove the module-level db_url = build_db_url() line.
# Replace with a lazy accessor:

_db_url: str | None = None


def get_db_url() -> str:
    """Return the database URL, building it lazily on first call.

    This allows env vars (e.g., from .env loading) to be set
    before the URL is constructed.
    """
    global _db_url
    if _db_url is None:
        _db_url = build_db_url()
    return _db_url
```

1. Update `db/__init__.py` to export `get_db_url` (and remove `db_url` from `__all__`):

```python
from db.url import build_db_url, get_db_url

__all__ = ["create_knowledge", "db_url", "get_db_url", "get_postgres_db"]
```

1. Update `db/session.py` to use `get_db_url()` instead of `db_url`:

```python
# Change:
from db.url import db_url
# To:
from db.url import get_db_url

# And in the factory functions, use get_db_url() instead of db_url:
def get_postgres_db(contents_table: str | None = None) -> PostgresDb:
    db_url = get_db_url()
    # ... rest unchanged ...
```

1. For **`agents/web_search.py`** (R-33): move the tool selection into a factory function. Replace the module-level conditional:

```python
# BEFORE:
if getenv("PARALLEL_API_KEY"):
    web_tools = ParallelTools()
else:
    web_tools = MCPTools(...)
```

With:

```python
def _build_web_tools():
    """Build web search tools, selecting SDK vs MCP based on env."""
    from os import getenv
    if getenv("PARALLEL_API_KEY"):
        return ParallelTools()
    return MCPTools(...)

web_tools = _build_web_tools()  # still module-level, but explicit
```

> **Note:** The root cause is import order. The evals harness already calls `load_dotenv()` before importing agent modules. The real fix is ensuring no module reads env vars at import time without the dotenv loader having run first. The lazy `get_db_url()` approach fixes the DB path; the web tools path is lower risk because the evals harness already handles import order correctly.

1. For **`evals/cases.py`** (R-34): move `_WEB_SEARCH_TOOL` into a function:

```python
# BEFORE:
_WEB_SEARCH_TOOL = "parallel_search" if getenv("PARALLEL_API_KEY") else "web_search"

# AFTER:
def _get_web_search_tool_name() -> str:
    return "parallel_search" if getenv("PARALLEL_API_KEY") else "web_search"
```

Then update the `CASES` tuple to use a lambda or compute it at eval-run time. Since `CASES` is a module-level constant and the eval harness loads dotenv before importing, this is lower priority — but for correctness, change the `Case` construction to use a property or compute it in `__main__.py` before building the cases list.

---

### Fix 2.3 — Validate `OPENAI_API_KEY` in `create_knowledge()` (R-11)

**File:** `db/session.py`

**Risk:** `create_knowledge()` hardcodes `OpenAIEmbedder(id="text-embedding-3-small")`. If `OPENAI_API_KEY` is unset, the first embedding call fails with an opaque 401.

**Instructions for coding agent:**

1. Add a validation check at the top of `create_knowledge()`:

```python
from os import getenv

def create_knowledge(name: str, table_name: str) -> Knowledge:
    """..."""
    # Validate API key presence early
    if not getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. The knowledge base requires "
            "OpenAI embeddings. Set OPENAI_API_KEY in your .env file."
        )

    embedder_id = getenv("EMBEDDER_MODEL_ID", "text-embedding-3-small")

    return Knowledge(
        name=name,
        vector_db=PgVector(
            db_url=get_db_url(),  # use lazy getter from Fix 2.2
            table_name=table_name,
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id=embedder_id),
        ),
        contents_db=get_postgres_db(contents_table=f"{table_name}_contents"),
    )
```

This also addresses **R-24** (hardcoded embedder model ID) by making it configurable via `EMBEDDER_MODEL_ID`.

---

### Fix 2.4 — Make Model ID Configurable (R-23)

**File:** `app/settings.py`

**Instructions for coding agent:**

Replace the hardcoded model ID with an env-var-driven one:

```python
"""Settings"""
from os import getenv
from agno.models.ollama import Ollama


def default_model():
    """Return the default model, configurable via AGENT_MODEL_ID env var."""
    model_id = getenv("AGENT_MODEL_ID", "glm-5.1:cloud")
    return Ollama(id=model_id)
```

---

### Fix 2.5 — Fix Documentation Out of Sync with Code (R-25)

**File:** `AGENTS.md` (and `CLAUDE.md` which symlinks to it)

**Risk:** AGENTS.md says `default_model()` returns `OpenAIResponses(id="gpt-5.4")` but code returns `Ollama(id="glm-5.1:cloud")`.

**Instructions for coding agent:**

1. Open `AGENTS.md`
2. Find the line that says something like:
   > `app.settings.default_model()` returns `OpenAIResponses(id="gpt-5.4")` — bump the model in one place.
3. Replace with:
   > `app.settings.default_model()` returns `Ollama(id=getenv("AGENT_MODEL_ID", "glm-5.1:cloud"))` — configurable via the `AGENT_MODEL_ID` env var. Change it in one place.

4. Also update the Environment Variables table in AGENTS.md to add:

   ```
   | `AGENT_MODEL_ID` | no | `glm-5.1:cloud` | Model ID for default_model(). |
   | `EMBEDDER_MODEL_ID` | no | `text-embedding-3-small` | OpenAI embedder model for Knowledge bases. |
   ```

---

### Fix 2.6 — Fix Compose Service Name Mismatch for `depends_on` (R-50)

Already addressed in **Fix 1.1**. The `depends_on: zeroteam-api` → `depends_on: zeroedge-api` change fixes both R-21 and R-50.

---

### Fix 2.7 — Update Eval Case for Three Registered Agents (R-44) — **URGENT: live regression**

**File:** `evals/cases.py`

**Risk:** The eval `code_search_lists_registered_agents` expects only `web-search` and `code-search`, but `app/main.py` now registers three agents (`web-search`, `code-search`, `agno-support-agent`) plus the engineering team. The LLM judge will fail this eval on the next `python -m evals` run because the response won't match "two registered agents." **This is a live regression from the recent agent extraction work — fix immediately.**

**Instructions for coding agent:**

1. Find the `code_search_lists_registered_agents` case in `evals/cases.py`
2. Update the `criteria` string:

```python
# BEFORE:
criteria=(
    "Identifies both `web-search` and `code-search` as the two registered agents. May reference app/main.py."
),

# AFTER:
criteria=(
    "Identifies `web-search`, `code-search`, and `agno-support-agent` as the "
    "three registered agents. May reference app/main.py."
),
```

---

### Fix 2.8 — Add Eval Cases for Uncovered Agents (R-43)

**File:** `evals/cases.py`

**Risk:** The Agno Support Agent and Engineering Leadership Team have zero eval coverage.

**Instructions for coding agent:**

1. Add the import for the team at the top of `evals/cases.py` (the variable is `engineering_team`, **not** `engineering_leadership_team`):

```python
from teams.engineering_team import engineering_team
```

1. Add two new cases to the `CASES` tuple:

```python
    # AgnoSupport — MCP docs lookup fires and response references agno.com docs.
    Case(
        name="agno_support_answers_guardrail_question",
        agent=agno_support_agent,
        input="How do I add a guardrail to an Agent in Agno?",
        criteria=(
            "Answers the question by referencing Agno documentation. "
            "Mentions pre_hooks and/or BaseGuardrail. The response is "
            "grounded in fetched doc content rather than a generic answer."
        ),
        # ⚠️ The Agno Support agent uses MCPTools(url="https://docs.agno.com/mcp"),
        # NOT the workspace context provider. Determine the actual MCP tool name
        # by inspecting the MCP endpoint's tool list (e.g., via a one-off run
        # that prints available tools) and set it here. Do NOT use "query_my_codebase".
        expected_tool_calls=("<actual_mcp_tool_name>",),
    ),
    # Engineering Team — team leader routes to a member.
    Case(
        name="engineering_team_routes_to_web_search",
        agent=engineering_team,
        input="Search the web for the latest news on OpenAI.",
        criteria=(
            "The response is a web search result about OpenAI. "
            "Indicates the team leader delegated to the web-search member."
        ),
        # No expected_tool_calls — team routing is hard to predict exactly.
    ),
```

> **Note:** The `expected_tool_calls` for the Agno Support agent must be determined from the actual MCP tool name exposed by `https://docs.agno.com/mcp`. Run a one-off inspection (e.g., `python -c "import asyncio; from agno.tools.mcp import MCPTools; ..."` or check the MCP endpoint's tool list) and replace `<actual_mcp_tool_name>` before running evals.

---

### Fix 2.9 — Add Test Step to CI (R-45)

**File:** `.github/workflows/validate.yml`

**Instructions for coding agent:**

1. Add a test step after the "Validate (lint + type)" step. The full step should be:

```yaml
      - name: Run unit tests
        run: uv run pytest tests/ -v --tb=short
```

> **Note:** Integration evals (`python -m evals`) require a running DB and API keys, so they're not suitable for CI without a service container. Unit tests (Fix 1.5) are CI-safe.

---

### Fix 2.10 — Share a Single `PostgresDb` Instance (R-56)

**Risk:** Each agent calls `get_postgres_db()` separately, creating multiple `PostgresDb` instances with the same `DB_ID` and `db_url`. While Agno handles this gracefully (table creation is idempotent — `CREATE TABLE IF NOT EXISTS`), it's wasteful and may create unnecessary connection pools.

**Validated from Agno docs:** The recommended pattern for shared sessions is a single `PostgresDb` instance passed to all agents ([/examples/memory/agents-share-memory](https://docs.agno.com/examples/memory/agents-share-memory)).

**Instructions for coding agent:**

1. Open `db/__init__.py` and add a shared singleton:

```python
"""Database initialization and shared instances."""
from functools import lru_cache
from agno.db.postgres import PostgresDb
from db.session import get_postgres_db, create_knowledge, get_db_url

# Note: get_postgres_db() already creates a new instance each call.
# For shared sessions, use this cached singleton:
@lru_cache(maxsize=1)
def get_shared_db() -> PostgresDb:
    """Return a singleton PostgresDb for shared session/memory storage."""
    return get_postgres_db()
```

1. Update `app/main.py` to use the shared instance:

```python
from db import get_shared_db

shared_db = get_shared_db()

agent_os = AgentOS(
    # ...
    agents=[
        web_search,  # these agents should be updated to use shared_db
        code_search,
        agno_support_agent,
    ],
    # ...
)
```

1. Update each agent file to accept the shared DB. For example in `agents/web_search.py`:

```python
from db import get_shared_db

web_search = Agent(
    # ...
    db=get_shared_db(),
    # ...
)
```

Repeat for `agents/code_search.py` and `agents/agno_support.py`.

> **Decision point — session isolation vs. shared sessions:** Currently each agent calls `get_postgres_db()` which creates a `PostgresDb` with the same `DB_ID` ("agentos-db") — they **already share the same `agno_sessions` table**. The `@lru_cache` singleton mainly saves connection pool overhead, not session isolation. The real question is whether you want **session isolation** between agents:
>
> - **Option A (shared, current behavior):** Use the singleton. Agents share `agno_sessions`. Simpler, less pool overhead. Sessions from one agent are visible to others with the same `session_id`.
> - **Option B (isolated):** Keep separate instances with explicit `session_table` values per agent. Sessions are isolated but more connection pools:
>
> ```python
> web_search = Agent(db=PostgresDb(db_url=get_db_url(), session_table="web_search_sessions"), ...)
> code_search = Agent(db=PostgresDb(db_url=get_db_url(), session_table="code_search_sessions"), ...)
> ```
>
> **Recommendation:** Option A (shared singleton) unless you have a specific isolation requirement. The current code already shares sessions — this fix just makes it explicit and efficient.

---

### Fix 2.11 — Fix Import Order Fragility in Evals (R-30)

**File:** `evals/__main__.py`

**Risk:** The `load_dotenv()` call must execute before any import that reads env vars. Future imports added above it will break silently.

**Instructions for coding agent:**

1. Add a guard comment block at the top of `evals/__main__.py`, right after the docstring:

```python
"""
... existing docstring ...
"""

# ⚠️ CRITICAL IMPORT ORDER ⚠️
# The dotenv loader MUST run before any module that reads environment
# variables at import time (db.url, agents.web_search, evals.cases, etc.).
# Do NOT add any imports above the load_dotenv() call below.
# If you need to add an import, add it AFTER load_dotenv().

from evals.dotenv import load_dotenv  # noqa: E402

load_dotenv()  # noqa: E402

# All other imports below this line are safe.
import asyncio  # noqa: E402
# ... rest of imports ...
```

---

## Phase 3: Low-Severity Fixes

### Fix 3.1 — Remove Duplicate `mcp` Dependency (R-27, R-37)

**File:** `pyproject.toml`

**Instructions:** Find the `[project] dependencies` list and remove the duplicate `"mcp"` entry. There should be only one `"mcp"` line.

---

### Fix 3.2 — Remove Unused `pymilvus` Dependency (R-41)

**File:** `pyproject.toml`

**Risk:** `pymilvus` is listed as a direct dependency but no agent or knowledge base uses Milvus (only pgvector is configured).

**Instructions:** Remove `"pymilvus"` from the `[project] dependencies` list. Then run `./scripts/generate_requirements.sh` to regenerate `requirements.txt` without pymilvus and its transitive deps (grpcio, etc.).

> **Note:** Verify no other code imports pymilvus before removing. Search for `import pymilvus` or `from pymilvus` across the codebase.

---

### Fix 3.3 — Quote Shell Variables in Scripts (R-35, R-36)

**Files:** `scripts/format.sh`, `scripts/validate.sh`, `scripts/venv_setup.sh`

**Instructions for coding agent:**

1. In `scripts/format.sh`, change:
   - `ruff format ${REPO_ROOT}` → `ruff format "${REPO_ROOT}"`
   - `ruff check --select I --fix ${REPO_ROOT}` → `ruff check --select I --fix "${REPO_ROOT}"`

2. In `scripts/validate.sh`, change:
   - `ruff check ${REPO_ROOT}` → `ruff check "${REPO_ROOT}"`
   - `mypy ${REPO_ROOT}` → `mypy "${REPO_ROOT}"`
   - `mypy ${REPO_ROOT} --config-file ${REPO_ROOT}/pyproject.toml` → `mypy "${REPO_ROOT}" --config-file "${REPO_ROOT}/pyproject.toml"`

3. In `scripts/venv_setup.sh`, change:
   - `rm -rf ${VENV_DIR}` → `rm -rf "${VENV_DIR}"`
   - `uv venv ${VENV_DIR} --python 3.12` → `uv venv "${VENV_DIR}" --python 3.12`
   - All other unquoted `${VENV_DIR}` and `${REPO_ROOT}` references

4. In `scripts/generate_requirements.sh`, change:
   - All unquoted `${REPO_ROOT}` references → `"${REPO_ROOT}"`
   - All unquoted `${VENV_DIR}` references → `"${VENV_DIR}"`

---

### Fix 3.4 — Validate `DB_DRIVER` Against Allowlist (R-02)

**File:** `db/url.py`

**Instructions for coding agent:**

Add an allowlist check in `build_db_url()`:

```python
ALLOWED_DB_DRIVERS = {
    "postgresql+psycopg",
    "postgresql+asyncpg",
    "postgresql+psycopg2",
}

def build_db_url() -> str:
    """Build database URL from environment variables."""
    driver = getenv("DB_DRIVER", "postgresql+psycopg")
    if driver not in ALLOWED_DB_DRIVERS:
        raise ValueError(
            f"Unsupported DB_DRIVER: {driver!r}. "
            f"Allowed: {', '.join(sorted(ALLOWED_DB_DRIVERS))}"
        )
    # ... rest unchanged ...
```

---

### Fix 3.5 — Add Structured Error Handling to Lifespan (R-09)

**File:** `app/main.py`

**Instructions for coding agent:**

Wrap the lifespan yield in try/except:

```python
from agno.utils.log import log_error, log_info

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    log_info("AgentOS starting up...")
    try:
        yield
    except Exception as e:
        log_error(f"AgentOS shutdown error: {e}")
        raise
    finally:
        log_info("AgentOS shutting down...")
```

---

### Fix 3.6 — Fix Bare `list` Type Hint (R-29)

**File:** `app/main.py`

**Instructions for coding agent:**

Find the line `interfaces: list = []` and change to:

```python
from agno.os.interfaces.base import BaseInterface
# ... later:
interfaces: list[BaseInterface] = []
```

If the exact import path for `BaseInterface` is uncertain, use:

```python
from typing import Any
interfaces: list[Any] = []
```

---

### Fix 3.7 — Disable Tracing When No Exporter Is Configured (R-47)

**File:** `app/main.py`

**Instructions for coding agent:**

Either set `tracing=False` or document that tracing needs an exporter. The simplest fix:

```python
from os import getenv

agent_os = AgentOS(
    # ...
    tracing=getenv("AGNO_TRACING", "false").lower() == "true",
    # ...
)
```

Add to `example.env`:

```env
# --- Tracing (optional) ---
# AGNO_TRACING=false
```

---

### Fix 3.8 — Fix `ruff format` Without Arguments (R-35 related)

**File:** `scripts/format.sh`

The `ruff format ${REPO_ROOT}` call formats the **entire** repo including the vendored `agno/` source. This may reformat library code that should be left untouched.

**Instructions for coding agent:**

1. Add the `agno/source/` directory to the `exclude` section in `pyproject.toml`'s `[tool.ruff]` config:

```toml
[tool.ruff]
exclude = [
    "agno/source",
    # ... existing excludes ...
]
```

1. **Also add `agno/source` to mypy's exclude** — the current `[tool.mypy]` config only excludes `.venv*`. Running `mypy ${REPO_ROOT}` would type-check vendored agno source, which is slow and noisy:

```toml
[tool.mypy]
exclude = [".venv*", "agno/source"]
```

Or alternatively, change the format script to target only app-level code:

```bash
ruff format app/ agents/ db/ evals/ teams/ tests/
```

---

## Phase 4: Documentation Updates

### Fix 4.1 — Update AGENTS.md with Guardrails Section

**File:** `AGENTS.md`

**Instructions for coding agent:**

Add a new section after the Architecture overview:

```markdown
## Guardrails

All agents include input validation guardrails via `pre_hooks`:

| Guardrail | Type | Agents |
|-----------|------|--------|
| `PromptInjectionGuardrail` | Pre-hook | All agents + team |
| `PIIDetectionGuardrail` | Pre-hook | Engineering Team only |

Output validation is enforced via `post_hooks`:

| Validator | Type | Agents |
|-----------|------|--------|
| `validate_citations_from_tools` | Post-hook | WebSearch |
| `make_file_path_validator` | Post-hook | CodeSearch |

All agents have `tool_call_limit=10` to bound tool invocations per run.
```

---

### Fix 4.2 — Update Environment Variables Table

Already covered in Fix 2.5. Ensure `AGENT_MODEL_ID`, `EMBEDDER_MODEL_ID`, and `AGNO_TRACING` are documented.

---

## Implementation Order

Execute fixes in this order to minimize conflicts. **Step 0 is urgent** — it's a live regression from the recent agent extraction work:

| Step | Fixes | Estimated Effort |
|------|-------|-----------------|
| **0** | **Fix 2.7 (eval criteria — URGENT live regression)** | **~5 min** |
| 1 | Fix 1.1 (compose names) + Fix 1.2 (enrich example.env) + Fix 1.3 (dockerize) | ~15 min |
| 2 | Fix 1.4a (create `app/guardrails.py`) | ~20 min |
| 3 | Fix 1.4b–e (add guardrails to each agent) | ~30 min |
| 4 | Fix 2.1 (verify tool_call_limit on all agents) | ~10 min |
| 5 | Fix 2.2 (lazy db_url) + Fix 2.3 (API key validation) + Fix 2.4 (model ID) | ~20 min |
| 6 | Fix 2.5 + Fix 4.1 (docs updates) | ~15 min |
| 7 | Fix 2.8 (add eval cases for uncovered agents) | ~15 min |
| 8 | Fix 1.5 (create test suite) | ~45 min |
| 9 | Fix 2.9 (CI test step) | ~5 min |
| 10 | Fix 2.10 (shared PostgresDb) | ~20 min |
| 11 | Fix 3.1–3.8 (low-severity cleanups) | ~30 min |
| 12 | Fix 2.11 (import order guard) + Fix 4.2 (env docs) | ~10 min |

**Total estimated effort:** ~4 hours

---

## Validation Checklist

After all fixes are applied, verify:

- [ ] `docker compose -f compose.yaml -f .devcontainer/compose.override.yaml config` shows correct merged services
- [ ] `cp example.env .env` works and `.env` is not committed
- [ ] `docker compose up` starts without `dockerize` errors
- [ ] `python -c "from app.guardrails import default_pre_hooks"` succeeds
- [ ] Each agent has `pre_hooks` set (check with `agent.pre_hooks is not None`)
- [ ] Each agent has `tool_call_limit` set
- [ ] `python -m pytest tests/ -v` passes all tests
- [ ] `python -m evals` runs without import errors
- [ ] `ruff check .` and `mypy .` pass
- [ ] `ruff format --check .` passes (no reformatting needed)
- [ ] `AGENTS.md` reflects the actual model and guardrails
- [ ] `pyproject.toml` has no duplicate `mcp` entry
- [ ] All shell scripts have quoted variables (`shellcheck scripts/*.sh` passes)
