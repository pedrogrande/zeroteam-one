"""
Database URL
============
"""

from os import getenv
from urllib.parse import quote

ALLOWED_DB_DRIVERS = {
    "postgresql+psycopg",
    "postgresql+asyncpg",
    "postgresql+psycopg2",
}


def build_db_url() -> str:
    """Build database URL from environment variables."""
    driver = getenv("DB_DRIVER", "postgresql+psycopg")
    if driver not in ALLOWED_DB_DRIVERS:
        raise ValueError(
            f"Unsupported DB_DRIVER: {driver!r}. Allowed: {', '.join(sorted(ALLOWED_DB_DRIVERS))}"
        )
    user = getenv("DB_USER", "ai")
    password = quote(getenv("DB_PASS", "ai"), safe="")
    host = getenv("DB_HOST", "localhost")
    port = getenv("DB_PORT", "5432")
    database = getenv("DB_DATABASE", "ai")

    return f"{driver}://{user}:{password}@{host}:{port}/{database}"


_db_url: str | None = None


def get_db_url() -> str:
    """Return the database URL, building it lazily on first call.

    This allows env vars (e.g., from .env loading) to be set
    before the URL is constructed.
    """
    global _db_url
    if _db_url is None:
        _db_url = build_db_url()
    return _db_url
