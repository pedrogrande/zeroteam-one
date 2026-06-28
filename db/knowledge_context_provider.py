"""
Knowledge Context Provider
==========================

A :class:`ContextProvider` that exposes every Studio knowledge base
behind a single ``query_knowledge(question, scope?)`` tool, collapsing
the 7 per-KB search tools + 1 implicit ``search_knowledge_base`` (8
tools) into 1.

The provider delegates fan-out + merge + dedup to
:class:`CompositeKnowledge` (the internal retrieval engine). An optional
``scope`` parameter lets the model target a specific domain (e.g.
``scope="sessions"``) without a separate tool; omit it for cross-domain
search.

This replaces the ``Agent(knowledge=...)`` protocol path for the
ThinkingPartner. The ``LearningMachine``'s write sink
(``user_profile_information``) is unaffected — it still uses a real
``Knowledge`` instance directly.

Usage
-----
    from db.knowledge_context_provider import KnowledgeContextProvider

    provider = KnowledgeContextProvider()
    agent = Agent(
        tools=provider.get_tools(),
        instructions=INSTRUCTIONS + "\\n\\n" + provider.instructions(),
        ...
    )
"""

from typing import List, Optional

from agno.context.provider import Answer, ContextProvider, Document, Status
from agno.knowledge.reranker.base import Reranker
from agno.run import RunContext
from agno.tools import tool

from db.composite_knowledge import CompositeKnowledge
from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES, Knowledge

# ---------------------------------------------------------------------------
# Scope aliases — short, model-friendly names keyed by table_name.
# The model passes one of these as the ``scope`` argument to
# ``query_knowledge`` to target a single KB. Maps to the KB's vector
# table name for lookup in STUDIO_KNOWLEDGE_BASES_BY_TABLE.
# ---------------------------------------------------------------------------
SCOPE_ALIASES: dict[str, str] = {
    "sessions": "agno_session_transcripts",
    "agent_design": "agent_design",
    "workflow": "agentic_workflow_design",
    "learning": "ai_assisted_learning",
    "user_profile": "user_profile_information",
    "agentos_lab": "agentos_lab",
    "task_contract": "task_contract",
}


class KnowledgeContextProvider(ContextProvider):
    """One ``query_knowledge`` tool across all Studio knowledge bases.

    Read-only. The ``scope`` parameter (optional) targets a single KB
    by short name; omit for unified fan-out across all KBs.
    """

    def __init__(
        self,
        knowledge_bases: Optional[List[Knowledge]] = None,
        per_kb_limit: int = 3,
        reranker: Optional[Reranker] = None,
    ) -> None:
        super().__init__(
            id="knowledge",
            name="Knowledge Bases",
            read=True,
            write=False,
        )
        bases = (
            knowledge_bases if knowledge_bases is not None else STUDIO_KNOWLEDGE_BASES
        )
        self._composite = CompositeKnowledge(
            knowledge_bases=bases,
            per_kb_limit=per_kb_limit,
            reranker=reranker,
        )
        # Build a table_name → Knowledge map for scoped queries.
        self._kb_by_table: dict[str, Knowledge] = {
            getattr(kb.vector_db, "table_name", ""): kb for kb in bases
        }

    # ------------------------------------------------------------------
    # Required: query / aquery
    # ------------------------------------------------------------------

    def query(
        self,
        question: str,
        *,
        run_context: Optional[RunContext] = None,
    ) -> Answer:
        """Sync search across KBs. Scoped if ``scope:`` prefix present."""
        scope, clean_question = _parse_scope(question)
        docs = self._search_sync(clean_question, scope=scope)
        return _docs_to_answer(docs, self._kb_by_table)

    async def aquery(
        self,
        question: str,
        *,
        run_context: Optional[RunContext] = None,
    ) -> Answer:
        """Async search across KBs. Scoped if ``scope:`` prefix present."""
        scope, clean_question = _parse_scope(question)
        docs = await self._search_async(clean_question, scope=scope)
        return _docs_to_answer(docs, self._kb_by_table)

    # ------------------------------------------------------------------
    # Required: status / astatus
    # ------------------------------------------------------------------

    def status(self) -> Status:
        return Status(
            ok=True,
            detail=f"{len(self._composite.knowledge_bases)} knowledge bases connected",
        )

    async def astatus(self) -> Status:
        return self.status()

    # ------------------------------------------------------------------
    # Optional: instructions (system-prompt guidance)
    # ------------------------------------------------------------------

    def instructions(self) -> str:
        lines = [
            "<knowledge_provider>",
            "You have access to a knowledge base via the `query_knowledge` tool.",
            "Search before answering questions that may touch prior context — don't assume you know the answer.",
            "",
            "## Usage",
            "",
            "- `query_knowledge(question)` — search ALL knowledge bases (default).",
            '- `query_knowledge(question, scope="<domain>")` — search one domain.',
            "",
            "## Available scopes",
            "",
        ]
        for short, table in SCOPE_ALIASES.items():
            kb = self._kb_by_table.get(table)
            desc = (kb.description or "").strip().replace("\n", " ") if kb else ""
            # Keep each line short — index, not content.
            if len(desc) > 90:
                desc = desc[:87] + "..."
            lines.append(f"- `{short}` — {desc}")
        lines.extend(
            [
                "",
                "## Guidance",
                "",
                "1. Omit `scope` for broad or cross-domain questions.",
                "2. Include `scope` when the question clearly targets one domain.",
                "3. Cite the source KB and document name when referencing results.",
                "</knowledge_provider>",
            ]
        )
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Override _query_tool to add an explicit `scope` parameter
    # ------------------------------------------------------------------

    def _query_tool(self):
        provider = self

        @tool(name=self.query_tool_name)
        async def _query(
            question: str,
            scope: Optional[str] = None,
            run_context: Optional[RunContext] = None,
        ) -> str:
            """Search the knowledge bases for information.

            Args:
                question: The query to search for.
                scope: Optional domain to search — one of: sessions,
                    agent_design, workflow, learning, user_profile,
                    agentos_lab, task_contract. Omit to search all.

            Returns:
                JSON with matching documents (name, content, source KB).
            """
            import json

            from agno.context.provider import serialize_answer

            try:
                # If the model passed an explicit scope, prefix it so
                # _parse_scope picks it up inside aquery().
                effective_question = (
                    f"scope: {scope} — {question}" if scope else question
                )
                answer = await provider.aquery(
                    effective_question, run_context=run_context
                )
            except Exception as exc:
                return json.dumps({"error": f"{type(exc).__name__}: {exc}"})
            return json.dumps(serialize_answer(answer))

        return _query

    # ------------------------------------------------------------------
    # Internal retrieval
    # ------------------------------------------------------------------

    def _search_sync(
        self,
        question: str,
        *,
        scope: Optional[str] = None,
    ) -> List:
        if scope and scope in SCOPE_ALIASES:
            table = SCOPE_ALIASES[scope]
            kb = self._kb_by_table.get(table)
            if kb:
                docs = kb.search(
                    query=question, max_results=self._composite.per_kb_limit
                )
                return self._composite._maybe_rerank(question, docs)
            return []
        return self._composite.retrieve(query=question)

    async def _search_async(
        self,
        question: str,
        *,
        scope: Optional[str] = None,
    ) -> List:
        if scope and scope in SCOPE_ALIASES:
            table = SCOPE_ALIASES[scope]
            kb = self._kb_by_table.get(table)
            if kb:
                docs = await kb.asearch(
                    query=question, max_results=self._composite.per_kb_limit
                )
                return self._composite._maybe_rerank(question, docs)
            return []
        return await self._composite.aretrieve(query=question)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_scope(question: str) -> tuple[Optional[str], str]:
    """Extract a ``scope: <name>`` prefix from the question.

    The model may pass ``scope: sessions — <actual question>``. Returns
    (scope_or_None, cleaned_question). Unknown scopes are ignored
    (treated as no scope).
    """
    import re

    match = re.match(r"^\s*scope:\s*([a-z_]+)\s*[—\-]\s*", question, re.IGNORECASE)
    if match:
        candidate = match.group(1).lower()
        if candidate in SCOPE_ALIASES:
            return candidate, question[match.end() :].strip()
    return None, question


def _docs_to_answer(docs: List, kb_by_table: dict[str, Knowledge]) -> Answer:
    """Convert a list of agno ``Document`` objects to a provider ``Answer``.

    The ``text`` field labels each result with its source KB + document
    name for citation. The ``results`` field carries structured
    ``Document`` entries.
    """
    if not docs:
        return Answer(text="No documents found.")

    parts: list[str] = []
    results: list[Document] = []
    for doc in docs:
        # Determine the source KB name from the doc's metadata if available.
        source = "Knowledge Base"
        meta = getattr(doc, "meta_data", {}) or {}
        if isinstance(meta, dict):
            # agno session chunks carry agent_name_slug; other KBs may
            # not carry a source field. Fall back to a generic label.
            slug = meta.get("agent_name_slug")
            if slug:
                source = slug
        name = doc.name or "Untitled"
        parts.append(f"### {source} — {name}\n{doc.content}")
        results.append(
            Document(
                id=getattr(doc, "id", name) or name,
                name=name,
                snippet=(
                    (doc.content[:200] + "...")
                    if len(doc.content) > 200
                    else doc.content
                ),
                source=source,
            )
        )
    return Answer(text="\n\n---\n\n".join(parts), results=results)
