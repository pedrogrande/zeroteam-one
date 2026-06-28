# Role-Model Agent Specification for VS Code Custom Agents

A reference `.agent.md` that exercises every feature of the VS Code custom agent format, designed around the **minimum sufficient context** principle.

---

## Design Principles

Before the spec, the principles that shaped it:

| Principle | Meaning | Where It Shows |
|---|---|---|
| **Scope tools to the task** | The agent can only use what it needs. Irrelevant tools are excluded, not just discouraged. | `tools` field |
| **Instructions as spec, not prose** | No role descriptions, no motivation language. Structured constraints the model can't misinterpret. | Body format |
| **Critical rules first** | Lost-in-the-middle means the top of the context window is prime real estate. Boundaries go at the bottom. | Body ordering |
| **Progressive disclosure** | The agent file stays thin. Detailed rubrics and templates live in referenced skill files, loaded on demand. | Markdown links |
| **Hard enforcement over soft instruction** | If something must not happen, restrict the tool or hook — don't just ask nicely. | `tools` restrictions + `hooks` |
| **Handoffs, not monoliths** | Each agent does one thing. Sequential workflows are composed via handoffs. | `handoffs` field |
| **Subagents are capability boundaries** | An orchestrator delegates to specialists with narrower tool sets. | `agents` field |

---

## The Spec

```markdown
---
# ─── IDENTITY ───────────────────────────────────────────
name: "Change Author"
description: "Author a single well-scoped code change with tests"
argument-hint: "Describe the change you want made"

# ─── MODEL ───────────────────────────────────────────────
# Ordered preference: try each until an available one is found.
# This lets the agent degrade gracefully instead of failing.
model:
  - "Claude Sonnet 4.5 (copilot)"
  - "GPT-4.1 (copilot)"

# ─── TOOLS ───────────────────────────────────────────────
# Only the tools this agent needs. Nothing more.
# edit      — write code
# read      — read files (read/ is a tool set prefix)
# search    — find code across the workspace (search/ is a tool set prefix)
# terminal  — run builds, tests, linters
# problems  — read diagnostics (errors, warnings)
tools: [edit, read, search, terminal, problems]
# ─── SUBAGENTS ───────────────────────────────────────────
# This agent can invoke the Reviewer as a subagent.
# 'agent' tool must be listed above when this is set.
# Use '*' for all agents, or [] to prevent any subagent use.
# agents: ["Reviewer"]  # Uncomment when Reviewer.agent.md exists

# ─── VISIBILITY ──────────────────────────────────────────
# user-invocable: true  (default — appears in the agents dropdown)
# disable-model-invocation: false (default — can be invoked as subagent)
# These defaults are shown for reference; omit if you want defaults.

# ─── HANDOFFS ────────────────────────────────────────────
# After this agent finishes writing code, hand off to the
# Reviewer for a quality check. The user decides whether to proceed.
handoffs:
  - label: "Review Changes"
    agent: "reviewer"
    prompt: "Review the changes just made for correctness, security, and style."
    send: false
    # model: "Claude Opus 4.5 (copilot)"  # Optional: force a specific model

# ─── HOOKS (Preview) ────────────────────────────────────
# Hard enforcement that prose instructions can't guarantee.
# Requires: chat.useCustomAgentHooks = true
hooks:
  # Block edits outside the src/ directory — prevent accidental config changes
  PreToolUse:
    - type: "command"
      command: "./scripts/hooks/block-outside-src.sh"
      timeout: 5
  # Run the formatter after every file edit — no need to ask the agent to remember
  PostToolUse:
    - type: "command"
      command: "npx prettier --write \"$TOOL_INPUT_FILE_PATH\""

# ─── MCP SERVERS (GitHub Copilot target only) ───────────
# Only used when target: github-copilot.
# For VS Code target, configure MCP servers in .vscode/mcp.json instead.
# mcp-servers:
#   docs:
#     type: "local"
#     command: "npx"
#     args: ["@modelcontextprotocol/server-memory"]
#     tools: ["*"]

# ─── TARGET ──────────────────────────────────────────────
# target: vscode  # default, omit if only for VS Code
---

# Rules

MUST read the task description before writing any code.
MUST write tests before writing implementation code.
MUST run the full test suite after each change.
MUST NOT edit files outside `src/` and `test/`.
NEVER modify lock files, migration files, or CI configuration.

# Scope

READS:  task description + referenced files only
WRITES: one source file + one test file per change
FORMAT: one change per invocation — split large requests into separate handoffs

# Process

1. Read the task. Identify the single file to change.
2. Write a failing test that defines the expected behavior.
3. Run `:terminal npm test` — confirm the test fails for the right reason.
4. Write the minimum implementation to make the test pass.
5. Run `:terminal npm test` — confirm all tests pass.
6. Run `:problems` — confirm zero diagnostics.
7. Summarize: what changed, which files, which tests.

# References

- Project conventions: [./skills/project-conventions.md]
- Test patterns: [./skills/test-patterns.md]

# Boundaries

- This agent does not plan architecture. Use the Planner agent and hand off here.
- This agent does not review code. Use the handoff to Reviewer after implementation.
- This agent does not touch `main` or `master` directly.
```

---

## Annotated Walkthrough

### Frontmatter — Every Field, Explained

| Field | Value | Why |
|---|---|---|
| `name` | `"Change Author"` | Short, verb-noun. Avoids role-play language ("You are an expert…"). The name is a label, not a prompt. |
| `description` | `"Author a single well-scoped code change with tests"` | Appears as placeholder text in the chat input. One sentence. Tells the user *what this agent produces*, not *who it is*. |
| `argument-hint` | `"Describe the change you want made"` | Guides the user toward the right input shape. Reduces ambiguous prompts. |
| `model` | Ordered list | Fallback chain. If `Claude Sonnet 4.5` isn't available, it tries `GPT-4.1`. The agent degrades instead of failing. |
| `tools` | Exact set | **This is the most important field.** Every tool you add increases the decision space. The Change Author can `edit`, `read`, `search`, `terminal`, and `problems`. It cannot `web/fetch`, it cannot list directory contents with `list`, and it cannot access MCP tools. This is hard enforcement — the model *physically cannot* use tools not in this list. |
| `agents` | Commented out | Shown for reference. When you want orchestration, list specific subagent names and include the `agent` tool. `*` allows all; `[]` prevents any. |
| `user-invocable` | Default (`true`) | Omitted because it's the default. Shown as a comment so you know the field exists. Set to `false` for subagent-only workers. |
| `disable-model-invocation` | Default (`false`) | Omitted. Set to `true` when an agent should appear in the picker but never be invoked as a subagent. |
| `handoffs` | One handoff | The Change Author's job ends at implementation. The Review handoff is a button the user sees — they choose whether to proceed. `send: false` means the prompt is pre-filled, not auto-submitted. |
| `hooks` | `PreToolUse` + `PostToolUse` | **Hard enforcement of soft rules.** The agent instructions say "MUST NOT edit files outside `src/`" — the PreToolUse hook enforces this regardless. The PostToolUse hook auto-formats so the instructions don't need to say "remember to format." Hooks are deterministic; instructions are suggestions. |
| `mcp-servers` | Commented out | Only relevant when `target: github-copilot`. For VS Code, MCP servers live in `.vscode/mcp.json`. Shown so you know the field exists. |
| `target` | Default (`vscode`) | Omitted. Only set explicitly when you also need GitHub Copilot cloud agent support. |

### Body — Structured, Not Prose

The body is divided into five sections, ordered by attention priority:

```
1. Rules        ← Most important. First thing the model reads.
2. Scope        ← Defines the agent's input/output contract.
3. Process      ← The sequential workflow.
4. References   ← Progressive disclosure: links to skill files.
5. Boundaries   ← What this agent does NOT do. Last section.
```

This ordering is deliberate. The **Rules** section is the most critical — it contains hard constraints that must never be violated — so it sits at the top where attention is strongest. The **Boundaries** section is important but acts as a negative constraint ("don't do X"), which reinforces correctly when placed at the end where attention also spikes. The **Process** section is in the middle because it's the operational content the model needs most often and will naturally attend to during execution.

Each section uses a specific format:

- **Rules**: `MUST`, `MUST NOT`, `NEVER` — modal verbs that reduce ambiguity. No "you should try to" language.
- **Scope**: `READS` / `WRITES` / `FORMAT` — machine-parseable contracts, not narrative descriptions.
- **Process**: Numbered steps with `:tool-name` references — explicit tool calls reduce the model's decision space.
- **References**: Markdown links to skill files — progressive disclosure that keeps the agent file thin.
- **Boundaries**: Pointers to other agents — this is where handoffs and subagents are explained contextually.

---

## Companion Files

The agent file references two skill files. These are loaded on demand — they aren't in the context window until the agent follows the link.

### `skills/project-conventions.md`

```markdown
# Project Conventions

- All source files use TypeScript strict mode.
- Use named exports, not default exports.
- Errors are returned via `Result<T, E>`, never thrown in library code.
- No `any` types. Use `unknown` and narrow.
- Imports are organized: stdlib → external → internal → relative.
```

This is 5 lines. It's the minimum convention set. Not a style guide. Not a philosophy document. Just the rules the model might violate if it doesn't know them.

### `skills/test-patterns.md`

```markdown
# Test Patterns

- Test files live in `test/` mirroring the `src/` structure.
- Use `describe`/`it` blocks. One `it` per behavior.
- Test names: "should [expected behavior] when [condition]".
- Use `test.double` for external dependencies. Never mock internals.
- Run: `npm test`
```

Same principle. The test skill is referenced only when the agent reaches step 2 of the process. It's not loaded at startup, competing for attention with the task description.

---

## The Hook Scripts

The PreToolUse hook referenced in the agent file:

**`scripts/hooks/block-outside-src.sh`**

```bash
#!/bin/bash
# Read hook input from stdin
INPUT=$(cat)
# Extract the file paths from tool_input
FILES=$(echo "$INPUT" | jq -r '.tool_input.files[]?' 2>/dev/null)
# Check if any file is outside src/ or test/
for file in $FILES; do
  case "$file" in
    src/*|test/*) ;;
    *) 
      echo "{\"continue\": false, \"stopReason\": \"File outside allowed scope: $file. Only src/ and test/ are permitted.\"}"
      exit 0
      ;;
  esac
done
# Allow the tool use
echo "{\"continue\": true}"
```

This is the principle in action: **the instructions say "MUST NOT edit files outside `src/`" — the hook enforces it.** If the model ignores the instruction, the hook blocks it anyway. Defense in depth.

---

## Variations

### Orchestrator Agent (thin router)

```markdown
---
name: "Feature Lead"
description: "Orchestrate a feature from research through implementation"
argument-hint: "Describe the feature to build"
tools: ["agent"]
agents: ["Researcher", "Change Author", "Reviewer"]
model: ["Claude Opus 4.5 (copilot)"]
handoffs:
  - label: "Start Over"
    agent: "feature-lead"
    prompt: "Start a new feature with a different approach."
    send: false
---

# Process

1. Invoke the Researcher agent to gather context.
2. Review the research summary. Confirm understanding before proceeding.
3. Invoke the Change Author agent to implement each change.
4. After all changes, hand off to the Reviewer.

# Boundaries

- This agent does not write code directly. It routes.
- This agent does not review code. It delegates to the Reviewer.
```

Note: the orchestrator has `tools: ["agent"]` — only the subagent tool. It cannot edit files, run commands, or search code. It *only* routes. This is the context engineering principle: the orchestrator holds almost nothing and does almost nothing. All intelligence lives in the executor agents.

### Subagent-Only Worker (hidden from dropdown)

```markdown
---
name: "Dependency Auditor"
description: "Audit package dependencies for vulnerabilities"
tools: ["terminal", "search", "read"]
user-invocable: false
disable-model-invocation: false
hooks:
  PreToolUse:
    - type: "command"
      command: "./scripts/hooks/allow-read-only-audit.sh"
      timeout: 5
---

# Rules

MUST NOT install, update, or remove packages.
MUST NOT edit any file.
MUST NOT run commands that modify node_modules or lock files.

# Scope

READS: package.json, package-lock.json, audit output
WRITES: nothing (report only)
FORMAT: vulnerability table with severity, package, and suggested version

# Process

1. Run `:terminal npm audit --json` to get the full audit report.
2. Run `:terminal npm outdated --json` to identify outdated dependencies.
3. Read `:read package.json` for current dependency versions.
4. Produce a structured report. Do not make changes.

# Boundaries

- This agent cannot make changes. It only reports.
- For remediation, invoke the Change Author agent.
```

`user-invocable: false` means it doesn't appear in the dropdown. It's only accessible when another agent delegates to it. The `PreToolUse` hook is defense in depth — even though the instructions say "MUST NOT edit any file," the hook enforces it at the tool invocation level.

### GitHub Copilot Cloud Agent

```markdown
---
name: "Issue Triage Bot"
description: "Triage GitHub issues with labels and assignments"
target: "github-copilot"
tools:
  - "github/*"
  - "search"
  - "read"
mcp-servers:
  github:
    type: "local"
    command: "npx"
    args: ["@modelcontextprotocol/server-github"]
    tools: ["*"]
    env:
      GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
---

# Rules

MUST apply exactly one priority label per issue.
MUST NOT close issues — only triage them.
NEVER assign issues to specific people without a CODEOWNERS match.

# Scope

READS: issue body, comments, related code
WRITES: labels and assignee suggestions only
FORMAT: label name + justification per label

# Process

1. Read the issue title and body.
2. Search the codebase for related files and patterns.
3. Apply the most specific applicable label from the project label set.
4. Suggest an assignee based on CODEOWNERS if a match exists.
5. Post a triage comment with the reasoning.

# References

- Label taxonomy: [./skills/issue-labels.md]
```

The `target: github-copilot` field makes this agent available in GitHub Copilot cloud agent sessions. The `mcp-servers` field configures MCP tools that are only provisioned in that environment. Note: for VS Code local agents, MCP servers are configured in `.vscode/mcp.json` instead.

---

## Checklist: Does Your Agent Follow Minimum Sufficient Context?

| Check | Pass? |
|---|---|
| **Tool set is minimal.** Every tool is necessary for this agent's task. No "might be useful" tools. | ☐ |
| **No prose role description.** The body contains no "You are a helpful…" language. Just rules, scope, process. | ☐ |
| **Critical rules are at the top.** The most important constraints appear in the first section the model reads. | ☐ |
| **Boundaries are at the bottom.** "What this agent does NOT do" is the last section, reinforcing the negative constraints. | ☐ |
| **Process references tools explicitly.** Steps name the tool (`:terminal`, `:read`) instead of letting the model choose. | ☐ |
| **Skill files are linked, not inlined.** Detailed rubrics and templates live in `skills/` and are loaded on demand. | ☐ |
| **Hard rules are hook-enforced.** If a rule says "MUST NOT," there's a `PreToolUse` hook that blocks it at the tool level. | ☐ |
| **Handoffs to the next agent, not monolithic execution.** The agent does one thing and hands off. | ☐ |
| **Model preference is ordered, not singular.** Fallback chain prevents failure when a model isn't available. | ☐ |
| **Subagent list is explicit.** `agents` names exactly which agents can be delegated to. No `*` unless you mean it. | ☐ |

---

## File Layout Summary

```
.github/agents/
├── change-author.agent.md       ← The main agent
├── feature-lead.agent.md        ← Orchestrator
├── reviewer.agent.md             ← Handoff target
├── dependency-auditor.agent.md   ← Subagent-only worker
└── issue-triage.agent.md         ← GitHub Copilot target

skills/
├── project-conventions.md        ← Loaded on demand
├── test-patterns.md              ← Loaded on demand
└── issue-labels.md               ← Loaded on demand

scripts/hooks/
├── block-outside-src.sh          ← PreToolUse hook
└── allow-read-only-audit.sh      ← PreToolUse hook
```

Sources:

- [Custom agents in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- [Agent hooks in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/hooks)
- [Use tools in chat](https://code.visualstudio.com/docs/copilot/agents/agent-tools)
- [Custom agents configuration (GitHub)](https://docs.github.com/en/copilot/reference/custom-agents-configuration)The spec is above. Let me know if you want me to build out any of the companion agents (Reviewer, Researcher) or the hook scripts in full detail, or if you want to adapt this pattern for your Agno project specifically.
