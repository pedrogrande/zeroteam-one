"""
Composite Knowledge
===================

Internal retrieval engine that aggregates multiple :class:`Knowledge`
bases behind a single fan-out + merge + dedup interface.

This module is **not** agent-facing. It exists to serve
:class:`KnowledgeContextProvider` (``db/knowledge_context_provider.py``),
which exposes one ``query_knowledge`` tool to the agent and delegates
retrieval here. The former per-KB ``search_<alias>`` tool surface and
``build_context()`` system-prompt injection have been removed — the
context provider replaces both.

Usage (internal)
----------------
    from db.composite_knowledge import CompositeKnowledge
    composite = CompositeKnowledge.from_registry()
    docs = await composite.aretrieve(query="agent design patterns")
"""

from typing import Any, Dict, List, Optional, Union

from agno.knowledge.document import Document
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reranker.base import Reranker
from agno.utils.log import log_debug, log_warning

# Per-KB results cap for the unified fan-out. With 7 KBs this yields up
# to 35 candidate docs (7 × 5), deduplicated and reranked down to
# ``RERANK_TOP_N`` (default 5) when a reranker is attached. Over-fetching
# candidates gives the reranker more signal — the standard
# over-fetch → rerank → trim pattern.
UNIFIED_PER_KB_LIMIT = 5


class CompositeKnowledge:
    """Aggregate multiple ``Knowledge`` bases for fan-out retrieval.

    ``retrieve()`` / ``aretrieve()`` search every KB in parallel, merge
    results, and deduplicate by document name. Read-only — no
    ``insert()``. Writes go through the ``LearningMachine``'s own
    knowledge sink (a real ``Knowledge`` instance).
    """

    def __init__(
        self,
        knowledge_bases: List[Knowledge],
        per_kb_limit: int = UNIFIED_PER_KB_LIMIT,
        reranker: Optional[Reranker] = None,
    ) -> None:
        if not knowledge_bases:
            raise ValueError("CompositeKnowledge requires at least one Knowledge base")
        self.knowledge_bases: List[Knowledge] = knowledge_bases
        self.per_kb_limit = per_kb_limit
        # Total cap after merge + dedup (pre-rerank).
        self.max_results: int = per_kb_limit * len(knowledge_bases)
        # Optional reranker applied AFTER merge + dedup, BEFORE returning.
        # When set, one ``reranker.rerank(query, merged)`` call is made per
        # retrieve() / aretrieve() invocation — not one per KB. This keeps
        # unscoped queries at 1 rerank API call instead of 7, which matters
        # under Cohere's trial-plan 10 rerank/min limit.
        # When ``None``, retrieval behaves exactly as before (no reranking).
        self.reranker: Optional[Reranker] = reranker

    # ------------------------------------------------------------------
    # Retrieval — fan-out + merge + dedup
    # ------------------------------------------------------------------

    def retrieve(
        self,
        query: str,
        max_results: Optional[int] = None,
        filters: Optional[Union[Dict[str, Any], List[Any]]] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """Fan-out search across all KBs, merge, deduplicate by name."""
        limit = max_results or self.max_results
        per_kb = self.per_kb_limit
        merged: List[Document] = []
        seen_names: set[str] = set()

        for kb in self.knowledge_bases:
            try:
                docs = kb.search(query=query, max_results=per_kb, filters=filters)
            except Exception as e:
                log_warning(f"CompositeKnowledge: KB {kb.name!r} search failed: {e}")
                continue
            for doc in docs:
                key = doc.name or doc.content_id or doc.content[:64]
                if key in seen_names:
                    continue
                seen_names.add(key)
                merged.append(doc)
                if len(merged) >= limit:
                    break
            if len(merged) >= limit:
                break

        merged = self._maybe_rerank(query, merged)
        log_debug(f"CompositeKnowledge.retrieve: {len(merged)} docs for {query!r}")
        return merged

    async def aretrieve(
        self,
        query: str,
        max_results: Optional[int] = None,
        filters: Optional[Union[Dict[str, Any], List[Any]]] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """Async fan-out search across all KBs, merge, deduplicate by name."""
        limit = max_results or self.max_results
        per_kb = self.per_kb_limit
        merged: List[Document] = []
        seen_names: set[str] = set()

        for kb in self.knowledge_bases:
            try:
                docs = await kb.asearch(query=query, max_results=per_kb, filters=filters)
            except Exception as e:
                log_warning(f"CompositeKnowledge: KB {kb.name!r} async search failed: {e}")
                continue
            for doc in docs:
                key = doc.name or doc.content_id or doc.content[:64]
                if key in seen_names:
                    continue
                seen_names.add(key)
                merged.append(doc)
                if len(merged) >= limit:
                    break
            if len(merged) >= limit:
                break

        merged = self._maybe_rerank(query, merged)
        log_debug(f"CompositeKnowledge.aretrieve: {len(merged)} docs for {query!r}")
        return merged

    # ------------------------------------------------------------------
    # Reranking
    # ------------------------------------------------------------------

    def _maybe_rerank(self, query: str, docs: List[Document]) -> List[Document]:
        """Apply the reranker to merged docs if one is attached.

        Belt-and-suspenders: ``CohereReranker.rerank()`` already catches
        exceptions and returns the original docs, but we wrap again so a
        buggy custom reranker can't break the retrieval path.
        """
        if self.reranker is None or not docs:
            return docs
        try:
            return self.reranker.rerank(query=query, documents=docs)
        except Exception as e:
            log_warning(f"CompositeKnowledge: rerank failed, returning unranked: {e}")
            return docs

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    @classmethod
    def from_registry(cls) -> "CompositeKnowledge":
        """Build a composite from the Studio KB registry."""
        from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES

        return cls(STUDIO_KNOWLEDGE_BASES)
