"""Tests for db/knowledge_bases.py — Studio domain knowledge bases."""

import os
from unittest.mock import patch


def test_studio_knowledge_bases_has_six_unique_instances():
    """Six domain KBs, each a Knowledge with a unique name and contents_db."""
    from agno.knowledge import Knowledge

    from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES

    assert len(STUDIO_KNOWLEDGE_BASES) == 6
    names = [kb.name for kb in STUDIO_KNOWLEDGE_BASES]
    assert len(names) == len(set(names)), f"Duplicate KB names: {names}"
    for kb in STUDIO_KNOWLEDGE_BASES:
        assert isinstance(kb, Knowledge)
        assert kb.name is not None
        assert kb.description is not None
        # contents_db is required for Studio resolution
        assert kb.contents_db is not None


def test_studio_knowledge_bases_expected_names():
    """The five domain names match the plan."""
    from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES

    names = {kb.name for kb in STUDIO_KNOWLEDGE_BASES}
    assert names == {
        "AI Assisted Learning",
        "Agent Design",
        "Agentic Workflow Design",
        "User Profile Information",
        "AgentOS Lab",
        "Task Contract",
    }


def test_studio_knowledge_bases_each_has_agentic_pdf_reader():
    """Every Studio KB pre-seeds a PDFReader with AgenticChunking."""
    from agno.knowledge.chunking.agentic import AgenticChunking
    from agno.knowledge.reader.pdf_reader import PDFReader

    from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES

    for kb in STUDIO_KNOWLEDGE_BASES:
        assert kb.readers is not None, f"{kb.name}: readers dict is None"
        pdf_reader = kb.readers.get("pdf")
        assert isinstance(pdf_reader, PDFReader), f"{kb.name}: no PDFReader"
        assert isinstance(
            pdf_reader.chunking_strategy, AgenticChunking
        ), f"{kb.name}: chunking strategy is not AgenticChunking"


def test_studio_knowledge_bases_raises_without_openai_key():
    """Importing db.knowledge_bases without OPENAI_API_KEY raises RuntimeError."""
    with patch.dict(os.environ, {}, clear=True):
        # Force a fresh import so the module-level KBs are (re)constructed.
        import sys

        sys.modules.pop("db.knowledge_bases", None)
        try:
            import db.knowledge_bases  # noqa: F401

            assert False, "Should have raised RuntimeError"
        except RuntimeError as e:
            assert "OPENAI_API_KEY" in str(e)
        finally:
            # Restore the real module for subsequent tests
            sys.modules.pop("db.knowledge_bases", None)
