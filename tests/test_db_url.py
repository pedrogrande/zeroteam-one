"""Tests for db/url.py — URL construction from env vars."""

import os
from unittest.mock import patch
from urllib.parse import quote


def test_build_db_url_with_defaults():
    """Test URL construction with default values when env vars are unset."""
    from db.url import build_db_url

    with patch.dict(os.environ, {}, clear=True):
        url = build_db_url()
        assert "postgresql+psycopg" in url
        assert "ai:ai" in url
        assert "localhost" in url
        assert "5432" in url
        assert url.endswith("/ai")


def test_build_db_url_with_custom_values():
    """Test URL construction with custom env vars."""
    from db.url import build_db_url

    with patch.dict(
        os.environ,
        {
            "DB_DRIVER": "postgresql+asyncpg",
            "DB_USER": "myuser",
            "DB_PASS": "p@ss w0rd",
            "DB_HOST": "db.example.com",
            "DB_PORT": "6543",
            "DB_DATABASE": "mydb",
        },
    ):
        url = build_db_url()
        assert (
            url
            == f"postgresql+asyncpg://myuser:{quote('p@ss w0rd')}@db.example.com:6543/mydb"
        )


def test_build_db_url_password_is_url_encoded():
    """Test that special characters in password are URL-encoded."""
    from db.url import build_db_url

    with patch.dict(os.environ, {"DB_PASS": "p@ss/w0rd"}):
        url = build_db_url()
        # The password should be percent-encoded (both @ and / encoded)
        assert "p%40ss%2Fw0rd" in url
        # Raw password not in the URL
        assert "p@ss/w0rd" not in url


def test_build_db_url_rejects_unsupported_driver():
    """Test that unsupported DB_DRIVER raises ValueError."""
    from db.url import build_db_url

    with patch.dict(os.environ, {"DB_DRIVER": "mysql+pymysql"}):
        try:
            build_db_url()
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "mysql+pymysql" in str(e)
            assert "postgresql+psycopg" in str(e)


def test_get_db_url_is_lazy():
    """Test that get_db_url builds on first call and caches."""
    import db.url as url_module
    from db.url import get_db_url

    # Reset the cache
    url_module._db_url = None

    with patch.dict(os.environ, {"DB_DATABASE": "lazy_test_db"}):
        url1 = get_db_url()
        assert "lazy_test_db" in url1
        # Second call should return the cached value (not re-read env)
        with patch.dict(os.environ, {"DB_DATABASE": "changed_db"}):
            url2 = get_db_url()
            assert url2 == url1  # cached, not rebuilt

    # Reset for other tests
    url_module._db_url = None
