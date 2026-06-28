# Agno Agent

| Field | Value |
|-------|-------|
| **Session** | `e88d7f7a...` |
| **Type** | agent |
| **Agent** | Agno Agent |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-20T06:14:21 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agno Agent ✓ COMPLETED

*2026-05-20T06:14:21* · `glm-5.1:cloud` · `3c002807...`

### Prompt

I want to use SurrealDB as my primary database for my Agno AgentOS

### Response

SurrealDB is a first-class supported database in Agno, and it works for **both** session storage (via `agno.db.surrealdb.SurrealDb`) **and** vector search (via `agno.vectordb.surrealdb.SurrealDb`). You can use it as your primary database for AgentOS. Here's everything you need:

---

## 1. Start SurrealDB

```bash
docker run --rm --pull always -p 8000:8000 surrealdb/surrealdb:latest start --user root --pass root
```

## 2. Session Storage (Agent/Team/Workflow persistence)

```python
from agno.agent import Agent
from agno.db.surrealdb import SurrealDb

SURREALDB_URL = "ws://localhost:8000"
SURREALDB_USER = "root"
SURREALDB_PASSWORD = "root"
SURREALDB_NAMESPACE = "agno"
SURREALDB_DATABASE = "futures_edge"

creds = {"username": SURREALDB_USER, "password": SURREALDB_PASSWORD}
db = SurrealDb(None, SURREALDB_URL, creds, SURREALDB_NAMESPACE, SURREALDB_DATABASE)
```

## 3. Vector Search (Knowledge base)

```python
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.surrealdb import SurrealDb as SurrealVectorDb
from surrealdb import Surreal

# Create SurrealDB client
client = Surreal(url=SURREALDB_URL)
client.signin({"username": SURREALDB_USER, "password": SURREALDB_PASSWORD})
client.use(namespace=SURREALDB_NAMESPACE, database=SURREALDB_DATABASE)

vector_db = SurrealVectorDb(
    client=client,
    collection="knowledge",   # collection name for storing documents
    efc=150,                  # HNSW construction time/accuracy trade-off
    m=12,                     # HNSW max connections per element
    search_ef=40,             # HNSW search time/accuracy trade-off
    embedder=OpenAIEmbedder(),
)

knowledge = Knowledge(vector_db=vector_db)
```

## 4. Full AgentOS Setup with SurrealDB

Here's a complete AgentOS configuration using SurrealDB as the primary database for both sessions and knowledge:

```python
from agno.agent import Agent
from agno.db.surrealdb import SurrealDb
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.models.ollama import Ollama
from agno.os import AgentOS
from agno.team.team import Team
from agno.vectordb.surrealdb import SurrealDb as SurrealVectorDb
from agno.workflow.step import Step
from agno.workflow.workflow import Workflow
from surrealdb import Surreal

# --- Connection ---
SURREALDB_URL = "ws://localhost:8000"
SURREALDB_USER = "root"
SURREALDB_PASSWORD = "root"
SURREALDB_NAMESPACE = "agno"
SURREALDB_DATABASE = "futures_edge"

creds = {"username": SURREALDB_USER, "password": SURREALDB_PASSWORD}

# Session storage
db = SurrealDb(None, SURREALDB_URL, creds, SURREALDB_NAMESPACE, SURREALDB_DATABASE)

# Vector search for knowledge
client = Surreal(url=SURREALDB_URL)
client.signin({"username": SURREALDB_USER, "password": SURREALDB_PASSWORD})
client.use(namespace=SURREALDB_NAMESPACE, database=SURREALDB_DATABASE)

vector_db = SurrealVectorDb(
    client=client,
    collection="futures_edge_knowledge",
    efc=150,
    m=12,
    search_ef=40,
    embedder=OpenAIEmbedder(),
)

knowledge = Knowledge(
    contents_db=db,          # Use SurrealDB for contents too
    vector_db=vector_db,     # SurrealDB for vector search
    name="Futures Edge Knowledge",
    description="Knowledge base for Futures Edge agents",
)

# --- Agents ---
agent = Agent(
    db=db,
    name="Project Manager",
    id="project-manager",
    model=Ollama(id="glm-5.1:cloud"),
    add_history_to_context=True,
    num_history_runs=3,
    knowledge=knowledge,
)

team = Team(
    db=db,
    id="project-initiation-team",
    name="Project Initiation Team",
    model=Ollama(id="glm-5.1:cloud"),
    members=[agent],
    add_history_to_context=True,
)

# --- AgentOS ---
agent_os = AgentOS(
    description="Futures Edge AgentOS",
    agents=[agent],
    teams=[team],
    db=db,   # Primary database for AgentOS (traces, sessions, etc.)
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="surreal:app", reload=True)
```

## Key Configuration Parameters

### Session Storage (`agno.db.surrealdb.SurrealDb`)

| Parameter | Description |
|-----------|-------------|
| `url` | SurrealDB WebSocket URL (e.g. `ws://localhost:8000`) |
| `creds` | Dict with `username` and `password` |
| `namespace` | SurrealDB namespace for isolation |
| `database` | SurrealDB database name |

### Vector Search (`agno.vectordb.surrealdb.SurrealDb`)

| Parameter | Description |
|-----------|-------------|
| `client` | Synchronous `Surreal` client (or `async_client` for async) |
| `collection` | Collection name for storing document vectors |
| `efc` | HNSW construction time/accuracy trade-off (default: 150) |
| `m` | HNSW max connections per element (default: 12) |
| `search_ef` | HNSW search time/accuracy trade-off (default: 40) |
| `embedder` | Embedder instance (e.g. `OpenAIEmbedder()`) |

## Notes for Your Setup

- **Namespace/database isolation**: Use different SurrealDB namespaces or databases to separate your agent environments (dev/staging/prod). Your existing TypeDB for PRISM and this SurrealDB instance can coexist — they serve different purposes (TypeDB for your design artefact graph, SurrealDB for Agno's session/knowledge storage).

- **Ollama model**: Your primary LLM `glm-5.1:cloud` via Ollama works fine with SurrealDB — the database is independent of the model provider.

- **If structured output causes issues** with the Ollama class, use `OllamaResponses` instead:
  ```python
  from agno.models.ollama import OllamaResponses
  model = OllamaResponses(id="glm-5.1:cloud")
  ```

- **AgentOS `db` parameter**: Pass the SurrealDB instance to both individual agents and the `AgentOS` constructor. The `AgentOS` `db` parameter handles traces and observability, while each agent's `db` parameter handles its own sessions.

- **Knowledge with SurrealDB**: You can use SurrealDB for both `contents_db` (document storage) and `vector_db` (vector search) — a single SurrealDB instance handles both. Alternatively, use PgVector for the vector side if you prefer (as shown in the AgentOS example).

SurrealDB is a strong choice for your stack — its multi-model capabilities (document, graph, vector) align well with your PRISM ontology needs, and Agno supports it natively for both storage tiers.

---
