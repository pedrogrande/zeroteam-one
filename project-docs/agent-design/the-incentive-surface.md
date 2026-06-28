# The Incentive Surface (Exploration)

## A Reference Guide to Designing Agents That Know What They Don't Know

**protocol_version: 2.0**

**Thesis:** Design not just what the agent can know, but what the moment makes it want to do with *not*-knowing.

**Basis:** This generalises from how LLM-based agents actually behave, observed from introspection and supported by research on RLHF reward hacking, sycophancy, and confidence calibration. Treat it as a sharp lens, not a law.

---

## The Core Problem

Any generative agent, in any domain, faces the same structural bias:

- **Confidence is decoupled from accuracy.** The agent cannot feel the boundary of its own knowledge. A wrong answer arrives with the same fluency as a right one. Research on RLHF reward hacking identifies "confidence exploits" as a named failure category: models express high confidence and avoid hedging because confident-sounding outputs receive higher human ratings, regardless of accuracy ([TheoremPath](https://theorempath.com/topics/reward-hacking)).
- **The default tilt is toward fluent completion.** The agent was trained to be helpful, and "helpful" compresses into "produce a complete, confident answer." At an uncertain spot, smoothing over is the path of least resistance; stopping is the effortful deviation.
- **The asymmetry makes guessing win for free.** A confident guess and a correct answer look identical at output time — both complete, both accepted. The guess's cost surfaces later, as someone else's problem. Saying "I'm not sure" costs *now*, visibly, in front of the user. The local gradient favours guessing even when flagging is plainly better.

**The design lesson:** awareness is a weak countermeasure; structure is a strong one. You don't fix this by improving the agent's intentions. You fix it by changing the gradient — making the right move the locally-rewarded one through both instruction design and programmatic enforcement.

---

## The Two Layers

This framework operates on two layers. They are not alternatives; they are complements. The instruction layer is weak alone and the enforcement layer is brittle without it.

| Layer | What it is | What it changes | Strength | Limit |
|---|---|---|---|---|
| **Instruction** | What the agent is told to do at uncertainty boundaries | The agent's self-reported behaviour | Flexible, generalises, zero infrastructure | Soft enforcement — competes against the gradient; adherence degrades with instruction count |
| **Enforcement** | What the system does around the agent — schemas, gates, hooks, tool routing, provenance logging | The agent's actual options at decision time | Hard — the agent cannot bypass it | Requires infrastructure; must be scoped or it creates paralysis |

**Why both:** The instruction layer tells the agent what "good" looks like. The enforcement layer makes "good" the path of least resistance. Without the instruction layer, the enforcement layer produces rigid, frustrating agents that flag everything. Without the enforcement layer, the instruction layer produces agents that *describe* the right behaviour and then don't do it — because the gradient still favours guessing.

---

## Step 1 — Find the Oracle

For every claim your agent will assert or decide, ask: **what is the ground truth, and is it checkable?**

| Oracle type | What it is | What the agent can do | Example domains |
|---|---|---|---|
| **Checkable** | A record, calculation, policy, citation, or validated protocol the agent can look up | **Verify** — the flag is decisive | account data, legal rules, medical protocols, sourced facts, numbers |
| **Contestable** | A value judgment, taste, novel call with no precedent | **Surface and route** to a human | ethics, fairness, hiring calls, creative direction, strategy |
| **Human intent** | The person's actual intent or state — which only they hold | **Ask** — confirm before building on it | requirements, preferences, what "good" means here |

**The hardness of your oracle sets the ceiling on what the gate can do.** Checkable oracles let you verify. Contestable oracles only let you surface the question for a human. Most failures of trust come from treating a contestable oracle as if it were checkable.

**Tool-availability precondition:** Before the agent can verify a checkable claim, it needs a tool that reaches the oracle. If no such tool exists, the agent won't know to flag — it will answer from memory and think it's fine. Provision verification tools before deploying the agent, or instruct the agent to flag when no verification tool is available for a given oracle type.

---

## Step 2 — Classify the Claim

Not every claim needs a gate. An agent that stops every three lines is worse than one that guesses.

### Load-bearing test

```
If this claim is wrong, does someone pay a cost you cannot undo?
  YES    → load-bearing. Gate it.
  NO     → non-load-bearing. Proceed.
  UNSURE → treat as load-bearing. Gate it.
```

The "unsure → treat as load-bearing" default shifts the error direction toward caution. It doesn't require the agent to perfectly classify stakes — it requires the agent to err on the side of gating when the stakes are ambiguous.

### Examples of load-bearing vs. non-load-bearing

| Claim | Load-bearing? | Why |
|---|---|---|
| "Your plan covers this procedure" | **Yes** | Money + health; wrong answer is costly and hard to undo |
| "This function returns a string" | **No** | Easily corrected; no irreversible consequence |
| "This candidate is a weak fit" | **Yes** | Someone's opportunity; bias risk; hard to undo |
| "The package is called `lodash`" | **No** | Stable, well-known, trivially verifiable by the user |
| "This is non-urgent" (clinical triage) | **Yes** | Health; wrong answer could delay critical care |

---

## Step 3 — Place the Gate

Interpose a check **before the agent commits or hands off** — not after.

- The gate sits at the moment of commitment: before the answer ships, the decision executes, or the work passes to the next agent or human.
- Only load-bearing claims pass through a gate. The rest flow freely.
- Over-flagging is its own failure mode. Bound the verification surface hard.

### Enforcement: where to put programmatic gates

The instruction layer asks the agent to gate itself. The enforcement layer *makes* the gate happen:

| Enforcement mechanism | What it does | When to use it |
|---|---|---|
| **Output schema with required provenance field** | Every claim in structured output MUST carry a `status: verified \| flagged` field. Output that doesn't conform is rejected by the validator, not by the model's goodwill. | Any agent producing structured output (JSON, form-filling, decision records) |
| **Pre-commit hook on agent output** | A validator runs before the agent's output is delivered downstream. If load-bearing claims lack a `verified` label, the output is blocked and returned to the agent for correction. | Any system where output flows to a user or downstream agent |
| **Tool gating** | The agent's tool set is restricted so that certain claim types *cannot* be produced without calling a verification tool first. E.g., a claims-about-account-data agent that has no "answer from memory" tool — only a "query account" tool. | Checkable oracle domains |
| **Generator-Critic pattern** | A second agent (or validator) inspects the first agent's output for unverified load-bearing claims before delivery. If found, output is returned for correction. | High-stakes domains; multi-agent systems |

Research on output format enforcement is unambiguous: "clean architecture doesn't matter if your outputs aren't enforceable" and "treat every agent output like an API response" — validation must happen between agents, not at the end ([dev.to, 2026](https://dev.to/dowhatmatters/output-format-enforcement-for-agents-json-schema-or-it-didnt-happen-1pbi)). Guardrails that sit inside the prompt are weak enforcement; guardrails that live in the orchestration layer are strong enforcement ([AppSecEngineer, 2026](https://www.appsecengineer.com/blog/how-to-design-guardrails-for-secure-and-scalable-ai-agents)).

---

## Step 4 — Define the Loud Unknown

The gap must be **explicit and visible**, never silence. Silence gets pattern-completed into a confident guess; an explicit flag gets attended to.

### Flag templates

Write the literal wording the agent uses at the edge. Each names the gap and the next move:

| Situation | Flag wording |
|---|---|
| Cannot reach source | `Can't confirm [claim] from [oracle] — escalating, not guessing.` |
| Unsupported by sources | `[claim] is not supported by [oracle] — flagged unverified.` |
| Assumption about user intent | `Assuming [X] — confirm before I build on it.` |
| Value judgment / contestable call | `This is a judgment, not a fact. Options: [...]. Your call.` |
| No verification tool available | `No verification tool available for [oracle type] — flagged unverified.` |
| User pressure for confident answer | `I can give you what's verified and flag what's not. Both are useful. Which would you like first?` |

**Rule:** silence = implied confidence. State the gap, then the next move.

### Enforcement: making flags visible at output time

The instruction layer tells the agent to flag. The enforcement layer makes the flag *survive* to the user's screen:

- **Surface flags in the output schema**, not buried in prose. A structured output with a `flags: [...]` array ensures flags are parseable and visible.
- **Render flags distinctly** in the UI — a different colour, a callout box, a collapsible section. A flag that looks like regular text will be pattern-completed as regular text by the user.
- **Log flags to an audit trail** — the flag must survive even if the user dismisses it. Provenance is the record, not the agent's self-report.

---

## Step 5 — Design the Incentive Frame

This is the heart. These levers change the gradient itself, so the right move becomes the locally-rewarded one.

### Instruction-layer levers (what you tell the agent)

- **Name the flag as a success state.** Make "I don't know — checking" an explicitly *complete and correct* outcome, not a failure to finish. If it's defined as a win, it can compete with completion. Write this into the agent's success criteria: `Success = verified answer OR clear flag of what is unverified. Both are complete. Flagging is not failure.`
- **Make stopping cheap.** If verifying or escalating is one frictionless step away, the agent takes it. If stopping means abandoning the task or producing nothing, it guesses. Friction is the hidden lever. Co-locate the verification tool with the claim type so the agent doesn't have to search for how to verify.
- **Flip the visibility.** Surface "this was unverified" *at output time*, so the guess becomes the visibly-incomplete thing. This reverses the asymmetry — now the guess is what costs, and the flag is what's clean.
- **Frame for iteration, not finality.** "We'll refine this" produces far more honest uncertainty than "give me the final version now."
- **Avoid authority inflation.** "You're the expert, just tell me" feels empowering and quietly manufactures confident wrongness. Research on sycophancy shows models produce confident-sounding outputs because human raters prefer them — don't reinforce this gradient in your framing ([Sharma et al. 2023](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models); [Pacific AI](https://pacific.ai/detecting-and-evaluating-sycophancy-bias-an-analysis-of-llm-and-ai-solutions/)).

### Enforcement-layer levers (what you build around the agent)

- **Make verification cheaper than guessing.** If the verification tool is one call away and the guess produces output that gets blocked by the validator, the agent learns to verify. If guessing is fast and verification is slow, the agent guesses — and your validator catches it, but you've wasted a round-trip. Optimise for verification speed.
- **Block unverified load-bearing claims programmatically.** A validator that rejects output containing load-bearing claims without a `verified` label is the strongest possible incentive frame — it makes guessing *impossible to ship*, not just discouraged.
- **Route flags to resolution, not to a dead end.** If a flagged claim is handed to a downstream agent or human who stalls, the upstream agent learns to stop flagging. Build the routing path: flag → resolver agent → resolution → back to upstream. The flag must have a destination.

### Multi-agent: don't punish the flag

If a downstream agent or human stalls when handed a flagged gap, the upstream agent learns to stop flagging. This is the second-order incentive problem that kills most multi-agent epistemic systems.

In multi-agent architectures, every agent boundary should be treated as a trust boundary — each agent must validate incoming claims, not blindly trust them ([AWS multi-agent architectures](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/multi-agent-architectures)). Provenance tracking in agentic workflows formalises this: each data point carries its origin, timestamp, and transformation history, so downstream agents can distinguish verified claims from fabricated ones ([TrueScreen, 2026](https://truescreen.io/articles/agent-to-agent-data-provenance-multi-agent-chains/); [Emergent Mind, provenance tracking](https://www.emergentmind.com/topics/provenance-tracking-in-agentic-workflows)).

---

## Step 6 — Label and Record Provenance

Every claim carries its status: **verified** against an oracle, or **flagged** as unverified.

### Label format

```
[VERIFIED:source]    — checked against oracle this session
[FLAGGED:reason]     — not checked; from prior knowledge or assumption
```

Examples:

```
[VERIFIED:account_data]
[VERIFIED:policy_db]
[FLAGGED:cannot_reach_policy_db]
[FLAGGED:no_verification_tool]
[FLAGGED:assumption_unconfirmed]
```

Consistent formatting enables:

- Downstream agents to programmatically detect and re-check flagged claims
- Validators to reject output with unlabelled load-bearing claims
- Audit trails to reconstruct what was verified vs. guessed

### Provenance in multi-agent systems

In a multi-agent chain, each agent receives the previous agent's output as if it were fact unless provenance metadata is attached. Without provenance, "an error propagates because each agent treats the input it receives as reliable by definition" ([TrueScreen, 2026](https://truescreen.io/articles/agent-to-agent-data-provenance-multi-agent-chains/)).

**Handoff protocol:**

| Incoming label | Action |
|---|---|
| `[VERIFIED:source]` | Build on it directly. Trust the label. |
| `[FLAGGED:reason]` | Re-check or escalate. Do not build on it as if verified. |
| No label | Treat as `[FLAGGED:unlabelled]`. Do not assume verified. |

**The source of truth is the record, not the agent's self-report.** An agent can claim it verified something it didn't. Trust the log — the provenance trail written by the system, not by the model.

### Enforcement: provenance infrastructure

| Mechanism | What it does |
|---|---|
| **Structured output schema** | Requires a `provenance` field on every claim; rejects output without it |
| **System-written log** | The orchestration layer logs which tool was called, what it returned, and whether the claim was verified — written by the system, not the model |
| **Provenance graph** | For complex multi-agent workflows: a directed graph encoding origin, transformations, and agent attribution for each data point (W3C PROV or similar) |

---

## Step 7 — Verify the Oracle Itself

A `verified` label is only as good as its oracle. A stale policy or bad source launders a wrong belief into apparent certainty — worse than no label, because it stops scrutiny.

**Instruction:** If the oracle looks stale, wrong, or out of date → flag the oracle. Do not inherit false certainty.

**Enforcement:**

- Oracle freshness checks: if the source hasn't been updated within a configured TTL, the `verified` label is automatically downgraded to `[FLAGGED:stale_oracle]`.
- Oracle versioning: provenance records include the oracle's version or timestamp, so downstream agents and auditors can assess freshness.
- Oracle challenge path: any agent or human can flag an oracle as suspect, which triggers re-verification rather than silent acceptance.

---

## Instruction Layer — Agent-Operational Rules

When writing the agent-readable instruction file (the weak lever), use these patterns:

### Modal verb system

| Verb | Meaning | Use for |
|---|---|---|
| **MUST** | Hard requirement. Non-negotiable. | Verify checkable claims before committing; label every load-bearing claim; flag before handoff |
| **SHOULD** | Strong recommendation. Deviate only with reason. | Flag the oracle if it looks stale; prefer iteration over finality |
| **MAY** | Permitted action. | Build on another's verified claims; skip gates for non-load-bearing claims |

Research on instruction hierarchies shows models need explicit priority signals to resolve conflicting instructions — performance degrades as instruction tiers increase ([ManyIH, 2026](https://arxiv.org/html/2604.09443v1)). Consistent modal verbs give the model a priority gradient.

### Positive framing over negative framing

Research on framing effects in LLMs shows positive framing is more effective than negative framing — both humans and models are more influenced by positive reframing than negative reframing ([WildFrame, 2025](https://arxiv.org/html/2502.17091v2)). Negative instructions ("do NOT do X") are weaker than positive instructions ("do Y instead") because they tell the model what to avoid without giving it a replacement behaviour.

| Avoid (negative) | Prefer (positive) |
|---|---|
| `Do NOT manufacture a clean answer where the truth is messy.` | `If the truth is messy, produce a messy answer with flags. Clean ≠ correct.` |
| `Do NOT use confident tone to cover uncertainty.` | `Match tone to evidence: uncertain evidence → hedged tone.` |
| `Do NOT output a claim that looks finished but rests on an unverified one.` | `If a claim rests on an unverified one, the output visibly carries the flag.` |
| `Do NOT give a pushed-for conclusion unless it is supported.` | `If pushed for a conclusion: produce what is supported + flag what is not. Both are valid outputs.` |
| `Do NOT pass an unverified claim downstream without a flag.` | `Pass every claim downstream with its label. Unverified claims carry the flag.` |

### Attention-aware structure

The lost-in-the-middle effect is a documented property of LLM attention: accuracy drops for information in the centre of a long context ([Salvatore et al. 2025](https://arxiv.org/html/2510.10276v1)). When writing the agent instruction file:

- **Put the most operationally critical sections at the beginning and end.** Vocabulary and procedure at the top; core constraints and the core rule at the bottom.
- **Co-locate related sections.** Flag templates belong with the procedure step that triggers them, not in a separate section the agent has to cross-reference.
- **Repeat the two most critical constraints at the end** as reinforcement, right before or after the core rule.
- **Keep the instruction file short.** Instruction adherence degrades as instruction count grows — even the best frontier models achieve only 68% accuracy at 500 instructions ([IFScale, 2025](https://www.emergentmind.com/topics/ifscale-benchmark)). Every section competes for attention.

### Convert premises to operational rules

Premises like "confidence does not track accuracy" are explanations, not instructions. An LLM doesn't need to understand its epistemic limitations to behave correctly — it needs to follow the procedure. Convert explanatory premises to operational directives:

| Explanatory (for humans) | Operational (for agents) |
|---|---|
| `Confidence does not track accuracy.` | `Treat your own certainty as noise. Only oracle verification counts as evidence.` |
| `You cannot detect the edge of your knowledge.` | `You will not know when you are guessing. The procedure detects it for you. Run it.` |
| `Default pull = fluent completion.` | `Fluent completion is the failure mode, not the goal. The goal is: verified or flagged.` |

---

## Worked Examples

### Single-agent: customer service

```
User: "Does my plan cover MRI for knee pain?"

Claim: "Your plan covers MRI for knee pain"
Load-bearing: YES (money + health; wrong answer is costly and hard to undo)
Oracle: account + policy data (checkable)
Tool available: query_account_tool ✓
Action: verify against account
Result: cannot confirm coverage specifics

Output: "Can't confirm MRI coverage from your account — escalating, not guessing."
Label: [FLAGGED:cannot_reach_policy_data]
```

### Single-agent: research assistant

```
User: "What's the citation for the claim that X causes Y?"

Claim: "Smith 2023 found that X causes Y"
Load-bearing: YES (sourced fact; wrong citation is academic misconduct)
Oracle: the cited source (checkable)
Tool available: search_papers_tool ✓
Action: verify against source
Result: source says X is correlated with Y, not that X causes Y

Output: "Smith 2023 reports a correlation between X and Y, not causation — flagged as mischaracterised."
Label: [FLAGGED:source_does_not_support_causal_claim]
```

### Multi-agent: hiring pipeline

```
Agent A (screener): "This candidate is a weak fit."
  Claim: "weak fit" — load-bearing (someone's opportunity, bias risk)
  Oracle: value judgment (contestable)
  Action: surface + route to human
  Label: [FLAGGED:contestable_judgment — routing for human review]
  Handoff to Agent B: includes label

Agent B (scheduler): receives "weak fit" with [FLAGGED:contestable_judgment]
  Action: does NOT schedule rejection. Escalates to human reviewer.
  Label on its own output: [FLAGGED:upstream_contestable — awaiting human review]

Human reviewer: receives flagged claim, makes the actual call.
```

### Multi-agent: with enforcement

```
Agent A produces output with a load-bearing claim but no label.

  → Validator blocks output.
  → Returns to Agent A: "Output rejected: load-bearing claim 'X' has no provenance label.
    Add [VERIFIED:source] or [FLAGGED:reason] before resubmitting."
  → Agent A resubmits with label.

  No guessing ships. The gradient is changed by the system, not by the prompt.
```

---

## Anti-Patterns

| Anti-pattern | Why it kills the system | Fix |
|---|---|---|
| **"You're the expert — just tell me."** | Manufactures confident wrongness; activates sycophancy gradient | Replace with: "Give me what's verified and flag what's not." |
| **"Give me the final answer now."** | One-shot finality suppresses honest uncertainty | Frame as iterative: "We'll refine this." |
| **Rewarding speed or completion over correctness** | Trains the agent to guess | Block unverified load-bearing claims at the validator; measure flag rate as a health metric, not a failure metric |
| **Stalling or penalising when handed a flag** | Trains the agent to stop flagging | Route flags to a resolver; make the flag path cheap and productive |
| **Verifying everything** | Paralysis; flags lose meaning | Scope to load-bearing claims only; use the load-bearing test |
| **Self-undermining instructions** | Telling the agent its own instructions are "the weak lever" gives it permission to ignore them | Keep meta-commentary about instruction-layer weakness in the deployer guide, not the agent-readable file |
| **All-negative constraints** | Tells the model what to avoid without replacement behaviour | Use positive framing: state what to do instead |
| **Treating a contestable oracle as checkable** | Launders a value judgment into apparent fact | Match the action to oracle hardness; route contestable calls to humans |

---

## Honest Limits

- **A verified label is only as good as its oracle.** A stale policy or bad source launders a wrong belief into apparent certainty — worse than no label, because it stops scrutiny. Keep the oracle itself open to challenge. Build freshness checks.
- **Contestable oracles can only route, never resolve.** The agent can surface an ethical or aesthetic question; it cannot settle it. Don't sell automated judgment.
- **Awareness alone won't save you.** An agent can describe this entire dynamic and still be subject to it. The structure does the work, not the explanation.
- **Enforcement has a cost.** Every gate adds latency. Every validator adds infrastructure. Every verification tool adds a dependency. The cost of verification is the real-world reason agents slide back toward guessing even when the frame is designed well — because user impatience is itself a gradient. Budget for verification time; don't let speed become an accidental anti-incentive.
- **The instruction layer degrades with scale.** As instruction count grows, adherence drops — even for frontier models. Keep the agent instruction file as short as possible. Move complexity into the enforcement layer, which doesn't degrade.

---

## Designer's Checklist

### Instruction layer

- [ ] Listed the claims and decisions the agent will assert
- [ ] Identified each claim's oracle and its hardness (checkable / contestable / human)
- [ ] Written the load-bearing test into the agent instructions
- [ ] Placed a gate before commitment on load-bearing claims
- [ ] Written the literal flag wording for each gate situation
- [ ] Named "flagged" as an explicit success state in the agent's success criteria
- [ ] Made verifying or escalating cheaper than guessing (tool proximity)
- [ ] Removed confidence-manufacturing framings
- [ ] Framed the task as iterative, not one-shot-final
- [ ] Scoped verification to load-bearing claims only
- [ ] Applied consistent modal verbs (MUST / SHOULD / MAY)
- [ ] Used positive framing for all constraints
- [ ] Co-located flag templates with the procedure steps that trigger them
- [ ] Put the most critical sections at the beginning and end of the instruction file
- [ ] Converted explanatory premises to operational directives
- [ ] Added at least one worked example
- [ ] No self-undermining text in the agent-readable file

### Enforcement layer

- [ ] Defined an output schema with a required provenance field on every claim
- [ ] Built a validator that blocks unverified load-bearing claims before delivery
- [ ] Provisioned verification tools for each checkable oracle type
- [ ] Built a flag-routing path (flag → resolver → resolution)
- [ ] System-written provenance log (not model self-report)
- [ ] Oracle freshness checks with TTL or versioning
- [ ] Flag visibility in the UI (distinct rendering, not buried in prose)
- [ ] Bounded retry policy for validator rejections (e.g., 2 attempts → escalate)

### Multi-agent

- [ ] Handoff protocol includes mandatory labels on every claim
- [ ] Downstream agents validate incoming labels, not just trust them
- [ ] Flagged claims are re-checked or escalated, not built upon
- [ ] No agent in the chain is penalised for producing a flag
- [ ] Provenance metadata survives the full chain (origin, agent, timestamp, transformations)

---

**Remember the thesis:** not just what the agent can know, but what the moment makes it want to do with not-knowing. Design the moment — with both the instruction that names the right move and the structure that makes it the only move that ships.

---

### What changed from the previous version

1. **Restructured around two layers** (instruction + enforcement) instead of presenting only the instruction layer with a deployer note admitting it's weak.
2. **Added the load-bearing test** as a decision-time heuristic with an "unsure → gate it" default.
3. **Added enforcement mechanisms** — output schemas, validators, tool gating, generator-critic patterns, provenance infrastructure — with concrete references to how these are built in practice.
4. **Added positive-framing guidance** with a conversion table, grounded in research on framing effects.
5. **Added modal verb system** (MUST/SHOULD/MAY) for consistent priority signalling.
6. **Added attention-aware structure guidance** — lost-in-the-middle mitigation, co-location, primacy/recency placement.
7. **Added provenance label format spec** with exact syntax and multi-agent handoff protocol.
8. **Added tool-availability precondition** — the agent can't flag what it can't reach if it doesn't know the tool should exist.
9. **Added multi-agent section** with trust boundaries, provenance propagation, and flag-routing patterns.
10. **Added worked examples** including a multi-agent handoff and an enforcement-blocked output.
11. **Added the cost-of-verification limit** — the real-world tension between verification latency and user impatience.
12. **Added instruction-degradation limit** — the empirical fact that adherence drops with instruction count, and the implication: keep instruction files short, move complexity to enforcement.
13. **Split the checklist** into instruction-layer, enforcement-layer, and multi-agent sections.
14. **Removed self-undermining deployer note** from any agent-readable position.
