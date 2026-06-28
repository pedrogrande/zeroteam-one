# Context Management Exploration

The Agno docs are rich with mechanisms for context management, and they directly support the principle of "minimum sufficient." Let me design the guidance system.

---

## The Core Problem

Every feature you enable adds **permanent overhead** to the context window on every single run. The Agno docs lay this out explicitly:

> *"Tool definitions can be a meaningful part of the total token count, especially with large parameter schemas or long descriptions."* ([/compression/token-counting](https://docs.agno.com/compression/token-counting))

> *"Without compression, tool results quickly consume your context window."* ([/compression/overview](https://docs.agno.com/compression/overview))

And the context engineering docs frame the fundamental question:

> *"Building context comes down to one question: 'Which information is most likely to achieve the desired outcome?'"* ([/context/agent/overview](https://docs.agno.com/context/agent/overview))

The building-agents docs reinforce starting simple:

> *"Start simple: a model, tools, and instructions. Once that works, layer in more functionality as needed."* ([/agents/building-agents](https://docs.agno.com/agents/building-agents))

---

## What Adds Context (The Full Inventory)

Here's what each enabled feature costs in the context window, based on the system message construction docs ([/context/agent/overview](https://docs.agno.com/context/agent/overview)) and token counting docs ([/compression/token-counting](https://docs.agno.com/compression/token-counting)):

### Static overhead (present on every run)

| Feature | What it adds to context | Cost |
|---|---|---|
| `description` | One line at the start of system message | Low |
| `instructions` | Full instruction text in `<instructions>` block | Medium–High (varies by length) |
| `expected_output` | Description appended to system message | Low–Medium |
| `additional_context` | Free text appended to system message | Variable |
| `markdown=True` | "Use markdown to format your answers" added to `<additional_information>` | Low |
| `add_datetime_to_context` | Current datetime in `<additional_information>` | Low |
| `add_location_to_context` | Location string in `<additional_information>` | Low |
| `add_name_to_context` | Agent name in `<additional_information>` | Low |
| `add_memories_to_context` | Full `<memories_from_previous_interactions>` block + disclaimer note | Medium (scales with memory count) |
| `add_session_summary_to_context` | Full `<summary_of_previous_interactions>` block + disclaimer note | Medium |
| `add_session_state_to_context` | Full `<session_state>` block | Variable (scales with state size) |
| `enable_agentic_memory` | Full `<updating_user_memories>` instructions block (~8 lines) | Medium |
| `enable_agentic_knowledge_filters` | Full filter instructions block (~12 lines with examples) | Medium–High |
| `add_knowledge_to_context` | `<references>` block appended to user message | Variable (scales with results) |
| `add_dependencies_to_context` | `<additional context>` block appended to user message | Variable |
| `additional_input` (few-shot) | Full message pairs (user + assistant) injected into context | High (scales with example count) |
| Each tool (function/Toolkit) | JSON schema tool definition sent with every request | Medium per tool |
| `output_schema` | Schema included in token count | Medium |
| `input_schema` | Validation schema overhead | Low–Medium |

### Dynamic overhead (grows during a run)

| Feature | What it adds to context | Cost |
|---|---|---|
| `add_history_to_context` with `num_history_runs=N` | N runs of messages (user + assistant + tool calls + tool results) | High (accumulates per run) |
| Tool call results | Each tool execution returns results into context | High (the main source of bloat) |
| `search_session_history` with `num_history_sessions=N` | N sessions of history retrieved and injected | Very High |

### Hidden overhead (not obvious to users)

| Feature | Hidden cost | Why it's surprising |
|---|---|---|
| Each Toolkit | A Toolkit like `YFinanceTools` with all features enabled exposes many sub-tools — each is a separate tool definition | Users think "I added one toolkit" but it may add 5–10 tool definitions |
| Agentic memory instructions | Adds ~8 lines of instruction text about the `update_user_memory` tool | Users don't see that enabling agentic memory *also* adds an implicit tool + instructions |
| Agentic knowledge filters | Adds ~12 lines of detailed filtering instructions with examples | Same — implicit instruction overhead |
| Agentic state | Adds an implicit `update_session_state` tool definition | Another hidden tool |
| `search_knowledge` | Adds an implicit `search_knowledge_base` tool definition | Enabled by default when knowledge is set |

---

## Guidance System Design

I'd implement this as three layers: a live context budget meter, inline warnings, and reduction suggestions.

### Layer 1: Context Budget Meter

A persistent sidebar or footer that shows a running estimate of static context overhead. This is inspired by the Agno token counting system, which counts messages, tool definitions, and output schemas together ([/compression/token-counting](https://docs.agno.com/compression/token-counting)).

```
┌─────────────────────────────────────────────┐
│  Context Budget Estimate                      │
│                                               │
│  System message overhead:  ~2,100 tokens     │
│  Tool definitions (7 tools): ~1,800 tokens   │
│  Output schema:              ~300 tokens      │
│  Implicit tools (3):         ~600 tokens     │
│  Few-shot examples (6 msgs): ~1,400 tokens   │
│  ─────────────────────────────────────────── │
│  Static total:               ~7,200 tokens   │
│                                               │
│  Model context window:       128,000 tokens   │
│  Static usage:               5.6%  ████░░░░  │
│                                               │
│  Status: ✓ Healthy                           │
└─────────────────────────────────────────────┘
```

**Status thresholds:**

| Static overhead as % of context window | Status | Colour |
|---|---|---|
| < 10% | ✓ Healthy | Green |
| 10–20% | ⚠ Moderate | Yellow |
| 20–35% | ⚠ High | Orange |
| > 35% | ✗ Risky | Red |

The red zone is where the *static* overhead alone leaves insufficient room for dynamic content (chat history, tool results, user messages). The compression docs show how fast tool results accumulate — 4 tool calls can consume 12,000 tokens on their own ([/compression/overview](https://docs.agno.com/compression/overview)).

### Layer 2: Inline Warnings

Contextual warnings that appear next to specific fields when the user's choices create risk:

#### Warning A: Too many tools

```
┌─ What tools does the agent need? ────────────────────────────┐
│                                                               │
│  Selected: YFinanceTools (all) · DuckDuckGoTools ·            │
│           HackerNewsTools · CalculatorTools ·                 │
│           SlackTools (all) · GmailTools (all)                 │
│                                                               │
│  ⚠ You've selected 6 toolkits exposing ~28 individual tools. │
│                                                               │
│  Each tool adds a JSON schema definition to every request.    │
│  At ~100-200 tokens per tool definition, this alone could     │
│  consume ~2,800-5,600 tokens on every run — before the agent  │
│  has even started working.                                     │
│                                                               │
│  Consider:                                                     │
│  • Use include_tools to select only what you need             │
│    (e.g. GmailTools(include_tools=["get_latest_emails"]))     │
│  • Split into separate specialised agents                     │
│  • Remove tools the agent is unlikely to need                 │
│                                                               │
│  [ Trim tool selection ]  [ Dismiss ]                        │
└─────────────────────────────────────────────────────────────┘
```

The docs support this — the `include_tools`/`exclude_tools` pattern exists specifically because *"this can be very useful to limit the number of tools that are available to an Agent"* ([/tools/selecting-tools](https://docs.agno.com/tools/selecting-tools)).

#### Warning B: History accumulation risk

```
┌─ Conversation memory ─────────────────────────────────────────┐
│                                                                │
│  Number of history runs to include: [ 5 ]                     │
│  Number of history messages to include: [ 10 ]                │
│  Max tool calls from history: [ (unlimited) ▾ ]                │
│                                                                │
│  ⚠ With 5 history runs and no tool call limit, tool results    │
│  from previous runs will accumulate in your context.           │
│  Each run with tool calls can add thousands of tokens.         │
│                                                                │
│  Consider setting max_tool_calls_from_history to keep only     │
│  the most recent tool calls. Your database always stores      │
│  the full history — this only controls what enters context.   │
│                                                                │
│  [ Set max_tool_calls_from_history = 3 ]  [ Dismiss ]         │
└──────────────────────────────────────────────────────────────┘
```

The docs explain this mechanism: *"The `max_tool_calls_from_history` parameter can be used to add only the n most recent tool calls from history to the context. This helps manage context size and reduce token costs."* And: *"Your database always contains the complete history."* ([/context/agent/overview](https://docs.agno.com/context/agent/overview))

#### Warning C: Implicit overhead alert

```
┌─ Knowledge base ───────────────────────────────────────────────┐
│                                                                 │
│  ☑ Enable knowledge base                                        │
│  ☑ Let agent choose its own filters (agentic)                  │
│  ☑ Let agent search knowledge base (search_knowledge)          │
│  ☑ Let agent update knowledge base (update_knowledge)          │
│                                                                 │
│  ℹ Enabling all four adds:                                      │
│  • 2 implicit tool definitions (search_knowledge_base,         │
│    update_knowledge)                                             │
│  • ~12 lines of filter instructions in the system message       │
│  • References block appended to user messages on search         │
│                                                                 │
│  If the agent only needs to search (not update), leave          │
│  "update knowledge base" unchecked to remove one tool           │
│  definition and its associated overhead.                        │
└─────────────────────────────────────────────────────────────────┘
```

#### Warning D: Feature stacking alert

```
┌─ Context sources enabled ──────────────────────────────────────┐
│                                                                  │
│  You have enabled:                                               │
│  ☑ Conversation history (5 runs)                                 │
│  ☑ User memories                                                │
│  ☑ Session summaries                                            │
│  ☑ Session state                                                │
│  ☑ Knowledge references                                          │
│  ☑ Dependencies                                                  │
│  ☑ Few-shot examples (6 messages)                               │
│                                                                  │
│  ⚠ Each of these adds a block to the system message or          │
│  user message on every run. Together they contribute             │
│  ~3,500 tokens of static overhead before the agent even          │
│  processes the current message.                                   │
│                                                                  │
│  Ask: does the agent truly need all of these on every run?      │
│  Some can be made dynamic (callable factories) so they're        │
│  only included when relevant. See: Callable Factories            │
│                                                                  │
│  [ Review context sources ]  [ Dismiss ]                        │
└──────────────────────────────────────────────────────────────────┘
```

The callable factories pattern from the building-agents docs is directly relevant: *"Pass a function instead of a static list for tools or knowledge. The function is called at the start of each run, so the toolset or knowledge base can vary per user or session."* ([/agents/building-agents](https://docs.agno.com/agents/building-agents))

#### Warning E: Tool call loop risk

```
┌─ Tool call limit ───────────────────────────────────────────────┐
│                                                                  │
│  Tool call limit: [ (unlimited) ▾ ]                              │
│                                                                  │
│  ⚠ No limit means the agent can make unlimited tool calls in a  │
│  single run. This can lead to loops, high costs, and long       │
│  response times.                                                 │
│                                                                  │
│  The docs recommend setting a limit "to prevent loops and have  │
│  better control over costs and performance."                     │
│                                                                  │
│  Suggested: 3-5 for most agents, 1-2 for single-action agents   │
│  [ Set limit = 5 ]  [ Dismiss ]                                 │
└──────────────────────────────────────────────────────────────────┘
```

The tool-call-limit docs: *"Limiting the number of tool calls an Agent can make is useful to prevent loops and have better control over costs and performance."* ([/tools/tool-call-limit](https://docs.agno.com/tools/tool-call-limit))

### Layer 3: Reduction Suggestions

A dedicated panel or "optimise" button that scans the current configuration and suggests specific reductions:

```
┌─ Optimization Suggestions ─────────────────────────────────────┐
│                                                                  │
│  Based on your current configuration, here are ways to reduce   │
│  context overhead:                                               │
│                                                                  │
│  1. ENABLE CONTEXT COMPRESSION                                    │
│     Your agent uses tools that can return verbose results.       │
│     Enabling compress_tool_results will summarise tool          │
│     results after a threshold, dramatically reducing token       │
│     costs while preserving key facts.                            │
│                                                                  │
│     Est. savings: ~60-80% of tool result tokens                   │
│     [ Enable compression ]                                        │
│                                                                  │
│  2. TRIM TOOLKIT SELECTIONS                                       │
│     YFinanceTools has all features enabled but you only          │
│     selected a finance use case template. Consider:              │
│     YFinanceTools(include_tools=["get_stock_price",              │
│                                 "get_company_info"])             │
│                                                                  │
│     Est. savings: ~4 tool definitions removed                     │
│     [ Apply suggestion ]                                          │
│                                                                  │
│  3. REDUCE HISTORY DEPTH                                          │
│     You have num_history_runs=5 but your use case                │
│     (data extraction) typically completes in 1-2 runs.           │
│     Reducing to 2 runs would save ~3,000 tokens per run.        │
│                                                                  │
│     Est. savings: ~3,000 tokens                                    │
│     [ Apply suggestion ]                                          │
│                                                                  │
│  4. USE A CHEAPER COMPRESSION MODEL                               │
│     If you enable compression, use a smaller model               │
│     (e.g. gpt-4o-mini) for the CompressionManager to             │
│     reduce latency and cost.                                      │
│                                                                  │
│     [ Configure ]                                                 │
│                                                                  │
│  5. MAKE TOOLS CONDITIONAL                                        │
│     Instead of always loading all tools, use a callable          │
│     factory that returns different toolsets based on             │
│     session state. This means the agent only sees the            │
│     tools relevant to the current task.                          │
│                                                                  │
│     [ Show pattern ]                                              │
└──────────────────────────────────────────────────────────────────┘
```

The compression suggestion is backed by the docs: *"Benefits: Dramatically reduced token costs, Stay within context window limits, Preserve critical facts and data, Automatic compression"* ([/compression/overview](https://docs.agno.com/compression/overview)). And the cheaper-model suggestion: *"Use a faster, cheaper model like gpt-4o-mini for compression to reduce latency and cost while using a more capable model as your Agent's main model."* ([/compression/overview](https://docs.agno.com/compression/overview))

---

## Built-In Context Budget Reference

Here's the data the form would use to estimate static overhead. These are rough ranges based on the docs' system message examples and token counting documentation:

| Context source | Estimated token cost | Present when | Scales with |
|---|---|---|---|
| `description` | 20–100 | Always set | Text length |
| `instructions` | 100–500 | Always set | Number + length of instructions |
| `expected_output` | 30–100 | When set | Text length |
| `additional_context` | 50–500 | When set | Text length |
| `markdown=True` | ~15 | When set | Fixed |
| `add_datetime_to_context` | ~20 | When set | Fixed |
| `add_location_to_context` | ~20 | When set | Fixed |
| `add_name_to_context` | ~10 | When set | Fixed |
| `add_memories_to_context` | 200–800 | When set | Number of memories |
| `add_session_summary_to_context` | 100–400 | When set | Summary length |
| `add_session_state_to_context` | 50–500 | When set | State dict size |
| `enable_agentic_memory` | ~200 | When set | Fixed (instruction block) |
| `enable_agentic_knowledge_filters` | ~300 | When set | Fixed (instruction block) |
| `add_knowledge_to_context` | 200–2,000 | When set | Number of references returned |
| `add_dependencies_to_context` | 50–500 | When set | Dependencies dict size |
| `additional_input` (few-shot) | 200–2,000+ | When set | Number + length of examples |
| Each tool definition | 100–200 | Per tool | Parameter schema complexity |
| `output_schema` | 100–400 | When set | Schema complexity |
| `input_schema` | 50–200 | When set | Schema complexity |
| Chat history (per run) | 500–3,000+ | When `add_history_to_context` | Messages + tool calls in run |
| Tool call results (per call) | 500–3,500 | Per tool execution | Result verbosity |

These are estimates — the token counting docs note: *"Token counts are estimates. Provider billing and exact tokenization can differ."* ([/compression/token-counting](https://docs.agno.com/compression/token-counting))

---

## Agno's Built-In Mitigations (Map to Form Suggestions)

The form should surface these Agno-native mechanisms when the user's config is heavy:

| Problem | Agno mechanism | Form suggestion |
|---|---|---|
| Too many tools in a Toolkit | `include_tools` / `exclude_tools` on Toolkits ([/tools/selecting-tools](https://docs.agno.com/tools/selecting-tools)) | "Trim to only the tools you need" |
| Tool results bloating context | `compress_tool_results=True` or `CompressionManager` ([/compression/overview](https://docs.agno.com/compression/overview)) | "Enable context compression" |
| Verbose compression cost | Use cheaper model in `CompressionManager` ([/compression/overview](https://docs.agno.com/compression/overview)) | "Use gpt-4o-mini for compression" |
| History too deep | `num_history_runs` reduction ([/context/agent/overview](https://docs.agno.com/context/agent/overview)) | "Reduce history depth" |
| Tool calls in history bloating context | `max_tool_calls_from_history=N` ([/context/agent/overview](https://docs.agno.com/context/agent/overview)) | "Limit tool calls from history" |
| Agent making too many calls | `tool_call_limit=N` ([/tools/tool-call-limit](https://docs.agno.com/tools/tool-call-limit)) | "Set a tool call limit" |
| Tools always present but rarely needed | Callable factory for `tools` ([/agents/building-agents](https://docs.agno.com/agents/building-agents)) | "Make tools conditional" |
| Knowledge always present but rarely needed | Callable factory for `knowledge` ([/agents/building-agents](https://docs.agno.com/agents/building-agents)) | "Make knowledge conditional" |
| Too many context sources | Remove `add_*_to_context` flags | "Review which context sources are needed on every run" |

---

## Design Principles for the Guidance

These map directly to the context engineering principles you've studied:

1. **Minimum sufficient context** — the budget meter shows what's being spent; warnings fire when it's excessive
2. **Progressive disclosure** — the form itself starts minimal; guidance appears only when triggered
3. **Hard enforcement over soft instruction** — `tool_call_limit` and `max_tool_calls_from_history` are hard limits, not suggestions — the form should present them as first-class controls, not advanced settings
4. **Cost awareness** — show token estimates so users can make informed tradeoffs, not just vague "this might be a lot" warnings
5. **Actionable, not just informational** — every warning should have a one-click fix that applies a specific Agno mechanism

---

**Sources used:**

- [https://docs.agno.com/context/agent/overview](https://docs.agno.com/context/agent/overview) — system message construction, all context sources, `max_tool_calls_from_history`
- [https://docs.agno.com/context/overview](https://docs.agno.com/context/overview) — context engineering principles
- [https://docs.agno.com/compression/overview](https://docs.agno.com/compression/overview) — tool result bloat, compression mechanism, cheaper model suggestion
- [https://docs.agno.com/compression/token-counting](https://docs.agno.com/compression/token-counting) — what counts toward token total (tools, schemas, messages, multimodal)
- [https://docs.agno.com/tools/tool-call-limit](https://docs.agno.com/tools/tool-call-limit) — preventing loops, controlling costs
- [https://docs.agno.com/tools/selecting-tools](https://docs.agno.com/tools/selecting-tools) — `include_tools` / `exclude_tools` for toolkit trimming
- [https://docs.agno.com/agents/building-agents](https://docs.agno.com/agents/building-agents) — callable factories for conditional tools/knowledge
- [https://docs.agno.com/tools/overview](https://docs.agno.com/tools/overview) — 120+ toolkits, how tools work
- [https://docs.agno.com/agents/overview](https://docs.agno.com/agents/overview) — agent definition
