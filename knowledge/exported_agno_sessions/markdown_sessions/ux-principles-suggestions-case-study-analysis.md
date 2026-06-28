<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Design Principles Driving Stage 1

Before the screens, four principles derived from the empathy mapping govern every decision:

- **Show, then confirm** — the system makes inferences and presents them for Jordan to accept or correct, rather than asking Jordan to produce them from scratch
- **Build, don't fill** — Jordan assembles their task description by making choices, not by composing text
- **Progress feels like understanding** — each screen should feel like the system is getting to know the task, not like a form is being completed
- **Escape hatches, not primary inputs** — a free-text field appears only when Jordan's situation isn't captured by the available options, and it appears contextually, not in advance

***

## Screen 1 — The Opening

**What Jordan sees:**

A single, centered question on a clean screen with no navigation, no sidebar, no secondary actions:

> *"What kind of work do you want AI to help with?"*

Below it, six large option cards arranged in a 2×3 grid. Each card has a short label and a one-line description:


| Card | Label | Description |
| :-- | :-- | :-- |
| 📊 | Reporting \& Summaries | Pulling together updates, data, or notes into a regular output |
| ✉️ | Client Communication | Drafting or preparing messages, responses, or updates for clients |
| 📋 | Coordination \& Planning | Managing tasks, schedules, or handoffs across people or tools |
| 🔍 | Research \& Analysis | Gathering, processing, or synthesising information |
| 📝 | Content Creation | Writing, editing, or producing materials for internal or external use |
| ✦ | Something else | I'll describe it in my own words |

**What happens:**

Jordan taps **Reporting \& Summaries**. The card highlights. A brief description builds in a persistent strip at the top of the screen:

> *"Reporting or summarising work..."*

This strip — the **task description builder** — remains visible for the rest of Stage 1, growing with each answer Jordan gives. It shows Jordan that their choices are being assembled into something, not just recorded.

**If Jordan taps "Something else":** A single-line text input slides into view inline, replacing the grid. Placeholder text reads: *"Describe it briefly — a sentence is enough."* This is the only free-text input on this screen, and it appears only for this case.

***

## Screen 2 — Who Is It For?

**What Jordan sees:**

The category tag is now locked in the builder strip. Below a new question:

> *"Who receives the output from this work?"*

Five option cards:


| Card | Label |
| :-- | :-- |
| 👤 | My clients or customers |
| 👥 | My team internally |
| 🏢 | Leadership or management |
| 🌐 | Multiple different audiences |
| 💭 | Not sure yet |

**What happens:**

Jordan selects **My clients or customers**. The builder strip updates:

> *"Reporting or summarising work... for clients or customers..."*

***

## Screen 3 — How Often?

> *"How often does this task happen?"*


| Card | Label |
| :-- | :-- |
| 📅 | Daily |
| 📆 | Weekly |
| 🗓️ | Monthly |
| 🔁 | It varies |
| 1️⃣ | It's a one-time project |

Jordan selects **Weekly**. Builder strip:

> *"A weekly task... reporting or summarising work for clients or customers..."*

***

## Screen 4 — What Makes It Hard?

> *"What makes doing this manually difficult or time-consuming?"*

Multi-select. Cards stay selected when tapped; tapping again deselects:


| Card | Label |
| :-- | :-- |
| ⏱️ | It takes too long |
| 🔄 | Results are inconsistent depending on who does it |
| 🗄️ | It requires pulling information from multiple places |
| 😓 | It's repetitive work that doesn't need judgment |
| 👤 | It depends too much on one person |
| ✦ | Something else |

Jordan selects: **It takes too long**, **Results are inconsistent**, **It requires pulling from multiple places**.

Tapping **Something else** reveals an inline free-text field beneath the card grid: *"What else makes this hard?"*

Builder strip:

> *"A weekly task... reporting or summarising work for clients... currently taking too long and producing inconsistent results from multiple sources..."*

***

## Screen 5 — What Would Concern You?

> *"If AI handled this, what would concern you most?"*

Multi-select:


| Card | Label |
| :-- | :-- |
| ❌ | Errors or inaccuracies in the output |
| 🎨 | It not sounding like us |
| 👁️ | Not knowing what it's doing or why |
| 🔒 | Data privacy or security |
| 💬 | How clients or stakeholders would react |
| ✅ | I'm not particularly concerned |
| ✦ | Something else |

Jordan selects: **Errors or inaccuracies** and **It not sounding like us**.

Builder strip:

> *"A weekly reporting task for clients... currently slow and inconsistent... with care needed around accuracy and brand tone."*

At this point the system has enough signal to invoke the Session Agent. A brief transition state: the builder strip animates gently — not a spinner, but a subtle pulse on the assembled text — for 2–3 seconds while the agent processes.

***

## Screen 6 — The Refined Description

This is the highest-stakes moment in Stage 1. Jordan sees the agent's synthesis for the first time.

**What Jordan sees:**

A heading:

> *"Here's how we understood your task:"*

Below it, the refined description is presented not as a block of text in a textarea, but as a set of **labelled sentence segments** — each one a distinct claim the agent has made, presented as a tappable chip:

```
[Automate the weekly client status report workflow] — currently a manual
process where [a team member spends approximately half a day each Friday]
[aggregating updates from multiple tools and sources] and [drafting a
written summary for each client]. The goal is to [reduce the time this
takes] and [improve consistency across reports], while ensuring outputs
are [accurate, on-brand, and appropriate for direct client delivery].
```

Each bracketed segment is a distinct chip with a subtle underline. Tapping any chip reveals a small panel:

> *"Does this capture it accurately?"*
> **[Yes]** **[Change this →]**

Tapping **Change this** on any chip reveals 2–4 alternative phrasings as option buttons, plus a final option: **"Describe it differently"** — which opens an inline single-line text field for that segment only.

**What Jordan actually does:**

Jordan reads it. Most of it is right. Jordan taps the chip **[a team member spends approximately half a day each Friday]** and sees:

- *"Half a day on Fridays"*
- *"Most of Friday afternoon"*
- *"Several hours each week"*
- *"Describe it differently →"*

Jordan taps **"Describe it differently"** and types:

> *"half a day on Fridays — though the reports are actually sent Monday morning after I review them"*

The chip updates inline. The rest of the description remains unchanged.

A **"This looks right"** button becomes available only after Jordan has seen the full description — enforced by a subtle scroll gate if the description is long enough to require scrolling.

***

## Screen 7 — Confirming the Inferred Fields

**What Jordan sees:**

Three confirmation cards, stacked vertically. Each presents one inferred field as a plain-language statement with a confirmation action:

***

**Card 1**
*"What type of work is this?"*
> Client services and operations
**[That's right]** **[Change this →]**

Tapping **Change this** reveals:

- Marketing and content
- Internal business operations
- Finance and administration
- Customer support
- Professional services
- *"Describe it differently →"* (inline text field)

***

**Card 2**
*"Who sees the final output?"*
> Clients and external contacts — this output leaves the business
**[That's right]** **[Change this →]**

Tapping **Change this** reveals:

- Internal team only
- Leadership or management
- Mixed — internal and external
- *"Describe it differently →"*

***

**Card 3**
*"How much does getting this right matter?"*
> High — errors or quality issues would affect client relationships
**[That's right]** **[Change this →]**

Tapping **Change this** reveals:

- Low — easy to correct if something goes wrong
- Medium — errors are noticeable but recoverable
- High — errors would be costly or embarrassing
- Critical — errors would have serious consequences
- *"Describe it differently →"*

***

Jordan confirms all three without changes. A **"Continue to questions →"** action becomes available after all three cards are actioned.

***

## Screen 8 — Stage 1 Complete

A brief, satisfying close to the stage before the transition to Stage 2. Not a confirmation dialog — a moment of genuine summary.

**What Jordan sees:**

> *"We've got what we need to start."*

A clean, read-only summary card:

> **Your task:**
> Automating the weekly client status report workflow — currently manual, time-consuming, and inconsistent. Reports are drafted Fridays and reviewed before sending to clients Monday morning.
>
> **Type of work:** Client services and operations
> **Who sees the output:** Clients and external contacts
> **Quality requirement:** High — accuracy and brand tone matter

Below this, a forward-looking statement that sets expectations for Stage 2:

> *"Next, we'll ask you a few questions to understand exactly what success looks like and what could go wrong. Most people complete this in under 5 minutes."*

A single action: **"Start the questions →"**

***

## How the No-Textarea Rule Is Applied

| Screen | Primary input | Textarea appears? | Condition |
| :-- | :-- | :-- | :-- |
| 1 — Category | Option cards | Yes — inline | Only if "Something else" selected |
| 2 — Audience | Option cards | No | — |
| 3 — Frequency | Option cards | No | — |
| 4 — Pain points | Multi-select cards | Yes — inline | Only if "Something else" selected |
| 5 — Concerns | Multi-select cards | Yes — inline | Only if "Something else" selected |
| 6 — Refined description | Tappable chips + alternatives | Yes — inline per chip | Only if "Describe it differently" selected for that chip |
| 7 — Inferred fields | Confirm cards + alternatives | Yes — inline per card | Only if "Describe it differently" selected |
| 8 — Summary | Read-only | No | — |

At no point does Jordan face an empty text input as the primary method of response. Every free-text field is subordinate to an option set — it appears only when Jordan's situation is not captured by any of the available choices, and it appears exactly where it is needed rather than at the top of the screen as the default.

