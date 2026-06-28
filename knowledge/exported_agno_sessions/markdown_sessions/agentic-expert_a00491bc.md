# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `a00491bc...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-16T01:41:01 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-16T01:41:01* · `glm-5.1:cloud` · `d9490a0c...`

### Prompt

I'm building a business 'operating system' platform and dashboard that provides an 'intelligence layer' where agents can access the organisation's data along with market research and other external sources to provide a range of findings, insights, recommendations, and strategic ideas.

I see that this will require a number of agents to perform different tasks and the agents would have differing context needs.

Let's review Agno's advice on implementing knowledge for agents and suggest the various domains that would be important for this application.

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agno.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Knowledge

> Attach Knowledge to your AgentOS instance

The AgentOS control plane provides a simple way to [manage](/agent-os/features/knowledge-management#adding-content) your Knowledge bases.
You can add, edit, and delete content from your Knowledge bases directly through the control plane.

You can specify multiple Knowledge bases and reuse the same Knowledge instance
across different Agents or Teams as needed.

## Prerequisites

Before setting up Knowledge management in AgentOS, ensure you have:

* PostgreSQL database running and accessible - used for this example
* Required dependencies installed: `uv pip install agno`
* OpenAI API key configured (for embeddings)
* Basic understanding of [Knowledge concepts](/knowledge/quickstart)

## Example

This example demonstrates how to attach multiple Knowledge bases to AgentOS
and populate them with content from different sources.

```python agentos_knowledge.py theme={null}
from textwrap import dedent

from agno.db.postgres import PostgresDb
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.os import AgentOS
from agno.vectordb.pgvector import PgVector, SearchType

# ************* Setup Knowledge Databases *************
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
documents_db = PostgresDb(
    db_url,
    id="agno_knowledge_db",
    knowledge_table="agno_knowledge_contents",
)
faq_db = PostgresDb(
    db_url,
    id="agno_faq_db",
    knowledge_table="agno_faq_contents",
)
# *******************************

documents_knowledge = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="agno_knowledge_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=documents_db,
)

faq_knowledge = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="agno_faq_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=faq_db,
)

agent_os = AgentOS(
    description="Example app with AgentOS Knowledge",
    # Add the knowledge bases to AgentOS
    knowledge=[documents_knowledge, faq_knowledge],
)


app = agent_os.get_app()

if __name__ == "__main__":
    documents_knowledge.insert(
        name="Agno Docs", url="https://docs.agno.com/llms-full.txt", skip_if_exists=True
    )
    faq_knowledge.insert(
        name="Agno FAQ",
        text_content=dedent("""
            What is Agno?
            Agno is a framework for building agents.
            Use it to build multi-agent systems with memory, knowledge,
            human in the loop and MCP support.
        """),
        skip_if_exists=True,
    )
    # Run your AgentOS
    # You can test your AgentOS at: http://localhost:7777/

    agent_os.serve(app="agentos_knowledge:app")
```

### Screenshots

The screenshots below show how you can access and manage your different Knowledge bases through the AgentOS interface:

<img src="https://mintcdn.com/agno-v2/tBgqL1LeYUKpZTuS/images/agno_knowledge_db.png?fit=max&auto=format&n=tBgqL1LeYUKpZTuS&q=85&s=b7def1bd459cf44ad505591fedb7d93c" alt="llm-app-aidev-run" width="3410" height="750" data-path="images/agno_knowledge_db.png" />

<img src="https://mintcdn.com/agno-v2/tBgqL1LeYUKpZTuS/images/agno_faq_db.png?fit=max&auto=format&n=tBgqL1LeYUKpZTuS&q=85&s=e0b00d9eaa45fa729acfea31f4c999e3" alt="llm-app-aidev-run" width="3410" height="750" data-path="images/agno_faq_db.png" />

## Knowledge ID

Each Knowledge instance registered with AgentOS gets a deterministic `knowledge_id`. This ID is generated from the combination of the instance's `name`, database ID, and table name. The same inputs always produce the same ID, so it is stable across restarts.

Use `knowledge_id` in API calls to target a specific Knowledge instance:

```bash theme={null}
# List content sources
curl http://localhost:7777/v1/knowledge/{knowledge_id}/sources

# Browse files in an S3 source
curl "http://localhost:7777/v1/knowledge/{knowledge_id}/sources/{source_id}/files?prefix=reports/"

# Upload content
curl -X POST http://localhost:7777/v1/knowledge/{knowledge_id}/content \
  -F "file=@report.pdf" \
  -F "name=Q4 Report"
```

### Finding your Knowledge ID

The `/knowledge/config` endpoint returns all registered Knowledge instances with their IDs:

```bash theme={null}
curl http://localhost:7777/v1/knowledge/config | jq '.knowledge_instances'
```

```json theme={null}
[
  {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "name": "documents_knowledge",
    "db_id": "agno_knowledge_db",
    "table": "agno_knowledge_contents"
  },
  {
    "id": "f9e8d7c6-b5a4-3210-fedc-ba0987654321",
    "name": "faq_knowledge",
    "db_id": "agno_faq_db",
    "table": "agno_faq_contents"
  }
]
```

### Backward compatibility

If you have a single Knowledge instance, you can omit `knowledge_id` from API calls. For multiple instances, you can also use the `db_id` query parameter, but `knowledge_id` is preferred as it uniquely identifies the instance even when multiple instances share the same database.

## Best Practices

* **Separate Knowledge by Domain**: Create separate Knowledge bases for different topics (e.g., technical docs, FAQs, policies)
* **Consistent Naming**: Use descriptive names for your Knowledge bases that reflect their content
* **Regular Updates**: Keep your Knowledge bases current by regularly adding new content and removing outdated information
* **Monitor Performance**: Use different table names for vector storage to avoid conflicts
* **Content Organization**: Use the `name` parameter when adding content to make it easily identifiable
* **Use metadata for filtering and searching**: Add metadata to your content to make it easier to find and filter

## Troubleshooting

<AccordionGroup>
  <Accordion title="Knowledge base not appearing in AgentOS interface">
    Ensure your knowledge base is properly added to the `knowledge` parameter when creating your AgentOS instance.
    Also make sure to attach a `contents_db` to your Knowledge instance.
  </Accordion>

  <Accordion title="Database connection errors">
    Verify your PostgreSQL connection string and ensure the database is running and accessible.
  </Accordion>

  <Accordion title="Content not being found in searches">
    Check that your content has been properly embedded by verifying entries in your vector database table.
  </Accordion>
</AccordionGroup>

### Response

This is a great application of your frameworks to an Agno implementation. Let me synthesise Agno's knowledge management approach with your established design work — the 20 intelligence domains, PRISM ontology, information quality framework, and CC-4 information boundaries.

## Agno Knowledge Management: What You Need to Know

Agno's knowledge architecture has three key components:

| Component | Purpose | Key Detail |
|---|---|---|
| **Knowledge** | Container for domain content | Each Knowledge instance = one domain |
| **Vector DB** | Semantic search | PgVector with hybrid search (keyword + vector) |
| **Contents DB** | Full content storage | PostgreSQL for raw content retrieval |

The critical architectural decision: **one Knowledge instance per domain**, not one giant knowledge base. This maps directly to your CC-4 Information Boundaries — agents should only access knowledge relevant to their domain and authority.

## Recommended Domain Architecture

Based on your 20 intelligence domains grouped by 4 orchestrator domains, here's the knowledge base architecture:

### Commercial Orchestrator Domain
| Knowledge Base | Content Sources | Primary Agents | Access Level |
|---|---|---|---|
| `kb_financial` | P&L, cash flow, invoicing, payroll, BAS | Financial specialists | Orchestrator + specialists |
| `kb_contract` | Active contracts, templates, obligations, milestones | Contract specialists | Orchestrator + specialists |
| `kb_regulatory` | Compliance requirements, industry regulations, deadlines | Compliance specialists | Orchestrator + specialists |
| `kb_operations` | SOPs, processes, vendor relationships, logistics | Operations specialists | Orchestrator + specialists |

### Growth Orchestrator Domain
| Knowledge Base | Content Sources | Primary Agents | Access Level |
|---|---|---|---|
| `kb_client` | Client profiles, history, preferences, communications | Client specialists | Orchestrator + specialists |
| `kb_market` | Market research, competitor analysis, industry trends | Market specialists | Orchestrator + specialists |
| `kb_partner` | Partner profiles, agreements, performance data | Partner specialists | Orchestrator + specialists |
| `kb_media` | Brand assets, content library, social performance | Media specialists | Orchestrator + specialists |

### Venture Orchestrator Domain
| Knowledge Base | Content Sources | Primary Agents | Access Level |
|---|---|---|---|
| `kb_product` | Product specs, roadmap, user feedback, features | Product specialists | Orchestrator + specialists |
| `kb_idea` | Innovation pipeline, idea evaluations, experiments | Innovation specialists | Orchestrator + specialists |
| `kb_technology` | Tech stack, capabilities, evaluation reports | Technology specialists | Orchestrator + specialists |
| `kb_project` | Project briefs, status, milestones, dependencies | Project specialists | Orchestrator + specialists |

### Stewardship Orchestrator Domain
| Knowledge Base | Content Sources | Primary Agents | Access Level |
|---|---|---|---|
| `kb_risk` | Risk register, incidents, mitigation plans | Risk specialists | Orchestrator + specialists |
| `kb_security` | Access policies, auth logs, compliance checks | Security specialists | Orchestrator ONLY |
| `kb_impact` | Impact assessments, sustainability, community | Impact specialists | Orchestrator + specialists |

### Cross-Domain Knowledge
| Knowledge Base | Content Sources | Primary Agents | Access Level |
|---|---|---|---|
| `kb_strategy` | Strategic decisions, positioning, vision, competition | Strategy specialists | All orchestrators |
| `kb_knowledge` | Institutional memory, lessons learned, specifications | Learning specialists | All orchestrators |
| `kb_prism` | PRISM knowledge graph, decision archaeology, relations | All agents (read) | System-managed |

## Agno Implementation Architecture

Here's how this maps to Agno code:

```python
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.pgvector import PgVector, SearchType
from agno.db.postgres import PostgresDb

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# ============================================================
# COMMERCIAL DOMAIN KNOWLEDGE
# ============================================================

kb_financial = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_financial_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_financial_db",
        knowledge_table="kb_financial_contents",
    ),
)

kb_contract = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_contract_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_contract_db",
        knowledge_table="kb_contract_contents",
    ),
)

# ... (kb_regulatory, kb_operations similarly)

# ============================================================
# GROWTH DOMAIN KNOWLEDGE
# ============================================================

kb_client = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_client_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_client_db",
        knowledge_table="kb_client_contents",
    ),
)

# ... (kb_market, kb_partner, kb_media similarly)

# ============================================================
# VENTURE DOMAIN KNOWLEDGE
# ============================================================

kb_product = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_product_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_product_db",
        knowledge_table="kb_product_contents",
    ),
)

# ... (kb_idea, kb_technology, kb_project similarly)

# ============================================================
# STEWARDSHIP DOMAIN KNOWLEDGE
# ============================================================

kb_risk = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_risk_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_risk_db",
        knowledge_table="kb_risk_contents",
    ),
)

# ... (kb_security, kb_impact similarly)

# ============================================================
# CROSS-DOMAIN KNOWLEDGE
# ============================================================

kb_strategy = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_strategy_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_strategy_db",
        knowledge_table="kb_strategy_contents",
    ),
)

kb_knowledge = Knowledge(
    vector_db=PgVector(
        db_url=db_url,
        table_name="kb_knowledge_vectors",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=PostgresDb(
        db_url, id="kb_knowledge_db",
        knowledge_table="kb_knowledge_contents",
    ),
)
```

## CC-4 Information Boundaries in Agno

This is where your framework adds significant value beyond Agno's default setup. Agno gives you **domain separation** (separate Knowledge instances). Your framework adds **authority boundaries** (who can access what and why).

```python
from agno.agent import Agent
from agno.models.ollama import Ollama

# ============================================================
# CC-4: Information Boundaries — agents only see what they need
# ============================================================

# Financial Extractor — ONLY financial knowledge
financial_extractor = Agent(
    name="Financial Extractor",
    model=Ollama(id="glm-5.1:cloud"),
    knowledge=[kb_financial],  # Single domain access
    instructions=[
        "You extract financial data. You NEVER interpret.",
        "You NEVER access client, contract, or strategy data.",
        "You flag missing data, you don't assume it.",
    ],
)

# Contract Assessor — contract knowledge + regulatory (need compliance context)
contract_assessor = Agent(
    name="Contract Assessor",
    model=Ollama(id="glm-5.1:cloud"),
    knowledge=[kb_contract, kb_regulatory],  # Two domains — compliance context needed
    instructions=[
        "You assess contract risk and compliance. You NEVER finalize.",
        "You flag regulatory implications. You NEVER make legal judgments.",
        "You access contract and regulatory data only.",
    ],
)

# Commercial Orchestrator — all Commercial domain knowledge
commercial_orchestrator = Agent(
    name="Commercial Orchestrator",
    model=Ollama(id="glm-5.1:cloud"),
    knowledge=[kb_financial, kb_contract, kb_regulatory, kb_operations],
    instructions=[
        "You prepare judgment for the human principal.",
        "You NEVER commit, finalize, or act without human authorization.",
        "You synthesise across Commercial domains.",
        "You include confidence, provenance, and what you DON'T know.",
    ],
)

# Security specialist — RESTRICTED: only Stewardship orchestrator
security_specialist = Agent(
    name="Security Specialist",
    model=Ollama(id="glm-5.1:cloud"),
    knowledge=[kb_security],  # Single domain, high restriction
    instructions=[
        "You monitor access policies and compliance.",
        "You NEVER share security data with other domain agents.",
        "You report to Stewardship Orchestrator only.",
    ],
)
```

## The Key Architectural Insight

Here's the critical point from your framework work that Agno's documentation doesn't address:

**Agno gives you domain separation. Your framework gives you authority boundaries.**

Agno's Knowledge system solves the **technical** problem — how to store and retrieve domain-specific knowledge. Your CAWDP framework solves the **governance** problem — who should see what, why, and what they're allowed to do with it.

This maps to your three enforcement regimes:

| Regime | Agno Supports | Your Framework Adds |
|---|---|---|
| **Declare** (agent told rules) | ✅ Instructions parameter | Authority boundaries tied to failure modes |
| **Detect** (system flags violations) | ⚠️ Logging exists but not boundary-specific | IDS/UPR monitoring, epistemic metadata |
| **Prevent** (system enforces structurally) | ✅ Knowledge isolation (separate instances) | Private schemas, access control tables, CC-4 at data layer |

Agno's Knowledge isolation is already Regime 3 enforcement at the domain level — an agent with `kb_financial` simply cannot access `kb_security`. This is exactly your private schema pattern from the Project Manager agent, applied at the knowledge layer.

## Knowledge Per Agent Class

Drawing from your 5-class taxonomy, different agent classes need fundamentally different knowledge access patterns:

| Agent Class | Knowledge Access Pattern | Reasoning |
|---|---|---|
| **Extractor** | Read-only, single domain | Never judges — only extracts. Minimal access to prevent overreach. |
| **Measurer** | Read-only, single domain + reference data | Measures against standards. Needs reference data, not interpretive knowledge. |
| **Assessor** | Read-only, cross-domain (scoped) | Assesses risk, compliance, quality. Needs cross-domain context but READ-ONLY. |
| **Generator** | Read-write, single domain + review context | Generates drafts within domain. Needs write access but constrained scope. |
| **Aggregator** | Read-only, multi-domain (orchestrated) | Assembles across domains. Broad read access but NEVER adds content. |

## Priority Implementation Order

Based on your "start with Extractors" principle and the 5 domains you identified for Future's Edge:

```python
# ============================================================
# PHASE 1: Start with 5 core domains (Extractors earn trust first)
# ============================================================

# 1. Client — lowest risk, highest trust-building
kb_client = Knowledge(...)

# 2. Financial — moderate risk, high value
kb_financial = Knowledge(...)

# 3. Strategy — moderate risk, judgment-rich
kb_strategy = Knowledge(...)

# 4. Product — moderate risk, generation-heavy
kb_product = Knowledge(...)

# 5. Knowledge/Learning — institutional memory, compounding value
kb_knowledge = Knowledge(...)
```

## What Agno's Docs Don't Cover (That Your Framework Does)

| Gap | Your Framework | Agno Equivalent |
|---|---|---|
| Epistemic metadata on knowledge (CC-3) | 6-field metadata on every knowledge object | None — knowledge is stored without quality metadata |
| Information boundaries by agent class | Agent classes get different access patterns | Only per-instance separation |
| Specification aging (CC-5) | Knowledge has `assessedAt` + `refreshCadenceDays` | None — knowledge doesn't self-signal staleness |
| Decision archaeology | Why decisions were made, what alternatives considered | None |
| PRISM knowledge graph | Typed relations between knowledge objects | Flat vector search only |
| ACP budget-aware retrieval | Token budgets with relevance/confidence weighting | Unlimited context injection |
| Quality-unit level granularity | Package-level + unit-level quality scoring | Single-level retrieval |

This is where your PRISM + TypeDB architecture adds the most value — Agno handles vector storage and retrieval well, but the **structured knowledge graph** with epistemic metadata, typed relations, authority boundaries, and quality scoring needs your PRISM layer on top.

The recommended architecture: **Agno Knowledge for vector search and retrieval (the search layer) + PRISM/TypeDB for structured knowledge with authority boundaries and quality metadata (the intelligence layer).**The architecture is clear: Agno Knowledge handles the **search and retrieval** layer well, but the **intelligence and governance** layer needs PRISM. Your 5-class taxonomy directly determines knowledge access patterns, and your CC-4 Information Boundaries principle applies at both the database layer (private schemas) and the knowledge layer (separate Knowledge instances with authority-scoped instructions).

What would you like to explore next — the PRISM/TypeDB integration for the intelligence layer, the orchestrator agent specifications, or the progressive trust deployment strategy?

---
