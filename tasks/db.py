"""
Task Contract Database
=======================

SQLAlchemy engine + session factory for the task contract tables.

Reuses the project's ``db/url.py:get_db_url()`` for the connection string
so the contracts tables live in the same Postgres instance as agno's
tables (``agno_sessions``, ``agno_memories``, etc.). The contracts module
manages its own tables via its own engine — agno's ``PostgresDb`` is not
involved.
"""

from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from db.url import get_db_url


@lru_cache(maxsize=1)
def get_engine():
    """Cached SQLAlchemy engine bound to the project's Postgres instance."""
    return create_engine(get_db_url(), pool_pre_ping=True, future=True)


@lru_cache(maxsize=1)
def _get_session_factory() -> sessionmaker[Session]:
    return sessionmaker(bind=get_engine(), expire_on_commit=False, future=True)


def get_session() -> Generator[Session, None, None]:
    """Yield a SQLAlchemy session. Used as a FastAPI dependency.

    The session is committed after the request completes successfully.
    If an exception is raised, the session is rolled back. ``expire_on_commit``
    is ``False`` so accessed attributes remain usable after commit.
    """
    factory = _get_session_factory()
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_tables() -> None:
    """Create all contract tables if they don't exist.

    Called from the FastAPI lifespan on startup. Uses ``create_all()``
    which is idempotent — safe to call on every boot.
    """
    from tasks.models import (
        Base,
    )  # noqa: F401 — imports models so metadata is populated

    Base.metadata.create_all(bind=get_engine())
