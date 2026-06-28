# Reranking Implementation Report

> **Date:** 2026-06-28
> **Status:** Implemented, not yet deployed to Railway
> **Branch:** `main`

## Summary

Added Cohere reranking to the agent knowledge retrieval pipeline. The key architectural decision was to attach the reranker at the **`CompositeKnowledge` level** (post-merge) rather than on each individual `PgVector` instance. This keeps unscoped `query_knowledge` calls at **1 rerank API call** instead of 7, making Cohere's trial plan (10 rerank/min) viable for a single-user system.

Reranking is **opt-in via `CO_API_KEY`**. When unset, the retrieval pipeline works exactly as before — no breaking change.

---

## Architecture

### Where the reranker sits

```
Agent (ThinkingPartner)
  └─ tools: [get_skill_instructions, ParallelTools, query_knowledge]
       └─ KnowledgeContextProvider (ContextProvider)
            └─ CompositeKnowledge
                 ├─ fan-out: 7 KBs × per_kb_limit(5) = up to 35 candidates
                 ├─ merge + dedup by document name
                 └─ _maybe_rerank(query, merged)  ← reranker fires HERE (1 call)
                      └─ CohereReranker.rerank(query, docs)
                           └─ top_n=5 → returns best 5 docs
```

The reranker is **NOT** on each `PgVector` instance. If it were, every unscoped `query_knowledge` call would trigger 7 rerank API calls (one per KB search). At the composite level, it's 1 call on the merged pool.

### Why composite-level, not per-KB

| Approach | Rerank calls per unscoped query | Trial plan (10/min) viability |
|---|---|---|
| Per-KB (`PgVector.reranker=`) | 7 | ❌ 1 query = 70% of budget |
| Composite-level (this impl) | 1 | ✅ 10 queries/min possible |

The `KnowledgeContextProvider` fans out across 7 Studio KBs. A per-KB reranker would multiply rerank calls by 7. The composite-level design collapses that to 1.

### Graceful degradation

Two layers of exception handling:

1. **`CohereReranker.rerank()`** (Agno source) — catches all exceptions, returns original unranked docs.
2. **`CompositeKnowledge._maybe_rerank()`** (our code) — belt-and-suspenders wrapper, same fallback.

Rate-limit (429) errors → agent gets unranked results instead of crashing.

### Scoped vs unscoped queries

Both paths rerank:

| Query type | Path | Rerank calls |
|---|---|---|
| Unscoped (`query_knowledge(question)`) | `CompositeKnowledge.aretrieve()` → `_maybe_rerank()` | 1 |
| Scoped (`query_knowledge(question, scope="agent_design")`) | `kb.asearch()` → `_maybe_rerank()` | 1 |

The scoped path in `KnowledgeContextProvider._search_async()` / `_search_sync()` calls `self._composite._maybe_rerank(question, docs)` after the single-KB search returns.

---

## Files Changed

| File | Change |
|---|---|
| `pyproject.toml` | Added `cohere` to `dependencies` |
| `requirements.txt` | Regenerated — `cohere==7.0.4` |
| `db/session.py` | Added `get_reranker()` factory + `Reranker` import |
| `db/composite_knowledge.py` | Added `reranker` param, `_maybe_rerank()` method, bumped `UNIFIED_PER_KB_LIMIT` 3→5 |
| `db/knowledge_context_provider.py` | Added `reranker` param, passes to `CompositeKnowledge`, reranks scoped search results |
| `agents/thinking_partner.py` | Passes `get_reranker()` to `KnowledgeContextProvider` |
| `example.env` | Added `CO_API_KEY`, `RERANKER_MODEL_ID`, `RERANK_TOP_N` |
| `example.env.production` | Same new env vars |
| `AGENTS.md` | Added 3 rows to env var table + new "Reranking" section |

---

## Implementation Phases

### Phase 1: Dependency

Added `cohere` to `pyproject.toml` dependencies (alphabetical, after `beautifulsoup4`). Regenerated `requirements.txt` via `./scripts/generate_requirements.sh upgrade`. Result: `cohere==7.0.4`.

### Phase 2: Reranker factory (`db/session.py`)

Added `get_reranker()` — reads `CO_API_KEY` from env. Returns `None` when unset (opt-in). When set, returns `CohereReranker(model="rerank-v3.5", api_key=..., top_n=5)`. Also reads `RERANKER_MODEL_ID` (default `rerank-v3.5`) and `RERANK_TOP_N` (default `5`) for tuning without code changes.

The import of `CohereReranker` is deferred inside the function body so the `cohere` package is only imported when `CO_API_KEY` is set — no import cost when reranking is off.

### Phase 3: Composite-level reranking (`db/composite_knowledge.py`)

- Added `reranker: Optional[Reranker] = None` param to `__init__()`.
- Added `_maybe_rerank(query, docs)` method — applies the reranker if attached, with a try/except fallback to unranked docs.
- Called `_maybe_rerank()` at the end of both `retrieve()` and `aretrieve()`, after merge + dedup, before returning.
- Bumped `UNIFIED_PER_KB_LIMIT` from 3 → 5. With 7 KBs × 5 = 35 candidates pre-rerank, trimmed to `top_n=5` post-rerank. This is the standard over-fetch → rerank → trim pattern.

### Phase 4: Provider wiring (`db/knowledge_context_provider.py`)

- Added `reranker: Optional[Reranker] = None` param to `__init__()`.
- Passes it through to `CompositeKnowledge(knowledge_bases=bases, per_kb_limit=per_kb_limit, reranker=reranker)`.
- Updated scoped search paths (`_search_sync`, `_search_async`) to rerank single-KB results via `self._composite._maybe_rerank(question, docs)`.

### Phase 5: Agent wiring (`agents/thinking_partner.py`)

- Added `from db.session import get_reranker` import.
- Changed `KnowledgeContextProvider()` → `KnowledgeContextProvider(reranker=get_reranker())`.

### Phase 6: Environment + docs

- Added `CO_API_KEY`, `RERANKER_MODEL_ID`, `RERANK_TOP_N` to both `example.env` and `example.env.production` with explanatory comments.
- Updated `AGENTS.md` Environment Variables table with 3 new rows.
- Added a "Reranking" section to `AGENTS.md` under Knowledge, explaining the composite-level design and the trial plan rationale.

---

## Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `CO_API_KEY` | no | — | Cohere API key. Unset → no reranking. Set → `CohereReranker` activates. |
| `RERANKER_MODEL_ID` | no | `rerank-v3.5` | Cohere reranker model ID. |
| `RERANK_TOP_N` | no | `5` | Number of results to return after reranking. |

---

## Capacity Analysis (single-user, Cohere trial plan)

The trial plan gives 10 rerank requests/min. Composite-level reranking means 1 call per `query_knowledge` invocation.

| Scenario | Rerank calls | Under 10/min? |
|---|---|---|
| 1 scoped call per turn | 1 | ✅ |
| 1 unscoped call per turn | 1 | ✅ |
| 3-4 searches in one turn (typical) | 3-4 | ✅ |
| 10 unscoped searches in one turn (max, unlikely) | 10 | ⚠️ At limit |
| 2 unscoped + 3 scoped in one turn | 5 | ✅ |

The only realistic failure mode is the agent making 10+ `query_knowledge` calls within 60 seconds, which is well beyond typical agent behavior (`tool_call_limit=10` caps total tool calls, not just knowledge searches). When it does hit the limit, `CohereReranker.rerank()` catches the 429 and returns unranked docs — the agent continues working.

---

## Validation

- **Ruff format:** ✅ All changed files pass `ruff format --check`.
- **Ruff lint:** ✅ All changed files pass `ruff check`.
- **Mypy:** ✅ No new errors in changed files. (1 pre-existing error in `knowledge_context_provider.py:196` — `serialize_answer` attribute — unrelated to this change.)

---

## Deployment Steps

### Local

```bash
# 1. Add CO_API_KEY to .env
echo 'CO_API_KEY=your_trial_key_here' >> .env

# 2. Rebuild (picks up new cohere dependency)
docker compose up -d --build

# 3. Smoke test — hit the ThinkingPartner with a knowledge-grounded question
#    Verify reranked results appear (docs have reranking_score in metadata)
```

### Railway

```bash
# 1. Add CO_API_KEY to .env.production
echo 'CO_API_KEY=your_trial_key_here' >> .env.production

# 2. Sync env vars to Railway (auto-triggers redeploy)
./scripts/railway/env-sync.sh

# 3. Verify the deploy succeeds and query_knowledge works
railway logs --service agent-os
```

---

## Verification Checklist

- [ ] `CO_API_KEY` unset → `get_reranker()` returns `None`, retrieval works as before
- [ ] `CO_API_KEY` set → `get_reranker()` returns `CohereReranker` with `model="rerank-v3.5"`, `top_n=5`
- [ ] Unscoped `query_knowledge` → 1 rerank API call (verify via Cohere dashboard)
- [ ] Scoped `query_knowledge` → 1 rerank API call
- [ ] Rate limit hit → agent gets unranked results (no crash)
- [ ] Local smoke test: reranked docs have `reranking_score` in metadata
- [ ] Railway deploy: agent-os starts without errors

---

## Guide: Adding Reranking Next Time

This section is a reusable guide for the next reranking implementation — whether swapping rerankers, adding reranking to a new agent, or adapting the pattern to a different project.

### Step 1: Choose the reranker

Agno ships 4 rerankers in `agno/source/agno/knowledge/reranker/`:

| Reranker | Package | API key | Cost | Best for |
|---|---|---|---|---|
| `CohereReranker` | `cohere` | `CO_API_KEY` | Per-request (paid) | Cloud deploys, best quality |
| `SentenceTransformerReranker` | `sentence-transformers` | None | Free (local CPU) | Local-first, no rate limits |
| `InfinityReranker` | `infinity_client` | Optional | Free (self-hosted server) | When you run an Infinity server |
| `AwsBedrockReranker` | `boto3` + `aioboto3` | AWS creds | Per-request (paid) | AWS-native stacks |

**Decision factors:**

- **Containerized deploy (Railway, Docker)?** Avoid `SentenceTransformerReranker` — the ~2GB model download on cold start is painful in containers. Use `CohereReranker`.
- **Local-only / no API key?** Use `SentenceTransformerReranker`. No rate limit, no cost, but needs disk + CPU.
- **Rate-limited trial plan?** See the capacity analysis section below — the composite-level design is what makes trial plans viable.

### Step 2: Decide where to attach the reranker

**The critical decision.** Two options:

#### Option A: Per-vector-DB (Agno's default pattern)

Attach `reranker=` to each `PgVector` (or other `VectorDb`) instance:

```python
vector_db = PgVector(
    ...,
    reranker=CohereReranker(model="rerank-v3.5"),
)
```

**When to use:** Single knowledge base, or when each KB search is independent and you want per-KB reranking.

**Cost:** 1 rerank API call per KB search. If you fan out across N KBs, that's N calls per query.

#### Option B: Composite-level (this implementation)

Attach the reranker to the composite/fan-out layer, after merging candidates from all KBs:

```python
composite = CompositeKnowledge(
    knowledge_bases=[kb1, kb2, ...],
    reranker=CohereReranker(model="rerank-v3.5"),
)
# After fan-out + merge + dedup:
merged = self._maybe_rerank(query, merged)
```

**When to use:** Multiple KBs behind a unified search interface (like `KnowledgeContextProvider`). This is the architecturally correct place when you have a fan-out composite.

**Cost:** 1 rerank API call per query, regardless of how many KBs are searched.

**This is what we did.** The `KnowledgeContextProvider` fans out across 7 KBs. Per-KB reranking would be 7 API calls per unscoped query; composite-level is 1.

### Step 3: Add the factory function

Put a factory in `db/session.py` that reads env vars and returns the reranker (or `None`):

```python
def get_reranker() -> Optional[Reranker]:
    """Build a reranker from env vars. Returns None if opt-in key is unset."""
    api_key = getenv("CO_API_KEY")
    if not api_key:
        return None

    from agno.knowledge.reranker.cohere import CohereReranker  # deferred import

    model = getenv("RERANKER_MODEL_ID", "rerank-v3.5")
    top_n = int(getenv("RERANK_TOP_N", "5"))
    return CohereReranker(model=model, api_key=api_key, top_n=top_n)
```

Key patterns:

- **Deferred import** inside the function — the `cohere` package is only imported when the key is set. No import cost when reranking is off.
- **`None` when unset** — reranking is opt-in via env var. No breaking change.
- **Tuning via env vars** — `RERANKER_MODEL_ID` and `RERANK_TOP_N` let you change model/result count without code changes.

### Step 4: Wire it into the retrieval path

For composite-level reranking, add a `_maybe_rerank()` method and call it after merge + dedup:

```python
def _maybe_rerank(self, query: str, docs: List[Document]) -> List[Document]:
    if self.reranker is None or not docs:
        return docs
    try:
        return self.reranker.rerank(query=query, documents=docs)
    except Exception as e:
        log_warning(f"Rerank failed, returning unranked: {e}")
        return docs
```

Call it at the end of both sync and async retrieve paths:

```python
# In retrieve() and aretrieve(), after the merge+dedup loop:
merged = self._maybe_rerank(query, merged)
return merged
```

**Don't forget the scoped path.** If your provider has a scoped search that bypasses the composite (like `KnowledgeContextProvider._search_async` does), add reranking there too:

```python
# In scoped search:
docs = kb.asearch(query=question, max_results=per_kb_limit)
return self._composite._maybe_rerank(question, docs)  # rerank scoped results
```

### Step 5: Over-fetch candidates

Reranking is most valuable when you retrieve more candidates than you need, then let the reranker trim. Bump the per-KB limit:

```python
# Before (no reranker): 3 candidates per KB
UNIFIED_PER_KB_LIMIT = 3

# After (with reranker): 5 candidates per KB, reranker trims to top_n=5
UNIFIED_PER_KB_LIMIT = 5
```

With 7 KBs × 5 = 35 candidates pre-rerank, the reranker has good signal to pick the best 5.

### Step 6: Add env vars + docs

- Add the new env vars to `example.env` and `example.env.production` with comments.
- Update the `AGENTS.md` Environment Variables table.
- Add a section to `AGENTS.md` explaining the reranking design (where it sits, why, degradation behavior).

### Step 7: Validate

```bash
source .venv/bin/activate
ruff format db/session.py db/composite_knowledge.py db/knowledge_context_provider.py
ruff check db/session.py db/composite_knowledge.py db/knowledge_context_provider.py
mypy db/session.py db/composite_knowledge.py db/knowledge_context_provider.py --config-file pyproject.toml
```

### Step 8: Deploy

```bash
# Local
echo 'CO_API_KEY=your_key' >> .env
docker compose up -d --build

# Railway
echo 'CO_API_KEY=your_key' >> .env.production
./scripts/railway/env-sync.sh
```

---

## Capacity Planning Cheat Sheet

When evaluating whether a reranker's rate limit is viable:

1. **Count the KBs** in your composite. This is your multiplier if you use per-KB reranking.
2. **Decide composite vs per-KB.** Composite = 1 call/query. Per-KB = N calls/query.
3. **Estimate queries per turn.** Typical agent behavior: 1-4 `query_knowledge` calls per user turn.
4. **Check the limit.** Cohere trial = 10/min. Paid plans scale up.
5. **Verify graceful degradation.** Check that `Reranker.rerank()` catches exceptions. `CohereReranker` does (source: `agno/source/agno/knowledge/reranker/cohere.py:71-74`). Add your own try/except as a second safety net.

| Reranker calls per query | 10/min limit | 100/min limit | 1000/min limit |
|---|---|---|---|
| 1 (composite-level) | 10 queries/min | 100/min | 1000/min |
| 7 (per-KB, 7 KBs) | 1.4 queries/min | 14/min | 142/min |

---

## Upgrade Paths

### Swap to a different reranker

Change `get_reranker()` in `db/session.py` to return a different `Reranker` subclass. No other code changes needed — the composite-level interface is reranker-agnostic.

```python
# Swap to SentenceTransformerReranker (local, no API key)
from agno.knowledge.reranker.sentence_transformer import SentenceTransformerReranker
return SentenceTransformerReranker(model="BAAI/bge-reranker-v2-m3", top_n=top_n)
```

### Upgrade to paid Cohere plan

Just get a new API key with higher limits. No code changes — the composite-level design means higher limits just raise the ceiling.

### Add reranking to another agent

1. Import `get_reranker` from `db.session`.
2. Pass `reranker=get_reranker()` to `KnowledgeContextProvider`.
3. Done. The provider + composite handle the rest.

### Make reranker type configurable via env

Add a `RERANKER_TYPE` env var (`cohere` | `sentence_transformer` | `none`) to `get_reranker()`:

```python
def get_reranker() -> Optional[Reranker]:
    reranker_type = getenv("RERANKER_TYPE", "cohere")
    if reranker_type == "none":
        return None
    # ... build based on type
```

This lets you switch between local (dev) and cloud (prod) rerankers without code changes.
