<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## The Experience Vision

### What We Hope Jordan Thinks

- *"This was designed for someone like me"* — not a developer, not an enterprise IT team, but a business owner who knows their work deeply and just needs a system that meets them there
- *"I understand what's been decided and why"* — not blind trust in a black box, but genuine comprehension of the logic behind every recommendation
- *"I could explain this to my team in ten minutes"* — the output is legible to people who weren't in the room
- *"I caught something the system would have missed"* — at least once per session, Jordan's knowledge of their specific context improved the analysis in a way that matters
- *"I know where I am and what comes next"* — never disoriented, never wondering whether progress is being saved


### What We Hope Jordan Feels

- **Competent, not coached** — the experience respects that Jordan is an expert in their own business; the system is the novice being brought up to speed, not the other way around
- **Cautiously trusting** — trust that has been earned through transparency, not assumed through confidence; Jordan can see the reasoning and therefore extend genuine trust rather than reluctant compliance
- **Appropriately slowed down** — particularly at risk and gate decisions, Jordan should feel the system is helping them think more carefully, not rushing them toward a conclusion
- **Ownership of the output** — the final design document should feel like *Jordan's* design, not something the system produced and Jordan approved; the editing, confirming, and adding throughout the process creates genuine authorship
- **Relieved at the end** — not just satisfied, but specifically relieved that the complexity of the decision has been handled carefully and the result is something Jordan can stand behind


### What We Hope Jordan Does

- **Edits at least one thing in every session** — if Jordan never edits, it means either the system is perfect (impossible) or Jordan is not genuinely engaging. We design to invite editing, not to avoid it.
- **Adds at least one outcome or risk the system missed** — this is the signal that Jordan's domain knowledge is being activated, not bypassed. It is also the system's primary learning mechanism.
- **Returns with a second task within two weeks** — the experience should create enough confidence and enough tangible value that the next task feels lower-friction than the first
- **Shares the session summary with someone** — if Jordan sends the output document to a team member, a developer, or a trusted advisor, the design has succeeded at legibility and trust simultaneously
- **Adjusts a risk score with a reason** — this is the highest-value behavioural signal in the system. It means Jordan engaged with the scoring logic, applied their contextual knowledge, and contributed to calibration improvement


### What Jordan Does That Helps Us Improve

Every behaviour we hope for is also a signal:


| Jordan's behaviour | What it tells the system |
| :-- | :-- |
| Edits the refined description | Which inferences the Session Agent gets wrong by domain or task type |
| Selects "Something else" on any screen | Which options are missing from the library |
| Adds an outcome the agent didn't propose | Which outcome types are systematically underrepresented |
| Adjusts a risk score | Which domains have miscalibrated default scores |
| Rejects an agent-generated outcome or risk | Which proposals are off-target for this task type |
| Changes an executor recommendation | Which subtask types the scoring model gets wrong |
| Abandons the session at a specific stage | Where cognitive load or confusion peaks |
| Completes in under 8 minutes with no edits | Whether the session is too short to be driving genuine engagement |
| Returns to a previous screen | Where the sequence creates confusion or second-guessing |

The system never asks Jordan for feedback. It reads what Jordan *does* as the feedback.

***

## Stage 1 Simulation — Customer Complaint Handling

### Step 1.1 — Jordan's Path Through the Cards

**Screen 1 — Category**

Jordan scans the six category cards. None of them quite fit — complaint handling is part communication, part process, part judgment. Jordan considers **Client Communication** for a moment, then taps it. The builder strip begins:

> *"Handling client or customer communication..."*

**Screen 2 — Audience**

> *"Who receives the output from this work?"*

Jordan immediately selects **My clients or customers**. Builder strip:

> *"Handling client communication... for clients or customers..."*

**Screen 3 — Frequency**

> *"How often does this task happen?"*

Jordan pauses. Complaints don't come on a schedule. Taps **It varies**.

Builder strip:

> *"Handling variable-frequency client communication..."*

**Screen 4 — What Makes It Hard**

Jordan selects:

- **It takes too long**
- **It depends too much on one person** *(right now only Jordan handles complaints)*
- **Something else →** inline field opens

Jordan types:
> *"Every complaint is different and the tone and response really matters — one wrong response can damage the relationship"*

Builder strip:

> *"Variable-frequency client communication... currently slow, person-dependent, and requiring careful judgment on tone and relationship management..."*

**Screen 5 — What Would Concern You**

Jordan selects:

- **Errors or inaccuracies in the output**
- **It not sounding like us**
- **How clients or stakeholders would react**

Then pauses — and also selects **Not knowing what it's doing or why**. Four concerns total.

Builder strip:

> *"Variable client communication requiring judgment... with significant concern around accuracy, brand voice, client reaction, and maintaining visibility over what AI does."*

***

### Step 1.2 — System Processing

**Validation result:** Pass — input rich enough to proceed

**Record created:**

```
TaskSession
  raw_description: [assembled from selections + Jordan's free text]
  status: clarifying
  domain: null
  stakeholder_context: null
  risk_tolerance: null
```

**System event emitted:** `session_created`

***

### Step 1.3 — Session Agent Processing

**Agent reasoning trace (internal):**

- Domain signals: "complaint", "tone", "relationship", "response" → customer relationship management; emotionally loaded work category
- Stakeholder signals: "clients or customers", "how clients react" → external-facing; high relationship sensitivity
- Risk signals: four concerns selected including visibility and client reaction; free text explicitly named relationship damage and tone judgment → this is not low-stakes automation; user is anxious about AI acting without oversight
- Risk tolerance: highest concern count seen in Stage 1 so far; free text contains explicit risk articulation before any benefit mentioned → inferred as `very_low`
- Friction signals: "every complaint is different" → this task has high variability; "tone and relationship matters" → significant productive friction present; this is not purely an unproductive friction target
- Critical distinction from the reports task: this task involves **reactive, variable, emotionally sensitive** interactions rather than **scheduled, structured, neutral** ones — the executor profile will be substantially more human-weighted

***

### Step 1.4 — Session Agent Output

**Refined description produced:**

> "Improve the handling of inbound customer complaints — currently managed by a single person, time-consuming, and requiring careful judgment on tone, relationship sensitivity, and appropriate resolution. Every complaint differs in nature and stakes. The goal is to reduce response time, ensure consistent quality, and scale capacity without losing the human judgment and brand voice that protects client relationships. Visibility and control over what AI does at each step is an explicit requirement."

**Inferred fields:**

```
domain: "customer_relationship_management"
stakeholder_context: "external_facing"
risk_tolerance: "very_low"
```

**Rationale stored:**

- Domain: complaint handling, tone management, relationship sensitivity, variable response type
- Stakeholder context: outputs are direct client communications; relationship is at stake in each interaction
- Risk tolerance: four concerns raised including explicit visibility requirement; free text named relationship damage; no benefit mentioned before a risk — this is a user who needs to feel in control before they will trust any automation

***

### Step 1.5 — Jordan Reviews the Refined Description

**The description chips:**

```
[Improve the handling of inbound customer complaints] — currently managed
by [a single person] and [requiring careful judgment on tone, relationship
sensitivity, and appropriate resolution]. [Every complaint differs in
nature and stakes]. The goal is to [reduce response time] and
[ensure consistent quality], while [retaining the human judgment and
brand voice] that protects client relationships. [Visibility and control
over what AI does] is an explicit requirement.
```

Jordan reads carefully. More carefully than the reports description. Two edits:

**Chip 1:** Jordan taps **[a single person]**
Alternative options shown:

- *"One team member"*
- *"Me personally"*
- *"Our customer service team"*
- *"Describe it differently →"*

Jordan selects **"Me personally"**. *(This is a signal: Jordan is the complaint handler. Executor recommendations should weight this — Jordan has the relationship knowledge that no team member can substitute.)*

**Chip 2:** Jordan taps **[Visibility and control over what AI does]**
Alternative options shown:

- *"Being able to review AI actions before they happen"*
- *"Understanding what AI is doing at each step"*
- *"Being notified before anything is sent to a client"*
- *"Describe it differently →"*

Jordan selects **"Being notified before anything is sent to a client"**. *(This is a critical structural signal: Jordan is explicitly stating that no output should reach a client without human review. This is an irreversibility gate requirement, stated by the user before Stage 4 has even begun.)*

**Updated description:**

> "Improve the handling of inbound customer complaints — currently managed by me personally, time-consuming, and requiring careful judgment on tone, relationship sensitivity, and appropriate resolution. Every complaint differs in nature and stakes. The goal is to reduce response time and ensure consistent quality, while retaining the human judgment and brand voice that protects client relationships. I need to be notified before anything is sent to a client."

***

### Step 1.6 — Inferred Field Confirmation

**Card 1 — Type of work:**
> Customer relationship management
**[That's right]** — Jordan confirms

**Card 2 — Who sees the output:**
> Clients and external contacts — this output leaves the business
**[That's right]** — Jordan confirms

**Card 3 — How much does getting this right matter:**
> Very high — errors could seriously damage client relationships
**[That's right]** — Jordan confirms without hesitation. *(Different from the reports task, where the option was "High". The system has surfaced a `very_low` risk tolerance which maps to a more emphatic label. Jordan's immediate confirmation validates the inference.)*

***

### Step 1.7 — System Output

**Session record:**

```
TaskSession
  refined_description: [Jordan's edited version]
  domain: "customer_relationship_management"
  stakeholder_context: "external_facing"
  risk_tolerance: "very_low"
  status: clarifying (locked)
```

**Critical signals recorded for downstream agents:**

```
user_explicit_gate_requirement: true
gate_trigger: "before_client_delivery"
executor_bias: "human_weighted"
variability: "high"
productive_friction_present: true
primary_executor_is_owner: true
```

**Audit events written:** session created, refinement confirmed, two chip edits recorded, fields confirmed, stage complete

***

## Comparing the Two Task Profiles

Running the simulation twice makes the contrast concrete:


| Dimension | Weekly Reports | Customer Complaints |
| :-- | :-- | :-- |
| Cadence | Scheduled, predictable | Variable, reactive |
| Variability | Low — same structure weekly | High — every instance differs |
| Emotional content | Neutral | High — relationship at stake |
| Risk tolerance inferred | Low | Very low |
| Productive friction | Low — mostly aggregation | High — judgment is the work |
| Executor profile | Agent-heavy | Human-heavy |
| Gate requirement | Implicit (Friday review exists) | Explicit — stated by Jordan |
| Concerns raised | 2 | 4 |
| Chip edits in Stage 1 | 1 | 2, both structurally significant |

### UX Improvement Opportunities These Differences Surface

**1. The category card system is undersized**
Jordan almost chose the wrong category for complaints. *Client Communication* was close but not right. A task that is reactive, judgment-intensive, and emotionally sensitive doesn't fit neatly into any of the six categories. The categories need a second dimension — not more cards, but a follow-up question:

> *"Is this task more about producing a consistent output or handling situations that each require individual judgment?"*

This single branch question changes the entire downstream profile and would have surfaced the productive friction signal earlier.

**2. Frequency is a proxy for variability, and they're not the same**
"It varies" was the closest option for complaints, but what Jordan meant was unpredictable and each instance is unique — not just variable in timing. A task that happens unpredictably is architecturally different from a task that happens on a flexible schedule. The frequency question should split into:

> *"How often does this happen?"* → cadence
> *"How similar are the instances to each other?"* → variability

Variability is one of the most important signals for executor recommendation. It should be captured explicitly, not inferred from frequency.

**3. Explicit gate requirements emerge in Stage 1 — the system should receive and record them**
Jordan's chip edit — *"Being notified before anything is sent to a client"* — was a direct statement of a structural gate requirement. The current design captures this as a text edit inside a refined description, but it should be treated as a first-class signal, not a prose edit.

When a chip edit amounts to *"I need a human in the loop before X"*, the system should recognise this pattern and create a preliminary gate record that pre-populates Stage 5, rather than burying it in the description text.

**4. Risk tolerance needs more granularity at the high end**
The reports task mapped to `low` and the complaints task to `very_low` — but in practice these require meaningfully different architectures. A `low` risk tolerance might mean "review before sending." A `very_low` risk tolerance means "I need to write the final response myself — AI can only draft." The confirmation card for this field should offer a brief elaboration at the high end:

> *"Very high — I need to approve every output before it reaches anyone"*
> *"Critical — AI can assist but I will always make the final decision"*

This gives the decomposition agent the signal it needs to recommend human-owned execution rather than human-gated agent execution — a distinction that matters enormously for the final system design.

**5. The task profile should become visible to Jordan**
By the end of Stage 1, the system has inferred a rich profile that will shape every downstream recommendation. Jordan doesn't see this. Making it briefly visible — not as data, but as a plain-language characterisation — would build trust and invite correction:

> *"This looks like a high-judgment, variable task where AI is best used as a support to your decision-making rather than as an autonomous processor. Does that sound right?"*

**[Yes, that's it]** **[Not quite →]**

This one confirmation card would catch profile mismatches before they propagate through four more stages — and would make Jordan feel seen rather than processed.

