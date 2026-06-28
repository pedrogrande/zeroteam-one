"""
Parse exported Agno session markdown files into structured session data.

Each markdown file has:
  - A header table with session metadata (Session, Type, Agent, User, Created, Runs)
  - Multiple Run sections, each with:
    - Run header: "## Run N — AgentName ✓/✗ STATUS"
    - Timestamp line: "*YYYY-MM-DDTHH:MM:SS* · `model` · `run_id...`"
    - ### Prompt section (user input)
    - ### Response section (agent output)

The filename also encodes the agent name and session ID:
  e.g., "agentic-expert_0e4a4724.md" → agent_name="agentic-expert", session_id="0e4a4724"
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class ParsedRun:
    """A single run within a session."""

    run_index: int  # 1-based
    agent_name: (
        str  # The agent that handled this run (may differ from session agent for teams)
    )
    status: str  # "COMPLETED" or other
    model: str
    run_id: str
    timestamp: str  # ISO 8601
    prompt: str
    response: str

    # Derived
    year: int = 0
    month: int = 0
    prompt_word_count: int = 0
    response_word_count: int = 0
    has_code_blocks: bool = False
    has_tables: bool = False


@dataclass
class ParsedSession:
    """A single parsed Agno session with metadata and runs."""

    filepath: str
    filename_slug: str  # e.g., "agentic-expert_0e4a4724"
    session_id: str  # e.g., "0e4a4724"
    agent_name: str  # From header table (display name)
    agent_name_slug: str  # From filename (e.g., "agentic-expert")
    agent_type: str  # "agent" or "team"
    user_email: str
    created_at: str  # ISO 8601
    run_count: int
    runs: list[ParsedRun] = field(default_factory=list)

    # Filesystem metadata
    file_size_bytes: int = 0

    # Content-derived metadata
    total_word_count: int = 0
    total_prompt_word_count: int = 0
    total_response_word_count: int = 0
    has_code_blocks: bool = False
    has_tables: bool = False
    reading_time_mins: int = 0

    # Derived from created_at
    year: int = 0
    month: int = 0

    @classmethod
    def from_file(cls, filepath: Path) -> "ParsedSession":
        """Parse a single markdown file into a ParsedSession."""
        filepath = Path(filepath)
        content = filepath.read_text(encoding="utf-8")
        stat = filepath.stat()

        # Extract agent_name_slug and session_id from filename
        # e.g., "agentic-expert_0e4a4724.md" → slug="agentic-expert", id="0e4a4724"
        stem = filepath.stem
        parts = stem.rsplit("_", 1)
        if len(parts) == 2 and len(parts[1]) >= 8:
            agent_name_slug = parts[0]
            session_id = parts[1]
        else:
            agent_name_slug = stem
            session_id = "unknown"

        # Parse header table
        agent_name = _extract_field(content, "Agent") or agent_name_slug
        agent_type = _extract_field(content, "Type") or "unknown"
        user_email = _extract_field(content, "User") or ""
        created_at = _extract_field(content, "Created") or ""
        runs_field = _extract_field(content, "Runs") or ""

        # Extract session_id from header if available (overrides filename)
        header_session_id = _extract_field(content, "Session")
        if header_session_id:
            # Remove trailing "..." if present
            header_session_id = header_session_id.rstrip(".")
            if len(header_session_id) >= 8:
                session_id = header_session_id

        # Parse runs
        runs = _parse_runs(content)

        # Derive year/month from created_at
        year, month = _parse_year_month(created_at)

        # Content-derived metadata
        total_word_count = len(content.split())
        total_prompt_word_count = sum(r.prompt_word_count for r in runs)
        total_response_word_count = sum(r.response_word_count for r in runs)
        has_code_blocks = bool(re.search(r"```\w*\n", content))
        has_tables = bool(re.search(r"\|.*\|.*\|", content))
        reading_time_mins = max(1, round(total_word_count / 200))

        return cls(
            filepath=str(filepath),
            filename_slug=stem,
            session_id=session_id,
            agent_name=agent_name,
            agent_name_slug=agent_name_slug,
            agent_type=agent_type,
            user_email=user_email,
            created_at=created_at,
            run_count=len(runs),
            runs=runs,
            file_size_bytes=stat.st_size,
            total_word_count=total_word_count,
            total_prompt_word_count=total_prompt_word_count,
            total_response_word_count=total_response_word_count,
            has_code_blocks=has_code_blocks,
            has_tables=has_tables,
            reading_time_mins=reading_time_mins,
            year=year,
            month=month,
        )


def parse_directory(directory: Path, limit: int = 0) -> list[ParsedSession]:
    """Parse all .md files in a directory into ParsedSession objects.

    Args:
        directory: Path to directory containing .md session files.
        limit: Maximum number of files to process (0 = all).

    Returns:
        List of ParsedSession objects, sorted by filename.
    """
    directory = Path(directory)
    md_files = sorted(directory.glob("*.md"))

    # Skip .DS_Store and other non-session files
    md_files = [f for f in md_files if not f.name.startswith(".")]

    if limit > 0:
        md_files = md_files[:limit]

    sessions = []
    for filepath in md_files:
        try:
            session = ParsedSession.from_file(filepath)
            sessions.append(session)
        except Exception as e:
            print(f"  ⚠️  Failed to parse {filepath.name}: {e}")

    return sessions


# ── Private helpers ─────────────────────────────────────────────────────────


def _extract_field(content: str, field_name: str) -> Optional[str]:
    """Extract a field value from the header table.

    The header table has rows like:
        | **Session** | `0e4a4724...` |
        | **Agent** | Agentic Expert |
    """
    pattern = rf"\|\s*\*\*{field_name}\*\*\s*\|\s*(.+?)\s*\|"
    match = re.search(pattern, content)
    if match:
        value = match.group(1).strip()
        # Remove markdown backticks wrapping the value
        value = re.sub(r"^`(.+)`$", r"\1", value)
        return value
    return None


def _parse_runs(content: str) -> list[ParsedRun]:
    """Parse all Run sections from the markdown content.

    Run sections look like:
        ## Run 1 — Agentic Expert ✓ COMPLETED

        *2026-04-26T08:09:58* · `glm-5.1:cloud` · `1a8feb35...`

        ### Prompt

        (user prompt text)

        ### Response

        (agent response text)
    """
    runs = []

    # Split on run headers: "## Run N — ..."
    # Status markers: ✓ COMPLETED, ✗ FAILED, ⚠️ ERROR, ⚠ ERROR
    run_pattern = re.compile(
        r"^##\s+Run\s+(\d+)\s+—\s+(.+?)\s*[✓✗⚠️⚠]\s*(\w+)\s*$",
        re.MULTILINE,
    )

    # Find all run header positions
    run_headers = list(run_pattern.finditer(content))

    for i, match in enumerate(run_headers):
        run_index = int(match.group(1))
        agent_name = match.group(2).strip()
        status = match.group(3).strip()

        # Extract the content between this run header and the next (or end of file)
        start_pos = match.end()
        end_pos = (
            run_headers[i + 1].start() if i + 1 < len(run_headers) else len(content)
        )
        run_content = content[start_pos:end_pos]

        # Parse timestamp line: *2026-04-26T08:09:58* · `glm-5.1:cloud` · `1a8feb35...`
        ts_match = re.search(
            r"\*(\d{4}-\d{2}-\d{2}T[\d:]+)\*\s*·\s*`([^`]+)`\s*·\s*`([^`]+)`",
            run_content,
        )
        timestamp = ts_match.group(1) if ts_match else ""
        model = ts_match.group(2) if ts_match else "unknown"
        run_id = ts_match.group(3) if ts_match else "unknown"
        # Remove trailing "..." from run_id if present
        if run_id.endswith("..."):
            run_id = run_id[:-3]

        # Extract prompt and response sections
        prompt = _extract_section(run_content, "Prompt")
        response = _extract_section(run_content, "Response")

        # Derived metadata
        year, month = _parse_year_month(timestamp)
        prompt_word_count = len(prompt.split()) if prompt else 0
        response_word_count = len(response.split()) if response else 0
        has_code_blocks = bool(re.search(r"```\w*\n", run_content))
        has_tables = bool(re.search(r"\|.*\|.*\|", run_content))

        runs.append(
            ParsedRun(
                run_index=run_index,
                agent_name=agent_name,
                status=status,
                model=model,
                run_id=run_id,
                timestamp=timestamp,
                prompt=prompt,
                response=response,
                year=year,
                month=month,
                prompt_word_count=prompt_word_count,
                response_word_count=response_word_count,
                has_code_blocks=has_code_blocks,
                has_tables=has_tables,
            )
        )

    return runs


def _extract_section(content: str, section_name: str) -> str:
    """Extract the content of a ### Prompt or ### Response section.

    Sections are delimited by ### headers or the next ## Run header.
    """
    # Match "### Prompt" or "### Response" and capture until the next ### or ## header
    pattern = rf"^###\s+{section_name}\s*\n(.*?)(?=^###|\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def _parse_year_month(timestamp: str) -> tuple[int, int]:
    """Extract year and month from an ISO 8601 timestamp string."""
    if not timestamp:
        return (0, 0)
    try:
        # Handle various formats: "2026-04-26T08:09:58", "2026-04-26"
        dt = datetime.fromisoformat(timestamp.replace("Z", ""))
        return (dt.year, dt.month)
    except (ValueError, TypeError):
        return (0, 0)
