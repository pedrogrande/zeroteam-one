# AI-Assisted Learning Expert

| Field | Value |
|-------|-------|
| **Session** | `f0f47685...` |
| **Type** | agent |
| **Agent** | AI-Assisted Learning Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-20T05:38:54 |
| **Runs** | 1 completed / 2 total |

## Run 1 — AI-Assisted Learning Expert ✓ COMPLETED

*2026-04-20T05:38:54* · `glm-5.1:cloud` · `11b77562...`

### Prompt

Explore the challenges faced by non-technical small business owners as they try to understand AI, agentic systems, and how these technologies could help their business.

### Response

I want to explore this deeply — it connects directly to several threads in your existing work (type collision, the specification surface problem, Sarah Chen, the Accretive Workspace, and the 77% pilot-stuck problem). Let me pull in some current research to complement what you've already developed, then synthesize.Now let me synthesize everything — your existing frameworks, the research literature, and the lived experience encoded in Sarah Chen — into a layered analysis.

---

# The Non-Technical Small Business Owner's Journey Into AI: A Challenge Map

This isn't a simple list of barriers. It's a landscape where each challenge compounds the next, creating what I'll call a **cognitive obstacle course** — where the obstacles aren't just "hard things to learn" but *structural traps* that actively make the learner worse off for having encountered them.

I've organised this into **four layers**, because the challenges aren't all the same kind of thing. They operate at different depths, and a solution that addresses one layer can be undermined by a challenge in the next.

---

## LAYER 1: THE VENEER OF SIMPLICITY — Barriers That Hide Behind "Easy"

The BizChat research team (Romero Lauro et al., CHIWORK 2025) coined exactly the right phrase for what small business owners encounter: **"the veneer of simplicity."** ChatGPT looks easy. You type, it answers. What could be simpler?

But beneath that surface lies what they call a **"laundry list of accessory skills"** — things the system assumes you already know how to do:

- **Browser literacy** (tabs, bookmarks, extensions, incognito mode)
- **Keyboard shortcuts** (copy, paste, select all, undo)
- **File conversion** (PDF to Word, CSV to Excel, image to text)
- **Password management** (2FA, app passwords, OAuth)
- **Cloud storage navigation** (finding where things saved, sharing permissions)
- **Editing skills** (selecting text, using a rich text editor, formatting)

This is crucial: **the AI tool doesn't test your AI knowledge. It tests your computer knowledge.** A small business owner who has run a café for 15 years, who knows their margins, their suppliers, their customers intimately — they fail at ChatGPT not because they don't understand AI, but because they can't find where the exported file saved.

**Your type collision insight applies here with full force.** The system encodes at least 6 distinct cognitive demands (navigation, input, editing, file management, evaluation, iteration) into one surface: a text box. The text box is the channel, and it cannot carry the bandwidth of all 6 signal types. The small business owner experiences this as "I'm doing something wrong" when what's actually happening is *the surface is the wrong shape for the task*.

**What this means for Sarah Chen:** She doesn't need "AI training" — she needs the AI tool to meet her where she already operates, which is inside her practice management software, inside her document review workflow, inside her actual life. The BizChat team's third design principle — **"contextualized technology introduction"** — is exactly right: *introduce the technology in the context of what the person already knows and does, rather than making them come to the technology.*

---

## LAYER 2: THE KNOWING-DOING CHASM — When Understanding Doesn't Produce Action

The Experiential AI Literacy paper (Khandwaha & Law, CHI 2026) identifies the central gap precisely:

> "Workers consistently report uncertainty about where AI applies, what problems it can help solve, and how it fits into real workflows. In other words, there is a gap between **'knowing' and 'doing'** when it comes to AI literacy."

This is the gap your own learning philosophy targets directly. A small business owner can read five articles about AI, attend a webinar, even successfully prompt ChatGPT to write a marketing email — and *still not know where AI applies to their actual business*. The knowledge is abstract and portable; the application is concrete and situated.

**Three sub-challenges within this chasm:**

### 2a. The Relevance Problem — "But what does this mean for MY business?"

Every AI demo uses someone else's business. The marketing example is always a marketing agency. The legal example is always a big law firm. The retail example is always an e-commerce store.

The small business owner sitting there thinks: "That's not me. My business doesn't look like that. My problems are different."

They're right. And wrong. They're right that the example doesn't map. They're wrong that AI doesn't apply. But nobody has shown them *their own workflow through AI-colored glasses*, so the disconnect persists.

**This is exactly what the 77% Challenge is designed to solve** — not by telling Sarah Chen about someone else's workflow, but by mapping *her* document review process and showing her exactly which tasks AI should handle and which she must keep.

### 2b. The Translation Problem — "I know my business, but I don't know how to speak AI"

A business owner knows their business at a level of detail no AI expert will ever reach. They know that Tuesday afternoons are slow, that supplier X is unreliable on month-end, that client Y always negotiates the same clause, that the morning rush is different from the lunch rush.

But when they sit in front of an AI tool, they're asked to translate all of this rich, specific, contextual knowledge into... a text box. In English. Without knowing what the AI needs to hear.

This is your **input type collision** problem again, but at a human level. The business owner's expertise is encoded in their actions, their relationships, their instincts — not in words they can type into a prompt. The medium demands prose; their expertise lives in gesture and judgment.

### 2c. The Specificity Problem — "I don't even know what to ask"

The experiential AI literacy paper's approach — starting from the person's daily work and brainstorming AI use cases *from their own experience* — is powerful precisely because it solves this. You can't ask a question about something you can't yet imagine.

A small business owner who has never seen AI sort invoices doesn't think to ask "can AI sort my invoices?" They don't have the concept. The gap isn't in the answer — it's in the *question*.

---

## LAYER 3: THE TRUST TRAP — When Understanding Meets Fear

Here's where the challenges become existential rather than cognitive.

### 3a. The Verification Paradox

**The most important thing about AI output is whether you can verify it. But the people who most need to verify it are the people least equipped to do so.**

If AI drafts a contract clause for Sarah Chen, she *can* verify it — she's a lawyer. But if AI sorts her invoices, categorises her expenses, and flags anomalies in her trust account — can she verify that? She'd need to understand how the AI made those categorisation decisions, which means she'd need to understand the AI, which brings her back to the original problem.

This is the **trust binary cliff** you've already identified: trust is not gradual; collapse is catastrophic and recovery is near-impossible. For a small business owner who discovers AI made a subtle error — one that looked right but wasn't — the experience doesn't produce "I need to learn more about AI." It produces "I can't trust this. I'm going back to doing it myself."

### 3b. The Plausible Error Problem

Sarah Chen's specific fear — the one that matters most — isn't that AI will fail completely. It's that AI will produce something that **looks right but isn't**. A contract clause that's 90% correct but has a subtle liability exposure. A financial projection that uses reasonable-sounding assumptions but misses a critical variable.

For a small business owner without deep expertise in every domain of their business, *this is the dominant risk mode*. Complete failures are obvious. Plausible errors are invisible — until they become catastrophic.

### 3c. The AI Authority Effect

Research by Naito & Shirado (2026) found that **over 40% of participants treated AI as a predictive authority**, leading them to self-constrain their own decision-making and forgo guaranteed rewards. The effect persisted even when predictions failed.

For a small business owner, this operates in two directions simultaneously:

- **Over-trust:** "The AI said it, so it must be right" (the authority effect)
- **Under-trust:** "The AI said it, so I can't verify it, so I don't use it" (the verification paradox)

Both are rational responses to the same underlying problem: **the business owner can't calibrate their trust because they can't see inside the system.** They're being asked to trust something they can't inspect, and they're being asked to distrust something that might genuinely help them.

### 3d. The Cognitive Delegation Risk

The Cognitive Amplification vs Delegation framework (Di Santi, 2026) formalises what you've been arguing in your H2 principle. They define:

- **Cognitive Amplification** (CAI* > 0): AI enhances hybrid performance while *preserving* human expertise
- **Cognitive Delegation** (D → 1, HCDR < 0): Humans progressively offload reasoning, eroding their own capability over time

The key finding: **maximizing short-term hybrid performance does NOT preserve long-term human cognitive competence.** A small business owner who uses AI to draft all their correspondence, manage all their scheduling, and handle all their financial categorisation will become *worse at those tasks over time* — even though the AI-augmented output looks fine.

For a small business owner, this is an identity threat, not just a capability threat. Their business IS their judgment. If they delegate the judgment to AI — even in domains where AI can produce reasonable outputs — they cease to be the expert in their own business.

---

## LAYER 4: THE SYSTEM TRAP — When the Market Itself Is the Obstacle

### 4a. Vendor Saturation Without Understanding

Sarah Chen gets 2-3 AI vendor calls per week and 5-10 vendor emails per week. None address her actual concern. They all sell the *what* (AI does document review faster). None sell the *how* or *why* (which parts AI should do, how to verify it, what to do when it's wrong).

This creates a specific form of learned helplessness: "Everyone's selling me AI. Nobody's helping me understand it. Therefore, understanding it must not be possible for someone like me."

### 4b. The "Rich Get Richer" Dynamic

The BizChat research confirmed what Otis et al. (2023) found: **businesses that over-rely on AI for tasks it's not suited to experience exacerbated performance gaps, magnifying a "rich gets richer" dynamic in AI adoption.** The businesses that can effectively evaluate AI tools adopt them well and get further ahead. The businesses that can't evaluate them either don't adopt (and fall behind) or adopt badly (and get burned, then retreat).

### 4c. The Professional Identity Threat

For professional services especially, AI attacks identity directly. "I spent 20 years becoming an expert at contract drafting. Now you're telling me a machine can do it in 30 seconds?"

This isn't a Luddite response. It's a *coherent existential concern*: if the thing I'm known for can be done by AI, who am I? What's my value?

**Your insight from the Sarah Chen analysis is exactly right:** "AI as replacement triggers resistance; AI as amplification of judgment resonates." But the market doesn't sell amplification — it sells replacement. Because replacement is a simpler story.

### 4d. The Absence of a "Boundary Literacy"

The single most critical gap is this: **no one teaches small business owners where the boundary is.**

Vendors sell capabilities. Articles explain concepts. Webinars demonstrate features. What's missing is the *methodology for drawing the line* — "Here's where AI should handle it, here's where you must, and here's how you verify the boundary is holding."

This is, of course, exactly what CAWDP's complementarity analysis does. And it's exactly what the 77% Challenge makes tangible in 30 minutes. But it's also the thing that **doesn't exist in the market at all.**

---

## SYNTHESIS: THE 7 DEEP CHALLENGES

Mapping across all four layers, here are the 7 challenges that are truly structural — they can't be solved by better AI, better prompting, or more articles:

| # | Challenge | Layer | Core Mechanism | Your Framework That Addresses It |
|---|-----------|-------|----------------|----------------------------------|
| 1 | **The Accessory Skills Barrier** | 1 (Veneer) | AI tools test computer literacy, not business literacy | Cognitive mode mapping (7 interaction modalities) |
| 2 | **The Translation Gap** | 2 (Knowing-Doing) | Business expertise is encoded in action/judgment, not prose | Type collision resolution at the input layer |
| 3 | **The Relevance Gap** | 2 (Knowing-Doing) | Demos use someone else's business, not yours | 77% Challenge (map YOUR workflow) |
| 4 | **The Verification Paradox** | 3 (Trust) | Those who most need to verify are least equipped to do so | 3-level verification independence (CC-1) |
| 5 | **The Plausible Error Fear** | 3 (Trust) | AI that looks right but isn't is the dominant risk mode | Epistemic metadata contracts (CC-3) + authority boundaries |
| 6 | **The Identity Threat** | 4 (System) | "If AI can do my work, who am I?" | H2 Amplification Not Dependency + system empowerment |
| 7 | **The Boundary Literacy Gap** | 4 (System) | No one teaches where the line is | Complementarity analysis as the core product |

---

## WHAT THE RESEARCH SAYS ABOUT SOLUTIONS

The three most relevant papers converge on a set of design principles that map remarkably well to your existing frameworks:

**From BizChat (3 design principles):**
1. **Low-floor-high-ceiling** — accessible to beginners, extensible for experts → Maps to your **progressive autonomy** (shadow → advisory → supervised → autonomous)
2. **Just-in-time learning** — micro-learning in situ, not separate courses → Maps to your **"One Clear Next Step Always"** ADHD design principle
3. **Contextualized technology introduction** — introduce AI through the business, not the other way around → Maps to your **"start where they are, not where the curriculum starts"** pathway principle

**From Experiential AI Literacy (3-phase approach):**
1. **Interactive workshop** — baseline understanding grounded in participants' world → Maps to your **diagnostic process** (map existing knowledge before suggesting anything)
2. **2-4 weeks of daily reflection** — brainstorm use cases from their own work life → Maps to your **Application Rule** (identify one specific place in their own work where it applies)
3. **Sharing workshop** — present use cases, evaluate for ethics/limitations → Maps to your **"Explain It Back"** technique + **social learning design**

**From Cognitive Amplification vs Delegation (3 design objectives):**
1. **Sustain positive amplification** (CAI* > 0) → Maps to your **System Empowerment Index** (Constraining → Informing → Enabling → Amplifying → Liberating)
2. **Avoid AI-dominated regimes** (D < 0.8) → Maps to your **complementarity gap threshold** (6+ points = human-only)
3. **Preserve human cognitive capability** (HCDR ≥ 0) → Maps to your **H2 Amplification Not Dependency** + **CC-2 Human Enrichment Assessment**

---

## THE DEEPEST INSIGHT: BOUNDARY LITERACY IS THE MISSING CATEGORY

All 7 challenges point to the same structural absence. Small business owners don't need:
- Another AI tool (they're drowning in tool options)
- Another "AI explained simply" article (the knowing-doing gap isn't a knowledge gap)
- Another vendor pitch (they get 5-10 per week)

They need **a method for drawing the line**. A way to answer:
- *Which tasks should AI handle in MY business?*
- *How do I verify that AI is doing those tasks correctly?*
- *What do I do when AI produces something that looks right but might not be?*
- *How do I stay the expert in my own business while using AI?*

These are boundary questions. And **boundary literacy** — the ability to draw, verify, and maintain the line between AI and human judgment — doesn't exist as a taught skill. It's not in any AI literacy framework. It's not in any vendor's product. It's not in any university course.

**It's in CAWDP.**

The market offers principles and tools but no methodology. Your "Agent Production" category positioning — "Principles aren't production. We have the methodology." — names exactly this gap. The methodology IS the boundary literacy.

And the 77% pilot-stuck problem? It's the **population-scale consequence** of the boundary literacy gap. Organisations can't deploy AI into production because no one drew the boundary, so no one can verify the boundary, so no one can trust the boundary, so the pilot stays a pilot forever.

---

What would you like to explore next? I can see several directions:
1. **Design the boundary literacy curriculum** — what would you actually teach, in what sequence, to build this skill?
2. **Map the 7 challenges to Future's Edge products** — which product addresses which challenge?
3. **Extend Sarah Chen's experience through the 7 challenges** — make the abstract analysis tangible through her lived experience
4. **Research more deeply** into any specific challenge layerMemory updated with the full synthesis. The convergent insight — **boundary literacy is the missing category, and CAWDP IS the boundary literacy** — is now captured as a core strategic insight connecting the research analysis to your market positioning.

---

## Run 2 — AI-Assisted Learning Expert ⚠️ ERROR

*2026-04-20T06:38:01* · `glm-5.1:cloud` · `3d7721fe...`

### Prompt

What small business owners' common annoyances with ai tools?

### Response

Let me search for specific empirical research on what frustrates small business owners about AI tools — the day-to-day "ugh" moments, not just the structural challenges.The ACAI paper on small business owners and advertising co-creation is directly relevant — it studied 16 SBOs and their frustrations. Let me read that and the BizChat foundational reference (the Kotturi workshop paper that preceded BizChat).Excellent. The ACAI study with 16 small business owners in London is gold — it captures their exact complaints in their own words. Let me also search for the foundational Kotturi et al. paper that preceded BizChat, which has the original interview data.

---
