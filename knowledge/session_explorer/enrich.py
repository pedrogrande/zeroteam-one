"""
Enrich parsed sessions with additional metadata.

Phase 1 enrichment: filename + filesystem + computed content stats.
Phase 2 (deferred): LLM-derived topic_tags and dominant_entities.

This module provides functions to add computed metadata to ParsedSession
objects before they are chunked and ingested.
"""

import re
from typing import Optional

from .parse import ParsedRun, ParsedSession


def enrich_session(session: ParsedSession) -> ParsedSession:
    """Enrich a ParsedSession with additional computed metadata.

    Phase 1: All metadata is derived from filename, frontmatter, and content analysis.
    No LLM calls — fast, deterministic, and free.

    Args:
        session: A parsed Agno session.

    Returns:
        The same session object with enriched fields.
    """
    # Enrich each run
    for run in session.runs:
        _enrich_run(run)

    # Recompute session-level aggregates from enriched runs
    session.total_prompt_word_count = sum(r.prompt_word_count for r in session.runs)
    session.total_response_word_count = sum(r.response_word_count for r in session.runs)
    session.total_word_count = (
        session.total_prompt_word_count + session.total_response_word_count
    )
    session.has_code_blocks = any(r.has_code_blocks for r in session.runs)
    session.has_tables = any(r.has_tables for r in session.runs)
    session.reading_time_mins = max(1, round(session.total_word_count / 200))

    # Derive year/month from created_at if not already set
    if session.year == 0 and session.created_at:
        from .parse import _parse_year_month

        session.year, session.month = _parse_year_month(session.created_at)

    return session


def enrich_sessions(sessions: list[ParsedSession]) -> list[ParsedSession]:
    """Enrich multiple sessions with computed metadata."""
    return [enrich_session(s) for s in sessions]


def _enrich_run(run: ParsedRun) -> None:
    """Enrich a single run with computed metadata (in-place)."""
    # Word counts (recalculate in case content was modified)
    run.prompt_word_count = len(run.prompt.split()) if run.prompt else 0
    run.response_word_count = len(run.response.split()) if run.response else 0

    # Content flags
    combined = f"{run.prompt}\n{run.response}"
    run.has_code_blocks = bool(re.search(r"```\w*\n", combined))
    run.has_tables = bool(re.search(r"\|.*\|.*\|", combined))

    # Derive year/month from timestamp if not already set
    if run.year == 0 and run.timestamp:
        from .parse import _parse_year_month

        run.year, run.month = _parse_year_month(run.timestamp)
