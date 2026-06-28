# Agent Design - Decision Tree (Exploration)

---

## Design Principles

The Agno docs themselves say: *"Start simple: a model, tools, and instructions. Once that works, layer in more functionality as needed."* ([/agents/building-agents](https://docs.agno.com/agents/building-agents))

The questionnaire follows that principle:

1. **Start with the irreducible minimum** — every agent needs a model, a name, and instructions
2. **Ask binary gateway questions** — each "No" eliminates an entire parameter cluster
3. **Only drill into details when a cluster is enabled** — progressive disclosure
4. **Auto-apply defaults** — if a user doesn't enable a feature, its parameters stay at their Agno defaults (mostly `False`/`None`) and never appear in the form

---

## The Full Decision Tree

### Stage 0 — Always Required (Base Agent)

These fields always appear. No question needed.

| Field | Input Type | Notes |
|---|---|---|
| `model` | Dropdown (provider → model) or free text `provider:model_id` | Required. See [/models/overview](https://docs.agno.com/models/overview) |
| `name` | Text | Required for deployment |
| `instructions` | Textarea (multi-line, parsed as `List[str]`) | Core agent behaviour |
| `description` | Text | Short description added to system message |

**→ Then proceed through Q1–Q12 below. Each "No" skips the entire sub-form for that cluster.**

---

### Q1: Does the agent need tools to interact with external services?

> *Tools let the agent call functions, APIs, databases, search engines, etc. as part of its reasoning loop.*

**If No** → skip `tools`, `tool_call_limit`, `tool_choice`, `tool_hooks`, `max_tool_calls_from_history`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `tools` | Multi-select from available Toolkits / custom callables | `None` | The core selection. See [/agents/usage/agent-with-tools](https://docs.agno.com/agents/usage/agent-with-tools) |
| `tool_call_limit` | Number input | `None` | Max tool calls per run |
| `tool_choice` | Dropdown: `auto` / `none` / `required` / specific tool | `None` | Controls model's tool selection |
| `tool_hooks` | List of callable references | `None` | Functions run between tool calls |

**→ Then ask Q1a:**

#### Q1a: Should the agent be able to read its own chat history or tool call history during a run?

**If No** → skip `read_chat_history`, `read_tool_call_history`

**If Yes** → show:

| Field | Input Type | Default |
|---|---|---|
| `read_chat_history` | Toggle | `False` |
| `read_tool_call_history` | Toggle | `False` |
| `max_tool_calls_from_history` | Number | `None` |

---

### Q2: Does the agent need persistent conversation history (storage)?

> *Storage lets the agent remember conversations across runs using the same session_id. Without it, each run is stateless.* See [/agents/usage/agent-with-storage](https://docs.agno.com/agents/usage/agent-with-storage)

**If No** → skip `db`, `add_history_to_context`, `num_history_runs`, `num_history_messages`, `store_tool_messages`, `store_history_messages`, `search_session_history`, `num_history_sessions`, `cache_session`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `db` | Dropdown (SqliteDb, PostgresDb, etc.) + connection params | `None` | Required for persistence |
| `add_history_to_context` | Toggle | `False` | Include past messages in model context |
| `num_history_runs` | Number | `None` | How many past runs to include |
| `num_history_messages` | Number | `None` | How many past messages to include |
| `store_tool_messages` | Toggle | `True` | Store tool results in DB |
| `store_history_messages` | Toggle | `False` | Store history messages in DB |

**→ Then ask Q2a:**

#### Q2a: Should the agent be able to search across *previous* sessions (not just the current one)?

**If No** → skip `search_session_history`, `num_history_sessions`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `search_session_history` | Toggle | `False` | |
| `num_history_sessions` | Number | `None` | Docs advise keeping to 2–3 |

**→ Then ask Q2b:**

#### Q2b: Should the session be cached in memory for faster access?

**If No** → `cache_session` stays `False`

**If Yes** → show `cache_session` toggle (default `False`)

---

### Q3: Does the agent need to maintain state within a session?

> *Session state is a dict that persists across runs in the same session, stored in the database.*

**If No** → skip `session_state`, `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state`

> **⚠️ Dependency**: If Q2 was "No" (no `db`), then session state cannot persist. Show a warning: *"Session state requires a database. You'll need to enable storage (Q2)."*

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `session_state` | Key-value editor (JSON dict) | `None` | Initial state |
| `add_session_state_to_context` | Toggle | `False` | Include state in model context |
| `enable_agentic_state` | Toggle | `False` | Give the agent tools to update state |
| `overwrite_db_session_state` | Toggle | `False` | Overwrite DB state on each run |

---

### Q4: Does the agent need user-level memory (preferences, facts about the user)?

> *Memory stores user-level information across all sessions — distinct from session history.* See [/agents/usage/agent-with-memory](https://docs.agno.com/agents/usage/agent-with-memory)

**If No** → skip `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context`

> **⚠️ Dependency**: Requires `db` (from Q2). If Q2 was "No", show warning.

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `memory_manager` | Config (model + db) | `None` | The MemoryManager instance |
| `enable_agentic_memory` | Toggle | `False` | Agent manages memory via tools |
| `update_memory_on_run` | Toggle | `False` | Auto-update memory after each run |
| `add_memories_to_context` | Toggle | `None` | Include memories in model context |

> **Note**: `enable_agentic_memory` and `update_memory_on_run` are two alternative modes — the docs describe them as either/or: *"Agent decides when to store/recall via tool calls"* vs *"Memory manager runs after every response"*.

---

### Q5: Does the agent need a searchable knowledge base (RAG)?

> *Knowledge gives the agent a searchable document store. The agent decides when to search based on the user's question.* See [/agents/usage/agent-with-knowledge](https://docs.agno.com/agents/usage/agent-with-knowledge)

**If No** → skip `knowledge`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `add_knowledge_to_context`, `knowledge_retriever`, `references_format`, `search_knowledge`, `update_knowledge`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `knowledge` | Config (vector DB + embedder + content sources) | `None` | The Knowledge instance |
| `add_knowledge_to_context` | Toggle | `False` | Auto-inject references into prompt |
| `knowledge_filters` | Key-value editor | `None` | Filter the knowledge base |
| `enable_agentic_knowledge_filters` | Toggle | `None` | Let agent choose its own filters |
| `references_format` | Dropdown: `json` / `yaml` | `"json"` | |
| `knowledge_retriever` | Callable reference | `None` | Custom retrieval function |

**→ Then ask Q5a:**

#### Q5a: Should the agent be able to search the knowledge base itself (agentic RAG)?

> *If Yes, a `search_knowledge` tool is automatically added.*

| Field | Input Type | Default |
|---|---|---|
| `search_knowledge` | Toggle | `True` (on by default when knowledge is set) |

**→ Then ask Q5b:**

#### Q5b: Should the agent be able to update the knowledge base?

| Field | Input Type | Default |
|---|---|---|
| `update_knowledge` | Toggle | `False` |

---

### Q6: Does the agent need guardrails or hooks?

> *Pre-hooks run before processing starts; post-hooks run after output is generated.* See [/hooks/overview](https://docs.agno.com/hooks/overview)

**If No** → skip `pre_hooks`, `post_hooks`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `pre_hooks` | Multi-select (BaseGuardrail subclasses, BaseEval, or custom callables) | `None` | Runs after session load, before processing |
| `post_hooks` | Multi-select (same types) | `None` | Runs after output, before response return |

---

### Q7: Should the agent use explicit step-by-step reasoning?

> *Reasoning enables the agent to work through problems step by step before producing an answer.*

**If No** → skip `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `reasoning` | Toggle | `False` | Master switch |
| `reasoning_model` | Dropdown or free text | `None` | Separate model for reasoning (can differ from main model) |
| `reasoning_agent` | Agent reference | `None` | Use a sub-agent for reasoning |
| `reasoning_min_steps` | Number | `1` | |
| `reasoning_max_steps` | Number | `10` | |

---

### Q8: Does the agent need structured (typed) output?

> *Structured output returns a Pydantic model or JSON schema instead of free-form text.* See [/agents/usage/agent-with-structured-output](https://docs.agno.com/agents/usage/agent-with-structured-output)

**If No** → skip `output_schema`, `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt`, `parse_response`, `structured_outputs`, `use_json_mode`, `input_schema`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `output_schema` | Pydantic model reference or JSON schema editor | `None` | The primary way to get structured output |
| `structured_outputs` | Toggle | `None` | Use model-native structured outputs if supported |
| `use_json_mode` | Toggle | `False` | Force JSON object response instead of Pydantic |
| `parse_response` | Toggle | `True` | Convert response into output_schema |

**→ Then ask Q8a:**

#### Q8a: Do you need a secondary model to parse or structure the response?

**If No** → skip `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt`

**If Yes** → show:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `parser_model` | Dropdown or free text | `None` | Secondary model to parse primary response |
| `parser_model_prompt` | Text | `None` | Prompt for parser model |
| `output_model` | Dropdown or free text | `None` | Model to structure the final response |
| `output_model_prompt` | Text | `None` | Prompt for output model |

**→ Then ask Q8b:**

#### Q8b: Do you need to validate the input with a schema?

| Field | Input Type | Default |
|---|---|---|
| `input_schema` | Pydantic model reference | `None` |

---

### Q9: Does the agent need session summaries?

> *Session summaries are auto-generated recaps of a conversation, created/updated at the end of runs.*

**If No** → skip `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager`

> **⚠️ Dependency**: Requires `db` (from Q2). If Q2 was "No", show warning.

**If Yes** → show:

| Field | Input Type | Default |
|---|---|---|
| `enable_session_summaries` | Toggle | `False` |
| `add_session_summary_to_context` | Toggle | `None` |
| `session_summary_manager` | Config | `None` |

---

### Q10: Does the agent need context compression?

> *Compression reduces the token cost of tool call results in the context window.*

**If No** → skip `compress_tool_results`, `compression_manager`

**If Yes** → show:

| Field | Input Type | Default |
|---|---|---|
| `compress_tool_results` | Toggle | `False` |
| `compression_manager` | Config | `None` |

---

### Q11: What output delivery and persistence options are needed?

This is a multi-select checklist rather than a single binary:

| Option | Field | Input Type | Default | When to show |
|---|---|---|---|---|
| Stream the response | `stream` | Toggle | `None` | Always show |
| Stream intermediate steps | `stream_events` | Toggle | `False` | Show if `stream` is enabled |
| Persist events on run response | `store_events` | Toggle | `False` | Always show |
| Skip specific event types | `events_to_skip` | Multi-select from `RunEvent` enum | `None` | Show if `store_events` is True |
| Save response to a file | `save_response_to_file` | Text (file path) | `None` | Always show |
| Format output as markdown | `markdown` | Toggle | `False` | Always show |

---

### Q12: Which context enrichment options are needed?

Another multi-select checklist:

| Option | Field | Input Type | Default | Notes |
|---|---|---|---|---|
| Add agent name to instructions | `add_name_to_context` | Toggle | `False` | |
| Add current datetime to instructions | `add_datetime_to_context` | Toggle | `False` | |
| Custom timezone for datetime | `timezone_identifier` | Text (TZ database name) | `None` | Show if `add_datetime_to_context` is True |
| Add current location to instructions | `add_location_to_context` | Toggle | `False` | |
| Wrap instructions in `<instructions>` tags | `add_instruction_tags` | Toggle | `True` | |
| Add additional context to system message | `additional_context` | Textarea | `None` | |
| Add introduction message | `introduction` | Text | `None` | |
| Add expected output description | `expected_output` | Text | `None` | |
| Additional input messages (between system and user) | `additional_input` | List editor | `None` | |

---

### Stage Final — Always Present (Operational)

These appear regardless of answers, but with sensible defaults:

| Field | Input Type | Default | Notes |
|---|---|---|---|
| `retries` | Number | `0` | |
| `delay_between_retries` | Number | `1` | Show if `retries > 0` |
| `exponential_backoff` | Toggle | `False` | Show if `retries > 0` |
| `debug_mode` | Toggle | `False` | |
| `debug_level` | Dropdown: `1` / `2` | `1` | Show if `debug_mode` is True |
| `telemetry` | Toggle | `True` | |
| `role` | Text | `None` | Show only if agent is part of a Team |
| `metadata` | Key-value editor | `None` | |
| `send_media_to_model` | Toggle | `True` | Show if multimodal input is possible |
| `store_media` | Toggle | `True` | Show if `db` is set (Q2 = Yes) |

---

## Parameter Elimination Summary

Here's how many parameters each "No" answer eliminates:

| Question | "No" eliminates | Params skipped |
|---|---|---|
| Q1 (Tools) | 4 + 3 (Q1a) | `tools`, `tool_call_limit`, `tool_choice`, `tool_hooks`, `max_tool_calls_from_history`, `read_chat_history`, `read_tool_call_history` |
| Q2 (Storage) | 8 + 2 (Q2a) + 1 (Q2b) | `db`, `add_history_to_context`, `num_history_runs`, `num_history_messages`, `store_tool_messages`, `store_history_messages`, `search_session_history`, `num_history_sessions`, `cache_session` |
| Q3 (Session State) | 4 | `session_state`, `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state` |
| Q4 (Memory) | 4 | `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context` |
| Q5 (Knowledge) | 6 + 2 (Q5a/b) | `knowledge`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `add_knowledge_to_context`, `knowledge_retriever`, `references_format`, `search_knowledge`, `update_knowledge` |
| Q6 (Hooks) | 2 | `pre_hooks`, `post_hooks` |
| Q7 (Reasoning) | 5 | `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps` |
| Q8 (Structured Output) | 8 + 4 (Q8a) + 1 (Q8b) | `output_schema`, `parse_response`, `structured_outputs`, `use_json_mode`, `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt`, `input_schema` |
| Q9 (Summaries) | 3 | `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager` |
| Q10 (Compression) | 2 | `compress_tool_results`, `compression_manager` |

**A minimal agent** (all "No" except Q1=Yes with tools) needs only: `model`, `name`, `instructions`, `description`, `tools`, `markdown`, `retries`, `debug_mode`, `telemetry` — **9 fields** out of ~75.

**A maximal agent** (all "Yes") surfaces the full ~75 fields, but organised into logical sub-forms with progressive disclosure.

---

## Dependency Matrix

Some questions have hard dependencies — answering "No" to an earlier question should grey out or auto-skip later ones:

| If "No" to... | Then disable... | Why |
|---|---|---|
| Q2 (Storage / `db`) | Q3 (Session State), Q4 (Memory), Q9 (Summaries) | All require database persistence |
| Q5 (Knowledge) | Q5a (`search_knowledge`), Q5b (`update_knowledge`) | No knowledge base = no knowledge tools |
| Q8 (Structured Output) | Q8a (parser/output model) | Parser model only relevant with structured output |
| Q11 `stream`=False | `stream_events` | Can't stream events without streaming |
| Q12 `add_datetime_to_context`=False | `timezone_identifier` | Timezone only matters if datetime is added |
| `retries`=0 | `delay_between_retries`, `exponential_backoff` | No retries = no retry config needed |
| `debug_mode`=False | `debug_level` | No debug = no debug level |

---

## Recommended Form UX Flow

```
┌─────────────────────────────────────┐
│  Stage 0: Base Agent (always shown) │
│  model · name · instructions ·      │
│  description                         │
└──────────────┬──────────────────────┘
               │
   ┌───────────┴───────────┐
   │  Q1: Tools?           │── No ──→ skip 7 params
   │  Q2: Storage?         │── No ──→ skip 11 params + block Q3,Q4,Q9
   │  Q3: Session State?   │── No ──→ skip 4 params
   │  Q4: Memory?          │── No ──→ skip 4 params
   │  Q5: Knowledge/RAG?   │── No ──→ skip 8 params
   │  Q6: Hooks?           │── No ──→ skip 2 params
   │  Q7: Reasoning?       │── No ──→ skip 5 params
   │  Q8: Structured Out?  │── No ──→ skip 13 params
   │  Q9: Summaries?       │── No ──→ skip 3 params
   │  Q10: Compression?   │── No ──→ skip 2 params
   │  Q11: Output/Delivery │  (checklist — always shown, 6 fields)
   │  Q12: Context enrich  │  (checklist — always shown, 9 fields)
   └───────────┬───────────┘
               │
   ┌───────────┴───────────┐
   │  Stage Final: Ops      │
   │  retries · debug ·     │
   │  telemetry · metadata  │
   └───────────────────────┘
```

Each "Yes" expands an inline sub-form with only the relevant fields. The user never sees more than what they've opted into.

---

**Sources used:**

- [https://docs.agno.com/reference/agents/agent](https://docs.agno.com/reference/agents/agent) — full parameter table
- [https://docs.agno.com/agents/building-agents](https://docs.agno.com/agents/building-agents) — "start simple" principle, callable factories
- [https://docs.agno.com/agents/running-agents](https://docs.agno.com/agents/running-agents) — run() override parameters, streaming
- [https://docs.agno.com/agents/usage/agent-with-storage](https://docs.agno.com/agents/usage/agent-with-storage) — storage concepts
- [https://docs.agno.com/agents/usage/agent-with-memory](https://docs.agno.com/agents/usage/agent-with-memory) — memory vs storage, agentic vs update_on_run
- [https://docs.agno.com/agents/usage/agent-with-knowledge](https://docs.agno.com/agents/usage/agent-with-knowledge) — knowledge/RAG concepts
- [https://docs.agno.com/agents/usage/agent-with-structured-output](https://docs.agno.com/agents/usage/agent-with-structured-output) — output_schema usage
- [https://docs.agno.com/agents/usage/agent-with-tools](https://docs.agno.com/agents/usage/agent-with-tools) — tools usage
