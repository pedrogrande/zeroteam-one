<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## The Persona

**Jordan Calloway**
Owner, Clearwater Consulting — a 6-person B2B marketing consultancy

Jordan has been running the business for 7 years. The team handles strategy, content, and campaign management for SME clients. Jordan uses Notion for project management, HubSpot for CRM, Slack for comms, and Xero for accounts — and is comfortable learning new SaaS tools when the value is clear. Jordan has experimented with ChatGPT for drafting content and has a genuine interest in AI but no technical background.

The business is growing faster than the team can comfortably scale. Jordan spends significant time on coordination, reporting, and administrative work that feels like it should be automatable — but every AI tool Jordan has tried either does too little or requires technical setup that feels out of reach.

**Jordan's goal entering this tool:** *"I want AI to help with some of the repetitive work so my team can focus on the client relationships and strategy that actually requires us."*

**Jordan's fear entering this tool:** *"I don't want to set something up incorrectly and have it cause problems with a client or produce something that reflects badly on us."*

***

## Empathy Map

### What Jordan **Sees**

- Competitors talking about AI productivity gains on LinkedIn
- Tool demos that look effortless but feel different in practice
- A dashboard full of integrations, all requiring configuration
- Team members doing repetitive tasks that look the same every week
- Other business owners expressing both excitement and confusion about AI agents
- Enterprise software designed for IT teams, not business owners


### What Jordan **Hears**

- *"You should be using AI for that"* — from peers, without specifics
- *"It's not that complicated"* — from technical people who underestimate the gap
- *"What happens when it gets something wrong?"* — from team members who are wary
- *"We tried something like that and it created more work than it saved"* — from a peer who had a bad experience
- Podcasts and newsletters full of agent jargon that requires translation


### What Jordan **Thinks and Feels**

*Underneath the surface:*

- Quietly unsure whether this is the right time or tool — doesn't want to waste hours on setup only to abandon it
- Anxious about being responsible if an agent sends something wrong to a client
- Slightly embarrassed to admit not knowing what "agent workflow" or "subtask decomposition" means
- Genuinely excited about the idea of reclaiming 5–8 hours a week of coordination time
- Wants to feel competent, not coached — prefers to figure things out independently when the interface makes it possible

*Surface thoughts:*

- *"If I can't explain this to my team in 5 minutes, it won't get adopted"*
- *"I need to understand what it's doing, not just hope it works"*
- *"Is this going to integrate with the tools we already use?"*


### What Jordan **Does**

- Watches 2–3 explainer videos before signing up for anything new
- Starts with the simplest possible use case to test whether something works
- Abandons tools that require more than 15 minutes of setup before delivering any value
- Asks one trusted tech-savvy contact for a second opinion before committing to new software
- Screenshots things that look confusing to ask about later
- Uses browser back button liberally — gets nervous when it doesn't work as expected


### Pains

- Time lost to coordination tasks that feel beneath the team's capability
- Fear of client-facing errors caused by an automated process
- Cognitive overload from learning new tools with no guarantee of payoff
- Jargon that creates distance instead of confidence
- Feeling like the product was designed for a more technical user
- No way to know whether an AI recommendation is trustworthy without understanding how it was made


### Gains

- More time for strategy and client relationships — the work Jordan actually wants to do
- Confidence that the system won't act without appropriate human oversight
- A workflow Jordan can explain to the team and get buy-in for
- The feeling of being ahead, not behind, on AI adoption
- A tool that respects Jordan's judgment rather than overriding it

***

## Work Experience Dimensions

*(From the human work experience map framework)*


| Dimension | Jordan's experience today |
| :-- | :-- |
| **Flow** | During strategy sessions and client presentations — almost never during admin |
| **Drain** | Weekly reporting, meeting coordination, chasing approvals |
| **Meaning** | Client impact, team development, solving interesting business problems |
| **Growth** | Stagnating — most time spent on execution, not learning |
| **Connection** | Strong with long-term clients; weak during high-volume coordination periods |
| **Alienation** | Feels like a project manager rather than a consultant when admin volume peaks |


***

## High-Level User Journey Map

### Stage 0: Arrival and First Impression

**What Jordan is doing:** Landing on the product for the first time, probably after a referral or a short demo video.

**Emotional state:** Cautiously optimistic, slightly evaluative — ready to leave if the first screen feels too complex.


| Moment | Jordan's internal experience | Potential challenge | Design opportunity |
| :-- | :-- | :-- | :-- |
| Landing page | *"Is this for someone like me?"* | Seeing enterprise language or technical diagrams | Lead with an outcome, not a feature list — *"Design how AI helps with your work — without writing a single line of code"* |
| Sign-up | *"How long will this take?"* | Multi-step onboarding forms before any value | Minimal sign-up, immediate entry to task input |
| First screen | *"What am I supposed to do?"* | Blank canvas with too many options | Single focused prompt: *"Describe a task you'd like AI to help with"* |


***

### Stage 1: Task Entry

**What Jordan is doing:** Typing a description of a task — probably something like *"I want to use AI to help prepare our weekly client status reports."*

**Emotional state:** Engaged, slightly uncertain about how much detail to give.


| Moment | Jordan's internal experience | Potential challenge | Design opportunity |
| :-- | :-- | :-- | :-- |
| Writing the description | *"Should I be more specific? Am I saying this right?"* | Over-explaining or under-explaining without knowing which matters | Placeholder text scaffolding — *"Describe the task, who it involves, and what a good outcome looks like"* — without making it feel like a form |
| Seeing the refined description | *"Oh — it understood me better than I expected"* or *"That's not quite right"* | Feeling unable to correct the agent without rewriting everything | Inline edit mode with a clear *"Edit this"* affordance alongside *"Yes, this is correct"* |
| Confirming inferred fields | *"What does 'stakeholder context' mean?"* | Jargon in the inferred field labels | Plain-language labels: instead of `stakeholder_context: external_facing`, show *"Who sees the output? → Clients and external contacts"* |

**Questions Jordan might ask at this stage:**

- *"How do I know if I've given enough information?"*
- *"Can I come back and change this later?"*
- *"Does it matter how I phrase this?"*

***

### Stage 2: Clarification

**What Jordan is doing:** Answering questions one at a time — selecting options, occasionally typing.

**Emotional state:** Engaged if the questions feel relevant; dropping off if they feel generic or too numerous.


| Moment | Jordan's internal experience | Potential challenge | Design opportunity |
| :-- | :-- | :-- | :-- |
| First question | *"Okay, this feels manageable"* | A poorly sequenced first question that feels abstract | Start with the most concrete question — something Jordan knows instinctively, like *"Who will receive this output?"* |
| Mid-way through | *"How many more of these are there?"* | No visibility of progress creates anxiety | Progress bar with category labels: *"You've covered: Context, Success Criteria. Coming up: Failure Modes, Constraints"* |
| A question Jordan can't answer | *"I don't know — is that a problem?"* | Required field on a question Jordan genuinely can't answer | Optional questions marked clearly; a *"Not sure"* option that records uncertainty rather than forcing a guess |
| *"Why is this being asked?"* moment | *"I'm not sure why this matters"* | Questions that feel irrelevant without context | *"Why we ask this"* note under each question — one sentence, not a paragraph |
| End of clarification | *"Did I do that right?"* | No summary or confirmation before moving on | Answer review screen — all answers on one page with edit links before proceeding |

**Questions Jordan might ask at this stage:**

- *"Are these questions specific to my task or the same for everyone?"*
- *"What happens if I answer something wrong?"*
- *"Can I go back and change an answer?"*

***

### Stage 3: Ideal Outcomes

**What Jordan is doing:** Reviewing a list of proposed outcomes and deciding whether they capture what success looks like.

**Emotional state:** Intellectually engaged — this is where Jordan first sees evidence that the system has understood the task. High stakes moment for trust.


| Moment | Jordan's internal experience | Potential challenge | Design opportunity |
| :-- | :-- | :-- | :-- |
| First view of proposed outcomes | *"Yes — that's exactly it"* or *"That's not quite what I meant"* | An outcome that's technically correct but misses the spirit | Show which clarification answers each outcome was derived from — *"Based on your answer about client communication"* |
| Seeing outcome types (primary / secondary / constraint) | *"What's the difference?"* | Label confusion | Inline plain-language explainer on first encounter; persistent tooltip thereafter |
| Reviewing input/output templates | *"What is this for?"* | Templates feeling technical and abstract | Frame templates as *"What does this need?"* and *"What will it produce?"* rather than schema language |
| Editing a template | *"I'm not sure I'm doing this right"* | Field builder feeling like a developer tool | Guided field-by-field form with examples per field type; *"Add a field"* button rather than raw JSON |
| Gap identification prompt | *"Actually, yes — there's something missing"* | Prompt being skippable or easy to overlook | Full-screen modal before proceeding: *"Before you continue — is there anything this task needs to achieve that isn't listed?"* |

**Questions Jordan might ask at this stage:**

- *"What happens if I get the template wrong?"*
- *"Can I add something the agent didn't think of?"*
- *"Does it matter if some of these are rejected?"*

***

### Stage 4: Risk Identification

**What Jordan is doing:** Reviewing a ranked list of risks and adjusting scores where the agent's calibration doesn't match Jordan's knowledge of the context.

**Emotional state:** This is the stage most likely to either build deep trust or create anxiety. Seeing risks clearly articulated is reassuring. Seeing irreversibility warnings is sobering — in a good way if handled well, in a bad way if handled clumsily.


| Moment | Jordan's internal experience | Potential challenge | Design opportunity |
| :-- | :-- | :-- | :-- |
| First view of the risk list | *"I hadn't thought about some of these"* | A long list feeling overwhelming | Show top 5 by composite score first; expand to full list below the fold |
| Understanding axis scores | *"What does a 7 for severity mean?"* | Score numbers without reference points | Plain-language calibration anchors for 1, 5, and 10 on each axis — *"10 = cannot be undone under any circumstances"* |
| Adjusting a score | *"I know this is lower risk than the agent thinks"* | No record of why the adjustment was made | Score adjustment requires selecting a reason from a short list — builds the calibration improvement loop while making Jordan feel heard |
| Seeing an irreversibility warning | *"Wait — what does that mean for how this gets set up?"* | Warning appearing without forward-looking context | Irreversibility warning includes a plain-language preview of what it means downstream: *"A human approval step will be added before this action runs"* |
| Adding a risk | *"There's a specific thing I know about our clients that the agent doesn't"* | Addition form being too open-ended | Structured addition form with category dropdown and a *"What would have to go wrong?"* prompt |

**Questions Jordan might ask at this stage:**

- *"Are these risks specific to my task or standard ones?"*
- *"What does the system do with these risks?"*
- *"Does a high risk score mean I shouldn't automate this?"*

***

### Stage 5: Decomposition and Executor Recommendations

**What Jordan is doing:** Reviewing each subtask with its executor recommendation, understanding which steps will be human-owned vs. agent-owned, and approving the full design.

**Emotional state:** This is the highest-cognitive-load stage. Jordan is forming a mental model of how the system will work. It is also the stage where the value of the whole process becomes tangible — or where it falls apart if the recommendations feel wrong or unexplained.


| Moment | Jordan's internal experience | Potential challenge | Design opportunity |
| :-- | :-- | :-- | :-- |
| First view of decomposition | *"Oh — so this is how it breaks down"* | A long flat list without visual structure | Show the workflow as a sequence — numbered cards in order with visual connectors — so it reads as a process, not a table |
| Seeing executor recommendations | *"Why is this one human and not agent?"* | Recommendation without rationale feeling arbitrary | Rationale always visible — not collapsed — on every subtask card |
| Seeing a human gate | *"What does that mean for me in practice?"* | Gate flag without operational context | Plain-language description: *"You will receive a notification and need to approve before this step runs"* |
| Seeing friction classification | *"What is 'productive friction'?"* | New term without grounding | On first encounter, show a brief inline definition with a real example from the task |
| Disagreeing with an executor recommendation | *"Actually, I want a human to do this one"* | Override feeling like overriding the whole system | Override is frictionless but records reason — *"Why are you changing this?"* with a short option list |
| Approving the full design | *"Is this really done? Did I do it right?"* | Approval feeling anticlimactic without a sense of completion | Final summary screen designed as a document, not a confirmation dialog — shareable, printable, meaningful |

**Questions Jordan might ask at this stage:**

- *"How do I know this is the right way to divide this up?"*
- *"What happens next — how does this become actual agents?"*
- *"Can I change any of this after I approve it?"*

***

## Emotional Journey Summary

```
Stage 1   Stage 2        Stage 3        Stage 4        Stage 5
  │          │              │              │              │
  ▲          ▲              ▲              ▲              ▲
  │ Curious  │ Engaged      │ Trust        │ Sobered/     │ Ownership
  │          │ or dropping  │ building     │ Reassured    │ + Relief
  │          │ off          │              │              │
──┼──────────┼──────────────┼──────────────┼──────────────┼──────────
  │          │              │              │              │
  ▼          ▼              ▼              ▼              ▼
  Uncertain  Overwhelmed    Confused by    Anxious at     Confused
  about      by question    templates or   irreversibility about
  how much   volume or      jargon         warnings       "what
  to say     irrelevance                                  happens next"
```

The two highest-risk drop-off points are the **mid-clarification fatigue zone** and the **first view of decomposition**. The two highest-trust-building moments are **seeing a well-understood refined description** and **the final summary document**. The design should invest disproportionately in those four moments.

