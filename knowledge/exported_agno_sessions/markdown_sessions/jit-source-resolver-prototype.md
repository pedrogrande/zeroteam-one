# Project Brief: JIT Source Resolver — Validated Prototype

**Project codename:** `context-gate`
**Owner:** Pete Argent ([@pedrogrande](https://github.com/pedrogrande))
**Date:** 20 June 2026
**Estimated duration:** 1–2 days (weekend prototype)
**Status:** Ready to build

***

## Purpose

This prototype exists to answer one falsifiable question before committing to a larger build:

> **Does injecting verified source-native context (signature + passing test + version delta) at the moment of API use reduce agent failure rate and self-correction cost on Agno tasks, compared to an unassisted agent?**

If yes: the JIT resolver pattern is validated and earns the next build layer.
If no: the dominant failure mode is not knowledge currency — investigate reasoning, spec ambiguity, or integration seams instead.

The brief is deliberately scoped to the minimum build that can produce a clean answer. No features are added that don't directly serve the measurement.

***

## Background

Today's exploration of agent-facing documentation produced a concept called the Knowledge Compiler — a system that assembles pre-built context bundles from framework source code and delivers them to coding agents before each task. A rigorous critique of that concept identified three structural problems:

- "Cannot be wrong" overclaims what source-native knowledge delivers — intent, idiom, and composition are not in the source
- The pre-compilation selection problem (choosing what goes in the bundle) is as hard as retrieval, just moved earlier
- The compiler metaphor promises formal verification the system cannot provide

The critique proposed a better frame: instead of pushing bundles ahead of time, expose source knowledge as a JIT lookup triggered by the agent's own API reach, gated by a Verified/Unknown signal that makes missing knowledge loud instead of silent.

This prototype tests that frame.

***

## Falsifiable Claim

> A JIT harness injecting `[signature + one passing test + version delta]` on first Agno framework symbol use will produce a **statistically measurable improvement** in task success rate and/or self-correction token count versus the same base model with no injection, across a five-task Agno evaluation set.

This claim is false if:

- Task success rate shows no significant difference between conditions
- Treatment is slower overall (harness overhead outweighs benefit)
- MISS rate exceeds 30% (extraction too shallow to be useful)

***

## What to Build

### Component 1: AST Extractor

**Scope:** Signatures and raised exceptions only — no full graph, no dependency edges.

Input: Agno source at `libs/agno/agno/` (commit-pinned)
Output: A queryable JSON index structured as:

```json
{
  "Agent.__init__": {
    "parameters": [
      {"name": "name", "type": "str", "default": null, "required": true},
      {"name": "model", "type": "Model", "default": null, "required": false},
      {"name": "storage", "type": "AgentStorage", "default": null, "required": false}
    ],
    "raises": ["AgentNameError", "StorageConnectionError"],
    "source_file": "agno/agent/agent.py",
    "commit": "f185b2d"
  }
}
```

**Do not build:** Full knowledge graph, dependency edges, concept nodes, constraint taxonomy.

***

### Component 2: Test Harvester

**Scope:** One passing test per framework symbol — the highest single-value artifact.

Input: Agno test suite at `libs/agno/tests/`
Output: An index mapping each symbol to its shortest complete, passing test example:

```json
{
  "Agent": {
    "example": "def test_basic_agent():\n    agent = Agent(name='test', model=OpenAIChat())\n    response = agent.run('hello')\n    assert response.content is not None",
    "test_file": "tests/unit/test_agent.py",
    "verified_at_commit": "f185b2d"
  }
}
```

Priority: prefer tests that show composition (Agent + Storage, Agent + Memory) over unit tests that test a single parameter. One example per symbol is the constraint — pick the most compositionally informative one.

**Do not build:** Example ranking, multiple examples per symbol, example quality scoring.

***

### Component 3: Version Delta Store

**Scope:** One version transition only — Agno 1.2 → 1.3.

Input: AST extractor run against both versions
Output: A flat diff index:

```json
{
  "Agent.__init__.storage": {
    "change_type": "new_parameter",
    "since_version": "1.3",
    "detail": "storage parameter added; previously set via agent.storage = ... after init"
  },
  "Agent.run": {
    "change_type": "deprecated_pattern",
    "since_version": "1.3",
    "detail": "synchronous run() deprecated for async contexts; use arun() instead"
  }
}
```

Scope strictly to signature-detectable changes. Do not attempt to detect behavioural changes — that requires human annotation and is out of scope for this prototype.

***

### Component 4: Living Spec (manual, flat file)

**Scope:** A single markdown file authored manually for the test project.

This is not automated in the prototype. Write it by hand before running the evaluation. It should contain:

```markdown
# Project: employee-qa-slack-bot — Living Spec

## Stack
- Agno 1.3 on Railway, Slack interface, PostgreSQL

## Architectural decisions
- Team(mode="route") — one specialist per turn, not coordinate
- PgAgentStorage — separate table per agent, named {agent_name}_storage
- AgentMemory enabled on all three specialists, not the team

## Known constraints (project-local)
- Railway: Postgres service must be provisioned before AgentOS deployment
- Slack: All handlers must be async; acknowledge within 3 seconds
- pgvector extension: must be enabled on Railway Postgres before first schema migration

## What has failed here
- (populated during runs)
```

Purpose: tests whether project-local knowledge (Living Spec) provides additive value on top of source-native knowledge. This is measured by comparing treatment variant A (source only) vs. treatment variant B (source + Living Spec).

***

### Component 5: The Gate

**Scope:** A system prompt rule that enforces lookup before framework API use, returns a clear MISS signal.

This is implemented as a system prompt instruction, not code:

```
SYSTEM RULE — FRAMEWORK API GATE

Before using any Agno framework class or method, you MUST call the
lookup tool with the symbol name. Do not proceed until the lookup
returns a result.

If the lookup returns "UNVERIFIED", you must STOP and output:
  KNOWLEDGE GAP: [symbol name]
  I do not have verified information for this symbol.
  Please provide the signature or I will not proceed.

This applies to: Agent, Team, AgentMemory, AgentStorage,
PgAgentStorage, PgMemoryDb, PgVector, PDFKnowledgeBase,
and all subclasses thereof.
```

The lookup tool is a simple function that queries the JSON indexes from Components 1–3 and returns a formatted context block:

```
VERIFIED — Agno 1.3 @ commit f185b2d

SIGNATURE:
  Agent(name: str, model: Model = None, storage: AgentStorage = None, ...)

RAISES:
  AgentNameError — if name contains spaces or special characters

PASSING TEST:
  def test_agent_with_storage():
      storage = PgAgentStorage(table_name="test_storage", db_url=...)
      agent = Agent(name="test", model=OpenAIChat(), storage=storage)
      assert agent.storage is not None

VERSION DELTA (since 1.2):
  storage parameter is new in 1.3. Previously set as agent.storage = ... post-init.
```

On a MISS (symbol not in index): returns `UNVERIFIED — training data only. [symbol]` — nothing else.

***

## Evaluation Design

### Task Set

Five tasks chosen to stress different failure mode hypotheses:

| # | Task | Failure mode being tested | Source coverage |
|---|---|---|---|
| 1 | Wire `PgAgentStorage` to three agents with unique table names | Constraint knowledge (silent uniqueness requirement) | Source-native |
| 2 | Configure `AgentMemory` correctly, distinct from `AgentStorage` | Concept confusion (two similar-named things) | Source-native |
| 3 | Build `Team(mode="route")` with routing instructions that correctly select one specialist | Composition knowledge (how pieces fit together) | Source-native |
| 4 | Implement async Slack 3-second acknowledgement with Bolt | Integration seam knowledge (not in Agno source) | Living Spec only |
| 5 | Migrate a working Agno 1.2 codebase to 1.3 | Version delta knowledge | Delta store |

Task 4 is the deliberate control: source-native knowledge cannot help here. If the treatment improves Tasks 1–3 but not Task 4, it confirms both the value of source knowledge and the structural limit of source-only extraction. If treatment improves Task 4 only via the Living Spec, that isolates the Living Spec's contribution cleanly.

### Conditions

Run each task under three conditions:

| Condition | Model | JIT harness | Living Spec |
|---|---|---|---|
| **Baseline** | Claude Sonnet 4.5 | None | None |
| **Treatment A** | Claude Sonnet 4.5 | Yes (Components 1–3) | None |
| **Treatment B** | Claude Sonnet 4.5 | Yes (Components 1–3) | Yes (Component 4) |

Use the same base model across all conditions. Use the same task prompt word-for-word. Run each task three times per condition (15 runs per condition, 45 total) to account for non-determinism.

### Evaluation Rubric

Each run is scored on four metrics. Score before looking at the condition — blind evaluation.

**1. Task success (primary) — binary**

- Pass: the produced code is runnable, correct, and meets the task specification with no further intervention
- Fail: requires any human correction, produces a runtime error, or produces code that violates the task specification

**2. Interventions required (secondary) — integer count**

- Count of human corrections, clarifications, or redirections required to reach a passing result
- Zero for baseline if the agent gives up or produces confidently wrong code without asking

**3. Self-correction tokens (secondary) — integer count**

- Count tokens spent on retries, apologies, corrections, and re-attempts
- Excludes productive reasoning; includes any turn where the agent corrects its own previous output

**4. Time to first passing test (secondary) — turn count**

- The turn number at which the first runnable, passing test is produced
- Undefined (∞) if no passing test is produced

### Kill Criteria — decide now, before running

Stop the build and change direction if:

- **Primary metric flat:** Treatment A shows no significant improvement over Baseline on task success rate across Tasks 1–3 → failure mode is not knowledge currency; investigate reasoning
- **Integration seam dominates:** Tasks 1–3 show no improvement but Task 4 does → source extraction is irrelevant; the Living Spec is the whole value and the rest is overengineering
- **MISS rate > 30%:** The extractor returns UNVERIFIED on more than 30% of lookups → extraction scope is too shallow before adding features
- **Treatment slower overall:** Treatment B is slower (more turns, more tokens) than Baseline → harness overhead is real; optimise the lookup before building further

***

## Repository Structure

```
context-gate/
├── README.md
├── extract/
│   ├── ast_extractor.py        # Component 1
│   ├── test_harvester.py       # Component 2
│   ├── delta_generator.py      # Component 3
│   └── run_extraction.sh       # runs all three, outputs to indexes/
├── indexes/
│   ├── signatures.json         # output of ast_extractor
│   ├── examples.json           # output of test_harvester
│   └── deltas_1.2_1.3.json     # output of delta_generator
├── gate/
│   ├── lookup.py               # the tool function the agent calls
│   ├── system_prompt.md        # Component 5 — the gate rule
│   └── formatter.py            # formats lookup result as context block
├── living_spec/
│   └── employee-qa-slack-bot.md  # Component 4 — manually authored
├── evaluation/
│   ├── tasks/
│   │   ├── task_01_pg_storage.md
│   │   ├── task_02_agent_memory.md
│   │   ├── task_03_team_routing.md
│   │   ├── task_04_slack_async.md
│   │   └── task_05_migration.md
│   ├── rubric.md               # scoring instructions
│   ├── results/
│   │   └── runs.csv            # one row per run: condition, task, scores
│   └── analyse.py              # produces summary stats from runs.csv
└── agno_source/
    └── (git submodule or pinned clone @ f185b2d)
```

***

## Sequence of Work

**Step 1 — Environment (30 min)**

- Create the `context-gate` repo
- Clone or submodule Agno source at commit `f185b2d` (current main)
- Also clone Agno at the last 1.2 tag for the delta generator

**Step 2 — Extraction pipeline (2–3 hrs)**

- Build `ast_extractor.py` — walk `agno/agent/`, `agno/team/`, `agno/memory/`, `agno/storage/`, `agno/knowledge/` — extract `__init__` signatures and `raise` statements only
- Build `test_harvester.py` — walk `tests/`, find tests that import target symbols, select the shortest complete example per symbol
- Build `delta_generator.py` — diff the two version indexes, emit only signature-detectable changes
- Run `run_extraction.sh`, inspect the output indexes for correctness

**Step 3 — Gate and lookup (1 hr)**

- Write `lookup.py` — takes a symbol name string, queries all three indexes, returns the formatted context block or the UNVERIFIED signal
- Write `system_prompt.md` — the gate rule, ready to paste as system prompt
- Smoke test: manually call the lookup for `Agent`, `PgAgentStorage`, `Team`, `AgentMemory`

**Step 4 — Living Spec (30 min)**

- Author `employee-qa-slack-bot.md` by hand — the four sections: stack, decisions, constraints, failures
- Include the Slack 3-second rule, Railway Postgres ordering, pgvector extension requirement

**Step 5 — Evaluation tasks (1 hr)**

- Write the five task prompts in `evaluation/tasks/` — identical wording used across all conditions
- Write `rubric.md` — the four metrics, scoring instructions, what counts as pass/fail
- Set up `runs.csv` with headers: `condition, task_id, run_number, success, interventions, self_correction_tokens, turns_to_first_test`

**Step 6 — Run evaluation (3–4 hrs)**

- Run all 45 sessions (3 conditions × 5 tasks × 3 runs)
- Score each run blind (score before noting condition)
- Record results in `runs.csv`

**Step 7 — Analysis (1 hr)**

- Run `analyse.py` — produces mean + std per condition per task for all metrics
- Apply kill criteria: does treatment beat baseline on primary metric?
- Write a one-page finding: what happened, what it means, what to build next

***

## Definition of Done

The prototype is complete — regardless of outcome — when:

- All 45 sessions are run and scored
- `runs.csv` is complete with no missing values
- `analyse.py` has been run and the output matches the rubric
- A one-page finding document is written that states: the claim was [supported / not supported], the kill criteria that fired (if any), and the recommended next step

A finding of "not supported" is not a failure. It is the correct outcome if knowledge currency is not the dominant failure mode — and it redirects effort toward what actually matters.

***

## Success Looks Like

Treatment A beats Baseline on Task success rate for Tasks 1–3 (source-extractable tasks) with at least 2 of 3 tasks showing improvement across all three runs. Treatment B shows additional improvement on Task 4 (Living Spec task) that Treatment A does not. MISS rate is below 20%. Self-correction tokens are lower in both treatment conditions.

That outcome validates the JIT resolver pattern, isolates the specific contribution of source-native knowledge vs. project-local knowledge, and gives precise guidance for which component to invest in next.

***

**Ready to create the GitHub repository?**
