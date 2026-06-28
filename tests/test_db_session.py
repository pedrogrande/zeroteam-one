"""Tests for db/session.py — factory functions."""

import os
from unittest.mock import patch


def test_get_postgres_db_returns_postgresdb():
    """Test that get_postgres_db returns a PostgresDb instance."""
    from agno.db.postgres import PostgresDb

    from db.session import get_postgres_db

    db = get_postgres_db()
    assert isinstance(db, PostgresDb)


def test_get_postgres_db_with_contents_table():
    """Test that contents_table parameter creates a knowledge-aware PostgresDb."""
    from agno.db.postgres import PostgresDb

    from db.session import get_postgres_db

    db = get_postgres_db(contents_table="test_contents")
    assert isinstance(db, PostgresDb)


def test_create_knowledge_returns_knowledge():
    """Test that create_knowledge returns a Knowledge instance."""
    from agno.knowledge import Knowledge

    from db.session import create_knowledge

    knowledge = create_knowledge(name="test_kb", table_name="test_vectors")
    assert isinstance(knowledge, Knowledge)


def test_create_knowledge_raises_without_openai_key():
    """Test that create_knowledge raises RuntimeError when OPENAI_API_KEY is unset."""
    from db.session import create_knowledge

    with patch.dict(os.environ, {}, clear=True):
        try:
            create_knowledge(name="test_kb", table_name="test_vectors")
            assert False, "Should have raised RuntimeError"
        except RuntimeError as e:
            assert "OPENAI_API_KEY" in str(e)


def test_create_studio_knowledge_returns_knowledge_with_agentic_pdf_reader():
    """Test that create_studio_knowledge returns a Knowledge with contents_db
    and a pre-seeded PDFReader using AgenticChunking."""
    from agno.knowledge import Knowledge
    from agno.knowledge.chunking.agentic import AgenticChunking
    from agno.knowledge.reader.pdf_reader import PDFReader
    from agno.vectordb.pgvector import PgVector, SearchType

    from db.session import create_studio_knowledge

    knowledge = create_studio_knowledge(
        name="studio_kb",
        table_name="studio_vectors",
        description="A Studio knowledge base.",
    )
    assert isinstance(knowledge, Knowledge)
    assert knowledge.name == "studio_kb"
    assert knowledge.description == "A Studio knowledge base."
    # contents_db is required for Studio resolution
    assert knowledge.contents_db is not None
    # PgVector with hybrid search
    assert isinstance(knowledge.vector_db, PgVector)
    assert knowledge.vector_db.search_type == SearchType.hybrid
    # Pre-seeded PDF reader with AgenticChunking under the "pdf" key
    assert knowledge.readers is not None
    pdf_reader = knowledge.readers.get("pdf")
    assert isinstance(pdf_reader, PDFReader)
    assert isinstance(pdf_reader.chunking_strategy, AgenticChunking)


def test_create_studio_knowledge_raises_without_openai_key():
    """Test that create_studio_knowledge raises RuntimeError when OPENAI_API_KEY is unset."""
    from db.session import create_studio_knowledge

    with patch.dict(os.environ, {}, clear=True):
        try:
            create_studio_knowledge(name="studio_kb", table_name="studio_vectors")
            assert False, "Should have raised RuntimeError"
        except RuntimeError as e:
            assert "OPENAI_API_KEY" in str(e)
