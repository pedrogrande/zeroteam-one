"""
Database Session
================

PostgreSQL connection helpers.
``get_postgres_db()`` for agent storage backed by Postgres.
``create_knowledge()`` for agent knowledge backed by PgVector.
"""

from os import getenv
from functools import lru_cache
from typing import Optional

from agno.db.postgres import PostgresDb
from agno.knowledge import Knowledge
from agno.knowledge.chunking.agentic import AgenticChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.reranker.base import Reranker
from agno.vectordb.pgvector import PgVector, SearchType

from db.url import get_db_url

DB_ID = "agentos-db"


@lru_cache(maxsize=1)
def _shared_db() -> PostgresDb:
    """Singleton PostgresDb for plain agent persistence (sessions, memory)."""
    return PostgresDb(id=DB_ID, db_url=get_db_url())


def get_postgres_db(contents_table: str | None = None) -> PostgresDb:
    """Get a PostgresDb instance.

    Pass ``contents_table`` only when this database is the ``contents_db``
    of a Knowledge base — it tells agno where to persist document contents.
    For plain agent persistence (sessions, memory) leave it unset.

    The plain case returns a cached singleton so every agent shares one
    ``PostgresDb`` (and one connection pool) instead of registering
    duplicate instances under the same id. Knowledge-base contents tables
    get a distinct id derived from the table name to avoid shadowing.
    """
    if contents_table is not None:
        return PostgresDb(
            id=f"{DB_ID}:{contents_table}",
            db_url=get_db_url(),
            knowledge_table=contents_table,
        )
    return _shared_db()


def create_knowledge(name: str, table_name: str) -> Knowledge:
    """PgVector knowledge base with hybrid search.

    Plug into an Agent's ``knowledge=`` to give it a RAG surface. Vectors
    land in ``table_name``; document contents in ``{table_name}_contents``.
    """
    # Validate API key presence early — avoids an opaque 401 on first embedding call.
    if not getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. The knowledge base requires "
            "OpenAI embeddings. Set OPENAI_API_KEY in your .env file."
        )

    embedder_id = getenv("EMBEDDER_MODEL_ID", "text-embedding-3-small")
    db_url = get_db_url()

    return Knowledge(
        name=name,
        vector_db=PgVector(
            db_url=db_url,
            table_name=table_name,
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id=embedder_id),
        ),
        contents_db=get_postgres_db(contents_table=f"{table_name}_contents"),
    )


def create_studio_knowledge(
    name: str,
    table_name: str,
    description: Optional[str] = None,
) -> Knowledge:
    """Knowledge base registered with the AgentOS Studio Registry.

    Same PgVector + OpenAI embedder + ``contents_db`` shape as
    :func:`create_knowledge`, plus two Studio-specific requirements:

    - ``description`` — surfaced in Studio's knowledge picker.
    - A pre-seeded ``PDFReader`` using :class:`AgenticChunking` so PDFs
      uploaded through the Studio Knowledge UI are chunked semantically
      rather than with the default fixed-size ``DocumentChunking``.

    The reader is injected via :meth:`Knowledge.add_reader` under the
    ``"pdf"`` key. ``Knowledge._get_reader("pdf")`` checks ``self.readers``
    before falling back to the :class:`ReaderFactory`, so this pre-seeded
    instance wins for Studio-initiated uploads.
    """
    knowledge = create_knowledge(name=name, table_name=table_name)
    # Re-attach the description (create_knowledge doesn't accept it).
    knowledge.description = description
    # Force agentic chunking on PDF uploads routed through this KB.
    # ``Knowledge.pdf_reader`` resolves via ``_get_reader("pdf")``, which checks
    # ``self.readers`` for the literal key ``"pdf"`` before falling back to the
    # ``ReaderFactory``. ``add_reader`` derives the key from the reader's name,
    # so we assign the dict entry directly to guarantee the ``"pdf"`` key.
    if knowledge.readers is None:
        knowledge.readers = {}
    knowledge.readers["pdf"] = PDFReader(
        name="Agentic Chunking PDF Reader",
        chunking_strategy=AgenticChunking(),
    )
    return knowledge


# ---------------------------------------------------------------------------
# Reranker
# ---------------------------------------------------------------------------
# Cohere reranker for composite-level reranking. Opt-in via ``CO_API_KEY``.
# When unset, ``get_reranker()`` returns ``None`` and the retrieval pipeline
# behaves exactly as before (no reranking).
#
# The reranker is attached at the ``CompositeKnowledge`` level — NOT on each
# ``PgVector`` instance. This is deliberate: the ``KnowledgeContextProvider``
# fans out across 7 Studio KBs per unscoped ``query_knowledge`` call. With a
# per-KB reranker that would be 7 Cohere API calls per query; at the composite
# level it is 1 call on the merged candidate pool. This keeps the Cohere trial
# plan's 10 rerank/min limit viable for a single-user system.
#
# ``CohereReranker.rerank()`` already catches all exceptions and returns the
# original unranked documents on failure (rate limit, network, etc.), so
# rate-limit errors degrade gracefully — the agent gets unranked results
# instead of crashing.
#
# Env vars:
# - ``CO_API_KEY``        — Cohere API key. Unset → no reranking.
# - ``RERANKER_MODEL_ID`` — Cohere model (default ``rerank-v3.5``).
# - ``RERANK_TOP_N``      — Results to return after reranking (default 5).
#
# Source: https://docs.agno.com/knowledge/concepts/search-and-retrieval/agentic-rag


def get_reranker() -> Optional[Reranker]:
    """Build a Cohere reranker from env vars. Returns ``None`` if ``CO_API_KEY`` is unset.

    Reranking is opt-in: when ``CO_API_KEY`` is not set, the retrieval
    pipeline works exactly as before (no reranking, no Cohere dependency
    exercised). When set, a :class:`CohereReranker` is returned for use at
    the :class:`CompositeKnowledge` level.
    """
    api_key = getenv("CO_API_KEY")
    if not api_key:
        return None

    from agno.knowledge.reranker.cohere import CohereReranker

    model = getenv("RERANKER_MODEL_ID", "rerank-v3.5")
    top_n = int(getenv("RERANK_TOP_N", "5"))
    return CohereReranker(model=model, api_key=api_key, top_n=top_n)
