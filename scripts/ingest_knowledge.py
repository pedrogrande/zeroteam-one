#!/usr/bin/env python3
"""
Ingest Content into a Studio Knowledge Base
===========================================

Reusable CLI that ingests files from a directory into one of the Studio
knowledge bases defined in ``db/knowledge_bases.py``.

The knowledge bases are registered with the AgentOS Studio Registry, so
once ingested the content is searchable from any Studio-composed agent,
team, or workflow that selects the KB.

Usage
-----
    source .venv/bin/activate

    # Ingest all *.md files from project-docs/agent-design/ into "Agent Design"
    python scripts/ingest_knowledge.py "Agent Design" project-docs/agent-design
    python scripts/ingest_knowledge.py "AI Assisted Learning" project-docs/ai-assisted-learning

    # Ingest PDFs (and markdown) from a folder into "AgentOS Lab"
    python scripts/ingest_knowledge.py "AgentOS Lab" path/to/docs --include "*.pdf" "*.md"

    # List the available knowledge bases
    python scripts/ingest_knowledge.py --list

Requirements
------------
- ``OPENAI_API_KEY`` set (in ``.env`` or the shell) — needed for embeddings.
- Postgres + pgvector reachable at the configured ``DB_*`` env vars
  (``docker compose up -d zeroedge-db`` for local dev).

Idempotent
----------
Re-running is safe. By default ``skip_if_exists=True`` skips files whose
content hash is already in the vector DB — the cheap path for re-runs (no
re-embedding of unchanged files). Pass ``--no-skip-if-exists`` to re-embed
and upsert in place when you've edited files and want them refreshed.

Reader selection
----------------
Per-file reader selection is automatic via ``ReaderFactory`` based on file
extension (``.md`` → ``MarkdownReader``, ``.pdf`` → ``PDFReader``). Each
Studio KB pre-seeds a ``PDFReader(chunking_strategy=AgenticChunking())``
under the ``pdf`` key, so PDFs are chunked semantically. Markdown uses
``MarkdownChunking`` (header-aware). Pass ``--reader`` to force a specific
reader on every file (rarely needed).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Load .env before importing modules that read env vars at import time.
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from evals.dotenv import load_dotenv  # noqa: E402

load_dotenv()

import os  # noqa: E402

from agno.knowledge.knowledge import Knowledge  # noqa: E402
from agno.knowledge.reader.base import Reader  # noqa: E402

from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES  # noqa: E402

# ---------------------------------------------------------------------------
# KB lookup — name → Knowledge instance
# ---------------------------------------------------------------------------
_KB_BY_NAME: dict[str, Knowledge] = {kb.name: kb for kb in STUDIO_KNOWLEDGE_BASES}


def list_knowledge_bases() -> int:
    """Print the available Studio knowledge bases and exit."""
    if not _KB_BY_NAME:
        print("No Studio knowledge bases registered.", file=sys.stderr)
        return 1
    print("Available Studio knowledge bases:")
    for name, kb in _KB_BY_NAME.items():
        table = getattr(kb.vector_db, "table_name", "?")
        desc = (kb.description or "").strip().replace("\n", " ")
        if len(desc) > 80:
            desc = desc[:77] + "..."
        print(f"  - {name}  (table: {table})")
        if desc:
            print(f"      {desc}")
    return 0


def _resolve_path(path_str: str) -> Path:
    """Resolve a path argument relative to the repo root if not absolute."""
    p = Path(path_str)
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    return p


def _build_reader(reader_name: Optional[str]) -> Optional[Reader]:
    """Build a reader instance from a name hint, or None to use auto-selection."""
    if reader_name is None:
        return None
    from agno.knowledge.reader.reader_factory import ReaderFactory

    # Map common aliases to reader keys.
    aliases = {
        "pdf": "pdf",
        "markdown": "markdown",
        "md": "markdown",
        "csv": "csv",
        "json": "json",
        "text": "text",
        "txt": "text",
    }
    key = aliases.get(reader_name.lower(), reader_name.lower())
    return ReaderFactory.create_reader(key)


def ingest(
    kb_name: str,
    source: str,
    includes: list[str],
    reader_name: Optional[str],
    skip_if_exists: bool = True,
    upsert: bool = True,
) -> int:
    """Ingest files from ``source`` into the named knowledge base.

    ``skip_if_exists=True`` (the default) skips re-processing files whose
    content hash is already in the vector DB — the cheap path for re-runs.
    ``upsert`` only applies when ``skip_if_exists`` is False: with
    ``upsert=True`` unchanged files are re-embedded and updated in place;
    with ``upsert=False`` a hash collision on existing content raises
    instead of updating.
    """
    # Guard: OpenAI key must be present for embeddings.
    if not os.getenv("OPENAI_API_KEY"):
        print(
            "ERROR: OPENAI_API_KEY is not set. Set it in .env or export it "
            "before running this script.",
            file=sys.stderr,
        )
        return 1

    # Guard: KB must exist.
    kb = _KB_BY_NAME.get(kb_name)
    if kb is None:
        print(
            f"ERROR: no Studio knowledge base named {kb_name!r}.\n"
            f"Available: {', '.join(_KB_BY_NAME) or '(none)'}",
            file=sys.stderr,
        )
        return 1

    # Guard: source must exist.
    source_path = _resolve_path(source)
    if not source_path.exists():
        print(f"ERROR: source path not found: {source_path}", file=sys.stderr)
        return 1

    # Collect the files that match the include patterns.
    if source_path.is_file():
        files = [source_path]
        includes = includes or [f"*{source_path.suffix}"]
    elif source_path.is_dir():
        if not includes:
            includes = ["*.md"]
        files = sorted(
            f
            for f in source_path.iterdir()
            if f.is_file() and any(f.match(pat) for pat in includes)
        )
    else:
        print(
            f"ERROR: source is neither file nor directory: {source_path}",
            file=sys.stderr,
        )
        return 1

    if not files:
        print(
            f"ERROR: no files matching {includes} found in {source_path}",
            file=sys.stderr,
        )
        return 1

    reader = _build_reader(reader_name)

    print(f"Ingesting {len(files)} file(s) from {source_path}")
    print(f"  → knowledge base: {kb.name!r}")
    print(f"  → vector table:   {getattr(kb.vector_db, 'table_name', '?')}")
    print(f"  → contents table: {getattr(kb.contents_db, 'knowledge_table_name', '?')}")
    print(f"  → include:        {includes}")
    if reader is not None:
        print(f"  → reader:         {reader.__class__.__name__}")
    print(f"  → skip_if_exists: {skip_if_exists}")
    print(
        f"  → upsert:         {upsert if not skip_if_exists else '(n/a — skip wins)'}"
    )
    print()

    # Knowledge.insert(path=<dir>) iterates the directory and inserts each
    # file, applying the include glob. Per-file reader selection is automatic
    # via ReaderFactory unless an explicit reader is provided.
    # - skip_if_exists=True: skip files whose content hash is already in the
    #   vector DB (cheap re-runs, no re-embedding).
    # - upsert=True (default, only when not skipping): re-embed and update in
    #   place on hash collision.
    kb.insert(
        path=str(source_path),
        include=includes,
        reader=reader,
        skip_if_exists=skip_if_exists,
        upsert=upsert,
    )

    # Summarise what's now in the KB.
    contents, total = kb.get_content(limit=100, page=1)
    print(f"Done. Knowledge base now holds {total} content row(s):")
    for c in contents:
        print(f"  - {c.name}  [{c.status}]")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ingest files from a directory into a Studio knowledge base.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "kb_name",
        nargs="?",
        help='Knowledge base name (e.g. "Agent Design"). Use --list to see options.',
    )
    parser.add_argument(
        "source",
        nargs="?",
        help="Directory or file to ingest from (relative paths resolve against the repo root).",
    )
    parser.add_argument(
        "--include",
        nargs="+",
        default=None,
        metavar="GLOB",
        help="Glob patterns to include (default: *.md). Example: --include '*.pdf' '*.md'",
    )
    parser.add_argument(
        "--reader",
        default=None,
        metavar="NAME",
        help="Force a reader for every file (pdf, markdown, csv, json, text). "
        "Default: auto-select per file extension.",
    )
    parser.add_argument(
        "--no-skip-if-exists",
        action="store_true",
        help="Re-process every file, even if its content hash is already in the "
        "vector DB. Use this when you've edited files and want them refreshed "
        "(re-embedded and upserted in place). Default: skip unchanged files.",
    )
    parser.add_argument(
        "--no-upsert",
        action="store_true",
        help="With upsert=False (and --no-skip-if-exists), a hash collision on "
        "existing content raises instead of updating in place. Rarely needed.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List the available Studio knowledge bases and exit.",
    )
    args = parser.parse_args(argv)

    if args.list:
        return list_knowledge_bases()

    if not args.kb_name or not args.source:
        parser.error("kb_name and source are required (or use --list)")

    return ingest(
        args.kb_name,
        args.source,
        args.include or [],
        args.reader,
        skip_if_exists=not args.no_skip_if_exists,
        upsert=not args.no_upsert,
    )


if __name__ == "__main__":
    raise SystemExit(main())
