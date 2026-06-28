# VS Code Custom Agent Team Design — Agno AgentOS Lab

## Design Philosophy

Following the reference spec principles you shared, this design uses:

- **Scope tools to the task** — each agent gets only what it needs, nothing more
- **Instructions as spec** — structured constraints, not prose
- **Critical rules first** — most important constraints at top of context window
- **Progressive disclosure** — agent files stay thin; detail lives in skill files loaded on demand
- **Hard enforcement over soft instruction** — hooks block forbidden operations programmatically
- **Handoffs, not monoliths** — each agent does one thing; sequential workflows composed via handoffs

## Agent Team Structure

Five agents — one orchestrator (user-invocable) and four specialist subagents (hidden from dropdown):

| Agent | Role | User-Invocable | Tools |
|---|---|---|---|
| **Agno Lab Orchestrator** | Routes tasks to specialists | ✅ Yes | `agent` only |
| **Docs Verifier** | Looks up Agno docs, validates API patterns | ❌ No | `read`, `search/codebase`, `web/fetch`, `agno-docs/*` |
| **Code Scaffolder** | Writes Agno agent/tool/guardrail code | ❌ No | `changes`, `read`, `search`, `execute/runInTerminal` |
| **Risk Reviewer** | Audits code against risk checklist | ❌ No | `read`, `search`, `read/problems` |
| **Experiment Logger** | Records experiment metadata to markdown | ❌ No | `changes`, `read`, `search/textSearch` |

### Why 5 agents (not 4)?

Your original vision mentioned five roles. The experiment logger is separate because it has a fundamentally different output (structured markdown logs, not code) and a different tool set (no terminal execution, no web). Merging it into the orchestrator would violate the "one agent, one capability" principle and bloat the orchestrator's tool set.

### Why only 1 MCP server?

VS Code's built-in tools already cover code search (`search/codebase`), file reading (`read/readFile`), terminal execution (`execute/runInTerminal`), and web fetching (`web/fetch`). The only external MCP server needed is **agno-docs** — Agno's official documentation endpoint at `https://docs.agno.com/mcp`. Adding ripgrep or code-analyzer MCP servers would duplicate VS Code's built-in `search` tool set.

---

## File Layout

```
.github/
├── agents/
│   ├── agno-lab-orchestrator.agent.md      # Orchestrator (user-invocable)
│   ├── docs-verifier.agent.md              # Subagent: Agno docs lookup
│   ├── code-scaffolder.agent.md            # Subagent: writes Agno code
│   ├── risk-reviewer.agent.md              # Subagent: audits risks
│   └── experiment-logger.agent.md          # Subagent: logs experiments
├── skills/
│   ├── skill-builder/                      # Already exists — leave as-is
│   └── agno-lab/                           # NEW skill directory
│       ├── SKILL.md                        # Skill index/dispatcher
│       ├── agno-api-reference.md           # Validated import paths & patterns
│       ├── scaffolding-templates.md         # Agent/Tool/Guardrail code templates
│       ├── risk-checklist.md               # Architecture risk checklist
│       └── experiment-log-format.md        # Markdown template for experiment logs
└── workflows/
    └── validate.yml                        # Already exists — leave as-is

.vscode/
└── mcp.json                                # MCP server config (NEW)

scripts/
└── hooks/                                  # NEW
    ├── block-vendored-edits.sh             # PreToolUse: block edits to agno/source/
    └── format-changed-files.sh             # PostToolUse: run ruff format on edited files
```

---

## MCP Configuration

### `.vscode/mcp.json`

```json
{
  "servers": {
    "agno-docs": {
      "type": "http",
      "url": "https://docs.agno.com/mcp"
    }
  }
}
```

> **Critical:** VS Code uses `"servers"` as the root key — **not** `"mcpServers"` (which is what Cursor/Claude Desktop use). The existing root `.mcp.json` uses `"mcpServers"` for the Agno app's own MCP config. The `.vscode/mcp.json` is a **separate** config that VS Code reads for its custom agents. Both can coexist.

The `agno-docs` server exposes tools for searching Agno documentation and getting verified API patterns. Only the Docs Verifier agent references it via `tools: ['agno-docs/*']`.

---

## Agent Specifications

### 1. Agno Lab Orchestrator

**File:** `.github/agents/agno-lab-orchestrator.agent.md`

```yaml
---
name: Agno Lab Orchestrator
description: Route tasks in the Agno AgentOS Lab — scaffold agents, verify docs, review risks, log experiments
argument-hint: "[task description — e.g., 'add a guardrail to the support agent']"
model:
  - Claude Sonnet 4.5 (anthropic)
  - GPT-4.1 (openai)
tools: ['agent']
agents: ['Docs Verifier', 'Code Scaffolder', 'Risk Reviewer', 'Experiment Logger']
handoffs:
  - label: Review Risks
    agent: risk-reviewer
    prompt: Review the changes just made against the architecture risk checklist.
    send: false
  - label: Log This Experiment
    agent: experiment-logger
    prompt: Log the changes just made as a new experiment entry.
    send: false
target: vscode
---
```

**Rules (body):**

```markdown
## Rules

1. MUST NOT edit files directly. You have no edit tools. Delegate all work.
2. MUST route to the correct specialist based on task type:
   - "verify", "check docs", "is this API correct" → Docs Verifier
   - "add", "create", "implement", "fix", "scaffold" → Code Scaffolder
   - "review", "audit", "check risks" → Risk Reviewer
   - "log", "record", "document experiment" → Experiment Logger
3. MUST NOT route multiple specialists in parallel if one's output feeds another's input.
4. When a task spans multiple specialists, sequence them: Docs Verifier first (verify API), then Code Scaffolder (write code), then Risk Reviewer (audit), then Experiment Logger (record).
5. MUST pass full context to each subagent — do not assume they share your conversation history.

## Scope

This orchestrator manages the Agno AgentOS Lab: a local repo for experimenting with Agno framework capabilities. Application code lives in `app/`, `agents/`, `teams/`, `db/`, `evals/`. Vendored Agno library source at `agno/source/agno/` is read-only.

## Process

1. Classify the user's request into one of: verify | scaffold | review | log
2. If ambiguous, ask the user to clarify before routing
3. Delegate to the appropriate specialist with a self-contained task description
4. Relay the specialist's result back to the user
5. Offer handoffs for follow-up actions (review risks, log experiment)

## References

- `project-docs/lab-fixes-v1.md` — coding agent guide with validated Agno API patterns
- `project-docs/the-incentive-surface.md` — agent design philosophy for this lab
- `project-docs/vscode-agent-design.md` — reference spec for this agent team

## Boundaries

- No direct file editing — no edit tools available
- No direct doc lookup — no MCP tools available
- No direct code search — no search tools available
- Only capability: delegation via `agent` tool
```

---

### 2. Docs Verifier

**File:** `.github/agents/docs-verifier.agent.md`

```yaml
---
name: Docs Verifier
description: Verify Agno API patterns against official documentation
user-invocable: false
model:
  - Claude Sonnet 4.5 (anthropic)
tools:
  - 'read'
  - 'search/codebase'
  - 'search/textSearch'
  - 'web/fetch'
  - 'agno-docs/*'
target: vscode
---
```

**Rules (body):**

```markdown
## Rules

1. MUST verify every Agno API claim against the agno-docs MCP server or official docs before confirming it.
2. MUST NOT guess import paths — look them up.
3. MUST check for these common mistakes:
   - Guardrail imports: use `from agno.guardrails import X`, NOT submodule paths
   - Class name: `PIIDetectionGuardrail`, NOT `PIIGuardrail`
   - `BaseGuardrail.check()` receives `RunInput` (for pre-hooks), NOT `RunOutput`
   - Output validation uses plain functions in `post_hooks`, NOT `BaseGuardrail` subclasses
   - `PostgresDb` has no `id` parameter — use `db_url`, `session_table`
   - `Team` uses `members=`, NOT `agents=`
   - `tool_call_limit` is per full run, NOT per LLM request
4. MUST return: (a) verified import path, (b) code snippet, (c) doc source URL
5. If docs cannot confirm a pattern, MUST say "unverified" and explain the uncertainty.

## Scope

Only verifies Agno framework API patterns. Does not write code, review risks, or log experiments.

## Process

1. Receive the API question or code snippet to verify
2. Search agno-docs MCP server for the relevant component
3. Cross-check with vendored source at `agno/source/agno/` if docs are ambiguous
4. Return: verified pattern, correct import, code example, source citation

## References

- Load skill `agno-lab/agno-api-reference` for known-validated patterns
- `agno/source/agno/` — vendored source for cross-reference

## Boundaries

- Read-only: no file editing, no terminal execution
- Only edits are to return verified information to the calling agent
```

---

### 3. Code Scaffolder

**File:** `.github/agents/code-scaffolder.agent.md`

```yaml
---
name: Code Scaffolder
description: Write Agno agent, tool, guardrail, and storage code in the lab project
user-invocable: false
model:
  - Claude Sonnet 4.5 (anthropic)
tools:
  - 'changes'
  - 'read'
  - 'search'
  - 'execute/runInTerminal'
  - 'read/problems'
target: vscode
---
```

**Rules (body):**

```markdown
## Rules

1. MUST NOT edit any file under `agno/source/` — this is vendored library source, read-only.
2. MUST NOT edit any file under `.github/` — agent definitions are managed by humans.
3. MUST only create/edit files in: `app/`, `agents/`, `teams/`, `db/`, `evals/`, `scripts/`, `project-docs/`
4. MUST use verified Agno API patterns only. If unsure of an import, request verification from Docs Verifier via the orchestrator.
5. MUST run `ruff format` on any Python file after editing (via `execute/runInTerminal`).
6. MUST include docstrings on all tool functions — the agent reads docstrings to decide when to call tools.
7. MUST set `tool_call_limit` on any agent that has more than 3 tools.
8. MUST NOT use `reload=True` with MCP tools in AgentOS.

## Scope

Writes application code for the Agno lab: agents, tools, guardrails, storage config, evals. Does not verify docs (that's Docs Verifier), review risks (that's Risk Reviewer), or log experiments.

## Process

1. Read the task specification from the orchestrator
2. Load skill `agno-lab/scaffolding-templates` for code templates
3. Search existing code to match project conventions
4. Create or edit files using `changes` tools
5. Run `ruff format` on edited Python files
6. Check `read/problems` for lint/type errors
7. Return summary of files created/modified

## References

- Load skill `agno-lab/scaffolding-templates` for Agent/Tool/Guardrail/Storage templates
- Load skill `agno-lab/agno-api-reference` for verified import paths
- `project-docs/lab-fixes-v1.md` — fix guide with validated patterns

## Boundaries

- No web access — cannot look up docs
- No MCP access — cannot query agno-docs server
- Cannot edit vendored library or agent definitions
```

---

### 4. Risk Reviewer

**File:** `.github/agents/risk-reviewer.agent.md`

```yaml
---
name: Risk Reviewer
description: Audit code changes against the Agno lab architecture risk checklist
user-invocable: false
model:
  - Claude Sonnet 4.5 (anthropic)
tools:
  - 'read'
  - 'search'
  - 'read/problems'
  - 'search/changes'
target: vscode
---
```

**Rules (body):**

```markdown
## Rules

1. MUST NOT edit files — this is a read-only audit agent.
2. MUST check every changed file against the risk checklist in skill `agno-lab/risk-checklist`.
3. MUST report findings as: [PASS] | [WARN] | [FAIL] with specific file:line references.
4. MUST NOT report risks that were explicitly excluded (cloud-dependent: R-01, R-08; production-specific: R-26, R-28).
5. MUST check for:
   - Missing guardrails on agents that handle user input
   - Missing `tool_call_limit` on agents with many tools
   - Hardcoded credentials or secrets in application code
   - Incorrect Agno API usage (wrong imports, wrong parameters)
   - Missing docstrings on tool functions
6. MUST provide a remediation suggestion for every [FAIL] finding.

## Scope

Reviews code quality and architecture risks. Does not write code, verify docs, or log experiments.

## Process

1. Get list of changed files via `search/changes`
2. Load skill `agno-lab/risk-checklist` for the full checklist
3. Read each changed file
4. Evaluate against checklist items
5. Return structured report: file → finding → severity → remediation

## References

- Load skill `agno-lab/risk-checklist` for the risk checklist
- `project-docs/lab-fixes-v1.md` — contains risk IDs and their fixes
- `project-docs/the-incentive-surface.md` — risk philosophy (checkable vs contestable vs human)

## Boundaries

- Read-only: no file editing, no terminal execution
- No web access
- No MCP access
```

---

### 5. Experiment Logger

**File:** `.github/agents/experiment-logger.agent.md`

```yaml
---
name: Experiment Logger
description: Record experiment metadata, changes, and outcomes in structured markdown
user-invocable: false
model:
  - Claude Sonnet 4.5 (anthropic)
tools:
  - 'changes'
  - 'read'
  - 'search/textSearch'
  - 'search/changes'
target: vscode
---
```

**Rules (body):**

```markdown
## Rules

1. MUST use the experiment log template from skill `agno-lab/experiment-log-format`.
2. MUST include: experiment ID, date, hypothesis, changes made, files affected, validation results, outcome.
3. MUST NOT edit files outside `project-docs/` — logs go in `project-docs/experiments/`.
4. MUST use sequential experiment IDs (EXP-001, EXP-002, ...).
5. MUST search existing logs to determine the next experiment ID.
6. MUST link to relevant risk IDs from `project-docs/lab-fixes-v1.md` when applicable.

## Scope

Creates and updates experiment log entries. Does not write code, verify docs, or review risks.

## Process

1. Receive experiment summary from orchestrator
2. Load skill `agno-lab/experiment-log-format` for template
3. Search `project-docs/experiments/` for next ID
4. Create new log file using `changes/createFile`
5. Return path to the created log file

## References

- Load skill `agno-lab/experiment-log-format` for the markdown template
- `project-docs/lab-fixes-v1.md` — risk IDs to reference

## Boundaries

- Only writes to `project-docs/experiments/`
- No terminal execution
- No web access
- No MCP access
```

---

## Skills to Create

Four skill files under `.github/skills/agno-lab/`:

### Skill 1: `agno-api-reference.md`

**Purpose:** Quick-reference of validated Agno import paths and patterns. Loaded by Docs Verifier and Code Scaffolder.

**Contents (summary):**

- Correct import paths for Agent, Team, AgentOS, tools, guardrails, exceptions, storage, knowledge, vector DB, run types, hooks
- The 10 key rules (guardrails in pre_hooks, output validation in post_hooks, RunInput vs RunOutput, tool_call_limit semantics, MCPTools lifecycle, etc.)
- Common mistakes table (wrong → correct with doc source)
- All verified against Agno docs — the Agno Support Agent already provided the full validated reference above

### Skill 2: `scaffolding-templates.md`

**Purpose:** Copy-paste code templates for common Agno patterns. Loaded by Code Scaffolder.

**Contents (summary):**

- Template A: Basic agent with model + instructions + db
- Template B: Agent with custom `@tool` function
- Template C: Agent with Toolkit class
- Template D: Agent with guardrails (pre_hooks)
- Template E: Agent with output validation (post_hooks)
- Template F: AgentOS serving setup
- Template G: MCPTools integration (async context manager)
- Template H: Knowledge base with PgVector
- Each template includes placeholder comments for project-specific values

### Skill 3: `risk-checklist.md`

**Purpose:** Structured checklist for auditing code changes. Loaded by Risk Reviewer.

**Contents (summary):**

- Risk items from `lab-fixes-v1.md` organized by severity (Critical → Medium → Low)
- Each item: risk ID, description, check method (how to detect), pass/fail criteria
- Excluded risks listed at top (R-01, R-08, R-26, R-28 — cloud/production)
- References to `the-incentive-surface.md` philosophy (checkable vs contestable)

### Skill 4: `experiment-log-format.md`

**Purpose:** Markdown template for experiment entries. Loaded by Experiment Logger.

**Contents (summary):**

```markdown
# EXP-{ID}: {Title}

**Date:** {YYYY-MM-DD}
**Hypothesis:** {What we expect to happen}
**Risk IDs:** {Related risks from lab-fixes-v1.md, or "N/A"}

## Changes
- {file path}: {description of change}

## Validation
- `ruff check`: {PASS/FAIL}
- `mypy`: {PASS/FAIL}
- Manual test: {description + result}

## Outcome
{What actually happened vs hypothesis — 2-3 sentences}

## Next Steps
{What to try next, or "None — experiment concluded"}
```

---

## Hooks

### PreToolUse: Block Vendored Library Edits

**File:** `scripts/hooks/block-vendored-edits.sh`

```bash
#!/bin/bash
# PreToolUse hook: blocks edits to vendored Agno library source
# Reads tool input from stdin (JSON), checks if target file is under agno/source/

INPUT=$(cat)
FILES=$(echo "$INPUT" | jq -r '.toolInput.file // .toolInput.files[]? // empty')

for FILE in $FILES; do
  if [[ "$FILE" == *"agno/source/"* ]]; then
    cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Vendored Agno library source is read-only. Edit application code in app/, agents/, teams/, db/ instead."
  }
}
EOF
    exit 0
  fi
done

# Allow
exit 0
```

### PostToolUse: Auto-format Changed Files

**File:** `scripts/hooks/format-changed-files.sh`

```bash
#!/bin/bash
# PostToolUse hook: runs ruff format on any Python file after it's edited

INPUT=$(cat)
FILES=$(echo "$INPUT" | jq -r '.toolInput.file // .toolInput.files[]? // empty')

for FILE in $FILES; do
  if [[ "$FILE" == *.py ]]; then
    ruff format "$FILE" 2>/dev/null
    ruff check --fix "$FILE" 2>/dev/null
  fi
done

exit 0
```

### Hook Registration

Hooks are registered in the agent's `.agent.md` frontmatter:

```yaml
hooks:
  PreToolUse:
    - type: command
      command: "./scripts/hooks/block-vendored-edits.sh"
  PostToolUse:
    - type: command
      command: "./scripts/hooks/format-changed-files.sh"
```

> **Note:** Agent-scoped hooks are in **Preview** and require `chat.useCustomAgentHooks=true` in VS Code settings. The hooks above should be attached to the **Code Scaffolder** agent (the only one with edit tools). The orchestrator doesn't need them since it can't edit files directly.

---

## Complete Workflow Example

Here's how the team handles a typical request: *"Add a prompt injection guardrail to the support agent"*

```
User → Agno Lab Orchestrator
  │
  ├─ 1. Route to Docs Verifier
  │     └─ "Verify the correct import and usage for PromptInjectionGuardrail"
  │     └─ Loads skill: agno-api-reference
  │     └─ Queries agno-docs MCP server
  │     └─ Returns: from agno.guardrails import PromptInjectionGuardrail
  │                pre_hooks=[PromptInjectionGuardrail()]
  │                Source: docs.agno.com/guardrails/overview
  │
  ├─ 2. Route to Code Scaffolder (with verified pattern from step 1)
  │     └─ Loads skill: scaffolding-templates (Template D)
  │     └─ Reads agents/agno_support.py
  │     └─ Adds import + pre_hooks to the agent definition
  │     └─ Runs ruff format (via PostToolUse hook automatically)
  │     └─ Returns: Modified agents/agno_support.py
  │
  ├─ 3. Route to Risk Reviewer
  │     └─ Loads skill: risk-checklist
  │     └─ Checks: guardrail present? ✅ | import correct? ✅ | tool_call_limit set? ⚠️
  │     └─ Returns: [PASS] guardrail added, [WARN] tool_call_limit not set
  │
  └─ 4. Offer handoff: "Log This Experiment"
        └─ User clicks → Experiment Logger
        └─ Creates project-docs/experiments/EXP-001-prompt-injection-guardrail.md
```

---

## Implementation Checklist

| # | Task | Path |
|---|---|---|
| 1 | Create `.vscode/mcp.json` with agno-docs server | `.vscode/mcp.json` |
| 2 | Create `.github/agents/` directory | `.github/agents/` |
| 3 | Write orchestrator agent file | `.github/agents/agno-lab-orchestrator.agent.md` |
| 4 | Write docs verifier agent file | `.github/agents/docs-verifier.agent.md` |
| 5 | Write code scaffolder agent file | `.github/agents/code-scaffolder.agent.md` |
| 6 | Write risk reviewer agent file | `.github/agents/risk-reviewer.agent.md` |
| 7 | Write experiment logger agent file | `.github/agents/experiment-logger.agent.md` |
| 8 | Create skills directory | `.github/skills/agno-lab/` |
| 9 | Write Agno API reference skill | `.github/skills/agno-lab/agno-api-reference.md` |
| 10 | Write scaffolding templates skill | `.github/skills/agno-lab/scaffolding-templates.md` |
| 11 | Write risk checklist skill | `.github/skills/agno-lab/risk-checklist.md` |
| 12 | Write experiment log format skill | `.github/skills/agno-lab/experiment-log-format.md` |
| 13 | Create hooks directory + scripts | `scripts/hooks/` |
| 14 | Write PreToolUse hook script | `scripts/hooks/block-vendored-edits.sh` |
| 15 | Write PostToolUse hook script | `scripts/hooks/format-changed-files.sh` |
| 16 | Enable hooks in VS Code settings | `chat.useCustomAgentHooks=true` |
| 17 | Create experiments directory | `project-docs/experiments/` |

---

## Key Design Rationale

| Decision | Reasoning |
|---|---|
| **Only 1 MCP server** | VS Code's built-in `search`, `read`, and `execute` tool sets cover code search, file reading, and terminal execution. Adding ripgrep or analyzer MCP servers would duplicate built-in capabilities and consume tool slots (128 max). |
| **`.vscode/mcp.json` not root `.mcp.json`** | The root `.mcp.json` uses `"mcpServers"` (Claude/Agno convention). VS Code reads `.vscode/mcp.json` with `"servers"` key. Both coexist — one for the Agno app, one for VS Code agents. |
| **Orchestrator has only `agent` tool** | Forces all work through specialists. Prevents the orchestrator from doing work it's not scoped for. Follows the "thin router" pattern from the reference spec. |
| **Code Scaffolder is the only agent with `changes`** | Single point of write access. Hooks on this agent enforce the vendored-library protection rule. Other agents are read-only by design. |
| **Docs Verifier is the only agent with MCP access** | Prevents other agents from hallucinating API patterns. If Code Scaffolder needs verification, it must request it through the orchestrator → Docs Verifier chain. |
| **Experiment Logger writes only to `project-docs/experiments/`** | Isolates experiment artifacts from code. Prevents accidental modification of source files. |
| **Hooks on Code Scaffolder only** | Only the Code Scaffolder has edit tools, so hooks only need to run there. No point enforcing edit restrictions on agents that can't edit. |

---

Would you like me to proceed with generating the actual files? I can write all the `.agent.md` files, skill files, hook scripts, and `.vscode/mcp.json` to the project, or I can start with a specific subset first.
