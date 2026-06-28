# Agno Agent Designer

| Field | Value |
|-------|-------|
| **Session** | `53d39396...` |
| **Type** | agent |
| **Agent** | Agno Agent Designer |
| **User** | pete@peterargent.com |
| **Created** | 2026-06-12T23:00:55 |
| **Runs** | 0 completed / 1 total |

## Run 1 — Agno Agent Designer ⚠️ PAUSED

*2026-06-12T23:00:55* · `glm-5.1:cloud` · `de3254d7...`

### Prompt

I've create a conversational thinking partner agent with the specs below. 
I want to have a workflow that processes session outputs and catalogues knowledge objects for use in future conversations. 

I want 'knowledge object' fragments to be analysed for relationships with a range of subject areas, and classified by knowledge/output type. The fragments should be enriched with epistemic metadata as part of the process. 

```
"""
ThinkingPartner Agent
=====================
"""

from pathlib import Path

from agno.agent import Agent
from agno.skills import Skills, LocalSkills
from agno.tools.mcp import MCPTools
from agno.tools.google.drive import GoogleDriveTools
from agno.tools.websearch import WebSearchTools
from agno.tools.crawl4ai import Crawl4aiTools
from agno.learn import (
    LearningMachine,
    LearningMode,
    EntityMemoryConfig,
    SessionContextConfig,
    UserProfileConfig,
    UserMemoryConfig,
    LearnedKnowledgeConfig,
    DecisionLogConfig,
)

from app.settings import default_model
from db import get_surrealdb
from prompts.thinking_partner_instructions import (
    INSTRUCTIONS,
    EXPECTED_OUTPUT,
    ADDITIONAL_CONTEXT,
    FEW_SHOT_EXAMPLES,
)
from agents.schemas import PeterCognitiveProfile, IntellectualEntityMemory
from agents.google_auth import (
    get_google_creds,
    google_creds_available,
    DRIVE_READONLY_SCOPE,
    DRIVE_FILE_SCOPE,
)

SKILLS_DIR = Path(__file__).parent / "skills"

# Google Drive auth: build Credentials directly from env vars (no file needed).
# Supports GOOGLE_SERVICE_ACCOUNT_B64 (base64), GOOGLE_SERVICE_ACCOUNT (raw JSON),
# GOOGLE_SERVICE_ACCOUNT_FILE (path), or the default file path.
_google_drive_available = google_creds_available()

# Export availability for main.py
__all__ = ["thinking_partner", "_google_drive_available"]

# Agno docs MCP — external server, reachable at runtime.
# refresh_connection=True: if the server is down at startup, AgentOS will
# retry the connection on each agent run instead of crashing the app.
mcp_tools = MCPTools(
    transport="streamable-http",
    url="https://docs.agno.com/mcp",
    refresh_connection=True,
)
# NOTE: No self-referential MCPTools(url="http://localhost:8006/mcp").
# The app exposes /mcp via enable_mcp_server=True for external clients.
# An agent inside the same process cannot connect to itself at startup
# (circular dependency — the server isn't running yet). Inter-agent
# delegation happens through AgentOS's built-in routing, not MCP.
if _google_drive_available:
    _drive_creds = get_google_creds(scopes=[DRIVE_READONLY_SCOPE, DRIVE_FILE_SCOPE])
    google_drive_tools = GoogleDriveTools(
        upload_file=True,
        download_file=True,
        creds=_drive_creds,
    )
else:
    google_drive_tools = None
web_search_tools = WebSearchTools()
crawl4ai_tools = Crawl4aiTools(max_length=5000)

# Build tools list — skip Google Drive if service account is unavailable
_thinking_partner_tools = [mcp_tools]
if google_drive_tools is not None:
    _thinking_partner_tools.append(google_drive_tools)
_thinking_partner_tools.extend([web_search_tools, crawl4ai_tools])

thinking_partner = Agent(
    id="thinking-partner",
    name="ThinkingPartner",
    model=default_model(),
    tools=_thinking_partner_tools,
    skills=Skills(loaders=[LocalSkills(str(SKILLS_DIR))]),
    db=get_surrealdb(
        memory_table="thinking_partner_memories",
        culture_table="thinking_partner_culture",
    ),
    instructions=INSTRUCTIONS,
    learning=LearningMachine(
        user_profile=UserProfileConfig(
            mode=LearningMode.ALWAYS,
            schema=PeterCognitiveProfile,
        ),
        user_memory=UserMemoryConfig(
            mode=LearningMode.ALWAYS,
        ),
        session_context=SessionContextConfig(
            mode=LearningMode.ALWAYS,
            enable_planning=True,
        ),
        entity_memory=EntityMemoryConfig(
            mode=LearningMode.ALWAYS,
            schema=IntellectualEntityMemory,
            namespace="user:{user_id}:thinking_partner",
        ),
        learned_knowledge=LearnedKnowledgeConfig(
            mode=LearningMode.AGENTIC,
        ),
        decision_log=DecisionLogConfig(
            mode=LearningMode.AGENTIC,
            enable_agent_tools=True,
            agent_can_save=True,
            agent_can_search=True,
        ),
    ),
    enable_agentic_memory=True,
    add_memories_to_context=True,
    add_culture_to_context=True,
    update_cultural_knowledge=True,
    add_history_to_context=True,
    num_history_runs=5,
    enable_session_summaries=True,
    add_session_summary_to_context=True,
    search_session_history=True,
    num_history_sessions=3,
    add_session_state_to_context=True,
    add_datetime_to_context=True,
    add_location_to_context=True,
    expected_output=EXPECTED_OUTPUT,
    additional_context=ADDITIONAL_CONTEXT,
    additional_input=FEW_SHOT_EXAMPLES,
    markdown=True,
)
```

### Response

Now let me put the complete design together. This connects deeply to your CCCT, PRISM, and type collision work — I'll design it with CAWDP principles baked in.

---
