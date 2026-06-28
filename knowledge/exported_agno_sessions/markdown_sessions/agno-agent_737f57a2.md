# Agno Agent

| Field | Value |
|-------|-------|
| **Session** | `737f57a2...` |
| **Type** | agent |
| **Agent** | Agno Agent |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-20T04:35:52 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agno Agent ✓ COMPLETED

*2026-05-20T04:35:52* · `glm-5.1:cloud` · `81824147...`

### Prompt

Which tools do you have access to?

### Response

I have access to three tools:

1. **search_agno** — Searches across the Agno knowledge base to find relevant information, code examples, API references, and guides about the Agno framework.

2. **query_docs_filesystem_agno** — Runs read-only shell-like queries against a virtualized in-memory filesystem containing Agno documentation pages and OpenAPI specs. Supports commands like `rg` (ripgrep), `grep`, `find`, `tree`, `ls`, `cat`, `head`, `tail`, `wc`, `sort`, `jq`, and other text utilities. Used for reading specific documentation pages, searching with exact keyword/regex matches, or exploring the docs structure.

3. **search_knowledge_base** — Searches a general knowledge base for information about a query. Useful for broader or non-Agno-specific questions.

In short: **search_agno** for Agno-specific docs, **query_docs_filesystem_agno** for detailed doc page reading and filesystem exploration, and **search_knowledge_base** for general knowledge lookups.

---

## Run 2 — Agno Agent ✓ COMPLETED

*2026-05-20T04:37:15* · `glm-5.1:cloud` · `538193ec...`

### Prompt

can you access agno docs with the search_knowledge_base tool?

### Response

Yes, but with a clarification: I have **two separate tools** for accessing documentation, and they serve different purposes:

1. **`search_agno`** — This is the dedicated tool for searching **Agno documentation** specifically. It finds relevant information, code examples, API references, and guides from the Agno knowledge base.

2. **`search_knowledge_base`** — This is a more general knowledge base search tool. It may contain some overlapping content but isn't specifically scoped to Agno docs.

3. **`query_docs_filesystem_agno`** — This lets me directly **read** Agno documentation pages (using commands like `cat`, `head`, `rg`, `tree` on a virtualized filesystem). This is useful when I need the full content of a specific page rather than just search results.

**In practice**, my typical workflow for Agno-related questions is:

- **`search_agno`** first to find relevant pages and get contextual snippets
- **`query_docs_filesystem_agno`** to read the full content of a specific page (by appending `.mdx` to the path returned from search)

So if you have an Agno-related question, I'd use `search_agno` as the primary search tool and `query_docs_filesystem_agno` for deep-diving into specific pages.

What would you like to look up?

---
