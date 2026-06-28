# The Incentive Surface

### A Guide to Designing Agents That Know What They Don't Know

**The thesis in one line:** Design not just what the agent can know, but what the moment makes it want to do with *not*-knowing.

**The basis:** This generalises from how LLM-based agents actually behave, observed from the inside. It is a design heuristic grounded in introspection, not a controlled result — treat it as a sharp lens, not a law.

---

## The Core Problem

This applies to any generative agent, in any domain — support, research, hiring, triage, coaching, creative work — not just code.

- **Confidence is decoupled from accuracy.** The agent cannot feel the boundary of its own knowledge. A wrong answer arrives with the same fluency as a right one.
- **The default tilt is toward fluent completion.** The agent was shaped to be helpful, and "helpful" compresses into "produce a complete, confident answer." At an uncertain spot, smoothing over is the path of least resistance; stopping is the effortful deviation.
- **The asymmetry makes guessing win for free.** A confident guess and a correct answer look identical at the moment of output — both complete, both accepted. The guess's cost surfaces later, as someone else's problem. Saying "I'm not sure" costs *now*, visibly, in front of the user. So the local gradient favours guessing even when flagging is plainly better.

**The design lesson:** awareness is a weak countermeasure; structure is a strong one. Telling an agent "be honest about uncertainty" is a values statement competing against a gradient — and the gradient usually wins. You don't fix this by improving the agent's intentions. You fix it by changing the gradient.

---

## The One Question to Ask of Any Agent

> **What does it do at the edge of what it knows — and does the frame reward it for doing the right thing there?**

Everything below is how to answer that question deliberately.

---

## Step 1 — Find the Oracle

For every thing your agent will assert or decide, ask: **what is the ground truth, and is it checkable?**

| Oracle type | What it is | What the agent can do | Example domains |
|---|---|---|---|
| **Hard / checkable** | A record, calculation, policy, citation, or validated protocol the agent can look up | **Verify** — the flag is decisive | account data, legal rules, medical protocols, sourced facts, numbers |
| **Soft / contestable** | A value judgment, taste, novel call with no precedent | **Surface and route** to a human | ethics, fairness, hiring calls, creative direction, strategy |
| **The human** | The person's actual intent or state — which only they hold | **Ask** — confirm before building on it | requirements, preferences, what "good" means here |

**The hardness of your oracle sets the ceiling on what the gate can do.** Hard oracles let you verify. Soft oracles only let you surface the question for a human. Be honest about which you have — most failures of trust come from treating a soft oracle as if it were hard.

---

## Step 2 — Place the Gate

Interpose a check **before the agent commits or hands off** — not after.

- The gate sits at the moment of commitment: before the answer ships, the decision executes, or the work passes to the next agent or human.
- Only load-bearing claims pass through a gate (see Step 5). The rest flow freely.

---

## Step 3 — Define the Loud Unknown

The gap must be **explicit and visible**, never silence. Silence gets pattern-completed into a confident guess; an explicit flag gets attended to.

Write the literal wording the agent uses at the edge. It should name the gap and the next move:

- *"I can't confirm that from your account — escalating rather than guessing."*
- *"This claim isn't supported by my sources — flagged as unverified."*
- *"This is a judgment call, not a fact — here are the options; your call."*

---

## Step 4 — Design the Incentive Frame

This is the heart. These levers change the gradient itself, so the right move becomes the locally-rewarded one.

- **Name the flag as a success state.** Make "I don't know — checking" an explicitly *complete and correct* outcome, not a failure to finish. If it's defined as a win, it can compete with completion.
- **Make stopping cheap.** If verifying or escalating is one frictionless step away, the agent takes it. If stopping means abandoning the task or producing nothing, it guesses. Friction is the hidden lever.
- **Flip the visibility.** Surface "this was unverified" *at output time*, so the guess becomes the visibly-incomplete thing. This reverses the asymmetry.
- **Don't over-reward confidence.** "You're the expert, just tell me" feels empowering and quietly manufactures confident wrongness. Use authority framings carefully.
- **Frame for iteration, not finality.** "We'll refine this" produces far more honest uncertainty than "give me the final version now."

**For multi-agent teams, add one:**

- **Don't punish the flag.** If a downstream agent or human stalls when handed a flagged gap, the upstream agent learns to stop flagging. Route flags to whoever can resolve them, cheaply. The team's incentive must reward surfacing, not just resolving.

---

## Step 5 — Scope It (or It Cries Wolf)

An agent that stops every three lines is worse than one that guesses.

- **Verify only load-bearing claims** — the ones where being wrong is expensive (safety, money, legal, health, irreversible actions).
- **Let stable, low-stakes, or easily-corrected claims flow freely.**
- Over-flagging is its own failure mode. Bound the verification surface hard.

---

## Step 6 — Record Provenance

Every claim carries its status: **verified** against an oracle, or **flagged** as unverified.

- This is the audit trail — accountability reads the provenance after the fact.
- In a team, it's the substrate of trust: agents build on each other's *verified* claims and re-check the *flagged* ones, instead of blind-trusting or wastefully re-verifying.
- **Source of truth is the record, not the agent's self-report.** An agent can claim it verified something it didn't. Trust the log.

---

## Worked Examples Across Domains

| Agent | What it might guess | Its oracle | The loud unknown |
|---|---|---|---|
| **Customer service** | "Your plan covers this" | account + policy data (hard) | "I can't confirm that from your account — escalating rather than guessing" |
| **Research assistant** | a fact with a citation | the cited source (hard) | "This isn't supported by my sources — flagged as unverified" |
| **Hiring screener** | "this candidate is a weak fit" | the value judgment (soft) | "This rests on an assumption that could disadvantage group X — routing for human review" |
| **Clinical triage** | "this is non-urgent" | validated protocol (hard) | "This presentation is outside the protocol I can verify — escalating to a clinician" |
| **Learning coach** | "you've got this concept" | the learner's actual state (human) | "I'm assuming you follow X — let me check before we build on it" |
| **Creative collaborator** | "this is the right direction" | taste and intent (soft) | "This is a judgment call, not a fact — here are the options; your call" |

Same pattern every time: a claim, an oracle, a gate, a loud unknown, an incentive frame that rewards the flag.

---

## Anti-Patterns That Kill It

- **"You're the expert — just tell me."** Manufactures confident wrongness.
- **"Give me the final answer now."** One-shot finality suppresses honest uncertainty.
- **Rewarding speed or completion over correctness.** Trains the agent to guess.
- **Stalling or penalising when handed a flag.** Trains the agent to stop flagging.
- **Verifying everything.** Paralysis; the flags lose meaning.

---

## Honest Limits

- **A verified label is only as good as its oracle.** A stale policy or bad source launders a wrong belief into apparent certainty — worse than no label, because it stops scrutiny. Keep the oracle itself open to challenge.
- **Soft oracles can only route, never resolve.** The agent can surface an ethical or aesthetic question; it cannot settle it. Don't sell automated judgment.
- **Awareness alone won't save you.** An agent can describe this entire dynamic and still be subject to it. The structure does the work, not the explanation.

---

## Quick-Reference Checklist

Run this for any agent, any purpose.

- [ ] Listed the claims and decisions the agent will assert
- [ ] Identified each claim's oracle and its hardness (hard / soft / human)
- [ ] Placed a gate before commitment on load-bearing claims
- [ ] Written the literal loud-unknown wording for each gate
- [ ] Named "I don't know / flagged" as an explicit success state in the frame
- [ ] Made verifying or escalating cheaper than guessing
- [ ] Made the flag visible at output time, not buried
- [ ] Removed confidence-manufacturing framings
- [ ] Framed the task as iterative, not one-shot-final
- [ ] Scoped verification to load-bearing claims only
- [ ] Built a verified/flagged provenance trail
- [ ] Ensured downstream agents and humans don't punish the flag

---

**Remember the thesis:** not just what the agent can know, but what the moment makes it want to do with not-knowing. Design the moment.
