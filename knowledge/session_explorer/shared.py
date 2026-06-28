"""
Shared resources for the Session Explorer pipeline.

Re-exports the "Agno Sessions" Studio knowledge base (defined in
``db/knowledge_bases.py``) so the ingest pipeline writes into the same
Postgres + OpenAI-embedder stack as every other Studio KB.

Previously this module constructed a standalone ``Knowledge`` with an
Ollama embedder on a separate Postgres instance (port 5532). It now
delegates to the project's single source of truth so sessions land in
the primary database and are searchable by any agent wired to the
``CompositeKnowledge`` (e.g. the ThinkingPartner).
"""

from agno.knowledge.knowledge import Knowledge

from db import get_shared_db
from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES_BY_TABLE

# ── Knowledge Base (PgVector, OpenAI embeddings, project DB) ────────────────
# The "Agno Sessions" KB is registered with the AgentOS Studio Registry,
# so ingested content is also selectable from Studio-composed agents.
# Table: agno_session_transcripts (vectors) + agno_session_transcripts_contents
# (content hashes for skip_if_exists idempotency). Note: the table is named
# ``agno_session_transcripts``, not ``agno_sessions``, to avoid colliding
# with Agno's reserved session-storage table (which holds session_data/runs,
# not vector columns).
session_knowledge: Knowledge = STUDIO_KNOWLEDGE_BASES_BY_TABLE[
    "agno_session_transcripts"
]

# Agno session storage — shared singleton PostgresDb (same instance as
# every agent). Used by the ingest pipeline for contents tracking.
session_db = get_shared_db()

# Expose the vector_db directly for callers that need the table name.
session_vector_db = session_knowledge.vector_db

__all__ = [
    "session_db",
    "session_knowledge",
    "session_vector_db",
]
