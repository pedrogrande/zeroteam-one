# Example of an AgentOS Studio Registry with knowledge bases

```python
from agno.db.postgres import PostgresDb
from agno.models.openai import OpenAIChat
from agno.models.anthropic import Claude
from agno.os import AgentOS
from agno.registry import Registry
from agno.tools.calculator import CalculatorTools
from agno.tools.websearch import WebSearchTools
from agno.vectordb.pgvector import PgVector
from pydantic import BaseModel

class InputSchema(BaseModel):
    input: str
    description: str

def custom_evaluator(input: str) -> bool:
    return "urgent" in input.lower()

db = PostgresDb(db_url="postgresql+psycopg://ai:ai@localhost:5532/ai", id="postgres_db")
user_memory_manager = MemoryManager(
    model=Claude(id="claude-opus-4-7"),
    db=db,
     additional_instructions="""
    IMPORTANT: Don't store any memories about the user's name. Just say "The User" instead of referencing the user's name.
    """,
)
concise_summary_manager = SessionSummaryManager(
    model=OpenAIResponses(id="gpt-5-mini"),
    session_summary_prompt=(
        "Summarize the conversation in 3-5 bullet points focused on decisions, "
        "open questions, and any follow-ups required."
    ),
    last_n_runs=10,
)
agent_knowledge = Knowledge(
    name="Agent Knowledge",
    description="Example knowledge base for agents",
    vector_db=PgVector(table_name="agent_knowledge_documents", db_url=DB_URL),
    contents_db=db,
)

registry = Registry(
    name="My Registry",
    tools=[CalculatorTools(), WebSearchTools()],
    models=[OpenAIChat(id="gpt-5-mini"), Claude(id="claude-sonnet-4-5")],
    dbs=[db],
    vector_dbs=[PgVector(db_url="postgresql+psycopg://ai:ai@localhost:5532/ai", table_name="embeddings")],
    schemas=[InputSchema],
    functions=[custom_evaluator],
    memory_managers=[user_memory_manager],
    session_summary_managers=[concise_summary_manager],
    knowledge=[agent_knowledge],
)

agent_os = AgentOS(id="my-app", registry=registry, db=db)
app = agent_os.get_app()
```
