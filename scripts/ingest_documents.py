#!/usr/bin/env python3
"""
Ingest Multi-Format Documents into a Studio Knowledge Base
==========================================================

Generic ingestion CLI that handles mixed file types — markdown, PDF,
DOCX, HTML — using Agno's built-in readers with format-appropriate
chunking strategies. Writes to any Studio knowledge base by name.

Unlike ``knowledge/session_explorer/ingest.py`` (which is purpose-built
for structured Agno session exports with parse → enrich → chunk), this
script delegates chunking to Agno's readers — each format gets its
optimal chunking strategy:

  - .md   → MarkdownReader + MarkdownChunking (split on H1/H2)
  - .pdf  → PDFReader + DocumentChunking
  - .docx → DocxReader + DocumentChunking
  - .html → BeautifulSoup text extraction + DocumentChunking

Idempotent: ``skip_if_exists=True`` skips files whose content hash is
already in the vector DB.

Usage
-----
    source .venv/bin/activate

    # Ingest all supported files from a directory into "Agno Sessions"
    python scripts/ingest_documents.py "Agno Sessions" knowledge/exported_agno_sessions/markdown_sessions

    # Restrict to specific file types
    python scripts/ingest_documents.py "Agno Sessions" path/to/docs --include "*.md" "*.docx"

    # List available knowledge bases
    python scripts/ingest_documents.py --list

Requirements
------------
- ``OPENAI_API_KEY`` set (in ``.env`` or the shell) — needed for embeddings.
- Postgres + pgvector reachable at the configured ``DB_*`` env vars.
- ``python-docx`` and ``beautifulsoup4`` installed (in pyproject.toml).
"""

from __future__ import annotations

import argparse
import asyncio
import os
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

from agno.knowledge.chunking.document import DocumentChunking  # noqa: E402
from agno.knowledge.knowledge import Knowledge  # noqa: E402
from agno.knowledge.reader.docx_reader import DocxReader  # noqa: E402
from agno.knowledge.reader.markdown_reader import MarkdownReader  # noqa: E402
from agno.knowledge.reader.pdf_reader import PDFReader  # noqa: E402

from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES  # noqa: E402

# MarkdownChunking requires the ``unstructured`` package. Try to import it;
# if unavailable, fall back to DocumentChunking for markdown files.
try:
    from agno.knowledge.chunking.markdown import MarkdownChunking  # noqa: E402

    _MARKDOWN_CHUNKING_AVAILABLE = True
except ImportError:
    _MARKDOWN_CHUNKING_AVAILABLE = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# File extensions this script handles. Everything else is skipped.
SUPPORTED_EXTENSIONS = {".md", ".pdf", ".docx", ".doc", ".html", ".htm"}

# Extensions to always skip (even if they match an include glob).
SKIP_EXTENSIONS = {".py", ".sh", ".json", ".csv", ".xlsx", ".xls", ".pptx"}

# Batch delay between files to avoid overwhelming the embedder API.
INTER_FILE_DELAY_SECS = 0.3

# ---------------------------------------------------------------------------
# KB lookup — name → Knowledge instance
# ---------------------------------------------------------------------------
_KB_BY_NAME: dict[str, Knowledge] = {kb.name: kb for kb in STUDIO_KNOWLEDGE_BASES}


# ---------------------------------------------------------------------------
# File classification — lightweight filename-based source_type tagging
# ---------------------------------------------------------------------------

_CHAT_KEYWORDS = {"chat", "transcript", "meeting", "call"}
_FRAMEWORK_KEYWORDS = {"strategy", "framework", "principles", "policy", "manifesto"}


def classify_source_type(filepath: Path) -> str:
    """Tag a file with a ``source_type`` based on filename heuristics.

    The tag is stored as metadata and is filterable at query time via
    the ``KnowledgeContextProvider`` scope parameter.
    """
    name_lower = filepath.stem.lower()

    if any(kw in name_lower for kw in _CHAT_KEYWORDS):
        return "chat_export"
    if any(kw in name_lower for kw in _FRAMEWORK_KEYWORDS):
        return "framework_doc"

    ext = filepath.suffix.lower()
    if ext in (".docx", ".doc", ".pdf"):
        return "document"
    if ext in (".html", ".htm"):
        return "web_page"
    return "document"


# ---------------------------------------------------------------------------
# Reader selection — per-extension reader with optimal chunking
# ---------------------------------------------------------------------------


def build_reader(filepath: Path):
    """Return the appropriate Agno reader for the file type.

    Each reader is configured with a chunking strategy suited to its format:
      - .md   → MarkdownReader + MarkdownChunking(split_on_headings=2)
      - .pdf  → PDFReader + DocumentChunking
      - .docx → DocxReader + DocumentChunking
      - .html → handled separately (text extraction, no reader)
    """
    ext = filepath.suffix.lower()

    if ext in (".md", ".markdown"):
        if _MARKDOWN_CHUNKING_AVAILABLE:
            return MarkdownReader(
                chunking_strategy=MarkdownChunking(split_on_headings=2),
            )
        # Fallback: DocumentChunking (structure-aware, no extra deps)
        return MarkdownReader(
            chunking_strategy=DocumentChunking(),
        )
    if ext == ".pdf":
        return PDFReader(
            chunking_strategy=DocumentChunking(),
        )
    if ext in (".docx", ".doc"):
        return DocxReader(
            chunking_strategy=DocumentChunking(),
        )
    if ext in (".html", ".htm"):
        return None  # HTML handled via text extraction, not a reader

    return None


# ---------------------------------------------------------------------------
# HTML text extraction
# ---------------------------------------------------------------------------


def extract_html_text(filepath: Path) -> str:
    """Extract readable text from an HTML file using BeautifulSoup.

    Strips script/style tags, converts block elements to newlines, and
    returns clean text suitable for embedding.
    """
    from bs4 import BeautifulSoup

    raw = filepath.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw, "html.parser")

    # Remove non-content tags
    for tag in soup(["script", "style", "noscript", "meta", "link", "head"]):
        tag.decompose()

    # Get text with line breaks for block elements
    text = soup.get_text(separator="\n", strip=True)

    # Collapse excessive blank lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n\n".join(lines)


# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------


async def aingest_file(kb: Knowledge, filepath: Path) -> tuple[bool, str]:
    """Ingest a single file into the knowledge base.

    Returns (success, message).
    """
    ext = filepath.suffix.lower()
    source_type = classify_source_type(filepath)
    metadata = {
        "source_type": source_type,
        "filename": filepath.name,
        "file_extension": ext,
    }

    if ext in (".html", ".htm"):
        # HTML: extract text, insert as text_content with DocumentChunking
        try:
            text = extract_html_text(filepath)
            if not text.strip():
                return False, "empty after extraction"
            await kb.ainsert(
                name=filepath.stem[:200],
                text_content=text,
                metadata=metadata,
                skip_if_exists=True,
            )
            return True, f"inserted ({len(text)} chars)"
        except Exception as e:
            return False, str(e)

    # All other formats: use the format-appropriate reader
    reader = build_reader(filepath)
    if reader is None:
        return False, "no reader for extension"

    try:
        await kb.ainsert(
            path=str(filepath),
            reader=reader,
            metadata=metadata,
            skip_if_exists=True,
        )
        return True, "inserted"
    except Exception as e:
        return False, str(e)


async def aingest_directory(
    kb: Knowledge,
    directory: Path,
    includes: list[str],
    limit: int = 0,
) -> None:
    """Ingest all supported files from a directory into the knowledge base.

    Args:
        kb: The target Knowledge instance.
        directory: Path to directory containing files.
        includes: Glob patterns to filter files (e.g. ["*.md", "*.docx"]).
            If empty, all supported extensions are included.
        limit: Maximum number of files to process (0 = all).
    """
    # Collect files
    all_files = sorted(f for f in directory.iterdir() if f.is_file())

    # Filter by include patterns or supported extensions
    if includes:
        matched = []
        for f in all_files:
            if any(f.match(pat) for pat in includes):
                matched.append(f)
    else:
        matched = [f for f in all_files if f.suffix.lower() in SUPPORTED_EXTENSIONS]

    # Exclude files we never want
    matched = [
        f
        for f in matched
        if f.suffix.lower() not in SKIP_EXTENSIONS and not f.name.startswith(".")
    ]

    if limit > 0:
        matched = matched[:limit]

    if not matched:
        print(
            "❌ No matching files found. Check the directory path and include patterns."
        )
        return

    # Summary
    ext_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    for f in matched:
        ext = f.suffix.lower()
        ext_counts[ext] = ext_counts.get(ext, 0) + 1
        st = classify_source_type(f)
        type_counts[st] = type_counts.get(st, 0) + 1

    print(f"📂 Found {len(matched)} file(s) in {directory}")
    print(f"   By extension: {dict(sorted(ext_counts.items(), key=lambda x: -x[1]))}")
    print(
        f"   By source_type: {dict(sorted(type_counts.items(), key=lambda x: -x[1]))}"
    )
    print()

    # Ingest
    total_success = 0
    total_skipped = 0
    total_failed = 0

    for i, filepath in enumerate(matched, 1):
        prefix = f"[{i}/{len(matched)}]"
        print(f"  {prefix} {filepath.name} ...", end=" ", flush=True)

        try:
            success, msg = await aingest_file(kb, filepath)
            if success:
                total_success += 1
                print(f"✅ {msg}")
            else:
                total_failed += 1
                print(f"❌ {msg}")
        except Exception as e:
            total_failed += 1
            print(f"❌ {e}")

        # Small delay between files
        if i < len(matched):
            await asyncio.sleep(INTER_FILE_DELAY_SECS)

    print()
    print(
        f"✅ Done! {total_success} inserted, {total_skipped} skipped, {total_failed} failed"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


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


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ingest multi-format documents (md, pdf, docx, html) into a Studio knowledge base.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "kb_name",
        nargs="?",
        help='Knowledge base name (e.g. "Agno Sessions"). Use --list to see options.',
    )
    parser.add_argument(
        "source",
        nargs="?",
        help="Directory to ingest from (relative paths resolve against the repo root).",
    )
    parser.add_argument(
        "--include",
        nargs="+",
        default=None,
        help='File patterns to include (e.g. "*.md" "*.docx"). Default: all supported types.',
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum number of files to process (0 = all).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available knowledge bases and exit.",
    )

    args = parser.parse_args()

    if args.list:
        return list_knowledge_bases()

    if not args.kb_name or not args.source:
        parser.error("kb_name and source are required (unless using --list)")

    # Guard: OpenAI key must be present for embeddings.
    if not os.getenv("OPENAI_API_KEY"):
        print(
            "ERROR: OPENAI_API_KEY is not set. Set it in .env or export it "
            "before running this script.",
            file=sys.stderr,
        )
        return 1

    # Guard: KB must exist.
    kb = _KB_BY_NAME.get(args.kb_name)
    if kb is None:
        print(
            f"ERROR: no Studio knowledge base named {args.kb_name!r}.\n"
            f"Available: {', '.join(_KB_BY_NAME) or '(none)'}",
            file=sys.stderr,
        )
        return 1

    # Resolve source path
    source_path = Path(args.source)
    if not source_path.is_absolute():
        source_path = (REPO_ROOT / source_path).resolve()

    if not source_path.exists():
        print(f"ERROR: source path not found: {source_path}", file=sys.stderr)
        return 1

    if not source_path.is_dir():
        print(f"ERROR: source is not a directory: {source_path}", file=sys.stderr)
        return 1

    asyncio.run(
        aingest_directory(
            kb, source_path, includes=args.include or [], limit=args.limit
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
