"""Shared test fixtures."""

import pytest


@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    """Ensure test env vars are set before any imports.

    These are set via monkeypatch so they apply to any module that
    reads env vars lazily (e.g., get_db_url, default_model).

    Uses the local Docker Compose Postgres defaults (ai/ai) so that
    tests which construct PostgresDb objects can connect when the
    local DB is running. Tests that don't need a DB won't connect.
    """
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_USER", "ai")
    monkeypatch.setenv("DB_PASS", "ai")
    monkeypatch.setenv("DB_DATABASE", "ai")
