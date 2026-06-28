"""
Session Explorer — Ingest and chat with exported Agno session data.

Provides:
  - parse: Parse markdown session exports into structured data
  - enrich: Add computed metadata to parsed sessions
  - chunker: Chunk sessions for vector embedding
  - ingest: CLI ingestion pipeline
  - agent: Interactive chat agent for querying session knowledge
"""

from .shared import session_knowledge, session_vector_db, session_db

__all__ = [
    "session_db",
    "session_knowledge",
    "session_vector_db",
]
