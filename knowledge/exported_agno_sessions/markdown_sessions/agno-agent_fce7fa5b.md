# Agno Agent

| Field | Value |
|-------|-------|
| **Session** | `fce7fa5b...` |
| **Type** | agent |
| **Agent** | Agno Agent |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-02T13:17:02 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agno Agent ✓ COMPLETED

*2026-05-02T13:17:02* · `glm-5.1:cloud` · `b5518e84...`

### Prompt

I have created a front end typescript web application that can consume the AgentOS api of my backend Agno server.

How can I bring a chat UI to the front end app that streams with the backend so a user can communicate with an agent?

### Response

Great question! You have **two main paths** to bring a streaming chat UI to your frontend TypeScript app that talks to your Agno AgentOS backend:

---

## Option 1: Use AgentUI (Fastest — Agno's Open-Source Chat UI)

Agno provides a fully open-source, TypeScript/Next.js chat UI called **AgentUI** that streams directly with AgentOS. This is the quickest way to get a working chat interface.

```bash
npx create-agent-ui@latest
```

Then connect it to your running AgentOS server by entering your AgentOS endpoint (e.g., `http://localhost:7777`) in the sidebar.

AgentUI gives you:
- Streaming chat with your agents
- Session management (create, list, resume)
- Memory and knowledge inspection
- Team and workflow support

You can either use it as-is, or clone and customize it to match your app's design:

```bash
git clone https://github.com/agno-agi/agent-ui.git
cd agent-ui && pnpm install && pnpm dev
```

---

## Option 2: Custom Integration via AgentOS REST API (Full Control)

If you want the chat UI embedded in your own app with full control over styling and behavior, call the AgentOS API directly.

### The Streaming Endpoint

The core endpoint is:

```
POST /agents/{agent_id}/runs
```

With `stream=true`, it returns **Server-Sent Events (SSE)** — real-time streaming responses.

#### Example curl:

```bash
curl http://localhost:7777/agents/my-agent/runs \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "message=Tell me about Agno" \
  -d "stream=true" \
  -d "user_id=john@example.com" \
  -d "session_id=session_123"
```

### TypeScript/Frontend Streaming Implementation

Here's how to consume the SSE stream from your frontend:

```typescript
// chat-stream.ts
export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface StreamEvent {
  event: string;
  data: string;
}

const AGENT_OS_BASE = "http://localhost:7777"; // Your AgentOS server

export async function streamAgentMessage(
  agentId: string,
  message: string,
  onChunk: (chunk: string) => void,
  onDone: () => void,
  onError: (error: Error) => void,
  options?: {
    sessionId?: string;
    userId?: string;
  }
) {
  const params = new URLSearchParams();
  params.append("message", message);
  params.append("stream", "true");
  if (options?.userId) params.append("user_id", options.userId);
  if (options?.sessionId) params.append("session_id", options.sessionId);

  const response = await fetch(
    `${AGENT_OS_BASE}/agents/${agentId}/runs`,
    {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: params.toString(),
    }
  );

  if (!response.ok) {
    onError(new Error(`HTTP ${response.status}: ${response.statusText}`));
    return;
  }

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  if (!reader) {
    onError(new Error("No readable stream"));
    return;
  }

  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      onDone();
      break;
    }

    buffer += decoder.decode(value, { stream: true });

    // Parse SSE events (newline-delimited JSON)
    const lines = buffer.split("\n");
    buffer = lines.pop() || ""; // Keep incomplete line in buffer

    for (const line of lines) {
      if (line.startsWith("data: ")) {
        try {
          const eventData = JSON.parse(line.slice(6));

          // Handle different event types
          if (eventData.content) {
            onChunk(eventData.content);
          }
        } catch {
          // Not JSON — might be a plain text chunk
          onChunk(line.slice(6));
        }
      } else if (line.startsWith("event: ")) {
        // Event type line (e.g., "event: RunCompleted")
        // You can use this to detect completion
      }
    }
  }
}
```

### React Chat Component Example

```tsx
import { useState, useRef, useCallback } from "react";
import { streamAgentMessage, ChatMessage } from "./chat-stream";

interface ChatProps {
  agentId: string;
  userId?: string;
}

export function AgentChat({ agentId, userId }: ChatProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [isStreaming, setIsStreaming] = useState(false);
  const [sessionId, setSessionId] = useState<string | undefined>();
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const handleSend = useCallback(async () => {
    if (!input.trim() || isStreaming) return;

    const userMessage = input.trim();
    setInput("");
    setMessages((prev) => [...prev, { role: "user", content: userMessage }]);
    setIsStreaming(true);

    let assistantContent = "";

    setMessages((prev) => [
      ...prev,
      { role: "assistant", content: "" },
    ]);

    await streamAgentMessage(
      agentId,
      userMessage,
      // onChunk — append to assistant message
      (chunk: string) => {
        assistantContent += chunk;
        setMessages((prev) => {
          const updated = [...prev];
          updated[updated.length - 1] = {
            role: "assistant",
            content: assistantContent,
          };
          return updated;
        });
      },
      // onDone
      () => setIsStreaming(false),
      // onError
      (error: Error) => {
        console.error("Stream error:", error);
        setIsStreaming(false);
      },
      { sessionId, userId }
    );
  }, [input, isStreaming, agentId, sessionId, userId]);

  return (
    <div className="flex flex-col h-full">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={msg.role === "user" ? "text-right" : "text-left"}
          >
            <div
              className={`inline-block max-w-[80%] rounded-lg px-4 py-2 ${
                msg.role === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-100 text-gray-900"
              }`}
            >
              <div className="whitespace-pre-wrap">{msg.content}</div>
              {msg.role === "assistant" && !msg.content && isStreaming && (
                <span className="animate-pulse">▊</span>
              )}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="border-t p-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Type a message..."
            className="flex-1 rounded-lg border px-4 py-2"
            disabled={isStreaming}
          />
          <button
            onClick={handleSend}
            disabled={isStreaming || !input.trim()}
            className="rounded-lg bg-blue-600 px-4 py-2 text-white disabled:opacity-50"
          >
            {isStreaming ? "..." : "Send"}
          </button>
        </div>
      </div>
    </div>
  );
}
```

### Session Management

To maintain conversation context across messages, use `session_id`:

```typescript
// Create a session ID for a new conversation
const newSessionId = crypto.randomUUID();

// First message starts the session
streamAgentMessage("my-agent", "Hello!", onChunk, onDone, onError, {
  sessionId: newSessionId,
  userId: "user@example.com",
});

// Subsequent messages continue the same session
streamAgentMessage("my-agent", "Follow-up question", onChunk, onDone, onError, {
  sessionId: newSessionId,  // Same session = conversation history
  userId: "user@example.com",
});
```

---

## Option 3: A2A Protocol (For Agent-to-Agent)

If you need **agent-to-agent** communication (not human-to-agent chat), use the A2A interface:

```python
# Backend: Enable A2A in your AgentOS
from agno.os import AgentOS

agent_os = AgentOS(agents=[my_agent], a2a_interface=True)
```

This exposes endpoints like:
- `/a2a/agents/{id}/v1/message:stream` — streaming A2A responses
- `/a2a/agents/{id}/v1/message:send` — non-streaming A2A responses

---

## Summary: Which Path?

| Approach | Best For | Effort | Customization |
|---|---|---|---|
| **AgentUI** | Quick start, internal tools, prototyping | Minutes | Medium (clone & modify) |
| **REST API + Custom UI** | Production apps, full design control | Hours-Days | Full |
| **A2A Protocol** | Agent-to-agent communication | Hours | N/A |

**Recommendation for your case**: Since you already have a TypeScript frontend, I'd start with **Option 2** (custom integration via the REST API). It gives you full control over the chat experience while leveraging AgentOS for the backend. The key is `POST /agents/{agent_id}/runs` with `stream=true`, parsing the SSE response in your frontend.

If you want to prototype fast first, spin up AgentUI alongside your app, use it to validate the streaming works, then build your custom UI.

---

## Run 2 — Agno Agent ✓ COMPLETED

*2026-05-02T13:27:22* · `glm-5.1:cloud` · `107da38c...`

### Prompt

how should we implement auth so agents can create user memories etc?

### Response

Great question — this connects directly to your Small Business Agentic Operating System and the CC-4 information boundaries pattern from the Project Manager. Here's how to implement auth so agents can create user memories, scoped correctly per user:

## How Agno Handles Auth + User Memories

Agno has a well-designed auth layer that connects authentication to memory scoping via **`user_id`**. Here's the flow:

### 1. JWT Middleware (Authentication + Parameter Injection)

The `JWTMiddleware` does the heavy lifting. It validates JWT tokens **and automatically injects** `user_id`, `session_id`, and custom claims into agent runs:

```python
from agno.os import AgentOS
from agno.os.middleware import JWTMiddleware, TokenSource

agent_os = AgentOS(
    id="edgeai-agent-os",
    agents=[my_agent],
    authorization=True,  # enables RBAC
)

app = agent_os.get_app()

app.add_middleware(
    JWTMiddleware,
    verification_keys=["your-jwt-verification-key"],  # or JWKS file
    algorithm="RS256",
    user_id_claim="sub",           # extracts user_id from JWT "sub" claim
    session_id_claim="session_id", # extracts session_id from JWT
    token_source=TokenSource.BOTH, # header + cookie
    cookie_name="access_token",
    validate=True,
    verify_audience=True,
)
```

**Key insight**: When a request hits the `/agents/{agent_id}/runs` endpoint with a valid JWT, Agno **automatically** uses the `user_id` and `session_id` from the token. You don't pass them manually — the middleware injects them.

### 2. User Memories Are Scoped by `user_id`

Memories are stored per-user. When an agent runs with `user_id="sarah@chenlegal.com"`, all memories it creates/retrieves are scoped to that user:

```python
# Automatic mode — agent creates/updates memories after each run
agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    db=db,
    update_memory_on_run=True,  # MemoryManager runs after each response
)

# OR agentic mode — agent has a tool to manage memories deliberately
agent = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    db=db,
    enable_agentic_memory=True,  # agent gets a memory management tool
)
```

Then in the API call (or via the JWT-injected `user_id`):
```python
agent.print_response(
    "What are my upcoming contract deadlines?",
    user_id="sarah@chenlegal.com",  # JWT middleware injects this automatically
    stream=True,
)
```

### 3. Agents Share Memories When They Share a Database

This is the critical pattern for your orchestrator + specialist architecture:

```python
from agno.db.postgres import PostgresDb

# SHARED database = shared memories
db = PostgresDb(db_url="postgresql+psycopg://ai:ai@localhost:5432/edgeai")

orchestrator = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    db=db,  # same db
    update_memory_on_run=True,
)

specialist = Agent(
    model=Ollama(id="glm-5.1:cloud"),
    db=db,  # same db
    update_memory_on_run=True,
)

# Sarah tells the orchestrator she likes hiking
orchestrator.print_response(
    "I review commercial contracts, mostly for SMEs.",
    user_id="sarah@chenlegal.com",
)

# The specialist ALREADY KNOWS this because they share the same db
specialist.print_response(
    "What type of contracts should I prioritise?",
    user_id="sarah@chenlegal.com",  # same user_id, same db = shared memories
)
```

### 4. RBAC Scopes for Memory Access Control

Agno has built-in RBAC scopes for memories:

| Scope | Description |
|-------|-------------|
| `memories:read` | View memories and memory topics |
| `memories:write` | Create, update, optimize memories |
| `memories:delete` | Delete memories |

You can also scope to specific agents:
- `agents:my-agent:run` — run a specific agent
- `memories:write` — write memories for any agent the user can access

### 5. Custom Memory Instructions (CC-3 Epistemic Metadata)

You can control **what** agents remember using `memory_capture_instructions`:

```python
memory = MemoryManager(
    model=Ollama(id="glm-5.1:cloud"),
    memory_capture_instructions="""
    Memories should only include:
    - Client preferences and priorities
    - Workflow patterns and bottlenecks
    - Decision-making tendencies
    - Verification preferences
    
    Ignore: personal opinions unrelated to work, 
    temporary emotional states, information already captured.
    """,
    db=db,
)
```

This is a lightweight form of **epistemic metadata** — you're controlling what the agent encodes as worth remembering, not just letting it store everything.

---

## Architecture for Your Small Business OS

Here's how this maps to your 3-tier architecture (AstroJS web → Hono/Cloudflare → Agno runtime → Data tier):

### Auth Flow

```
1. User logs in via AstroJS web app
2. AstroJS backend (or auth service) issues JWT:
   {
     "sub": "sarah@chenlegal.com",    ← user_id
     "session_id": "session_abc123",   ← session tracking
     "scopes": [
       "agents:run",
       "memories:read",
       "memories:write",
       "sessions:read"
     ],
     "aud": "edgeai-agent-os",
     "exp": 1735689600
   }

3. Web app sends JWT in Authorization header to Hono API
4. Hono proxies to AgentOS runtime (or calls directly)
5. JWTMiddleware validates, injects user_id + session_id
6. Agent runs scoped to that user
7. Memories are stored in Postgres with user_id foreign key
8. Multiple agents sharing the same db share memories per user
```

### Implementation Pattern

```python
# agent_runtime/main.py
from agno.os import AgentOS
from agno.os.middleware import JWTMiddleware, TokenSource
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.models.ollama import Ollama

# Shared database for memory sharing
db = PostgresDb(
    db_url="postgresql+psycopg://edgeai:edgeai@localhost:5432/edgeai",
    memory_table="user_memories",
)

# Orchestrator agents
commercial_orchestrator = Agent(
    name="Commercial Orchestrator",
    model=Ollama(id="glm-5.1:cloud"),
    db=db,
    enable_agentic_memory=True,
    # ... your orchestrator config
)

# Specialist agents
contract_extractor = Agent(
    name="Contract Extractor",
    model=Ollama(id="glm-5.1:cloud"),
    db=db,
    update_memory_on_run=True,  # automatic memory, simpler for Extractors
    # ... your specialist config
)

agent_os = AgentOS(
    id="edgeai-agent-os",
    agents=[commercial_orchestrator, contract_extractor],
    authorization=True,
)

app = agent_os.get_app()

app.add_middleware(
    JWTMiddleware,
    verification_keys=["your-public-key"],
    algorithm="RS256",
    token_source=TokenSource.BOTH,
    cookie_name="access_token",
    validate=True,
    verify_audience=True,
    user_id_claim="sub",
    session_id_claim="session_id",
    authorization=True,  # enable RBAC
)

# Exclude public routes from auth
# (login, register, health checks, etc.)
```

### Connecting to Your CC-4 Private Schema Pattern

Your Project Manager agent uses a private Postgres schema (`project_manager`) for data isolation. This pattern works **alongside** user-scoped memories:

- **Private schema** = agent-specific data (tasks, projects, agent_instructions) — CC-4 enforced at database level
- **User memories** = user-scoped contextual knowledge (preferences, patterns, history) — scoped by `user_id`
- **They're complementary**: the private schema stores structured agent data; user memories store unstructured user context

### Connecting to Your CC-8 Audit Trail

The `agent_instructions` table from your Project Manager design is the **structured** audit trail. User memories are the **contextual** audit trail. Together they give you:
- What the agent did (agent_instructions table — who authorized, what instruction, what status)
- What the agent knows about the user (user_memories — preferences, patterns, priorities)

### Key Decisions for Your Architecture

| Decision | Recommendation | Why |
|----------|---------------|-----|
| Auth method | JWT (RS256) | Agno has native support, works with your Cloudflare edge layer |
| Token source | `TokenSource.BOTH` | Web app uses cookies (XSS protection), API clients use headers |
| Memory mode for orchestrators | `enable_agentic_memory=True` | Orchestrators need deliberate memory control (CAWDP: boundary-aware) |
| Memory mode for Extractors | `update_memory_on_run=True` | Simpler, automatic — Extractors don't need to decide what to remember |
| Memory mode for Assessors | `enable_agentic_memory=True` | Assessors should be deliberate about what they encode (CC-3) |
| Custom memory instructions | Yes — per agent class | Extractors capture facts; Assessors capture patterns + flags; Generators capture preferences |
| RBAC scopes | Per-role | Sarah Chen gets `memories:read+write`, `agents:*:run`; agents get `memories:read` only |
| Private schema + user memories | Both | Private schema for CC-4 data isolation; user memories for shared context |

### One Watch-Out

Agno's user memories are **flat** (topic-tagged strings). They're not PRISM-typed knowledge objects with epistemic metadata. For your Agent-Native Knowledge Base, you'll want to supplement user memories with your PRISM graph in TypeDB for the structured, typed, epistemically-transparent knowledge layer. The user memories handle the "Sarah likes X" layer; PRISM handles the "Decision X was made on date Y with confidence Z by authority W" layer.

---
