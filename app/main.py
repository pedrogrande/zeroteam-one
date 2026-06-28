"""
AgentOS Entrypoint
==================
"""

from contextlib import asynccontextmanager
from os import getenv
from pathlib import Path

from agno.os import AgentOS
from agno.utils.log import log_error, log_info
from fastapi import FastAPI

from agents.agno_support import agno_support_agent
from agents.code_search import code_search
from agents.thinking_partner import thinking_partner
from agents.web_search import web_search
from api.router import api_router
from db import get_shared_db
from db.knowledge_bases import STUDIO_KNOWLEDGE_BASES
from teams.engineering_team import engineering_team

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
runtime_env = getenv("RUNTIME_ENV", "prd")
scheduler_base_url = getenv("AGENTOS_URL", "http://127.0.0.1:8000")

# ---------------------------------------------------------------------------
# Interfaces
# - The CodeSearch agent becomes available on Slack when both env vars are set
# ---------------------------------------------------------------------------
SLACK_BOT_TOKEN = getenv("SLACK_BOT_TOKEN", "")
SLACK_SIGNING_SECRET = getenv("SLACK_SIGNING_SECRET", "")

interfaces: list = []
if SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET:
    from agno.os.interfaces.slack import Slack

    interfaces.append(
        Slack(
            agent=code_search,
            streaming=True,
            token=SLACK_BOT_TOKEN,
            signing_secret=SLACK_SIGNING_SECRET,
            resolve_user_identity=True,
        )
    )


# ---------------------------------------------------------------------------
# Lifespan — extension hook for app-level startup / teardown.
#
# AgentOS handles the MCP lifecycle (connect on startup, close on shutdown).
# Keep this hook in place so you can plug in your own setup as needed.
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app):  # type: ignore[no-untyped-def]
    log_info("AgentOS lifespan: startup")
    # Create task contract tables (idempotent — safe on every boot)
    try:
        from tasks.db import init_tables

        init_tables()
        log_info("Task contract tables initialized")
    except Exception as e:
        log_error(f"Failed to initialize task contract tables: {e}")
    try:
        yield
    except Exception as e:
        log_error(f"AgentOS lifespan error: {e}")
        raise
    finally:
        log_info("AgentOS lifespan: shutdown")


# ---------------------------------------------------------------------------
# Custom FastAPI app — carries the /api/v1 task contract router
# ---------------------------------------------------------------------------
app = FastAPI(
    title="AgentOS",
    description="Agent platform with task contract API.",
    version="1.0.0",
)
app.include_router(api_router)

# ---------------------------------------------------------------------------
# Create AgentOS — pass our custom app as base_app so AgentOS adds its
# routes (agents, sessions, etc.) alongside our /api/v1 routes.
# on_route_conflict="preserve_base_app" keeps our custom routes if any
# conflict with AgentOS built-ins.
# ---------------------------------------------------------------------------
agent_os = AgentOS(
    name="AgentOS",
    tracing=getenv("AGNO_TRACING", "false").lower() == "true",
    scheduler=True,
    scheduler_base_url=scheduler_base_url,
    authorization=runtime_env == "prd",
    lifespan=lifespan,
    db=get_shared_db(),
    agents=[
        thinking_partner,
        web_search,
        code_search,
        agno_support_agent,
    ],
    teams=[engineering_team],
    interfaces=interfaces,
    knowledge=STUDIO_KNOWLEDGE_BASES,
    config=str(Path(__file__).parent / "config.yaml"),
    base_app=app,
    on_route_conflict="preserve_base_app",
)
app = agent_os.get_app()


if __name__ == "__main__":
    agent_os.serve(app="app.main:app", reload=runtime_env == "dev")
