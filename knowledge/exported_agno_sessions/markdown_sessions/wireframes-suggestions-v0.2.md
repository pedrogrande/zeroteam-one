<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Create ascii wireframes for your recommended design upgrade flow.

All 9 screens generated. Here they are in sequence, each annotated with the upgrades it demonstrates.

***

## Upgrade Key

```
①  Design brief metaphor      ⑤  Confidence indicators on inferences
②  Understanding-based progress  ⑥  Done for now / save & come back later
③  Assertion cards            ⑦  This will matter later marker
④  Session warmth indicators
```


***

## Screen 1 — The Opening Brief *(initial)*

`① ② ⑥`

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │  ← ⑥
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  —                                                   │  ← ②
│  Still building:  task type · audience · timing · difficulty · concerns  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  You're writing a brief for your agent team.                             │  ← ①
│  Each section shapes what agents handle, what they escalate,             │
│  and where you stay in control.                                          │
│                                                                            │
│  Start with the type of work.                                            │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📊  Reporting &       │   │  ✉   Client             │                │
│  │      Summaries         │   │      Communication      │                │
│  │                        │   │                         │                │
│  │  Pulling together      │   │  Handling messages,     │                │
│  │  updates into a        │   │  responses or updates   │                │
│  │  regular output        │   │  to or from clients     │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📋  Coordination &    │   │  🔍  Research &         │                │
│  │      Planning          │   │      Analysis           │                │
│  │                        │   │                         │                │
│  │  Managing tasks,       │   │  Gathering or           │                │
│  │  schedules, handoffs   │   │  synthesising info      │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📝  Content           │   │  ⚙   Process &          │                │
│  │      Creation          │   │      Operations         │                │
│  │                        │   │                         │                │
│  │  Writing materials     │   │  Recurring workflows    │                │
│  │  for any audience      │   │  and operational tasks  │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  Or describe it in your own words:                                       │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│                                              ░░░[ Continue → ]░░░        │
│                                              (select an option above)    │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 1b — Category Selected

`② ④`

The warmth note appears immediately on selection, in a bordered strip that slides in below the progress line. The selected card takes the double-border treatment. Unselected cards visually recede.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓                                         │  ← ②
│  Still building:  audience · timing · difficulty · concerns             │
├──────────────────────────────────────────────────────────────────────────┤
│  ✦ Good start — reporting tasks have well-established automation         │  ← ④
│    patterns. We'll use this to shape which questions matter most.        │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Start with the type of work.                                            │
│                                                                            │
│  ╔════════════════════════╗   ┌────────────────────────┐                │
│  ║  📊  Reporting &    ✓  ║   │  ✉   Client             │                │
│  ║      Summaries         ║   │      Communication      │                │
│  ║                        ║   │                         │                │
│  ║  Pulling together      ║   │  Handling messages,     │                │
│  ║  updates into a        ║   │  responses or updates   │                │
│  ║  regular output        ║   │  to or from clients     │                │
│  ╚════════════════════════╝   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📋  Coordination ...  │   │  🔍  Research ...       │                │
│  └────────────────────────┘   └────────────────────────┘                │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📝  Content ...       │   │  ⚙   Process ...        │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  Or describe it in your own words:                                       │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│                                                    [ Continue → ]        │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 2 — Audience

`③ ⑤ ⑦`

The biggest structural change from the baseline design. A question has become an **assertion card**: the system states what it believes, explains why, and asks Jordan to confirm or correct. The `▓▓▓▓░░ Medium` confidence indicator tells Jordan exactly how certain the system is, so they know whether to trust the claim or inspect it.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓                                         │
│  Still building:  audience · timing · difficulty · concerns             │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Who receives the output from this work?                                 │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  We think →  Clients or external contacts                        │   │  ← ③
│  │  ─────────────────────────────────────  ▓▓▓▓░░  Medium          │   │  ← ⑤
│  │  Your description mentioned sending reports to clients.          │   │
│  │                                                                  │   │
│  │  [ ✓ That's right ]                                             │   │
│  │                                                                  │   │
│  │  Or select a different answer:                                   │   │
│  │  ┌──────────────────────┐   ┌──────────────────────┐           │   │
│  │  │  👥  My team only    │   │  🏢  Leadership or   │           │   │
│  │  │                      │   │      Management       │           │   │
│  │  └──────────────────────┘   └──────────────────────┘           │   │
│  │  ┌──────────────────────┐                                       │   │
│  │  │  🌐  Mixed — both    │                                       │   │
│  │  └──────────────────────┘                                       │   │
│  │                                                                  │   │
│  │  Or describe the audience in your own words:                    │   │
│  │  ┌──────────────────────────────────────────────────────────┐  │   │
│  │  │                                                          │  │   │
│  │  └──────────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ⚑ Client-facing output will shape your risk and gate design later       │  ← ⑦
│                                                                            │
│  ◀ Back                                              [ Continue → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 2b — Audience Confirmed, Frequency Asserted

`③ ④ ⑤`

Jordan taps `[ ✓ That's right ]`. The assertion card collapses with a confirmation tick, a warmth note appears, and the next assertion card renders immediately below — keeping the entire interaction on a single surface.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓  audience ✓                             │
│  Still building:  timing · difficulty · concerns                        │
├──────────────────────────────────────────────────────────────────────────┤
│  ✦ Noted — client-facing outputs get extra care in the risk design.      │  ← ④
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  How often does this task happen?                                        │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  We think →  Weekly                                              │   │  ← ③
│  │  ─────────────────────────────────────  ▓▓▓▓▓░  High            │   │  ← ⑤
│  │  You mentioned "weekly" in your description.                     │   │
│  │                                                                  │   │
│  │  [ ✓ That's right ]                                             │   │
│  │                                                                  │   │
│  │  Or select a different answer:                                   │   │
│  │  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐        │   │
│  │  │  📅  Daily   │   │  🗓  Monthly  │   │  🔁  Varies  │        │   │
│  │  └──────────────┘   └──────────────┘   └──────────────┘        │   │
│  │  ┌──────────────┐                                               │   │
│  │  │  1  One-time │                                               │   │
│  │  └──────────────┘                                               │   │
│  │                                                                  │   │
│  │  Or describe the frequency in your own words:                   │   │
│  │  ┌──────────────────────────────────────────────────────────┐  │   │
│  │  │                                                          │  │   │
│  │  └──────────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                              [ Continue → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 4 — Pain Points

`⑦ ②`

The `⚑` marker appears **below the card** once it's selected — not before, so it doesn't prime Jordan's choices. It reads as a consequence acknowledgment, not a nudge.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓  audience ✓  timing ✓                  │
│  Still building:  difficulty · concerns                                 │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  What makes doing this manually difficult?  Select all that apply.      │
│                                                                            │
│  ╔════════════════════════╗   ╔════════════════════════╗                │
│  ║  ⏱  It takes too    ✓  ║   ║  🔄  Results are     ✓  ║                │
│  ║     long               ║   ║      inconsistent       ║                │
│  ║                        ║   ║                         ║                │
│  ║  A meaningful amount   ║   ║  Output varies by       ║                │
│  ║  of time each cycle    ║   ║  who does it            ║                │
│  ╚════════════════════════╝   ╚════════════════════════╝                │
│  ⚑ Shapes the agent's scope   ⚑ Affects the output spec                 │  ← ⑦
│                                                                            │
│  ╔════════════════════════╗   ┌────────────────────────┐                │
│  ║  🗄  Multiple       ✓  ║   │  😓  Repetitive work    │                │
│  ║     sources            ║   │                         │                │
│  ║                        ║   │  Same steps each time,  │                │
│  ║  Pulling data from     ║   │  little variation       │                │
│  ║  several tools         ║   │                         │                │
│  ╚════════════════════════╝   └────────────────────────┘                │
│  ⚑ Shapes data integration design                                        │  ← ⑦
│                                                                            │
│  ┌────────────────────────┐                                              │
│  │  👤  Depends on one    │                                              │
│  │      person            │                                              │
│  └────────────────────────┘                                              │
│                                                                            │
│  Or describe what else makes it difficult:                               │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                              [ Continue → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 5 — Concerns

`④ ⑦ ②`

The warmth note here is the most substantively meaningful one in the flow — it names a *consequence* (a human review step), not just an acknowledgement. Jordan learns something about what the system will do with their answer.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓  audience ✓  timing ✓  difficulty ✓   │
│  Still building:  concerns                                              │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  If AI handled this, what would concern you?  Select all that apply.    │
│                                                                            │
│  ╔════════════════════════╗   ╔════════════════════════╗                │
│  ║  ✗  Errors or       ✓  ║   ║  🎨  Not sounding    ✓  ║                │
│  ║     inaccuracies       ║   ║      like us            ║                │
│  ║                        ║   ║                         ║                │
│  ║  Wrong information     ║   ║  Output doesn't match   ║                │
│  ║  reaching clients      ║   ║  our voice or style     ║                │
│  ╚════════════════════════╝   ╚════════════════════════╝                │
│  ⚑ Drives your verification design                                       │  ← ⑦
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  👁  Not knowing       │   │  🔒  Data privacy       │                │
│  │     what it's doing    │   │                         │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  💬  Client reaction   │   │  ✓  Not particularly   │                │
│  │                        │   │     concerned           │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ✦ Good to know — accuracy concerns add a human review step before       │  ← ④
│    anything reaches a client.                                            │
│                                                                            │
│  Or describe any other concerns:                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                              [ Continue → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 6 — Draft Brief Assertions

`③ ⑤ ②`

This is the most transformed screen. Each inference is a numbered, titled, individually-confirming assertion card. Confidence indicators are prominent — Jordan can skip High-confidence cards quickly and focus attention on Medium and Low cards where the system is genuinely less certain. Card 4 carries a `⚠` warning beside its Low indicator.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓  audience ✓  timing ✓  difficulty ✓   │
│                      concerns ✓  — now reviewing your draft brief       │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Here's our draft brief. Confirm or correct each statement.             │
│                                                                            │
│  ╔══════════════════════════════════════════════════════════════════╗   │
│  ║  1 · The primary goal                    ▓▓▓▓▓░  High           ║   │  ← ⑤
│  ║  ──────────────────────────────────────────────────────────────  ║   │
│  ║  Automate the weekly client status report workflow to reduce     ║   │  ← ③
│  ║  time and improve consistency across reports                     ║   │
│  ║                                                                  ║   │
│  ║  [ ✓ Confirmed ]     [ Needs adjusting → ]                      ║   │
│  ║                                                                  ║   │
│  ║  Or describe it more precisely:                                  ║   │
│  ║  ┌──────────────────────────────────────────────────────────┐   ║   │
│  ║  │                                                          │   ║   │
│  ║  └──────────────────────────────────────────────────────────┘   ║   │
│  ╚══════════════════════════════════════════════════════════════════╝   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  2 · How it works today                  ▓▓▓░░░  Medium         │   │  ← ⑤
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  A team member spends approximately half a day each Friday       │   │
│  │  aggregating updates from multiple tools and sources             │   │
│  │                                                                  │   │
│  │  [ ✓ Confirmed ]     [ Needs adjusting → ]                      │   │
│  │                                                                  │   │
│  │  Or describe it more precisely:                                  │   │
│  │  ┌──────────────────────────────────────────────────────────┐   │   │
│  │  │                                                          │   │   │
│  │  └──────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  3 · What the output looks like          ▓▓▓▓░░  Medium         │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  A written summary per client — accurate, on-brand, and ready   │   │
│  │  for direct client delivery                                      │   │
│  │                                                                  │   │
│  │  [ ✓ Confirmed ]     [ Needs adjusting → ]                      │   │
│  │                                                                  │   │
│  │  Or describe it more precisely:                                  │   │
│  │  ┌──────────────────────────────────────────────────────────┐   │   │
│  │  │                                                          │   │   │
│  │  └──────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  4 · The review step                     ▓▓░░░░  Low  ⚠         │   │  ← ⑤
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  Reports are reviewed before sending — likely by the owner on   │   │
│  │  Friday before Monday delivery                                   │   │
│  │                                                                  │   │
│  │  ⚠  We're less certain here — please check this carefully       │   │
│  │                                                                  │   │
│  │  [ ✓ Confirmed ]     [ Needs adjusting → ]                      │   │
│  │                                                                  │   │
│  │  Or describe it more precisely:                                  │   │
│  │  ┌──────────────────────────────────────────────────────────┐   │   │
│  │  │                                                          │   │   │
│  │  └──────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                      [ This looks right → ]     │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 6b — One Assertion Being Corrected

`③ ④`

Jordan taps `[ Needs adjusting → ]` on card 2. The card expands inline. Options and textarea are both immediately visible. No extra click needed to reach the textarea. When Jordan submits, a warmth note acknowledges the specific correction.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Here's our draft brief. Confirm or correct each statement.             │
│                                                                            │
│  ╔══════════════════════════════════════════════════════════════════╗   │
│  ║  1 · The primary goal                    ▓▓▓▓▓░  High      ✓   ║   │
│  ║  Automate the weekly client status report workflow               ║   │
│  ╚══════════════════════════════════════════════════════════════════╝   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  2 · How it works today                  ▓▓▓░░░  Medium         │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  "A team member spends approximately half a day each Friday"     │   │
│  │                                           ← adjusting this      │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  What's closest?                                                 │   │
│  │                                                                  │   │
│  │  [ Me personally — not a team member              ]             │   │
│  │  [ Half a day on Fridays, sent Monday morning     ]             │   │
│  │  [ More than half a day — most of the day         ]             │   │
│  │  [ Less than half a day — under 2 hours           ]             │   │
│  │                                                                  │   │
│  │  Or describe what actually happens:                             │   │
│  │  ┌──────────────────────────────────────────────────────────┐  │   │
│  │  │ half a day on Fridays — reports are sent Monday morning  │  │   │
│  │  │ after I review them                                      │  │   │
│  │  └──────────────────────────────────────────────────────────┘  │   │
│  │                                          [ Update this ✓ ]     │   │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  3 · What the output looks like          ▓▓▓▓░░  Medium         │   │
│  │  A written summary per client, accurate and on-brand            │   │
│  │  [ ✓ Confirmed ]    [ Needs adjusting → ]                       │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  4 · The review step                     ▓▓░░░░  Low  ⚠         │   │
│  │  Reports reviewed before sending — likely by the owner          │   │
│  │  [ ✓ Confirmed ]    [ Needs adjusting → ]                       │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                      [ This looks right → ]     │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 7 — Final Checks

`⑤ ⑦ ⑥`

Card 1 is already confirmed (double-border treatment). Cards 2 and 3 remain open. The Low-confidence card carries both the `⚠` flag and a `⚑` consequence marker — it's the most consequential card on the screen and deserves the most attention. Continue stays inactive until all three are actioned.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Understood so far:  task type ✓  audience ✓  timing ✓  difficulty ✓   │
│                      concerns ✓  draft brief ✓                          │
│  Now: three final checks before we build your brief                     │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Before we design your agent team, confirm these three things.          │
│                                                                            │
│  ╔══════════════════════════════════════════════════════════════════╗   │
│  ║  What type of work is this?              ▓▓▓▓▓░  High      ✓   ║   │  ← ⑤
│  ║  ──────────────────────────────────────────────────────────────  ║   │
│  ║  Client services and operations                                  ║   │
│  ╚══════════════════════════════════════════════════════════════════╝   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Who sees the final output?              ▓▓▓▓▓░  High           │   │  ← ⑤
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  Clients and external contacts                                   │   │
│  │  ⚑ Shapes your human gate placement                             │   │  ← ⑦
│  │                                                                  │   │
│  │  [ ✓ That's right ]  [ Internal only ]  [ Mixed — both ]       │   │
│  │                                                                  │   │
│  │  Or describe it in your own words:                              │   │
│  │  ┌──────────────────────────────────────────────────────────┐  │   │
│  │  │                                                          │  │   │
│  │  └──────────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  How much does getting this right matter?  ▓▓░░░░  Low  ⚠       │   │  ← ⑤
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  High — errors would affect client relationships                 │   │
│  │                                                                  │   │
│  │  ⚠  We're less certain here — please check this carefully       │   │
│  │  ⚑ Directly sets your risk threshold and gate frequency        │   │  ← ⑦
│  │                                                                  │   │
│  │  [ ✓ That's right ]  [ Low — easy to fix ]  [ Medium ]         │   │
│  │  [ Critical — any error is serious       ]                      │   │
│  │                                                                  │   │
│  │  Or describe it in your own words:                              │   │
│  │  ┌──────────────────────────────────────────────────────────┐  │   │
│  │  │                                                          │  │   │
│  │  └──────────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                               ░░[ Confirm & build brief → ]░░   │  ← ⑥
│                                       (confirm all three cards above)   │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 8 — Brief Ready

`① ④ ⑥`

The warmth note is the most specific in the entire flow — it names the exact thing Jordan added (*"the Monday send"*) and tells them what it changed (*"shaped the oversight design"*). This is the difference between acknowledgment and genuine confirmation that input was heard and used.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Agent Brief                          Save & come back later  ×       │
├──────────────────────────────────────────────────────────────────────────┤
│  Brief complete  ✓                                                       │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Your brief is ready.  ✓                                                 │  ← ①
│                                                                            │
│  ✦ You added one detail we didn't have — the Monday send after           │  ← ④
│    Friday review. That's already shaped the oversight design.            │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Your brief                                                      │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  Automating the weekly client status report workflow —           │   │
│  │  currently manual, time-consuming, and inconsistent. Reports    │   │
│  │  are drafted Fridays and reviewed before sending to clients     │   │
│  │  Monday morning.                                                 │   │
│  │                                                                  │   │
│  │  Type of work       Client services and operations              │   │
│  │  Who sees output    Clients and external contacts               │   │
│  │  Quality bar        High — accuracy and brand tone matter       │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  What happens next                                               │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  We'll work through what success looks like and what could      │   │
│  │  go wrong. Most people finish in under 5 minutes.               │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Edit anything                         [ Continue to outcomes → ]      │  ← ①⑥
│                                                                            │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## What Changed From the Baseline

| Screen | Baseline | Upgraded |
| :-- | :-- | :-- |
| Header | "Task Designer" | "Agent Brief" + permanent save link |
| Progress | Step 1 of 8 | Named understanding tracker |
| Screen 1 | Opens cold | Opens with brief framing and purpose |
| After any selection | Nothing | Warmth note contextualised to that selection |
| Screens 2–3 | Open questions | Assertion cards with confidence + reason |
| Screens 4–5 | Select cards | Select cards + `⚑` markers on high-signal answers |
| Screen 6 | Chips in prose | Numbered assertion cards, each independently confirming |
| Screen 6–7 | No confidence signal | `▓▓▓░░░` confidence bar on every inference |
| Low-confidence inferences | No distinction | `⚠` flag + explicit invitation to check carefully |
| Screen 8 | Generic completion | Specific warmth note naming Jordan's actual contribution |

