# Agent Design - Parameter Categorisations

Great question. Having confirmed the parameter table against the official Agno docs at [/reference/agents/agent](https://docs.agno.com/reference/agents/agent), here are **ten distinct categorisation schemes** you could apply to these ~75 parameters, each revealing a different structural view of the `Agent` class.

---

## 1. By Functional Feature / Domain

Groups parameters by *what capability they configure*:

| Category | Parameters |
|---|---|
| **Identity & Metadata** | `model`, `name`, `id`, `user_id`, `session_id`, `role`, `metadata` |
| **Session State** | `session_state`, `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state`, `cache_session` |
| **Session History** | `search_session_history`, `num_history_sessions`, `add_history_to_context`, `num_history_runs`, `num_history_messages`, `max_tool_calls_from_history`, `read_chat_history`, `read_tool_call_history` |
| **Dependencies** | `dependencies`, `add_dependencies_to_context` |
| **Database / Storage** | `db`, `store_media`, `store_tool_messages`, `store_history_messages` |
| **Memory** | `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context` |
| **Session Summaries** | `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager` |
| **Compression** | `compress_tool_results`, `compression_manager` |
| **Knowledge / RAG** | `knowledge`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `add_knowledge_to_context`, `knowledge_retriever`, `references_format`, `search_knowledge`, `update_knowledge` |
| **Tools** | `tools`, `tool_call_limit`, `tool_choice`, `tool_hooks` |
| **Hooks / Guardrails** | `pre_hooks`, `post_hooks` |
| **Reasoning** | `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps` |
| **Prompt / Instructions** | `system_message`, `system_message_role`, `introduction`, `build_context`, `description`, `instructions`, `add_instruction_tags`, `expected_output`, `additional_context`, `markdown`, `add_name_to_context`, `add_datetime_to_context`, `add_location_to_context`, `timezone_identifier`, `resolve_in_context`, `additional_input`, `user_message_role`, `build_user_context` |
| **Input / Output Schema** | `input_schema`, `output_schema`, `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt`, `parse_response`, `structured_outputs`, `use_json_mode` |
| **Media** | `send_media_to_model` |
| **Response Handling** | `save_response_to_file`, `stream`, `stream_events`, `store_events`, `events_to_skip` |
| **Retry / Resilience** | `retries`, `delay_between_retries`, `exponential_backoff` |
| **Debug / Telemetry** | `debug_mode`, `debug_level`, `telemetry` |

---

## 2. By Data Type

Groups parameters by their Python type signature:

| Type Pattern | Parameters |
|---|---|
| **`bool`** (plain) | `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state`, `cache_session`, `add_dependencies_to_context`, `enable_agentic_memory`, `update_memory_on_run`, `enable_session_summaries`, `compress_tool_results`, `add_history_to_context`, `add_knowledge_to_context`, `reasoning`, `read_chat_history`, `update_knowledge`, `read_tool_call_history`, `send_media_to_model`, `store_media`, `store_tool_messages`, `store_history_messages`, `build_context`, `add_instruction_tags`, `markdown`, `add_name_to_context`, `add_datetime_to_context`, `add_location_to_context`, `resolve_in_context`, `build_user_context`, `exponential_backoff`, `parse_response`, `use_json_mode`, `stream_events`, `store_events`, `debug_mode`, `telemetry` |
| **`Optional[bool]`** | `search_session_history`, `add_memories_to_context`, `add_session_summary_to_context`, `enable_agentic_knowledge_filters`, `structured_outputs`, `stream` |
| **`int`** (plain) | `reasoning_min_steps`, `reasoning_max_steps`, `retries`, `delay_between_retries` |
| **`Optional[int]`** | `num_history_sessions`, `num_history_runs`, `num_history_messages`, `max_tool_calls_from_history`, `tool_call_limit` |
| **`str` / `Optional[str]`** | `name`, `id`, `user_id`, `session_id`, `system_message_role`, `introduction`, `description`, `expected_output`, `additional_context`, `timezone_identifier`, `user_message_role`, `role`, `save_response_to_file`, `parser_model_prompt`, `output_model_prompt` |
| **`Dict[str, Any]`** | `session_state`, `dependencies`, `knowledge_filters`, `metadata` |
| **`Literal[...]`** | `references_format` (`"json"` / `"yaml"`), `debug_level` (`1` / `2`) |
| **Complex objects** (Model, BaseDb, Knowledge, etc.) | `model`, `db`, `memory_manager`, `session_summary_manager`, `compression_manager`, `knowledge`, `reasoning_model`, `reasoning_agent`, `system_message`, `instructions`, `input_schema`, `output_schema`, `parser_model`, `output_model` |
| **List / Callable types** | `tools`, `tool_hooks`, `pre_hooks`, `post_hooks`, `knowledge_retriever`, `additional_input`, `events_to_skip` |

---

## 3. By Default Value

| Default | Count | Examples |
|---|---|---|
| **`None`** | ~48 | `model`, `name`, `id`, `session_state`, `db`, `tools`, `knowledge`, `instructions`, `output_schema`, … |
| **`False`** | ~23 | `add_session_state_to_context`, `enable_agentic_memory`, `reasoning`, `stream_events`, `debug_mode`, … |
| **`True`** | ~10 | `search_knowledge`, `send_media_to_model`, `store_media`, `build_context`, `add_instruction_tags`, `resolve_in_context`, `build_user_context`, `parse_response`, `telemetry` |
| **Specific non-`None` value** | ~8 | `system_message_role="system"`, `user_message_role="user"`, `reasoning_min_steps=1`, `reasoning_max_steps=10`, `retries=0`, `delay_between_retries=1`, `debug_level=1`, `references_format="json"` |

---

## 4. By Optionality (`Optional` wrapper vs. not)

| Category | Description | Examples |
|---|---|---|
| **`Optional[...]`** | Explicitly nullable — the parameter can be absent | `model`, `name`, `id`, `user_id`, `session_id`, `session_state`, `db`, `tools`, `knowledge`, `instructions`, `output_schema`, `pre_hooks`, `post_hooks`, `stream`, `role`, … (~48 params) |
| **Non-Optional** | Always has a value (even if default is `False`/`0`/`""`) | All `bool` params, `int` params like `retries`/`reasoning_min_steps`, `str` params like `system_message_role`/`user_message_role`, `Literal` params (~27 params) |

---

## 5. By Lifecycle Phase (when the parameter takes effect)

| Phase | Parameters |
|---|---|
| **Construction / Identity** (set once) | `model`, `name`, `id`, `role`, `metadata`, `db`, `debug_mode`, `debug_level`, `telemetry` |
| **Session Setup** | `user_id`, `session_id`, `session_state`, `cache_session` |
| **Pre-processing / Context Building** (before model call) | `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state`, `dependencies`, `add_dependencies_to_context`, `search_session_history`, `num_history_sessions`, `add_history_to_context`, `num_history_runs`, `num_history_messages`, `max_tool_calls_from_history`, `memory_manager`, `enable_agentic_memory`, `add_memories_to_context`, `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager`, `compress_tool_results`, `compression_manager`, `knowledge`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `add_knowledge_to_context`, `knowledge_retriever`, `references_format`, `system_message`, `system_message_role`, `introduction`, `build_context`, `description`, `instructions`, `add_instruction_tags`, `expected_output`, `additional_context`, `markdown`, `add_name_to_context`, `add_datetime_to_context`, `add_location_to_context`, `timezone_identifier`, `resolve_in_context`, `additional_input`, `user_message_role`, `build_user_context`, `read_chat_history`, `search_knowledge`, `update_knowledge`, `read_tool_call_history`, `send_media_to_model`, `pre_hooks` |
| **During Model Call / Tool Loop** | `tools`, `tool_call_limit`, `tool_choice`, `tool_hooks`, `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps`, `input_schema`, `output_schema` |
| **Post-processing** (after response, before return) | `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt`, `parse_response`, `structured_outputs`, `use_json_mode`, `post_hooks`, `update_memory_on_run`, `save_response_to_file` |
| **Storage / Persistence** | `store_media`, `store_tool_messages`, `store_history_messages`, `store_events`, `events_to_skip` |
| **Delivery / Output** | `stream`, `stream_events` |
| **Resilience** (wraps entire run) | `retries`, `delay_between_retries`, `exponential_backoff` |

---

## 6. By Scope (what entity the parameter pertains to)

| Scope | Parameters |
|---|---|
| **Agent-level** (intrinsic definition) | `model`, `name`, `id`, `role`, `description`, `instructions`, `expected_output`, `additional_context`, `markdown`, `tools`, `tool_call_limit`, `tool_choice`, `tool_hooks`, `pre_hooks`, `post_hooks`, `reasoning` + reasoning sub-params, `input_schema`, `output_schema` + output sub-params, `debug_mode`, `debug_level`, `telemetry`, `metadata`, `save_response_to_file` |
| **User-level** | `user_id`, `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context` |
| **Session-level** | `session_id`, `session_state`, `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state`, `cache_session`, `search_session_history`, `num_history_sessions`, `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager` |
| **Run-level** | `retries`, `delay_between_retries`, `exponential_backoff`, `stream`, `stream_events`, `store_events`, `events_to_skip` |
| **Knowledge-level** | `knowledge`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `add_knowledge_to_context`, `knowledge_retriever`, `references_format`, `search_knowledge`, `update_knowledge` |
| **History-level** | `add_history_to_context`, `num_history_runs`, `num_history_messages`, `max_tool_calls_from_history`, `read_chat_history`, `read_tool_call_history` |
| **Database / Storage-level** | `db`, `store_media`, `store_tool_messages`, `store_history_messages` |
| **Context / Prompt-level** | `system_message`, `system_message_role`, `introduction`, `build_context`, `add_instruction_tags`, `add_name_to_context`, `add_datetime_to_context`, `add_location_to_context`, `timezone_identifier`, `resolve_in_context`, `additional_input`, `user_message_role`, `build_user_context`, `dependencies`, `add_dependencies_to_context` |
| **Media-level** | `send_media_to_model`, `store_media` |
| **Compression-level** | `compress_tool_results`, `compression_manager` |

---

## 7. By Effect on LLM Context Window

Whether and how the parameter injects content into the messages sent to the model:

| Effect | Parameters |
|---|---|
| **System message construction** | `system_message`, `system_message_role`, `description`, `instructions`, `add_instruction_tags`, `expected_output`, `additional_context`, `introduction`, `markdown`, `build_context` |
| **Context enrichment (injected into instructions)** | `add_name_to_context`, `add_datetime_to_context`, `add_location_to_context`, `timezone_identifier`, `resolve_in_context` |
| **Session state → context** | `add_session_state_to_context` |
| **Dependencies → context** | `add_dependencies_to_context` |
| **History → context** | `add_history_to_context`, `num_history_runs`, `num_history_messages`, `max_tool_calls_from_history` |
| **Memory → context** | `add_memories_to_context` |
| **Session summaries → context** | `add_session_summary_to_context` |
| **Knowledge / RAG → context** | `add_knowledge_to_context`, `knowledge_retriever`, `references_format` |
| **Additional messages** | `additional_input` |
| **Media → context** | `send_media_to_model` |
| **Implicit tool injection** (adds tools that appear in the tool schema) | `read_chat_history`, `search_knowledge`, `update_knowledge`, `read_tool_call_history`, `enable_agentic_state`, `enable_agentic_memory`, `enable_agentic_knowledge_filters` |
| **No direct context effect** | `model`, `name`, `id`, `user_id`, `session_id`, `db`, `metadata`, `tool_call_limit`, `tool_choice`, `tool_hooks`, `pre_hooks`, `post_hooks`, reasoning params, retry params, store params, stream params, debug params, telemetry, output schema params, `save_response_to_file` |

---

## 8. By Whether They Implicitly Inject Tools

A special sub-category — these `bool` flags don't just configure behaviour; they **automatically add tools** to the agent's tool list:

| Parameter | Tool(s) added |
|---|---|
| `enable_agentic_state` | Tools to update `session_state` dynamically |
| `read_chat_history` | Tool to read chat history |
| `search_knowledge` (default `True`) | Tool to search the knowledge base |
| `update_knowledge` | Tool to update the knowledge base |
| `read_tool_call_history` | Tool to get tool call history |
| `enable_agentic_memory` | Tools to manage user memories |
| `enable_agentic_knowledge_filters` | Lets the agent choose knowledge filters |

---

## 9. By Dependency Clusters (parameters that work together)

Parameters that form tightly coupled configuration groups — setting one without the other(s) is often meaningless:

| Cluster | Parameters |
|---|---|
| **Session State** | `session_state` → `add_session_state_to_context` → `enable_agentic_state` → `overwrite_db_session_state` → `cache_session` |
| **History** | `add_history_to_context` → `num_history_runs` → `num_history_messages` → `max_tool_calls_from_history` → `read_chat_history` → `read_tool_call_history` |
| **Memory** | `memory_manager` → `enable_agentic_memory` → `update_memory_on_run` → `add_memories_to_context` |
| **Session Summaries** | `enable_session_summaries` → `add_session_summary_to_context` → `session_summary_manager` |
| **Compression** | `compress_tool_results` → `compression_manager` |
| **Knowledge / RAG** | `knowledge` → `knowledge_filters` → `enable_agentic_knowledge_filters` → `add_knowledge_to_context` → `knowledge_retriever` → `references_format` → `search_knowledge` → `update_knowledge` |
| **Reasoning** | `reasoning` → `reasoning_model` → `reasoning_agent` → `reasoning_min_steps` → `reasoning_max_steps` |
| **Output Schema** | `output_schema` → `parser_model` → `parser_model_prompt` → `output_model` → `output_model_prompt` → `parse_response` → `structured_outputs` → `use_json_mode` |
| **Retry** | `retries` → `delay_between_retries` → `exponential_backoff` |
| **Prompt / Instructions** | `system_message` → `system_message_role` → `description` → `instructions` → `add_instruction_tags` → `expected_output` → `additional_context` → `introduction` → `markdown` |
| **Context Enrichment** | `add_name_to_context` → `add_datetime_to_context` → `add_location_to_context` → `timezone_identifier` → `resolve_in_context` |
| **Dependencies** | `dependencies` → `add_dependencies_to_context` |
| **Events** | `stream` → `stream_events` → `store_events` → `events_to_skip` |
| **Debug** | `debug_mode` → `debug_level` |

---

## 10. By Run-Time Override-ability

Based on the `run()` / `arun()` method signatures in the reference docs, some constructor parameters can be **overridden per-run** while others are **constructor-only**:

| Category | Parameters |
|---|---|
| **Overridable at `run()` time** | `user_id`, `session_id`, `session_state`, `retries`, `knowledge_filters`, `add_history_to_context`, `add_dependencies_to_context`, `add_session_state_to_context`, `dependencies`, `metadata`, `output_schema`, `debug_mode`, `stream`, `stream_events` |
| **Constructor-only** (cannot be overridden per-run) | Everything else — `model`, `tools`, `instructions`, `knowledge`, `db`, `memory_manager`, `pre_hooks`, `post_hooks`, reasoning params, compression params, store params, etc. |

---

### Summary

| # | Categorisation Axis | What It Reveals |
|---|---|---|
| 1 | **Functional feature** | What capability domain each parameter belongs to |
| 2 | **Data type** | The Python type system shape of the API |
| 3 | **Default value** | Agno's opinionated defaults (what's on/off by default) |
| 4 | **Optionality** | Whether a parameter is nullable (`Optional`) or always present |
| 5 | **Lifecycle phase** | When in the agent run the parameter takes effect |
| 6 | **Scope** | What entity (agent, user, session, run, knowledge) the parameter governs |
| 7 | **Context window effect** | Whether/how the parameter injects content into the LLM prompt |
| 8 | **Implicit tool injection** | Which `bool` flags auto-add tools vs. just configuring behaviour |
| 9 | **Dependency clusters** | Which parameters must be used together to be meaningful |
| 10 | **Run-time override-ability** | Which params can be overridden per-run vs. locked at construction |

These aren't mutually exclusive — they're **lenses**. Schemes 1, 5, and 9 are probably the most useful for building a mental model of the agent's architecture, while schemes 7 and 8 are the most useful for **context engineering** (managing what actually reaches the model's context window). Scheme 10 is critical for understanding the constructor vs. run-time API surface.

**Source**: [https://docs.agno.com/reference/agents/agent](https://docs.agno.com/reference/agents/agent)
