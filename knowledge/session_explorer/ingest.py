"""
Ingest parsed, chunked, and enriched Agno sessions into PgVector.

Usage:
    python -m session_explorer.ingest /path/to/markdown_sessions [--strategy run] [--limit 10]

This script:
1. Parses all .md files in the given directory
2. Enriches them with computed metadata
3. Chunks them into run-level pairs (or chosen strategy)
4. Inserts them into PgVector via Agno Knowledge

Idempotent: uses skip_if_exists=True to avoid duplicates on re-run.
"""

import argparse
import asyncio
import sys
from pathlib import Path

from .chunker import Chunk, chunk_sessions
from .enrich import enrich_sessions
from .parse import parse_directory
from .shared import session_knowledge

# Small delay between batches to avoid overwhelming local Ollama
BATCH_DELAY_SECS = 0.5


def chunks_to_insert_data(chunks: list[Chunk]) -> list[dict]:
    """Convert Chunk objects to Agno Knowledge.insert_many() format.

    Each chunk becomes a dict with:
      - name: human-readable identifier
      - text_content: the chunk text for embedding
      - metadata: all filterable fields
    """
    insert_data = []
    for chunk in chunks:
        if chunk.chunk_type == "run":
            name = (
                f"{chunk.agent_name} — Run {chunk.chunk_index} ({chunk.session_id[:8]})"
            )
        else:
            name = f"{chunk.agent_name} — Session Summary ({chunk.session_id[:8]})"
        # Truncate name to 200 chars for safety
        name = name[:200]

        insert_data.append(
            {
                "name": name,
                "text_content": chunk.text,
                "metadata": chunk.to_metadata(),
            }
        )
    return insert_data


async def aingest(directory: Path, strategy: str = "run", limit: int = 0) -> None:
    """Async ingestion pipeline.

    Args:
        directory: Path to directory containing .md session files.
        strategy: Chunking strategy — "run", "session_summary", or "hybrid".
        limit: Maximum number of files to process (0 = all).
    """
    print(f"📂 Parsing files from {directory}...")
    sessions = parse_directory(directory, limit=limit)
    print(f"   Found {len(sessions)} sessions")

    if not sessions:
        print("❌ No sessions found. Check the directory path.")
        return

    # Print summary of what we found
    agent_counts = {}
    for s in sessions:
        agent_counts[s.agent_name] = agent_counts.get(s.agent_name, 0) + 1
    print(f"   Agents: {dict(sorted(agent_counts.items(), key=lambda x: -x[1]))}")

    print(f"🔧 Enriching with metadata...")
    sessions = enrich_sessions(sessions)

    print(f"✂️  Chunking with strategy: {strategy}")
    chunks = chunk_sessions(sessions, strategy=strategy)
    print(f"   Created {len(chunks)} chunks")

    if not chunks:
        print("❌ No chunks created. Check the session files.")
        return

    # Print chunk summary
    run_chunks = sum(1 for c in chunks if c.chunk_type == "run")
    summary_chunks = sum(1 for c in chunks if c.chunk_type == "session_summary")
    if strategy == "hybrid":
        print(f"   Run chunks: {run_chunks}, Session summary chunks: {summary_chunks}")
    elif strategy == "run":
        print(f"   Run chunks: {run_chunks}")
    else:
        print(f"   Session summary chunks: {summary_chunks}")

    print(f"📥 Inserting into PgVector (skip_if_exists=True)...")
    insert_data = chunks_to_insert_data(chunks)

    # Insert in batches to avoid overwhelming the local embedder
    batch_size = 20
    total_inserted = 0
    total_skipped = 0

    for i in range(0, len(insert_data), batch_size):
        batch = insert_data[i : i + batch_size]
        try:
            result = await session_knowledge.ainsert_many(batch, skip_if_exists=True)
            inserted = len(batch)  # ainsert_many doesn't return count, assume all
            total_inserted += inserted
            print(f"   Inserted {total_inserted}/{len(insert_data)} chunks")
        except Exception as e:
            print(f"   ⚠️  Batch {i // batch_size + 1} failed: {e}")
            # Try inserting one by one to isolate failures
            for item in batch:
                try:
                    await session_knowledge.ainsert(
                        name=item["name"],
                        text_content=item["text_content"],
                        metadata=item["metadata"],
                        skip_if_exists=True,
                    )
                    total_inserted += 1
                except Exception as e2:
                    print(f"      ⚠️  Failed: {item['name'][:80]}... — {e2}")
                    total_skipped += 1

        # Small delay between batches
        if i + batch_size < len(insert_data):
            await asyncio.sleep(BATCH_DELAY_SECS)

    print(f"\n✅ Done! Inserted {total_inserted} chunks, skipped {total_skipped}")


def main():
    parser = argparse.ArgumentParser(
        description="Ingest exported Agno session markdown files into PgVector"
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="Path to directory containing .md session files",
    )
    parser.add_argument(
        "--strategy",
        choices=["run", "session_summary", "hybrid"],
        default="run",
        help="Chunking strategy (default: run)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum number of files to process (0 = all)",
    )

    args = parser.parse_args()

    if not args.directory.exists():
        print(f"❌ Directory not found: {args.directory}")
        sys.exit(1)

    asyncio.run(aingest(args.directory, strategy=args.strategy, limit=args.limit))


if __name__ == "__main__":
    main()
