# Frontend Chat Setup — AstroJS + Prompt-Kit → Agno API

> **Audience:** Frontend dev team.
> **Scope:** Phase 1 — standard chat surface against the Mind Partner agent.

A chat UI built with AstroJS (React islands), Prompt-Kit (shadcn/ui components), and a custom `useChat` hook that talks to the Agno AgentOS FastAPI backend via `fetch()` + Server-Sent Events.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│  AstroJS Frontend                                │
│  ┌───────────────────────────────────────────┐  │
│  │  React Island (client:load)               │  │
│  │  ┌─────────────┐  ┌──────────────────┐    │  │
│  │  │ useChat()   │→ │ Prompt-Kit       │    │  │
│  │  │ custom hook │  │ components        │    │  │
│  │  │ (useState +  │  │ (PromptInput,    │    │  │
│  │  │  fetch)     │  │  Message, etc.)  │    │  │
│  │  └─────────────┘  └──────────────────┘    │  │
│  └───────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────┘
                        │ fetch POST (form-encoded)
                        ▼
┌─────────────────────────────────────────────────┐
│  Agno AgentOS FastAPI                            │
│  POST /agents/{agent_id}/runs   (agent run)     │
│  GET  /sessions/{session_id}    (history)       │
│  GET  /sessions/{session_id}/runs (run list)    │
│  SSE streaming via typed events                 │
└─────────────────────────────────────────────────┘
```

---

## 1. API Contract

### Base URL

```
http://localhost:8000
```

Routes are mounted at the root — there is no `/v1` prefix.

### Core endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/agents` | GET | List registered agents |
| `/agents/{agent_id}` | GET | Get agent details |
| `/agents/{agent_id}/runs` | POST | **Execute an agent** (send message) |
| `/agents/{agent_id}/runs/{run_id}` | GET | Get a specific run's result |
| `/agents/{agent_id}/runs/{run_id}/cancel` | POST | Cancel a running run |
| `/agents/{agent_id}/runs/{run_id}/resume` | POST | Resume a disconnected SSE stream |
| `/sessions` | GET | List sessions (paginated, filterable) |
| `/sessions/{session_id}` | GET | Get session details + message history |
| `/sessions/{session_id}/runs` | GET | List runs in a session |
| `/sessions/{session_id}/runs/{run_id}` | GET | Get a run within a session |
| `/sessions/{session_id}` | DELETE | Delete a session |

### The primary call: `POST /agents/{agent_id}/runs`

This is the critical endpoint for chat. The `agent_id` is a **path parameter**, not a body field.

#### Request — form-encoded

The endpoint accepts `application/x-www-form-urlencoded` (or `multipart/form-data` when uploading files). Use `URLSearchParams`:

```typescript
const params = new URLSearchParams();
params.set("message", text);
params.set("stream", "true");
if (sessionId) params.set("session_id", sessionId);
if (userId) params.set("user_id", userId);

const res = await fetch(`${API_BASE}/agents/${agentId}/runs`, {
  method: "POST",
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: params,
});
```

**Form parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `message` | string | required | The input message or prompt |
| `stream` | bool | `true` | Enable SSE streaming (on by default) |
| `session_id` | string? | `null` | Session ID for conversation continuity. If omitted, a new session is created |
| `user_id` | string? | `null` | User identifier for personalization and cross-session memory |
| `files` | file[]? | `null` | Files to upload (images, audio, video, documents) |
| `background` | bool | `false` | Run in background, return immediately with run metadata |
| `version` | string? | `null` | Agent version to use |

> **Streaming is the default.** If you omit `stream`, you get SSE. Set `stream=false` explicitly for a single JSON response.

#### Response — streaming (SSE, default)

When `stream=true`, the response is `text/event-stream` with **typed events**. Each event is two lines separated by a blank line:

```
event: <EventName>
data: <JSON payload>

```

**Event types:**

| Event | When | Key fields | Use for chat |
|---|---|---|---|
| `RunStarted` | Run begins | `run_id`, `session_id`, `model`, `model_provider` | **Capture `session_id` + `run_id`** |
| `RunContent` | Each content delta | `content` (the delta), `content_type`, `reasoning_content`, `citations` | **Append `content` to message** |
| `RunContentCompleted` | Content stream finished | — | Mark streaming done |
| `ToolCallStarted` | Tool invoked | `tool` (ToolExecution) | Render tool badge (optional) |
| `ToolCallCompleted` | Tool finished | `tool`, `content`, `images`, `files` | Update tool badge (optional) |
| `ToolCallError` | Tool failed | `tool`, `error` | Render error (optional) |
| `ReasoningStepStarted` / `ReasoningStepCompleted` | Reasoning model steps | `reasoning_content` | Render reasoning (optional) |
| `RunCompleted` | Run finished | `content` (**final authoritative**), `content_type`, `citations`, `tools`, `images`, `files`, `status` | **Replace accumulated deltas with this `content`** |
| `RunError` | Run failed | `error` | Show error |

**Parsing rules:**

1. **Parse the `event:` line** to know the payload type. Each event type has a different payload shape — don't treat every `data:` line as content.
2. **Append `content` from `RunContent` events only** — these are deltas.
3. **On `RunCompleted`, replace** the accumulated message with `event.content` — this is the final, authoritative content (deltas may not concatenate perfectly).
4. **Capture `session_id` and `run_id` from `RunStarted`** — without `session_id`, every message starts a new session and history is lost.

#### Response — non-streaming (JSON)

When `stream=false`, the response is a JSON object with these key fields:

```json
{
  "run_id": "uuid",
  "agent_id": "thinking-partner",
  "session_id": "uuid",
  "content": "The assistant's reply text",
  "content_type": "str",
  "status": "completed",
  "messages": [...],
  "tools": [...],
  "metrics": {...},
  "citations": {...},
  "reasoning_content": null,
  "images": null,
  "files": null,
  "created_at": 1735689600
}
```

Use `content` for the reply. Capture `session_id` and `run_id` for continuity.

---

## 2. Dependencies

### 2.1 Astro + React + Tailwind

```bash
npm create astro@latest -- --template minimal --typescript strict
npx astro add react
npx astro add tailwind
```

### 2.2 shadcn/ui (required by Prompt-Kit)

Prompt-Kit is a collection of shadcn/ui-compatible components installed via the **shadcn CLI**. shadcn/ui must be configured first.

Follow the shadcn/ui installation guide for Astro: <https://ui.shadcn.com/docs/installation>

This sets up:

- `components.json`
- `@/components/ui/` alias
- `@/lib/utils.ts` (the `cn` helper)
- Tailwind config with shadcn theme tokens

### 2.3 Prompt-Kit components

Install individual components via the shadcn CLI:

```bash
npx shadcn@latest add "https://prompt-kit.com/c/prompt-input.json"
npx shadcn@latest add "https://prompt-kit.com/c/message.json"
npx shadcn@latest add "https://prompt-kit.com/c/chat-container.json"
npx shadcn@latest add "https://prompt-kit.com/c/markdown.json"
npx shadcn@latest add "https://prompt-kit.com/c/reasoning.json"
npx shadcn@latest add "https://prompt-kit.com/c/tool.json"
```

Components land in `src/components/ui/` and are imported as:

```typescript
import { PromptInput } from "@/components/ui/prompt-input";
import { Message } from "@/components/ui/message";
```

Available components: `PromptInput`, `Message`, `ChatContainer`, `Markdown`, `Reasoning`, `Tool`, `Source`, `CodeBlock`, `Loader`, `ScrollButton`, `PromptSuggestion`, `Steps`, `FileUpload`, `Image`, `FeedbackBar`, `TextShimmer`, `ThinkingBar`. Full docs: <https://www.prompt-kit.com/docs/introduction>

### 2.4 Prerequisites

- **Node.js 18+**
- **React 19+** (Prompt-Kit requires it)

---

## 3. Project Structure

```
src/
├── pages/
│   └── index.astro              ← page shell, loads the chat island
├── components/
│   ├── ChatIsland.tsx          ← React island (client:load)
│   └── ui/                      ← shadcn/prompt-kit components land here
│       ├── prompt-input.tsx
│       ├── message.tsx
│       └── ...
├── lib/
│   ├── useChat.ts               ← custom hook: message state + fetch + SSE
│   ├── api.ts                   ← Agno API client (form-encoded, SSE parser)
│   ├── types.ts                 ← message types, event types, session types
│   └── utils.ts                 ← cn() helper (shadcn)
├── styles/
│   └── global.css               ← Tailwind imports + shadcn theme
└── env.d.ts
```

---

## 4. Types

```typescript
// src/lib/types.ts

export type Message = {
  id: string;
  role: "user" | "assistant";
  content: string;
  createdAt: string;
  runId?: string;
  toolCalls?: ToolCall[];
};

export type ToolCall = {
  toolName: string;
  status: "running" | "completed" | "error";
  content?: string;
};

// SSE event types — mirror the Agno RunEvent enum
export type SSEEventType =
  | "RunStarted"
  | "RunContent"
  | "RunContentCompleted"
  | "ToolCallStarted"
  | "ToolCallCompleted"
  | "ToolCallError"
  | "RunCompleted"
  | "RunError";

export type SSEEvent = {
  event: SSEEventType | string;
  data: Record<string, any>;
};

export type UseChatOptions = {
  agentId: string;
  apiUrl?: string;        // defaults to http://localhost:8000
  sessionId?: string;
  userId?: string;        // stable anonymous id for personalization
};
```

---

## 5. API Client

```typescript
// src/lib/api.ts

const DEFAULT_API = "http://localhost:8000";

/**
 * Send a message to an agent and parse the SSE stream.
 * Returns the final content from RunCompleted (or accumulated deltas as fallback).
 */
export async function sendMessage(
  agentId: string,
  message: string,
  opts: {
    sessionId?: string;
    userId?: string;
    apiUrl?: string;
    stream?: boolean;
    onEvent?: (event: string, data: Record<string, any>) => void;
  } = {}
): Promise<{ content: string; sessionId?: string; runId?: string }> {
  const {
    sessionId,
    userId,
    apiUrl = DEFAULT_API,
    stream = true,
    onEvent,
  } = opts;

  const params = new URLSearchParams();
  params.set("message", message);
  params.set("stream", stream ? "true" : "false");
  if (sessionId) params.set("session_id", sessionId);
  if (userId) params.set("user_id", userId);

  const res = await fetch(`${apiUrl}/agents/${agentId}/runs`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params,
  });

  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`API error ${res.status}: ${text}`);
  }

  // Non-streaming: parse JSON RunOutput
  if (!stream || !res.body) {
    const data = await res.json();
    return {
      content: data.content ?? "",
      sessionId: data.session_id,
      runId: data.run_id,
    };
  }

  // Streaming: parse typed SSE events
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let accumulated = "";
  let finalContent = "";
  let capturedSessionId: string | undefined;
  let capturedRunId: string | undefined;
  let currentEvent = "message";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });

    // SSE events are separated by \n\n
    const events = buffer.split("\n\n");
    buffer = events.pop() ?? "";

    for (const rawEvent of events) {
      const lines = rawEvent.split("\n");
      let eventData = "";

      for (const line of lines) {
        if (line.startsWith("event: ")) {
          currentEvent = line.slice(7).trim();
        } else if (line.startsWith("data: ")) {
          eventData = line.slice(6);
        }
      }

      if (!eventData) continue;

      let parsed: Record<string, any>;
      try {
        parsed = JSON.parse(eventData);
      } catch {
        continue; // skip malformed
      }

      // Dispatch to handler
      onEvent?.(currentEvent, parsed);

      // Handle by event type
      switch (currentEvent) {
        case "RunStarted":
          capturedSessionId = parsed.session_id;
          capturedRunId = parsed.run_id;
          break;
        case "RunContent":
          if (typeof parsed.content === "string") {
            accumulated += parsed.content;
          }
          break;
        case "RunCompleted":
          // Final content is authoritative — replace accumulated deltas
          finalContent =
            typeof parsed.content === "string" ? parsed.content : accumulated;
          capturedSessionId = capturedSessionId ?? parsed.session_id;
          capturedRunId = capturedRunId ?? parsed.run_id;
          break;
        case "RunError":
          throw new Error(parsed.error ?? "Run failed");
      }
    }
  }

  return {
    content: finalContent || accumulated,
    sessionId: capturedSessionId,
    runId: capturedRunId,
  };
}

/** Fetch session history (message list). */
export async function getSession(
  sessionId: string,
  apiUrl: string = DEFAULT_API
): Promise<any> {
  const res = await fetch(`${apiUrl}/sessions/${sessionId}`);
  if (!res.ok) throw new Error(`API error ${res.status}`);
  return res.json();
}

/** List runs in a session. */
export async function getSessionRuns(
  sessionId: string,
  apiUrl: string = DEFAULT_API
): Promise<any> {
  const res = await fetch(`${apiUrl}/sessions/${sessionId}/runs`);
  if (!res.ok) throw new Error(`API error ${res.status}`);
  return res.json();
}

/** Cancel a running run. */
export async function cancelRun(
  agentId: string,
  runId: string,
  sessionId: string,
  apiUrl: string = DEFAULT_API
): Promise<void> {
  const params = new URLSearchParams();
  params.set("session_id", sessionId);
  const res = await fetch(
    `${apiUrl}/agents/${agentId}/runs/${runId}/cancel`,
    { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: params }
  );
  if (!res.ok) throw new Error(`API error ${res.status}`);
}
```

---

## 6. The `useChat` Hook

```typescript
// src/lib/useChat.ts
import { useState, useCallback, useRef } from "react";
import { sendMessage, cancelRun } from "./api";
import type { Message } from "./types";

const ANON_USER_KEY = "agentos-anon-user-id";

function getOrCreateUserId(): string {
  if (typeof window === "undefined") return "anonymous";
  const existing = localStorage.getItem(ANON_USER_KEY);
  if (existing) return existing;
  const id = crypto.randomUUID();
  localStorage.setItem(ANON_USER_KEY, id);
  return id;
}

export function useChat({
  agentId,
  apiUrl,
  sessionId,
  userId,
}: {
  agentId: string;
  apiUrl?: string;
  sessionId?: string;
  userId?: string;
}) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const sessionRef = useRef<string | undefined>(sessionId);
  const runIdRef = useRef<string | undefined>(undefined);
  const userIdRef = useRef<string>(userId ?? getOrCreateUserId());

  const send = useCallback(
    async (text: string) => {
      if (!text.trim() || isLoading) return;

      const userMsg: Message = {
        id: crypto.randomUUID(),
        role: "user",
        content: text,
        createdAt: new Date().toISOString(),
      };

      const assistantMsg: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: "",
        createdAt: new Date().toISOString(),
      };

      setMessages((prev) => [...prev, userMsg, assistantMsg]);
      setIsLoading(true);
      setError(null);

      try {
        const result = await sendMessage(agentId, text, {
          sessionId: sessionRef.current,
          userId: userIdRef.current,
          apiUrl,
          stream: true,
          onEvent: (event, data) => {
            switch (event) {
              case "RunStarted":
                if (data.session_id) sessionRef.current = data.session_id;
                if (data.run_id) runIdRef.current = data.run_id;
                break;
              case "RunContent":
                // Append delta to assistant message
                if (typeof data.content === "string") {
                  setMessages((prev) =>
                    prev.map((m) =>
                      m.id === assistantMsg.id
                        ? { ...m, content: m.content + data.content }
                        : m
                    )
                  );
                }
                break;
              case "RunCompleted":
                // Replace with final authoritative content
                if (typeof data.content === "string") {
                  setMessages((prev) =>
                    prev.map((m) =>
                      m.id === assistantMsg.id
                        ? { ...m, content: data.content }
                        : m
                    )
                  );
                }
                break;
              // ToolCallStarted / ToolCallCompleted can be handled here
              // for Phase 1.5 tool-call rendering.
            }
          },
        });

        // Final sync in case RunCompleted wasn't emitted
        setMessages((prev) =>
          prev.map((m) =>
            m.id === assistantMsg.id
              ? {
                  ...m,
                  content: result.content || m.content,
                  runId: result.runId,
                }
              : m
          )
        );

        // Persist session id for continuity
        if (result.sessionId) sessionRef.current = result.sessionId;
        if (result.runId) runIdRef.current = result.runId;
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
        // Remove the empty assistant message on failure
        setMessages((prev) => prev.filter((m) => m.id !== assistantMsg.id));
      } finally {
        setIsLoading(false);
      }
    },
    [agentId, apiUrl, isLoading]
  );

  const stop = useCallback(async () => {
    if (runIdRef.current && sessionRef.current) {
      try {
        await cancelRun(agentId, runIdRef.current, sessionRef.current, apiUrl);
      } catch {
        // ignore — run may already be done
      }
    }
    setIsLoading(false);
  }, [agentId, apiUrl]);

  return { messages, send, stop, isLoading, error, sessionId: sessionRef.current };
}
```

---

## 7. The Chat Island Component

```tsx
// src/components/ChatIsland.tsx
import { useChat } from "../lib/useChat";
import { PromptInput } from "@/components/ui/prompt-input";
import { Message } from "@/components/ui/message";
// ChatContainer, Markdown, Reasoning, Tool components as needed

export default function ChatIsland() {
  const { messages, send, stop, isLoading, error } = useChat({
    agentId: "thinking-partner",
    apiUrl: "http://localhost:8000",
  });

  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto">
      <header className="p-4 border-b">
        <h1 className="text-lg font-semibold">Mind Partner</h1>
      </header>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((m) => (
          <Message
            key={m.id}
            from={m.role === "user" ? "user" : "assistant"}
          >
            {m.content}
          </Message>
        ))}
        {isLoading && (
          <div className="text-sm text-muted-foreground">Thinking…</div>
        )}
        {error && (
          <div className="text-red-500 text-sm">{error}</div>
        )}
      </div>

      <div className="p-4 border-t">
        <PromptInput
          onSubmit={send}
          disabled={isLoading}
          placeholder="Ask Mind Partner…"
        />
        {isLoading && (
          <button onClick={stop} className="text-sm text-muted-foreground mt-2">
            Stop
          </button>
        )}
      </div>
    </div>
  );
}
```

> **Verify Prompt-Kit component props.** The exact prop names (`from`, `onSubmit`, etc.) depend on the shadcn-generated component. Check `src/components/ui/message.tsx` and `src/components/ui/prompt-input.tsx` after installation and adapt. Prompt-Kit docs: <https://www.prompt-kit.com/docs/introduction>

---

## 8. The Astro Page

```astro
---
// src/pages/index.astro
import ChatIsland from "../components/ChatIsland.tsx";
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Mind Partner</title>
  </head>
  <body class="bg-gray-50 min-h-screen">
    <ChatIsland client:load />
  </body>
</html>
```

---

## 9. Authentication

In local dev, JWT auth is **off** — no token needed. The backend team handles the dev/prod environment switch.

In production, every endpoint requires a JWT bearer token. When targeting production, add the auth header to all fetch calls:

```typescript
const headers: Record<string, string> = {
  "Content-Type": "application/x-www-form-urlencoded",
};
if (jwtToken) {
  headers["Authorization"] = `Bearer ${jwtToken}`;
}
```

**Phase 1 scope:** local-dev only (no auth). Token acquisition for production is a Phase 2+ concern.

---

## 10. Step-by-Step Setup Sequence

| Step | Action | Done when |
|---|---|---|
| **1** | `npm create astro@latest` → minimal + TypeScript | Astro dev server runs on `localhost:4321` |
| **2** | `npx astro add react` + `npx astro add tailwind` | React island renders, Tailwind classes work |
| **3** | Configure shadcn/ui (follow <https://ui.shadcn.com/docs/installation>) | `components.json` exists, `@/components/ui/` alias works |
| **4** | Install Prompt-Kit components via `npx shadcn@latest add "https://prompt-kit.com/c/..."` | Components exist in `src/components/ui/` |
| **5** | Test Agno API with curl (see §11) | You get a response, know the JSON/SSE shape |
| **6** | Write `types.ts` + `api.ts` | API client works standalone (test with a simple script) |
| **7** | Write `useChat.ts` hook | Can call `send()` and see messages stream in |
| **8** | Write `ChatIsland.tsx` with Prompt-Kit components | Chat UI renders, messages display |
| **9** | Wire up `index.astro` | Full page loads, chat works end-to-end |
| **10** | Verify session continuity: send 2 messages, confirm same `session_id` | Second message has context from the first |

---

## 11. Verification Commands (run before writing frontend code)

Run these against the running backend to confirm the API contract and see the real response shapes.

### 11.1 Confirm the agent is registered

```bash
curl http://localhost:8000/agents | jq '.[] | {id, name}'
# Expect: {"id": "thinking-partner", "name": "Mind Partner"} in the list
```

### 11.2 Test non-streaming run

```bash
curl -X POST http://localhost:8000/agents/thinking-partner/runs \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "message=Hello&stream=false" | jq '{content, session_id, run_id, status}'
```

### 11.3 Test streaming run

```bash
curl -N -X POST http://localhost:8000/agents/thinking-partner/runs \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "message=Hello&stream=true"
# You should see:
# event: RunStarted
# data: {"run_id":"...","session_id":"...","content":""}
#
# event: RunContent
# data: {"content":"Hi","content_type":"str",...}
#
# event: RunCompleted
# data: {"content":"full reply","content_type":"str",...}
```

### 11.4 Test session continuity

```bash
# First message — capture session_id from the response
SESSION=$(curl -s -X POST http://localhost:8000/agents/thinking-partner/runs \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "message=My name is Pete&stream=false" | jq -r .session_id)

# Second message — reuse session_id
curl -X POST http://localhost:8000/agents/thinking-partner/runs \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "message=What is my name?&stream=false&session_id=$SESSION" | jq .content
# Expect: the agent knows your name is Pete
```

---

## 12. Phase 1.5 Opportunities (cheap wins)

### 12.1 Tool-call rendering

The SSE stream emits `ToolCallStarted` and `ToolCallCompleted` events with structured `tool` data. Render these as collapsible "Used tool X" badges in the `onEvent` handler. No extra API calls needed.

### 12.2 Stop / regenerate

`runId` is captured from `RunStarted`. Wire the `stop` function (already in `useChat`) to `POST /agents/{agent_id}/runs/{run_id}/cancel`. For regenerate, cancel the current run and re-send the last user message.

### 12.3 Reasoning display

If the model emits reasoning (`ReasoningStepStarted`/`ReasoningStepCompleted` events with `reasoning_content`), render in a collapsible "Thinking" section using Prompt-Kit's `Reasoning` component.

### 12.4 Citations

`RunCompleted` may include `citations`. Render with Prompt-Kit's `Source` component.

---

## 13. Best Practices

1. **Always use `URLSearchParams` + `application/x-www-form-urlencoded`** for the request body. The endpoint expects form data.
2. **Parse SSE by event type** — read the `event:` line to know what payload follows. Each event type has a different shape.
3. **Capture `session_id` from `RunStarted`** (streaming) or the top-level `session_id` field (non-streaming) and reuse it for all subsequent messages. Without it, every message starts a new session and history is lost.
4. **Replace accumulated deltas with `RunCompleted.content`** when it arrives — it's the final, authoritative content.
5. **Confirm the agent is registered** with `curl http://localhost:8000/agents` before hardcoding the `agentId`.
6. **Install Prompt-Kit via the shadcn CLI** (`npx shadcn@latest add "https://prompt-kit.com/c/..."`), not npm.
7. **Generate a stable anonymous `user_id`** (localStorage UUID) so the agent's cross-session memory and personalization work across visits.