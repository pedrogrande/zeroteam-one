<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Now provide ASCII wireframes for the key screens in this user flow.

The only change I want to make to your designs is the text area input fields must always be visible alongside the provided options. The user should not need to click a button unnecessarily and the field in this situation gives the user more feeling of autonomy and agency. This also means we don't need the Something Else buttons.

Here are all 10 screens in sequence, representing the complete Stage 1 user flow.

## Wireframe Conventions

- `╔═╗ ╚═╝ ║` — selected card or persistent strip
- `┌─┐ └─┘ │` — unselected card, textarea, or panel
- `◉` — current step, `●` — completed, `○` — upcoming
- `░░[ Button ]░░` — inactive/disabled button
- `[ Button ]` — active button
- Textareas are always open and labelled — no trigger needed

***

## Screen 1 — Category (initial)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ◉ ── ○ ── ○ ── ○ ── ○ ── ○ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
│  What Who  When Pain Risk Draft Confirm Done                             │
├──────────────────────────────────────────────────────────────────────────┤
│  ╔═ Your task description ════════════════════════════════════════════╗  │
│  ║  Make your first selection below to get started                   ║  │
│  ╚════════════════════════════════════════════════════════════════════╝  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  What kind of work do you want AI to help with?                          │
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
│  │  schedules, and        │   │  synthesising           │                │
│  │  handoffs              │   │  information            │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📝  Content           │   │  ⚙   Process &          │                │
│  │      Creation          │   │      Operations         │                │
│  │                        │   │                         │                │
│  │  Writing materials     │   │  Recurring workflows    │                │
│  │  for internal or       │   │  and operational        │                │
│  │  external audiences    │   │  tasks                  │                │
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

## Screen 1b — Category (Reporting selected)

The builder strip updates immediately on selection. Continue activates. Unselected cards visually recede.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ◉ ── ○ ── ○ ── ○ ── ○ ── ○ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│  ╔═ Your task description ════════════════════════════════════════════╗  │
│  ║  Reporting & summaries...                                          ║  │
│  ╚════════════════════════════════════════════════════════════════════╝  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  What kind of work do you want AI to help with?                          │
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
│  │  📋  Coordination &    │   │  🔍  Research &         │                │
│  │      Planning ...      │   │      Analysis ...       │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  📝  Content ...       │   │  ⚙   Process &  ...     │                │
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

## Screen 2 — Audience (Clients selected)

Builder strip grows. Each new screen appends to the description in progress.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ◉ ── ○ ── ○ ── ○ ── ○ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│  ╔═ Your task description ════════════════════════════════════════════╗  │
│  ║  Reporting & summaries...                                          ║  │
│  ╚════════════════════════════════════════════════════════════════════╝  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Who receives the output from this work?                                 │
│                                                                            │
│  ╔════════════════════════╗   ┌────────────────────────┐                │
│  ║  👤  My clients or  ✓  ║   │  👥  My team            │                │
│  ║      customers         ║   │      internally         │                │
│  ║                        ║   │                         │                │
│  ║  The output is         ║   │  For internal use       │                │
│  ║  delivered to people   ║   │  only — no external     │                │
│  ║  outside the business  ║   │  parties                │                │
│  ╚════════════════════════╝   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  🏢  Leadership or     │   │  🌐  Multiple           │                │
│  │      Management        │   │      audiences          │                │
│  │                        │   │                         │                │
│  │  Reported upward       │   │  Both internal and      │                │
│  │  within the            │   │  external recipients    │                │
│  │  organisation          │   │                         │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  Or describe the audience in your own words:                             │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                              [ Continue → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 3 — Frequency (Weekly selected)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ◉ ── ○ ── ○ ── ○ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│  ╔═ Your task description ════════════════════════════════════════════╗  │
│  ║  Reporting & summaries for clients...                              ║  │
│  ╚════════════════════════════════════════════════════════════════════╝  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  How often does this task happen?                                        │
│                                                                            │
│  ┌────────────────────────┐   ╔════════════════════════╗                │
│  │  📅  Daily             │   ║  📆  Weekly          ✓  ║                │
│  │                        │   ║                         ║                │
│  │  Every working day     │   ║  Once a week on a       ║                │
│  │                        │   ║  regular schedule       ║                │
│  └────────────────────────┘   ╚════════════════════════╝                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  🗓  Monthly           │   │  🔁  It varies          │                │
│  │                        │   │                         │                │
│  │  Once a month or on    │   │  Timing depends on      │                │
│  │  a monthly cycle       │   │  events or demand       │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐                                              │
│  │  1  One-time project   │                                              │
│  │                        │                                              │
│  │  A single task,        │                                              │
│  │  not recurring         │                                              │
│  └────────────────────────┘                                              │
│                                                                            │
│  Or describe the frequency in your own words:                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                              [ Continue → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 4 — Pain Points (3 selected, textarea visible)

Multi-select — cards toggle on and off. Builder strip grows with each selection.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ● ── ◉ ── ○ ── ○ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│  ╔═ Your task description ════════════════════════════════════════════╗  │
│  ║  A weekly reporting task for clients...                            ║  │
│  ╚════════════════════════════════════════════════════════════════════╝  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  What makes doing this manually difficult?  Select all that apply.      │
│                                                                            │
│  ╔════════════════════════╗   ╔════════════════════════╗                │
│  ║  ⏱  It takes too    ✓  ║   ║  🔄  Results are     ✓  ║                │
│  ║     long               ║   ║      inconsistent       ║                │
│  ║                        ║   ║                         ║                │
│  ║  A meaningful amount   ║   ║  Output quality varies  ║                │
│  ║  of time each cycle    ║   ║  depending on who       ║                │
│  ║                        ║   ║  does it                ║                │
│  ╚════════════════════════╝   ╚════════════════════════╝                │
│                                                                            │
│  ╔════════════════════════╗   ┌────────────────────────┐                │
│  ║  🗄  Multiple       ✓  ║   │  😓  Repetitive work    │                │
│  ║     sources            ║   │                         │                │
│  ║                        ║   │  The same steps each    │                │
│  ║  Pulling data from     ║   │  time with little or    │                │
│  ║  several tools or      ║   │  no variation           │                │
│  ║  places                ║   │                         │                │
│  ╚════════════════════════╝   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐                                              │
│  │  👤  Depends on one    │                                              │
│  │      person            │                                              │
│  │                        │                                              │
│  │  Only one person knows │                                              │
│  │  how to do this well   │                                              │
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

## Screen 5 — Concerns (2 selected)

Builder strip now carries meaningful content. Jordan is near the end of the intake phase.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ● ── ● ── ◉ ── ○ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│  ╔═ Your task description ════════════════════════════════════════════╗  │
│  ║  A weekly reporting task for clients, currently slow, inconsistent ║  │
│  ║  and drawing from multiple sources...                              ║  │
│  ╚════════════════════════════════════════════════════════════════════╝  │
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
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  👁  Not knowing what  │   │  🔒  Data privacy or    │                │
│  │     it's doing         │   │      security           │                │
│  │                        │   │                         │                │
│  │  No visibility into    │   │  Sensitive information  │                │
│  │  AI actions or         │   │  processed externally   │                │
│  │  decisions             │   │                         │                │
│  └────────────────────────┘   └────────────────────────┘                │
│                                                                            │
│  ┌────────────────────────┐   ┌────────────────────────┐                │
│  │  💬  How clients       │   │  ✓  Not particularly   │                │
│  │      might react       │   │     concerned           │                │
│  │                        │   │                         │                │
│  │  Clients noticing or   │   │                         │                │
│  │  reacting to AI work   │   │                         │                │
│  └────────────────────────┘   └────────────────────────┘                │
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

## Screen 6 — Refined Description (chip view)

The agent's synthesis is broken into tappable chips. Each is editable in place. The description reads as flowing prose punctuated by highlighted segments.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ● ── ● ── ● ── ◉ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Here's how we understood your task.                                     │
│  Tap any underlined phrase to refine it.                                 │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │  ╔═══════════════════════════════════════════════╗              │   │
│  │  ║  Automate the weekly client status report     ║  ← tap      │   │
│  │  ║  workflow                                     ║              │   │
│  │  ╚═══════════════════════════════════════════════╝              │   │
│  │  — currently a manual process where                             │   │
│  │  ╔═══════════════════════════════════════════════╗              │   │
│  │  ║  a team member spends approximately half a    ║  ← tap      │   │
│  │  ║  day each Friday                              ║              │   │
│  │  ╚═══════════════════════════════════════════════╝              │   │
│  │                                                                  │   │
│  │  ╔══════════════════════════════════════════════╗               │   │
│  │  ║  aggregating updates from multiple tools     ║  ← tap       │   │
│  │  ╚══════════════════════════════════════════════╝               │   │
│  │  and sources and drafting a written summary for                 │   │
│  │  each client. The goal is to                                    │   │
│  │  ╔═════════════════════════╗  and                               │   │
│  │  ║  reduce time taken      ║  ← tap                            │   │
│  │  ╚═════════════════════════╝                                    │   │
│  │  ╔════════════════════════════╗  while ensuring outputs are    │   │
│  │  ║  improve consistency       ║  ← tap                        │   │
│  │  ╚════════════════════════════╝                                 │   │
│  │  ╔═══════════════════════════════════════════════╗              │   │
│  │  ║  accurate, on-brand, and fit for direct       ║  ← tap      │   │
│  │  ║  client delivery                              ║              │   │
│  │  ╚═══════════════════════════════════════════════╝              │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                     [ This looks right → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 6b — Chip Edit Open

Jordan taps the second chip. Alternatives appear inline. The textarea is already visible — Jordan types directly without any additional click.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ● ── ● ── ● ── ◉ ── ○ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Here's how we understood your task.                                     │
│  Tap any underlined phrase to refine it.                                 │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                                                                  │   │
│  │  ╔═══════════════════════════════════════════════╗              │   │
│  │  ║  Automate the weekly client status report     ║              │   │
│  │  ║  workflow                                     ║              │   │
│  │  ╚═══════════════════════════════════════════════╝              │   │
│  │  — currently a manual process where                             │   │
│  │                                                                  │   │
│  │  ┌──────────────────────────────────────────────────────────┐  │   │
│  │  │  "a team member spends approximately half a day          │  │   │
│  │  │   each Friday"                                           │  │   │
│  │  │  ────────────────────────────────────────────────────    │  │   │
│  │  │  [ Half a day on Fridays                      ]         │  │   │
│  │  │  [ Most of Friday afternoon                   ]         │  │   │
│  │  │  [ Several hours each week                    ]         │  │   │
│  │  │  [ Me personally, on Friday afternoons        ]         │  │   │
│  │  │                                                          │  │   │
│  │  │  Or describe it in your own words:                       │  │   │
│  │  │  ┌────────────────────────────────────────────────────┐ │  │   │
│  │  │  │ half a day on Fridays — though reports are sent   │ │  │   │
│  │  │  │ Monday morning after I review them                │ │  │   │
│  │  │  └────────────────────────────────────────────────────┘ │  │   │
│  │  │                                                          │  │   │
│  │  │                       [ Use this ✓ ]   [ Cancel ]       │  │   │
│  │  └──────────────────────────────────────────────────────────┘  │   │
│  │                                                                  │   │
│  │  ╔══════════════════════════════════════════════╗               │   │
│  │  ║  aggregating updates from multiple tools     ║  ← tap       │   │
│  │  ╚══════════════════════════════════════════════╝               │   │
│  │  [remaining chips below...]                                     │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                     [ This looks right → ]      │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 7 — Inferred Field Confirmation

The first card is already confirmed (double border, ✓). Two cards remain open. Continue stays inactive until all three are actioned.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ● ── ● ── ● ── ● ── ◉ ── ○                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  We've made a few inferences. Confirm or adjust each one.               │
│                                                                            │
│  ╔══════════════════════════════════════════════════════════════════╗   │
│  ║  What type of work is this?                               ✓      ║   │
│  ║  ──────────────────────────────────────────────────────────────  ║   │
│  ║  Client services and operations                                  ║   │
│  ╚══════════════════════════════════════════════════════════════════╝   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Who sees the final output?                                      │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  Clients and external contacts — this output leaves the business │   │
│  │                                                                  │   │
│  │  [ ✓ That's right ]  [ Internal only ]  [ Mixed — both ]        │   │
│  │                                                                  │   │
│  │  Or describe it in your own words:                               │   │
│  │  ┌──────────────────────────────────────────────────────────┐   │   │
│  │  │                                                          │   │   │
│  │  └──────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  How much does getting this right matter?                        │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  High — errors would affect client relationships                 │   │
│  │                                                                  │   │
│  │  [ ✓ That's right ]  [ Low — easy to fix ]  [ Medium ]          │   │
│  │  [ Critical — any error is serious       ]                       │   │
│  │                                                                  │   │
│  │  Or describe it in your own words:                               │   │
│  │  ┌──────────────────────────────────────────────────────────┐   │   │
│  │  │                                                          │   │   │
│  │  └──────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Back                                 ░░[ Continue to questions → ]░░  │
│                                         (confirm all three cards above)  │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Screen 8 — Stage 1 Complete

A document, not a dialog. Designed to be readable, shareable, and satisfying. The ◀ Edit anything link allows full return without data loss.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◈ Task Designer                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ● ── ● ── ● ── ● ── ● ── ● ── ● ── ◉                                    │
│  1    2    3    4    5    6    7    8                                     │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  We've got what we need to start.  ✓                                     │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Your task                                                       │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  Automating the weekly client status report workflow —           │   │
│  │  currently manual, time-consuming, and inconsistent. Reports    │   │
│  │  are drafted on Fridays and reviewed before sending to clients  │   │
│  │  Monday morning.                                                 │   │
│  │                                                                  │   │
│  │  Type of work       Client services and operations              │   │
│  │  Who sees output    Clients and external contacts               │   │
│  │  Quality bar        High — accuracy and brand tone matter       │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  What's next                                                     │   │
│  │  ──────────────────────────────────────────────────────────────  │   │
│  │  We'll ask a few questions about what success looks like and     │   │
│  │  what could go wrong. Most people finish in under 5 minutes.    │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  ◀ Edit anything                         [ Start the questions → ]       │
│                                                                            │
└──────────────────────────────────────────────────────────────────────────┘
```


***

## Design Notes Across All Screens

| Decision | Rationale |
| :-- | :-- |
| Builder strip persists across all 8 screens | Reassures Jordan their input is being assembled into something real, not just recorded |
| Double-border `╔═╗` consistently means selected or confirmed | One visual language for "this is locked in" — no ambiguity |
| Textarea always open, never triggered | Respects autonomy; removes a click barrier; signals that Jordan's words are always welcome |
| `░░[ Continue ]░░` with note when inactive | Makes the blocking condition visible without an error message |
| Chip alternatives are buttons, textarea is open beneath them | Jordan can pick fast or be precise — the interface supports both without choosing |
| Screen 8 is a document, not a confirmation dialog | Shifts the emotional register from "form complete" to "this is real and ready" |

