"""
Database Module
===============
"""

from functools import lru_cache

from agno.db.postgres import PostgresDb

from db.session import create_knowledge, create_studio_knowledge, get_postgres_db
from db.url import build_db_url, get_db_url

__all__ = [
    "create_knowledge",
    "create_studio_knowledge",
    "get_db_url",
    "get_postgres_db",
    "get_shared_db",
    "build_db_url",
]


@lru_cache(maxsize=1)
def get_shared_db() -> PostgresDb:
    """Return a singleton PostgresDb for shared session/memory storage.

    All agents already share the same ``DB_ID`` ("agentos-db") and thus the
    same ``agno_sessions`` table. This cached singleton avoids creating
    redundant connection pools.
    """
    return get_postgres_db()
