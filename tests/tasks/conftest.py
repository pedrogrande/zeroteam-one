"""
Shared fixtures for task contract tests.

Uses a dedicated Postgres test database (``zeroedge-test-db`` on port 5433)
so tests exercise the real schema — JSONB, GIN indexes, CHECK constraints,
PGUUID — without polluting the development database.

Each test gets a fresh schema: tables are created before and dropped after.
The test database is shared across tests in a session but the tables are
per-test for isolation.
"""

from __future__ import annotations

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------------------------
# Test database URL — dedicated test instance on port 5433
# ---------------------------------------------------------------------------

TEST_DB_URL = "postgresql+psycopg://ai:ai@localhost:5433/task_test"


# ---------------------------------------------------------------------------
# Engine + session factory (session-scoped — one engine for all tests)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def test_engine():
    """Session-scoped engine bound to the test Postgres instance."""
    engine = create_engine(TEST_DB_URL, pool_pre_ping=True, future=True)
    yield engine
    engine.dispose()


@pytest.fixture(scope="session")
def test_session_factory(test_engine):
    """Session-scoped sessionmaker bound to the test engine."""
    return sessionmaker(bind=test_engine, expire_on_commit=False, future=True)


# ---------------------------------------------------------------------------
# Per-test table lifecycle — create before, drop after
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _isolated_tables(test_engine):
    """Create all tables before each test, drop them after.

    This gives each test a clean slate without needing a separate database
    per test. The engine is shared (session-scoped) for connection pooling.
    """
    import tasks.models as tasks_models

    tasks_models.Base.metadata.create_all(bind=test_engine)
    yield
    tasks_models.Base.metadata.drop_all(bind=test_engine)


# ---------------------------------------------------------------------------
# Patch tasks.db to use the test engine
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _patch_engine(test_engine, test_session_factory, monkeypatch):
    """Patch ``tasks.db`` so all code under test hits the test database."""
    import tasks.db as tasks_db

    monkeypatch.setattr(tasks_db, "get_engine", lambda: test_engine)
    monkeypatch.setattr(tasks_db, "_get_session_factory", lambda: test_session_factory)
    monkeypatch.setattr(
        tasks_db,
        "get_session",
        lambda: _test_session_generator(test_session_factory),
    )


def _test_session_generator(factory):
    """Yield a session, commit on success, rollback on error."""
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# ---------------------------------------------------------------------------
# FastAPI TestClient fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def client(test_session_factory):
    """TestClient with the /api/v1 router, using the test Postgres."""
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from api.deps import get_db_session
    from api.router import api_router

    def _override_session():
        yield from _test_session_generator(test_session_factory)

    test_app = FastAPI()
    test_app.include_router(api_router)
    test_app.dependency_overrides[get_db_session] = _override_session

    return TestClient(test_app)
