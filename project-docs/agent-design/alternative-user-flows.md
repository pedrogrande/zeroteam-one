# Agent Design - Alternative Approaches (Exploration)

*Agent ideation*

---

## A Human-centered, Outcome-focused Approach

The framing maps to **three plain-English questions a person can actually answer**:

1. **What information does the agent need?** → context window content
2. **What tools does the agent need?** → action capabilities
3. **What information do you need about the agent's performance?** → observability

This is better than the previous approach because:

- **It asks about outcomes, not parameters** — a user knows they want "the agent to remember our conversation," not that they need `add_history_to_context=True` with `num_history_runs=5`
- **It groups by user intent** — not by Python type or feature cluster
- **Each answer is independently actionable** — no dependency matrix to manage (mostly)
- **The language is accessible** — no SDK terminology required

The Agno docs themselves support this framing: *"A stateful control loop around a stateless model. The model reasons and calls tools in a loop, guided by instructions. Add memory, knowledge, storage, human-in-the-loop, and guardrails as needed."* ([/agents/overview](https://docs.agno.com/agents/overview))

---

## Refined Version of Your Approach

I'd suggest four sections, not three — splitting out **output** as its own section since it's a distinct decision domain:

### Section 1: What information does the agent need?

These are things the agent needs *to know about* when generating a response — context that gets injected into the messages sent to the model.

| Question (plain English) | If Yes → reveals these fields | Agno docs concept |
|---|---|---|
| **Should the agent remember the current conversation?** | `add_history_to_context`, `num_history_runs`, `num_history_messages` | Chat history → context ([/agents/usage/agent-with-storage](https://docs.agno.com/agents/usage/agent-with-storage)) |
| **Should the agent remember past conversations (other sessions)?** | `search_session_history`, `num_history_sessions` | Session search |
| **Should the agent learn and remember things about its users?** | `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context` | Memory ([/agents/usage/agent-with-memory](https://docs.agno.com/agents/usage/agent-with-memory)) |
| **Should the agent have access to a document/knowledge base (RAG)?** | `knowledge`, `add_knowledge_to_context`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `knowledge_retriever`, `references_format` | Knowledge ([/agents/usage/agent-with-knowledge](https://docs.agno.com/agents/usage/agent-with-knowledge)) |
| **Should the agent know the current date, time, and/or location?** | `add_datetime_to_context`, `timezone_identifier`, `add_location_to_context` | Context enrichment |
| **Should the agent know its own name and identity?** | `add_name_to_context`, `description`, `introduction` | Context enrichment |
| **Does the agent need custom data passed to it (dependencies)?** | `dependencies`, `add_dependencies_to_context` | Dependencies |
| **Does the agent need to maintain state within a session?** | `session_state`, `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state` | Session state |
| **Does the agent need extra context added to its instructions?** | `additional_context`, `expected_output`, `additional_input` | Context engineering ([/context/overview](https://docs.agno.com/context/overview)) |

> **Hidden consequence**: Answering "Yes" to conversation memory, past sessions, user memory, or session state reveals the **database** question: *"Where should this be stored?"* → `db`, `store_tool_messages`, `store_history_messages`, `cache_session`

### Section 2: What tools does the agent need?

These are actions the agent can take — functions it can call during its reasoning loop. Agno ships 120+ pre-built toolkits ([/tools/overview](https://docs.agno.com/tools/overview)).

| Question (plain English) | If Yes → reveals these fields | Notes |
|---|---|---|
| **What pre-built toolkits should the agent have?** | `tools` (multi-select from Agno's 120+ toolkits) | Web search, scraping, databases, email, file generation, social, etc. |
| **Do you have custom tools (your own Python functions)?** | `tools` (add custom callables) | See [/tools/overview](https://docs.agno.com/tools/overview) |
| **Should the agent be able to read its own chat history?** | `read_chat_history` | Implicit tool injection |
| **Should the agent be able to search its knowledge base?** | `search_knowledge` | Implicit tool injection (default `True` when knowledge is set) |
| **Should the agent be able to update its knowledge base?** | `update_knowledge` | Implicit tool injection |
| **Should the agent be able to read its tool call history?** | `read_tool_call_history` | Implicit tool injection |
| **Should the agent be able to update its own session state?** | `enable_agentic_state` | Implicit tool injection |
| **Do you need to limit or control tool usage?** | `tool_call_limit`, `tool_choice`, `max_tool_calls_from_history` | |
| **Do you need functions to run between tool calls?** | `tool_hooks` | See [/tools/hooks](https://docs.agno.com/tools/hooks) |

### Section 3: How should the agent's output be structured and delivered?

| Question (plain English) | If Yes → reveals these fields | Agno docs concept |
|---|---|---|
| **Should the response be structured (typed) instead of free-form text?** | `output_schema`, `parse_response`, `structured_outputs`, `use_json_mode` | Structured output ([/agents/usage/agent-with-structured-output](https://docs.agno.com/agents/usage/agent-with-structured-output)) |
| **Do you need a secondary model to parse or improve the response?** | `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt` | Output model ([/input-output/output-model](https://docs.agno.com/input-output/output-model)) |
| **Should the input be validated with a schema?** | `input_schema` | Structured input |
| **Should the response be streamed?** | `stream`, `stream_events` | Streaming ([/agents/running-agents](https://docs.agno.com/agents/running-agents)) |
| **Should events be persisted?** | `store_events`, `events_to_skip` | |
| **Should the response be saved to a file?** | `save_response_to_file` | |
| **Should the response be formatted as markdown?** | `markdown` | |
| **Can the agent receive images, audio, video, or files?** | `send_media_to_model`, `store_media` | Multimodal ([/input-output/multimodal](https://docs.agno.com/input-output/multimodal)) |

### Section 4: What information do you need about the agent's performance?

| Question (plain English) | If Yes → reveals these fields | Agno docs concept |
|---|---|---|
| **Do you need to inspect the agent's execution flow?** | `debug_mode`, `debug_level` | Debugging ([/agents/debugging-agents](https://docs.agno.com/agents/debugging-agents)) |
| **Do you need security checks or input/output validation?** | `pre_hooks`, `post_hooks` | Hooks/guardrails ([/hooks/overview](https://docs.agno.com/hooks/overview)) |
| **Do you need the agent to reason step-by-step before answering?** | `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps` | Reasoning |
| **Should the agent create summaries of its sessions?** | `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager` | Session summaries |
| **Do you need to compress tool results to save context space?** | `compress_tool_results`, `compression_manager` | Compression |
| **Should the agent retry on failure?** | `retries`, `delay_between_retries`, `exponential_backoff` | Error handling ([/models/overview](https://docs.agno.com/models/overview)) |
| **Is this agent part of a team?** | `role` | Team membership |
| **Do you need to store metadata with the agent?** | `metadata` | |
| **Do you want to disable telemetry?** | `telemetry` (default `True`) | |

---

## Alternative Approaches to Consider

### Alternative A: Goal-Driven (Use-Case Templates)

Instead of asking about features, ask **what the agent is for**:

```
What is this agent's primary purpose?

  ○ Chatbot / conversational assistant
  ○ Data extraction / classification
  ○ Research / report generation
  ○ Code assistant
  ○ Customer support
  ○ Custom
```

Each template pre-fills a recommended parameter set and greys out irrelevant options.

| Strength | Weakness |
|---|---|
| Fastest path to a working agent | Templates may not fit edge cases |
| Reduces cognitive load dramatically | User still needs to customize |
| Maps to Agno's "start simple" philosophy | Limited flexibility for unusual combos |

**When to use**: Onboarding flow, MVP builder, users who don't know what they need yet.

---

### Alternative B: Capability Toggles (Feature Checklist)

A single flat page of toggle switches, each labelled in plain English:

```
☑ Tools (external actions)
☑ Conversation memory
☐ User memory (learning)
☐ Knowledge base (RAG)
☐ Session state
☐ Structured output
☐ Step-by-step reasoning
☐ Input guardrails
☐ Output guardrails
☐ Streaming
...
```

Each toggle expands inline to reveal its sub-fields.

| Strength | Weakness |
|---|---|
| Everything visible at a glance — no surprise features | Can be overwhelming (~15+ toggles) |
| No multi-step wizard flow | Doesn't enforce dependencies |
| Familiar pattern (settings page) | Still requires the user to know what each means |

**When to use**: Power-user config screen, experienced users who know exactly what they want.

---

### Alternative C: Progressive Wizard (Question → Question)

A single-column wizard that asks one question at a time, branching based on answers:

```
Q1: "What should this agent do?"
     └─ User types description
Q2: "Should it be able to take actions (call APIs, search the web, etc.)?"
     ├─ Yes → "Which tools?" → multi-select
     └─ No → continue
Q3: "Should it remember your conversations?"
     ├─ Yes → "Across sessions too?" → ...
     └─ No → continue
...
```

| Strength | Weakness |
|---|---|
| Lowest cognitive load per step | Many clicks for complex agents |
| Natural dependency handling | Slow for power users |
| Feels like a guided conversation | Hard to jump to a specific section |

**When to use**: First-time users, consumer-facing builder UI.

---

### Alternative D: Hybrid (Recommended)

Combine your question-based approach with templates and progressive disclosure:

```
Step 1: Pick a starting point
        ○ Start blank
        ○ Conversational assistant (template)
        ○ Research agent (template)
        ○ Data extraction (template)
        ○ Custom

Step 2: Adjust capabilities (your four sections as toggle groups)
        ┌─ What information does the agent need? ──────┐
        │  ☑ Conversation memory                      │
        │  ☐ User memory                              │
        │  ☐ Knowledge base                            │
        │  ...                                         │
        └─────────────────────────────────────────────┘
        ┌─ What tools does the agent need? ───────────┐
        │  ...                                         │
        └─────────────────────────────────────────────┘
        ┌─ How should output be structured? ──────────┐
        │  ...                                         │
        └─────────────────────────────────────────────┘
        ┌─ What do you need to observe? ───────────────┐
        │  ...                                         │
        └─────────────────────────────────────────────┘

Step 3: Review generated code
        (live preview of the Agent() constructor)
```

| Strength | Weakness |
|---|---|
| Templates give fast start; toggles allow full control | More engineering effort to build |
| Serves both novices and power users | Need to maintain template definitions |
| Live code preview builds confidence | |
| Dependency hints can be inline warnings | |

---

## Recommendation

Your approach (four intent-based sections) is the right foundation. I'd build it as the **Hybrid (Alternative D)**:

1. **Templates up front** for fast starts — they answer 80% of needs in one click
2. **Your four sections as collapsible toggle groups** for the remaining 20%
3. **Inline dependency hints** — e.g. selecting "user memory" shows a note: *"This requires a database — configure storage below"*
4. **Live code preview** at the bottom so the user sees what they're building

The four sections map cleanly to how Agno itself describes agents: *"a stateful control loop around a stateless model — add memory, knowledge, storage, human-in-the-loop, and guardrails as needed"* ([/agents/overview](https://docs.agno.com/agents/overview)).

---

**Sources used:**

- [https://docs.agno.com/agents/overview](https://docs.agno.com/agents/overview) — agent definition, "add features as needed"
- [https://docs.agno.com/agents/building-agents](https://docs.agno.com/agents/building-agents) — "start simple" principle
- [https://docs.agno.com/agents/running-agents](https://docs.agno.com/agents/running-agents) — streaming, run overrides
- [https://docs.agno.com/agents/debugging-agents](https://docs.agno.com/agents/debugging-agents) — debug mode
- [https://docs.agno.com/agents/usage/agent-with-storage](https://docs.agno.com/agents/usage/agent-with-storage) — storage concepts
- [https://docs.agno.com/agents/usage/agent-with-memory](https://docs.agno.com/agents/usage/agent-with-memory) — memory vs storage
- [https://docs.agno.com/agents/usage/agent-with-knowledge](https://docs.agno.com/agents/usage/agent-with-knowledge) — knowledge/RAG
- [https://docs.agno.com/agents/usage/agent-with-structured-output](https://docs.agno.com/agents/usage/agent-with-structured-output) — structured output
- [https://docs.agno.com/tools/overview](https://docs.agno.com/tools/overview) — 120+ toolkits, tool definition
- [https://docs.agno.com/tools/selecting-tools](https://docs.agno.com/tools/selecting-tools) — include/exclude tools
- [https://docs.agno.com/hooks/overview](https://docs.agno.com/hooks/overview) — hooks/guardrails
- [https://docs.agno.com/context/overview](https://docs.agno.com/context/overview) — context engineering
- [https://docs.agno.com/input-output/overview](https://docs.agno.com/input-output/overview) — input/output formats
- [https://docs.agno.com/models/overview](https://docs.agno.com/models/overview) — models, retry/error handling
- [https://docs.agno.com/reference/agents/agent](https://docs.agno.com/reference/agents/agent) — full parameter reference

===

These are three different lenses — let me map each one against the Agent parameters, then assess whether they're distinct from or fold into the four-section approach.

---

## By Outputs

"What does the agent produce, and in what form?"

This is closely related to Section 3, but could be broadened to cover *everything that comes out of a run* — not just the response format, but also side effects, persisted artifacts, and observability data.

| Output Category | Parameters |
|---|---|
| **Response format** | `output_schema`, `parse_response`, `structured_outputs`, `use_json_mode`, `markdown` |
| **Response transformation** | `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt` |
| **Response delivery** | `stream`, `stream_events`, `save_response_to_file` |
| **Events / telemetry output** | `store_events`, `events_to_skip`, `telemetry` |
| **Side effects** (things written to DB) | `store_media`, `store_tool_messages`, `store_history_messages` |
| **Auto-generated artifacts** | `enable_session_summaries` → produces session summaries; `update_memory_on_run` → produces user memories; `update_knowledge` → produces knowledge updates |
| **Validated output** | `post_hooks` (output validation before return) |
| **Input validation** (what gets accepted as input) | `input_schema`, `pre_hooks` |

**Verdict**: This already fits into Section 3 almost entirely. The only addition is recognising that session summaries, memory updates, and knowledge updates are also "outputs" — they're things the agent *produces* as a side effect of running. That's a useful reframing but doesn't require a new section.

---

## By Goals

"What is this agent trying to achieve?"

This is the highest-level lens — it's about purpose, not mechanism. A goal-driven form would start with the agent's mission and derive parameters from that.

| Goal | Parameters it implies | Existing section |
|---|---|---|
| **Answer questions from a knowledge base** | `knowledge`, `add_knowledge_to_context`, `search_knowledge`, `references_format` | Section 1 (info) |
| **Have ongoing conversations** | `db`, `add_history_to_context`, `num_history_runs`, `num_history_messages` | Section 1 (info) |
| **Learn about users over time** | `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context`, `user_id` | Section 1 (info) |
| **Take actions in external systems** | `tools`, `tool_call_limit`, `tool_choice`, `tool_hooks` | Section 2 (tools) |
| **Produce structured/validated data** | `output_schema`, `input_schema`, `parse_response`, `structured_outputs`, `post_hooks` | Section 3 (output) |
| **Reason through complex problems** | `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps` | Section 4 (performance) |
| **Maintain safe interactions** | `pre_hooks`, `post_hooks` | Section 4 (performance) |
| **Operate reliably under failure** | `retries`, `delay_between_retries`, `exponential_backoff` | Section 4 (performance) |
| **Be observable and debuggable** | `debug_mode`, `debug_level`, `store_events`, `events_to_skip` | Section 4 (performance) |
| **Manage its own state** | `session_state`, `enable_agentic_state`, `add_session_state_to_context` | Section 1 (info) |
| **Work as part of a team** | `role` | (Not covered — team-level) |

**Verdict**: Goals don't map to a new section — they map *across* all four existing sections. A goal is a cross-section intent that activates fields in multiple sections at once. This makes goals ideal as a **pre-selection mechanism** (the template approach from Alternative A in my previous answer), not as a replacement for the sections.

For example, selecting the goal "Learn about users over time" would auto-enable fields in Section 1 (memory params) *and* require a database (revealing storage fields also in Section 1). The goal doesn't replace the sections — it *pre-populates* them.

---

## By Responsibilities

"What is this agent accountable for?"

This is the most interesting lens because it's genuinely orthogonal to the existing approach. The four sections ask "what does the agent *have*?" (capabilities). Responsibilities ask "what must the agent *ensure*?" (obligations). That's a different mental model that groups parameters differently.

| Responsibility | What the agent must ensure | Parameters |
|---|---|---|
| **Remembering** | Conversations continue across runs and sessions | `db`, `add_history_to_context`, `num_history_runs`, `num_history_messages`, `search_session_history`, `num_history_sessions`, `cache_session`, `session_state`, `add_session_state_to_context`, `enable_agentic_state`, `overwrite_db_session_state` |
| **Learning** | User knowledge accumulates over time | `memory_manager`, `enable_agentic_memory`, `update_memory_on_run`, `add_memories_to_context` |
| **Knowing** | Agent has access to relevant information | `knowledge`, `add_knowledge_to_context`, `knowledge_filters`, `enable_agentic_knowledge_filters`, `knowledge_retriever`, `references_format`, `search_knowledge`, `update_knowledge`, `dependencies`, `add_dependencies_to_context` |
| **Self-awareness** | Agent knows when it is, where it is, who it is | `add_name_to_context`, `add_datetime_to_context`, `add_location_to_context`, `timezone_identifier`, `introduction`, `description` |
| **Safety** | Inputs and outputs are validated and filtered | `pre_hooks`, `post_hooks`, `input_schema` |
| **Quality** | Output meets structural and content standards | `output_schema`, `parse_response`, `structured_outputs`, `use_json_mode`, `parser_model`, `parser_model_prompt`, `output_model`, `output_model_prompt`, `expected_output`, `markdown` |
| **Reliability** | Agent recovers from failure and doesn't lose data | `retries`, `delay_between_retries`, `exponential_backoff`, `store_tool_messages`, `store_history_messages`, `store_media` |
| **Efficiency** | Context window is used wisely | `compress_tool_results`, `compression_manager`, `max_tool_calls_from_history`, `tool_call_limit` |
| **Transparency** | You can see what the agent did and why | `debug_mode`, `debug_level`, `store_events`, `events_to_skip`, `telemetry`, `read_chat_history`, `read_tool_call_history` |
| **Delivery** | Output reaches the user in the right form | `stream`, `stream_events`, `save_response_to_file`, `send_media_to_model` |
| **Reasoning** | Agent thinks before acting | `reasoning`, `reasoning_model`, `reasoning_agent`, `reasoning_min_steps`, `reasoning_max_steps` |
| **Summarising** | Sessions are captured for future reference | `enable_session_summaries`, `add_session_summary_to_context`, `session_summary_manager` |

### How responsibilities differ from the four-section approach

| | Four-Section (Capabilities) | Responsibilities |
|---|---|---|
| **Question** | "What does the agent need?" | "What must the agent ensure?" |
| **Mental model** | Builder (assembling parts) | Owner (defining duties) |
| **Grouping logic** | By feature domain | By obligation type |
| **Overlap** | Each param in exactly one section | Some params appear in multiple responsibilities (e.g. `pre_hooks` is both Safety and Quality) |
| **Best for** | Developers configuring an agent | Product owners / spec writers defining requirements |

The key difference: responsibilities have **overlapping membership**. `post_hooks` is both a Safety responsibility (output filtering) and a Quality responsibility (output validation). The four-section approach avoids this by putting each parameter in exactly one bucket.

---

## How They All Fit Together

Here's the relationship:

```
Goals          →  Pre-selection (templates)
                  "I want an agent that does X"
                       │
                       ▼
Responsibilities  →  Requirements definition (optional layer)
                  "The agent must ensure Y"
                       │
                       ▼
Four Sections    →  Configuration (the actual form)
                  "What info? What tools? What output? What observability?"
                       │
                       ▼
Outputs          →  Post-run verification (preview/validation)
                  "Did the agent produce Z?"
```

### Practical recommendation

You don't need to choose between these. They work as **layers**:

1. **Goals as the entry point** — templates that pre-select across all four sections. This is the fastest path for users who know what they want but not how to configure it.

2. **The four sections as the configuration body** — this is where the user actually toggles and fills fields. It remains the core of the form.

3. **Responsibilities as an optional view/filter** — for users who prefer to think in terms of obligations ("my agent must be safe, must remember, must produce quality output"), offer a toggle that re-groups the same fields by responsibility instead of by capability. Same fields, different labels and grouping.

4. **Outputs as the preview/validation step** — at the bottom of the form, show what the agent will produce: "This agent will produce structured Pydantic responses, stream them in real-time, persist conversation history to SQLite, and auto-generate session summaries." This is a confirmation/summary, not a configuration section.

### What this looks like in the UI

```
┌─────────────────────────────────────────────────┐
│  Step 1: What's this agent for?                  │
│  [ Conversational assistant ▾ ]  ← goal/template │
│  (pre-fills sections below)                      │
├─────────────────────────────────────────────────┤
│  Step 2: Configure                               │
│                                                   │
│  View by: [Capabilities ▾]  ← or "Responsibilities"│
│                                                   │
│  ┌─ What info does the agent need? ──────────────┐│
│  │  (or "Remembering & Learning" in resp. view)  ││
│  │  ☑ Conversation memory                        ││
│  │  ☑ User memory                                ││
│  │  ☐ Knowledge base                             ││
│  │  ...                                          ││
│  └───────────────────────────────────────────────┘│
│  ┌─ What tools? ───────────────────────────────┐ │
│  │  ...                                          ││
│  └───────────────────────────────────────────────┘│
│  ┌─ How should output be structured? ───────────┐│
│  │  ...                                          ││
│  └───────────────────────────────────────────────┘│
│  ┌─ What do you need to observe? ────────────────┐│
│  │  ...                                          ││
│  └───────────────────────────────────────────────┘│
├─────────────────────────────────────────────────┤
│  Step 3: Preview                                  │
│  This agent will:                                 │
│  · Produce structured Pydantic responses         │← outputs
│  · Stream responses in real-time                 │
│  · Persist conversations to SQLite               │
│  · Auto-generate session summaries               │
│  · Validate inputs with pre-hooks                │
│                                                   │
│  [ Generated code preview ]                       │
└─────────────────────────────────────────────────┘
```

The **view toggle** between "Capabilities" and "Responsibilities" is the key innovation — same fields, same form, just regrouped and relabeled for a different mental model. A developer thinks "what does it need?" A product owner thinks "what must it ensure?" Both end up configuring the same agent.

---

**Summary**: Goals, outputs, and responsibilities don't replace the four-section approach — they *layer on top of it*. Goals become the entry point (templates), outputs become the preview/confirmation, and responsibilities become an alternative view/filter for the same configuration fields. The four sections remain the structural backbone because they have clean non-overlapping parameter membership, which makes for a clean form.
