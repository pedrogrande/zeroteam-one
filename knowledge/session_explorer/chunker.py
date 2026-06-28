"""
Chunk parsed Agno sessions into run-level chunks for vector embedding.

Run-level chunking preserves the prompt+response context that makes
agent sessions meaningful. Each chunk contains one user prompt and
its corresponding agent response, keeping semantic intent intact.

Strategies:
  - "run": Each prompt+response exchange is one chunk (default, best for search)
  - "session_summary": One chunk per full session (best for topic clustering)
  - "hybrid": Store both, use chunk_type metadata to filter at query time
"""

from dataclasses import dataclass, field
from typing import Optional

from .parse import ParsedSession


@dataclass
class Chunk:
    """A single chunk of an Agno session, ready for embedding."""

    session_id: str
    agent_name: str  # Display name from header (e.g., "Agentic Expert")
    agent_name_slug: str  # Slug from filename (e.g., "agentic-expert")
    agent_type: str  # "agent" or "team"
    chunk_type: str  # "run" | "session_summary"
    chunk_index: (
        int  # run number within session (0-based for session_summary, 1-based for runs)
    )
    text: str  # the chunk content

    # Metadata for filtering
    year: int = 0
    month: int = 0
    user_email: str = ""
    model: str = ""
    run_status: str = ""  # COMPLETED, etc.
    word_count: int = 0
    prompt_word_count: int = 0
    response_word_count: int = 0
    has_code_blocks: bool = False
    has_tables: bool = False
    file_size_bytes: int = 0
    filename_slug: str = ""
    reading_time_mins: int = 0
    run_count: int = 0  # total runs in the session

    def to_metadata(self) -> dict:
        """Convert to Agno-compatible metadata dict for Knowledge.insert()."""
        return {
            "session_id": self.session_id,
            "agent_name": self.agent_name,
            "agent_name_slug": self.agent_name_slug,
            "agent_type": self.agent_type,
            "chunk_type": self.chunk_type,
            "chunk_index": self.chunk_index,
            "year": self.year,
            "month": self.month,
            "user_email": self.user_email,
            "model": self.model,
            "run_status": self.run_status,
            "word_count": self.word_count,
            "prompt_word_count": self.prompt_word_count,
            "response_word_count": self.response_word_count,
            "has_code_blocks": self.has_code_blocks,
            "has_tables": self.has_tables,
            "file_size_bytes": self.file_size_bytes,
            "filename_slug": self.filename_slug,
            "reading_time_mins": self.reading_time_mins,
            "run_count": self.run_count,
        }


def chunk_session(session: ParsedSession, strategy: str = "run") -> list[Chunk]:
    """Chunk a single session according to the chosen strategy.

    Args:
        session: A parsed Agno session.
        strategy: "run", "session_summary", or "hybrid".

    Returns:
        List of Chunk objects.
    """
    if strategy == "run":
        return _chunk_runs(session)
    elif strategy == "session_summary":
        return _chunk_session_summary(session)
    elif strategy == "hybrid":
        return _chunk_runs(session) + _chunk_session_summary(session)
    else:
        raise ValueError(f"Unknown chunking strategy: {strategy}")


def chunk_sessions(sessions: list[ParsedSession], strategy: str = "run") -> list[Chunk]:
    """Chunk multiple sessions.

    Args:
        sessions: List of parsed Agno sessions.
        strategy: "run", "session_summary", or "hybrid".

    Returns:
        List of all chunks from all sessions.
    """
    chunks = []
    for session in sessions:
        chunks.extend(chunk_session(session, strategy=strategy))
    return chunks


# ── Private helpers ─────────────────────────────────────────────────────────


def _chunk_runs(session: ParsedSession) -> list[Chunk]:
    """Create one chunk per run (prompt+response pair).

    This preserves the conversational context — each chunk contains
    what the user asked and how the agent responded.
    """
    chunks = []

    for run in session.runs:
        # Build the chunk text: prompt + response with clear section markers
        text_parts = []
        if run.prompt:
            text_parts.append(f"## Prompt\n\n{run.prompt}")
        if run.response:
            text_parts.append(f"## Response\n\n{run.response}")

        text = "\n\n".join(text_parts) if text_parts else ""

        if not text.strip():
            continue  # Skip empty chunks

        chunk = Chunk(
            session_id=session.session_id,
            agent_name=run.agent_name or session.agent_name,
            agent_name_slug=session.agent_name_slug,
            agent_type=session.agent_type,
            chunk_type="run",
            chunk_index=run.run_index,
            text=text,
            year=run.year or session.year,
            month=run.month or session.month,
            user_email=session.user_email,
            model=run.model,
            run_status=run.status,
            word_count=run.prompt_word_count + run.response_word_count,
            prompt_word_count=run.prompt_word_count,
            response_word_count=run.response_word_count,
            has_code_blocks=run.has_code_blocks,
            has_tables=run.has_tables,
            file_size_bytes=session.file_size_bytes,
            filename_slug=session.filename_slug,
            reading_time_mins=session.reading_time_mins,
            run_count=session.run_count,
        )
        chunks.append(chunk)

    return chunks


def _chunk_session_summary(session: ParsedSession) -> list[Chunk]:
    """Create one chunk per full session.

    This is useful for topic clustering and finding sessions about a theme,
    but loses the granularity of individual prompt+response pairs.
    """
    # Build the full session text
    text_parts = [
        f"# {session.agent_name}",
        "",
        f"Session: {session.session_id}",
        f"Type: {session.agent_type}",
        f"Created: {session.created_at}",
        f"Runs: {session.run_count}",
        "",
    ]

    for run in session.runs:
        text_parts.append(f"## Run {run.run_index} — {run.agent_name} {run.status}")
        text_parts.append("")
        if run.prompt:
            text_parts.append(f"### Prompt")
            text_parts.append("")
            text_parts.append(run.prompt)
            text_parts.append("")
        if run.response:
            text_parts.append(f"### Response")
            text_parts.append("")
            text_parts.append(run.response)
            text_parts.append("")

    text = "\n".join(text_parts)

    if not text.strip():
        return []

    return [
        Chunk(
            session_id=session.session_id,
            agent_name=session.agent_name,
            agent_name_slug=session.agent_name_slug,
            agent_type=session.agent_type,
            chunk_type="session_summary",
            chunk_index=0,
            text=text,
            year=session.year,
            month=session.month,
            user_email=session.user_email,
            model=session.runs[0].model if session.runs else "unknown",
            run_status=(
                ", ".join(set(r.status for r in session.runs)) if session.runs else ""
            ),
            word_count=session.total_word_count,
            prompt_word_count=session.total_prompt_word_count,
            response_word_count=session.total_response_word_count,
            has_code_blocks=session.has_code_blocks,
            has_tables=session.has_tables,
            file_size_bytes=session.file_size_bytes,
            filename_slug=session.filename_slug,
            reading_time_mins=session.reading_time_mins,
            run_count=session.run_count,
        )
    ]
